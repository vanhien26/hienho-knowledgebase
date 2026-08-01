# PRODUCT REQUIREMENT DOCUMENT (PRD) - WEB & IN-APP CHANNEL
*Dự án tiềm năng: MoMo SmartWealth AI - Trợ lý Tài chính Cá nhân Thông minh*

## THÔNG TIN CHUNG (Metadata)
> *   **Tên dự án / Sản phẩm (PRODUCT NAME):** MoMo SmartWealth AI (Trợ lý Tài chính Cá nhân Thông minh)
> *   **Phiên bản & Ngày (Version & Date):** Version 1.0 - 30/06/2026
> *   **Đơn vị đề xuất (Business Owner / Cell Team):** Cell Team Wealthtech & AI Platform
> *   **Web Product Lead (Đầu mối tiếp nhận & phê duyệt):** Hien.ho
> *   **Product Owner (PO) phụ trách:** Nguyễn Văn A - po-wealth@momo.vn
> *   **Product Manager (Người phê duyệt sản phẩm):** Trần Thị B - pm-ai@momo.vn
> *   **Engineer Lead (Người phụ trách kỹ thuật):** Lê Văn C - tech-lead@momo.vn
> *   **UI/UX Designer:** Phạm Minh D - ux-wealth@momo.vn
> *   **Trạng thái tài liệu (Document status):** DRAFT
> *   **Giai đoạn S-P-A dự kiến:** Stage S (reSearch) & Stage P (Pilot) - Dự kiến triển khai Q3/2026
> *   **Loại yêu cầu:**
>     *   [x] **1. Tính năng mới (New Feature):** Tạo mới Microsite giới thiệu, tích hợp Web Widget Tính toán Phân bổ thu nhập và hệ thống in-app AI Coach Dashboard & Chatbot.

---

## I. RELATED DOCUMENTS
*Các liên kết tài liệu nghiệp vụ, thiết kế hiện có (Giả lập cho dự án).*

*   [x] **Figma Design Link:** `https://www.figma.com/file/momo-smartwealth-ai-prototype`
*   [x] **Tài liệu nghiệp vụ (BRD / PRD in-app gốc):** [BRD-SmartWealth-AI-Core-V1.0](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_USE_CASE_MOMO/smartwealth-brd.md) *(Đường dẫn giả định)*
*   [x] **Tài liệu đặc tả API (Swagger / Postman):** `https://api-docs.momo.vn/smartwealth/v1`

---

## II. BACKGROUND & PROBLEM STATEMENT

### 1. Bối cảnh dự án (Background)
MoMo đang giữ vị thế ứng dụng thanh toán hàng đầu tại Việt Nam với lượng dữ liệu giao dịch khổng lồ (hóa đơn, ăn uống, di chuyển, mua sắm...). Tuy nhiên, MoMo đang dịch chuyển mạnh mẽ sang mảng **Wealthtech** (tài chính cá nhân, đầu tư, tích lũy) để tăng biên lợi nhuận.
Hiện tại, các sản phẩm tài chính như *Túi Thần Tài, Tiết Kiệm Online, Ví Trả Sau, Chứng Chỉ Quỹ (Chứng Khoán)* đang đứng độc lập. Người dùng chưa có một công cụ trung tâm để kết nối, quản lý dòng tiền và tối ưu hóa tài sản một cách tự động.

### 2. Vấn đề cần giải quyết (Problem)
*   **Đối với khách hàng (Gaps):**
    *   **Lười ghi chép chi tiêu:** Hơn 75% người dùng trẻ (Gen Z & Millennials) thừa nhận gặp hội chứng "cháy túi" cuối tháng nhưng không đủ kiên nhẫn để tự nhập tay các khoản chi tiêu vào các app quản lý như Money Lover hay Excel.
    *   **Sợ đầu tư phức tạp:** Người dùng có tiền nhàn rỗi trong Ví MoMo (0% lãi suất) nhưng ngại chuyển sang Túi Thần Tài hoặc Chứng chỉ quỹ vì thiếu kiến thức tài chính hoặc sợ quy trình rườm rà.
    *   **Bất cân xứng thông tin chi tiêu:** Người dùng không nhận biết được các hành vi tiêu dùng bất hợp lý (ví dụ: tiền đăng ký các app dịch vụ hàng tháng bị trừ tự động mà không dùng tới, hóa đơn điện nước tăng đột biến...).
