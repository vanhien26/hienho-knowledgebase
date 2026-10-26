#!/usr/bin/env python3
"""
CLI ANALYTICS QUERY TOOL
Công cụ tra cứu số liệu đa chiều tức thì từ SQLite Data Mart SSOT.
Cho phép truy vấn SQL tự do hoặc chạy các góc nhìn phân tích chuẩn hóa:
- Hiệu suất Hubs & Chuyển đổi W2A
- Top Landing Pages tạo chuyển đổi App
- Từ khóa Quick Wins (Top 4-15, nhiều impression, low CTR)
- Phân tích từ khóa cạnh tranh nội bộ (Cannibalization)
"""

import sys
import argparse
import sqlite3
from pathlib import Path
from tabulate import tabulate

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import (
    get_connection,
    DEFAULT_DB_PATH,
    query_hubs_summary,
    query_top_w2a_drivers,
    query_quick_wins
)


def format_table(headers, rows):
    """Format markdown table without emojis."""
    return tabulate(rows, headers=headers, tablefmt="github")


def show_hubs():
    rows = query_hubs_summary()
    if not rows:
        print("Không có dữ liệu Hubs.")
        return
    table_data = []
    for r in rows:
        table_data.append([
            r["hub_name"],
            f"{r['active_pages']:,}",
            f"{r['total_sessions']:,}",
            f"{r['engagement_rate_pct']:.1f}%",
            f"{r['w2a_clicks']:,}",
            f"{r['w2a_cvr_pct']:.2f}%"
        ])
    headers = ["Hub Name", "Active Pages", "Sessions", "Engagement Rate", "W2A Clicks", "W2A CVR"]
    print("\n--- BÁO CÁO HIỆU SUẤT TỔNG THỂ CÁC HUBS ---")
    print(format_table(headers, table_data))


def show_top_w2a(limit=15):
    rows = query_top_w2a_drivers(limit=limit)
    if not rows:
        print("Không có dữ liệu W2A.")
        return
    table_data = []
    for r in rows:
        lp = r["landing_page"]
        if len(lp) > 45:
            lp = lp[:42] + "..."
        table_data.append([
            lp,
            r["hub_name"],
            r["primary_project"],
            f"{r['sessions']:,}",
            f"{r['total_w2a']:,}",
            f"{r['w2a_cvr_pct']:.2f}%"
        ])
    headers = ["Landing Page", "Hub", "Project", "Sessions", "W2A Clicks", "CVR"]
    print(f"\n--- TOP {limit} TRANG CHUYỂN ĐỔI WEB-TO-APP CAO NHẤT ---")
    print(format_table(headers, table_data))


def show_quick_wins(limit=15, min_imp=1000):
    rows = query_quick_wins(min_impressions=min_imp, limit=limit)
    if not rows:
        print("Không có từ khóa Quick Wins thỏa điều kiện.")
        return
    table_data = []
    for r in rows:
        q = r["query"]
        if len(q) > 30:
            q = q[:27] + "..."
        url = r["page_url"].replace("https://www.momo.vn", "")
        if len(url) > 35:
            url = url[:32] + "..."
        table_data.append([
            q,
            url,
            f"{r['impressions']:,}",
            f"{r['clicks']:,}",
            f"{r['ctr_pct']:.2f}%",
            f"{r['avg_position']:.1f}",
            f"{int(r['potential_gain']):,}"
        ])
    headers = ["Query", "Path", "Impressions", "Clicks", "CTR", "Pos", "Potential Gain"]
    print(f"\n--- TOP {limit} TỪ KHÓA QUICK WINS (POS 4-15, IMP >= {min_imp:,}) ---")
    print(format_table(headers, table_data))


def show_cannibalization(min_pages=2, limit=15):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            query,
            COUNT(DISTINCT page_url) AS page_count,
            SUM(impressions) AS total_imp,
            SUM(clicks) AS total_clicks,
            ROUND(AVG(position), 1) AS avg_pos
        FROM gsc_search_analytics
        GROUP BY query
        HAVING page_count >= ? AND total_imp >= 2000
        ORDER BY page_count DESC, total_imp DESC
        LIMIT ?;
    """, (min_pages, limit))
    rows = cur.fetchall()
    conn.close()

    table_data = []
    for r in rows:
        q = r["query"]
        if len(q) > 35:
            q = q[:32] + "..."
        table_data.append([
            q,
            r["page_count"],
            f"{r['total_imp']:,}",
            f"{r['total_clicks']:,}",
            f"{r['avg_pos']:.1f}"
        ])
    headers = ["Query", "Conflicting URLs", "Total Imp", "Total Clicks", "Avg Pos"]
    print(f"\n--- TOP {limit} TỪ KHÓA CẠNH TRANH NỘI BỘ (CANNIBALIZATION) ---")
    print(format_table(headers, table_data))


def run_custom_sql(sql):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        if not rows:
            print("Query thực thi thành công nhưng không trả về dòng dữ liệu nào.")
            return
        headers = [desc[0] for desc in cur.description]
        formatted_rows = []
        for r in rows[:50]:
            formatted_rows.append([str(v) if v is not None else "NULL" for v in r])
        print(f"\n--- KẾT QUẢ SQL QUERY (Hiển thị tối đa 50 dòng) ---")
        print(format_table(headers, formatted_rows))
        if len(rows) > 50:
            print(f"... và còn {len(rows) - 50} dòng nữa.")
    except Exception as e:
        print(f"[ERROR] Lỗi thực thi SQL: {e}")
    finally:
        conn.close()


def main():
    parser = argparse.ArgumentParser(description="CLI Analytics Query Tool")
    parser.add_argument("--hubs", action="store_true", help="Hiển thị hiệu suất các Hubs")
    parser.add_argument("--w2a", action="store_true", help="Hiển thị Top trang chuyển đổi Web-to-App")
    parser.add_argument("--quick-wins", action="store_true", help="Hiển thị từ khóa Quick Wins")
    parser.add_argument("--cannibalization", action="store_true", help="Hiển thị từ khóa ăn thịt lẫn nhau")
    parser.add_argument("--sql", type=str, help="Chạy câu truy vấn SQL tùy ý")
    parser.add_argument("--limit", type=int, default=15, help="Giới hạn số dòng hiển thị")

    args = parser.parse_args()

    if args.sql:
        run_custom_sql(args.sql)
    elif args.hubs:
        show_hubs()
    elif args.w2a:
        show_top_w2a(limit=args.limit)
    elif args.quick_wins:
        show_quick_wins(limit=args.limit)
    elif args.cannibalization:
        show_cannibalization(limit=args.limit)
    else:
        # Mặc định hiển thị bảng tổng quan Hubs và Top W2A
        show_hubs()
        show_top_w2a(limit=10)


if __name__ == "__main__":
    main()
