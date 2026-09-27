import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter


from scripts._lib import load_workbook_safe, save_with_backup, standard_argparser

def main(args=None):
    wb = load_workbook_safe('05_HUBS/financial-hub-roadmap.xlsx')

    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(name='Arial', size=10, bold=True, color='FFFFFF')
    section_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    section_font = Font(name='Arial', size=10.5, bold=True, color='1F4E78')
    thin_side = Side(style='thin', color='64748B')
    thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

    p0_fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid") # Gray (T7)
    p1_fill = PatternFill(start_color="E2F0D9", end_color="E2F0D9", fill_type="solid") # Green (T8, T9)
    p2_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid") # Blue (T10+)

    status_done_fill = PatternFill(start_color="1E7E34", end_color="1E7E34", fill_type="solid")
    status_done_font = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')
    status_prog_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")
    status_prog_font = Font(name='Arial', size=9.5, bold=True, color='B9770E')
    status_plan_fill = PatternFill(start_color="1B4F72", end_color="1B4F72", fill_type="solid")
    status_plan_font = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')

    font_bold = Font(name='Arial', size=9.5, bold=True)
    font_regular = Font(name='Arial', size=9.5)

    # Rebuild Roadmap sheet to match exactly user's breakdown:
    # Tháng 7: Ví trả sau, Vay nhanh
    # Tháng 8: Giá vàng, Tính lương, Bảo hiểm xã hội, Lương hưu (+ Financial Hub, Chuyên trang Điểm Tín Dụng)
    # Tháng 9: Tỷ giá, Phân bổ lương, Lãi suất (+ Chứng khoán & Chứng chỉ quỹ)
    # Tháng 10+: Quản lý dòng tiền, FIRE
    roadmap_items = [
        # 0: Phase, 1: Timeline, 2: Track, 3: Product Name, 4: Tech & UX Scope, 5: W2A Hook, 6: Status
        # THÁNG 7/2026
        ("Phase 0", "Tháng 7/2026", "Tín Dụng & Tiêu Dùng", "Ví Trả Sau",
         "• Công cụ tính toán hạn mức và dự toán số tiền trả góp hàng tháng khi thanh toán qua Ví Trả Sau.\n"
         "• Mô phỏng biểu phí, lãi suất 0% tối đa 45 ngày và chuyển đổi trả góp 3 - 12 tháng.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) phản hồi động theo mức nhập + Lưới Icon Dịch Vụ MoMo (chi tiết xem sheet Utilities).",
         "CTA 'Mở Ví Trả Sau TPBank' nhận ngay hạn mức đến 20 triệu đồng chi tiêu trước trả sau.",
         "Done"),

        ("Phase 0", "Tháng 7/2026", "Tín Dụng & Cho Vay", "Vay Nhanh",
         "• Công cụ tính lịch trả nợ giảm dần và số tiền thanh toán hàng tháng theo khoản vay (5 - 100 triệu) và kỳ hạn (6 - 48 tháng).\n"
         "• Bảng minh bạch lãi suất đối tác tài chính (EVN Finance, Shinhan Finance, Mcredit).\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) phản hồi động theo mức nhập + Lưới Icon Dịch Vụ MoMo (chi tiết xem sheet Utilities).",
         "CTA 'Đăng Ký Vay Nhanh 1 Phút' giải ngân trực tiếp vào ví MoMo không cần thế chấp.",
         "Done"),

        # THÁNG 8/2026
        ("Phase 1", "Tháng 8/2026", "Master Gateway", "Financial Hub",
         "• Master Gateway quy hoạch 3 Hero Product Banners nổi bật nhất tại Hero Zone: Điểm Tín Dụng CIC, Gửi Tiết Kiệm TKO, Thực Tập Sinh Đầu Tư.\n"
         "• Cấu hình 301 Redirect toàn diện từ /trung-tam-tai-chinh sang /tai-chinh.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "Universal OneLink dẫn trực diện vào 3 phễu chính: Kiểm Tra CIC / Mở Sổ Tiết Kiệm / Thực Tập Sinh Đầu Tư.",
         "Done"),

        ("Phase 1", "Tháng 8/2026", "Sức Khỏe Tín Dụng", "Điểm Tín Dụng (/diem-tin-dung)",
         "• Chuyên trang Điểm Tín Dụng & Tra Cứu CIC chính thức (/diem-tin-dung).\n"
         "• Widget CIC Simulator đánh giá nhóm nợ 1-5 và cơ chế Pre-scoring Lead Capture thu thập SĐT trước khi mở App.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "CTA 'Kiểm Tra Báo Cáo CIC Miễn Phí Trên App MoMo' & 'Mở Sổ Tiết Kiệm Tăng Điểm Uy Tín'.",
         "Done"),

        ("Phase 1", "Tháng 8/2026", "Đầu Tư & Vàng", "Giá Vàng",
         "• Bảng giá vàng realtime đa thương hiệu SJC, PNJ, DOJI, 9999 kèm biểu đồ lịch sử.\n"
         "• Widget So Sánh Hiệu Suất Tích Sản: Vàng vs Gửi Tiết Kiệm vs Chứng Chỉ Quỹ.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) phản hồi động theo mức nhập + Lưới Icon Dịch Vụ MoMo.",
         "CTA 'Tích Lũy Vàng Nhẫn Online Từ 0.1 Chỉ Cùng Vàng Tài Lộc' & 'Mở Sổ Tiết Kiệm Phòng Thủ'.",
         "Done"),

        ("Phase 1", "Tháng 8/2026", "Thu Nhập & Thuế", "Tính Lương",
         "• Công cụ tính lương Gross sang Net 2026 (Pure Client-side JS, không phụ thuộc API ngoài).\n"
         "• Nhúng cơ chế MoMo Gợi Ý động: Lương 10tr (tích lũy 20%), 30tr (chia Tiết kiệm + Đầu tư), 60tr (quản trị thuế & tài sản).\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "Bộ 3 nút CTA trực tiếp sau tính lương: 'Mở Sổ Tiết Kiệm Bản Việt / VPBank' | 'Thực Tập Sinh Đầu Tư' | 'Kiểm Tra CIC'.",
         "Done"),

        ("Phase 1", "Tháng 8/2026", "An Sinh Xã Hội", "Bảo Hiểm Xã Hội",
         "• Công cụ tính toán và ước tính tiền rút Bảo Hiểm Xã Hội (BHXH) một lần cập nhật Luật BHXH mới nhất.\n"
         "• Giả lập số tiền nhận được dựa trên mức đóng bình quân và tổng số năm/tháng tham gia BHXH bắt buộc/tự nguyện.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "CTA 'Dòng Tiền Sau Rút BHXH: Tự Động Trích Tiền Vào Túi Thần Tài Sinh Lời Hàng Ngày 4-6%/năm Hoặc Mua Sổ Tiết Kiệm'.",
         "Done"),

        ("Phase 1", "Tháng 8/2026", "An Sinh Xã Hội", "Lương Hưu",
         "• Công cụ dự toán mức hưởng Lương Hưu hàng tháng khi về già dựa trên số năm đóng BHXH và độ tuổi nghỉ hưu.\n"
         "• So sánh tỷ lệ hưởng lương hưu tối đa (75%) và phân tích bài toán bù đắp thiếu hụt thu nhập tuổi già.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "CTA 'Chuẩn Bị Quỹ Hưu Trí Tự Thân: Tích Sản Chứng Chỉ Quỹ SIP Từ 10k/Ngày & Gửi Tiết Kiệm Dài Hạn'.",
         "Done"),

        # THÁNG 9/2026
        ("Phase 1", "Tháng 9/2026", "Tiền Tệ & Ngoại Hối", "Tỷ Giá",
         "• Cổng tỷ giá master (/tai-chinh/ty-gia) và programmatic subpages theo từng cặp tiền (/tai-chinh/ty-gia/[pair-slug]) cho 20+ ngoại tệ (USD/VND, JPY/VND, EUR/VND...).\n"
         "• Widget Phân Tích Lợi Suất: So sánh 'Giữ Ngoại Tệ vs Đổi Sang VND Gửi Tiết Kiệm Lãi Cao' ➔ Kéo traffic về sản phẩm Tiết Kiệm Online.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) phản hồi động theo mức nhập + Lưới Icon Dịch Vụ MoMo.",
         "CTA 'Tối Ưu Dòng Tiền: Đổi Sang VND Gửi Tiết Kiệm Lãi Suất Đến 6.5%' hoặc 'Tích Sản Chứng Chỉ Quỹ'.",
         "In Progress"),

        ("Phase 1", "Tháng 9/2026", "Thu Nhập & Quản Lý Chi Tiêu", "Phân Bổ Lương",
         "• Công cụ phân bổ 50/30/20 & 6 Chiếc Hũ tự động mapping:\n"
         "  • Hũ Tích Lũy 20% ➔ Suggest trực diện mở Sổ Tiết Kiệm Bản Việt / VPBank.\n"
         "  • Hũ Đầu Tư 10% ➔ Suggest tham gia Thực Tập Sinh Đầu Tư.\n"
         "  • Đo lường chỉ số an toàn đòn bẩy ➔ Suggest kiểm tra Điểm Tín Dụng CIC.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "CTA 1-Click: 'Tự Động Trích Tiền Sang Tiết Kiệm TKO' và 'Kích Hoạt Gói Thực Tập Sinh Đầu Tư'.",
         "In Progress"),

        ("Phase 1", "Tháng 9/2026", "Tiết Kiệm & Lãi Suất", "Lãi Suất",
         "• Xây dựng Bảng So Sánh Lãi Suất Tiền Gửi 30+ Ngân Hàng (/lai-suat) theo các kỳ hạn 1 - 36 tháng (Online TKO vs Tại quầy).\n"
         "• Ghim sản phẩm Tiết Kiệm Online MoMo (Bản Việt & VPBank) ở vị trí Top 1 kèm nhãn ưu đãi '+0.2% Lãi Suất Khi Mở Trên MoMo'.\n"
         "• Tab đối chiếu: 'So sánh Gửi Tiết Kiệm (5%/năm) vs Chứng Chỉ Quỹ (10-15%/năm)' để kéo user trẻ tích sản.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "Nút CTA 'Mở Sổ Tiết Kiệm Online Bản Việt / VPBank Lãi Suất Ưu Đãi' & 'Tích Sản SIP Cùng Thực Tập Sinh Đầu Tư'.",
         "In Progress"),

        # THÁNG 10/2026+ (PHASE 2)
        ("Phase 2", "Tháng 10/2026", "Đầu Tư & Chứng Chỉ Quỹ", "Chứng Khoán & Chứng Chỉ Quỹ",
         "• Cổng thông tin chính thức của Chương Trình 'Thực Tập Sinh Đầu Tư' (Chứng khoán CVX & Chứng Chỉ Quỹ SIP Dragon Capital, VinaCapital, SSIAM).\n"
         "• Bộ giả lập Lãi Kép Tích Lũy Định Kỳ từ 10k/ngày.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "CTA Trọng Tâm: 'Đăng Ký Tham Gia Thực Tập Sinh Đầu Tư - Nhận Quà Khởi Nghiệp' & 'Mở Sổ Tiết Kiệm Cân Bằng'.",
         "Planned"),

        ("Phase 2", "Tháng 10/2026", "Dòng Tiền & Tiêu Dùng", "Quản Lý Dòng Tiền & Tiêu Dùng",
         "• Bộ tính Dòng Tiền Tự Do (Free Cash Flow) & Hạn mức tiêu dùng ➔ Tự động phân luồng dòng tiền dư thừa vào Tiết Kiệm TKO / Túi Thần Tài / Đầu tư SIP.\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "CTA 'Phân Bổ Dòng Tiền Thặng Dư: Gửi Tiết Kiệm Online / Tích Sản SIP Đầu Tư / Kiểm Tra Sức Khỏe CIC'.",
         "Planned"),

        ("Phase 2", "Tháng 10/2026", "Tích Sản & Hưu Trí", "Đầu Tư & Tích Sản FIRE",
         "• Bộ Giả Lập Tự Do Tài Chính & Nghỉ Hưu Sớm (FIRE Simulator).\n"
         "• Phân bổ 2 Trụ Cột: Vốn Phòng Thủ (Tiết Kiệm 30 Bank) + Vốn Tăng Trưởng (Chứng Chỉ Quỹ).\n"
         "• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) + Lưới Icon Dịch Vụ MoMo.",
         "CTA 'Xây Dựng Danh Mục FIRE: 50% Gửi Tiết Kiệm An Toàn + 50% Thực Tập Sinh Đầu Tư Tăng Trưởng'.",
         "Planned")
    ]

    if 'Roadmap' in wb.sheetnames:
        del wb['Roadmap']

    ws_rd = wb.create_sheet('Roadmap', index=1)
    ws_rd.append(["LỘ TRÌNH TRIỂN KHAI TOÀN DIỆN CÁC TÍNH NĂNG FINANCIAL MASTER HUB (2026 - 2027)"])
    ws_rd.merge_cells("A1:G1")
    ws_rd.cell(row=1, column=1).fill = section_fill
    ws_rd.cell(row=1, column=1).font = section_font
    ws_rd.row_dimensions[1].height = 25.0

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

    for row_item in roadmap_items:
        ws_rd.append(list(row_item))
        r = ws_rd.max_row
        num_lines = max(row_item[4].count('\n') + 1, row_item[5].count('\n') + 1)
        ws_rd.row_dimensions[r].height = max(55.0, num_lines * 17.5)

        ws_rd.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
        ws_rd.cell(row=r, column=2).alignment = Alignment(horizontal='center', vertical='center')
        ws_rd.cell(row=r, column=3).alignment = Alignment(horizontal='center', vertical='center'); ws_rd.cell(row=r, column=3).font = font_bold
        ws_rd.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center'); ws_rd.cell(row=r, column=4).font = font_bold
        ws_rd.cell(row=r, column=5).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
        ws_rd.cell(row=r, column=6).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
        ws_rd.cell(row=r, column=7).alignment = Alignment(horizontal='center', vertical='center')

        phase = row_item[0]
        time_str = row_item[1]
        if "Tháng 7" in time_str: ws_rd.cell(row=r, column=1).fill = p0_fill
        elif "Tháng 8" in time_str or "Tháng 9" in time_str: ws_rd.cell(row=r, column=1).fill = p1_fill
        else: ws_rd.cell(row=r, column=1).fill = p2_fill

        status_val = row_item[6]
        c_st = ws_rd.cell(row=r, column=7)
        if status_val == "Done": c_st.fill = status_done_fill; c_st.font = status_done_font
        elif status_val == "In Progress": c_st.fill = status_prog_fill; c_st.font = status_prog_font
        elif status_val == "Planned": c_st.fill = status_plan_fill; c_st.font = status_plan_font

        for c_i in range(1, 8): ws_rd.cell(row=r, column=c_i).border = thin_border

    col_widths = [14, 16, 26, 28, 75, 48, 16]
    for idx, w in enumerate(col_widths, start=1):
        ws_rd.column_dimensions[get_column_letter(idx)].width = w

    save_with_backup(wb, '05_HUBS/financial-hub-roadmap.xlsx', dry_run=args.dry_run, make_backup=not args.no_backup)
    print("Successfully synced Roadmap sheet with exact tools: Tháng 7 (Ví trả sau, Vay nhanh), Tháng 8 (Giá vàng, Tính lương, BHXH, Lương hưu), Tháng 9 (Tỷ giá, Phân bổ lương, Lãi suất)!")

if __name__ == "__main__":
    _ap = standard_argparser("Fix runner - safe with --dry-run")
    main(_ap.parse_args())

