# BRD: Soundbox

> - **Project:** Soundbox Web D2C - Website Order Loa Báo Chuyển Khoản MoMo
> - **Division:** PS (Payment Services) | SME Offline
> - **Main URL:** momo.vn/loa-thong-bao-chuyen-khoan
> - **Owner:** Web Platform
> - **Governance:** Web Product Lead (Hiến)
> - **Version:** 2.0 - Tháng 05/2026
> - **Status:** Draft - Chờ stakeholder review

---

> **Problem:** Chủ quán và tiểu thương đang tìm "loa thông báo chuyển khoản" mỗi ngày - nhưng không có trang momo.vn nào cho họ đặt hàng. 46.000 searches/tháng đang chảy về đối thủ hoặc bị bỏ ngỏ hoàn toàn.
> **KPI Owned:** Số Soundbox đặt hàng qua web (Web Order Volume) = f(Traffic × CR%)
> **Conversion Flow:** Search "loa thông báo chuyển khoản" → momo.vn/loa-thong-bao-chuyen-khoan → Product info + CTA → ipos.vn checkout → Purchase confirmed

---

## 1. Executive Summary

### Situation

Chủ quán, tiểu thương, người bán online đang nhận tiền chuyển khoản mà không có cách xác nhận tức thì - điện thoại trong túi, tay bận giao hàng, thông báo đến trễ, khách đã đi. Họ đang tìm giải pháp: search volume "loa thông báo chuyển khoản" tăng x10 trong 12 tháng, đạt ~46.000 lượt/tháng. MoMo có đúng sản phẩm họ cần - nhưng không có D2C web channel để capture intent đó.

### Complication

Kênh bán hàng hiện tại chỉ đi qua in-app MoMo, tạo ra ba rào cản nghiêm trọng:

1. Bỏ sót hoàn toàn nhóm Non-MoMo Users dù nhu cầu tìm kiếm đang ở ~30.000 lượt/quý.
2. Deep-link từ Ads/Affiliate bị đứt tracking khiến không đo được ROAS.
3. Domain momo.vn chưa có giấy phép TMĐT nên không thể hoàn tất giao dịch trực tuyến.

Song song, sự kiện thay đổi URL ngày 11/05/2025 đã phá vỡ ranking đã build từ 2024 - organic traffic sụt từ đỉnh ~6.900 sessions (T12/2024) xuống còn ~2.500 sessions (T06/2025), mất ~64% trong 6 tháng. Competitors mới (MB Bank, Techcombank, Vietcombank, Loa Ting Ting, Loa Thần Tài Mobifone) liên tục tăng market share.

### Resolution

Xây dựng kênh D2C qua website với hai luồng song song: (1) Tối ưu và khôi phục MiniWeb momo.vn để phục vụ MoMo users và capture organic traffic; (2) Build web bán hàng trên domain ipos.vn (có giấy phép TMĐT) để tiếp cận Non-MoMo Users và khép kín tracking phễu. Product drives order - từ search intent đến confirmed purchase, không cần sales, không cần in-app.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Web & Traffic

| Kênh | URL | Trạng thái | Vấn đề |
|---|---|---|---|
| MiniWeb MoMo | momo.vn/loa-thong-bao-chuyen-khoan | Đang hoạt động, đang phục hồi | URL đổi 11/5/2025 phá ranking; chưa có checkout |
| IPOS Web | thietbi.ipos.vn/soundbox/ | Đang hoạt động | Chưa optimize SEO; tracking chưa đầy đủ |
| In-App MoMo | Luồng đặt hàng nội bộ app | Đang hoạt động | Chỉ reach MoMo users; tracking bị gián đoạn |

### 2.2 Traffic Historical Data

| Giai đoạn | Organic Sessions | Click to App | CR% | Ghi chú |
|---|---|---|---|---|
| T08/2024 | 184 | 77 | 41.8% | MiniWeb launch |
| T10/2024 | 4.800 | 2.414 | 50.3% | Tăng tốt |
| T12/2024 | 6.900 | 1.666 | 24.1% | Peak |
| T01/2025 | 5.700 | 930 | 16.3% | Sau Tết drop |
| T06/2025 | 2.500 | 362 | 14.5% | Điểm đáy sau URL change |

**Nhận xét:** CR% sụt mạnh từ 41-50% (T8-T10/2024) xuống còn 14-16% (H1/2025). Vấn đề không chỉ là traffic mà là chất lượng landing và intent matching.

