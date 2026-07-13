# Web Product Lead - Strategic & OKRs H2 2026

> - **Document:** Web Product Lead - Strategic & OKRs H2 2026
> - **Division:** Growth Platform Division (GPD)
> - **Role:** Web Product Lead (Out-App Traffic Team)
> - **Owner:** Văn Hiến
> - **Direct Manager:** Web Platform Manager
> - **Version:** 1.1 · July 2026
> - **Status:** Active
> - **Last updated:** 2026-07-13

---

## I. STRATEGIC CONTEXT

### 1.1. Bối cảnh Thị trường & Thách thức GEO (AI Search)
*   **Sự dịch chuyển của Search:** Hành vi tìm kiếm đang thay đổi nhanh chóng khi lượng tìm kiếm trên Google giảm ~20% YoY (2025), trong khi ChatGPT đạt 700M người dùng hàng tuần và Perplexity đạt 780M truy vấn/tháng. AI Overviews (SGE) hiện xuất hiện trên 13-30% truy vấn, đặc biệt là nhóm tài chính/fintech.
*   **Thực trạng của MoMo:** MoMo đang tụt hậu trong GEO (Generative Engine Optimization) với tỉ lệ AI Chatbot referral còn rất hạn chế (~0%). Tuy nhiên, các đối thủ trong nước (ZaloPay, VPBank, Cake) chưa triển khai `llms.txt` hay AI-native content pipeline. Đây là thời cơ chiến lược để MoMo chiếm lĩnh thị trường tìm kiếm AI.
*   **Elegant Problem:** momo.vn không thể tăng trưởng organic bền vững khi PM phụ thuộc Dev cho mọi thứ, AI sản xuất content không có guardrail, và không ai biết MoMo đang chiếm bao nhiêu % thị trường tìm kiếm.

### 1.2. Thực trạng H1/2026 & Định hướng Hành động H2/2026
*   **Thực trạng H1/2026 (Kết quả & Nền tảng đã đạt được):**
    *   *Traffic & Conversion:* Đạt 5.9M clicks từ organic search. Dự án Ads Website (New to MoMo) mang lại hiệu quả phễu thực tế vượt kỳ vọng (36.8K Installs -> 7K MAU).
    *   *Sản phẩm PLG:* Rollout Phạt Nguội Phase 1 (Live), CIC Simulator widget và thiết lập wireframe cho các công cụ giả lập tài chính Finhub. Chạy thử nghiệm Local SEO cho 39 Merchant.
    *   *Platform Health:* Đưa hệ thống MoSpark CMS vào hoạt động; dọn dẹp crawl waste bằng cách xóa bỏ hơn 3.670 URL rác; tích hợp thành công Identity Platform (Edge Cookie) stitch hành vi người dùng.
*   **Khoảng cách & Định hướng Hành động H2/2026 (Những việc cần giải quyết):**
    *   *Quy mô GenAI & Chất lượng:* Tự động hóa hoàn toàn quy trình sinh nội dung end-to-end trên MoSpark, siết chặt chất lượng nội dung bằng bộ lọc SEO/GEO Scoring Gate (≥ 80 điểm) trước khi publish để tránh lỗi YMYL tài chính.
    *   *PLG & Thẩm quyền Tài chính:* Đóng gói và phát hành chính thức các công cụ giả lập tài chính Finhub; scale-up tự động tạo trang Local SEO cho toàn bộ đối tác Merchant (Ví Trả Sau); tối ưu hóa sâu phễu chuyển đổi Web-to-App.
    *   *Vận hành tự trị của Cell Teams:* Ban hành Platform Guidelines hướng dẫn Cell Teams tự triển khai Mini Web; vận hành Publish Gate để kiểm duyệt và phê duyệt độc lập chất lượng đầu ra trước khi Go-Live mà không phụ thuộc vào nguồn lực lập trình.
    *   *Quản trị domain:* Rà soát crawl budget, quản lý file `robots.txt`/`llms.txt` và rà quét chặn link spam để bảo vệ thẩm quyền tên miền (Domain Authority).

