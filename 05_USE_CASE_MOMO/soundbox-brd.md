# BRD: Soundbox

> - **Project:** Soundbox Web D2C - Website Order Loa Báo Chuyển Khoản MoMo  
> - **Division:** PS (Payment Services) | **Team:** SME Offline  
> - **Main URL:** momo.vn/loa-thong-bao-chuyen-khoan (hiện tại) / URL mới cần confirm  
> - **Owner:** Inbound Team (Out-App Traffic / GPD) + BU Soundbox (SME Offline)  
> - **Timeline:** Kick-off tháng 05/2026 → Launch Phase 1 tháng 07/2026  
> - **Version:** 1.0 · Tháng 05/2026  
> - **Status:** Draft - Chờ stakeholder review  

---

## 1. Executive Summary

**Situation:** Soundbox (Loa Báo Chuyển Khoản MoMo) là sản phẩm phần cứng chiến lược phục vụ nhóm SME/tiểu thương - những người cần xác nhận giao dịch tức thì tại điểm bán. Thị trường từ khoá này đã tăng trưởng **x10 lần** trong vòng 12 tháng (từ 06/2024 đến 05/2025), đạt tổng volume ~46.000 lượt/tháng tính đến 2026. Inbound đã xây nền tảng từ H2/2024: MiniWeb Soundbox ra mắt tháng 8/2024 đạt đỉnh 6.900 sessions/tháng vào tháng 12/2024.

**Complication:** Kênh bán hàng hiện tại chỉ đi qua in-app MoMo, tạo ra ba rào cản nghiêm trọng: (1) bỏ sót hoàn toàn nhóm Non-MoMo Users dù nhu cầu tìm kiếm đang ở ~30.000 lượt/quý; (2) deep-link từ Ads/Affiliate bị đứt tracking khiến không đo được ROAS; (3) domain momo.vn chưa có giấy phép TMĐT nên không thể hoàn tất giao dịch trực tuyến. Song song, sự kiện thay đổi URL ngày 11/05/2025 đã phá vỡ ranking đã build từ 2024, organic traffic sụt từ đỉnh ~6.900 sessions (T12/2024) xuống còn ~2.500 sessions (T06/2025) - mất ~64% trong 6 tháng. Trong khi đó, competitors mới (MB Bank, Techcombank, Vietcombank, Loa Ting Ting, Loa Thần Tài Mobifone) liên tục tăng market share.

**Resolution:** Dự án này xây dựng kênh D2C (Direct-to-Consumer) qua website với hai luồng song song: (1) Tối ưu và khôi phục MiniWeb momo.vn để phục vụ MoMo users và capture organic traffic; (2) Build web bán hàng trên domain ipos.vn (hoặc domain tương đương có giấy phép TMĐT) để tiếp cận Non-MoMo Users và khép kín tracking phễu. Mục tiêu kép: **40.000 sessions/tháng** organic traffic + **CR = 3%** (số lượng Soundbox bán qua web).

---

## 2. Bối Cảnh Hiện Tại

### 2.1 Hiện trạng Web & Traffic

| Kênh | URL | Trạng thái | Vấn đề |
|---|---|---|---|
| MiniWeb MoMo (chính) | momo.vn/loa-thong-bao-chuyen-khoan | Đang hoạt động, đang phục hồi | URL đổi 11/5/2025 phá ranking; chưa có checkout |
| IPOS Web | thietbi.ipos.vn/product/loa-bao-tien-ve-momo-md711/ | Đang hoạt động | Chưa optimize SEO; chưa integrate tracking đầy đủ |
| In-App MoMo | Luồng đặt hàng nội bộ app | Đang hoạt động | Chỉ reach MoMo users; deep-link tracking broken |

### 2.2 Traffic Historical Data

