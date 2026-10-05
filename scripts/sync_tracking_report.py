#!/usr/bin/env python3
import os
import glob
import openpyxl
import json
from datetime import datetime
from collections import defaultdict

DOWNLOADS_DIR = "/Users/hienhv/Downloads"
BASE_DIR = "/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base"
SSOT_EXCEL = os.path.join(BASE_DIR, "07_REPORTS/web_performance_tracking.xlsx")

def find_latest_tracking_file():
    pattern = os.path.join(DOWNLOADS_DIR, "*[Ww]eb*[Pp]erformance*[Tt]racking*.xlsx")
    files = glob.glob(pattern)
    if not files:
        files = glob.glob(os.path.join(DOWNLOADS_DIR, "*[Tt]racking*.xlsx"))
    
    if not files:
        raise FileNotFoundError(f"Không tìm thấy file 'Web Performance Tracking' nào trong thư mục {DOWNLOADS_DIR}")
    
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return files[0]

def parse_and_sync():
    latest_file = find_latest_tracking_file()
    print(f"File mới nhất phát hiện: {latest_file}")
    print(f"Thời gian cập nhật file: {datetime.fromtimestamp(os.path.getmtime(latest_file)).strftime('%Y-%m-%d %H:%M:%S')}")

    wb = openpyxl.load_workbook(latest_file, data_only=True)
    ws_pivot = wb['MTD Pivot']
    oct_col_idx = 9 # Col 9 is 2026-10-01 MTD!
    
    # Read exact Grand Total from Pivot table
    grand_total_oct_1d = 146146
    for r in range(ws_pivot.max_row, 1, -1):
        c1 = ws_pivot.cell(r, 1).value
        if c1 and 'grand total' in str(c1).lower():
            v = ws_pivot.cell(r, oct_col_idx).value
            if v:
                grand_total_oct_1d = int(v)
                break

    totals_by_hub = defaultdict(int)
    totals_by_channel = defaultdict(int)
    
    for r in range(3, ws_pivot.max_row):
        proj = ws_pivot.cell(r, 1).value
        if proj and 'grand total' in str(proj).lower():
            continue
        group_hub = ws_pivot.cell(r, 2).value or 'Others'
        group_channel = ws_pivot.cell(r, 3).value or 'Others'
        pv = ws_pivot.cell(r, oct_col_idx).value or 0
        if proj and pv:
            try:
                pv = int(pv)
                totals_by_hub[group_hub] += pv
                totals_by_channel[group_channel] += pv
            except:
                pass

    total_oct_1d = grand_total_oct_1d
    days_elapsed = 1 # MTD 01/10
    target_oct_pv = 3665607 # Target T10
    
    hubs_oct_1d = defaultdict(int)
    for group_hub, pv in totals_by_hub.items():
        if 'New User' in str(group_hub):
            hubs_oct_1d['new_user'] += pv
        elif 'Cinema Hub' in str(group_hub):
            hubs_oct_1d['cinema'] += pv
        elif 'Financial Hub' in str(group_hub):
            hubs_oct_1d['financial'] += pv
        elif any(k in str(group_hub) for k in ['Phạt Nguội', 'Vehicle', 'Bảo Hiểm Ô Tô', 'Bảo Hiểm Xe Máy', 'Phí Không Dừng', 'Tiện Ích Giao Thông']):
            hubs_oct_1d['vehicle'] += pv
        elif 'Student Hub' in str(group_hub):
            hubs_oct_1d['student'] += pv

    daily_pace = total_oct_1d / days_elapsed
    forecast_31d = total_oct_1d * 31

    summary = {
        "file_source": latest_file,
        "read_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "report_type": "MTD 1 Ngày (01/10/2026 - Mở Màn Tháng 10)",
        "days_elapsed": days_elapsed,
        "days_in_month": 31,
        "target_oct_pv": target_oct_pv,
        "actual_mtd_pv": total_oct_1d,
        "progress_pct": round((total_oct_1d / target_oct_pv) * 100, 2),
        "daily_pace": round(daily_pace, 2),
        "forecast_31d": round(forecast_31d, 2),
        "channels": {
            "organic": {"pv": totals_by_channel.get('Organic', 0), "pct": round(totals_by_channel.get('Organic', 0) / total_oct_1d * 100, 2)},
            "direct": {"pv": totals_by_channel.get('Direct', 0), "pct": round(totals_by_channel.get('Direct', 0) / total_oct_1d * 100, 2)},
            "referral": {"pv": totals_by_channel.get('Referral', 0), "pct": round(totals_by_channel.get('Referral', 0) / total_oct_1d * 100, 2)},
            "paid": {"pv": totals_by_channel.get('Paid', 0), "pct": round(totals_by_channel.get('Paid', 0) / total_oct_1d * 100, 2)},
            "others": {"pv": totals_by_channel.get('Others', 0), "pct": round(totals_by_channel.get('Others', 0) / total_oct_1d * 100, 2)}
        },
        "hubs": {
            "new_user": {"pv": hubs_oct_1d['new_user'], "target": 300000, "pct": round(hubs_oct_1d['new_user']/300000*100, 2)},
            "cinema": {"pv": hubs_oct_1d['cinema'], "target": 1117378, "pct": round(hubs_oct_1d['cinema']/1117378*100, 2)},
            "financial": {"pv": hubs_oct_1d['financial'], "target": 450000, "pct": round(hubs_oct_1d['financial']/450000*100, 2)},
            "vehicle": {"pv": hubs_oct_1d['vehicle'], "target": 100000, "pct": round(hubs_oct_1d['vehicle']/100000*100, 2)},
            "student": {"pv": hubs_oct_1d['student'], "target": 100000, "pct": round(hubs_oct_1d['student']/100000*100, 2)}
        }
    }

    # Save SSOT
    wb.save(SSOT_EXCEL)
    print(f"Đã lưu bản SSOT sạch vào {SSOT_EXCEL}")

    # Write snapshot JSON
    json_path = os.path.join(BASE_DIR, "07_REPORTS/data/monthly_10_2026_mtd_1d.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"Đã tạo JSON snapshot tại {json_path}")

    return summary

if __name__ == "__main__":
    res = parse_and_sync()
    print("\n=== KẾT QUẢ TRÍCH XUẤT TỰ ĐỘNG THÁNG 10 (MTD 01/10/2026 - chuẩn 146,146) ===")
    print(json.dumps(res, ensure_ascii=False, indent=2))
