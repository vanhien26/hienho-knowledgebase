# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN) - USE CASE: BIEN SO XE (1)

- **Use Case:** Bien So Xe (1)
- **URL Pillar Hub:** `/bien-so-xe (1)/`
- **Tổng dung lượng tìm kiếm của Cụm (Addressable Search Volume):** 619,140 lượt/tháng
- **Số lượng URLs phân bổ:** 6 URLs (1 Pillar Hub + 5 Cluster Pages)
- **Quy tắc phân bổ:** Mỗi URL giải quyết duy nhất 1 Search Intent độc lập để triệt tiêu hiện tượng ăn thịt từ khóa (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Keywords | Search Volume | Search Intent | Định Dạng (Format) | Phễu | Ưu Tiên | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| 1 | `/bien-so-xe (1)/` | Cẩm Nang & Bảng Tra Cứu Bien So Xe (1) Toàn Diện | `biển đăng ký xe` | biển số xe, biển số xe các tỉnh, đăng ký xe | 599,500 | `Transactional` | Pillar Hub Page + Interactive Widget | `TOFU` | `P0` | Form tra cứu trực tiếp trên Web -> Nút nộp phạt / Nạp tài khoản giao thông MoMo |
| 2 | `/bien-so-xe (1)/cong-cu-tinh-toan/` | Công Cụ Tính Bien So Xe (1) Trực Tuyến & Bảng Tính Chi Tiết | `làm biển số xe bao nhiêu tiền` | biển số xe bao nhiêu tiền, biển số xe full 9 bao nhiêu tiền, biển số xe tính như thế nào | 80 | `Tool/Calculator` | Interactive Calculator / Lookup Tool | `BOFU` | `P0` | Form tra cứu trực tiếp trên Web -> Nút nộp phạt / Nạp tài khoản giao thông MoMo |
| 3 | `/bien-so-xe (1)/so-sanh-danh-gia/` | So Sánh & Đánh Giá Bien So Xe (1): Lựa Chọn Nào Tốt Nhất? | `biển số xe nên tránh` | biển số xe xấu nên tránh, so sánh biển số xe, biển số xe nên tránh những số nào | 30 | `Commercial` | Comparison Table & Evaluation | `MOFU` | `P0` | Banner tiện ích giao thông toàn diện trên MoMo App |
| 4 | `/bien-so-xe (1)/an-toan-bao-mat/` | Bien So Xe (1) Online Có An Toàn Không? Rủi Ro & Biện Pháp Bảo Vệ | `đăng ký biển số xe máy online` | đăng ký biển số xe online, định giá biển số xe online, bấm biển số xe online | 4,030 | `Informational` | Trust & Security Guide | `MOFU` | `P1` | Banner tiện ích giao thông toàn diện trên MoMo App |
| 5 | `/bien-so-xe (1)/thu-tuc-huong-dan/` | Hướng Dẫn Thủ Tục Bien So Xe (1): Hồ Sơ, Quy Trình & Lưu Ý | `thủ tục đăng ký xe máy mới` | thủ tục đăng ký biển số xe ô tô cũ, hướng dẫn đăng ký xe máy, thủ tục đăng ký biển số xe máy | 800 | `Transactional` | Step-by-step How-to & Action Form | `MOFU` | `P1` | Form tra cứu trực tiếp trên Web -> Nút nộp phạt / Nạp tài khoản giao thông MoMo |
| 6 | `/bien-so-xe (1)/kien-thuc-chuyen-sau/` | Tổng Hợp Kinh Nghiệm & Giải Đáp Thắc Mắc Về Bien So Xe (1) | `biển số đẹp` | biển số, biển số xe hà nội, bảng số | 14,700 | `Informational` | Comprehensive Guide & FAQ | `TOFU` | `P2` | Banner tiện ích giao thông toàn diện trên MoMo App |

---

## 2. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`/bien-so-xe (1)/`) đặt contextual links tới toàn bộ các Cluster Pages trong các mục nội dung liên quan.
   - 100% Cluster Pages bắt buộc đặt 1 anchor text tự nhiên trong 100 từ đầu tiên trỏ về Pillar Page (ví dụ: *"tra cứu thông tin tổng hợp tại cẩm nang..."*).
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết ngang sang trang Đánh giá (`so-sanh-danh-gia/`) để hỗ trợ người dùng ra quyết định.
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ link sang trang An toàn bảo mật (`an-toan-bao-mat/`) để gia tăng niềm tin.
3. **Móc chuyển đổi Web-to-App:**
   - Mọi trang đều tích hợp Utility Widget trực tiếp trên Web. Khi người dùng bấm nút xác nhận kết quả hoặc cần thực hiện giao dịch thực tế, kích hoạt Deeplink mở trực tiếp App MoMo.
