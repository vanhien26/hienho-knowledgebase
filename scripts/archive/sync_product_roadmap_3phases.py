import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Load financial-hub-roadmap.xlsx
wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')

header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(name='Arial', size=10, bold=True, color='FFFFFF')
section_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
section_font = Font(name='Arial', size=10.5, bold=True, color='1F4E78')
thin_side = Side(style='thin', color='64748B')
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

p1_fill = PatternFill(start_color="E2F0D9", end_color="E2F0D9", fill_type="solid") # Green
p2_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid") # Yellow
p3_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid") # Orange
font_bold_blue = Font(name='Arial', size=9.5, bold=True, color='002060')

# Standardized 3-Phase Roadmap Items (Aligned with 5 Pillars, Quick Wins P0 in Phase 1, SEO root URLs)
roadmap_data = [
    # Phase, Time, Proj_Name, Route, Target_Vol, Spec_Desc, Deliverable_Status, Priority, Strategic_Cluster
    ("Phase 1", "Tháng 8 - 9/2026", "Dự Án 1: Master Gateway & Mega Navigation", "momo.vn/tai-chinh", "1,000,000+ PV/tháng",
     "Xây dựng Trang Cổng Trung Tâm, bảng Dashboard thị trường tổng hợp, thanh điều hướng tài chính thống nhất (Global Nav) và danh mục 5 nhóm nhu cầu JTBD.",
     "Production Ready", "P0", "Master Gateway"),

    ("Phase 1", "Tháng 8 - 9/2026", "Dự Án 2: Hero Widget Tính Lãi Tiết Kiệm Live", "momo.vn/tai-chinh & /tiet-kiem-online", "230,110 search/tháng",
     "Tích hợp Widget tính lãi đơn gửi 1 lần & lãi kép gửi hàng tháng (1-24 tháng), cho phép kéo trượt số tiền linh hoạt và mở sổ online trực tiếp vào Bản Việt/VPBank.",
     "Production Ready", "P0", "Khối Tiết Kiệm"),

    ("Phase 1", "Tháng 8 - 9/2026", "Dự Án 3: Bộ Đôi Công Cụ Thu Nhập & Thuế 2026", "momo.vn/tinh-luong & /thue-tncn", "1,350,140 search/tháng",
     "Phát triển Tool tính lương Gross - Net (áp dụng luật thuế mới 2026), Tool quyết toán thuế TNCN tự động, thanh trượt phân bổ thu chi 50/30/20 và CTA Ứng Lương / Túi Thần Tài.",
     "Ready for Dev", "P0", "Khối Thu Nhập & Thuế"),

    ("Phase 1", "Tháng 8 - 9/2026", "Dự Án 4: Cổng Tra Cứu CIC & Khám Sức Khỏe Tín Dụng", "momo.vn/tra-cuu-cic & /xoa-no-xau", "398,890 search/tháng",
     "Xây dựng Cổng tra cứu thông tin CIC chính thống, Widget tự đánh giá phân loại nhóm nợ 1-5, cẩm nang phục hồi điểm tín dụng và CTA Check Điểm Tín Dụng MoMo miễn phí 100%.",
     "Ready for Dev", "P0", "Khối Tín Dụng & Vay"),

    ("Phase 1", "Tháng 8 - 9/2026", "Dự Án 5: Programmatic Bank Hub (34 Ngân Hàng & Napas)", "momo.vn/ngan-hang/[slug] & /napas", "7,015,550 search/tháng",
     "Triển khai Programmatic template tự động cho 34 ngân hàng đối tác và Cổng chuyển tiền Napas 247. Tích hợp biểu phí, Swift code, hotline và hướng dẫn liên kết nhận quà 500k.",
     "Ready for Dev", "P0", "Khối Ngân Hàng & Thẻ"),

    ("Phase 2", "Tháng 10 - 11/2026", "Dự Án 6: Siêu Động Cơ Tra Cứu Giá Vàng Realtime", "momo.vn/gia-vang", "78,879,270 search/tháng",
     "Xây dựng bảng giá vàng realtime (SJC, PNJ, DOJI, Mi Hồng, 24K, 9999, Nhẫn trơn), biểu đồ biến động lịch sử 7-30 ngày, công cụ tính chênh lệch Mua - Bán và nút Mua Vàng Online.",
     "Planning", "P1", "Khối Đầu Tư & Vàng"),

    ("Phase 2", "Tháng 10 - 11/2026", "Dự Án 7: Bộ Quy Đổi Ngoại Tệ & Tỷ Giá Live", "momo.vn/ty-gia & /ngoai-te", "9,476,250 search/tháng",
     "Bộ công cụ quy đổi tiền tệ tức thì giữa 20+ ngoại tệ (USD, EUR, JPY...) và bảng tỷ giá so sánh chênh lệch giữa các ngân hàng thương mại, dẫn luồng mở thẻ quốc tế.",
     "Planning", "P1", "Khối Tiền Tệ & Tỷ Giá"),

    ("Phase 2", "Tháng 10 - 11/2026", "Dự Án 8: Bảng So Sánh Lãi Suất 30+ Ngân Hàng", "momo.vn/lai-suat-ngan-hang", "1,246,620 search/tháng",
     "Bảng so sánh đa chiều biểu lãi suất tiền gửi tiết kiệm theo kỳ hạn 1-36 tháng của 30+ ngân hàng, tích hợp bộ lọc ngân hàng có lãi suất cao nhất và mở sổ online.",
     "Planning", "P1", "Khối Tiết Kiệm"),

    ("Phase 2", "Tháng 10 - 11/2026", "Dự Án 9: Ma Trận So Sánh Thẻ Tín Dụng & Thẻ Quốc Tế", "momo.vn/the-tin-dung & /the-visa", "656,330 search/tháng",
     "Ma trận so sánh quyền lợi hoàn tiền, phí thường niên của các dòng thẻ tín dụng ngân hàng đối tác và thẻ quốc tế Visa/Mastercard, tích hợp mở thẻ 100% online không chứng minh thu nhập.",
     "Planning", "P1", "Khối Ngân Hàng & Thẻ"),

    ("Phase 2", "Tháng 10 - 11/2026", "Dự Án 10: Máy Tính Trả Góp 0% & Đăng Ký Vay Nhanh", "momo.vn/tra-gop & /vay-tin-chap", "632,170 search/tháng",
     "Máy tính trả góp 0% tổng quát cho mọi mặt hàng công nghệ/điện máy (kích hoạt Ví Trả Sau 20 triệu) và Công cụ tính lãi vay mua nhà/vay tín chấp dư nợ giảm dần.",
     "Planning", "P1", "Khối Tín Dụng & Vay"),

    ("Phase 2", "Tháng 10 - 11/2026", "Dự Án 11: Trung Tâm Đầu Tư Quỹ Mở & Cổ Phiếu F0", "momo.vn/chung-khoan & /chung-chi-quy", "4,183,460 search/tháng",
     "Công cụ 'Có Tiền Đầu Tư Gì?', Bộ giả lập Lãi kép tích lũy định kỳ SIP từ 10.000đ và cẩm nang kiến thức đầu tư chứng khoán cơ bản cho người mới bắt đầu.",
     "Planning", "P1", "Khối Đầu Tư & Tích Sản"),

    ("Phase 3", "Tháng 12/2026 - Q1/2027", "Dự Án 12: AI Financial Pulse & News Stream", "momo.vn/tai-chinh (Module Pulse)", "Tương tác Daily Active",
     "Hệ thống tự động hóa ingest tin tức tài chính, lọc nhiễu AI, tóm tắt 2 gạch đầu dòng và kết hợp alert biến động số liệu thị trường 24/7 (theo mô hình Finpath AI).",
     "Concept", "P2", "Nền Tảng Thông Minh"),

    ("Phase 3", "Tháng 12/2026 - Q1/2027", "Dự Án 13: Đóng Gói Toàn Diện Embeddable Widgets SDK", "Embed Component SDK", "Cross-sell Toàn Sàn",
     "Đóng gói 7 bộ công cụ tiện ích thành React Web Components nhúng linh hoạt vào mọi điểm chạm Web MoMo và hệ thống đối tác ngoài (Affiliate & Partner Web).",
     "Concept", "P2", "Hạ Tầng Dùng Chung"),

    ("Phase 3", "Tháng 12/2026 - Q1/2027", "Dự Án 14: Cá Nhân Hóa Thời Gian Thực & Phễu U18/F0", "Toàn bộ hệ thống Hub", "Nâng CVR W2A +30%",
     "Triển khai Real-time Personalization dựa trên self-declared intent của người dùng trên Web, tối ưu hóa hành trình kích hoạt cho phân khúc Sinh Viên (U18 - U23) và Nhà Đầu Tư F0.",
     "Concept", "P2", "Tối Ưu Chuyển Đổi")
]

