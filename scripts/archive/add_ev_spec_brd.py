import openpyxl
from openpyxl.styles import Alignment, Border, Side, PatternFill, Font

# 1. Update BRD
file_brd = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_brd, 'r', encoding='utf-8') as f:
    content = f.read()

target_marker = '## IV. RISK & ROADMAP'

ev_spec = """### 3.9 Đặc Tả Kỹ Thuật: Chuyên Trang Trạm Sạc Xe Điện (/tram-sac) & Bộ Tiện Ích Sạc Pin

Chuyên trang Trạm Sạc Xe Điện (`/tram-sac`) thâu tóm lưu lượng tìm kiếm đứng thứ 3 toàn hệ sinh thái (1.237.970 search volume/tháng). Nhằm tối ưu hóa tài nguyên và tập trung 100% vào tệp ô tô điện có giá trị kinh tế cao (High ARPU), hệ thống quy hoạch **7 trang trọng điểm** và **duy nhất 1 tiện ích lõi (Core Utility)**:

#### A. Danh Mục 7 Trang Trọng Điểm Cụm Trạm Sạc EV
1. `/tien-ich-giao-thong/tram-sac`: Bản đồ trạm sạc xe điện toàn quốc (Master Hub).
2. `/tien-ich-giao-thong/tram-sac/vinfast`: Chuyên trang mạng lưới trạm sạc VinFast / V-Green (thâu tóm 85% lượng tìm kiếm toàn thị trường).
3. `/tien-ich-giao-thong/tram-sac/cao-toc`: Mạng lưới trụ sạc nhanh DC tại các trạm dừng nghỉ trên các trục cao tốc huyết mạch (Pháp Vân - Cầu Giẽ, Hà Nội - Hải Phòng, Long Thành - Dầu Giây - Phan Thiết).
4. `/tien-ich-giao-thong/tram-sac/ha-noi`: Trạm sạc ô tô điện tại Hà Nội (mật độ chung cư & Vincom lớn nhất miền Bắc).
5. `/tien-ich-giao-thong/tram-sac/tp-hcm`: Trạm sạc ô tô điện tại TP. Hồ Chí Minh.
6. `/tien-ich-giao-thong/tram-sac/da-nang`: Trạm sạc ô tô điện tại Đà Nẵng.
7. `/tien-ich-giao-thong/tram-sac/hai-phong`: Trạm sạc ô tô điện tại Hải Phòng (thủ phủ xe điện VinFast).

*(Toàn bộ các trang trên dùng chung 1 Component Template bản đồ, chỉ thay đổi tham số lọc khu vực `network=VINFAST`, `city=...`, `type=HIGHWAY`).*

#### B. Utility Duy Nhất: Máy Tính Thời Gian & Chi Phí Sạc Pin (EV Charging & Cost Estimator)

Bộ công cụ tính toán được thiết kế siêu gọn nhẹ theo nguyên tắc 1 chạm (Zero-Friction UX), giải quyết trực diện 2 câu hỏi lớn nhất của tài xế: *"Sạc bao lâu?"* và *"Hết bao nhiêu tiền so với đổ xăng?"*.

##### 1. Hệ Thống Biến Số & Cơ Sở Dữ Liệu Xe Điện (EV Database)
* $E_{cap}$: Tổng dung lượng pin khả dụng của xe (kWh). Nạp sẵn từ Database:
  * VinFast VF 3: 18.64 kWh
  * VinFast VF 5 Plus: 37.23 kWh
  * VinFast VF 6 (Base / Plus): 59.60 kWh
  * VinFast VF 7 (Base / Plus): 75.30 kWh
  * VinFast VF 8 (Eco / Plus): 87.70 kWh
  * VinFast VF 9 (Eco / Plus): 123.00 kWh
  * Hãng khác (BYD Atto 3: 60.48 kWh, Hyundai Ioniq 5: 72.60 kWh, Porsche Taycan: 93.40 kWh).
* $P_{charger}$: Công suất danh định của trụ sạc (kW):
  * Trụ siêu nhanh DC: 150 kW - 250 kW
  * Trụ nhanh DC: 60 kW
  * Trụ thường AC: 11 kW
* $P_{unit}$: Đơn giá điện sạc công cộng hiện hành (mặc định lấy theo biểu phí V-Green: **3.858 VNĐ/kWh**).
* $Target_{\\%}$ và $Current_{\\%}$: Mức pin mục tiêu và mức pin hiện tại. Cung cấp 2 nút chọn nhanh:
  * **Chế độ 1 (Mặc định): Sạc Nhanh Đường Dài [ 20% ➔ 80% ]** (Khung sạc tối ưu bảo vệ pin và nhanh nhất).
  * **Chế độ 2: Sạc Đầy Kịch Khung [ 10% ➔ 100% ]** (Sạc trước chuyến đi xa).

##### 2. Chi Tiết Công Thức Thuật Toán (Calculation Formulas)
* **Bước 1 - Tính lượng điện năng thực tế cần nạp:**
  $$\\Delta E = \\text{round}\\big(E_{cap} \\times (Target_{\\%} - Current_{\\%}), 2\\big) \\quad (\\text{kWh})$$
* **Bước 2 - Tính thời gian sạc ước tính (Phút):**
  * Hiệu suất tiếp nhận thực tế của xe đạt trung bình $\\eta = 0.85$ (85% công suất trụ do giới hạn hệ thống quản lý pin BMS của xe):
    $$P_{effective} = \\min(P_{charger}, P_{max\\_car\\_input}) \\times \\eta$$
  * Thời gian sạc:
    $$T_{charge} = \\text{round}\\left( \\frac{\\Delta E}{P_{effective}} \\times 60 \\right) \\quad (\\text{Phút})$$
* **Bước 3 - Tính tổng chi phí sạc điện (VNĐ):**
  $$\\text{Total\\_Cost\\_EV} = \\text{round}(\\Delta E \\times P_{unit})$$
* **Bước 4 - Tính tiền xăng tương đương & Khoản tiền tiết kiệm:**
  * Quãng đường đi thêm được: $Range_{added} = \\text{round}\\left( \\frac{\\Delta E}{FC_{ev}} \\times 100 \\right)$ Km (với $FC_{ev}$ là định mức tiêu thụ điện ~14-18 kWh/100km).
  * Chi phí xe xăng cùng quãng đường: $\\text{Cost\\_Gas} = \\text{round}\\left( \\frac{Range_{added}}{100} \\times 7.5 \\times P_{RON95} \\right)$.
  * Khoản tiền tiết kiệm: $\\text{Savings} = \\text{Cost\\_Gas} - \\text{Total\\_Cost\\_EV}$.

##### 3. Kết Quả Hiển Thị Mẫu (Output Card)
Khi người dùng chọn **[ VF 5 ]** ➔ Bấm **[ Sạc 20% - 80% tại trụ DC 60kW ]**:
* **Thời gian chờ sạc:** **~28 Phút** (vừa đủ thời gian uống nước/nghỉ ngơi).
* **Tổng tiền sạc:** **86.000 đ** (nạp được ~22.3 kWh điện, đi thêm được khoảng 190 km).
* **So sánh tài chính:** *"Cùng quãng đường này xe xăng tốn ~220.000 đ ➔ Bạn tiết kiệm được ~134.000 đ"*.

#### C. Luồng Chuyển Đổi Web-to-App (W2A Hooks)
* **Bán chéo Bảo hiểm Thân vỏ Ô tô điện:** Khối banner chân trang: *"Bảo hiểm xe điện MoMo – Bảo vệ pin toàn diện, cam kết đền bù thủy kích 100%"*.
* **Nạp ví ePass / VETC:** Đón đầu các tài xế xe điện chạy cao tốc.

---

"""

