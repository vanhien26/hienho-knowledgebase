#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ingest pipeline for Bing AI Performance (Microsoft Copilot citations) for momo.vn.

Scans ~/Downloads for Bing Webmaster Tools AI Performance exports (CSV or ZIP),
identifies file types by actual column headers (not filename), copies raw files to
07_REPORTS/data/bing_ai/raw/, normalizes data into a standard schema, creates
a timestamped historical snapshot, and updates ai_performance_latest.json.
"""

import argparse
import csv
import json
import os
import re
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


def parse_citations(val: Any) -> int:
    """
    Parse citation count into integer.
    Handles '9.7K', '1.2M', '2,878', 2878, '500', '', None, etc.
    """
    if val is None:
        return 0
    if isinstance(val, (int, float)):
        return int(val)
    s = str(val).strip().replace(",", "").replace(" ", "")
    if not s or s in ("-", "null", "None", "N/A"):
        return 0

    multiplier = 1
    last_char = s[-1].upper()
    if last_char == "K":
        multiplier = 1_000
        s = s[:-1]
    elif last_char == "M":
        multiplier = 1_000_000
        s = s[:-1]
    elif last_char == "B":
        multiplier = 1_000_000_000
        s = s[:-1]

    try:
        return int(round(float(s) * multiplier))
    except ValueError:
        return 0


def parse_citation_share(val: Any) -> Optional[float]:
    """
    Parse citation share into decimal between 0.0 and 1.0.
    Handles '13.26%', '13.26', '0.1326', 0.1326, etc.
    """
    if val is None:
        return None
    s = str(val).strip().replace(" ", "")
    if not s or s in ("-", "null", "None", "N/A"):
        return None

    is_percent = False
    if s.endswith("%"):
        is_percent = True
        s = s[:-1]

    try:
        num = float(s)
        if is_percent or num > 1.0:
            return round(num / 100.0, 6)
        return round(num, 6)
    except ValueError:
        return None


def read_header_from_file(file_path: Path) -> List[str]:
    """Read first non-empty line of CSV and return column names."""
    for encoding in ("utf-8-sig", "utf-8", "latin1"):
        try:
            with open(file_path, "r", encoding=encoding) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        reader = csv.reader([line])
                        return [col.strip() for col in next(reader) if col.strip()]
        except UnicodeDecodeError:
            continue
        except Exception:
            break
    return []


def read_header_from_zip_member(zip_ref: zipfile.ZipFile, member_name: str) -> List[str]:
    """Read first non-empty line of CSV inside ZIP."""
    with zip_ref.open(member_name) as f:
        for line_bytes in f:
            line = line_bytes.decode("utf-8-sig", errors="ignore").strip()
            if line:
                reader = csv.reader([line])
                return [col.strip() for col in next(reader) if col.strip()]
    return []


def classify_headers(headers: List[str]) -> str:
    """
    Classify file type by column headers:
    - OVERVIEW: contains date and citations
    - QUERIES: contains query/grounding and citations
    - PAGES: contains page/url and citations (and not query)
    - UNKNOWN: not recognized
    """
    if not headers:
        return "UNKNOWN"

    norm = [re.sub(r'["\']', '', h).strip().lower() for h in headers if h and h.strip()]

    has_date = any("date" in h or "ngày" in h for h in norm)
    has_citation = any("citation" in h or "trích dẫn" in h for h in norm)
    has_query = any(k in h for h in norm for k in ("grounding", "query", "keyword", "truy vấn", "từ khóa"))
    has_page = any(k in h for h in norm for k in ("page", "url", "landing", "trang"))

    if has_date and has_citation:
        return "OVERVIEW"

    if has_query and has_citation:
        return "QUERIES"

    if has_page and has_citation and not has_query:
        return "PAGES"

    if has_page and has_citation:
        first_col = norm[0] if norm else ""
        if "page" in first_col or "url" in first_col:
            return "PAGES"
        return "QUERIES"

    return "UNKNOWN"


def find_matching_column(headers: List[str], keywords: List[str]) -> Optional[str]:
    """Find the original header string that matches any of the given keywords."""
    norm_headers = [(h, re.sub(r'["\']', '', h).strip().lower()) for h in headers]
    for orig, norm in norm_headers:
        for kw in keywords:
            if kw in norm:
                return orig
    return None


def parse_date(date_str: str) -> Optional[datetime]:
    """Parse various date strings into datetime object."""
    if not date_str:
        return None
    s = str(date_str).strip().replace('"', "")
    formats = [
        "%m/%d/%Y %I:%M:%S %p",
        "%m/%d/%Y %H:%M:%S",
        "%m/%d/%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%d/%m/%Y",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def parse_overview_csv(file_path_or_stream) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Parse OverviewStats CSV to compute period and totals.
    """
    if isinstance(file_path_or_stream, (str, Path)):
        f = open(file_path_or_stream, "r", encoding="utf-8-sig")
        should_close = True
    else:
        f = file_path_or_stream
        should_close = False

    try:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        date_col = find_matching_column(headers, ["date", "ngày"])
        citations_col = find_matching_column(headers, ["citation", "trích dẫn"])
        pages_col = find_matching_column(headers, ["cited page", "page", "trang"])

        dates = []
        total_citations = 0
        pages_counts = []

        for row in reader:
            if date_col and row.get(date_col):
                d = parse_date(row[date_col])
                if d:
                    dates.append(d)
            if citations_col and row.get(citations_col):
                total_citations += parse_citations(row[citations_col])
            if pages_col and row.get(pages_col):
                pages_counts.append(parse_citations(row[pages_col]))

        period: Dict[str, Any] = {"start": None, "end": None, "days": None}
        if dates:
            min_d = min(dates)
            max_d = max(dates)
            period["start"] = min_d.strftime("%Y-%m-%d")
            period["end"] = max_d.strftime("%Y-%m-%d")
            period["days"] = len(set(d.date() for d in dates))

        avg_cited_pages = round(sum(pages_counts) / len(pages_counts), 2) if pages_counts else 0
        totals = {
            "citations": total_citations,
            "avg_cited_pages": avg_cited_pages,
        }
        return period, totals
    finally:
        if should_close:
            f.close()


