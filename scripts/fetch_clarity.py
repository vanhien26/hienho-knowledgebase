#!/usr/bin/env python3
"""
Microsoft Clarity Data Export Pipeline for momo.vn
Thực hiện:
1. Đọc CLARITY_API_TOKEN an toàn từ file .env.
2. Gọi 4 requests hàng ngày (URL, Source/Medium, Channel, URL/Source) theo chuẩn Clarity Data Export API.
3. Phân loại traffic AI (ChatGPT, Perplexity, Copilot, Gemini, Claude, You, Meta AI, DeepSeek, Duck.ai...).
4. Lưu raw responses, daily snapshots và tổng hợp clarity_latest.json (180 ngày daily, 30 ngày pages).
5. In tóm tắt báo cáo chuẩn Product Lead / Tech Lead.
"""

import os
import sys
import json
import glob
import time
import argparse
from datetime import datetime, timedelta

# ==============================================================================
# 0. BẢO MẬT & CẤU HÌNH HỆ THỐNG
# ==============================================================================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV_FILE = os.path.join(BASE_DIR, ".env")
CLARITY_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data", "clarity")
RAW_DIR = os.path.join(CLARITY_DIR, "raw")
HISTORY_DIR = os.path.join(CLARITY_DIR, "history")
LATEST_FILE = os.path.join(CLARITY_DIR, "clarity_latest.json")

CLARITY_API_URL = "https://www.clarity.ms/export-data/api/v1/project-live-insights"

# Danh sách domain nhận diện nguồn AI
AI_DOMAINS = [
    "chatgpt.com",
    "chat.openai.com",
    "copilot.microsoft.com",
    "bing.com/chat",
    "perplexity.ai",
    "gemini.google.com",
    "claude.ai",
    "you.com",
    "meta.ai",
    "deepseek",
    "duck.ai"
]

def load_env(env_path):
    """Đọc file .env nội bộ mà không in token ra màn hình."""
    if not os.path.exists(env_path):
        return
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    if key and key not in os.environ:
                        os.environ[key] = val
    except Exception:
        pass

def get_api_token():
    """Kiểm tra và lấy token từ biến môi trường. Nếu thiếu thì dừng ngay lập tức."""
    load_env(ENV_FILE)
    token = os.environ.get("CLARITY_API_TOKEN", "").strip()
    if not token:
        print("Thiếu CLARITY_API_TOKEN")
        sys.exit(1)
    return token

def is_ai_source(source_str):
    """Xác định nguồn có phải là AI hay không."""
    if not source_str:
        return False
    source_lower = source_str.lower().strip()
    return any(domain in source_lower for domain in AI_DOMAINS)

