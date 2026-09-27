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

font_bold = Font(name='Arial', size=9.5, bold=True)
font_regular = Font(name='Arial', size=9.5)
font_role_key_owner = Font(name='Arial', size=9.5, bold=True, color='B91C1C') # Red bold
font_role_co_owner = Font(name='Arial', size=9.5, bold=True, color='15803D')  # Green bold
font_role_contributor = Font(name='Arial', size=9.5, bold=True, color='1D4ED8') # Blue bold
font_role_consulted = Font(name='Arial', size=9.5, bold=False, color='D97706') # Amber
font_role_informed = Font(name='Arial', size=9.5, bold=False, color='64748B')  # Slate

if 'RACI & Resource Allocation' in wb.sheetnames:
    del wb['RACI & Resource Allocation']

ws_raci = wb.create_sheet('RACI & Resource Allocation', index=4)

ws_raci.append(["MA TRẬN PHÂN ĐỊNH TRÁCH NHIỆM RACI (WEB PLATFORM x FINHUB BU)"])
ws_raci.merge_cells("A1:E1")
ws_raci.cell(row=1, column=1).fill = section_fill
ws_raci.cell(row=1, column=1).font = section_font
ws_raci.row_dimensions[1].height = 24.0

ws_raci.append(["Quy định rõ ràng vai trò Key Owner (A/R), Co-Owner (A/R), Contributor (R), Consulted (C), Informed (I)"])
ws_raci.merge_cells("A2:E2")
ws_raci.cell(row=2, column=1).font = Font(name='Arial', size=9.5, italic=True, color='475569')
ws_raci.row_dimensions[2].height = 18.0