def parse_queries_csv(file_path_or_stream) -> Tuple[List[Dict[str, Any]], Set[str]]:
    """
    Parse Grounding Queries CSV.
    Returns: (queries_list, detected_missing_fields)
    """
    if isinstance(file_path_or_stream, (str, Path)):
        f = open(file_path_or_stream, "r", encoding="utf-8-sig")
        should_close = True
    else:
        f = file_path_or_stream
        should_close = False

    try:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []

        query_col = find_matching_column(headers, ["grounding query", "query", "keyword", "truy vấn", "từ khóa"])
        citations_col = find_matching_column(headers, ["citation", "trích dẫn"])
        intent_col = find_matching_column(headers, ["intent", "ý định"])
        topic_col = find_matching_column(headers, ["topic", "theme", "chủ đề"])
        share_col = find_matching_column(headers, ["share", "tỷ lệ", "%"])
        url_col = find_matching_column(headers, ["url", "cited url", "page", "trang"])

        missing_fields: Set[str] = set()
        if not intent_col:
            missing_fields.add("intent")
        if not topic_col:
            missing_fields.add("topic")
        if not share_col:
            missing_fields.add("citation_share")
        if not url_col:
            missing_fields.add("cited_urls")

        queries_map: Dict[str, Dict[str, Any]] = {}

        for row in reader:
            if not query_col or not row.get(query_col):
                continue
            q_text = row[query_col].strip()
            c_val = parse_citations(row.get(citations_col)) if citations_col else 0
            i_val = row[intent_col].strip() if (intent_col and row.get(intent_col)) else None
            t_val = row[topic_col].strip() if (topic_col and row.get(topic_col)) else None
            s_val = parse_citation_share(row.get(share_col)) if share_col else None
            u_val = row[url_col].strip() if (url_col and row.get(url_col)) else None

            if q_text not in queries_map:
                queries_map[q_text] = {
                    "query": q_text,
                    "intent": i_val,
                    "topic": t_val,
                    "citations": c_val,
                    "citation_share": s_val,
                    "cited_urls": [],
                }
                if u_val:
                    queries_map[q_text]["cited_urls"].append({"url": u_val, "citations": c_val})
            else:
                # Grouping if duplicate query row
                if u_val:
                    queries_map[q_text]["cited_urls"].append({"url": u_val, "citations": c_val})
                    queries_map[q_text]["citations"] += c_val
                elif c_val > queries_map[q_text]["citations"]:
                    queries_map[q_text]["citations"] = c_val

        queries_list = list(queries_map.values())
        queries_list.sort(key=lambda x: x["citations"], reverse=True)
        return queries_list, missing_fields
    finally:
        if should_close:
            f.close()


