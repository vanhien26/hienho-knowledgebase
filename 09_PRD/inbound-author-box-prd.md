# TÀI LIỆU YÊU CẦU SẢN PHẨM & BỐI CẢNH NGHIỆP VỤ (PRD & BUSINESS CONTEXT) - WEB CHANNEL
*Bắt buộc Cell Team điền đầy đủ và cung cấp cho Web Platform Team trước khi tiến hành triển khai dự án*

## THÔNG TIN CHUNG (Metadata)
> *   **Tên dự án / Use Case:** Tích hợp khối thông tin tác giả (Author Box) vào trang Blog
> *   **Đơn vị đề xuất:** Inbound Marketing Team
> *   **Product Owner (PO) phụ trách:** Nguyễn Mai Phương - PO Inbound Marketing
> *   **Dự án / Sản phẩm In-App liên kết:** Không (Tính năng thuộc CMS Blog của Web Platform)
> *   **Giai đoạn S-P-A dự kiến:** Stage P: Pilot (Chạy thử nghiệm trên 1 Microsite Tài chính trước khi áp dụng toàn bộ momo.vn)
> *   **Loại yêu cầu (Chọn các ô áp dụng):**
>     *   [ ] **1. Tính năng mới (New Feature):** Tạo mới Microsite, Widget hoặc trang tương tác.
>     *   [x] **2. Cải tiến (Improvement):** Nâng cấp, tối ưu hóa giao diện/tính năng hiện tại.
>     *   [x] **3. Thay đổi cấu trúc (Structural Change):** Thay đổi bố cục layout, phân cấp URL hoặc site structure.
>     *   [ ] **4. Bổ sung thông tin (Content Update):** Cập nhật bài viết, thông tin tĩnh, FAQs hoặc SEO/GEO content.

---

## I. RELATED DOCUMENTS
*Các liên kết tài liệu nghiệp vụ, thiết kế hiện có từ phía Cell Team (Vui lòng đính kèm link trước khi mô tả chi tiết).*

*   [x] **Figma Design Link:** https://figma.com/file/inbound-author-box-design-mockup
*   [x] **Tài liệu nghiệp vụ (BRD / PRD in-app):** https://wiki.momo.vn/display/SEO/EEAT+Guidelines+2026
*   [ ] **Tài sản thương hiệu (Brand Assets / Guideline riêng):** N/A
*   [ ] **Tài liệu đặc tả API (Swagger / Postman):** N/A

---

## II. PROBLEM STATEMENT & PRODUCT VISION

### 1. Hiện trạng & Vấn đề cần giải quyết (Problem Statement)
Các bài viết trên Blog momo.vn hiện tại hiển thị dưới dạng "vô danh" (không có tên người viết, không có thông tin chuyên gia kiểm duyệt). Điều này làm giảm điểm chất lượng E-E-A-T (Chuyên môn & Độ tin cậy) theo quy chuẩn của Google Search, khiến bài viết dễ bị tụt hạng khi Google cập nhật thuật toán Core Update. Đồng thời, AI Search (ChatGPT, Perplexity) có xu hướng từ chối trích dẫn (Citation) các nội dung không có định danh tác giả rõ ràng.

### 2. Tầm nhìn sản phẩm (Product Vision)
Mọi bài viết Blog trên Web MoMo được định danh tác giả chuyên môn và chuyên gia kiểm duyệt uy tín. Trở thành nguồn tri thức đáng tin cậy nhất được Google xếp hạng cao và các AI Search Engine ưu tiên trích dẫn làm câu trả lời chính thống.

---

## III. JOBS-TO-BE-DONE (JTBD)
*Bóc tách rõ nhu cầu của người dùng Web thành 2 lớp: Nhu cầu tương tác tính năng trên trang và Nhu cầu tìm kiếm thông tin trên Search Engine.*

### 1. Product JTBD (Nhu cầu tương tác với Widget/Công cụ trên Web)
*   **Khi bối cảnh xảy ra (When...):** Khi tôi đang đọc một bài viết hướng dẫn đăng ký tài khoản Ví Trả Sau trên Web MoMo và băn khoăn liệu các thông tin tài chính này có chính xác và an toàn để làm theo hay không.
*   **Hành động trên Web (I want to...):** Tôi muốn nhìn thấy ngay phần giới thiệu chi tiết về tác giả viết bài này cùng thông tin chuyên gia tài chính đã kiểm duyệt nội dung ở cuối bài viết.
*   **Kết quả kỳ vọng (So I can...):** Để tôi yên tâm tin tưởng vào kiến thức được cung cấp, từ đó tự tin click vào nút đăng ký sản phẩm mà không ngần ngại.