raci_headers = [
    "Hạng Mục / Đầu Việc Triển Khai",
    "Web Platform Team",
    "FinHub BU (CreditTech)",
    "Hạ Tầng / Backend Team",
    "Mô Tả Trách Nhiệm Chi Tiết & Tiêu Chí Nghiệm Thu"
]
ws_raci.append(raci_headers)
for c_i in range(1, len(raci_headers) + 1):
    c = ws_raci.cell(row=3, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_raci.row_dimensions[3].height = 28.0

raci_matrix_data = [
    ("GROUP", "NHÓM I: CHIẾN LƯỢC SẢN PHẨM & QUẢN TRỊ KPI (STRATEGY & GOVERNANCE)", "", "", ""),
    ("ROW", "1.1 Thiết Lập Mục Tiêu KPI Chung (1M MPV, 500K MEU, W2A CVR +25%)",
     "Key Owner (A/R)", "Co-Owner (A/R)", "Informed (I)",
     "Web Platform và FinHub BU cùng cam kết các chỉ số chiến lược: Lượng truy cập Web (1M MPV), Người dùng tương tác tiện ích (500K MEU), Tỷ lệ nhấp Web-to-App (15-25%) và Giao dịch tài chính đầu tiên (+25% MoM)."),
    
    ("ROW", "1.2 Lập Kế Hoạch Sprint 1 Tháng & Nhịp Check-in 2 Tuần/Lần",
     "Key Owner (A/R)", "Co-Owner (A/R)", "Contributor (R)",
     "Tổ chức Sprint Planning đầu tháng để chốt danh mục tính năng/tiện ích tài chính cần build; Check-in ngày 15 & 30 hàng tháng rà soát tiến độ và tháo gỡ điểm nghẽn."),

    ("GROUP", "NHÓM II: XÂY DỰNG GIAO DIỆN & BỘ CÔNG CỤ TIỆN ÍCH TRÊN WEB", "", "", ""),
    ("ROW", "2.1 Xây dựng Trang Chủ Master Hub (momo.vn/tai-chinh)",
     "Key Owner (A/R)", "Consulted (C)", "Consulted (C)",
     "Lập trình mặt tiền Cổng Khám Phá & Ra Quyết Định Tài Chính Toàn Diện, thiết kế Mega Navigation Bar, Dashboard thị trường và các thẻ điều hướng theo 5 nhóm JTBD."),

    ("ROW", "2.2 Phát triển Bộ Simulator & Client-side Calculators (Lương, Thuế, Lãi Tiết Kiệm, FIRE)",
     "Key Owner (A/R)", "Consulted (C)", "Informed (I)",
     "Web Platform phát triển các công cụ tính toán không cần đăng nhập (Zero-Latency UI); FinHub BU cung cấp và chuẩn hóa công thức nghiệp vụ tài chính và biên độ lãi suất đối tác."),

    ("ROW", "2.3 Cấu hình Điểm Chạm Chuyển Tiếp Web-to-App (Universal OneLink & Dynamic QR)",
     "Key Owner (A/R)", "Co-Owner (A/R)", "Consulted (C)",
     "Tích hợp mã Appsflyer OneLink cho nút CTA trên Mobile Web và Dynamic QR Code trên Desktop Web; FinHub cung cấp deeplink chính xác dẫn thẳng vào màn hình sản phẩm tương ứng trong App."),

    ("GROUP", "NHÓM III: TÍCH HỢP DỮ LIỆU THỊ TRƯỜNG & ĐỐI TÁC NGÂN HÀNG (DATA & PARTNERS)", "", "", ""),
    ("ROW", "3.1 Tích Hợp Dữ Liệu Realtime Giá Vàng SJC/9999 & Tỷ Giá Ngoại Tệ",
     "Co-Owner (A/R)", "Informed (I)", "Key Owner (A/R)",
     "Backend Team kết nối API dữ liệu giá vàng và tỷ giá ngoại tệ đa ngân hàng; Web Platform lập trình biểu đồ lịch sử 7-30 ngày và bộ chuyển đổi tiền tệ 2 chiều."),

    ("ROW", "3.2 Triển Khai Programmatic Hub 34 Ngân Hàng Đối Tác (/tai-chinh/ngan-hang/[slug])",
     "Key Owner (A/R)", "Co-Owner (A/R)", "Consulted (C)",
     "Web Platform tự động sinh 34 trang chi tiết ngân hàng chuẩn SEO; FinHub BU phối hợp đối tác ngân hàng cung cấp gói quà tặng liên kết ví 500k."),

    ("ROW", "3.3 Vận Hành Cổng Tra Cứu CIC & Điểm Tín Dụng MoMo (/tra-cuu-cic)",
     "Key Owner (A/R)", "Co-Owner (A/R)", "Consulted (C)",
     "Web Platform xây dựng CIC Simulator & cẩm nang nợ xấu; FinHub BU chịu trách nhiệm logic tính điểm tín dụng MoMo độc quyền và luồng mở báo cáo in-app."),

    ("GROUP", "NHÓM IV: NỘI DUNG CHUẨN E-E-A-T & TỰ ĐỘNG HÓA AI (CONTENT & PULSE)", "", "", ""),
    ("ROW", "4.1 Sản Xuất Cẩm Nang Tài Chính & MoSpark GenAI Pipeline",
     "Key Owner (A/R)", "Consulted (C)", "Contributor (R)",
     "Web Platform biên soạn và vận hành pipeline GenAI trên MoSpark; FinHub BU kiểm duyệt nội dung đảm bảo tuân thủ quy định pháp luật và chính sách tín dụng của NHNN."),

    ("ROW", "4.2 Vận Hành Hệ Thống Tin Tức Thị Trường Tự Động (AI Financial Pulse)",
     "Key Owner (A/R)", "Informed (I)", "Consulted (C)",
     "Lập trình module quét tin báo chí tự động, lọc nhiễu AI, tóm tắt 2 gạch đầu dòng và hiển thị dòng tin tức 24/7 (mô hình Finpath AI) mà không tốn người viết."),

    ("GROUP", "NHÓM V: BÁO CÁO TIẾN ĐỘ & TRÁCH NHIỆM GIẢI TRÌNH (ACCOUNTABILITY)", "", "", ""),
    ("ROW", "5.1 Báo Cáo Hiệu Quả Phễu Web-to-App Hàng Tháng Lên Ban Lãnh Đạo IVP",
     "Key Owner (A/R)", "Co-Owner (A/R)", "Contributor (R)",
     "Web Platform và FinHub BU đồng chủ trì gửi báo cáo tiến độ và hiệu quả chuyển đổi W2A hàng tháng lên Ban Lãnh Đạo IVP (theo chuẩn Key Highlights & Business Impact)."),

    ("ROW", "5.2 Quy Chế Rút Lui & Điều Phối Tài Nguyên (Deprioritization & Accountability)",
     "Key Owner (A/R)", "Co-Owner (A/R)", "Informed (I)",
     "Nếu sau 1-2 tháng phối hợp mà FinHub BU không tập trung cung cấp chính sách đối tác/deeplink hoặc trễ cam kết, Web Platform sẽ chủ động bàn giao lại dự án và chuyển tài nguyên sang BU khác.")
]

for item in raci_matrix_data:
    item_type = item[0]
    if item_type == "GROUP":
        ws_raci.append([item[1], "", "", "", ""])
        r = ws_raci.max_row
        ws_raci.merge_cells(f"A{r}:E{r}")
        ws_raci.cell(row=r, column=1).fill = section_fill
        ws_raci.cell(row=r, column=1).font = section_font
        ws_raci.row_dimensions[r].height = 22.0
    elif item_type == "ROW":
        ws_raci.append(list(item[1:]))
        r = ws_raci.max_row
        ws_raci.row_dimensions[r].height = 36.0
        
        c1 = ws_raci.cell(row=r, column=1); c1.font = font_bold; c1.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
        c2 = ws_raci.cell(row=r, column=2); c2.alignment = Alignment(horizontal='center', vertical='center')
        c3 = ws_raci.cell(row=r, column=3); c3.alignment = Alignment(horizontal='center', vertical='center')
        c4 = ws_raci.cell(row=r, column=4); c4.alignment = Alignment(horizontal='center', vertical='center')
        c5 = ws_raci.cell(row=r, column=5); c5.font = font_regular; c5.alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)

        for cell, role_txt in [(c2, item[2]), (c3, item[3]), (c4, item[4])]:
            if "Key Owner" in role_txt: cell.font = font_role_key_owner
            elif "Co-Owner" in role_txt: cell.font = font_role_co_owner
            elif "Contributor" in role_txt: cell.font = font_role_contributor
            elif "Consulted" in role_txt: cell.font = font_role_consulted
            elif "Informed" in role_txt: cell.font = font_role_informed
            else: cell.font = font_bold

        for c_i in range(1, 6): ws_raci.cell(row=r, column=c_i).border = thin_border

