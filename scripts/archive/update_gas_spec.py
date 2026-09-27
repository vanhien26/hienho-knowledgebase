import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

gas_spec = """### 3.7 Đặc Tả Kỹ Thuật: Chuyên Trang Giá Xăng & Cây Xăng (/gia-xang)

Trang Giá Xăng (`/gia-xang`) đóng vai trò là phễu lưu lượng truy cập lớn nhất toàn hệ sinh thái (10.523.210 search volume/tháng). Ngoài các khối bài viết tĩnh tối ưu SEO/GEO cẩm nang, giao diện người dùng (UI) bắt buộc phải tích hợp **3 thành phần động (Dynamic Components)** cốt lõi:

#### A. Component 1: Bảng Giá Xăng Realtime & Biểu Đồ Lịch Sử (Chart)
* **Bảng Giá Xăng Dầu Chuẩn Hóa:**
  * Phân loại hiển thị theo 2 vùng địa lý: **Giá Vùng 1** (tỉnh thành gần cảng/kho) và **Giá Vùng 2** (vùng sâu/vùng xa, quy chuẩn cao hơn ~2%).
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
Bộ công cụ tính toán nhiên liệu cung cấp 3 tab chuyển đổi linh hoạt:
1. **Chế độ 1 - Tính Theo Số Lít (Liters Mode):**
   * Input: Nhập số lít xăng cần mua (thanh trượt hoặc ô nhập tay từ 1L đến 150L) + Chọn loại xăng.
   * Công thức: `Tổng tiền = Số lít * Đơn giá hiện tại`.
   * So sánh kỳ trước: `Chênh lệch = Số lít * (Đơn giá hiện tại - Đơn giá kỳ trước)`.
2. **Chế độ 2 - Tính Theo Loại Xe / Đầy Bình (Vehicle Tank Mode):**
   * Input: Dropdown chọn Nhóm xe (Xe máy / Ô tô) ➔ Hãng xe (Honda, Yamaha, Toyota, Hyundai, Mazda...) ➔ Dòng xe cụ thể (Vision, SH, Vios, CX-5...).
   * Dữ liệu mặc định: Hệ thống tự động điền dung tích bình nhiên liệu chuẩn (`V_tank`, VD: Honda Vision = 5.2L; Toyota Vios = 42L; Ford Everest = 80L).
   * Input phụ: Thanh trượt mức xăng hiện có trong bình (0% - Bình cạn, 25%, 50%, 75%).
   * Công thức:
     * `Lượng xăng cần đổ = V_tank * (1 - Tỷ lệ còn lại)`.
     * `Tổng tiền đầy bình = Lượng xăng cần đổ * Đơn giá hiện tại`.
     * `Khoản tiết kiệm/tăng thêm = Lượng xăng cần đổ * (Đơn giá hiện tại - Đơn giá kỳ trước)`.
3. **Chế độ 3 - Tính Theo Khoảng Cách & Lộ Trình (Distance / Route Mode):**
   * Input: Nhập quãng đường di chuyển (Km) hoặc chọn lộ trình mẫu (Hà Nội - Hải Phòng 120km, TP.HCM - Vũng Tàu 100km).
   * Input phụ: Chọn loại xe để tự động áp dụng định mức tiêu hao nhiên liệu (`FC`: Lít/100km) hoặc người dùng tự nhập số.
   * Công thức:
     * `Lượng xăng tiêu thụ = (Quãng đường / 100) * FC`.
     * `Tổng chi phí nhiên liệu lộ trình = Lượng xăng tiêu thụ * Đơn giá hiện tại`.
     * `Chi phí trên mỗi Km di chuyển = Tổng chi phí / Quãng đường`.
   * Output: Bảng chi phí tổng, chi phí 2 chiều và chi phí bình quân chia đầu người (hữu ích cho các chuyến đi nhóm/du lịch).

#### D. Luồng Chuyển Đổi Web-to-App (W2A Hooks)
* **CTA Thanh Toán Tại Trạm:** Nút Onelink dẫn vào luồng quét mã thanh toán MoMo tại trạm xăng kèm mã ưu đãi hoàn tiền/giảm giá (Voucher 20k).
* **CTA Lưu Lộ Trình:** Dẫn vào Mini App tiện ích giao thông để theo dõi lịch sử đổ xăng và nhắc nhở bảo dưỡng xe định kỳ.

---

"""

# Insert before ## IV. RISK & ROADMAP
content = content.replace('## IV. RISK & ROADMAP', gas_spec + '## IV. RISK & ROADMAP', 1)

# Add Change Log entry
changelog_entry = """| **v8.7** | 2026-09-03 | Web Product Lead | **Đặc Tả Chi Tiết Chuyên Trang Giá Xăng & Cây Xăng (/gia-xang):** Chuẩn hóa chi tiết 3 Components động cốt lõi: Bảng giá xăng realtime kèm Chart biến động; Bản đồ GPS định vị cây xăng dual-view (bản đồ + danh sách); Bộ máy tính nhiên liệu đa năng 3 chế độ (Tính theo Lít, Tính theo Loại xe/Đầy bình, Tính theo Khoảng cách/Lộ trình). |
"""
content = content.replace('| **v8.6**', changelog_entry + '| **v8.6**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Gas price spec added to BRD successfully.")