### 2. SEO/GEO JTBD (Nhu cầu tìm kiếm thông tin ngoài App)
*   **Từ khóa / Câu hỏi nguồn (Search Intent / Keyword):** "cách đăng ký ví trả sau momo an toàn", "chuyên gia tài chính đánh giá ví trả sau momo"
*   **Khi người dùng tìm kiếm (When...):** Khi tôi tra cứu trên Google/ChatGPT về độ uy tín và tính pháp lý của sản phẩm Ví Trả Sau.
*   **Nội dung họ cần đọc (I want to...):** Tôi muốn tìm thấy bài viết của MoMo có cấu trúc dữ liệu tác giả (Schema Author) đạt điểm E-E-A-T cao, hiển thị ở Top 1 Google hoặc được ChatGPT trích dẫn trực tiếp tên tác giả từ Web MoMo.
*   **Hành vi chuyển đổi kỳ vọng (So I can...):** Để tôi click vào bài viết của MoMo thay vì đối thủ, sau đó thực hiện chuyển đổi mở app sử dụng dịch vụ.

---

## IV. OBJECTIVES & SUCCESS METRICS
*Đo lường hiệu quả kỳ vọng đạt được của dự án.*

| Chỉ số (KPI) | Trước thay đổi (Baseline) | Mục tiêu sau thay đổi (Target) | Thời gian đo lường (Timeframe) |
|---|---|---|---|
| Số lượt nhấp mở App (W2A Clicks) | 5,000 click/tháng | > 6,000 click/tháng | Q3/2026 |
| Tỷ lệ chuyển đổi Web-to-App (W2A CR) | 4.2% | > 5.0% | Q3/2026 |
| SEO Traffic (Pageviews) | 80,000 views/tháng | > 100,000 views/tháng | Q3/2026 |
| AI Search Citation Rate (đo qua SoV) | 0% | > 25% | Q3/2026 |

---

## V. BUSINESS CONTEXT
*Cung cấp thông tin nghiệp vụ cốt lõi để đội ngũ phát triển hiểu rõ về sản phẩm/dịch vụ.*

### 1. Mô tả nghiệp vụ sản phẩm (Product Description & Rules)
Author Box là một khối thông tin động hiển thị ở cuối bài viết Blog. Nội dung bao gồm: Ảnh chân dung tác giả (Avatar), Họ tên, Chức danh chuyên môn (ví dụ: Financial Writer), tiểu sử ngắn (Bio < 150 ký tự), và link LinkedIn cá nhân. 
Đối với các bài viết thuộc nhóm tài chính nhạy cảm (YMYL), cần hiển thị thêm khối "Reviewed by: [Tên chuyên gia]" bên cạnh khối tác giả.

### 2. Giá trị cốt lõi & Thông điệp chính (Value Propositions & Key Messages)
"Nội dung được viết bởi chuyên gia – Kiểm duyệt kỹ lưỡng trước khi xuất bản."

### 3. Giới hạn & Các từ cấm (Constraints & Blacklist)
*   *Giới hạn:* Tác giả bắt buộc phải là nhân sự thuộc MoMo hoặc cộng tác viên được Inbound Team xác thực chuyên môn. Không được sử dụng tác giả ảo hoặc ảnh mạng không bản quyền làm avatar.
*   *Từ cấm (Blacklist):* Tránh ghi chức danh của chuyên gia kiểm duyệt quá khoa trương (ví dụ: "Chuyên gia tài chính số 1 Việt Nam").

---

## VI. FEATURE REQUIREMENTS BY TYPE
*(Vui lòng điền mục tương ứng với Loại yêu cầu đã chọn ở phần Metadata)*

### LOẠI 2: CẢI TIẾN (IMPROVEMENT)
*   **Chi tiết thay đổi:** 
    *   Tích hợp hệ thống quản lý danh sách Tác giả (Authors) vào CMS MoSpark. Khi biên tập bài viết, Content Writer có thể chọn Tác giả từ danh sách có sẵn.
    *   Hiển thị thông tin tóm tắt ở đầu bài (dưới Tiêu đề): Avatar nhỏ + Tên tác giả + Link LinkedIn.
    *   Hiển thị khung thông tin chi tiết (Author Box) ở cuối bài viết (sau phần nội dung chính, trước phần bình luận/bài viết liên quan) theo đúng mockup Figma.

