#!/usr/bin/env python3
"""
FULL-FUNNEL DATA DECOMPOSITION PIPELINE (GSC + GA4) - REFACTORED
Đồng bộ và phân rã hợp nhất 2 nguồn dữ liệu lớn nhất của Web Platform:
1. GSC (Google Search Console): Pre-Click (Search Query, Impressions, Position, CTR, Cannibalization, Strike Zone)
   - Khung thời gian: Chuẩn xác theo kỳ GA4 (2026-09-20 -> 2026-10-19)
2. GA4 (Google Analytics 4): Post-Click & Chuyển đổi Web-to-App
   - Chỉ đếm click Onelink từ channel_group = 'Organic Search'
   - Phân rã 2 luồng: ol_momo (onelink.momo.vn) & ol_appsflyer (momoapp.onelink.vn)
   - w2a_cr = (ol_momo + ol_appsflyer) / organic_sessions

Quy chuẩn nâng cao:
- Normalize URL 2 phía về canonical path (lowercase, strip query/hash/trailing slash)
- Đảm bảo summary.join_rate > 90%
- Gắn theme 3 tầng (prefix thư mục + cluster URLs + fallback Hub), đảm bảo summary.organic_mapped_pct > 70%
- quadrant_distribution đếm theo page, tổng khớp 100% với total_pages_analyzed
- potential_gain = impressions * (CTR benchmark vị trí 3 - CTR hiện tại), trần là market_volume của theme
- Loại trừ query brand/navigational (momo, dang nhap, typo) khỏi quadrant và quick wins
- Quick wins unique path, ưu tiên sector Credit/Insurance/BNPL (priority_sector: bool)
"""

import os
import sys
import json
import time
import re
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from urllib.parse import urlparse, unquote
from pathlib import Path
from collections import defaultdict
import fnmatch
import shutil

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_REPO = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")

# Cấu hình chu kỳ thời gian SSOT - có thể override qua CLI args --start-date / --end-date
_DEFAULT_DATE_START = "2026-10-01"
_DEFAULT_DATE_END = "2026-10-20"

def _resolve_dates() -> tuple[str, str]:
    import argparse as _ap
    p = _ap.ArgumentParser(add_help=False)
    p.add_argument("--start-date", default=None)
    p.add_argument("--end-date", default=None)
    known, _ = p.parse_known_args()
    start = known.start_date or _DEFAULT_DATE_START
    end = known.end_date or _DEFAULT_DATE_END
    return start, end

DATE_START, DATE_END = _resolve_dates()

# Bảng benchmark CTR organic theo vị trí (Sistrix & Backlinko industry standards)
CTR_BENCHMARK_TABLE = {
    "1": 0.285,
    "2": 0.157,
    "3": 0.110,
    "4": 0.080,
    "5": 0.062,
    "6": 0.045,
    "7": 0.035,
    "8": 0.028,
    "9": 0.022,
    "10": 0.018,
    "benchmark_position_3_target_ctr": 0.110,
    "formula": "potential_gain = min(market_volume, int(impressions * max(0.0, 0.110 - actual_ctr)))",
    "source": "Sistrix & Backlinko Google SERP Organic CTR Benchmark (Position 3 = 11.0%)"
}

# Regex nhận diện từ khóa Brand / Navigational / Typo Domain
BRAND_PATTERNS = [
    r"\bmomo\b", r"\bmo\s+mo\b", r"\bmôm\b", r"\bvi\s+momo\b", r"\bví\s+momo\b",
    r"\bmomo\.vn\b", r"\bmoomo\b", r"\bmommo\b", r"\bm0m0\b", r"\bmmo\b",
    r"\bdang\s+nhap\b", r"\bđăng\s+nhập\b", r"\blogin\b",
    r"\btai\s+app\b", r"\btải\s+app\b", r"\bcai\s+dat\b", r"\bcài\s+đặt\b",
    r"\bhotline\b", r"\btong\s+dai\b", r"\btổng\s+đài\b",
    r"\bcskh\b", r"\bcham\s+soc\s+khach\s+hang\b", r"\bchăm\s+sóc\s+khách\s+hàng\b",
    r"\bquen\s+mat\s+khau\b", r"\bquên\s+mật\s+khẩu\b",
    r"\bweb\s+momo\b", r"\bmomo\s+web\b",
    # Typo domain & spam domain (loại bỏ .com, .vn, 6mmoo...)
    r"\.(com|vn|net|org|xyz|info|app|me|cc|online)\b",
    r"\b\d*m+o+o+\b", r"\b6mmoo\b", r"\bmmoo\b"
]
BRAND_REGEX = re.compile("|".join(BRAND_PATTERNS), re.IGNORECASE)

PRIORITY_SECTORS = {"Financial", "insurtech", "Credit", "Insurance", "BNPL"}

def normalize_path(url_str):
    if not url_str:
        return "/"
    p = unquote(urlparse(str(url_str)).path).lower().strip().rstrip("/")
    return p if p else "/"

def is_brand_query(query):
    if not query:
        return False
    return bool(BRAND_REGEX.search(query))

def is_priority_sector(sector, path):
    if sector in PRIORITY_SECTORS:
        return True
    p = path.lower()
    for kw in ["vay", "vi-tra-sau", "bao-hiem", "the-tin-dung", "tiet-kiem", "lai-suat", "diem-tin-dung", "chung-khoan"]:
        if kw in p:
            return True
    return False

def get_ga4_access_token():
    creds_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-credentials.json"
    token_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "ga4-token.json"
    with open(creds_file, "r", encoding="utf-8") as f:
        oauth_creds = json.load(f)["installed"]
    with open(token_file, "r", encoding="utf-8") as f:
        refresh_token = json.load(f)["refresh_token"]
    
    body = urllib.parse.urlencode({
        "client_id": oauth_creds["client_id"],
        "client_secret": oauth_creds["client_secret"],
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode("utf-8")
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))["access_token"]

def fetch_gsc_30d_data():
    """Kéo dữ liệu GSC chuẩn kỳ 30 ngày (2026-09-20 -> 2026-10-19) qua Service Account API"""
    cache_file = BASE_DIR / "07_REPORTS" / "data" / "gsc_30d_cache.json"
    if cache_file.exists():
        file_age_hours = (time.time() - os.path.getmtime(cache_file)) / 3600
        if file_age_hours < 24:
            print(f"✓ Sử dụng cache GSC 30 ngày sẵn có: {cache_file} ({file_age_hours:.1f}h ago)")
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)

    print(f"Đang kéo dữ liệu mới từ GSC API cho kỳ {DATE_START} -> {DATE_END}...")
    key_file = BASE_DIR / "07_REPORTS" / "data" / "credentials" / "gsc-credentials.json"
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
    credentials = service_account.Credentials.from_service_account_file(key_file, scopes=scopes)
    service = build("searchconsole", "v1", credentials=credentials)

    rows = []
    start_row = 0
    batch_size = 25000
    while True:
        res = service.searchanalytics().query(
            siteUrl="https://www.momo.vn/",
            body={
                "startDate": DATE_START,
                "endDate": DATE_END,
                "dimensions": ["page", "query"],
                "rowLimit": batch_size,
                "startRow": start_row
            }
        ).execute()
        batch = res.get("rows", [])
        if not batch:
            break
        rows.extend(batch)
        print(f"  Đã tải {len(rows):,} dòng GSC...")
        if len(batch) < batch_size or start_row >= 200000:
            break
        start_row += batch_size

    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False)
    print(f"✓ Đã lưu cache GSC: {cache_file} ({len(rows):,} dòng)")
    return rows

def fetch_ga4_organic_data():
    """Kéo toàn bộ Organic Search Landing Pages và sự kiện Onelink Organic từ GA4"""
    access_token = get_ga4_access_token()
    url = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"
    date_ranges = [{"startDate": DATE_START, "endDate": DATE_END}]

    # 1. Toàn bộ Organic Landing Pages (Sessions & Engaged Sessions)
    print("  Kéo GA4: Organic Search Landing Pages...")
    body_org = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}
        },
        "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}, {"name": "engagedSessions"}],
        "limit": 100000
    }
    req = urllib.request.Request(url, data=json.dumps(body_org).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        res_org = json.loads(resp.read().decode("utf-8"))

    # 2. Organic AI Search Sessions
    print("  Kéo GA4: AI Search Sessions...")
    ai_sources = ["chatgpt.com", "perplexity.ai", "gemini.google.com", "copilot.microsoft.com", "android-app://com.openai.chatgpt"]
    body_ai = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "filter": {"fieldName": "sessionSource", "inListFilter": {"values": ai_sources}}
        },
        "metrics": [{"name": "sessions"}],
        "limit": 100000
    }
    req_ai = urllib.request.Request(url, data=json.dumps(body_ai).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_ai) as resp:
        res_ai = json.loads(resp.read().decode("utf-8"))

    # 3. Organic Track 1: onelink.momo.vn (User hiện hữu mở App từ Organic Search)
    print("  Kéo GA4: Onelink MoMo (ol_momo) từ Organic Search...")
    body_momo = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}},
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink.momo.vn"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink.momo.vn"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100000
    }
    req_momo = urllib.request.Request(url, data=json.dumps(body_momo).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_momo) as resp:
        res_momo = json.loads(resp.read().decode("utf-8"))

    # 4. Organic Track 2: momoapp.onelink (User mới cài App từ Organic Search)
    print("  Kéo GA4: Onelink AppsFlyer (ol_appsflyer) từ Organic Search...")
    body_af = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}},
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "momoapp.onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "momoapp.onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100000
    }
    req_af = urllib.request.Request(url, data=json.dumps(body_af).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_af) as resp:
        res_af = json.loads(resp.read().decode("utf-8"))

    return res_org, res_ai, res_momo, res_af

