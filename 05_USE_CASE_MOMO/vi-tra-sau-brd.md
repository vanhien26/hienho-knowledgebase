# BRD: Ví Trả Sau (BNPL) - Web Growth & SEO/GEO Project

> - **Project:** Use Case Ví Trả Sau - Web Growth & Inbound SEO/GEO
> - **Main URL:** momo.vn/vi-tra-sau
> - **Division:** FS (Financial Services) - PayLater
> - **Version:** 1.4 · Tháng 5/2026
> - **Status:** Active

---

> **Problem:** Hàng triệu người search "trả góp", "nợ xấu mua được không", "mua trước trả sau" mỗi tháng - nhưng không có trang VTS nào xuất hiện khi họ tìm. 485K SV/tháng adjacent intent đang chảy về Home Credit và ZaloPay trong khi VTS là giải pháp phù hợp nhất: không check CIC, duyệt 3 phút, hạn mức đến 20 triệu.
> **KPI Owned:** Activated VTS Users from Web (user lần đầu kích hoạt VTS có nguồn gốc từ organic momo.vn, trong 7 ngày kể từ lần đầu visit)
> **Conversion Flow:** Search "trả góp CMND" / "nạp game hết tiền" / "nợ xấu mua được không" → /vi-tra-sau/{slug} → Hiểu VTS + CTA → App MoMo → VTS Activation → Transaction

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
- **Vấn đề cốt lõi:** Người dùng có nhu cầu mua sắm/trả góp khẩn cấp nhưng bị ngân hàng từ chối vì nợ xấu hoặc thủ tục rườm rà. Họ search Google tìm giải pháp nhưng VTS (dù duyệt 3 phút, không check CIC) lại hoàn toàn "vô hình" trên Search.
- **Giải pháp (The "What"):** Biến Web thành kênh "Cứu cánh tài chính 1 chạm". Cung cấp công cụ giả lập trả góp trực quan và chặn đầu (intercept) mọi từ khóa ngách để dắt user tải App kích hoạt VTS ngay lập tức.

### 1.2 Situation
Người search "mua điện thoại trả góp chỉ cần CMND", "nợ xấu có mua được không", "nạp game hết tiền" - đây là nhóm đã có intent mua, cần credit, đang bị loại trừ bởi hệ thống ngân hàng truyền thống. VTS là đúng sản phẩm cho họ. Nhưng khi họ search, trang `/vi-tra-sau` không xuất hiện. Hub page có 1,56M impressions/tháng nhưng CTR CTA chỉ 7,25%.

### 1.3 Complication
Core market "Trả Sau" chỉ có 135K SV/tháng và VTS đã chiếm 54% SOV - growth room trong core market hạn chế. Adjacent market (Trả Góp: 200K SV; Tín Dụng: 700K SV) tổng ~900K SV/tháng là pool intent lớn nhưng SOV VTS tại đó chỉ 10-40%. 

### 1.4 Resolution
Build sub-pages use-case và **PLG Interactive Tool** để intercept adjacent intent; revamp hub `/vi-tra-sau` để tăng W2A CVR từ 7% lên 20%; scale blog 20-30 bài targeting Trả Góp + Tín Dụng clusters; tối ưu GEO/AEO `llms.txt` để maintain TOM. Product drives activation - user tìm thấy đúng lúc cần, hiểu trong 30 giây, kích hoạt ngay.

---

## 2. Bối Cảnh Hiện Tại

### 2.1 Hiện trạng Web Assets

| Asset | URL | Trạng thái | Ghi chú |
|---|---|---|---|
| Hub page | /vi-tra-sau | Live, cần revamp | CTR CTA ~7,25%, scroll depth yếu trên mobile |
| Blog VTS | /blog/vi-tra-sau-* | Live, có traffic cao | Top page: 128K clicks. Cần update + GEO layer |
| FAQ / Hỏi đáp | /hoi-dap/dieu-kien-dieu-khoan-su-dung-vi-tra-sau | Live | 16K clicks, avg pos 4.78 |
| Sub-pages use-case | /vi-tra-sau/nap-game, /tra-gop, /mua-sam, ... | Chưa build | P1 deliverable H1 2026 |
| Merchant pages | /doi-tac/{brand} | Đang triển khai | Cross-sell VTS |
| Microsite Trả Góp | TBD | Chưa build | Simulator + CIC cross-sell |