*   **Đối với nội bộ MoMo (Business Needs):**
    *   **Tối ưu hóa nguồn tiền nhàn rỗi (AUM Growth):** Lượng tiền nằm im trên tài khoản ví chính rất lớn nhưng chưa được chuyển hóa thành tài sản quản lý (AUM) tại các sản phẩm đầu tư có phí của MoMo.
    *   **Tăng điểm chạm gắn kết (Retention Rate):** Khách hàng chỉ mở app khi cần thanh toán. MoMo cần một tính năng mang tính tương tác hàng ngày (Daily Engagement) thông qua các cảnh báo chi tiêu và tư vấn thông minh.

---

## III. OBJECTIVES & VALUE PROPOSITION

### 1. Mục tiêu & Chỉ số đo lường (Objectives, Goals & Success criteria)
Dự án nhằm thu hút người dùng từ kênh Web (thông qua SEO/GEO về quản lý tài chính) sang App MoMo, từ đó thúc đẩy kích hoạt tính năng Trợ lý AI và tăng trưởng tài sản tích lũy.

| Chỉ số (KPI) | Trước thay đổi (Baseline) | Mục tiêu sau thay đổi (Target) | Thời gian đo lường (Timeframe) |
|---|---|---|---|
| Traffic Web (Pageviews/tháng) | 0 (New Web Widget) | > 150,000 Pageviews/tháng | 3 tháng sau ra mắt |
| Tỷ lệ chuyển đổi Web-to-App (W2A CR) | 0% | > 10% | 3 tháng sau ra mắt |
| Số lượng người kích hoạt AI Coach in-app | 0 | > 500,000 người dùng | 6 tháng sau ra mắt |
| Tỷ lệ chuyển đổi dòng tiền nhàn rỗi | 0% | > 8% người dùng bật AI thực hiện chuyển tiền nhàn rỗi vào Túi Thần Tài/Quỹ | 6 tháng sau ra mắt |
| Tăng trưởng AUM của mảng Wealthtech | N/A | Tăng +12% AUM lũy kế từ tệp người dùng kích hoạt AI | Q4/2026 |

### 2. Tuyên ngôn giá trị (Value Proposition)
> Chúng tôi giúp **người dùng trẻ bận rộn tại Việt Nam** **quản lý tài chính cá nhân tự động và đầu tư thông minh chỉ dưới 3 phút mỗi tuần** bằng cách **cung cấp Trợ lý ảo MoMo SmartWealth AI - tự động gom nhóm chi tiêu thực tế, cảnh báo vượt hạn mức và đề xuất phân bổ dòng tiền nhàn rỗi vào các quỹ sinh lời tối ưu.**

---

## IV. TARGET PERSONAS & HIGH-LEVEL USER EXPERIENCE (JTBD)

### 1. Khách hàng mục tiêu (Target Personas)
*   **Persona 1: Vy (24 tuổi) - Gen Z năng động, "Money Blindness"**
    *   *Đặc điểm:* Thu nhập văn phòng 12 triệu/tháng, thích uống trà sữa, mua sắm Shopee qua MoMo, thường xuyên hết tiền vào ngày 20 hàng tháng. Ngại các thuật ngữ tài chính phức tạp.
    *   *Nhu cầu:* Muốn biết tiền đi đâu tự động mà không phải ghi chép, cần lời khuyên thực tế để tiết kiệm mua iPhone mới.
*   **Persona 2: Anh Đức (32 tuổi) - Trụ cột gia đình trẻ**
    *   *Đặc điểm:* Thu nhập 30 triệu/tháng, phải thanh toán 4-5 loại hóa đơn cố định hàng tháng (điện, nước, học phí cho con, trả góp Ví Trả Sau).
    *   *Nhu cầu:* Tối ưu hóa quỹ khẩn cấp của gia đình, đầu tư tích lũy an toàn và tự động nhắc thanh toán đúng hạn để tránh phí trễ hạn.

### 2. Jobs-to-be-Done (JTBD)

