#!/usr/bin/env python3
"""
Google Suggest / Autocomplete Keyword Expander (100% Free, Unlimited)
Mục đích:
1. Gọi Google Suggest API hoàn toàn miễn phí: https://suggestqueries.google.com/complete/search
2. Mở rộng từ khóa đệ quy theo 3 chiều:
   - A-Z Alphabet Expansion (seed + a..z)
   - Question & Informational Modifiers (là gì, ở đâu, cách, bao nhiêu, tại sao...)
   - Commercial & Transactional Modifiers (mua, bán, tra cứu, biểu phí, hôm nay, online...)
3. Làm sạch, phân loại Intent và xuất JSON/CSV hoặc tích hợp trực tiếp vào pipeline Use Cases.
"""

import os
import sys
import json
import urllib.parse
import urllib.request
import time
from typing import List, Dict, Set

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

# Danh sách tiền tố & hậu tố mở rộng ngữ nghĩa tiếng Việt
QUESTION_PREFIXES = ["cách", "hướng dẫn", "tra cứu", "kiểm tra", "xem"]
QUESTION_SUFFIXES = ["là gì", "ở đâu", "bao nhiêu", "như thế nào", "có an toàn không", "hôm nay", "mới nhất"]
COMMERCIAL_MODIFIERS = ["online", "trực tuyến", "ở đâu uy tín", "giá rẻ", "miễn phí", "ưu đãi", "khuyến mãi"]
ALPHABET = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def fetch_single_suggest(query: str, hl: str = "vi", gl: str = "vn") -> List[str]:
    """Gửi 1 request đến Google Suggest API và bóc tách danh sách từ khóa"""
    params = urllib.parse.urlencode({
        "client": "firefox",
        "hl": hl,
        "gl": gl,
        "q": query
    })
    url = f"https://suggestqueries.google.com/complete/search?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8", errors="ignore"))
            # Google Suggest format: [query, [suggestions...], ...]
            if len(data) >= 2 and isinstance(data[1], list):
                return [s.strip().lower() for s in data[1] if isinstance(s, str)]
    except Exception as e:
        # Im lặng vượt qua khi gặp lỗi mạng tạm thời
        pass
    return []

def expand_keyword_comprehensive(seed: str, depth: str = "medium", delay: float = 0.2) -> Dict[str, any]:
    """
    Mở rộng từ khóa đa chiều:
    - depth 'fast': Chỉ lấy suggestions trực tiếp và một vài modifier chính (~20-40 KWs)
    - depth 'medium': Trực tiếp + Questions + Commercial + Top 10 ký tự a-z (~60-120 KWs)
    - depth 'deep': Trực tiếp + Questions + Commercial + Full 26 ký tự a-z (~150-300+ KWs)
    """
    seed_clean = seed.strip().lower()
    discovered: Set[str] = set()
    category_map = {
        "direct": [],
        "questions": [],
        "commercial": [],
        "alphabet": []
    }

    # 1. Direct Suggestions
    directs = fetch_single_suggest(seed_clean)
    for kw in directs:
        if kw not in discovered and kw != seed_clean:
            discovered.add(kw)
            category_map["direct"].append(kw)
    time.sleep(delay)

    # 2. Questions & How-to Expansion
    for p in QUESTION_PREFIXES:
        sub_query = f"{p} {seed_clean}"
        res = fetch_single_suggest(sub_query)
        for kw in res:
            if kw not in discovered:
                discovered.add(kw)
                category_map["questions"].append(kw)
        time.sleep(delay)

    for s in QUESTION_SUFFIXES:
        sub_query = f"{seed_clean} {s}"
        res = fetch_single_suggest(sub_query)
        for kw in res:
            if kw not in discovered:
                discovered.add(kw)
                category_map["questions"].append(kw)
        time.sleep(delay)

    # 3. Commercial Modifiers
    for c in COMMERCIAL_MODIFIERS:
        sub_query = f"{seed_clean} {c}"
        res = fetch_single_suggest(sub_query)
        for kw in res:
            if kw not in discovered:
                discovered.add(kw)
                category_map["commercial"].append(kw)
        time.sleep(delay)

    # 4. Alphabet Expansion (a-z)
    alpha_pool = ALPHABET if depth == "deep" else ALPHABET[:8] if depth == "medium" else []
    for char in alpha_pool:
        sub_query = f"{seed_clean} {char}"
        res = fetch_single_suggest(sub_query)
        for kw in res:
            if kw not in discovered:
                discovered.add(kw)
                category_map["alphabet"].append(kw)
        time.sleep(delay)

    all_keywords = sorted(list(discovered))
    
    return {
        "seed_keyword": seed,
        "total_discovered": len(all_keywords),
        "categorized": category_map,
        "all_keywords": all_keywords
    }

def main():
    if len(sys.argv) < 2:
        print("Cách dùng:")
        print("  python3 scripts/google_suggest_expander.py \"tỷ giá vcb\" [fast|medium|deep]")
        print("Ví dụ:")
        print("  python3 scripts/google_suggest_expander.py \"giá vàng sjc\" fast")
        sys.exit(1)

    seed_keyword = sys.argv[1]
    depth = sys.argv[2] if len(sys.argv) > 2 else "medium"

    print(f"=== ĐANG MỞ RỘNG TỪ KHÓA TỪ GOOGLE SUGGEST: '{seed_keyword}' (Depth: {depth}) ===")
    start_time = time.time()
    result = expand_keyword_comprehensive(seed_keyword, depth=depth)
    elapsed = round(time.time() - start_time, 2)

    print(f"\n[HOÀN TẤT TRONG {elapsed}s] Tổng cộng tìm thấy: {result['total_discovered']} từ khóa đề xuất từ người dùng thật:")
    
    print(f"\n1. Gợi ý trực tiếp ({len(result['categorized']['direct'])} KWs):")
    for kw in result['categorized']['direct'][:8]:
        print(f"   • {kw}")
        
    print(f"\n2. Câu hỏi & Hướng dẫn tra cứu ({len(result['categorized']['questions'])} KWs):")
    for kw in result['categorized']['questions'][:8]:
        print(f"   • {kw}")

    print(f"\n3. Ý định giao dịch & Thương mại ({len(result['categorized']['commercial'])} KWs):")
    for kw in result['categorized']['commercial'][:8]:
        print(f"   • {kw}")

    print(f"\n4. Mở rộng ký tự A-Z ({len(result['categorized']['alphabet'])} KWs):")
    for kw in result['categorized']['alphabet'][:8]:
        print(f"   • {kw}")

    # Xuất ra JSON snapshot nếu chạy từ terminal
    out_dir = os.path.join(os.path.dirname(__file__), "..", "07_REPORTS", "data", "suggestions")
    os.makedirs(out_dir, exist_ok=True)
    slug = urllib.parse.quote_plus(seed_keyword.replace(" ", "-"))
    out_file = os.path.join(out_dir, f"{slug}.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nĐã lưu snapshot JSON tại: {out_file}")

if __name__ == "__main__":
    main()