content = content.replace(target_marker, ev_spec + target_marker, 1)

# Add Change Log v8.12
changelog_entry = """| **v8.12** | 2026-09-03 | Web Product Lead | **Chuẩn Hóa Đặc Tả Chuyên Trang Trạm Sạc EV (/tram-sac) & Utility Duy Nhất:** Loại bỏ hoàn toàn trang sạc xe máy điện; quy hoạch 7 trang trọng điểm tập trung vào ô tô điện (1 Master, 1 VinFast brand, 1 Cao tốc, 4 Tỉnh/Thành lớn). Khóa duy nhất 1 Utility lõi: Máy tính Thời gian & Chi phí sạc pin xe điện (EV Charging & Cost Estimator) với đầy đủ Database dung lượng pin và công thức tính tiền/thời gian sạc. |
"""
content = content.replace('| **v8.11**', changelog_entry + '| **v8.11**', 1)

with open(file_brd, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated BRD with EV spec successfully!")

# 2. Update Excel Utilities sheet
file_excel = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-roadmap.xlsx'
wb = openpyxl.load_workbook(file_excel)
ws = wb['Utilities & Formula Specs']

border_thin = Border(left=Side(style='thin', color='D9D9D9'),
                     right=Side(style='thin', color='D9D9D9'),
                     top=Side(style='thin', color='D9D9D9'),
                     bottom=Side(style='thin', color='D9D9D9'))
align_left = Alignment(horizontal='left', vertical='center', wrap_text=True)
align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)

# Append Tool 5
tool_5_data = [
    5,
    'Máy Tính Thời Gian & Chi Phí Sạc Pin Xe Điện (EV Estimator)',
    'Interactive Quick Widget / Battery Level Card',
    'Ước tính chính xác số phút cần chờ sạc pin và tổng chi phí tiền điện sạc trụ công cộng so với đổ xăng truyền thống.',
    '• Mẫu xe điện (VF3, VF5, VF6, VF7, VF8, VF9...)\n• Khung sạc: Sạc nhanh đường dài (20% - 80%) hoặc Sạc đầy (10% - 100%)\n• Loại trụ sạc: DC 60kW, DC 150kW-250kW, AC 11kW',
    '1. Điện năng nạp: Delta_E = E_cap * (Target% - Current%).\n2. Thời gian sạc: T_charge = (Delta_E / P_effective) * 60 (phút).\n3. Tổng tiền điện: Cost_EV = Delta_E * 3.858 đ/kWh.\n4. Tiết kiệm so với xăng: Savings = Cost_Gas - Cost_EV.',
    '• Thời gian sạc ước tính (Phút).\n• Tổng chi phí sạc pin (VND).\n• Quãng đường đi thêm được (Km).\n• Khoản tiền tiết kiệm so với đổ xăng.',
    "Nút 'Mua Bảo Hiểm Thân Vỏ Pin Xe Điện' & 'Nạp ePass Cao Tốc'.",
    'Trang Trạm Sạc (/tram-sac), Chuyên trang VinFast (/tram-sac/vinfast), Trang chi tiết mẫu xe điện, Cẩm nang xe điện MoMo.'
]

ws.append(tool_5_data)
row_idx = ws.max_row
ws.row_dimensions[row_idx].height = 45
for col in range(1, 10):
    c = ws.cell(row_idx, col)
    c.border = border_thin
    c.alignment = align_center if col in [1, 3] else align_left
    c.font = Font(name='Calibri', size=10)

wb.save(file_excel)
print("Updated Excel Utilities sheet with Tool 5 successfully!")
