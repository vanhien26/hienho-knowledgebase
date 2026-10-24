# -*- coding: utf-8 -*-
"""
URL PROJECT RESOLVER (CORE LIBRARY)
Xác định URL thuộc Project nào dựa trên bảng DIM: WEB_DIM_PAGE_URL (url_info).

Nguồn SSOT: 07_REPORTS/data/web_dim_page_url.csv
Schema: project_name, page_type, type, page_rule

Cơ chế khớp:
- Rule tĩnh (không có '*')  -> khớp chính xác.
- Rule glob (có '*')        -> khớp theo mẫu, ưu tiên rule có tiền tố literal dài nhất (cụ thể nhất).
- Một URL có thể khớp nhiều Project (trùng lặp Blog/News/Tin tức dùng chung) -> trả toàn bộ.
"""

import os
import re
import csv
import sys
import json
import argparse
import urllib.parse

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_CSV = os.path.join(BASE_DIR, "07_REPORTS", "data", "web_dim_page_url.csv")

# Chuẩn hóa tên Project (gộp các biến thể chỉ khác hoa/thường)
CANONICAL_PROJECT = {
    "vay nhanh": "Vay Nhanh",
    "phạt nguội": "Phạt Nguội",
    "tnc": "TnC",
    "dịch vụ liên kết": "Dịch vụ liên kết",
    "quản lý chi tiêu": "Quản Lý Chi Tiêu",
    "trung tâm tài chính": "Trung Tâm Tài Chính",
}


def _canonical_project(name: str) -> str:
    return CANONICAL_PROJECT.get(name.strip().lower(), name.strip())


# ---------------------------------------------------------------------------
# FALLBACK SUY LUẬN (INFERRED) - chỉ dùng khi DIM không khớp.
# Bổ sung rule catch-all cho các section nội dung mà DIM chưa liệt kê.
# specificity: code rule (120) > prefix rule (110) > generic blog (100).
# confidence: high = ánh xạ 1:1 rõ ràng | low = umbrella mặc định.
# ---------------------------------------------------------------------------
# Mã category blog -> Project (chỉ giữ các mã ánh xạ 1:1 đủ tin cậy, đối chiếu từ DIM)
INFERRED_BLOG_CODE = {
    "c100": ("Merchant", "high"),
    "c102": ("Merchant", "high"),
    "c101": ("OTA", "high"),
    "c116": ("Trung Tâm Tài Chính", "high"),
    "c117": ("Blog", "high"),
    "c181": ("Quản Lý Chi Tiêu", "high"),
    "c193": ("Data", "high"),
    "c198": ("Trust", "high"),
    "c199": ("Chứng Khoán", "high"),
}

INFERRED_PREFIX = [
    (r"^momo\.vn/hoi-dap(?:/.*)?$", "Hỏi đáp", "FAQ", "high"),
    (r"^momo\.vn/huong-dan(?:/.*)?$", "Guide", "Guide", "high"),
    (r"^momo\.vn/tin-tuc(?:/.*)?$", "Tin Tức", "News", "high"),
    (r"^momo\.vn/chao-ban-moi(?:/.*)?$", "New User", "Landing Page", "high"),
]


def load_inferred_rules() -> list:
    """Rule suy luận bổ sung khi DIM không khớp (source='inferred')."""
    rules = []
    for rx, project, ptype, conf in INFERRED_PREFIX:
        rules.append({"project": project, "page_type": ptype, "type": "Inferred",
                      "rule": f"(inferred) {rx}", "regex": re.compile(rx),
                      "kind": "inferred", "specificity": 110, "confidence": conf,
                      "source": "inferred"})
    for code, (project, conf) in INFERRED_BLOG_CODE.items():
        rx = re.compile(r"^momo\.vn/blog/.*-" + code + r"dt[^/]*$")
        rules.append({"project": project, "page_type": "Blog", "type": "Inferred",
                      "rule": f"(inferred) /blog/*-{code}dt*", "regex": rx,
                      "kind": "inferred", "specificity": 120, "confidence": conf,
                      "source": "inferred"})
    rules.append({"project": "Blog", "page_type": "Blog", "type": "Inferred",
                  "rule": "(inferred) /blog/*", "regex": re.compile(r"^momo\.vn/blog/.*$"),
                  "kind": "inferred", "specificity": 100, "confidence": "low",
                  "source": "inferred"})
    return rules


def normalize_url(url: str) -> str:
    """Chuẩn hóa URL để so khớp: bỏ scheme khác biệt, www, query, fragment, trailing slash."""
    if not url:
        return ""
    u = url.strip()
    if u.startswith("//"):
        u = "https:" + u
    elif u.startswith("/"):
        u = "https://momo.vn" + u
    elif not u.startswith("http"):
        u = "https://" + u
    p = urllib.parse.urlsplit(u)
    host = p.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = (p.path or "").rstrip("/")
    return f"{host}{path}".lower()


