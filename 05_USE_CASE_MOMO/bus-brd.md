> - **Project:** OTA - BUS (Đặt vé xe khách)
> - **Main URL:** momo.vn/ve-xe
> - **Division:** GPD - OTA (Non-Air)
> - **Owner:** GPD - Out-App Traffic
> - **Governance:** Web Product Lead
> - **Version:** 2.0 - Tháng 05/2026
> - **Status:** Draft
> - **Business Model:** Marketplace - MoMo là nền tảng tra cứu, đặt và thanh toán vé xe khách; thu phí từ nhà xe đối tác

---

> **Problem:** Hàng triệu người Việt tìm vé xe khách mỗi tháng - không tìm thấy MoMo, dù MoMo đang bán vé của hơn 500 nhà xe.
>
> **KPI Owned:** Transactions (số vé bán được) từ web channel → attributed via Appsflyer
>
> **Conversion Flow:** Search "vé xe A đi B" → momo.vn/ve-xe → Chọn nhà xe + giờ đi → Mở MoMo App → Thanh toán vé

---

## 1. Executive Summary

**Situation**

Người dùng Việt Nam có nhu cầu đặt vé xe khách rất lớn và đang tìm kiếm trên Google với tổng lượng tìm kiếm ước tính hơn 5 triệu lượt/tháng (theo Inbound Plan 2025). Hành vi tìm kiếm trải dài qua nhiều intent: tuyến đường cụ thể ("vé xe Sài Gòn đi Đà Lạt"), nhà xe cụ thể ("vé xe Phương Trang"), điểm đến ("xe đi Đà Lạt"), và seasonal peak (vé xe Tết). MoMo hiện là đối tác đặt vé của hơn 500 nhà xe và đã có sản phẩm hoạt động trong App, nhưng web channel gần như vắng mặt trên Search - traffic organic năm 2024 chỉ đạt 84.466 sessions toàn năm, tương đương chưa đến 1,7% market share.

**Complication**

Khoảng cách giữa inventory MoMo (hơn 500 nhà xe) và số user thực sự đặt được vé qua web là rất lớn. Ba lý do từ góc nhìn người dùng:

Thứ nhất, user search "vé xe Phương Trang đi Nha Trang" không gặp trang MoMo nào. Họ vào VeXeRe - dù MoMo có đầy đủ nhà xe đó - vì momo.vn chưa có trang riêng cho từng tuyến đường và từng nhà xe.

Thứ hai, user vào được momo.vn/ve-xe nhưng không đủ thông tin để quyết định: thiếu lịch khởi hành, thiếu giá, thiếu đánh giá nhà xe. Họ thoát ra và tìm chỗ khác.

Thứ ba, user muốn đặt vé nhưng không biết bước tiếp theo - không có luồng rõ ràng từ web vào App để hoàn tất booking.

**Resolution**

Product job cốt lõi: Người dùng tìm vé xe trên Google gặp đúng trang momo.vn với thông tin họ cần - nhà xe, giờ đi, giá, đánh giá - ra quyết định ngay, sau đó mở MoMo App hoàn tất đặt vé trong một flow liền mạch không cần nhập lại.

Nền tảng để đáp ứng toàn bộ search intent: 8 loại trang (Routes, Destination, Bus Operator, Bus Operator + Route, Bus Terminal, Bus Terminal + Destination, Bus Type/Limousine, Vé Xe Tết) - kết hợp blog content dẫn về các trang giao dịch và booking entry point trực tiếp trên trang.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Market Size

| Metric | Giá trị | Ghi chú |
|---|---|---|
| Tổng lượng search/tháng (ước tính) | ~5.000.000 searches | Inbound Plan 2025 [cần verify GSC + Ahrefs] |
| Market share momo.vn hiện tại (2024) | ~1,7% | 84.466 sessions / 5M market |
| Target market share 2025 (Base Case 1) | 4,4% | 1.035.000 sessions |
| Target market share 2025 (Base Case 3) | 5,2% | 1.500.000 sessions |
| Số nhà xe trên MoMo | 500+ | Theo PPTX slide 4 |
| Tickets processed (top merchant) | 571.861 (xe Phương Trang) | Dashboard BUS Performance |

### 2.2 Hiện Trạng Traffic

| Năm | Total Sessions | Click to App | CR W2A |
|---|---|---|---|
| 2022 | ~17.886 | Chưa có data | - |
| 2023 | 75.266 | 3.319 | ~4,4% |
| 2024 | 84.466 | 9.085 | ~10,8% |
| 2025 (Base Case 1 target) | 1.035.000 | 73.100 | ~7,1% |