### 2.2 Baseline Performance (GSC Historical)

| Trang | Clicks | Impressions | CTR | Avg Pos |
|---|---|---|---|---|
| /vi-tra-sau (hub) | 108.879 | 1.564.515 | 6,96% | 7,85 |
| /blog/vi-tra-sau-momo-thanh-toan-duoc-nhung-dich-vu-gi | 128.467 | 736.479 | 17,44% | 9,35 |
| /blog/cham-thanh-toan-vi-tra-sau | 57.724 | 379.561 | 15,21% | 4,41 |
| /blog/rut-tien-tu-vi-tra-sau-momo | 57.420 | 485.753 | 11,82% | 3,46 |
| /uu-dai-vi-tra-sau | 943 | 439.290 | 0,21% | 6,06 |

**Nhận xét:** Hub page có impressions rất cao (1,56M) nhưng CTR thấp (6,96%) và avg position 7,85 - dư địa lớn để cải thiện content relevance + title/description. Trang /uu-dai-vi-tra-sau có 439K impressions nhưng CTR cực thấp (0,21%) - cần xem lại intent alignment.

### 2.3 Market Size & SOV Baseline

| Thị trường | TAM (SV/tháng) | Target Market | SOV Hiện tại | SOV Mục tiêu |
|---|---|---|---|---|
| Trả Sau | 180.000 | 131.580 (73% TAM) | ~54% | Maintain 70% |
| Trả Góp | 200.000 | 81.150 (40% TAM) | ~10% | 40% |
| Tín Dụng | 700.000 | 630.000 (90% TAM) | ~40% | 60% |

*SOV Trả Sau ~54% = brand SoV đã verify (MoMo chiếm 54% brand search cluster). Nguồn: Keyword Research T5/2026.*

### 2.4 Web-to-App Conversion Baseline

| Funnel step | Metric | Baseline |
|---|---|---|
| CTR tới CTA (hub page) | % sessions click CTA | ~7,25% |
| Tỷ lệ scroll đến CTA block (mobile) | % user reach CTA block | ~75-80% reach block, chưa click |
| W2A CVR (end-to-end) | Organic session → Activated VTS | TBD (chờ Appsflyer data) |

### 2.5 Competitive Landscape

VTS cạnh tranh với ZaloPay (Ví Trả Sau ZaloPay), Home Credit, Fundiin trên SERP. MoMo chiếm 54% Brand SOV trong cluster "Trả Sau" - lợi thế brand đã có. Điểm yếu: SOV trong "Trả Góp" và "Tín Dụng" còn thấp, đây là nơi Home Credit và các TCTD có mặt dày hơn.

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi

**User cần credit nhưng không đủ điều kiện ngân hàng - tìm thấy VTS đúng lúc đang search - hiểu ngay không check CIC, duyệt 3 phút - kích hoạt trong app MoMo, thanh toán được ngay.**

Web closes the acquisition loop: từ search intent đến VTS activation mà không cần campaign, không cần sales.

4 outcome phát sinh từ loop này:

**① Adjacent Acquisition:** Intercept 485K SV/tháng Trả Góp + Tín Dụng - nhóm intent cao nhất nhưng VTS đang bỏ ngỏ hoàn toàn.

**② W2A Improvement:** Revamp hub từ 7% → 20% CTA CTR. Traffic đã có - conversion chưa được tối ưu.

**③ GEO/AIO Position:** VTS là nguồn được cite trong AI Overview cho BNPL queries tài chính - maintain TOM khi AI compress traditional SERP.

**④ ORM Flood:** Scale content chính thống cho cluster "rút tiền VTS" - ngăn scam sites chiếm intent này.

### 3.2 Đối Tượng Phục Vụ

