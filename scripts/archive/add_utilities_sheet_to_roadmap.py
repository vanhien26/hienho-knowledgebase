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
font_highlight = Font(name='Arial', size=9.5, bold=True, color='002060')

# 1. CREATE SHEET UTILITIES
if 'Utilities' in wb.sheetnames:
    del wb['Utilities']

ws_u = wb.create_sheet('Utilities', index=2)

ws_u.append(["ĐẶC TẢ BỘ TIỆN ÍCH FINANCIAL HUB & QUY CHUẨN CHUYỂN ĐỔI (UTILITIES CONVERSION DOCK SPECIFICATION)"])
ws_u.merge_cells("A1:H1")
ws_u.cell(row=1, column=1).fill = section_fill
ws_u.cell(row=1, column=1).font = section_font
ws_u.row_dimensions[1].height = 25.0

ws_u.append(["Mỗi công cụ tính toán (Utility Tool) bắt buộc phải tích hợp 2 thành phần chuyển đổi: (1) Hộp MoMo Gợi Ý (AI) phản hồi động theo mức tiền user nhập; (2) Lưới Icon Dịch Vụ MoMo điều hướng in-app"])
ws_u.merge_cells("A2:H2")
ws_u.cell(row=2, column=1).font = Font(name='Arial', size=9.5, italic=True, color='475569')
ws_u.row_dimensions[2].height = 20.0

