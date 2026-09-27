file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '#### C. Quy Chuẩn Triển Khai Kỹ Thuật Cho 10 Trang Con'
end_marker = '---'

pos_start = content.find(start_marker)
pos_end = content.find(end_marker, pos_start)

if pos_start == -1 or pos_end == -1:
    print("Markers not found!")
    exit(1)

new_section_c = """#### C. Hai Yêu Cầu Kỹ Thuật & Tăng Trưởng Bắt Buộc Khi Triển Khai (Critical Requirements)

Để cụm trang Cây Xăng thực sự giải quyết được bài toán người dùng và chiếm lĩnh thứ hạng Top Google, đội ngũ Dev và Content bắt buộc phải thực thi nghiêm ngặt 2 tiêu chí cốt lõi:

##### 1. Yêu Cầu 1: Năng Lực Lọc Đa Thuộc Tính Của Component (Multi-Property Filtering Engine)
Component Bản đồ và Danh sách trạm phải được lập trình theo cơ chế lọc kết hợp (Multi-facet Filters) hoàn toàn trên Client-side, cho phép người dùng hoặc URL tự động lọc theo toàn bộ các thuộc tính nghiệp vụ:
* **Lọc theo Khu vực (Location Facet):** Tham số hóa theo Tỉnh/Thành (`city`), Quận/Huyện (`district`) hoặc Tuyến đường huyết mạch (`route` - ví dụ: Quốc Lộ 1A). Khi vào trang con nào, Component tự động apply filter khu vực đó làm giá trị mặc định.
* **Lọc theo Thương hiệu (Brand Facet):** Lọc theo Petrolimex, PVOil, Comeco, Saigon Petro, Khác.
* **Lọc theo Giờ hoạt động (Operating Hours Facet):**
  * `is_open_now`: Tự động so khớp giờ hiện tại của thiết bị với `open_hours` của trạm để chỉ hiển thị các trạm đang mở cửa.
  * `is_24h`: Lọc riêng danh sách các cây xăng mở cửa 24/24 xuyên đêm (đáp ứng đúng nhu cầu tìm kiếm sau 22h).
* **Lọc theo Phương thức thanh toán (Payment Facet):**
  * `momo_accepted: true`: Lọc các trạm chấp nhận thanh toán MoMo QR hoặc liên kết PVOil Easy, ưu tiên đẩy lên đầu danh sách kèm nhãn badge nổi bật.
* **Lọc theo Chủng loại nhiên liệu (Fuel Availability Facet):** Lọc trạm có bán Xăng cao cấp RON 95-V (Euro 5) hoặc Dầu Diesel cao cấp DO 0,001S-V (Euro 5) cho các dòng xe đời mới.
* **Hiệu năng xử lý:** Kết quả lọc bản đồ và danh sách phải cập nhật tức thì (độ trễ <20ms), tuyệt đối không reload lại trang.

##### 2. Yêu Cầu 2: Tối Ưu Hóa Chuyên Sâu Nội Dung SEO / Local GEO
Mỗi trang trong cụm 10 trang con bắt buộc phải đi kèm khối nội dung chuẩn hóa để tối đa hóa thứ hạng Google SERP:
* **Tự động sinh Metadata chuẩn Local SEO (Programmatic Metadata):**
  * **Title:** `Cây Xăng [Tên Khu Vực] Gần Nhất - Mở Cửa 24/24, Có Thanh Toán MoMo | MoMo`
  * **Meta Description:** `Danh sách tổng hợp các cây xăng uy tín tại [Tên Khu Vực] mở cửa 24/7, chỉ đường Google Maps nhanh chóng, cập nhật giờ hoạt động và hướng dẫn thanh toán MoMo nhận ưu đãi hoàn tiền 20K.`
* **Cấu trúc dữ liệu có cấu trúc chuẩn mực (Schema JSON-LD):**
  * Khai báo Schema `LocalBusiness` / `GasStation` cho từng cây xăng xuất hiện trong danh sách (tên, địa chỉ, tọa độ GPS `GeoCoordinates`, giờ mở cửa `openingHoursSpecification`).
  * Khai báo Schema `ItemList` định danh danh bạ địa phương chuẩn Google.
  * Khai báo Schema `FAQPage` cho các câu hỏi thường gặp đặc thù khu vực (Ví dụ: *"Cây xăng nào ở Quận 1 mở cửa qua đêm?"*, *"Cây xăng ở Cầu Giấy có thanh toán chuyển khoản/MoMo không?"*).
* **Khối bài viết SEO Local hữu ích (Onpage Content Block):**
  * Nằm dưới khối bản đồ, cung cấp bài viết ngắn 600 - 800 từ phân tích các tuyến đường tập trung nhiều trạm xăng lớn trong khu vực, khung giờ cao điểm hay kẹt xe tại các trạm và mẹo đổ xăng tiết kiệm.

##### 3. Cơ Chế Chuyển Đổi Web-to-App (W2A Conversion Hook)
* Dưới chân mỗi Card trạm xăng đối tác, tích hợp nút hành động: *"Nhận Voucher 20K Đổ Xăng"* kích hoạt Onelink mở App MoMo nhận gói quà ưu đãi.
* Nút *"Chỉ đường"* kích hoạt Intent mở thẳng ứng dụng Google Maps / Apple Maps với tọa độ đích chính xác của trạm."""

content = content[:pos_start] + new_section_c + content[pos_end:]

# Update Change Log to v8.11
changelog_entry = """| **v8.11** | 2026-09-03 | Web Product Lead | **Chuẩn Hóa 2 Yêu Cầu Kỹ Thuật Bắt Buộc Cho Cụm Cây Xăng:** Bổ sung vào Mục 3.8.C: (1) Năng lực Component phải hỗ trợ lọc động kết hợp (Multi-facet) theo mọi properties (Khu vực, Thương hiệu, Mở cửa 24/24, Thanh toán MoMo, Loại xăng dầu Euro 5); (2) Chiến lược Content SEO/GEO chuyên sâu (Schema LocalBusiness, FAQPage, Dynamic Metadata, bài viết Onpage Local). |
"""
content = content.replace('| **v8.10**', changelog_entry + '| **v8.10**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated BRD with 2 critical requirements successfully!")
