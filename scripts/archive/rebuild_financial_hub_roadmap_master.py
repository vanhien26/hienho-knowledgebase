import os, glob, csv, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

folder = '/Users/hienhv/Downloads/Inventory/Financial'

def clean(val):
    val = val.strip()
    if val.startswith('='): val = val[1:]
    return val.strip('\"').strip()

def read_csv(fname):
    fpath = os.path.join(folder, fname)
    kws = {}
    if not os.path.exists(fpath):
        return kws
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        try: next(reader)
        except: pass
        for r in reader:
            if len(r) >= 2 and r[0].strip():
                kw = clean(r[0]).lower()
                try: v = int(clean(r[1]))
                except: v = 10
                v = 10 if v <= 0 else v
                kws[kw] = max(kws.get(kw, 0), v)
    return kws

# 34 Banks definition
bank_definitions = [
    ('Vietcombank', 'Vietcombank.csv', 'Ngân hàng TMCP Ngoại Thương Việt Nam', 'Big4 Nhà Nước', '/tai-chinh/ngan-hang/vietcombank', 'P0'),
    ('VietinBank', 'VietinBank.csv', 'Ngân hàng TMCP Công Thương Việt Nam', 'Big4 Nhà Nước', '/tai-chinh/ngan-hang/vietinbank', 'P0'),
    ('BIDV', 'BIDV.csv', 'Ngân hàng TMCP Đầu tư và Phát triển VN', 'Big4 Nhà Nước', '/tai-chinh/ngan-hang/bidv', 'P0'),
    ('Agribank', 'agribank.csv', 'Ngân hàng Nông nghiệp & PTNT Việt Nam', 'Big4 Nhà Nước', '/tai-chinh/ngan-hang/agribank', 'P0'),
    ('MBBank', 'mbbank.csv', 'Ngân hàng TMCP Quân Đội', 'TMCP Lớn', '/tai-chinh/ngan-hang/mbbank', 'P0'),
    ('Techcombank', 'Techcombank.csv', 'Ngân hàng TMCP Kỹ Thương Việt Nam', 'TMCP Lớn', '/tai-chinh/ngan-hang/techcombank', 'P0'),
    ('ACB', 'ACB.csv', 'Ngân hàng TMCP Á Châu', 'TMCP Lớn', '/tai-chinh/ngan-hang/acb', 'P0'),
    ('VPBank', 'vpbank.csv', 'Ngân hàng TMCP Việt Nam Thịnh Vượng', 'TMCP Lớn (Đối tác Tiết Kiệm MoMo)', '/tai-chinh/ngan-hang/vpbank', 'P0'),
    ('TPBank', 'tpbank.csv', 'Ngân hàng TMCP Tiên Phong', 'TMCP Lớn', '/tai-chinh/ngan-hang/tpbank', 'P0'),
    ('Sacombank', 'sacombank.csv', 'Ngân hàng TMCP Sài Gòn Thương Tín', 'TMCP Lớn', '/tai-chinh/ngan-hang/sacombank', 'P0'),
    ('HDBank', 'hd-bank.csv', 'Ngân hàng TMCP Phát triển TP.HCM', 'TMCP Lớn', '/tai-chinh/ngan-hang/hdbank', 'P1'),
    ('SHB', 'shb.csv', 'Ngân hàng TMCP Sài Gòn - Hà Nội', 'TMCP Lớn', '/tai-chinh/ngan-hang/shb', 'P1'),
    ('VIB', 'vib.csv', 'Ngân hàng TMCP Quốc Tế Việt Nam', 'TMCP Lớn', '/tai-chinh/ngan-hang/vib', 'P1'),
    ('MSB', 'MSB.csv', 'Ngân hàng TMCP Hàng Hải Việt Nam', 'TMCP Lớn', '/tai-chinh/ngan-hang/msb', 'P1'),
    ('OCB', 'ocb.csv', 'Ngân hàng TMCP Phương Đông', 'TMCP Lớn', '/tai-chinh/ngan-hang/ocb', 'P1'),
    ('LPBank', 'LPBank .csv', 'Ngân hàng TMCP Lộc Phát Việt Nam', 'TMCP Lớn', '/tai-chinh/ngan-hang/lpbank', 'P1'),
    ('Eximbank', 'Eximbank.csv', 'Ngân hàng TMCP Xuất Nhập Khẩu Việt Nam', 'TMCP Lớn', '/tai-chinh/ngan-hang/eximbank', 'P1'),
    ('SeABank', 'seabank.csv', 'Ngân hàng TMCP Đông Nam Á', 'TMCP Lớn', '/tai-chinh/ngan-hang/seabank', 'P1'),
    ('Bản Việt (BVBank)', 'ban-viet.csv', 'Ngân hàng TMCP Bản Việt', 'TMCP Lớn (Đối tác Tiết Kiệm MoMo)', '/tai-chinh/ngan-hang/bvbank', 'P0'),
    ('Nam A Bank', 'nam-a-bank.csv', 'Ngân hàng TMCP Nam Á', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/nam-a-bank', 'P1'),
    ('Bac A Bank', 'bac-a-bank.csv', 'Ngân hàng TMCP Bắc Á', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/bac-a-bank', 'P1'),
    ('VietBank', 'vietbank.csv', 'Ngân hàng TMCP Việt Nam Thương Tín', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/vietbank', 'P1'),
    ('KienlongBank', 'kien-long-bank.csv', 'Ngân hàng TMCP Kiên Long', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/kienlongbank', 'P2'),
    ('BaoViet Bank', 'bao-viet-bank.csv', 'Ngân hàng TMCP Bảo Việt', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/baovietbank', 'P2'),
    ('Saigonbank', 'saigonbank.csv', 'Ngân hàng TMCP Sài Gòn Công Thương', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/saigonbank', 'P2'),
    ('ABBank', 'ab-bank.csv', 'Ngân hàng TMCP An Bình', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/abbank', 'P2'),
    ('DongA Bank', 'donga bank.csv', 'Ngân hàng TMCP Đông Á', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/donga-bank', 'P2'),
    ('PVcomBank', 'pvcom bank.csv', 'Ngân hàng TMCP Đại Chúng Việt Nam', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/pvcombank', 'P2'),
    ('OceanBank', 'ocean-bank.csv', 'Ngân hàng Thương mại TNHH MTV Đại Dương', 'TM TNHH MTV', '/tai-chinh/ngan-hang/oceanbank', 'P2'),
    ('NCB', 'ncb.csv', 'Ngân hàng TMCP Quốc Dân', 'TMCP Đô Thị', '/tai-chinh/ngan-hang/ncb', 'P2'),
    ('SCB', 'scb.csv', 'Ngân hàng TMCP Sài Gòn', 'TMCP Kiểm soát đặc biệt', '/tai-chinh/ngan-hang/scb', 'P2'),
    ('Shinhan Bank', 'Shinhan Bank.csv', 'Ngân hàng TNHH MTV Shinhan Việt Nam', 'Ngân Hàng Ngoại (FDI)', '/tai-chinh/ngan-hang/shinhan-bank', 'P1'),
    ('Indovina Bank', 'Indovina Bank.csv', 'Ngân hàng TNHH Indovina (IVB)', 'Ngân Hàng Liên Doanh', '/tai-chinh/ngan-hang/indovina-bank', 'P2'),
    ('VRB', 'vrb.csv', 'Ngân hàng Liên doanh Việt - Nga', 'Ngân Hàng Liên Doanh', '/tai-chinh/ngan-hang/vrb', 'P2')
]

bank_data_rows = []
for name, fname, full_name, group, slug, prio in bank_definitions:
    kws = read_csv(fname)
    vol = sum(kws.values())
    cnt = len(kws)
    bank_data_rows.append({
        'name': name,
        'full_name': full_name,
        'vol': vol,
        'kws': cnt,
        'group': group,
        'slug': slug,
        'prio': prio
    })

# Sort banks by volume descending
bank_data_rows.sort(key=lambda x: x['vol'], reverse=True)

# Rebuild Excel file
wb = openpyxl.Workbook()
# remove default sheet
wb.remove(wb.active)

# Styling tokens
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(name='Arial', size=10, bold=True, color='FFFFFF')
section_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
section_font = Font(name='Arial', size=10.5, bold=True, color='1F4E78')
thin_side = Side(style='thin', color='64748B')
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

p1_fill = PatternFill(start_color="E2F0D9", end_color="E2F0D9", fill_type="solid") # Green
p2_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid") # Yellow
p3_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid") # Orange

status_done_fill = PatternFill(start_color="1E7E34", end_color="1E7E34", fill_type="solid")
status_done_font = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')
status_prog_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")
status_prog_font = Font(name='Arial', size=9.5, bold=True, color='B9770E')
status_plan_fill = PatternFill(start_color="1B4F72", end_color="1B4F72", fill_type="solid")
status_plan_font = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')

font_bold = Font(name='Arial', size=9.5, bold=True)
font_bold_blue = Font(name='Arial', size=9.5, bold=True, color='002060')
font_regular = Font(name='Arial', size=9.5)

# ==========================================
# 1. SHEET: Readme
# ==========================================
ws_rm = wb.create_sheet('Readme')
ws_rm.append(["HỆ THỐNG QUẢN TRỊ ROADMAP & DỮ LIỆU ĐỐI TÁC FINANCIAL MASTER HUB"])
ws_rm.merge_cells("A1:B1")
ws_rm.cell(row=1, column=1).fill = section_fill
ws_rm.cell(row=1, column=1).font = section_font
ws_rm.row_dimensions[1].height = 24.0

readme_notes = [
    ("Tên Dự Án", "Financial Master Hub (momo.vn/tai-chinh) & 24 Thị Trường Ngành"),
    ("Mục Tiêu", "Cổng Khám Phá & Ra Quyết Định Tài Chính Cá Nhân Toàn Diện (Pre-install Discovery & Decision Gateway)"),
    ("Quy Mô Toàn Ngành", "102,140,030 search/tháng (58,164 Unique Keywords) qua 24 Thị trường CreditTech"),
    ("Quy Chuẩn Đồng Bộ", "Kế thừa 100% dữ liệu chính thức từ 05_HUBS/inventory.xlsx và bộ 27 CSVs"),
    ("Cơ Chế Bảo Toàn SEO", "Giữ nguyên các URL gốc (/tiet-kiem-online, /vay-nhanh, /tinh-luong, /gia-vang), hợp nhất qua Master Hub /tai-chinh"),
    ("Lộ Trình Thực Thi", "3 Giai Đoạn (Phase 1: Tháng 8-9/2026, Phase 2: Tháng 10-11/2026, Phase 3: Tháng 12/2026 - Q1/2027)"),
    ("Danh Bạ 34 Ngân Hàng", "Phân tích chi tiết 34 ngân hàng đối tác với tổng Search Volume 17,658,980 lượt/tháng")
]
for k, v in readme_notes:
    ws_rm.append([k, v])
    r = ws_rm.max_row
    ws_rm.row_dimensions[r].height = 22.0
    ws_rm.cell(row=r, column=1).font = font_bold; ws_rm.cell(row=r, column=1).border = thin_border
    ws_rm.cell(row=r, column=2).font = font_regular; ws_rm.cell(row=r, column=2).border = thin_border

ws_rm.column_dimensions['A'].width = 25
ws_rm.column_dimensions['B'].width = 95

# ==========================================
# 2. SHEET: Roadmap (Exact Real Execution Roadmap)
# ==========================================
ws_rd = wb.create_sheet('Roadmap')
ws_rd.append(["LỘ TRÌNH TRIỂN KHAI TOÀN DIỆN CÁC DỰ ÁN FINANCIAL HUB (THỰC TẾ TRIỂN KHAI 2026 - 2027)"])
ws_rd.merge_cells("A1:E1")
ws_rd.cell(row=1, column=1).fill = section_fill
ws_rd.cell(row=1, column=1).font = section_font
ws_rd.row_dimensions[1].height = 24.0

rd_headers = ["Giai Đoạn (Phase)", "Thời Gian", "Tên Dự Án / Module Trọng Tâm", "Chi Tiết Triển Khai & Nhiệm Vụ Kỹ Thuật", "Trạng Thái"]
ws_rd.append(rd_headers)
for c_i in range(1, len(rd_headers) + 1):
    c = ws_rd.cell(row=2, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_rd.row_dimensions[2].height = 26.0

real_roadmap_rows = [
    ("Phase 1", "Tháng 8/2026", "Dự Án 1: Master Financial Hub",
     "Xây dựng trang cổng trung tâm, thiết kế Mega Menu 5 nhóm nhu cầu tài chính, thanh Trợ thủ đồng hành và các thẻ điều hướng sản phẩm.",
     "Done"),

    ("Phase 1", "Tháng 8/2026", "Dự Án 2: CIC, Tiết Kiệm",
     "Công cụ CIC Simulator và Nợ Xấu (tra cứu 339k volume).\nCông cụ tính lãi suất tiết kiệm cho TKO (Bản Việt, VPBank).",
     "Done"),

    ("Phase 1", "Tháng 8/2026", "Dự Án 3: Content Strategy & Blog Tài Chính",
     "Thiết lập quy trình tự động hóa xuất bản cẩm nang tài chính bằng AI độc lập trên MoSpark.",
     "In Progress"),

    ("Phase 1", "Tháng 8/2026", "Dự Án 4: Tra Cứu Giá Vàng Realtime",
     "Xây dựng bảng giá vàng realtime (SJC, PNJ, DOJI, 24K, 9999, Nhẫn trơn), biểu đồ lịch sử 7-30 ngày.",
     "Done"),

    ("Phase 1", "Tháng 9/2026", "Dự Án 5: Tính Lương & Thuế TNCN 2026",
     "Bộ công cụ tính lương Gross - Net (áp dụng luật thuế mới 2026) và cẩm nang tự quyết toán/hoàn thuế TNCN.",
     "In Progress"),

    ("Phase 1", "Tháng 9/2026", "Dự Án 7: Bộ Quy Đổi Ngoại Tệ & Tỷ Giá",
     "Bộ công cụ quy đổi tiền tệ tức thì giữa 20+ ngoại tệ (USD, JPY, EUR...) và bảng tỷ giá so sánh giữa các ngân hàng thương mại lớn.",
     "In Progress"),

    ("Phase 1", "Tháng 9/2026", "Dự Án 8: Thực Tập Sinh Đầu Tư (Chứng Khoán)",
     "Công cụ tra cứu, hướng dẫn và giả lập Đầu Tư Chứng Khoán dành cho người mới bắt đầu (F0), mua Quỹ mở SIP từ 10.000đ.",
     "Planned"),

    ("Phase 2", "Tháng 10/2026", "Dự Án 9: Bổ sung các công cụ tính toán tài chính",
     "Công cụ 'Có Tiền Đầu Tư Gì?' phân bổ tài sản Lump Sum (An toàn, Tăng trưởng, Mạo hiểm), Bộ giả lập Lãi kép tích lũy SIP và FIRE.",
     "Planned"),

    ("Phase 2", "Tháng 10/2026", "Dự Án 9: Trung Tâm Đầu Tư & Tích Sản FIRE",
     "Công cụ 'Có Tiền Đầu Tư Gì?' phân bổ tài sản Lump Sum (An toàn, Tăng trưởng, Mạo hiểm), Bộ giả lập Lãi kép tích lũy SIP và FIRE.",
     "Planned")
]

for p, t, n, d, s in real_roadmap_rows:
    ws_rd.append([p, t, n, d, s])
    r = ws_rd.max_row
    ws_rd.row_dimensions[r].height = 30.0 if '\n' in d else 24.0
    ws_rd.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_rd.cell(row=r, column=2).alignment = Alignment(horizontal='center', vertical='center')
    ws_rd.cell(row=r, column=3).alignment = Alignment(horizontal='left', vertical='center'); ws_rd.cell(row=r, column=3).font = font_bold
    ws_rd.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_rd.cell(row=r, column=5).alignment = Alignment(horizontal='center', vertical='center')

    if "Phase 1" in p: ws_rd.cell(row=r, column=1).fill = p1_fill
    elif "Phase 2" in p: ws_rd.cell(row=r, column=1).fill = p2_fill

    c_st = ws_rd.cell(row=r, column=5)
    if s == "Done": c_st.fill = status_done_fill; c_st.font = status_done_font
    elif s == "In Progress": c_st.fill = status_prog_fill; c_st.font = status_prog_font
    elif s == "Planned": c_st.fill = status_plan_fill; c_st.font = status_plan_font

    for c_i in range(1, 6): ws_rd.cell(row=r, column=c_i).border = thin_border

ws_rd.column_dimensions['A'].width = 16
ws_rd.column_dimensions['B'].width = 18
ws_rd.column_dimensions['C'].width = 40
ws_rd.column_dimensions['D'].width = 75
ws_rd.column_dimensions['E'].width = 18

# ==========================================
# 3. SHEET: Partner Banks Directory (34 Banks Full Listing)
# ==========================================
ws_bk = wb.create_sheet('Partner Banks Directory')
ws_bk.append(["DANH BẠ 34 NGÂN HÀNG ĐỐI TÁC & DUNG LƯỢNG TÌM KIẾM (SEARCH VOLUME TỪ TỆP NGUYÊN BẢN NGAN-HANG CSVs)"])
ws_bk.merge_cells("A1:H1")
ws_bk.cell(row=1, column=1).fill = section_fill
ws_bk.cell(row=1, column=1).font = section_font
ws_bk.row_dimensions[1].height = 24.0

bk_headers = [
    "STT", "Tên Thương Hiệu", "Tên Đầy Đủ Ngân Hàng", "Search Volume / Tháng",
    "Tỷ Trọng Trong Khối Bank (%)", "Số Từ Khóa SEO", "Nhóm Phân Loại", "URL Route Chuẩn Hóa", "Mức Độ Ưu Tiên"
]
ws_bk.append(bk_headers)
for c_i in range(1, len(bk_headers) + 1):
    c = ws_bk.cell(row=2, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_bk.row_dimensions[2].height = 26.0

total_bank_vol_sum = sum(b['vol'] for b in bank_data_rows)
total_bank_kws_sum = sum(b['kws'] for b in bank_data_rows)

for idx, b in enumerate(bank_data_rows, start=1):
    pct = f"{(b['vol'] / total_bank_vol_sum)*100:.2f}%" if total_bank_vol_sum > 0 else "0.00%"
    ws_bk.append([idx, b['name'], b['full_name'], b['vol'], pct, b['kws'], b['group'], b['slug'], b['prio']])
    r = ws_bk.max_row
    ws_bk.row_dimensions[r].height = 22.0
    ws_bk.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_bk.cell(row=r, column=2).alignment = Alignment(horizontal='left', vertical='center'); ws_bk.cell(row=r, column=2).font = font_bold
    ws_bk.cell(row=r, column=3).alignment = Alignment(horizontal='left', vertical='center')
    ws_bk.cell(row=r, column=4).alignment = Alignment(horizontal='right', vertical='center'); ws_bk.cell(row=r, column=4).font = font_bold_blue; ws_bk.cell(row=r, column=4).number_format = '#,##0'
    ws_bk.cell(row=r, column=5).alignment = Alignment(horizontal='center', vertical='center')
    ws_bk.cell(row=r, column=6).alignment = Alignment(horizontal='right', vertical='center'); ws_bk.cell(row=r, column=6).number_format = '#,##0'
    ws_bk.cell(row=r, column=7).alignment = Alignment(horizontal='left', vertical='center')
    ws_bk.cell(row=r, column=8).alignment = Alignment(horizontal='left', vertical='center')
    ws_bk.cell(row=r, column=9).alignment = Alignment(horizontal='center', vertical='center'); ws_bk.cell(row=r, column=9).font = font_bold

    prio = b['prio']
    if prio == 'P0': ws_bk.cell(row=r, column=9).font = Font(name='Arial', size=9.5, bold=True, color='B91C1C')
    elif prio == 'P1': ws_bk.cell(row=r, column=9).font = Font(name='Arial', size=9.5, bold=True, color='1D4ED8')

    for c_i in range(1, 10): ws_bk.cell(row=r, column=c_i).border = thin_border

# Grand Total Row for Banks
ws_bk.append(["TỔNG CỘNG 34 NGÂN HÀNG", "", "", total_bank_vol_sum, "100.00%", total_bank_kws_sum, "Toàn Bộ Hệ Thống", "34 Dynamic Routes", "Master SSOT"])
r_tot = ws_bk.max_row
ws_bk.merge_cells(f"A{r_tot}:C{r_tot}")
ws_bk.row_dimensions[r_tot].height = 24.0
ws_bk.cell(row=r_tot, column=1).fill = section_fill; ws_bk.cell(row=r_tot, column=1).font = section_font
ws_bk.cell(row=r_tot, column=1).alignment = Alignment(horizontal='center', vertical='center')
for c_i in range(1, 10):
    c = ws_bk.cell(row=r_tot, column=c_i)
    c.fill = section_fill; c.font = font_bold; c.border = thin_border
ws_bk.cell(row=r_tot, column=4).number_format = '#,##0'
ws_bk.cell(row=r_tot, column=6).number_format = '#,##0'

ws_bk.column_dimensions['A'].width = 8
ws_bk.column_dimensions['B'].width = 22
ws_bk.column_dimensions['C'].width = 44
ws_bk.column_dimensions['D'].width = 22
ws_bk.column_dimensions['E'].width = 18
ws_bk.column_dimensions['F'].width = 16
ws_bk.column_dimensions['G'].width = 30
ws_bk.column_dimensions['H'].width = 35
ws_bk.column_dimensions['I'].width = 14

# ==========================================
# 4. SHEET: Consolidated Financial Markets (24 Canonical Markets from inventory.xlsx)
# ==========================================
ws_cm = wb.create_sheet('Consolidated Financial Markets')
ws_cm.append(["TỔNG HỢP 24 THỊ TRƯỜNG DỊCH VỤ TÀI CHÍNH CREDITTECH (KẾ THỪA CHÍNH THỨC TỪ INVENTORY.XLSX)"])
ws_cm.merge_cells("A1:G1")
ws_cm.cell(row=1, column=1).fill = section_fill
ws_cm.cell(row=1, column=1).font = section_font
ws_cm.row_dimensions[1].height = 24.0

cm_headers = ["STT", "Thị Trường / Dịch Vụ", "Trụ Cột Nghiệp Vụ", "Nguồn Dữ Liệu Tệp", "Search Volume / Tháng", "Tỷ Trọng Ngành (%)", "Định Vị & Ưu Tiên"]
ws_cm.append(cm_headers)
for c_i in range(1, len(cm_headers) + 1):
    c = ws_cm.cell(row=2, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_cm.row_dimensions[2].height = 26.0

# 24 Canonical markets from inventory.xlsx
markets_24 = [
    (1, "Giá Vàng", "Đầu Tư & Tích Sản", "gia-vang.csv", 78879270, "Big Bet (P1)"),
    (2, "Tỷ Giá", "Tiền Tệ & Ngoại Hối", "ty-gia.csv", 8516910, "Big Bet (P1)"),
    (3, "Ngân Hàng", "Ngân Hàng & Thẻ", "ngan-hang.csv + 34 banks", 6629420, "Big Bet / Programmatic (P0)"),
    (4, "Chứng Khoán", "Đầu Tư & Tích Sản", "chung-khoan.csv", 3026340, "Big Bet (P1)"),
    (5, "Lãi Suất", "Tiết Kiệm & Lãi Suất", "lai-suat.csv", 1246620, "Big Bet (P1)"),
    (6, "Thuế (TNCN)", "Thu Nhập & Thuế", "thue.csv", 1159450, "Top Quick Win (P0)"),
    (7, "Cổ Phiếu", "Đầu Tư & Tích Sản", "co-phieu.csv", 1077540, "Big Bet (P1)"),
    (8, "Ngoại Tệ", "Tiền Tệ & Ngoại Hối", "ngoai-te.csv", 959340, "Standard Feature (P2)"),
    (9, "Crypto", "Tài Sản Số", "crypto.csv", 469420, "Low Priority (P2)"),
    (10, "Thẻ Tín Dụng", "Ngân Hàng & Thẻ", "the-tin-dung.csv", 394590, "Big Bet (P1)"),
    (11, "Vay Tín Chấp", "Tín Dụng & Vay Vốn", "vay-tin-chap.csv", 389820, "Big Bet (P1)"),
    (12, "CIC (Điểm tín dụng)", "Tín Dụng & Vay Vốn", "cic.csv + diem-tin-dung.csv", 339000, "Top Quick Win #1 (P0)"),
    (13, "Thẻ Visa", "Ngân Hàng & Thẻ", "the-visa.csv", 243110, "Core Driver (P1)"),
    (14, "Gửi Tiết Kiệm", "Tiết Kiệm & Lãi Suất", "gui-tiet-kiem.csv", 230110, "High-Impact Quick Win (P0)"),
    (15, "Tính Lương", "Thu Nhập & Thuế", "tinh-luong.csv", 190690, "Top Quick Win (P0)"),
    (16, "Vay Thế Chấp", "Tín Dụng & Vay Vốn", "vay-the-chap.csv", 125960, "Core Driver (P1)"),
    (17, "Trả Góp", "Tín Dụng & Vay Vốn", "tra-gop.csv", 116390, "Top Quick Win (P0)"),
    (18, "Tiền Số & Tiền Ảo", "Tài Sản Số", "tien-so.csv + tien-ao.csv", 104500, "Low Priority (P2)"),
    (19, "Trái Phiếu", "Đầu Tư & Tích Sản", "trai-phieu.csv", 79580, "Standard Feature (P2)"),
    (20, "Thẻ Ghi Nợ (ATM)", "Ngân Hàng & Thẻ", "the-ghi-no.csv", 73290, "Top Quick Win (P0)"),
    (21, "Nợ Xấu", "Tín Dụng & Vay Vốn", "no-xau.csv", 59890, "Top Quick Win (P0)"),
    (22, "Napas", "Ngân Hàng & Thẻ", "napas.csv", 51100, "Top Quick Win (P0)"),
    (23, "Chứng Chỉ Quỹ", "Đầu Tư & Tích Sản", "chung-chi-quy.csv", 25790, "Top Quick Win (P0)"),
    (24, "Mastercard", "Ngân Hàng & Thẻ", "masteer-card.csv", 18630, "Core Driver (P1)")
]

grand_total_mkt = 102140030

for stt, name, pillar, src, vol, prio_str in markets_24:
    pct = f"{(vol / grand_total_mkt)*100:.2f}%"
    ws_cm.append([stt, name, pillar, src, vol, pct, prio_str])
    r = ws_cm.max_row
    ws_cm.row_dimensions[r].height = 22.0
    ws_cm.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_cm.cell(row=r, column=2).alignment = Alignment(horizontal='left', vertical='center'); ws_cm.cell(row=r, column=2).font = font_bold
    ws_cm.cell(row=r, column=3).alignment = Alignment(horizontal='left', vertical='center')
    ws_cm.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center')
    ws_cm.cell(row=r, column=5).alignment = Alignment(horizontal='right', vertical='center'); ws_cm.cell(row=r, column=5).font = font_bold_blue; ws_cm.cell(row=r, column=5).number_format = '#,##0'
    ws_cm.cell(row=r, column=6).alignment = Alignment(horizontal='center', vertical='center')
    ws_cm.cell(row=r, column=7).alignment = Alignment(horizontal='center', vertical='center'); ws_cm.cell(row=r, column=7).font = font_bold

    if "P0" in prio_str: ws_cm.cell(row=r, column=7).font = Font(name='Arial', size=9.5, bold=True, color='B91C1C')
    elif "P1" in prio_str: ws_cm.cell(row=r, column=7).font = Font(name='Arial', size=9.5, bold=True, color='1D4ED8')

    for c_i in range(1, 8): ws_cm.cell(row=r, column=c_i).border = thin_border

# Grand Total Row
ws_cm.append(["TỔNG CREDITTECH (DEDUPLICATED)", "", "", "27 Tệp Gốc Khử Trùng", grand_total_mkt, "100.00%", "58,164 Unique Keywords"])
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
ws_cm.column_dimensions['B'].width = 25
ws_cm.column_dimensions['C'].width = 25
ws_cm.column_dimensions['D'].width = 30
ws_cm.column_dimensions['E'].width = 24
ws_cm.column_dimensions['F'].width = 20
ws_cm.column_dimensions['G'].width = 28

# ==========================================
# 5. SHEET: Market Difficulty & Quick Wins
# ==========================================
ws_qw = wb.create_sheet('Market Difficulty & Quick Wins')
ws_qw.append(["ĐÁNH GIÁ 8 TIÊU CHÍ ĐỘ KHÓ & CHỈ SỐ QUICK WINS CỦA 24 THỊ TRƯỜNG TÀI CHÍNH"])
ws_qw.merge_cells("A1:M1")
ws_qw.cell(row=1, column=1).fill = section_fill
ws_qw.cell(row=1, column=1).font = section_font
ws_qw.row_dimensions[1].height = 24.0

qw_headers = [
    "STT", "Thị Trường / Dịch Vụ", "Search Volume", "DR Đối Thủ (20%)", "YMYL (15%)", "Tool Intent (15%)",
    "QDF Realtime (15%)", "Zero-Click (10%)", "Topical Depth (10%)", "Brand Bias (10%)", "UX / Speed (5%)",
    "Tổng Điểm Độ Khó (1-10)", "Chỉ Số Quick Win (QW Index)"
]
ws_qw.append(qw_headers)
for c_i in range(1, len(qw_headers) + 1):
    c = ws_qw.cell(row=2, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_qw.row_dimensions[2].height = 26.0

diff_data = [
    (1, "CIC (Điểm tín dụng)", 339000, 4.0, 5.0, 5.0, 4.0, 4.0, 5.0, 5.0, 5.0, 4.65, 16.6),
    (2, "Gửi Tiết Kiệm", 230110, 5.0, 7.0, 7.0, 6.0, 5.0, 5.0, 5.0, 5.0, 5.67, 14.5),
    (3, "Napas", 51100, 4.0, 4.0, 4.0, 4.0, 5.0, 5.0, 5.0, 4.0, 4.33, 14.3),
    (4, "Thẻ Ghi Nợ (ATM)", 73290, 4.0, 4.0, 4.0, 4.0, 5.0, 6.0, 5.0, 4.0, 4.50, 13.8),
    (5, "Thuế (TNCN)", 1159450, 5.0, 6.0, 7.0, 6.0, 6.0, 6.0, 6.0, 5.0, 5.80, 13.8),
    (6, "Trả Góp", 116390, 5.0, 5.0, 6.0, 5.0, 5.0, 6.0, 5.0, 5.0, 5.23, 13.8),
    (7, "Tính Lương", 190690, 4.0, 5.0, 7.0, 5.0, 5.0, 6.0, 5.0, 5.0, 5.13, 13.1),
    (8, "Nợ Xấu", 59890, 4.0, 6.0, 5.0, 4.0, 5.0, 6.0, 5.0, 4.0, 4.90, 12.7),
    (9, "Chứng Chỉ Quỹ", 25790, 5.0, 5.0, 5.0, 4.0, 5.0, 6.0, 5.0, 5.0, 5.00, 12.6),
    (10, "Thẻ Visa", 243110, 5.0, 5.0, 5.0, 5.0, 5.0, 6.0, 6.0, 5.0, 5.27, 13.5),
    (11, "Thẻ Tín Dụng", 394590, 6.0, 7.0, 7.0, 6.0, 6.0, 7.0, 7.0, 6.0, 6.38, 12.9),
    (12, "Lãi Suất", 1246620, 6.0, 7.0, 8.0, 8.0, 6.0, 7.0, 6.0, 6.0, 6.78, 12.7),
    (13, "Vay Tín Chấp", 389820, 6.0, 7.0, 7.0, 7.0, 6.0, 7.0, 7.0, 6.0, 6.65, 12.3),
    (14, "Chứng Khoán", 3026340, 7.0, 7.0, 8.0, 8.0, 6.0, 8.0, 7.0, 7.0, 7.28, 11.8),
    (15, "Ngân Hàng", 6629420, 6.0, 6.0, 6.0, 6.0, 6.0, 7.0, 7.0, 5.0, 6.08, 14.8),
    (16, "Cổ Phiếu", 1077540, 7.0, 7.0, 7.0, 8.0, 6.0, 8.0, 7.0, 7.0, 7.13, 11.2),
    (17, "Vay Thế Chấp", 125960, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.00, 11.2),
    (18, "Ngoại Tệ", 959340, 6.0, 6.0, 7.0, 7.0, 6.0, 7.0, 6.0, 6.0, 6.33, 11.1),
    (19, "Mastercard", 18630, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 4.85, 10.9),
    (20, "Giá Vàng", 78879270, 8.0, 8.0, 8.0, 9.0, 7.0, 8.0, 8.0, 7.0, 7.95, 10.6),
    (21, "Tỷ Giá", 8516910, 7.0, 7.0, 8.0, 9.0, 7.0, 8.0, 8.0, 7.0, 7.65, 10.3),
    (22, "Trái Phiếu", 79580, 5.0, 6.0, 6.0, 6.0, 5.0, 6.0, 6.0, 5.0, 5.65, 9.0),
    (23, "Crypto", 469420, 6.0, 6.0, 6.0, 7.0, 5.0, 6.0, 6.0, 5.0, 5.90, 6.4),
    (24, "Tiền Số & Tiền Ảo", 104500, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.03, 6.0)
]

for item in diff_data:
    ws_qw.append(list(item))
    r = ws_qw.max_row
    ws_qw.row_dimensions[r].height = 22.0
    ws_qw.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_qw.cell(row=r, column=2).alignment = Alignment(horizontal='left', vertical='center'); ws_qw.cell(row=r, column=2).font = font_bold
    ws_qw.cell(row=r, column=3).alignment = Alignment(horizontal='right', vertical='center'); ws_qw.cell(row=r, column=3).font = font_bold_blue; ws_qw.cell(row=r, column=3).number_format = '#,##0'
    for c_i in range(4, 12):
        ws_qw.cell(row=r, column=c_i).alignment = Alignment(horizontal='center', vertical='center')
    ws_qw.cell(row=r, column=12).alignment = Alignment(horizontal='center', vertical='center'); ws_qw.cell(row=r, column=12).font = font_bold
    ws_qw.cell(row=r, column=13).alignment = Alignment(horizontal='center', vertical='center'); ws_qw.cell(row=r, column=13).font = font_bold

    qw_val = item[12]
    if qw_val >= 13.0:
        ws_qw.cell(row=r, column=13).fill = p1_fill
        ws_qw.cell(row=r, column=13).font = Font(name='Arial', size=9.5, bold=True, color='15803D')

    for c_i in range(1, 14): ws_qw.cell(row=r, column=c_i).border = thin_border

for idx, w in enumerate([6, 24, 18, 16, 14, 16, 16, 15, 16, 15, 14, 22, 22], start=1):
    ws_qw.column_dimensions[get_column_letter(idx)].width = w

# Save rebuilt master roadmap
wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully rebuilt 05_HUBS/financial-hub-roadmap.xlsx with complete 34 Partner Banks directory and 100% synchronization!")
