# KẾ HOẠCH NỘI DUNG CHUẨN (CONTENT PLAN V2 - SHIELDED) - USE CASE: TUYEN SINH

- **Use Case:** Tuyen Sinh
- **Phân Khối Ngành:** student
- **URL Pillar Hub:** `/tuyen-sinh/`
- **Tổng từ khóa thô ban đầu:** 487 từ khóa
- **Từ khóa nhiễu bị loại bỏ:** 0 từ khóa
- **Từ khóa trùng Intent được gom cụm (Shielded):** 14 từ khóa
- **Số lượng URLs phân bổ:** 7 URLs (1 Pillar Hub + 6 Cluster Pages)
- **Quy tắc bảo vệ:** Mỗi URL giải quyết duy nhất 1 Intent độc lập. Các từ khóa cùng Intent đã được gom thành Secondary Synonyms (Zero Keyword Cannibalization).

---

## 1. BẢNG KẾ HOẠCH BÀI VIẾT CHI TIẾT (ACTIONABLE CONTENT PLAN)

| STT | URL Slug | Tiêu Đề Bài Viết / Trang Đích | Primary Keyword | Secondary Synonyms (Đã Gom Chống Ăn Thịt) | Search Volume | Search Intent | Định Dạng Nội Dung | Phễu | Ưu Tiên | Điểm Chạm Web-to-App (CTA Hook) |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- | :---: | :---: | :--- |
| 1 | `/tuyen-sinh/` | Cẩm Nang & Bảng Tra Cứu Tuyển Sinh & Xét Tuyển Đại Học Toàn Diện | `ts10 hcm edu vn` | tuyển sinh 247, hcmue online, thongtindaotao | 49,500 | `Informational` | Pillar Hub Page + Interactive Widget | `TOFU` | `P0` | None |
| 2 | `/tuyen-sinh/tuyen-sinh/` | Tuyển sinh & Xét tuyển Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết | `tuyển sinh 247` | thi tốt nghiệp, thi tốt nghiệp thpt, tuyển sinh | 193,920 | `Informational` | Educational Guide & FAQ | `TOFU` | `P0` | None |
| 3 | `/tuyen-sinh/truong-nganh-hoc/` | Trường & Ngành học Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết | `trường thpt trần đại nghĩa` | trường cao đẳng cảnh sát nhân dân 2, trường sĩ quan phòng hóa, trường cao đẳng nghề kỹ thuật công nghệ | 45,530 | `Informational` | Educational Guide & FAQ | `TOFU` | `P0` | None |
| 4 | `/tuyen-sinh/so-sanh/` | So sánh & Đánh giá Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết | `thi đánh giá năng lực` | đánh giá năng lực đợt 2, bài thi đánh giá năng lực của bộ công an, bài thi đánh giá năng lực bộ công an | 9,380 | `Commercial` | Comparison Table & Evaluation | `MOFU` | `P1` | None |
| 5 | `/tuyen-sinh/sinh-vien-cong-thong-tin/` | Sinh viên & Cổng thông tin Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết | `hactech đăng nhập` | sinh viên fpt | 5,660 | `Navigational` | Educational Guide & FAQ | `TOFU` | `P0` | None |
| 6 | `/tuyen-sinh/viec-lam-ky-nang/` | Việc làm & Kỹ năng Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết | `phenikaa tuyển dụng` | tuyển dụng giảng viên, vinuni tuyển dụng | 3,080 | `Informational` | Educational Guide & FAQ | `TOFU` | `P0` | None |
| 7 | `/tuyen-sinh/hoc-phi-hoc-bong/` | Học phí & Học bổng Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết | `đh kinh tế tài chính học phí` | học phí thương mại, học phí tài chính ngân hàng, thi học bổng fpt | 680 | `Informational` | Educational Guide & FAQ | `TOFU` | `P2` | None |

---

## 2. NHẬT KÝ BẢO VỆ CHỐNG ĂN THỊT TỪ KHÓA (CANNIBALIZATION SHIELD LOG)

Dưới đây là các từ khóa có Search Intent và thực thể trùng lặp đã được tự động gom về bài viết tương ứng thay vì tách bài mới:

| STT | Từ Khóa Bị Trùng Lặp (Merged) | Gom Về Primary Keyword | Lý Do Hợp Nhất (Canonical Fingerprint / Similarity) | Volume Được Bảo Toàn |
| :---: | :--- | :--- | :--- | :---: |

---

## 3. NGUYÊN TẮC LIÊN KẾT NỘI BỘ (INTERNAL LINKING ARCHITECTURE)

1. **Liên kết 2 chiều Pillar <-> Cluster:**
   - Trang Pillar (`/tuyen-sinh/`) liên kết bối cảnh tới tất cả các Cluster Pages.
   - 100% Cluster Pages bắt buộc đặt anchor text tự nhiên trong 100 từ đầu tiên dẫn về Pillar Page.
