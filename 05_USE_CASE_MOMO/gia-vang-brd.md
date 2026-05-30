# BRD: Giá Vàng - SEO Inventory Assessment & Web Product Direction

> - **Use Case ID:** gia-vang
> - **Market:** Gold
> - **Division:** GPD - Out-App Traffic
> - **Owner:** GPD - Out-App Traffic
> - **Governance:** Web Product Lead
> - **Version:** v1.2 - 2026-05-23
> - **Status:** Draft - Chờ 3 pre-conditions (xem Section 3.3)
> - **Business Model:** Financial Utility + PLG Activation (không có sản phẩm mua/bán vàng)

---

> **Problem:** Hàng chục triệu người tra giá vàng mỗi ngày trên các trang báo đầy quảng cáo - không ai đang build một financial utility thực sự cho daily habit này.
> **KPI Owned:** Price Alert Sign-ups (MoMo login) → seed pipeline cross-sell tiết kiệm/đầu tư → MAU
> **Conversion Flow:** Search "giá vàng" → Widget load <1.5s → Financial context (vàng vs tiết kiệm) → Price Alert signup (MoMo login) → Cross-sell sản phẩm tài chính → Transaction

---

## 1. Executive Summary

### Situation

Tra giá vàng là daily financial habit của hàng chục triệu người Việt - 84M searches/tháng, user tra như tra thời tiết. Nhưng experience hiện tại là tệ: báo lớn đầy quảng cáo, load chậm, không có financial context, không có tính năng cá nhân hóa. Tất cả đang phục vụ user như một bài báo, không phải một công cụ tài chính. MoMo SoV = 0% - greenfield hoàn toàn.

### Complication

MoMo không có sản phẩm mua/bán vàng. Điều này có nghĩa là không thể direct-sell - conversion path sang App phải được thiết kế thông minh, không thể ép buộc. Nếu không có PLG bridge rõ ràng, đây chỉ là traffic play thuần túy - volume lớn nhưng không có business value, và leadership sẽ không approve ngân sách. Đồng thời 3 technical blockers phải được giải quyết trước khi commit build: API giá vàng real-time reliable, BU Owner vận hành long-term, và KPI framework được leadership align. Thiếu một trong ba - không nên build.

### Resolution

`momo.vn/gia-vang` là một **financial utility product**, không phải trang SEO. Product job duy nhất: user tra giá vàng trong 2 giây, nhận financial context thực sự (vàng đang tốt hơn hay tệ hơn tiết kiệm MoMo?), và nếu muốn theo dõi giá - đăng ký price alert bằng MoMo account.

Price alert là PLG hook của toàn bộ use case: chuyển anonymous visitor thành MoMo registered user một cách tự nhiên - user chủ động muốn tính năng này, không bị push. Sau khi login, cross-sell tiết kiệm/đầu tư xảy ra contextual trong hệ sinh thái, không phải CTA cứng.

---

## 2. Bối Cảnh Thị Trường

### 2.1 SEO Inventory - Volume Theo Cluster

| Cluster | Volume Search/tháng | Số Keywords | Ghi chú |
|---|---|---|---|
| Giá vàng | 63.875.790 | 2.751 | Cluster lớn nhất, cạnh tranh cực cao |
| Vàng SJC | 19.468.380 | 2.091 | Brand search, SJC.com.vn dominant |
| Vàng nhẫn | 892.590 | 3.313 | Long-tail cao, cơ hội tốt |
| Mua vàng | 634.630 | 1.336 | Transactional - ngoài scope |
| Vàng miếng | 259.360 | 456 | Informational |
| Tỷ giá vàng | 123.500 | 294 | Overlap tỷ giá ngoại tệ |
| Vàng 24k | 87.060 | 443 | Informational |
| **TỔNG ADDRESSABLE** | **~84.3M** | | Sau khi loại cluster ngoài scope |

### 2.2 Competitor Landscape