def parse_pages_csv(file_path_or_stream) -> Tuple[List[Dict[str, Any]], Set[str]]:
    """
    Parse Pages CSV.
    Returns: (pages_list, detected_missing_fields)
    """
    if isinstance(file_path_or_stream, (str, Path)):
        f = open(file_path_or_stream, "r", encoding="utf-8-sig")
        should_close = True
    else:
        f = file_path_or_stream
        should_close = False

    try:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []

        url_col = find_matching_column(headers, ["page", "url", "landing", "trang"])
        citations_col = find_matching_column(headers, ["citation", "trích dẫn"])
        top_queries_col = find_matching_column(headers, ["top query", "top queries", "queries", "query"])

        missing_fields: Set[str] = set()
        if not top_queries_col:
            missing_fields.add("top_queries")

        pages_map: Dict[str, Dict[str, Any]] = {}

        for row in reader:
            if not url_col or not row.get(url_col):
                continue
            u_text = row[url_col].strip()
            c_val = parse_citations(row.get(citations_col)) if citations_col else 0

            q_list = []
            if top_queries_col and row.get(top_queries_col):
                raw_q = row[top_queries_col].strip()
                # support delimiter by semicolon, comma, or newline
                parts = re.split(r"[;\n,]+", raw_q)
                q_list = [p.strip() for p in parts if p.strip()]

            if u_text not in pages_map:
                pages_map[u_text] = {
                    "url": u_text,
                    "citations": c_val,
                    "top_queries": q_list,
                }
            else:
                pages_map[u_text]["citations"] += c_val
                if q_list:
                    pages_map[u_text]["top_queries"].extend(q_list)

        pages_list = list(pages_map.values())
        pages_list.sort(key=lambda x: x["citations"], reverse=True)
        return pages_list, missing_fields
    finally:
        if should_close:
            f.close()