| Giai đoạn | Organic Sessions | Click to App | CR% | Ghi chú |
|---|---|---|---|---|
| T08/2024 | 184 | 77 | 41.8% | MiniWeb launch |
| T09/2024 | 2.000 | 711 | 35.6% | Ramp-up |
| T10/2024 | 4.800 | 2.414 | 50.3% | Tăng tốt |
| T11/2024 | 5.900 | 1.531 | 25.9% | Đỉnh giai đoạn 1 |
| T12/2024 | 6.900 | 1.666 | 24.1% | Peak |
| T01/2025 | 5.700 | 930 | 16.3% | Sau Tết drop |
| T03/2025 | 4.200 | 366 | 8.7% | Tiếp tục giảm |
| T06/2025 | 2.500 | 362 | 14.5% | Điểm đáy |
| **H1/2025 total** | **25.300** | **3.178** | **12.5%** | Baseline H1 |

**Nhận xét:** CR% sụt mạnh từ 41-50% (T8-T10/2024) xuống còn 8-16% (H1/2025). Đây không chỉ là vấn đề traffic mà là vấn đề **chất lượng landing và intent matching** - cần investigate thêm.

### 2.3 Market Landscape

| Metric | Giá trị | Nguồn |
|---|---|---|
| Total search volume thị trường loa thông báo | ~46.000 lượt/tháng | Market Research 2026 - XLSX |
| Tăng trưởng thị trường (12 tháng) | x10 lần so với 06/2024 | Sheet 1.1 |
| Số lượng từ khoá tracked | 627 từ khoá | Sheet 1.1 |
| MoMo current market share (traffic) | [cần đo - GSC vs total volume] | [cần verify] |

**Top competitor clusters theo volume (Market Research 2026):**

| Cluster | Volume ước tính |
|---|---|
| Loa Thông Báo Chuyển Khoản (generic) | ~8.000+/tháng |
| Loa MoMo (branded) | ~2.500+/tháng |
| Loa Ngân Hàng (Vietcombank, MB, Techcombank, BIDV, Vietinbank) | ~8.000+/tháng |
| Loa Ting Ting / Thần Tài Mobifone / Tingee | ~2.500+/tháng |

**Nhận định:** Nhóm loa ngân hàng đang là threat lớn nhất - các ngân hàng có authority domain cực cao, tặng loa miễn phí cho khách hàng mở tài khoản. MoMo không thể thắng ở nhóm brand intent ngân hàng, nhưng có thể dominate nhóm generic intent và how-to intent.

---

## 3. Định Hướng Dự Án

**Dự án này phục vụ điều gì?**
Xây dựng kênh D2C qua website để: (1) mở rộng reach sang Non-MoMo Users chưa được touch bởi in-app funnel; (2) khép kín tracking cho Performance Marketing (Ads/Affiliate); (3) khôi phục và mở rộng organic traffic đã mất do sự cố URL tháng 5/2025.

**Ai được phục vụ?**
- **Primary:** SME/tiểu thương, chủ shop nhỏ, người bán hàng online chưa có tài khoản MoMo - đang tìm kiếm giải pháp xác nhận thanh toán tức thì
- **Secondary:** MoMo users hiện tại nhưng chưa biết/chưa đặt hàng Soundbox qua web

**Dự án này KHÔNG phải là gì?**
- KHÔNG phải build mobile app hay cải tiến in-app ordering flow (thuộc Mobile/Product team)
- KHÔNG phải dự án PR/brand awareness (không có KPI về impressions, reach)
- KHÔNG phải cover toàn bộ danh mục thiết bị phần cứng MoMo - chỉ focus Soundbox
- KHÔNG tự triển khai giải pháp TMĐT trên momo.vn nếu chưa có giấy phép - phải qua ipos.vn hoặc domain được phép

---

## 4. Phạm Vi & Deliverables

### Workstream Chính

