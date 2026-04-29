# BRD - Web Growth: eSIM Du Lịch
**MoMo (MService) · Out-App Traffic Team**
**Phiên bản:** 1.0 · **Ngày:** Tháng 4/2026 · **Author:** Hiến (SEO & GEO Lead)
**Status:** Draft - chờ review PO + Dev

---

## Mục lục

1. [Executive Summary](#1-executive-summary)
2. [Bối cảnh & Cơ hội](#2-bối-cảnh--cơ-hội)
3. [Mục tiêu dự án (OKR)](#3-mục-tiêu-dự-án-okr)
4. [Stakeholders & RACI](#4-stakeholders--raci)
5. [Phạm vi dự án (Scope)](#5-phạm-vi-dự-án-scope)
6. [Yêu cầu chức năng](#6-yêu-cầu-chức-năng)
7. [Yêu cầu phi chức năng](#7-yêu-cầu-phi-chức-năng)
8. [Information Architecture & URL Structure](#8-information-architecture--url-structure)
9. [Page Specs](#9-page-specs)
10. [Content Requirements](#10-content-requirements)
11. [Tracking & Analytics](#11-tracking--analytics)
12. [Phụ thuộc & Rủi ro](#12-phụ-thuộc--rủi-ro)
13. [Sprint Plan & Timeline](#13-sprint-plan--timeline)
14. [Definition of Done](#14-definition-of-done)

---

## 1. Executive Summary

Dự án xây dựng cluster web **eSIM Du Lịch** trên `momo.vn` gồm 1 Hub page, 10 Destination pages, và ~10 bài blog. Mục tiêu là capture organic traffic từ keyword pool ~38,000 SV/tháng và convert sang lượt mua eSIM trong MoMo App thông qua deep link.

MoMo phân phối eSIM của đối tác **Gohub** (raise $500K Iterative, 6/2024), hỗ trợ 150+ quốc gia. Lợi thế cạnh tranh của MoMo không nằm ở sản phẩm (Gohub cũng bán trực tiếp) mà ở **distribution + payment seamless + trust** từ hệ sinh thái ví điện tử. Chiến lược web khai thác lợi thế này bằng cách giữ user trên web dài hơn qua content, sau đó chuyển sang app để hoàn thành giao dịch.

**Business case tóm gọn:**
- Tổng addressable SV: ~38,050/tháng (380 keywords)
- Cluster lớn nhất chưa có trang tối ưu: eSIM Trung Quốc (7,850 SV)
- Conversion path: Web → Deep link → App → Mua gói → Thanh toán ví MoMo
- Revenue driver: GMV từ bán eSIM + NPS từ trải nghiệm du lịch liền mạch

---

## 2. Bối cảnh & Cơ hội

### 2.1 Thị trường

- eSIM global đạt $2.45B (2024), CAGR 14% đến 2032
- Du lịch quốc tế của người Việt phục hồi mạnh sau COVID - H1/2025 VN đón 10.7M lượt khách quốc tế, người Việt xuất cảnh tăng tương ứng
- Nhu cầu kết nối khi đi du lịch nước ngoài là pain point phổ biến: SIM vật lý tại sân bay bất tiện, chuyển vùng quốc tế đắt (đắt hơn eSIM 60-80%)

### 2.2 Competitive Landscape

| Player | Điểm mạnh | Điểm yếu vs MoMo |
|---|---|---|
| **Gohub** *(đối tác)* | Dẫn đầu thị trường, 195+ quốc gia | Brand awareness thấp với user phổ thông |
| **Gloka** | B2C mạnh, SEO tốt | Không có siêu app distribution |
| **Airalo** | Global #1, brand quốc tế | Không bản địa hóa cho người Việt |
| **Klook** | OTA distribution, SV đáng kể | Không phải core product |
| **InfiGate/VNA** | Tích hợp VNA Lotusmiles (10/2025) | Mới gia nhập, chưa có traction |

**Strategic position:** MoMo không cạnh tranh trên sản phẩm eSIM - cạnh tranh trên **distribution, UX, và trust**. Người dùng MoMo sẵn có ví, thẻ liên kết - friction mua hàng thấp hơn bất kỳ competitor nào.

### 2.3 Keyword Opportunity

Tổng keyword pool 380 từ khóa, 38,050 SV/tháng. Top clusters theo SV:

| Cluster | SV/tháng | Priority |
|---|---|---|
| eSIM Chung | 8,510 | P0 |
| eSIM + Sim Trung Quốc | 7,850 | P0 |
| Sim Ngoại Quốc Chung | 4,100 | P0 |
| Thái Lan | 3,930 | P0 |
| Nhật Bản | 1,950 | P1 |
| Singapore | 1,530 | P1 |
| Cẩm nang / How-to | 1,430 | P0 (Blog) |
| Hàn Quốc | 1,160 | P1 |
| Châu Âu | 1,090 | P2 |
| Mỹ | 900 | P2 |

**4 Strategic Observations cần action ngay:**

1. **OB1 - Intercept competitor intent:** `cách chuyển vùng quốc tế viettel` (1,000 SV) + `mobi` (260 SV) = 1,260 SV user đang tìm giải pháp thay thế - đây là moment dễ convert nhất. Cần 1 bài blog comparison capture query này.
2. **OB2 - Bilingual queries đáng kể:** `esim thailand` (480), `china esim` (170), `korea esim` (110) - người Việt search bằng tiếng Anh khi biết rõ điểm đến. Không cần trang riêng, xử lý bằng bilingual title tag + H2 trong body.
3. **OB3 - Loại keyword sai intent:** `mua sim trung quốc vĩnh viễn` (390 SV) - nhu cầu SIM vật lý dài hạn, không match với eSIM du lịch. Target sẽ tăng bounce rate. Loại khỏi danh sách.
4. **OB4 - Branded competitor keywords:** `sim klook` (50), `esim gigago` (70), `sim gloka` (20) - chỉ intercept qua blog comparison, không target trên landing page. Cần approval stakeholder trước khi viết.

---

## 3. Mục tiêu dự án (OKR)

### Objective
Xây dựng cluster web eSIM Du Lịch thành kênh organic acquisition hiệu quả, convert được traffic thành lượt mở app và mua hàng.

### Key Results - 6 tháng sau full launch Sprint 1

| KR | Metric | Target | Tool đo |
|---|---|---|---|
| KR1 | Organic Clicks - `/esim-du-lich/*` | +40% vs baseline | GSC |
| KR2 | Average Position - 5 keywords P0 | Top 10 | GSC |
| KR3 | AI Overview Appearances | ≥3 FAQ queries cited | GSC / Manual check |
| KR4 | Click-to-App Rate (web → app, mobile) | >3% | GA4 + Appsflyer |
| KR5 | New Users từ eSIM Funnel | Grow MoM | Appsflyer |
| KR6 | FAQ Schema Eligibility | 0 error, ≥5 FAQ indexed/trang | GSC Enhancements |

> **Baseline measurement:** Đo toàn bộ metrics ngay sau khi publish Sprint 1 (Hub + 2 destination P0). Không so sánh với trước khi có trang vì không có baseline hữu ý.

---

## 4. Stakeholders & RACI

| Role | Người phụ trách | R | A | C | I |
|---|---|---|---|---|---|
| SEO & GEO Lead | Hiến | ✓ | | | |
| Product Owner (Web) | TBD | | ✓ | | |
| Frontend Dev | TBD | ✓ | | | |
| Backend / API Dev | TBD | ✓ | | | |
| Content Writer | TBD (hiring) | ✓ | | | |
| Design | TBD | ✓ | | | |
| Partnership (Gohub) | TBD | | | ✓ | |
| Legal (comparison content) | TBD | | | ✓ | |
| Data / Analytics | TBD | | | | ✓ |
| Growth Cell Lead | TBD | | | | ✓ |

**R** = Responsible · **A** = Accountable · **C** = Consulted · **I** = Informed

---

## 5. Phạm vi dự án (Scope)

### 5.1 Trong scope

- **Hub Page:** `/esim-du-lich` - 1 trang, full component build
- **Destination Pages:** 10 trang theo URL pattern `/esim-du-lich/{country-slug}`
- **Blog Cluster:** ~10 bài theo 3 tiers (xem mục 10)
- **Deep Link Integration:** Web → MoMo App (iOS + Android), fallback App Store / CH Play nếu chưa cài
- **Smart Banner / App Clip:** Hiển thị trên mobile browser
- **Schema Markup:** FAQPage, HowTo, Product, AggregateOffer, BreadcrumbList trên tất cả trang
- **UTM Framework:** Chuẩn hóa UTM params cho toàn bộ CTA trong cluster
- **GA4 Event Tracking:** Click CTA, scroll depth, deep link click
- **Gohub API Integration:** Fetch giá và danh sách gói cước theo real-time (không hardcode)

### 5.2 Ngoài scope (BRD này)

- App-side UI/UX cho màn hình eSIM trong MoMo App (đã tồn tại)
- Hệ thống inventory / fulfillment phía Gohub
- Social media / paid campaign cho eSIM cluster
- Đa ngôn ngữ (EN, TH, ZH) - chỉ tiếng Việt + bilingual title/H2 theo nhu cầu
- Trang so sánh competitor trực tiếp (cần approval riêng, nằm ngoài scope Sprint 1-2)

### 5.3 Out-of-scope explicit

- Không build trang landing page dạng SPA riêng cho eSIM - tất cả nằm trong cấu trúc `momo.vn` hiện có
- Không tạo subdomain `esim.momo.vn` - dùng subdirectory `/esim-du-lich/` để giữ domain authority

---

## 6. Yêu cầu chức năng

### 6.1 Hub Page - `/esim-du-lich`

**FR-HUB-01 - Hero Section**
- H1: "Mua eSIM Du Lịch Quốc Tế - Kết Nối Ngay Khi Hạ Cánh"
- Sub-headline: 3 trust signals dạng inline (QR code · 150+ quốc gia · Hoàn tiền nếu lỗi)
- CTA Primary: Deep link → màn hình eSIM trong app. Copy: "Mua eSIM Ngay"
- CTA Secondary: Anchor scroll xuống Destination Grid. Copy: "Xem Gói Theo Điểm Đến ↓"
- Breadcrumb: Trang chủ > eSIM Du Lịch

**FR-HUB-02 - Answer Block (AEO Gate)**
- H2: "eSIM Du Lịch Là Gì?"
- Đoạn text 60-80 từ, câu đầu = definition trực tiếp, không marketing fluff
- Comparison table 3 cột: eSIM vs SIM vật lý vs Chuyển vùng - tối thiểu 5 tiêu chí (giá, setup time, coverage, giữ số VN, phù hợp cho)
- Schema FAQPage markup cho block này

**FR-HUB-03 - Destination Grid**
- H2: "Chọn eSIM Theo Điểm Đến"
- Grid 10 card, mỗi card: Flag emoji + Tên quốc gia + Giá từ [X]đ + Số ngày phổ biến + Button → `/esim-du-lich/{country}`
- Giá fetch từ Gohub API (không hardcode)
- Responsive: 2 cột mobile → 4-5 cột desktop

**FR-HUB-04 - How-to Section**
- H2: "Cách Mua Và Kích Hoạt eSIM Trên MoMo"
- 4 bước dạng numbered list: Mở app → Chọn gói → Thanh toán → Nhận QR/kích hoạt
- Mỗi bước có icon, tiêu đề ngắn, mô tả 1-2 câu
- Schema HowTo markup

**FR-HUB-05 - FAQ Block**
- 8 câu hỏi AEO priority (xem Appendix A)
- Accordion collapse/expand, default closed
- Schema FAQPage markup - validate 0 error trên Google Rich Results Test

**FR-HUB-06 - Cross-sell Block**
- "Chuẩn bị thêm cho chuyến đi": Link đến Bảo hiểm du lịch, Đổi ngoại tệ (nếu có trên MoMo)
- "Cẩm nang eSIM": 4-6 card blog dạng thumbnail + title + category tag

### 6.2 Destination Pages - `/esim-du-lich/{country}`

*Áp dụng cho tất cả 10 trang - 1 template chung, data thay đổi theo country.*

**FR-DEST-01 - Hero**
- H1 pattern: "eSIM Du Lịch [Quốc Gia] ([EN Name] eSIM) - [Ngày phổ biến] / [Dung lượng] / Từ [Giá]đ"
- Breadcrumb: Trang chủ > eSIM Du Lịch > [Quốc Gia]
- Schema BreadcrumbList

**FR-DEST-02 - Product Table**
- Cột: Thời hạn (3/5/7/15/30 ngày) · Dung lượng · Tốc độ (4G/5G) · Giá · [Mua Ngay]
- Giá: fetch real-time từ Gohub API - nếu API lỗi, hiển thị "Xem giá trong app"
- Highlight row "Bán chạy nhất" cho gói phổ biến nhất
- Button "Mua Ngay" trong mỗi row → deep link vào app với pre-selected gói tương ứng
- Schema Product + AggregateOffer + PriceSpecification

**FR-DEST-03 - Country Context + FAQ**
- Đoạn context 100-150 từ về đặc thù kết nối tại quốc gia đó
- 5-7 FAQ riêng theo country (xem content spec tại mục 10)
- Schema FAQPage

**FR-DEST-04 - Related Destinations**
- 3-4 trang destination liên quan về địa lý / use case (ví dụ: Nhật → Singapore, Hàn Quốc, Đài Loan)
- Không cross-link random - phải có logic địa lý hoặc trip pattern

**FR-DEST-05 - Sticky CTA**
- Floating button visible toàn bộ scroll
- Copy: "[Flag emoji] Mua eSIM [Quốc Gia]"
- Deep link + UTM: `utm_source=web&utm_medium=esim-dest&utm_campaign={country}&utm_content=sticky`

**FR-DEST-06 - Critical Flag: Trang Trung Quốc**
- Bắt buộc có disclaimer rõ về Great Firewall: eSIM thông thường KHÔNG bypass GFW
- Xác nhận với Gohub gói nào có VPN support trước khi publish - ghi rõ trong trang
- Không publish trang `/esim-du-lich/trung-quoc` trước khi có thông tin này từ Gohub

### 6.3 Smart Banner / Deep Link

**FR-DL-01 - Smart Banner**
- Hiển thị trên tất cả trang eSIM khi user truy cập từ mobile browser
- Copy: "Mở trong MoMo để mua eSIM nhanh hơn"
- Tap → deep link vào app; nếu chưa cài → fallback App Store (iOS) / CH Play (Android)

**FR-DL-02 - Deep Link Spec**
- Mỗi destination page có deep link riêng dẫn thẳng vào màn hình eSIM của quốc gia tương ứng trong app, không phải homepage
- Test required: iOS + Android, cả trường hợp đã cài và chưa cài app
- Fallback URL nếu deep link fail: `momo.vn/esim-du-lich/{country}`

### 6.4 Gohub API Integration

**FR-API-01 - Giá và gói cước**
- Fetch danh sách gói cước (tên, thời hạn, dung lượng, tốc độ, giá) từ Gohub API
- Cache: 15 phút (giá không thay đổi real-time từng giây nhưng cần tương đối fresh)
- Fallback nếu API timeout (>3s): hiển thị "Xem giá trong app" thay vì error state

**FR-API-02 - Availability**
- Nếu Gohub API báo sold out hoặc unavailable cho quốc gia cụ thể → ẩn product table, hiển thị "Tạm thời không có gói cho điểm đến này"
- Không để trang hiển thị giá nhưng CTA không hoạt động

---

## 7. Yêu cầu phi chức năng

### 7.1 Performance

| Metric | Target | Điều kiện |
|---|---|---|
| LCP (Largest Contentful Paint) | < 2.5s | Mobile 4G, Lighthouse |
| CLS (Cumulative Layout Shift) | < 0.1 | Cần check khi Gohub API load async |
| FID / INP | < 200ms | |
| TTI (Time to Interactive) | < 3.5s | Mobile |

> **Lưu ý API:** Gohub API response phải không block render. Load giá async sau khi trang render xong - tránh CLS khi giá load vào bảng.

### 7.2 SEO Technical

- Canonical tag: self-referencing trên tất cả trang, tránh duplicate từ filter/sort params nếu có
- Hreflang: không áp dụng (chỉ tiếng Việt)
- Robots: allow tất cả trang trong cluster (không noindex)
- Sitemap: tất cả URL phải có trong XML sitemap, submit GSC sau khi publish
- Pagination: nếu có phân trang trong bảng gói - dùng `rel="next/prev"` hoặc AJAX không thay đổi URL

### 7.3 Schema Validation

- Tất cả schema markup phải pass Google Rich Results Test với 0 error trước khi publish
- Schema types required theo page:

| Page type | Schema required |
|---|---|
| Hub | WebPage + FAQPage + BreadcrumbList + HowTo |
| Destination | Product + AggregateOffer + PriceSpecification + FAQPage + BreadcrumbList |
| Blog | Article + FAQPage (+ HowTo nếu có step-by-step) |

### 7.4 Mobile-first

- Layout: mobile-first responsive. Tất cả component phải usable trên màn 375px
- CTA sticky: visible và không bị overlap bởi browser chrome (trên iOS Safari đặc biệt)
- Bảng gói cước: scroll ngang trên mobile - không collapse column, không ẩn thông tin quan trọng

### 7.5 Bảo mật & Compliance

- Giá và dữ liệu gói fetch từ API không cache ở phía client (không localStorage giá)
- Deep link không expose Gohub API key ở phía client
- Không hiển thị giá đối thủ nếu không có quy trình verify - tuân thủ nguyên tắc commercial content của MoMo

---

## 8. Information Architecture & URL Structure

```
momo.vn/
└── esim-du-lich/                          [Hub Pillar - SV: 8,510+]
    ├── trung-quoc/                         [P0 - SV: 7,850] ⚠️ GFW
    ├── thai-lan/                           [P0 - SV: 3,930]
    ├── nhat-ban/                           [P1 - SV: 1,950]
    ├── singapore/                          [P1 - SV: 1,530]
    ├── han-quoc/                           [P1 - SV: 1,160]
    ├── chau-au/                            [P2 - SV: 1,090]
    ├── my/                                 [P2 - SV: 900]
    ├── uc/                                 [P2 - SV: 790]
    ├── dai-loan/                           [P3 - SV: 700]
    └── malaysia/                           [P3 - SV: 610]

momo.vn/tin-tuc/
    ├── esim-la-gi/                         [Blog Tier 1 - P0]
    ├── esim-vs-chuyen-vung-quoc-te/        [Blog Tier 1 - P0, intercept 1,260 SV]
    ├── cach-mua-esim-tren-momo/            [Blog Tier 1 - P0]
    ├── dien-thoai-ho-tro-esim-2026/        [Blog Tier 1 - P1]
    ├── esim-trung-quoc-co-vao-google-khong/ [Blog Tier 2 - P0]
    ├── esim-thai-lan-ais-vs-true-move/     [Blog Tier 2 - P1]
    ├── kinh-nghiem-esim-nhat-ban/          [Blog Tier 2 - P1]
    ├── esim-chau-au-1-goi-bao-nhieu-nuoc/  [Blog Tier 2 - P2]
    ├── klook-esim-vs-momo-esim/            [Blog Tier 3 - Cần approval]
    └── airalo-vs-gohub-vs-momo-esim/       [Blog Tier 3 - Cần approval]
```

**URL Rules:**
- Lowercase, hyphenated, không dấu tiếng Việt
- Không trailing slash không nhất quán - chọn 1 convention, redirect cái kia
- Không dùng query params trong URL cấu trúc (filter, sort dùng AJAX nếu cần)
- Độ dài URL: tối đa 75 ký tự (không tính domain)

---

## 9. Page Specs

### 9.1 Hub Page - `/esim-du-lich`

**JTBD:** "Tôi sắp đi du lịch nước ngoài, muốn có internet ngay khi xuống máy bay, không muốn xếp hàng mua SIM ở sân bay và không muốn trả phí roaming đắt đỏ."

**Target keywords chính:** `esim du lịch` (1,600) · `esim quốc tế` (210) · `sim du lịch quốc tế` (1,000) · `mua esim du lịch` (70)

**Component sequence:**

| # | Component | Mục tiêu | Schema |
|---|---|---|---|
| C1 | Hero + CTA | Convert immediate intent | WebPage, BreadcrumbList |
| C2 | Answer Block "eSIM là gì?" | AEO citation gate | FAQPage |
| C3 | Destination Grid | Hub → Spoke navigation | - |
| C4 | How-to 4 bước | GEO How-to citation | HowTo |
| C5 | FAQ Block (8 câu) | AEO long-tail coverage | FAQPage |
| C6 | Cross-sell + Blog links | Ecosystem / retention | - |

**Title tag:** `Mua eSIM Du Lịch Quốc Tế - Kết Nối Ngay Khi Hạ Cánh | MoMo` (≤60 ký tự)
**Meta description:** `Mua eSIM du lịch 150+ quốc gia trên MoMo - kích hoạt bằng QR code, có mạng ngay khi hạ cánh. Tiết kiệm đến 80% so với chuyển vùng quốc tế.` (120-155 ký tự)

### 9.2 Destination Pages - `/esim-du-lich/{country}`

**Component sequence:**

| # | Component | Mục tiêu | Schema |
|---|---|---|---|
| C1 | Hero + Breadcrumb | Keyword relevance signal | Product, BreadcrumbList |
| C2 | Product Table + CTA | Direct conversion | AggregateOffer, PriceSpecification |
| C3 | Country Context (100-150 từ) + FAQ | AEO country-specific | FAQPage |
| C4 | Related Destinations | Internal link equity | - |
| [Sticky] | Floating CTA button | Capture intent bất kỳ lúc nào | - |

**Title tag pattern:** `eSIM Du Lịch [Quốc Gia] ([EN Name] eSIM) - Gói Cước & Mua Ngay | MoMo`

**Bilingual title spec:**

| Destination | Title tag | H2 bilingual trong body |
|---|---|---|
| Thái Lan | "eSIM Thái Lan (Thailand eSIM) - Gói Cước & Mua Ngay" | "Thailand eSIM Plans for Vietnamese Travelers" |
| Trung Quốc | "eSIM Trung Quốc (China eSIM) - Kết Nối Không Giới Hạn" | "China eSIM - What You Need to Know" |
| Hàn Quốc | "eSIM Hàn Quốc (Korea eSIM) - Mua Nhanh Kích Hoạt Ngay" | "Korea eSIM - Compare Plans" |
| Singapore | "eSIM Singapore - Gói Data & Giá Tốt Nhất 2026" | "Singapore eSIM Options Compared" |
| Châu Âu | "eSIM Châu Âu (Europe eSIM) - 1 Gói Cho Cả Schengen" | "Europe eSIM - Cover Multiple Countries" |

---

## 10. Content Requirements

### 10.1 Tone & Voice

MoMo được định vị là **người bạn hiểu công nghệ đang giúp bạn chuẩn bị chuyến đi** - không phải travel blogger, không phải sales rep. Tone: thân thiện + có chuyên môn. Ngắn gọn nhưng đủ để quyết định.

**Rules bắt buộc:**
- Câu đầu mỗi đoạn = point chính (không warm-up)
- Claim phải có evidence (số liệu, so sánh giá cụ thể)
- Mỗi comparison section kết thúc bằng verdict 1 câu kiểu "Chọn X nếu... Chọn Y nếu..."
- Giá không hardcode nếu có thể thay đổi
- Tiếng Việt phổ thông + giữ nguyên: eSIM, QR code, 4G/5G, SIM, data

**Tuyệt đối tránh:**
- Marketing superlative không có data: "tốt nhất", "rẻ nhất", "nhanh nhất"
- Opener rỗng: "Bạn có biết...", "Trong thế giới ngày nay..."
- Passive voice lòng vòng: "được xem là" → viết trực tiếp
- Không address Great Firewall trong trang Trung Quốc

### 10.2 Content Types & Word Count

| Type | Áp dụng | Word count | Schema |
|---|---|---|---|
| Transaction Content | Hub + Destination pages | <800 từ body (không tính FAQ) | Product, FAQPage, HowTo |
| Informational Blog | Blog Tier 1 | 1,000-2,000 từ | Article, FAQPage |
| Experience Blog | Blog Tier 2 | 800-1,500 từ | Article, FAQPage |
| Comparison Blog | Blog Tier 3 | 1,200-2,000 từ, bắt buộc có bảng | Article, FAQPage |

### 10.3 Blog Roadmap

**Tier 1 - Must-have (P0, Sprint 1-2):**

| Bài | Target keyword | Est. SV | Ghi chú |
|---|---|---|---|
| eSIM Là Gì? Hướng Dẫn Từ A Đến Z | `esim du lịch là gì`, `cách kích hoạt esim` | ~200 | AEO priority, HowTo schema |
| Chuyển Vùng vs eSIM: Cái Nào Rẻ Hơn? | `cách chuyển vùng quốc tế viettel/mobi` | 1,260 | Intercept competitor query - P0 |
| Cách Mua eSIM Trên MoMo - Bước Bước | `mua esim du lịch`, `cách dùng esim du lịch` | ~200 | How-to focus |
| Điện Thoại Nào Hỗ Trợ eSIM? 2026 | `điện thoại hỗ trợ esim`, `1 esim dùng mấy máy` | ~50 | Update 6 tháng/lần |

**Tier 2 - Destination-specific (P0-P1, Sprint 2-3):**

| Bài | Target keyword | Est. SV |
|---|---|---|
| eSIM Trung Quốc: Có Vào Google Không? | `esim trung quốc`, `sim vpn china` | ~790 |
| eSIM Thái Lan: AIS vs DTAC vs Gói MoMo | `esim thailand`, `sim dtac thái lan` | ~530 |
| Kinh Nghiệm Dùng eSIM Nhật Bản | `esim nhật bản`, `kinh nghiệm mua sim nhật` | ~340 |
| eSIM Châu Âu: 1 Gói Hay Mua Từng Nước? | `esim du lịch châu âu`, `sim châu âu` | ~220 |

**Tier 3 - Competitor comparison (cần approval, Sprint 3+):**

| Bài | Target keyword | Yêu cầu trước khi viết |
|---|---|---|
| Klook eSIM vs MoMo eSIM | `klook esim`, `mua sim klook` | Approval pháp lý + commercial |
| Airalo vs Gohub vs MoMo eSIM | `esim airalo` | Verify giá đối thủ ngày publish + approval |

### 10.4 AEO Priority Questions (8 câu - bắt buộc có trong Hub FAQ)

1. eSIM du lịch là gì? Khác SIM vật lý thế nào?
2. Nên mua eSIM hay chuyển vùng quốc tế?
3. Điện thoại nào hỗ trợ eSIM?
4. Mua eSIM bao lâu trước chuyến đi?
5. eSIM Trung Quốc có dùng được Google, Facebook không?
6. 1 eSIM dùng được mấy máy?
7. Mua eSIM du lịch ở đâu uy tín?
8. Cách kích hoạt eSIM như thế nào?

*Format mỗi câu: 40-60 từ, câu đầu = answer trực tiếp, không marketing jargon.*

### 10.5 CTA Copy Framework

| Vị trí | Copy chuẩn | Tránh |
|---|---|---|
| Hero Primary | "Mua eSIM [Quốc Gia] Ngay" | "Tìm hiểu thêm", "Click here" |
| Hero Secondary | "Xem Gói Theo Điểm Đến ↓" | "Khám phá thêm" |
| Product Table row | "Mua Gói Này", "Chọn 7 Ngày" | "Buy", "Order" |
| Sticky Floating | "[Flag] Mua eSIM [Country]" | "MoMo eSIM", "Mua eSIM" (thiếu quốc gia) |
| Blog Inline | Anchor text = destination page title | Banner ngắt flow đọc |
| Blog End | "[Context 1 câu] → [Link destination]" | "Cảm ơn đã đọc!" |

---

## 11. Tracking & Analytics

### 11.1 GA4 Events - Required

| Event name | Trigger | Parameters |
|---|---|---|
| `esim_cta_click` | Click bất kỳ CTA trong cluster | `page_type` (hub/dest/blog), `country`, `cta_position` (hero/sticky/inline/end), `destination_url` |
| `esim_deeplink_click` | Click deep link → app | `country`, `package_id` (nếu có), `source_page` |
| `esim_faq_expand` | Expand FAQ accordion item | `question_id`, `page_type` |
| `esim_product_view` | User scroll đến product table | `country`, `packages_loaded` (true/false - kiểm tra API load) |
| `esim_blog_cta_click` | Click CTA trong bài blog | `blog_slug`, `cta_position` |

### 11.2 UTM Naming Convention

```
utm_source=web
utm_medium=esim-[hub|dest|blog]
utm_campaign=[country-slug | blog-slug]
utm_content=[hero-cta | sticky | inline | end-cta | table-row]
```

**Ví dụ:**
- Hub Hero CTA: `utm_source=web&utm_medium=esim-hub&utm_campaign=esim-du-lich&utm_content=hero-cta`
- Destination Sticky: `utm_source=web&utm_medium=esim-dest&utm_campaign=thai-lan&utm_content=sticky`
- Blog End CTA: `utm_source=web&utm_medium=esim-blog&utm_campaign=esim-vs-chuyen-vung&utm_content=end-cta`

> Mỗi CTA vị trí phải có `utm_content` riêng để distinguish performance theo position trong GA4.

### 11.3 Looker Studio / Reporting

- Dashboard: Organic clicks + impressions + avg position theo page (GSC data)
- Dashboard: Click-to-App Rate = `esim_deeplink_click` / `session` (GA4)
- Segment: Mobile vs Desktop riêng - conversion pattern khác nhau đáng kể
- Review cadence: Weekly trong 30 ngày đầu sau mỗi sprint publish → Monthly sau đó

---

## 12. Phụ thuộc & Rủi ro

### 12.1 Phụ thuộc

| Phụ thuộc | Owner | Deadline cần confirm | Impact nếu trễ |
|---|---|---|---|
| Gohub API spec (endpoint, auth, response format) | Partnership team | Trước khi Dev bắt đầu Sprint 1 | Không build product table, không có giá real-time |
| Gohub xác nhận gói nào support VPN (cho trang TQ) | Partnership team | Trước khi publish `/esim-du-lich/trung-quoc` | Không publish được trang P0 lớn nhất (7,850 SV) |
| Deep link scheme từ App team | App team | Trước khi Dev bắt đầu Sprint 1 | CTA trên web không hoạt động |
| CMS support cho schema injection (FAQPage, Product) | Dev/CMS | Confirm trước khi build | Schema phải inject qua code thay vì CMS → tăng effort |
| Legal approval cho Blog Tier 3 (comparison) | Legal | Sprint 3 | Blog comparison bị delay |

### 12.2 Rủi ro

| Rủi ro | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Gohub API không stable, timeout thường xuyên | Medium | High | Implement fallback "Xem giá trong app" + cache 15 phút |
| Gói Gohub không bypass GFW - user TQ bị disappointed | High | High | Disclaimer rõ ràng trong trang TQ trước khi publish. Confirm với Gohub trước. |
| CMS không support schema injection | Medium | Medium | Dev inject qua code, không dùng CMS plugin |
| Deep link fail trên thiết bị cụ thể (iOS/Android version cũ) | Low | Medium | Test matrix đủ device trước launch, có fallback URL |
| Competitor publish trang tốt hơn trong thời gian build | Medium | Medium | Ưu tiên P0 trước - Hub + TQ + Thái Lan phải live trước đối thủ |
| Giá eSIM thay đổi → hardcode bị stale | High (nếu hardcode) | Medium | Bắt buộc dùng API, không hardcode giá bất kỳ đâu |

---

## 13. Sprint Plan & Timeline

> **Giả định:** 1 Frontend Dev + 1 Content Writer + SEO Lead review. Không bao gồm thời gian legal review (Tier 3 blogs) và Gohub API integration time.

### Sprint 1 - P0 Core (Tuần 1-3)

| Deliverable | Owner | Ghi chú |
|---|---|---|
| Hub page `/esim-du-lich` | Dev + Content | Cần Gohub API + deep link scheme trước khi start |
| Destination `/esim-du-lich/thai-lan` | Dev + Content | Template base cho các trang sau |
| Blog: "Chuyển vùng vs eSIM" | Content | Intercept 1,260 SV - priority cao nhất về organic value |
| GA4 event tracking setup | Dev + Data | Phải có trước khi publish để có baseline |
| UTM implementation | Dev | Tất cả CTA |
| Schema validation | SEO | 0 error trước publish |
| Submit GSC | SEO | Trong 48h sau publish |

**Blocker Sprint 1:** Gohub API spec + Deep link scheme phải ready trước ngày Dev bắt đầu.

### Sprint 2 - P0 Remaining + P1 (Tuần 4-6)

| Deliverable | Owner | Ghi chú |
|---|---|---|
| Destination `/esim-du-lich/trung-quoc` | Dev + Content | **Không publish trước khi có xác nhận GFW từ Gohub** |
| Destination `/esim-du-lich/nhat-ban` | Dev + Content | Reuse template từ Sprint 1 |
| Destination `/esim-du-lich/singapore` | Dev + Content | |
| Destination `/esim-du-lich/han-quoc` | Dev + Content | |
| Blog: "eSIM là gì A-Z" | Content | AEO priority |
| Blog: "Điện thoại hỗ trợ eSIM 2026" | Content | |
| Blog: "eSIM Trung Quốc: Có vào Google không?" | Content | Publish đồng thời với trang /trung-quoc |

### Sprint 3 - P2/P3 + Blog Tier 2 (Tuần 7-10)

| Deliverable | Owner | Ghi chú |
|---|---|---|
| Destination `/esim-du-lich/chau-au`, `/my`, `/uc` | Dev + Content | |
| Destination `/esim-du-lich/dai-loan`, `/malaysia` | Dev + Content | |
| Blog Tier 2: Thái Lan, Nhật Bản, Châu Âu | Content | |
| Blog Tier 3 | Content + Legal | Chỉ bắt đầu sau khi có legal approval |
| Performance audit: CWV check toàn cluster | Dev | |
| Reporting dashboard setup Looker Studio | Data | |

---

## 14. Definition of Done

Một page/blog được coi là **Done** khi đáp ứng toàn bộ các tiêu chí sau:

### Technical DoD

- [ ] H1 chứa keyword chính, unique trong toàn site
- [ ] Title tag: 50-60 ký tự, có keyword + "MoMo"
- [ ] Meta description: 120-155 ký tự, có CTA ngầm
- [ ] URL: lowercase, hyphenated, không dấu, ≤75 ký tự
- [ ] Schema markup pass Google Rich Results Test - 0 error
- [ ] Canonical tag: self-referencing
- [ ] Deep link: test pass trên iOS + Android (cả installed và not installed)
- [ ] LCP < 2.5s, CLS < 0.1 trên mobile Lighthouse
- [ ] Trang trong XML sitemap
- [ ] Alt text đầy đủ trên tất cả hình ảnh

### Content DoD

- [ ] Answer Block AEO: 40-60 từ, câu đầu = answer trực tiếp (trang sản phẩm + blog)
- [ ] FAQ: ≥5 câu cho trang hub/dest, ≥3 câu cho blog
- [ ] Giá: dynamic từ API (trang sản phẩm) hoặc không có giá cụ thể (blog)
- [ ] Internal links: ≥2 link đến trang liên quan trong cluster
- [ ] CTA: đúng copy theo framework, đúng UTM params
- [ ] Trang TQ: có disclaimer GFW, đã confirm với Gohub
- [ ] Blog comparison Tier 3: có legal approval trước khi publish

### Tracking DoD

- [ ] GA4 events: `esim_cta_click`, `esim_deeplink_click` fire đúng
- [ ] UTM params đúng format trên tất cả CTA
- [ ] GSC: Request Indexing trong 48h sau publish

---

## Appendix A - 8 AEO Priority Questions (Full Answer Text)

*Dùng làm nội dung FAQ block trên Hub page. Format chuẩn: 40-60 từ per answer, câu đầu = answer chính.*

**Q1. eSIM du lịch là gì? Khác SIM vật lý thế nào?**
eSIM (embedded SIM) là SIM điện tử tích hợp sẵn trong điện thoại, kích hoạt qua QR code mà không cần cắm SIM vật lý. Khi đi du lịch, bạn mua eSIM online, nhận QR code, quét là có mạng ngay khi xuống máy bay - không cần xếp hàng mua SIM tại sân bay.

**Q2. Nên mua eSIM hay chuyển vùng quốc tế?**
eSIM du lịch rẻ hơn chuyển vùng từ 60-80% và không cần đăng ký hay hủy gói sau chuyến đi. Chuyển vùng quốc tế phù hợp nếu bạn chỉ đi 1-2 ngày và cần giữ số điện thoại Việt Nam để nhận OTP liên tục.

**Q3. Điện thoại nào hỗ trợ eSIM?**
iPhone XS (2018) trở lên, Samsung Galaxy S21 trở lên, Google Pixel 3 trở lên đều hỗ trợ eSIM. Đến 2025-2026, hầu hết flagship đều tương thích. Kiểm tra nhanh: vào Cài đặt → Thông tin điện thoại → xem có mục "eSIM" hay không.

**Q4. Mua eSIM bao lâu trước chuyến đi?**
Nên mua eSIM trước 1-3 ngày để có thời gian cài đặt và test kết nối. eSIM MoMo giao trong vài phút qua QR code, có thể cài ngay - nhưng không nên để sát giờ bay vì cần kiểm tra thiết bị tương thích.

**Q5. eSIM Trung Quốc có dùng được Google, Facebook không?**
Trung Quốc chặn Google, Facebook, Instagram (Great Firewall). eSIM thông thường không bypass được trừ khi gói eSIM đó có tích hợp VPN hoặc dùng mạng quốc tế riêng. Trước khi mua, xác nhận với nhà cung cấp gói có support VPN hay không.

**Q6. 1 eSIM dùng được mấy máy?**
Mỗi eSIM du lịch chỉ dùng được cho 1 thiết bị. Sau khi quét QR code và cài vào máy, mã QR đó không thể dùng lại trên máy khác. Nếu đi cùng nhiều người, mỗi người cần mua 1 gói riêng.

**Q7. Mua eSIM du lịch ở đâu uy tín?**
Có thể mua qua các nền tảng uy tín như MoMo, Airalo, Gohub, Klook. MoMo cung cấp eSIM qua đối tác Gohub, hỗ trợ 150+ quốc gia, thanh toán bằng ví MoMo, hoàn tiền nếu không kết nối được.

**Q8. Cách kích hoạt eSIM như thế nào?**
Sau khi mua: (1) Vào Cài đặt → Điện thoại → Thêm eSIM; (2) Chọn "Quét QR code"; (3) Quét mã nhận được sau khi mua; (4) Xác nhận cài đặt. Toàn bộ quá trình mất khoảng 2-3 phút. Nên kích hoạt khi còn ở Việt Nam để test trước.

---

## Appendix B - Destination-specific FAQ Samples

### `/esim-du-lich/trung-quoc`
- eSIM Trung Quốc có bypass được Great Firewall (Google, Facebook) không?
- Gói nào trên MoMo có hỗ trợ VPN tại Trung Quốc?
- eSIM Trung Quốc của MoMo dùng mạng nhà mạng nào?
- Tôi có thể dùng Google Maps ở TQ với eSIM này không?
- Nên tải VPN trước khi đi hay sau khi đến TQ?

### `/esim-du-lich/thai-lan`
- eSIM Thái Lan gói Unlimited có thực sự không giới hạn không?
- AIS hay True Move H - gói nào tốt hơn?
- eSIM Thái Lan có dùng được ở đảo Koh Samui, Koh Phangan không?
- Có thể chia sẻ hotspot (tethering) từ eSIM Thái Lan không?
- Tôi cần bao nhiêu data cho 7 ngày tại Thái Lan?

### `/esim-du-lich/nhat-ban`
- eSIM Nhật Bản có nhắn tin SMS về Việt Nam được không?
- Coverage ở Hokkaido và vùng nông thôn Kyoto có ổn không?
- eSIM Nhật có hỗ trợ tethering không?
- Gói nào phù hợp cho chuyến 10 ngày Tokyo-Osaka-Kyoto?
- eSIM có dùng được trên Shinkansen không?

### `/esim-du-lich/chau-au`
- 1 gói eSIM Châu Âu dùng được bao nhiêu nước?
- Croatia, Albania, Montenegro có nằm trong vùng phủ sóng không?
- eSIM Châu Âu có hỗ trợ 5G không?
- Tôi đi 3 tuần qua 6 nước Schengen - nên mua 1 gói hay mua theo từng nước?
- eSIM có hoạt động ở Anh (UK) sau Brexit không?

---

*BRD này được compile từ Web Growth Strategy Document v2.0 - eSIM Du Lịch. Mọi thay đổi scope cần approval từ PO và SEO Lead trước khi cập nhật document.*
