#!/usr/bin/env python3
"""
Analyze all 107 CSV files in 05_HUBS/inventory/Financial/
Map them into comprehensive Financial Hub Market structure.
Deduplicate keywords and compute exact search volumes.
"""

import csv
import json
from pathlib import Path

def clean_val(v):
    if v is None:
        return ""
    v = str(v).strip()
    if v.startswith('="') and v.endswith('"'):
        v = v[2:-1]
    return v.strip()

BASE_DIR = Path(__file__).resolve().parent.parent
INV_DIR = BASE_DIR / "05_HUBS" / "inventory" / "Financial"

def load_all_inventory():
    file_kws = {}
    csv_files = sorted(INV_DIR.glob("*.csv"))
    for f in csv_files:
        kws = {}
        with open(f, mode="r", encoding="utf-8-sig", errors="ignore") as fp:
            reader = csv.reader(fp)
            header = next(reader, None)
            if not header:
                continue
            vol_idx, kw_idx = 1, 0
            for i, h in enumerate(header):
                cleaned_h = clean_val(h).lower()
                if "volume" in cleaned_h or "search volume" in cleaned_h:
                    vol_idx = i
                if "keyword" in cleaned_h:
                    kw_idx = i
            for row in reader:
                if not row or len(row) <= max(kw_idx, vol_idx):
                    continue
                kw = clean_val(row[kw_idx]).lower()
                v_str = clean_val(row[vol_idx]).replace(",", "").replace(".", "")
                try:
                    v = int(v_str) if v_str else 0
                except ValueError:
                    v = 0
                kws[kw] = max(kws.get(kw, 0), v)
        file_kws[f.stem.strip()] = kws
    return file_kws

