# -*- coding: utf-8 -*-
"""
CONTENT PLAN & SUB-CLUSTER CONFIGURATION (SSOT)
Chứa các quy tắc phân cụm ngữ nghĩa thực tế (Demand-driven Sub-clusters),
Bản đồ tính năng MoMo Web-to-App (CTA Hook cụ thể) và các hàm chuẩn hóa.
"""

import re
import unicodedata

THRESHOLD = 500

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def make_norm_key(text):
    text = text.lower().strip()
    text = remove_accents(text)
    return re.sub(r'[^a-z0-9]', '', text)

def slugify(text):
    text = remove_accents(text.lower().strip())
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text

# Bản đồ ánh xạ tính năng MoMo thực tế kèm Deeplink & Event đo lường chuẩn Umami
FEATURE_MOMO_MAP = {
    # Financial Hub
    'diem-tin-dung': ('Tra cứu Điểm Tín Dụng & Hồ Sơ CIC', 'momo://credit-score', 'web_cic_lookup_btn_click'),
    'no-xau': ('Kiểm tra Nợ Xấu & Điểm Tín Dụng CIC', 'momo://credit-score', 'web_cic_lookup_btn_click'),
    'gui-tiet-kiem': ('Mở Sổ Tiết Kiệm Online / Túi Thần Tài', 'momo://saving-partner', 'web_saving_interest_calculator_btn_click'),
    'lai-suat': ('Gửi Tiết Kiệm Online Lãi Suất Tốt', 'momo://saving-partner', 'web_saving_interest_calculator_btn_click'),
    'tich-luy': ('Tích Lũy Tiền Nhàn Rỗi Túi Thần Tài', 'momo://saving-partner', 'web_saving_interest_calculator_btn_click'),
    'gia-vang': ('Mua Vàng Tích Lũy / Túi Thần Tài', 'momo://gold-accumulation', 'web_gold_price_lookup_btn_click'),
    'ty-gia': ('Trải Nghiệm Nhận Tiền Quốc Tế MoMo', 'momo://international-remittance', 'web_exchange_rate_lookup_btn_click'),
    'doi-tien': ('Trải Nghiệm Nhận Tiền Quốc Tế MoMo', 'momo://international-remittance', 'web_exchange_rate_lookup_btn_click'),
    'kieu-hoi': ('Nhận Kiều Hối Trực Tiếp Vào MoMo', 'momo://international-remittance', 'web_exchange_rate_lookup_btn_click'),
    'chuyen-khoan': ('Chuyển Tiền Miễn Phí 24/7 Đến 50+ Ngân Hàng', 'momo://money-transfer', 'web_money_transfer_btn_click'),
    'thanh-toan-qr': ('Quét Mã QR MoMo Thanh Toán Đa Dịch Vụ', 'momo://qr-payment', 'web_qr_payment_btn_click'),
    'thue': ('Nộp Thuế Điện Tử Trực Tuyến Qua MoMo', 'momo://tax-payment', 'web_tax_payment_btn_click'),
    'thue-tncn': ('Nộp Thuế Thu Nhập Cá Nhân Trực Tuyến', 'momo://tax-payment', 'web_tax_payment_btn_click'),
    'tinh-luong': ('Tính Lương Gross Sang Net & Quản Lý Chi Tiêu', 'momo://financial-management', 'web_gross_net_calculator_btn_click'),
    'vay': ('Đăng Ký Khoản Vay Tiêu Dùng Online', 'momo://consumer-loan', 'web_consumer_loan_btn_click'),
    'vay-tin-chap': ('Vay Tín Chấp Hạn Mức Đến 100 Triệu', 'momo://consumer-loan', 'web_consumer_loan_btn_click'),
    'vay-the-chap': ('Đăng Ký Vay Thế Chấp Ngân Hàng Đối Tác', 'momo://consumer-loan', 'web_consumer_loan_btn_click'),
    'lai-vay': ('Mô Phỏng Khoản Vay & Đăng Ký In-App', 'momo://consumer-loan', 'web_consumer_loan_btn_click'),
    'vi-tra-sau': ('Kích Hoạt Ví Trả Sau Hạn Mức Đến 20 Triệu', 'momo://postpaid-wallet', 'web_postpaid_wallet_btn_click'),
    'mua-truoc-tra-sau': ('Kích Hoạt Ví Trả Sau Mua Sắm 0% Lãi', 'momo://postpaid-wallet', 'web_postpaid_wallet_btn_click'),
    'tra-gop': ('Thanh Toán Mua Hàng Trả Góp Qua MoMo', 'momo://installment-payment', 'web_installment_btn_click'),

    # Lottery Hub
    'vietlott': ('Đặt Vé Số Vietlott Online Qua MoMo', 'momo://lottery', 'web_lottery_btn_click'),
    'xo-so': ('Dò Kết Quả & Đặt Vé Số Trực Tuyến', 'momo://lottery', 'web_lottery_btn_click'),
    've-so': ('Dò Vé Số & Đặt Vé Số Trực Tuyến', 'momo://lottery', 'web_lottery_btn_click'),

    # Vehicle Hub
    'phat-nguoi': ('Nộp Phạt Nguội Giao Thông Toàn Quốc', 'momo://traffic-fine', 'web_traffic_fine_lookup_btn_click'),
    'gia-xang': ('Tìm Cây Xăng Thanh Toán MoMo', 'momo://gas-station', 'web_fuel_price_lookup_btn_click'),
    'gia-dau': ('Tìm Cây Xăng Thanh Toán MoMo', 'momo://gas-station', 'web_fuel_price_lookup_btn_click'),
    'tram-xang': ('Tìm Cây Xăng Thanh Toán MoMo', 'momo://gas-station', 'web_fuel_price_lookup_btn_click'),
    'vetc': ('Nạp Tiền Thu Phí Tự Động VETC Không Dừng', 'momo://etc-topup', 'web_etc_topup_btn_click'),
    'epass': ('Nạp Tiền Thu Phí Tự Động ePass Không Dừng', 'momo://etc-topup', 'web_etc_topup_btn_click'),
    'phi-khong-dung': ('Nạp Tài Khoản Thu Phí ETC Không Dừng', 'momo://etc-topup', 'web_etc_topup_btn_click'),
    'cuu-ho-xe': ('Gọi Cứu Hộ Ô Tô & Xe Máy Khẩn Cấp', 'momo://rescue-garage', 'web_garage_lookup_btn_click'),
    'gara-o-to': ('Tìm Gara Ô Tô Uy Tín Gần Nhất', 'momo://rescue-garage', 'web_garage_lookup_btn_click'),
    'thue-truoc-ba': ('Nộp Lệ Phí Trước Bạ Phương Tiện Online', 'momo://tax-payment', 'web_tax_payment_btn_click'),

    # Insurtech Hub
    'bhyt': ('Gia Hạn Thẻ Bảo Hiểm Y Tế (BHYT) Online', 'momo://bhyt-renew', 'web_bhyt_lookup_btn_click'),
    'bhxh': ('Đóng Tiếp BHXH Tự Nguyện Trực Tuyến', 'momo://bhxh-payment', 'web_bhxh_payment_btn_click'),
    'bao-hiem-xe-may': ('Mua Bảo Hiểm Xe Máy Bắt Buộc Nhận Thẻ Điện Tử', 'momo://motorbike-insurance', 'web_motorbike_insurance_btn_click'),
    'bao-hiem-o-to': ('Mua Bảo Hiểm Ô Tô (TNDS & Vật Chất)', 'momo://car-insurance', 'web_car_insurance_btn_click'),
    'bao-hiem-tai-nan': ('Mua Bảo Hiểm Tai Nạn & Sức Khỏe Toàn Diện', 'momo://accident-insurance', 'web_accident_insurance_btn_click'),
    'bao-hiem-chay-no': ('Mua Bảo Hiểm Cháy Nổ Nhà Tư Nhân Online', 'momo://fire-insurance', 'web_fire_insurance_btn_click'),

    # OTA Hub
    've-may-bay': ('Đặt Vé Máy Bay Giá Rẻ Trên MoMo', 'momo://flight-booking', 'web_flight_booking_btn_click'),
    've-tau': ('Đặt Vé Tàu Hỏa Bắc Nam Trên MoMo', 'momo://train-booking', 'web_train_booking_btn_click'),
    'xe-khach': ('Đặt Vé Xe Khách Liên Tỉnh Trên MoMo', 'momo://bus-booking', 'web_bus_booking_btn_click'),
    've-xe': ('Đặt Vé Xe Khách & Xe Limousine', 'momo://bus-booking', 'web_bus_booking_btn_click'),

    # Cinema Hub
    'dat-phim': ('Đặt Vé Phim & Chọn Ghế Rạp Rẻ Nhất', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),
    'phim': ('Đặt Vé Phim Rạp Chiếu Mới Nhất', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),
    'rap': ('Đặt Vé Cụm Rạp CGV, Lotte, Galaxy', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),
    've-xem-phim': ('Mua Vé Xem Phim Nhận Ưu Đãi MoMo', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),
    'lich-phim': ('Tra Cứu Lịch Phim & Đặt Vé Tức Thì', 'momo://cinema-booking', 'web_cinema_booking_btn_click'),

    # PS Hub
    'nap-game': ('Nạp Thẻ Game Trực Tuyến Chiết Khấu Cao', 'momo://game-topup', 'web_game_card_topup_btn_click'),
    'nap-tiktok': ('Nạp Xu TikTok Trực Tuyến', 'momo://tiktok-topup', 'web_tiktok_topup_btn_click'),

    # Telco Hub
    'data-3g': ('Nạp Gói Data 3G Tốc Độ Cao MoMo', 'momo://data-topup', 'web_data_topup_btn_click'),
    'data-4g': ('Nạp Gói Cước Data 4G Viettel, Vina, Mobi', 'momo://data-topup', 'web_data_topup_btn_click'),
    'data-5g': ('Nạp Gói Cước 5G Siêu Tốc Độ', 'momo://data-topup', 'web_data_topup_btn_click'),
    'nap-data': ('Nạp Dung Lượng Data 3G/4G/5G Trực Tuyến', 'momo://data-topup', 'web_data_topup_btn_click'),
    'sim': ('Mua SIM Chính Chủ & Chọn Gói Cước Data', 'momo://sim-store', 'web_sim_store_btn_click'),

    # Hospital Hub
    'dat-lich-kham-benh': ('Đặt Lịch Khám Bệnh Tại Bệnh Viện Hàng Đầu', 'momo://hospital-booking', 'web_hospital_booking_btn_click'),
    'benh-vien': ('Thanh Toán Viện Phí & Đặt Lịch Khám Bệnh', 'momo://hospital-booking', 'web_hospital_booking_btn_click'),

    # Other Hub
    'ma-giam-gia': ('Săn Voucher Khuyến Mãi & Mã Giảm Giá MoMo', 'momo://voucher-hub', 'web_voucher_claim_btn_click'),
    'tu-vi': ('Xem Tử Vi & Quẻ Đầu Năm Cùng MoMo', 'momo://horoscope', 'web_horoscope_btn_click'),
}

