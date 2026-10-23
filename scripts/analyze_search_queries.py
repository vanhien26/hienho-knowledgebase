#!/usr/bin/env python3
"""
ANALYZE SEARCH QUERIES FROM GA4 DATA
Phân tích và tóm tắt top search queries cho /tim-kiem
"""

import json
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parents[1]
input_file = BASE_DIR / "07_REPORTS" / "data" / "search_analytics" / "tim-kiem-analytics-2026-10-01-to-2026-10-22.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

summary = data["summary"]
traffic_data = data["traffic_by_date_channel"]
search_queries = data["search_queries_from_dimension"]

print("=" * 70)
print("PHÂN TÍCH SEARCH QUERIES GA4 - /TIM-KIEM (1/10 - 22/10/2026)")
print("=" * 70)

print("\n[1] TỔNG QUAN TRAFFIC")
print(f"- Total Sessions: {summary['total_sessions']:,}")
print(f"- Total Engaged Sessions: {summary['total_engaged_sessions']:,}")
print(f"- Total Active Users: {summary['total_active_users']:,}")
print(f"- Engagement Rate: {summary['total_engaged_sessions']/summary['total_sessions']*100:.1f}%")

print("\n[2] PHÂN BỔ TRAFFIC THEO CHANNEL")
channel_summary = {}
for r in traffic_data:
    cg = r["channel_group"]
    channel_summary[cg] = channel_summary.get(cg, 0) + r["sessions"]

sorted_channels = sorted(channel_summary.items(), key=lambda x: x[1], reverse=True)
for cg, sess in sorted_channels:
    pct = sess / summary['total_sessions'] * 100
    print(f"- {cg}: {sess:,} sessions ({pct:.1f}%)")

print("\n[3] PHÂN TÍCH SEARCH QUERIES")
print(f"- Total unique search terms: {len(search_queries):,}")

# Top 50 search terms by sessions
sorted_queries = sorted(search_queries, key=lambda x: x["sessions"], reverse=True)
print("\n[4] TOP 50 SEARCH TERMS (by sessions)")
for i, q in enumerate(sorted_queries[:50], 1):
    print(f"{i:3d}. {q['search_term'][:60]:60s} ({q['sessions']:3d} sessions)")

# Phân loại search terms theo intent
def classify_intent(term):
    term_lower = term.lower()
    # Account/Auth
    if any(k in term_lower for k in ['đăng nhập', 'đăng ký', 'đăng nhâ', 'đăng kí', 'sign', 'login', 'register']):
        return "Account/Auth"
    # Contact/Transfer
    if any(k in term_lower for k in ['chuyển tiền', 'nạp', 'rút', 'số điện thoại', 'sdt', 'điện thoại']):
        return "Payment/Transfer"
    # Services
    if any(k in term_lower for k in ['vé', 'phim', 'máy bay', 'đặt', 'nghỉ', 'khách sạn']):
        return "Services/Ticketing"
    # Support/Issues
    if any(k in term_lower for k in ['lỗi', 'khóa', 'quên', 'thất bại', 'bị', 'không', 'hỗ trợ', 'giải quyết']):
        return "Support/Issues"
    # Financial
    if any(k in term_lower for k in ['vay', 'trả sau', 'cic', 'tín dụng', 'bh', 'bảo hiểm', 'gold', 'vàng']):
        return "Financial/Insurance"
    # Info/General
    if any(k in term_lower for k in ['đối tác', 'địa chỉ', 'liên hệ', 'thông tin', 'hoạt động']):
        return "Information"
    # Errors/Typo (sai chính tả nhiều)
    if any(k in term_lower for k in ['moom', 'môm', 'mom', 'mo mo', 'mô mô']):
        return "Typo/Brand"
    return "Other/Unknown"

intent_summary = Counter()
for q in search_queries:
    intent = classify_intent(q["search_term"])
    intent_summary[intent] += q["sessions"]

print("\n[5] PHÂN BỔ SEARCH INTENT")
sorted_intents = sorted(intent_summary.items(), key=lambda x: x[1], reverse=True)
for intent, sess in sorted_intents:
    pct = sess / summary['total_sessions'] * 100
    print(f"- {intent:25s}: {sess:4d} sessions ({pct:5.1f}%)")

# Detect số điện thoại
phone_queries = [q for q in search_queries if q["search_term"].replace(" ", "").isdigit() and len(q["search_term"].replace(" ", "")) >= 9]
print(f"\n[6] SỐ ĐIỆN THOẠI ĐƯỢC TÌM KIẾM")
print(f"- Total phone number queries: {len(phone_queries):,}")
print(f"- Sessions from phone queries: {sum(q['sessions'] for q in phone_queries):,}")

# Detect các từ khóa phổ biến sai chính tả
typo_keywords = ['moom', 'môm', 'mom', 'mo mo', 'mô mô', 'moomo', 'mo mo', 'momo web', 'momo wep', 'wep', 'wed']
typo_queries = [q for q in search_queries if any(t in q["search_term"].lower() for t in typo_keywords)]
print(f"\n[7] TỪ KHÓA SAI CHÍNH TẢ (TYPO)")
print(f"- Total typo queries: {len(typo_queries):,}")
print(f"- Sessions from typo queries: {sum(q['sessions'] for q in typo_queries):,}")
print("\nTop 20 typo queries:")
sorted_typos = sorted(typo_queries, key=lambda x: x["sessions"], reverse=True)
for i, q in enumerate(sorted_typos[:20], 1):
    print(f"{i:3d}. {q['search_term'][:50]:50s} ({q['sessions']:3d} sessions)")

print("\n" + "=" * 70)