#### A. Product JTBD (Tương tác in-app & trên Web Widget)
*   **Khi bối cảnh xảy ra (When...):** Khi tôi nhận lương hàng tháng hoặc khi tôi đang phân vân không biết mình có nên mua một món đồ xa xỉ hay không.
*   **Hành động tôi muốn thực hiện (I want to...):** Xem biểu đồ phân tích quỹ tiền tiêu dùng còn lại (Safe-To-Spend) được tính toán tự động từ hành vi chi tiêu trước đó và nhờ AI tính toán xem nếu tôi mua món đồ này thì có ảnh hưởng đến mục tiêu tiết kiệm hay không.
*   **Kết quả kỳ vọng (So I can...):** Đưa ra quyết định mua sắm hợp lý mà không lo sợ bị thiếu tiền trả hóa đơn cố định vào cuối tháng.
*   **Phân tích 3 cấu thành:**
    *   *Functional (Chức năng):* Tự động phân loại chi tiêu thực tế, tính toán số tiền "an toàn để tiêu" (Safe-to-spend) theo ngày/tuần.
    *   *Emotional (Cảm xúc):* Cảm thấy làm chủ được tiền bạc của mình, xóa bỏ cảm giác tội lỗi khi chi tiêu mua sắm cá nhân.
    *   *Social (Xã hội):* Trở thành một người trẻ có phong cách sống hiện đại, biết cách quản lý tài chính thông minh trong mắt bạn bè.

#### B. SEO/GEO JTBD (Tìm kiếm thông tin ngoài App để kéo Traffic)
*   **Từ khóa nguồn (Search Intent):** "cách chia 6 hũ tài chính cá nhân", "tính toán ngân sách 50 30 20 online", "nên tiết kiệm bao nhiêu tiền một tháng", "túi thần tài momo có tốt không".
*   **Khi người dùng tìm kiếm (When...):** Khi tôi đang đọc các bài viết hướng dẫn lập kế hoạch tài chính cá nhân và muốn thực hành phân bổ thử thu nhập của mình xem có hợp lý không.
*   **Nội dung họ cần đọc (I want to...):** Tiếp cận một trang Web của MoMo có công cụ Widget cho phép nhập mức lương (ví dụ: 15,000,000đ) và tự động chia tiền thành các hũ tài chính ngay trên giao diện Web mà không cần đăng nhập.
*   **Hành vi chuyển đổi kỳ vọng (So I can...):** Thấy kết quả gợi ý trực quan, sau đó quét mã QR/nhấp Link để tải hoặc mở app MoMo, nơi trợ lý AI đã đồng bộ hóa mô hình phân bổ này và tự động theo dõi chi tiêu thực tế của tôi.
*   **Phân tích 3 cấu thành:**
    *   *Functional (Chức năng):* Cung cấp máy tính phân bổ thu nhập (Budget Calculator) tức thì, chính xác theo các trường phái tài chính nổi tiếng.
    *   *Emotional (Cảm xúc):* Thấy việc lập ngân sách thật dễ dàng và hào hứng muốn bắt đầu hành động ngay.
    *   *Social (Xã hội):* Chia sẻ kết quả phân bổ tài chính cá nhân của mình lên mạng xã hội để thể hiện lối sống kỷ luật.

---

## V. BUSINESS CONTEXT

### 1. Mô tả nghiệp vụ sản phẩm (Product Description & Rules)
*   **Cơ chế gom nhóm dữ liệu (Aggregation):** Hệ thống quét lịch sử giao dịch MoMo của người dùng (trong vòng 3-6 tháng gần nhất) và sử dụng AI Classification Model để phân loại vào 6 nhóm chi tiêu tiêu chuẩn:
    1. Thiết yếu (Ăn uống, đi lại, hóa đơn điện nước...)
    2. Hưởng thụ (Giải trí, xem phim, ăn hàng...)
    3. Tích lũy/Đầu tư (Chuyển tiền vào Túi Thần Tài, Mua Chứng chỉ quỹ...)
    4. Giáo dục (Học phí, mua sách, khóa học...)
    5. Quỹ khẩn cấp (Tiết kiệm online ngắn hạn...)
    6. Mua sắm lớn (Trả góp Ví Trả Sau, mua đồ công nghệ...)
*   **Quy tắc Cảnh báo (Alert Rules):**
    *   Khi một nhóm chi tiêu vượt quá **80%** hạn mức thiết lập cho tháng, gửi cảnh báo đẩy (Push notification) in-app.
    *   Khi phát hiện có tiền nhàn rỗi trong Ví chính (số dư ví chính > 2,000,000đ liên tục trong 7 ngày mà không phát sinh giao dịch lớn), AI Coach đề xuất tự động tối ưu: *“Bạn đang có 2,000,000đ nhàn rỗi. Chuyển vào Túi Thần Tài để nhận lãi mỗi ngày lên tới 4%/năm?”*.
