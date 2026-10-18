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
import json
from collections import defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)
from scripts.lib.keyword_intelligence import (
    MultiSignalIntentClassifier,
    clean_val,
    normalize_text,
    calculate_opportunity_score,
    classify_quadrant
)

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
            
            intent = MultiSignalIntentClassifier.classify(kw)['intent']
            opp_score = calculate_opportunity_score(vol, cpc, comp, intent)
            quadrant = classify_quadrant(vol, comp, intent)
            
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
