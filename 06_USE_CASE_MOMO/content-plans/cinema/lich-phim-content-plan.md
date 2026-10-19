# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - USE CASE: LICH PHIM

- **Use Case:** Lich Phim
- **Phân Khối Ngành:** cinema
- **URL Pillar Hub:** `/lich-phim/`
- **Tổng từ khóa thô ban đầu:** 2,544 từ khóa
- **Từ khóa nhiễu bị loại bỏ:** 0 từ khóa
- **Từ khóa trùng Intent được gom cụm (Shielded):** 89 từ khóa
- **Số lượng URLs phân bổ:** 3 URLs (1 Pillar Hub + 2 Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Ưu Tiên | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| 1 | `/lich-phim/` | Cẩm Nang & Bảng Tra Cứu Lịch Chiếu Phim Rạp Toàn Diện | `lịch chiếu phim` | lịch chiếu phim cgv, cgv lịch chiếu, lịch chiếu phim lotte | 74,000 | `Informational` | Pillar Hub Page + Interactive Widget | `TOFU` | `P0` | Tra Cứu Lịch Phim & Đặt Vé Tức Thì -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 2 | `/lich-phim/lich-phim-theo-rap/` | Lịch Phim Theo Rạp CGV / Lotte / BHD Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `lich chiếu cgv` | rạp cgv, phim cgv, giá vé cgv | 116,710 | `Informational` | Educational Guide & FAQ | `TOFU` | `P1` | Tra Cứu Lịch Phim & Đặt Vé Tức Thì -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |
| 3 | `/lich-phim/cam-nang/` | Cẩm nang & Hỏi đáp Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết | `lịch phim` | chieuphimquocgia, lịch phim vincom, lịch phim beta | 27,820 | `Informational` | Educational Guide & FAQ | `TOFU` | `P0` | Tra Cứu Lịch Phim & Đặt Vé Tức Thì -> Deeplink: momo://cinema-booking -> Event: web_cinema_booking_btn_click |

---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |

---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`/lich-phim/`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.

---

## 4. CONTENT BRIEF & DÀN Ý H2/H3 ENTITY CHECKLIST CHO TỪNG BÀI

Dưới đây là cấu trúc dàn ý chuẩn E-E-A-T và chỉ tiêu dung lượng bài viết để đội ngũ nội dung triển khai:

### Bài 1: `Cẩm Nang & Bảng Tra Cứu Lịch Chiếu Phim Rạp Toàn Diện`
- **URL Slug:** `/lich-phim/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `lịch chiếu phim`
- **Secondary Synonyms:** lịch chiếu phim cgv, cgv lịch chiếu, lịch chiếu phim lotte, lịch chiếu phim galaxy
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về lịch chiếu phim
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về lịch chiếu phim
   - ### H3 5.1: Lịch chiếu phim cgv?
   - ### H3 5.2: Cgv lịch chiếu?
   - ### H3 5.3: Lịch chiếu phim lotte?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 2: `Lịch Phim Theo Rạp CGV / Lotte / BHD Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/lich-phim/lich-phim-theo-rap/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `lich chiếu cgv`
- **Secondary Synonyms:** rạp cgv, phim cgv, giá vé cgv, rạp lotte
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về lich chiếu cgv
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về lich chiếu cgv
   - ### H3 5.1: Rạp cgv?
   - ### H3 5.2: Phim cgv?
   - ### H3 5.3: Giá vé cgv?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 3: `Cẩm nang & Hỏi đáp Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/lich-phim/cam-nang/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `lịch phim`
- **Secondary Synonyms:** chieuphimquocgia, lịch phim vincom, lịch phim beta, lịch phim starlight
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về lịch phim
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về lịch phim
   - ### H3 5.1: Chieuphimquocgia?
   - ### H3 5.2: Lịch phim vincom?
   - ### H3 5.3: Lịch phim beta?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

---

## 5. DỮ LIỆU CẤU TRÚC JSON-LD (STRUCTURED DATA SCHEMA) CHO WEB DEV

Đội ngũ Frontend tại `hubs-momo` có thể sao chép trực tiếp 2 khối Schema này vào thẻ `<script type="application/ld+json">` của trang:

### A. BreadcrumbList Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Trang chủ",
      "item": "https://momo.vn"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Cinema",
      "item": "https://momo.vn/cinema"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Lich Phim",
      "item": "https://momo.vn/lich-phim"
    }
  ]
}
```

### B. FAQPage Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "name": "Hỏi đáp thường gặp về Lich Phim",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Lịch Phim Theo Rạp CGV / Lotte / BHD Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về lich chiếu cgv được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Cẩm nang & Hỏi đáp Lịch Chiếu Phim Rạp: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về lịch phim được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    }
  ]
}
```