**Nhóm Báo Lớn (chiếm phần lớn Top SERP):**
- **Tuổi Trẻ** (tuoitre.vn) - Bảng giá realtime PNJ, SJC, DOJI, 9999. Domain authority cực cao.
- **VnExpress** (vnexpress.net) - Cập nhật từng giờ, tích hợp sâu vào homepage.
- **VietnamNet** - Cập nhật liên tục SJC, nhẫn 9999, biểu đồ biến động.
- **24h.com.vn** - Giá vàng SJC, 9999, 24k, phân tích dự báo xu hướng.

**Nhóm Chuyên Trang Tài Chính:**
- **24HMoney** (24hmoney.vn) - Bảng giá realtime + community phân tích.
- **Simplize** (simplize.vn) - Tích hợp công cụ tính lãi suất cạnh bảng giá vàng.
- **GiaVang.Net** - Chuyên trang thuần giá vàng, tỷ giá, phân tích market.

**Nhóm Official Brand Sites:**
- **SJC.com.vn** - Nguồn giá gốc, brand authority tuyệt đối cho cluster "Vàng SJC".
- **PNJ.com.vn** - Nguồn giá chính thức PNJ.
- **DOJI** - App riêng: realtime + quản lý giao dịch + tìm cửa hàng gần nhất.

### 2.3 Gap Analysis - Điểm Yếu Của Tất Cả Competitors

| Điểm yếu của Competitors | Cơ hội cho MoMo |
|---|---|
| Báo lớn: UX nặng quảng cáo, load chậm, không có financial context | Widget sạch, nhanh, có context tài chính (vàng vs tiết kiệm) |
| Tất cả: không có price alert thông minh | Price alert là PLG hook - user chủ động login MoMo |
| Tất cả: không cá nhân hóa, không kết nối tài chính cá nhân | Sau login: context hóa dựa trên portfolio MoMo của user |
| Chuyên trang: thiếu tích hợp fintech ecosystem | Bridge tự nhiên sang tiết kiệm/đầu tư MoMo |
| Brand sites (SJC, PNJ): thiếu context tài chính rộng hơn | So sánh đa chiều: vàng vs tỷ giá vs lãi suất tiết kiệm |

**Nhận định thực tế:** Chiếm Top 3 head keyword "giá vàng hôm nay" là không thực tế - báo lớn có domain authority áp đảo và đã build thói quen user từ nhiều năm. Chiến lược đúng là chiếm long-tail + sub-cluster + build product đủ tốt để user bookmark/return trực tiếp nhờ price alert.

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi

User hoàn thành daily habit "tra giá vàng" trên MoMo với experience tốt nhất thị trường - sạch, nhanh, và có financial context mà không nơi nào khác có. Price alert là tính năng PLG: user muốn dùng thì đăng nhập MoMo - đây là activation path tự nhiên không ép buộc.

3 business outcomes phát sinh từ product:

**Financial Authority:** MoMo = nguồn thông tin tài chính đáng tin cậy trong daily life. Đây là brand moat dài hạn cho toàn bộ FS vertical - không chỉ riêng gold. User tra vàng trên MoMo mỗi ngày = MoMo là financial companion, không phải chỉ là ví điện thoại.

**PLG Activation via Price Alert:** User muốn nhận thông báo khi vàng đạt ngưỡng giá → phải login MoMo → user trong ecosystem → cross-sell tiết kiệm/đầu tư contextual. Không phải CTA cứng - user tự convert vì sản phẩm đủ tốt.

**Long-tail Organic Traffic:** Chiếm sub-clusters cạnh tranh thấp (vàng nhẫn 9999, tỷ giá vàng thế giới, informational queries) để build domain authority dài hạn trong vertical tài chính.

### 3.2 Dự Án Này KHÔNG Phải

- Không phải trang giao dịch mua/bán vàng
- Không phải trang quản lý tài sản vàng của user
- Không phải đối tác phân phối với SJC/PNJ
- Không phải cạnh tranh head keyword "giá vàng hôm nay" với báo lớn
- Không phải W2A Play với CTA ép buộc - conversion phải xảy ra tự nhiên qua product value

