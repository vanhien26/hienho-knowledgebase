# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - USE CASE: BHYT

- **Use Case:** Bhyt
- **Phân Khối Ngành:** insurtech
- **URL Pillar Hub:** `/bhyt/`
- **Tổng từ khóa thô ban đầu:** 517 từ khóa
- **Từ khóa nhiễu bị loại bỏ:** 0 từ khóa
- **Từ khóa trùng Intent được gom cụm (Shielded):** 240 từ khóa
- **Số lượng URLs phân bổ:** 4 URLs (1 Pillar Hub + 3 Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Ưu Tiên | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| 1 | `/bhyt/` | Cẩm Nang & Bảng Tra Cứu Bhyt Toàn Diện | `bảo hiểm y tế` | bhyt, làm bảo hiểm y tế, có bảo hiểm y tế | 114,800 | `Informational` | Pillar Hub Page + Interactive Widget | `TOFU` | `P0` | Tích hợp Widget tương tác trên Web -> Deeplink mở MoMo App kích hoạt dịch vụ |
| 2 | `/bhyt/an-toan-bao-mat/` | Bhyt Online Có An Toàn Không? Rủi Ro & Biện Pháp Bảo Vệ | `bhyt online` | bảo hiểm y tế online, làm bảo hiểm y tế online, làm bhyt online | 2,680 | `Informational` | Trust & Security Guide | `MOFU` | `P1` | Tích hợp Widget tương tác trên Web -> Deeplink mở MoMo App kích hoạt dịch vụ |
| 3 | `/bhyt/thu-tuc-huong-dan/` | Hướng Dẫn Thủ Tục Bhyt: Hồ Sơ, Quy Trình & Lưu Ý | `làm thẻ bảo hiểm y tế` | làm thẻ bhyt, thủ tục làm bảo hiểm y tế, thủ tục gộp 2 the bảo hiểm y tế | 220 | `Transactional` | Step-by-step How-to & Action Form | `MOFU` | `P1` | Tích hợp Widget tương tác trên Web -> Deeplink mở MoMo App kích hoạt dịch vụ |
| 4 | `/bhyt/kien-thuc-chuyen-sau/` | Tổng Hợp Kinh Nghiệm & Giải Đáp Thắc Mắc Về Bhyt | `trả bảo hiểm y tế` | tracuubhyt, thẻ bảo hiểm y tế, bhyt hộ gia đình | 34,980 | `Informational` | Comprehensive Guide & FAQ | `TOFU` | `P2` | Tích hợp Widget tương tác trên Web -> Deeplink mở MoMo App kích hoạt dịch vụ |

---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |
| 1 | `bhyt` | `bảo hiểm y tế` | Exact Intent Fingerprint: Informational::bao_hiem_y_te | 40,500 |
| 2 | `gia bhyt` | `gia bảo hiểm y tế` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_gia | 1,000 |
| 3 | `bảo hiểm y tế hộ gia đình` | `bhyt hộ gia đình` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_gia_hộ_đình | 1,000 |
| 4 | `giá trị thẻ bhyt` | `giá trị bhyt` | High Semantic Token Similarity (0.75 >= 0.7) | 880 |
| 5 | `số thẻ bảo hiểm y tế` | `số thẻ bhyt` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_số_thẻ | 880 |
| 6 | `bảo hiểm y tế online` | `bhyt online` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_online | 720 |
| 7 | `bảo hiểm y tế giá` | `giá bảo hiểm y tế` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_giá | 480 |
| 8 | `bảo hiểm y tế gia đình` | `bhyt hộ gia đình` | High Semantic Token Similarity (0.75 >= 0.7) | 390 |
| 9 | `bhyt điện tử` | `thẻ bảo hiểm y tế điện tử` | High Semantic Token Similarity (0.75 >= 0.7) | 320 |
| 10 | `số bhyt` | `số bảo hiểm y tế` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_số | 320 |
| 11 | `giá bhyt hộ gia đình` | `bhyt hộ gia đình` | High Semantic Token Similarity (0.8 >= 0.7) | 260 |
| 12 | `giá bảo hiểm y tế hộ gia đình` | `bhyt hộ gia đình` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_gia_giá_hộ_đình | 260 |
| 13 | `giá trị thẻ bảo hiểm y tế` | `giá trị bhyt` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_giá_thẻ_trị | 260 |
| 14 | `số thẻ bảo hiểm y tế là số nào` | `số thẻ bhyt` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_số_thẻ | 260 |
| 15 | `thẻ bhyt điện tử` | `thẻ bảo hiểm y tế điện tử` | Exact Intent Fingerprint: Informational::bao_hiem_y_te_thẻ_tử_điện | 210 |

---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`/bhyt/`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.