### LOẠI 3: THAY ĐỔI CẤU TRÚC (STRUCTURAL CHANGE)
*   **Bố cục layout mới:** 
    *   Chèn khối Author Box (kích thước 100% width trên mobile, float left trên desktop) vào template chung của CMS Blog.
    *   Đồng bộ mã nguồn HTML tự động render thẻ dữ liệu cấu trúc `Schema.org/Person` (Tác giả) và `Schema.org/Reviewer` (Người kiểm duyệt) vào mã code để Google Bot đọc hiểu.

---

## VII. W2A CONVERSION & DATA REQUIREMENTS

### 1. Luồng chuyển đổi Web-to-App (W2A Trigger Points)
*Không thay đổi (Hệ thống CTA mở app in-app của bài viết giữ nguyên theo cấu hình cũ).*

### 2. API Nghiệp Vụ & Fallback Logic
*   **Tài liệu API:** CMS MoSpark sẽ lấy dữ liệu Author từ bảng database cục bộ (không cần gọi API của đối tác thứ ba).
*   **Kịch bản khi lỗi (Fallback):** Nếu bài viết không được gán tác giả cụ thể, hệ thống sẽ tự động hiển thị tác giả mặc định là "Đội ngũ Biên tập MoMo" kèm Avatar là logo MoMo.

---

## VIII. GOVERNANCE & GO-LIVE

### 1. Kênh phân phối thông tin bổ sung (Distribution Channels)
*Nội dung/tri thức này ngoài hiển thị trên Web trang đích, Cell Team có muốn đồng bộ lên các kênh phân phối tự động khác thuộc PLG Infrastructure không?*
- [x] **AI Assistant / RAG Chatbot:** Cho phép AI Chatbot trích dẫn thông tin tác giả và người kiểm duyệt khi trả lời câu hỏi.
- [ ] **Help Center (Trung tâm trợ giúp):** N/A
- [x] **Chỉ hiển thị tại trang đích (Microsite / Landing Page / Blog).**

### 2. Kênh đẩy Traffic chủ động (Traffic Acquisition Channels)
*Cell Team sẽ chủ động kéo người dùng vào trang Web bằng cách nào để đạt mục tiêu KPIs?*
- [x] SEO tự nhiên (Organic Search)
- [ ] Quảng cáo trả phí (Paid SEM / Google Ads / Facebook Ads)
- [ ] Kênh In-App (Banner, Push Notification từ App về Web)
- [ ] Khác: [Mô tả chi tiết]

### 3. Cam kết nguồn lực & Đầu mối phê duyệt (Stakeholders & Commitments)
*Vui lòng chỉ định rõ người chịu trách nhiệm nghiệm thu sản phẩm:*
*   **Đầu mối phê duyệt nội dung/nghiệp vụ:** Nguyễn Mai Phương (PO Inbound Marketing)
*   **Đầu mối phê duyệt Pháp lý (Legal Approval):** N/A
*   **Đầu mối vận hành kỹ thuật (Tech Lead Cell Team):** N/A
*   **Cam kết đồng hành (Bắt buộc tích chọn để duyệt khởi chạy):**
    *   [x] **Cam kết nguồn lực:** Product Owner (PO) của Cell Team cam kết dành tối thiểu **2 giờ/tuần** để đồng hành kiểm duyệt chất lượng nội dung tác giả, cập nhật hồ sơ chuyên gia trên hệ thống.
    *   [x] **Chất lượng nội dung:** Cell Team chịu trách nhiệm hoàn toàn về tính chính xác, bản quyền hình ảnh tác giả và an toàn pháp lý của toàn bộ nội dung nghiệp vụ được cung cấp.

### 4. Câu hỏi / Vấn đề cần làm rõ thêm (Open Questions)

| # | Câu hỏi | Người chịu trách nhiệm | Hạn chót trả lời | Trạng thái |
|---|---|---|---|---|
| 1 | Link LinkedIn của tác giả có cần bắt buộc xác thực domain momo.vn không? | PO Inbound | 25/06/2026 | OPEN |