def discover_and_classify_inputs(explicit_files: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    Discover candidate files from explicit arguments or ~/Downloads directory.
    Prints actual header before processing.
    """
    downloads_dir = Path.home() / "Downloads"
    discovered = []

    files_to_check: List[Path] = []
    if explicit_files:
        for f in explicit_files:
            p = Path(f).expanduser().resolve()
            if p.exists():
                files_to_check.append(p)
            else:
                print(f"[CẢNH BÁO] Không tìm thấy file chỉ định: {f}")
    else:
        # Search ~/Downloads
        for ext in ("*.csv", "*.zip"):
            files_to_check.extend(downloads_dir.glob(ext))
        # Sort newest first
        files_to_check.sort(key=lambda p: p.stat().st_mtime, reverse=True)

    seen_types = set()

    for file_path in files_to_check:
        if file_path.name.startswith("~$") or file_path.name.startswith("."):
            continue

        if file_path.suffix.lower() == ".csv":
            headers = read_header_from_file(file_path)
            file_type = classify_headers(headers)
            if file_type != "UNKNOWN":
                print(f"[INPUT] File: {file_path}")
                print(f"[HEADER]: {headers} -> Nhận diện: {file_type}")
                if file_type not in seen_types or explicit_files:
                    discovered.append({
                        "source_type": "csv",
                        "path": file_path,
                        "file_type": file_type,
                        "headers": headers,
                    })
                    seen_types.add(file_type)

        elif file_path.suffix.lower() == ".zip":
            try:
                with zipfile.ZipFile(file_path, "r") as z:
                    for member in z.namelist():
                        if member.lower().endswith(".csv") and not member.startswith("__MACOSX"):
                            headers = read_header_from_zip_member(z, member)
                            file_type = classify_headers(headers)
                            if file_type != "UNKNOWN":
                                print(f"[INPUT] ZIP: {file_path} | Entry: {member}")
                                print(f"[HEADER]: {headers} -> Nhận diện: {file_type}")
                                if file_type not in seen_types or explicit_files:
                                    discovered.append({
                                        "source_type": "zip",
                                        "path": file_path,
                                        "member": member,
                                        "file_type": file_type,
                                        "headers": headers,
                                    })
                                    seen_types.add(file_type)
            except Exception as e:
                print(f"[LỖI] Không thể đọc file ZIP {file_path}: {e}")

    return discovered


def save_history_snapshot(history_dir: Path, today_str: str, payload: Dict[str, Any]) -> Path:
    """Save payload to history/<YYYY-MM-DD>.json, appending _2, _3 if already exists."""
    history_dir.mkdir(parents=True, exist_ok=True)
    base_file = history_dir / f"{today_str}.json"
    if not base_file.exists():
        target_path = base_file
    else:
        index = 2
        while True:
            candidate = history_dir / f"{today_str}_{index}.json"
            if not candidate.exists():
                target_path = candidate
                break
            index += 1

    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return target_path


def main():
    parser = argparse.ArgumentParser(
        description="Ingest dữ liệu Bing AI Performance (Copilot citations) cho momo.vn."
    )
    parser.add_argument(
        "--file",
        nargs="+",
        help="Đường dẫn đến một hoặc nhiều file CSV/ZIP tải về từ Bing Webmaster Tools.",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    data_dir = project_root / "07_REPORTS" / "data" / "bing_ai"
    raw_dir = data_dir / "raw"
    history_dir = data_dir / "history"
    latest_file = data_dir / "ai_performance_latest.json"

    raw_dir.mkdir(parents=True, exist_ok=True)
    history_dir.mkdir(parents=True, exist_ok=True)

    today_str = datetime.now().strftime("%Y-%m-%d")
    current_iso = datetime.now(timezone.utc).astimezone().isoformat()

    print("======================================================================")
    print("BING AI PERFORMANCE INGESTION PIPELINE (momo.vn)")
    print(f"Thời gian: {current_iso} | Ngày ghi nhận: {today_str}")
    print("======================================================================")

    # 1. Discover and classify inputs
    inputs = discover_and_classify_inputs(args.file)
    if not inputs:
        print("\n[LỖI] Không tìm thấy file export AI Performance hợp lệ trong ~/Downloads hoặc đường dẫn cung cấp.")
        print("Vui lòng tải file export từ Bing Webmaster Tools (Queries, Pages hoặc Overview) vào ~/Downloads.")
        sys.exit(1)

    print(f"\nPhát hiện {len(inputs)} file dữ liệu hợp lệ:")
    for inp in inputs:
        print(f"  - Phân loại: {inp['file_type']:<10} | Nguồn: {inp['path'].name}")

    # 2. Process each input and copy to raw/
    queries_data: List[Dict[str, Any]] = []
    pages_data: List[Dict[str, Any]] = []
    overview_period: Optional[Dict[str, Any]] = None
    overview_totals: Optional[Dict[str, Any]] = None

    all_missing_fields: Set[str] = set()
    copied_raw_files = []

    for inp in inputs:
        ftype = inp["file_type"]
        src_path = inp["path"]

        # Copy original file into raw/<YYYY-MM-DD>_<type>.csv
        target_name = f"{today_str}_{ftype.lower()}.csv"
        raw_target = raw_dir / target_name

        if inp["source_type"] == "csv":
            shutil.copy2(src_path, raw_target)
            copied_raw_files.append(raw_target)
            stream_or_path = raw_target
        else:
            # Extract from ZIP
            with zipfile.ZipFile(src_path, "r") as z:
                with z.open(inp["member"]) as member_file, open(raw_target, "wb") as out_f:
                    shutil.copyfileobj(member_file, out_f)
            copied_raw_files.append(raw_target)
            stream_or_path = raw_target

        if ftype == "QUERIES":
            q_list, q_missing = parse_queries_csv(stream_or_path)
            queries_data = q_list
            all_missing_fields.update(q_missing)
        elif ftype == "PAGES":
            p_list, p_missing = parse_pages_csv(stream_or_path)
            pages_data = p_list
            all_missing_fields.update(p_missing)
        elif ftype == "OVERVIEW":
            o_period, o_totals = parse_overview_csv(stream_or_path)
            overview_period = o_period
            overview_totals = o_totals

    # 3. Consolidate period and totals
    if overview_period and overview_period.get("start"):
        period = overview_period
    else:
        period = {"start": None, "end": None, "days": None}
        all_missing_fields.add("period")

    if overview_totals and overview_totals.get("citations") is not None:
        totals = overview_totals
    else:
        calc_citations = sum(q["citations"] for q in queries_data) if queries_data else (
            sum(p["citations"] for p in pages_data) if pages_data else 0
        )
        avg_p = round(len(pages_data) / period["days"], 2) if (pages_data and period.get("days")) else (
            len(pages_data) if pages_data else 0
        )
        totals = {
            "citations": calc_citations,
            "avg_cited_pages": avg_p,
        }
        if not overview_totals:
            all_missing_fields.add("avg_cited_pages")

    if not queries_data:
        all_missing_fields.add("queries")
    if not pages_data:
        all_missing_fields.add("pages")

    sorted_missing_fields = sorted(list(all_missing_fields))

    # 4. Construct output JSON payload
    payload = {
        "source": "bing_ai_performance",
        "exported_at": current_iso,
        "period": period,
        "totals": totals,
        "missing_fields": sorted_missing_fields,
        "queries": queries_data,
        "pages": pages_data,
    }

    # 5. Save latest JSON
    with open(latest_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    # 6. Save history snapshot
    history_file = save_history_snapshot(history_dir, today_str, payload)

    # 7. Print summary
    print("\n" + "=" * 70)
    print("KẾT QUẢ INGEST DỮ LIỆU BING AI PERFORMANCE")
    print("=" * 70)
    print(f"- Số query ghi nhận:       {len(queries_data):,}")
    print(f"- Tổng citations:          {totals['citations']:,}")
    print(f"- Số trang (Pages):        {len(pages_data):,}")
    print(f"- Cited Pages trung bình:  {totals['avg_cited_pages']}")
    print(f"- Chu kỳ dữ liệu:          {period.get('start')} -> {period.get('end')} ({period.get('days')} ngày)")
    print(f"- Cột / Dữ liệu bị thiếu:  {', '.join(sorted_missing_fields) if sorted_missing_fields else 'Không'}")

    print("\nTOP 10 QUERY THEO CITATIONS:")
    if queries_data:
        print(f" {'STT':<4} | {'Query':<40} | {'Citations':<10} | {'Share':<8}")
        print("-" * 70)
        for idx, q in enumerate(queries_data[:10], start=1):
            q_text = q['query'][:38] + (".." if len(q['query']) > 38 else "")
            share_str = f"{round(q['citation_share'] * 100, 2)}%" if q.get('citation_share') is not None else "N/A"
            print(f" {idx:<4} | {q_text:<40} | {q['citations']:<10,} | {share_str:<8}")
    else:
        print(" (Chưa có dữ liệu Grounding Queries trong nguồn vào lần này)")

    print("\nLƯU TRỮ VÀ ĐỒNG BỘ:")
    print(f"- File Raw:                {', '.join(str(f.relative_to(project_root)) for f in copied_raw_files)}")
    print(f"- File Latest:             {latest_file.relative_to(project_root)}")
    print(f"- File Snapshot Lịch sử:   {history_file.relative_to(project_root)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
