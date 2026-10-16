#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SERP COMPETITOR ANALYZER ENGINE (Single Intent & Keyword Analysis)
Công cụ cào và phân tích đối thủ cạnh tranh theo một Intent tìm kiếm:
1. Thu thập Top 5-10 kết quả tìm kiếm tự nhiên (Organic SERP Results).
2. Cào sâu On-page của Top 3-5 đối thủ dẫn đầu (Title, H1, H2, H3, Word Count, Schemas).
3. Phân tích Khoảng trống nội dung (Competitor Content Gaps).
4. Thiết lập Chiến lược vượt mặt đối thủ cho MoMo Web Platform (Winning Blueprint).
"""

import sys
import os
import re
import json
import time
import ssl
import argparse
import urllib.request
import urllib.parse
from collections import Counter
import lxml.html

# Bỏ qua kiểm tra chứng chỉ SSL cho các cổng thông tin Việt Nam
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPORTS_DIR = os.path.join(BASE_DIR, "07_REPORTS", "competitors")
DATA_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data", "competitors")

USER_AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'
]

STOPWORDS = {
    'và', 'là', 'của', 'ở', 'tại', 'cho', 'với', 'trong', 'các', 'những',
    'được', 'có', 'ra', 'khi', 'về', 'này', 'đó', 'từ', 'theo', 'như',
    'để', 'lại', 'thì', 'người', 'cái', 'làm', 'hay', 'bao', 'nhiêu',
    'gì', 'sao', 'nao', 'nào', 'mấy', 'một', 'hai', 'ba', 'bốn', 'năm'
}

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

class SERPFetcher:
    """Thu thập kết quả tìm kiếm tự nhiên từ SERP"""
    @classmethod
    def fetch_serp_results(cls, query: str, limit: int = 5) -> list:
        print(f"Đang truy vấn bảng xếp hạng tìm kiếm cho: '{query}'...")
        headers = {
            'User-Agent': USER_AGENTS[0],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        # Sử dụng DuckDuckGo HTML Engine vì ổn định, không chặn IP và chuẩn kết quả tiếng Việt
        data = urllib.parse.urlencode({'q': query, 'kl': 'vn-vi'}).encode('utf-8')
        req = urllib.request.Request('https://html.duckduckgo.com/html/', data=data, headers=headers)
        
        serp_items = []
        try:
            with urllib.request.urlopen(req, timeout=12, context=ssl_ctx) as resp:
                html_content = resp.read().decode('utf-8', errors='ignore')
                tree = lxml.html.fromstring(html_content)
                
                for r in tree.xpath('//div[contains(@class, "result__body")]'):
                    a = r.xpath('.//a[contains(@class, "result__url")]')
                    snippet_el = r.xpath('.//a[contains(@class, "result__snippet")]')
                    title_el = r.xpath('.//h2[contains(@class, "result__title")]//a')
                    
                    if title_el and a:
                        raw_url = a[0].get('href', '').strip()
                        # Chuẩn hóa url từ DuckDuckGo redirect nếu có
                        if '/l/?kh=-1&uddg=' in raw_url:
                            parsed_target = urllib.parse.parse_qs(urllib.parse.urlparse(raw_url).query).get('uddg')
                            if parsed_target:
                                raw_url = parsed_target[0]
                        
                        # Bỏ qua các liên kết mạng xã hội hoặc chính trang momo.vn nếu muốn phân tích đối thủ ngoài
                        domain = urllib.parse.urlparse(raw_url).netloc.lower()
                        if any(ign in domain for ign in ['youtube.com', 'facebook.com', 'tiktok.com']):
                            continue
                            
                        title = clean_text(title_el[0].text_content())
                        snippet = clean_text(snippet_el[0].text_content()) if snippet_el else ""
                        
                        serp_items.append({
                            'rank': len(serp_items) + 1,
                            'title': title,
                            'url': raw_url,
                            'domain': domain,
                            'snippet': snippet
                        })
                        if len(serp_items) >= limit:
                            break
        except Exception as e:
            print(f"Lỗi khi cào SERP: {e}")
            
        return serp_items

class CompetitorPageParser:
    """Cào sâu cấu trúc On-Page của từng trang đối thủ"""
    @classmethod
    def parse_page(cls, item: dict) -> dict:
        url = item['url']
        print(f"Đang bóc tách On-page: [{item['rank']}] {item['domain']}...")
        headers = {
            'User-Agent': USER_AGENTS[item['rank'] % len(USER_AGENTS)],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'vi-VN,vi;q=0.9,en;q=0.8'
        }
        
        parsed_data = {
            'rank': item['rank'],
            'title': item['title'],
            'url': item['url'],
            'domain': item['domain'],
            'snippet': item['snippet'],
            'h1': [],
            'h2': [],
            'h3': [],
            'word_count': 0,
            'schemas': [],
            'has_table': False,
            'has_form_or_tool': False,
            'format_type': 'Article Guide'
        }
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10, context=ssl_ctx) as resp:
                html_content = resp.read().decode('utf-8', errors='ignore')
                tree = lxml.html.fromstring(html_content)
                
                # Trích xuất thẻ tiêu đề chính
                page_title = tree.xpath('//title/text()')
                if page_title:
                    parsed_data['page_title'] = clean_text(page_title[0])
                
                parsed_data['h1'] = [clean_text(h.text_content()) for h in tree.xpath('//h1') if clean_text(h.text_content())]
                
                # Trích xuất H2 và H3 (chỉ lấy các đề mục có ý nghĩa thực tế > 6 ký tự)
                h2_list = [clean_text(h.text_content()) for h in tree.xpath('//h2')]
                h2_filtered = [h for h in h2_list if len(h) >= 8 and not any(nav in h.lower() for nav in ['menu', 'tìm kiếm', 'liên hệ', 'bình luận', 'tin liên quan', 'bài viết khác'])]
                parsed_data['h2'] = h2_filtered[:12]
                
                h3_list = [clean_text(h.text_content()) for h in tree.xpath('//h3')]
                h3_filtered = [h for h in h3_list if len(h) >= 8 and not any(nav in h.lower() for nav in ['menu', 'đăng nhập', 'chia sẻ', 'xem thêm'])]
                parsed_data['h3'] = h3_filtered[:15]
                
                # Đếm số từ bài viết (tập trung vào body / article / main container)
                main_containers = tree.xpath('//article | //main | //div[contains(@class, "content") or contains(@class, "post") or contains(@class, "detail")]')
                target_container = main_containers[0] if main_containers else tree.xpath('//body')[0]
                text_content = target_container.text_content()
                words = re.findall(r'\b\w+\b', text_content)
                parsed_data['word_count'] = len(words)
                
                # Kiểm tra yếu tố tương tác (Table, Form, Tool)
                parsed_data['has_table'] = len(tree.xpath('//table')) > 0
                parsed_data['has_form_or_tool'] = len(tree.xpath('//form | //input | //select | //button[contains(@class, "calc") or contains(text(), "Tính")]')) > 0
                
                if parsed_data['has_form_or_tool']:
                    parsed_data['format_type'] = 'Interactive Tool / Calculator'
                elif parsed_data['has_table']:
                    parsed_data['format_type'] = 'Comparison & Data Table'
                elif any('hỏi' in h.lower() or 'faq' in h.lower() for h in parsed_data['h2']):
                    parsed_data['format_type'] = 'FAQ & In-depth Guide'
                
                # Trích xuất Schema JSON-LD
                for s in tree.xpath('//script[@type="application/ld+json"]'):
                    try:
                        s_text = s.text_content().strip()
                        if s_text:
                            data = json.loads(s_text)
                            if isinstance(data, dict):
                                stype = data.get('@type')
                                if stype:
                                    parsed_data['schemas'].append(stype)
                            elif isinstance(data, list):
                                for d in data:
                                    if isinstance(d, dict) and d.get('@type'):
                                        parsed_data['schemas'].append(d.get('@type'))
                    except Exception:
                        pass
                parsed_data['schemas'] = list(set(parsed_data['schemas']))
                
        except Exception as e:
            print(f"   ⚠️ Lỗi cào trang {url}: {e}")
            parsed_data['error'] = str(e)
            
        return parsed_data

class ContentGapAnalyzer:
    """Phân tích khoảng trống nội dung và thiết kế chiến lược vượt mặt đối thủ"""
    @classmethod
    def analyze_gap_and_strategy(cls, query: str, competitor_pages: list) -> dict:
        valid_pages = [p for p in competitor_pages if p.get('word_count', 0) > 0]
        if not valid_pages:
            return {'error': 'Không thu thập được trang đối thủ hợp lệ'}
            
        # 1. Tính toán Word Count Benchmark
        word_counts = [p['word_count'] for p in valid_pages]
        avg_word_count = round(sum(word_counts) / len(word_counts))
        max_word_count = max(word_counts)
        recommended_target_words = max(round(max_word_count * 1.15), round(avg_word_count * 1.3), 1800)
        
        # 2. Bóc tách chủ đề chung (Common Subtopics từ H2)
        all_h2s = []
        for p in valid_pages:
            all_h2s.extend(p.get('h2', []))
            
        # Thống kê từ khóa/thực thể xuất hiện nhiều nhất trong H2 đối thủ
        h2_token_counter = Counter()
        for h2 in all_h2s:
            tokens = [t.lower() for t in re.findall(r'\b\w{3,}\b', h2) if t.lower() not in STOPWORDS]
            h2_token_counter.update(tokens)
            
        top_entities = [t for t, _ in h2_token_counter.most_common(10)]
        
        # 3. Phân loại định dạng dẫn đầu (Dominant SERP Format)
        format_counts = Counter(p['format_type'] for p in valid_pages)
        dominant_format = format_counts.most_common(1)[0][0]
        
        # 4. Xác định khoảng trống (Missing Gaps) mà đối thủ thường thiếu
        has_calculator = any(p['has_form_or_tool'] for p in valid_pages)
        has_faq_schema = any('FAQPage' in p.get('schemas', []) for p in valid_pages)
        
        gaps_detected = []
        if not has_calculator:
            gaps_detected.append("Thiếu công cụ tính toán / tra cứu tương tác trực tiếp (đa số trang chỉ có bài viết chữ đơn thuần).")
        if not has_faq_schema:
            gaps_detected.append("Chưa tối ưu Schema FAQPage để chiếm đoạt vị trí Rich Snippets trên kết quả tìm kiếm.")
        gaps_detected.append("Thiếu cơ chế chuyển tiếp liền mạch sang ứng dụng tài chính / giao dịch tức thì (Web-to-App).")
        gaps_detected.append("Thiếu bảng đối soát so sánh trực quan đa chiều giữa các phương án.")
        
        # 5. Thiết lập Dàn ý Vượt Trội của MoMo (Beating Outline Blueprint)
        beating_outline = [
            f"## H2 1: Tổng quan & Định nghĩa chuẩn xác về {query}",
            f"## H2 2: Bảng so sánh chi tiết & Tiêu chí lựa chọn tối ưu nhất",
            f"## H2 3: Công cụ tính toán / Tra cứu trực tuyến trên Nền tảng Web MoMo (Vượt trội đối thủ)",
            f"### H3 3.1: Hướng dẫn các bước thao tác và tính toán kết quả theo thời gian thực",
            f"## H2 4: Hướng dẫn quy trình & Thủ tục thực hiện từng bước đơn giản",
            f"## H2 5: 5 Lưu ý quan trọng & Rủi ro thường gặp cần phòng tránh",
            f"## H2 6: Giải đáp thắc mắc thường gặp (FAQs chuẩn Schema)",
            f"## H2 7: Giải pháp liên kết và nhận quyền lợi tối đa qua Ứng dụng MoMo"
        ]
        
        return {
            'query': query,
            'competitors_crawled': len(valid_pages),
            'avg_word_count': avg_word_count,
            'max_word_count': max_word_count,
            'recommended_target_words': recommended_target_words,
            'dominant_format': dominant_format,
            'top_competitor_entities': top_entities,
            'gaps_detected': gaps_detected,
            'beating_outline': beating_outline
        }

def export_analysis_markdown(query: str, competitor_pages: list, analysis: dict) -> str:
    """Xuất bản báo cáo phân tích đối thủ định dạng Markdown chuẩn Tech/Product Lead"""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    out_file = os.path.join(REPORTS_DIR, f"{slugify(query)}-competitor-analysis.md")
    
    md = f"""# BÁO CÁO PHÂN TÍCH ĐỐI THỦ SERP & CHIẾN LƯỢC VƯỢT MẶT (COMPETITOR INTELLIGENCE)