*Nhận xét: CR W2A 2024 đạt 10,8% là tín hiệu tốt - người dùng đến từ organic có intent cao. Vấn đề là volume traffic quá thấp. Growth 2022-2024 chủ yếu đến từ tự nhiên, chưa có đầu tư có hệ thống.*

### 2.3 Competitive Landscape

| Đối thủ | Điểm mạnh | Điểm yếu so với MoMo |
|---|---|---|
| VeXeRe (vexere.com) | Hàng nghìn trang programmatic, domain authority cao, blog du lịch tốt | Không có super-app ecosystem, không có MoMo Pay |
| BusMap | App-first, dữ liệu realtime tốt | Web channel yếu hơn VeXeRe |
| Baolau.vn | SEO blog mạnh, coverage tuyến đường rộng | Ít nhà xe hơn MoMo |

**MoMo's moat:** Inventory nhà xe lớn (500+), hệ sinh thái thanh toán, user trust. Chưa được khai thác qua web channel.

### 2.4 Keyword Clusters

| Cluster | Intent | Ví dụ keyword | Volume Est. |
|---|---|---|---|
| Routes | Commercial - Do | "vé xe Sài Gòn đi Đà Lạt" | Cao |
| Bus Operator | Commercial - Do | "vé xe Phương Trang", "xe Điền Linh" | Cao |
| Destination | Informational + Commercial | "xe đi Đà Lạt", "vé xe đi Nha Trang" | Cao |
| Bus Terminal | Informational | "bến xe Miền Tây", "bến xe Miền Đông" | Trung bình |
| Bus Type | Commercial | "xe limousine Sài Gòn Đà Lạt" | Trung bình |
| Seasonal - Tết | Commercial - High urgency | "vé xe Tết 2026", "vé xe tết Sài Gòn" | Spike cao theo mùa |
| Blog / Guide | Informational | "kinh nghiệm đi xe khách", "nhà xe uy tín" | Trung bình |

---

## 3. Định Hướng Dự Án

### Product Job Cốt Lõi

Người dùng search vé xe trên Google - tìm thấy momo.vn với đúng thông tin họ cần (nhà xe, tuyến đường, giá, đánh giá) - đưa ra quyết định ngay trên web - mở App để thanh toán nhanh.

3 outcomes phát sinh từ product job này:
- New user acquisition: người dùng chưa có MoMo App install App để thanh toán vé
- Re-engagement: người dùng đã có App quay lại dùng tính năng vé xe
- Brand recall: MoMo Travel - BUS được associate với search intent vé xe khách

### Dự án này KHÔNG phải là:

- Một chiến dịch paid traffic hay remarketing
- Một tính năng App mới - web là entry point, App là transaction layer
- Blog travel thuần túy - content phải anchor vào booking intent
- Một project độc lập: BUS web là một phần của hệ sinh thái OTA (phối hợp với Air, Hotel)

### PLG Hook

PLG hook của BUS là **Search Widget + Booking Flow liền mạch trên web**. Cụ thể:

User search tuyến đường → vào trang Routes → thấy danh sách nhà xe kèm giá realtime → chọn chuyến → deep link mở MoMo App với pre-fill thông tin → thanh toán trong App.

Khác với use case Vay Nhanh hay BH có calculator giúp user convert mà không cần login, BUS có booking flow tự nhiên dẫn vào App - đây là PLG hook mạnh vì user đã ở bước "muốn mua" khi vào trang.

### Pre-conditions - Phải Giải Quyết Trước Khi Commit Build

**Thiếu 1 trong 4 - dừng lại.**

| # | Pre-condition | Trạng thái | Owner giải quyết |
|---|---|---|---|
| P1 | Các landing pages (Routes, Destination, Operator...) hoàn thành xây dựng và được Google index trước thời điểm T | Đang triển khai | Web Platform + Dev |
| P2 | Content API hoặc ChatGPT-generated content pipeline hoạt động và phủ đủ trang programmatic | Pilot - chưa confirm | Inbound + Tech |
| P3 | Internal Link API hoặc cơ chế thay thế giữa các page types được cấu hình đúng | Chưa giải quyết | Tech |
| P4 | Tracking web (GA4 event + Appsflyer W2A) được setup trước khi launch để có baseline data | Chưa setup | Web Data Tracking |

---

## 4. JTBD Analysis

### Job 1: "Tôi cần tìm chuyến xe cụ thể từ A đến B, chọn nhà xe và giờ đi phù hợp"

