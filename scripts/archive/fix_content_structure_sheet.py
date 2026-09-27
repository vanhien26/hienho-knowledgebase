import openpyxl
from openpyxl.styles import Alignment, Border, Side, PatternFill, Font

file_excel = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-roadmap.xlsx'
wb = openpyxl.load_workbook(file_excel)
ws = wb['Content Structure']

# Rebuild Content Structure clean and comprehensive
border_thin = Border(left=Side(style='thin', color='D9D9D9'),
                     right=Side(style='thin', color='D9D9D9'),
                     top=Side(style='thin', color='D9D9D9'),
                     bottom=Side(style='thin', color='D9D9D9'))
align_left = Alignment(horizontal='left', vertical='top', wrap_text=True)
align_center = Alignment(horizontal='center', vertical='top', wrap_text=True)

# Clear existing rows from 2 downwards
ws.delete_rows(2, ws.max_row)

rows_data = [
    # 1. Trang Chủ
    ('Master Hub', 'Trang Chủ\n(/tien-ich-giao-thong)', 
     "1. Hero Section: H1 + Hero Widget 3-in-1 (Phạt Nguội, ePass, Giá Xăng)\n"
     "2. Metric Bar: Lượt tra cứu, mạng lưới trạm & cam kết dịch vụ\n"
     "3. Component Bảng Giá Xăng & Bản Đồ Cây Xăng Gần Nhất\n"
     "4. Component Tìm Garage Sửa Xe & Cứu Hộ Giao Thông\n"
     "5. Cross-Sell Block: Mua nhanh Bảo hiểm Ô tô / Xe máy bắt buộc\n"
     "6. FAQ: Giải đáp thắc mắc dịch vụ giao thông\n"
     "7. Long Content: Giới thiệu hệ sinh thái Tiện Ích Giao Thông MoMo"),

    # 2. Phạt Nguội
    ('Transaction', 'Cổng Tra Cứu Phạt Nguội\n(/phat-nguoi & 63 Location Pages)',
     "1. Hero Section: H1 + Search Box nhập biển số xe & chọn loại phương tiện (Ô tô / Xe máy)\n"
     "2. Result Component (2 Nhánh kết quả):\n"
     "   - Nhánh Có vi phạm: Chi tiết lỗi, hình ảnh camera, nút CTA 'Nộp Phạt In-App'\n"
     "   - Nhánh Không vi phạm: Huy hiệu An toàn, nút Cross-sell Bảo hiểm & Lưu biển số\n"
     "3. Programmatic Location Grid: Danh sách liên kết 63 trang Phạt Nguội Tỉnh/Thành\n"
     "4. Metric: Số vụ vi phạm đã tra cứu & cảnh báo lỗi phổ biến theo Nghị định 100/123\n"
     "5. FAQ & Long Content: Quy trình xử lý phạt nguội, thời hạn nộp phạt"),

    # 3. Giá Xăng
    ('Location & Pricing', 'Bảng Giá Xăng Dầu Hôm Nay\n(/gia-xang)',
     "1. Hero Section: H1 + Bảng Giá Xăng Dầu Realtime 7 loại nhiên liệu (Vùng 1 & Vùng 2)\n"
     "2. Metric: Biểu đồ đường tương tác lịch sử biến động giá (Interactive Line Chart 1T, 3T, 1N)\n"
     "3. Utility Component: Bộ Máy Tính Giá Xăng 1-Chạm (3 Chế độ: Đầy bình theo xe, Tiền tròn, Dự toán lộ trình Km)\n"
     "4. Component Bản Đồ Mini: Định vị trạm xăng Petrolimex/PVOil gần nhất\n"
     "5. Cross-Sell / W2A: Thu thập Voucher 20K đổ xăng MoMo\n"
     "6. FAQ & Long Content: Lịch điều hành giá xăng thứ Năm, cơ chế quỹ bình ổn"),

    # 4. Cây Xăng
    ('Location & Maps', 'Bản Đồ Cây Xăng Gần Đây\n(/cay-xang & 10 trang con)',
     "1. Hero Section: H1 ('Cây Xăng Gần Đây Mở Cửa 24/24') + Nút GPS 'Tìm Cây Xăng Gần Tôi Nhất'\n"
     "2. Multi-Property Filter Bar: Lọc Tỉnh/Quận/Tuyến đường | Brand (Petrolimex, PVOil) | Mở 24/24 | Quét MoMo | Xăng Euro 5\n"
     "3. Dual-View Component: Bản đồ GPS tương tác (Pin có logo trạm) + Bottom Sheet danh sách trạm xếp theo khoảng cách mét/km\n"
     "4. 1-Tap Utilities: Nút 'Chỉ đường' mở Google/Apple Maps + Mini Quick Converter (Đổi 50k/100k/500k ra số lít tại trụ bơm)\n"
     "5. Programmatic Cluster: Cụm 10 trang con có Vol to (TP.HCM, Hà Nội, Đà Nẵng, Bình Dương, Q.1, Q.7, Thủ Đức, Cầu Giấy, Đống Đa, QL1A)\n"
     "6. Voucher & Loyalty Hook: Banner nhận voucher 20k đổ xăng MoMo\n"
     "7. FAQ & Long Content SEO Local: Danh bạ cây xăng uy tín theo khu vực, Schema LocalBusiness"),

    # 5. Trạm Sạc EV
    ('Location & Maps', 'Bản Đồ Trạm Sạc Ô Tô Điện EV\n(/tram-sac & 7 trang con)',
     "1. Hero Section: H1 + Quick GPS Bar tìm trạm sạc ô tô điện gần nhất\n"
     "2. EV Matrix Filter Bar: Mạng lưới (VinFast V-Green / Bên thứ 3) | Công suất trụ (Siêu nhanh DC 150-250kW, Nhanh DC 60kW, AC 11kW) | Vị trí (Vincom, Trạm dừng cao tốc, Cây xăng)\n"
     "3. Dual-View Component: Bản đồ trụ sạc pin có hiển thị công suất + Danh sách trạm kèm loại cổng sạc (CCS2, Type 2)\n"
     "4. Core Utility: Máy Tính Thời Gian & Chi Phí Sạc Pin (EV Estimator) theo dòng xe (VF3 đến VF9) + So sánh tiết kiệm tiền triệu so với xe xăng\n"
     "5. Programmatic Cluster: Chuyên trang VinFast (/tram-sac/vinfast) + Tuyến Cao tốc + Hà Nội, TP.HCM, Đà Nẵng, Hải Phòng\n"
     "6. Cross-Sell / W2A: Mua Bảo hiểm Thân vỏ pin ô tô điện & Nạp tiền tài khoản ePass đi cao tốc\n"
     "7. FAQ & Long Content: Cẩm nang sạc xe điện, kinh nghiệm bảo vệ pin chống chai"),

    # 6. Đăng Kiểm
    ('Utilities', 'Tra Cứu Hạn Đăng Kiểm\n(/dang-kiem)',
     "1. Hero Section: H1 + Component Tra cứu Chu kỳ & Hạn Đăng kiểm theo loại xe và năm sản xuất\n"
     "2. Result Component: Đồng hồ đếm ngược ngày hết hạn + Cảnh báo mức phạt quá hạn\n"
     "3. Component Bản Đồ: Danh sách & tọa độ Trung tâm Đăng kiểm xe cơ giới toàn quốc\n"
     "4. Cross-Sell / W2A: Nút 'Đặt lịch hẹn đăng kiểm' & 'Tái tục Bảo hiểm TNDS bắt buộc'\n"
     "5. FAQ & Long Content: Biểu phí kiểm định, danh mục hồ sơ giấy tờ cần chuẩn bị"),

    # 7. Thu Phí Không Dừng
    ('Transaction', 'Thu Phí Không Dừng BOT\n(/phi-khong-dung)',
     "1. Hero Section: H1 + Component Tra cứu số dư tài khoản ePass / VETC qua biển số xe\n"
     "2. CTA Chuyển Đổi: Nút Onelink 'Liên kết tài khoản giao thông & Bật nạp tiền tự động trên MoMo'\n"
     "3. Component Bảng Phí: Danh sách trạm thu phí BOT toàn quốc và mức cước từng loại xe\n"
     "4. Metric: Số lượt qua trạm không dừng thành công & ưu đãi giảm phí\n"
     "5. FAQ & Long Content: Hướng dẫn dán thẻ, cách xử lý khi thẻ không nhận diện"),

    # 8. Cứu Hộ Ô Tô
    ('Emergency', 'Cứu Hộ Giao Thông 24/7\n(/cuu-ho)',
     "1. Hero Section: H1 + Nút gọi khẩn cấp SOS một chạm theo tọa độ GPS\n"
     "2. Component Bản Đồ & Danh Bạ: Đội xe cứu hộ gần nhất (Cẩu kéo xe, vá lốp lưu động, kích bình ắc quy)\n"
     "3. Bảng Giá Dịch Vụ: Bảng giá cẩu kéo niêm yết minh bạch theo km\n"
     "4. Cross-Sell: Giới thiệu quyền lợi Cứu hộ miễn phí khi mua Bảo hiểm Thân vỏ MoMo\n"
     "5. FAQ & Long Content: Kỹ năng xử lý khi xe gặp sự cố trên cao tốc, cách đặt biển cảnh báo"),

    # 9. Bảo Hiểm Xe
    ('Monetize', 'Bảo Hiểm Ô Tô & Xe Máy\n(/bao-hiem-o-to, /bao-hiem-xe-may)',
     "1. Hero Section: H1 + Form báo giá nhanh theo đời xe / dòng xe\n"
     "2. Comparison Component: Bảng so sánh quyền lợi và mức phí của 9 hãng bảo hiểm hàng đầu (Bảo Việt, PVI, MIC, PTI...)\n"
     "3. Special Clause Badges: Cam kết đền bù thủy kích, bồi thường pin xe điện, gara tự chọn\n"
     "4. CTA 1-Chạm W2A: 'Mua ngay nhận ấn chỉ điện tử trong 30 giây'\n"
     "5. FAQ & Long Content: Quy trình bồi thường bảo hiểm, thủ tục giám định tai nạn"),

    # 10. Chi Phí Lăn Bánh
    ('Calculator', 'Công cụ Dự Toán Chi Phí Lăn Bánh\n(/lan-banh)',
     "1. Hero Section: H1 + Form chọn Hãng xe / Mẫu xe / Tỉnh thành đăng ký biển số\n"
     "2. Calculator Result: Bóc tách chi tiết: Thuế trước bạ, Phí ra biển, Phí đường bộ, Bảo hiểm TNDS, Phí đăng kiểm\n"
     "3. Lead Capture Hook: Trích xuất Lead chuyển tiếp tư vấn gói Vay mua ô tô & Bảo hiểm thân vỏ xe mới\n"
     "4. FAQ & Long Content: Hướng dẫn thủ tục tự đi đăng ký xe mới tiết kiệm chi phí dịch vụ")
]

for idx, r_data in enumerate(rows_data, start=2):
    ws.append([r_data[0], r_data[1], r_data[2]])
    ws.row_dimensions[idx].height = 110
    c1 = ws.cell(idx, 1)
    c2 = ws.cell(idx, 2)
    c3 = ws.cell(idx, 3)
    
    c1.border = border_thin
    c1.alignment = align_center
    c1.font = Font(name='Calibri', size=11, bold=True)
    
    c2.border = border_thin
    c2.alignment = align_center
    c2.font = Font(name='Calibri', size=11, bold=True, color='1F4E78')
    
    c3.border = border_thin
    c3.alignment = align_left
    c3.font = Font(name='Calibri', size=10)

ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 30
ws.column_dimensions['C'].width = 95

wb.save(file_excel)
print("Content Structure sheet synchronized perfectly!")
