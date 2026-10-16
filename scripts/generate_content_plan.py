#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CONTENT PLAN GENERATOR ENGINE (V2 - BATCH & SHIELDED)
Quy chuẩn Lọc đa tín hiệu, Chống Cannibalization và Tự động sinh Content Plan chuẩn Product/Tech Lead
Hỗ trợ sinh đơn lẻ (1 file) hoặc sinh hàng loạt (toàn bộ phân khối / toàn bộ 188 Use Cases).
"""

import sys
import os
import glob
import csv
import re
import math
import json
import argparse
from collections import defaultdict, Counter

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INVENTORY_DIR = os.path.join(BASE_DIR, "05_HUBS", "inventory")
OUTPUT_DIR = os.path.join(BASE_DIR, "06_USE_CASE_MOMO", "content-plans")

sys.path.insert(0, BASE_DIR)
from scripts.lib.keyword_intelligence import (
    MultiSignalIntentClassifier,
    SemanticDomainFilter,
    SERPCannibalizationShield,
    StructuredSchemaGenerator,
    ContentBriefGenerator,
    InternalLinkingTopologyEngine,
    GEODirectAnswerGenerator,
    STOPWORDS,
    TELEX_FIXES
)

def clean_val(val):
    if not val:
        return ""
    val = val.strip()
    if val.startswith('="') and val.endswith('"'):
        return val[2:-1]
    return val

def normalize_text(text):
    text = text.lower().strip()
    for err, fix in TELEX_FIXES.items():
        text = text.replace(err, fix)
    text = re.sub(r'\s+', ' ', text)
    return text

def calculate_opportunity_score(volume, cpc, competition, intent):
    intent_weights = {
        'Transactional': 2.0,
        'Tool/Calculator': 1.8,
        'Commercial': 1.5,
        'Informational': 1.0,
        'Navigational': 0.7
    }
    weight = intent_weights.get(intent, 1.0)
    
    comp_val = competition.lower()
    comp_factor = 0.2
    if 'high' in comp_val:
        comp_factor = 0.8
    elif 'medium' in comp_val:
        comp_factor = 0.5
    elif 'low' in comp_val:
        comp_factor = 0.2
        
    vol_score = math.log10(volume + 1) if volume > 0 else 0
    cpc_bonus = min(cpc * 0.2, 0.5)
    score = vol_score * (1.2 - comp_factor) * weight * (1.0 + cpc_bonus)
    return round(score, 2)

def classify_priority(volume, competition, intent):
    comp_val = competition.lower()
    is_high_comp = 'high' in comp_val or 'medium' in comp_val
    if (volume >= 2000 and not is_high_comp) or (intent in ['Tool/Calculator', 'Transactional'] and volume >= 500):
        return 'P0'
    elif volume >= 1000 or intent == 'Commercial':
        return 'P1'
    else:
        return 'P2'

def determine_funnel(intent):
    if intent in ['Tool/Calculator', 'Transactional']:
        return 'BOFU'
    elif intent == 'Commercial':
        return 'MOFU'
    return 'TOFU'

def recommend_format(intent, is_pillar=False):
    if is_pillar:
        return 'Pillar Hub Page + Interactive Widget'
    if intent == 'Tool/Calculator':
        return 'Interactive Calculator / Lookup Tool'
    elif intent == 'Commercial':
        return 'Comparison Table & Evaluation'
    elif intent == 'Transactional':
        return 'Step-by-step How-to & Action Form'
    return 'Educational Guide & FAQ'

def recommend_cta_hook(usecase_slug, intent):
    slug = usecase_slug.lower()
    if 'tiet-kiem' in slug:
        if intent in ['Tool/Calculator', 'Transactional']:
            return "Widget tính lãi nhận được thực tế -> Deeplink mở Túi Thần Tài / Tiết kiệm đối tác MoMo nhận lãi mỗi ngày"
        return "Bảng so sánh lợi suất cố định vs lợi suất linh hoạt Túi Thần Tài MoMo"
    elif 'bien-so' in slug or 'phat-nguoi' in slug:
        if intent in ['Tool/Calculator', 'Transactional']:
            return "Form tra cứu trực tiếp trên Web -> Nút nộp phạt / Nạp tài khoản giao thông MoMo"
        return "Banner tiện ích giao thông toàn diện trên MoMo App"
    elif 'vay' in slug:
        return "Mô phỏng khoản vay hàng tháng -> Deeplink xét duyệt hồ sơ online trong 3 phút"
    elif 'bao-hiem' in slug:
        return "Form tính phí bảo hiểm tức thì -> Xuất chứng nhận điện tử qua MoMo"
    return "Tích hợp Widget tương tác trên Web -> Deeplink mở MoMo App kích hoạt dịch vụ"

def build_content_plan(csv_path):
    usecase_slug = os.path.splitext(os.path.basename(csv_path))[0]
    usecase_name = usecase_slug.replace('-', ' ').replace('_', ' ').title()
    sector = os.path.basename(os.path.dirname(csv_path))
    
    raw_keywords = []
    outliers_filtered = 0
    
    with open(csv_path, 'r', encoding='utf-8-sig', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            kw_raw = row.get('Keyword', '')
            if not kw_raw:
                continue
            kw = normalize_text(clean_val(kw_raw))
            
            is_out, _ = SemanticDomainFilter.is_outlier(kw, sector, usecase_slug)
            if is_out:
                outliers_filtered += 1
                continue
                
            try:
                vol = int(clean_val(row.get('Volume', '0')) or 0)
            except ValueError:
                vol = 0
            try:
                cpc = float(clean_val(row.get('CPC', '0')) or 0.0)
            except ValueError:
                cpc = 0.0
            comp = clean_val(row.get('PPC Competition', 'Low'))
            
            intent_res = MultiSignalIntentClassifier.classify(kw)
            intent = intent_res['intent']
            score = calculate_opportunity_score(vol, cpc, comp, intent)
            priority = classify_priority(vol, comp, intent)
            
            raw_keywords.append({
                'keyword': kw,
                'volume': vol,
                'cpc': cpc,
                'competition': comp,
                'intent': intent,
                'intent_confidence': intent_res['confidence'],
                'score': score,
                'priority': priority
            })
            
    if not raw_keywords:
        return None, "Không tìm thấy từ khóa hợp lệ sau khi lọc.", []
        
    canonical_topics, merge_log = SERPCannibalizationShield.cluster_and_shield(raw_keywords)
    canonical_topics.sort(key=lambda x: (x['total_cluster_volume'], x['opportunity_score']), reverse=True)
    
    pillar_item = canonical_topics[0]
    pillar_slug = f"/{usecase_slug}/"
    pillar_title = f"Cẩm Nang & Bảng Tra Cứu {usecase_name} Toàn Diện"
    pillar_plan = {
        'slug': pillar_slug,
        'title': pillar_title,
        'primary_kw': pillar_item['keyword'],
        'secondary_kws': pillar_item.get('secondary_keywords', [])[:5],
        'volume': pillar_item['total_cluster_volume'],
        'intent': pillar_item['intent'],
        'format': recommend_format(pillar_item['intent'], is_pillar=True),
        'funnel': 'TOFU',
        'priority': 'P0',
        'cta_hook': recommend_cta_hook(usecase_slug, pillar_item['intent']),
        'shielded_count': len(pillar_item.get('secondary_keywords', []))
    }
    
    cluster_buckets = defaultdict(list)
    for topic in canonical_topics[1:]:
        kw = topic['keyword']
        intent = topic['intent']
        if intent == 'Tool/Calculator' or any(w in kw for w in ['tính', 'bao nhiêu tiền', 'lãi bao nhiêu', 'cách tính']):
            cluster_buckets['calculator'].append(topic)
        elif any(w in kw for w in ['online', 'trực tuyến', 'an toàn', 'lừa đảo', 'bảo mật']):
            cluster_buckets['trust_online'].append(topic)
        elif intent == 'Commercial' or any(w in kw for w in ['so sánh', 'nào tốt', 'nên', 'cao nhất', 'ưu đãi']):
            cluster_buckets['comparison'].append(topic)
        elif intent == 'Transactional' or any(w in kw for w in ['thủ tục', 'quy trình', 'hướng dẫn', 'điều kiện', 'giấy tờ', 'rút tiền']):
            cluster_buckets['how_to'].append(topic)
        else:
            cluster_buckets['general'].append(topic)
            
    cluster_pages = []
    
    if cluster_buckets['calculator']:
        c_kws = cluster_buckets['calculator']
        c_leader = c_kws[0]
        sec_list = c_leader.get('secondary_keywords', []) + [x['keyword'] for x in c_kws[1:4]]
        cluster_pages.append({
            'slug': f"/{usecase_slug}/cong-cu-tinh-toan/",
            'title': f"Công Cụ Tính {usecase_name} Trực Tuyến & Bảng Tính Chi Tiết",
            'primary_kw': c_leader['keyword'],
            'secondary_kws': sec_list[:5],
            'volume': sum(x['total_cluster_volume'] for x in c_kws[:5]),
            'intent': 'Tool/Calculator',
            'format': 'Interactive Calculator / Lookup Tool',
            'funnel': 'BOFU',
            'priority': 'P0',
            'cta_hook': recommend_cta_hook(usecase_slug, 'Tool/Calculator'),
            'shielded_count': len(sec_list)
        })
        
    if cluster_buckets['comparison']:
        c_kws = cluster_buckets['comparison']
        c_leader = c_kws[0]
        sec_list = c_leader.get('secondary_keywords', []) + [x['keyword'] for x in c_kws[1:4]]
        cluster_pages.append({
            'slug': f"/{usecase_slug}/so-sanh-danh-gia/",
            'title': f"So Sánh & Đánh Giá {usecase_name}: Lựa Chọn Nào Tốt Nhất?",
            'primary_kw': c_leader['keyword'],
            'secondary_kws': sec_list[:5],
            'volume': sum(x['total_cluster_volume'] for x in c_kws[:5]),
            'intent': 'Commercial',
            'format': 'Comparison Table & Evaluation',
            'funnel': 'MOFU',
            'priority': 'P0',
            'cta_hook': recommend_cta_hook(usecase_slug, 'Commercial'),
            'shielded_count': len(sec_list)
        })
        
    if cluster_buckets['trust_online']:
        c_kws = cluster_buckets['trust_online']
        c_leader = c_kws[0]
        sec_list = c_leader.get('secondary_keywords', []) + [x['keyword'] for x in c_kws[1:4]]
        cluster_pages.append({
            'slug': f"/{usecase_slug}/an-toan-bao-mat/",
            'title': f"{usecase_name} Online Có An Toàn Không? Rủi Ro & Biện Pháp Bảo Vệ",
            'primary_kw': c_leader['keyword'],
            'secondary_kws': sec_list[:5],
            'volume': sum(x['total_cluster_volume'] for x in c_kws[:5]),
            'intent': 'Informational',
            'format': 'Trust & Security Guide',
            'funnel': 'MOFU',
            'priority': 'P1',
            'cta_hook': recommend_cta_hook(usecase_slug, 'Informational'),
            'shielded_count': len(sec_list)
        })
        
    if cluster_buckets['how_to']:
        c_kws = cluster_buckets['how_to']
        c_leader = c_kws[0]
        sec_list = c_leader.get('secondary_keywords', []) + [x['keyword'] for x in c_kws[1:4]]
        cluster_pages.append({
            'slug': f"/{usecase_slug}/thu-tuc-huong-dan/",
            'title': f"Hướng Dẫn Thủ Tục {usecase_name}: Hồ Sơ, Quy Trình & Lưu Ý",
            'primary_kw': c_leader['keyword'],
            'secondary_kws': sec_list[:5],
            'volume': sum(x['total_cluster_volume'] for x in c_kws[:5]),
            'intent': 'Transactional',
            'format': 'Step-by-step How-to & Action Form',
            'funnel': 'MOFU',
            'priority': 'P1',
            'cta_hook': recommend_cta_hook(usecase_slug, 'Transactional'),
            'shielded_count': len(sec_list)
        })
        
    if cluster_buckets['general']:
        c_kws = cluster_buckets['general']
        c_leader = c_kws[0]
        sec_list = c_leader.get('secondary_keywords', []) + [x['keyword'] for x in c_kws[1:4]]
        cluster_pages.append({
            'slug': f"/{usecase_slug}/kien-thuc-chuyen-sau/",
            'title': f"Tổng Hợp Kinh Nghiệm & Giải Đáp Thắc Mắc Về {usecase_name}",
            'primary_kw': c_leader['keyword'],
            'secondary_kws': sec_list[:5],
            'volume': sum(x['total_cluster_volume'] for x in c_kws[:5]),
            'intent': 'Informational',
            'format': 'Comprehensive Guide & FAQ',
            'funnel': 'TOFU',
            'priority': 'P2',
            'cta_hook': recommend_cta_hook(usecase_slug, 'Informational'),
            'shielded_count': len(sec_list)
        })
        
    full_plan = [pillar_plan] + cluster_pages
    stats = {
        'total_raw_keywords': len(raw_keywords) + outliers_filtered,
        'outliers_pruned': outliers_filtered,
        'canonical_topics_count': len(canonical_topics),
        'cannibalized_merged': len(merge_log),
        'total_cluster_volume': sum(p['volume'] for p in full_plan),
        'sector': sector
    }
    return full_plan, stats, merge_log

def export_content_plan_markdown(plan, stats, merge_log, usecase_slug, sector=None):
    usecase_name = usecase_slug.replace('-', ' ').replace('_', ' ').title()
    target_dir = os.path.join(OUTPUT_DIR, sector) if sector else OUTPUT_DIR
    os.makedirs(target_dir, exist_ok=True)
    out_file = os.path.join(target_dir, f"{usecase_slug}-content-plan.md")
    
    md = f"""# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - USE CASE: {usecase_name.upper()}

