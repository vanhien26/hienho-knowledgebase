file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Note in Section 3.7 for Gia Xang
gas_marker = "#### A. Component 1: Bảng Giá Xăng Realtime & Biểu Đồ Lịch Sử (Chart)"
gas_rule = """* **Quy Tắc Kiến Trúc URL (Bắt Buộc):** Trang Giá Xăng duy nhất tồn tại ở đường dẫn `/tien-ich-giao-thong/gia-xang`. **Tuyệt đối KHÔNG tạo trang con theo Tỉnh/Thành** (như `/gia-xang/ha-noi`, `/gia-xang/tp-hcm`...). Giá bán lẻ xăng dầu do Nhà nước quản lý đồng nhất theo 2 phân vùng (Vùng 1 & Vùng 2), giá giữa các tỉnh Vùng 1 hoàn toàn giống nhau; việc tạo trang theo tỉnh sẽ gây lỗi Duplicate Content (Trùng lặp nội dung 100%) và bị Google phạt rớt hạng. Sự khác biệt theo vùng được giải quyết bằng nút gạt chuyển đổi nhanh [Giá Vùng 1] vs [Giá Vùng 2] ngay trên bảng giá.\n"""

if gas_marker in content and "Tuyệt đối KHÔNG tạo trang con theo Tỉnh/Thành" not in content:
    content = content.replace(gas_marker, gas_marker + "\n" + gas_rule)

# 2. Add Section 3.10: Anti-Duplicate & SEO Framework before ## IV. RISK & ROADMAP
target_marker = "## IV. RISK & ROADMAP"

anti_duplicate_spec = """### 3.10 Nguyên Tắc Quản Trị URL & Phòng Chống Trùng Lặp Nội Dung (Anti-Cannibalization & De-Duplication)

Nhằm tránh nhầm lẫn giữa các đội ngũ Dev, Product và Content trong quá trình triển khai thực tế, toàn bộ hệ thống tuân thủ nghiêm ngặt **Khung kiểm soát ranh giới URL và phòng chống trùng lặp**:

#### A. Ma Trận Quy Hoạch URL Theo Đặc Thù Quản Lý & Search Volume
* **Nhóm Tuyệt Đối Không Sinh Trang Con (Chỉ 1 Trang Đơn Lẻ):**
  * **Giá Xăng (`/gia-xang`):** 1 Trang duy nhất. Không chia theo tỉnh/thành vì xăng dầu niêm yết theo Vùng 1 và Vùng 2 toàn quốc.
  * **Đăng Kiểm (`/dang-kiem`):** 1 Trang duy nhất. Dữ liệu từ khóa cho thấy Volume tìm kiếm theo địa phương bằng 0. Toàn bộ tiện ích tra hạn, chu kỳ Thông tư mới và bản đồ trạm đăng kiểm 63 tỉnh được gom gọn trong 1 trang duy nhất để dồn sức mạnh SEO.
  * **Thu Phí BOT (`/phi-khong-dung`), Cứu Hộ (`/cuu-ho`), Máy Tính Lăn Bánh (`/lan-banh`):** Đều là các trang độc lập đơn lẻ.
* **Nhóm Được Phép Tạo Trang Con (Có Search Volume Lớn & Dữ Liệu POI Thực Tế):**
  * **Cây Xăng (`/cay-xang`):** 1 Master Map + **Chính xác 10 Trang con** có Search Volume lớn nhất (4 Tỉnh/Thành: TP.HCM, Hà Nội, Đà Nẵng, Bình Dương; 6 Quận/Tuyến: Q.1, Q.7, Thủ Đức, Cầu Giấy, Đống Đa, Quốc Lộ 1A).
  * **Trạm Sạc EV (`/tram-sac`):** 1 Master Map + **Chính xác 6 Trang con trọng điểm** (Chuyên trang VinFast/V-Green chiếm 85% volume; Trục Cao tốc liên tỉnh; 4 Thành phố lớn: Hà Nội, TP.HCM, Đà Nẵng, Hải Phòng). Đã loại bỏ hoàn toàn trang sạc xe máy điện.
  * **Phạt Nguội (`/phat-nguoi`):** 1 Standalone Master + 63 Trang Location Pages theo các tỉnh/thành phố để hứng từ khóa công an tỉnh.

#### B. 4 Rào Chắn Kỹ Thuật Chống Phạt Thuật Toán Google (Doorway Pages / Duplicate)
1. **Dữ liệu POI độc bản (100% Unique Data):** Mỗi trang con Cây xăng hoặc Trạm sạc bắt buộc phải nạp danh sách địa điểm thực tế của riêng khu vực đó từ CDN Cache (không chia sẻ chung danh sách để tránh trùng lặp mã nguồn).
2. **Khai báo Schema tách biệt theo chuyên ngành:**
   * Cây xăng khai báo: `type: "GasStation"`
   * Trạm sạc xe điện khai báo: `type: "EVChargingStation"`
   * Cổng phạt nguội khai báo: `type: "GovernmentService"` / `FAQPage`
3. **Thẻ Canonical tự tham chiếu (Self-referencing Canonical):** Mỗi trang con đều phải có thẻ `<link rel="canonical" href="...">` trỏ chính xác về URL của chính nó để xác nhận tính pháp lý của thực thể trang trước Google Bot.
4. **Địa phương hóa nội dung bổ trợ (Localized FAQ):** Tuyệt đối không sao chép văn bản tĩnh giữa các trang con; mỗi địa phương bắt buộc có 2-3 câu hỏi giải đáp đặc thù cho khu vực đó.

---

"""

if "### 3.10 Nguyên Tắc Quản Trị URL" not in content:
    content = content.replace(target_marker, anti_duplicate_spec + target_marker, 1)

# 3. Add Change Log v8.13
changelog_entry = """| **v8.13** | 2026-09-03 | Web Product Lead | **Khóa Toàn Bộ Quy Chuẩn URL & Bộ Nguyên Tắc Chống Trùng Lặp (Mục 3.10):** Khẳng định dứt điểm: Trang Giá Xăng (/gia-xang) và Đăng Kiểm (/dang-kiem) là 1 trang duy nhất, tuyệt đối KHÔNG tạo trang con theo tỉnh/thành (tránh lỗi Duplicate Content). Chốt chặn ranh giới số lượng trang con cho Cây Xăng (10 trang) và Trạm Sạc (6 trang). Thiết lập 4 rào chắn kỹ thuật chống thuật toán Doorway Pages của Google. |
"""
content = content.replace('| **v8.12**', changelog_entry + '| **v8.12**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated BRD with Anti-Duplicate Rules successfully!")
