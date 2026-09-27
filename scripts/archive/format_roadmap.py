import openpyxl
from openpyxl.styles import Alignment, Border, Side, PatternFill, Font

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-roadmap.xlsx'
wb = openpyxl.load_workbook(file_path)

# Clear existing Roadmap sheet if exists, we rebuild it from scratch
if 'Roadmap' in wb.sheetnames:
    ws = wb['Roadmap']
    ws.merged_cells.ranges.clear()
    ws.delete_rows(1, ws.max_row)
else:
    ws = wb.create_sheet('Roadmap', index=1)

# Define Styles
font_title = Font(bold=True, size=14, color="FFFFFF")
fill_title = PatternFill("solid", fgColor="4C1130") # Dark MoMo Pink

font_header = Font(bold=True, color="000000")
fill_header = PatternFill("solid", fgColor="EFEFEF")

align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_top = Alignment(horizontal="left", vertical="top", wrap_text=True)
border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))

# Row 1: Title (Matches Financial Hub style)
ws.append(['LỘ TRÌNH TRIỂN KHAI TOÀN DIỆN CÁC TÍNH NĂNG VEHICLE HUB (2026 - 2027)'])
ws.merge_cells('A1:G1')
cell = ws['A1']
cell.font = font_title
cell.fill = fill_title
cell.alignment = align_center

# Row 2: Headers
headers = ['Giai Đoạn (Phase)', 'Thời Gian', 'Cụm Sản Phẩm (Track)', 'Tên Tính Năng / Sản Phẩm', 'Chi Tiết Triển Khai Kỹ Thuật & UX Scope', 'Cơ Chế Chuyển Đổi Web-to-App (W2A Hook)', 'Trạng Thái']
ws.append(headers)

for col_num in range(1, 8):
    cell = ws.cell(row=2, column=col_num)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center
    cell.border = border

data = [
    # Phase 1.0
    ['Phase 1.0', 'Tháng 8/2026', 'Master Gateway', 'Trang Chủ Vehicle Hub', '• Xây dựng mặt tiền tổng hợp hệ sinh thái giao thông.\n• Hero Widget tra cứu 3-in-1 (Phạt Nguội, ePass, Giá Xăng).', 'Universal Dynamic OneLink điều hướng mở app MoMo.', 'Done'],
    
    # Phase 1.1
    ['Phase 1.1', 'Tuần 1-2 Tháng 9/2026', 'Magnet & Transaction', 'Cổng Tra Cứu Phạt Nguội', '• Mở rộng trang Phạt nguội theo 63 tỉnh/thành.\n• Trả kết quả Inline 2 nhánh (Có/Không vi phạm).\n(Search Volume: 2.900.000/tháng)', 'Nút CTA \'Nộp Phạt In-App\' và Cross-sell \'Mua Bảo Hiểm Ô Tô\'.', 'In Progress'],
    ['Phase 1.1', 'Tuần 1-2 Tháng 9/2026', 'Location (High Volume)', 'Giá Xăng & Cây Xăng', '• Bảng giá xăng dầu realtime cập nhật định kỳ.\n• Bản đồ định vị GPS cây xăng gần nhất.\n(Search Volume: 11.073.210/tháng)', 'Nút CTA \'Thanh toán MoMo tại trạm\' kèm hiển thị Voucher.', 'In Progress'],
    
    # Phase 1.2
    ['Phase 1.2', 'Tuần 3-4 Tháng 9/2026', 'Location & Maps', 'Bản đồ Trạm sạc, Bãi đỗ & Rửa xe', '• Bản đồ định vị Trạm sạc EV (VinFast/V-Green), Garage/Bảo dưỡng, Bãi đỗ xe.\n(Search Volume: ~1.76M/tháng)', 'CTA Hướng dẫn đường đi Google Maps hoặc gọi điện Hotline.', 'Planned'],
    ['Phase 1.2', 'Tuần 3-4 Tháng 9/2026', 'Content & SEO', 'Blog & Content Production', '• Sản xuất cẩm nang giao thông, tra cứu mức phạt NĐ 100/123, biển báo giao thông.', 'Inline Banner điều hướng sử dụng dịch vụ tài chính/xe trên App.', 'Planned'],
    ['Phase 1.2', 'Tuần 3-4 Tháng 9/2026', 'Utilities', 'Tra Cứu Hạn Đăng Kiểm', '• Tra cứu hạn kiểm định xe và chu kỳ.\n• Đếm ngược ngày hết hạn.', 'Nút W2A đặt lịch hẹn Trung tâm đăng kiểm.', 'Planned'],
    
    # Phase 2
    ['Phase 2', 'Tháng 10/2026', 'Transaction', 'Thu Phí BOT (ePass/VETC)', '• Tra cứu tình trạng thẻ thu phí không dừng.\n(Search Volume: 108.210/tháng)', 'Nút CTA liên kết tài khoản và nạp tiền định kỳ.', 'Planned'],
    ['Phase 2', 'Tháng 10/2026', 'Emergency', 'Cứu Hộ Ô Tô', '• Danh bạ khẩn cấp gọi xe cứu hộ, cẩu xe, vá lốp 24/7.\n(Search Volume: 788.400/tháng)', 'Nút Click-to-call gọi nhanh SOS.', 'Planned'],
    ['Phase 2', 'Tháng 10/2026', 'Monetize', 'Bảo Hiểm Phương Tiện', '• Bảng so sánh hãng bảo hiểm, prefill form thông tin xe tự động.\n(Search Volume: 116.320/tháng)', 'Nút CTA Mua Ngay và Thanh toán 1 chạm trên App.', 'Planned'],
    ['Phase 2', 'Tháng 10/2026', 'Calculator', 'Công cụ Tài chính Xe', '• Máy tính dự toán phí lăn bánh, chi phí nuôi xe, so sánh mẫu xe.\n(Search Volume: 16.140/tháng)', 'Trích xuất Lead (SDT/Biển số) để Cross-sell bảo hiểm xe mới / Vay tiêu dùng.', 'Planned'],
    ['Phase 2', 'Tháng 10/2026', 'Smart City', 'Camera & Lộ trình', '• Xem camera điểm kẹt xe, ghi log nhật ký chuyến đi.', 'Chuyển hướng vào luồng nhật ký lái xe In-App.', 'Planned']
]

# Write data
for row_idx, row_data in enumerate(data, start=3):
    for col_idx, val in enumerate(row_data, start=1):
        cell = ws.cell(row=row_idx, column=col_idx, value=val)
        cell.alignment = align_top if col_idx in [5, 6] else align_center
        cell.border = border
        
        # Color specific columns if needed, but keeping it clean for now
        # Giai đoạn formatting:
        if val == 'Done':
            cell.fill = PatternFill("solid", fgColor="D9EAD3")
            cell.font = Font(color="274E13", bold=True)
        elif val == 'In Progress':
            cell.fill = PatternFill("solid", fgColor="FFF2CC")
            cell.font = Font(color="B45F06", bold=True)
        elif val == 'Planned':
            cell.fill = PatternFill("solid", fgColor="F3F3F3")
            cell.font = Font(color="434343")

# Adjust column widths (Matching Financial Hub style)
col_widths = {'A': 12, 'B': 18, 'C': 22, 'D': 25, 'E': 45, 'F': 40, 'G': 12}
for col, width in col_widths.items():
    ws.column_dimensions[col].width = width
    
wb.save(file_path)
print("Roadmap rebuilt successfully following Financial Hub format and Search Volumes.")
