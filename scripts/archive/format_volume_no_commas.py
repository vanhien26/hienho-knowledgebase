import openpyxl

wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')

for sheetname in wb.sheetnames:
    ws = wb[sheetname]
    for r in range(1, ws.max_row + 1):
        for c in range(1, ws.max_column + 1):
            cell = ws.cell(row=r, column=c)
            # If the format contains comma or dot thousands separator
            if cell.number_format and ('#,##0' in cell.number_format or '#,#' in cell.number_format):
                cell.number_format = '0'
            
            # If value is integer, ensure it's int and format is '0'
            if isinstance(cell.value, int) and cell.number_format != '0' and cell.number_format != 'General':
                cell.number_format = '0'

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully updated all number formats to '0' (no commas, no dots) across all sheets!")