def main():
    file_kws = load_all_inventory()
    print(f"Loaded {len(file_kws)} files from inventory.")

    # Bank brands list
    bank_files = [
        "ncb", "viet-bank", "Techcombank", "vietcombank", "vcb", "nam-a-bank", "vpbank",
        "mbbank", "acb", "vrb", "BIDV", "agribank", "tpbank", "MSB", "viettinbank",
        "sacombank", "shb", "ab-bank", "ocb", "Shinhan Bank", "bac", "ban-viet",
        "eximbank", "vib", "hd-bank", "pvcom bank", "donga bank", "seabank",
        "bac-a-bank", "LPBank", "LPBank ", "bao-viet-bank", "uob", "scb", "kien-long-bank",
        "Indovina Bank", "ocean-bank", "saigonbank"
    ]

    # Structure of Markets in Financial Hub
    # Can be detailed by 24-28 core markets matching Product Lead taxonomy
    MARKETS_DEF = [
        {
            "name": "Giá Vàng & Thị Trường Vàng",
            "pillar": "Đầu Tư & Tích Sản",
            "files": ["gia-vang", "vang"],
            "desc": "Giá vàng SJC, nhẫn 9999, DOJI, PNJ, biểu đồ biến động và quy đổi"
        },
        {
            "name": "Thương Hiệu 34+ Ngân Hàng",
            "pillar": "Ngân Hàng & Đối Tác",
            "files": bank_files,
            "desc": "Tra cứu mã ngân hàng, hotline, chi nhánh, biểu phí 34 ngân hàng"
        },
        {
            "name": "Tỷ Giá & Đổi Ngoại Tệ",
            "pillar": "Tiền Tệ & Ngoại Hối",
            "files": ["ty-gia", "ngoai-te", "doi-tien", "kieu-hoi"],
            "desc": "Bảng tỷ giá 30+ ngoại tệ, tool quy đổi tiền tệ và kiều hối"
        },
        {
            "name": "Ngân Hàng Số & Chuyển Tiền",
            "pillar": "Ngân Hàng & Số Hóa",
            "files": ["ngan-hang", "internet-banking", "chuyen-khoan", "thanh-toan-qr", "vi-dien-tu"],
            "desc": "Dịch vụ ngân hàng số, Internet Banking, chuyển khoản 24/7, QR code"
        },
        {
            "name": "Mã Số Thuế",
            "pillar": "Thu Nhập & Thuế",
            "files": ["ma-so-thue"],
            "desc": "Tra cứu mã số thuế cá nhân, doanh nghiệp và người phụ thuộc"
        },
        {
            "name": "Chứng Khoán & Mã Cổ Phiếu",
            "pillar": "Đầu Tư & Tích Sản",
            "files": ["chung-khoan", "co-phieu", "ma-chung-khoan", "co-tuc", "chia-co-tuc", "phai-sinh", "ky-quy"],
            "desc": "Cổng Cổ phiếu VN30, tra cứu mã, cổ tức, margin, phái sinh"
        },
        {
            "name": "Cho Vay & Lãi Suất Vay",
            "pillar": "Tín Dụng & Cho Vay",
            "files": ["vay", "lai-vay", "vay-tin-chap", "tin-dung", "vay-the-chap", "thau-chi", "du-no"],
            "desc": "Vay tín chấp, vay mua nhà thế chấp, tính lãi vay và lịch trả nợ"
        },
        {
            "name": "Thuế TNCN & Giảm Trừ",
            "pillar": "Thu Nhập & Thuế",
            "files": ["thue", "thue-tncn", "giam-tru-gia-canh"],
            "desc": "Biểu thuế TNCN lũy tiến 7 bậc, giảm trừ gia cảnh, quyết toán thuế"
        },
        {
            "name": "Tiết Kiệm & Lãi Suất Tiền Gửi",
            "pillar": "Tiết Kiệm & Lãi Suất",
            "files": ["lai-suat", "gui-tiet-kiem", "tiet-kiem", "lai-kep", "chung-chi-tien-gui", "tich-luy"],
            "desc": "Bảng lãi suất 40 ngân hàng, tính lãi tiết kiệm, lãi kép và tích lũy"
        },
        {
            "name": "Thẻ Tín Dụng & Visa/Mastercard",
            "pillar": "Ngân Hàng & Thẻ",
            "files": ["the-tin-dung", "the-visa", "the-ghi-no", "napas", "master-card", "the-tra-truoc"],
            "desc": "Mở thẻ tín dụng online, biểu phí, thẻ hoàn tiền, Napas, Visa, Mastercard"
        },
        {
            "name": "Tiền Số & Tài Sản Mã Hóa",
            "pillar": "Tài Sản Số & Xu Hướng",
            "files": ["crypto", "tien-so", "tien-ao", "tien-dien-tu"],
            "desc": "Kiến thức tiền mã hóa, blockchain, tiền kỹ thuật số và an toàn"
        },
        {
            "name": "Tính Lương Gross - Net",
            "pillar": "Thu Nhập & Lao Động",
            "files": ["tinh-luong", "thu-nhap"],
            "desc": "Công cụ chuyển đổi lương Gross sang Net và ngược lại chuẩn 2026"
        },
        {
            "name": "Đầu Tư & Quản Trị Tài Sản",
            "pillar": "Đầu Tư & Tích Sản",
            "files": ["dau-tu", "tai-san", "tieu-san", "von-luu-dong"],
            "desc": "Phân bổ danh mục đầu tư, quản lý tài sản và dòng vốn"
        },
        {
            "name": "Điểm Tín Dụng & Nợ Xấu (CIC)",
            "pillar": "Tín Dụng & Sức Khỏe Tín Dụng",
            "files": ["diem-tin-dung", "no-xau", "no"],
            "desc": "Tra cứu điểm tín dụng cá nhân CIC, kiểm tra nợ xấu và xóa nợ"
        },
        {
            "name": "Trả Góp & Mua Trước Trả Sau",
            "pillar": "Tín Dụng & Tiêu Dùng",
            "files": ["tra-gop", "vi-tra-sau", "mua-truoc-tra-sau"],
            "desc": "Tính phí trả góp 0%, chuyển đổi trả góp Ví Trả Sau và BNPL"
        },
        {
            "name": "Trái Phiếu Doanh Nghiệp & CP",
            "pillar": "Đầu Tư & Tích Sản",
            "files": ["trai-phieu"],
            "desc": "Tra cứu thị trường trái phiếu, lợi suất đáo hạn YTM và rủi ro"
        },
        {
            "name": "Chứng Chỉ Quỹ & Quỹ Mở SIP",
            "pillar": "Đầu Tư & Tích Sản",
            "files": ["chung-chi-quy", "quy-etf", "quy-mo", "uy-thac"],
            "desc": "Cổng 30 quỹ mở, giá NAV, tích sản SIP định kỳ từ 10.000đ/ngày"
        },
        {
            "name": "Kinh Tế Vĩ Mô & Chỉ Số",
            "pillar": "Kinh Tế Vĩ Mô",
            "files": ["gdp", "lam-phat", "giam-phat"],
            "desc": "Chỉ số GDP, tỷ lệ lạm phát, CPI và dự báo kinh tế vĩ mô"
        },
        {
            "name": "Quản Lý Dòng Tiền & Kế Hoạch FIRE",
            "pillar": "Quản Lý Tài Chính Cá Nhân",
            "files": ["dong-tien", "ke-hoach-tai-chinh", "tu-do-tai-chinh", "quy-du-phong", "quy-huu-tri"],
            "desc": "Kế hoạch tự do tài chính FIRE, quỹ dự phòng khẩn cấp và hưu trí"
        }
    ]

    all_kws_hub = {}
    market_results = []

    for m in MARKETS_DEF:
        m_kws = {}
        for fname in m["files"]:
            k_dict = file_kws.get(fname.strip(), {})
            for k, v in k_dict.items():
                m_kws[k] = max(m_kws.get(k, 0), v)
                all_kws_hub[k] = max(all_kws_hub.get(k, 0), v)
        
        m_vol = sum(m_kws.values())
        market_results.append({
            "name": m["name"],
            "pillar": m["pillar"],
            "kw_count": len(m_kws),
            "volume": m_vol,
            "desc": m["desc"]
        })

    # Sort descending by volume
    market_results.sort(key=lambda x: x["volume"], reverse=True)

    total_hub_vol = sum(all_kws_hub.values())
    total_hub_kw = len(all_kws_hub)

    print("=" * 95)
    print("FINANCIAL HUB INVENTORY SYNTHESIS (DEDUPLICATED)")
    print("=" * 95)
    print(f"Total Unique Keywords in Financial Hub: {total_hub_kw:,}")
    print(f"Total Unique Monthly Search Volume:     {total_hub_vol:,}\n")

    print(f"{'STT':<4} | {'Thị Trường / Dịch Vụ':<32} | {'Trụ Cột Nghiệp Vụ':<24} | {'Từ Khóa':<8} | {'Volume / Tháng':<14} | {'Tỷ Trọng (%)':<9}")
    print("-" * 105)
    for i, r in enumerate(market_results):
        share = (r["volume"] / total_hub_vol * 100) if total_hub_vol > 0 else 0
        print(f"{i+1:<4} | {r['name']:<32} | {r['pillar']:<24} | {r['kw_count']:<8,d} | {r['volume']:<14,d} | {share:6.2f}%")

if __name__ == "__main__":
    main()
