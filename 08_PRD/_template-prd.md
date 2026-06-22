# PRODUCT REQUIREMENT DOCUMENT (PRD) - WEB CHANNEL
*Bắt buộc Cell Team điền đầy đủ và cung cấp cho Web Platform Team trước khi tiến hành triển khai dự án*

## THÔNG TIN CHUNG (Metadata)
> *   **Tên dự án / Sản phẩm (PRODUCT NAME):** [Ví dụ: Tra cứu Phạt nguội, Đăng ký Ví Trả Sau...]
> *   **Phiên bản & Ngày (Version & Date):** Version 1.0 - [dd/mm/yyyy]
> *   **Đơn vị đề xuất (Business Owner / Cell Team):** [Tên Cell Team / Division]
> *   **Web Product Lead (Đầu mối tiếp nhận & phê duyệt):** Hien.ho
> *   **Product Owner (PO) phụ trách:** [Họ và tên - Email]
> *   **Product Manager (Người phê duyệt sản phẩm):** [Họ và tên - Email]
> *   **Engineer Lead (Người phụ trách kỹ thuật):** [Họ và tên - Email]
> *   **UI/UX Designer:** [Họ và tên - Email]
> *   **Trạng thái tài liệu (Document status):** [DRAFT / UNDER REVIEW / APPROVED]
> *   **Giai đoạn S-P-A dự kiến:** [Stage S: reSearch / Stage P: Pilot / Stage A: Action]
> *   **Loại yêu cầu (Vui lòng chọn loại yêu cầu và chỉ điền các mục tương ứng ở Mục VI):**
>     *   [ ] **1. Tính năng mới (New Feature):** Tạo mới Microsite, xây dựng Widget tra cứu/tính toán mới. *(Bắt buộc áp dụng PRD)*
>     *   [ ] **2. Cải tiến lớn (Major Improvement):** Thay đổi luồng trải nghiệm, thay đổi logic nghiệp vụ, tích hợp thêm API mới hoặc đổi cơ chế xác thực. *(Bắt buộc áp dụng PRD)*
>     *   [ ] **3. Thay đổi cấu trúc (Structural Change):** Thay đổi phân cấp đường dẫn (URL Structure), bố cục layout hoặc site structure. *(Bắt buộc áp dụng PRD)*

## I. RELATED DOCUMENTS
*Các liên kết tài liệu nghiệp vụ, thiết kế hiện có từ phía Cell Team (Vui lòng đính kèm link trước khi đi vào chi tiết).*

*   [ ] **Figma Design Link:** [Chèn link thiết kế UI/UX tại đây]
*   [ ] **Tài liệu nghiệp vụ (BRD / PRD in-app gốc):** [Chèn link slide giới thiệu hoặc file BRD chi tiết của sản phẩm]
*   [ ] **Tài sản thương hiệu (Brand Assets / Guideline riêng):** [Chèn link logo, key visuals, palette màu sắc nếu có]
*   [ ] **Tài liệu đặc tả API (Swagger / Postman):** [Chèn link tài liệu kỹ thuật tích hợp]

## II. BACKGROUND & PROBLEM STATEMENT

### 1. Bối cảnh dự án (Background)
*Tóm tắt chung về sáng kiến sản phẩm, lý do đề xuất và ngữ cảnh cần thiết để người đọc hiểu được sáng kiến này.*
- [Điền nội dung của bạn vào đây]

### 2. Vấn đề cần giải quyết (Problem)
*Mô tả các vấn đề của khách hàng đang cần được giải quyết. Đồng thời chỉ rõ các vấn đề nội bộ (nếu có) của doanh nghiệp.*
*   **Điểm nghẽn ở sản phẩm hiện tại (Gaps):** [Người dùng đang gặp khó khăn gì? Khó dùng trên Web hay khó thực hiện hành động?]
*   **Vấn đề nội bộ doanh nghiệp cần giải quyết:** [Hiệu suất vận hành kém (Process efficiency) hay tốn kém chi phí (Cost savings)?]
> **Ví dụ mẫu (Dự án Phạt Nguội):** Giao diện tra cứu phạt nguội hiện tại của Cục CSGT khó dùng trên mobile và bắt nhập mã CAPTCHA dễ sai. Trên Web momo.vn chưa có công cụ này khiến người dùng thoát trang và tìm đến đối thủ. Về mặt vận hành, việc chưa tự động hóa nạp dữ liệu phạt nguội khiến đội ngũ content phải tạo bài thủ công, tốn nhiều chi phí nhân sự.

