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

p0_font = Font(name='Arial', size=9.5, bold=True, color='B91C1C')
p1_font = Font(name='Arial', size=9.5, bold=True, color='1D4ED8')
p2_font = Font(name='Arial', size=9.5, bold=False, color='475569')

font_bold = Font(name='Arial', size=9.5, bold=True)
font_bold_blue = Font(name='Arial', size=9.5, bold=True, color='002060')
font_regular = Font(name='Arial', size=9.5)

# Complete 31 Financial Markets across FS (CreditTech + Điểm Tín Dụng + Thuế/BHXH + InsurTech)
full_financial_markets = [
    # STT, Market, UseCase/Pillar, Source, Vol, Position/Prio
    (1, "Giá Vàng", "Đầu Tư & Tích Sản", "gia-vang.csv", 78879270, "Big Bet (P1)"),
    (2, "Ngân Hàng", "Ngân Hàng & Thẻ", "ngan-hang.csv + 34 banks", 6629420, "Big Bet / Programmatic (P0)"),
    (3, "Tỷ Giá", "Tiền Tệ & Ngoại Hối", "ty-gia.csv", 8516910, "Big Bet (P1)"),
    (4, "Mã Số Thuế", "Thu Nhập & Thuế", "thue.csv", 3903480, "Big Bet (P1)"),
    (5, "Chứng Khoán", "Đầu Tư & Tích Sản", "chung-khoan.csv", 3026340, "Big Bet (P1)"),
    (6, "Lãi Suất", "Tiết Kiệm & Lãi Suất", "lai-suat.csv", 1246620, "Big Bet (P1)"),
    (7, "Thuế (TNCN)", "Thu Nhập & Thuế", "thue.csv", 1159450, "Top Quick Win (P0)"),
    (8, "Cổ Phiếu", "Đầu Tư & Tích Sản", "co-phieu.csv", 1077540, "Big Bet (P1)"),
    (9, "Ngoại Tệ", "Tiền Tệ & Ngoại Hối", "ngoai-te.csv", 959340, "Standard Feature (P2)"),
    (10, "Crypto", "Tài Sản Số", "crypto.csv", 469420, "Low Priority (P2)"),
    (11, "Bảo Hiểm Xã Hội", "Thu Nhập & An Sinh Xã Hội", "bao-hiem-xa-hoi.csv", 441060, "Top Quick Win (P0)"),
    (12, "Thẻ Tín Dụng", "Ngân Hàng & Thẻ", "the-tin-dung.csv", 394590, "Big Bet (P1)"),
    (13, "Vay Tín Chấp (Vay Nhanh)", "Tín Dụng & Vay Vốn", "vay-tin-chap.csv", 389820, "Big Bet (P1)"),
    (14, "CIC (Điểm Tín Dụng)", "Tín Dụng & Sức Khỏe Tín Dụng", "cic.csv + diem-tin-dung.csv", 339000, "Top Quick Win #1 (P0)"),
    (15, "Thẻ Visa", "Ngân Hàng & Thẻ", "the-visa.csv", 243110, "Core Driver (P1)"),
    (16, "Gửi Tiết Kiệm", "Tiết Kiệm & Lãi Suất", "gui-tiet-kiem.csv", 230110, "High-Impact Quick Win (P0)"),
    (17, "Tính Lương", "Thu Nhập & Thuế", "tinh-luong.csv", 190690, "Top Quick Win (P0)"),
    (18, "Bảo Hiểm Y Tế", "Bảo Hiểm (InsurTech)", "bao-hiem-y-te.csv", 188720, "Core Driver (P1)"),
    (19, "Vay Thế Chấp (Mua Nhà)", "Tín Dụng & Vay Vốn", "vay-the-chap.csv", 125960, "Core Driver (P1)"),
    (20, "Trả Góp (Ví Trả Sau)", "Tín Dụng & Vay Vốn", "tra-gop.csv", 116390, "Top Quick Win (P0)"),
    (21, "Bảo Hiểm Xe Máy", "Bảo Hiểm (InsurTech)", "bao-hiem-xe-may.csv", 116320, "Top Quick Win (P0)"),
    (22, "Tiền Số & Tiền Ảo", "Tài Sản Số", "tien-so.csv + tien-ao.csv", 104500, "Low Priority (P2)"),
    (23, "Trái Phiếu", "Đầu Tư & Tích Sản", "trai-phieu.csv", 79580, "Standard Feature (P2)"),
    (24, "Thẻ Ghi Nợ (ATM)", "Ngân Hàng & Thẻ", "the-ghi-no.csv", 73290, "Top Quick Win (P0)"),
    (25, "Nợ Xấu", "Tín Dụng & Sức Khỏe Tín Dụng", "no-xau.csv", 59890, "Top Quick Win (P0)"),
    (26, "Bảo Hiểm Ô Tô", "Bảo Hiểm (InsurTech)", "bao-hiem-o-to.csv", 54590, "Core Driver (P1)"),
    (27, "Napas", "Ngân Hàng & Thẻ", "napas.csv", 51100, "Top Quick Win (P0)"),
    (28, "Bảo Hiểm Sức Khỏe +", "Bảo Hiểm (InsurTech)", "bao-hiem-suc-khoe.csv", 37930, "Top Quick Win (P0)"),
    (29, "Chứng Chỉ Quỹ", "Đầu Tư & Tích Sản", "chung-chi-quy.csv", 25790, "Top Quick Win (P0)"),
    (30, "Mastercard", "Ngân Hàng & Thẻ", "masteer-card.csv", 18630, "Core Driver (P1)"),
    (31, "Bảo Hiểm Du Lịch & Phí BH", "Bảo Hiểm (InsurTech)", "bao-hiem-du-lich.csv", 16600, "Top Quick Win (P0)")
]

