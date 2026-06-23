# QUY TRÌNH HỢP TÁC & TĂNG TRƯỞNG USE CASE TRÊN WEB PLATFORM (S-P-A FRAMEWORK)

| Mã quy trình | QT-WP-01-2026 | Phiên bản | v1.0 |
| :--- | :--- | :--- | :--- |
| **Đơn vị ban hành** | Web Platform Team - Growth Platform Division (GPD) | **Ngày ban hành** | 16/05/2026 |
| **Người phê duyệt** | Head of Web Platform & Web Product Lead | **Hiệu lực** | Từ ngày ban hành |
| **Đối tượng áp dụng** | Các Cell Teams, Inbound Marketing Team, PM/PO, Content Creators | **Trạng thái** | Chính thức ban hành |

---

## I. MỤC ĐÍCH & PHẠM VI ÁP DỤNG

### 1. Mục đích
Quy trình này quy định các bước phối hợp, xây dựng và tối ưu hóa các Use Case/Tính năng mới trên nền tảng Web MoMo (MoSpark). Quy trình nhằm:
*   Chuyển dịch vai trò của Web Platform từ hỗ trợ kỹ thuật thuần túy sang **Nhà cung cấp Dịch vụ Sản phẩm (Product Service Provider)**.
*   Cung cấp các gói giải pháp tăng trưởng (Discovery, Pilot, Growth) giúp các Cell Team tối ưu hóa chỉ số người dùng hoạt động (**MAU**), người dùng phát sinh giao dịch tài chính (**MEU**) và thu hút người dùng mới (**New Users**).
*   Đảm bảo tính nhất quán, chất lượng nội dung (SEO/GEO) và an toàn pháp lý cho mọi sản phẩm phát hành trên tên miền `momo.vn`.

### 2. Phạm vi áp dụng
Áp dụng cho mọi yêu cầu (Request) phát triển Microsite mới, Landing Page mới hoặc nhúng các Tiện ích tương tác (Widgets) phát sinh từ các Cell Teams (Ví Trả Sau, Bảo Hiểm, Dịch Vụ Công...) hoặc Inbound Marketing Team.

---

## II. QUY ĐỊNH CHUNG

1.  **Nguyên tắc "Web as a Product":** Mọi sản phẩm trên Web của MoMo phải được thiết kế và vận hành như một sản phẩm tăng trưởng độc lập, có phễu chuyển đổi Web-to-App (W2A) rõ ràng và được cài đặt đo lường đầy đủ.
2.  **Khung thực thi S-P-A:** Toàn bộ vòng đời của một Use Case từ lúc đề xuất đến lúc tăng tốc quy mô lớn bắt buộc đi qua 3 giai đoạn: **reSearch (Stage S)** ➔ **Pilot (Stage P)** ➔ **Action (Stage A)**.
3.  **Mô hình Phân phối Giải pháp (Growth Solutions):** Sự phối hợp giữa Web Platform và các Cell Team được đóng gói thành 3 giải pháp tương ứng với tiến trình S-P-A:

```text
[Stage S: reSearch]  ───►  [Stage P: Pilot]  ───►  [Stage A: Action]
(Giải pháp Discovery)      (Giải pháp Pilot)       (Giải pháp Growth)
```

---

## III. QUY TRÌNH TRIỂN KHAI CHI TIẾT (S-P-A FLOW)

### BƯỚC 1: TIẾP NHẬN & NGHIÊN CỨU CHIẾN LƯỢC (Stage S: reSearch & Strategy)
*   **Mục tiêu:** Đánh giá dung lượng thị trường tiềm năng (Market Cap) và xác định cơ hội thu hút traffic tự nhiên của sản phẩm.
*   **Trình tự thực hiện:**
    1.  Cell Team gửi phiếu yêu cầu theo biểu mẫu đề xuất (Mẫu ở Mục V), cung cấp đầy đủ tài liệu Business Context và Market Research.
    2.  Web Platform tiếp nhận thông tin, chuẩn hóa chiến lược từ khóa (Keyword Research) dựa trên Market Research của Cell Team và thiết lập SEO/GEO Inventory định hướng.
    3.  Web Platform tổ chức buổi họp đề xuất giải pháp với Cell Team Head để trình bày **SEO/GEO Proposal Deck**.