| WST | Hạng mục | Owner | Mô tả | Priority |
|---|---|---|---|---|
| WST1 | MiniWeb MoMo - Tối ưu & Khôi phục | Inbound + BU | Revamp LP hiện tại; bổ sung long content; optimize onpage; cải thiện CR từ organic traffic | P1 |
| WST2 | IPOS Web - D2C Channel cho Non-MoMo | IPOS Dev + BU | Build hoặc optimize web bán hàng trên domain có phép TMĐT, tích hợp checkout đầy đủ | P1 |
| WST3 | Tracking Integration | DA + Dev + Inbound | Khép kín tracking toàn bộ phễu: Click → LP → Checkout → Purchase. Phục vụ cả SEO analytics và Ads optimization | P1 |
| WST4 | SEO/Content Scale | Inbound | Phục hồi ranking + mở rộng content cluster (blog, comparison, how-to) để capture mid-funnel và top-funnel | P2 |

### Out of Scope
- Build payment gateway mới trên momo.vn
- Chạy Paid Media campaigns (thuộc BU/SEM team)
- Develop tính năng aftercare / warranty tracking
- Tối ưu in-app ordering flow

---

## 5. JTBD Analysis (Keyword-Driven)

Từ Market Research 2026 (627 từ khoá, ~46.000 lượt/tháng), phân tích thành 5 Jobs chính:

---

### Job #1: Tìm Giải Pháp Xác Nhận Thanh Toán Tức Thì

**Search Intent Cluster (Buy/Go):** "loa thông báo chuyển khoản", "loa momo", "soundbox", "loa thanh toán", "loa bán hàng", "máy đọc tiền chuyển khoản"
**Volume ước tính:** ~12.000-15.000 lượt/tháng (generic + MoMo branded)

> *"Tôi đang bán hàng, khách chuyển khoản xong tôi không nghe được có tiền vào không. Cần thiết bị đọc to để tôi biết ngay - không cần nhìn điện thoại."*

| Dimension | Nội dung |
|---|---|
| Functional | Xác nhận giao dịch nhận tiền tức thì, hands-free, không phụ thuộc điện thoại |
| Emotional | Tự tin khi bán hàng; tránh bị khách "giả chuyển khoản" lừa |
| Social | Chuyên nghiệp hơn - đặc biệt trong bối cảnh shop nhỏ và quầy hàng |
| Trigger | Mất tiền vì không nghe thông báo; hoặc thấy shop khác dùng |
| Barrier | Không biết MoMo Soundbox khác gì loa ngân hàng; lo phí dịch vụ |

**Content/Page đáp ứng:** Landing Page chính + Product Page D2C với đầy đủ specs, giá, CTA đặt hàng

---

### Job #2: So Sánh Và Chọn Giữa Các Thương Hiệu

**Search Intent Cluster (Know/Buy):** "loa ting ting", "loa thần tài mobifone", "loa tingee", "loa mb bank", "loa techcombank", "loa vnpay", "so sánh loa chuyển khoản"
**Volume ước tính:** ~15.000-18.000 lượt/tháng (competitor branded)

> *"Tôi thấy có nhiều loại loa, không biết loa nào tốt hơn, rẻ hơn, dễ dùng hơn - nhất là loa ngân hàng tặng miễn phí vs loa MoMo phải mua."*

| Dimension | Nội dung |
|---|---|
| Functional | Hiểu sự khác biệt; đưa ra quyết định mua đúng |
| Emotional | Không muốn chọn sai - mất tiền hoặc trải nghiệm kém |
| Trigger | Bị overwhelmed bởi quá nhiều lựa chọn; thấy quảng cáo từ nhiều nguồn |
| Barrier | Loa ngân hàng tặng miễn phí là lợi thế lớn của đối thủ; MoMo cần argue bằng multi-bank support và UX |

**Content/Page đáp ứng:** Blog so sánh trung lập (MoMo vs Ting Ting, MoMo vs Loa Thần Tài Mobifone); trang clone LP theo competitor intent

---

### Job #3: Cài Đặt, Kết Nối & Troubleshoot

**Search Intent Cluster (Do/Know):** "cài đặt loa momo", "kết nối loa momo", "cách reset loa momo", "kết nối wifi loa momo", "loa momo không đọc tiền"
**Volume ước tính:** ~2.500-3.500 lượt/tháng (branded how-to)

> *"Tôi đã mua rồi nhưng setup không được - không biết connect wifi thế nào, loa không đọc."*