# Update Roadmap sheet in financial-hub-roadmap.xlsx
if 'Roadmap' in wb.sheetnames:
    del wb['Roadmap']

ws_rm = wb.create_sheet('Roadmap', index=1)
ws_rm.append(["LỘ TRÌNH TRIỂN KHAI TOÀN DIỆN FINANCIAL MASTER HUB THEO 3 GIAI ĐOẠN (MASTER ROADMAP 2026 - 2027)"])
ws_rm.merge_cells("A1:I1")
ws_rm.cell(row=1, column=1).fill = section_fill
ws_rm.cell(row=1, column=1).font = section_font
ws_rm.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')

headers = [
    "Giai Đoạn (Phase)",
    "Thời Gian",
    "Tên Dự Án / Module Trọng Tâm",
    "URL Route / Sản Phẩm Đầu Ra",
    "Dung Lượng Search / Tác Động",
    "Chi Tiết Triển Khai & Nhiệm Vụ Kỹ Thuật",
    "Trạng Thái",
    "Mức Độ Ưu Tiên",
    "Trụ Cột Nghiệp Vụ"
]
ws_rm.append(headers)
for c_i in range(1, len(headers) + 1):
    c = ws_rm.cell(row=2, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_rm.row_dimensions[2].height = 26.0

for item in roadmap_data:
    ws_rm.append(list(item))
    r = ws_rm.max_row
    ws_rm.row_dimensions[r].height = 24.0
    
    ws_rm.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_rm.cell(row=r, column=2).alignment = Alignment(horizontal='center', vertical='center')
    ws_rm.cell(row=r, column=3).alignment = Alignment(horizontal='left', vertical='center'); ws_rm.cell(row=r, column=3).font = Font(name='Arial', size=9.5, bold=True)
    ws_rm.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center')
    ws_rm.cell(row=r, column=5).alignment = Alignment(horizontal='center', vertical='center'); ws_rm.cell(row=r, column=5).font = font_bold_blue
    ws_rm.cell(row=r, column=6).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_rm.cell(row=r, column=7).alignment = Alignment(horizontal='center', vertical='center')
    ws_rm.cell(row=r, column=8).alignment = Alignment(horizontal='center', vertical='center'); ws_rm.cell(row=r, column=8).font = Font(name='Arial', size=9.5, bold=True)
    ws_rm.cell(row=r, column=9).alignment = Alignment(horizontal='center', vertical='center')
    
    phase = item[0]
    if "Phase 1" in phase: ws_rm.cell(row=r, column=1).fill = p1_fill
    elif "Phase 2" in phase: ws_rm.cell(row=r, column=1).fill = p2_fill
    elif "Phase 3" in phase: ws_rm.cell(row=r, column=1).fill = p3_fill
    
    for c_i in range(1, 10): ws_rm.cell(row=r, column=c_i).border = thin_border

widths = [14, 20, 36, 32, 25, 60, 18, 16, 22]
for idx, w in enumerate(widths, start=1):
    col_letter = get_column_letter(idx)
    ws_rm.column_dimensions[col_letter].width = w

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully synchronized Roadmap sheet in 05_HUBS/financial-hub-roadmap.xlsx!")