### 3.3 Pre-conditions - Phải Giải Quyết Trước Khi Commit Build

**Đây là điều kiện tiên quyết, không phải rủi ro có thể chấp nhận.** Thiếu 1 trong 3 - dừng lại.

| # | Pre-condition | Trạng thái | Owner giải quyết |
|---|---|---|---|
| P1 | API giá vàng real-time reliable - partnership hoặc aggregator có SLA uptime >99% | Chưa giải quyết | GPD + Legal |
| P2 | BU Owner xác nhận - người chịu trách nhiệm vận hành và update long-term | Chưa xác định | Bảo escalate lên Công |
| P3 | KPI framework aligned với leadership: Traffic + Price Alert Signups, không phải W2A Conversion Rate | Chưa align | Bảo present với Công |

---

## 4. JTBD Analysis

### Job #1: Tra Giá Vàng Nhanh Hằng Ngày

> "Hôm nay vàng bao nhiêu? SJC tăng hay giảm so hôm qua?"

| Dimension | Nội dung |
|---|---|
| Functional | Xem giá vàng SJC, DOJI, PNJ ngay lập tức. Biết delta so hôm qua và xu hướng 7 ngày |
| Emotional | Nắm bắt thị trường, không bị lỡ thông tin. Daily financial habit |
| Social | Chia sẻ thông tin giá vàng với gia đình khi có biến động lớn |
| Trigger | Mở điện thoại buổi sáng - Nghe tin thị trường biến động - Chuẩn bị mua/bán |
| Search → App | "giá vàng hôm nay" → Widget (<1.5s) → Đọc xong → Price alert setup → MoMo login |

**Giải pháp:** Widget giá vàng realtime above-the-fold, load dưới 1.5s, không cần đăng nhập để xem giá.

---

### Job #2: So Sánh Để Ra Quyết Định Đầu Tư

> "Vàng đang tốt hay gửi tiết kiệm MoMo tốt hơn? Tôi có nên chuyển sang vàng không?"

| Dimension | Nội dung |
|---|---|
| Functional | So sánh hiệu suất vàng vs lãi suất tiết kiệm trong 30/90 ngày |
| Emotional | Ra quyết định tài chính thông minh, không bị cảm tính |
| Social | Tư vấn được cho người thân về cách phân bổ tài sản |
| Trigger | Vàng biến động mạnh - Nhận tiền thưởng - Muốn đa dạng hóa |
| Search → App | "nên mua vàng hay gửi tiết kiệm 2026" → Blog → Internal link sang widget → So sánh → "Mở tiết kiệm MoMo" |

**Giải pháp:** Bảng so sánh contextual "Vàng vs Tiết kiệm MoMo" embedded trong widget - PLG bridge tự nhiên nhất.

---

### Job #3: Đặt Cảnh Báo Giá Để Không Lỡ Cơ Hội

> "Tôi muốn mua vàng khi xuống 90 triệu/lượng - ai đó nhắc tôi khi đến ngưỡng đó."

| Dimension | Nội dung |
|---|---|
| Functional | Nhận push notification khi vàng đạt ngưỡng giá user đặt |
| Emotional | Không cần theo dõi thủ công hằng ngày, không bị lỡ cơ hội |
| Social | "Anh cài alert trên MoMo, vàng lên 110 triệu rồi em ơi" - đây là "bữa tối test" |
| Trigger | Muốn mua vàng nhưng thấy giá hiện tại chưa hợp lý |
| Search → App | Widget → "Đặt cảnh báo giá" → Login MoMo → Push notification → Mở App khi alert fire |

**Giải pháp:** Price alert feature - đây là PLG hook cốt lõi của toàn bộ use case. Yêu cầu MoMo login để kích hoạt.

---

### Job #4: Tìm Hiểu Vàng (Giáo Dục Tài Chính)

> "Vàng SJC khác vàng nhẫn chỗ nào? Loại nào phù hợp với người thường?"