2. **Liên kết ngang giữa các Cluster:**
   - Trang Tính toán (`cong-cu-tinh-toan/`) liên kết sang trang So sánh (`so-sanh-danh-gia/`).
   - Trang Thủ tục (`thu-tuc-huong-dan/`) trỏ sang trang An toàn bảo mật (`an-toan-bao-mat/`).
3. **Móc chuyển đổi Web-to-App:**
   - Tích hợp Widget tương tác trực tiếp trên Web. Deeplink dẫn vào App MoMo để kích hoạt dịch vụ thực tế.

---

## 4. CONTENT BRIEF & DÀN Ý H2/H3 ENTITY CHECKLIST CHO TỪNG BÀI

Dưới đây là cấu trúc dàn ý chuẩn E-E-A-T và chỉ tiêu dung lượng bài viết để đội ngũ nội dung triển khai:

### Bài 1: `Cẩm Nang & Bảng Tra Cứu Tuyển Sinh & Xét Tuyển Đại Học Toàn Diện`
- **URL Slug:** `/tuyen-sinh/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `ts10 hcm edu vn`
- **Secondary Synonyms:** tuyển sinh 247, hcmue online, thongtindaotao, thi tốt nghiệp
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về ts10 hcm edu vn
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về ts10 hcm edu vn
   - ### H3 5.1: Tuyển sinh 247?
   - ### H3 5.2: Hcmue online?
   - ### H3 5.3: Thongtindaotao?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 2: `Tuyển sinh & Xét tuyển Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/tuyen-sinh/tuyen-sinh/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `tuyển sinh 247`
- **Secondary Synonyms:** thi tốt nghiệp, thi tốt nghiệp thpt, tuyển sinh, đăng ký tuyển sinh
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về tuyển sinh 247
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về tuyển sinh 247
   - ### H3 5.1: Thi tốt nghiệp?
   - ### H3 5.2: Thi tốt nghiệp thpt?
   - ### H3 5.3: Tuyển sinh?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 3: `Trường & Ngành học Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/tuyen-sinh/truong-nganh-hoc/`
- **Chỉ tiêu độ dài:** `2,500 - 3,500 từ` (Cấp bậc: `Master Hub Pillar`)
- **Primary Keyword:** `trường thpt trần đại nghĩa`
- **Secondary Synonyms:** trường cao đẳng cảnh sát nhân dân 2, trường sĩ quan phòng hóa, trường cao đẳng nghề kỹ thuật công nghệ, trường phổ thông năng khiếu
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về trường thpt trần đại nghĩa
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về trường thpt trần đại nghĩa
   - ### H3 5.1: Trường cao đẳng cảnh sát nhân dân 2?
   - ### H3 5.2: Trường sĩ quan phòng hóa?
   - ### H3 5.3: Trường cao đẳng nghề kỹ thuật công nghệ?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 4: `So sánh & Đánh giá Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/tuyen-sinh/so-sanh/`
- **Chỉ tiêu độ dài:** `1,800 - 2,500 từ` (Cấp bậc: `Comparison & Review`)
- **Primary Keyword:** `thi đánh giá năng lực`
- **Secondary Synonyms:** đánh giá năng lực đợt 2, bài thi đánh giá năng lực của bộ công an, bài thi đánh giá năng lực bộ công an, kết quả thi đánh giá năng lực 2022
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về thi đánh giá năng lực
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: So sánh chi tiết các lựa chọn hàng đầu trên thị trường hiện nay
   - ### H3 3.1: Ưu và nhược điểm của từng đơn vị cung cấp
   - ## H2 4: Lời khuyên nên chọn giải pháp nào tối ưu nhất theo nhu cầu
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về thi đánh giá năng lực
   - ### H3 5.1: Đánh giá năng lực đợt 2?
   - ### H3 5.2: Bài thi đánh giá năng lực của bộ công an?
   - ### H3 5.3: Bài thi đánh giá năng lực bộ công an?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 5: `Sinh viên & Cổng thông tin Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/tuyen-sinh/sinh-vien-cong-thong-tin/`
- **Chỉ tiêu độ dài:** `1,200 - 1,600 từ` (Cấp bậc: `Educational Spoke`)
- **Primary Keyword:** `hactech đăng nhập`
- **Secondary Synonyms:** sinh viên fpt
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về hactech đăng nhập
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về hactech đăng nhập
   - ### H3 5.1: Sinh viên fpt?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 6: `Việc làm & Kỹ năng Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/tuyen-sinh/viec-lam-ky-nang/`
- **Chỉ tiêu độ dài:** `1,200 - 1,600 từ` (Cấp bậc: `Educational Spoke`)
- **Primary Keyword:** `phenikaa tuyển dụng`
- **Secondary Synonyms:** tuyển dụng giảng viên, vinuni tuyển dụng
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về phenikaa tuyển dụng
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về phenikaa tuyển dụng
   - ### H3 5.1: Tuyển dụng giảng viên?
   - ### H3 5.2: Vinuni tuyển dụng?
   - ## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo

### Bài 7: `Học phí & Học bổng Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết`
- **URL Slug:** `/tuyen-sinh/hoc-phi-hoc-bong/`
- **Chỉ tiêu độ dài:** `1,200 - 1,600 từ` (Cấp bậc: `Educational Spoke`)
- **Primary Keyword:** `đh kinh tế tài chính học phí`
- **Secondary Synonyms:** học phí thương mại, học phí tài chính ngân hàng, thi học bổng fpt, học phí kinh tế tài chính
- **Dàn ý H2/H3 bắt buộc (SEO Entity Checklist):**
   - ## H2 1: Tổng quan & Khái niệm cốt lõi về đh kinh tế tài chính học phí
   - ## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất
   - ## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi
   - ## H2 4: Những sai lầm thường gặp và cách phòng tránh
   - ## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về đh kinh tế tài chính học phí
   - ### H3 5.1: Học phí thương mại?
   - ### H3 5.2: Học phí tài chính ngân hàng?
   - ### H3 5.3: Thi học bổng fpt?
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
      "name": "Student",
      "item": "https://momo.vn/student"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Tuyen Sinh",
      "item": "https://momo.vn/tuyen-sinh"
    }
  ]
}
```

### B. FAQPage Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "name": "Hỏi đáp thường gặp về Tuyen Sinh",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Tuyển sinh & Xét tuyển Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về tuyển sinh 247 được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "Trường & Ngành học Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về trường thpt trần đại nghĩa được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
      }
    },
    {
      "@type": "Question",
      "name": "So sánh & Đánh giá Tuyển Sinh & Xét Tuyển Đại Học: Hướng Dẫn & Tra Cứu Chi Tiết?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thông tin chi tiết về thi đánh giá năng lực được cập nhật chính xác và minh bạch tại MoMo Web Platform. Người dùng có thể tra cứu và thực hiện tiện ích trực tiếp trên ứng dụng MoMo."
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
| 1 | `Cao Đẳng & Tuyển Sinh Cao Đẳng` | `/cao-dang/` | `cao đẳng` | `0.25` | 22,430 |
| 2 | `Đại Học & Trường Đại Học` | `/dai-hoc/` | `mydtu` | `0.238` | 2,288,060 |
| 3 | `Việc Làm Sinh Viên & Bán Thời Gian` | `/viec-lam-sinh-vien/` | `việc làm tiếng hàn` | `0.143` | 34,050 |
| 4 | `Điểm Chuẩn & Thi Tốt Nghiệp THPT` | `/diem-chuan/` | `thi tốt nghiệp thpt` | `0.114` | 226,460 |

### C. Cầu nối liên kết xuyên ngành (Cross-Silo Bridges):
| Thứ tự | Use Case Đích | Phân Khối Ngành | Đường Dẫn Khuyến Nghị | Anchor Text Móc Nối | Search Volume |
| :---: | :--- | :--- | :--- | :--- | :---: |

---

## 7. TỐI ƯU HÓA TÌM KIẾM TẠO SINH (GEO & AI DIRECT ANSWERS)

Cung cấp sẵn khối thông tin trích dẫn phục vụ trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini:

### A. Đoạn trích dẫn trực tiếp (Direct Answer Snippet - 40-60 từ):
> "Ts10 hcm edu vn là giải pháp tiện ích số trên Nền tảng Web MoMo, cho phép người dùng thực hiện giao dịch trực tuyến tuyen sinh một cách nhanh chóng, minh bạch và chính xác theo thời gian thực. Dịch vụ liên kết với các đối tác uy tín hàng đầu, đảm bảo chuẩn bảo mật PCI DSS quốc tế và hỗ trợ thao tác liền mạch từ trình duyệt Web đến Ứng dụng MoMo trong 1-3 phút."

### B. Bảng thuộc tính thực thể (Entity Knowledge Graph Factsheet):
| Thuộc Tính Thực Thể | Giá Trị Chuẩn Hóa |
| :--- | :--- |
| Phân loại giải pháp | Tiện ích Web Student - MoMo Web Platform |
| Đối tượng áp dụng | Toàn bộ người dùng cá nhân có nhu cầu tra cứu và giao dịch trực tuyến |
| Thời gian xử lý | Xử lý tức thì (Real-time), hỗ trợ 24/7 không phụ thuộc giờ hành chính |
| Hạ tầng kỹ thuật | Kết nối API trực tiếp từ hệ thống đối tác liên kết chính thức |
| Tiêu chuẩn bảo mật | Bảo mật đa tầng, đạt chứng chỉ bảo mật quốc tế PCI DSS Level 1 |
| Kênh thao tác liền mạch | Trình duyệt Web (Desktop/Mobile) kết hợp chuyển tiếp Web-to-App MoMo |