- **Segment 1 - Underbanked / No Credit Card:** 18-35 tuổi, không đủ điều kiện mở thẻ tín dụng hoặc nợ xấu, có nhu cầu mua trước trả sau.
- **Segment 2 - Gen Z / Game thủ:** 18-24 tuổi, cần nạp game / mua item gấp khi ví hết tiền.
- **Segment 3 - Household spender:** Người quản lý chi tiêu gia đình, cần thanh toán hóa đơn khi chưa có lương.
- **Segment 4 - Freelancer / Dòng tiền không đều:** Cần hạn mức tín dụng linh hoạt không cần chứng minh thu nhập cố định.

### 3.3 Dự Án Này KHÔNG Phải

- KHÔNG build mobile app feature (thuộc scope Mobile team).
- KHÔNG là media campaign hay paid acquisition (thuộc Media Team).
- KHÔNG cover Vay Nhanh hay VTS B2B / merchant-side - chỉ user-facing organic web.
- KHÔNG build backlink campaign độc lập (Inbound team phối hợp Procurement - track riêng).
- KHÔNG đảm bảo launch sub-pages nếu BU chưa confirm product roadmap cho Trả Góp.
- KHÔNG phải SEO Lead execute trực tiếp - SEO Lead GOVERN (set standard, brief, audit, sign-off).

---

## 4. Phân Tích Thị Trường & Keyword Research

### 4.1 TAM Breakdown - 3 Keyword Markets

**Market 1: Trả Sau (VTS Core)**

| Cluster | Total SV | Ghi chú |
|---|---|---|
| Ví Trả Sau (branded) | 12.100 | Core brand cluster |
| Kích hoạt / Kiểm tra VTS | 810 | High-intent BOFU |
| Rút tiền VTS (negative search) | 6.600 | ORM priority |
| Trả trước trả sau là gì | 450 | Education TOFU |
| **Total addressable** | **~135.290** | |

**Market 2: Trả Góp (Adjacent - intercept)**

| Cluster | Total SV | Intent | Ghi chú |
|---|---|---|---|
| Nợ xấu có mua trả góp được không | 2.680 | MOFU | VTS = giải pháp không check CIC |
| Mua điện thoại trả góp chỉ cần CMND | 1.380 | BOFU | VTS thay thế |
| Phí chuyển đổi trả góp | 3.590 | MOFU | So sánh phí VTS vs thẻ |
| Mua điện thoại trả góp online trả trước 0 đồng | 720 | BOFU | |
| Trả góp VF3/VF5 (xe điện) | 2.300+ | BOFU | |
| **Total addressable** | **~198.560** | | |

**Market 3: Tín Dụng (Pain-point intercept)**

| Cluster | Total SV | Intent | Ghi chú |
|---|---|---|---|
| Dịch vụ rút tiền thẻ tín dụng | 3.600 | Commercial | Pain-point → VTS |
| Rút tiền thẻ tín dụng VPBank | 1.600 | Commercial | |
| Phí thường niên thẻ tín dụng | 590 | Info/Compare | |
| Thẻ ATM là thẻ tín dụng hay ghi nợ | 320 | Info/TOFU | |
| **Total addressable** | **~681.760** | | |

### 4.2 Opportunity Map - Keyword Cluster → URL

| Cluster | SV/tháng | Intent | Target URL | Content angle |
|---|---|---|---|---|
| Kích hoạt / kiểm tra VTS | 810 | Nav/BOFU | /vi-tra-sau | Hướng dẫn kích hoạt từng bước |
| Điện thoại trả góp chỉ cần CMND | 1.380 | Trans/BOFU | /vi-tra-sau/mua-dien-thoai | VTS = giải pháp, không cần thẻ ngân hàng |
| Nợ xấu có mua trả góp được không | 2.680 | Info/MOFU | /vi-tra-sau/mua-dien-thoai | VTS không check CIC - giải pháp khi nợ xấu |
| Phí chuyển đổi trả góp | 3.590 | Info/MOFU | /vi-tra-sau (hub) + Blog | So sánh phí 3% VTS vs phí chuyển đổi thẻ |
| Trả góp qua thẻ tín dụng | 4.860 | Compare/MOFU | /vi-tra-sau (hub) + Blog | VTS vs trả góp thẻ: không cần thủ tục |
| Phí thường niên / phí rút thẻ | 7.760 | Info/TOFU | Blog MOFU | Pain point thẻ → giới thiệu VTS |
| Rút tiền VTS (ORM cluster) | 6.600 | Nav/Transact | Blog ORM | Cảnh báo, educate, driven traffic đúng |
| Mua thẻ game trả sau | TBD | Trans/BOFU | /vi-tra-sau/mua-the-game | "Hết tiền? Nạp ngay, trả sau" |
| Thanh toán hóa đơn điện nước trả sau | TBD | Trans/BOFU | /vi-tra-sau/thanh-toan-hoa-don | "Chưa có lương, trả sau được" |
| Mua vé máy bay trả sau | TBD | Trans/BOFU | /vi-tra-sau/mua-ve-may-bay | "Đặt vé ngay, trả sau" |

