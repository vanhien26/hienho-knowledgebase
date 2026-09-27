import openpyxl
from openpyxl.styles import Alignment, Border, Side, PatternFill, Font
from openpyxl.utils import get_column_letter

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-roadmap.xlsx'
wb = openpyxl.load_workbook(file_path)

# Styles
border_thin = Border(left=Side(style='thin', color='D9D9D9'),
                     right=Side(style='thin', color='D9D9D9'),
                     top=Side(style='thin', color='D9D9D9'),
                     bottom=Side(style='thin', color='D9D9D9'))
border_header = Border(left=Side(style='thin', color='FFFFFF'),
                       right=Side(style='thin', color='FFFFFF'),
                       top=Side(style='thin', color='FFFFFF'),
                       bottom=Side(style='medium', color='1F4E78'))

font_header = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
fill_header = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')

font_subhead = Font(name='Calibri', size=11, bold=True, color='1F4E78')
fill_subhead = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')

font_data = Font(name='Calibri', size=10)
font_data_bold = Font(name='Calibri', size=10, bold=True)
font_url = Font(name='Consolas', size=9, color='1F4E78')

align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
align_left = Alignment(horizontal='left', vertical='top', wrap_text=True)
align_center_top = Alignment(horizontal='center', vertical='top', wrap_text=True)

# ==========================================
# 1. OVERHAUL SHEET: Roadmap
# ==========================================
ws_road = wb['Roadmap']
# Clear all rows from row 3 downwards
ws_road.delete_rows(3, ws_road.max_row)

