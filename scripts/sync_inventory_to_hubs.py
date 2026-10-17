#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYNC INVENTORY TO HUBS-MOMO PIPELINE
Tự động quét toàn bộ kho từ khóa Use Cases (05_HUBS/inventory/),
áp dụng động cơ Keyword Intelligence (Multi-signal Intent Classifier,
Semantic Domain Filter, SERP Cannibalization Shield)
và đồng bộ trực tiếp sang hubs-momo (react-web-momo) phục vụ giao diện & nội dung.
"""

import sys
import os
import glob
import csv
import re
import math
import json
from collections import defaultdict, Counter

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INVENTORY_DIR = os.path.join(BASE_DIR, "05_HUBS", "inventory")
HUBS_REPO = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"

# Thêm scripts vào path để import thư viện lib
sys.path.insert(0, BASE_DIR)
from scripts.lib.keyword_intelligence import (
    MultiSignalIntentClassifier,
    SemanticDomainFilter,
    SERPCannibalizationShield,
    MoMoDomainSERPShield,
    InternalLinkingTopologyEngine,
    GEODirectAnswerGenerator
)

MERGE_MAP = {
    # Financial
    'vang': 'gia-vang',
    'tiet-kiem': 'gui-tiet-kiem',
    'no': 'no-xau',
    'thu-nhap': 'thue-tncn',
    'cic': 'diem-tin-dung',
    # Lottery
    'xskt': 'xo-so',
    # Insurtech
    'bao-hiem-y-te': 'bhyt',
    'bao-hiem-xe': 'bao-hiem-xe-may',
    'bao-hiem-than-vo': 'bao-hiem-o-to',
    'bao-hiem-vat-chat': 'bao-hiem-o-to',
    'dong-bao-hiem': 'bhxh',
    'bao-hiem': 'bhxh',
    'bao-hiem-benh': 'bao-hiem-tai-nan',
    # PS
    'nap-xu-tiktok': 'nap-tiktok',
    'nap-the-game': 'nap-game',
    # Cinema
    'mua-ve-phim': 'dat-phim',
    # OTA
    'du-lich-my': 'visa-du-lich',
    # Vehicle Hub
    'bien-so': 'bien-so-xe',
    'garage-o-to': 'gara-o-to',
    'cuu-ho-o-to': 'cuu-ho-xe',
    'trạm-sac': 'tram-sac',
    'cay-xang': 'tram-xang',
}

VIETNAMESE_THEME_NAMES = {
    # === Financial (101) ===
    'ACB': 'Ngân Hàng ACB',
    'BIDV': 'Ngân Hàng BIDV',
    'Eximbank': 'Ngân Hàng Eximbank',
    'Indovina Bank': 'Ngân Hàng Indovina Bank',
    'LPBank': 'Ngân Hàng LPBank',
    'MSB': 'Ngân Hàng MSB',
    'Shinhan Bank': 'Ngân Hàng Shinhan Bank',
    'Techcombank': 'Ngân Hàng Techcombank',
    'Vietcombank': 'Ngân Hàng Vietcombank',
    'VietinBank': 'Ngân Hàng VietinBank',
    'ab-bank': 'Ngân Hàng ABBank',
    'agribank': 'Ngân Hàng Agribank',
    'bac': 'Bạc & Kim Loại Quý',
    'bac-a-bank': 'Ngân Hàng Bac A Bank',
    'ban-viet': 'Ngân Hàng Bản Việt (BVBank)',
    'bao-viet-bank': 'Ngân Hàng BaoViet Bank',
    'chia-co-tuc': 'Chia Cổ Tức',
    'chung-chi-quy': 'Chứng Chỉ Quỹ',
    'chung-chi-tien-gui': 'Chứng Chỉ Tiền Gửi',
    'chung-khoan': 'Chứng Khoán',
    'chuyen-khoan': 'Chuyển Khoản & Chuyển Tiền',
    'co-phieu': 'Cổ Phiếu',
    'co-tuc': 'Cổ Tức',
    'crypto': 'Tiền Điện Tử (Crypto)',
    'dau-tu': 'Đầu Tư Tài Chính',
    'diem-tin-dung': 'Điểm Tín Dụng & Tra Cứu CIC',
    'doi-tien': 'Đổi Ngoại Tệ',
    'dong-tien': 'Quản Lý Dòng Tiền',
    'donga bank': 'Ngân Hàng Đông Á',
    'du-no': 'Dư Nợ Tín Dụng',
    'gdp': 'Tổng Sản Phẩm Quốc Nội (GDP)',
    'gia-vang': 'Giá Vàng',
    'giam-phat': 'Giảm Phát',
    'giam-tru-gia-canh': 'Giảm Trừ Gia Cảnh',
    'gui-tiet-kiem': 'Gửi Tiết Kiệm',
    'hd-bank': 'Ngân Hàng HDBank',
    'internet-banking': 'Ngân Hàng Trực Tuyến (Internet Banking)',
    'ke-hoach-tai-chinh': 'Kế Hoạch Tài Chính',
    'kien-long-bank': 'Ngân Hàng KienlongBank',
    'kieu-hoi': 'Kiều Hối',
    'ky-quy': 'Ký Quỹ',
    'lai-kep': 'Lãi Kép & Công Thức Tính',
    'lai-suat': 'Lãi Suất Ngân Hàng',
    'lai-vay': 'Lãi Vay',
    'lam-phat': 'Lạm Phát',
    'ma-chung-khoan': 'Mã Cổ Phiếu & Chứng Khoán',
    'masteer-card': 'Thẻ Mastercard',
    'mbbank': 'Ngân Hàng MBBank',
    'mua-truoc-tra-sau': 'Mua Trước Trả Sau (BNPL)',
    'nam-a-bank': 'Ngân Hàng Nam A Bank',
    'napas': 'Cổng Thanh Toán NAPAS',
    'ncb': 'Ngân Hàng NCB',
    'ngan-hang': 'Hệ Thống Ngân Hàng',
    'ngoai-te': 'Tỷ Giá Ngoại Tệ',
    'no-xau': 'Nợ Xấu & CIC',
    'ocb': 'Ngân Hàng OCB',
    'ocean-bank': 'Ngân Hàng OceanBank',
    'phai-sinh': 'Chứng Khoán Phái Sinh',
    'pvcom bank': 'Ngân Hàng PVcomBank',
    'quy-du-phong': 'Quỹ Dự Phòng Khẩn Cấp',
    'quy-etf': 'Quỹ ETF',
    'quy-huu-tri': 'Quỹ Hưu Trí Tự Nguyện',
    'quy-mo': 'Quỹ Mở',
    'sacombank': 'Ngân Hàng Sacombank',
    'saigonbank': 'Ngân Hàng Saigonbank',
    'scb': 'Ngân Hàng SCB',
    'seabank': 'Ngân Hàng SeABank',
    'shb': 'Ngân Hàng SHB',
    'tai-san': 'Quản Trị Tài Sản',
    'thanh-toan-qr': 'Thanh Toán Mã QR',
    'thau-chi': 'Thấu Chi Tài Khoản',
    'the-ghi-no': 'Thẻ Ghi Nợ (Debit Card)',
    'the-tin-dung': 'Thẻ Tín Dụng',
    'the-tra-truoc': 'Thẻ Trả Trước',
    'the-visa': 'Thẻ Quốc Tế Visa',
    'thue': 'Tra Cứu & Nộp Thuế',
    'thue-tncn': 'Thuế Thu Nhập Cá Nhân (TNCN)',
    'tich-luy': 'Tích Lũy Tiền',
    'tien-ao': 'Tiền Ảo & Tài Sản Số',
    'tien-dien-tu': 'Tiền Điện Tử & Ví Điện Tử',
    'tien-so': 'Tiền Kỹ Thuật Số',
    'tieu-san': 'Tài Sản & Tiêu Sản',
    'tin-dung': 'Tín Dụng Cá Nhân',
    'tinh-luong': 'Tính Lương Gross Sang Net',
    'tpbank': 'Ngân Hàng TPBank',
    'tra-gop': 'Mua Hàng Trả Góp',
    'trai-phieu': 'Trái Phiếu Doanh Nghiệp',
    'tu-do-tai-chinh': 'Tự Do Tài Chính (FIRE)',
    'ty-gia': 'Tỷ Giá Ngoại Tệ',
    'uy-thac': 'Ủy Thác Đầu Tư',
    'vay': 'Vay Tiền Nhanh',
    'vay-the-chap': 'Vay Thế Chấp',
    'vay-tin-chap': 'Vay Tín Chấp',
    'vi-dien-tu': 'Ví Điện Tử',
    'vi-tra-sau': 'Ví Trả Sau',
    'vib': 'Ngân Hàng VIB',
    'vietbank': 'Ngân Hàng Vietbank',
    'von-luu-dong': 'Vốn Lưu Động',
    'vpbank': 'Ngân Hàng VPBank',
    'vrb': 'Ngân Hàng Việt Nga (VRB)',

    # === Lottery (3) ===
    've-so': 'Dò Vé Số Trực Tuyến',
    'vietlott': 'Vietlott Mega & Power',
    'xo-so': 'Xổ Số Kiến Thiết 3 Miền',

    # === PS (4) ===
    'game-app': 'Ứng Dụng Game',
    'nap-game': 'Nạp Thẻ Game',
    'nap-the-game': 'Nạp Thẻ Game',
    'nap-tiktok': 'Nạp Xu TikTok',
    'nph-game': 'Nhà Phát Hành Game',

    # === cinema (5) ===
    'dat-phim': 'Đặt Vé Phim Online',
    'lich-phim': 'Lịch Chiếu Phim Rạp',
    'phim': 'Phim Chiếu Rạp Mới Nhất',
    'rap': 'Rạp Chiếu Phim & Cụm Rạp',
    've-xem-phim': 'Giá Vé Xem Phim & Khuyến Mãi',

    # === hospital (5) ===
    'benh-vien': 'Bệnh Viện & Phòng Khám',
    'bmi': 'Chỉ Số BMI Chuẩn',
    'dat-lich-kham-benh': 'Đặt Lịch Khám Bệnh',
    'tinh-bmi': 'Tính Chỉ Số BMI',
    'tinh-calo': 'Tính Calo & Dinh Dưỡng',

    # === insurtech (8) ===
    'bao-hiem-chay-no': 'Bảo Hiểm Cháy Nổ',
    'bao-hiem-nhan-tho': 'Bảo Hiểm Nhân Thọ',
    'bao-hiem-o-to': 'Bảo Hiểm Ô Tô (TNDS & Vật Chất)',
    'bao-hiem-tai-nan': 'Bảo Hiểm Tai Nạn & Sức Khỏe',
    'bao-hiem-xe-may': 'Bảo Hiểm Xe Máy Bắt Buộc',
    'bhxh': 'Bảo Hiểm Xã Hội (BHXH)',
    'bhyt': 'Bảo Hiểm Y Tế (BHYT)',
    'phi-bao-hiem': 'Biểu Phí Bảo Hiểm',

    # === ota (19) ===
    'dat-resort': 'Đặt Resort Nghỉ Dưỡng',
    'du-lich': 'Cẩm Nang Du Lịch',
    'du-lich-an-do': 'Du Lịch Ấn Độ',
    'du-lich-dai-loan': 'Du Lịch Đài Loan',
    'du-lich-han-quoc': 'Du Lịch Hàn Quốc',
    'du-lich-hongkong': 'Du Lịch Hồng Kông',
    'du-lich-nhat': 'Du Lịch Nhật Bản',
    'du-lich-singapore': 'Du Lịch Singapore',
    'du-lich-thai-lan': 'Du Lịch Thái Lan',
    'du-lich-trung-quoc': 'Du Lịch Trung Quốc',
    'du-lich-viet-nam': 'Du Lịch Việt Nam',
    'gia-pha': 'Cây Gia Phả Dòng Họ',
    'tour-du-lich': 'Tour Du Lịch Trọn Gói',
    've-cap-treo': 'Vé Cáp Treo',
    've-may-bay': 'Vé Máy Bay Giá Rẻ',
    've-tau': 'Vé Tàu Hỏa Bắc Nam',
    've-xe': 'Vé Xe Khách & Xe Bus',
    'visa-du-lich': 'Thủ Tục Visa Du Lịch',
    'xe-khach': 'Đặt Vé Xe Khách',

    # === other (6) ===
    'lich-am': 'Lịch Âm Hôm Nay',
    'lich-van-nien': 'Lịch Vạn Niên',
    'ma-giam-gia': 'Mã Giảm Giá & Voucher',
    'ma-so-thue': 'Tra Cứu Mã Số Thuế',
    'tu-vi': 'Tử Vi Hàng Ngày & Trọn Đời',
    'voucher': 'Voucher Ưu Đãi & Khuyến Mãi',

    # === telco (5) ===
    'Data-3g': 'Gói Cước Data 3G',
    'data-4g': 'Gói Cước Data 4G Tốc Độ Cao',
    'data-5g': 'Gói Cước Data 5G Siêu Tốc',
    'nap-data': 'Nạp Data 3G/4G/5G Trực Tuyến',
    'sim': 'SIM Số Đẹp & eSIM',

    # === trust (2) ===
    'bao-cao-lua-dao': 'Báo Cáo Gian Lận & Lừa Đảo',
    'lua-dao': 'Cảnh Báo Thủ Đoạn Lừa Đảo',

    # === vehicle-hub (35) ===
    'bai-do-xe': 'Bãi Đỗ Xe & Bãi Giữ Xe',
    'bai-giu-xe': 'Bãi Giữ Xe Ô Tô & Xe Máy',
    'bao-duong-xe': 'Bảo Dưỡng Xe Định Kỳ',
    'bien-so-dep': 'Đấu Giá Biển Số Đẹp',
    'bien-so-xe': 'Tra Cứu Biển Số Xe Toàn Quốc',
    'chi-duong': 'Chỉ Đường & Bản Đồ Giao Thông',
    'cuu-ho-xe': 'Cứu Hộ Ô Tô & Xe Máy',
    'dang-kiem': 'Tra Cứu & Đặt Hẹn Đăng Kiểm Xe',
    'dinh-gia-xe': 'Định Giá Xe Ô Tô & Xe Máy',
    'doi-pin': 'Trạm Đổi Pin Xe Điện',
    'epass': 'Thu Phí Tự Động ePass',
    'gara-o-to': 'Gara Ô Tô Uy Tín',
    'garage-keywords-for-search-volume': 'Tra Cứu Hệ Thống Garage',
    'garage-keywords-list': 'Gara Ô Tô (Tổng Hợp)',
    'gia-dau': 'Giá Dầu Hôm Nay',
    'gia-xang': 'Giá Xăng Hôm Nay',
    'gia-xe': 'Bảng Giá Xe Ô Tô & Xe Máy',
    'giay-phep-lai-xe': 'Tra Cứu Giấy Phép Lái Xe',
    'loi-giao-thong': 'Tra Cứu Lỗi Vi Phạm Giao Thông',
    'ly-thuyet-lai-xe': 'Học Lý Thuyết Lái Xe A1, B1, B2',
    'metro': 'Tuyến Metro Bến Thành - Suối Tiên',
    'partner-garages': 'Danh Sách Đối Tác Garage',
    'phan-mem-mo-phong': 'Phần Mềm Mô Phỏng 120 Tình Huống',
    'phat-nguoi': 'Tra Cứu Phạt Nguội Toàn Quốc',
    'phi-duong-bo': 'Biểu Phí Sử Dụng Đường Bộ',
    'phi-khong-dung': 'Thu Phí Không Dừng (ETC)',
    'rua-xe': 'Dịch Vụ Rửa Xe Chuyên Nghiệp',
    'sang-ten-xe': 'Thủ Tục Sang Tên Đổi Chủ Xe',
    'sua-xe': 'Dịch Vụ Sửa Xe Lưu Động',
    'thi-bang-lai-xe': 'Thi Bằng Lái Xe Máy & Ô Tô',
    'thue-truoc-ba': 'Tính Thuế Trước Bạ Xe',
    'tram-sac': 'Trạm Sạc Xe Điện Toàn Quốc',
    'tram-xang': 'Trạm Xăng Gần Nhất',
    'tuyen-xe-buyt': 'Tra Cứu Tuyến Xe Buýt',
    'vetc': 'Thu Phí Tự Động VETC',
}

SECTOR_SPECIFIC_RULES = {
    'Financial': [
        ('Tỷ giá & Ngoại tệ', ['tỷ giá', 'ty gia', 'đô la', 'usd', 'ngoại tệ', 'ngoai te', 'euro', 'dxy', 'vnd', 'chuyển đổi']),
        ('Giá vàng & Kim loại quý', ['giá vàng', 'gia vang', 'vàng sjc', 'vàng 9999', 'nhẫn trơn', 'vàng miếng', 'vàng tây']),
        ('Lãi suất & Tiền gửi', ['lãi suất', 'lai suat', 'tiết kiệm', 'tiet kiem', 'gửi tiền', 'gui tien', 'kỳ hạn', 'ky han', 'rút tiền']),
        ('Vay vốn & Tín chấp', ['vay', 'vay vốn', 'vay von', 'vay tiền', 'vay tien', 'tín chấp', 'tin chap', 'thế chấp', 'the chap', 'trả góp', 'tra gop', 'hạn mức']),
        ('Thẻ & Tài khoản', ['thẻ', 'the atm', 'thẻ tín dụng', 'the tin dung', 'mở thẻ', 'mo the', 'tài khoản', 'tai khoan', 'số tài khoản', 'phát hành thẻ']),
        ('Biểu phí & Thủ tục', ['phí', 'biểu phí', 'bieu phi', 'thủ tục', 'thu tuc', 'hồ sơ', 'ho so', 'điều kiện', 'dieu kien', 'hướng dẫn', 'huong dan', 'cách']),
        ('Tra cứu & Chi nhánh', ['tra cứu', 'tra cuu', 'chi nhánh', 'chi nhanh', 'phòng giao dịch', 'tổng đài', 'tong dai', 'hotline', 'địa chỉ', 'dia chi', 'swift']),
    ],
    'vehicle-hub': [
        ('Phạt nguội & Luật giao thông', ['phạt nguội', 'phat nguoi', 'lỗi vi phạm', 'mức phạt', 'nghị định', 'trừ điểm', 'bằng lái', 'giấy phép', 'camera']),
        ('Bảo dưỡng & Nuôi xe', ['bảo dưỡng', 'bao duong', 'thay nhớt', 'chi phí', 'nuôi xe', 'xăng dầu', 'giá xăng', 'tiêu hao', 'đăng kiểm', 'sang tên']),
        ('Gara & Cứu hộ', ['gara', 'garage', 'cứu hộ', 'cuu ho', 'sửa xe', 'sua xe', 'rửa xe', 'rua xe', 'vá lốp', 'kéo xe']),
        ('Định giá & Mua bán xe', ['giá xe', 'gia xe', 'định giá', 'dinh gia', 'lăn bánh', 'lan banh', 'mua xe', 'bán xe', 'trả góp xe']),
    ],
    'insurtech': [
        ('Quy định & Mức bồi thường', ['bồi thường', 'boi thuong', 'chi trả', 'mức phạt', 'bắt buộc', 'tnds', 'quy định', 'luật', 'nghị định', 'hồ sơ']),
        ('Biểu phí & Mua bảo hiểm', ['phí', 'biểu phí', 'giá', 'bao nhiêu tiền', 'mua', 'đóng', 'nộp', 'tái tục', 'online', 'trực tuyến']),
        ('Tra cứu & Hạn sử dụng', ['tra cứu', 'kiểm tra', 'check', 'thời hạn', 'hạn sử dụng', 'mã số', 'thẻ', 'sổ']),
        ('Quyền lợi & Chế độ', ['quyền lợi', 'khám chữa bệnh', 'bệnh viện', 'thanh toán', 'hưởng', 'chế độ', 'thai sản', 'hưu trí', 'ốm đau']),
    ],
    'Lottery': [
        ('Kết quả xổ số', ['kết quả', 'ket qua', 'xsmb', 'xsmn', 'xsmt', 'sxtt', 'trực tiếp', 'truc tiep', 'kqsx', 'sxmb', 'sxmn', 'sxmt', 'xo so', 'xổ số', 'xô số', 'xô sô', 'xo số', 'xskt', 'kiến thiết', 'kien thiet', 'hôm nay', 'hom nay', 'miền bắc', 'miền nam', 'miền trung', 'minh ngọc', 'minhngoc']),
        ('Thống kê & Soi cầu', ['thống kê', 'thong ke', 'soi cầu', 'soi cau', 'lô gan', 'chu kỳ', 'tần suất', 'đầu đuôi', 'bạch thủ']),
        ('Cơ cấu & Đổi thưởng', ['giải thưởng', 'giai thuong', 'trúng thưởng', 'đổi vé', 'lãnh thưởng', 'thời hạn', 'cơ cấu', 'co cau', 'vé số', 've so']),
    ],
    'cinema': [
        ('Lịch chiếu & Suất chiếu', ['lịch chiếu', 'lich chieu', 'suất chiếu', 'suat chieu', 'gio chieu', 'chiếu rạp', 'phim chiếu', 'lịch phim']),
        ('Giá vé & Khuyến mãi', ['giá vé', 'gia ve', 'vé rẻ', 've re', 'khuyến mãi', 'khuyen mai', 'ưu đãi', 'voucher', 'combo', 'giảm giá']),
        ('Cụm rạp & Đặt vé', ['rạp', 'cgv', 'lotte', 'bhd', 'galaxy', 'cinestar', 'đặt vé', 'dat ve', 'đặt phim', 'mua vé']),
        ('Review & Đánh giá phim', ['review', 'đánh giá', 'danh gia', 'nội dung', 'diễn viên', 'trailer', 'phim hay', 'top phim']),
    ],
    'PS': [
        ('Nạp thẻ & Nạp game', ['nạp', 'nap', 'thẻ', 'the', 'chiết khấu', 'chiet khau', 'garena', 'zing', 'vcoin', 'xu', 'tiktok', 'mua thẻ']),
        ('Tựa game & Sự kiện', ['game', 'liên quân', 'free fire', 'pubg', 'tốc chiến', 'sự kiện', 'giftcode', 'code']),
        ('Tài khoản & Nhà phát hành', ['tài khoản', 'tai khoan', 'đăng ký', 'nhà phát hành', 'nph', 'vng', 'garena', 'vtc']),
    ],
    'hospital': [
        ('Đặt khám & Bác sĩ', ['đặt khám', 'dat kham', 'bác sĩ', 'bac si', 'bệnh viện', 'benh vien', 'phòng khám', 'chuyên khoa']),
        ('Chỉ số & Sức khỏe', ['bmi', 'calo', 'cân nặng', 'chiều cao', 'dinh dưỡng', 'sức khỏe']),
    ],
    'ota': [
        ('Đặt phòng & Resort', ['khách sạn', 'khach san', 'resort', 'homestay', 'đặt phòng', 'dat phong', 'villa']),
        ('Vé máy bay & Di chuyển', ['vé máy bay', 've may bay', 'chuyến bay', 'vé tàu', 'vé xe', 'xe khách', 'cáp treo']),
        ('Tour & Điểm đến', ['tour', 'du lịch', 'du lich', 'hành trình', 'lịch trình', 'visa', 'điểm đến']),
    ],
    'telco': [
        ('Gói cước & Data 4G/5G', ['data', '4g', '5g', '3g', 'gói cước', 'goi cuoc', 'nạp data', 'dung lượng']),
        ('SIM & Tài khoản', ['sim', 'sim số', 'chính chủ', 'esim', 'tài khoản điện thoại', 'nạp thẻ']),
    ]
}

# Đầu ra dữ liệu
LOCAL_DATA_DIR = os.path.join(BASE_DIR, "07_REPORTS", "data")
LOCAL_OUTPUT_PATH = os.path.join(LOCAL_DATA_DIR, "inventory_clusters_summary.json")
LOCAL_MD_PATH = os.path.join(BASE_DIR, "07_REPORTS", "KEYWORD_INVENTORY_MASTER.md")

HUBS_DASHBOARD_DATA = os.path.join(HUBS_REPO, "lib", "dashboard", "seo-inventory-clusters.json")
HUBS_PUBLIC_DATA = os.path.join(HUBS_REPO, "data", "seo-clusters-summary.json")

STOPWORDS = {
    'và', 'là', 'của', 'ở', 'tại', 'cho', 'với', 'trong', 'các', 'những',
    'được', 'có', 'ra', 'khi', 'về', 'này', 'đó', 'từ', 'theo', 'như',
    'để', 'lại', 'thì', 'người', 'cái', 'làm', 'hay', 'bao', 'nhiêu',
    'gì', 'sao', 'nao', 'nào', 'mấy'
}

TELEX_FIXES = {
    'ddaaus': 'đấu',
    'ddieenj': 'điện',
    'ddoof': 'đồ',
    'ddoongf': 'đồng',
    'ngan hang': 'ngân hàng',
    'tiet kiem': 'tiết kiệm',
    'lai suat': 'lãi suất',
    'bien so': 'biển số',
    'bao hiem': 'bảo hiểm',
    'o to': 'ô tô',
    'xe may': 'xe máy',
}

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

def classify_quadrant(volume, competition, intent):
    comp_val = competition.lower()
    is_high_comp = 'high' in comp_val or 'medium' in comp_val
    if volume >= 1500 and not is_high_comp:
        return 'Quick Win'
    elif volume >= 5000 and is_high_comp:
        return 'Strategic Pillar'
    elif volume >= 200 and intent in ['Commercial', 'Tool/Calculator', 'Transactional']:
        return 'Commercial Converter'
    else:
        return 'Long-tail / Supporting'

def build_adaptive_clusters(canonical_clusters, sector=None, top_n_clusters=5):
    """
    Gom cụm các Canonical Leaders theo các nhóm thực thể chủ đạo chuẩn ngữ nghĩa phân tách theo Sector
    """
    clusters = defaultdict(list)
    rules = SECTOR_SPECIFIC_RULES.get(sector, [])

    for item in canonical_clusters:
        kw = item['keyword'].lower()
        matched = False
        for topic_name, triggers in rules:
            if any(tr in kw for tr in triggers):
                clusters[topic_name].append(item)
                matched = True
                break
        if not matched:
            intent = item['intent']
            intent_fallback_names = {
                'Tool/Calculator': 'Công cụ & Tra cứu trực tuyến',
                'Commercial': 'So sánh & Đánh giá giải pháp',
                'Transactional': 'Đăng ký & Giao dịch trực tuyến',
                'Informational': 'Cẩm nang & Hướng dẫn chi tiết',
                'Navigational': 'Cổng dịch vụ & Liên hệ'
            }
            fb_name = intent_fallback_names.get(intent, 'Chủ đề liên quan')
            clusters[fb_name].append(item)

    result_clusters = []
    sorted_clusters = sorted(clusters.items(), key=lambda x: sum(k['total_cluster_volume'] for k in x[1]), reverse=True)

    for cluster_name, items in sorted_clusters[:top_n_clusters]:
        tot_vol = sum(k['total_cluster_volume'] for k in items)
        top_kws = sorted(items, key=lambda x: (x['opportunity_score'], x['volume']), reverse=True)[:5]
        result_clusters.append({
            'cluster_name': cluster_name,
            'count': len(items),
            'total_volume': tot_vol,
            'top_keywords': [
                {
                    'keyword': k['keyword'],
                    'volume': k['volume'],
                    'cluster_volume': k['total_cluster_volume'],
                    'intent': k['intent'],
                    'score': k['opportunity_score'],
                    'secondary_synonyms': k.get('secondary_keywords', [])[:3]
                } for k in top_kws
            ]
        })

    return result_clusters

def process_csv_paths(csv_paths, sector, canonical_slug):
    usecase_slug = canonical_slug
    usecase_name = VIETNAMESE_THEME_NAMES.get(usecase_slug, usecase_slug.replace('-', ' ').replace('_', ' ').title())
    
    raw_keywords_map = {}
    outliers_filtered = 0
    total_raw_rows = 0

    for csv_path in csv_paths:
        with open(csv_path, 'r', encoding='utf-8-sig', errors='replace') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_raw_rows += 1
                kw_raw = row.get('Keyword', '')
                if not kw_raw:
                    continue
                kw = normalize_text(clean_val(kw_raw))
                if kw in raw_keywords_map:
                    continue

                # 1. Dynamic Domain Outlier Filtering
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

                # 2. Multi-Signal Weighted Intent Classifier
                intent_res = MultiSignalIntentClassifier.classify(kw)
                intent = intent_res['intent']
                opp_score = calculate_opportunity_score(vol, cpc, comp, intent)
                quadrant = classify_quadrant(vol, comp, intent)

                raw_keywords_map[kw] = {
                    'keyword': kw,
                    'volume': vol,
                    'cpc': cpc,
                    'competition': comp,
                    'intent': intent,
                    'intent_confidence': intent_res['confidence'],
                    'opportunity_score': opp_score,
                    'quadrant': quadrant
                }

    raw_keywords = list(raw_keywords_map.values())
    if not raw_keywords:
        return None

    # 3. SERP Intent Fingerprinting & Cannibalization Shield
    canonical_clusters, merge_log = SERPCannibalizationShield.cluster_and_shield(raw_keywords)

    total_volume = sum(k['volume'] for k in raw_keywords)

    intent_counts = Counter(k['intent'] for k in canonical_clusters)
    quadrant_counts = Counter(k['quadrant'] for k in canonical_clusters)

    top_opportunities = sorted(canonical_clusters, key=lambda x: (x['opportunity_score'], x['volume']), reverse=True)[:10]
    pillar_item = sorted(canonical_clusters, key=lambda x: x['total_cluster_volume'], reverse=True)[0]

    sub_clusters = build_adaptive_clusters(canonical_clusters, sector=sector)

    # 4. Domain SERP Cannibalization Shield
    shield_eval = MoMoDomainSERPShield.evaluate_cannibalization_risk(pillar_item['keyword'], sector=sector, check_live_serp=False)
    cannibalization_shield = {
        'risk_level': shield_eval['risk_level'],
        'verdict': shield_eval['verdict'],
        'action': shield_eval['action'],
        'serp_rank': shield_eval.get('serp_rank'),
        'top_live_url': shield_eval.get('top_live_url'),
        'rationale': shield_eval['rationale']
    }

    return {
        'id': usecase_slug,
        'name': usecase_name,
        'display_name': usecase_name,
        'sector': sector,
        'file_name': ", ".join([os.path.basename(p) for p in csv_paths]),
        'total_raw_keywords': total_raw_rows,
        'clean_keywords_count': len(raw_keywords),
        'outliers_filtered_count': outliers_filtered,
        'canonical_topics_count': len(canonical_clusters),
        'cannibalization_merged_count': len(merge_log),
        'total_volume': total_volume,
        'cannibalization_shield': cannibalization_shield,
        'pillar_keyword': {
            'keyword': pillar_item['keyword'],
            'volume': pillar_item['volume'],
            'cluster_volume': pillar_item['total_cluster_volume'],
            'intent': pillar_item['intent'],
            'secondary_synonyms': pillar_item.get('secondary_keywords', [])[:5]
        },
        'intent_breakdown': dict(intent_counts),
        'quadrant_breakdown': dict(quadrant_counts),
        'top_opportunities': [
            {
                'keyword': k['keyword'],
                'volume': k['volume'],
                'cluster_volume': k['total_cluster_volume'],
                'cpc': k['cpc'],
                'competition': k['competition'],
                'intent': k['intent'],
                'score': k['opportunity_score'],
                'quadrant': k['quadrant'],
                'secondary_synonyms': k.get('secondary_keywords', [])[:3]
            } for k in top_opportunities
        ],
        'sub_clusters': sub_clusters
    }

def main():
    print(f"Bắt đầu quét và đồng bộ kho Inventory từ: {INVENTORY_DIR}")
    if not os.path.exists(INVENTORY_DIR):
        print(f"Lỗi: Không tìm thấy thư mục {INVENTORY_DIR}")
        sys.exit(1)
        
    sectors = sorted([d for d in os.listdir(INVENTORY_DIR) if os.path.isdir(os.path.join(INVENTORY_DIR, d)) and not d.startswith('.')])
    
    all_usecases = []
    sector_summary = {}
    total_kws_all = 0
    total_vol_all = 0
    total_cannibalized_all = 0
    total_outliers_all = 0
    
    for s in sectors:
        s_dir = os.path.join(INVENTORY_DIR, s)
        csv_files = sorted(glob.glob(os.path.join(s_dir, '*.csv')))

        slug_groups = defaultdict(list)
        for fpath in csv_files:
            raw_slug = os.path.splitext(os.path.basename(fpath))[0]
            # Tự động loại bỏ hậu tố nhân bản như (1), (2), _copy...
            clean_slug = re.sub(r'[\s_]*\(\d+\)$', '', raw_slug).strip()
            canonical_slug = MERGE_MAP.get(clean_slug, clean_slug)
            slug_groups[canonical_slug].append(fpath)

        s_usecases = []
        s_kws = 0
        s_vol = 0
        s_cannibalized = 0
        s_outliers = 0
        
        for canonical_slug, paths in slug_groups.items():
            # Ưu tiên tệp có thời gian sửa đổi (mtime) mới nhất
            paths.sort(key=lambda p: os.path.getmtime(p), reverse=True)
            res = process_csv_paths(paths, s, canonical_slug)
            if res:
                s_usecases.append(res)
                all_usecases.append(res)
                s_kws += res['clean_keywords_count']
                s_vol += res['total_volume']
                s_cannibalized += res['cannibalization_merged_count']
                s_outliers += res['outliers_filtered_count']
                
        sector_summary[s] = {
            'usecase_count': len(s_usecases),
            'total_keywords': s_kws,
            'total_volume': s_vol,
            'cannibalized_merged': s_cannibalized,
            'outliers_filtered': s_outliers
        }
        total_kws_all += s_kws
        total_vol_all += s_vol
        total_cannibalized_all += s_cannibalized
        total_outliers_all += s_outliers
        print(f"- Hub {s:15s}: {len(s_usecases):3d} themes | {s_kws:7,d} kws | {s_cannibalized:5,d} cannibalized merged | {s_vol:12,d} vol")
        
    print(f"\nTổng kết: {len(all_usecases)} themes | {total_kws_all:,} từ khóa sạch | {total_cannibalized_all:,} từ khóa được gom chống ăn thịt | {total_outliers_all:,} từ khóa nhiễu bị chặn.")
    
    # 0. Làm giàu dữ liệu: Tính toán Mạng lưới Liên kết nội bộ (Silo Topology) & GEO Direct Answers
    print("Đang tính toán mạng lưới liên kết nội bộ (Internal Linking Topology) & GEO Direct Answers...")
    for uc in all_usecases:
        # A. Internal Linking Matrix
        silo = InternalLinkingTopologyEngine.build_silo_matrix(uc, all_usecases)
        uc['internal_links'] = silo
        
        # B. GEO Optimization Block
        p_kw = uc['pillar_keyword']['keyword']
        p_intent = uc['pillar_keyword']['intent']
        uc['geo_optimization'] = {
            'direct_answer_snippet': GEODirectAnswerGenerator.generate_direct_answer_snippet(uc['name'], p_kw, p_intent, uc['sector']),
            'entity_facts': GEODirectAnswerGenerator.generate_entity_factsheet(uc['name'], uc['sector'], p_intent)
        }

    # 1. Đóng gói Snapshot Master & SSOT Local
    data_payload = {
        'version': '3.1-enterprise',
        'generated_at': '2026-10-16',
        'stats': {
            'total_usecases': len(all_usecases),
            'total_keywords': total_kws_all,
            'total_volume': total_vol_all,
            'total_cannibalized_shielded': total_cannibalized_all,
            'total_outliers_pruned': total_outliers_all,
            'total_sectors': len(sectors)
        },
        'sector_summary': sector_summary,
        'usecases': all_usecases
    }
    
    os.makedirs(LOCAL_DATA_DIR, exist_ok=True)
    with open(LOCAL_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(data_payload, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu Snapshot SSOT tại: {LOCAL_OUTPUT_PATH}")
    
    # 2. Tổng hợp Danh mục Quick Wins Toàn Nền Tảng (Cross-Hub Quick Wins Portfolio)
    all_quick_wins = []
    for uc in all_usecases:
        for opp in uc['top_opportunities']:
            if opp['quadrant'] == 'Quick Win':
                all_quick_wins.append({
                    'keyword': opp['keyword'],
                    'volume': opp['volume'],
                    'cluster_volume': opp['cluster_volume'],
                    'intent': opp['intent'],
                    'score': opp['score'],
                    'usecase': uc['name'],
                    'usecase_id': uc['id'],
                    'sector': uc['sector'],
                    'synonyms': opp.get('secondary_synonyms', [])
                })
    all_quick_wins.sort(key=lambda x: (x['score'], x['volume']), reverse=True)
    
    # Xuất Báo cáo Quick Wins Markdown
    qw_md_path = os.path.join(BASE_DIR, "07_REPORTS", "QUICK_WINS_PORTFOLIO.md")
    qw_md = f"""# DANH MỤC TỪ KHÓA QUICK WINS TOÀN WEB PLATFORM (HIGH ROI OPPORTUNITIES)