# Definitions at the bottom
ws_raci.append([""])
ws_raci.append(["BẢNG CHÚ GIẢI KÝ HIỆU & NGUYÊN TẮC PHÂN CÔNG RACI:"])
r_def = ws_raci.max_row
ws_raci.cell(row=r_def, column=1).font = Font(name='Arial', size=10, bold=True, color='002060')

raci_glossary = [
    ("Key Owner (A/R)", "Accountable & Responsible", "Chủ Trì & Chịu Trách Nhiệm Chính", "Đội ngũ chịu trách nhiệm giải trình cao nhất (Accountability) trước Ban Lãnh Đạo IVP và trực tiếp thực thi/nghiệm thu hạng mục."),
    ("Co-Owner (A/R)", "Co-Accountable & Responsible", "Đồng Sở Hữu & Đồng Thực Thi", "Đội ngũ cùng cam kết kết quả đầu ra, chịu trách nhiệm cung cấp chính sách, deeplink, dữ liệu nghiệp vụ và đồng sở hữu KPI."),
    ("Contributor (R)", "Responsible Contributor", "Đội Ngũ Thực Thi Hỗ Trợ", "Đội ngũ trực tiếp tham gia hỗ trợ kỹ thuật, đấu nối hệ thống hoặc cung cấp hạ tầng dữ liệu theo đúng cam kết thời hạn."),
    ("Consulted (C)", "Consulted", "Tham Vấn Chuyên Môn 2 Chiều", "Đội ngũ được tham khảo ý kiến chuyên môn (công thức lãi suất, kiểm duyệt luật tài chính YMYL, góp ý luồng UX) trước khi ban hành."),
    ("Informed (I)", "Informed", "Nhận Thông Tin 1 Chiều", "Đội ngũ nhận báo cáo cập nhật tiến độ định kỳ để nắm bối cảnh liên phòng ban, không bắt buộc tham gia vận hành chi tiết.")
]

ws_raci.append(["Thuật Ngữ RACI", "Tên Tiếng Anh", "Vai Trò Thực Tế", "Mô Tả Trách Nhiệm Chi Tiết"])
r_h = ws_raci.max_row
for c_i in range(1, 5):
    c = ws_raci.cell(row=r_h, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center')
ws_raci.row_dimensions[r_h].height = 24.0

for g in raci_glossary:
    ws_raci.append(list(g))
    r = ws_raci.max_row
    ws_raci.row_dimensions[r].height = 22.0
    ws_raci.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center'); ws_raci.cell(row=r, column=1).font = font_bold
    ws_raci.cell(row=r, column=2).alignment = Alignment(horizontal='left', vertical='center'); ws_raci.cell(row=r, column=2).font = font_bold
    ws_raci.cell(row=r, column=3).alignment = Alignment(horizontal='left', vertical='center')
    ws_raci.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center')
    for c_i in range(1, 5): ws_raci.cell(row=r, column=c_i).border = thin_border

raci_widths = [42, 22, 24, 22, 75]
for idx, w in enumerate(raci_widths, start=1):
    ws_raci.column_dimensions[get_column_letter(idx)].width = w

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully updated RACI terms to Key Owner (A/R), Co-Owner (A/R), Contributor (R), Consulted (C), Informed (I) in 05_HUBS/financial-hub-roadmap.xlsx!")
