# MoSpark - Chatbot
Trợ lý AI tư vấn và hỗ trợ người dùng toàn trang Web

> - **Project Name:** MoSpark Web Platform
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Bảo
> - **PIC:** Duy (Tech)
> - **Version:** 1.1 · June 2026


---

## 1. Mục Đích & Vai Trò Chiến Lược

### 1.1. Bối cảnh
Với định hướng phát triển của MoSpark, website momo.vn ngày càng đa dạng với hàng chục Use Case (Ví Trả Sau, Vay Nhanh, Bảo Hiểm, Phạt Nguội, Đối tác...) và lượng thông tin đồ sộ. Tuy nhiên, người dùng thường có xu hướng "lười đọc" toàn bộ nội dung tĩnh mà chỉ muốn tìm nhanh thông tin để giải quyết một JTBD cụ thể (VD: "Phí bảo hiểm xe máy là bao nhiêu?", "Nợ xấu có mở Ví Trả Sau được không?"). 

Việc không tìm thấy thông tin nhanh chóng trên một trang web lớn dẫn đến tỷ lệ thoát trang (bounce rate) cao và mất cơ hội chuyển đổi Web-to-App (W2A).

### 1.2. Giải pháp: mospark_chatbot - Agentic Web Chatbot
Định vị không phải là một công cụ trò chuyện mở (open-domain chat), mà là một **PLG Tool (Utility)** được nhúng trên **toàn bộ website momo.vn**. 

**3 Nguyên tắc thiết kế cốt lõi:**
1. **Zero-Scripting (Contextual Grounding):** Dù người dùng đang ở bất kỳ trang nào, Chatbot tự động nhận diện ngữ cảnh (URL) để load đúng Knowledge Base (Business Context 12 fields + Content + LLM) của dự án/Use Case tương ứng để dẫn dắt và giải quyết JTBD. Không cấu hình kịch bản thủ công.
2. **Intent-First:** Cung cấp sẵn các Quick Replies thay đổi linh hoạt theo trang người dùng đang xem để họ chạm là ra kết quả (Không bắt ép phải gõ phím).
3. **Conversion-Driven:** Mọi tương tác của chatbot đều hướng đến việc điều hướng người dùng mở App (OneLink) để hoàn tất luồng (Ví dụ: "Mở Ví Trả Sau", "Nộp Phạt Ngay", "Thanh toán ngay").

---

## 2. Nhu Cầu Người Dùng & JTBD (Jobs-To-Be-Done)

Chatbot được thiết kế để giải quyết các nhu cầu (JTBD) phổ biến nhất khi người dùng duyệt website. Dưới đây là ví dụ minh họa cơ chế:

| Nhu cầu (Intent) | Lựa chọn (Quick Reply) | Hành động của Chatbot (Từ Knowledge Base) | Call-to-Action (CTA) kỳ vọng |
|---|---|---|---|
| **Tìm hiểu USP/Tính năng nổi bật** | *Sản phẩm này có gì đặc biệt?* | Trích xuất USPs từ Business Context. | Xem chi tiết trên App |
| **Kiểm tra điều kiện tham gia** | *Tôi có đủ điều kiện không?* | Đối chiếu điều kiện từ nội dung YMYL/Disclaimer. | Mở App / Xác thực |
| **Hỗ trợ thực hiện tác vụ/JTBD** | *Hướng dẫn cách làm* | Hướng dẫn từng bước dựa trên bài Blog/How-to. | Thực hiện ngay trên App |
| **Tra cứu thông tin Merchant (O2O)** | *Quán này có nhận Ví Trả Sau không? Giờ mở cửa?* | Truy xuất từ Structured Custom Fields (Địa chỉ, Giờ, Payment) của trang Đối tác. | Thanh toán / Kích hoạt Ví Trả Sau |
| **Hỏi đáp thông tin cụ thể** | *[Câu hỏi cụ thể]* | LLM truy vấn Knowledge Base để trả lời chính xác. | Mở dịch vụ tương ứng |
| **Tóm tắt nhanh toàn bộ** | *Tóm tắt thông tin* | Gom ý chính thành 3-4 bullet points. | Chuyển đổi / Mở App |

---

## 3. Kiến Trúc Luồng Identity & Web-to-App Tracking

Đây là tính năng bắt buộc để chứng minh ROI của Chatbot (Đóng góp vào M11 - Revenue Attribution Pipeline của MoSpark). Mục tiêu: Liên kết toàn trình từ *Web Anonymous User → Chatbot Interaction → OneLink Click → App Conversion*.

### 3.1. Luồng xử lý kỹ thuật (5 Tầng)

1. **Tầng 1 - User Identification Request:**
   - Khi người dùng truy cập bất kỳ trang nào trên momo.vn, Edge Middleware đọc HttpOnly Cookie.
