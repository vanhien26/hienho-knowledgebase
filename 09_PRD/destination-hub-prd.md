# PRODUCT REQUIREMENT DOCUMENT (PRD) - WEB & IN-APP CHANNEL
*Dự án chiến lược: MoMo Destination Hub - Cổng Thông Tin & Đặt Dịch Vụ Du Lịch Outbound*

## THÔNG TIN CHUNG (Metadata)
> *   **Tên dự án / Sản phẩm (PRODUCT NAME):** MoMo Destination Hub (Cổng Thông Tin & Đặt Dịch Vụ Du Lịch Quốc Tế)
> *   **Phiên bản & Ngày (Version & Date):** Version 1.0 - 30/06/2026
> *   **Đơn vị đề xuất (Business Owner / Cell Team):** Joint Team: Cell Team OTA (MoMo Travel) & Cell Team Telco/Fintech
> *   **Web Product Lead (Đầu mối tiếp nhận & phê duyệt):** Hien.ho
> *   **Product Owner (PO) phụ trách:** Trần Minh E - po-ota@momo.vn
> *   **Product Manager (Người phê duyệt sản phẩm):** Nguyễn Văn F - pm-destination@momo.vn
> *   **Engineer Lead (Người phụ trách kỹ thuật):** Hoàng Văn G - tech-ota@momo.vn
> *   **UI/UX Designer:** Lê Thị H - ux-travel@momo.vn
> *   **Trạng thái tài liệu (Document status):** DRAFT
> *   **Giai đoạn S-P-A dự kiến:** Stage S (reSearch) & Stage P (Pilot) - Triển khai Q3/2026
> *   **Loại yêu cầu:**
>     *   [x] **1. Tính năng mới (New Feature):** Xây dựng Cổng thông tin Destination Hub (Web Landing Pages) kết hợp Widget tính toán tỷ giá ngoại tệ và luồng in-app mua sắm combo dịch vụ Outbound (eSIM + Vé bay + Khách sạn + QR Thanh toán quốc tế).

---

## I. RELATED DOCUMENTS
*Các liên kết tài liệu nghiệp vụ, thiết kế và thông tin nền tảng.*

*   [x] **Figma Design Link:** `https://www.figma.com/file/momo-destination-hub-prototype`
*   [x] **Tài liệu tham chiếu eSIM Du Lịch:** [esim-du-lich-brd.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_USE_CASE_MOMO/esim-du-lich-brd.md)
*   [x] **Tài liệu tham chiếu MoMo Travel (OTA):** [ota-brd.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_USE_CASE_MOMO/ota-brd.md)
*   [x] **Tài liệu đặc tả API đối tác (Gohub eSIM / Agoda Hotel):** `https://api-docs.momo.vn/travel/v1/integrations`

---

## II. BACKGROUND & PROBLEM STATEMENT

### 1. Bối cảnh dự án (Background)
Thị trường du lịch nước ngoài (Outbound) của Việt Nam đang tăng trưởng bùng nổ, với hơn 5.44 triệu lượt khách xuất cảnh trong 9 tháng đầu năm 2025 (+33.1% YoY).
Người Việt đi du lịch tự túc ngày càng trẻ hóa và có xu hướng lập kế hoạch hoàn toàn trên môi trường số. Tuy nhiên, thay vì mua dịch vụ trọn gói (Tour), họ tự đặt riêng lẻ từng dịch vụ. Nhận thấy MoMo có đầy đủ mảnh ghép sản phẩm (Vé máy bay quốc tế, Khách sạn, eSIM du lịch của đối tác Gohub, và các phương thức thanh toán xuyên biên giới như liên kết QR quốc tế qua Lắp QR code - e.g. PromptPay ở Thái Lan, NETS ở Singapore), chúng ta cần xây dựng một **Destination Hub** tập trung để tạo trải nghiệm đồng nhất và bán chéo (cross-sell) hiệu quả.

