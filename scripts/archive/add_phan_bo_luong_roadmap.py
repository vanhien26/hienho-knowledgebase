import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')

header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(name='Arial', size=10, bold=True, color='FFFFFF')
section_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
section_font = Font(name='Arial', size=10.5, bold=True, color='1F4E78')
thin_side = Side(style='thin', color='64748B')
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

p1_fill = PatternFill(start_color="E2F0D9", end_color="E2F0D9", fill_type="solid") # Green
p2_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid") # Light Blue

status_done_fill = PatternFill(start_color="1E7E34", end_color="1E7E34", fill_type="solid")
status_done_font = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')
status_prog_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")
status_prog_font = Font(name='Arial', size=9.5, bold=True, color='B9770E')
status_plan_fill = PatternFill(start_color="1B4F72", end_color="1B4F72", fill_type="solid")
status_plan_font = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')

font_bold = Font(name='Arial', size=9.5, bold=True)
font_regular = Font(name='Arial', size=9.5)

# 10 complete rows including "Phân Bổ Lương"
complete_roadmap = [
    # 0: Phase, 1: Timeline, 2: Track, 3: Product Name, 4: Tech & UX Scope, 5: W2A Hook, 6: Status
    ("Phase 1", "Tháng 8/2026", "Master Gateway", "Financial Hub",
     "• Xây dựng Cổng Khám Phá & Ra Quyết Định Tài Chính Toàn Diện (Master Gateway) quy hoạch theo 5 nhóm nhu cầu JTBD (Tín Dụng, Tiết Kiệm, Đầu Tư, Ngân Hàng, Thu Nhập/Thuế).\n• Thiết kế Mega Navigation Bar & Thanh Trợ Thủ Đồng Hành cố định (Floating Dock).\n• Module Dashboard thị trường tổng hợp (Cập nhật biến động Vàng, Tỷ giá, Lãi suất cao nhất trong ngày).\n• Cấu hình 301 Redirect toàn diện từ /trung-tam-tai-chinh sang /tai-chinh.",
     "Universal Dynamic OneLink dẫn thẳng vào Financial Hub in-app nhận gói quà tân thủ 500k.",
     "Done"),

    ("Phase 1", "Tháng 8/2026", "Sức Khỏe Tín Dụng & Tiết Kiệm", "CIC & Tiết Kiệm",
     "• Widget CIC Simulator: Cho phép người dùng tự đánh giá nhóm nợ tín dụng 1-5, cẩm nang điều kiện xóa nợ xấu và phục hồi điểm tín dụng.\n• Hero Widget Tính Lãi Tiết Kiệm TKO: Tính lãi đơn gửi 1 lần vs lãi kép gửi định kỳ hàng tháng (1-24 tháng), thanh kéo trượt linh hoạt từ 1 triệu đến 500 triệu đồng.\n• Bảng so sánh quyền lợi & kỳ hạn gửi tiết kiệm online Bản Việt (BVBank) và VPBank.",
     "• CIC: Nút 'Kiểm Tra Điểm Tín Dụng MoMo Miễn Phí 100%' mở báo cáo tín dụng in-app.\n• Tiết Kiệm: Nút 'Mở Sổ Tiết Kiệm Bản Việt / VPBank' kích hoạt mở sổ online ngay.",
     "Done"),

    ("Phase 1", "Tháng 8/2026", "Content & AI Pipeline", "Blog & Cẩm Nang Tài Chính",
     "• Thiết lập quy trình tự động hóa xuất bản cẩm nang tài chính bằng GenAI Pipeline độc lập trên CMS MoSpark.\n• Chuẩn hóa cấu trúc nội dung tuân thủ nghiêm ngặt tiêu chuẩn E-E-A-T và YMYL đối với thông tin tài chính cá nhân (Author Schema, FinancialProduct Markup).\n• Cơ chế nhúng tự động các Embeddable Calculator Widgets vào nội dung bài viết theo ngữ cảnh.",
     "Dynamic Inline Banners & Sticky Floating CTA mở tính năng tài chính tương ứng trên App.",
     "In Progress"),

    ("Phase 1", "Tháng 8/2026", "Đầu Tư & Vàng", "Giá Vàng",
     "• Bảng giá vàng realtime đa thương hiệu: SJC, PNJ, DOJI, Mi Hồng, Bảo Tín Minh Châu, Vàng 24K, 9999, Vàng Nhẫn trơn.\n• Biểu đồ lịch sử biến động giá tương tác (Interactive Charts 7 ngày, 30 ngày, 3 tháng, 1 năm).\n• Công cụ tự động tính chênh lệch Mua - Bán và ước tính lợi nhuận đầu tư theo số lượng vàng.",
     "Nút CTA 'Mua Vàng Tài Lộc Online' & 'Mở Hũ Tích Lũy Vàng MoMo' giải ngân tức thì.",
     "Done"),

    ("Phase 1", "Tháng 9/2026", "Thu Nhập & Thuế", "Tính Lương & Thuế TNCN",
     "• Công cụ tính lương Gross - Net cập nhật Luật Bảo hiểm xã hội mới, mức đóng BHXH/BHYT/BHTN và giảm trừ gia cảnh 11tr/4.4tr.\n• Công cụ dự toán quyết toán & hoàn thuế TNCN tự động theo biểu lũy tiến từng phần 7 bậc.\n• Cổng tra cứu thông tin Mã Số Thuế cá nhân/doanh nghiệp và tình trạng người nộp thuế.",
     "CTA 'Nhận Lương Ứng MoMo' & 'Mở Túi Thần Tài' nhận tiền lời trên lương nhàn rỗi mỗi ngày.",
     "In Progress"),

    ("Phase 1", "Tháng 9/2026", "Thu Nhập & Quản Lý Chi Tiêu", "Phân Bổ Lương",
     "• Công cụ phân bổ thu nhập tự động sau khi tính lương Net theo mô hình 50/30/20 (50% Thiết yếu, 30% Linh hoạt, 20% Tích lũy) và mô hình 6 Chiếc Hũ Tài Chính (JARS).\n• Gợi ý số tiền tích lũy và dòng tiền nhàn rỗi mỗi tháng dựa trên mức lương thực nhận.\n• Widget phân bổ ngân sách tương tác trực quan (Interactive Budget Pie Chart & Sliders).",
     "CTA 'Mở Hũ Tài Chính MoMo' & 'Thiết Lập Tự Động Trích Tiền Lương Sang Túi Thần Tài' sinh lời 4-6%/năm.",
     "In Progress"),

    ("Phase 1", "Tháng 9/2026", "Tiền Tệ & Ngoại Hối", "Tỷ Giá & Ngoại Tệ",
     "• Trang Cổng Master Tỷ Giá (/tai-chinh/ty-gia) tích hợp bảng so sánh realtime 30+ ngân hàng.\n• Hệ thống Programmatic Subpages theo từng Cặp Tiền Tệ (/tai-chinh/ty-gia/[pair-slug]) cho 20+ ngoại tệ (USD/VND, JPY/VND, EUR/VND, KRW/VND, CNY/VND...).\n• Biểu đồ biến động lịch sử và bộ chuyển đổi tiền tệ 2 chiều tức thì.",
     "CTA 'Mở Thẻ Quốc Tế Visa/Mastercard MoMo' miễn phí chuyển đổi ngoại tệ chi tiêu quốc tế.",
     "In Progress"),

    ("Phase 1", "Tháng 9/2026", "Đầu Tư & Quỹ Mở F0", "Chứng Khoán & Quỹ Mở",
     "• Cổng cẩm nang tra cứu và hướng dẫn đầu tư chứng khoán cơ bản dành cho người mới bắt đầu (F0).\n• Bộ giả lập Lãi Kép Tích Lũy Định Kỳ SIP: Nhập số tiền gửi định kỳ (từ 10.000đ/ngày) ➔ Mô phỏng tài sản đạt được sau 5 - 20 năm với các quỹ mở Dragon Capital, VinaCapital, SSIAM, DCBF.\n• Cổng tra cứu thông tin niêm yết 957 mã cổ phiếu 3 sàn HOSE/HNX/UPCOM.",
     "CTA 'Mở Tài Khoản Chứng Khoán CVX' & 'Mua Chứng Chỉ Quỹ SIP Chỉ Từ 10.000đ' in-app.",
     "Planned"),

    ("Phase 2", "Tháng 10/2026", "Tiện Ích Tài Chính Cá Nhân", "Công Cụ Tài Chính Cá Nhân",
     "• Công cụ ước tính tiền rút Bảo Hiểm Xã Hội (BHXH) một lần cập nhật Luật BHXH 2026.\n• Công cụ dự toán Thưởng Tết & Lương Tháng 13 (tính chính xác số tiền Net thực nhận sau thuế TNCN lũy tiến vào dịp cuối năm).\n• Công cụ tra cứu & ước tính mức hưởng trợ cấp thất nghiệp (BHTN 2026) theo thời gian đóng bảo hiểm.",
     "Dòng tiền sau rút BHXH / Thưởng Tết ➔ Dẫn mở Túi Thần Tài / Gửi Tiết Kiệm sinh lời 6.5%/năm.",
     "Planned"),

    ("Phase 2", "Tháng 10/2026", "Tích Sản & Hưu Trí", "Đầu Tư & Tích Sản FIRE",
     "• Bộ Giả Lập Tự Do Tài Chính & Nghỉ Hưu Sớm (FIRE Simulator): Áp dụng Quy tắc 4% (25 lần chi tiêu năm) tính số vốn mục tiêu và số tiền cần đầu tư định kỳ hàng tháng.\n• Công cụ 'Có Tiền Đầu Tư Gì?': Khảo sát khẩu vị rủi ro và phân bổ tài sản Lump Sum (An Toàn - Tăng Trưởng - Mạo Hiểm).\n• Bảng so sánh lãi suất tiền gửi tiết kiệm 30+ Ngân hàng thương mại theo kỳ hạn 1-36 tháng với bộ lọc lãi suất cao nhất.",
     "Đăng ký Gói Tích Sản Hưu Trí / Mở Sổ Tiết Kiệm Lãi Suất Cao Nhất trực tiếp trên MoMo.",
     "Planned")
]

