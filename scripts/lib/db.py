"""
MoMo Web Platform - SQLite Database Layer SSOT
Quản lý tập trung dữ liệu hiệu suất Google Search Console (GSC) và Google Analytics 4 (GA4).
Tối ưu hóa:
- Zero dependency (dùng built-in sqlite3 của Python)
- Portable: đường dẫn tương đối, chạy được trên mọi máy
- O(1) query latency nhờ B-Tree Indexing trên (page_url, query)
- WAL Mode: Đọc ghi đồng thời hiệu năng cao
"""

import os
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "07_REPORTS" / "data"
DEFAULT_DB_PATH = DATA_DIR / "performance.sqlite"


def get_connection(db_path: Optional[Path] = None) -> sqlite3.Connection:
    """Khởi tạo kết nối SQLite với cấu hình hiệu năng cao."""
    path = db_path or DEFAULT_DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    # Tối ưu WAL mode và Cache size
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    conn.execute("PRAGMA cache_size = -64000;")  # 64MB cache
    return conn


def init_db(db_path: Optional[Path] = None) -> None:
    """Tạo bảng và các chỉ mục (Indexes) nếu chưa tồn tại."""
    conn = get_connection(db_path)
    with conn:
        # 1. Bảng Search Console Analytics (GSC Raw & Filtered)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS gsc_search_analytics (
                page_url TEXT NOT NULL,
                query TEXT NOT NULL,
                clicks INTEGER NOT NULL DEFAULT 0,
                impressions INTEGER NOT NULL DEFAULT 0,
                ctr REAL NOT NULL DEFAULT 0.0,
                position REAL NOT NULL DEFAULT 0.0,
                synced_at TEXT,
                PRIMARY KEY (page_url, query)
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_gsc_query ON gsc_search_analytics(query);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_gsc_page ON gsc_search_analytics(page_url);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_gsc_clicks ON gsc_search_analytics(clicks DESC);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_gsc_impressions ON gsc_search_analytics(impressions DESC);")

        # 2. Bảng GA4 Landing Pages & W2A Funnel
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ga4_landing_pages (
                landing_page TEXT NOT NULL,
                channel_group TEXT NOT NULL DEFAULT '',
                source TEXT NOT NULL DEFAULT '',
                sessions INTEGER NOT NULL DEFAULT 0,
                engaged_sessions INTEGER NOT NULL DEFAULT 0,
                onelink_clicks_track1 INTEGER NOT NULL DEFAULT 0,
                onelink_clicks_track2 INTEGER NOT NULL DEFAULT 0,
                synced_at TEXT,
                PRIMARY KEY (landing_page, channel_group, source)
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ga4_page ON ga4_landing_pages(landing_page);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ga4_sessions ON ga4_landing_pages(sessions DESC);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ga4_channel ON ga4_landing_pages(channel_group);")

        # 3. Bảng GSC Keyword Ranking Inventory Matching
        conn.execute("""
            CREATE TABLE IF NOT EXISTS gsc_keyword_ranking (
                query TEXT PRIMARY KEY,
                clicks INTEGER NOT NULL DEFAULT 0,
                impressions INTEGER NOT NULL DEFAULT 0,
                position REAL NOT NULL DEFAULT 0.0,
                rounded_position INTEGER NOT NULL DEFAULT 0,
                opportunity_score REAL NOT NULL DEFAULT 0.0,
                synced_at TEXT
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ranking_pos ON gsc_keyword_ranking(position);")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_ranking_opp ON gsc_keyword_ranking(opportunity_score DESC);")

    conn.close()


def query_gsc_by_keyword(query: str, limit: int = 20, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu nhanh các URL xếp hạng theo từ khóa (O(1) latency)."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT page_url, query, clicks, impressions, ctr, position
        FROM gsc_search_analytics
        WHERE query = ?
        ORDER BY clicks DESC, impressions DESC
        LIMIT ?;
    """, (query, limit))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_gsc_by_url(url: str, limit: int = 50, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu các từ khóa đem lại lượt click nhiều nhất cho một URL."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT query, clicks, impressions, ctr, position
        FROM gsc_search_analytics
        WHERE page_url = ?
        ORDER BY clicks DESC, impressions DESC
        LIMIT ?;
    """, (url, limit))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def query_ga4_by_path(path_pattern: str, limit: int = 50, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Tra cứu hiệu suất GA4 theo đường dẫn landing page."""
    conn = get_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        SELECT landing_page, channel_group, source, sessions, engaged_sessions,
               onelink_clicks_track1, onelink_clicks_track2
        FROM ga4_landing_pages
        WHERE landing_page LIKE ?
        ORDER BY sessions DESC
        LIMIT ?;
    """, (f"{path_pattern}%", limit))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


if __name__ == "__main__":
    init_db()
    print(f"[OK] Đã khởi tạo thành công cấu trúc SQLite tại: {DEFAULT_DB_PATH}")
