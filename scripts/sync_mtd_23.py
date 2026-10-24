#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC GA4 MTD 23 DATA ACROSS WEB PLATFORM SSOT & WEB HUBS (/dashboard)
Đồng bộ toàn diện luồng số liệu MTD 23 ngày (01/10 -> 23/10/2026):
1. Snapshot JSON:
   - 07_REPORTS/data/monthly_10_2026_mtd_23d.json
   - 07_REPORTS/data/monthly_10_2026_consolidated.json
2. Summary JSON:
   - 07_REPORTS/data/summary.json
   - react-web-momo/lib/dashboard/summary.json
   - react-web-momo/data/analytics/summary.json
3. Hubs Dashboard Data:
   - react-web-momo/lib/dashboard/web-data.json (chính là file cấp dữ liệu cho /dashboard)
4. Excel SSOTs:
   - 07_REPORTS/web_platform_performance.xlsx
   - 07_REPORTS/web_performance_tracking.xlsx
"""

import os
import sys
import json
import zipfile
import re
import xml.etree.ElementTree as ET
from datetime import datetime

BASE_DIR = "/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base"
HUBS_REPO = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"

SNAPSHOT_23D = os.path.join(BASE_DIR, "07_REPORTS/data/monthly_10_2026_mtd_23d.json")
CONSOLIDATED_JSON = os.path.join(BASE_DIR, "07_REPORTS/data/monthly_10_2026_consolidated.json")
SUMMARY_JSON = os.path.join(BASE_DIR, "07_REPORTS/data/summary.json")
HUBS_SUMMARY_JSON = os.path.join(HUBS_REPO, "lib/dashboard/summary.json")
HUBS_ANALYTICS_SUMMARY = os.path.join(HUBS_REPO, "data/analytics/summary.json")
HUBS_WEB_DATA = os.path.join(HUBS_REPO, "lib/dashboard/web-data.json")

EXCEL_FILES = [
    os.path.join(BASE_DIR, "07_REPORTS/web_platform_performance.xlsx"),
    os.path.join(BASE_DIR, "07_REPORTS/web_performance_tracking.xlsx")
]

# Dữ liệu GA4 MTD 23 Ngày (2026-10-01 -> 2026-10-23)
TOTAL_PV = 2735276
TARGET_OCT = 3665607
DAYS_ELAPSED = 23
DAYS_IN_MONTH = 31

ORGANIC_PV = 1366847
DIRECT_PV = 709997
PAID_PV = 306109
REFERRAL_PV = 114546
OTHERS_PV = 237777 # Unassigned (168,532) + Social (46,487) + AI Assistant (12,070) + Cross/Video/Email (10,688)
NON_PAID_PV = ORGANIC_PV + DIRECT_PV + REFERRAL_PV + OTHERS_PV # 2,429,167

TOTAL_USERS = 1353431
TOTAL_SESSIONS = 1838201

# Hubs breakdown MTD 23d
HUB_CINEMA = 889399
HUB_FINANCIAL = 163850
HUB_NEW_USER = 92150
HUB_VEHICLE = 29740
HUB_STUDENT = 1892
HUB_OTHERS = TOTAL_PV - (HUB_CINEMA + HUB_FINANCIAL + HUB_NEW_USER + HUB_VEHICLE + HUB_STUDENT) # 1,558,245

# Cinema sub-pages
CINEMA_RAP = 545468
CINEMA_PHIM = 297746
CINEMA_HOME = 26978
CINEMA_BLOG = 15002
CINEMA_LANDING = 2598
CINEMA_NEWS = 1607

NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace("", NS_MAIN)

def update_cell(root, coord, formula=None, val=None):
    c = root.find(f".//{{{NS_MAIN}}}c[@r=\"{coord}\"]")
    if c is None:
        m = re.match(r"([A-Z]+)(\d+)", coord)
        if not m:
            return
        col_str, row_str = m.groups()
        row_el = root.find(f".//{{{NS_MAIN}}}row[@r=\"{row_str}\"]")
        if row_el is None:
            sheet_data = root.find(f".//{{{NS_MAIN}}}sheetData")
            row_el = ET.SubElement(sheet_data, f"{{{NS_MAIN}}}row", {"r": row_str})
        c = ET.SubElement(row_el, f"{{{NS_MAIN}}}c", {"r": coord})
    
    # Formula
    f_el = c.find(f"{{{NS_MAIN}}}f")
    if formula is not None:
        if formula == "":
            if f_el is not None:
                c.remove(f_el)
        else:
            if f_el is None:
                f_el = ET.Element(f"{{{NS_MAIN}}}f")
                c.insert(0, f_el)
            f_el.text = formula
            f_el.attrib.pop("t", None)
            f_el.attrib.pop("ref", None)
            
    # Value
    v_el = c.find(f"{{{NS_MAIN}}}v")
    if val is not None:
        if v_el is None:
            v_el = ET.SubElement(c, f"{{{NS_MAIN}}}v")
        v_el.text = str(val)
        val_str = str(val)
        if not val_str.replace("-", "").replace(".", "").isdigit():
            c.attrib["t"] = "str"
        elif "t" in c.attrib:
            del c.attrib["t"]

def patch_excel(file_path):
    if not os.path.exists(file_path):
        print(f"Bỏ qua file không tồn tại: {file_path}")
        return
    temp_path = file_path + ".tmp"
    with zipfile.ZipFile(file_path, "r") as z_in, zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as z_out:
        for item in z_in.infolist():
            content = z_in.read(item.filename)
            
            # Sheet 3: Overall Performance
            if item.filename == "xl/worksheets/sheet3.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val=f"Update to: {DAYS_ELAPSED}")
                update_cell(root, "K5", formula="SUM(K9:K13)", val=str(TOTAL_PV))
                update_cell(root, "K6", formula="K5-J5", val=str(TOTAL_PV - 3764435))
                update_cell(root, "K7", formula="IFERROR((K5/J5)-1, 0)", val=str(round((TOTAL_PV / 3764435) - 1, 10)))
                update_cell(root, "K9", formula="", val=str(ORGANIC_PV))
                update_cell(root, "K10", formula="", val=str(PAID_PV))
                update_cell(root, "K11", formula="", val=str(DIRECT_PV))
                update_cell(root, "K12", formula="", val=str(REFERRAL_PV))
                update_cell(root, "K13", formula="", val=str(OTHERS_PV))
                update_cell(root, "T5", formula="SUM(T9:T13)", val=str(TOTAL_PV))
                update_cell(root, "T6", formula="T5-S5", val=str(TOTAL_PV - 2654786))
                update_cell(root, "T7", formula="IFERROR((T5/S5)-1, 0)", val=str(round((TOTAL_PV / 2654786) - 1, 10)))
                update_cell(root, "T9", formula="", val=str(ORGANIC_PV))
                update_cell(root, "T10", formula="", val=str(PAID_PV))
                update_cell(root, "T11", formula="", val=str(DIRECT_PV))
                update_cell(root, "T12", formula="", val=str(REFERRAL_PV))
                update_cell(root, "T13", formula="", val=str(OTHERS_PV))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # Sheet 4: PaidNonPaid
            elif item.filename == "xl/worksheets/sheet4.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val=f"Update to: {DAYS_ELAPSED}")
                update_cell(root, "K5", formula="'Overall Performance'!K5", val=str(TOTAL_PV))
                update_cell(root, "K6", formula="K5-J5", val=str(TOTAL_PV - 3764435))
                update_cell(root, "K7", formula="IFERROR((K5/J5)-1, 0)", val=str(round((TOTAL_PV / 3764435) - 1, 10)))
                update_cell(root, "K8", formula="SUM(K9:K12)", val=str(NON_PAID_PV))
                update_cell(root, "K9", formula="", val=str(ORGANIC_PV))
                update_cell(root, "K10", formula="", val=str(DIRECT_PV))
                update_cell(root, "K11", formula="", val=str(REFERRAL_PV))
                update_cell(root, "K12", formula="", val=str(OTHERS_PV))
                update_cell(root, "K13", formula="", val=str(PAID_PV))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # Sheet 5: Target
            elif item.filename == "xl/worksheets/sheet5.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val=f"Update to: {DAYS_ELAPSED}")
                update_cell(root, "K6", formula="'Overall Performance'!K5", val=str(TOTAL_PV))
                update_cell(root, "K7", formula="K6-J6", val=str(TOTAL_PV - 3764435))
                update_cell(root, "K8", formula="IFERROR((K6/J6)-1, 0)", val=str(round((TOTAL_PV / 3764435) - 1, 10)))
                prog_pct = round((TOTAL_PV / TARGET_OCT) * 100)
                update_cell(root, "K9", formula='IFERROR(REPT("█", ROUND(K6/K3*4,0)) & " " & TEXT(K6/K3,"0%"), "")', val=f"███ {prog_pct}%")
                update_cell(root, "K10", formula="", val=str(ORGANIC_PV))
                update_cell(root, "K11", formula="", val=str(PAID_PV))
                update_cell(root, "K12", formula="", val=str(DIRECT_PV))
                update_cell(root, "K13", formula="", val=str(REFERRAL_PV))
                update_cell(root, "K14", formula="", val=str(OTHERS_PV))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # Sheet 8: Cinema
            elif item.filename == "xl/worksheets/sheet8.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val=f"Update to: {DAYS_ELAPSED}")
                update_cell(root, "H3", formula="SUM(H9,H16,H23,H30,H37,H44)", val=str(HUB_CINEMA))
                update_cell(root, "H4", formula="H3-G3", val=str(HUB_CINEMA - 863885))
                update_cell(root, "H5", formula="(H3/G3)-1", val=str(round((HUB_CINEMA / 863885) - 1, 6)))
                update_cell(root, "H9", formula="", val=str(CINEMA_RAP))
                update_cell(root, "H16", formula="", val=str(CINEMA_PHIM))
                update_cell(root, "H23", formula="", val=str(CINEMA_HOME))
                update_cell(root, "H30", formula="", val=str(CINEMA_BLOG))
                update_cell(root, "H37", formula="", val=str(CINEMA_NEWS))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            z_out.writestr(item, content)
            
    os.replace(temp_path, file_path)
    print(f"✓ Đã patch Excel SSOT: {file_path}")

def update_web_data_json():
    if not os.path.exists(HUBS_WEB_DATA):
        print(f"Cảnh báo: Không tìm thấy {HUBS_WEB_DATA}")
        return

    with open(HUBS_WEB_DATA, "r", encoding="utf-8") as f:
        web_data = json.load(f)

    # 1. Cập nhật running object
    web_data["running"] = {
        "month": "2026-10",
        "daysElapsed": DAYS_ELAPSED,
        "daysInMonth": DAYS_IN_MONTH,
        "report": f"monthly_10_2026_mtd_{DAYS_ELAPSED}d.json"
    }
    web_data["generatedAt"] = datetime.now().isoformat()

    # 2. Phân bổ lưu lượng tăng thêm (+110,941 PV) vào tháng 10 (index 9) của các projects
    # Kênh thứ tự: 0=organic, 1=paid, 2=direct, 3=referral, 4=others
    oct_idx = web_data["months"].index("2026-10")

    # Tính tỷ lệ scale từng kênh cho ngày 23
    current_channel_totals = [0, 0, 0, 0, 0]
    for p in web_data["projects"]:
        for i in range(5):
            current_channel_totals[i] += p["full"][oct_idx][i]

    target_channels = [ORGANIC_PV, PAID_PV, DIRECT_PV, REFERRAL_PV, OTHERS_PV]
    scale_factors = [
        target_channels[i] / current_channel_totals[i] if current_channel_totals[i] > 0 else 1.0
        for i in range(5)
    ]

    new_totals = [0, 0, 0, 0, 0]
    for p in web_data["projects"]:
        for i in range(5):
            new_val = round(p["full"][oct_idx][i] * scale_factors[i])
            p["full"][oct_idx][i] = new_val
            p["mtd"][oct_idx][i] = new_val
            new_totals[i] += new_val

    # Điều chỉnh vi mô làm tròn để khớp chính xác 100% từng kênh
    for i in range(5):
        diff = target_channels[i] - new_totals[i]
        if diff != 0:
            # Cộng/trừ vào project lớn nhất của kênh
            max_p = max(web_data["projects"], key=lambda p: p["full"][oct_idx][i])
            max_p["full"][oct_idx][i] += diff
            max_p["mtd"][oct_idx][i] += diff

    with open(HUBS_WEB_DATA, "w", encoding="utf-8") as f:
        json.dump(web_data, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã cập nhật chính thức {HUBS_WEB_DATA} (Running MTD {DAYS_ELAPSED}d, Total: {TOTAL_PV:,} PV)")

def sync_all():
    print("=" * 70)
    print(f"KHỞI CHẠY ĐỒNG BỘ DỮ LIỆU GA4 MTD {DAYS_ELAPSED}D SANG HUBS /dashboard")
    print("=" * 70)

    daily_pace = round(TOTAL_PV / DAYS_ELAPSED, 2)
    forecast_31d = round(daily_pace * DAYS_IN_MONTH, 2)
    forecast_pct = round((forecast_31d / TARGET_OCT) * 100, 2)
    progress_pct = round((TOTAL_PV / TARGET_OCT) * 100, 2)
    daily_needed = round((TARGET_OCT - TOTAL_PV) / max(1, DAYS_IN_MONTH - DAYS_ELAPSED), 2)

    # 1. Snapshot JSON (monthly_10_2026_mtd_23d.json)
    snapshot_data = {
        "file_source": "GA4 Data API (Property 270743103)",
        "read_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "report_type": f"MTD {DAYS_ELAPSED} Ngày (01/10 - {DAYS_ELAPSED}/10/2026 - Lũy Kế {DAYS_ELAPSED} Ngày Tháng 10)",
        "days_elapsed": DAYS_ELAPSED,
        "days_in_month": DAYS_IN_MONTH,
        "target_oct_pv": TARGET_OCT,
        "actual_mtd_pv": TOTAL_PV,
        "progress_pct": progress_pct,
        "daily_pace": daily_pace,
        "daily_needed": daily_needed,
        "forecast_31d": forecast_31d,
        "forecast_pct": forecast_pct,
        "users": TOTAL_USERS,
        "sessions": TOTAL_SESSIONS,
        "channels": {
            "organic": {"pv": ORGANIC_PV, "pct": round(ORGANIC_PV / TOTAL_PV * 100, 2)},
            "direct": {"pv": DIRECT_PV, "pct": round(DIRECT_PV / TOTAL_PV * 100, 2)},
            "paid": {"pv": PAID_PV, "pct": round(PAID_PV / TOTAL_PV * 100, 2)},
            "referral": {"pv": REFERRAL_PV, "pct": round(REFERRAL_PV / TOTAL_PV * 100, 2)},
            "others": {"pv": OTHERS_PV, "pct": round(OTHERS_PV / TOTAL_PV * 100, 2)},
            "non_paid_total": {"pv": NON_PAID_PV, "pct": round(NON_PAID_PV / TOTAL_PV * 100, 2)}
        },
        "hubs": {
            "cinema": {"pv": HUB_CINEMA, "target": 1117378, "pct": round(HUB_CINEMA / 1117378 * 100, 2), "forecast": round(HUB_CINEMA / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "financial": {"pv": HUB_FINANCIAL, "target": 450000, "pct": round(HUB_FINANCIAL / 450000 * 100, 2), "forecast": round(HUB_FINANCIAL / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "new_user": {"pv": HUB_NEW_USER, "target": 300000, "pct": round(HUB_NEW_USER / 300000 * 100, 2), "forecast": round(HUB_NEW_USER / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "vehicle": {"pv": HUB_VEHICLE, "target": 100000, "pct": round(HUB_VEHICLE / 100000 * 100, 2), "forecast": round(HUB_VEHICLE / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "student": {"pv": HUB_STUDENT, "target": 100000, "pct": round(HUB_STUDENT / 100000 * 100, 2), "forecast": round(HUB_STUDENT / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "others": {"pv": HUB_OTHERS, "target": 0, "pct": 0, "forecast": round(HUB_OTHERS / DAYS_ELAPSED * DAYS_IN_MONTH, 2)}
        },
        "cinema_breakdown": {
            "Trang Rạp phim": {"pv": CINEMA_RAP, "pct_hub": round(CINEMA_RAP / HUB_CINEMA * 100, 2)},
            "Trang phim chi tiết": {"pv": CINEMA_PHIM, "pct_hub": round(CINEMA_PHIM / HUB_CINEMA * 100, 2)},
            "Cinema_Home Page": {"pv": CINEMA_HOME, "pct_hub": round(CINEMA_HOME / HUB_CINEMA * 100, 2)},
            "Cinema_Blog": {"pv": CINEMA_BLOG, "pct_hub": round(CINEMA_BLOG / HUB_CINEMA * 100, 2)},
            "Cinema_Landing Page": {"pv": CINEMA_LANDING, "pct_hub": round(CINEMA_LANDING / HUB_CINEMA * 100, 2)},
            "Tin tức": {"pv": CINEMA_NEWS, "pct_hub": round(CINEMA_NEWS / HUB_CINEMA * 100, 2)}
        }
    }

    with open(SNAPSHOT_23D, "w", encoding="utf-8") as f:
        json.dump(snapshot_data, f, indent=2, ensure_ascii=False)
    print(f"✓ Đã lưu snapshot MTD 23d: {SNAPSHOT_23D}")

    with open(CONSOLIDATED_JSON, "w", encoding="utf-8") as f:
        json.dump(snapshot_data, f, indent=2, ensure_ascii=False)
    print(f"✓ Đã lưu consolidated JSON: {CONSOLIDATED_JSON}")

    # 2. Summary JSON cho Hubs & Card Trang Chủ
    summary_data = {
        "lastFull": {
            "month": "2026-09",
            "pv": 3952859,
            "prevPv": 3465363,
            "target": 3509044
        },
        "running": {
            "month": "2026-10",
            "daysElapsed": DAYS_ELAPSED,
            "daysInMonth": DAYS_IN_MONTH,
            "report": f"monthly_10_2026_mtd_{DAYS_ELAPSED}d.json",
            "pv": TOTAL_PV,
            "target": TARGET_OCT,
            "dailyPace": round(daily_pace),
            "dailyNeeded": round(daily_needed),
            "forecast": round(forecast_31d),
            "forecastPct": forecast_pct
        },
        "hubs": [
            {"id": "cinema", "name": "Cinema Hub", "pv": HUB_CINEMA},
            {"id": "financial", "name": "Financial Hub", "pv": HUB_FINANCIAL},
            {"id": "new_user", "name": "New User Hub", "pv": HUB_NEW_USER},
            {"id": "vehicle", "name": "Vehicle Hub", "pv": HUB_VEHICLE},
            {"id": "student", "name": "Student Hub", "pv": HUB_STUDENT}
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
            "organic": ORGANIC_PV,
            "direct": DIRECT_PV,
            "referral": REFERRAL_PV,
            "paid": PAID_PV,
            "others": OTHERS_PV
        }
    }

    with open(SUMMARY_JSON, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)
    print(f"✓ Đã cập nhật KB summary.json: {SUMMARY_JSON}")

    with open(HUBS_SUMMARY_JSON, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)
    print(f"✓ Đã cập nhật Hubs summary.json: {HUBS_SUMMARY_JSON}")

    if os.path.exists(os.path.dirname(HUBS_ANALYTICS_SUMMARY)):
        with open(HUBS_ANALYTICS_SUMMARY, "w", encoding="utf-8") as f:
            json.dump(summary_data, f, indent=2, ensure_ascii=False)
        print(f"✓ Đã cập nhật Hubs analytics summary: {HUBS_ANALYTICS_SUMMARY}")

    # 3. Cập nhật trực tiếp web-data.json
    update_web_data_json()

    # 4. Patch các file Excel SSOT
    for p in EXCEL_FILES:
        patch_excel(p)

    print("=" * 70)
    print(f"HOÀN THÀNH ĐỒNG BỘ DỮ LIỆU MTD {DAYS_ELAPSED}D SANG HUBS /dashboard!")
    print("=" * 70)

if __name__ == "__main__":
    sync_all()
