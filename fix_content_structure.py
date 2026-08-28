import openpyxl
from openpyxl.styles import Alignment, Border, Side, PatternFill, Font

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-roadmap.xlsx'
wb = openpyxl.load_workbook(file_path)

sheet_name = 'Content Structure'
if sheet_name in wb.sheetnames:
    del wb[sheet_name]
ws = wb.create_sheet(sheet_name, index=3)

# Define Styles
font_header = Font(bold=True, color="FFFFFF")
fill_header = PatternFill("solid", fgColor="4C1130") # MoMo color
align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_top = Alignment(horizontal="left", vertical="top", wrap_text=True)
border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))

headers = ['Nhóm Tính Năng', 'Tên Trang (URL)', 'Content Structure (Trình tự Block từ trên xuống)']
ws.append(headers)

for col_num in range(1, 4):
    cell = ws.cell(row=1, column=col_num)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center
    cell.border = border

data = [
    # Master Hub
    ['Master Hub', 'Trang Chủ\n(/tien-ich-giao-thong)', 
     '1. Hero Section: H1 + Component tra cứu\n2. Metric\n3. Giá Xăng + Cây Xăng\n4. Garage\n5. Cross-Sell Bảo Hiểm Ô tô/xe máy\n6. FAQ\n7. Long Content'],
    
    # Phạt nguội
    ['Transaction', 'Cổng Tra Cứu Phạt Nguội\n(/phat-nguoi)', 
     '1. Hero Section: H1 + Search Box nhập biển số\n2. Result Component (Trả kết quả Lỗi / Không lỗi)\n3. Cross-Sell Bảo Hiểm & CTA Nộp phạt In-App\n4. Bảng tra cứu mã lỗi phổ biến (NĐ 100/123)\n5. Cụm liên kết Location Page (Phạt nguội theo Tỉnh/Thành)\n6. FAQ\n7. Long Content'],
    
    # Giá xăng / Cây xăng
    ['Location & Maps', 'Giá Xăng & Cây Xăng\n(/gia-xang, /cay-xang)', 
     '1. Hero Section: H1 + Bảng Giá xăng cập nhật Realtime\n2. Component Bản đồ (Định vị GPS Cây xăng gần nhất)\n3. Metric (Lịch sử biến động giá)\n4. Component Calculator (Tính tiền đầy bình)\n5. Cross-Sell (Bảo hiểm hoặc CTA Mở App)\n6. FAQ\n7. Long Content'],
    
    # Trạm sạc EV
    ['Location & Maps', 'Trạm Sạc Xe Điện EV\n(/tram-sac)', 
     '1. Hero Section: H1 + Search Box khu vực\n2. Component Bản đồ (Định vị Trạm sạc VinFast/V-Green)\n3. Filter Component (Lọc trạm AC/DC)\n4. Cross-Sell Bảo Hiểm Ô tô\n5. FAQ\n6. Long Content'],
    
    # Đăng kiểm
    ['Utilities', 'Tra Cứu Hạn Đăng Kiểm\n(/dang-kiem)', 
     '1. Hero Section: H1 + Component Tra cứu Hạn Đăng kiểm\n2. Kết quả chu kỳ & Countdown ngày hết hạn\n3. Component Đặt lịch kiểm định\n4. Cross-Sell Bảo Hiểm (Bắt buộc mang theo khi kiểm định)\n5. Bảng chu kỳ kiểm định các loại xe\n6. FAQ\n7. Long Content'],
    
    # Thu phí BOT
    ['Transaction', 'Thu Phí Không Dừng\n(/phi-khong-dung)', 
     '1. Hero Section: H1 + Component Tra cứu tài khoản ePass/VETC\n2. CTA Liên kết & Nạp tiền tự động\n3. Bảng cước phí trạm thu phí BOT\n4. Hướng dẫn dán thẻ\n5. FAQ\n6. Long Content'],
    
    # Cứu hộ
    ['Emergency', 'Cứu Hộ Ô Tô\n(/cuu-ho)', 
     '1. Hero Section: H1 + Dropdown chọn Vị trí\n2. Component Bản đồ & Danh sách Garage Cứu hộ 24/7\n3. Hotline Component (SOS Click-to-call)\n4. Bảng giá dịch vụ khẩn cấp tham khảo\n5. FAQ\n6. Long Content'],
    
    # Bảo hiểm
    ['Monetize', 'Bảo Hiểm Phương Tiện\n(/bao-hiem-o-to)', 
     '1. Hero Section: H1 + Bảng so sánh 9 hãng bảo hiểm\n2. Component Nhập thông tin xe (Auto-fill)\n3. Bảng quyền lợi & CTA Mua ngay\n4. Metric (Lượt bồi thường, uy tín)\n5. FAQ\n6. Long Content'],
    
    # Calculator
    ['Calculator', 'Công cụ Chi phí Lăn Bánh\n(/lan-banh)', 
     '1. Hero Section: H1 + Form chọn Hãng/Dòng xe/Tỉnh thành\n2. Component Bảng tính chi phí lăn bánh chi tiết\n3. Cross-Sell (Bảo hiểm xe mới / Vay mua xe)\n4. FAQ\n5. Long Content']
]

for idx, row_data in enumerate(data, start=2):
    for col, val in enumerate(row_data, start=1):
        cell = ws.cell(row=idx, column=col, value=val)
        cell.alignment = align_top if col == 3 else align_center
        cell.border = border

# Adjust column widths
ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 35
ws.column_dimensions['C'].width = 75

wb.save(file_path)
print("Content Structure rewritten exactly as requested.")