| Dimension | Nội dung |
|---|---|
| Functional | Sản phẩm hoạt động đúng như mong đợi |
| Emotional | Không muốn cảm thấy "mua nhầm"; muốn tự xử lý được |
| Trigger | Sản phẩm không work sau khi mua; hoặc đổi điện thoại/số tài khoản |

**Content/Page đáp ứng:** Blog how-to, FAQ page trên miniWeb; hỗ trợ retention (giảm churn của user đang dùng)

---

### Job #4: Xác Định Giá & Điều Kiện Sở Hữu

**Search Intent Cluster (Know/Buy):** "loa momo giá bao nhiêu", "loa momo có mất phí không", "đăng ký loa momo", "mua loa momo ở đâu", "giá loa thông báo chuyển khoản"
**Volume ước tính:** ~1.500-2.000 lượt/tháng

> *"Loa MoMo có miễn phí không? Hay phải mua? Mua ở đâu? Điều kiện là gì?"*

| Dimension | Nội dung |
|---|---|
| Functional | Biết chính xác chi phí sở hữu trước khi ra quyết định |
| Emotional | Lo ngại chi phí ẩn; muốn minh bạch |
| Barrier | Loa ngân hàng tặng miễn phí tạo ra perception "Tại sao MoMo lại tính tiền?" |

**Content/Page đáp ứng:** Pricing section rõ ràng trên LP; FAQ về phí, điều kiện đăng ký; CTA "Đặt hàng ngay" với price visible

---

### Job #5: Khám Phá Tính Năng & Ứng Dụng Thực Tế

**Search Intent Cluster (Know):** "soundbox là gì", "loa thông báo chuyển khoản là gì", "tính năng loa momo", "loa bán hàng dùng cho gì"
**Volume ước tính:** ~1.000-1.500 lượt/tháng (awareness/education)

> *"Tôi mới nghe đến soundbox - không rõ nó là cái gì, dùng cho trường hợp nào."*

| Dimension | Nội dung |
|---|---|
| Functional | Hiểu product fit trước khi consider mua |
| Trigger | Thấy quảng cáo hoặc nghe người khác nhắc đến |

**Content/Page đáp ứng:** Educational blog, FAQ section trên LP, video/visual minh họa use case thực tế

---

## 6. Scope & Site Architecture

### Kiến Trúc Web 2 Domain

```
momo.vn/loa-thong-bao-chuyen-khoan  (MoMo Web - SEO Hub)
├── Main Landing Page (revamp - optimize conversion)
├── /blog/loa-momo-*                  (how-to, comparison cluster)
├── /loa-momo-vs-[competitor]/        (comparison pages - 8 URLs)
└── Internal links → ipos.vn (D2C checkout)

thietbi.ipos.vn/soundbox/            (IPOS Web - D2C Checkout)
├── Product Page (full checkout)
├── Pricing & điều kiện rõ ràng
└── Onelink/tracking integration
```

### Content Priority Matrix

| Content Type | Intent | Volume | Priority | Channel |
|---|---|---|---|---|
| Main LP Revamp | Transaction | ~8.000/tháng | P1 | momo.vn |
| Comparison Pages (8 URLs) | Comparison/Buy | ~15.000/tháng aggregate | P1 | momo.vn |
| How-to / Setup Guides (5 URLs) | Do/Technical | ~2.500/tháng | P2 | momo.vn/blog |
| Pricing & FAQ | Know/Buy | ~2.000/tháng | P2 | momo.vn + ipos |
| Educational Blog (soundbox là gì, use cases) | Know | ~1.500/tháng | P3 | momo.vn/blog |

---

## 7. Success Metrics

### North Star Metric

**Số lượng Soundbox đặt hàng qua web** = f(Web Traffic × CR%)

---

### Metric 1: Organic Traffic (North Star Driver)

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| Monthly organic sessions | ~2.500/tháng (T06/2025) | 40.000/tháng | T12/2026 | GSC + GA4 |
| H2/2025 organic total (actual) | 34.447 (target cũ, [cần verify actual]) | - | - | GSC |
| Market share (traffic/total volume) | [cần đo: ước tính <10% hiện tại] | ≥20% market share | T12/2026 | GSC vs Keyword tool |