- **Truy Vấn Tìm Kiếm (Intent Query):** `{query}`
- **Thời Gian Phân Tích:** {time.strftime('%Y-%m-%d %H:%M:%S')}
- **Số Lượng Đối Thủ Cào Chi Tiết:** {analysis.get('competitors_crawled', 0)} trang
- **Định Dạng Thống Trị SERP (Dominant Format):** `{analysis.get('dominant_format', 'N/A')}`
- **Chỉ Tiêu Độ Dài MoMo Khuyến Nghị:** `{analysis.get('recommended_target_words', 0):,} từ` (Vượt trội mức trung bình đối thủ: `{analysis.get('avg_word_count', 0):,} từ`)

---

## 1. BẢNG SO SÁNH CẤU TRÚC TOP ĐỐI THỦ DẪN ĐẦU (SERP LEADERBOARD)

| Thứ Hạng | Tên Miền (Domain) | Tiêu Đề Bài Viết (Title Tag) | Độ Dài (Words) | Định Dạng Trang | Cấu Trúc H2 Đáng Chú Ý | Schema JSON-LD |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- |
"""
    for p in competitor_pages:
        h2_preview = ", ".join([f"`{h[:35]}...`" if len(h) > 35 else f"`{h}`" for h in p.get('h2', [])[:3]]) if p.get('h2') else "Không có H2 rõ ràng"
        schemas_str = ", ".join(p.get('schemas', [])) if p.get('schemas') else "Trống"
        md += f"| Top {p['rank']} | `{p['domain']}` | {p['title']} | {p.get('word_count', 0):,} | {p.get('format_type', 'N/A')} | {h2_preview} | {schemas_str} |\n"

    md += """\n---