### 1.3. 3 Vai trò Chiến lược (Mandate Chiến lược) của Website momo.vn
Website momo.vn không còn là corporate site hay blog SEO đơn thuần. MoSpark được xây dựng để hiện thực hóa 3 vai trò chiến lược dưới sự quản trị của Web Product Lead:
1.  **Financial & Payment Authority:** Xây dựng momo.vn thành điểm đến uy tín và có thẩm quyền hàng đầu trong ngành tài chính/thanh toán tại Việt Nam thông qua chính sách quản trị chất lượng nghiêm ngặt (Quality Gate, Named Author Policy và nội dung chuẩn YMYL).
2.  **Website Growth Traffic & MAU:** Thúc đẩy lưu lượng truy cập tự nhiên (Organic Traffic) ngoài App và tối ưu hóa tỷ lệ chuyển đổi phễu Web-to-App (W2A) nhằm gia tăng lượng người dùng mới (New User/MAU) hoạt động tích cực.
3.  **Product-Led Growth theo JTBD:** Phát triển các công cụ tiện ích tương tác (Calculators/Simulators) để giải quyết trực tiếp nhu cầu thực tế (Jobs-to-be-Done) của người dùng trên Web, làm đòn bẩy thúc đẩy tăng trưởng tự nhiên dựa trên giá trị sản phẩm.

### 1.4. Nguyên tắc cốt lõi: Product-Led Growth (PLG)
*   **Product-Led Growth (PLG):** Sự tăng trưởng của kênh Web MoMo (momo.vn) được dẫn dắt hoàn toàn bởi chính giá trị của bản thân sản phẩm Web. Các công cụ tương tác, tiện ích (Calculator, Simulator, Checker) đóng vai trò là lõi sản phẩm giúp giải quyết trực tiếp Jobs-to-be-Done (JTBD) của người dùng ngay trên Web. Nội dung (content) chỉ đóng vai trò là lớp hỗ trợ tạo khả năng khám phá (discoverability) và giáo dục. Trải nghiệm sản phẩm tốt sẽ tự nhiên chuyển đổi người dùng sang App (New User/MAU) qua các luồng tối ưu (Smart CTA, pre-filled data) mà không cần quảng cáo gây phiền hay spam nội dung thông tin thuần túy.
*   **Quy tắc bất biến:** Mỗi Use Case mới trên Web phải trả lời được câu hỏi: *"Utility tool của Use Case này là gì?"* và tuân thủ flow chuyển đổi PLG:
    ```
    Content → Keywords → Ranking → Use Case → User Journey → App/Transaction (New User / MAU)
    ```

---

## II. VISION & STRATEGIC FRAMEWORK

### 2.1. Web Platform Vision
> **Scale MoMo to Vietnam's #1 financial destination with 6M monthly visitors via an Agentic, SEO/GEO-first platform that turns underserved market needs into high-authority traffic.**

### 2.2. Strategic Framework - 3 Value Layers (Khung Chiến lược - 3 Lớp Giá trị)
Chiến lược phát triển Web MoMo được xây dựng trên 3 lớp giá trị cốt lõi nhằm tối ưu hóa sự tăng trưởng từ ngoài App vào trong App:
*   **Layer 1 - MoMo (Brand & Authority Governance):** Xây dựng thương hiệu và thẩm quyền tên miền (Domain Authority) của momo.vn thông qua:
    *   *Content Authority:* Sở hữu các Use Cases chiến lược thuộc thị trường underserved (đặc biệt là các dự án cốt lõi như Phạt Nguội, Bảo hiểm ô tô, eSIM du lịch, Cinema) để MoMo thiết lập thẩm quyền nội dung và chiếm vị trí số 1 thị trường.
    *   *AI-powered (GEO):* Cấu trúc nội dung chuẩn semantic để các công cụ tìm kiếm AI (ChatGPT, Gemini, Perplexity) trích dẫn MoMo làm nguồn uy tín.
    *   *Kết quả:* Chuyển hóa thị trường underserved ngoài App (Phạt Nguội, Bảo hiểm ô tô, eSIM du lịch, Cinema...) thành traffic uy tín có tỷ lệ chuyển đổi cao.