| Dimension | Chi tiết |
|---|---|
| Functional | Tra cứu chuyến xe theo tuyến đường + ngày đi, xem nhà xe, giờ khởi hành, giá vé |
| Trigger | Cần đi về quê, đi du lịch, đi công tác - thường lên kế hoạch 1-7 ngày trước |
| Emotional | Muốn chắc chắn chọn được nhà xe uy tín, không bị miss chuyến |
| Social | Mua vé xong chia sẻ link lên nhóm chat cho cả nhà confirm giờ đi |
| Search → App | "vé xe Sài Gòn Đà Lạt" → /ve-xe/ve-xe-khach-tu-ho-chi-minh-di-da-lat → Chọn chuyến → Mở App → Thanh toán |

### Job 2: "Tôi đã biết nhà xe muốn đi, cần xem lịch + đặt vé nhanh"

| Dimension | Chi tiết |
|---|---|
| Functional | Search tên nhà xe, xem tất cả tuyến đường nhà xe đó chạy, chọn tuyến phù hợp |
| Trigger | Đã dùng nhà xe này trước đó và hài lòng, muốn dùng lại |
| Emotional | Tiết kiệm thời gian so sánh - đã có preference nhà xe |
| Social | Nhắn bạn: "Đi Phương Trang là ổn, mình hay đặt trên MoMo" - không cần giải thích thêm |
| Search → App | "vé xe Phương Trang" / "xe Điền Linh Limousine" → /ve-xe/xe-phuong-trang → Chọn tuyến + chuyến → Mở App |

### Job 3: "Tôi muốn đến một điểm đến cụ thể, chưa biết chọn nhà xe nào"

| Dimension | Chi tiết |
|---|---|
| Functional | Xem tất cả nhà xe có tuyến đến điểm đến mình muốn, so sánh giá và thời gian |
| Trigger | Lên kế hoạch chuyến đi chưa rõ lịch trình - đang ở giai đoạn khám phá |
| Emotional | Muốn có overview toàn diện trước khi quyết định |
| Social | Share link trang Đà Lạt cho cả nhóm cùng chọn nhà xe và chuyến đi |
| Search → App | "xe đi Đà Lạt", "vé xe đến Nha Trang" → /ve-xe/da-lat → Chọn nhà xe → Mở App |

### Job 4: "Tôi cần đặt vé xe Tết sớm trước khi hết chỗ"

| Dimension | Chi tiết |
|---|---|
| Functional | Xem vé xe Tết còn hay hết, nhà xe nào còn chỗ, giá bao nhiêu |
| Trigger | Gần đến Tết (tháng 11-12) + nghe người quen nói vé sắp hết |
| Emotional | Lo lắng không có vé về quê - high urgency, high anxiety |
| Social | Nhắn anh chị: "Còn vé Tết đó, đặt ngay đi trước khi hết" - tự mình đã check rồi |
| Search → App | "vé xe Tết 2026", "mua vé xe Tết sớm" → /ve-xe/ve-xe-tet → Booking → Mở App |

### Job 5: "Tôi muốn đi xe limousine/VIP cho chuyến đi thoải mái hơn"

| Dimension | Chi tiết |
|---|---|
| Functional | Tìm nhà xe có dịch vụ limousine cho tuyến cụ thể, xem chất lượng xe |
| Trigger | Chuyến đi xa (>3 giờ), đi cùng đối tác/người lớn tuổi, không muốn vé bình thường |
| Emotional | Muốn thoải mái, thể hiện mình chọn lựa tốt |
| Social | Book limousine cho cả team đi công tác - chọn MoMo trông chuyên nghiệp hơn đặt lẻ từng người |
| Search → App | "xe limousine Sài Gòn Đà Lạt" → /ve-xe/limousine-tu-ho-chi-minh-di-da-lat → Mở App |

### Job 6: "Tôi cần thông tin về bến xe (giờ mở cửa, bến nào phù hợp, xe nào xuất phát từ bến này)"

| Dimension | Chi tiết |
|---|---|
| Functional | Xem nhà xe xuất phát từ bến xe cụ thể, giờ chạy, cách di chuyển đến bến |
| Trigger | Không rõ mình nên ra bến nào, cần chọn bến gần nơi ở |
| Emotional | Lo lắng ra sai bến, miss xe |
| Social | Tự tìm được thông tin bến xe mà không cần hỏi người quen - chủ động lộ trình |
| Search → App | "bến xe Miền Đông đi Đà Nẵng" → /ve-xe/ben-xe-mien-dong-di-da-nang → Chọn nhà xe → Mở App |

---

## 5. Kiến Trúc Web / Phạm Vi Build