- [Điền nội dung của bạn vào đây]

## III. OBJECTIVES & VALUE PROPOSITION

### 1. Mục tiêu & Chỉ số đo lường (Objectives, Goals & Success criteria)
*Dự án này cần đạt được mục tiêu gì? Thành công của sản phẩm trông như thế nào?*
> **Ví dụ mẫu (Dự án Phạt Nguội):**
> *   *W2A Clicks:* Đạt > 15,000 lượt click mở App/tháng.
> *   *W2A CR:* Đạt tỷ lệ chuyển đổi Click/Session tối thiểu > 8%.
> *   *Giao dịch in-app đích (MEU):* Người dùng thực hiện nộp phạt thành công trong app MoMo qua luồng chuyển tiếp.

| Chỉ số (KPI) | Trước thay đổi (Baseline) | Mục tiêu sau thay đổi (Target) | Thời gian đo lường (Timeframe) |
|---|---|---|---|
| Số lượt nhấp mở App (W2A Clicks) | [Ví dụ: 0] | [Ví dụ: >10,000/tháng] | Q3/2026 |
| Tỷ lệ chuyển đổi Web-to-App (W2A CR) | [Ví dụ: 0%] | [Ví dụ: > 5%] | Q3/2026 |
| Traffic mong muốn (Users/Pageviews) | | | |
| Giao dịch in-app đích (MEU) | [Ví dụ: 0] | [Ví dụ: >500 giao dịch/tháng] | Q3/2026 |

### 2. Tuyên ngôn giá trị (Value Proposition)
*Sản phẩm này mang lại lợi ích gì cho khách hàng? Điểm vượt trội nào so với đối thủ cạnh tranh? Định dạng theo cấu trúc: Chúng tôi giúp [Persona/Khách hàng] thực hiện [Hành động/Lợi ích] bằng cách cung cấp [Giải pháp].*
> **Ví dụ mẫu:** Chúng tôi giúp *các tài xế lái xe tại Việt Nam* *tra cứu và nộp phạt nguội nhanh chóng dưới 1 phút* bằng cách *cung cấp widget tra cứu phạt nguội 1-click không cần CAPTCHA trên Web MoMo*.

- [Điền nội dung của bạn vào đây]

## IV. TARGET PERSONAS & HIGH-LEVEL USER EXPERIENCE (JTBD)

### 1. Khách hàng mục tiêu (Target Personas)
*Ai là khách hàng lý tưởng sử dụng sản phẩm này? Họ sẽ được hưởng lợi ích gì?*
- [Điền nội dung của bạn vào đây]

### 2. Jobs-to-be-Done (JTBD)
*Bóc tách rõ nhu cầu của người dùng Web thành 2 lớp và phân tích theo 3 cấu thành: Chức năng (Functional), Cảm xúc (Emotional), Xã hội (Social).*