Tập hợp các từ khóa có **Search Volume cao ($\ge 1.500$) và Mức độ Cạnh tranh Thấp (Low PPC Competition)** trên toàn bộ 188 Use Cases của Web Platform. Đây là các chủ đề ưu tiên P0 mang lại lưu lượng truy cập nhanh nhất với chi phí nội dung tối thiểu.

- **Tổng số từ khóa Quick Wins phát hiện:** {len(all_quick_wins):,} từ khóa
- **Tổng dung lượng tìm kiếm Quick Wins:** {sum(x['volume'] for x in all_quick_wins):,} lượt/tháng

---

## TOP 50 TỪ KHÓA QUICK WINS ƯU TIÊN SẢN XUẤT P0

| STT | Từ Khóa Quick Win | Search Volume | Search Intent | Điểm Cơ Hội | Use Case | Phân Khối Ngành | Biến Thể Đồng Nghĩa Đã Gom Cụm |
| :---: | :--- | :---: | :---: | :---: | :--- | :--- | :--- |
"""
    for idx, qw in enumerate(all_quick_wins[:50], 1):
        syn_str = ", ".join(qw['synonyms'][:2]) if qw['synonyms'] else "Độc lập"
        qw_md += f"| {idx} | `{qw['keyword']}` | {qw['volume']:,} | `{qw['intent']}` | {qw['score']} | {qw['usecase']} | {qw['sector']} | {syn_str} |\n"

    with open(qw_md_path, 'w', encoding='utf-8') as f:
        f.write(qw_md)
    print(f"Đã xuất bản Danh mục Quick Wins tại: {qw_md_path}")

    # 3. Tạo Báo cáo Master Markdown
    md_content = f"""# TỔNG QUAN TÀI NGUYÊN TỪ KHÓA & TOPIC CLUSTERS WEB PLATFORM (SSOT INVENTORY V2)