*   **Layer 2 - User (Product-Led Growth - PLG):** Phục vụ hành trình tìm kiếm và giải quyết Jobs-to-be-Done (JTBD) của người dùng thông qua:
    *   *Mọi sản phẩm Web đi theo tinh thần PLG:* Định hướng tất cả các sản phẩm xây dựng trên Website momo.vn đều bám sát triết lý tăng trưởng dẫn dắt bởi sản phẩm (Product-Led Growth), tập trung phát triển các tiện ích tương tác giải quyết JTBD với trọng tâm là các công cụ tiện ích tài chính (Financial Utilities) nói riêng và các giải pháp PLG nói chung (như các công cụ tài chính Finhub, CIC Simulator, Phạt Nguội real-time Checker).
    *   *Kết quả:* Giải quyết trực tiếp nhu cầu người dùng ngay trên Web, kích hoạt trải nghiệm "Aha moment" và thúc đẩy hành vi chuyển đổi tự nhiên vào App (New User/MAU) qua các luồng tối ưu (Smart CTA, pre-filled data).
*   **Layer 3 - Cell Team (Platform-as-a-Service - PaaS):** Hỗ trợ các Cell Teams tiếp cận thị trường ngoài App thông qua:
    *   *Mô hình PaaS:* Cung cấp giải pháp, quy trình, nền tảng (MoSpark, boilerplate mẫu, hướng dẫn kỹ thuật SEO/GEO) và kiểm soát chất lượng qua Quality Gate.
    *   *Kết quả:* Các Cell Teams tự chủ xây dựng và vận hành sản phẩm Web nhanh chóng, đúng tiêu chuẩn kỹ thuật và đo lường được ROI.

### 2.3. 4 Growth Pillars (Kiến trúc Thị trường)
momo.vn không tổ chức theo BU mà theo Product/Search Ecosystem. 4 Pillars đại diện cho 4 growth engine độc lập sở hữu các vertical thị trường dưới sự kiểm duyệt kỹ thuật của Web Product Lead:

| Pillar | Use Cases tiêu biểu | Chiến lược Content | Ràng buộc quản trị (Hiến sở hữu & audit) |
|---|---|---|---|
| **P1 - Tài chính & Tín dụng** | CIC Score, Ví Trả Sau, Vay Nhanh | Hub-Spoke kết hợp các Interactive Tools (Tính lãi, Mô phỏng CIC) | **Named Author Policy** - Gate kiểm duyệt cứng bắt buộc trước khi launch |
| **P2 - Bảo hiểm Công nghệ** | Bảo hiểm xe máy, BHYT, BHXH, Bảo hiểm ô tô | Neutral Aggregator - Cổng so sánh trung lập | **Không dùng geo-based URL** cho bảo hiểm |
| **P3 - Dịch vụ Công & Tiện ích** | Phạt Nguội, Thanh toán Hóa đơn | API real-time kết hợp programmatic SEO (pSEO) cho 63 tỉnh | **llms.txt pipeline mandatory** trước khi rollout |
| **P4 - Đời sống & Merchant** | Cinema, OTA, eSIM, Merchant | Intent-first, trang chi tiết Merchant (Merchant Detail Page) | **Noindex mandatory** cho các URL hết hạn |
---

## III. OKRS H2/2026 - WEB PRODUCT LEAD

