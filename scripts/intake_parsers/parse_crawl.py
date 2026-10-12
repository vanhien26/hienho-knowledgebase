"""Parse GSC Crawl Stats export (zip hoac csv) -> gsc_crawl_stats_latest.json.

Support 2 dinh dang:
- zip chua CSV daily crawl stats (GSC export)
- csv daily truc tiep

Output schema giong gsc_crawl_stats_latest.json hien tai (monthly_run_rate).
"""

import csv
import io
import json
import os
import zipfile
from collections import defaultdict
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_PATH = os.path.join(BASE_DIR, "07_REPORTS/technical_seo/crawl_stats/gsc_crawl_stats_latest.json")


def _read_daily_rows(path):
    """Tra ve list[(date, crawled_pages, download_kb, response_time_ms)]."""
    rows = []
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as zf:
            csv_names = [n for n in zf.namelist() if n.lower().endswith(".csv")]
            if not csv_names:
                raise RuntimeError("Zip khong chua CSV crawl stats.")
            with zf.open(csv_names[0]) as f:
                text = io.TextIOWrapper(f, encoding="utf-8-sig", errors="replace")
                rows = list(csv.reader(text))
    else:
        with open(path, "r", encoding="utf-8-sig", errors="replace") as f:
            rows = list(csv.reader(f))
    return rows


def _norm(s):
    return (s or "").strip().lower()


def _parse_date(s):
    s = (s or "").strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def parse(file_path):
    raw = _read_daily_rows(file_path)
    if len(raw) < 2:
        raise RuntimeError("Crawl stats file qua nguong (khong du dong du lieu).")

    header = [_norm(c) for c in raw[0]]
    # Tim chi so cot
    idx_date = idx_pages = idx_kb = idx_ms = None
    for i, h in enumerate(header):
        if "date" in h or h == "ngay":
            idx_date = i
        elif "crawled" in h or "pages" in h:
            idx_pages = i
        elif "download" in h or "kb" in h:
            idx_kb = i
        elif "time" in h or "response" in h or "ms" in h:
            idx_ms = i
    if idx_date is None or idx_pages is None:
        raise RuntimeError(f"Khong nhan dien duoc cot Date/Crawled pages. Header: {header}")

    by_month = defaultdict(lambda: {"days": 0, "requests": 0, "kb": 0, "ms": 0})
    total_requests = 0
    first_date = last_date = None

    for row in raw[1:]:
        if not row or idx_date >= len(row):
            continue
        d = _parse_date(row[idx_date])
        if not d:
            continue
        try:
            pages = int(float(row[idx_pages] or 0))
        except (ValueError, IndexError):
            pages = 0
        try:
            kb = int(float(row[idx_kb] or 0)) if idx_kb is not None and idx_kb < len(row) else 0
        except (ValueError, IndexError):
            kb = 0
        try:
            ms = int(float(row[idx_ms] or 0)) if idx_ms is not None and idx_ms < len(row) else 0
        except (ValueError, IndexError):
            ms = 0

        mkey = d.strftime("%Y-%m")
        bucket = by_month[mkey]
        bucket["days"] += 1
        bucket["requests"] += pages
        bucket["kb"] += kb
        bucket["ms"] += ms
        total_requests += pages
        if first_date is None or d < first_date:
            first_date = d
        if last_date is None or d > last_date:
            last_date = d

    monthly = {}
    for mkey, b in sorted(by_month.items()):
        if b["days"] == 0:
            continue
        monthly[mkey] = {
            "days": b["days"],
            "requests_per_day": round(b["requests"] / b["days"]),
            "download_mb_per_day": round(b["kb"] / b["days"] / 1024),
            "kb_per_request": round(b["kb"] / b["requests"], 1) if b["requests"] else 0,
            "response_time_ms": round(b["ms"] / b["days"]),
        }

    out = {
        "source": "Google Search Console - Crawl Stats (www.momo.vn)",
        "export_date": datetime.now().strftime("%Y-%m-%d"),
        "window": {
            "start": first_date.isoformat() if first_date else None,
            "end": last_date.isoformat() if last_date else None,
            "total_requests": total_requests,
            "host_status": "No problems",
        },
        "monthly_run_rate": monthly,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Da ghi crawl stats vao {OUT_PATH} ({len(monthly)} thang)")
    return {"parser": "crawl_stats", "source": file_path, "months": len(monthly), "total_requests": total_requests}