| Dimension | Nội dung |
|---|---|
| Functional | Hiểu sự khác biệt giữa các loại vàng. Biết cách đọc bảng giá |
| Emotional | Không muốn bị thiệt thòi vì không hiểu biết |
| Trigger | Lần đầu mua vàng - Nghe tin tức thị trường - Chuẩn bị mua vàng cho đám cưới |
| Search → App | "vàng sjc là gì" → Blog cluster → Internal link → Widget → Price alert signup |

**Giải pháp:** Blog cluster informational chất lượng cao targeting long-tail queries - funnel về widget + price alert.

---

## 5. Kiến Trúc Web

### 5.1 Sitemap Hub & Spoke

```
momo.vn/gia-vang [Hub - Widget + Financial Context]
    |
    ├── momo.vn/gia-vang/sjc          - Sub-cluster: Vàng SJC
    ├── momo.vn/gia-vang/nhan-9999    - Sub-cluster: Vàng nhẫn 9999
    ├── momo.vn/gia-vang/ty-gia       - Sub-cluster: Tỷ giá vàng thế giới
    |
    └── Blog Cluster (long-tail capture)
         ├── /blog/gia-vang-hom-nay-bao-nhieu
         ├── /blog/nen-mua-vang-sjc-hay-vang-nhan
         ├── /blog/gia-vang-the-gioi-anh-huong-trong-nuoc
         └── /blog/dau-tu-vang-hay-gui-tiet-kiem   [PLG bridge content]
```

### 5.2 Widget Giá Vàng - Yêu Cầu Cốt Lõi

Widget là product - không phải component phụ trợ. Phải load nhanh, đọc ngay, không yêu cầu interaction để lấy giá trị cơ bản. Price alert là tính năng premium yêu cầu login.

**Must-have (không login):**
- Bảng giá realtime: SJC miếng, SJC nhẫn, DOJI, PNJ, 9999 (mua vào / bán ra / delta so hôm qua)
- Giá vàng thế giới (USD/ounce + quy đổi VND/lượng)
- Timestamp cập nhật ("Cập nhật lúc HH:MM DD/MM")
- Biểu đồ biến động 7 ngày (line chart)
- **So sánh tài chính:** "Vàng tăng X% (30 ngày) | Tiết kiệm MoMo: X.X%/năm" - PLG bridge embedded tự nhiên

**PLG Feature (yêu cầu MoMo login):**
- Price alert: đặt ngưỡng giá → nhận push notification khi đến ngưỡng
- Máy tính quy đổi nâng cao: nhập số chỉ/lượng → ra VND → so sánh với tiết kiệm cùng số tiền đó
- Lịch sử tra cứu và portfolio vàng cá nhân

**Nguyên tắc cứng:**
- Không có tính năng mua/bán trực tiếp
- Không nhúng quảng cáo third-party vào widget
- Giá cơ bản không yêu cầu đăng nhập - user phải nhận value trước khi được ask to login

### 5.3 Data Source

| Dữ liệu | Nguồn đề xuất | Phương án dự phòng |
|---|---|---|
| Giá SJC | Partnership SJC.com.vn (ưu tiên) | NHNN (chính thức nhưng cập nhật chậm) |
| Giá DOJI, PNJ | API partner hoặc aggregator | WebGia |
| Giá thế giới (XAU/USD) | Investing.com API / Kitco API | Gold-API.io |
| Tỷ giá USD/VND | Vietcombank API (miễn phí) | NHNN |

**Lưu ý:** SJC và các thương hiệu vàng không có public API chính thức. Partnership chính thức với ít nhất 1 thương hiệu là điều kiện tiên quyết (Pre-condition P1).

### 5.4 User Flow Chính

**Flow 1: Tra giá hằng ngày → Price Alert (PLG core flow)**
```
Search "giá vàng hôm nay"
    → SERP (Organic Result / Direct)
    → momo.vn/gia-vang - Widget load <1.5s
    → Đọc giá, xem biểu đồ 7 ngày
    → Thấy so sánh "Vàng +8% (30 ngày) | Tiết kiệm MoMo 6.5%/năm"
    → "Đặt cảnh báo khi vàng xuống 90 triệu"
    → Login MoMo (PLG activation)
    → Alert active → Cross-sell tiết kiệm contextual
```