## 2. BÓC TÁCH CHI TIẾT CẤU TRÚC HEADING (H2/H3) TỪNG ĐỐI THỦ
"""
    for p in competitor_pages:
        md += f"""
### Top {p['rank']}: `{p['domain']}` - [{p['title']}]({p['url']})
- **Độ dài bài viết:** `{p.get('word_count', 0):,} từ`
- **H1:** `{p.get('h1', ['N/A'])[0] if p.get('h1') else 'N/A'}`
- **Dàn ý H2 đối thủ triển khai:**
"""
        if p.get('h2'):
            for h2 in p.get('h2', []):
                md += f"  - `{h2}`\n"
        else:
            md += "  - *(Không phát hiện cấu trúc H2 chuẩn)*\n"

    md += f"""\n---

## 3. PHÂN TÍCH KHOẢNG TRỐNG NỘI DUNG (CONTENT GAPS)

Qua đối soát cấu trúc On-Page của các đối thủ dẫn đầu, hệ thống phát hiện các điểm yếu và khoảng trống sau:

"""
    for idx, gap in enumerate(analysis.get('gaps_detected', []), 1):
        md += f"{idx}. **Khoảng trống {idx}:** {gap}\n"

    md += f"""
- **Các thực thể ngữ nghĩa trọng tâm đối thủ tập trung:** {", ".join([f"`{e}`" for e in analysis.get('top_competitor_entities', [])])}