### 2. Vấn đề cần giải quyết (Problem)
*   **Hành trình rời rạc & Phức tạp (User Friction):** Khách du lịch outbound đang phải mở 3-4 nền tảng khác nhau: Đặt vé trên Traveloka, đặt phòng trên Agoda, đặt SIM du lịch trên Klook hoặc Shopee, và đổi tiền mặt hoặc mở thẻ tín dụng riêng. Điều này làm gia tăng sự bất tiện và rủi ro thanh toán.
*   **Thiếu nhận diện thương hiệu về mảng Outbound (Low Mindshare):** Người dùng chưa định vị MoMo Travel là một kênh mua vé quốc tế và đặt khách sạn nước ngoài chất lượng. Các dịch vụ eSIM của MoMo bị chôn sâu dưới menu viễn thông và không tiếp cận được đúng tệp khách đang lên kế hoạch đi du lịch.
*   **Nỗi lo thanh toán & Phí ẩn (Payment Pain Points):** Khi chi tiêu ở nước ngoài, khách hàng cực kỳ lo sợ:
    *   Phí chuyển đổi ngoại tệ của ngân hàng quá cao (từ 3% - 4.5% mỗi giao dịch).
    *   Tỷ giá quy đổi mập mờ, không minh bạch.
    *   Rủi ro mất thẻ vật lý hoặc thiếu thẻ tín dụng khi thanh toán đặt phòng khách sạn.

---

## III. OBJECTIVES & VALUE PROPOSITION

### 1. Mục tiêu & Chỉ số đo lường (Objectives, Goals & Success criteria)
Dự án hướng tới việc tối ưu hóa tỷ lệ bán chéo dịch vụ và khẳng định vị thế "All-in-one Travel Hub" của MoMo cho thị trường du lịch nước ngoài.

| Chỉ số (KPI) | Trước thay đổi (Baseline) | Mục tiêu sau thay đổi (Target) | Thời gian đo lường (Timeframe) |
|---|---|---|---|
| Traffic truy cập Hub Web | 0 | > 250,000 Pageviews/tháng | 3 tháng sau ra mắt |
| Tỷ lệ chuyển đổi Web-to-App (W2A CR) | 0% | > 12% | 3 tháng sau ra mắt |
| Tỷ lệ bán chéo sản phẩm (Cross-sell Rate) | < 2% (Mua vé bay có kèm eSIM) | > 15% khách mua vé máy bay quốc tế sẽ mua kèm eSIM hoặc Khách sạn | 6 tháng sau ra mắt |
| Doanh thu từ thanh toán QR Quốc tế | N/A | Tăng trưởng giao dịch QR quốc tế (outbound) đạt +35% MoM | 6 tháng sau ra mắt |
| Tốc độ tăng trưởng doanh số eSIM du lịch | N/A | Tăng trưởng +45% YoY | Q4/2026 |

### 2. Tuyên ngôn giá trị (Value Proposition)
> Chúng tôi giúp **người Việt đi du lịch tự túc nước ngoài** **lên kế hoạch, chuẩn bị kết nối internet, đặt vé máy bay, khách sạn và quản trị chi phí thanh toán quốc tế chỉ trong 3 phút** bằng cách **cung cấp cổng Destination Hub - nền tảng trọn gói giúp tự động đồng bộ hành trình, tích hợp eSIM kích hoạt ngay và tối ưu hóa tỷ giá quy đổi ngoại tệ khi quét QR quốc tế.**

---

## IV. TARGET PERSONAS & HIGH-LEVEL USER EXPERIENCE (JTBD)

### 1. Khách hàng mục tiêu (Target Personas)
*   **Persona 1: Trang (26 tuổi) - Gen Z đam mê xê dịch tự túc**
    *   *Hành vi:* Thường đi Thái Lan, Singapore 2 lần/năm. Thích check-in, cập nhật Story mạng xã hội liên tục.
    *   *Nỗi đau:* Sợ shock bill chuyển vùng quốc tế, lười mang nhiều tiền mặt vì sợ rơi mất, muốn thanh toán không tiền mặt tiện lợi như ở Việt Nam.
*   **Persona 2: Anh Nam (35 tuổi) - Trưởng nhóm du lịch gia đình**
    *   *Hành vi:* Đặt vé và khách sạn cho cả nhà 4 người đi Nhật Bản.
    *   *Nỗi đau:* Rất mệt mỏi khi phải quản lý vé máy bay của 4 người, đặt 2 phòng khách sạn, mua 4 cái SIM vật lý rồi loay hoay tháo lắp khi xuống sân bay. Cần sự đơn giản, an tâm tuyệt đối cho gia đình.