roadmap_rows = [
    # Phase 1.0
    ("Phase 1.0", "Tháng 8/2026", "Master Gateway", "Trang Chủ Vehicle Hub (/tien-ich-giao-thong)",
     "• Xây dựng mặt tiền tổng hợp hệ sinh thái giao thông.\n"
     "• Hero Widget tra cứu 3-in-1 (Phạt Nguội, ePass, Giá Xăng).\n"
     "• Metric Bar, danh bạ dịch vụ, FAQ Schema và Long Content.",
     "Universal Dynamic OneLink điều hướng mở app MoMo tạo Thẻ Xe Số.", "Done"),

    # Phase 1.1: Phạt Nguội
    ("Phase 1.1", "Tuần 1-2 Tháng 9/2026", "Magnet & Transaction", "Cổng Tra Cứu Phạt Nguội (/phat-nguoi)",
     "• 1 Trang Standalone Master (/phat-nguoi) + 63 Trang con Location Pages theo tỉnh/thành.\n"
     "• Trả kết quả Inline 2 nhánh: Có vi phạm (Nộp phạt ngay) / Không vi phạm (Bảo hiểm).\n"
     "(Search Volume toàn cụm: 2.900.000 search/tháng)",
     "Nút CTA 'Nộp Phạt In-App' và Cross-sell 'Mua Bảo Hiểm Ô Tô'.", "In Progress"),

    # Phase 1.1: Giá Xăng
    ("Phase 1.1", "Tuần 1-2 Tháng 9/2026", "Location & Pricing", "Bảng Giá Xăng Dầu Hôm Nay (/gia-xang)",
     "• 1 TRANG DUY NHẤT (/gia-xang) - TUYỆT ĐỐI KHÔNG TẠO TRANG CON THEO TỈNH/THÀNH (xăng dầu quy định theo Vùng 1 & Vùng 2, tránh phạt Duplicate Content).\n"
     "• Bảng giá realtime 7 loại nhiên liệu (RON 95-V Euro 5, DO 0.001S-V Euro 5...) kèm nút gạt chuyển vùng [Giá Vùng 1] vs [Giá Vùng 2].\n"
     "• Bộ máy tính giá xăng 1-chạm (Đầy bình theo loại xe, Nút tiền tròn 50k/100k/500k ra lít, Dự toán lộ trình Km).\n"
     "(Search Volume: 10.523.210 search/tháng)",
     "Nút CTA 'Thanh toán MoMo tại trạm Petrolimex/PVOil' kèm hiển thị Voucher 20K.", "In Progress"),

    # Phase 1.1: Cây Xăng (Master + 10 Subpages)
    ("Phase 1.1", "Tuần 1-2 Tháng 9/2026", "Location & Maps", "Bản Đồ Cây Xăng (Master + 10 Trang Con)",
     "• 1 Trang Master Hub (/cay-xang): Tập trung 'Cây xăng gần đây' (GPS Realtime) & 'Cây xăng mở cửa 24/24'.\n"
     "• TRIỂN KHAI CHÍNH XÁC 10 TRANG CON CÓ SEARCH VOLUME LỚN NHẤT:\n"
     "  1. /cay-xang/tp-hcm (Cây xăng TP.HCM)\n"
     "  2. /cay-xang/ha-noi (Cây xăng Hà Nội)\n"
     "  3. /cay-xang/da-nang (Cây xăng Đà Nẵng)\n"
     "  4. /cay-xang/binh-duong (Cây xăng Bình Dương)\n"
     "  5. /cay-xang/tp-hcm/quan-1 (Cây xăng Quận 1)\n"
     "  6. /cay-xang/tp-hcm/quan-7 (Cây xăng Quận 7)\n"
     "  7. /cay-xang/tp-hcm/thu-duc (Cây xăng TP. Thủ Đức)\n"
     "  8. /cay-xang/ha-noi/cau-giay (Cây xăng Quận Cầu Giấy)\n"
     "  9. /cay-xang/ha-noi/dong-da (Cây xăng Quận Đống Đa)\n"
     "  10. /cay-xang/quoc-lo-1a (Cây xăng Tuyến Quốc Lộ 1A)\n"
     "• 2 TIÊU CHÍ BẮT BUỘC: Multi-property Filter (24/7, Brand, MoMo QR, Euro 5) + Local SEO Schema.\n"
     "(Search Volume toàn cụm: 550.000 search/tháng)",
     "Nút 'Chỉ đường 1-chạm' Google Maps + Nút 'Thu thập Voucher 20K xăng xe MoMo'.", "In Progress"),

    # Phase 1.2: Trạm Sạc EV (Master + 6 Subpages)
    ("Phase 1.2", "Tuần 3-4 Tháng 9/2026", "Location & EV Maps", "Bản Đồ Trạm Sạc EV (Master + 6 Trang Con)",
     "• 1 Trang Master Hub (/tram-sac): Bản đồ trạm sạc ô tô điện toàn quốc (đã cắt bỏ xe máy điện).\n"
     "• TRIỂN KHAI CHÍNH XÁC 6 TRANG CON TRỌNG ĐIỂM:\n"
     "  1. /tram-sac/vinfast (Chuyên trang VinFast / V-Green - thâu tóm 85% search volume)\n"
     "  2. /tram-sac/cao-toc (Trạm dừng nghỉ sạc nhanh DC trên các tuyến cao tốc huyết mạch)\n"
     "  3. /tram-sac/ha-noi (Trạm sạc ô tô điện Hà Nội)\n"
     "  4. /tram-sac/tp-hcm (Trạm sạc ô tô điện TP.HCM)\n"
     "  5. /tram-sac/da-nang (Trạm sạc ô tô điện Đà Nẵng)\n"
     "  6. /tram-sac/hai-phong (Trạm sạc ô tô điện Hải Phòng - thủ phủ xe điện)\n"
     "• UTILITY DUY NHẤT: Máy Tính Thời Gian & Chi Phí Sạc Pin (EV Estimator) theo dòng xe (VF3 đến VF9) + So sánh tiết kiệm tiền triệu so với xe xăng.\n"
     "(Search Volume toàn cụm: 1.237.970 search/tháng)",
     "CTA 'Mua Bảo Hiểm Thân Vỏ Pin Xe Điện MoMo' + 'Nạp ePass Cao Tốc'.", "Planned"),

    # Phase 1.2: Bãi Đỗ Xe & Rửa Xe
    ("Phase 1.2", "Tuần 3-4 Tháng 9/2026", "Location & Care", "Bản Đồ Bãi Đỗ Xe & Garage / Rửa Xe",
     "• Trang Bãi Đỗ Xe (/bai-do-xe): Tìm bãi gửi ô tô theo giờ/qua đêm.\n"
     "• Trang Garage & Rửa Xe (/bao-duong hoặc /tim-garage): Danh bạ garage bảo dưỡng, chăm sóc xe, cứu hộ ắc quy.\n"
     "(Search Volume: 520.000 search/tháng)",
     "CTA Chỉ đường Google Maps + Gọi điện hotline đặt chỗ.", "Planned"),

    # Phase 1.2: Đăng Kiểm
    ("Phase 1.2", "Tuần 3-4 Tháng 9/2026", "Utilities", "Tra Cứu Hạn Đăng Kiểm (/dang-kiem)",
     "• 1 TRANG DUY NHẤT (/dang-kiem) - KHÔNG TẠO TRANG CON TỈNH/THÀNH (do search volume địa phương = 0, tập trung 100% SEO vào 1 URL).\n"
     "• Tra cứu chu kỳ & ngày hết hạn tự động theo Thông tư 02/2023 & 08/2023 (đếm ngược ngày).\n"
     "• Bảng dự toán tổng phí kiểm định (340k) + phí bảo trì đường bộ (1.560k/năm).\n"
     "• Bản đồ danh bạ 300 trạm kiểm định xe toàn quốc tích hợp bộ lọc dropdown.\n"
     "(Search Volume: 182.000 search/tháng)",
     "Nút CTA BẮT BUỘC: 'Mua Bảo Hiểm TNDS Bắt Buộc Ô Tô 480K' (điều kiện để trạm nhận xe).", "Planned"),

    # Phase 1.2: Blog SEO
    ("Phase 1.2", "Tuần 3-4 Tháng 9/2026", "Content & SEO", "Blog & Content Production (122 Articles)",
     "• Sản xuất cụm 122 bài viết cẩm nang: Tra cứu mức phạt NĐ 100/123, biển báo giao thông, kinh nghiệm đăng kiểm, cẩm nang xe điện.\n"
     "• Thiết lập cấu trúc Internal Link dẫn sâu về các trang Tool/Map.",
     "Inline Banner điều hướng sử dụng dịch vụ tài chính & tiện ích giao thông trên App.", "Planned"),

    # Phase 2: Thu Phí BOT
    ("Phase 2", "Tháng 10/2026", "Transaction", "Thu Phí BOT ePass/VETC (/phi-khong-dung)",
     "• Tra cứu tình trạng thẻ, số dư tài khoản giao thông và biểu phí các trạm BOT toàn quốc.\n"
     "(Search Volume: 108.210 search/tháng)",
     "Nút CTA liên kết tài khoản giao thông & Bật nạp tiền tự động trên MoMo.", "Planned"),

    # Phase 2: Cứu Hộ Ô Tô
    ("Phase 2", "Tháng 10/2026", "Emergency", "Cứu Hộ Giao Thông 24/7 (/cuu-ho)",
     "• Danh bạ khẩn cấp gọi xe cứu hộ, cẩu xe, vá lốp, kích bình ắc quy 24/7 theo định vị GPS.\n"
     "(Search Volume: 788.400 search/tháng)",
     "Nút Click-to-call gọi nhanh SOS cứu hộ một chạm.", "Planned"),

    # Phase 2: Bảo Hiểm Phương Tiện
    ("Phase 2", "Tháng 10/2026", "Monetize", "Bảo Hiểm Ô Tô & Xe Máy (/bao-hiem-o-to, /bao-hiem-xe-may)",
     "• Bảng so sánh phí và quyền lợi của 9 hãng bảo hiểm hàng đầu (Bảo Việt, PVI, MIC...).\n"
     "• Cấp chứng nhận bảo hiểm điện tử tức thì sau 30 giây.\n"
     "(Search Volume: 116.320 search/tháng)",
     "Nút CTA 'Mua ngay nhận ấn chỉ điện tử' và thanh toán 1 chạm trên App.", "Planned"),

    # Phase 2: Calculator Tài Chính Xe
    ("Phase 2", "Tháng 10/2026", "Calculator", "Công Cụ Tài Chính Xe (/lan-banh, /chi-phi-nuoi-xe, /so-sanh-xe)",
     "• Bộ máy tính: Dự toán chi phí lăn bánh ô tô, Chi phí nuôi xe hàng tháng, So sánh thông số xe.\n"
     "(Search Volume: 16.140 search/tháng)",
     "Trích xuất Lead khách hàng để bán chéo gói Vay mua ô tô & Bảo hiểm thân vỏ.", "Planned"),

    # Phase 2: Smart City
    ("Phase 2", "Tháng 10/2026", "Smart City", "Camera Giao Thông & Sổ Chuyến Đi",
     "• Xem camera giao thông thời gian thực tại các nút giao kẹt xe.\n"
     "• Tra cứu phong thủy biển số xe và ghi log nhật ký chuyến đi.",
     "Chuyển hướng mở Mini App Quản Lý Xe trên App MoMo.", "Planned")
]