---

## 6. KIẾN TRÚC LIÊN KẾT NỘI BỘ (INTERNAL LINKING & SILO MATRIX)

Phân tầng dòng chảy uy tín trang (PageRank) và định vị chuyên môn chủ đề (Topic Authority):

### A. Parent Hub Pillar:
- **Trang Cột Trụ Cấp 1:** `[Tiện Ích Nền Tảng](/tien-ich)`
- **Anchor Text Mỏ Neo:** `"Hệ sinh thái tiện ích Web MoMo"`

### B. Liên kết ngang cùng ngành (Peer In-Silo):
| Thứ tự | Use Case Bổ Trợ | Đường Dẫn Khuyến Nghị | Anchor Text Tự Nhiên | Độ Tương Đồng | Search Volume |
| :---: | :--- | :--- | :--- | :---: | :---: |
| 1 | `Đặt Vé Phim Online` | `/dat-phim/` | `đặt vé cgv` | `0.158` | 14,050 |
| 2 | `Rạp Chiếu Phim & Cụm Rạp` | `/rap/` | `phim chiếu rạp` | `0.105` | 1,229,160 |
| 3 | `Phim Chiếu Rạp Mới Nhất` | `/phim/` | `phim` | `0.1` | 5,409,760 |
| 4 | `Giá Vé Xem Phim & Khuyến Mãi` | `/ve-xem-phim/` | `vé xem phim` | `0.033` | 0 |

### C. Cầu nối liên kết xuyên ngành (Cross-Silo Bridges):
| Thứ tự | Use Case Đích | Phân Khối Ngành | Đường Dẫn Khuyến Nghị | Anchor Text Móc Nối | Search Volume |
| :---: | :--- | :--- | :--- | :--- | :---: |

---

## 7. TỐI ƯU HÓA TÌM KIẾM TẠO SINH (GEO & AI DIRECT ANSWERS)

Cung cấp sẵn khối thông tin trích dẫn phục vụ trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini:

### A. Đoạn trích dẫn trực tiếp (Direct Answer Snippet - 40-60 từ):
> "Lịch chiếu phim là giải pháp tiện ích số trên Nền tảng Web MoMo, cho phép người dùng thực hiện giao dịch trực tuyến lich phim một cách nhanh chóng, minh bạch và chính xác theo thời gian thực. Dịch vụ liên kết với các đối tác uy tín hàng đầu, đảm bảo chuẩn bảo mật PCI DSS quốc tế và hỗ trợ thao tác liền mạch từ trình duyệt Web đến Ứng dụng MoMo trong 1-3 phút."

### B. Bảng thuộc tính thực thể (Entity Knowledge Graph Factsheet):
| Thuộc Tính Thực Thể | Giá Trị Chuẩn Hóa |
| :--- | :--- |
| Phân loại giải pháp | Tiện ích Web Cinema - MoMo Web Platform |
| Đối tượng áp dụng | Toàn bộ người dùng cá nhân có nhu cầu tra cứu và giao dịch trực tuyến |
| Thời gian xử lý | Xử lý tức thì (Real-time), hỗ trợ 24/7 không phụ thuộc giờ hành chính |
| Hạ tầng kỹ thuật | Kết nối API trực tiếp từ hệ thống đối tác liên kết chính thức |
| Tiêu chuẩn bảo mật | Bảo mật đa tầng, đạt chứng chỉ bảo mật quốc tế PCI DSS Level 1 |
| Kênh thao tác liền mạch | Trình duyệt Web (Desktop/Mobile) kết hợp chuyển tiếp Web-to-App MoMo |