### 2. Jobs-to-be-Done (JTBD)

#### A. Product JTBD (Hành trình tích hợp trên Web & App)
*   **Khi bối cảnh xảy ra (When...):** Khi tôi đã quyết định chọn điểm đến (ví dụ: Thái Lan) và chuẩn bị đặt vé/khách sạn cho chuyến đi sắp tới.
*   **Hành động tôi muốn thực hiện (I want to...):** Đặt mua cùng một lúc vé máy bay khứ hồi, phòng khách sạn, eSIM du lịch và kích hoạt trước phương thức thanh toán QR không tiền mặt của MoMo tại điểm đến.
*   **Kết quả kỳ vọng (So I can...):** Hoàn thành toàn bộ công tác chuẩn bị chuyến đi tại một nơi duy nhất, nhận mã eSIM cài đặt ngay bằng mã QR trước khi bay, hạ cánh là có mạng dùng và tự tin quét QR mua sắm tại Thái Lan bằng tiền trong ví MoMo mà không cần đổi nhiều ngoại tệ mặt.
*   **Phân tích 3 cấu thành:**
    *   *Functional (Chức năng):* Đặt trọn bộ dịch vụ (Vé + Phòng + eSIM) trong 1 luồng thanh toán duy nhất, hiển thị tỷ giá quy đổi VNĐ real-time chuẩn xác.
    *   *Emotional (Cảm xúc):* Cảm giác an tâm hoàn toàn, không lo sợ bị "mất kết nối" hay gặp rủi ro tài chính khi xuất cảnh.
    *   *Social (Xã hội):* Trở thành người du lịch thông thái, hiện đại, không cần phụ thuộc vào đại lý tour truyền thống.

#### B. SEO/GEO JTBD (Chiến lược kéo Traffic Web cho Hub)
*   **Từ khóa / Câu hỏi nguồn (Search Intent):** `mua esim thái lan ở đâu`, `quét mã qr ở thái lan bằng momo`, `đặt phòng khách sạn agoda qua momo`, `kinh nghiệm mua sim du lịch nhật bản`.
*   **Khi người dùng tìm kiếm (When...):** Khi người dùng đang tìm kiếm các bài viết cẩm nang chuẩn bị hành trang đi du lịch nước ngoài tự túc trên Google hoặc hỏi các công cụ AI.
*   **Nội dung họ cần đọc (I want to...):** Tìm thấy Landing Page của MoMo chuyên về điểm đến đó (ví dụ: `momo.vn/esim-du-lich/thai-lan`), cung cấp công cụ widget so sánh chi phí thanh toán (MoMo QR vs. Thẻ tín dụng truyền thống) và bảng chọn gói dịch vụ đi kèm.
*   **Hành vi chuyển đổi kỳ vọng (So I can...):** Nhấp chọn gói combo ưu đãi và chuyển đổi liền mạch sang App MoMo để thanh toán hoàn tất.

---

## V. BUSINESS CONTEXT & PRODUCT SPECS

### 1. Cấu trúc cổng dịch vụ (Destination Hub Structure)
Hệ thống Destination Hub sẽ được tổ chức theo cấu trúc hình cây (Hub-and-Spoke model):
*   **Trang Hub chính (Destination Hub Portal):** `momo.vn/du-lich-quoc-te` ➔ Hiển thị bản đồ tương tác, tổng hợp các ưu đãi hot nhất cho toàn bộ các nước Outbound và cung cấp widget so sánh tỷ giá ngoại tệ.
*   **Trang điểm đến cụ thể (Destination Pages):** `momo.vn/du-lich-quoc-te/{quoc-gia}` (Ví dụ: `/thai-lan`, `/singapore`, `/nhat-ban`). Mỗi trang điểm đến chứa 4 cấu phần dịch vụ:
    1.  **Tab 1: Vé Máy Bay Quốc Tế:** Hiển thị giá vé rẻ nhất trong tháng (Fare API real-time) đi đến nước đó.
    2.  **Tab 2: Khách Sạn Khuyên Dùng:** Các khách sạn hàng đầu tại các thành phố lớn của nước đó được phân phối qua đối tác (Agoda/Booking.com).
    3.  **Tab 3: eSIM Du Lịch:** Danh sách gói cước eSIM từ đối tác Gohub phù hợp cho chuyến đi (số ngày, dung lượng data/ngày).
    4.  **Tab 4: Cẩm Nang Thanh Toán:** Hướng dẫn cách quét QR MoMo thanh toán tại nước sở tại (Ví dụ: quét mã PromptPay tại Thái Lan, NETS tại Singapore, PayPay tại Nhật Bản) kèm công cụ tính toán tỷ giá thực tế để chứng minh lợi ích kinh tế (không phí ẩn, tỷ giá tốt hơn đổi tiền mặt tại sân bay).