**Logic target 40K:** Total thị trường ~46.000 lượt/tháng (Market Research 2026). Target 20% market share organic = ~9.200 sessions từ SEO MoMo-branded + generic. Tuy nhiên target 40K bao gồm cả traffic từ Paid (SEM/Affiliate) và Referral từ IPOS web. Cần breakdown rõ hơn theo channel. **[Cần align với BU về traffic mix breakdown]**

---

### Metric 2: Web-to-Purchase Conversion Rate

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| CR (sessions → đặt hàng thành công) | Hiện tại = 0% (không có D2C checkout) | 3% | T12/2026 | GA4 + IPOS analytics |
| Số đơn hàng/tháng qua web | 0 | ~1.200 đơn/tháng (40.000 × 3%) | T12/2026 | IPOS order system |
| Click-to-checkout rate | [cần đo sau launch] | ≥15% | T12/2026 | GA4 funnel |

---

### Metric 3: Ranking Keywords

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| Keywords ranking Top 5 (volume ≥ 500/tháng) | [cần đo từ GSC - bị ảnh hưởng bởi URL change] | 10 keywords | T09/2026 | SEO tool + GSC |
| Keywords ranking Top 10 (volume ≥ 200/tháng) | [cần đo] | 25 keywords | T12/2026 | SEO tool + GSC |
| Avg position cho cluster "loa thông báo chuyển khoản" | [cần đo] | ≤ 5 | T12/2026 | GSC |

---

## 8. Dependencies & Constraints

| Dependency | Owner | Mô tả | Blocker? | Status |
|---|---|---|---|---|
| **Giấy phép TMĐT momo.vn** | Legal / BU | momo.vn hiện không được phép checkout trực tiếp. Nếu không có license → phải đi qua ipos.vn cho toàn bộ checkout flow | **Hard blocker** | [cần confirm từ Legal] |
| **IPOS Dev Team** | IPOS + BU | Build/optimize product page trên ipos.vn với checkout, pricing, CTA rõ ràng. Cần confirm scope: điều chỉnh trang cũ hay build mới? | **Hard** | [chưa xác nhận] |
| **URL Canonicalization sau sự kiện 11/5/2025** | Web Platform | Cần confirm 301 redirect từ URL cũ về URL mới đã được setup đúng chưa. Nếu sai → link equity bị mất | **Hard** | [cần kiểm tra GSC Coverage] |
| **Onelink / Appsflyer tracking setup** | DA Team + Dev | Setup tracking parameter đầy đủ cho toàn bộ phễu từ web → app (cho MoMo users) và web → checkout (cho Non-MoMo users) | **Hard** | [cần DA confirm] |
| **BU Soundbox - Content Brief** | BU | Cần BU cung cấp: list tính năng sản phẩm, list lỗi thường gặp + cách xử lý, pricing chính thức, điều kiện đặt hàng | P1 | [chưa có] |
| **GTM Container Update** | Web Platform / GTM Owner | Deploy tracking tags mới; QA trước launch | P1 | [chưa start] |
| **Inbound Content Team** | Inbound | Sản xuất 15-25 bài blog/tháng theo content calendar. Cần template + angle brief từ SEO Lead | P2 | [đang plan] |
| **Clone LP - Legal/BMC Approve** | Legal + BMC | 8 comparison pages cần content được approve trước khi air (mention competitor brands) | P2 | [chưa start] |

**Hard constraint không thể thay đổi:**
- momo.vn không thể xử lý payment trực tiếp cho đến khi có giấy phép TMĐT
- Nội dung mention competitor brand (ngân hàng, Ting Ting...) phải qua legal review

---

## 9. Risk Assessment