#### A. Product JTBD (Nhu cầu tương tác với Widget/Công cụ trên Web)
*Giải quyết hành động trực tiếp của người dùng khi sử dụng các công cụ tính toán, tra cứu ngay trên trang Web.*
*   **Khi bối cảnh xảy ra (When...):** [Ví dụ: Khi tôi đi đăng kiểm xe ô tô và lo lắng không biết mình có lỗi phạt nguội nào chưa nộp hay không]
*   **Hành động trên Web (I want to...):** [Ví dụ: Nhập biển số xe vào ô tra cứu trên Web MoMo để kiểm tra kết quả ngay lập tức]
*   **Kết quả kỳ vọng (So I can...):** [Ví dụ: Biết chính xác mình có bị phạt nguội không để chủ động nộp phạt trước khi đăng kiểm]
*   **Phân tích 3 cấu thành của Job:**
    *   *Functional (Chức năng):* Tra cứu kết quả phạt nguội nhanh, chính xác, không CAPTCHA.
    *   *Emotional (Cảm xúc):* Giải tỏa sự lo lắng bị từ chối đăng kiểm, mang lại cảm giác an tâm khi lái xe.
    *   *Social (Xã hội):* Được nhìn nhận là người lái xe có ý thức chấp hành luật giao thông.

- [Điền nội dung của bạn vào đây]

#### B. SEO/GEO JTBD (Nhu cầu tìm kiếm thông tin ngoài App)
*Giải quyết ý định tìm kiếm (Search Intent) khi người dùng tra cứu thông tin trên Google hoặc đặt câu hỏi cho AI Search (ChatGPT, Perplexity). Lớp nhu cầu này xuất phát trực tiếp từ các từ khóa trong **SEO/GEO Inventory** ở giai đoạn reSearch.*
*   **Từ khóa / Câu hỏi nguồn (Search Intent / Keyword):** [Ví dụ: "nộp phạt nguội ở đâu", "phạt nguội quá hạn có đăng kiểm được không?"]
*   **Khi người dùng tìm kiếm (When...):** [Ví dụ: Khi tôi nhận được thông báo phạt nguội gửi về nhà và chưa rõ các bước đóng tiền phạt hành chính online thế nào]
*   **Nội dung họ cần đọc (I want to...):** [Ví dụ: Tìm thấy bài viết hướng dẫn từng bước ngắn gọn, rõ ràng của MoMo xuất hiện trên top đầu công cụ tìm kiếm]
*   **Hành vi chuyển đổi kỳ vọng (So I can...):** [Ví dụ: Tin cậy giải pháp của MoMo và click vào nút CTA mở App MoMo đóng phạt trực tuyến ngay lập tức]
*   **Phân tích 3 cấu thành của Job:**
    *   *Functional (Chức năng):* Tiếp cận thông tin quy trình đóng phạt online chính thống, dễ hiểu.
    *   *Emotional (Cảm xúc):* Tự tin vì biết cách xử lý vấn đề pháp lý giao thông mà không cần qua môi giới trung gian.
    *   *Social (Xã hội):* Chia sẻ thông tin hữu ích này cho bạn bè, hội nhóm tài xế để giúp họ tránh bị lừa đảo.

- [Điền nội dung của bạn vào đây]

## V. BUSINESS CONTEXT
*Cung cấp thông tin nghiệp vụ cốt lõi để đội ngũ phát triển hiểu rõ về sản phẩm/dịch vụ.*

### 1. Mô tả nghiệp vụ sản phẩm (Product Description & Rules)
*Mô tả ngắn gọn sản phẩm hoạt động thế nào, các điều khoản/quy định nghiệp vụ cốt lõi mà người dùng cần biết.*
> **Ví dụ mẫu (Sản phẩm Ví Trả Sau):** Hạn mức từ 1-10 triệu, miễn lãi lên đến 45 ngày. Người dùng phải từ 18 tuổi, đã KYC tài khoản MoMo. Khách hàng phải đóng dư nợ trước ngày 5 hoặc ngày 10 hàng tháng để tránh phát sinh phí chậm trả.

- [Điền nội dung của bạn vào đây]

### 2. Giá trị cốt lõi & Thông điệp chính (Value Propositions & Key Messages)
*Điểm độc đáo của sản phẩm giúp thuyết phục người dùng là gì? Thông điệp chính cần truyền thông trên Web là gì?*
- [Điền nội dung của bạn vào đây]