### 2. Mô tả nghiệp vụ & Quy tắc tích hợp (Product Rules)
*   **Gói Combo Ưu Đãi (Cross-sell Engine):**
    *   Hệ thống áp dụng chính sách giảm giá thông minh: Khách hàng mua vé máy bay chặng quốc tế bất kỳ sẽ được tự động tặng mã giảm giá **15%** cho gói eSIM du lịch tương ứng với điểm đến đó, hoặc giảm **100,000đ** khi đặt khách sạn.
*   **Cơ chế eSIM:**
    *   Sau khi thanh toán thành công, hệ thống gửi email tự động chứa mã QR eSIM kèm tài liệu hướng dẫn cấu hình (iOS/Android) trong vòng 2 phút.
    *   *Chính sách hoàn hủy:* eSIM chưa kích hoạt được phép hủy và hoàn tiền 100% trong vòng 7 ngày kể từ ngày mua.
*   **Tính năng thanh toán quốc tế (QR Roaming):**
    *   Tích hợp tỷ giá quy đổi ngoại tệ real-time được cập nhật mỗi 30 giây từ ngân hàng đối tác liên kết.
    *   Miễn phí giao dịch quốc tế (Cross-border transaction fee) cho người dùng quét QR trực tiếp từ tài khoản ví (thay vì mức phí 3-4% của thẻ tín dụng truyền thống).

### 3. Giới hạn & Từ cấm (Constraints & Blacklist)
*   **Giới hạn:** Mua eSIM yêu cầu thiết bị của người dùng phải hỗ trợ công nghệ eSIM (từ iPhone XS trở lên, Samsung S20 trở lên...). Hệ thống Web/App phải có widget kiểm tra tính tương thích thiết bị trước khi cho phép thanh toán.
*   **Blacklist:** Không sử dụng các từ *"chuyển vùng quốc tế giá rẻ nhất"* (tránh tranh chấp với các nhà mạng viễn thông Viettel, Mobifone, Vinaphone). Không so sánh tỷ giá trực tiếp bằng cách ghi tên cụ thể của một ngân hàng đối thủ (dùng cụm từ *"Thẻ tín dụng ngân hàng thông thường"*).

---

## VI. FEATURE REQUIREMENTS & RELEASE PHASES

### 1. Lộ trình phát hành (Release Phases)
*   **Phase 1 (MVP - Dự kiến Tháng 9/2026):**
    *   Xây dựng cổng Web Hub chính và 3 trang điểm đến hot nhất: **Thái Lan, Singapore, Nhật Bản**.
    *   Tích hợp tính năng bán chéo (Mua vé bay tự động đề xuất eSIM tại trang thanh toán in-app).
    *   Tích hợp Widget tính toán tỷ giá và cẩm nang thanh toán QR tại nước sở tại.
*   **Phase 2 (Scale - Dự kiến Tháng 11/2026):**
    *   Mở rộng thêm 5 điểm đến: Hàn Quốc, Đài Loan, Trung Quốc, Malaysia, Úc.
    *   Tích hợp gói combo Vé máy bay + Khách sạn (Flight + Hotel bundle) thanh toán 1-lần.
    *   Tích hợp tính năng nhắc nhở chuẩn bị trước chuyến đi qua hệ thống thông báo đẩy (Push Notification) của app MoMo (Ví dụ: *"Còn 3 ngày nữa bay đi Singapore, bạn đã cài đặt eSIM chưa?"*).
*   **Phase 3 (Tối ưu - Dự kiến Q1/2027):**
    *   Hỗ trợ mua sắm miễn thuế (Duty-Free) trước chuyến đi ngay trên MoMo và nhận hàng tại sân bay nước ngoài.
    *   Tích hợp AI Travel Planner thiết kế lịch trình cá nhân hóa dựa trên thời gian bay và địa điểm khách sạn đã đặt.

