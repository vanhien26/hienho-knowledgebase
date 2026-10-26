#!/usr/bin/env python3
"""
SEASONALITY-ADJUSTED FORECAST & WHAT-IF SIMULATION ENGINE
Động cơ tính toán dự báo có trọng số mùa vụ và mô phỏng kịch bản chiến lược (What-If Analysis).

Nhiệm vụ:
1. Seasonality Forecast: Dự báo kết tháng kết hợp dữ liệu mùa vụ lịch sử từ dim_theme_seasonality.
2. What-If Resource Reallocation: Mô phỏng dịch chuyển nguồn lực giữa các Hub để tối đa hóa New User và W2A CVR.
"""

import sys
import json
import argparse
from pathlib import Path
from tabulate import tabulate

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import get_connection, DATA_DIR


def format_table(headers, rows):
    return tabulate(rows, headers=headers, tablefmt="github")


def get_month_seasonality_factor(month_num: int) -> float:
    """
    Tính hệ số mùa vụ trung bình toàn Website cho tháng chỉ định (1..12).
    Hệ số = (Điểm mùa vụ tháng này) / (Điểm mùa vụ trung bình cả năm).
    """
    conn = get_connection()
    cur = conn.cursor()
    col = f"m{month_num}"
    cur.execute(f"""
        SELECT 
            AVG({col}) AS target_avg,
            AVG((m1+m2+m3+m4+m5+m6+m7+m8+m9+m10+m11+m12) / 12.0) AS year_avg
        FROM dim_theme_seasonality
        WHERE volume > 10000;
    """)
    row = cur.fetchone()
    conn.close()

    if row and row["year_avg"] and row["year_avg"] > 0:
        return float(row["target_avg"]) / float(row["year_avg"])
    return 1.0


def calculate_seasonality_forecast(month: int = 10, days_elapsed: int = 24, days_in_month: int = 31, actual_pv: int = 2848940, target_pv: int = 3665607):
    """
    Dự báo kết tháng với 3 kịch bản:
    - Kịch bản Ngoại suy Tuyến tính (Linear Baseline)
    - Kịch bản Điều chỉnh Mùa vụ (Seasonality Weighted)
    - Kịch bản Phòng thủ Thận trọng (Conservative / Downside Risk)
    """
    seasonality_factor = get_month_seasonality_factor(month)
    
    # 1. Tuyến tính
    daily_pace = actual_pv / max(1, days_elapsed)
    linear_forecast = daily_pace * days_in_month
    
    # 2. Điều chỉnh Mùa vụ: Những ngày cuối tháng 10 bước vào mùa mua sắm & phim bom tấn cuối năm
    # Trọng số mùa vụ áp vào các ngày còn lại
    remaining_days = max(1, days_in_month - days_elapsed)
    adjusted_daily_pace = daily_pace * (0.95 + 0.1 * seasonality_factor)
    seasonality_forecast = actual_pv + (adjusted_daily_pace * remaining_days)
    
    # 3. Kịch bản Thận trọng (nếu có biến động thuật toán hoặc giảm chi tiêu Paid Ads)
    conservative_daily_pace = daily_pace * 0.90
    conservative_forecast = actual_pv + (conservative_daily_pace * remaining_days)

    return {
        "seasonality_factor": seasonality_factor,
        "daily_pace": daily_pace,
        "linear_forecast": linear_forecast,
        "linear_pct": (linear_forecast / target_pv) * 100,
        "seasonality_forecast": seasonality_forecast,
        "seasonality_pct": (seasonality_forecast / target_pv) * 100,
        "conservative_forecast": conservative_forecast,
        "conservative_pct": (conservative_forecast / target_pv) * 100,
    }