*   **Quy định Pháp lý & Nghiệp vụ chứng khoán:**
    *   Không cam kết lợi nhuận cố định khi giới thiệu các quỹ mở đầu tư.
    *   Mọi giao dịch đầu tư đều yêu cầu người dùng xác thực sinh trắc học/mật khẩu riêng biệt. AI Coach chỉ đóng vai trò gợi ý và phân tích, không tự động thực hiện giao dịch chuyển tiền ra ngoài hệ thống MoMo nếu không được sự đồng ý của người dùng.

### 2. Thông điệp truyền thông chính (Key Messages)
*   *"Tài chính thông minh, thảnh thơi từng bước."*
*   *"Không cần ghi chép, MoMo tự lo."*
*   *"Tiền nhàn rỗi tự sinh lời mỗi ngày cùng SmartWealth AI."*

### 3. Giới hạn & Từ cấm (Constraints & Blacklist)
*   **Giới hạn:** Giao diện Web Widget chỉ hỗ trợ tính toán giả lập dựa trên input tự nhập của người dùng. Không hiển thị số dư thực tế hay lịch sử giao dịch thật của ví trên Web browser công cộng để bảo vệ an toàn thông tin tối đa.
*   **Blacklist:** Không sử dụng các từ *"cho vay lãi rẻ"*, *"đầu tư chắc thắng"*, *"cam kết sinh lời X%"*, *"vượt trội hơn gửi tiết kiệm ngân hàng"* (tránh các rủi ro pháp lý và cạnh tranh không lành mạnh).

---

## VI. FEATURE REQUIREMENTS & RELEASE PHASES

### 1. Lộ trình phát hành (Release Phases)

*   **Phase 1 (MVP - Dự kiến Tháng 8/2026):**
    *   **Web:** Landing Page giới thiệu + Widget "Máy tính Chia Hũ Tài Chính" (User tự nhập lương, hệ thống tính toán ra biểu đồ phân bổ). Nút CTA "Đồng bộ vào App MoMo" (Sinh mã QR chứa Deep Link mang tham số ngân sách đã cấu hình).
    *   **In-App:** Màn hình Dashboard phân tích chi tiêu thực tế (Auto-tracking) + Kích hoạt tính năng cảnh báo chi tiêu. Chatbot AI trả lời các câu hỏi tài chính cá nhân cơ bản (dựa trên cơ sở tri thức RAG).
*   **Phase 2 (Scale - Dự kiến Tháng 10/2026):**
    *   **In-App:** Tích hợp tính năng **Auto-Save & Invest**: Tự động làm tròn giao dịch lẻ (ví dụ: mua ly nước 32,000đ, làm tròn thành 40,000đ, tự động đầu tư 8,000đ chênh lệch vào Túi Thần Tài).
    *   **In-App:** Tích hợp với **Ví Trả Sau** để phân tích dòng tiền âm/dương nhằm gợi ý hạn mức vay/trả an toàn nhất.
*   **Phase 3 (Optimization - Dự kiến Q1/2027):**
    *   **Web & App:** Tích hợp AI Agent đề xuất danh mục quỹ đầu tư cá nhân hóa dựa trên khảo sát khẩu vị rủi ro và thói quen chi tiêu thực tế của người dùng.

### 2. Đặc tả yêu cầu chi tiết (User stories and requirements - Phase 1)

#### A. Trải nghiệm trên Kênh Web (Microsite & Widget)
*   **Luồng trải nghiệm:** Người dùng truy cập `momo.vn/smartwealth` ➔ Đọc giới thiệu ➔ Nhập thu nhập hàng tháng tại Widget Máy tính ➔ Chọn trường phái phân bổ (50/30/20 hoặc 6 chiếc hũ) ➔ Xem biểu đồ phân bổ tiền trực quan ➔ Nhấp "Áp dụng vào Ví MoMo của tôi" ➔ Hiện mã QR kèm hướng dẫn quét mã bằng Camera/App MoMo để kích hoạt.
*   **Xác thực:** Công khai (Public). Không yêu cầu đăng nhập trên Web.