total_all_fs_vol = sum(m[4] for m in full_financial_markets)

if 'Consolidated Financial Markets' in wb.sheetnames:
    del wb['Consolidated Financial Markets']

ws_cm = wb.create_sheet('Consolidated Financial Markets', index=3)
ws_cm.append(["TỔNG HỢP TOÀN DIỆN CÁC THỊ TRƯỜNG DỊCH VỤ TÀI CHÍNH FS (ĐẦY ĐỦ TỪ INVENTORY.XLSX: CREDITTECH + THUẾ/BHXH + INSURTECH)"])
ws_cm.merge_cells("A1:G1")
ws_cm.cell(row=1, column=1).fill = section_fill
ws_cm.cell(row=1, column=1).font = section_font
ws_cm.row_dimensions[1].height = 24.0

cm_headers = ["STT", "Thị Trường / Dịch Vụ", "Khối Nghiệp Vụ (Use Case)", "Nguồn Dữ Liệu Tệp", "Search Volume / Tháng", "Tỷ Trọng Ngành (%)", "Định Vị & Ưu Tiên"]
ws_cm.append(cm_headers)
for c_i in range(1, len(cm_headers) + 1):
    c = ws_cm.cell(row=2, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_cm.row_dimensions[2].height = 26.0

for stt, name, pillar, src, vol, prio_str in full_financial_markets:
    pct = f"{(vol / total_all_fs_vol)*100:.2f}%"
    ws_cm.append([stt, name, pillar, src, vol, pct, prio_str])
    r = ws_cm.max_row
    ws_cm.row_dimensions[r].height = 22.0
    ws_cm.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_cm.cell(row=r, column=2).alignment = Alignment(horizontal='left', vertical='center'); ws_cm.cell(row=r, column=2).font = font_bold
    ws_cm.cell(row=r, column=3).alignment = Alignment(horizontal='left', vertical='center')
    ws_cm.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center')
    ws_cm.cell(row=r, column=5).alignment = Alignment(horizontal='right', vertical='center'); ws_cm.cell(row=r, column=5).font = font_bold_blue; ws_cm.cell(row=r, column=5).number_format = '#,##0'
    ws_cm.cell(row=r, column=6).alignment = Alignment(horizontal='center', vertical='center')
    ws_cm.cell(row=r, column=7).alignment = Alignment(horizontal='center', vertical='center')

    if "P0" in prio_str: ws_cm.cell(row=r, column=7).font = p0_font
    elif "P1" in prio_str: ws_cm.cell(row=r, column=7).font = p1_font
    else: ws_cm.cell(row=r, column=7).font = p2_font

    for c_i in range(1, 8): ws_cm.cell(row=r, column=c_i).border = thin_border

# Grand Total Row
ws_cm.append(["TỔNG CỘNG TOÀN BỘ FINANCIAL SERVICES (FS)", "", "", "Toàn Bộ Khối Tài Chính (CreditTech + InsurTech + An Sinh)", total_all_fs_vol, "100.00%", "31 Thị Trường Chuẩn Hóa"])
r_tot = ws_cm.max_row
ws_cm.merge_cells(f"A{r_tot}:C{r_tot}")
ws_cm.row_dimensions[r_tot].height = 24.0
ws_cm.cell(row=r_tot, column=1).fill = section_fill; ws_cm.cell(row=r_tot, column=1).font = section_font
ws_cm.cell(row=r_tot, column=1).alignment = Alignment(horizontal='center', vertical='center')
for c_i in range(1, 8):
    c = ws_cm.cell(row=r_tot, column=c_i)
    c.fill = section_fill; c.font = font_bold; c.border = thin_border
ws_cm.cell(row=r_tot, column=5).number_format = '#,##0'

ws_cm.column_dimensions['A'].width = 8
ws_cm.column_dimensions['B'].width = 30
ws_cm.column_dimensions['C'].width = 30
ws_cm.column_dimensions['D'].width = 32
ws_cm.column_dimensions['E'].width = 24
ws_cm.column_dimensions['F'].width = 20
ws_cm.column_dimensions['G'].width = 28

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print(f"Successfully updated Consolidated Financial Markets in financial-hub-roadmap.xlsx with ALL 31 financial markets (Total Vol: {total_all_fs_vol:,d})!")
