#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ALL-IN-ONE GA4 MTD PERFORMANCE SYNC (SINGLE COMMAND EXECUTION)
Đồng bộ trọn gói 1 lệnh duy nhất (One-Click) từ GA4 API sang:
1. Snapshot JSON & Consolidated (07_REPORTS/data/monthly_*.json)
2. Toàn bộ giao diện Hubs /dashboard (web-data.json & summary.json)
3. Bảng Retention Matrix & Funnel (page-retention-matrix.json)
4. Excel SSOT (web_performance_tracking.xlsx)
5. Markdown SSOT (WEB_PERFORMANCE_TRACKING_MASTER.md)
6. Tự động commit & push sang GitHub Hubs (main) qua REST API trong 10-15s.

Cách dùng:
    ./.venv/bin/python scripts/sync_ga4_master.py              # Tự động lấy MTD hôm qua
    ./.venv/bin/python scripts/sync_ga4_master.py --mtd 23     # Chỉ định cụ thể ngày MTD
    ./.venv/bin/python scripts/sync_ga4_master.py --no-push    # Chạy offline, không đẩy GitHub
"""

import os
import sys
import json
import time
import argparse
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")

sys.path.insert(0, str(BASE_DIR))
from scripts.sync_ga4_to_hubs import get_access_token, PROPERTY_ID, run_ga4_report
from scripts.build_full_funnel_matrix import build_theme_matcher
from scripts.sync_mtd_23 import patch_excel

TARGET_OCT = 3665607

def main():
    start_time = time.time()
    
    parser = argparse.ArgumentParser(description="Sync GA4 MTD All-In-One")
    parser.add_argument("--mtd", type=int, default=None, help="Số ngày MTD (mặc định: ngày hôm qua)")
    parser.add_argument("--no-push", action="store_true", help="Không tự động push sang Hubs GitHub")
    args = parser.parse_args()

    # Xác định số ngày MTD
    now = datetime.now()
    if args.mtd:
        days_elapsed = args.mtd
    else:
        yesterday = now - timedelta(days=1)
        days_elapsed = yesterday.day

    days_in_month = 31
    month_str = f"{now.year}-{now.month:02d}"
    start_date = f"{month_str}-01"
    end_date = f"{month_str}-{days_elapsed:02d}"

    print("=" * 75)
    print(f"KHỞI CHẠY PIPELINE GA4 ALL-IN-ONE (CHU KỲ: {start_date} -> {end_date})")
    print("=" * 75)

    # 1. Xác thực Google OAuth
    print("[1/6] Xác thực Google OAuth 2.0...")
    token = get_access_token()
    date_ranges = [{"startDate": start_date, "endDate": end_date}]

    # 2. Kéo chỉ số tổng thể toàn Website (Deduplicated Property Totals)
    print("[2/6] Kéo chỉ số tổng thể toàn Website từ GA4...")
    res_prop = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "sessions"},
            {"name": "totalUsers"},
            {"name": "engagedSessions"},
            {"name": "userEngagementDuration"}
        ]
    })
    row_p = res_prop["rows"][0]
    total_pv = int(row_p["metricValues"][0]["value"])
    total_sessions = int(row_p["metricValues"][1]["value"])
    total_users = int(row_p["metricValues"][2]["value"])
    total_engaged = int(row_p["metricValues"][3]["value"])
    total_duration = float(row_p["metricValues"][4]["value"])

    # 3. Kéo phân bổ kênh lưu lượng & W2A OneLink clicks
    print("[3/6] Kéo phân bổ kênh lưu lượng (Non-Paid vs. Paid)...")
    res_ch = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [
            {"name": "screenPageViews"},
            {"name": "sessions"},
            {"name": "totalUsers"}
        ],
        "limit": 50
    })

    res_w2a = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 50
    })

    w2a_map = {}
    for r in res_w2a.get("rows", []):
        w2a_map[r["dimensionValues"][0]["value"]] = int(r["metricValues"][0]["value"])

    channel_stats = {}
    organic_pv = 0
    direct_pv = 0
    paid_pv = 0
    referral_pv = 0
    others_pv = 0
    non_paid_pv = 0

    for r in res_ch.get("rows", []):
        ch = r["dimensionValues"][0]["value"]
        pv = int(r["metricValues"][0]["value"])
        sess = int(r["metricValues"][1]["value"])
        us = int(r["metricValues"][2]["value"])
        w2a_cl = w2a_map.get(ch, 0)
        channel_stats[ch] = {"pv": pv, "sessions": sess, "users": us, "w2a": w2a_cl}

        cn = ch.lower()
        if "organic search" in cn:
            organic_pv += pv
            non_paid_pv += pv
        elif "direct" in cn:
            direct_pv += pv
            non_paid_pv += pv
        elif "referral" in cn:
            referral_pv += pv
            non_paid_pv += pv
        elif any(k in cn for k in ["paid", "cpc", "display"]):
            paid_pv += pv
        else:
            others_pv += pv
            non_paid_pv += pv

    # 4. Kéo phân bổ Hubs
    print("[4/6] Kéo phân bổ lưu lượng theo Hubs...")
    res_lp = run_ga4_report(token, {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "metrics": [{"name": "screenPageViews"}],
        "limit": 10000
    })

    matcher = build_theme_matcher()
    hubs_pv = {
        "cinema": 0,
        "financial": 0,
        "new_user": 0,
        "vehicle": 0,
        "student": 0,
        "others": 0
    }

    for r in res_lp.get("rows", []):
        lp = r["dimensionValues"][0]["value"]
        pv = int(r["metricValues"][0]["value"])
        t_info = matcher(lp)
        h_name = t_info[4] if t_info else "Khác"
        if h_name == "Cinema":
            hubs_pv["cinema"] += pv
        elif h_name in ["Ví Trả Sau", "Điểm Tín Dụng", "Vay Nhanh", "Tiết Kiệm Online", "Mở Thẻ Tín Dụng", "Trung Tâm Tài Chính", "Chứng Chỉ Quỹ", "Chứng Khoán"]:
            hubs_pv["financial"] += pv
        elif h_name in ["New User"]:
            hubs_pv["new_user"] += pv
        elif h_name in ["Phạt Nguội", "Tiện Ích Giao Thông", "Phí Không Dừng", "Bảo Hiểm Ô Tô", "Bảo Hiểm Xe Máy"]:
            hubs_pv["vehicle"] += pv
        elif h_name in ["Student Hub"]:
            hubs_pv["student"] += pv
        else:
            hubs_pv["others"] += pv

    # Tính Pacing & Forecast
    daily_pace = round(total_pv / days_elapsed, 2)
    daily_needed = round((TARGET_OCT - total_pv) / max(1, days_in_month - days_elapsed), 2)
    forecast_31d = round(daily_pace * days_in_month, 2)
    forecast_pct = round((forecast_31d / TARGET_OCT) * 100, 2)
    progress_pct = round((total_pv / TARGET_OCT) * 100, 2)

    # 5. Cập nhật các đích dữ liệu (SSOT & Hubs)
    print("[5/6] Ghi dữ liệu đồng bộ vào SSOT Knowledge Base & Hubs /dashboard...")
    
    # 5.1 Snapshot JSON
    snapshot_path = BASE_DIR / "07_REPORTS" / "data" / f"monthly_10_2026_mtd_{days_elapsed}d.json"
    consolidated_path = BASE_DIR / "07_REPORTS" / "data" / "monthly_10_2026_consolidated.json"
    snapshot_payload = {
        "file_source": f"GA4 Data API (Property {PROPERTY_ID})",
        "read_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "report_type": f"MTD {days_elapsed} Ngày (01/10 - {days_elapsed}/10/2026)",
        "days_elapsed": days_elapsed,
        "days_in_month": days_in_month,
        "target_oct_pv": TARGET_OCT,
        "actual_mtd_pv": total_pv,
        "progress_pct": progress_pct,
        "daily_pace": daily_pace,
        "daily_needed": daily_needed,
        "forecast_31d": forecast_31d,
        "forecast_pct": forecast_pct,
        "users": total_users,
        "sessions": total_sessions,
        "channels": {
            "organic": {"pv": organic_pv, "pct": round(organic_pv / total_pv * 100, 2)},
            "direct": {"pv": direct_pv, "pct": round(direct_pv / total_pv * 100, 2)},
            "paid": {"pv": paid_pv, "pct": round(paid_pv / total_pv * 100, 2)},
            "referral": {"pv": referral_pv, "pct": round(referral_pv / total_pv * 100, 2)},
            "others": {"pv": others_pv, "pct": round(others_pv / total_pv * 100, 2)},
            "non_paid_total": {"pv": non_paid_pv, "pct": round(non_paid_pv / total_pv * 100, 2)}
        },
        "hubs": {
            "cinema": {"pv": hubs_pv["cinema"], "target": 1117378, "pct": round(hubs_pv["cinema"] / 1117378 * 100, 2)},
            "financial": {"pv": hubs_pv["financial"], "target": 450000, "pct": round(hubs_pv["financial"] / 450000 * 100, 2)},
            "new_user": {"pv": hubs_pv["new_user"], "target": 300000, "pct": round(hubs_pv["new_user"] / 300000 * 100, 2)},
            "vehicle": {"pv": hubs_pv["vehicle"], "target": 100000, "pct": round(hubs_pv["vehicle"] / 100000 * 100, 2)},
            "student": {"pv": hubs_pv["student"], "target": 100000, "pct": round(hubs_pv["student"] / 100000 * 100, 2)}
        }
    }
    with open(snapshot_path, "w", encoding="utf-8") as f:
        json.dump(snapshot_payload, f, ensure_ascii=False, indent=2)
    with open(consolidated_path, "w", encoding="utf-8") as f:
        json.dump(snapshot_payload, f, ensure_ascii=False, indent=2)

    # 5.2 Summary JSON
    summary_payload = {
        "lastFull": {
            "month": "2026-09",
            "pv": 3952859,
            "prevPv": 3465363,
            "target": 3509044
        },
        "running": {
            "month": "2026-10",
            "daysElapsed": days_elapsed,
            "daysInMonth": days_in_month,
            "report": f"monthly_10_2026_mtd_{days_elapsed}d.json",
            "pv": total_pv,
            "target": TARGET_OCT,
            "dailyPace": round(daily_pace),
            "dailyNeeded": round(daily_needed),
            "forecast": round(forecast_31d),
            "forecastPct": forecast_pct
        },
        "hubs": [
            {"id": "cinema", "name": "Cinema Hub", "pv": hubs_pv["cinema"]},
            {"id": "financial", "name": "Financial Hub", "pv": hubs_pv["financial"]},
            {"id": "new_user", "name": "New User Hub", "pv": hubs_pv["new_user"]},
            {"id": "vehicle", "name": "Vehicle Hub", "pv": hubs_pv["vehicle"]},
            {"id": "student", "name": "Student Hub", "pv": hubs_pv["student"]}
        ],
        "lastFullHubs": [
            {"id": "cinema", "name": "Cinema Hub", "pv": 1220075},
            {"id": "payment", "name": "Payment Hub", "pv": 520612},
            {"id": "home", "name": "Home MoMo", "pv": 467476},
            {"id": "new_user", "name": "New User Hub", "pv": 462878},
            {"id": "financial", "name": "Financial Hub", "pv": 249823},
            {"id": "travel", "name": "Travel Hub", "pv": 114475}
        ],
        "channels": {
            "organic": organic_pv,
            "direct": direct_pv,
            "referral": referral_pv,
            "paid": paid_pv,
            "others": others_pv
        }
    }
    with open(BASE_DIR / "07_REPORTS" / "data" / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_payload, f, ensure_ascii=False, indent=2)
    with open(HUBS_REPO / "lib" / "dashboard" / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_payload, f, ensure_ascii=False, indent=2)
    if (HUBS_REPO / "data" / "analytics").exists():
        with open(HUBS_REPO / "data" / "analytics" / "summary.json", "w", encoding="utf-8") as f:
            json.dump(summary_payload, f, ensure_ascii=False, indent=2)

    # 5.3 Web-data.json cho /dashboard
    web_data_path = HUBS_REPO / "lib" / "dashboard" / "web-data.json"
    if web_data_path.exists():
        with open(web_data_path, "r", encoding="utf-8") as f:
            web_data = json.load(f)
        web_data["running"] = {
            "month": "2026-10",
            "daysElapsed": days_elapsed,
            "daysInMonth": days_in_month,
            "report": f"monthly_10_2026_mtd_{days_elapsed}d.json"
        }
        web_data["generatedAt"] = datetime.now().isoformat()
        oct_idx = web_data["months"].index("2026-10")
        
        cur_ch = [0, 0, 0, 0, 0]
        for p in web_data["projects"]:
            for i in range(5):
                cur_ch[i] += p["full"][oct_idx][i]
        tgt_ch = [organic_pv, paid_pv, direct_pv, referral_pv, others_pv]
        scales = [tgt_ch[i] / cur_ch[i] if cur_ch[i] > 0 else 1.0 for i in range(5)]
        
        new_ch = [0, 0, 0, 0, 0]
        for p in web_data["projects"]:
            for i in range(5):
                val = round(p["full"][oct_idx][i] * scales[i])
                p["full"][oct_idx][i] = val
                p["mtd"][oct_idx][i] = val
                new_ch[i] += val
        for i in range(5):
            d_val = tgt_ch[i] - new_ch[i]
            if d_val != 0:
                max_p = max(web_data["projects"], key=lambda p: p["full"][oct_idx][i])
                max_p["full"][oct_idx][i] += d_val
                max_p["mtd"][oct_idx][i] += d_val

        with open(web_data_path, "w", encoding="utf-8") as f:
            json.dump(web_data, f, ensure_ascii=False, indent=2)

    # 5.4 Patch Excel
    for xl_p in [BASE_DIR / "07_REPORTS" / "web_platform_performance.xlsx", BASE_DIR / "07_REPORTS" / "web_performance_tracking.xlsx"]:
        if xl_p.exists():
            patch_excel(str(xl_p))

    # 6. Push GitHub REST API
    if not args.no_push:
        print("[6/6] Tự động đẩy dữ liệu sang GitHub Hubs qua REST API...")
        push_script = BASE_DIR / "scripts" / "push_to_hubs_api.py"
        subprocess.run([
            sys.executable, str(push_script),
            "-m", f"data(ga4): automated all-in-one sync MTD {days_elapsed}d ({total_pv:,} PV)"
        ], check=True)
    else:
        print("[6/6] Chế độ no-push: Bỏ qua đẩy GitHub.")

    elapsed = time.time() - start_time
    print("=" * 75)
    print(f"HOÀN THÀNH TOÀN BỘ PIPELINE TRONG {elapsed:.1f} GIÂY")
    print(f"- Lũy kế MTD: {total_pv:,} PV / Target: {TARGET_OCT:,} ({progress_pct}%)")
    print(f"- Nhịp chạy : {daily_pace:,.0f} PV/ngày | Dự phóng 31d: {forecast_31d:,.0f} ({forecast_pct}%)")
    print(f"- Non-Paid  : {non_paid_pv:,} PV ({non_paid_pv/total_pv*100:.1f}%) | Paid: {paid_pv:,} PV ({paid_pv/total_pv*100:.1f}%)")
    print("=" * 75)

if __name__ == "__main__":
    main()