### 2.3 Market Landscape

| Metric | Giá trị |
|---|---|
| Total search volume thị trường | ~46.000 lượt/tháng |
| Tăng trưởng thị trường (12 tháng) | x10 lần so với 06/2024 |
| Số lượng từ khoá tracked | 627 từ khoá |

**Top competitor clusters:**

| Cluster | Volume ước tính |
|---|---|
| Loa Thông Báo Chuyển Khoản (generic) | ~8.000+/tháng |
| Loa MoMo (branded) | ~2.500+/tháng |
| Loa Ngân Hàng (Vietcombank, MB, Techcombank, BIDV, Vietinbank) | ~8.000+/tháng |
| Loa Ting Ting / Thần Tài Mobifone / Tingee | ~2.500+/tháng |

**Nhận định:** Nhóm loa ngân hàng là threat lớn nhất - các ngân hàng có authority domain cực cao và tặng loa miễn phí khi mở tài khoản. MoMo không thể thắng ở nhóm brand intent ngân hàng, nhưng có thể dominate nhóm generic intent và how-to intent.

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi

**Tiểu thương tìm loa báo chuyển khoản - tìm thấy momo.vn - xem giá, tính năng, đặt hàng ngay - nhận loa, xác nhận giao dịch tức thì, bán hàng tự tin hơn.**

Web closes the D2C loop: từ search intent đến confirmed purchase mà không cần vào app, không cần gặp sales.

4 outcome phát sinh từ loop này:

**① SME Acquisition:** Capture Non-MoMo Users đang search generic intent - nhóm không thể reach qua in-app funnel.

**② Tracking Completeness:** ipos.vn checkout domain cho phép đo ROAS đầy đủ - mở khoá Performance Marketing.

**③ Ranking Recovery:** Khôi phục link equity bị mất do sự kiện URL 11/5/2025, rebuild organic foundation cho toàn cluster.

**④ Competitive Moat:** Chiếm generic intent "loa thông báo chuyển khoản" + how-to cluster trước khi ngân hàng dominate hoàn toàn.

### 3.2 Dự Án Này KHÔNG Phải

- Không build mobile app hay cải tiến in-app ordering flow
- Không phải dự án brand awareness (KPI đo conversion, không đo impressions)
- Không cover toàn bộ danh mục thiết bị phần cứng MoMo - chỉ focus Soundbox
- Không triển khai checkout trực tiếp trên momo.vn khi chưa có giấy phép TMĐT

---

## 4. JTBD Analysis

### Job #1: Tìm Giải Pháp Xác Nhận Thanh Toán Tức Thì

> "Tôi đang bán hàng, khách chuyển khoản xong tôi không nghe được có tiền vào không. Cần thiết bị đọc to để tôi biết ngay."

| Dimension | Nội dung |
|---|---|
| Functional | Xác nhận giao dịch nhận tiền tức thì, hands-free, không phụ thuộc điện thoại |
| Emotional | Tự tin khi bán hàng; tránh bị khách "giả chuyển khoản" lừa |
| Social | Chuyên nghiệp hơn trong mắt khách hàng - quầy có thiết bị bài bản, không cầm điện thoại suốt |
| Trigger | Mất tiền vì không nghe thông báo; hoặc thấy shop khác dùng |
| Search → App | "loa thông báo chuyển khoản", "loa momo" → momo.vn/loa-thong-bao-chuyen-khoan → "Đặt hàng ngay" → ipos.vn checkout (Non-MoMo) hoặc App MoMo (MoMo user) → Purchase confirmed |

**Giải pháp:** Landing Page chính + Product Page D2C với đầy đủ specs, giá, CTA đặt hàng.

---

### Job #2: So Sánh Và Chọn Giữa Các Thương Hiệu

> "Tôi thấy có nhiều loại loa, không biết loa nào tốt hơn - nhất là loa ngân hàng tặng miễn phí vs loa MoMo phải mua."

| Dimension | Nội dung |
|---|---|
| Functional | Hiểu sự khác biệt; đưa ra quyết định mua đúng |
| Emotional | Không muốn chọn sai - mất tiền hoặc trải nghiệm kém |
| Social | Bạn bè hay đồng nghiệp cùng ngành hỏi "loa nào ngon hơn" - cần câu trả lời tự tin từ so sánh thực tế, không phải phỏng đoán |
| Trigger | Bị overwhelmed bởi quá nhiều lựa chọn; thấy quảng cáo từ nhiều nguồn |
| Search → App | "loa momo vs ting ting", "so sánh loa báo chuyển khoản", "loa ngân hàng nào tốt" → /blog/so-sanh-loa-momo-vs-ting-ting → CTA "Đặt loa MoMo" → ipos.vn checkout |