Dữ liệu được trích xuất, lọc nhiễu tự động và bảo vệ chống ăn thịt từ khóa (Cannibalization Shield) từ kho `05_HUBS/inventory/`.
- **Tổng số Themes:** {len(all_usecases)}
- **Tổng số từ khóa theo dõi:** {total_kws_all:,}
- **Tổng số từ khóa trùng Intent được gom cụm (Shielded):** {total_cannibalized_all:,}
- **Tổng số từ khóa nhiễu bị loại bỏ:** {total_outliers_all:,}
- **Tổng dung lượng tìm kiếm thị trường:** {total_vol_all:,} lượt/tháng

---

## 1. TỔNG HỢP THEO HUBS

| Hub | Số Lượng Themes | Từ Khóa Sạch | Từ Khóa Gom Chống Cannibalization | Dung Lượng Tìm Kiếm (Volume/Tháng) |
| :--- | :---: | :---: | :---: | :---: |
"""
    for sec, stats in sorted(sector_summary.items(), key=lambda x: x[1]['total_volume'], reverse=True):
        md_content += f"| {sec} | {stats['usecase_count']:,} | {stats['total_keywords']:,} | {stats['cannibalized_merged']:,} | {stats['total_volume']:,} |\n"

    md_content += """\n---\n\n## 2. TOP THEMES CÓ QUY MÔ LỚN NHẤT\n\n| STT | Theme | Hub | Số Từ Khóa | Gom Cannibalized | Search Volume | Từ Khóa Cột Trụ (Pillar KW) | Top Quick Win |\n| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :--- |\n"""

    top_usecases = sorted(all_usecases, key=lambda x: x['total_volume'], reverse=True)[:25]
    for idx, uc in enumerate(top_usecases, 1):
        pkw = uc['pillar_keyword']['keyword']
        pvol = uc['pillar_keyword']['cluster_volume']
        qwin = next((k['keyword'] for k in uc['top_opportunities'] if k['quadrant'] == 'Quick Win'), 'N/A')
        md_content += f"| {idx} | {uc['name']} | {uc['sector']} | {uc['clean_keywords_count']:,} | {uc['cannibalization_merged_count']:,} | {uc['total_volume']:,} | {pkw} ({pvol:,}) | {qwin} |\n"

    with open(LOCAL_MD_PATH, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Đã cập nhật tài liệu báo cáo tại: {LOCAL_MD_PATH}")

    # 4. Xuất Modular Chunks & Đẩy trực tiếp sang hubs-momo
    if os.path.exists(HUBS_REPO):
        # A. Cập nhật Dashboard Payload siêu nhẹ
        os.makedirs(os.path.dirname(HUBS_DASHBOARD_DATA), exist_ok=True)
        dashboard_payload = {
            'stats': data_payload['stats'],
            'sector_summary': sector_summary,
            'top_usecases': sorted(all_usecases, key=lambda x: x['total_volume'], reverse=True)[:35],
            'recent_sync': data_payload['generated_at']
        }
        with open(HUBS_DASHBOARD_DATA, 'w', encoding='utf-8') as f:
            json.dump(dashboard_payload, f, ensure_ascii=False, indent=2)
        print(f"Đã push sang hubs-momo (Dashboard): {HUBS_DASHBOARD_DATA}")
        
        # B. Cập nhật File Tổng tương thích ngược
        os.makedirs(os.path.dirname(HUBS_PUBLIC_DATA), exist_ok=True)
        with open(HUBS_PUBLIC_DATA, 'w', encoding='utf-8') as f:
            json.dump(data_payload, f, ensure_ascii=False, indent=2)
        print(f"Đã push sang hubs-momo (Data layer master): {HUBS_PUBLIC_DATA}")

        # C. TRIỂN KHAI MODULAR CHUNKING: data/seo-clusters/index.json + chunks từng use case
        modular_dir = os.path.join(HUBS_REPO, "data", "seo-clusters")
        os.makedirs(modular_dir, exist_ok=True)

        # Index siêu nhẹ (~45 KB)
        index_payload = {
            'version': '3.0-modular',
            'generated_at': data_payload['generated_at'],
            'stats': data_payload['stats'],
            'sector_summary': sector_summary,
            'quick_wins_count': len(all_quick_wins),
            'usecases': [
                {
                    'id': uc['id'],
                    'name': uc['name'],
                    'display_name': uc.get('display_name', uc['name']),
                    'sector': uc['sector'],
                    'total_volume': uc['total_volume'],
                    'clean_keywords_count': uc['clean_keywords_count'],
                    'pillar_keyword': uc['pillar_keyword']['keyword'],
                    'pillar_volume': uc['pillar_keyword']['cluster_volume'],
                    'pillar_intent': uc['pillar_keyword']['intent'],
                    'quick_wins_count': len([k for k in uc['top_opportunities'] if k['quadrant'] == 'Quick Win']),
                    'chunk_url': f"/data/seo-clusters/{uc['sector']}/{uc['id']}.json"
                } for uc in all_usecases
            ]
        }
        index_file = os.path.join(modular_dir, "index.json")
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index_payload, f, ensure_ascii=False, indent=2)
        print(f"Đã tạo Modular Index siêu nhẹ tại: {index_file} ({round(os.path.getsize(index_file)/1024, 1)} KB)")

        # Xuất file Quick Wins độc lập
        qw_file = os.path.join(modular_dir, "quick-wins.json")
        with open(qw_file, 'w', encoding='utf-8') as f:
            json.dump({'quick_wins': all_quick_wins[:100]}, f, ensure_ascii=False, indent=2)
        print(f"Đã tạo Quick Wins JSON tại: {qw_file}")

        # Xuất từng Chunk Use Case độc lập
        chunk_count = 0
        for uc in all_usecases:
            sec_dir = os.path.join(modular_dir, uc['sector'])
            os.makedirs(sec_dir, exist_ok=True)
            uc_file = os.path.join(sec_dir, f"{uc['id']}.json")
            with open(uc_file, 'w', encoding='utf-8') as f:
                json.dump(uc, f, ensure_ascii=False, indent=2)
            chunk_count += 1
        print(f"Đã phân rã và xuất bản thành công {chunk_count} Modular Chunks tại {modular_dir}/<sector>/<id>.json!")
    else:
        print(f"Cảnh báo: Không tìm thấy hubs-momo tại {HUBS_REPO}")

if __name__ == '__main__':
    main()
