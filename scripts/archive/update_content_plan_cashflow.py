import openpyxl

wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')
ws_cp = wb['Content Plan']

for r in range(3, ws_cp.max_row + 1):
    val3 = str(ws_cp.cell(row=r, column=3).value or '')
    if 'Thưởng Tết' in val3:
        ws_cp.cell(row=r, column=2).value = "Dòng Tiền & Tiêu Dùng"
        ws_cp.cell(row=r, column=3).value = "Cách Quản Lý Dòng Tiền Cá Nhân Hàng Tháng & Tối Ưu Tiền Nhàn Rỗi"
        ws_cp.cell(row=r, column=4).value = "quản lý dòng tiền cá nhân"
        ws_cp.cell(row=r, column=5).value = 14800
        ws_cp.cell(row=r, column=5).number_format = '0'
        ws_cp.cell(row=r, column=6).value = "Cẩm Nang Quản Lý Tài Chính"
        ws_cp.cell(row=r, column=7).value = "/tai-chinh/quan-ly-dong-tien-ca-nhan"
        ws_cp.cell(row=r, column=8).value = "Mở Túi Thần Tài Sinh Lời Hàng Ngày"
        print(f"Updated Content Plan Row {r} to Cash Flow & Spending management article.")
        break

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully updated Content Plan to eliminate Thưởng Tết and focus on Cash Flow!")