if 'Roadmap' in wb.sheetnames:
    del wb['Roadmap']

ws_rd = wb.create_sheet('Roadmap', index=1)
ws_rd.append(["LỘ TRÌNH TRIỂN KHAI TOÀN DIỆN CÁC TÍNH NĂNG FINANCIAL MASTER HUB (2026 - 2027)"])
ws_rd.merge_cells("A1:G1")
ws_rd.cell(row=1, column=1).fill = section_fill
ws_rd.cell(row=1, column=1).font = section_font
ws_rd.row_dimensions[1].height = 24.0

rd_headers = [
    "Giai Đoạn (Phase)",
    "Thời Gian",
    "Cụm Sản Phẩm (Track)",
    "Tên Tính Năng / Sản Phẩm",
    "Chi Tiết Triển Khai Kỹ Thuật & UX Scope",
    "Cơ Chế Chuyển Đổi Web-to-App (W2A Hook)",
    "Trạng Thái"
]
ws_rd.append(rd_headers)
for c_i in range(1, len(rd_headers) + 1):
    c = ws_rd.cell(row=2, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_rd.row_dimensions[2].height = 28.0

for row_item in complete_roadmap:
    ws_rd.append(list(row_item))
    r = ws_rd.max_row
    
    num_lines = row_item[4].count('\n') + 1
    ws_rd.row_dimensions[r].height = max(55.0, num_lines * 18.0)
    
    ws_rd.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_rd.cell(row=r, column=2).alignment = Alignment(horizontal='center', vertical='center')
    ws_rd.cell(row=r, column=3).alignment = Alignment(horizontal='center', vertical='center'); ws_rd.cell(row=r, column=3).font = font_bold
    ws_rd.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center'); ws_rd.cell(row=r, column=4).font = font_bold
    ws_rd.cell(row=r, column=5).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_rd.cell(row=r, column=6).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_rd.cell(row=r, column=7).alignment = Alignment(horizontal='center', vertical='center')

    phase = row_item[0]
    if "Phase 1" in phase: ws_rd.cell(row=r, column=1).fill = p1_fill
    elif "Phase 2" in phase: ws_rd.cell(row=r, column=1).fill = p2_fill

    status_val = row_item[6]
    c_st = ws_rd.cell(row=r, column=7)
    if status_val == "Done": c_st.fill = status_done_fill; c_st.font = status_done_font
    elif status_val == "In Progress": c_st.fill = status_prog_fill; c_st.font = status_prog_font
    elif status_val == "Planned": c_st.fill = status_plan_fill; c_st.font = status_plan_font

    for c_i in range(1, 8): ws_rd.cell(row=r, column=c_i).border = thin_border

col_widths = [14, 16, 28, 28, 75, 48, 16]
for idx, w in enumerate(col_widths, start=1):
    ws_rd.column_dimensions[get_column_letter(idx)].width = w

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully added 'Phân Bổ Lương' as an independent product row in Roadmap sheet!")