---

## 5. JTBD Analysis

### Job #VTS-01 - Urgency Payment

*Search cluster:* "nạp game ví trả sau", "thanh toán điện trả sau momo" - ~1.500-3.000 SV/tháng (cluster gián tiếp)

> "Tôi cần thanh toán ngay bây giờ nhưng ví hết tiền, và tôi không muốn phải xin tiền ai hay bị gián đoạn việc đang làm."

| Dimension | Nội dung |
|---|---|
| Functional | Hoàn thành giao dịch (nạp game/điện/mua đồ) trong dưới 3 phút, không bị block |
| Emotional | Không stress, không xấu hổ, tự giải quyết được vấn đề của mình |
| Social | Không ai biết mình hết tiền - giữ được hình ảnh tự chủ tài chính với bạn bè, team |
| Trigger | Đang chơi game hết tiền - Hóa đơn điện đến hạn - Flash sale sắp hết giờ |
| Search → App | "nạp game hết tiền", "mua thẻ game ví trả sau", "thanh toán điện nước trả sau", "mua thẻ cào điện thoại" → /vi-tra-sau/mua-the-game / /vi-tra-sau/thanh-toan-hoa-don / /vi-tra-sau/nap-data / /vi-tra-sau/mua-the-cao-dien-thoai → CTA "Nạp ngay, trả sau" → App MoMo → VTS activation → Transaction hoàn thành |

**Giải pháp:** /vi-tra-sau/mua-the-game (Garena, Zing, Valorant, Steam Wallet) - /vi-tra-sau/nap-data - /vi-tra-sau/thanh-toan-hoa-don - /vi-tra-sau/mua-the-cao-dien-thoai - CTA "Nạp ngay, trả sau" - Deeplink VTS activation.

---

### Job #VTS-02 - Access Credit

*Search cluster:* "nợ xấu có mua trả góp được không" (390 SV), "mua điện thoại trả góp chỉ cần CMND" (1.000 SV) - ~2.680+ SV/tháng

> "Tôi muốn có hạn mức tín dụng để mua đồ hoặc trả góp, nhưng tôi không đủ điều kiện mở thẻ tín dụng ngân hàng (nợ xấu / không có thu nhập cố định)."

| Dimension | Nội dung |
|---|---|
| Functional | Có hạn mức tín dụng mà không cần CIC, không cần chứng minh thu nhập |
| Emotional | Cảm thấy được "công nhận" tài chính, không bị loại trừ khỏi hệ thống |
| Social | Trông như người có thẻ tín dụng - "mua trước trả sau" là modern, không phải yếu kém |
| Trigger | Bị từ chối mở thẻ ngân hàng - Cần mua điện thoại nhưng nợ xấu |
| Search → App | "nợ xấu có mua trả góp được không", "mua điện thoại trả góp chỉ cần CMND", "mua hàng online không cần thẻ tín dụng" → /vi-tra-sau/mua-dien-thoai → Copy "Không check CIC, duyệt 3 phút" → App MoMo → VTS activation |

**Giải pháp:** /vi-tra-sau/mua-dien-thoai (anchor use-case cho Underbanked) - /vi-tra-sau/thanh-toan-sieu-thi - Blog MOFU "nợ xấu + VTS" - Copy: "Không check CIC, duyệt trong 3 phút".

---

### Job #VTS-03 - Compare & Decide

*Search cluster:* "phí chuyển đổi trả góp" (3.590 SV), "trả góp qua thẻ tín dụng là gì" (4.860 SV) - ~9.000+ SV/tháng

