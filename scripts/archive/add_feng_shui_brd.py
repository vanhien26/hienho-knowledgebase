import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Sitemap count from 21 to 22 URLs
content = content.replace('Sitemap Architecture (Tổng Hợp 21 URLs)', 'Sitemap Architecture (Tổng Hợp 22 URLs)')
content = content.replace('bao gồm **21 URLs**', 'bao gồm **22 URLs**')

# 2. Add the Phong Thuy URL to the table "Pháp Lý, Đăng Kiểm & Hồ Sơ Xe"
old_table_6 = """#### 6. Pháp Lý, Đăng Kiểm & Hồ Sơ Xe (Vehicle Paperwork & Legal)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 14 | `https://www.momo.vn/tien-ich-giao-thong/dang-kiem` | Tra cứu hạn đăng kiểm & đặt lịch kiểm định xe. |
| 15 | `https://www.momo.vn/tien-ich-giao-thong/bao-hiem-o-to` | Mua & so sánh bảo hiểm TNDS, Thân vỏ xe 9 hãng. |"""

new_table_6 = """#### 6. Pháp Lý, Đăng Kiểm & Hồ Sơ Xe (Vehicle Paperwork & Legal)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 14 | `https://www.momo.vn/tien-ich-giao-thong/dang-kiem` | Tra cứu hạn đăng kiểm & đặt lịch kiểm định xe. |
| 15 | `https://www.momo.vn/tien-ich-giao-thong/phong-thuy-bien-so` | Tra cứu Cát/Hung phong thủy biển số xe. |
| 16 | `https://www.momo.vn/tien-ich-giao-thong/bao-hiem-o-to` | Mua & so sánh bảo hiểm TNDS, Thân vỏ xe 9 hãng. |"""

content = content.replace(old_table_6, new_table_6)

# Need to re-number the STT for the table below it
old_table_7 = """#### 7. Bãi Đỗ, Cứu Hộ, Bảo Dưỡng & Giao Thông (Mobility Services)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 16 | `https://www.momo.vn/tien-ich-giao-thong/bai-do-xe` | Tìm kiếm & đặt chỗ bãi đỗ ô tô / xe máy (VETC Parking). |
| 17 | `https://www.momo.vn/tien-ich-giao-thong/cuu-ho` | Gọi cứu hộ xe 24/7 (Kéo xe, vá lốp, kích bình). |
| 18 | `https://www.momo.vn/tien-ich-giao-thong/tram-thu-phi` | Tra cứu biểu phí ePass / VETC các trạm thu phí BOT. |
| 19 | `https://www.momo.vn/tien-ich-giao-thong/camera-giao-thong` | Xem camera giao thông quan sát điểm kẹt xe realtime. |
| 20 | `https://www.momo.vn/tien-ich-giao-thong/bao-duong` | Đặt lịch bảo dưỡng, rửa xe & chăm sóc xe (Detailing). |
| 21 | `https://www.momo.vn/tien-ich-giao-thong/chuyen-di` | Nhật ký chuyến đi & công cụ quản lý lộ trình. |"""

new_table_7 = """#### 7. Bãi Đỗ, Cứu Hộ, Bảo Dưỡng & Giao Thông (Mobility Services)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 17 | `https://www.momo.vn/tien-ich-giao-thong/bai-do-xe` | Tìm kiếm & đặt chỗ bãi đỗ ô tô / xe máy (VETC Parking). |
| 18 | `https://www.momo.vn/tien-ich-giao-thong/cuu-ho` | Gọi cứu hộ xe 24/7 (Kéo xe, vá lốp, kích bình). |
| 19 | `https://www.momo.vn/tien-ich-giao-thong/tram-thu-phi` | Tra cứu biểu phí ePass / VETC các trạm thu phí BOT. |
| 20 | `https://www.momo.vn/tien-ich-giao-thong/camera-giao-thong` | Xem camera giao thông quan sát điểm kẹt xe realtime. |
| 21 | `https://www.momo.vn/tien-ich-giao-thong/bao-duong` | Đặt lịch bảo dưỡng, rửa xe & chăm sóc xe (Detailing). |
| 22 | `https://www.momo.vn/tien-ich-giao-thong/chuyen-di` | Nhật ký chuyến đi & công cụ quản lý lộ trình. |"""

content = content.replace(old_table_7, new_table_7)

# 3. Add Technical Specification Block for Feng Shui
spec_block = """---

### 3.5 Đặc Tả Kỹ Thuật Thuật Toán: Phong Thủy Biển Số Xe

Tiện ích tra cứu phong thủy đóng vai trò là "Traffic Magnet" kéo lượng lớn người dùng tự nhiên (989K Volume Search). Logic xử lý được thiết kế tĩnh (không cần AI):

**1. Dữ liệu nạp tĩnh (Database):**
*   **Bảng mã 80 Dịch Lý (JSON):** 80 bản ghi chứa ý nghĩa Cát/Hung.
*   **Dictionary Biển Đẹp/Xấu:** Chứa các cụm Regex số đẹp (Tứ quý, 39, 79, 68) hoặc kỵ (49, 53).

**2. Công thức chạy tuần tự (Logic Flow):**
*   **Bước 1 (Regex Check):** Quét 4-5 số cuối. Nếu khớp Dictionary Biển Đẹp/Xấu ➔ In luôn kết quả Cát/Hung.
*   **Bước 2 (Công thức 80):** Gọi `N` = Số đuôi. Tính `R = (N/80 - INT(N/80)) * 80`. Lấy kết quả `R` tra bảng JSON 80 Dịch Lý.
*   **Bước 3 (Tổng Nút):** `Sum(các chữ số) % 10` để trả số nút biển.

"""

content = content.replace('---', spec_block + '\n---', 1)

# Add Change Log v8.6
changelog_entry = """| **v8.6** | 2026-09-02 | Web Product Lead | **Bổ sung tính năng Phong Thủy Biển Số:** Tái tích hợp tiện ích `/phong-thuy-bien-so` vào Nhóm Pháp lý & Hồ sơ nhằm đẩy mạnh khả năng hứng Traffic (ước tính 989K search volume). Cập nhật đặc tả kỹ thuật thuật toán xử lý dữ liệu tĩnh tĩnh (Chia 80 Dịch Lý, Quét Regex cặp số đẹp). |
"""
content = content.replace('| **v8.5**', changelog_entry + '| **v8.5**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Feng Shui added to BRD successfully.")