- **Use Case:** {usecase_name}
- **Phân Khối Ngành:** {sector or 'General'}
- **URL Pillar Hub:** `{plan[0]['slug']}`
- **Tổng từ khóa thô ban đầu:** {stats['total_raw_keywords']:,} từ khóa
- **Từ khóa nhiễu bị loại bỏ:** {stats['outliers_pruned']:,} từ khóa
- **Từ khóa trùng Intent được gom cụm (Shielded):** {stats['cannibalized_merged']:,} từ khóa
- **Số lượng URLs phân bổ:** {len(plan)} URLs (1 Pillar Hub + {len(plan)-1} Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Ưu Tiên | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
"""
    for idx, p in enumerate(plan, 1):
        sec_str = ", ".join(p['secondary_kws'][:3]) if p['secondary_kws'] else "Đã bao hàm toàn cụm"
        md += f"| {idx} | `{p['slug']}` | {p['title']} | `{p['primary_kw']}` | {sec_str} | {p['volume']:,} | `{p['intent']}` | {p['format']} | `{p['funnel']}` | `{p['priority']}` | {p['cta_hook']} |\n"

    md += """\n---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |
"""
    for idx, m in enumerate(merge_log[:15], 1):
        md += f"| {idx} | `{m['merged_keyword']}` | `{m['canonical_primary']}` | {m['reason']} | {m['volume_added']:,} |\n"

    md += """\n---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`""" + plan[0]['slug'] + """`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.

---

## 4. CONTENT BRIEF & DÀN Ý H2/H3 ENTITY CHECKLIST CHO TỪNG BÀI

Dưới đây là cấu trúc dàn ý chuẩn E-E-A-T và chỉ tiêu dung lượng bài viết để đội ngũ nội dung triển khai:
"""
    for idx, p in enumerate(plan, 1):
        wc = ContentBriefGenerator.estimate_word_count(p['format'], p['intent'], p['volume'])
        outline = ContentBriefGenerator.generate_outline_checklist(p, usecase_name)
        outline_str = "\n".join([f"   - {item}" for item in outline])
        md += f"""
### Bài {idx}: `{p['title']}`
- **URL Slug:** `{p['slug']}`
- **Chỉ tiêu độ dài:** `{wc['min_words']:,} - {wc['target_words']:,} từ` (Cấp bậc: `{wc['tier']}`)
- **Primary Keyword:** `{p['primary_kw']}`
- **Secondary Synonyms:** {", ".join(p['secondary_kws'][:4]) if p['secondary_kws'] else "Bao hàm ngữ nghĩa"}
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
{outline_str}
"""

    # 5. Sinh Schema JSON-LD mẫu cho Pillar Hub
    faq_qa = []
    for p in plan[1:4]:
        faq_qa.append((
            f"{p['title']}?",
            f"Thông tin chi tiết về {p['primary_kw']} được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
        ))
    faq_schema = StructuredSchemaGenerator.generate_faq_jsonld(usecase_name, faq_qa)
    breadcrumb_schema = StructuredSchemaGenerator.generate_breadcrumb_jsonld(sector or "Dịch Vụ", usecase_name, plan[0]['slug'])

    md += f"""\n---

## 5. DỮ LIỆU CẤU TRÚC JSON-LD (STRUCTURED DATA SCHEMA) CHO WEB DEV

Đội ngũ Frontend tại `hubs-momo` có thể sao chép trực tiếp 2 khối Schema này vào thẻ `<script type="application/ld+json">` của trang:

### A. BreadcrumbList Schema:
```json
{json.dumps(breadcrumb_schema, ensure_ascii=False, indent=2)}
```

### B. FAQPage Schema:
```json
{json.dumps(faq_schema, ensure_ascii=False, indent=2)}
```
"""

    # 6. Mạng lưới liên kết nội bộ phân tầng (Internal Linking & Silo Matrix)
    summary_path = os.path.join(BASE_DIR, "07_REPORTS", "data", "inventory_clusters_summary.json")
    all_usecases_cache = []
    if os.path.exists(summary_path):
        try:
            with open(summary_path, 'r', encoding='utf-8') as f:
                all_usecases_cache = json.load(f).get('usecases', [])
        except Exception:
            pass

    cur_uc_mock = {
        'id': usecase_slug,
        'name': usecase_name,
        'sector': sector or 'other',
        'top_opportunities': [{'keyword': p['primary_kw']} for p in plan]
    }
    silo_matrix = InternalLinkingTopologyEngine.build_silo_matrix(cur_uc_mock, all_usecases_cache)

    md += f"""\n---

## 6. KIẾN TRÚC LIÊN KẾT NỘI BỘ (INTERNAL LINKING & SILO MATRIX)

Phân tầng dòng chảy uy tín trang (PageRank) và định vị chuyên môn chủ đề (Topic Authority):

### A. Parent Hub Pillar:
- **Trang Cột Trụ Cấp 1:** `[{silo_matrix['parent_hub']['title']}]({silo_matrix['parent_hub']['url']})`
- **Anchor Text Mỏ Neo:** `"{silo_matrix['parent_hub']['anchor']}"`

### B. Liên kết ngang cùng ngành (Peer In-Silo):
| Thứ tự | Use Case Bổ Trợ | Đường Dẫn Khuyến Nghị | Anchor Text Tự Nhiên | Độ Tương Đồng | Search Volume |
| :---: | :--- | :--- | :--- | :---: | :---: |
"""
    for idx, peer in enumerate(silo_matrix['peer_in_silo'], 1):
        md += f"| {idx} | `{peer['target_name']}` | `{peer['target_url']}` | `{peer['suggested_anchor']}` | `{peer['similarity_score']}` | {peer['volume']:,} |\n"

    md += """\n### C. Cầu nối liên kết xuyên ngành (Cross-Silo Bridges):
| Thứ tự | Use Case Đích | Phân Khối Ngành | Đường Dẫn Khuyến Nghị | Anchor Text Móc Nối | Search Volume |
| :---: | :--- | :--- | :--- | :--- | :---: |
"""
    for idx, bridge in enumerate(silo_matrix['cross_silo_bridges'], 1):
        md += f"| {idx} | `{bridge['target_name']}` | `{bridge['target_sector']}` | `{bridge['target_url']}` | `{bridge['suggested_anchor']}` | {bridge['volume']:,} |\n"

    # 7. Tối ưu hóa Tìm kiếm Tạo sinh (GEO & AI Direct Answers)
    primary_kw = plan[0]['primary_kw']
    primary_intent = plan[0]['intent']
    geo_snippet = GEODirectAnswerGenerator.generate_direct_answer_snippet(usecase_name, primary_kw, primary_intent, sector or 'other')
    entity_facts = GEODirectAnswerGenerator.generate_entity_factsheet(usecase_name, sector or 'other', primary_intent)

    md += f"""\n---

## 7. TỐI ƯU HÓA TÌM KIẾM TẠO SINH (GEO & AI DIRECT ANSWERS)

Cung cấp sẵn khối thông tin trích dẫn phục vụ trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini:

### A. Đoạn trích dẫn trực tiếp (Direct Answer Snippet - 40-60 từ):
> "{geo_snippet}"

### B. Bảng thuộc tính thực thể (Entity Knowledge Graph Factsheet):
| Thuộc Tính Thực Thể | Giá Trị Chuẩn Hóa |
| :--- | :--- |
"""
    for fact in entity_facts:
        md += f"| {fact['entity_field']} | {fact['value']} |\n"

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(md)
    return out_file

def process_file(csv_path):
    usecase_slug = os.path.splitext(os.path.basename(csv_path))[0]
    sector = os.path.basename(os.path.dirname(csv_path))
    plan, stats, merge_log = build_content_plan(csv_path)
    if not plan:
        return None, stats
    out_file = export_content_plan_markdown(plan, stats, merge_log, usecase_slug, sector)
    return out_file, stats

def main():
    parser = argparse.ArgumentParser(description="Content Plan Generator Engine (Batch & Shielded)")
    parser.add_argument("target", nargs="?", help="Tên file CSV cụ thể hoặc slug của use case")
    parser.add_argument("--all", action="store_true", help="Sinh Content Plan cho toàn bộ 188 Use Cases")
    parser.add_argument("--sector", help="Chỉ sinh Content Plan cho một phân khối ngành cụ thể (ví dụ: Financial, vehicle-hub, insurtech)")
    args = parser.parse_args()

    if args.all:
        print(f"Bắt đầu sinh hàng loạt Content Plan cho toàn bộ 188 Use Cases tại: {INVENTORY_DIR}")
        csv_files = sorted(glob.glob(os.path.join(INVENTORY_DIR, "**", "*.csv"), recursive=True))
        success_count = 0
        total_vol = 0
        for idx, f in enumerate(csv_files, 1):
            out_file, stats = process_file(f)
            if out_file:
                success_count += 1
                total_vol += stats['total_cluster_volume']
                print(f"[{idx}/{len(csv_files)}] {os.path.basename(out_file)}: {stats['canonical_topics_count']} topics | Gom {stats['cannibalized_merged']:,} cannibalized | Vol {stats['total_cluster_volume']:,}")
        print(f"\nHoàn tất! Đã xuất bản {success_count}/{len(csv_files)} Content Plans tại: {OUTPUT_DIR}")
        build_index_markdown()
        return

    if args.sector:
        sec_dir = os.path.join(INVENTORY_DIR, args.sector)
        if not os.path.exists(sec_dir):
            print(f"Lỗi: Không tìm thấy phân khối '{args.sector}'")
            sys.exit(1)
        csv_files = sorted(glob.glob(os.path.join(sec_dir, "*.csv")))
        print(f"Bắt đầu sinh Content Plan cho phân khối '{args.sector}' ({len(csv_files)} use cases)...")
        for idx, f in enumerate(csv_files, 1):
            out_file, stats = process_file(f)
            if out_file:
                print(f"[{idx}/{len(csv_files)}] {os.path.basename(out_file)} - Topics: {stats['canonical_topics_count']} - Vol: {stats['total_cluster_volume']:,}")
        build_index_markdown()
        return

    if not args.target:
        parser.print_help()
        sys.exit(1)

    target = args.target
    csv_file = target
    if not os.path.exists(csv_file):
        matches = glob.glob(os.path.join(INVENTORY_DIR, "**", f"*{target}*.csv"), recursive=True)
        if matches:
            csv_file = matches[0]
        else:
            print(f"Lỗi: Không tìm thấy file từ khóa cho '{target}'")
            sys.exit(1)

    print(f"Đang xử lý tệp đơn lẻ: {csv_file}")
    out_file, stats = process_file(csv_file)
    if out_file:
        print(f"Đã xuất bản thành công Content Plan tại: {out_file}")
        print(f"- Tổng từ khóa sạch: {stats['total_raw_keywords'] - stats['outliers_pruned']:,} (Loại bỏ {stats['outliers_pruned']} nhiễu)")
        print(f"- Số từ khóa gom cụm chống ăn thịt: {stats['cannibalized_merged']:,}")
        print(f"- Tổng volume cụm được bảo toàn: {stats['total_cluster_volume']:,} lượt/tháng")
        build_index_markdown()

def build_index_markdown():
    """
    Tự động quét toàn bộ các file Content Plan Markdown trong OUTPUT_DIR
    và tạo tệp mục lục điều hướng trung tâm 06_USE_CASE_MOMO/content-plans/INDEX.md
    """
    plan_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "**", "*.md"), recursive=True))
    plan_files = [f for f in plan_files if not f.endswith("INDEX.md")]
    
    entries = []
    for pf in plan_files:
        rel_path = os.path.relpath(pf, OUTPUT_DIR)
        parts = rel_path.split(os.sep)
        sector = parts[0] if len(parts) > 1 else "Root"
        slug = os.path.splitext(os.path.basename(pf))[0]
        
        total_vol = 0
        canonical_count = 0
        usecase_title = ""
        sector_name = sector
        with open(pf, 'r', encoding='utf-8') as f:
            for line in f:
                if "**Use Case:**" in line:
                    usecase_title = line.split("**Use Case:**")[-1].strip()
                elif "**Phân Khối Ngành:**" in line:
                    sector_name = line.split("**Phân Khối Ngành:**")[-1].strip()
                elif "**Số lượng URLs phân bổ:**" in line:
                    m = re.search(r'(\d+)', line)
                    if m:
                        canonical_count = int(m.group(1))
                elif line.strip().startswith('|') and '|' in line:
                    cols = [c.strip() for c in line.split('|')]
                    if len(cols) >= 8:
                        val = cols[6].replace(',', '').strip()
                        if val.isdigit():
                            total_vol += int(val)
        entries.append({
            'sector': sector_name,
            'slug': slug.replace('-content-plan', ''),
            'rel_path': rel_path,
            'total_vol': total_vol,
            'canonical_count': canonical_count,
            'title': usecase_title or slug
        })

    entries.sort(key=lambda x: (x['sector'], -x['total_vol']))
    
    idx_content = f"""# MỤC LỤC CHIẾN LƯỢC NỘI DUNG TOÀN DIỆN (CONTENT PLANS DIRECTORY)

Trang mục lục tra cứu toàn bộ các bản kế hoạch nội dung (Content Plans) của MoMo Web Platform. Được tạo lập và đồng bộ tự động từ kho dữ liệu Semantic Keyword Inventory.

- **Tổng số Content Plans đã xuất bản:** {len(entries)} bản kế hoạch
- **Tổng dung lượng tìm kiếm phục vụ:** {sum(e['total_vol'] for e in entries):,} lượt/tháng

---

## DANH SÁCH CHI TIẾT THEO PHÂN KHỐI NGÀNH

| Phân Khối | Use Case / Dịch Vụ | Số Lượng Topic Clusters | Dung Lượng Tìm Kiếm | Liên Kết Chi Tiết |
| :--- | :--- | :---: | :---: | :--- |
"""
    for e in entries:
        idx_content += f"| `{e['sector']}` | **{e['slug']}** | {e['canonical_count']} topics | {e['total_vol']:,} | [{e['slug']}.md]({e['rel_path']}) |\n"

    index_path = os.path.join(OUTPUT_DIR, "INDEX.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(idx_content)
    print(f"Đã cập nhật tệp Mục Lục Trung Tâm tại: {index_path}")

if __name__ == '__main__':
    main()