| # | Rủi ro | Loại | Khả năng | Impact | Mitigation |
|---|---|---|---|---|---|
| R1 | URL change T5/2025 chưa được 301 redirect đúng - link equity mất vĩnh viễn | Technical | Cao | Cao | Kiểm tra GSC Coverage ngay trong tuần 1; verify 301 chain; nếu sai → escalate Web Platform |
| R2 | ipos.vn domain không có đủ SEO authority để rank → traffic không đến checkout page | Market | Cao | Cao | Strategy: momo.vn làm hub SEO, internal link về ipos.vn cho checkout - không cần ipos.vn rank tự nhiên |
| R3 | Competitor ngân hàng dominate phần lớn SERP với domain authority cao hơn, tặng loa miễn phí | Market | Rất cao | Trung bình | Focus vào generic intent (không branded) + how-to niche; differentiate bằng "multi-bank support" và ease of setup |
| R4 | CR 3% quá cao nếu traffic quality thấp (informational intent landing on transaction page) | Data/Tracking | Trung bình | Cao | Phân tích intent từng traffic source; không gom tất cả vào 1 CR metric; tách CR by channel |
| R5 | BU chậm cung cấp content brief (tính năng, lỗi thường gặp) → content production bị block | Execution | Trung bình | Trung bình | Lock brief deadline trong kick-off; Inbound viết assumption trước, BU review và điều chỉnh |
| R6 | Legal không approve comparison page mention competitor → mất toàn bộ traffic cluster competitor branded | Legal | Trung bình | Cao | Viết nội dung "neutral comparison" thay vì attack competitor; brief Legal sớm trước khi production |
| R7 | Tracking bị broken sau launch (Onelink param không fire, GA4 event miss) → không đo được conversion | Technical | Trung bình | Cao | QA tracking checklist trước launch; dual-stack GA4 + PostHog; weekly data audit tháng đầu |
| R8 | Market volume tăng x10 nhưng intent chủ yếu là bank-specific ("loa vietcombank") - MoMo không thể capture | Market | Cao | Trung bình | Accept: không cạnh tranh branded intent ngân hàng; focus generic + MoMo-branded cluster |

---

## 10. Next Steps

| # | Deliverable | Owner | Mô tả | Target date |
|---|---|---|---|---|
| 1 | **Technical Audit - URL & Redirect Check** | SEO Lead + Web Platform | Kiểm tra 301 redirect từ URL cũ → mới; verify trong GSC Coverage; kiểm tra link equity status | Tuần 1 (T5/2026) |
| 2 | **BU Brief Collection** | SEO Lead + BU Soundbox | Lock danh sách tính năng, lỗi thường gặp, pricing, điều kiện đặt hàng từ BU | Tuần 1-2 |
| 3 | **Tracking Design Doc (Web-to-Purchase)** | DA Team + SEO Lead | Define toàn bộ GA4 events, Onelink params, Appsflyer mapping cho funnel mới. Bao gồm cả luồng MoMo users và Non-MoMo users | Tuần 2 |
| 4 | **IPOS Web Scope Confirmation** | BU + IPOS Dev | Xác định: điều chỉnh trang cũ hay build product page mới? Timeline dev? | Tuần 2 |
| 5 | **Content Calendar Q3/2026** | Inbound Content | Plan 15-25 bài/tháng theo cluster priority (Phase 1: comparison + transaction intent; Phase 2: how-to + educational) | Tuần 3 |
| 6 | **Main LP Revamp Brief** | Inbound + BU | Brief chi tiết cho LP revamp: copy, structure, CTA placement, A/B test hypotheses | Tuần 3 |
| 7 | **Comparison Pages - Legal Brief** | SEO Lead + Legal/BMC | Submit 8 comparison page outlines để Legal review trước production | Tuần 3-4 |
| 8 | **PRD - WST1 & WST2** | Inbound + IPOS Dev | Viết PRD chi tiết cho MiniWeb revamp và IPOS D2C page; define acceptance criteria | Tuần 4 |
| 9 | **Launch Phase 1 (LP Revamp + Basic Tracking)** | All | Go-live WST1 + WST3 cơ bản | T7/2026 |
| 10 | **Launch Phase 2 (D2C Checkout + Content Scale)** | All | Go-live WST2 + WST4 | T9/2026 |