*   **Đầu ra (Deliverable):** Giải pháp **Discovery** (SEO/GEO Proposal Deck + Bản đồ từ khóa).
*   **Chi phí:** Cell Team được tài trợ **0đ** (đầu tư 1 buổi brief 60 phút).

### BƯỚC 2: XÂY DỰNG & THỬ NGHIỆM MVP (Stage P: Pilot & Plan)
*   **Mục tiêu:** Chứng minh tính khả thi của giải pháp và đo lường baseline tỷ lệ chuyển đổi Web-to-App (W2A CR) với nguồn lực tối thiểu.
*   **Trình tự thực hiện:**
    1.  Web Platform phát triển MVP Mini Web/Landing Page hoặc Widget tương tác dựa trên đặc tả kỹ thuật.
    2.  Thiết lập cấu hình SEO/GEO tiêu chuẩn và hệ thống đo lường (Appsflyer, Umami).
    3.  Chạy thử nghiệm sản xuất 10-15 bài nội dung qua GenAI content pipeline. PM của Cell Team phối hợp kiểm duyệt chất lượng nội dung.
*   **Đầu ra (Deliverable):** Giải pháp **Pilot** (Live Mini Web + Dashboard đo lường traffic và W2A conversion).
*   **Chi phí:** Cell Team được tài trợ tài nguyên kỹ thuật của Web Platform (Cell Team cử nhân sự phối hợp review content 2h/tuần).

### BƯỚC 3: TỐI ƯU HÓA & TĂNG TỐC QUY MÔ (Stage A: Action & Amplifier)
*   **Mục tiêu:** Chiếm lĩnh vị trí Top 1 - Top 3 trên các công cụ tìm kiếm và AI Search Engines, tối đa hóa lượng MAU/MEU chuyển đổi thực tế.
*   **Trình tự thực hiện:**
    1.  Sau khi giai đoạn Pilot nghiệm thu đạt chỉ số cam kết, Cell Team Head phê duyệt ngân sách đầu tư chính thức.
    2.  Web Platform thực hiện sản xuất nội dung hàng loạt (50-200 bài/tháng) qua GenAI engine kết hợp nhân sự QC.
    3.  Vận hành các chiến dịch SEO Off-page qua Vendor/Partner được phê duyệt và triển khai SEM/Programmatic SEO để phủ sóng địa phương.
*   **Đầu ra (Deliverable):** Giải pháp **Growth** (Traffic quy mô lớn + Báo cáo đóng góp MAU/MEU định kỳ).
*   **Chi phí:** **Cell Team đầu tư 100% ngân sách thực tế** cho các hoạt động Media, SEM, Content & SEO Vendor.

---

## IV. TIÊU CHUẨN CHUYỂN GIAI ĐOẠN & CỔNG KIỂM SOÁT (STAGE GATES)

Quy trình S-P-A áp dụng cơ chế "Bóc vỏ hành" - chỉ cho phép nâng cấp dự án khi vượt qua các chốt kiểm định sau:

```
[ stage S ]  ──(Gate 1)──►  [ stage P ]  ──(Gate 2)──►  [ stage A ]
```

*   **Chốt kiểm duyệt 1 (Gate 1: Duyệt sang Pilot):**
    *   [ ] Tổng dung lượng tìm kiếm (Search Volume) trong SEO Inventory phải đạt tối thiểu > 10,000 lượt/tháng.
    *   [ ] Đã hoàn thành và kiểm duyệt file **Business Context (Markdown)** cung cấp từ Cell Team.
    *   [ ] PO của Cell Team ký cam kết dành tối thiểu 2 giờ/tuần để đồng hành kiểm duyệt nghiệp vụ sản phẩm.