### Objective 1: Xây dựng và phát triển MoSpark trở thành nền tảng AI-Powered trong hoạt động GenAI Content
*Focus: AI-powered scale, automation flow, content quality gate, and merchant data enrichment.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Hiến (Web Product Lead) |
|---|---|---|---|
| **KR 1.1** | **PLG Project SoV** | Đạt mức tăng trưởng **>30% thị phần (Share of Voice)** cho các dự án tiềm năng hoặc dự án được chỉ đạo. | Xây dựng và vận hành hệ thống quản lý Content Plan theo Topic Cluster và hành vi JTBD User. |
| **KR 1.2** | **GenAI Production Efficiency** | Cắt giảm **80-90% thời gian sản xuất** các định dạng nội dung (Blog, Mini Web, Short Video, Text-to-Speech) và tối ưu chi phí token. | Thiết lập quy trình sinh nội dung tự động end-to-end trên MoSpark CMS, tối ưu Prompt và benchmark chi phí/chất lượng. |
| **KR 1.3** | **Merchant Page Enrichment** | Tự động hóa sản xuất nội dung giới thiệu và làm giàu dữ liệu đối tác bằng AI (**Google Maps API Context**) cho các trang Merchant (Ví Trả Sau). | Thiết kế luồng dữ liệu, context prompt và logic enrich thông tin Merchant để tối ưu Local SEO. |
| **KR 1.4** | **Content Quality Gate** | Đảm bảo **100% nội dung AI sinh ra đạt điểm số chất lượng ≥ 80 điểm** và không dính lỗi kỹ thuật (CWV, broken links). | Quản trị bộ quy tắc chấm điểm (5 blocks) và cơ chế Hard-Block ngăn chặn xuất bản nội dung lỗi trên CMS. |

---

### Objective 2: Tư vấn giải pháp tăng trưởng và đảm bảo các tiêu chuẩn Technical & Content Foundation cho các chiến dịch
*Focus: Tech SEO optimization, growth enablement, and framework implementation.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Hiến (Web Product Lead) |
|---|---|---|---|
| **KR 2.1** | **Web Performance Governance** | Đảm bảo kỹ thuật web luôn ở mức tối ưu, **không phát sinh lỗi kỹ thuật nghiêm trọng** ảnh hưởng đến trải nghiệm người dùng. | Theo dõi chỉ số Core Web Vitals, rà quét lỗi kỹ thuật định kỳ thông qua công cụ chuyên dụng. |
| **KR 2.2** | **Mini Web Implementation (CreditTech)** | Tư vấn và phối hợp triển khai các giải pháp Web-to-App cho các sản phẩm **Ví Trả Sau, Vay Nhanh**. | Trực tiếp thiết kế sitemap, cấu trúc cluster và luồng chuyển đổi W2A tối ưu cho nhóm dịch vụ tài chính. |
| **KR 2.3** | **Campaign PM Support (BMC)** | Đồng hành và hỗ trợ kỹ thuật cho các chiến dịch Inbound đóng vai trò chủ trì (PM) để tối ưu phễu chuyển đổi. | Cố vấn SEO/GEO và kỹ thuật hạ tầng cho các chiến dịch PR, Mega Campaigns của Inbound. |
| **KR 2.4** | **Growth Framework (SPA)** | Áp dụng quy trình **SPA (reSearch - Pilot - Action)** để tư vấn giải pháp tăng trưởng cho các Cell Teams. | Đóng vai trò tư vấn tăng trưởng, thẩm định tính khả thi của dự án (pSEO feasibility) cho các đơn vị nội bộ. |

---

### Objective 3: Xây dựng giải pháp tăng trưởng và thúc đẩy mục tiêu tăng trưởng Web Traffic và MAU
*Focus: Traffic acquisition, conversion optimization, and simulation hooks.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Hiến (Web Product Lead) |
|---|---|---|---|
| **KR 3.1** | **Web Platform Projects (Own Use Cases)** | Triển khai các dự án do Web Platform chủ trì (**Merchant Page** thúc đẩy tăng trưởng và **Phạt Nguội** làm phễu thu hút). | Quản lý vòng đời sản phẩm Phạt Nguội (API realtime, cảnh báo vi phạm) và scale-up Local SEO cho hệ thống Merchant. |
| **KR 3.2** | **Cell Team Growth Projects** | Phối hợp triển khai các dự án (**Vehicle Hub, Cinema, eSIM, Bảo hiểm Ô tô**) đáp ứng cam kết về chỉ số giao dịch/doanh thu. | Hỗ trợ cấu trúc kỹ thuật web, pSEO và tracking cho các Cell Teams để đảm bảo ROI tăng trưởng. |
| **KR 3.3** | **User Growth W2A Funnel** | Thiết lập hệ thống đo lường và tối ưu hóa phễu chuyển đổi Web-to-App (W2A) nhằm thúc đẩy **New User/MAU**. | Phối hợp cùng User Growth tối ưu cơ chế Smart CTA, Universal Links và truyền dữ liệu ngữ cảnh (Zero-Party Data Passing). |
| **KR 3.4** | **Financial Authority (Finhub)** | Xây dựng và phát hành các công cụ giả lập tài chính Finhub Simulation Tools (lương hưu, lãi tiết kiệm, vàng, ngoại tệ...). | Thiết lập logic toán học, kịch bản JTBD và thiết kế wireframe cho các công cụ giả lập để làm phễu organic traffic. |

