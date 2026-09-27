import openpyxl

wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')
ws_rd = wb['Roadmap']

# Append the mandatory conversion dock note to every tool row in Roadmap
for r in range(3, ws_rd.max_row + 1):
    val_scope = str(ws_rd.cell(row=r, column=5).value or '')
    val_hook = str(ws_rd.cell(row=r, column=6).value or '')
    
    if "Utility Conversion Dock" not in val_scope and "Khối Chốt Hạ Chuyển Đổi" not in val_scope:
        updated_scope = val_scope + "\n• Chuẩn UX bắt buộc: Tích hợp Khối Chốt Hạ Chuyển Đổi gồm Hộp MoMo Gợi Ý (AI) phản hồi động theo mức nhập + Lưới Icon Dịch Vụ MoMo (chi tiết xem sheet Utilities)."
        ws_rd.cell(row=r, column=5).value = updated_scope
        num_lines = max(updated_scope.count('\n') + 1, val_hook.count('\n') + 1)
        ws_rd.row_dimensions[r].height = max(65.0, num_lines * 18.0)

# Check Readme sheet structure
ws_readme = wb['Readme']
# Add row for Utilities in Readme index if there is a sheet list
found_sheet_list = False
for r in range(1, ws_readme.max_row + 1):
    v = str(ws_readme.cell(row=r, column=1).value or '')
    if 'Utilities' in v or 'Roadmap' in v:
        pass

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully synced Roadmap sheet with Utility Conversion Dock requirement!")