**Giải pháp:** Blog so sánh trung lập (MoMo vs Ting Ting, MoMo vs Loa Thần Tài Mobifone); landing page theo competitor intent.

---

### Job #3: Cài Đặt, Kết Nối & Troubleshoot

> "Tôi đã mua rồi nhưng setup không được - không biết connect wifi thế nào, loa không đọc."

| Dimension | Nội dung |
|---|---|
| Functional | Sản phẩm hoạt động đúng như mong đợi |
| Emotional | Không muốn cảm thấy "mua nhầm"; muốn tự xử lý được |
| Social | Không muốn gọi hotline rồi bị thấy là "không biết dùng đồ công nghệ" trước mặt nhân viên hay hàng xóm |
| Trigger | Sản phẩm không work sau khi mua; hoặc đổi điện thoại/số tài khoản |
| Search → App | "cách cài đặt loa momo", "kết nối wifi loa momo không được", "reset loa momo" → /blog/cai-dat-loa-momo → Hướng dẫn từng bước + CTA upsell cho user chưa có loa |

**Giải pháp:** Blog how-to + FAQ page trên miniWeb; hỗ trợ retention user đang dùng.

---

### Job #4: Xác Định Giá & Điều Kiện Sở Hữu

> "Loa MoMo có miễn phí không? Hay phải mua? Mua ở đâu? Điều kiện là gì?"

| Dimension | Nội dung |
|---|---|
| Functional | Biết chính xác chi phí sở hữu trước khi ra quyết định |
| Emotional | Lo ngại chi phí ẩn; muốn minh bạch |
| Social | Thấy shop cạnh bên có loa mà mình chưa có - không muốn thua kém về sự chuyên nghiệp trong mắt khách |
| Trigger | Thấy giá quảng cáo khác nhau ở nhiều nơi; chưa rõ điều kiện đăng ký |
| Search → App | "loa momo giá bao nhiêu", "mua loa momo ở đâu", "điều kiện đăng ký loa momo" → momo.vn/loa-thong-bao-chuyen-khoan#pricing → Pricing section rõ ràng → "Đặt hàng ngay" → ipos.vn |

**Giải pháp:** Pricing section rõ ràng trên LP; FAQ về phí, điều kiện đăng ký; CTA "Đặt hàng ngay" với price visible.

---

### Job #5: Khám Phá Tính Năng & Ứng Dụng Thực Tế

> "Tôi mới nghe đến soundbox - không rõ nó là cái gì, dùng cho trường hợp nào."

| Dimension | Nội dung |
|---|---|
| Functional | Hiểu product fit trước khi consider mua |
| Emotional | Không muốn mua thứ "không cần thiết"; cần thấy use case cụ thể giống mình |
| Social | Thấy hàng xóm hay người bán cùng chợ dùng - muốn hiểu xem mình có cần không trước khi hỏi họ |
| Trigger | Thấy quảng cáo hoặc nghe người khác nhắc đến |
| Search → App | "soundbox là gì", "loa thông báo chuyển khoản là gì", "cách dùng loa báo tiền" → Educational blog/FAQ → CTA xem sản phẩm → momo.vn LP → ipos.vn đặt hàng |

**Giải pháp:** Educational blog + FAQ section trên LP + video/visual minh họa use case thực tế.

---

## 5. Kiến Trúc Web

### 5.1 Kiến Trúc 2 Domain

```
momo.vn/loa-thong-bao-chuyen-khoan  [SEO Hub]
├── Main Landing Page (revamp - optimize conversion)
├── /blog/loa-momo-*                  (how-to, comparison cluster)
├── /loa-momo-vs-[competitor]/        (8 comparison pages)
└── Internal links -> ipos.vn (D2C checkout)

thietbi.ipos.vn/soundbox/            [D2C Checkout]
├── Product Page (full checkout)
├── Pricing & điều kiện rõ ràng
└── Tracking integration đầy đủ
```

**Logic phân tách:** momo.vn là SEO hub, capture organic và tăng trust. ipos.vn là checkout point (có giấy phép TMĐT). Không cần ipos.vn rank tự nhiên - momo.vn làm hub và internal link về ipos.vn.

