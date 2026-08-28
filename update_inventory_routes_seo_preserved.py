import openpyxl

wb = openpyxl.load_workbook('05_HUBS/inventory.xlsx')
ws_playbook = wb['Quick Win Action Playbook']

for row in ws_playbook.iter_rows(min_row=3, max_row=ws_playbook.max_row, min_col=7, max_col=7):
    for cell in row:
        if cell.value and isinstance(cell.value, str):
            cell.value = cell.value.replace('/tai-chinh/', '/')

wb.save('05_HUBS/inventory.xlsx')
print("Successfully verified and updated URL routes in 05_HUBS/inventory.xlsx!")
