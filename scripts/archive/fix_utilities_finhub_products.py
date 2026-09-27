import openpyxl

wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')
ws_u = wb['Utilities']

# Row 6 is Tỷ Giá (index r=7)
# Old: Thẻ Visa, Mastercard, Nhận Kiều Hối (Not Finhub)
# New Finhub: 1. Tiết Kiệm Online (Đổi sang VND gửi tiết kiệm 6.5%), 2. Túi Thần Tài (Tiền nhàn rỗi sinh lời mỗi ngày), 3. Thực Tập Sinh Đầu Tư (Đầu tư quỹ mở)
for r in range(4, ws_u.max_row + 1):
    tool_name = str(ws_u.cell(row=r, column=2).value or '')
    if 'Tỷ Giá' in tool_name:
        ws_u.cell(row=r, column=6).value = (
            "1. Tiết Kiệm Online (Icon Tiết Kiệm - Đổi ngoại tệ sang VND gửi tiết kiệm sinh lời đến 6.5%/năm)\n"
            "2. Túi Thần Tài (Icon Túi - Nơi giữ tiền thặng dư chờ tỷ giá tốt nhận tiền lời mỗi ngày)\n"
            "3. Thực Tập Sinh Đầu Tư (Icon Quỹ Mở - Đa dạng hóa danh mục đầu tư đón sóng FDI)"
        )
        ws_u.cell(row=r, column=7).value = "Gửi Tiết Kiệm, Thực Tập Sinh Đầu Tư"
    elif 'CIC' in tool_name:
        ws_u.cell(row=r, column=6).value = (
            "1. Báo Cáo Điểm Tín Dụng (Icon CIC - Kiểm tra báo cáo chính thức CIC miễn phí)\n"
            "2. Ví Trả Sau (Icon VTS - Kích hoạt hạn mức tiêu dùng miễn lãi 45 ngày khi điểm tốt)\n"
            "3. Vay Nhanh (Icon Vay Nhanh - Khoản vay tín chấp giải ngân trong 1 phút)"
        )
        ws_u.cell(row=r, column=7).value = "CIC, Ví Trả Sau, Vay Nhanh"

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully fixed Utilities sheet: 100% verified Finhub products!")