# ==============================================================================
# 1. API CALL VỚI EXPONENTIAL BACKOFF
# ==============================================================================
def query_clarity_api(params, token, max_retries=3):
    """Gọi Clarity API với cơ chế Exponential Backoff khi gặp HTTP 429."""
    import requests

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    for attempt in range(max_retries):
        try:
            resp = requests.get(CLARITY_API_URL, params=params, headers=headers, timeout=45)
            if resp.status_code == 200:
                try:
                    return resp.json()
                except json.JSONDecodeError:
                    print(f"[ERROR] Không thể parse JSON từ API response: {resp.text[:200]}")
                    return None
            elif resp.status_code == 429:
                wait_sec = (attempt + 1) * 6
                print(f"[WARN] HTTP 429 (TooManyRequests). Đang chờ {wait_sec}s để thử lại ({attempt + 1}/{max_retries})...")
                time.sleep(wait_sec)
            elif resp.status_code == 401:
                print("[ERROR] HTTP 401 Unauthorized: Token không hợp lệ hoặc đã hết hạn.")
                return None
            elif resp.status_code == 403:
                print("[ERROR] HTTP 403 Forbidden: Token không có quyền truy cập project.")
                return None
            else:
                print(f"[ERROR] HTTP {resp.status_code}: {resp.text[:200]}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"[WARN] Lỗi kết nối mạng: {e}. Đang thử lại...")
            time.sleep(3)

    print("[ERROR] Vượt quá số lần thử lại tối đa cho request.")
    return None

def determine_num_of_days(history_dir):
    """Tự động tính numOfDays để bù dữ liệu nếu cron bị trễ."""
    history_files = glob.glob(os.path.join(history_dir, "*.json"))
    if not history_files:
        return 1

    dates = []
    for f in history_files:
        basename = os.path.splitext(os.path.basename(f))[0]
        try:
            dates.append(datetime.strptime(basename, "%Y-%m-%d").date())
        except ValueError:
            pass

    if not dates:
        return 1

    latest_date = max(dates)
    yesterday = (datetime.now() - timedelta(days=1)).date()
    gap = (yesterday - latest_date).days

    if gap <= 1:
        return 1
    elif gap == 2:
        return 2
    else:
        return 3

# ==============================================================================
# 2. XỬ LÝ & PARSE DỮ LIỆU TỪ 4 REQUESTS
# ==============================================================================
def parse_clarity_response(data):
    """
    Chuẩn hóa dữ liệu trả về từ Clarity API.
    Clarity API trả về danh sách các Metric objects: [{"metricName": "Traffic", "information": [...]}]
    """
    if not data or not isinstance(data, list):
        return {}

    metric_map = {}
    for block in data:
        if isinstance(block, dict) and "metricName" in block:
            m_name = block["metricName"]
            metric_map[m_name] = block.get("information", [])
    return metric_map

def get_row_val(row, *possible_keys, default=None):
    """Lấy giá trị từ dict theo nhiều biến thể tên key hoa/thường."""
    for k in possible_keys:
        if k in row:
            return row[k]
        for rk in row:
            if rk.lower() == k.lower():
                return row[rk]
    return default

def process_daily_data(r1_data, r2_data, r3_data, r4_data):
    """
    Tổng hợp dữ liệu từ 4 request R1..R4:
    - R1: URL (traffic & behavioral metrics)
    - R2: Source, Medium (traffic sources)
    - R3: Channel (kênh traffic)
    - R4: URL, Source (phân bổ nguồn cho từng URL)
    """
    r1_metrics = parse_clarity_response(r1_data)
    r2_metrics = parse_clarity_response(r2_data)
    r3_metrics = parse_clarity_response(r3_data)
    r4_metrics = parse_clarity_response(r4_data)

    # 1. Xử lý R2: Source & Medium
    traffic_info_r2 = r2_metrics.get("Traffic", [])
    if not traffic_info_r2 and r2_metrics:
        traffic_info_r2 = list(r2_metrics.values())[0]

    actual_sources = set()
    total_sessions_from_r2 = 0
    total_ai_sessions = 0
    by_ai_source = {}
    sources_detail = []

    for row in traffic_info_r2:
        src = str(get_row_val(row, "Source", "source", default="")).strip()
        med = str(get_row_val(row, "Medium", "medium", default="")).strip()
        cnt_val = get_row_val(row, "totalSessionCount", "sessions", "sessionCount", default=0)
        try:
            cnt = int(cnt_val)
        except (ValueError, TypeError):
            cnt = 0

        if src:
            actual_sources.add(src)
        total_sessions_from_r2 += cnt

        is_ai = is_ai_source(src)
        if is_ai:
            total_ai_sessions += cnt
            by_ai_source[src] = by_ai_source.get(src, 0) + cnt

        sources_detail.append({
            "source": src,
            "medium": med,
            "sessions": cnt,
            "is_ai_source": is_ai
        })

    # 2. Xử lý R3: Channel
    traffic_info_r3 = r3_metrics.get("Traffic", [])
    if not traffic_info_r3 and r3_metrics:
        traffic_info_r3 = list(r3_metrics.values())[0]

    channels_detail = []
    has_ai_channel = False
    ai_channel_names = []

    for row in traffic_info_r3:
        ch = str(get_row_val(row, "Channel", "channel", default="unknown")).strip()
        cnt_val = get_row_val(row, "totalSessionCount", "sessions", "sessionCount", default=0)
        try:
            cnt = int(cnt_val)
        except (ValueError, TypeError):
            cnt = 0

        # Kiểm tra chính xác Channel kiểu AI (loại bỏ match nhầm "PaidSearch")
        ch_lower = ch.lower()
        is_ai_ch = (
            ch_lower in ["ai", "aiplatform", "ai platform", "generative ai", "genai", "artificial intelligence"]
            or "aiplatform" in ch_lower
            or "generative" in ch_lower
        )

        if is_ai_ch:
            has_ai_channel = True
            ai_channel_names.append(ch)

        channels_detail.append({
            "channel": ch,
            "sessions": cnt
        })

    # 3. Thu thập các Metric hành vi từ cả R1 và R4
    scroll_depth_map = {}
    engagement_time_map = {}
    dead_clicks_map = {}
    rage_clicks_map = {}
    quickbacks_map = {}

    for m_source in [r4_metrics, r1_metrics]:
        for m_name, info_list in m_source.items():
            m_lower = m_name.lower()
            for row in info_list:
                u = str(get_row_val(row, "Url", "URL", "url", default="")).strip()
                if not u:
                    continue
                if "scrolldepth" in m_lower:
                    val = get_row_val(row, "averageScrollDepth", "scrollDepth", "ScrollDepthPercentage")
                    if val is not None:
                        try: scroll_depth_map[u] = float(val)
                        except: pass
                elif "engagementtime" in m_lower or "active" in m_lower:
                    val = get_row_val(row, "activeTime", "engagementTime")
                    if val is not None:
                        try: engagement_time_map[u] = float(val)
                        except: pass
                elif "deadclickcount" in m_lower:
                    val = get_row_val(row, "subTotal", "deadClickCount", "deadClicks")
                    if val is not None:
                        try: dead_clicks_map[u] = float(val)
                        except: pass
                elif "rageclickcount" in m_lower:
                    val = get_row_val(row, "subTotal", "rageClickCount", "rageClicks")
                    if val is not None:
                        try: rage_clicks_map[u] = float(val)
                        except: pass
                elif "quickbackclick" in m_lower:
                    val = get_row_val(row, "subTotal", "quickbackClick", "quickbacks")
                    if val is not None:
                        try: quickbacks_map[u] = float(val)
                        except: pass

    # 4. Hợp nhất danh sách Pages từ cả R1 (Top Site) và R4 (Nguồn AI chi tiết)
    pages_dict = {}

    # Nạp từ R1 Traffic
    traffic_info_r1 = r1_metrics.get("Traffic", [])
    total_sessions_from_r1 = 0
    for row in traffic_info_r1:
        url = str(get_row_val(row, "Url", "URL", "url", default="")).strip()
        if not url:
            continue
        cnt_val = get_row_val(row, "totalSessionCount", "sessions", "sessionCount", default=0)
        try: cnt = int(cnt_val)
        except: cnt = 0

        total_sessions_from_r1 += cnt
        pages_dict[url] = {
            "url": url,
            "sessions": cnt,
            "ai_sessions": 0,
            "by_ai_source": {},
            "scroll_depth": scroll_depth_map.get(url),
            "engagement_time": engagement_time_map.get(url),
            "dead_clicks": dead_clicks_map.get(url),
            "rage_clicks": rage_clicks_map.get(url),
            "quickbacks": quickbacks_map.get(url)
        }

    # Nạp và gán AI sessions từ R4 Traffic
    traffic_info_r4 = r4_metrics.get("Traffic", [])
    for row in traffic_info_r4:
        url = str(get_row_val(row, "Url", "URL", "url", default="")).strip()
        src = str(get_row_val(row, "Source", "source", default="")).strip()
        cnt_val = get_row_val(row, "totalSessionCount", "sessions", "sessionCount", default=0)
        try: cnt = int(cnt_val)
        except: cnt = 0

        if not url:
            continue

        if url not in pages_dict:
            pages_dict[url] = {
                "url": url,
                "sessions": cnt,
                "ai_sessions": 0,
                "by_ai_source": {},
                "scroll_depth": scroll_depth_map.get(url),
                "engagement_time": engagement_time_map.get(url),
                "dead_clicks": dead_clicks_map.get(url),
                "rage_clicks": rage_clicks_map.get(url),
                "quickbacks": quickbacks_map.get(url)
            }

        if is_ai_source(src):
            pages_dict[url]["ai_sessions"] += cnt
            pages_dict[url]["by_ai_source"][src] = pages_dict[url]["by_ai_source"].get(src, 0) + cnt

    pages = list(pages_dict.values())
    pages.sort(key=lambda x: (x["ai_sessions"], x["sessions"]), reverse=True)

    # Xác định các trường bị thiếu hoàn toàn trên API
    potential_fields = ["scroll_depth", "engagement_time", "dead_clicks", "rage_clicks", "quickbacks"]
    missing_fields = []
    for f in potential_fields:
        if all(p.get(f) is None for p in pages):
            missing_fields.append(f)

    final_sessions = total_sessions_from_r2 if total_sessions_from_r2 > 0 else total_sessions_from_r1

    return {
        "total_sessions": final_sessions,
        "total_ai_sessions": total_ai_sessions,
        "by_ai_source": by_ai_source,
        "actual_sources": sorted(list(actual_sources)),
        "has_ai_channel": has_ai_channel,
        "ai_channel_names": ai_channel_names,
        "channels": channels_detail,
        "sources": sources_detail,
        "pages": pages,
        "missing_fields": missing_fields
    }

# ==============================================================================
# 3. SNAPSHOT & TỔNG HỢP LỊCH SỬ CLARITY_LATEST.JSON
# ==============================================================================
def save_daily_snapshot(date_str, daily_result, raw_meta, overwrite=False):
    """Lưu snapshot dữ liệu theo ngày vào history/<YYYY-MM-DD>.json."""
    os.makedirs(HISTORY_DIR, exist_ok=True)
    snapshot_file = os.path.join(HISTORY_DIR, f"{date_str}.json")

    if os.path.exists(snapshot_file) and not overwrite:
        print(f"[INFO] Snapshot ngày {date_str} đã tồn tại, bảo lưu bản ghi.")
        return snapshot_file

    snapshot_data = {
        "date": date_str,
        "fetched_at": datetime.now().isoformat(),
        "total_sessions": daily_result["total_sessions"],
        "total_ai_sessions": daily_result["total_ai_sessions"],
        "by_ai_source": daily_result["by_ai_source"],
        "has_ai_channel": daily_result["has_ai_channel"],
        "ai_channel_names": daily_result["ai_channel_names"],
        "missing_fields": daily_result["missing_fields"],
        "pages": daily_result["pages"],
        "raw_meta": raw_meta
    }

    with open(snapshot_file, "w", encoding="utf-8") as f:
        json.dump(snapshot_data, f, ensure_ascii=False, indent=2)

    print(f"[INFO] Đã lưu snapshot ngày {date_str} vào: {snapshot_file}")
    return snapshot_file

def build_clarity_latest():
    """
    Xây dựng file clarity_latest.json:
    - daily: dồn từ history, giữ tối thiểu 180 ngày.
    - pages: cộng dồn 30 ngày gần nhất.
    - missing_fields: ghi nhận rõ các trường null.
    """
    os.makedirs(CLARITY_DIR, exist_ok=True)
    history_files = sorted(glob.glob(os.path.join(HISTORY_DIR, "*.json")))

    if not history_files:
        print("[WARN] Chưa có file snapshot nào trong history.")
        return None

    all_snapshots = []
    for hf in history_files:
        try:
            with open(hf, "r", encoding="utf-8") as f:
                all_snapshots.append(json.load(f))
        except Exception as e:
            print(f"[WARNING] Không thể đọc snapshot {hf}: {e}")

    # Sắp xếp snapshots theo ngày giảm dần
    all_snapshots.sort(key=lambda x: x.get("date", ""), reverse=True)

    # 1. Daily: giữ tối thiểu 180 ngày
    daily_list = []
    days_covered = []
    for s in all_snapshots[:180]:
        d_str = s.get("date", "")
        days_covered.append(d_str)
        daily_list.append({
            "date": d_str,
            "sessions": s.get("total_sessions", 0),
            "ai_sessions": s.get("total_ai_sessions", 0),
            "by_ai_source": s.get("by_ai_source", {})
        })

    days_covered_sorted = sorted(days_covered)

    # 2. Pages: cộng dồn 30 ngày gần nhất
    now_date = datetime.now().date()
    cutoff_30d = now_date - timedelta(days=30)

    pages_aggregated = {}
    missing_fields_set = set(["scroll_depth", "engagement_time", "dead_clicks", "rage_clicks", "quickbacks"])

    for s in all_snapshots:
        try:
            s_date = datetime.strptime(s.get("date", ""), "%Y-%m-%d").date()
        except ValueError:
            continue

        if s_date < cutoff_30d:
            continue

        for p in s.get("pages", []):
            u = p.get("url")
            if not u:
                continue

            if u not in pages_aggregated:
                pages_aggregated[u] = {
                    "url": u,
                    "sessions": 0,
                    "ai_sessions": 0,
                    "scroll_depth_weighted": 0.0,
                    "engagement_time_weighted": 0.0,
                    "dead_clicks_total": 0.0,
                    "rage_clicks_total": 0.0,
                    "quickbacks_total": 0.0,
                    "scroll_depth_count": 0,
                    "engagement_time_count": 0,
                    "dead_clicks_count": 0,
                    "rage_clicks_count": 0,
                    "quickbacks_count": 0,
                }

            item = pages_aggregated[u]
            sess = p.get("sessions", 0)
            ai_sess = p.get("ai_sessions", 0)
            item["sessions"] += sess
            item["ai_sessions"] += ai_sess

            if p.get("scroll_depth") is not None:
                item["scroll_depth_weighted"] += p["scroll_depth"] * max(sess, 1)
                item["scroll_depth_count"] += max(sess, 1)
                missing_fields_set.discard("scroll_depth")

            if p.get("engagement_time") is not None:
                item["engagement_time_weighted"] += p["engagement_time"] * max(sess, 1)
                item["engagement_time_count"] += max(sess, 1)
                missing_fields_set.discard("engagement_time")

            if p.get("dead_clicks") is not None:
                item["dead_clicks_total"] += p["dead_clicks"]
                item["dead_clicks_count"] += 1
                missing_fields_set.discard("dead_clicks")

            if p.get("rage_clicks") is not None:
                item["rage_clicks_total"] += p["rage_clicks"]
                item["rage_clicks_count"] += 1
                missing_fields_set.discard("rage_clicks")

            if p.get("quickbacks") is not None:
                item["quickbacks_total"] += p["quickbacks"]
                item["quickbacks_count"] += 1
                missing_fields_set.discard("quickbacks")

    final_pages = []
    for u, item in pages_aggregated.items():
        final_pages.append({
            "url": u,
            "sessions": item["sessions"],
            "ai_sessions": item["ai_sessions"],
            "scroll_depth": round(item["scroll_depth_weighted"] / item["scroll_depth_count"], 2) if item["scroll_depth_count"] > 0 else None,
            "engagement_time": round(item["engagement_time_weighted"] / item["engagement_time_count"], 2) if item["engagement_time_count"] > 0 else None,
            "dead_clicks": round(item["dead_clicks_total"], 2) if item["dead_clicks_count"] > 0 else None,
            "rage_clicks": round(item["rage_clicks_total"], 2) if item["rage_clicks_count"] > 0 else None,
            "quickbacks": round(item["quickbacks_total"], 2) if item["quickbacks_count"] > 0 else None,
        })

    # Sắp xếp pages theo AI sessions giảm dần, sau đó theo Sessions
    final_pages.sort(key=lambda x: (x["ai_sessions"], x["sessions"]), reverse=True)

    latest_output = {
        "source": "clarity_data_export",
        "fetched_at": datetime.now().isoformat(),
        "days_covered": days_covered_sorted,
        "daily": daily_list,
        "pages": final_pages,
        "missing_fields": sorted(list(missing_fields_set))
    }

    with open(LATEST_FILE, "w", encoding="utf-8") as f:
        json.dump(latest_output, f, ensure_ascii=False, indent=2)

    print(f"[INFO] Đã cập nhật file Master: {LATEST_FILE}")
    return latest_output

# ==============================================================================
# 4. CHƯƠNG TRÌNH CHÍNH & IN BÁO CÁO TỔNG KẾT
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(description="Fetch Microsoft Clarity Live Insights Data for momo.vn")
    parser.add_argument("--days", type=int, choices=[1, 2, 3], default=None, help="Số ngày kéo dữ liệu (1, 2, hoặc 3). Mặc định tự động tính toán.")
    parser.add_argument("--date", default=None, help="Ngày gán nhãn cho snapshot (YYYY-MM-DD). Mặc định là ngày hôm qua.")
    parser.add_argument("--reprocess", action="store_true", help="Xử lý lại dữ liệu từ file raw đã lưu mà không gọi API (tiết kiệm quota)")
    args = parser.parse_args()

    # 1. Xác thực Token (dừng và báo lỗi nếu thiếu, trừ khi reprocess)
    token = None
    if not args.reprocess:
        token = get_api_token()

    # 2. Xác định ngày và numOfDays
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(HISTORY_DIR, exist_ok=True)

    today = datetime.now()
    yesterday = today - timedelta(days=1)
    target_date = args.date if args.date else yesterday.strftime("%Y-%m-%d")

    num_of_days = args.days if args.days else determine_num_of_days(HISTORY_DIR)
    print("=== BẮT ĐẦU KÉO DỮ LIỆU MICROSOFT CLARITY (DATA EXPORT API) ===")
    print(f"[INFO] Ngày chỉ định snapshot: {target_date}")
    print(f"[INFO] Khoảng thời gian numOfDays: {num_of_days}")

    raw_responses = {}
    raw_saved = {}
    requests_used = 0

    if args.reprocess:
        print("[INFO] Chế độ Reprocess: Đọc từ các file raw response có sẵn để bảo toàn hạn mức 10 reqs/ngày...")
        for req_id in ["r1", "r2", "r3", "r4"]:
            raw_file = os.path.join(RAW_DIR, f"{target_date}_{req_id}.json")
            if not os.path.exists(raw_file):
                print(f"[ERROR] Không tìm thấy file raw: {raw_file}")
                sys.exit(1)
            with open(raw_file, "r", encoding="utf-8") as f:
                raw_responses[req_id] = json.load(f)
            raw_saved[req_id] = raw_file
    else:
        req_configs = [
            {"id": "r1", "params": {"numOfDays": str(num_of_days), "dimension1": "URL"}, "desc": "Hành vi theo trang (URL)"},
            {"id": "r2", "params": {"numOfDays": str(num_of_days), "dimension1": "Source", "dimension2": "Medium"}, "desc": "Nguồn traffic (Source, Medium)"},
            {"id": "r3", "params": {"numOfDays": str(num_of_days), "dimension1": "Channel"}, "desc": "Kênh traffic (Channel)"},
            {"id": "r4", "params": {"numOfDays": str(num_of_days), "dimension1": "URL", "dimension2": "Source"}, "desc": "Trang và Nguồn (URL, Source)"},
        ]

        for req in req_configs:
            req_id = req["id"]
            print(f"\n[REQUEST {req_id.upper()}] {req['desc']}...")
            res_json = query_clarity_api(req["params"], token)
            requests_used += 1

            if res_json is None:
                print(f"[ERROR] Request {req_id.upper()} thất bại. Dừng luồng để bảo toàn quota.")
                sys.exit(1)

            raw_responses[req_id] = res_json

            raw_file = os.path.join(RAW_DIR, f"{target_date}_{req_id}.json")
            with open(raw_file, "w", encoding="utf-8") as f:
                json.dump(res_json, f, ensure_ascii=False, indent=2)
            raw_saved[req_id] = raw_file
            print(f"[INFO] Đã lưu raw response: {raw_file}")
            time.sleep(2)

    # 4. Phân tích và tổng hợp dữ liệu
    daily_result = process_daily_data(
        raw_responses["r1"],
        raw_responses["r2"],
        raw_responses["r3"],
        raw_responses["r4"]
    )

    # 5. Lưu snapshot lịch sử (nếu reprocess thì cho phép overwrite)
    save_daily_snapshot(target_date, daily_result, raw_saved, overwrite=True)

    # 6. Cập nhật file master clarity_latest.json
    build_clarity_latest()

    # 7. In tóm tắt báo cáo chuẩn Product Lead / Tech Lead
    print("\n" + "=" * 65)
    print("BÁO CÁO TỔNG KẾT CLARITY DATA EXPORT (momo.vn)")
    print("=" * 65)
    print(f"- Số request đã sử dụng: {requests_used}/10 requests (trong hạn mức cho phép)")
    print(f"- Tổng số Sessions: {daily_result['total_sessions']:,}")
    pct_ai = (daily_result['total_ai_sessions'] / daily_result['total_sessions'] * 100) if daily_result['total_sessions'] > 0 else 0
    print(f"- Tổng số AI Sessions: {daily_result['total_ai_sessions']:,} ({pct_ai:.2f}%)")

    # Phân bổ nguồn AI
    print("\nChi tiết phiên truy cập theo nguồn AI (by_ai_source):")
    if daily_result["by_ai_source"]:
        for src, cnt in sorted(daily_result["by_ai_source"].items(), key=lambda x: x[1], reverse=True):
            print(f"  * {src}: {cnt:,} sessions")
    else:
        print("  * Không ghi nhận traffic từ các nguồn AI định danh trong ngày.")

    # Kiểm tra Channel AI
    print("\nKiểm tra kênh Channel từ Clarity API:")
    if daily_result["has_ai_channel"]:
        print(f"  * API CÓ trả về Channel dạng AI: {', '.join(daily_result['ai_channel_names'])}")
    else:
        print("  * API KHÔNG trả về Channel kiểu 'AI' (các kênh thực tế: " +
              ", ".join([f"{c['channel']} ({c['sessions']:,})" for c in daily_result['channels']]) + ")")

    # Top 10 URL nhận traffic AI
    print("\nTop 10 URL nhận traffic từ nguồn AI nhiều nhất:")
    ai_pages = [p for p in daily_result["pages"] if p["ai_sessions"] > 0]
    ai_pages.sort(key=lambda x: (x["ai_sessions"], x["sessions"]), reverse=True)

    if ai_pages:
        for idx, p in enumerate(ai_pages[:10], start=1):
            src_str = ", ".join([f"{k}: {v}" for k, v in p["by_ai_source"].items()])
            scroll_s = f"{p['scroll_depth']}%" if p['scroll_depth'] is not None else "N/A"
            eng_s = f"{p['engagement_time']}s" if p['engagement_time'] is not None else "N/A"
            print(f"  {idx:>2}. {p['url']}")
            print(f"      AI Sessions: {p['ai_sessions']:,} | Tổng: {p['sessions']:,} | Scroll: {scroll_s} | ActiveTime: {eng_s} | Nguồn: [{src_str}]")
    else:
        print("  * Chưa có trang nào ghi nhận traffic từ nguồn AI.")

    # Danh sách các Source thực tế có trong dữ liệu
    print("\nDanh sách toàn bộ các Source thực tế phát hiện trong dữ liệu (để kiểm tra rule):")
    for s in daily_result["actual_sources"]:
        is_ai_flag = "[AI SOURCE]" if is_ai_source(s) else ""
        print(f"  - {s} {is_ai_flag}")

    # Cảnh báo các trường metric không được API trả về
    if daily_result["missing_fields"]:
        print("\nCác trường metric không được API trả về (ghi nhận null trong missing_fields):")
        print(f"  * {', '.join(daily_result['missing_fields'])}")
    else:
        print("\nToàn bộ 5 chỉ số hành vi (Scroll, Engagement, Dead Clicks, Rage Clicks, Quickbacks) đã được thu thập đầy đủ.")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