u_headers = [
    "STT",
    "Tên Tiện Ích / Công Cụ",
    "Trường Đầu Vào & Logic Kích Hoạt (Inputs / Triggers)",
    "Kết Quả Tính Toán Tức Thì (Zero-Latency Output)",
    "MoMo Gợi Ý (AI) - Phản Hồi Động Theo Mức Nhập (Dynamic Rule Engine)",
    "Đề Xuất Dịch Vụ MoMo Qua Icon Điều Hướng (Service Icon Grid)",
    "Sản Phẩm FinHub Thúc Đẩy",
    "Trạng Thái"
]
ws_u.append(u_headers)
for c_i in range(1, len(u_headers) + 1):
    c = ws_u.cell(row=3, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_u.row_dimensions[3].height = 32.0

utilities_data = [
    (1, "Tính Lương (Gross - Net)",
     "• Lương Gross (VND)\n• Số người phụ thuộc\n• Mức đóng bảo hiểm (Trên lương chính thức hay theo mức thỏa thuận)",
     "• Lương Net thực nhận\n• Tiền đóng BHXH (8%), BHYT (1.5%), BHTN (1%)\n• Tiền thuế TNCN tạm nộp theo biểu lũy tiến 7 bậc",
     "• Nhập < 11tr: 'Với mức lương [10 triệu], bạn chưa phải nộp thuế TNCN. Mẹo tích lũy: Hãy trích ngay [1.8 triệu] (20% lương) vào Túi Thần Tài để sau 1 năm có sẵn quỹ dự phòng [22 triệu] sinh lời mỗi ngày.'\n"
     "• Nhập 15 - 35tr: 'Với mức lương [30 triệu], bạn chịu khoảng [2.15 triệu] thuế TNCN. Dòng tiền thặng dư sau sinh hoạt ước đạt [8-10 triệu]. Mẹo tối ưu: Chia [5 triệu] vào Tiết Kiệm Online và [3 triệu] vào Thực Tập Sinh Đầu Tư để tối ưu lợi suất kép.'\n"
     "• Nhập > 40tr: 'Với mức lương [60 triệu], thuế TNCN khoảng [9.8 triệu]/tháng. Mẹo quản trị: Hãy đăng ký người phụ thuộc để giảm trừ thuế, đồng thời trích 20 triệu phân bổ cân bằng: 50% Tiết Kiệm + 50% Quỹ Cổ Phiếu.'",
     "1. Túi Thần Tài (Icon Túi Thần Tài - Sinh lời 4-6%/năm rút bất kỳ lúc nào)\n"
     "2. Tiết Kiệm Online (Icon Tiết Kiệm - Bản Việt & VPBank cộng thêm 0.2% lãi)\n"
     "3. Hũ Chi Tiêu (Icon Hũ Chi Tiêu - Tự động khóa hạn mức chi tiêu sinh hoạt)",
     "Gửi Tiết Kiệm, Thực Tập Sinh Đầu Tư", "Live"),

    (2, "Phân Bổ Lương 50/30/20 & Hũ Tài Chính",
     "• Thu nhập thực nhận hàng tháng\n• Các khoản chi phí cố định (Tiền nhà, tiền học, trả góp)\n• Tùy chọn mô hình (50/30/20 hoặc 6 Chiếc Hũ)",
     "• Biểu đồ tròn ngân sách trực quan\n• Số tiền cụ thể cho 3 hũ: Thiết yếu (50%), Linh hoạt (30%), Tích lũy (20%)\n• Cảnh báo thâm hụt ngân sách",
     "• Chi phí thiết yếu > 65%: 'Chi phí cố định đang chiếm [68%] thu nhập, vượt ngưỡng an toàn 50%. Hãy dùng Hũ Chi Tiêu MoMo để kiểm soát chặt chẽ ngân sách sinh hoạt.'\n"
     "• Tích lũy đạt chuẩn >= 20%: 'Bạn đang trích được [4 triệu] (20% thu nhập) để tích sản. Gợi ý: Tự động hóa việc trích tiền vào Tiết Kiệm TKO và Quỹ Mở SIP ngay ngày nhận lương.'",
     "1. Hũ Chi Tiêu (Icon Hũ - Cài đặt tự động chia tiền lương vào các hũ)\n"
     "2. Túi Thần Tài (Icon Túi - Hũ tích lũy 20% sinh lời mỗi ngày)\n"
     "3. Thực Tập Sinh Đầu Tư (Icon Quỹ Mở - Tích sản SIP từ 10.000đ)",
     "Gửi Tiết Kiệm, Thực Tập Sinh Đầu Tư, CIC", "In Progress"),

    (3, "Bảng So Sánh Lãi Suất 30+ Ngân Hàng",
     "• Số tiền dự kiến gửi (VND)\n• Kỳ hạn gửi mong muốn (1, 3, 6, 9, 12, 18, 24, 36 tháng)\n• Hình thức (Gửi Online TKO vs Gửi Tại Quầy)",
     "• Bảng xếp hạng lãi suất 30+ bank từ cao nhất đến thấp nhất\n• Số tiền lãi thực nhận khi đáo hạn của từng ngân hàng\n• Highlight ngân hàng đối tác MoMo",
     "• Số tiền < 20tr, kỳ hạn ngắn: 'Với số tiền [10 triệu] gửi ngắn hạn, tiền lãi ngân hàng chênh lệch không đáng kể. Hãy để trong Túi Thần Tài nhận lời mỗi ngày và rút ra chi tiêu bất kỳ lúc nào không lo mất lãi.'\n"
     "• Số tiền > 100tr, kỳ hạn 12 tháng: 'Với số tiền [300 triệu], chênh lệch 0.5% lãi suất mang lại thêm [1.5 triệu] tiền lời mỗi năm. Mở sổ Tiết kiệm Bản Việt trên MoMo hiện được cộng thêm 0.2% lãi suất ưu đãi.'",
     "1. Tiết Kiệm Bản Việt (Icon BVBank - Lãi suất top đầu +0.2% qua MoMo)\n"
     "2. Tiết Kiệm VPBank (Icon VPBank - Mở sổ online 100%, bảo mật ngân hàng)\n"
     "3. Túi Thần Tài (Icon Túi - Giữ tiền nhàn rỗi gom đủ mở sổ tiết kiệm)",
     "Gửi Tiết Kiệm (Top 1 Priority)", "In Progress"),

    (4, "Giá Vàng & Quy Đổi Đơn Vị Vàng",
     "• Số lượng vàng (Ounce, Cây, Lượng, Chỉ, Gram)\n• Thương hiệu quan tâm (SJC, PNJ, DOJI, Mi Hồng, Vàng 9999, Nhẫn trơn)",
     "• Giá mua vào và bán ra realtime\n• Giá trị quy đổi tương đương ra VND\n• Mức chênh lệch (Spread) Mua - Bán và biến động lịch sử 7-30 ngày",
     "• Số lượng nhỏ (< 1 chỉ): 'Vàng nhẫn trơn 9999 có biên độ mua - bán hẹp hơn vàng miếng SJC, thích hợp cho tích lũy lâu dài từng chỉ nhỏ. Tích lũy vàng online trên MoMo chỉ từ 0.1 chỉ.'\n"
     "• Số tiền lớn (> 1 lượng): 'Vàng đang ở vùng giá biến động mạnh. Hãy cân đối 50% vàng và 50% gửi Tiết Kiệm Online để bảo vệ dòng tiền phòng thủ.'",
     "1. Vàng Tài Lộc (Icon Vàng - Tích lũy vàng nhẫn online chỉ từ 0.1 chỉ)\n"
     "2. Túi Thần Tài (Icon Túi - Nơi để tiền sẵn sàng bắt đáy khi giá vàng điều chỉnh)\n"
     "3. Tiết Kiệm Online (Icon Tiết Kiệm - Cân bằng danh mục tài sản an toàn)",
     "Gửi Tiết Kiệm, Vàng Tài Lộc", "Live"),

    (5, "Tỷ Giá & Quy Đổi Đa Ngoại Tệ",
     "• Chọn loại ngoại tệ (USD, JPY, EUR, KRW, CNY, GBP...)\n• Số tiền cần đổi\n• Chọn ngân hàng thương mại đối chiếu",
     "• Số tiền VND tương đương theo tỷ giá Mua tiền mặt / Mua chuyển khoản / Bán ra\n• So sánh chênh lệch giữa các ngân hàng thương mại lớn",
     "• Đổi tiền đi du lịch / công tác: 'Khi chi tiêu nước ngoài, ưu tiên dùng Thẻ Visa/Mastercard MoMo với phí chuyển đổi ngoại tệ ưu đãi dưới 2% để tiết kiệm hàng triệu đồng so với đổi tiền mặt tại sân bay.'\n"
     "• Giữ ngoại tệ chờ tăng giá: 'Tỷ giá ngoại tệ biến động 1-2%/năm thấp hơn lãi suất gửi tiết kiệm VND (5-6%/năm). Chuyển đổi sang VND gửi Tiết kiệm Online để tối ưu tiền lời.'",
     "1. Thẻ Visa MoMo (Icon Visa - Miễn phí phát hành thẻ, phí ngoại tệ ưu đãi)\n"
     "2. Thẻ Mastercard (Icon Mastercard - Thanh toán toàn cầu, hoàn tiền mua sắm)\n"
     "3. Nhận Kiều Hối (Icon Kiều Hối - Nhận tiền từ Nhật, Hàn, Mỹ về ví)",
     "Gửi Tiết Kiệm, Thẻ Quốc Tế", "In Progress"),

    (6, "CIC Simulator & Đánh Giá Nhóm Nợ",
     "• Số ngày quá hạn thanh toán dài nhất (Chưa từng / Dưới 10 ngày / 10-30 ngày / 30-90 ngày / Trên 90 ngày)\n• Số lượng thẻ tín dụng và khoản vay hiện tại\n• Tỷ lệ sử dụng hạn mức thẻ",
     "• Dự báo Nhóm Nợ CIC (Nhóm 1 đến Nhóm 5)\n• Đánh giá khả năng phê duyệt hồ sơ vay / mở thẻ ngân hàng\n• Thời gian cần thiết để làm sạch lịch sử nợ xấu",
     "• Nợ Nhóm 1 (Chuẩn): 'Điểm tín dụng của bạn đang ở mức tốt. Duy trì không dùng quá 70% hạn mức thẻ để được ưu tiên nâng hạn mức vay tiêu dùng in-app.'\n"
     "• Nợ Nhóm 2 (Cần chú ý): 'Khoản trễ hạn khiến hồ sơ rơi vào Nhóm 2. Hãy tất toán ngay dư nợ trong 3 ngày tới để ngăn chặn hồ sơ chuyển sang nợ xấu Nhóm 3 trên hệ thống CIC Quốc Gia.'",
     "1. Báo Cáo Điểm Tín Dụng (Icon CIC - Kiểm tra báo cáo chính thức miễn phí)\n"
     "2. Ví Trả Sau (Icon VTS - Kích hoạt hạn mức tiêu dùng miễn lãi đến 45 ngày)\n"
     "3. Thanh Toán Hóa Đơn (Icon Hóa Đơn - Cài đặt tự động thanh toán giữ điểm sạch)",
     "CIC (Top 1 Priority)", "Live"),

    (7, "Quản Lý Dòng Tiền & Tiêu Dùng",
     "• Thu nhập tổng các nguồn\n• Danh mục chi tiêu thiết yếu hàng tháng\n• Khoản tiền dự phòng hiện có",
     "• Dòng Tiền Tự Do (Free Cash Flow)\n• Quy mô Quỹ Khẩn Cấp khuyến nghị (3 - 6 tháng chi phí)\n• Số tháng tài chính cầm cự nếu mất nguồn thu nhập",
     "• Dòng tiền tự do dương: 'Bạn đang có thặng dư [6 triệu]/tháng sau khi trừ sinh hoạt. Mẹo dòng tiền: Đừng để tiền nhàn rỗi đứng yên, hãy tự động chuyển vào Túi Thần Tài nhận tiền lời mỗi ngày.'\n"
     "• Quỹ khẩn cấp chưa đủ: 'Quỹ dự phòng hiện tại chỉ đủ [1.5 tháng] chi tiêu. Hãy tạm hoãn đầu tư rủi ro và trích tiền xây dựng quỹ khẩn cấp tối thiểu 3 tháng.'",
     "1. Hũ Chi Tiêu (Icon Hũ - Khóa trần hạn mức chi tiêu tuần/tháng chống bội chi)\n"
     "2. Túi Thần Tài (Icon Túi - Nơi cất giữ quỹ khẩn cấp sinh lời an toàn)\n"
     "3. Tiết Kiệm Online (Icon Tiết Kiệm - Sổ tiết kiệm dự phòng rút gốc linh hoạt)",
     "Gửi Tiết Kiệm, Túi Thần Tài", "Planned"),

    (8, "Tích Sản FIRE & Giả Lập SIP",
     "• Chi phí sinh hoạt mong muốn khi nghỉ hưu (VND/tháng)\n• Tuổi hiện tại và tuổi mục tiêu nghỉ hưu\n• Số vốn khởi điểm và số tiền có thể tích lũy định kỳ mỗi tháng",
     "• Số tiền mục tiêu để đạt Tự Do Tài Chính (FIRE Number = Chi phí năm x 25)\n• Số tiền cần đầu tư mỗi tháng để đạt mục tiêu\n• Biểu đồ lãi kép tích sản theo thời gian",
     "• Tuổi trẻ (< 30 tuổi): 'Bạn có lợi thế lớn về thời gian. Chỉ cần trích [1.5 triệu]/tháng đầu tư Quỹ Mở SIP với lợi suất kỳ vọng 12%/năm, sức mạnh lãi kép sau 15 năm sẽ mang lại hơn [750 triệu] đồng.'\n"
     "• Mục tiêu FIRE lớn: 'Để đạt tự do tài chính ở tuổi [40], danh mục cần phân bổ theo 2 chân kiềng: 50% vào Tiết Kiệm an toàn và 50% vào Quỹ Cổ Phiếu tăng trưởng.'",
     "1. Thực Tập Sinh Đầu Tư (Icon Chứng Khoán CVX - Mua cổ phiếu từ 1 cổ)\n"
     "2. Quỹ Mở SIP (Icon Dragon/SSIAM - Tích sản định kỳ quỹ mở từ 10.000đ)\n"
     "3. Tiết Kiệm Online (Icon Tiết Kiệm - Chân kiềng tài sản an toàn 50% vốn)",
     "Thực Tập Sinh Đầu Tư, Gửi Tiết Kiệm", "Planned")
]

for row_item in utilities_data:
    ws_u.append(list(row_item))
    r = ws_u.max_row
    num_lines = max(row_item[4].count('\n') + 1, row_item[5].count('\n') + 1)
    ws_u.row_dimensions[r].height = max(55.0, num_lines * 17.0)

    ws_u.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_u.cell(row=r, column=2).alignment = Alignment(horizontal='left', vertical='center'); ws_u.cell(row=r, column=2).font = font_bold
    ws_u.cell(row=r, column=3).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_u.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_u.cell(row=r, column=5).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_u.cell(row=r, column=6).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_u.cell(row=r, column=7).alignment = Alignment(horizontal='center', vertical='center'); ws_u.cell(row=r, column=7).font = font_highlight
    ws_u.cell(row=r, column=8).alignment = Alignment(horizontal='center', vertical='center')

    for c_i in range(1, 9):
        ws_u.cell(row=r, column=c_i).border = thin_border

col_widths_u = [6, 26, 32, 34, 60, 42, 28, 14]
for idx, w in enumerate(col_widths_u, start=1):
    ws_u.column_dimensions[get_column_letter(idx)].width = w

# 2. UPDATE README TABLE OF CONTENTS
ws_readme = wb['Readme']
# Look for Table of Contents or Structure in Readme and add Utilities sheet
readme_updated = False
for r in range(1, ws_readme.max_row + 1):
    v = str(ws_readme.cell(row=r, column=1).value or '')
    if 'Cấu Trúc Các Sheet' in v or 'MỤC LỤC' in v or 'Danh Sách Sheet' in v:
        # Check next rows
        pass

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully created 'Utilities' sheet in 05_HUBS/financial-hub-roadmap.xlsx!")