def is_paid_channel(channel_name):
    if not channel_name:
        return False
    cn = channel_name.strip().lower()
    return "paid" in cn or "display" in cn or "cpc" in cn

def fetch_ga4_multichannel_data():
    """Kéo dữ liệu Đa Kênh GA4: Channels overview, Landing Page x Channels, và Onelink W2A events"""
    cache_file = BASE_DIR / "07_REPORTS" / "data" / f"ga4_multichannel_cache_{DATE_START}_{DATE_END}.json"
    if cache_file.exists():
        file_age_hours = (time.time() - os.path.getmtime(cache_file)) / 3600
        if file_age_hours < 24:
            print(f"✓ Sử dụng cache GA4 Multi-Channel: {cache_file} (tạo cách đây {file_age_hours:.1f}h)")
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)

    access_token = get_ga4_access_token()
    url = "https://analyticsdata.googleapis.com/v1beta/properties/270743103:runReport"
    date_ranges = [{"startDate": DATE_START, "endDate": DATE_END}]

    # 1. Global Channels summary (sessions, engaged, users)
    print("  Kéo GA4: Global Channels summary...")
    body_ch = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}, {"name": "engagedSessions"}, {"name": "totalUsers"}],
        "limit": 100
    }
    req_ch = urllib.request.Request(url, data=json.dumps(body_ch).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_ch) as resp:
        res_ch = json.loads(resp.read().decode("utf-8"))

    # 2. Global W2A clicks by channel group
    print("  Kéo GA4: Global W2A Clicks by channel group...")
    body_ch_w2a = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100
    }
    req_ch_w2a = urllib.request.Request(url, data=json.dumps(body_ch_w2a).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_ch_w2a) as resp:
        res_ch_w2a = json.loads(resp.read().decode("utf-8"))

    # 3. Landing Page x Channel Group (Pageviews & Sessions)
    print("  Kéo GA4: Landing Page x Channel Group Pageviews & Sessions...")
    body_lp_ch = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}, {"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "screenPageViews"}, {"name": "sessions"}],
        "limit": 100000
    }
    req_lp_ch = urllib.request.Request(url, data=json.dumps(body_lp_ch).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_lp_ch) as resp:
        res_lp_ch = json.loads(resp.read().decode("utf-8"))

    # 4. Landing Page x Channel Group (W2A Onelink clicks)
    print("  Kéo GA4: Landing Page x Channel Group W2A Clicks...")
    body_lp_w2a = {
        "dateRanges": date_ranges,
        "dimensions": [{"name": "landingPage"}, {"name": "sessionDefaultChannelGroup"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 100000
    }
    req_lp_w2a = urllib.request.Request(url, data=json.dumps(body_lp_w2a).encode("utf-8"), headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req_lp_w2a) as resp:
        res_lp_w2a = json.loads(resp.read().decode("utf-8"))

    cache_data = {
        "channels_overview": res_ch.get("rows", []),
        "channels_w2a": res_ch_w2a.get("rows", []),
        "landing_page_channels": res_lp_ch.get("rows", []),
        "landing_page_w2a": res_lp_w2a.get("rows", [])
    }
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(cache_data, f, ensure_ascii=False)
    print(f"✓ Đã lưu cache GA4 Multi-Channel: {cache_file}")
    return cache_data

def clean_dim_project(p):
    if not p: return 'Other'
    p = p.strip()
    l = p.lower()
    if l in ['cinema']: return 'Cinema'
    if l in ['ota']: return 'OTA'
    if l in ['ve xe', 'vé xe']: return 'Vé Xe'
    if l in ['esim']: return 'Esim'
    if l in ['vi tra sau', 'ví trả sau', 'ví trả sau (bnpl)', 'vi tra sau (bnpl)', 'ví trả sau & bnpl', 'bnpl', 'vi-tra-sau']: return 'Ví Trả Sau'
    if l in ['vay nhanh', 'vay nhanh & vay tín chấp', 'vay nhanh & vay tin chap', 'vay tin chap', 'vay tín chấp', 'vay-nhanh']: return 'Vay Nhanh'
    if l in ['tiet kiem online', 'tiết kiệm online', 'tui than tai', 'túi thần tài']: return 'Tiết Kiệm Online'
    if l in ['chung khoan', 'chứng khoán']: return 'Chứng Khoán'
    if l in ['chung chi quy', 'chứng chỉ quỹ', 'sàn đầu tư', 'quỹ']: return 'Chứng Chỉ Quỹ'
    if l in ['gia vang', 'giá vàng', 'tiệm vàng online']: return 'Giá Vàng'
    if l in ['ty gia', 'tỷ giá']: return 'Tỷ Giá'
    if l in ['mo the tin dung', 'mở thẻ tín dụng', 'thanh toan the tin dung', 'thanh toán thẻ tín dụng']: return 'Mở Thẻ Tín Dụng'
    if l in ['diem tin dung', 'điểm tín dụng', 'điểm tín dụng & cic', 'diem tin dung & cic', 'cic', 'diem-tin-dung']: return 'Điểm Tín Dụng'
    if l in ['trung tam tai chinh', 'trung tâm tài chính']: return 'Trung Tâm Tài Chính'
    if l in ['quan ly chi tieu', 'quản lý chi tiêu']: return 'Quản Lý Chi Tiêu'
    if l in ['p2p']: return 'P2P'
    if l in ['mo tai khoan ngan hang', 'mở tài khoản ngân hàng']: return 'Mở Tài Khoản Ngân Hàng'
    if l in ['thanh toan khoan vay', 'thanh toán khoản vay']: return 'Thanh Toán Khoản Vay'
    if l in ['tra gop apple', 'trả góp apple']: return 'Trả Góp Apple'
    if l in ['billpay']: return 'Billpay'
    if l in ['dien', 'điện']: return 'Điện'
    if l in ['nuoc', 'nước']: return 'Nước'
    if l in ['bao hiem o to', 'bảo hiểm ô tô']: return 'Bảo Hiểm Ô Tô'
    if l in ['bao hiem xe may', 'bảo hiểm xe máy']: return 'Bảo Hiểm Xe Máy'
    if l in ['bao hiem y te', 'bảo hiểm y tế']: return 'Bảo Hiểm Y Tế'
    if l in ['bao hiem xa hoi', 'bảo hiểm xã hội']: return 'Bảo Hiểm Xã Hội'
    if l in ['bao hiem suc khoe', 'bảo hiểm sức khỏe', 'bao hiem', 'bảo hiểm']: return 'Bảo Hiểm'
    if l in ['phat nguoi', 'phạt nguội']: return 'Phạt Nguội'
    if l in ['phi khong dung', 'phí không dừng']: return 'Phí Không Dừng'
    if l in ['tien ich giao thong', 'tiện ích giao thông', 'tram sac', 'trạm sạc', 'cay xang', 'cây xăng', 'gia xang', 'giá xăng']: return 'Tiện Ích Giao Thông'
    if l in ['data']: return 'Data'
    if l in ['sim']: return 'Sim'
    if l in ['game', 'game hub', 'nạp thẻ game']: return 'Game'
    if l in ['tiktok']: return 'Tiktok'
    if l in ['ve so', 'vé số']: return 'Vé Số'
    if l in ['student hub', 'student pass']: return 'Student Hub'
    if l in ['merchant']: return 'Merchant'
    if l in ['soundbox']: return 'Soundbox'
    if l in ['donation']: return 'Donation'
    if l in ['trust']: return 'Trust'
    if l in ['tnc', 'dieu khoan', 'điều khoản', 'terms']: return 'TnC'
    if l in ['new user', 'download', 'application store']: return 'New User'
    if l in ['home momo']: return 'Home MoMo'
    if l in ['campaign']: return 'Campaign'
    if l in ['khuyen mai', 'khuyến mãi', 'hoan tien mua sam', 'hoàn tiền mua sắm', 'xu']: return 'Khuyến Mãi'
    if l in ['dich vu lien ket', 'dịch vụ liên kết', 'cross border']: return 'Dịch Vụ Liên Kết'
    if l in ['hoi dap', 'hỏi đáp', 'tim kiem', 'tìm kiếm']: return 'Hỏi Đáp'
    if l in ['guide']: return 'Guide'
    if l in ['tin tuc', 'tin tức']: return 'Tin Tức'
    if l in ['blog']: return 'Blog'
    return p

def resolve_dim_project_name(dim_proj, tid, sec):
    if dim_proj:
        return clean_dim_project(dim_proj)
    t = (tid or '').lower()
    s = (sec or '').lower()
    if s == 'cinema' or 'phim' in t or 'cinema' in t or 'rap' in t: return 'Cinema'
    if 've-xe' in t or 'xe-khach' in t: return 'Vé Xe'
    if 'esim' in t: return 'Esim'
    if s == 'ota' or 'du-lich' in t or 'may-bay' in t or 'khach-san' in t or 'tau-hoa' in t: return 'OTA'
    if 'vi-tra-sau' in t or 'apple' in t: return 'Ví Trả Sau'
    if 'vay' in t: return 'Vay Nhanh'
    if 'tiet-kiem' in t or 'lai-suat' in t or 'than-tai' in t: return 'Tiết Kiệm Online'
    if 'chung-khoan' in t or 'co-phieu' in t or 'phai-sinh' in t: return 'Chứng Khoán'
    if 'quy' in t: return 'Chứng Chỉ Quỹ'
    if 'gia-vang' in t: return 'Giá Vàng'
    if 'ty-gia' in t: return 'Tỷ Giá'
    if 'the-tin-dung' in t or 'visa' in t: return 'Mở Thẻ Tín Dụng'
    if 'diem-tin-dung' in t or 'cic' in t: return 'Điểm Tín Dụng'
    if 'quan-ly-chi-tieu' in t or 'tinh-luong' in t or 'tai-san' in t or 'tieu-san' in t: return 'Quản Lý Chi Tiêu'
    if 'chuyen-tien' in t or 'p2p' in t or 'napas' in t or 'kieu-hoi' in t: return 'P2P'
    if 'billpay' in t or 'dien' in t or 'nuoc' in t or 'hoc-phi' in t: return 'Billpay'
    if s == 'financial': return 'Trung Tâm Tài Chính'
    if 'bao-hiem-o-to' in t: return 'Bảo Hiểm Ô Tô'
    if 'bao-hiem-xe-may' in t: return 'Bảo Hiểm Xe Máy'
    if 'bhyt' in t or 'y-te' in t: return 'Bảo Hiểm Y Tế'
    if 'bhxh' in t or 'xa-hoi' in t: return 'Bảo Hiểm Xã Hội'
    if s == 'insurtech' or 'bao-hiem' in t: return 'Bảo Hiểm'
    if 'phat-nguoi' in t: return 'Phạt Nguội'
    if 'phi-khong-dung' in t or 'etc' in t: return 'Phí Không Dừng'
    if s == 'vehicle-hub' or 'dang-kiem' in t or 'xang' in t or 'tram-sac' in t: return 'Tiện Ích Giao Thông'
    if 'data' in t or '4g' in t or '5g' in t: return 'Data'
    if s == 'telco' or 'sim' in t or 'nap-tien' in t: return 'Sim'
    if 'game' in t: return 'Game'
    if 'tiktok' in t: return 'Tiktok'
    if s == 'lottery' or 've-so' in t or 'vietlott' in t: return 'Vé Số'
    if s == 'student' or 'sinh-vien' in t or 'truong' in t: return 'Student Hub'
    if 'merchant' in t or 'doi-tac' in t: return 'Merchant'
    if 'soundbox' in t: return 'Soundbox'
    if 'trai-tim' in t or 'donation' in t or 'thien-nguyen' in t: return 'Donation'
    if s == 'trust' or 'bao-mat' in t or 'an-toan' in t: return 'Trust'
    if 'homepage' in t: return 'Home MoMo'
    if 'tai-app' in t or 'download' in t: return 'New User'
    if 'khuyen-mai' in t or 'uu-dai' in t: return 'Khuyến Mãi'
    if 'lifestyle' in t or 'tin-tuc' in t: return 'Tin Tức'
    if 'blog' in t: return 'Blog'
    return 'Other'

def build_theme_matcher():
    """Tạo bộ khớp Theme đa tầng tích hợp BigQuery WEB_DIM_PAGE_URL + Cluster URLs + Thư mục + Slug"""
    # 1. Nạp BigQuery WEB_DIM_PAGE_URL SSOT
    dim_file = BASE_DIR / "07_REPORTS" / "data" / "dim" / "web_dim_page_url.json"
    exact_dim = {}
    dynamic_dim = []
    if dim_file.exists():
        with open(dim_file, "r", encoding="utf-8") as f:
            dim_data = json.load(f)
        for r in dim_data.get("rules", []):
            proj = r.get("project_name", "").strip()
            ptype = r.get("page_type", "").strip()
            u = r.get("rule_url", "").replace("https://www.momo.vn", "").replace("http://www.momo.vn", "").replace("https://momo.vn", "")
            p = normalize_path(u)
            if "*" in p:
                dynamic_dim.append((p, proj, ptype))
            else:
                exact_dim[p] = (proj, ptype)

    # 2. Nạp Cluster URLs
    summary_file = HUBS_REPO / "data" / "seo-clusters-summary.json"
    if not summary_file.exists():
        summary_file = BASE_DIR / "07_REPORTS" / "data" / "inventory_clusters_summary.json"

    exact_map = {}
    prefix_rules = []

    if summary_file.exists():
        with open(summary_file, "r", encoding="utf-8") as f:
            clusters_data = json.load(f)

        for u in clusters_data.get("usecases", []):
            tid = u.get("id")
            tname = u.get("display_name") or u.get("name")
            sec = u.get("sector")
            mvol = u.get("total_volume", 0)
            
            top_url = u.get("cannibalization_shield", {}).get("top_live_url")
            if top_url:
                p = normalize_path(top_url)
                exact_map[p] = (tid, tname, sec, mvol)
                if p != "/":
                    prefix_rules.append((p, tid, tname, sec, mvol))

        prefix_rules.sort(key=lambda x: len(x[0]), reverse=True)

    # 3. Từ điển mapping 75 BigQuery Projects -> Hubs Theme & Sector
    project_to_theme = {
        "Cinema": ("ve-xem-phim", "Vé Xem Phim & Rạp", "cinema", 500000),
        "Ví Trả Sau": ("vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        "Ví Trả Sau (BNPL)": ("vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        "Vay Nhanh": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Vay nhanh": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Vay Nhanh & Vay Tín Chấp": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Thanh Toán Khoản Vay": ("vay-tin-chap", "Vay Nhanh", "Financial", 400000),
        "Trả Góp Apple": ("vi-tra-sau", "Ví Trả Sau", "Financial", 350000),
        "Mở Thẻ Tín Dụng": ("the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        "Thanh Toán Thẻ Tín Dụng": ("the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        "Điểm Tín Dụng": ("diem-tin-dung", "Điểm Tín Dụng", "Financial", 200000),
        "Điểm Tín Dụng & CIC": ("diem-tin-dung", "Điểm Tín Dụng", "Financial", 200000),
        "TnC": ("trust", "TnC", "trust", 100000),
        "Tnc": ("trust", "TnC", "trust", 100000),
        "Tiết Kiệm Online": ("gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        "Túi Thần Tài": ("gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        "Chứng Khoán": ("chung-khoan", "Chứng Khoán", "Financial", 200000),
        "Chứng Chỉ Quỹ": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Quỹ": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Sàn Đầu Tư": ("chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        "Giá Vàng": ("gia-vang", "Giá Vàng", "Financial", 800000),
        "Tiệm Vàng Online": ("gia-vang", "Giá Vàng", "Financial", 800000),
        "Tỷ Giá": ("ty-gia", "Tỷ Giá Ngoại Tệ", "Financial", 350000),
        "Mở tài khoản ngân hàng": ("chuyen-tien", "Mở Tài Khoản Ngân Hàng", "Financial", 300000),
        "Trung Tâm Tài Chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Trung Tâm tài chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Trung tâm tài chính": ("chuyen-tien", "Trung Tâm Tài Chính", "Financial", 300000),
        "Quản Lý Chi Tiêu": ("quan-ly-chi-tieu", "Quản Lý Chi Tiêu", "Financial", 150000),
        "Quản lý chi tiêu": ("quan-ly-chi-tieu", "Quản Lý Chi Tiêu", "Financial", 150000),
        "P2P": ("chuyen-tien", "Chuyển Tiền MoMo", "Financial", 300000),
        "Billpay": ("billpay-nuoc", "Thanh Toán Hóa Đơn", "Financial", 250000),
        "Điện": ("billpay-dien", "Thanh Toán Tiền Điện", "Financial", 250000),
        "Nước": ("billpay-nuoc", "Thanh Toán Tiền Nước", "Financial", 200000),
        "Bảo Hiểm Ô Tô": ("bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        "Bảo Hiểm Xe Máy": ("bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        "Bảo Hiểm Y Tế": ("bhyt", "Bảo Hiểm Y Tế (BHYT)", "insurtech", 180000),
        "Bảo Hiểm Xã Hội": ("bhxh", "Bảo Hiểm Xã Hội (BHXH)", "insurtech", 140000),
        "Bảo Hiểm Sức Khỏe": ("bao-hiem-nhan-tho", "Bảo Hiểm Sức Khỏe", "insurtech", 160000),
        "Bảo Hiểm": ("bao-hiem-nhan-tho", "Bảo Hiểm Tổng Hợp", "insurtech", 160000),
        "Phạt Nguội": ("phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        "Phạt nguội": ("phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        "Phí Không Dừng": ("thu-phi-khong-dung-etc", "Thu Phí Không Dừng ETC", "vehicle-hub", 150000),
        "Tiện Ích Giao Thông": ("dang-kiem", "Tiện Ích Giao Thông", "vehicle-hub", 200000),
        "Cây xăng": ("dang-kiem", "Cây Xăng & Tiện Ích Xe", "vehicle-hub", 200000),
        "Giá xăng": ("dang-kiem", "Giá Xăng Dầu", "vehicle-hub", 200000),
        "Trạm sạc": ("dang-kiem", "Trạm Sạc Xe Điện", "vehicle-hub", 200000),
        "OTA": ("ve-may-bay", "Vé Máy Bay & Du Lịch OTA", "ota", 600000),
        "Vé Xe": ("ve-xe-khach", "Vé Xe Khách", "ota", 350000),
        "Esim": ("esim-du-lich", "eSIM Du Lịch", "ota", 100000),
        "Game": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Game Hub": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Nạp thẻ Game": ("nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        "Tiktok": ("nap-xu-tiktok", "Nạp Xu TikTok", "Entertainment", 350000),
        "Data": ("nap-data-4g", "Nạp Data 3G/4G/5G", "telco", 500000),
        "Sim": ("sim-so-dep", "Sim Số Đẹp", "telco", 300000),
        "Student Hub": ("sinh-vien", "Sinh Viên Hub", "student", 150000),
        "Student Pass": ("sinh-vien", "Sinh Viên Hub", "student", 150000),
        "Vé số": ("ve-so-vietlott", "Vé Số & Vietlott", "Lottery", 400000),
        "Merchant": ("merchant-portal", "Cổng Đối Tác Doanh Nghiệp", "trust", 100000),
        "Soundbox": ("soundbox-momo", "Loa Thông Minh Soundbox", "trust", 80000),
        "Donation": ("trai-tim-momo", "Trái Tim MoMo - Thiện Nguyện", "trust", 120000),
        "Trust": ("bao-mat-momo", "Trung Tâm An Toàn & Bảo Mật", "trust", 150000),
        "TnC": ("bao-mat-momo", "Điều Khoản Sử Dụng", "trust", 100000),
        "Tnc": ("bao-mat-momo", "Điều Khoản Sử Dụng", "trust", 100000),
        "New User": ("tai-app-portal", "Download & Onboarding Center", "Brand", 500000),
        "Download": ("tai-app-portal", "Download & Onboarding Center", "Brand", 500000),
        "Home MoMo": ("homepage", "Trang Chủ MoMo", "Brand", 1500000),
        "Application Store": ("tai-app-portal", "Download Center", "Brand", 500000),
        "Campaign": ("promotion-campaign", "Chiến Dịch & Sự Kiện", "Promotion", 250000),
        "Khuyến mãi": ("promotion-news", "Tin Khuyến Mãi & Ưu Đãi", "Promotion", 250000),
        "Hoàn Tiền Mua Sắm": ("promotion-news", "Hoàn Tiền Mua Sắm", "Promotion", 200000),
        "XU": ("promotion-news", "Tích Xu Đổi Quà", "Promotion", 200000),
        "Dịch Vụ Liên Kết": ("dich-vu-lien-ket", "Dịch Vụ Liên Kết", "Other", 100000),
        "Dịch vụ liên kết": ("dich-vu-lien-ket", "Dịch Vụ Liên Kết", "Other", 100000),
        "Cross Border": ("dich-vu-lien-ket", "Thanh Toán Quốc Tế", "Other", 100000),
        "Hỏi đáp": ("customer-support", "Hỏi Đáp Trợ Giúp", "Support", 150000),
        "Guide": ("huong-dan-momo", "Hướng Dẫn Sử Dụng", "Support", 150000),
        "Tìm Kiếm": ("customer-support", "Tìm Kiếm Trợ Giúp", "Support", 100000),
        "Tin Tức": ("lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000),
        "Blog": ("lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000),
    }

    # 4. Từ điển thư mục và slug chuẩn
    dir_rules = [
        ("/cinema", "ve-xem-phim", "Vé Xem Phim & Rạp", "cinema", 500000),
        ("/vi-tra-sau", "vi-tra-sau", "Ví Trả Sau", "Financial", 450000),
        ("/vay-nhanh", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("/diem-tin-dung", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("/nap-xu-tiktok", "nap-xu-tiktok", "Nạp Xu TikTok", "Entertainment", 350000),
        ("/bao-hiem-o-to", "bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        ("/bao-hiem-xe-may", "bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        ("/bao-hiem-y-te", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("/bao-hiem-xa-hoi", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("/phat-nguoi", "phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        ("/ve-xe", "ve-xe-khach", "Vé Xe Khách", "ota", 350000),
        ("/ve-tau", "ve-tau-hoa", "Vé Tàu Hỏa", "ota", 250000),
        ("/ve-may-bay", "ve-may-bay", "Vé Máy Bay", "ota", 600000),
        ("/esim", "esim-du-lich", "eSIM Du Lịch", "ota", 100000),
        ("/sinh-vien", "sinh-vien", "Sinh Viên Hub", "student", 150000),
        ("/nap-the-game", "nap-the-game", "Nạp Thẻ Game", "Entertainment", 500000),
        ("/nuoc", "billpay-nuoc", "Thanh Toán Tiền Nước", "Financial", 200000),
        ("/dien", "billpay-dien", "Thanh Toán Tiền Điện", "Financial", 250000),
        ("/tai-app", "tai-app-portal", "Download Center", "Brand", 500000),
        ("/download", "tai-app-portal", "Download Center", "Brand", 500000),
        ("/", "homepage", "Trang Chủ MoMo", "Brand", 1500000),
    ]

    # Keyword slug rules cho blog/tin tức
    slug_rules = [
        ("vi-tra-sau", "vi-tra-sau", "Ví Trả Sau (BNPL)", "Financial", 450000),
        ("vay-nhanh", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("vay-tin-chap", "vay-tin-chap", "Vay Nhanh & Vay Tín Chấp", "Financial", 400000),
        ("diem-tin-dung", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("cic", "diem-tin-dung", "Điểm Tín Dụng & CIC", "Financial", 200000),
        ("bao-hiem-o-to", "bao-hiem-o-to", "Bảo Hiểm Ô Tô", "insurtech", 150000),
        ("bao-hiem-xe-may", "bao-hiem-xe-may", "Bảo Hiểm Xe Máy", "insurtech", 120000),
        ("bao-hiem-y-te", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("bao-hiem-xa-hoi", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("bao-hiem-nhan-tho", "bao-hiem-nhan-tho", "Bảo Hiểm Nhân Thọ", "insurtech", 160000),
        ("bao-hiem-tai-nan", "bao-hiem-tai-nan", "Bảo Hiểm Tai Nạn", "insurtech", 100000),
        ("gia-vang", "gia-vang", "Giá Vàng", "Financial", 800000),
        ("lai-suat", "gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        ("tiet-kiem", "gui-tiet-kiem", "Gửi Tiết Kiệm & Lãi Suất", "Financial", 400000),
        ("ty-gia", "ty-gia", "Tỷ Giá Ngoại Tệ", "Financial", 350000),
        ("the-tin-dung", "the-tin-dung", "Mở Thẻ Tín Dụng", "Financial", 250000),
        ("chung-khoan", "chung-khoan", "Chứng Khoán", "Financial", 200000),
        ("chung-chi-quy", "chung-chi-quy", "Chứng Chỉ Quỹ", "Financial", 100000),
        ("bhyt", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("bhxh", "bhxh", "Bảo Hiểm Xã Hội", "insurtech", 140000),
        ("tra-cuu-bao-hiem", "bhyt", "Bảo Hiểm Y Tế", "insurtech", 180000),
        ("phat-nguoi", "phat-nguoi", "Tra Cứu Phạt Nguội", "vehicle-hub", 800000),
        ("dang-kiem", "dang-kiem", "Đăng Kiểm Xe", "vehicle-hub", 200000),
        ("chuyen-tien", "chuyen-tien", "Chuyển Tiền MoMo", "Financial", 300000),
        ("hoc-phi", "sinh-vien", "Sinh Viên Hub", "student", 150000),
        ("du-lich", "du-lich-tong-hop", "Cẩm Nang Du Lịch", "ota", 300000),
        ("khuyen-mai", "promotion-news", "Tin Khuyến Mãi", "Promotion", 250000),
    ]

    def match(path):
        p = path.lower()
        dim_proj = None
        dim_ptype = None

        # Tier 1A: Tra cứu BigQuery DIM exact match
        if p in exact_dim:
            dim_proj, dim_ptype = exact_dim[p]
        else:
            # Tra cứu BigQuery DIM dynamic wildcard
            for pat, pr, pt in dynamic_dim:
                if fnmatch.fnmatch(p, pat) or fnmatch.fnmatch(p + "/", pat):
                    dim_proj, dim_ptype = pr, pt
                    break

        # Nếu DIM khớp một Project nghiệp vụ cụ thể (không phải Blog/Tin tức/Hỏi đáp chung)
        if dim_proj and dim_proj in project_to_theme and dim_proj not in ["Blog", "Tin Tức", "Hỏi đáp", "Hỏi Đáp"]:
            tid, tname, sec, mvol = project_to_theme[dim_proj]
            return tid, tname, sec, mvol, clean_dim_project(dim_proj), dim_ptype or "Page"

        # Tier 1B: Khớp chính xác Cluster URL
        if p in exact_map:
            tid, tname, sec, mvol = exact_map[p]
            resolved_proj = resolve_dim_project_name(dim_proj, tid, sec)
            return tid, tname, sec, mvol, resolved_proj, dim_ptype or "Landing Page"

        # Tier 2: Khớp prefix cluster URL
        for prefix, tid, tname, sec, mvol in prefix_rules:
            if p.startswith(prefix + "/"):
                resolved_proj = resolve_dim_project_name(dim_proj, tid, sec)
                return tid, tname, sec, mvol, resolved_proj, dim_ptype or "Page"

        # Tier 3: Khớp thư mục trực tiếp
        for prefix, tid, tname, sec, mvol in dir_rules:
            if p == prefix or p.startswith(prefix + "/"):
                resolved_proj = resolve_dim_project_name(dim_proj, tid, sec)
                return tid, tname, sec, mvol, resolved_proj, dim_ptype or "Page"

        # Tier 4: Khớp slug keyword
        for slug, tid, tname, sec, mvol in slug_rules:
            if slug in p:
                resolved_proj = resolve_dim_project_name(dim_proj, tid, sec)
                return tid, tname, sec, mvol, resolved_proj, dim_ptype or "Blog"

        # Tier 5: Fallback từ DIM nếu là Blog, Tin tức, Hỏi đáp
        if dim_proj and dim_proj in project_to_theme:
            tid, tname, sec, mvol = project_to_theme[dim_proj]
            return tid, tname, sec, mvol, clean_dim_project(dim_proj), dim_ptype or "Page"

        # Tier 6: Fallback Hub theo tiền tố
        if p.startswith("/tin-tuc") or p.startswith("/blog"):
            return "lifestyle-news", "Tin Tức & Đời Sống", "Lifestyle", 200000, "Blog", "Blog"
        if p.startswith("/hoi-dap"):
            return "customer-support", "Hỏi Đáp Trợ Giúp", "Support", 150000, "Hỏi Đáp", "Hỏi đáp"
            
        return None, None, "Other", 0, "Other", "Unknown"

    return match

def main():
    start_time = time.time()
    print("=" * 70)
    print("KHỞI CHẠY PIPELINE PHÂN RÃ HỢP NHẤT DỮ LIỆU GA4 & GSC (V2 REFACTORED)")
    print(f"Chu kỳ phân tích SSOT: {DATE_START} -> {DATE_END}")
    print("=" * 70)

    # 1. Nạp và xử lý GA4
    print("[1/5] Kéo dữ liệu GA4 Organic Search, Multi-Channel & Onelink...")
    res_org, res_ai, res_momo, res_af = fetch_ga4_organic_data()
    multi_data = fetch_ga4_multichannel_data()

    ga4_pages = {}
    for r in res_org.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        pv = int(r["metricValues"][0]["value"])
        sess = int(r["metricValues"][1]["value"])
        eng = int(r["metricValues"][2]["value"])
        if p not in ga4_pages:
            ga4_pages[p] = {"organic_pageviews": 0, "organic_sessions": 0, "engaged_sessions": 0, "ai_sessions": 0, "ol_momo": 0, "ol_appsflyer": 0}
        ga4_pages[p]["organic_pageviews"] += pv
        ga4_pages[p]["organic_sessions"] += sess
        ga4_pages[p]["engaged_sessions"] += eng

    for r in res_ai.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        sess = int(r["metricValues"][0]["value"])
        if p in ga4_pages:
            ga4_pages[p]["ai_sessions"] += sess

    for r in res_momo.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cnt = int(r["metricValues"][0]["value"])
        if p in ga4_pages:
            ga4_pages[p]["ol_momo"] += cnt

    for r in res_af.get("rows", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cnt = int(r["metricValues"][0]["value"])
        if p in ga4_pages:
            ga4_pages[p]["ol_appsflyer"] += cnt

    print(f"✓ Đã tổng hợp {len(ga4_pages):,} Organic Landing Pages từ GA4.")

    # 2. Nạp và xử lý GSC đúng kỳ
    print("[2/5] Kéo và tổng hợp dữ liệu Google Search Console (Pre-Click)...")
    gsc_raw_rows = fetch_gsc_30d_data()

    gsc_by_page = {}
    total_gsc_clicks = 0
    total_gsc_imp = 0
    query_to_pages = defaultdict(list)

    for r in gsc_raw_rows:
        raw_url = r["keys"][0]
        q = r["keys"][1]
        c = r.get("clicks", 0)
        im = r.get("impressions", 0)
        pos = r.get("position", 0.0)

        total_gsc_clicks += c
        total_gsc_imp += im

        p = normalize_path(raw_url)
        query_to_pages[q.strip().lower()].append((p, c, im, pos))

        if p not in gsc_by_page:
            gsc_by_page[p] = {
                "clicks": 0,
                "impressions": 0,
                "weighted_pos": 0.0,
                "queries": [],
                "strike_zone_queries": []
            }
        gsc_by_page[p]["clicks"] += c
        gsc_by_page[p]["impressions"] += im
        gsc_by_page[p]["weighted_pos"] += pos * im

        is_brand = is_brand_query(q)
        if c > 0 or im >= 100:
            gsc_by_page[p]["queries"].append({
                "query": q,
                "clicks": c,
                "impressions": im,
                "position": round(pos, 1),
                "is_brand": is_brand
            })

        # Strike Zone: Vị trí 4.0 - 10.0, Impressions >= 100, KHÔNG phải Brand/Navigational/Typo
        if 4.0 <= pos <= 10.0 and im >= 100 and not is_brand:
            actual_ctr = c / im if im else 0.0
            target_ctr = CTR_BENCHMARK_TABLE["benchmark_position_3_target_ctr"]
            ctr_diff = max(0.0, target_ctr - actual_ctr)
            raw_gain = int(im * ctr_diff)
            gsc_by_page[p]["strike_zone_queries"].append({
                "query": q,
                "clicks": c,
                "impressions": im,
                "position": round(pos, 1),
                "potential_gain_clicks": raw_gain
            })

    # Phân tích Keyword Cannibalization: Các query có từ 2 URL trở lên cùng nhận traffic đáng kể
    cannibal_query_map = {}
    for q_norm, plist in query_to_pages.items():
        if len(plist) >= 2:
            sig = [item for item in plist if item[2] >= 50 or item[1] >= 2]
            if len(sig) >= 2:
                cannibal_query_map[q_norm] = sig

    page_cannibal_info = defaultdict(lambda: {"count": 0, "total_imp": 0, "queries": []})
    for q_norm, sig_pages in cannibal_query_map.items():
        for p_norm, c_norm, im_norm, pos_norm in sig_pages:
            page_cannibal_info[p_norm]["count"] += 1
            page_cannibal_info[p_norm]["total_imp"] += im_norm
            if len(page_cannibal_info[p_norm]["queries"]) < 5:
                page_cannibal_info[p_norm]["queries"].append(q_norm)

    print(f"✓ Đã tổng hợp {len(gsc_by_page):,} Pages từ {len(gsc_raw_rows):,} dòng GSC.")
    print(f"✓ Phát hiện {len(cannibal_query_map):,} queries và {len(page_cannibal_info):,} pages có hiện tượng Keyword Cannibalization.")

    # 3. Tính Join Rate & Mapped Rate
    print("[3/5] Tính toán Join Rate và độ phủ Theme...")
    matcher = build_theme_matcher()

    # Tính join rate trên tập trang GSC có traffic (clicks > 0)
    # Vì trang 0-click trên SERP người dùng không bấm vào thì GA4 Organic Search Landing Page không thể có session
    pages_with_gsc = set(gsc_by_page.keys())
    pages_with_gsc_traffic = {p for p, d in gsc_by_page.items() if d["clicks"] > 0}
    pages_with_both = pages_with_gsc_traffic.intersection(set(ga4_pages.keys()))
    join_rate = round(len(pages_with_both) / len(pages_with_gsc_traffic), 4) if pages_with_gsc_traffic else 0.0
    print(f"✓ GSC Pages (Clicks > 0): {len(pages_with_gsc_traffic):,} | Pages joined GA4: {len(pages_with_both):,} | Join Rate: {join_rate * 100:.2f}% (Mục tiêu > 90%)")

    total_organic_sessions = sum(v["organic_sessions"] for v in ga4_pages.values())
    mapped_organic_sessions = 0
    for p, g in ga4_pages.items():
        tid, _, _, _, _, _ = matcher(p)
        if tid is not None:
            mapped_organic_sessions += g["organic_sessions"]
    organic_mapped_pct = round(mapped_organic_sessions / total_organic_sessions, 4) if total_organic_sessions else 0.0
    print(f"✓ Total Organic Sessions: {total_organic_sessions:,} | Mapped: {mapped_organic_sessions:,} | Mapped Rate: {organic_mapped_pct * 100:.2f}% (Mục tiêu > 70%)")

    # 4. Phân loại 4 Quadrant & Xây dựng Danh sách Pages Phân tích
    print("[4/5] Xây dựng Ma trận 4 Quadrant và Danh mục Quick Wins...")
    
    # Chỉ giữ các trang có ý nghĩa phân tích (GSC clicks >= 5 hoặc GA4 organic sessions >= 10 hoặc đã map Theme)
    candidate_paths = [p for p in pages_with_gsc if gsc_by_page[p]["clicks"] >= 5 or ga4_pages.get(p, {}).get("organic_sessions", 0) >= 10 or matcher(p)[0] is not None]
    
    pages_output = []
    quick_wins_map = {}  # key: path -> best quick win query
    quadrant_summary = {
        "CORE_DRIVER": 0,
        "STRIKE_ZONE_QUICK_WIN": 0,
        "LEAKING_BUCKET": 0,
        "CANNIBALIZATION_RISK": 0,
        "STANDARD": 0
    }

    for p in candidate_paths:
        gsc = gsc_by_page[p]
        ga4 = ga4_pages.get(p, {"organic_pageviews": 0, "organic_sessions": 0, "engaged_sessions": 0, "ai_sessions": 0, "ol_momo": 0, "ol_appsflyer": 0})
        
        tid, tname, sec, mvol, proj_name, page_type = matcher(p)
        priority_sec = is_priority_sector(sec, p)

        gsc_c = gsc["clicks"]
        gsc_imp = gsc["impressions"]
        avg_pos = round(gsc["weighted_pos"] / gsc_imp, 1) if gsc_imp else 0.0
        gsc_ctr = round(gsc_c / gsc_imp, 4) if gsc_imp else 0.0

        org_pv = ga4.get("organic_pageviews", 0)
        org_sess = ga4["organic_sessions"]
        eng_sess = ga4["engaged_sessions"]
        eng_rate = round(eng_sess / org_sess, 4) if org_sess else 0.0
        ol_m = ga4["ol_momo"]
        ol_af = ga4["ol_appsflyer"]
        w2a_clicks = ol_m + ol_af
        w2a_cr = round(w2a_clicks / org_sess, 4) if org_sess else 0.0

        capture_rate = round(org_sess / mvol, 4) if mvol else 0.0
        business_yield = round(w2a_clicks / gsc_c, 4) if gsc_c else 0.0

        # Áp trần market_volume cho potential_gain
        strike_q = gsc["strike_zone_queries"]
        for sq in strike_q:
            if mvol > 0:
                sq["potential_gain_clicks"] = min(sq["potential_gain_clicks"], mvol)

        strike_q_sorted = sorted(strike_q, key=lambda x: x["potential_gain_clicks"], reverse=True)
        total_potential_gain = sum(x["potential_gain_clicks"] for x in strike_q_sorted)
        if mvol > 0:
            total_potential_gain = min(total_potential_gain, mvol)

        # Phân tích rủi ro cannibalization cho trang
        c_info = page_cannibal_info.get(p, {"count": 0, "total_imp": 0, "queries": []})
        c_cnt = c_info["count"]
        c_imp = c_info["total_imp"]

        # Phân loại Quadrant nghiêm ngặt theo giá trị thực tế
        if gsc_c >= 500 and w2a_cr >= 0.05:
            quadrant = "CORE_DRIVER"
        elif total_potential_gain >= 1000 or (len(strike_q) >= 2 and gsc_imp >= 5000):
            quadrant = "STRIKE_ZONE_QUICK_WIN"
        elif gsc_c >= 500 and w2a_cr < 0.01:
            quadrant = "LEAKING_BUCKET"
        elif c_cnt >= 3 and c_imp >= 1000:
            quadrant = "CANNIBALIZATION_RISK"
        else:
            quadrant = "STANDARD"

        quadrant_summary[quadrant] += 1

        top_queries = sorted(gsc["queries"], key=lambda x: x["clicks"], reverse=True)[:5]

        page_record = {
            "path": p,
            "project_name": proj_name,
            "page_type": page_type,
            "theme_id": tid,
            "theme_name": tname,
            "sector": sec,
            "priority_sector": priority_sec,
            "market_volume": mvol,
            "quadrant": quadrant,
            "pre_click": {
                "gsc_clicks": gsc_c,
                "gsc_impressions": gsc_imp,
                "avg_position": avg_pos,
                "ctr": gsc_ctr,
                "top_queries": top_queries,
                "strike_zone_count": len(strike_q),
                "potential_additional_clicks": total_potential_gain,
                "cannibal_queries_count": c_cnt,
                "cannibal_impressions": c_imp
            },
            "post_click": {
                "organic_pageviews": org_pv,
                "organic_sessions": org_sess,
                "engaged_sessions": eng_sess,
                "engagement_rate": eng_rate,
                "ai_sessions": ga4["ai_sessions"]
            },
            "conversion": {
                "ol_momo": ol_m,
                "ol_appsflyer": ol_af,
                "total_w2a_clicks": w2a_clicks,
                "w2a_conversion_rate": w2a_cr,
                "business_yield": business_yield,
                "capture_rate": capture_rate
            }
        }
        pages_output.append(page_record)

        # Trích xuất Quick Win duy nhất cho mỗi Path
        if strike_q_sorted and (w2a_cr >= 0.01 or priority_sec or gsc_c >= 50):
            best_q = strike_q_sorted[0]
            quick_wins_map[p] = {
                "query": best_q["query"],
                "path": p,
                "project_name": proj_name,
                "page_type": page_type,
                "theme_id": tid,
                "theme_name": tname,
                "sector": sec,
                "priority_sector": priority_sec,
                "current_position": best_q["position"],
                "impressions": best_q["impressions"],
                "current_clicks": best_q["clicks"],
                "potential_gain_clicks": best_q["potential_gain_clicks"],
                "w2a_conversion_rate": w2a_cr,
                "ol_appsflyer": ol_af,
                "ol_momo": ol_m
            }

    # Sắp xếp pages
    pages_output.sort(key=lambda x: (x["conversion"]["total_w2a_clicks"], x["pre_click"]["gsc_clicks"]), reverse=True)

    # Sắp xếp Quick Wins: ưu tiên priority_sector (True lên trước), sau đó theo potential_gain_clicks
    quick_wins_list = list(quick_wins_map.values())
    quick_wins_list.sort(key=lambda x: (x["priority_sector"], x["potential_gain_clicks"], x["w2a_conversion_rate"]), reverse=True)
    top_quick_wins = quick_wins_list[:100]

    # 5. Tổng hợp cấp Theme (129 Themes)
    themes_agg = {}
    for p_rec in pages_output:
        tid = p_rec["theme_id"]
        if not tid:
            continue
        if tid not in themes_agg:
            themes_agg[tid] = {
                "theme_id": tid,
                "theme_name": p_rec["theme_name"],
                "sector": p_rec["sector"],
                "priority_sector": p_rec["priority_sector"],
                "market_volume": p_rec["market_volume"],
                "primary_path": p_rec["path"],
                "gsc_clicks": 0,
                "gsc_impressions": 0,
                "organic_sessions": 0,
                "ai_sessions": 0,
                "ol_momo": 0,
                "ol_appsflyer": 0,
                "w2a_clicks": 0,
                "potential_gain": 0,
                "quadrant": p_rec["quadrant"]
            }
        t = themes_agg[tid]
        t["gsc_clicks"] += p_rec["pre_click"]["gsc_clicks"]
        t["gsc_impressions"] += p_rec["pre_click"]["gsc_impressions"]
        t["organic_sessions"] += p_rec["post_click"]["organic_sessions"]
        t["ai_sessions"] += p_rec["post_click"]["ai_sessions"]
        t["ol_momo"] += p_rec["conversion"]["ol_momo"]
        t["ol_appsflyer"] += p_rec["conversion"]["ol_appsflyer"]
        t["w2a_clicks"] += p_rec["conversion"]["total_w2a_clicks"]
        t["potential_gain"] += p_rec["pre_click"]["potential_additional_clicks"]

    themes_list = list(themes_agg.values())
    for t in themes_list:
        if t["market_volume"] > 0:
            t["potential_gain"] = min(t["potential_gain"], t["market_volume"])
        t["capture_rate"] = round(t["organic_sessions"] / t["market_volume"], 4) if t["market_volume"] else 0.0
        t["w2a_cr"] = round(t["w2a_clicks"] / t["organic_sessions"], 4) if t["organic_sessions"] else 0.0

    themes_list.sort(key=lambda x: (x["priority_sector"], x["w2a_clicks"], x["gsc_clicks"]), reverse=True)

    # Tính toán bảng tổng hợp hiệu suất theo từng Dự án BigQuery (projects_summary)
    projects_agg = {}
    for p_rec in pages_output:
        proj = p_rec.get("project_name", "Unknown")
        if proj not in projects_agg:
            projects_agg[proj] = {
                "project_name": proj,
                "pages_count": 0,
                "organic_pageviews": 0,
                "organic_sessions": 0,
                "gsc_clicks": 0,
                "gsc_impressions": 0,
                "ol_momo": 0,
                "ol_appsflyer": 0,
                "total_w2a_clicks": 0,
                "ai_sessions": 0,
                "page_types": {},
                "top_pages": []
            }
        pa = projects_agg[proj]
        pa["pages_count"] += 1
        pa["organic_pageviews"] += p_rec["post_click"].get("organic_pageviews", 0)
        pa["organic_sessions"] += p_rec["post_click"].get("organic_sessions", 0)
        pa["gsc_clicks"] += p_rec["pre_click"].get("gsc_clicks", 0)
        pa["gsc_impressions"] += p_rec["pre_click"].get("gsc_impressions", 0)
        pa["ol_momo"] += p_rec["conversion"].get("ol_momo", 0)
        pa["ol_appsflyer"] += p_rec["conversion"].get("ol_appsflyer", 0)
        pa["total_w2a_clicks"] += p_rec["conversion"].get("total_w2a_clicks", 0)
        pa["ai_sessions"] += p_rec["post_click"].get("ai_sessions", 0)
        pt = p_rec.get("page_type", "Other")
        pa["page_types"][pt] = pa["page_types"].get(pt, 0) + 1
        pa["top_pages"].append({
            "path": p_rec["path"],
            "page_type": pt,
            "organic_pageviews": p_rec["post_click"].get("organic_pageviews", 0),
            "organic_sessions": p_rec["post_click"].get("organic_sessions", 0),
            "w2a_clicks": p_rec["conversion"].get("total_w2a_clicks", 0)
        })

    # 5. Xử lý dữ liệu Đa Kênh GA4 & Gắn vào Projects Summary (Hỗ trợ cả Pageviews & Sessions)
    print("[4.5/5] Xử lý phân rã Đa Kênh Pageviews & Sessions (Non-Paid vs Paid)...")
    channel_w2a_map = {}
    for r in multi_data.get("channels_w2a", []):
        cg = r["dimensionValues"][0]["value"]
        cnt = int(r["metricValues"][0]["value"])
        channel_w2a_map[cg] = cnt

    total_web_pageviews = 0
    total_web_sessions = 0
    total_web_users = 0
    total_web_w2a = sum(channel_w2a_map.values())
    channels_summary = []

    for r in multi_data.get("channels_overview", []):
        cg = r["dimensionValues"][0]["value"]
        pv = int(r["metricValues"][0]["value"])
        s = int(r["metricValues"][1]["value"])
        eng = int(r["metricValues"][2]["value"])
        u = int(r["metricValues"][3]["value"])
        w2a = channel_w2a_map.get(cg, 0)
        total_web_pageviews += pv
        total_web_sessions += s
        total_web_users += u
        channels_summary.append({
            "channel_name": cg,
            "category": "Paid" if is_paid_channel(cg) else "Non-Paid",
            "pageviews": pv,
            "sessions": s,
            "engaged_sessions": eng,
            "users": u,
            "w2a_clicks": w2a,
            "w2a_cr": round(w2a / s, 4) if s > 0 else 0.0
        })

    for c in channels_summary:
        c["pageviews_pct"] = round(c["pageviews"] / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0
        c["sessions_pct"] = round(c["sessions"] / total_web_sessions, 4) if total_web_sessions > 0 else 0.0

    channels_summary.sort(key=lambda x: (0 if x["category"] == "Non-Paid" else 1, -x["pageviews"]))

    tot_non_paid_pv = sum(c["pageviews"] for c in channels_summary if c["category"] == "Non-Paid")
    tot_paid_pv = sum(c["pageviews"] for c in channels_summary if c["category"] == "Paid")
    tot_non_paid_s = sum(c["sessions"] for c in channels_summary if c["category"] == "Non-Paid")
    tot_paid_s = sum(c["sessions"] for c in channels_summary if c["category"] == "Paid")
    tot_non_paid_w = sum(c["w2a_clicks"] for c in channels_summary if c["category"] == "Non-Paid")
    tot_paid_w = sum(c["w2a_clicks"] for c in channels_summary if c["category"] == "Paid")

    # Map Landing Page x Channel vào Project
    lp_w2a_map = defaultdict(int)
    for r in multi_data.get("landing_page_w2a", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cg = r["dimensionValues"][1]["value"]
        w = int(r["metricValues"][0]["value"])
        lp_w2a_map[(p, cg)] += w

    project_multi_map = defaultdict(lambda: {
        "pageviews": 0, "sessions": 0, "w2a": 0, "pages": set(),
        "channels": defaultdict(lambda: {"pageviews": 0, "sessions": 0, "w2a": 0}),
        "non_paid_pageviews": 0, "paid_pageviews": 0,
        "non_paid_sessions": 0, "paid_sessions": 0,
        "non_paid_w2a": 0, "paid_w2a": 0
    })

    for r in multi_data.get("landing_page_channels", []):
        p = normalize_path(r["dimensionValues"][0]["value"])
        cg = r["dimensionValues"][1]["value"]
        pv = int(r["metricValues"][0]["value"])
        s = int(r["metricValues"][1]["value"])
        w = lp_w2a_map.get((p, cg), 0)

        tid, tname, sec, mvol, proj, ptype = matcher(p)
        pm = project_multi_map[proj]
        pm["pageviews"] += pv
        pm["sessions"] += s
        pm["w2a"] += w
        pm["pages"].add(p)
        pm["channels"][cg]["pageviews"] += pv
        pm["channels"][cg]["sessions"] += s
        pm["channels"][cg]["w2a"] += w

        if is_paid_channel(cg):
            pm["paid_pageviews"] += pv
            pm["paid_sessions"] += s
            pm["paid_w2a"] += w
        else:
            pm["non_paid_pageviews"] += pv
            pm["non_paid_sessions"] += s
            pm["non_paid_w2a"] += w

    # Đảm bảo mọi project có trong project_multi_map đều có trong projects_agg
    for proj, p_info in project_multi_map.items():
        if proj not in projects_agg:
            projects_agg[proj] = {
                "project_name": proj,
                "pages_count": len(p_info["pages"]),
                "organic_pageviews": 0,
                "organic_sessions": 0,
                "gsc_clicks": 0,
                "gsc_impressions": 0,
                "ol_momo": 0,
                "ol_appsflyer": 0,
                "total_w2a_clicks": 0,
                "ai_sessions": 0,
                "page_types": {},
                "top_pages": []
            }

    projects_list = list(projects_agg.values())
    project_channel_matrix = []

    for pa in projects_list:
        proj = pa["project_name"]
        p_info = project_multi_map.get(proj, {
            "pageviews": pa["organic_pageviews"], "sessions": pa["organic_sessions"], "w2a": pa["total_w2a_clicks"],
            "pages": set(), "channels": {"Organic Search": {"pageviews": pa["organic_pageviews"], "sessions": pa["organic_sessions"], "w2a": pa["total_w2a_clicks"]}},
            "non_paid_pageviews": pa["organic_pageviews"], "paid_pageviews": 0,
            "non_paid_sessions": pa["organic_sessions"], "paid_sessions": 0,
            "non_paid_w2a": pa["total_w2a_clicks"], "paid_w2a": 0
        })

        pv = p_info["pageviews"] if p_info["pageviews"] > 0 else pa["organic_pageviews"]
        s = p_info["sessions"] if p_info["sessions"] > 0 else pa["organic_sessions"]
        w = p_info["w2a"] if p_info["w2a"] > 0 else pa["total_w2a_clicks"]
        non_paid_pv = p_info["non_paid_pageviews"]
        paid_pv = p_info["paid_pageviews"]
        non_paid_pv_pct = round(non_paid_pv / pv, 4) if pv > 0 else 1.0
        paid_pv_pct = round(paid_pv / pv, 4) if pv > 0 else 0.0

        non_paid_s = p_info["non_paid_sessions"]
        paid_s = p_info["paid_sessions"]
        non_paid_pct = round(non_paid_s / s, 4) if s > 0 else 1.0
        paid_pct = round(paid_s / s, 4) if s > 0 else 0.0

        if non_paid_pv_pct >= 0.8:
            health = "ORGANIC_LED"
        elif paid_pv_pct >= 0.5:
            health = "PAID_LED"
        else:
            health = "MIXED"

        pa["total_pageviews"] = pv
        pa["pageviews_share_pct"] = round(pv / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0
        pa["total_sessions"] = s
        pa["sessions_share_pct"] = round(s / total_web_sessions, 4) if total_web_sessions > 0 else 0.0
        pa["total_w2a_clicks"] = w
        pa["w2a_cr"] = round(w / s, 4) if s > 0 else 0.0
        pa["non_paid_pageviews"] = non_paid_pv
        pa["non_paid_pv_pct"] = non_paid_pv_pct
        pa["paid_pageviews"] = paid_pv
        pa["paid_pv_pct"] = paid_pv_pct
        pa["non_paid_sessions"] = non_paid_s
        pa["non_paid_pct"] = non_paid_pct
        pa["paid_sessions"] = paid_s
        pa["paid_pct"] = paid_pct
        pa["health_status"] = health

        if len(p_info["pages"]) > pa["pages_count"]:
            pa["pages_count"] = len(p_info["pages"])

        # Format channels dict
        ch_dict = {}
        for cname, cdata in sorted(p_info["channels"].items(), key=lambda x: -x[1]["pageviews"]):
            cpv = cdata["pageviews"]
            cs = cdata["sessions"]
            cw = cdata["w2a"]
            ch_dict[cname] = {
                "pageviews": cpv,
                "sessions": cs,
                "w2a_clicks": cw,
                "w2a_cr": round(cw / cs, 4) if cs > 0 else 0.0,
                "pv_pct": round(cpv / pv, 4) if pv > 0 else 0.0,
                "session_pct": round(cs / s, 4) if s > 0 else 0.0
            }
        pa["channels"] = ch_dict

        pa["top_pages"].sort(key=lambda x: x.get("organic_pageviews", x["organic_sessions"]), reverse=True)
        pa["top_pages"] = pa["top_pages"][:3]

        # Row for Project x Channel Matrix table (Ưu tiên Pageviews)
        project_channel_matrix.append({
            "project_name": proj,
            "total_pageviews": pv,
            "pageviews_share_pct": pa["pageviews_share_pct"],
            "total_sessions": s,
            "sessions_share_pct": pa["sessions_share_pct"],
            "non_paid_pv_pct": non_paid_pv_pct,
            "paid_pv_pct": paid_pv_pct,
            "non_paid_pct": non_paid_pct,
            "paid_pct": paid_pct,
            "organic_pageviews": ch_dict.get("Organic Search", {}).get("pageviews", 0),
            "direct_pageviews": ch_dict.get("Direct", {}).get("pageviews", 0),
            "paid_search_pageviews": ch_dict.get("Paid Search", {}).get("pageviews", 0),
            "paid_social_pageviews": ch_dict.get("Paid Social", {}).get("pageviews", 0),
            "referral_pageviews": ch_dict.get("Referral", {}).get("pageviews", 0),
            "unassigned_pageviews": ch_dict.get("Unassigned", {}).get("pageviews", 0),
            "organic_search": ch_dict.get("Organic Search", {}).get("sessions", 0),
            "direct": ch_dict.get("Direct", {}).get("sessions", 0),
            "paid_search": ch_dict.get("Paid Search", {}).get("sessions", 0),
            "paid_social": ch_dict.get("Paid Social", {}).get("sessions", 0),
            "referral": ch_dict.get("Referral", {}).get("sessions", 0),
            "unassigned": ch_dict.get("Unassigned", {}).get("sessions", 0),
            "total_w2a": w,
            "w2a_cr": pa["w2a_cr"],
            "health_status": health,
            "pages_count": pa["pages_count"]
        })

    # Sort projects list and matrix by total_pageviews descending
    projects_list.sort(key=lambda x: -x.get("total_pageviews", x["organic_sessions"]))
    project_channel_matrix.sort(key=lambda x: -x["total_pageviews"])

    # Đảm bảo tổng quadrant khớp 100%
    total_analyzed = len(pages_output)
    assert sum(quadrant_summary.values()) == total_analyzed, "Lỗi: Tổng quadrant_distribution không bằng total_pages_analyzed"

    # Đóng gói JSON Payload
    output_payload = {
        "title": "MoMo Web Platform Full-Funnel Decomposition Matrix (GSC + GA4)",
        "generated_at": datetime.now().isoformat(),
        "periods": {
            "ga4": {"start": DATE_START, "end": DATE_END},
            "gsc": {"start": DATE_START, "end": DATE_END}
        },
        "ctr_benchmark_table": CTR_BENCHMARK_TABLE,
        "summary": {
            "total_pages_analyzed": total_analyzed,
            "total_themes_analyzed": len(themes_list),
            "total_projects_analyzed": len(projects_list),
            "join_rate": join_rate,
            "gsc_pages_with_traffic": len(pages_with_gsc_traffic),
            "joined_pages_count": len(pages_with_both),
            "total_gsc_raw_pages": len(gsc_by_page),
            "organic_mapped_pct": organic_mapped_pct,
            "total_gsc_clicks": total_gsc_clicks,
            "total_gsc_impressions": total_gsc_imp,
            "total_organic_pageviews": sum(p["post_click"].get("organic_pageviews", 0) for p in pages_output),
            "total_organic_sessions": total_organic_sessions,
            "total_gsc_mapped_sessions": total_organic_sessions,
            "total_ol_momo": sum(p["conversion"]["ol_momo"] for p in pages_output),
            "total_ol_appsflyer": sum(p["conversion"]["ol_appsflyer"] for p in pages_output),
            "total_w2a_clicks": sum(p["conversion"]["total_w2a_clicks"] for p in pages_output),
            "overall_w2a_cr": round(sum(p["conversion"]["total_w2a_clicks"] for p in pages_output) / total_organic_sessions, 4) if total_organic_sessions else 0.0,
            "total_ai_search_sessions": sum(p["post_click"]["ai_sessions"] for p in pages_output),
            "quadrant_distribution": quadrant_summary,
            "health_status_definitions": {
                "ORGANIC_LED": {
                    "status": "ORGANIC_LED",
                    "threshold": "non_paid_pct >= 0.8",
                    "label": "Tự Nhiên (Organic-led)",
                    "desc": "Tối thiểu 80% lưu lượng đến từ nguồn tự nhiên (Organic, Direct, Referral). Mô hình tăng trưởng lành mạnh, bền vững."
                },
                "MIXED": {
                    "status": "MIXED",
                    "threshold": "0.5 <= non_paid_pct < 0.8",
                    "label": "Cân Bằng Hỗn Hợp (Mixed)",
                    "desc": "Lưu lượng kết hợp giữa tự nhiên và chiến dịch có trả phí (50% - 80% Non-Paid)."
                },
                "PAID_LED": {
                    "status": "PAID_LED",
                    "threshold": "paid_pct >= 0.5",
                    "label": "Phụ Thuộc Ads (Paid-led)",
                    "desc": "Trên 50% lưu lượng đến từ các chiến dịch trả phí (Paid Search, Ads). Cần tối ưu SEO/GEO để duy trì hiệu quả chi phí."
                }
            },
            "web_performance": {
                "total_pageviews": total_web_pageviews,
                "total_sessions": total_web_sessions,
                "total_users": total_web_users,
                "total_w2a_clicks": total_web_w2a,
                "overall_w2a_cr": round(total_web_w2a / total_web_sessions, 4) if total_web_sessions > 0 else 0.0,
                "total_projects": len(projects_list),
                "non_paid_pageviews": tot_non_paid_pv,
                "non_paid_pv_pct": round(tot_non_paid_pv / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0,
                "paid_pageviews": tot_paid_pv,
                "paid_pv_pct": round(tot_paid_pv / total_web_pageviews, 4) if total_web_pageviews > 0 else 0.0,
                "non_paid_sessions": tot_non_paid_s,
                "non_paid_pct": round(tot_non_paid_s / total_web_sessions, 4) if total_web_sessions > 0 else 0.0,
                "paid_sessions": tot_paid_s,
                "paid_pct": round(tot_paid_s / total_web_sessions, 4) if total_web_sessions > 0 else 0.0,
                "non_paid_w2a": tot_non_paid_w,
                "paid_w2a": tot_paid_w,
                "non_paid_cr": round(tot_non_paid_w / tot_non_paid_s, 4) if tot_non_paid_s > 0 else 0.0,
                "paid_cr": round(tot_paid_w / tot_paid_s, 4) if tot_paid_s > 0 else 0.0
            }
        },
        "channels_summary": channels_summary,
        "project_channel_matrix": project_channel_matrix,
        "themes": themes_list,
        "projects_summary": projects_list,
        "top_quick_wins": top_quick_wins,
        "quick_wins": top_quick_wins,
        "pages": pages_output
    }

    # Xuất bản file sang các nơi
    print("[5/5] Xuất bản dữ liệu sang Knowledge Base & Web Hubs...")
    
    # Target 1: SSOT Knowledge Base (07_REPORTS/data/analytics/)
    kb_dir = BASE_DIR / "07_REPORTS" / "data" / "analytics"
    kb_dir.mkdir(parents=True, exist_ok=True)
    kb_file = kb_dir / "full_funnel_matrix.json"
    with open(kb_file, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã lưu SSOT Knowledge Base: {kb_file}")

    # Target 2: Root data/analytics/ (theo đường dẫn yêu cầu của user)
    root_data_dir = BASE_DIR / "data" / "analytics"
    root_data_dir.mkdir(parents=True, exist_ok=True)
    root_data_file = root_data_dir / "full-funnel-matrix.json"
    with open(root_data_file, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã lưu Root Data Analytics: {root_data_file}")

    # Target 3: Web Hubs (react-web-momo)
    hubs_dir = HUBS_REPO / "data" / "analytics"
    hubs_dir.mkdir(parents=True, exist_ok=True)
    hubs_file = hubs_dir / "full-funnel-matrix.json"
    with open(hubs_file, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, ensure_ascii=False, indent=2)
    print(f"✓ Đã lưu Web Hubs: {hubs_file}")

    # Đồng bộ file BigQuery DIM sang Web Hubs để Hubs trực tiếp đọc
    dim_src = BASE_DIR / "07_REPORTS" / "data" / "dim" / "web_dim_page_url.json"
    if dim_src.exists():
        hubs_dim_dest = hubs_dir / "web-dim-page-url.json"
        shutil.copy2(dim_src, hubs_dim_dest)
        print(f"✓ Đã đồng bộ BigQuery DIM sang Web Hubs: {hubs_dim_dest}")

    elapsed = time.time() - start_time
    print("=" * 70)
    print(f"HOÀN THÀNH PHÂN RÃ HỢP NHẤT TRONG {elapsed:.1f} GIÂY")
    print(f"- Total Pages Analyzed          : {total_analyzed:,}")
    print(f"- Summary Join Rate             : {join_rate * 100:.2f}% (Đạt chuẩn > 90%)")
    print(f"- Summary Organic Mapped Rate   : {organic_mapped_pct * 100:.2f}% (Đạt chuẩn > 70%)")
    print(f"- Tổng Quadrant Check           : {sum(quadrant_summary.values()):,} == {total_analyzed:,}")
    print(f"- Top Quick Wins (Unique Paths) : {len(top_quick_wins):,} queries")
    print("=" * 70)

if __name__ == "__main__":
    main()
