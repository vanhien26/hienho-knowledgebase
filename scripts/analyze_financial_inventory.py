#!/usr/bin/env python3
"""
Analyze all CSV files in 05_HUBS/inventory/Financial/
Extract keywords and total search volume.
"""

import os
import csv
from pathlib import Path

def clean_val(v):
    if v is None:
        return ""
    v = str(v).strip()
    if v.startswith('="') and v.endswith('"'):
        v = v[2:-1]
    return v.strip()

def analyze():
    inv_dir = Path("05_HUBS/inventory/Financial")
    csv_files = sorted(inv_dir.glob("*.csv"))

    results = []
    file_keywords = {}

    for f in csv_files:
        total_vol = 0
        kw_count = 0
        kws = {}
        with open(f, mode="r", encoding="utf-8-sig", errors="ignore") as fp:
            reader = csv.reader(fp)
            header = next(reader, None)
            if not header:
                continue
            vol_idx = 1
            kw_idx = 0
            for i, h in enumerate(header):
                cleaned_h = clean_val(h).lower()
                if "volume" in cleaned_h or "search volume" in cleaned_h:
                    vol_idx = i
                if "keyword" in cleaned_h:
                    kw_idx = i
            for row in reader:
                if not row or len(row) <= max(kw_idx, vol_idx):
                    continue
                kw = clean_val(row[kw_idx]).lower()
                v_str = clean_val(row[vol_idx]).replace(",", "").replace(".", "")
                try:
                    v = int(v_str) if v_str else 0
                except ValueError:
                    v = 0
                total_vol += v
                kw_count += 1
                kws[kw] = max(kws.get(kw, 0), v)
        results.append({
            "name": f.stem,
            "filename": f.name,
            "kw_count": kw_count,
            "unique_kw_count": len(kws),
            "total_vol": total_vol,
            "kws": kws
        })
        file_keywords[f.stem] = kws

    # Sort descending by volume
    results.sort(key=lambda x: x["total_vol"], reverse=True)

    total_all_vol = sum(r["total_vol"] for r in results)
    total_all_kw = sum(r["kw_count"] for r in results)

    print(f"Total CSV Files: {len(results)}")
    print(f"Total Raw Rows/Keywords: {total_all_kw:,}")
    print(f"Total Raw Search Volume: {total_all_vol:,}\n")

    print(f"{'STT':<4} | {'File / Market':<28} | {'Keywords':<9} | {'Total Volume':<15} | {'Share (%)':<9}")
    print("-" * 75)
    for i, r in enumerate(results):
        share = (r["total_vol"] / total_all_vol * 100) if total_all_vol > 0 else 0
        print(f"{i+1:<4} | {r['name']:<28} | {r['kw_count']:<9,d} | {r['total_vol']:<15,d} | {share:6.2f}%")

if __name__ == "__main__":
    analyze()