def get_concrete_cta_hook(theme_slug):
    slug = theme_slug.lower()
    if slug in FEATURE_MOMO_MAP:
        name, link, evt = FEATURE_MOMO_MAP[slug]
        return f"{name} -> Deeplink: {link} -> Event: {evt}"
    return None

# Quy tắc gom cụm Sub-clusters theo Demand thực tế
SUB_CLUSTER_RULES = {
    'vietlott': [
        ('Power 6/55', ['power 6 55', 'power 6/55', 'power 655', 'power655', 'xspower', 'power'], 'power-6-55'),
        ('Mega 6/45', ['mega 6 45', 'mega 6/45', 'mega 645', 'mega645', 'xổ số mega', 'mega'], 'mega-6-45'),
        ('Keno', ['keno', 'quay số nhanh'], 'keno'),
        ('Max 3D', ['max 3d', 'max3d', 'max 4d', 'max4d', 'max 3d pro'], 'max-3d'),
        ('Bingo 18', ['bingo', 'bingo18', 'bingo 18'], 'bingo-18'),
        ('Đại lý & Mua vé online', ['mua vé', 'mua ve', 'đại lý', 'dai ly', 'điểm bán', 'sms', 'app', 'online'], 'dai-ly-mua-ve'),
        ('Cơ cấu & Trúng thưởng', ['cơ cấu', 'co cau', 'giải thưởng', 'giai thuong', 'trúng thưởng', 'dò vé', 'do ve'], 'co-cau-trung-thuong'),
    ],
    'xo-so': [
        ('Xổ số Miền Bắc', ['miền bắc', 'mien bac', 'xsmb', 'sxmb', 'kqsxmb', 'bắc'], 'mien-bac'),
        ('Xổ số Miền Nam', ['miền nam', 'mien nam', 'xsmn', 'sxmn', 'kqsxmn', 'nam'], 'mien-nam'),
        ('Xổ số Miền Trung', ['miền trung', 'mien trung', 'xsmt', 'sxmt', 'kqsxmt', 'trung'], 'mien-trung'),
        ('Thống kê & Soi cầu', ['thống kê', 'thong ke', 'soi cầu', 'soi cau', 'lô gan', 'tần suất', 'bạch thủ'], 'thong-ke-soi-cau'),
        ('Quay thử & Trực tiếp', ['quay thử', 'quay thu', 'trực tiếp', 'truc tiep', 'live', 'sxtt'], 'quay-thu-truc-tiep'),
        ('Cơ cấu & Đổi thưởng', ['cơ cấu', 'co cau', 'giải thưởng', 'giai thuong', 'trúng', 'đổi vé', 'lãnh thưởng'], 'co-cau-doi-thuong'),
    ],
    've-so': [
        ('Dò vé số kiến thiết', ['dò', 'tra cứu', 'kiểm tra', 'hôm nay'], 'do-ve-so'),
        ('Đại lý & Điểm đổi vé', ['đại lý', 'đổi vé', 'hoa hồng', 'vé dạo'], 'dai-ly-doi-ve'),
        ('Cơ cấu giải thưởng vé số', ['cơ cấu', 'giải đặc biệt', 'giải phụ', 'vé số cào'], 'co-cau-giai-thuong'),
    ],
    'gia-vang': [
        ('Giá vàng SJC', ['sjc', 'vàng miếng'], 'gia-vang-sjc'),
        ('Vàng nhẫn 9999 & Vàng 24K', ['9999', 'nhẫn trơn', '24k', 'vàng nhẫn', 'vàng tây'], 'vang-nhan-9999'),
        ('Giá vàng DOJI & PNJ', ['doji', 'pnj', 'mi hồng', 'bảo tín'], 'vang-doji-pnj'),
        ('Biểu đồ & Dự báo giá vàng', ['biểu đồ', 'dự báo', 'xu hướng', 'thế giới', 'kitco'], 'bieu-do-du-bao'),
    ],
    'gui-tiet-kiem': [
        ('Lãi suất ngân hàng', ['lãi suất', 'lai suat', 'ngân hàng nào cao nhất', 'cao nhất'], 'lai-suat-ngan-hang'),
        ('Công cụ tính lãi', ['cách tính', 'tính lãi', 'công thức', '100 triệu', '50 triệu', '1 tỷ', 'bao nhiêu tiền'], 'tinh-lai'),
        ('Kỳ hạn & Hình thức gửi', ['kỳ hạn', 'không kỳ hạn', 'có kỳ hạn', 'bậc thang', 'online'], 'ky-han-hinh-thuc'),
        ('Thủ tục mở sổ & Rút tiền', ['thủ tục', 'rút tiền', 'trước hạn', 'sổ tiết kiệm', 'tất toán', 'mở sổ', 'đáo hạn'], 'thu-tuc-mo-so'),
        ('So sánh giải pháp tiết kiệm', ['so sánh', 'nên gửi', 'túi thần tài', 'vàng hay tiết kiệm', 'chứng chỉ tiền gửi'], 'so-sanh-tiet-kiem'),
    ],
    'diem-tin-dung': [
        ('Tra cứu CIC & Kiểm tra nợ xấu', ['tra cứu cic', 'kiểm tra cic', 'nợ xấu', 'nhóm nợ', 'check cic'], 'tra-cuu-cic'),
        ('Xóa nợ xấu & Cải thiện điểm', ['xóa nợ', 'cải thiện', 'điểm tín dụng', 'bao lâu'], 'xoa-no-xau'),
        ('Thủ tục & Biểu phí CIC', ['thủ tục', 'phí tra cứu', 'hồ sơ', 'mẫu đơn'], 'thu-tuc-bieu-phi'),
        ('Vay vốn theo điểm tín dụng', ['vay', 'ngân hàng', 'hạn mức', 'duyet vay'], 'vay-theo-diem-tin-dung'),
    ],
    'bmi': [
        ('Công cụ tính chỉ số BMI', ['tính bmi', 'tinh bmi', 'cách tính', 'máy tính', 'calculator', 'online', 'công thức', 'phần mềm'], 'cong-cu-tinh-bmi'),
        ('Bảng BMI chuẩn Nam & Nữ', ['nam', 'nữ', 'người lớn', 'chuẩn', 'bảng', 'châu á', 'who', 'tiêu chuẩn'], 'bang-bmi-nam-nu'),
        ('Chỉ số BMI trẻ em', ['trẻ em', 'tuổi', 'bé', 'học sinh', 'mầm non'], 'bmi-tre-em'),
        ('Đánh giá thể trạng & Thừa cân', ['béo phì', 'gầy', 'thừa cân', 'suy dinh dưỡng', 'giảm cân', 'tăng cân'], 'the-trang-suc-khoe'),
    ],
    'lich-am': [
        ('Lịch Vạn Niên & Ngày Hoàng Đạo', ['vạn niên', 'van nien', 'ngày tốt', 'ngày hoàng đạo', 'giờ hoàng đạo', 'ngày xấu', 'hắc đạo', 'xuất hành', 'vạn sự'], 'lich-van-nien'),
        ('Đổi Ngày Âm Dương & Hôm Nay', ['đổi ngày', 'doi ngay', 'âm sang dương', 'dương sang âm', 'hôm nay', 'tra cứu', 'lịch âm dương', 'âm lịch hôm nay'], 'doi-ngay-am-duong'),
        ('Lịch Tết & Ngày Lễ Âm Lịch', ['tết', 'tet', 'nguyên đán', 'rằm', 'mùng 1', 'tháng giêng', 'ông công ông táo', 'vu lan', 'trung thu'], 'lich-tet-ngay-le'),
        ('Lịch Âm Các Năm', ['2025', '2026', '2027', 'năm nay', 'năm sau'], 'lich-am-cac-nam'),
    ],
    'ma-giam-gia': [
        ('Mã Giảm Giá Sàn TMĐT & Freeship', ['shopee', 'lazada', 'tiktok', 'tiki', 'freeship', 'chợ', '0đ', 'mã freeship', 'voucher shopee'], 'ma-giam-gia-tmdt'),
        ('Voucher Ăn Uống & Cafe', ['highland', 'highlands', 'phúc long', 'phuc long', 'cgv', 'haidilao', 'jollibee', 'kfc', 'lotteria', 'ăn uống', 'cafe', 'voucher highland'], 'voucher-an-uong-cafe'),
        ('Voucher Du Lịch & Di Chuyển', ['klook', 'traveloka', 'grab', 'grabfood', 'be', 'agoda', 'booking', 'vé máy bay', 'voucher klook'], 'voucher-du-lich-dich-vu'),
        ('Mã Giảm Giá & Voucher MoMo', ['momo', 'ví momo', 'thanh toán', 'chiết khấu', 'hoàn tiền', 'voucher momo', 'ưu đãi momo'], 'voucher-momo-uu-dai'),
    ]
}

