import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-roadmap.xlsx'
wb = openpyxl.load_workbook(file_path)
ws = wb['Roadmap']

# Clear rows from 4 downwards
ws.delete_rows(4, ws.max_row)

# Styles
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))

fill_p1 = PatternFill("solid", fgColor="D9EAD3")
fill_p2 = PatternFill("solid", fgColor="FFF2CC")
fill_block = PatternFill("solid", fgColor="F4CCCC")

data = [
    # PHASE 1 (Tháng 9) - Tất cả High Search Intent + Nền tảng
    ['Phase 1: Go-live Toàn bộ Phễu Search Intent Cao (Hoàn thành trong Tháng 9/2026)', 'Master Hub Gateway', 'Trang Chủ Master Hub (/tien-ich-giao-thong)', '1. Mặt tiền trung tâm với Hero Widget tra cứu 3-in-1.\n2. Gắn điểm chạm Onelink/QR Code điều hướng In-App.', 'Trong Tháng 9'],
    ['None', 'Magnet + Transaction (P1)', 'Cổng Tra Cứu Phạt Nguội (/phat-nguoi)', '1. Trả kết quả Inline 2 nhánh (Có/Không vi phạm).\n2. Block Cross-sell gợi ý nộp phạt In-App & Mua Bảo hiểm.\nVai trò: Phễu thu thập Lead lớn nhất (3.6M search).', 'Trong Tháng 9'],
    ['None', 'Magnet + Transaction (P1)', 'Thu Phí Không Dừng ePass/VETC (/phi-khong-dung, /tram-thu-phi)', '1. Hướng dẫn & luồng liên kết ePass/VETC theo biển số.\n2. Nút W2A nạp ví thu phí không dừng định kỳ.', 'Trong Tháng 9'],
    ['None', 'Conversion & Cross-sell (Intent Cao)', 'Bảo Hiểm Phương Tiện (/bao-hiem-o-to, /bao-hiem-xe-may)', '1. Block cross-sell chuẩn hóa theo loại xe.\n2. Prefill Vehicle Profile (Auto-fill) khi mua BH.\n3. Xây UI Consent lưu biển số theo Nghị định 13.', 'Trong Tháng 9'],
    ['None', 'Calculator (Intent GD Cao)', 'Tính Phí Trước Bạ & Nuôi Xe (/lan-banh, /chi-phi-nuoi-xe, /so-sanh-xe)', '1. Công cụ tính phí trước bạ, giá lăn bánh, so sánh xe.\nVai trò: Intent Mua Bán cao (Điểm GD: 4-5/5) -> Lead mua BH mới.', 'Trong Tháng 9'],
    ['None', 'Khẩn cấp (Intent Cao)', 'Danh Bạ Cứu Hộ Ô tô 24/7 (/cuu-ho)', '1. Danh sách/bản đồ đơn vị cứu hộ theo vị trí.\nVai trò: Xử lý Intent khẩn cấp (Điểm GD: 4/5).', 'Trong Tháng 9'],
    ['None', 'Giữ Chân & Acquisition (Volume)', 'Bảng Giá Xăng & Cây Xăng (/gia-xang, /cay-xang)', '1. Giá xăng update realtime & Bản đồ định vị GPS.\nVai trò: Phễu Acquisition (10M+ search).', 'Trong Tháng 9'],
    ['None', 'Giữ Chân & Acquisition (Volume)', 'Bản Đồ Trạm Sạc EV (/tram-sac, /tram-sac/vinfast)', '1. Bản đồ trạm sạc xe điện theo tỉnh/thành phố, brand.\nVai trò: Đón đầu tệp xe điện.', 'Trong Tháng 9'],

    # PHASE 2 (Tháng 10) - Long tail & Tiện ích giữ chân
    ['Phase 2: Phủ sóng Long-tail SEO & Tiện ích Giữ chân (Tháng 10 - 11/2026)', 'Giữ Chân (Intent Thấp)', 'Bản Đồ Bãi Đỗ Xe (/bai-do-xe)', '1. Bản đồ bãi đỗ xe VETC Parking theo vị trí, giá.\nVai trò: Tiện ích giữ chân (Điểm GD: 3/5).', 'Tháng 10/2026'],
    ['None', 'Legal & Rules (Long-tail SEO)', 'Tra Cứu Luật Giao Thông (/tra-cuu-muc-phat, /bien-bao-giao-thong, /kinh-nghiem-lai-xe)', '1. Từ điển tra cứu mức phạt theo Nghị định 100/123.\n2. Cẩm nang biển báo giao thông & kinh nghiệm lái xe.', 'Tháng 11/2026'],
    ['None', 'Smart City', 'Camera Giao Thông (/camera-giao-thong)', '1. Tích hợp quan sát luồng live stream camera.', 'Tháng 11/2026'],
    ['None', 'Maintenance & Tracking', 'Chăm Sóc & Theo Dõi Hành Trình (/bao-duong, /chuyen-di)', '1. Đặt lịch rửa xe, bảo dưỡng xe.\n2. Nhật ký chuyến đi cá nhân.', 'Tháng 11/2026'],

    # BLOCKED
    ['Blocked / Pending (Vướng Phụ Thuộc)', 'Magnet + Transaction (P1)', 'Tra Cứu Hạn Đăng Kiểm (/dang-kiem)', '1. Tra cứu hạn đăng kiểm & đặt lịch kiểm định.\nTRẠNG THÁI: Blocked. API bảo trì từ phía TTĐK.', 'Blocked']
]

for idx, row_data in enumerate(data, start=4):
    for col, val in enumerate(row_data, start=1):
        cell = ws.cell(row=idx, column=col, value=val if val != 'None' else None)
        cell.alignment = align_left if col in [3, 4] else align_center
        cell.border = border
        
        if idx <= 11:
            cell.fill = fill_p1
        elif idx <= 15:
            cell.fill = fill_p2
        else:
            cell.fill = fill_block

ws.merge_cells('A4:A11')
ws.merge_cells('A12:A15')

wb.save(file_path)
print("Updated intent-based roadmap successfully.")