> "Tôi đang cân nhắc giữa trả góp qua thẻ tín dụng và một giải pháp khác - tôi cần biết thực sự cái nào rẻ hơn và ít thủ tục hơn."

| Dimension | Nội dung |
|---|---|
| Functional | So sánh được phí/lãi/điều kiện giữa các giải pháp, ra quyết định nhanh |
| Emotional | An tâm rằng mình đang chọn lựa thông minh, không bị lừa bởi "0% lãi suất" ẩn phí |
| Social | Là người tiêu dùng thông minh, biết quản lý tài chính - kể lại cho bạn bè "dùng VTS không mất phí thường niên" |
| Trigger | Thấy quảng cáo "trả góp 0% lãi" nhưng nghi ngờ - Đang so sánh trước khi mua đồ lớn |
| Search → App | "phí chuyển đổi trả góp", "trả góp thẻ tín dụng phí bao nhiêu", "phí thường niên thẻ tín dụng" → /vi-tra-sau (hub - comparison section) / Blog so sánh → So sánh VTS vs thẻ + CTA → App MoMo → VTS activation |

**Giải pháp:** /vi-tra-sau hub (comparison section) - /vi-tra-sau/mua-dien-thoai (highest ticket use-case) - Blog: "VTS vs thẻ tín dụng: so sánh thực tế".

---

### Job #VTS-04 - Negative Search / ORM

*Search cluster:* "rút ví trả sau MoMo" (6.600 SV), top blog "rút tiền từ ví trả sau MoMo" đạt 57.420 clicks

> "Tôi nghe nói có thể rút tiền mặt từ Ví Trả Sau, hoặc thấy quảng cáo đó - tôi muốn kiểm tra xem có thật không."

| Dimension | Nội dung |
|---|---|
| Functional | Tìm hiểu xem rút tiền VTS có được không, tránh bị lừa đảo |
| Emotional | Lo ngại, không chắc - cần được reassure bởi nguồn chính thống của MoMo |
| Social | Bạn bè hỏi hoặc thấy người khác chia sẻ link "dịch vụ rút VTS" - muốn biết thật hay lừa trước khi forward |
| Trigger | Thấy quảng cáo "dịch vụ rút tiền VTS" trên mạng - Bạn bè gửi link hỏi |
| Search → App | "rút tiền ví trả sau momo có được không", "dịch vụ rút ví trả sau" → Blog ORM "Sự thật + cảnh báo lừa đảo" → FAQ schema → Reassure + giới thiệu các use-case hợp lệ của VTS → App MoMo |

**Giải pháp:** Blog ORM: "Rút tiền từ VTS có được không? - Sự thật + cảnh báo lừa đảo" - FAQ schema - AIO citation.

---

## 6. Kiến Trúc & Scope Build

### 6.1 URL Architecture VTS

| URL | Content Type | Mục tiêu |
|---|---|---|
| /vi-tra-sau | Hub - Pillar page | Brand anchor, intercept tất cả jobs, comparison section |
| /vi-tra-sau/mua-dien-thoai | Sub-page use-case | Job #1, #2 - Anchor cho Underbanked + Compare |
| /vi-tra-sau/mua-the-cao-dien-thoai | Sub-page use-case | Job #1 - Nạp thẻ cào khẩn cấp |
| /vi-tra-sau/nap-data/{nha-mang} | Sub-page use-case (per nhà mạng) | Job #1 - Nạp data, hết gói giữa tháng |
| /vi-tra-sau/mua-the-game | Sub-page use-case | Job #1 - Garena, Zing, Valorant, Steam Wallet |
| /vi-tra-sau/thanh-toan-xang-dau | Sub-page use-case | Job #1 - Đổ xăng, thiếu tiền mặt |
| /vi-tra-sau/thanh-toan-nha-hang | Sub-page + Merchant list | Job #1 - Ăn nhà hàng, thanh toán sau |
| /vi-tra-sau/dat-do-an | Sub-page use-case | Job #1 - GrabFood, ShopeeFood, Baemin |
| /vi-tra-sau/thanh-toan-sieu-thi | Sub-page + Merchant list | Job #2 - WinMart, CoopMart, BigC |
| /vi-tra-sau/mua-ve-may-bay | Sub-page use-case | Job #2 - Du lịch, công tác chưa đủ tiền |
| /vi-tra-sau/thanh-toan-hoa-don | Sub-page use-case | Job #1 - Điện, Nước, Internet chưa có lương |
| /blog/ (cluster VTS) | Blog TOFU/MOFU | Job #2, #3, #4 - Intercept adjacent intent |
| /hoi-dap/ (VTS) | FAQ schema | AIO citation + rich snippets |
| /vi-tra-sau/llms.txt | AEO/GEO Standard | Chuẩn hóa AI Indexing (Bắt buộc theo chuẩn VP GPD) |