---

## 11. Product Ideas & Thinking Notes

> **Lưu ý:** Đây là các ý tưởng định hướng sản phẩm đang được ghi nhận để phát triển thêm — chưa phải requirement chính thức. Cần evaluate thêm về feasibility, tech effort và business case trước khi đưa vào Roadmap.

---

### Idea 1: Multi-SKU Catalog + "Add to Cart" → Redirect IPOS (No Checkout trên momo.vn)

**Vấn đề đang giải quyết:** Hiện tại momo.vn chỉ có 1 trang cho toàn bộ Soundbox, trong khi thực tế có 3-4 dòng loa (SKU) khác nhau. User không có trải nghiệm browse sản phẩm và so sánh trước khi quyết định.

**Ý tưởng:**
- Build một **Mini Catalog** trên momo.vn với đầy đủ 3-4 SKU Soundbox, mỗi SKU có trang riêng (specs, giá, use case phù hợp).
- Thêm tính năng **"Add to Cart"** trên momo.vn — giỏ hàng chỉ là UI (không có payment gateway), đóng vai trò ghi nhận intent của user.
- Khi user bấm **"Đặt hàng / Thanh toán"** → Redirect sang ipos.vn với thông tin SKU đã chọn được truyền qua URL params (pre-filled order).

**Lợi ích kỳ vọng:**
- Nâng cao conversion intent: User đã "commit" khi add to cart → CR sang ipos cao hơn click cold link.
- Đánh giải quyết **Job #4 (Xác định giá & điều kiện)** trực tiếp trên momo.vn trước khi redirect.
- SEO benefit: Mỗi SKU page = 1 URL riêng → capture long-tail keyword theo model (VD: "loa momo MD711 giá bao nhiêu").

**Cần clarify:**
- [ ] BU cung cấp danh sách đầy đủ SKU hiện tại (tên, model, giá, specs).
- [ ] Tech: URL param scheme để pre-fill SKU trên ipos.vn khi redirect.
- [ ] UX: Giỏ hàng mini (sidebar/modal) hay trang /cart riêng?

---

### Idea 2: IPOS Page Build Theo Brand Guideline MoMo (Seamless Handoff)

**Vấn đề đang giải quyết:** Khi user từ momo.vn bị redirect sang ipos.vn (domain lạ), họ có thể mất trust và thoát — đây là điểm rò rỉ lớn nhất của funnel.

**Ý tưởng:**
- Build **landing/product page trên ipos.vn** sử dụng đúng brand guideline của MoMo: màu sắc, typography, logo placement, tone of voice.
- Tại điểm handoff (trước khi redirect), **mention rõ ràng trên momo.vn**: *"Bạn sẽ được chuyển đến trang đặt hàng chính thức của MoMo trên ipos.vn — đối tác bán hàng được ủy quyền."*
- Trang ipos cần có: trust signals (logo MoMo prominent, "Đối tác chính thức"), pre-filled SKU, pricing rõ ràng, checkout flow đơn giản.

**Lợi ích kỳ vọng:**
- Giảm trust gap khi chuyển domain.
- Tỷ lệ thoát khỏi ipos thấp hơn so với redirect "lạnh" hiện tại.

**Cần clarify:**
- [ ] Thỏa thuận với IPOS về quyền customize giao diện theo brand MoMo.
- [ ] Legal: Copy "đối tác được ủy quyền" cần approve.
- [ ] Design resource: Ai design trang ipos theo MoMo guideline?

---

### Idea 3: Revamp momo.vn/loa-thong-bao-chuyen-khoan → Sales Page (Chốt Đơn)

**Vấn đề đang giải quyết:** Trang hiện tại đang thiên về thông tin/giới thiệu sản phẩm — chưa được tối ưu để **thúc đẩy hành động mua hàng ngay**.

**Ý tưởng:** Revamp hoàn toàn trang thành **Sales Page với cấu trúc chốt đơn**, bao gồm:

