"""Parse GSC Top Linking Sites CSV -> backlink_profile_latest.json.

Dinh dang CSV: Site, Linking pages, Target pages
Output schema giong backlink_profile_latest.json hien tai.
"""

import csv
import json
import os
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_PATH = os.path.join(BASE_DIR, "07_REPORTS/technical_seo/backlinks/backlink_profile_latest.json")


def _norm(s):
    return (s or "").strip().lower()


def parse(file_path):
    with open(file_path, "r", encoding="utf-8-sig", errors="replace") as f:
        rows = list(csv.reader(f))
    if len(rows) < 2:
        raise RuntimeError("Backlink CSV qua nguong (khong du dong).")

    header = [_norm(c) for c in rows[0]]
    idx_site = idx_pages = idx_targets = None
    for i, h in enumerate(header):
        if h in ("site", "domain", "source"):
            idx_site = i
        elif "linking pages" in h or h == "pages":
            idx_pages = i
        elif "target" in h:
            idx_targets = i
    if idx_site is None or idx_pages is None:
        raise RuntimeError(f"Khong nhan dien duoc cot Site/Linking pages. Header: {header}")

    sites = []
    total_pages = 0
    for row in rows[1:]:
        if not row or idx_site >= len(row):
            continue
        site = (row[idx_site] or "").strip()
        if not site:
            continue
        try:
            pages = int(float(row[idx_pages] or 0))
        except (ValueError, IndexError):
            pages = 0
        try:
            targets = int(float(row[idx_targets] or 0)) if idx_targets is not None and idx_targets < len(row) else 0
        except (ValueError, IndexError):
            targets = 0
        sites.append({"domain": site, "linking_pages": pages, "target_urls_count": targets})
        total_pages += pages

    if not sites:
        raise RuntimeError("Khong trich duoc site nao tu CSV.")

    sites.sort(key=lambda x: x["linking_pages"], reverse=True)

    # Distribution buckets
    buckets = {
        "ge_1000_pages": {"sites_count": 0, "linking_pages": 0},
        "100_to_999_pages": {"sites_count": 0, "linking_pages": 0},
        "10_to_99_pages": {"sites_count": 0, "linking_pages": 0},
        "1_to_9_pages": {"sites_count": 0, "linking_pages": 0},
    }
    for s in sites:
        p = s["linking_pages"]
        if p >= 1000:
            k = "ge_1000_pages"
        elif p >= 100:
            k = "100_to_999_pages"
        elif p >= 10:
            k = "10_to_99_pages"
        else:
            k = "1_to_9_pages"
        buckets[k]["sites_count"] += 1
        buckets[k]["linking_pages"] += p
    for b in buckets.values():
        b["pct"] = round(b["linking_pages"] / total_pages * 100, 1) if total_pages else 0

    top_concentrations = [
        {
            "domain": s["domain"],
            "linking_pages": s["linking_pages"],
            "target_urls_count": s["target_urls_count"],
            "pct": round(s["linking_pages"] / total_pages * 100, 1) if total_pages else 0,
        }
        for s in sites[:10]
    ]

    out = {
        "source": "Google Search Console - Top Linking Sites (www.momo.vn)",
        "export_date": datetime.now().strftime("%Y-%m-%d"),
        "total_referring_domains": len(sites),
        "total_linking_pages": total_pages,
        "distribution_buckets": buckets,
        "top_concentrations": top_concentrations,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Da ghi backlink profile vao {OUT_PATH} ({len(sites)} sites)")
    return {"parser": "backlink", "source": file_path, "sites": len(sites), "total_pages": total_pages}