### 5.2 Workstreams

| WST | Hạng mục | Mô tả |
|---|---|---|
| WST1 | MiniWeb MoMo - Tối ưu & Khôi phục | Revamp LP hiện tại; bổ sung long content; optimize onpage; cải thiện CR từ organic traffic |
| WST2 | IPOS Web - D2C Channel cho Non-MoMo | Build/optimize web bán hàng trên domain có phép TMĐT, tích hợp checkout đầy đủ |
| WST3 | Tracking Integration | Khép kín tracking toàn bộ phễu: Click → LP → Checkout → Purchase. Phục vụ SEO analytics và Ads optimization |
| WST4 | SEO/Content Scale | Phục hồi ranking + mở rộng content cluster (blog, comparison, how-to) để capture mid-funnel và top-funnel |

### 5.3 Content Structure

| Content Type | Intent | Volume | Channel |
|---|---|---|---|
| Main LP Revamp | Transaction | ~8.000/tháng | momo.vn |
| Comparison Pages (8 URLs) | Comparison/Buy | ~15.000/tháng aggregate | momo.vn |
| How-to / Setup Guides (5 URLs) | Do/Technical | ~2.500/tháng | momo.vn/blog |
| Pricing & FAQ | Know/Buy | ~2.000/tháng | momo.vn + ipos |
| Educational Blog | Know | ~1.500/tháng | momo.vn/blog |

---

## 6. Success Metrics

### 6.1 North Star Metric

**Số lượng Soundbox đặt hàng qua web** = f(Web Traffic × CR%)

**Funnel:**
```
Search → momo.vn LP → CTA click → ipos.vn checkout → Purchase confirmed
```

### 6.2 KPI Framework

| Metric | Baseline | Target (EOY 2026) | Source |
|---|---|---|---|
| Monthly organic sessions | ~2.500/tháng (T06/2025) | 40.000/tháng | GSC + GA4 |
| Market share (traffic/total volume) | Dưới 10% ước tính | 20% market share | GSC vs Keyword tool |
| CR (sessions → đặt hàng thành công) | 0% (chưa có D2C checkout) | 3% | GA4 + IPOS analytics |
| Số đơn hàng/tháng qua web | 0 | ~1.200 đơn/tháng | IPOS order system |
| Keywords ranking Top 5 (volume 500+/tháng) | Đang đo baseline | 10 keywords | GSC + SEO tool |
| Keywords ranking Top 10 (volume 200+/tháng) | Đang đo baseline | 25 keywords | GSC + SEO tool |

---

## 7. Dependencies & Constraints

| Dependency | Mô tả | Blocker? |
|---|---|---|
| Giấy phép TMĐT momo.vn | momo.vn hiện không được phép checkout trực tiếp. Chưa có license → toàn bộ checkout qua ipos.vn | Hard blocker |
| IPOS Dev Team | Build/optimize product page trên ipos.vn với checkout, pricing, CTA rõ ràng | Hard |
| URL Canonicalization sau sự kiện 11/5/2025 | Cần confirm 301 redirect từ URL cũ về URL mới đã được setup đúng chưa. Nếu sai → link equity bị mất | Hard |
| Onelink / Appsflyer tracking setup | Setup tracking parameter đầy đủ cho toàn bộ phễu từ web → app (MoMo users) và web → checkout (Non-MoMo users) | Hard |
| BU Soundbox - Content Brief | Cần BU cung cấp: danh sách tính năng sản phẩm, lỗi thường gặp + cách xử lý, pricing chính thức, điều kiện đặt hàng | Có |
| Legal review comparison pages | 8 comparison pages mention competitor brands cần Legal approve trước khi publish | Có |

**Constraints:**
- momo.vn không thể xử lý payment trực tiếp cho đến khi có giấy phép TMĐT - constraint không thể thay đổi
- Nội dung mention competitor brand (ngân hàng, Ting Ting...) bắt buộc qua legal review
- URL 301 redirect phải được verify trước khi làm bất kỳ SEO optimization nào (để không mất link equity thêm)

---

## Change Log

- **Tháng 5/2026 (v2.0):** Apply CEO BRD Standard: Thêm Problem Statement block, rewrite Situation theo user-centric, thêm Product Job Cốt Lõi (Section 3.1), thêm Search → App + Social dimension vào tất cả JTBD. Xóa Risk Assessment (Section 8). Xóa Appendix A Keyword Clusters.
- **Tháng 5/2026 (v1.0):** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.