| ID | Tính năng (Feature) | User Story | Yêu cầu kỹ thuật Phase 1 |
|---|---|---|---|
| SW-W01 | Web Budget Calculator Widget | As a Web Visitor, I want to input my monthly income and select a budgeting method, so that I can see how my money should be distributed. | - Cho phép nhập số từ 1,000,000đ đến 500,000,000đ.<br>- Chọn giữa 2 phương pháp: 50/30/20 hoặc 6 chiếc hũ.<br>- Hiển thị biểu đồ tròn (Pie chart) tương tác (dùng Chart.js/SVG).<br>- Không cần lưu trữ DB phía Web, tính toán trực tiếp client-side. |
| SW-W02 | QR Code Generator for App Sync | As a Web Visitor, I want to generate a sync QR code, so that I can easily apply this configuration to my mobile app. | - Sinh QR chứa Deep link: `momo://app/smartwealth?income={val}&rule={type}`.<br>- Mã hóa các tham số để tránh lỗi ký tự đặc biệt.<br>- Hiển thị nút "Tải mã QR" hoặc "Mở trực tiếp trên điện thoại" (nếu truy cập Web bằng Mobile Chrome/Safari). |

#### B. Trải nghiệm in-app MoMo (Mobile App)
*   **Luồng trải nghiệm:** Người dùng quét mã QR từ Web hoặc nhấp vào Banner in-app ➔ Chuyển hướng đến màn hình SmartWealth Dashboard ➔ Xác nhận áp dụng ngân sách gợi ý ➔ Dashboard hiển thị biểu đồ so sánh giữa Ngân sách Đặt ra vs. Chi tiêu Thực tế trong tháng.
*   **Xác thực:** Cần đăng nhập ví MoMo (OTP/Sinh trắc học).

| ID | Tính năng (Feature) | User Story | Yêu cầu kỹ thuật Phase 1 |
|---|---|---|---|
| SW-A01 | SmartWealth Dashboard | As a MoMo User, I want to view my monthly budget progress vs my actual expenses, so that I know if I am overspending. | - Đọc dữ liệu giao dịch từ Core Payment DB theo thời gian thực.<br>- Tự động phân loại qua AI classification engine.<br>- Hiển thị thanh tiến trình (Progress bar) cho từng hũ chi tiêu (Xanh: An toàn, Vàng: Sắp chạm hạn mức, Đỏ: Vượt hạn mức). |
| SW-A02 | AI Personal Finance Chatbot | As a MoMo User, I want to ask the AI coach questions about my spending habits and financial advice, so that I can get actionable tips. | - Tích hợp mô hình ngôn ngữ lớn (LLM) qua API Gateway MoMo với dữ liệu RAG về tài chính cá nhân.<br>- Trả lời các câu hỏi như: *"Tháng này tôi đã tiêu bao nhiêu tiền ăn?"*, *"Làm sao để tiết kiệm 5 triệu mua xe?"*.<br>- Chỉ hiển thị tips tài chính, tuyệt đối không ra quyết định đầu tư hộ người dùng. |

### 3. Ngoài phạm vi triển khai (Out of scope - Phase 1)
*   Không tích hợp tự động trích tiền từ tài khoản ngân hàng liên kết vào MoMo (chỉ quản lý dòng tiền trong phạm vi ví MoMo).
*   Chưa hỗ trợ quản lý chi tiêu nhóm/gia đình (Shared Ledger) trong Phase 1.

---

## VII. W2A CONVERSION & DATA REQUIREMENTS

### 1. Luồng chuyển đổi Web-to-App (W2A Trigger Points)

| Vị trí CTA trên Web | Câu chữ hiển thị (CTA Text) | Deep Link mở App | Hành động in-app |
|---|---|---|---|
| Nút dưới Widget Tính toán | "Áp dụng ngân sách này vào MoMo" | `momo://app/smartwealth?action=sync&income={income}&method={method}` | Tự động điền dữ liệu ngân sách vào luồng cài đặt SmartWealth AI in-app. |
| Banner cuối Landing Page | "Trải nghiệm Trợ lý AI miễn phí" | `momo://app/smartwealth?action=activate` | Điều hướng thẳng đến trang đăng ký kích hoạt dịch vụ AI Coach. |

### 2. API Nghiệp Vụ & Fallback Logic
*   **API tính toán ngân sách trên Web:** Chạy hoàn toàn bằng Javascript client-side để tối ưu tốc độ tải trang và giảm tải server.
*   **API đồng bộ in-app:** Khi người dùng mở app qua Deep Link, nếu hệ thống AI Core gặp sự cố tải dữ liệu chi tiêu thực tế (timeout > 4s), hệ thống sẽ fallback về màn hình Dashboard tĩnh hiển thị biểu đồ ngân sách mục tiêu đã đồng bộ từ Web và một banner thông báo: *"Dữ liệu chi tiêu thực tế đang được cập nhật. Vui lòng quay lại sau ít phút."*