| Section | Nội dung | Mục tiêu |
|---------|----------|----------|
| **Hero** | H1 mạnh (Pain-point → Solution) + CTA "Đặt hàng ngay" nổi bật | Capture intent ngay từ giây đầu |
| **Social Proof** | Số lượng merchants đang dùng, rating, testimonial thực tế từ tiểu thương | Xây dựng trust |
| **Product Showcase** | 3-4 SKU với giá và CTA per SKU | Facilitate lựa chọn |
| **Value Props** | Multi-bank support, tốc độ thông báo, bảo hành | Differentiate vs loa ngân hàng miễn phí |
| **FAQ Accordion** | Trả lời các barrier mua hàng phổ biến (phí, điều kiện, setup) | Giảm friction trước checkout |
| **Sticky CTA bar** | "Đặt hàng ngay — Giao trong 2 ngày" cố định khi scroll | Luôn có điểm convert |
| **Trust Signals footer** | Logo MoMo + TTDK partnership, giấy tờ, hỗ trợ | Tăng credibility cuối trang |

**SEO note:** Trang Sale Page vẫn phải maintain SEO value — cần đảm bảo long-form content (mức phạt, hướng dẫn setup) không bị loại bỏ hoàn toàn mà chuyển vào accordion/tab để trang vừa convert vừa rank.

**Cần clarify:**
- [ ] A/B test: Sales Page structure vs. trang hiện tại để đo CR trước khi fully commit.
- [ ] Copywriter brief: Cần social proof thực tế (số merchants, review) từ BU Soundbox.

---

## Appendix A: Keyword Clusters - Priority Summary

### Cluster P1 - Transaction/Go Intent (Target ngay)

| Keyword | Volume/tháng | Ghi chú |
|---|---|---|
| loa thông báo chuyển khoản | 1.900 | Primary keyword |
| loa momo | 1.300 | Branded, must rank #1 |
| loa chuyển khoản | 590 | Generic |
| loa báo chuyển khoản | 480 | Generic |
| loa thanh toán | 480 | Generic |
| loa thông báo chuyển khoản momo | 260 | Long-tail branded |
| soundbox | 390 | English variant |
| đăng ký loa momo | [<200] | Conversion intent cao |
| mua loa momo | [<200] | Bottom funnel |

### Cluster P2 - Competitor-Adjacent (Comparison pages)

| Cluster | Keywords tiêu biểu | Volume aggregate |
|---|---|---|
| Loa Ting Ting | loa ting ting, loa tingting | ~1.100+/tháng |
| Loa Thần Tài Mobifone | loa thần tài mobifone, loa mobifone | ~1.000+/tháng |
| Loa Techcombank | loa techcombank, loa ting ting techcombank | ~1.500+/tháng |
| Loa Vietcombank | loa vcb, loa thần tài vietcombank | ~1.800+/tháng |
| Loa MB Bank | loa mb, loa thanh toán mb | ~1.800+/tháng |

### Cluster P3 - How-to/Technical (Blog content)

Keywords how-to "cài đặt loa momo", "kết nối wifi loa momo", "reset loa momo", "cách kết nối loa momo với điện thoại" - aggregate ~500-800/tháng.

---

## Appendix B: Open Questions Cần Confirm Trước Kick-off

1. **Legal:** momo.vn có timeline cụ thể để obtain giấy phép TMĐT không? Hay toàn bộ checkout đi qua ipos.vn dài hạn?
2. **BU:** CR target 3% được define trên base traffic nào? (Tất cả sessions hay chỉ qualified sessions từ transaction-intent keywords?)
3. **DA:** GSC data hiện tại sau URL change có đang được track đúng không? Cần pull actual traffic H2/2025 để confirm vs KPI target.
4. **Web Platform:** 301 redirect từ URL cũ đã được setup chưa? Kiểm tra crawl log.
5. **BU + IPOS:** Scope IPOS web là build mới hay optimize trang hiện tại tại thietbi.ipos.vn?

---

## Change Log
- **Tháng 5/2026:** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.

