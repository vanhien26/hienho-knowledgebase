#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KEYWORD CLUSTER ENGINE
Công cụ xử lý, lọc ngữ nghĩa (Semantic Filtering), gom cụm (Clustering),
thiết lập Topic Cluster và xếp hạng từ khóa tiềm năng (Opportunity Score)
từ kho dữ liệu thô trong 05_HUBS/inventory/.
"""

import sys
import os
import csv
import re
import math
import json
from collections import defaultdict

def clean_val(val):
    if not val:
        return ""
    val = val.strip()
    if val.startswith('="') and val.endswith('"'):
        return val[2:-1]
    return val

def normalize_text(text):
    text = text.lower().strip()
    # Chuẩn hóa lỗi gõ Telex cơ bản thường gặp trong keyword research tool
    telex_fixes = {
        'ddaaus': 'đấu',
        'ddieenj': 'điện',
        'ddoof': 'đồ',
        'ddoongf': 'đồng',
        'ngan hang': 'ngân hàng',
        'tiet kiem': 'tiết kiệm',
        'lai suat': 'lãi suất',
        'bien so': 'biển số',
    }
    for err, fix in telex_fixes.items():
        text = text.replace(err, fix)
    # Xóa khoảng trắng thừa
    text = re.sub(r'\s+', ' ', text)
    return text

def detect_intent(keyword):
    kw = keyword.lower()
    # Transactional / Conversion
    if any(w in kw for w in ['mở sổ', 'đăng ký', 'mua', 'nạp', 'thanh toán', 'đặt', 'vay ngay', 'làm thẻ', 'đổi biển']):
        return 'Transactional'
    # Commercial / Comparison
    if any(w in kw for w in ['nên', 'tốt nhất', 'so sánh', 'nào tốt', 'lãi suất', 'bảng giá', 'giá bao nhiêu', 'chi phí', 'ưu đãi', 'đánh giá', 'review']):
        return 'Commercial'
    # Tool / Calculator / Lookup
    if any(w in kw for w in ['tính', 'công cụ tính', 'tra cứu', 'kiểm tra', 'check', 'bao nhiêu tiền', 'lãi bao nhiêu']):
        return 'Tool/Calculator'
    # Navigational
    if any(w in kw for w in ['online vcb', 'app', 'login', 'đăng nhập', 'chi nhánh', 'tổng đài', 'hotline', 'website']):
        return 'Navigational'
    # Informational (Default)
    return 'Informational'

def calculate_opportunity_score(volume, cpc, competition, intent):
    # Trọng số intent
    intent_weights = {
        'Transactional': 2.0,
        'Tool/Calculator': 1.8,
        'Commercial': 1.5,
        'Informational': 1.0,
        'Navigational': 0.7
    }
    weight = intent_weights.get(intent, 1.0)
    
    # Chuẩn hóa competition (High: 0.8, Medium: 0.5, Low: 0.2)
    comp_val = competition.lower()
    comp_factor = 0.2
    if 'high' in comp_val:
        comp_factor = 0.8
    elif 'medium' in comp_val:
        comp_factor = 0.5
    elif 'low' in comp_val:
        comp_factor = 0.2
        
    # Công thức: log10(Volume + 1) * (1.2 - comp_factor) * intent_weight * (1 + cpc_bonus)
    vol_score = math.log10(volume + 1) if volume > 0 else 0
    cpc_bonus = min(cpc * 0.2, 0.5) # bonus nếu CPC cao (thể hiện tính thương mại)
    
    score = vol_score * (1.2 - comp_factor) * weight * (1.0 + cpc_bonus)
    return round(score, 2)

def classify_quadrant(volume, competition, opportunity_score):
    comp_val = competition.lower()
    is_high_comp = 'high' in comp_val or 'medium' in comp_val
    if volume >= 2000 and not is_high_comp:
        return 'Quick Win'
    elif volume >= 5000 and is_high_comp:
        return 'Strategic Pillar'
    elif volume >= 500 and not is_high_comp:
        return 'Commercial Converter'
    else:
        return 'Long-tail / Supporting'

def load_inventory_csv(file_path):
    keywords = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    with open(file_path, 'r', encoding='utf-8-sig', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            kw_raw = row.get('Keyword', '')
            if not kw_raw:
                continue
            kw = normalize_text(clean_val(kw_raw))
            try:
                vol = int(clean_val(row.get('Volume', '0')) or 0)
            except ValueError:
                vol = 0
            try:
                cpc = float(clean_val(row.get('CPC', '0')) or 0.0)
            except ValueError:
                cpc = 0.0
            comp = clean_val(row.get('PPC Competition', 'Low'))
            
            intent = detect_intent(kw)
            opp_score = calculate_opportunity_score(vol, cpc, comp, intent)
            quadrant = classify_quadrant(vol, comp, opp_score)
            
            keywords.append({
                'keyword': kw,
                'volume': vol,
                'cpc': cpc,
                'competition': comp,
                'intent': intent,
                'opportunity_score': opp_score,
                'quadrant': quadrant
            })
    return keywords

def cluster_keywords(keywords, core_entities=None):
    """
    Gom cụm theo thực thể (Entity-based & Pattern-based Clustering).
    Nếu không truyền core_entities, engine tự động bóc tách các n-gram phổ biến.
    """
    clusters = defaultdict(list)
    unassigned = []
    
    # Định nghĩa mẫu thực thể mặc định cho tài chính & phương tiện
    default_patterns = {
        'Tra Cứu Lãi Suất & So Sánh Ngân Hàng': [
            'lãi suất', 'ngân hàng', 'vietcombank', 'agribank', 'bidv', 'techcombank', 
            'mb', 'vietinbank', 'sacombank', 'acb', 'vpbank', 'scb', 'bảng lãi suất'
        ],
        'Công Cụ Tính Lãi & Calculator': [
            'lãi bao nhiêu', 'tính lãi', '1 triệu', '100 triệu', '50 triệu', '10 triệu', 
            'cách tính', 'công cụ tính'
        ],
        'Gửi Tiết Kiệm Online & An Toàn': [
            'online', 'trực tuyến', 'an toàn', 'có nên', 'lừa đảo', 'bảo mật', 
            'tiết kiệm điện tử', 'rủi ro'
        ],
        'Kỳ Hạn & Hình Thức Tiết Kiệm': [
            'kỳ hạn', 'không kỳ hạn', 'có kỳ hạn', '1 tháng', '3 tháng', '6 tháng', 
            '12 tháng', 'bậc thang', 'tích lũy', 'gửi góp'
        ],
        'Thủ Tục, Mở Sổ & Rút Tiền': [
            'thủ tục', 'rút trước hạn', 'mở sổ', 'tất toán', 'điều kiện', 'giấy tờ', 
            'sổ tiết kiệm', 'phí'
        ],
        'Tra Cứu Biển Số & Tỉnh Thành': [
            'các tỉnh', 'tỉnh thành', 'hà nội', 'tp hcm', 'hồ chí minh', 'đà nẵng', 
            'hải phòng', 'nghệ an', 'bình dương', 'đồng nai', '63 tỉnh', '64 tỉnh'
        ],
        'Đấu Giá & Biển Số Định Danh': [
            'đấu giá', 'định danh', 'biển số đẹp', 'ngũ quý', 'tứ quý', 'phong thủy'
        ],
        'Thủ Tục Sang Tên, Đổi Biển & Phí': [
            'sang tên', 'đổi biển', 'biển vàng', 'lệ phí', 'thủ tục', 'đăng ký'
        ],
        'Tra Cứu Phạt Nguội & Xe Cộ': [
            'phạt nguội', 'xe máy', 'ô tô', 'tra cứu phạt'
        ]
    }
    
    patterns = core_entities if core_entities else default_patterns
    
    for item in keywords:
        kw = item['keyword']
        matched = False
        for cluster_name, match_words in patterns.items():
            if any(w in kw for w in match_words):
                clusters[cluster_name].append(item)
                matched = True
                break
        if not matched:
            clusters['Chủ Đề Khác & Long-Tail'].append(item)
            
    return clusters

def generate_cluster_summary(clusters):
    summary = []
    for cluster_name, items in clusters.items():
        if not items:
            continue
        tot_vol = sum(i['volume'] for i in items)
        avg_score = round(sum(i['opportunity_score'] for i in items) / len(items), 2)
        top_kws = sorted(items, key=lambda x: (x['opportunity_score'], x['volume']), reverse=True)[:5]
        summary.append({
            'cluster_name': cluster_name,
            'count': len(items),
            'total_volume': tot_vol,
            'avg_opportunity_score': avg_score,
            'top_keywords': top_kws
        })
    summary.sort(key=lambda x: x['total_volume'], reverse=True)
    return summary

if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else '05_HUBS/inventory/Financial/gui-tiet-kiem.csv'
    print(f"Loading: {file_path}")
    kws = load_inventory_csv(file_path)
    print(f"Loaded {len(kws)} keywords. Total search volume: {sum(k['volume'] for k in kws):,}")
    
    cls = cluster_keywords(kws)
    summary = generate_cluster_summary(cls)
    
    print("\n=== TOPIC CLUSTER SUMMARY ===")
    for c in summary:
        print(f"\n[Cluster] {c['cluster_name']}")
        print(f"  Keywords Count: {c['count']} | Total Volume: {c['total_volume']:,} | Avg Opp Score: {c['avg_opportunity_score']}")
        print("  Top Opportunities:")
        for tk in c['top_keywords']:
            print(f"    - {tk['keyword']}: Vol {tk['volume']:,} | Opp {tk['opportunity_score']} | Intent {tk['intent']} | Quad: {tk['quadrant']}")