---

## VIII. GOVERNANCE & RISKS

### 1. Kênh phân phối thông tin bổ sung (Distribution Channels)
*   [x] **AI Assistant / RAG Chatbot:** Đồng bộ toàn bộ tài liệu FAQ, cẩm nang quản lý tài chính và các quy định về Túi Thần Tài vào dữ liệu huấn luyện RAG để chatbot trả lời đồng nhất.
*   [x] **Help Center (Trung tâm trợ giúp):** Tạo danh mục bài viết hướng dẫn sử dụng MoMo SmartWealth AI trên `momo.vn/tro-giup`.

### 2. Kênh đẩy Traffic chủ động (Traffic Acquisition Channels)
*   [x] **SEO tự nhiên (Organic Search):** Tập trung viết các bài viết tối ưu SEO cho bộ từ khóa ngân sách, hũ tài chính để đón đầu xu hướng tìm kiếm trên Google.
*   [x] **Quảng cáo trả phí (Paid SEM):** Chạy quảng cáo Google Search cho các từ khóa công cụ tính toán tài chính.
*   [x] **Kênh In-App:** Hiển thị Banner trên màn hình chính của App MoMo cho tệp khách hàng có số dư ví chính cao để chuyển đổi họ sang sử dụng AI.

### 3. Cam kết nguồn lực & Đầu mối phê duyệt (Stakeholders & Commitments)
*   **Đầu mối phê duyệt phía Web Platform (Web Product Lead):** Hien.ho
*   **Đầu mối phê duyệt nghiệp vụ phía Cell Team Wealthtech:** Nguyễn Văn A (PO)
*   **Đầu mối phê duyệt Pháp lý (Legal Approval):** Trần Thị L - legal@momo.vn *(Bắt buộc duyệt nội dung khuyến nghị đầu tư của AI trước khi Go-live)*
*   **Đầu mối vận hành kỹ thuật (Tech Lead Cell Team):** Lê Văn C (Tech Lead)
*   **Cam kết đồng hành:**
    *   [x] **Cam kết nguồn lực:** PO Wealthtech cam kết dành tối thiểu 3 giờ/tuần tham gia họp tiến độ và rà soát chất lượng huấn luyện mô hình AI chatbot.
    *   [x] **Chất lượng nội dung:** Đội ngũ Nghiệp vụ cam kết kiểm soát chặt chẽ các kịch bản trả lời của AI, đảm bảo tuân thủ đầy đủ quy định của Ủy ban Chứng khoán Nhà nước.

### 4. Quản trị rủi ro tiềm tàng (Potential Risk)

| Rủi ro (Risk) | Mức độ ảnh hưởng (Impact) | Phương án giảm thiểu (Risk management plan) | Người chịu trách nhiệm (PIC) |
|---|---|---|---|
| AI Chatbot đưa ra lời khuyên đầu tư sai lệch hoặc cam kết lợi nhuận ngoài ý muốn (AI Hallucination). | Cao | - Áp dụng cơ chế RAG giới hạn phạm vi trả lời trong thư viện tài liệu đã được Legal duyệt.<br>- Thêm cảnh báo từ chối trách nhiệm (Disclaimer) ở đầu mỗi phiên chat: *"Mọi phản hồi của AI chỉ mang tính chất tham khảo, không cấu thành lời khuyên đầu tư chính thức."* | PO & Tech Lead AI |
| Rò rỉ thông tin chi tiêu cá nhân của người dùng qua kênh Web. | Nghiêm trọng | - Tuyệt đối không hiển thị bất kỳ thông tin cá nhân thực tế nào trên Kênh Web.<br>- Mã hóa các tham số chuyển tiếp qua Deep Link bằng giao thức mã hóa một chiều an toàn. | Tech Lead Cell Team |

---

## LỊCH SỬ THAY ĐỔI (Changelog)

| Phiên bản | Ngày cập nhật | Người thực hiện | Nội dung thay đổi |
|---|---|---|---|
| 1.0 | 2026-06-30 | PO Wealthtech | Khởi tạo tài liệu PRD nháp đầu tiên cho dự án MoMo SmartWealth AI |