### 2. Đặc tả yêu cầu chi tiết (User stories and requirements - Phase 1)

#### A. Trải nghiệm Kênh Web (Landing Page & Widget)
*   **Xác thực:** Công khai (Public). Không bắt buộc đăng nhập để xem thông tin và dùng thử máy tính tỷ giá.

| ID | Tính năng (Feature) | User Story | Yêu cầu kỹ thuật Phase 1 |
|---|---|---|---|
| DH-W01 | Destination Filter & Content Hub | As a Web Visitor, I want to filter destinations and view combined options for Flight, Hotel, and eSIM, so that I can prepare my trip easily. | - Thiết kế giao diện thẻ (Tabs) chuyển đổi mượt mà giữa các dịch vụ cho mỗi nước.<br>- Dữ liệu giá vé và khách sạn được cache mỗi 15 phút từ API để đảm bảo tốc độ tải trang tối ưu.<br>- Thiết kế responsive chuẩn mobile-first. |
| DH-W02 | Exchange Rate & Cost Calculator | As a traveler, I want to input foreign currency (e.g., SGD, THB) and compare the cost of MoMo QR vs Traditional Credit Card, so that I can see the savings. | - Tự động tải tỷ giá ngoại tệ hiện tại.<br>- Tính toán: `Số tiền VND = Ngoại tệ * Tỷ giá MoMo` (không phí ẩn).<br>- So sánh với thẻ tín dụng: `Số tiền VND = Ngoại tệ * Tỷ giá ngân hàng + 3% phí chuyển đổi ngoại tệ`. |

#### B. Trải nghiệm in-app MoMo (Mobile App)
*   **Xác thực:** Đăng nhập tài khoản ví MoMo.

| ID | Tính năng (Feature) | User Story | Yêu cầu kỹ thuật Phase 1 |
|---|---|---|---|
| DH-A01 | In-app Cross-sell Checkout | As a MoMo traveler, I want to purchase an eSIM directly at the flight checkout step, so that I don't have to buy it separately later. | - Khi người dùng ở bước thanh toán vé máy bay đi Thái Lan, hiển thị popup đề xuất: *"Thêm eSIM du lịch Thái Lan chỉ với 99,000đ (Đã giảm 15%)"*.<br>- Nếu đồng ý, cộng gộp giá trị đơn hàng và xử lý thanh toán 1-chạm. |
| DH-A02 | eSIM Auto-Delivery & Guide | As an eSIM buyer, I want to receive my QR code and configuration guide inside the app, so that I don't lose it. | - Hiển thị tab "Ví Voucher / Lịch sử dịch vụ" lưu trữ mã QR eSIM dạng SVG.<br>- Hiển thị hướng dẫn từng bước kích hoạt cho 2 hệ điều hành chính (iOS/Android). |

---

## VII. W2A CONVERSION & DATA REQUIREMENTS

### 1. Luồng chuyển đổi Web-to-App (W2A Trigger Points)

| Vị trí CTA trên Web | Câu chữ hiển thị (CTA Text) | Deep Link mở App | Hành động in-app |
|---|---|---|---|
| Widget Vé Máy Bay trên Web | "Đặt vé rẻ trên App MoMo" | `momo://app/travel/flight?destination={country_code}&promo=true` | Mở trực tiếp màn hình tìm kiếm vé máy bay đi quốc gia đó với bộ lọc giá rẻ. |
| Widget Mua eSIM trên Web | "Mua eSIM & Nhận mã ngay" | `momo://app/telecom/esim?country={country_code}&partner=gohub` | Mở màn hình thanh toán gói cước eSIM của nước tương ứng. |
| Tab Cẩm nang thanh toán | "Bật tính năng quét QR Quốc tế" | `momo://app/payment/qr_roaming` | Chuyển hướng người dùng đến trang xác thực và kích hoạt quét QR quốc tế. |

