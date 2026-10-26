#!/usr/bin/env python3
"""
DECISION AUDIT TRAIL & CLOSED-LOOP TRACKER
Sổ cái theo dõi quyết định chiến lược và tự động đối soát kết quả sau triển khai (Closed-Loop Validation).

Quy trình vận hành:
1. Ghi nhận quyết định (Log Decision): Lưu vết Ngày quyết định, Hub, Mục tiêu (Target KPI), và Chỉ số cơ sở (Baseline).
2. Đối soát tự động (Closed-Loop Audit): Tự động truy vấn số liệu thực tế từ Data Mart sau 14 - 30 ngày.
3. Đánh giá thành bại (Attribution & Post-Mortem): Đo lường độ lệch thực tế vs kỳ vọng, cập nhật trạng thái ACHIEVED / MISSED.
"""

import sys
import argparse
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from tabulate import tabulate

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.lib.db import get_connection, DEFAULT_DB_PATH


def format_table(headers, rows):
    return tabulate(rows, headers=headers, tablefmt="github")


def init_decision_table(conn):
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS decision_audit_trail (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                logged_at TEXT NOT NULL,
                project_hub TEXT NOT NULL,
                decision_name TEXT NOT NULL,
                target_url TEXT NOT NULL,
                metric_name TEXT NOT NULL,
                baseline_val REAL NOT NULL,
                target_val REAL NOT NULL,
                actual_val REAL DEFAULT NULL,
                review_date TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'IN_PROGRESS',
                notes TEXT DEFAULT ''
            );
        """)


def seed_initial_decisions(conn):
    """Nạp mẫu các quyết định gần nhất từ 08_DECISION_LOG vào sổ cái theo dõi."""
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM decision_audit_trail;")
    cnt = cur.fetchone()[0]
    if cnt > 0:
        return

    today = datetime.now()
    seeds = [
        (
            "2026-10-14",
            "New User Hub",
            "Tách biệt luồng tải App /tai-app khỏi trang /download",
            "/tai-app",
            "W2A CVR",
            10.86,
            25.00,
            10.86,
            (today + timedelta(days=14)).strftime("%Y-%m-%d"),
            "IN_PROGRESS",
            "Default Web Fallback cho OneLink Desktop; nâng tỷ lệ quét QR"
        ),
        (
            "2026-10-13",
            "Vehicle Hub",
            "Chuẩn hóa URL Spoke Subpages /tien-ich-giao-thong/garage",
            "/tien-ich-giao-thong/garage",
            "Impressions",
            5000,
            20000,
            7200,
            (today + timedelta(days=7)).strftime("%Y-%m-%d"),
            "IN_PROGRESS",
            "Loại bỏ tiền tố tim-, chuẩn hóa SEO Entity"
        ),
        (
            "2026-10-09",
            "Financial Hub",
            "Chuẩn hóa thuật toán Trợ lý AI Tiết kiệm (Net Yield Gap)",
            "/tiet-kiem-online",
            "W2A CVR",
            5.00,
            18.00,
            16.60,
            "2026-10-23",
            "ACHIEVED",
            "Thay text đếm ngân hàng bằng số tiền chênh lệch cụ thể"
        )
    ]

    with conn:
        conn.executemany("""
            INSERT INTO decision_audit_trail
            (logged_at, project_hub, decision_name, target_url, metric_name, baseline_val, target_val, actual_val, review_date, status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, seeds)


def add_decision(hub: str, name: str, url: str, metric: str, baseline: float, target: float, days_to_review: int = 14, notes: str = ""):
    conn = get_connection()
    init_decision_table(conn)
    logged_at = datetime.now().strftime("%Y-%m-%d")
    review_date = (datetime.now() + timedelta(days=days_to_review)).strftime("%Y-%m-%d")

    with conn:
        conn.execute("""
            INSERT INTO decision_audit_trail
            (logged_at, project_hub, decision_name, target_url, metric_name, baseline_val, target_val, actual_val, review_date, status, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'IN_PROGRESS', ?);
        """, (logged_at, hub, name, url, metric, baseline, target, baseline, review_date, notes))
    conn.close()
    print(f"\n[OK] Đã ghi nhận quyết định chiến lược vào Sổ cái Audit Trail (Mã ID mới, ngày đối soát: {review_date}).")