### 6.2 Scope Build - Core Deliverables

| Deliverable | Mô tả | Mục tiêu |
|---|---|---|
| Revamp /vi-tra-sau hub | UI mới: highlight use-cases rõ (10 categories); Social proof (số user, đối tác brands); Comparison section VTS vs thẻ; Sticky CTA bar trên mobile; FAQPage schema | CTR CTA tăng từ 7% → 20% |
| **PLG Interactive Tool** | **VTS Installment Simulator (Trình giả lập trả góp):** User nhập số tiền cần vay → Kéo slider chọn kỳ hạn (1-12 tháng) → Tool tự động tính chính xác số tiền trả mỗi tháng (hiển thị phí ẩn nếu có minh bạch 100%). | Tạo "Aha Moment", thuyết phục W2A ngay lập tức (CEO & VP GPD standard) |
| Sub-pages × 10 | Build 10 use-case pages theo nhóm sản phẩm: **Thẻ & Data** (mua-the-game, mua-the-cao-dien-thoai, nap-data) - **Ẩm thực** (thanh-toan-nha-hang + merchant list, dat-do-an) - **Mua sắm** (mua-dien-thoai, thanh-toan-sieu-thi + merchant list) - **Di chuyển** (mua-ve-may-bay, thanh-toan-xang-dau) - **Hóa đơn** (thanh-toan-hoa-don). Mỗi trang có deeplink VTS activation | Intercept adjacent intent theo use-case cụ thể |
| OneLink deeplink per use-case | Deep link từ mỗi sub-page → app → đúng merchant/service flow | Track W2A attribution per use-case |
| FAQPage schema | Toàn bộ trang /hoi-dap/ VTS + hub page | Rich snippets + AIO citation |
| Blog ORM refresh | Update blog "rút tiền VTS" - cảnh báo lừa đảo rõ, hero heading negative signal | SERP flood + AIO |
| Blog scale 20-30 bài | Cluster Tín Dụng pain points + Trả Góp adjacent + Use-case guides per sub-page | Intercept Market 2 & 3 |

**Technical gate bắt buộc:** Tất cả trang VTS phải đạt LCP ≤ 2,5s trên mobile; CTA above fold trên 375px viewport. MoSpark SEO/GEO Scoring Gate >80 điểm - hard block nếu fail.

### 6.3 Content Governance

| Content type | Intent | Owner | Gate |
|---|---|---|---|
| Blog VTS (How-to, Tips, Giải thích) | Informational | Inbound team execute | SEO Lead sign-off pre-publish |
| Sub-pages LP (/nap-game, /tra-gop...) | Transactional / Navigational | SEO Lead own, Web Platform build | SEO Lead sign-off |
| FAQ / Hỏi đáp | Mixed | SEO Lead brief, Web Platform update | SEO Lead sign-off |
| Merchant Pages | Navigational + Commercial | SEO Lead brief, Inbound + BU produce | SEO Lead audit final |

**Rule cứng: Inbound KHÔNG làm việc trực tiếp với Web Platform. Mọi technical request đi qua SEO Lead trước khi vào Web Platform.**

---

## 7. Success Metrics

### 7.1 North Star Metric

**Activated VTS Users from Web** - Số user lần đầu kích hoạt Ví Trả Sau trong app MoMo, có nguồn gốc từ organic web (momo.vn/vi-tra-sau và sub-pages), trong vòng 7 ngày kể từ lần đầu visit.

Baseline: TBD | Target: 500 activated users/tháng vào tháng 6/2026