*   **Chốt kiểm duyệt 2 (Gate 2: Duyệt sang Scale/Growth):**
    *   [ ] Dữ liệu đo lường thực tế của MVP chứng minh tỷ lệ chuyển đổi Click-to-App đạt tối thiểu > 5%.
    *   [ ] Hệ thống tracking (Appsflyer, Umami) đã ghi nhận dữ liệu chính xác trên dashboard.
    *   [ ] Cell Team Head chính thức phê duyệt và ký cấp ngân sách chạy Off-page/Vendor.

---

## V. BIỂU MẪU ĐỀ XUẤT ĐẦU VÀO CHUẨN HÓA (S-P-A REQUIREMENT TEMPLATE)
*Các đơn vị Cell Team/Inbound sao chép biểu mẫu này, điền đầy đủ thông tin gửi về Web Platform Team để khởi động quy trình.*

```markdown
# PHIẾU ĐỀ XUẤT PHÁT TRIỂN USE CASE (MÔ HÌNH S-P-A)
> - **Đơn vị đề xuất:** [Tên Cell Team]
> - **Product Owner (PO) phụ trách:** [Họ và tên - Email - Slack]
> - **Dự án/Sản phẩm in-app liên kết:** [Mô tả ngắn & link sản phẩm trong app]
> - **Mục tiêu ưu tiên cốt lõi:** [Tăng MAU / Tăng MEU / Thu hút New Users]

---

### 1. GIAI ĐOẠN S (reSearch & Strategy): Dữ liệu & Bối cảnh ban đầu
*   **Dự kiến bối cảnh tìm kiếm của người dùng:** 
    *   *Khi người dùng gặp tình huống:* [Mô tả bối cảnh ngoài đời, ví dụ: Lo lắng bị camera phạt nguội khi đi qua ngã tư]
    *   *Họ sẽ tìm kiếm trên mạng để:* [Mục tiêu tìm kiếm, ví dụ: Check nhanh xem biển số xe của mình có bị phạt nguội không]
    *   *Để đạt được kết quả:* [Ví dụ: Chủ động nộp phạt sớm để đi đăng kiểm đúng hạn]
*   **Gợi ý danh sách từ khóa ban đầu từ Cell Team (nếu có):** [Nhập các cụm từ khóa định hướng]

---

### 2. GIAI ĐOẠN P (Pilot & Plan): Định hướng MVP & Tương tác
*   **Đề xuất tiện ích tương tác (Widget):** [Ví dụ: Bảng tính toán số tiền lãi tiết kiệm nhận được, bộ trắc nghiệm phân loại tính cách tài chính...]
*   **Thông tin nghiệp vụ cần chuyển tự động sang App (Zero-Party Data):** [Ví dụ: Số tiền muốn gửi tiết kiệm, Kỳ hạn lựa chọn]
*   **Cam kết nguồn lực phối hợp:**
    *   [ ] Cam kết cử PO tham gia review content tối thiểu 2 giờ/tuần.
    *   [ ] Đã sẵn sàng cung cấp file đặc tả sản phẩm làm Business Context.

---

### 3. GIAI ĐOẠN A (Action & Amplifier): Kế hoạch Quy mô lớn
*   **Kế hoạch ngân sách dự kiến cho giai đoạn Scale:** [Dự kiến ngân sách chi trả cho quảng cáo Google Search hoặc thuê ngoài viết bài chuẩn SEO/GEO]
```

---

## VI. ĐIỀU KHOẢN THI HÀNH

1.  **Hiệu lực thi hành:** Quy trình này có hiệu lực áp dụng kể từ ngày ký ban hành. Mọi hoạt động phát triển Use Case trên Web Platform từ thời điểm này bắt buộc tuân thủ quy trình.
2.  **Sửa đổi và bổ sung:** Nội dung quy trình sẽ được rà soát và cập nhật định kỳ mỗi 6 tháng để tối ưu hóa hiệu năng vận hành. Mọi đề xuất điều chỉnh gửi về đầu mối quản trị Web Platform.
3.  **Phân quyền trách nhiệm hỗ trợ:**
    *   **Phê duyệt & Điều phối:** Web Product Lead
    *   **Triển khai kỹ thuật:** Web Platform Developers
    *   **Cài đặt Tracking:** DA/Tracking Specialist