for idx, r in enumerate(roadmap_rows, start=3):
    ws_road.append(list(r))
    ws_road.row_dimensions[idx].height = 140 if 'Trang Con' in r[3] else 65
    for c in range(1, 8):
        cell = ws_road.cell(idx, c)
        cell.border = border_thin
        cell.font = font_data
        if c in [1, 2, 7]:
            cell.alignment = align_center_top
        elif c == 3 or c == 4:
            cell.alignment = align_center_top
            cell.font = font_data_bold
        else:
            cell.alignment = align_left

ws_road.column_dimensions['A'].width = 14
ws_road.column_dimensions['B'].width = 22
ws_road.column_dimensions['C'].width = 24
ws_road.column_dimensions['D'].width = 34
ws_road.column_dimensions['E'].width = 75
ws_road.column_dimensions['F'].width = 40
ws_road.column_dimensions['G'].width = 14

# ==========================================
# 2. CREATE / UPDATE SHEET: Subpages Directory
# ==========================================
sheet_name_sub = 'Subpages Directory'
if sheet_name_sub in wb.sheetnames:
    del wb[sheet_name_sub]

ws_sub = wb.create_sheet(title=sheet_name_sub)
ws_sub.views.sheetView[0].showGridLines = True

# Title row
ws_sub.merge_cells('A1:H1')
t_cell = ws_sub['A1']
t_cell.value = "DANH BẠ QUY HOẠCH CHI TIẾT CÁC TRANG CON & LOCATION PAGES (SUBPAGES ARCHITECTURE)"
t_cell.font = Font(name='Calibri', size=13, bold=True, color='1F4E78')
t_cell.fill = fill_subhead
t_cell.alignment = Alignment(horizontal='center', vertical='center')
ws_sub.row_dimensions[1].height = 35

