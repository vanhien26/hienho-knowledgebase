#!/usr/bin/env python3
"""
SCENARIO MODELING & STRATEGIC DECISION ENGINE
Mô hình hóa kịch bản kinh doanh và định lượng tác động quyết định (What-If Analysis).

4 Kịch bản mô phỏng cốt lõi:
1. Reallocation (Tái phân bổ nguồn lực giữa các Hub)
2. Paid-to-Organic Shift (Cắt giảm ngân sách Paid Ads, tái đầu tư vào Non-Paid SEO Evergreen)
3. Quick Wins CTR Uplift (Định lượng lợi ích khi tối ưu Title/Meta cho từ khóa Pos 4-15)
4. Funnel UX & CVR Lift (Định lượng tác động khi tối ưu tỷ lệ chuyển đổi Web-to-App)
"""

import sys
import argparse
import json
from pathlib import Path
from tabulate import tabulate

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import get_connection


def format_table(headers, rows):
    return tabulate(rows, headers=headers, tablefmt="github")


def simulate_reallocation(source_hub="cinema", target_hub="financial", sessions_shifted=50000):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT hub_id, hub_name, total_sessions, w2a_clicks, w2a_cvr_pct
        FROM v_hub_performance
        WHERE hub_id IN (?, ?);
    """, (source_hub, target_hub))
    data = {r["hub_id"]: dict(r) for r in cur.fetchall()}
    conn.close()

    src = data.get(source_hub, {"hub_name": source_hub, "w2a_cvr_pct": 2.34})
    tgt = data.get(target_hub, {"hub_name": target_hub, "w2a_cvr_pct": 3.36})

    src_cvr = src["w2a_cvr_pct"] / 100.0
    tgt_cvr = tgt["w2a_cvr_pct"] / 100.0

    lost_w2a = int(sessions_shifted * src_cvr)
    gained_w2a = int(sessions_shifted * tgt_cvr)
    net_w2a = gained_w2a - lost_w2a

    print("\n--- KỊCH BẢN 1: TÁI PHÂN BỔ NGUỒN LỰC GIỮA CÁC HUBS ---")
    rows = [
        ["Hub giảm tải (Source)", f"{src['hub_name']} (CVR: {src['w2a_cvr_pct']:.2f}%)"],
        ["Hub gia tăng (Target)", f"{tgt['hub_name']} (CVR: {tgt['w2a_cvr_pct']:.2f}%)"],
        ["Quy mô dịch chuyển", f"{sessions_shifted:,} Sessions"],
        ["Chuyển đổi mất đi tại nguồn", f"-{lost_w2a:,} W2A Clicks"],
        ["Chuyển đổi gia tăng tại đích", f"+{gained_w2a:,} W2A Clicks"],
        ["Tăng trưởng chuyển đổi ròng (Net Lift)", f"{net_w2a:+,} W2A Clicks (CVR Delta: +{(tgt_cvr - src_cvr)*100:.2f}%)"],
        ["Ước tính New User App tăng ròng", f"+{int(net_w2a * 0.40):,} Người dùng mới (giả định 40% W2A Click to Install)"]
    ]
    print(format_table(["Chỉ số mô phỏng", "Kết quả định lượng"], rows))


def simulate_paid_to_organic_shift(cut_pct=30.0, monthly_paid_pv=327570):
    """Mô phỏng cắt giảm Paid Ads và dồn lực vào Non-Paid SEO Evergreen."""
    cut_pv = int(monthly_paid_pv * (cut_pct / 100.0))
    # Giả định chi phí trung bình 1,200đ / Paid PV
    cost_saved = cut_pv * 1200
    # Với chi phí tiết kiệm được, đầu tư sản xuất N bài chuẩn SEO/GEO (chi phí 300,000đ/bài chất lượng cao)
    content_pieces = int(cost_saved / 300000)
    # Trung bình 1 bài Evergreen mang lại 800 PV/tháng ổn định sau 3 tháng
    organic_pv_month3 = content_pieces * 800

    print("\n--- KỊCH BẢN 2: DỊCH CHUYỂN NGÂN SÁCH PAID ADS SANG NON-PAID SEO EVERGREEN ---")
    rows = [
        ["Tỷ lệ cắt giảm Paid Ads", f"{cut_pct:.1f}% (-{cut_pv:,} Paid PV/tháng)"],
        ["Ngân sách tiết kiệm dự kiến", f"{cost_saved:,.0f} VNĐ / tháng"],
        ["Năng lực sản xuất Content tương đương", f"{content_pieces:,} bài viết chuẩn Topic Cluster / GEO"],
        ["Traffic Organic bù đắp (Tháng 1)", f"+{int(organic_pv_month3 * 0.20):,} PV (Giai đoạn đang index)"],
        ["Traffic Organic bù đắp (Tháng 3)", f"+{organic_pv_month3:,} PV / tháng (Tích lũy bền vững)"],
        ["Lợi ích dài hạn", f"Sau tháng thứ 3, lượng Traffic tạo ra mỗi tháng vượt {organic_pv_month3 - cut_pv:+,.0f} PV so với cắt Paid, chi phí duy trì gần như bằng 0."]
    ]
    print(format_table(["Chỉ số kịch bản", "Kết quả dự báo"], rows))


def simulate_quick_wins_uplift(target_ctr=1.5):
    """Mô phỏng tối ưu CTR Title/Meta cho nhóm từ khóa Quick Wins."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT query, page_url, impressions, clicks, ctr_pct, avg_position
        FROM v_keyword_quick_wins
        WHERE impressions >= 50000
        LIMIT 10;
    """)
    rows = cur.fetchall()
    conn.close()

    total_imp = sum(r["impressions"] for r in rows)
    current_clicks = sum(r["clicks"] for r in rows)
    projected_clicks = int(total_imp * (target_ctr / 100.0))
    net_click_gain = projected_clicks - current_clicks
    # Giả định CVR trung bình vào App là 3.0%
    net_w2a_gain = int(net_click_gain * 0.03)

    print(f"\n--- KỊCH BẢN 3: TỐI ƯU CTR CHO TOP 10 TỪ KHÓA QUICK WINS (MỤC TIÊU CTR: {target_ctr}%) ---")
    table_rows = [
        ["Tổng Impressions 10 cụm từ khóa", f"{total_imp:,} lượt hiển thị / tháng"],
        ["Clicks hiện tại (CTR thực tế)", f"{current_clicks:,} clicks (CTR trung bình: {current_clicks/total_imp*100:.2f}%)"],
        ["Clicks kỳ vọng khi tối ưu Title/Meta", f"{projected_clicks:,} clicks"],
        ["Clicks tự nhiên tăng thêm (Net Gain)", f"+{net_click_gain:,} Organic Clicks / tháng"],
        ["Chuyển đổi Web-to-App tăng thêm", f"+{net_w2a_gain:,} OneLink Clicks / tháng (CVR 3.0%)"],
        ["Chi phí triển khai", "0 VNĐ (Chỉ cần Content Team & SEO Vendor tối ưu lại thẻ Title/Meta)"]
    ]
    print(format_table(["Chỉ số đo lường", "Tác động định lượng"], table_rows))


def simulate_funnel_cvr_lift(hub_id="cinema", target_cvr=3.20):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT hub_name, total_sessions, w2a_clicks, w2a_cvr_pct
        FROM v_hub_performance
        WHERE hub_id = ?;
    """, (hub_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        print(f"[ERROR] Không tìm thấy dữ liệu Hub: {hub_id}")
        return

    sessions = row["total_sessions"]
    curr_w2a = row["w2a_clicks"]
    curr_cvr = row["w2a_cvr_pct"]

    new_w2a = int(sessions * (target_cvr / 100.0))
    net_w2a_lift = new_w2a - curr_w2a

    print(f"\n--- KỊCH BẢN 4: NÂNG CẤP TỶ LỆ CHUYỂN ĐỔI (W2A CVR) TẠI {row['hub_name'].upper()} ---")
    table_rows = [
        ["Lưu lượng Sessions của Hub", f"{sessions:,} Sessions"],
        ["Tỷ lệ CVR hiện tại", f"{curr_cvr:.2f}% ({curr_w2a:,} OneLink Clicks)"],
        ["Tỷ lệ CVR mục tiêu sau tối ưu UX", f"{target_cvr:.2f}%"],
        ["OneLink Clicks mới đạt được", f"{new_w2a:,} Clicks"],
        ["Chuyển đổi gia tăng ròng (Net W2A Lift)", f"+{net_w2a_lift:,} OneLink Clicks / kỳ"],
        ["Giải pháp kỹ thuật yêu cầu", "Web Dev bổ sung Sticky Bottom App Bar, OneLink Banner cá nhân hóa trên Mobile Web."]
    ]
    print(format_table(["Chỉ số phễu", "Kết quả định lượng"], table_rows))


def main():
    parser = argparse.ArgumentParser(description="Scenario Modeling & What-If Engine")
    parser.add_argument("--scenario", type=str, choices=["all", "reallocate", "paid_shift", "quick_wins", "cvr_lift"], default="all", help="Kịch bản mô phỏng cần chạy")
    parser.add_argument("--from-hub", type=str, default="cinema", help="Hub nguồn (mặc định: cinema)")
    parser.add_argument("--to-hub", type=str, default="financial", help="Hub đích (mặc định: financial)")
    parser.add_argument("--shift", type=int, default=50000, help="Số sessions dịch chuyển")
    args = parser.parse_args()

    print("=" * 80)
    print("MÔ HÌNH HÓA KỊCH BẢN CHIẾN LƯỢC & ĐỊNH LƯỢNG QUYẾT ĐỊNH (SCENARIO SIMULATOR)")
    print("=" * 80)

    if args.scenario in ["all", "reallocate"]:
        simulate_reallocation(args.from_hub, args.to_hub, args.shift)
    if args.scenario in ["all", "paid_shift"]:
        simulate_paid_to_organic_shift(cut_pct=30.0)
    if args.scenario in ["all", "quick_wins"]:
        simulate_quick_wins_uplift(target_ctr=1.5)
    if args.scenario in ["all", "cvr_lift"]:
        simulate_funnel_cvr_lift(hub_id="cinema", target_cvr=3.20)

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