**Flow 2: Blog informational → Hub → PLG**
```
Search "nên mua vàng hay gửi tiết kiệm 2026"
    → Blog article (long-tail)
    → Internal link "Xem giá vàng thực tế hôm nay"
    → momo.vn/gia-vang
    → Widget + So sánh contextual → Price alert → MoMo login
```

---

## 6. Success Metrics

### 6.1 KPI Framework

**North Star Metric:** Price Alert Sign-ups (MoMo login từ widget) - đây là chỉ số duy nhất chứng minh product có business value, không phải chỉ là traffic play.

| Metric | Target (6 tháng) | Source | Ghi chú |
|---|---|---|---|
| Price Alert Sign-ups | TBD sau pilot | GA4 + Appsflyer | North Star - PLG activation |
| Monthly Unique Visitors (MUV) | 500K - 1M sessions | GA4 | Brand awareness indicator |
| Return Rate (7 ngày) | ≥ 30% | GA4 | Daily habit indicator |
| Widget engagement rate | ≥ 40% | GA4 Events | % user interact với widget |
| Cross-sell click (tiết kiệm/đầu tư) | TBD | GA4 Events | Revenue pipeline proxy |
| Long-tail keywords Top 10 | 50+ keywords | GSC | SEO authority build |

**Quan trọng - KPI Alignment (Pre-condition P3):**
KPI chính là Price Alert Sign-ups + Return Rate, không phải W2A Conversion Rate. W2A sẽ thấp do intent bridge indirect - đây là đặc tính của use case, không phải thất bại. Nếu leadership vẫn đo bằng W2A, phải align lại trước khi commit build - không phải sau khi launch.

---

## 7. Dependencies & Constraints

| Dependency | Mô tả | Blocker? |
|---|---|---|
| API giá vàng reliable (uptime >99%) | Không có dữ liệu chính xác = toàn bộ product mất giá trị. Pre-condition P1 | Có - tuyệt đối |
| Partnership hoặc legal clearance data source | SJC không có public API. Scraping có rủi ro pháp lý. Pre-condition P1 | Có - YMYL + legal |
| KPI alignment với leadership | Nếu KPI vẫn là W2A, use case bị đánh giá sai. Pre-condition P3 | Có - quyết định đầu tư |
| BU Owner xác nhận | Trang cross nhiều team - cần owner rõ ràng để vận hành long-term. Pre-condition P2 | Có - governance |
| MoMo login integration cho Price Alert | Price alert là PLG core - không có login integration thì mất toàn bộ business value | Có - PLG hook |
| Push notification permission | Alert giá vàng cần push notification - phụ thuộc App team | Có - product dependency |

**Constraints:**
- Widget phải có timestamp cập nhật rõ ràng - không hiển thị giá cũ không có cảnh báo
- Không dùng giá vàng không có nguồn gốc xác thực - YMYL content, sai data = mất trust
- Cross-sell CTA không dùng ngôn ngữ "khuyến nghị đầu tư" - tuân thủ pháp lý tư vấn tài chính
- Giá cơ bản phải xem được không cần login - user nhận value trước khi được ask to sign up

---

## Change Log

- **Tháng 5/2026 (v1.4):** Xóa Tracking Event Schema + AB Test Hypothesis - thuộc PRD/Action Plan, không phải BRD.
- **Tháng 5/2026 (v1.3):** Xóa Risk Assessment - thuộc PRD/Action Plan, không phải BRD.
- **Tháng 5/2026 (v1.2):** Reframe toàn bộ theo CEO/VP thinking. Đổi Business Model từ "Traffic Play" sang "Financial Utility + PLG". Xác định Price Alert là PLG hook cốt lõi. Thêm Pre-conditions gate, Tracking Event Schema, AB Test Hypothesis. Conversion flow explicit.
- **Tháng 5/2026 (v1.1):** Khởi tạo tài liệu assessment và chuẩn hóa cấu trúc.