### 3. Giới hạn & Các từ cấm (Constraints & Blacklist)
*Những gì sản phẩm KHÔNG làm được trên Web và danh sách từ ngữ nhạy cảm/tên đối thủ tuyệt đối không được nhắc tới.*
> **Ví dụ mẫu:** Không dùng các từ "Cho vay tiền", "Giải ngân nhanh" (tránh hiểu lầm là tín dụng đen), không so sánh trực tiếp với thẻ tín dụng của ngân hàng X.

- [Điền nội dung của bạn vào đây]

## VI. FEATURE REQUIREMENTS & RELEASE PHASES
*(Mô tả chi tiết các tính năng cần làm theo từng Giai đoạn phát hành)*

### 1. Lộ trình phát hành (Release Phases)
*Phân rã lộ trình triển khai tính năng theo từng phiên bản để kiểm chứng baselines.*
*   **Phase 1 (MVP/Pilot):** [Ví dụ: Xây dựng Landing Page phạt nguội + Widget tra cứu lỗi phạt nguội theo biển số xe cho 2 tỉnh thành lớn]
*   **Phase 2 (Scale):** [Ví dụ: Mở rộng tra cứu toàn quốc + Tích hợp API tự động thông báo lỗi vi phạm]
*   **Phase 3 (Tối ưu):** [Ví dụ: Tích hợp AI Assistant chatbot tự động tư vấn thủ tục nộp phạt]

### 2. Đặc tả yêu cầu chi tiết (User stories and requirements per release)
*(Cell Team chỉ cần điền các mục tương ứng với Loại yêu cầu đã chọn ở phần Metadata)*

#### LOẠI 1: TÍNH NĂNG MỚI (NEW FEATURE)
*   **Hành trình người dùng (User Journey Flows / Designs):** [Mô tả luồng từ lúc vào trang web đến lúc mở App MoMo]
*   **Yêu cầu xác thực người dùng (User Authentication):**
    *   [ ] **Công khai (Public):** Không cần đăng nhập vẫn sử dụng được tính năng (Ví dụ: Tra cứu phạt nguội).
    *   [ ] **Cần đăng nhập (Requires Login):** Yêu cầu OTP / đăng nhập tài khoản MoMo để lấy thông tin cá nhân.
*   **Bảng User Stories và Yêu cầu theo từng Release:**

| Tính năng (Feature) | User Story | Yêu cầu trong Phase 1 | Yêu cầu trong Phase 2 |
|---|---|---|---|
| [Ví dụ: Widget Tra cứu] | As a [user], I want to [action] so that [outcome] | Nhập biển số ➔ Hiện lỗi chi tiết | Tự động lưu biển số cho lần tra cứu sau |
| | | | |

#### LOẠI 2: CẢI TIẾN (IMPROVEMENT)
*   **Điểm cần tối ưu:** Chỉ rõ tính năng/nút bấm/giao diện nào hiện tại hoạt động chưa tốt.
*   **Kịch bản tối ưu đề xuất:**
    *   [Mô tả thay đổi logic hoặc thay đổi trải nghiệm, ví dụ: Rút ngắn form đăng ký từ 4 bước xuống 2 bước].

#### LOẠI 3: THAY ĐỔI CẤU TRÚC (STRUCTURAL CHANGE)
*   **Bố cục layout mới:** [Ví dụ: Thay đổi thứ tự hiển thị các khối nội dung trên trang].
*   **Thay đổi đường dẫn (URL):**
    *   *URL hiện tại:* momo.vn/...
    *   *URL mới mong muốn:* momo.vn/...

### 3. Ngoài phạm vi triển khai (Out of scope)
*Xác định rõ ranh giới của dự án, những gì không được thực hiện trong dự án này.*
- [Điền nội dung của bạn vào đây]

## VII. W2A CONVERSION & DATA REQUIREMENTS

### 1. Luồng chuyển đổi Web-to-App (W2A Trigger Points)
*CTA nút bấm hoặc Banner sẽ mở màn hình cụ thể nào trong App MoMo?*

| Vị trí CTA trên Web | Câu chữ hiển thị (CTA Text) | Deep Link mở App |
|---|---|---|
| [Ví dụ: Trang kết quả] | "Mở App thanh toán ngay" | `momo://app/...` |