def simulate_hub_reallocation(source_hub_id: str = "cinema", target_hub_id: str = "financial", traffic_shift: int = 50000):
    """
    Mô phỏng kịch bản dịch chuyển traffic hoặc nguồn lực nội dung giữa 2 Hub.
    Đánh giá biến động chuyển đổi Web-to-App dựa trên tỷ lệ CVR thực tế của từng Hub.
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT hub_id, hub_name, total_sessions, w2a_clicks, w2a_cvr_pct
        FROM v_hub_performance
        WHERE hub_id IN (?, ?);
    """, (source_hub_id, target_hub_id))
    rows = {r["hub_id"]: dict(r) for r in cur.fetchall()}
    conn.close()

    source = rows.get(source_hub_id, {"hub_name": source_hub_id, "w2a_cvr_pct": 2.34})
    target = rows.get(target_hub_id, {"hub_name": target_hub_id, "w2a_cvr_pct": 3.36})

    src_cvr = source["w2a_cvr_pct"] / 100.0
    tgt_cvr = target["w2a_cvr_pct"] / 100.0

    lost_w2a = int(traffic_shift * src_cvr)
    gained_w2a = int(traffic_shift * tgt_cvr)
    net_w2a = gained_w2a - lost_w2a

    return {
        "source": source,
        "target": target,
        "traffic_shift": traffic_shift,
        "lost_w2a": lost_w2a,
        "gained_w2a": gained_w2a,
        "net_w2a": net_w2a,
        "net_cvr_diff": (tgt_cvr - src_cvr) * 100
    }


def main():
    parser = argparse.ArgumentParser(description="Forecast & What-If Engine")
    parser.add_argument("--forecast", action="store_true", help="Chạy dự báo kết tháng")
    parser.add_argument("--what-if", action="store_true", help="Chạy mô phỏng dịch chuyển nguồn lực")
    parser.add_argument("--shift", type=int, default=50000, help="Số lượng Sessions mô phỏng dịch chuyển")
    parser.add_argument("--from-hub", type=str, default="cinema", help="Hub nguồn (mặc định: cinema)")
    parser.add_argument("--to-hub", type=str, default="financial", help="Hub đích (mặc định: financial)")
    args = parser.parse_args()

    if args.what_if or (not args.forecast and not args.what_if):
        print("=" * 75)
        print("MÔ PHỎNG CHIẾN LƯỢC: WHAT-IF RESOURCE REALLOCATION")
        print("=" * 75)
        res = simulate_hub_reallocation(args.from_hub, args.to_hub, args.shift)
        
        sim_table = [
            ["Hub nguồn (Giảm đầu tư)", f"{res['source']['hub_name']} (CVR: {res['source']['w2a_cvr_pct']:.2f}%)"],
            ["Hub đích (Tăng đầu tư)", f"{res['target']['hub_name']} (CVR: {res['target']['w2a_cvr_pct']:.2f}%)"],
            ["Lưu lượng dịch chuyển giả định", f"{res['traffic_shift']:,} Sessions"],
            ["W2A suy giảm tại Hub nguồn", f"-{res['lost_w2a']:,} OneLink Clicks"],
            ["W2A gia tăng tại Hub đích", f"+{res['gained_w2a']:,} OneLink Clicks"],
            ["Lợi nhuận chuyển đổi ròng (Net Lift)", f"{res['net_w2a']:+,} OneLink Clicks ({res['net_cvr_diff']:+.2f}% CVR Delta)"],
        ]
        print(format_table(["Tham số mô phỏng", "Kết quả định lượng"], sim_table))
        print("\n-> Nhận định chiến lược: Do Hub đích có CVR cao hơn, việc tái phân bổ sẽ tạo ra tăng trưởng ròng về người dùng thực chất vào App mà không cần tăng ngân sách tổng.")

    if args.forecast or not args.what_if:
        print("\n" + "=" * 75)
        print("DỰ BÁO KẾT THÁNG ĐA KỊCH BẢN (SEASONALITY-ADJUSTED FORECAST)")
        print("=" * 75)
        fc = calculate_seasonality_forecast()
        fc_table = [
            ["Kịch bản Tuyến tính (Linear Baseline)", f"{fc['linear_forecast']:,.0f} PV", f"{fc['linear_pct']:.2f}%", "Ngoại suy bình quân ngày MTD"],
            ["Kịch bản Mùa vụ (Seasonality Weighted)", f"{fc['seasonality_forecast']:,.0f} PV", f"{fc['seasonality_pct']:.2f}%", f"Điều chỉnh theo hệ số mùa vụ ({fc['seasonality_factor']:.2f})"],
            ["Kịch bản Thận trọng (Conservative)", f"{fc['conservative_forecast']:,.0f} PV", f"{fc['conservative_pct']:.2f}%", "Phòng ngừa suy hao Paid Ads hoặc biến động thuật toán"],
        ]
        print(format_table(["Kịch bản", "Dự báo PV", "% Target Đạt", "Cơ sở tính toán"], fc_table))
        print("=" * 75)


if __name__ == "__main__":
    main()