---

### Objective 4: Đảm bảo các hoạt động trên Website đáp ứng các tiêu chuẩn Technical & Content Foundation
*Focus: Quality gates, domains health, crawl budget optimization, and brand trust.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Hiến (Web Product Lead) |
|---|---|---|---|
| **KR 4.1** | **Platform Guidelines** | Ban hành đầy đủ tài liệu hướng dẫn kỹ thuật (SEO/GEO, tracking) cho các Cell Teams. | Soạn thảo, cập nhật và truyền thông SOP, Guidelines giúp Cell Teams triển khai độc lập. |
| **KR 4.2** | **Quality Gate Auditing** | Thực hiện **kiểm duyệt kỹ thuật nghiêm ngặt 100% dự án Web mới** trước khi Go-live. | Đóng vai trò người gác cổng (Publish Gate), trực tiếp phê duyệt và ký duyệt (sign-off) kỹ thuật trước khi deploy. |
| **KR 4.3** | **Backlink Security** | Kiểm soát, rà quét và **ngăn chặn triệt để 100% nguồn backlink xấu** (spam links) bảo vệ Domain Authority. | Vận hành quy trình kiểm tra sức khỏe link profile, disavow spam links định kỳ. |
| **KR 4.4** | **URL & Content Governance** | Rà soát định kỳ loại bỏ các nội dung lỗi thời và các **URL không có giá trị (zero-traffic/thin content)**. | Tối ưu crawl waste bằng chính sách dọn dẹp URL rác (như xử lý 3.000+ URL rác H1), tối ưu ngân sách cào dữ liệu (Crawl Budget) của Googlebot. |

---

## IV. STRATEGIC ACTIONS & KEY METHODOLOGY FOR H2/2026

1.  **Vận hành Quy chuẩn YMYL & Named Author Policy:**
    *   Enforce quy chuẩn Named Author Policy bắt buộc cho các bài viết thuộc Pillar 1 (Tài chính & Tín dụng) nhằm vượt qua thuật toán đánh giá chất lượng khắt khe của Google và AI Search.
2.  **Đồng bộ Hóa Use Case ID qua Hệ thống Platform:**
    *   Áp dụng Use Case ID làm định danh gốc để liên kết toàn bộ dữ liệu Content, Ads và Analytics, xóa bỏ các Silo của hệ thống cũ.
3.  **Triển khai Thử nghiệm và Tối ưu hóa GEO (AI Citation):**
    *   Ứng dụng `llms.txt` và `robots.txt` nâng cao nhằm kiểm soát ngân sách crawl của AI Bots, hướng tới tối đa hóa citation rate của MoMo trong Google AI Overviews, ChatGPT và Perplexity.
4.  **Enforce Tiêu chuẩn Quality Gate trên MoSpark CMS:**
    *   Sử dụng công thức chấm điểm 5-Block (100 điểm) trực tiếp trên CMS MoSpark. Thực thi hard block đối với các lỗi Core Web Vitals và kỹ thuật SEO nghiêm trọng trước khi xuất bản.
5.  **Duy trì Vòng lặp Kiểm thử SPA (reSearch - Pilot - Action):**
    *   Bảo đảm mọi giải pháp và tính năng mới đều đi qua chu trình nghiên cứu chuyên sâu (Feasibility & Demand), thử nghiệm thực tế (Pilot), và sau đó mới scale-up trên diện rộng.

---

*Tài liệu được biên soạn và bảo trì bởi **Văn Hiến - Web Product Lead**.*