### 5.1 Sitemap - Hub & Spoke

```
/ve-xe                              (Hub - Home)
├── /ve-xe/ve-xe-khach-tu-[A]-di-[B]      (Routes - pSEO)
├── /ve-xe/[tinh-thanh-pho]               (Destination - pSEO)
├── /ve-xe/xe-[nha-xe]                    (Bus Operator - pSEO)
├── /ve-xe/nha-xe-[nha-xe]-tu-[A]-di-[B]  (Bus Operator + Route - pSEO)
├── /ve-xe/ben-xe-[ben-xe]                (Bus Terminal - pSEO)
├── /ve-xe/ben-xe-[ben-xe]-di-[diem-den]  (Bus Terminal + Destination - pSEO)
├── /ve-xe/limousine-tu-[A]-di-[B]        (Bus Type - pSEO)
├── /ve-xe/ve-xe-tet                      (LDP Seasonal)
├── /ve-xe/khuyen-mai                     (Promotions)
├── /ve-xe/blog                           (Blog Hub)
│   └── /ve-xe/blog/[slug]               (Blog Articles)
└── /ve-xe/tra-cuu-ve                     (Search Tool)
```

### 5.2 URL Architecture

| Page Type | URL Pattern | Ưu tiên | Volume Potential | Số URL ước tính |
|---|---|---|---|---|
| Home | /ve-xe | P1 | Cao (head term) | 1 |
| Routes | /ve-xe/ve-xe-khach-tu-[A]-di-[B] | P1 | Rất cao | 500-1.000+ |
| Destination | /ve-xe/[tinh-thanh-pho] | P1 | Cao | 63 tỉnh thành |
| Bus Operator | /ve-xe/xe-[nha-xe] | P1 | Cao | 500+ nhà xe |
| Bus Operator + Route | /ve-xe/nha-xe-[nha-xe]-tu-[A]-di-[B] | P1 | Rất cao (long-tail) | 2.000+ |
| Bus Terminal | /ve-xe/ben-xe-[ben-xe] | P2 | Trung bình | 50-100 bến xe |
| Bus Terminal + Destination | /ve-xe/ben-xe-[ben-xe]-di-[diem-den] | P2 | Trung bình | 200+ |
| Bus Type (Limousine) | /ve-xe/limousine-tu-[A]-di-[B] | P2 | Trung bình | 100-200 |
| LDP Tết | /ve-xe/ve-xe-tet | P1 (seasonal) | Spike cao tháng 11-1 | 1 (evergreen URL) |
| Blog | /ve-xe/blog + articles | P2 | Trung bình - dài hạn | 200-800 bài |
| Promotions | /ve-xe/khuyen-mai | P3 | Thấp | 1 |

### 5.3 On-Page Component Anatomy (Các trang P1)

**Routes Page - /ve-xe/ve-xe-khach-tu-[A]-di-[B]**

| Block | Mô tả | SEO Purpose |
|---|---|---|
| Breadcrumb | MoMo > Vé xe khách > Vé xe đi từ A đến B | Schema BreadcrumbList |
| H1 | "Danh sách các chuyến xe từ A đi B" | Primary keyword target |
| Search Widget (Product) | Module tìm vé theo ngày/người | PLG hook - booking entry |
| Long Content | Top XX nhà xe từ A đi B - có Table of Contents, outline từng nhà xe | Semantic depth, internal linking |
| Navigation Block | 20 anchor text Routes liên quan (B đi C, D đi B...) | Internal linking, crawl depth |
| Blog Embed | 3-4 bài blog liên quan | EEAT, semantic relevance |
| FAQ | 5 câu hỏi về tuyến đường | FAQPage schema, AEO |

**Bus Operator Page - /ve-xe/xe-[nha-xe]**

| Block | Mô tả | SEO Purpose |
|---|---|---|
| Breadcrumb | MoMo > Vé xe khách > Nhà xe | Schema BreadcrumbList |
| H1 | "Đặt vé xe [Tên nhà xe] với mức giá tốt nhất trên MoMo" | Brand + commercial intent |
| Giới thiệu nhà xe | Mô tả sơ lược, ảnh nhà xe | E-E-A-T |
| Long Content | XX tuyến đường nhà xe hoạt động | Programmatic content |
| FAQ | 5 câu hỏi về nhà xe | FAQPage schema |
| Blog Embed | Bài blog liên quan | Internal linking |

### 5.4 Schema Requirements

