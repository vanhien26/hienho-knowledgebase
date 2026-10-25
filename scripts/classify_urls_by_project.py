#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLASSIFY URLs BY PROJECT
Gán nhãn Project cho danh sách URL dựa trên bảng DIM WEB_DIM_PAGE_URL.

Input hỗ trợ:
- JSON: {"urls": [...]} (như momo_live_urls.json) hoặc list thuần.
- CSV/TXT: cột 'url' hoặc mỗi dòng 1 URL.

Output:
- Bảng tổng hợp số URL theo Project (và nhóm UNMATCHED).
- File JSON mapping URL -> Project(s) tại --output.
"""

import os
import sys
import json
import csv
import argparse
from collections import Counter, defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(BASE_DIR, "scripts", "lib"))
from url_project_resolver import load_rules, load_inferred_rules, resolve, DEFAULT_CSV


def load_urls(path: str) -> list:
    if path.endswith(".json"):
        data = json.load(open(path, "r", encoding="utf-8"))
        if isinstance(data, dict):
            return data.get("urls", [])
        return data
    urls = []
    with open(path, "r", encoding="utf-8-sig") as f:
        if path.endswith(".csv"):
            for row in csv.DictReader(f):
                u = row.get("url") or row.get("URL") or ""
                if u.strip():
                    urls.append(u.strip())
        else:
            urls = [ln.strip() for ln in f if ln.strip()]
    return urls


def main():
    parser = argparse.ArgumentParser(description="Phân loại URL theo Project (WEB_DIM_PAGE_URL)")
    parser.add_argument("--input", required=True, help="File URL đầu vào (json/csv/txt)")
    parser.add_argument("--output", default=os.path.join(BASE_DIR, "07_REPORTS", "data", "url_project_mapping.json"),
                        help="File JSON mapping đầu ra")
    parser.add_argument("--csv", default=DEFAULT_CSV, help="Bảng DIM (mặc định SSOT trong repo)")
    parser.add_argument("--no-infer", action="store_true", help="Tắt fallback suy luận (chỉ dùng DIM)")
    args = parser.parse_args()

    rules = load_rules(args.csv)
    inferred = [] if args.no_infer else load_inferred_rules(rules)
    urls = load_urls(args.input)
    # Loại trùng lặp, giữ thứ tự
    urls = list(dict.fromkeys([u for u in urls if u]))
    print(f"Nạp {len(rules)} rule DIM + {len(inferred)} rule suy luận | {len(urls)} URL cần phân loại")

    primary_counter = Counter()   # mỗi URL chỉ cộng cho Project chính, không đếm trùng
    multi_counter = Counter()     # số project/URL
    source_counter = Counter()    # dim vs inferred
    mapping = []
    unmatched = []

    for u in urls:
        res = resolve(u, rules, inferred)
        if res["matched"]:
            primary_counter[res["primary"]] += 1
            multi_counter[len(res["projects"])] += 1
            source_counter[res["source"]] += 1
            mapping.append({"url": u, "projects": res["projects"],
                            "primary": res["primary"], "ambiguous": res["ambiguous"],
                            "match_type": res.get("match_type"),
                            "source": res["source"]})
        else:
            unmatched.append(u)
            mapping.append({"url": u, "projects": [], "primary": "", "ambiguous": False,
                            "match_type": None, "source": None})

    total = len(urls)
    matched = total - len(unmatched)

    print("\n=== TỔNG HỢP THEO PROJECT CHÍNH (đếm theo URL) ===")
    print(f"{'PROJECT':<28} | URL")
    print("-" * 45)
    for p, c in primary_counter.most_common():
        print(f"{p:<28} | {c}")
    print("-" * 45)
    print(f"{'(UNMATCHED)':<28} | {len(unmatched)}")
    print(f"\nTổng URL: {total} | Matched: {matched} ({round(matched/total*100,1) if total else 0}%) | Unmatched: {len(unmatched)}")
    print(f"  - Theo DIM (authoritative): {source_counter.get('dim', 0)}")
    print(f"  - Theo suy luận (inferred): {source_counter.get('inferred', 0)}")
    print(f"URL khớp nhiều Project: {sum(v for k,v in multi_counter.items() if k>1)}")

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
            "dim_source": args.csv,
            "total_urls": total,
            "matched": matched,
            "unmatched": len(unmatched),
            "by_source": {"dim": source_counter.get("dim", 0), "inferred": source_counter.get("inferred", 0)},
            "project_summary": dict(primary_counter.most_common()),
            "mapping": mapping,
        }, f, ensure_ascii=False, indent=2)
    print(f"\nĐã lưu mapping: {args.output}")


if __name__ == "__main__":
    main()