### 7.2 Organic Traffic (GSC)

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| Organic sessions - VTS cluster | ~25K sessions/tháng | 75K sessions/tháng (+200%) | Oct 2026 (90 ngày post-launch) | GSC + GA4 |
| Avg position - VTS branded kw | 7,85 (hub page) | ≤ 5 | Oct 2026 | GSC |
| SOV - Thị trường Trả Sau | ~54% SOV | 75% SOV | Dec 2026 | SEO tool |
| SOV - Thị trường Trả Góp | ~10% SOV | 40% SOV | Dec 2026 | SEO tool |
| SOV - Thị trường Tín Dụng | ~40% SOV | 60% SOV | Dec 2026 | SEO tool |

**Target logic:** SEO channel cần deliver 25.188 sessions/tháng để contribute 403 MAU/tháng (W2A 8% tham khảo, in-app CR 20% tham khảo - cần verify bằng Appsflyer trước khi dùng làm commitment). SOV target: Trả Sau 75%, Trả Góp 40%, Tín Dụng 60%. SOV Trả Góp 40% là aspirational - cần milestone check Aug 2026 để assess lại nếu Inbound execution bị chậm.

### 7.3 Web-to-App Conversion

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| CTR tới CTA (/vi-tra-sau hub) | ~7,25% | ≥ 15% (threshold) → ≥ 20% (stretch) | Oct 2026 (90 ngày post-revamp) | GA4: cta_click event |
| Onelink click → Install % | TBD | ≥ 30% | Oct 2026 | Appsflyer |
| W2A end-to-end CVR | **Chưa có baseline** - establish Q2/2026 | Set target sau khi có baseline (Q3 review) | Dec 2026 | GA4 + Appsflyer |
| Scroll depth mobile (hub) | ~75-80% reach block, không click | ≥ 85% reach + click | Oct 2026 (post-revamp) | Heatmap tool |

### 7.4 Mandatory Tracking & AB Test Hypothesis (MoSpark Standard)
- **Hypothesis (Giả thuyết test):** Nếu đặt "VTS Installment Simulator" (Máy tính trả góp) ở màn hình đầu tiên (First Fold) thay cho banner quảng cáo tĩnh, tỷ lệ CTR tới CTA W2A sẽ tăng ít nhất 50% vì user trực tiếp thấy được quyền lợi tài chính của mình (Utility-first).
- **Tracking Event Schema:** Gắn sự kiện trên GA4 & Appsflyer cho mọi tương tác: `vts_slider_drag` (Kéo slider chọn tiền), `vts_term_select` (Chọn kỳ hạn), `vts_cta_click` (Click nút Trả góp ngay).

### 7.4 Ranking & GEO

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| Keywords top 10 - Trả Sau cluster | TBD | ≥ 70% of 550 target kw | Dec 2026 | SEO tool |
| Keywords top 10 - Trả Góp cluster | TBD | ≥ 50% of 269 target kw | Dec 2026 | SEO tool |
| AIO citation - VTS | TBD | ≥ 10 queries | Jun 2026 | GSC AIO filter + manual audit |

---

## 8. Dependencies & Constraints

### 8.1 Go-to-Market: SPA Framework (Service Productization)
- **reSearch / Strategy:** Đã hoàn tất phân tích Keyword cluster (Trả sau, Trả góp, Tín dụng) với tổng volume ~900K SV/tháng.
- **Pilot / Plan (T6/2026):** Revamp Hub `/vi-tra-sau` + Build VTS Installment Simulator + 10 Sub-pages.
- **Action / Amplify (Q3/2026):** SEO Lead cùng VP GPD pitch BU VTS để commit ngân sách scale 20-30 bài blog đánh chiếm SOV Tín Dụng & Trả Góp.

### 8.2 Operational Constraints