| Page Type | Schema |
|---|---|
| Routes, Bus Operator + Route | BusTrip, BusStop, Product, Offer |
| Destination | ItemList, Place |
| Bus Operator | LocalBusiness, Review |
| Bus Terminal | Place, LocalBusiness |
| Blog | Article, BreadcrumbList |
| LDP Tết | Event, Offer |
| Tất cả | FAQPage (trên các trang có FAQ block) |

---

## 6. Success Metrics

### North Star Metric

**Transactions (số vé bán được) từ web channel - được tracked via Appsflyer**

Lý do chọn Transactions thay vì W2A: W2A đo việc user mở App nhưng chưa xác nhận mua vé. Transactions = vé bán thành công sau thanh toán - đây mới là bước tạo revenue trực tiếp cho MoMo từ web channel. W2A và Organic Sessions là Tier B metrics đo tiến trình funnel.

*KPI Alignment Note: Giai đoạn đầu khi Transactions baseline chưa có - track W2A làm proxy. Sau 30 ngày đủ data Appsflyer thì chuyển North Star về Transactions.*

### Targets (Base Case 1 - Recommended)

| Metric | Lane | Target 2025 | Timeframe | Tracking |
|---|---|---|---|---|
| Transactions (vé bán được) | North Star | Establish baseline T+1, set target T+3 | T+12 | Appsflyer |
| Click to App (W2A) | Tier B | 73.100 clicks | T+12 | GA4 + Appsflyer |
| Organic Sessions | Tier B | 1.035.000 sessions | T+12 | GSC + GA4 |
| W2A Conversion Rate | Tier B | ~7,1% | EOY 2025 | GA4 |
| Organic Market Share | Tier B | 4,4% của 5M search/month | T+12 | GSC + SEO tools |
| Keyword Top 10 (Routes) | Tier B | [cần define số lượng cụ thể] | T+6 | GSC |
| Indexed Pages | Tier B | [cần define - ước tính 2.000+ URLs] | T+3 | GSC |


---

## 7. Dependencies & Constraints

### Dependencies

| Dependency | Mô tả | Blocker? | Status |
|---|---|---|---|
| Web Platform - Page Build | Hoàn thành build 8 loại page types trước thời điểm T launch | Có | Đang triển khai |
| Tech - Google Indexing | Các trang phải được Google index trước T để có thời gian rank | Có | Phụ thuộc P1 |
| Tech - Content Pipeline | ChatGPT pipeline hoặc Content API generate long content cho programmatic pages | Có | Pilot chưa confirm |
| Tech - Internal Link API | Cơ chế cross-link tự động giữa Routes/Operator/Destination | Có | Chưa giải quyết |
| App Data Tracking | Appsflyer setup W2A attribution cho BUS | Có | Chưa setup |
| Web Tracking (GA4) | Event tracking setup trước launch: page view, CTA click, booking initiation | Có | Chưa setup |
| BU/PO OTA | Xác nhận danh sách nhà xe, tuyến đường, giá realtime được expose qua API cho web | Có | Cần confirm |

### Constraints

- KHÔNG can thiệp UX/UI của booking flow - Inbound chỉ đề xuất Canonical, không yêu cầu chỉnh sửa trang payment
- KHÔNG build mobile app riêng cho BUS web - toàn bộ transaction xảy ra trong MoMo App
- Canonical phải được set đúng trên tất cả trang parameter (date, number of passengers) về trang canonical Routes/Operator
- Content có liên quan đến giá vé phải được cập nhật realtime hoặc ghi rõ disclaimer "giá tham khảo, có thể thay đổi" để tránh YMYL violation
- Google Core Algorithm Updates có thể tác động đến ranking tại 4 thời điểm/năm (tháng 3, 6, 9, 12) - không thể kiểm soát

---

## Change Log

- **Tháng 05/2025 (v1.0):** Khởi tạo BRD từ 3 input: Dashboard BUS Performance, Inbound Plan 2025, Advanced Mini Web PPTX. Base Case 1 được chọn làm reference target chính.
- **Tháng 05/2026 (v2.0):** Apply BRD CEO Standard - (1) Fix Problem Statement: bỏ SEO language, reframe user-centric; (2) Fix Complication: bỏ technical SEO, giữ user experience framing; (3) Fix Resolution: product job first, không liệt kê features trước; (4) Fix North Star: W2A → Transactions; (5) Fix 6 Social JTBD: bữa tối test; (6) Remove Section 5.5 Technical Foundation (→ PRD); (7) Remove Quarterly Ramp + Pilot Gate (→ Action Plan); (8) Remove Backlink Budget + SEM Support khỏi Dependencies (→ Action Plan) (Hiến).
