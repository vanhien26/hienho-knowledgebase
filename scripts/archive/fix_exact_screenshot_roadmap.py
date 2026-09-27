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

p1_fill = PatternFill(start_color="E2F0D9", end_color="E2F0D9", fill_type="solid") # Green
p2_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid") # Light Blue

status_done_fill = PatternFill(start_color="1E7E34", end_color="1E7E34", fill_type="solid") # Dark Green
status_done_font = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')

status_prog_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid") # Orange/Yellow
status_prog_font = Font(name='Arial', size=9.5, bold=True, color='B9770E')

status_plan_fill = PatternFill(start_color="1B4F72", end_color="1B4F72", fill_type="solid") # Dark Blue
status_plan_font = Font(name='Arial', size=9.5, bold=True, color='FFFFFF')

# Exact rows strictly matching the screenshot media_1788140063121.png
exact_screenshot_rows = [
    ("Phase 1", "Tháng 8/2026", "Dự Án 1: Master Financial Hub",
     "Xây dựng trang cổng trung tâm, thiết kế Mega Menu 5 nhóm nhu cầu tài chính, thanh Trợ thủ đồng hành và các thẻ điều hướng sản phẩm.",
     "Done"),

    ("Phase 1", "Tháng 8/2026", "Dự Án 2: CIC, Tiết Kiệm",
     "Công cụ CIC Simulator và Nợ Xấu.\nCông cụ tiết lãi suất tiết kiệm cho TKO",
     "Done"),

    ("Phase 1", "Tháng 8/2026", "Dự Án 3: Content Strategy & Blog Tài Chính",
     "Thiết lập quy trình tự động hóa xuất bản cẩm nang tài chính bằng AI độc lập trên MoSpark",
     "In Progress"),

    ("Phase 1", "Tháng 8/2026", "Dự Án 4: Tra Cứu Giá Vàng Realtime",
     "Xây dựng bảng giá vàng realtime (SJC, PNJ, DOJI, 24K, 9999, Nhẫn trơn), biểu đồ lịch sử 7-30 ngày",
     "Done"),

    ("Phase 1", "Tháng 9/2026", "Dự Án 5: Tính Lương & Thuế TNCN 2026",
     "Bộ công cụ quy đổi tiền tệ tức thì giữa 20+ ngoại tệ (USD, JPY, EUR...) và bảng tỷ giá so sánh giữa các ngân hàng thương mại lớn.",
     "In Progress"),

    ("Phase 1", "Tháng 9/2026", "Dự Án 7: Bộ Quy Đổi Ngoại Tệ & Tỷ Giá",
     "Bảng so sánh đa chiều biểu lãi suất tiền gửi tiết kiệm theo các kỳ hạn 1-36 tháng của 30+ ngân hàng, tích hợp bộ lọc lãi suất cao nhất.",
     "In Progress"),

    ("Phase 1", "Tháng 9/2026", "Dự Án 8: Thực Tập Sinh Đầu Tư (Chứng Khoán)",
     "Công cụ tra cứu, hướng dẫn và giả lập Đầu Tư Chứng Khoán",
     "Planned"),

    ("Phase 2", "Tháng 10/2026", "Dự Án 9: Bổ sung các công cụ tính toán tài chính",
     "Công cụ 'Có Tiền Đầu Tư Gì?' phân bổ tài sản Lump Sum (An toàn, Tăng trưởng, Mạo hiểm), Bộ giả lập Lãi kép tích lũy SIP và FIRE.",
     "Planned"),

    ("Phase 2", "Tháng 10/2026", "Dự Án 9: Trung Tâm Đầu Tư & Tích Sản FIRE",
     "Công cụ 'Có Tiền Đầu Tư Gì?' phân bổ tài sản Lump Sum (An toàn, Tăng trưởng, Mạo hiểm), Bộ giả lập Lãi kép tích lũy SIP và FIRE.",
     "Planned")
]

if 'Roadmap' in wb.sheetnames:
    del wb['Roadmap']

ws_rm = wb.create_sheet('Roadmap', index=1)
ws_rm.append(["LỘ TRÌNH TRIỂN KHAI TOÀN DIỆN CÁC DỰ ÁN FINANCIAL HUB"])
ws_rm.merge_cells("A1:E1")
ws_rm.cell(row=1, column=1).fill = section_fill
ws_rm.cell(row=1, column=1).font = section_font
ws_rm.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')

headers = [
    "Giai Đoạn (Phase)",
    "Thời Gian",
    "Tên Dự Án / Module Trọng Tâm",
    "Chi Tiết Triển Khai & Nhiệm Vụ Kỹ Thuật",
    "Trạng Thái"
]
ws_rm.append(headers)
for c_i in range(1, len(headers) + 1):
    c = ws_rm.cell(row=2, column=c_i)
    c.fill = header_fill; c.font = header_font; c.border = thin_border
    c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
ws_rm.row_dimensions[2].height = 26.0