| Dependency | Mô tả | Blocker? | Status |
|---|---|---|---|
| BU VTS - Product roadmap Trả Góp | Confirm sản phẩm Trả Góp có expand không → điều kiện để build /tra-gop đúng insight | Yes | Cần confirm |
| BU VTS - Formula Simulator Trả Góp | Cung cấp công thức tính phí/kỳ hạn chính xác cho Simulator | Yes | Pending |
| Web Platform - Build hub + sub-pages | Revamp /vi-tra-sau + 4 sub-pages + Simulator. Inbound KHÔNG contact trực tiếp Web Platform | Yes | Pending align |
| Web Platform - Merchant Pages VTS | Build Admin Panel + Merchant page template với VTS cross-sell widget | No | Active |
| DA Team - GA4 events + Appsflyer | Setup GA4 event tracking (cta_click, scroll, onelink); map Appsflyer VTS activation | Yes | Cần setup trước launch |
| Inbound team - Blog 20-30 bài | Viết theo keyword brief từ SEO Lead, qua BU/Legal duyệt, SEO Lead audit trước publish | No | Phụ thuộc capacity + Legal SLA |
| BU/Legal - Duyệt content YMYL | Duyệt nội dung tài chính/YMYL trước publish. Cần SLA rõ (5-7 ngày/bài) | Yes | Chưa có SLA |
| MKT Team - Campaign message | Cung cấp thông điệp campaign VTS 2026 (value prop, CTA copy) để align với blog + LP | No | Cần input trước khi brief content |
| MoSpark SEO/GEO Scoring Gate | Pre-publish gate phải active trên MoSpark. BRD v1.1 done - chờ implementation | No | Pending Dev |
| Backlink campaign | Booking 100-150 backlinks (partner + paid); SEO Lead set standard, Inbound/Agency execute | No | Pitching Q2 2026 |

**Constraints:**
- Mọi content tài chính phải qua Legal review trước publish (YMYL compliance).
- Inbound không làm việc trực tiếp với Web Platform - mọi request kỹ thuật phải qua SEO Lead.
- Agency chạy qua Inbound review trước khi SEO Lead audit final.
- URL structure giữ nguyên momo.vn - không thay đổi domain/subdomain.

---

## Appendix A: KPI Model - SEO Channel Contribution

| Channel | Target Traffic/tháng | W2A CR | Traffic to App | In-App CR | MAU contribution |
|---|---|---|---|---|---|
| SEO | 25.188 sessions | 8% | 2.015 | 20% | 403 MAU |
| SEM | 4.000 sessions | 8% | 320 | 20% | 64 MAU |
| **Total** | **29.188** | | **2.335** | | **467 MAU** |

SEO channel cần đóng góp ~87% total search traffic. Model này dùng W2A CR 8% và in-app CR 20% làm **reference benchmark** - không phải verified baseline. Appsflyer attribution chưa được setup (xem Dependencies), vì vậy 403 MAU/tháng là con số định hướng cho sizing, không phải commitment. Target MAU sẽ được recalibrate sau khi có baseline thực từ Appsflyer (dự kiến Q3/2026).

---

## Change Log

- **Tháng 5/2026 (v1.6):** Recalibrate Success Metrics: đổi timeframe Jun 2026 → Oct 2026 cho traffic và CTA targets; thêm threshold/stretch cho CTR; W2A CVR không commit target khi chưa có baseline; SOV Tín Dụng thống nhất 60% (sửa inconsistency Section 2.3 vs 7.2); ghi rõ W2A 8% trong Appendix A là reference benchmark.
- **Tháng 5/2026 (v1.5):** Cập nhật URL Architecture theo 10 sub-pages thực tế được build (thay thế scope 4 sub-pages cũ). Update Opportunity Map, JTBD Giải pháp references, Scope Build table.
- **Tháng 5/2026 (v1.4):** Apply CEO BRD Standard: Thêm Problem Statement block, rewrite Situation theo user-centric, thêm Product Job Cốt Lõi (Section 3.1), thêm Search → App vào tất cả 4 JTBD, thêm Social vào VTS-04. Xóa Section 9 Risk Assessment. Xóa Section 6.2 Content Matrix. Xóa Appendix B Dữ Liệu Cần Verify. Chuẩn hóa section headers và dấu gạch ngang.
- **Tháng 5/2026 (v1.3):** Chuẩn hóa tài liệu - loại bỏ liên kết nội bộ, thông tin vận hành, tên nhân sự; chuẩn bị cho Head of BU / C-Level review.
- **Tháng 5/2026 (v1.2):** Bổ sung market data, JTBD, competitive landscape, dependencies.
- **Tháng 5/2026 (v1.0):** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.
