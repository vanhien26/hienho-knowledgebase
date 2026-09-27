file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '### 3.7 Đặc Tả Kỹ Thuật: Chuyên Trang Giá Xăng & Cây Xăng (/gia-xang)'
end_marker = '## IV. RISK & ROADMAP'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    exit(1)

detailed_spec = """### 3.7 Đặc Tả Kỹ Thuật: Chuyên Trang Giá Xăng & Cây Xăng (/gia-xang)

Trang Giá Xăng (`/gia-xang`) đóng vai trò là phễu lưu lượng truy cập lớn nhất toàn hệ sinh thái (10.523.210 search volume/tháng). Ngoài các khối bài viết tĩnh tối ưu SEO/GEO cẩm nang, giao diện người dùng (UI) bắt buộc phải tích hợp **3 thành phần động (Dynamic Components)** cốt lõi:

#### A. Component 1: Bảng Giá Xăng Realtime & Biểu Đồ Lịch Sử (Chart)
* **Bảng Giá Xăng Dầu Chuẩn Hóa:**
  * Phân loại hiển thị theo 2 vùng địa lý: **Giá Vùng 1** (các tỉnh thành gần cảng/kho đầu mối) và **Giá Vùng 2** (các địa bàn xa cảng/kho, quy định giá cao hơn tối đa 2%).
  * Danh mục 5 mặt hàng nhiên liệu: Xăng RON 95-III, RON 95-V, Xăng Sinh Học E5 RON 92-II, Dầu Diesel 0.05S-II, Dầu Hỏa.
  * Cấu trúc hiển thị: `Loại Nhiên Liệu`, `Giá Hiện Tại (VNĐ/lít)`, `Biến Động So Với Kỳ Trước (+/- VNĐ/lít)`, `Kỳ Điều Hành Trước`.
  * Nhãn trạng thái (Status Badge): "Cập nhật lúc 15:00 DD/MM/YYYY" (tô màu xanh lá nếu giá giảm, đỏ nếu giá tăng, xám nếu giữ nguyên).
* **Biểu Đồ Lịch Sử Biến Động (Interactive Line Chart):**
  * Tương tác chọn khung thời gian: 1 Tháng, 3 Tháng, 6 Tháng, 1 Năm.
  * Đường đồ thị so sánh trực quan giữa RON 95, E5 và Diesel. Tooltip hiển thị giá cụ thể tại từng mốc kỳ điều hành.

#### B. Component 2: Bản Đồ Định Vị & Tìm Cây Xăng Gần Đây
* **Cơ Chế Định Vị & Tìm Kiếm:**
  * Tự động bắt tọa độ GPS của người dùng (với sự đồng thuận - Location Permission) hoặc Dropdown chọn Tỉnh/Thành phố ➔ Quận/Huyện.
  * Bộ lọc thương hiệu cây xăng: Petrolimex, PVOil, Comeco, Saigon Petro, Khác.
  * Bộ lọc tiện ích: "Chấp nhận MoMo", "Mở cửa 24/7", "Có vòi rửa xe / cứu hộ".
* **Giao Diện Kép (Dual View):**
  * Bản đồ nhúng (Interactive Map): Hiển thị các pin cây xăng kèm logo nhận diện chính thức (PVOil, Comeco) hoặc icon mặc định.
  * Danh sách hiển thị liền kề: Liệt kê các trạm gần nhất theo thứ tự khoảng cách (mét/km), địa chỉ chi tiết, nhãn "Chấp nhận MoMo" và nút CTA "Chỉ đường" (Google Maps) + "Thu thập Voucher MoMo".

#### C. Component 3: Bộ Công Cụ Máy Tính Giá Xăng Đa Năng (Calculator 3 Chế Độ)

Bộ máy tính được thiết kế dạng Multi-tab, cho phép chuyển đổi tức thì giữa 3 chế độ tính toán. Mọi phép tính đều chạy Client-side (JavaScript) với độ trễ 0ms.

##### 1. Hệ Thống Biến Số Toán Học (Mathematical Variables)
* $P_{curr}$: Đơn giá nhiên liệu hiện tại (VNĐ/lít), phụ thuộc vào loại xăng được chọn và phân vùng địa lý (Vùng 1 hoặc Vùng 2). Mặc định chọn RON 95-III Vùng 1.
* $P_{prev}$: Đơn giá nhiên liệu kỳ điều hành trước liền kề (VNĐ/lít).
* $\\Delta P = P_{curr} - P_{prev}$: Độ biến động đơn giá (+/- VNĐ/lít).
* $V_{refill}$: Thể tích nhiên liệu cần nạp vào bình (Lít).
* $V_{tank}$: Dung tích toàn phần của bình nhiên liệu phương tiện (Lít).
* $R_{\\%} \\in [0.0, 1.0]$: Tỷ lệ nhiên liệu hiện còn lại trong bình (0% - Bình cạn, 25%, 50%, 75%).
* $D$: Tổng quãng đường di chuyển của chuyến đi (Km).
* $FC$: Định mức tiêu hao nhiên liệu trung bình (Fuel Consumption) (Lít / 100 Km).
* $N_{passengers}$: Số người tham gia chuyến đi (dùng để chia tiền bình quân).

##### 2. Chi Tiết Công Thức Toán Học Theo Từng Chế Độ

**Chế độ 1: Tính Theo Số Lít (Liters Mode)**
* **Mục đích:** Người dùng muốn biết đổ bao nhiêu lít xăng thì hết bao nhiêu tiền và đắt/rẻ hơn kỳ trước bao nhiêu.
* **Input:** Số lít cần đổ $V_{refill}$ (Slider kéo từ 1.0L đến 150.0L, bước nhảy 0.5L hoặc ô nhập số tay) + Loại xăng ($P_{curr}$).
* **Công thức tính tổng tiền:**
  $$\\text{Total\\_Cost} = \\text{round}(V_{refill} \\times P_{curr})$$
* **Công thức tính chênh lệch so với kỳ điều hành trước:**
  $$\\Delta \\text{Cost} = \\text{round}(V_{refill} \\times \\Delta P) = \\text{round}(V_{refill} \\times (P_{curr} - P_{prev}))$$
* **Logic hiển thị kết quả:**
  * Nếu $\\Delta \\text{Cost} > 0$: Hiển thị *"Trả thêm +[\\Delta \\text{Cost}] đ so với kỳ trước"* (chữ màu đỏ).
  * Nếu $\\Delta \\text{Cost} < 0$: Hiển thị *"Tiết kiệm [|\\Delta \\text{Cost}|] đ so với kỳ trước"* (chữ màu xanh lá).
  * Nếu $\\Delta \\text{Cost} = 0$: Hiển thị *"Giá không đổi so với kỳ trước"* (chữ màu xám).

**Chế độ 2: Tính Theo Loại Xe / Đầy Bình (Vehicle Tank Mode)**
* **Mục đích:** Người dùng chọn xe của mình để biết đổ đầy bình hết bao nhiêu tiền mà không cần nhớ bình xăng xe mình bao nhiêu lít.
* **Input:** Chọn Nhóm xe (Xe máy / Ô tô) ➔ Chọn Hãng xe ➔ Chọn Dòng xe ➔ Chọn Mức xăng còn lại $R_{\\%}$ (0%, 25%, 50%, 75%).
* **Bước 1 (Tra cứu dung tích chuẩn):** Hệ thống lấy $V_{tank} = \\text{Lookup}(\\text{Hãng}, \\text{Dòng xe})$ từ Database nạp sẵn:
  * *Bảng tham chiếu xe máy phổ biến:* Honda Wave Alpha (3.7L), Honda Vision (5.2L), Honda Lead (6.0L), Honda Air Blade (4.4L), Honda SH 125/160 (7.8L), Yamaha Grande (4.4L), Yamaha Exciter 155 (5.4L).
  * *Bảng tham chiếu ô tô phổ biến:* Hyundai Grand i10 (37L), Toyota Vios (42L), Honda City (40L), Mazda 3 (51L), Mitsubishi Xpander (45L), Mazda CX-5 (56L), Hyundai SantaFe (67L), Toyota Fortuner (80L), Ford Everest (80L).
* **Bước 2 (Tính lượng xăng cần nạp):**
  $$V_{refill} = \\text{round}\\big(V_{tank} \\times (1.0 - R_{\\%}), 2\\big)$$
* **Bước 3 (Tính tổng tiền đổ đầy bình):**
  $$\\text{Total\\_Cost\\_Tank} = \\text{round}(V_{refill} \\times P_{curr})$$
* **Bước 4 (Tính tiền chênh lệch khi đổ đầy bình):**
  $$\\Delta \\text{Cost\\_Tank} = \\text{round}(V_{refill} \\times (P_{curr} - P_{prev}))$$

**Chế độ 3: Tính Theo Khoảng Cách & Lộ Trình (Distance / Route Mode)**
* **Mục đích:** Dự toán ngân sách tiền xăng cho các chuyến công tác, về quê, hoặc đi du lịch phượt; hỗ trợ tính chi phí trên mỗi Km và chia tiền cho đoàn.
* **Input:**
  * Quãng đường $D$ (Km): Nhập trực tiếp số Km hoặc bấm chọn nút lộ trình gợi ý sẵn (Hà Nội - Hải Phòng: 120km; Hà Nội - Ninh Bình: 95km; TP.HCM - Vũng Tàu: 100km; TP.HCM - Phan Thiết: 215km).
  * Định mức tiêu hao nhiên liệu $FC$ (Lít/100km): Tự động nạp theo phân khúc xe được chọn hoặc người dùng tự kéo thanh chỉnh (từ 1.5 đến 20.0 L/100km).
    * *Định mức chuẩn:* Xe số (1.7L/100km), Xe ga (2.3L/100km), Ô tô Sedan (6.5L/100km), Ô tô Crossover/SUV 5 chỗ (8.0L/100km), Ô tô SUV lớn 7 chỗ (9.8L/100km).
  * Số lượng người trên xe $N_{passengers}$ (mặc định = 1, cho phép chọn từ 1 đến 7 người).
  * Loại hành trình: 1 Chiều (One-way) hoặc Khứ Hồi (Round-trip, nhân đôi quãng đường).
* **Bước 1 (Tính tổng lượng nhiên liệu tiêu thụ của hành trình):**
  $$V_{trip} = \\text{round}\\left( \\frac{D}{100} \\times FC, 2 \\right)$$
  *(Nếu chọn Khứ Hồi: $V_{trip\\_round} = V_{trip} \\times 2$)*
* **Bước 2 (Tính tổng chi phí xăng cho chuyến đi):**
  $$\\text{Total\\_Cost\\_Trip} = \\text{round}(V_{trip} \\times P_{curr})$$
* **Bước 3 (Tính chi phí trung bình trên mỗi 1 Km di chuyển):**
  $$\\text{Cost\\_Per\\_Km} = \\text{round}\\left( \\frac{\\text{Total\\_Cost\\_Trip}}{D} \\right) = \\text{round}\\left( \\frac{FC \\times P_{curr}}{100} \\right)$$
* **Bước 4 (Tính chi phí chia theo đầu người):**
  $$\\text{Cost\\_Per\\_Person} = \\text{round}\\left( \\frac{\\text{Total\\_Cost\\_Trip}}{N_{passengers}} \\right)$$

##### 3. Quy Tắc Validation & Xử Lý Biên (Edge Cases & Formatting)
* **Quy tắc làm tròn:**
  * Số tiền (VNĐ): Luôn làm tròn đến hàng đơn vị (`Math.round`), hiển thị chuẩn phân tách hàng nghìn bằng dấu chấm (`.`) kèm ký hiệu `đ` (Ví dụ: `1.045.000 đ`).
  * Số lít ($V$): Làm tròn chính xác 2 chữ số thập phân (Ví dụ: `31.50 Lít`).
* **Trigger Re-calculate:**
  * Khi người dùng thay đổi vùng giá (Vùng 1 ➔ Vùng 2) hoặc đổi loại xăng (RON 95 ➔ E5 ➔ Diesel), hệ thống tự động cập nhật lại toàn bộ kết quả đang hiển thị trên cả 3 tab mà không làm mất các thông số người dùng đã chọn trước đó.
* **Validation Input:**
  * Quãng đường $D$ phải $> 0$ và $\\le 3.000$ km. Nếu nhập số âm hoặc để trống, hiển thị cảnh báo viền đỏ inline và vô hiệu hóa nút tính.
  * Số người $N_{passengers} \\in [1, 50]$.

#### D. Luồng Chuyển Đổi Web-to-App (W2A Hooks)
* **CTA Nhận Voucher Đổ Xăng:** Gắn Onelink mở App MoMo nhận gói quà ưu đãi 20.000đ khi thanh toán xăng dầu tại trạm Petrolimex/PVOil.
* **CTA Lưu Lộ Trình:** Dẫn vào Mini App tiện ích giao thông để theo dõi chi phí xăng thực tế và nhận thông báo tự động trước giờ điều chỉnh giá xăng (14:30 thứ Năm hàng tuần).

---

"""

new_content = content[:start_idx] + detailed_spec + content[end_idx:]

# Update Change Log
changelog_entry = """| **v8.8** | 2026-09-03 | Web Product Lead | **Chi Tiết Hóa Toàn Bộ Công Thức Tính Toán Trang Giá Xăng:** Chuẩn hóa hệ thống biến số toán học ($P_{curr}, P_{prev}, \\Delta P, V_{tank}, FC, D$), quy chuẩn công thức chi tiết cho 3 chế độ (Theo Lít, Theo Loại Xe/Đầy Bình, Theo Khoảng Cách/Lộ Trình), bổ sung bảng tham chiếu dung tích bình xăng chuẩn và quy tắc validation làm tròn tiền VNĐ. |
"""
new_content = new_content.replace('| **v8.7**', changelog_entry + '| **v8.7**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated BRD with deep detailed formulas successfully via string replacement.")