for item in exact_screenshot_rows:
    phase, time_val, name, desc, status_val = item
    ws_rm.append([phase, time_val, name, desc, status_val])
    r = ws_rm.max_row
    ws_rm.row_dimensions[r].height = 30.0 if '\n' in desc else 24.0
    
    ws_rm.cell(row=r, column=1).alignment = Alignment(horizontal='center', vertical='center')
    ws_rm.cell(row=r, column=2).alignment = Alignment(horizontal='center', vertical='center')
    ws_rm.cell(row=r, column=3).alignment = Alignment(horizontal='left', vertical='center'); ws_rm.cell(row=r, column=3).font = Font(name='Arial', size=9.5, bold=True)
    ws_rm.cell(row=r, column=4).alignment = Alignment(horizontal='left', vertical='center', wrap_text=True)
    ws_rm.cell(row=r, column=5).alignment = Alignment(horizontal='center', vertical='center')

    if "Phase 1" in phase: ws_rm.cell(row=r, column=1).fill = p1_fill
    elif "Phase 2" in phase: ws_rm.cell(row=r, column=1).fill = p2_fill

    # Status Pill Styling
    c_st = ws_rm.cell(row=r, column=5)
    if status_val == "Done":
        c_st.fill = status_done_fill; c_st.font = status_done_font
    elif status_val == "In Progress":
        c_st.fill = status_prog_fill; c_st.font = status_prog_font
    elif status_val == "Planned":
        c_st.fill = status_plan_fill; c_st.font = status_plan_font

    for c_i in range(1, 6): ws_rm.cell(row=r, column=c_i).border = thin_border

widths = [16, 18, 40, 75, 18]
for idx, w in enumerate(widths, start=1):
    col_letter = get_column_letter(idx)
    ws_rm.column_dimensions[col_letter].width = w

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully synced EXACT screenshot roadmap to 05_HUBS/financial-hub-roadmap.xlsx!")

# Update BRD Section 10
with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    brd = f.read()

new_s10_exact = """## 10. LỘ TRÌNH TRIỂN KHAI TOÀN DIỆN CÁC DỰ ÁN FINANCIAL HUB (THỰC TẾ TRIỂN KHAI)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.85em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Giai Đoạn (Phase)</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Thời Gian</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Tên Dự Án / Module Trọng Tâm</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Chi Tiết Triển Khai & Nhiệm Vụ Kỹ Thuật</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Trạng Thái</th>
    </tr>
  </thead>
  <tbody>
    <!-- PHASE 1 - THÁNG 8/2026 -->
    <tr style="background-color:#f0fdf4;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;" rowspan="4"><strong>Phase 1</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 8/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 1: Master Financial Hub</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Xây dựng trang cổng trung tâm, thiết kế Mega Menu 5 nhóm nhu cầu tài chính, thanh Trợ thủ đồng hành và các thẻ điều hướng sản phẩm.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#15803d; background-color:#dcfce7;">Done</td>
    </tr>
    <tr style="background-color:#f0fdf4;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 8/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 2: CIC, Tiết Kiệm</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Công cụ CIC Simulator và Nợ Xấu.<br/>Công cụ tiết lãi suất tiết kiệm cho TKO</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#15803d; background-color:#dcfce7;">Done</td>
    </tr>
    <tr style="background-color:#fefce8;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 8/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 3: Content Strategy & Blog Tài Chính</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Thiết lập quy trình tự động hóa xuất bản cẩm nang tài chính bằng AI độc lập trên MoSpark</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#b45309; background-color:#fef9c3;">In Progress</td>
    </tr>
    <tr style="background-color:#f0fdf4;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 8/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 4: Tra Cứu Giá Vàng Realtime</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Xây dựng bảng giá vàng realtime (SJC, PNJ, DOJI, 24K, 9999, Nhẫn trơn), biểu đồ lịch sử 7-30 ngày</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#15803d; background-color:#dcfce7;">Done</td>
    </tr>
    <!-- PHASE 1 - THÁNG 9/2026 -->
    <tr style="background-color:#fefce8;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;" rowspan="3"><strong>Phase 1</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 9/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 5: Tính Lương & Thuế TNCN 2026</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Bộ công cụ tính lương Gross - Net (áp dụng luật thuế mới 2026) và cẩm nang tự quyết toán/hoàn thuế TNCN.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#b45309; background-color:#fef9c3;">In Progress</td>
    </tr>
    <tr style="background-color:#fefce8;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 9/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 7: Bộ Quy Đổi Ngoại Tệ & Tỷ Giá</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Bộ công cụ quy đổi tiền tệ tức thì giữa 20+ ngoại tệ (USD, JPY, EUR...) và bảng tỷ giá so sánh giữa các ngân hàng thương mại lớn.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#b45309; background-color:#fef9c3;">In Progress</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 9/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 8: Thực Tập Sinh Đầu Tư (Chứng Khoán)</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Công cụ tra cứu, hướng dẫn và giả lập Đầu Tư Chứng Khoán</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1d4ed8; background-color:#dbeafe;">Planned</td>
    </tr>
    <!-- PHASE 2 - THÁNG 10/2026 -->
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;" rowspan="2"><strong>Phase 2</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 10/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 9: Bổ sung các công cụ tính toán tài chính</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Công cụ 'Có Tiền Đầu Tư Gì?' phân bổ tài sản Lump Sum (An toàn, Tăng trưởng, Mạo hiểm), Bộ giả lập Lãi kép tích lũy SIP và FIRE.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1d4ed8; background-color:#dbeafe;">Planned</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 10/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 9: Trung Tâm Đầu Tư & Tích Sản FIRE</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Công cụ 'Có Tiền Đầu Tư Gì?' phân bổ tài sản Lump Sum (An toàn, Tăng trưởng, Mạo hiểm), Bộ giả lập Lãi kép tích lũy SIP và FIRE.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1d4ed8; background-color:#dbeafe;">Planned</td>
    </tr>
  </tbody>
</table>
"""

s10_start = brd.find("## 10. LỘ TRÌNH")
if s10_start != -1:
    brd = brd[:s10_start] + new_s10_exact
    with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
        f.write(brd)
    print("Successfully updated BRD Section 10 with EXACT screenshot content!")