### 2. API Nghiệp Vụ & Fallback Logic
*Nếu tính năng cần dữ liệu thời gian thực từ Cell Team (Ví dụ: Tra cứu điểm tín dụng, Số tiền vay tối đa...).*
*   **Kịch bản khi lỗi (Fallback):** [Khi API của Cell Team lỗi hoặc timeout > 3s, giao diện Web sẽ hiển thị thế nào?]

## VIII. GOVERNANCE & RISKS

### 1. Kênh phân phối thông tin bổ sung (Distribution Channels)
*Nội dung/tri thức này ngoài hiển thị trên Web trang đích, Cell Team có muốn đồng bộ lên các kênh phân phối tự động khác thuộc PLG Infrastructure không?*
- [ ] **AI Assistant / RAG Chatbot:** Cho phép AI Chatbot học thông tin này để tự động trả lời người dùng.
- [ ] **Help Center (Trung tâm trợ giúp):** Tự động đồng bộ các bài viết FAQ lên hệ thống Help Center chung của MoMo.
- [ ] **Chỉ hiển thị tại trang đích (Microsite / Landing Page / Blog).**

### 2. Kênh đẩy Traffic chủ động (Traffic Acquisition Channels)
*Cell Team sẽ chủ động kéo người dùng vào trang Web bằng cách nào để đạt mục tiêu KPIs?*
- [ ] SEO tự nhiên (Organic Search)
- [ ] Quảng cáo trả phí (Paid SEM / Google Ads / Facebook Ads)
- [ ] Kênh In-App (Banner, Push Notification từ App về Web)
- [ ] Khác: [Mô tả chi tiết]

### 3. Cam kết nguồn lực & Đầu mối phê duyệt (Stakeholders & Commitments)
*Vui lòng chỉ định rõ người chịu trách nhiệm nghiệm thu sản phẩm và ký cam kết:*
*   **Đầu mối phê duyệt phía Web Platform (Web Product Lead):** Hien.ho
*   **Đầu mối phê duyệt nội dung/nghiệp vụ phía Cell Team:** [Họ tên - Email]
*   **Đầu mối phê duyệt Pháp lý (Legal Approval) (nếu có):** [Họ tên - Email]
*   **Đầu mối vận hành kỹ thuật (Tech Lead Cell Team):** [Họ tên - Email]
*   **Cam kết đồng hành (Bắt buộc tích chọn để duyệt khởi chạy):**
    *   [ ] **Cam kết nguồn lực:** Product Owner (PO) của Cell Team cam kết dành tối thiểu **2 giờ/tuần** để đồng hành kiểm duyệt chất lượng nội dung tác giả, cập nhật hồ sơ chuyên gia trên hệ thống.
    *   [ ] **Chất lượng nội dung:** Cell Team chịu trách nhiệm hoàn toàn về tính chính xác và an toàn pháp lý của toàn bộ nội dung nghiệp vụ được cung cấp.

### 4. Quản trị rủi ro tiềm tàng (Potential Risk)
*Dự báo các rủi ro có thể xảy ra trong quá trình triển khai hoặc vận hành và phương án giảm thiểu.*

| Rủi ro (Risk) | Mức độ ảnh hưởng (Impact) | Phương án giảm thiểu (Risk management plan) | Người chịu trách nhiệm (PIC) |
|---|---|---|---|
| [Ví dụ: API đối tác bị nghẽn] | Cao | Fallback về luồng hướng dẫn mở App tra cứu thủ công | Dev Cell Team |
| | | | |

## LỊCH SỬ THAY ĐỔI (Changelog)

| Phiên bản | Ngày cập nhật | Người thực hiện | Nội dung thay đổi |
|---|---|---|---|
| 3.4 | 2026-06-18 | Web Product Lead | Bỏ loại yêu cầu Content Update; đưa Hien.ho làm Web Product Lead phê duyệt chính |