# Subtitle row
ws_sub.merge_cells('A2:H2')
st_cell = ws_sub['A2']
st_cell.value = "Quy định ranh giới URL chuẩn hóa: Cây xăng (10 trang con), Trạm sạc EV (6 trang con), Giá xăng (1 trang đơn), Đăng kiểm (1 trang đơn). Tuyệt đối cấm sinh trang con không có volume."
st_cell.font = Font(name='Calibri', size=9, italic=True, color='595959')
st_cell.alignment = Alignment(horizontal='center', vertical='center')
ws_sub.row_dimensions[2].height = 20

# Header
headers_sub = [
    "STT", "Cụm Sản Phẩm", "Phân Cấp / Loại Trang", "Tên Trang Con", 
    "URL Chuẩn Hóa", "Mục Tiêu Từ Khóa & Search Volume", 
    "Tiện Ích & Filter Trọng Tâm", "Phase / Trạng Thái"
]
for col_idx, h in enumerate(headers_sub, start=1):
    c = ws_sub.cell(3, col_idx, value=h)
    c.fill = fill_header
    c.font = font_header
    c.alignment = align_center
    c.border = border_header
ws_sub.row_dimensions[3].height = 28

subpages_data = [
    # CỤM CÂY XĂNG (1 Master + 10 Trang con)
    ("1", "Cây Xăng", "Master Hub", "Bản Đồ Cây Xăng Gần Đây Toàn Quốc", "/tien-ich-giao-thong/cay-xang", 
     "cây xăng gần đây, cây xăng mở cửa 24/24 (550.000 search/tháng)", 
     "GPS định vị trạm gần nhất, Lọc 24/24, Lọc trạm nhận MoMo QR", "Phase 1.1 (In Progress)"),
    ("2", "Cây Xăng", "Tỉnh / Thành", "Cây Xăng TP. Hồ Chí Minh", "/tien-ich-giao-thong/cay-xang/tp-hcm", 
     "cây xăng tphcm, cây xăng gần đây tphcm (Thị trường lớn nhất phía Nam)", 
     "Lọc hệ thống Comeco, Petrolimex, PVOil tại TP.HCM", "Phase 1.1 (In Progress)"),
    ("3", "Cây Xăng", "Tỉnh / Thành", "Cây Xăng Hà Nội", "/tien-ich-giao-thong/cay-xang/ha-noi", 
     "cây xăng hà nội, cây xăng petrolimex hà nội (Thị trường lớn nhất phía Bắc)", 
     "Lọc trạm Petrolimex & MIPEC nội đô mở 24/7", "Phase 1.1 (In Progress)"),
    ("4", "Cây Xăng", "Tỉnh / Thành", "Cây Xăng Đà Nẵng", "/tien-ich-giao-thong/cay-xang/da-nang", 
     "cây xăng đà nẵng, cây xăng gần đây đà nẵng", 
     "Phục vụ khách thuê xe máy du lịch & tài xế dịch vụ", "Phase 1.1 (In Progress)"),
    ("5", "Cây Xăng", "Tỉnh / Thành", "Cây Xăng Bình Dương", "/tien-ich-giao-thong/cay-xang/binh-duong", 
     "cây xăng bình dương, trạm xăng bình dương", 
     "Mạng lưới trạm xăng xe tải & khu công nghiệp", "Phase 1.1 (In Progress)"),
    ("6", "Cây Xăng", "Quận / Huyện", "Cây Xăng Quận 1 (TP.HCM)", "/tien-ich-giao-thong/cay-xang/tp-hcm/quan-1", 
     "cây xăng quận 1, cây xăng gần đây quận 1", 
     "Lọc trạm mở đêm trung tâm Sài Gòn & quét mã MoMo", "Phase 1.1 (In Progress)"),
    ("7", "Cây Xăng", "Quận / Huyện", "Cây Xăng Quận 7 (TP.HCM)", "/tien-ich-giao-thong/cay-xang/tp-hcm/quan-7", 
     "cây xăng quận 7, cây xăng nguyễn thị thập", 
     "Khu đô thị Phú Mỹ Hưng & cửa ngõ Nam Sài Gòn", "Phase 1.1 (In Progress)"),
    ("8", "Cây Xăng", "Quận / Huyện", "Cây Xăng TP. Thủ Đức", "/tien-ich-giao-thong/cay-xang/tp-hcm/thu-duc", 
     "cây xăng thủ đức, cây xăng xa lộ hà nội", 
     "Nút giao ngã tư Thủ Đức & trạm xăng xe liên tỉnh", "Phase 1.1 (In Progress)"),
    ("9", "Cây Xăng", "Quận / Huyện", "Cây Xăng Quận Cầu Giấy (Hà Nội)", "/tien-ich-giao-thong/cay-xang/ha-noi/cau-giay", 
     "cây xăng cầu giấy, cây xăng nguyễn phong sắc", 
     "Tập trung khối văn phòng Duy Tân & sinh viên đại học", "Phase 1.1 (In Progress)"),
    ("10", "Cây Xăng", "Quận / Huyện", "Cây Xăng Quận Đống Đa (Hà Nội)", "/tien-ich-giao-thong/cay-xang/ha-noi/dong-da", 
     "cây xăng đống đa, cây xăng láng hạ", 
     "Mật độ dân cư dày đặc nhất Hà Nội, lọc trạm tránh kẹt xe", "Phase 1.1 (In Progress)"),
    ("11", "Cây Xăng", "Tuyến Đường", "Cây Xăng Tuyến Quốc Lộ 1A", "/tien-ich-giao-thong/cay-xang/quoc-lo-1a", 
     "cây xăng quốc lộ 1a, trạm dừng chân đổ xăng ql1a", 
     "Phục vụ xe khách, xe tải đường dài Bắc - Nam", "Phase 1.1 (In Progress)"),

    # CỤM TRẠM SẠC Ô TÔ ĐIỆN EV (1 Master + 6 Trang con)
    ("12", "Trạm Sạc EV", "Master Hub", "Bản Đồ Trạm Sạc Ô Tô Điện Toàn Quốc", "/tien-ich-giao-thong/tram-sac", 
     "trạm sạc xe điện, trạm sạc ô tô điện (135.000 search/tháng)", 
     "Lọc công suất DC 150-250kW, Utility tính thời gian/tiền sạc", "Phase 1.2 (Planned)"),
    ("13", "Trạm Sạc EV", "Thương Hiệu", "Chuyên Trang Trạm Sạc VinFast & V-Green", "/tien-ich-giao-thong/tram-sac/vinfast", 
     "trạm sạc vinfast, vinfast trạm sạc điện (874.000 search/tháng - 85% thị phần)", 
     "Toàn bộ mạng lưới V-Green phủ khắp Vincom & Vinhomes", "Phase 1.2 (Planned)"),
    ("14", "Trạm Sạc EV", "Tuyến Huyết Mạch", "Trạm Sạc Cao Tốc & Tuyến Liên Tỉnh", "/tien-ich-giao-thong/tram-sac/cao-toc", 
     "trạm sạc cao tốc, trạm sạc xe điện cao tốc", 
     "Trụ sạc siêu nhanh tại trạm dừng nghỉ Pháp Vân, Phan Thiết, Hải Phòng", "Phase 1.2 (Planned)"),
    ("15", "Trạm Sạc EV", "Tỉnh / Thành", "Trạm Sạc Ô Tô Điện Hà Nội", "/tien-ich-giao-thong/tram-sac/ha-noi", 
     "trạm sạc vinfast hà nội, trạm sạc ô tô hà nội", 
     "Mật độ trạm sạc chung cư & TTTM Vincom dày đặc nhất", "Phase 1.2 (Planned)"),
    ("16", "Trạm Sạc EV", "Tỉnh / Thành", "Trạm Sạc Ô Tô Điện TP. Hồ Chí Minh", "/tien-ich-giao-thong/tram-sac/tp-hcm", 
     "trạm sạc vinfast tphcm, trạm sạc xe điện tphcm", 
     "Thị trường ô tô điện lớn nhất miền Nam", "Phase 1.2 (Planned)"),
    ("17", "Trạm Sạc EV", "Tỉnh / Thành", "Trạm Sạc Ô Tô Điện Đà Nẵng", "/tien-ich-giao-thong/tram-sac/da-nang", 
     "trạm sạc vinfast đà nẵng, sạc ô tô điện đà nẵng", 
     "Cửa ngõ du lịch & đội xe taxi điện Xanh SM", "Phase 1.2 (Planned)"),
    ("18", "Trạm Sạc EV", "Tỉnh / Thành", "Trạm Sạc Ô Tô Điện Hải Phòng", "/tien-ich-giao-thong/tram-sac/hai-phong", 
     "trạm sạc vinfast hải phòng", 
     "Thủ phủ nhà máy xe điện VinFast Đình Vũ", "Phase 1.2 (Planned)"),

    # CÁC TRANG DUY NHẤT (SINGLE PAGES - QUY ĐỊNH KHÔNG TẠO TRANG CON)
    ("19", "Giá Xăng", "Trang Độc Lập", "Bảng Giá Xăng Dầu Hôm Nay", "/tien-ich-giao-thong/gia-xang", 
     "giá xăng hôm nay, giá xăng ron 95 (10.523.210 search/tháng)", 
     "Bảng giá 7 loại xăng dầu, Nút gạt [Vùng 1] vs [Vùng 2], Máy tính 1-chạm", "Phase 1.1 (In Progress)"),
    ("20", "Đăng Kiểm", "Trang Độc Lập", "Cổng Tra Cứu Hạn & Chu Kỳ Đăng Kiểm", "/tien-ich-giao-thong/dang-kiem", 
     "đăng kiểm xe ô tô, hạn đăng kiểm, phí đăng kiểm (182.000 search/tháng)", 
     "Tool đếm ngược ngày hết hạn TT 02/2023, Bản đồ 300 trạm, Bán bảo hiểm TNDS", "Phase 1.2 (Planned)"),
    ("21", "Phạt Nguội", "Trang Độc Lập", "Cổng Tra Cứu Phạt Nguội Toàn Quốc", "/phat-nguoi", 
     "tra cứu phạt nguội, phạt nguội ô tô (2.900.000 search/tháng)", 
     "Nhập biển số xe, trả kết quả 2 nhánh, dẫn Onelink nộp phạt In-App", "Phase 1.1 (In Progress)")
]

for row_idx, r in enumerate(subpages_data, start=4):
    ws_sub.append(list(r))
    ws_sub.row_dimensions[row_idx].height = 25
    for col_idx in range(1, 9):
        c = ws_sub.cell(row_idx, col_idx)
        c.border = border_thin
        c.font = font_data
        if col_idx in [1, 3, 8]:
            c.alignment = align_center
        elif col_idx == 2:
            c.alignment = align_center
            c.font = font_data_bold
        elif col_idx == 5:
            c.alignment = align_left
            c.font = font_url
        else:
            c.alignment = align_left

ws_sub.column_dimensions['A'].width = 6
ws_sub.column_dimensions['B'].width = 16
ws_sub.column_dimensions['C'].width = 20
ws_sub.column_dimensions['D'].width = 32
ws_sub.column_dimensions['E'].width = 38
ws_sub.column_dimensions['F'].width = 45
ws_sub.column_dimensions['G'].width = 45
ws_sub.column_dimensions['H'].width = 22

wb.save(file_path)
print("Updated Roadmap sheet and created Subpages Directory sheet successfully!")