### 2. API Nghiệp Vụ & Fallback Logic
*   **Fallback khi lỗi API giá vé:** Nếu API giá vé thời gian thực bị lỗi hoặc phản hồi lâu hơn 3 giây, giao diện Web sẽ hiển thị mức giá sàn tĩnh trung bình (Ví dụ: *"Vé đi Thái Lan chỉ từ 1,800,000đ"* kèm lưu ý: *"Giá vé thay đổi theo thời gian thực"* và chuyển hướng người dùng vào App tìm kiếm thủ công).
*   **Fallback khi lỗi gửi eSIM:** Nếu hệ thống API Gohub gặp sự cố không sinh được mã QR eSIM sau khi thanh toán, hệ thống MoMo sẽ tự động chuyển trạng thái đơn hàng sang "Đang xử lý", gửi thông báo xin lỗi người dùng và cam kết xử lý hoàn thành thủ công bởi bộ phận CSKH trong vòng 15 phút.

---

## VIII. GOVERNANCE & RISKS

### 1. Kênh phân phối thông tin bổ sung (Distribution Channels)
*   [x] **AI Assistant / RAG Chatbot:** Đồng bộ toàn bộ tài liệu hướng dẫn cài đặt eSIM, danh sách thiết bị hỗ trợ eSIM, hướng dẫn quét QR thanh toán tại Thái Lan/Singapore vào cơ sở tri thức của AI để trả lời khách hàng tự động 24/7.
*   [x] **Help Center:** Xây dựng chuyên mục giải đáp sự cố du lịch outbound trên hệ thống Trợ giúp của MoMo.

### 2. Kênh đẩy Traffic chủ động (Traffic Acquisition Channels)
*   [x] **SEO tự nhiên (Organic Search):** Viết các bài viết tối ưu SEO về du lịch tự túc các nước Đông Nam Á và Đông Á, nhấn mạnh tính tiện lợi của eSIM và thanh toán không tiền mặt.
*   [x] **Kênh In-App:** Đẩy thông báo (Push Notification) đến tệp người dùng vừa mua vé máy bay quốc tế trên MoMo nhưng chưa mua eSIM hoặc đặt phòng khách sạn.

### 3. Cam kết nguồn lực & Đầu mối phê duyệt (Stakeholders & Commitments)
*   **Đầu mối phê duyệt phía Web Platform (Web Product Lead):** Hien.ho
*   **Đầu mối phê duyệt nghiệp vụ phía Cell Team OTA:** Trần Minh E (PO)
*   **Đầu mối vận hành kỹ thuật (Tech Lead Cell Team):** Hoàng Văn G (Tech Lead)
*   **Cam kết đồng hành:**
    *   [x] **Cam kết chất lượng dịch vụ (SLA):** Đội ngũ OTA cam kết duy trì kết nối API eSIM với Gohub hoạt động với tỷ lệ Uptime tối thiểu 99.9%. Đội ngũ CSKH cam kết túc trực hỗ trợ sự cố kết nối eSIM tại nước ngoài 24/7.

### 4. Quản trị rủi ro tiềm tàng (Potential Risk)

| Rủi ro (Risk) | Mức độ ảnh hưởng (Impact) | Phương án giảm thiểu (Risk management plan) | Người chịu trách nhiệm (PIC) |
|---|---|---|---|
| Người dùng mua eSIM nhưng thiết bị không hỗ trợ (không đọc kỹ lưu ý). | Trung bình | - Bổ sung bước kiểm tra/chọn dòng máy (Dropdown select) bắt buộc trên Web/App trước khi nhấn nút "Thanh toán".<br>- Có chính sách hoàn tiền tự động nhanh nếu phát hiện thiết bị chưa từng kích hoạt profile eSIM nào. | PO OTA & Tech Lead |
| Tỷ giá ngoại tệ biến động mạnh gây chênh lệch lỗ cho MoMo khi thanh toán quốc tế. | Cao | - Thiết lập biên độ an toàn tỷ giá (+0.5% so với tỷ giá liên ngân hàng thực tế).<br>- Tự động tạm dừng tính năng QR Roaming nếu API tỷ giá bị mất kết nối quá 10 phút. | Tech Lead Fintech |

---

## LỊCH SỬ THAY ĐỔI (Changelog)

| Phiên bản | Ngày cập nhật | Người thực hiện | Nội dung thay đổi |
|---|---|---|---|
| 1.0 | 2026-06-30 | PO Travel & Telco | Khởi tạo tài liệu PRD đầu tiên cho dự án MoMo Destination Hub |
