import openpyxl

wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')
ws_rd = wb['Roadmap']

for r in range(3, ws_rd.max_row + 1):
    feat_name = str(ws_rd.cell(row=r, column=4).value or '').strip()
    if 'Công Cụ Tài Chính Cá Nhân' in feat_name:
        ws_rd.cell(row=r, column=3).value = "Dòng Tiền & Tiêu Dùng"
        ws_rd.cell(row=r, column=4).value = "Quản Lý Dòng Tiền & Tiêu Dùng"
        ws_rd.cell(row=r, column=5).value = (
            "• Bộ Tối Ưu Hóa Dòng Tiền Hàng Tháng (Cash Flow Optimizer): Nhập thu nhập và danh mục chi tiêu cố định/biến đổi ➔ Xác định chính xác Dòng Tiền Tự Do (Free Cash Flow) và số tiền nhàn rỗi có thể sinh lời mỗi ngày.\n"
            "• Bộ Giả Lập Quỹ Dự Phòng Khẩn Cấp (Emergency Fund Planner): Tính toán số vốn dự phòng an toàn (3 - 6 tháng sinh hoạt phí thiết yếu), đo lường chỉ số an toàn tài chính trước khi mang tiền đi đầu tư.\n"
            "• Bộ Kiểm Soát Hạn Mức Tiêu Dùng & Chi Phí Sinh Hoạt (Spending Budget Tracker): Giả lập hạn mức chi tiêu tối đa theo ngày/tuần, cảnh báo rủi ro bội chi và gợi ý cơ chế bóc tách tiền sinh hoạt."
        )
        ws_rd.cell(row=r, column=6).value = (
            "Dòng tiền nhàn rỗi ➔ Tự động trích tiền vào Túi Thần Tài nhận lời mỗi ngày; Dòng tiền tiêu dùng ➔ Mở Hũ Chi Tiêu MoMo và cài đặt Hạn Mức Thanh Toán linh hoạt."
        )
        ws_rd.row_dimensions[r].height = 65.0

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully updated Row 11: Replaced salary/bonus with Cash Flow & Consumption/Spending Management!")