SECTOR_RULES = {
    'Financial': [
        ('Tỷ giá & Ngoại tệ', ['tỷ giá', 'ty gia', 'đô la', 'usd', 'ngoại tệ', 'ngoai te', 'euro', 'dxy', 'vnd', 'chuyển đổi'], 'ty-gia'),
        ('Lãi suất & Tiền gửi', ['lãi suất', 'lai suat', 'tiết kiệm', 'tiet kiem', 'gửi tiền', 'gui tien', 'kỳ hạn', 'ky han', 'rút tiền'], 'lai-suat'),
        ('Vay vốn & Tín chấp', ['vay', 'vay vốn', 'vay von', 'vay tiền', 'vay tien', 'tín chấp', 'tin chap', 'thế chấp', 'the chap', 'trả góp', 'tra gop', 'hạn mức'], 'vay-von'),
        ('Thẻ & Tài khoản', ['thẻ', 'the atm', 'thẻ tín dụng', 'the tin dung', 'mở thẻ', 'mo the', 'tài khoản', 'tai khoan', 'số tài khoản', 'phát hành thẻ'], 'the-tai-khoan'),
        ('Biểu phí & Thủ tục', ['phí', 'biểu phí', 'bieu phi', 'thủ tục', 'thu tuc', 'hồ sơ', 'ho so', 'điều kiện', 'dieu kien', 'hướng dẫn', 'huong dan', 'cách'], 'bieu-phi-thu-tuc'),
        ('Tra cứu & Chi nhánh', ['tra cứu', 'tra cuu', 'chi nhánh', 'chi nhanh', 'phòng giao dịch', 'tổng đài', 'tong dai', 'hotline', 'địa chỉ', 'dia chi', 'swift'], 'chi-nhanh'),
        ('Giá vàng & Kim loại quý', ['giá vàng', 'gia vang', 'vàng sjc', 'vàng 9999', 'nhẫn trơn', 'vàng miếng', 'vàng tây'], 'gia-vang'),
    ],
    'vehicle-hub': [
        ('Phạt nguội & Luật giao thông', ['phạt nguội', 'phat nguoi', 'lỗi vi phạm', 'mức phạt', 'nghị định', 'trừ điểm', 'bằng lái', 'giấy phép', 'camera'], 'phat-nguoi'),
        ('Bảo dưỡng & Nuôi xe', ['bảo dưỡng', 'bao duong', 'thay nhớt', 'chi phí', 'nuôi xe', 'xăng dầu', 'giá xăng', 'tiêu hao', 'đăng kiểm', 'sang tên'], 'bao-duong-nuoi-xe'),
        ('Gara & Cứu hộ', ['gara', 'garage', 'cứu hộ', 'cuu ho', 'sửa xe', 'sua xe', 'rửa xe', 'rua xe', 'vá lốp', 'kéo xe'], 'gara-cuu-ho'),
        ('Định giá & Mua bán xe', ['giá xe', 'gia xe', 'định giá', 'dinh gia', 'lăn bánh', 'lan banh', 'mua xe', 'bán xe', 'trả góp xe'], 'dinh-gia-xe'),
        ('Thu phí & Cây xăng', ['vetc', 'epass', 'không dừng', 'cây xăng', 'trạm xăng', 'petrolimex'], 'thu-phi-tram-xang'),
    ],
    'insurtech': [
        ('Tra cứu & Hạn sử dụng', ['tra cứu', 'kiểm tra', 'check', 'thời hạn', 'hạn sử dụng', 'mã số', 'thẻ', 'sổ'], 'tra-cuu-han-dung'),
        ('Biểu phí & Mua bảo hiểm', ['phí', 'biểu phí', 'giá', 'bao nhiêu tiền', 'mua', 'đóng', 'nộp', 'tái tục', 'online', 'trực tuyến'], 'bieu-phi-mua-online'),
        ('Quyền lợi & Chế độ', ['quyền lợi', 'khám chữa bệnh', 'bệnh viện', 'thanh toán', 'hưởng', 'chế độ', 'thai sản', 'hưu trí', 'ốm đau'], 'quyen-loi-che-do'),
        ('Quy định & Bồi thường', ['bồi thường', 'boi thuong', 'chi trả', 'mức phạt', 'bắt buộc', 'tnds', 'quy định', 'luật', 'nghị định', 'hồ sơ'], 'boi-thuong-quy-dinh'),
    ],
    'cinema': [
        ('Lịch chiếu & Suất chiếu', ['lịch chiếu', 'lich chieu', 'suất chiếu', 'suat chieu', 'gio chieu', 'chiếu rạp', 'phim chiếu', 'lịch phim'], 'lich-chieu'),
        ('Giá vé & Khuyến mãi', ['giá vé', 'gia ve', 'vé rẻ', 've re', 'khuyến mãi', 'khuyen mai', 'ưu đãi', 'voucher', 'combo', 'giảm giá'], 'gia-ve-khuyen-mai'),
        ('Cụm rạp & Đặt vé', ['rạp', 'cgv', 'lotte', 'bhd', 'galaxy', 'cinestar', 'đặt vé', 'dat ve', 'đặt phim', 'mua vé'], 'rap-dat-ve'),
        ('Review & Đánh giá phim', ['review', 'đánh giá', 'danh gia', 'nội dung', 'diễn viên', 'trailer', 'phim hay', 'top phim'], 'review-danh-gia'),
    ],
    'PS': [
        ('Nạp thẻ & Chiết khấu', ['nạp', 'nap', 'thẻ', 'the', 'chiết khấu', 'chiet khau', 'garena', 'zing', 'vcoin', 'xu', 'tiktok', 'mua thẻ'], 'nap-the-chiet-khau'),
        ('Tựa game & Sự kiện', ['game', 'liên quân', 'free fire', 'pubg', 'tốc chiến', 'sự kiện', 'giftcode', 'code'], 'tua-game-su-kien'),
        ('Tài khoản & Hướng dẫn', ['tài khoản', 'tai khoan', 'đăng ký', 'nhà phát hành', 'nph', 'vng', 'garena', 'vtc'], 'tai-khoan-huong-dan'),
    ],
    'ota': [
        ('Vé máy bay & Di chuyển', ['vé máy bay', 've may bay', 'chuyến bay', 'vé tàu', 'vé xe', 'xe khách', 'cáp treo'], 've-di-chuyen'),
        ('Đặt phòng & Resort', ['khách sạn', 'khach san', 'resort', 'homestay', 'đặt phòng', 'dat phong', 'villa'], 'dat-phong-resort'),
        ('Tour & Điểm đến', ['tour', 'du lịch', 'du lich', 'hành trình', 'lịch trình', 'visa', 'điểm đến'], 'tour-diem-den'),
    ],
    'telco': [
        ('Gói cước & Data 4G/5G', ['data', '4g', '5g', '3g', 'gói cước', 'goi cuoc', 'nạp data', 'dung lượng'], 'goi-cuoc-data'),
        ('SIM & Tài khoản', ['sim', 'sim số', 'chính chủ', 'esim', 'tài khoản điện thoại', 'nạp thẻ'], 'sim-tai-khoan'),
    ],
    'hospital': [
        ('Đặt khám & Bác sĩ', ['đặt khám', 'dat kham', 'bác sĩ', 'bac si', 'bệnh viện', 'benh vien', 'phòng khám', 'chuyên khoa'], 'dat-kham-bac-si'),
        ('Chỉ số & Sức khỏe', ['bmi', 'calo', 'cân nặng', 'chiều cao', 'dinh dưỡng', 'sức khỏe'], 'chi-so-suc-khoe'),
    ],
    'student': [
        ('Tuyển sinh & Xét tuyển', ['tuyển sinh', 'xét tuyển', 'điểm chuẩn', 'thi tốt nghiệp', 'thi thpt', 'nguyện vọng', 'học bạ', 'tổ hợp môn'], 'tuyen-sinh'),
        ('Trường & Ngành học', ['trường', 'đại học', 'cao đẳng', 'trung cấp', 'học viện', 'ngành học', 'chuyên ngành', 'mã trường'], 'truong-nganh-hoc'),
        ('Học phí & Học bổng', ['học phí', 'học bổng', 'miễn giảm', 'lệ phí', 'tín chỉ'], 'hoc-phi-hoc-bong'),
        ('Nhà trọ & Ký túc xá', ['nhà trọ', 'phòng trọ', 'ký túc xá', 'thuê trọ', 'tìm trọ', 'chỗ ở'], 'nha-tro-ktx'),
        ('Sinh viên & Cổng thông tin', ['sinh viên', 'cổng thông tin', 'đăng nhập', 'tài khoản', 'email', 'thẻ sinh viên'], 'sinh-vien-cong-thong-tin'),
        ('Việc làm & Kỹ năng', ['việc làm', 'part-time', 'bán thời gian', 'thực tập', 'tuyển dụng', 'kỹ năng'], 'viec-lam-ky-nang'),
    ]
}