2. **Tầng 2 - Identity Generation:**
   - Đã login Web: Sử dụng `hashed_uid` từ cookie.
   - Chưa login (Anonymous): Gọi hàm `generateAnonId()`.
   - Kết xuất ra một `Identity Object { identityId, userType }` chuẩn hóa.
3. **Tầng 3 - Analytics Tracking:**
   - Init Chatbot Session: Push `identity_init` lên DataLayer (GTM -> GA4) và gọi `umami.identify(identityId)`.
   - Track các event: `chatbot_opened`, `quick_reply_clicked`, `question_asked`.
4. **Tầng 4 - CTA Distribution (Crucial Step):**
   - Mọi Onelink được Chatbot sinh ra hoặc hiển thị trên khung chat **phải được tự động gắn tham số `wui`**.
   - Định dạng: `https://onelink.momo.vn/.../?wui=<identityId>&ref=web_chatbot`
5. **Tầng 5 - App Attribution:**
   - Khi mở App qua OneLink, App MoMo tiếp nhận `wui` và map với `IdentityId`.
   - Data pipeline (Appsflyer + BigQuery) sẽ khâu nối: Hành vi hỏi Chatbot trên Web -> Giao dịch/thanh toán trên App.

---

## 4. Giao Diện (UI/UX) & Placement

- **Format:** Nút Floating (Balloon) ở góc phải dưới toàn màn hình website, có notification badge để thu hút sự chú ý.
- **Trải nghiệm:** Bấm vào mở dạng Bottom Sheet (Mobile) hoặc Slide-out Panel (Desktop).
- **Thiết kế mặc định:** Khi mở ra, hiển thị ngay 5 nút bấm Quick Replies (tương ứng với các JTBD của Use Case đó) thay vì bắt người dùng gõ câu hỏi.

---

## 5. Quy Trình Vận Hành (Content & Quality Governance)

Đảm bảo tuân thủ chuẩn MoSpark (Layer 3 - Quality Gate):

1. **Nguồn dữ liệu (Dynamic Knowledge Base):** Chatbot tự động nội suy câu trả lời từ kho dữ liệu tương ứng với trang web hiện tại:
   - **Đối với bài viết/Blog/Use Case chung:** Lấy từ trường thông tin `Business Context` (12 fields) và nội dung Content dài đang thuộc về Use Case đó.
   - **Đối với trang Merchant (Đối tác):** Chatbot ưu tiên đọc dữ liệu tĩnh được bóc tách tự động từ luồng GenAI Single-Pass của MoSpark (Structured Custom Fields bao gồm `merchant_address`, `price_range`, `operating_hours`, `amenities_services`, `payment_policy`) thông qua Webhook API. Cơ chế cấu trúc hóa này giúp tối ưu token (RAG) và chống hallucination (bịa thông tin).
2. **Anti-Hallucination:** System Prompt của LLM bắt buộc chứa rule: *"Chỉ trả lời dựa trên Knowledge Base được cung cấp của trang hiện hành. Nếu thông tin không có, trả lời 'Hiện tại chưa có thông tin này' thay vì bịa ra."*
3. **Quality Gate:** Trang web hiện tại phải đạt điểm SEO/GEO Scoring >= 60 mới được kích hoạt tính năng trả lời tự động bằng AI (vì nội dung gốc rác thì AI trả lời cũng rác).

---

## 6. Measurement-First: Hypothesis & KPIs

### 6.1. AB Test Hypothesis
- **Hypothesis:** "Việc đặt Chatbot (có khả năng nhận diện ngữ cảnh trang + Onelink tracking `wui`) trên toàn website sẽ làm tăng tỷ lệ Click-to-App (W2A CR) lên ít nhất 15% so với việc chỉ để người dùng tự duyệt web."
- **Variant A (Baseline):** Website chuẩn, không có Chatbot.
- **Variant B:** Website + Floating Chatbot Widget (mospark_chatbot).

### 6.2. Metrics Tracked (Umami & Appsflyer)
| Metric | Định nghĩa | Target |
|---|---|---|
| **Chatbot Interaction Rate** | % Session có click mở chatbot | > 20% traffic trang |
| **Quick Reply Usage** | % Session mở chatbot có bấm vào ít nhất 1 Quick Reply | > 60% (chứng minh tính hữu dụng) |
| **W2A Chatbot CTR** | Lượt click OneLink trong Chatbot / Tổng số session mở Chatbot | > 10% |
| **End-to-End Conversion** | App Install / App Open thành công mang theo `wui` từ Chatbot | Đo lường baseline sau 1 tháng |

---
*Tài liệu này được lập theo chuẩn quy trình Spec của MoSpark Platform. Web Platform team sẽ dựa vào mục 3 và 6 để tiến hành setup schema trước khi build UI.*
