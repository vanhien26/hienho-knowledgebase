#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULATION & AUDIT ENGINE: KEYWORD REALLOCATION & VARIANT MERGING
Quét toàn bộ kho dữ liệu, mô phỏng chuyển keyword sai theme, gộp biến thể chính tả (max volume)
và xuất báo cáo chi tiết để người dùng review trước khi sync sang Web.
"""

import os
import glob
import re
import json
import unicodedata
import pandas as pd
from collections import defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INVENTORY_DIR = os.path.join(BASE_DIR, "05_HUBS", "inventory")
OUTPUT_REPORT = os.path.join(BASE_DIR, "07_REPORTS", "KEYWORD_REALLOCATION_REVIEW.md")

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def make_norm_key(text):
    text = text.lower().strip()
    text = remove_accents(text)
    return re.sub(r'[^a-z0-9]', '', text)

def clean_csv(path):
    if not os.path.exists(path):
        return pd.DataFrame(columns=['kw', 'vol', 'cpc', 'comp', 'raw_row'])
    df = pd.read_csv(path)
    kws = df['Keyword'].astype(str).str.replace('="', '', regex=False).str.replace('"', '', regex=False)
    vols = df['Volume'].astype(str).str.replace('="', '', regex=False).str.replace('"', '', regex=False)
    df['clean_kw'] = kws
    df['clean_vol'] = pd.to_numeric(vols, errors='coerce').fillna(0).astype(int)
    return df

# -------------------------------------------------------------
# 1. RÀ SOÁT CHUYỂN KEYWORD SAI THEME (REALLOCATION)
# -------------------------------------------------------------
reallocation_records = []

# A. Xổ số (Lottery)
VIETLOTT_ENTITIES = [
    'vietlott', 'viet lott', 'mega', 'power',
    'keno', 'max 3d', 'max3d', 'max 4d', 'max4d', 'bingo18', 'bingo 18',
    'bingo', '6/55', '6/45', '6 55', '6 45', '655', '645', 'xspower', 'xsp0wer', 'vietluck'
]

def has_vl(kw):
    k = kw.lower()
    return any(e in k for e in VIETLOTT_ENTITIES)

df_vl = clean_csv(os.path.join(INVENTORY_DIR, 'Lottery', 'vietlott.csv'))
df_xs = clean_csv(os.path.join(INVENTORY_DIR, 'Lottery', 'xo-so.csv'))
df_vs = clean_csv(os.path.join(INVENTORY_DIR, 'Lottery', 've-so.csv'))

# Vietlott -> XSKT / Vé Số
for idx, r in df_vl.iterrows():
    kw, vol = r['clean_kw'], r['clean_vol']
    if not has_vl(kw):
        to_t = 've-so' if ('vé số' in kw.lower() or 'dò vé' in kw.lower()) else 'xo-so'
        reallocation_records.append({
            'keyword': kw,
            'volume': vol,
            'from_theme': 'vietlott (Vietlott)',
            'to_theme': f'{to_t} (Xổ Số Kiến Thiết)' if to_t == 'xo-so' else 've-so (Vé Số)',
            'category': 'Xổ số & Vé số',
            'reason': 'Chứa thực thể XSKT truyền thống (xsmb, xsmn, xsmt, xổ số miền...)'
        })

# XSKT -> Vietlott
for idx, r in df_xs.iterrows():
    kw, vol = r['clean_kw'], r['clean_vol']
    if has_vl(kw):
        reallocation_records.append({
            'keyword': kw,
            'volume': vol,
            'from_theme': 'xo-so (Xổ Số Kiến Thiết)',
            'to_theme': 'vietlott (Vietlott)',
            'category': 'Xổ số & Vé số',
            'reason': 'Chứa sản phẩm Vietlott (vietlott, mega, power, keno, max3d)'
        })

# Ve So -> Vietlott
for idx, r in df_vs.iterrows():
    kw, vol = r['clean_kw'], r['clean_vol']
    if has_vl(kw):
        reallocation_records.append({
            'keyword': kw,
            'volume': vol,
            'from_theme': 've-so (Vé Số)',
            'to_theme': 'vietlott (Vietlott)',
            'category': 'Xổ số & Vé số',
            'reason': 'Chứa sản phẩm Vietlott (mua vé số vietlott, dò vietlott)'
        })

# B. Ngân Hàng (Financial - Banks)
BANK_THEMES = {
    'mbbank': ['mb bank', 'mbbank', 'ngan hang mb', 'ngân hàng mb'],
    'Vietcombank': ['vietcombank', 'vcb', 'vietcom bank'],
    'Techcombank': ['techcombank', 'tcb', 'techcom bank'],
    'VietinBank': ['vietinbank', 'ctg', 'vietin bank'],
    'BIDV': ['bidv', 'ngan hang bidv', 'ngân hàng bidv'],
    'agribank': ['agribank', 'ngan hang agribank', 'ngân hàng agribank'],
    'ACB': ['acb bank', 'ngân hàng acb', 'ngan hang acb', 'acb'],
    'sacombank': ['sacombank', 'stb'],
    'vpbank': ['vpbank', 'vp bank'],
    'tpbank': ['tpbank', 'tp bank', 'tien phong bank', 'tiên phong bank'],
    'shb': ['shb bank', 'ngân hàng shb', 'ngan hang shb'],
    'hd-bank': ['hdbank', 'hd bank'],
    'vib': ['vib bank', 'ngân hàng vib', 'ngan hang vib'],
    'MSB': ['msb bank', 'ngân hàng msb', 'hàng hải'],
    'ocb': ['ocb bank', 'ngân hàng ocb', 'phương đông'],
    'seabank': ['seabank', 'sea bank', 'đông nam á'],
    'scb': ['scb bank', 'ngân hàng scb', 'sài gòn thương tín'],
    'ab-bank': ['ab bank', 'abbank', 'an bình'],
    'bac-a-bank': ['bac a bank', 'baca bank', 'bắc á bank'],
    'ban-viet': ['bản việt', 'bvbank', 'ban viet bank'],
    'bao-viet-bank': ['baoviet bank', 'bảo việt bank'],
    'kien-long-bank': ['kienlong bank', 'kienlongbank'],
    'LPBank': ['lpbank', 'lp bank', 'liên việt'],
    'nam-a-bank': ['nam a bank', 'namabank'],
    'ncb': ['ncb bank', 'quốc dân'],
    'ocean-bank': ['oceanbank', 'ocean bank', 'đại dương'],
    'pvcom bank': ['pvcombank', 'pvcom bank'],
    'saigonbank': ['saigonbank', 'saigon bank'],
    'Shinhan Bank': ['shinhan bank', 'shinhan'],
    'vietbank': ['vietbank', 'viet bank'],
    'vrb': ['vrb bank', 'việt nga'],
    'Indovina Bank': ['indovina bank', 'ivb'],
    'donga bank': ['đông á bank', 'donga bank', 'dong a bank'],
    'Eximbank': ['eximbank', 'exim bank']
}

for b_theme, aliases in BANK_THEMES.items():
    matches = glob.glob(f'{INVENTORY_DIR}/Financial/*{b_theme}*.csv')
    if not matches:
        continue
    df_b = clean_csv(matches[0])
    for idx, r in df_b.iterrows():
        kw, vol = r['clean_kw'], r['clean_vol']
        kw_l = kw.lower().strip()
        # Nếu có chứa alias của chính nó thì giữ lại
        if any(a in kw_l for a in aliases):
            continue
        # Kiểm tra xem có chứa tên ngân hàng khác không
        for other_b, other_aliases in BANK_THEMES.items():
            if other_b == b_theme:
                continue
            strong = [a for a in other_aliases if len(a) >= 4 and a in kw_l]
            if strong:
                reallocation_records.append({
                    'keyword': kw,
                    'volume': vol,
                    'from_theme': b_theme,
                    'to_theme': other_b,
                    'category': 'Ngân Hàng (Financial)',
                    'reason': f'Chứa thương hiệu ngân hàng đối thủ ({strong[0]})'
                })
                break

# C. Bảo hiểm (Insurtech)
df_bhyt = clean_csv(os.path.join(INVENTORY_DIR, 'insurtech', 'bhyt.csv'))
df_bhxh = clean_csv(os.path.join(INVENTORY_DIR, 'insurtech', 'bhxh.csv'))

for idx, r in df_bhyt.iterrows():
    kw, vol = r['clean_kw'], r['clean_vol']
    kw_l = kw.lower()
    if ('bhxh' in kw_l or 'bảo hiểm xã hội' in kw_l) and ('bhyt' not in kw_l and 'bảo hiểm y tế' not in kw_l):
        reallocation_records.append({
            'keyword': kw,
            'volume': vol,
            'from_theme': 'bhyt (Bảo Hiểm Y Tế)',
            'to_theme': 'bhxh (Bảo Hiểm Xã Hội)',
            'category': 'Bảo hiểm số (Insurtech)',
            'reason': 'Chứa từ khóa thuần Bảo Hiểm Xã Hội'
        })

for idx, r in df_bhxh.iterrows():
    kw, vol = r['clean_kw'], r['clean_vol']
    kw_l = kw.lower()
    if ('bhyt' in kw_l or 'bảo hiểm y tế' in kw_l) and ('bhxh' not in kw_l and 'bảo hiểm xã hội' not in kw_l):
        reallocation_records.append({
            'keyword': kw,
            'volume': vol,
            'from_theme': 'bhxh (Bảo Hiểm Xã Hội)',
            'to_theme': 'bhyt (Bảo Hiểm Y Tế)',
            'category': 'Bảo hiểm số (Insurtech)',
            'reason': 'Chứa từ khóa thuần Bảo Hiểm Y Tế'
        })

# D. Thu phí không dừng (Vehicle Hub)
df_vetc = clean_csv(os.path.join(INVENTORY_DIR, 'vehicle-hub', 'vetc.csv'))
for idx, r in df_vetc.iterrows():
    kw, vol = r['clean_kw'], r['clean_vol']
    kw_l = kw.lower()
    if 'epass' in kw_l and 'vetc' not in kw_l:
        reallocation_records.append({
            'keyword': kw,
            'volume': vol,
            'from_theme': 'vetc (Thu Phí VETC)',
            'to_theme': 'epass (Thu Phí ePass)',
            'category': 'Giao thông (Vehicle Hub)',
            'reason': 'Chứa từ khóa thương hiệu ePass'
        })

# -------------------------------------------------------------
# 2. RÀ SOÁT BIẾN THỂ CHÍNH TẢ & GỘP VARIANT (MAX VOLUME)
# -------------------------------------------------------------
# Xây dựng danh sách keyword sạch cho Vietlott sau khi đã chuyển
vl_reallocated = []
# Các từ khóa giữ lại trong vietlott
for idx, r in df_vl.iterrows():
    if has_vl(r['clean_kw']):
        vl_reallocated.append((r['clean_kw'], r['clean_vol']))
# Các từ khóa chuyển từ xo-so sang vietlott
for idx, r in df_xs.iterrows():
    if has_vl(r['clean_kw']):
        vl_reallocated.append((r['clean_kw'], r['clean_vol']))
# Các từ khóa chuyển từ ve-so sang vietlott
for idx, r in df_vs.iterrows():
    if has_vl(r['clean_kw']):
        vl_reallocated.append((r['clean_kw'], r['clean_vol']))

vl_df_re = pd.DataFrame(vl_reallocated, columns=['kw', 'vol']).drop_duplicates(subset=['kw'])

vl_variant_groups = defaultdict(list)
for idx, r in vl_df_re.iterrows():
    vl_variant_groups[make_norm_key(r['kw'])].append((r['kw'], r['vol']))

vietlott_merged_variants = []
for key, items in vl_variant_groups.items():
    if len(items) > 1:
        max_vol = max(v for kw, v in items)
        # Chọn canonical: ưu tiên chuẩn có dấu, độ dài hợp lý
        canonical = sorted(items, key=lambda x: (x[1], len(x[0])), reverse=True)[0][0]
        variants = [kw for kw, v in items if kw != canonical]
        vietlott_merged_variants.append({
            'canonical_keyword': canonical,
            'max_volume': max_vol,
            'variants': variants,
            'all_items': items
        })

vietlott_merged_variants.sort(key=lambda x: x['max_volume'], reverse=True)

# Tương tự cho XSKT
xs_reallocated = []
for idx, r in df_xs.iterrows():
    if not has_vl(r['clean_kw']):
        xs_reallocated.append((r['clean_kw'], r['clean_vol']))
for idx, r in df_vl.iterrows():
    if not has_vl(r['clean_kw']):
        xs_reallocated.append((r['clean_kw'], r['clean_vol']))

xs_df_re = pd.DataFrame(xs_reallocated, columns=['kw', 'vol']).drop_duplicates(subset=['kw'])

xs_variant_groups = defaultdict(list)
for idx, r in xs_df_re.iterrows():
    xs_variant_groups[make_norm_key(r['kw'])].append((r['kw'], r['vol']))

xs_merged_variants = []
for key, items in xs_variant_groups.items():
    if len(items) > 1:
        max_vol = max(v for kw, v in items)
        canonical = sorted(items, key=lambda x: (x[1], len(x[0])), reverse=True)[0][0]
        variants = [kw for kw, v in items if kw != canonical]
        xs_merged_variants.append({
            'canonical_keyword': canonical,
            'max_volume': max_vol,
            'variants': variants,
            'all_items': items
        })

xs_merged_variants.sort(key=lambda x: x['max_volume'], reverse=True)

print(f"Total Reallocated Keywords: {len(reallocation_records)}")
print(f"Total Vietlott Variant Groups: {len(vietlott_merged_variants)}")
print(f"Total XSKT Variant Groups: {len(xs_merged_variants)}")

# Lưu kết quả dạng JSON tạm thời để phân tích
with open(os.path.join(BASE_DIR, "07_REPORTS", "data", "reallocation_audit.json"), "w", encoding="utf-8") as f:
    json.dump({
        'total_moves': len(reallocation_records),
        'moves': reallocation_records,
        'vietlott_variants': vietlott_merged_variants,
        'xskt_variants': xs_merged_variants
    }, f, ensure_ascii=False, indent=2)

print("Đã lưu audit snapshot JSON thành công.")