---

## 4. CHIẾN LƯỢC VƯỢT MẶT ĐỐI THỦ CHO MOMO WEB PLATFORM (WINNING BLUEPRINT)

Để đưa trang MoMo Web Platform chiếm lĩnh vị trí **Top 1 Google** và **Trích dẫn ưu tiên trên Google AI Overviews**, bài viết bắt buộc phải tuân thủ quy chuẩn sau:

### A. Chỉ tiêu định lượng kỹ thuật:
- **Hạn mức độ dài bài viết:** Tối thiểu `{analysis.get('recommended_target_words', 2200):,} từ`.
- **Dữ liệu cấu trúc bắt buộc:** Nhúng đầy đủ `BreadcrumbList` và `FAQPage` Schema.
- **Điểm chạm chuyển đổi (UX Hook):** Bắt buộc tích hợp Widget tra cứu / tính toán trực tiếp trên Web kết hợp Deeplink chuyển đổi sang App MoMo.

### B. Dàn ý H2/H3 vượt trội (Beating Outline Blueprint):
"""
    for item in analysis.get('beating_outline', []):
        md += f"- {item}\n"

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"\nĐã xuất bản báo cáo phân tích đối thủ tại: {out_file}")
    return out_file

def main():
    parser = argparse.ArgumentParser(description="SERP Competitor Analyzer Engine (Single Intent & Keyword)")
    parser.add_argument("query", help="Từ khóa hoặc Intent tìm kiếm cần phân tích đối thủ")
    parser.add_argument("--limit", type=int, default=5, help="Số lượng đối thủ SERP cần cào sâu (Mặc định: 5)")
    parser.add_argument("--json", action="store_true", help="Xuất file JSON thô vào 07_REPORTS/data/competitors/")
    args = parser.parse_args()

    query = args.query.strip()
    print(f"\n=== KHỞI ĐỘNG PHÂN TÍCH ĐỐI THỦ SERP CHO TRUY VẤN: '{query}' ===\n")
    
    # Bước 1: Cào kết quả SERP
    serp_items = SERPFetcher.fetch_serp_results(query, limit=args.limit)
    if not serp_items:
        print("Không thể thu thập kết quả tìm kiếm. Vui lòng kiểm tra lại kết nối mạng hoặc thử lại.")
        sys.exit(1)
        
    print(f"Đã phát hiện Top {len(serp_items)} đối thủ trên bảng xếp hạng.")
    
    # Bước 2: Cào sâu On-Page từng đối thủ
    competitor_pages = []
    for item in serp_items:
        page_data = CompetitorPageParser.parse_page(item)
        competitor_pages.append(page_data)
        time.sleep(0.5) # Giãn cách an toàn
        
    # Bước 3: Phân tích khoảng trống nội dung & Chiến lược MoMo
    analysis = ContentGapAnalyzer.analyze_gap_and_strategy(query, competitor_pages)
    
    # Bước 4: Xuất báo cáo Markdown
    out_md = export_analysis_markdown(query, competitor_pages, analysis)
    
    # Bước 5: Lưu dữ liệu JSON (nếu có yêu cầu hoặc mặc định lưu SSOT)
    os.makedirs(DATA_DIR, exist_ok=True)
    json_path = os.path.join(DATA_DIR, f"{slugify(query)}.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'query': query,
            'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'analysis': analysis,
            'competitors': competitor_pages
        }, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu Snapshot dữ liệu đối thủ tại: {json_path}")
    
    print("\n=== HOÀN TẤT PHÂN TÍCH ĐỐI THỦ SERP ===")

if __name__ == '__main__':
    main()