FALLBACK_INTENT_CLUSTERS = [
    ('Công cụ & Tra cứu', 'Tool/Calculator', 'tra-cuu'),
    ('So sánh & Đánh giá', 'Commercial', 'so-sanh'),
    ('Đăng ký & Hướng dẫn thủ tục', 'Transactional', 'thu-tuc'),
    ('Cẩm nang & Hỏi đáp', 'Informational', 'cam-nang'),
    ('Cổng dịch vụ & Liên hệ', 'Navigational', 'lien-he'),
]

VIETLOTT_ENTITIES = [
    'vietlott', 'viet lott', 'việt lott', 'mega 6 45', 'mega 6/45', 'mega645',
    'power 6 55', 'power 6/55', 'power 655', 'power655', 'keno', 'max 3d', 'max3d',
    'max 3d pro', 'bingo18', 'bingo 18', 'vietlott sms', 'mua vietlott', 'vé số vietlott'
]

BANK_THEMES = {
    'Vietcombank': ['vietcombank', 'vcb', 'vietcom bank', 'việt com bank', 'ngoại thương'],
    'Techcombank': ['techcombank', 'techcom bank', 'kỹ thương'],
    'BIDV': ['bidv', 'đầu tư và phát triển'],
    'VietinBank': ['vietinbank', 'vietin bank', 'việt tin', 'công thương'],
    'agribank': ['agribank', 'agri bank', 'nông nghiệp'],
    'mbbank': ['mbbank', 'mb bank', 'quân đội', 'ngân hàng mb'],
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
