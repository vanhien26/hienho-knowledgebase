file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target_marker = '## IV. RISK & ROADMAP'

station_spec = """### 3.8 Đặc Tả Kỹ Thuật: Chuyên Trang Bản Đồ Cây Xăng Gần Đây (/cay-xang) & 10 Trang Con Trọng Điểm

Chuyên trang Cây Xăng (`/cay-xang`) thâu tóm toàn bộ nhóm từ khóa có ý định hành động khẩn cấp (Local & Urgent Search - 550.000 volume/tháng). Sản phẩm được thiết kế gồm **1 Trang Master Map** và **10 Trang Con (Subpages)** đánh vào các khu vực có mật độ tìm kiếm cao nhất cả nước:

#### A. Định Vị Trang Chính Master Hub (/cay-xang)
* **Trọng tâm sản phẩm:** Tập trung giải quyết 2 bài toán tìm kiếm lớn nhất: **"Cây xăng gần đây"** (theo định vị GPS tức thời) và **"Cây xăng mở cửa 24/24"** (đáp ứng nhu cầu ban đêm).
* **Cơ chế hiển thị:**
  * Bản đồ tương tác kết hợp Bottom Sheet trượt trên Mobile.
  * Tự động tính khoảng cách theo công thức Haversine chạy Client-side (<15ms).
  * Bộ lọc nhanh (Filter Chips): Thương hiệu (Petrolimex, PVOil, Comeco), Đang mở cửa / Mở 24/7, Chấp nhận thanh toán MoMo.
  * Thao tác 1 chạm: Bấm nút "Chỉ đường" mở thẳng ứng dụng Google Maps / Apple Maps với tọa độ đích `{lat, lng}`.

#### B. Danh Mục 10 Trang Con Trọng Điểm (Target Subpages)

Nhằm tối ưu hóa nguồn lực sản xuất nội dung, hệ thống không làm dàn trải mà tập trung xây dựng chuẩn xác **10 trang con có Search Volume lớn nhất** phân bổ thành 2 nhóm:

| STT | Phân Nhóm | Tên Trang Con | URL Chuẩn Hóa | Mục Tiêu Từ Khóa & Đặc Điểm Khu Vực |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Tỉnh / Thành** | Cây Xăng TP. Hồ Chí Minh | `/tien-ich-giao-thong/cay-xang/tp-hcm` | Thâu tóm thị trường lớn nhất phía Nam; tích hợp mạng lưới trạm Comeco, Petrolimex, PVOil. |
| **2** | **Tỉnh / Thành** | Cây Xăng Hà Nội | `/tien-ich-giao-thong/cay-xang/ha-noi` | Thị trường lớn nhất phía Bắc; tập trung các trạm Petrolimex & MIPEC mở cửa 24/7 nội đô. |
| **3** | **Tỉnh / Thành** | Cây Xăng Đà Nẵng | `/tien-ich-giao-thong/cay-xang/da-nang` | Trung tâm du lịch miền Trung; tập trung phục vụ khách thuê xe máy và tài xế du lịch. |
| **4** | **Tỉnh / Thành** | Cây Xăng Bình Dương | `/tien-ich-giao-thong/cay-xang/binh-duong` | Thủ phủ khu công nghiệp; tập trung lưu lượng xe tải, container và phương tiện công nhân. |
| **5** | **Quận / Tuyến** | Cây Xăng Quận 1 (TP.HCM) | `/tien-ich-giao-thong/cay-xang/tp-hcm/quan-1` | Trung tâm thương mại & du lịch Sài Gòn; nhu cầu tìm trạm mở đêm và chấp nhận thanh toán MoMo cực cao. |
| **6** | **Quận / Tuyến** | Cây Xăng Quận 7 (TP.HCM) | `/tien-ich-giao-thong/cay-xang/tp-hcm/quan-7` | Cửa ngõ Nam Sài Gòn & khu đô thị Phú Mỹ Hưng; mật độ ô tô cá nhân dày đặc. |
| **7** | **Quận / Tuyến** | Cây Xăng TP. Thủ Đức (TP.HCM) | `/tien-ich-giao-thong/cay-xang/tp-hcm/thu-duc` | Khu đô thị sáng tạo, nút giao ngã tư Thủ Đức, Xa Lộ Hà Nội; lưu lượng xe liên tỉnh khổng lồ. |
| **8** | **Quận / Tuyến** | Cây Xăng Quận Cầu Giấy (Hà Nội) | `/tien-ich-giao-thong/cay-xang/ha-noi/cau-giay` | Điểm nóng tập trung nhiều trường đại học, khu công nghệ cao Duy Tân và giới văn phòng trẻ. |
| **9** | **Quận / Tuyến** | Cây Xăng Quận Đống Đa (Hà Nội) | `/tien-ich-giao-thong/cay-xang/ha-noi/dong-da` | Quận có mật độ dân số cao nhất Hà Nội, nhiều nút giao ùn tắc; nhu cầu tìm trạm xăng gần nhất trên đường. |
| **10** | **Quận / Tuyến** | Cây Xăng Tuyến Quốc Lộ 1A | `/tien-ich-giao-thong/cay-xang/quoc-lo-1a` | Trục xương sống giao thông Bắc - Nam; phục vụ xe khách đường dài, xe tải và đoàn phượt liên tỉnh. |

#### C. Quy Chuẩn Triển Khai Kỹ Thuật Cho 10 Trang Con
* Sử dụng chung 1 Component Bản đồ của trang Master, chỉ thay đổi tham số lọc khu vực (`Filter Parameter: City / District / Route`) để tiết kiệm tối đa thời gian phát triển của Dev.
* Khai báo tự động Schema Markup `LocalBusiness` và `ItemList` chuẩn Google cho từng trang con để chiếm lĩnh Rich Snippets trên kết quả tìm kiếm tự nhiên.
* Nút CTA W2A: Nhận Voucher xăng xe MoMo 20K tại các trạm đối tác trong khu vực đó.

---

"""

content = content.replace(target_marker, station_spec + target_marker, 1)

# Add Change Log entry
changelog_entry = """| **v8.10** | 2026-09-03 | Web Product Lead | **Quy Hoạch Chi Tiết Chuyên Trang Cây Xăng & 10 Trang Con Local SEO:** Trang chính tập trung vào 'Cây xăng gần đây' & 'Cây xăng 24/24'. Quy hoạch chính xác cụm 10 trang con có Volume lớn nhất (4 Tỉnh/Thành: TP.HCM, Hà Nội, Đà Nẵng, Bình Dương; 6 Quận/Tuyến đường: Q.1, Q.7, Thủ Đức, Cầu Giấy, Đống Đa, Quốc Lộ 1A) để thâu tóm Local Search Traffic. |
"""
content = content.replace('| **v8.9**', changelog_entry + '| **v8.9**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Inserted Section 3.8 and updated Change Log v8.10 successfully!")