def list_decisions():
    conn = get_connection()
    init_decision_table(conn)
    seed_initial_decisions(conn)

    cur = conn.cursor()
    cur.execute("""
        SELECT id, logged_at, project_hub, decision_name, target_url, metric_name,
               baseline_val, target_val, actual_val, review_date, status, notes
        FROM decision_audit_trail
        ORDER BY id DESC;
    """)
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("Sổ cái quyết định đang trống.")
        return

    table_data = []
    for r in rows:
        unit = "%" if "CVR" in r["metric_name"] or "CTR" in r["metric_name"] else ""
        dname = r["decision_name"] if len(r["decision_name"]) <= 35 else r["decision_name"][:32] + "..."
        url = r["target_url"] if len(r["target_url"]) <= 30 else r["target_url"][:27] + "..."
        table_data.append([
            r["id"],
            r["logged_at"],
            r["project_hub"],
            dname,
            url,
            r["metric_name"],
            f"{r['baseline_val']:.2f}{unit}",
            f"{r['target_val']:.2f}{unit}",
            f"{r['actual_val']:.2f}{unit}" if r["actual_val"] is not None else "Đang đo",
            r["review_date"],
            r["status"]
        ])

    headers = ["ID", "Ngày chốt", "Hub", "Tên Quyết định", "URL Target", "Chỉ số", "Baseline", "Target", "Thực tế", "Hạn đối soát", "Trạng thái"]
    print("\n" + "=" * 90)
    print("SỔ CÁI THEO DÕI QUYẾT ĐỊNH & ĐỐI SOÁT KẾT QUẢ THỰC TẾ (DECISION AUDIT TRAIL)")
    print("=" * 90)
    print(format_table(headers, table_data))
    print("=" * 90)


def audit_closed_loop():
    conn = get_connection()
    init_decision_table(conn)
    seed_initial_decisions(conn)

    cur = conn.cursor()
    cur.execute("""
        SELECT id, target_url, metric_name, baseline_val, target_val, review_date, status
        FROM decision_audit_trail
        WHERE status = 'IN_PROGRESS';
    """)
    rows = cur.fetchall()

    today_str = datetime.now().strftime("%Y-%m-%d")
    updates = []

    for r in rows:
        did = r["id"]
        url = r["target_url"]
        metric = r["metric_name"]
        baseline = r["baseline_val"]
        target = r["target_val"]
        rev_date = r["review_date"]

        actual = None
        # Tự động truy vấn số liệu thực tế từ Data Mart
        if "CVR" in metric.upper():
            cur.execute("""
                SELECT ROUND(SUM(onelink_clicks_track1 + onelink_clicks_track2) * 100.0 / NULLIF(SUM(sessions), 0), 2)
                FROM ga4_landing_pages
                WHERE landing_page = ?;
            """, (url,))
            res = cur.fetchone()
            if res and res[0] is not None:
                actual = float(res[0])
        elif "CTR" in metric.upper():
            cur.execute("""
                SELECT ROUND(AVG(ctr) * 100, 2)
                FROM gsc_search_analytics
                WHERE page_url = ? OR page_url = ('https://www.momo.vn' || ?);
            """, (url, url))
            res = cur.fetchone()
            if res and res[0] is not None:
                actual = float(res[0])

        if actual is not None:
            # Đánh giá trạng thái
            if actual >= target:
                new_status = "ACHIEVED"
            elif today_str > rev_date:
                new_status = "MISSED"
            else:
                new_status = "IN_PROGRESS"
            updates.append((actual, new_status, did))

    if updates:
        with conn:
            conn.executemany("""
                UPDATE decision_audit_trail
                SET actual_val = ?, status = ?
                WHERE id = ?;
            """, updates)
        print(f"[OK] Đã tự động đối soát và cập nhật {len(updates)} quyết định với số liệu thực tế.")
    else:
        print("[INFO] Chưa có quyết định nào đến hạn đối soát hoặc có biến động dữ liệu mới.")

    conn.close()
    list_decisions()


def main():
    parser = argparse.ArgumentParser(description="Decision Audit Trail & Tracker")
    parser.add_argument("--list", action="store_true", help="Xem danh sách quyết định trong sổ cái")
    parser.add_argument("--audit", action="store_true", help="Chạy đối soát tự động với số liệu Data Mart")
    parser.add_argument("--add", type=str, help="Tiêu đề quyết định cần ghi nhận")
    parser.add_argument("--hub", type=str, default="Web Platform", help="Hub liên quan")
    parser.add_argument("--url", type=str, default="/", help="URL mục tiêu")
    parser.add_argument("--metric", type=str, default="W2A CVR", help="Tên chỉ số (CTR, W2A CVR, Sessions)")
    parser.add_argument("--baseline", type=float, default=0.0, help="Giá trị mốc ban đầu (Baseline)")
    parser.add_argument("--target", type=float, default=0.0, help="Giá trị mục tiêu cam kết (Target)")
    parser.add_argument("--days", type=int, default=14, help="Số ngày hẹn đối soát")
    parser.add_argument("--notes", type=str, default="", help="Ghi chú bối cảnh quyết định")
    args = parser.parse_args()

    if args.add:
        add_decision(args.hub, args.add, args.url, args.metric, args.baseline, args.target, args.days, args.notes)
    elif args.audit:
        audit_closed_loop()
    else:
        list_decisions()


if __name__ == "__main__":
    main()