def _rule_to_regex(rule: str):
    """Chuyển rule thành (regex, kind, specificity). specificity = độ dài literal (không tính *)."""
    norm = normalize_url(rule)
    if "*" in norm:
        pattern = re.escape(norm).replace(r"\*", ".*")
        spec = len(norm.replace("*", ""))
        return re.compile("^" + pattern + "$", re.IGNORECASE), "glob", spec
    return re.compile("^" + re.escape(norm) + "$", re.IGNORECASE), "exact", len(norm)


def load_rules(csv_path: str = DEFAULT_CSV) -> list:
    """Nạp và biên dịch toàn bộ rule từ bảng DIM."""
    rules = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            project = (row.get("project_name") or "").strip()
            rule = (row.get("page_rule") or "").strip()
            if not project or project.upper() == "STRING":
                continue
            if not rule.startswith("http"):
                continue
            rx, kind, spec = _rule_to_regex(rule)
            rules.append({
                "project": _canonical_project(project),
                "page_type": (row.get("page_type") or "").strip(),
                "type": (row.get("type") or "").strip(),
                "rule": rule,
                "regex": rx,
                "kind": kind,
                "specificity": spec,
                "source": "dim",
                "confidence": "authoritative",
            })
    return rules


def resolve(url: str, rules: list, inferred_rules: list = None) -> dict:
    """
    Xác định Project của 1 URL. DIM luôn ưu tiên tuyệt đối; chỉ khi DIM không khớp
    mới dùng rule suy luận (source='inferred').
    Trả về dict: {url, normalized, matched, source, projects[], matches[]}.
    """
    nurl = normalize_url(url)
    exact, globs = [], []
    for r in rules:
        if r["regex"].match(nurl):
            (exact if r["kind"] == "exact" else globs).append(r)

    if exact:
        matches, match_type, source = exact, "exact", "dim"
    elif globs:
        best = max(r["specificity"] for r in globs)
        matches, match_type, source = [r for r in globs if r["specificity"] == best], "glob", "dim"
    elif inferred_rules:
        inf = [r for r in inferred_rules if r["regex"].match(nurl)]
        if not inf:
            return {"url": url, "normalized": nurl, "matched": False,
                    "source": None, "projects": [], "matches": []}
        best = max(r["specificity"] for r in inf)
        matches, match_type, source = [r for r in inf if r["specificity"] == best], "inferred", "inferred"
    else:
        return {"url": url, "normalized": nurl, "matched": False,
                "source": None, "projects": [], "matches": []}

    projects = sorted({r["project"] for r in matches})
    return {
        "url": url,
        "normalized": nurl,
        "matched": True,
        "match_type": match_type,
        "source": source,
        "projects": projects,
        "matches": [{"project": r["project"], "page_type": r["page_type"],
                     "rule": r["rule"], "match_type": r["kind"],
                     "source": r.get("source", "dim"),
                     "confidence": r.get("confidence", "authoritative")} for r in matches],
    }


def resolve_primary(url: str, rules: list, inferred_rules: list = None) -> str:
    """Trả về tên Project chính (đầu tiên theo thứ tự) hoặc '' nếu không khớp."""
    res = resolve(url, rules, inferred_rules)
    return res["projects"][0] if res["projects"] else ""


def main():
    parser = argparse.ArgumentParser(description="Xác định URL thuộc Project nào (WEB_DIM_PAGE_URL)")
    parser.add_argument("urls", nargs="*", help="Danh sách URL cần phân loại")
    parser.add_argument("--input", help="File chứa danh sách URL (mỗi dòng 1 URL)")
    parser.add_argument("--csv", default=DEFAULT_CSV, help="Đường dẫn bảng DIM (mặc định: SSOT trong repo)")
    parser.add_argument("--json", action="store_true", help="Xuất kết quả dạng JSON")
    parser.add_argument("--list-projects", action="store_true", help="Chỉ liệt kê Project & số rule")
    parser.add_argument("--no-infer", action="store_true", help="Tắt fallback suy luận (chỉ dùng DIM)")
    args = parser.parse_args()

    rules = load_rules(args.csv)
    inferred = [] if args.no_infer else load_inferred_rules()

    if args.list_projects:
        from collections import Counter
        counts = Counter(r["project"] for r in rules)
        print(f"Tổng rule: {len(rules)} | Project: {len(counts)}")
        for p, c in counts.most_common():
            print(f"  {p}: {c}")
        return

    urls = list(args.urls)
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            urls += [ln.strip() for ln in f if ln.strip()]
    if not urls:
        parser.error("Cần cung cấp URL (tham số) hoặc --input")

    results = [resolve(u, rules, inferred) for u in urls]

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    print(f"{'URL':<66} | {'PROJECT(S)':<34} | SOURCE/MATCH")
    print("-" * 130)
    for r in results:
        proj = ", ".join(r["projects"]) if r["projects"] else "(UNMATCHED)"
        tag = f"{r.get('source','-')}/{r.get('match_type','-')}" if r["matched"] else "-"
        print(f"{r['normalized'][:66]:<66} | {proj[:34]:<34} | {tag}")


if __name__ == "__main__":
    main()
