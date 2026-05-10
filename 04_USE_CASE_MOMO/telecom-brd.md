# 📄 Telecom Brd
Case Viễn Thông — Out-App Traffic (SEO/GEO Project)

> **Project:** MoMo Telecom Growth — Sim Số Đẹp · Nạp Data · eSIM Du Lịch · Nạp Tiền ĐT
> **Main URL:** momo.vn/vien-thong (hub) · /sim-so-dep · /nap-data · /esim-du-lich · /nap-tien-dien-thoai
> **Division:** PS (Payment Services)
> **Use Case:** Telco
> **Product:** PS - Telco
> **SEO/GEO Project ID:** `vien-thong`
> **Owner:** Klaus Bot 3 — SEO & GEO Lead, Out-App Traffic Team
> **Governance:** Văn Hiến (SEO & GEO Lead)
> **Timeline:** Q1/2026 (roll-out) → Q4/2026 (full scale)
> **Version:** 1.1 · Tháng 4/2026
> **Status:** Draft - Division/Product Metadata

---

## 1. Executive Summary

**Situation:** Thị trường viễn thông Việt Nam có tổng 6 nhà mạng, với tổng search demand ước tính 500K–800K searches/tháng cho các nhóm từ khóa liên quan đến sim số đẹp, gói data, eSIM và nạp tiền điện thoại [cần verify — GSC + Ahrefs]. MoMo hiện đã có tính năng nạp tiền điện thoại với traffic organic ổn định (~30,000 sessions/tháng ước tính), nhưng 3 sản phẩm còn lại — Sim Số Đẹp, Nạp Data, eSIM Du Lịch — chưa có web presence đủ mạnh để capture organic demand.

**Complication:** Đối thủ như Thế Giới Di Động đã xây dựng hệ thống landing page gói cước (`thegioididong.com/goi-cuoc/`) và sim phong thủy có độ phủ sóng từ khóa rộng. MoMo hiện rank yếu hoặc không rank cho các nhóm từ khóa có volume cao như "sim số đẹp hợp tuổi [năm sinh]" (~2,000–5,000 searches/tháng per năm), "gói data [nhà mạng]" (~10,000–15,000 searches/tháng per nhà mạng), và "esim du lịch [quốc gia]" (~1,000–5,000 per nước hot). Điều này đồng nghĩa với việc MoMo đang bỏ lỡ một lượng intent cao và CAC = 0 từ organic channel.

**Resolution:** Use Case Viễn Thông xây dựng hệ thống web content gồm: (1) Hub `/vien-thong` làm trang trung tâm điều phối 4 sản phẩm; (2) Sitemap 3 tầng cho từng sản phẩm; (3) pSEO engine tạo 10,000+ trang sim phong thủy và 330+ trang gói cước; (4) eSIM landing cho 200+ quốc gia; (5) Blog Embed components để tối ưu conversion từ content. Mục tiêu EOY 2026: tổng 270,000+ organic sessions/tháng và establish MoMo là top-of-mind cho telecom transactions online tại Việt Nam.

---

## 2. Bối Cảnh Hiện Tại

### 2.1 Hiện trạng sản phẩm

| Sản phẩm | URL | Trạng thái web hiện tại | Organic traffic ước tính | Ghi chú |
|---|---|---|---|---|
| Nạp Tiền ĐT | momo.vn/nap-tien-dien-thoai | Đã có, ranking tốt nhóm branded | ~30,000 sessions/tháng [cần verify GSC] | Sản phẩm trưởng thành nhất |
| Sim Số Đẹp | momo.vn/sim-so-dep | Có landing cơ bản, thiếu pSEO | ~5,000 sessions/tháng [cần verify] | Tiềm năng pSEO cực lớn |
| Nạp Data | momo.vn/nap-data | Có, thiếu landing từng gói | ~8,000 sessions/tháng [cần verify] | TGDD đang dominate |
| eSIM Du Lịch | momo.vn/esim-du-lich | Chưa có / mới | ~2,000 sessions/tháng [cần verify] | New product — ramp-up phase |

### 2.2 Search Demand Landscape

| Nhóm từ khóa | Ví dụ keyword | Volume ước tính | Intent | Competitor ranking |
|---|---|---|---|---|
| Sim phong thủy × năm sinh | "sim số đẹp hợp tuổi 1990" | 2,000–5,000/tháng per năm × 50 năm = ~150K total | Buy | Các site phong thủy, TGDD |
| Sim phong thủy × tên | "sim hợp tên Minh", "sim tên Lan" | ~500K/tháng total (5,000 tên) | Buy | Yếu — cơ hội cho MoMo |
| Gói data nhà mạng | "gói data Viettel", "gói D90N" | ~15K/tháng per nhà mạng | Buy | TGDD rank #1–3 |
| eSIM quốc gia | "esim Nhật Bản", "esim Hàn Quốc" | ~3,000–8,000/tháng per nước hot | Buy | Esimdb, eSIM providers nước ngoài |
| Nạp tiền branded | "nạp tiền điện thoại qua MoMo" | ~20,000/tháng | Go | MoMo đang rank tốt |
| So sánh / hướng dẫn | "cách chọn sim hợp phong thủy" | ~5,000–10,000/tháng | Know | Blog site, TGDD |

*Tất cả số liệu là ước tính từ keyword research — cần validate bằng Ahrefs/SEMrush + GSC trước Q1 launch.*

### 2.3 Phân tích cạnh tranh

| Đối thủ | Điểm mạnh | Điểm yếu | MoMo advantage |
|---|---|---|---|
| Thế Giới Di Động | Domain authority cao, phủ sóng rộng gói cước + sim | Không có payment app tích hợp, không có phong thủy AI | MoMo Pay ecosystem, AI giải luận personalized |
| Các site sim phong thủy | Content depth về phong thủy, UX đơn giản | Không bán được sim online, không có nhà mạng filter | MoMo có thể bán trực tiếp — zero friction |
| eSIM providers quốc tế | Phủ sóng toàn cầu | Không có tiếng Việt tốt, không có local payment | MoMo Pay + tiếng Việt native |
| Nhà mạng (Viettel, Mobi, Vina) | Brand awareness | Web UX kém, không aggregate cross-carrier | MoMo là neutral aggregator — so sánh được |

---

## 3. Định Hướng Dự Án

**Dự án này phục vụ điều gì?**
Xây dựng organic acquisition engine cho 4 sản phẩm viễn thông của MoMo, giảm CAC và tăng số lượng user thực hiện giao dịch viễn thông qua MoMo (Nạp tiền, Mua gói data, Mua sim, Mua eSIM). North Star Metric: **Organic sessions → Web-to-App conversion**.

**Ai được phục vụ?**

| Segment | Nhu cầu chính | Sản phẩm liên quan |
|---|---|---|
| Người Việt 25–45 tuổi, quan tâm phong thủy | Chọn sim hợp mệnh/năm sinh | Sim Số Đẹp |
| Người dùng smartphone muốn tiết kiệm | Tìm gói data value nhất | Nạp Data |
| Du khách / người đi công tác nước ngoài | Internet khi hạ cánh, không lo roaming | eSIM Du Lịch |
| Tất cả người dùng điện thoại di động | Nạp tiền nhanh, 24/7 | Nạp Tiền ĐT |

**Dự án này KHÔNG phải là gì:**
- KHÔNG build mobile app feature (trách nhiệm của Mobile Team)
- KHÔNG quản lý inventory sim (trách nhiệm của Cellteam / nhà mạng partner)
- KHÔNG làm CRM / retention cho user đã mua (ngoài scope Out-App Traffic)
- KHÔNG cover nạp tiền điện thoại bàn (landline)
- KHÔNG build tính năng so sánh nhà mạng theo phong cách telco aggregator đầy đủ (defer sang phase 2)

---

## 4. Phạm Vi Dự Án (Scope)

### 4.1 In Scope — P1 (Launch Blockers)

| Item | Mô tả | URL | Owner |
|---|---|---|---|
| Telecom Hub | Trang tổng quan điều phối 4 sản phẩm, 10-section anatomy | momo.vn/vien-thong | SEO Lead + Dev |
| Sim hub + 6 nhà mạng | Trang cha sim + 6 landing nhà mạng | /sim-so-dep · /sim-so-dep/[nha-mang] | SEO Lead + Content |
| 8 trang phong thủy loại | Thần tài, lộc phát, tứ quý, ngũ quý, liên hoa, tam hoa... | /sim-so-dep/phong-thuy/[loai] | SEO Lead + Content |
| Nạp Data hub + 6 nhà mạng | Trang cha + landing 6 nhà mạng với bảng gói đầy đủ | /nap-data · /nap-data/[nha-mang] | SEO Lead + Dev |
| eSIM hub + 20 quốc gia P1 | Trang cha eSIM + 20 quốc gia có demand cao nhất (JP, KR, TH, SG, US...) | /esim-du-lich · /khu-vuc/[quoc-gia] | SEO Lead + Content |
| Nạp Tiền hub + 6 nhà mạng | Rebuild/optimize trang hiện tại, thêm 6 trang nhà mạng | /nap-tien-dien-thoai · /[nha-mang] | SEO Lead + Dev |
| Schema markup toàn bộ | FAQPage, HowTo, Product, ItemList, BreadcrumbList | Tất cả trang P1 | Tech SEO + Dev |
| GA4 event tracking | embed_view, embed_interact, embed_convert, purchase flow | GTM | DA Team + Dev |
| Blog embed components (6 loại) | C-SIM-01/02, C-DATA-01/02, C-ESIM-01, C-NAP-01 | momo.vn/blog (nhúng vào) | Dev + SEO Lead |

### 4.2 In Scope — P2 (Launch + Scale)

| Item | Mô tả | Timeline |
|---|---|---|
| pSEO sim phong thủy × tên (500 trang batch 1) | Template tên × mệnh × nhà mạng, AI giải luận | Q2/2026 |
| pSEO sim phong thủy × năm sinh (100 trang) | Template năm sinh × mệnh × nhà mạng | Q2/2026 |
| pSEO gói cước (Batch 1 — 100 gói Viettel + 60 Mobi + 40 Vina) | Landing từng gói: /nap-data/[nha-mang]/[ten-goi] | Q2/2026 |
| eSIM mở rộng 100 quốc gia | Priority 2 countries | Q2/2026 |
| Blog content (20 bài TOFU) | momo.vn/blog — sim phong thủy, gói data, eSIM guide | Q1–Q2/2026 |
| Cross-sell engine: telecom → BH du lịch | Sau mua eSIM → offer BH du lịch pre-filled | Q3/2026 |

### 4.3 In Scope — P3 (Optimize & Dominate)

| Item | Timeline |
|---|---|
| pSEO sim 5,000 trang | Q3/2026 |
| pSEO sim 10,000 trang (full scale) | Q4/2026 |
| pSEO gói cước full 330 trang | Q3–Q4/2026 |
| eSIM 200 quốc gia hoàn chỉnh | Q3/2026 |
| AI chatbot tư vấn sim phong thủy | Q3/2026 |
| Review system cho sim + eSIM (AggregateRating schema) | Q3/2026 |
| eSIM Travel Planner AI itinerary | Q4/2026 |
| Loyalty hub — MoMo Điểm telecom | Q4/2026 |

---

## 5. JTBD Analysis (Keyword-Driven)

### Job #SIM-01 — Chọn sim hợp phong thủy

**Search Intent Cluster:** "sim số đẹp hợp tuổi 1990", "sim hợp mệnh thổ", "sim phong thủy năm sinh", "sim thần tài", "sim số đẹp năm Canh Ngọ"
**Volume:** ~150,000 searches/tháng tổng cộng (50 năm × 2,000–5,000/tháng) [cần verify Ahrefs]

> "Tôi cần chọn số điện thoại mới, nhưng không muốn dùng số bừa bãi — tôi muốn số hợp với mệnh, tuổi của mình để mang may mắn."

| Dimension | Nội dung |
|---|---|
| Functional | Tìm được sim có đuôi số hợp mệnh/năm sinh, mua online không cần ra đại lý |
| Emotional | An tâm đã chọn đúng, không lo dùng số "xấu" ảnh hưởng công việc, sức khỏe |
| Social | Người thân/đối tác thấy mình chỉn chu, am hiểu phong thủy |
| Trigger moment | Mua sim mới · Khai trương kinh doanh · Đầu năm mới · Chuyển mạng |
| Content implication | pSEO trang năm sinh × mệnh × nhà mạng · AI Giải Luận widget · Badge "Hợp mệnh [X]" |
| CTA | "Xem sim phù hợp với tuổi [năm sinh] của bạn →" |

---

### Job #SIM-02 — Tặng sim số đẹp làm quà

**Search Intent Cluster:** "sim số đẹp tặng sinh nhật", "mua sim tặng khai trương", "sim đẹp tặng người tuổi [X]"
**Volume:** ~10,000–20,000 searches/tháng [cần verify]

> "Tôi muốn tặng một thứ gì đó ý nghĩa hơn phong bì tiền — sim số đẹp hợp tuổi người được tặng là quà độc đáo và thiết thực."

| Dimension | Nội dung |
|---|---|
| Functional | Nhập năm sinh người được tặng → AI gợi ý sim phù hợp → mua và giao nhận đúng dịp |
| Emotional | Cảm thấy đã chuẩn bị chu đáo, quà có ý nghĩa thay vì mua đại |
| Social | Người nhận cảm nhận được sự quan tâm cá nhân hóa |
| Trigger moment | Sinh nhật · Tết · Khai trương · Ra trường · Đám cưới |
| Content implication | Landing /sim-so-dep/tang-sim-so-dep · Widget nhập năm sinh người được tặng · Cross-sell gói data combo |

---

### Job #SIM-03 — Số điện thoại kinh doanh đẹp, dễ nhớ

**Search Intent Cluster:** "sim kinh doanh đẹp", "sim hotline đẹp", "sim số lặp cho doanh nghiệp", "sim đuôi 168 888"
**Volume:** ~15,000–25,000 searches/tháng [cần verify]

> "Số điện thoại là bộ mặt của doanh nghiệp — tôi cần số dễ nhớ, in được lên danh thiếp, và hợp phong thủy kinh doanh."

| Dimension | Nội dung |
|---|---|
| Functional | Filter được sim theo pattern (đuôi lặp, số đẹp), chọn nhà mạng, giá range |
| Emotional | Tự tin khi đưa số cho khách, cảm giác chuyên nghiệp |
| Social | Khách hàng nhớ ngay số, thấy chủ doanh nghiệp đầu tư nghiêm túc |
| Trigger moment | Mở cơ sở mới · Rebranding · Đổi số hotline |
| Content implication | Landing /sim-so-dep/sim-kinh-doanh · Premium tier sim 2–50 triệu · Blog sim hotline theo ngành |

---

### Job #DATA-01 — Đăng ký gói data khẩn cấp

**Search Intent Cluster:** "đăng ký gói data Viettel", "mua gói 4G nhanh", "gói D90N là gì", "hết data mua gói nào"
**Volume:** ~40,000–60,000 searches/tháng tổng [cần verify]

> "Điện thoại vừa thông báo hết data — tôi cần đăng ký gói ngay, nhanh nhất có thể, không muốn bị gián đoạn."

| Dimension | Nội dung |
|---|---|
| Functional | Đăng ký gói trong 3 bước, thanh toán ví MoMo sẵn có, kích hoạt tức thì |
| Emotional | Không bị "chết internet" giữa chừng, không cần nhờ ai hay tìm wifi |
| Social | Vẫn available với công việc và mọi người xung quanh |
| Trigger moment | Thông báo hết data · Mạng chậm đột ngột · Cuối tháng |
| Content implication | pSEO landing /nap-data/[nha-mang]/[ten-goi] rank #1 · Speed là ưu tiên #1 · "Kích hoạt tức thì" badge |

---

### Job #DATA-02 — So sánh và chọn gói data value nhất

**Search Intent Cluster:** "gói data Viettel tốt nhất 2026", "so sánh gói data 100k", "gói nào rẻ nhất tháng này"
**Volume:** ~20,000–30,000 searches/tháng [cần verify]

> "Tôi muốn biết mình đang trả tiền có đáng không — gói nào cho nhiều GB nhất với giá tốt nhất trong tháng này."

| Dimension | Nội dung |
|---|---|
| Functional | So sánh được tất cả gói của nhà mạng mình, hiểu rõ data/ngày và tổng data |
| Emotional | Tự tin đã chọn gói "value nhất", không bị cảm giác bị thiệt |
| Social | Recommend được gói tốt cho bạn bè/đồng nghiệp — người "biết chỗ hay" |
| Trigger moment | Gói hết hiệu lực · Review chi phí hàng tháng · Thấy quảng cáo gói mới |
| Content implication | Trang nhà mạng: bảng đầy đủ + filter · Badge "Best Value" · C-DATA-02 embed trong blog so sánh |

---

### Job #ESIM-01 — Internet ngay khi hạ cánh nước ngoài

**Search Intent Cluster:** "esim nhật bản", "mua esim đi nhật", "esim du lịch giá rẻ", "sim data khi đi nước ngoài"
**Volume:** ~50,000–80,000 searches/tháng tổng (20 nước × 2,000–5,000) [cần verify]

> "Tôi muốn có internet ngay khi vừa hạ cánh — không phải xếp hàng ở sân bay, không lo bị mất liên lạc với gia đình."

| Dimension | Nội dung |
|---|---|
| Functional | Mua và cài eSIM trước khi đi, đến nơi chỉ bật lên là có mạng ngay |
| Emotional | An tâm hoàn toàn — không "tối tăm" khi vừa đến nơi lạ |
| Social | Update được ngay cho gia đình biết đã đến an toàn |
| Trigger moment | Mua vé máy bay · 1–2 tuần trước chuyến đi · Check-in online |
| Content implication | Hero copy "Internet ngay khi hạ cánh" · Hướng dẫn cài trước khi đi · Trust signal "X khách đã dùng eSIM [nước]" |

---

### Job #ESIM-02 — Tránh sốc hóa đơn roaming

**Search Intent Cluster:** "roaming vs esim", "esim có rẻ hơn roaming không", "cách tiết kiệm data khi đi nước ngoài"
**Volume:** ~15,000–25,000 searches/tháng [cần verify]

> "Lần trước tôi về nước mới biết bill roaming đến vài triệu — lần này tôi muốn biết trước sẽ trả bao nhiêu, không có phí ẩn."

| Dimension | Nội dung |
|---|---|
| Functional | Giá cố định đã biết trước, không có phí ẩn hay cước roaming bất ngờ |
| Emotional | Dùng internet thoải mái không phải dè xẻn, không lo về con số hóa đơn |
| Social | Chia sẻ được ảnh/video real-time cho bạn bè không cần đợi về nhà |
| Trigger moment | Đã từng bị bill roaming cao · Chuẩn bị cho chuyến đi dài ngày |
| Content implication | So sánh eSIM MoMo vs roaming Viettel/Mobi · Calculator tiết kiệm · Blog "Roaming vs eSIM — nên chọn gì?" |

---

### Job #NAP-01 — Nạp tiền điện thoại khẩn cấp

**Search Intent Cluster:** "nạp tiền điện thoại online", "nạp tiền Viettel nhanh", "nạp tiền MoMo"
**Volume:** ~50,000–80,000 searches/tháng [cần verify — sản phẩm đã có baseline tốt]

> "Điện thoại vừa báo sắp hết tiền — tôi cần nạp ngay trước khi bị cắt cuộc gọi giữa chừng."

| Dimension | Nội dung |
|---|---|
| Functional | Nạp trong 10 giây, nhận xác nhận ngay, 24/7 không cần ra cửa hàng |
| Emotional | Không lo bị cắt cuộc gọi quan trọng, không cần dè xẻn từng tin nhắn |
| Social | Luôn available cho gia đình, đồng nghiệp, khách hàng |
| Trigger moment | SMS "tài khoản sắp hết" · Cuộc gọi bị ngắt · Cuối tháng |
| Content implication | Form nạp above-the-fold · "Nạp trong 5 giây" badge · Auto-detect nhà mạng từ đầu số |

---

## 6. Yêu Cầu Tính Năng (Feature Requirements)

### 6.1 Core Web Infrastructure

| # | Feature | Mô tả | Priority | Owner |
|---|---|---|---|---|
| F-01 | Telecom Hub `/vien-thong` | 10-section hub page: hero, stats, product grid, quick actions, operator strip, phong thủy widget, trust, cross-sell, FAQ, internal links | P1 | Dev + SEO |
| F-02 | Sim hub + filter engine | Bộ lọc sim theo nhà mạng / phong thủy / mệnh / giá. Sort: mới nhất / giá tăng / giá giảm / phổ biến | P1 | Dev |
| F-03 | AI Giải Luận Widget | Input: tên + năm sinh (+ tùy chọn giờ sinh) → AI 5-layer logic → Output: mệnh + số cát + gợi ý 3 sim + giải thích 200+ chữ unique | P1 | Dev + AI Team |
| F-04 | Data gói cước engine | Bảng gói real-time từ API nhà mạng, filter tab (thời hạn / mệnh giá / loại), sort, "Best Value" badge | P1 | Dev + API |
| F-05 | eSIM country pages | 200 landing quốc gia: bảng gói, local network info, HowTo iOS/Android, travel context, FAQ | P1 (20 nước) → P3 (200) | Content + Dev |
| F-06 | Nạp tiền form | Auto-detect nhà mạng, quick-select mệnh giá, thanh toán 1-click, cross-sell data sau nạp | P1 | Dev |
| F-07 | Schema markup | FAQPage, HowTo, Product, ItemList, BreadcrumbList, AggregateRating per sản phẩm | P1 | Tech SEO + Dev |

### 6.2 pSEO Engine

| # | Feature | Scale | Priority |
|---|---|---|---|
| F-08 | pSEO sim × tên | 500 trang batch 1 → 10,000 trang full | P1 (batch 1) → P3 (full) |
| F-09 | pSEO sim × năm sinh | 100 trang (năm 1960–2009) × 6 nhà mạng = 600 trang | P2 |
| F-10 | pSEO sim × can chi (tuổi) | 60 can chi × 6 nhà mạng = 360 trang | P3 |
| F-11 | pSEO gói cước | 120 Viettel + 90 Mobi + 70 Vina + 50 nhỏ = ~330 trang | P2 |
| F-12 | Content freshness pipeline | Tự động update gói hết / dừng đăng ký → noindex / redirect | P2 |

### 6.3 Blog Embed Components

| Component | Dùng trong blog | Priority |
|---|---|---|
| C-SIM-01: Sim Lookup Widget | Sim phong thủy × năm sinh | P1 |
| C-SIM-02: Sim Results Card Strip | Top sim theo loại/nhà mạng | P1 |
| C-DATA-01: Data Package Card | Review gói, bài so sánh | P1 |
| C-DATA-02: Data Comparison Table | So sánh gói cùng mệnh giá | P2 |
| C-ESIM-01: eSIM Destination Card | Travel guide theo quốc gia | P1 |
| C-NAP-01: Quick Top-up Form | Bài hướng dẫn nạp tiền | P1 |

**Spec chung:** Web Component nhúng qua shortcode CMS · Fetch realtime từ API MoMo · Lazy load (IntersectionObserver) · GA4 events: `embed_view`, `embed_interact`, `embed_convert` · LCP overhead < 200ms.

### 6.4 Analytics & Tracking

| Event | Trigger | Parameters |
|---|---|---|
| `telecom_sim_view` | User vào trang sim | sim_type, nhà mạng, price |
| `telecom_sim_filter` | Dùng bộ lọc | filter_type, filter_value |
| `telecom_sim_purchase` | Click mua sim | sim_id, nhà mạng, price |
| `telecom_data_view` | Xem trang gói | goi_name, nhà mạng |
| `telecom_data_register` | Click đăng ký gói | goi_id, nhà mạng, price |
| `telecom_esim_view` | Xem trang quốc gia | country, plan_count |
| `telecom_esim_purchase` | Mua eSIM | country, plan_id, price |
| `telecom_topup_complete` | Nạp tiền thành công | nhà mạng, amount |
| `embed_view` | Blog embed vào viewport | component_type, blog_slug, position |
| `embed_convert` | Click CTA trong embed | component_type, product_id |

*Tất cả events cần Appsflyer attribution parameter để map Web → App W2A journey.*

---

## 7. Success Metrics

### 7.1 North Star — Organic Sessions (Volume Growth)

**Lý do chọn:** Use Case Viễn Thông là acquisition-focused — mục tiêu chính là capture organic demand từ Google và dẫn vào MoMo app. Organic sessions là leading indicator rõ ràng nhất.

| Metric | Definition | Baseline (Q0/Roll-out) | Target Q2 | Target Q4 EOY | Tracking |
|---|---|---|---|---|---|
| **Total Organic Sessions** | Monthly organic sessions từ Google/Bing đến tất cả 4 sản phẩm telecom | ~45,000/tháng (ước tính, [cần verify GSC]) | 90,000/tháng | **270,000+/tháng** | GA4 + GSC |

### 7.2 Organic Traffic — Breakdown theo sản phẩm

| Sản phẩm | Baseline | Q1 | Q2 | Q3 | Q4 EOY |
|---|---|---|---|---|---|
| Sim Số Đẹp | ~5,000 [cần verify] | 5,000 | 25,000 | 80,000 | **150,000+** |
| Nạp Data | ~8,000 [cần verify] | 8,000 | 20,000 | 35,000 | **55,000** |
| eSIM Du Lịch | ~2,000 [cần verify] | 2,000 | 8,000 | 20,000 | **35,000** |
| Nạp Tiền ĐT | ~30,000 [cần verify] | 30,000 | 40,000 | 50,000 | **60,000** |

### 7.3 Web-to-App Conversion Rate

| Metric | Definition | Baseline | Target Q4 | Tracking |
|---|---|---|---|---|
| **Organic W2A %CR — Sim** | (Sim orders từ organic / organic sim sessions) × 100 | ~1.5% [cần measure] | **4–5%** | Appsflyer + GA4 |
| **Organic W2A %CR — Data** | (Gói đăng ký từ organic / organic data sessions) × 100 | ~3% [cần measure] | **6–7%** | Appsflyer + GA4 |
| **Organic W2A %CR — eSIM** | (eSIM purchased từ organic / organic esim sessions) × 100 | ~2% [cần measure] | **5–6%** | Appsflyer + GA4 |
| **Organic W2A %CR — Nạp** | (Nạp thành công từ organic / organic nạp sessions) × 100 | ~8% [cần measure] | **11–13%** | Appsflyer + GA4 |

### 7.4 Ranking Keywords (SEO)

| Metric | Definition | Baseline | Target Q2 | Target Q4 | Tracking |
|---|---|---|---|---|---|
| Top 3 keywords — Sim | # từ khóa sim phong thủy / năm sinh rank top 3 | ~5 KW [cần verify] | 50 KW | **200+ KW** | Ahrefs / SEMrush |
| Top 3 keywords — Data | # từ khóa tên gói cước rank top 3 | ~10 KW [cần verify] | 80 KW | **250+ KW** | Ahrefs / SEMrush |
| Top 5 keywords — eSIM | # từ khóa "esim [quốc gia]" rank top 5 | ~2 KW [cần verify] | 30 KW | **100+ KW** | Ahrefs / SEMrush |
| Avg Position — Nạp tiền | Avg position cho keyword set "nạp tiền [nhà mạng]" | ~2.5 [cần verify] | Defend ≤ 3 | **Defend ≤ 2** | GSC |

### 7.5 pSEO Engine Health

| Metric | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| pSEO pages indexed | 0 | 600+ | 5,000+ | **10,000+** |
| pSEO Index Rate | — | ≥ 70% | ≥ 80% | ≥ 85% |
| pSEO Avg CTR | — | ≥ 2% | ≥ 3% | ≥ 3.5% |

---

## 8. Dependencies & Constraints

| Dependency | Owner | Mô tả | Blocker? | Status |
|---|---|---|---|---|
| **Sim inventory API** | Cellteam / PO Cell | API cung cấp danh sách sim available real-time, filter theo nhà mạng / giá / đuôi số | **Yes** | [cần confirm readiness] |
| **Gói cước API** | PO Cell (Telecom) | API gói cước từng nhà mạng: tên, giá, data, cú pháp, tình trạng hoạt động | **Yes** | [cần confirm] |
| **eSIM package API** | PO Cell (eSIM) | API gói eSIM theo quốc gia, real-time inventory | **Yes** | [cần confirm] |
| **W2A tracking (Onelink + Appsflyer)** | Dev + DA Team | Deep link setup cho từng sản phẩm, Appsflyer attribution parameters | **Yes** | [cần setup trước launch] |
| **GA4 event setup** | DA Team | Custom events telecom (xem Section 6.4), GTM container update | **Yes** | [cần DA Team confirm timeline] |
| **AI Giải Luận Engine** | Dev + AI Team | 5-layer logic: Can Chi → Nạp Âm Mệnh → Tứ Trụ → Đầu số mapping → Content generation | **Yes** (cho pSEO sim) | [cần AI Team estimate] |
| **CMS Blog shortcode** | Dev (Web Platform) | Shortcode system để nhúng Blog Embed components vào bài blog | **Yes** | [cần confirm CMS capability] |
| **GTM container approval** | GTM Owner / Web Platform | Approval để deploy tracking events telecom | No (soft) | [weekly GTM cycle] |
| **Content review (YMYL)** | Inbound Content Team | Review các bài blog tài chính / viễn thông theo YMYL checklist | No (soft) | [editorial calendar align] |
| **Schema deployment** | Tech SEO + Dev | FAQPage, HowTo, Product schema per trang — cần Dev deploy, SEO validate qua GSC | No | [phụ thuộc sprint Dev] |

**Constraints (không thể thay đổi):**
- MoMo app là conversion endpoint cuối cùng — web chỉ là acquisition layer
- Tất cả giá sim/gói phải lấy real-time từ API, không hardcode
- Content phong thủy phải được giải luận từ data engine, không được copy từ nguồn khác (copyright + thin content risk)
- pSEO pages tên phải có ≥ 200 chữ unique content per page (Google thin content policy)

---

## 9. Risk Assessment

| # | Rủi ro | Loại | Khả năng | Impact | Mitigation |
|---|---|---|---|---|---|
| R-01 | API nhà mạng không ổn định / sai data gói cước | Technical | Cao | Cao | Build cache layer + timestamp "cập nhật lần cuối" · Fallback UI khi API down |
| R-02 | Gói cước nhà mạng thay đổi / dừng không báo trước | Market | Rất cao | Trung bình | Pipeline auto-check định kỳ · Trang gói dừng → noindex + redirect về trang nhà mạng |
| R-03 | pSEO sim 10K trang bị Google đánh giá thin content | SEO | Trung bình | Cao | Mỗi trang ≥ 200 chữ AI unique · Validate CTR trên 500 trang batch 1 trước khi scale |
| R-04 | AI Giải Luận Engine sai logic phong thủy → mất user trust | Product | Trung bình | Cao | Review nội dung giải luận với phong thủy specialist · User-test 50 cases trước launch |
| R-05 | W2A tracking không setup đúng → mất attribution data | Data | Trung bình | Rất cao | QA Appsflyer + GA4 mandatory trước launch · DA Team sign-off |
| R-06 | Cạnh tranh từ TGDD/nhà mạng tăng cường SEO | Market | Trung bình | Trung bình | MoMo unique advantage: AI phong thủy + payment integration — differentiate, không chỉ copy |
| R-07 | Dev timeline slip do nhiều dependencies | Execution | Cao | Cao | Chia thành waves nhỏ (20 eSIM quốc gia trước, scale sau) · Buffer 2 tuần per milestone |
| R-08 | eSIM inventory hết cho quốc gia hot vào mùa cao điểm | Product | Trung bình | Trung bình | Real-time stock indicator trên trang · Pre-order flow nếu out of stock |
| R-09 | Core Web Vitals tụt do pSEO pages nặng | Technical | Thấp | Trung bình | Lazy load images · Skeleton loading · LCP target < 2.5s cho tất cả P1 pages |

---

## 10. Next Steps

| # | Deliverable | Owner | Mô tả | Target date |
|---|---|---|---|---|
| NS-01 | Validate baseline metrics | Klaus + DA Team | Pull GSC data 3 tháng gần nhất cho 4 sản phẩm · Confirm baseline organic sessions và avg position | Tuần 1 (Q1/2026) |
| NS-02 | API readiness confirmation | PO Cell + Dev Lead | Confirm 3 API: Sim, Gói Cước, eSIM có thể integrate và timeline | Tuần 1–2 |
| NS-03 | GA4 + Appsflyer tracking spec | Klaus + DA Team | Viết tracking spec đầy đủ cho 10 events telecom (Section 6.4) · Review với DA + GTM Owner | Tuần 1–2 |
| NS-04 | PRD — Content & Page Spec | Klaus + PO Cell | Mô tả chi tiết anatomy từng trang P1, content brief cho từng section, UX wireframe | Tuần 2–3 |
| NS-05 | AI Giải Luận Engine spec | Klaus + AI Team | 5-layer logic spec, data layer (tên × mệnh × số nét), content template, unique text generation rules | Tuần 2–4 |
| NS-06 | pSEO Batch 1 — 500 trang tên | Dev + Content | Build pipeline gen, launch 500 trang phổ biến nhất, validate indexing + CTR trong 4 tuần | Q2/2026 bắt đầu |
| NS-07 | Blog Embed Component build | Dev | Build 6 components (C-SIM-01/02, C-DATA-01/02, C-ESIM-01, C-NAP-01) · GA4 events · Shortcode CMS | Q1/2026 cuối |
| NS-08 | Content calendar — 20 bài TOFU | Klaus + Inbound | Lên editorial calendar 20 bài Q1–Q2 · Assign writers · YMYL review process | Tuần 2–3 |
| NS-09 | Tracking QA plan | DA Team + Dev | Test plan cho tất cả GA4 events + Appsflyer attribution · Sign-off checklist trước launch | Trước launch Q1 |

---

## Appendix A — Phong Thủy Logic Reference

**Mệnh ngũ hành theo cặp năm sinh (Nạp Âm):**

| Năm sinh | Can Chi | Mệnh | Số cát (đuôi) | Số kỵ | Nhà mạng gợi ý |
|---|---|---|---|---|---|
| 1984–1985 | Giáp Tý / Ất Sửu | Kim | 1, 6, 7 | 2, 3, 8 | Viettel 086, 096 |
| 1986–1987 | Bính Dần / Đinh Mão | Hỏa | 2, 7, 9 | 1, 6, 4 | MobiFone 090, 089 |
| 1988–1989 | Mậu Thìn / Kỷ Tỵ | Mộc | 3, 4, 8 | 1, 6, 7 | Vinaphone 081, 082 |
| 1990–1991 | Canh Ngọ / Tân Mùi | Thổ | 2, 5, 8 | 3, 4, 9 | Viettel 086, Vina 094 |
| 1992–1993 | Nhâm Thân / Quý Dậu | Kim | 1, 6, 7 | 2, 3, 8 | Viettel 096, 097 |
| 1994–1995 | Giáp Tuất / Ất Hợi | Hỏa | 2, 7, 9 | 1, 6, 4 | MobiFone 079, Viettel 038 |

*Data này làm seed cho AI Giải Luận Engine — cần consultant phong thủy review trước production.*

---

## Appendix B — Keyword Clusters Cần Validate

Các cluster từ khóa dưới đây là ước tính — **cần verify bằng Ahrefs/SEMrush + GSC trước Q1 rollout:**

| Cluster | Ví dụ keyword | Volume ước tính | Priority để build page |
|---|---|---|---|
| Sim phong thủy × năm sinh | "sim hợp tuổi [1960–2010]" | ~150K/tháng tổng | P1 (pSEO) |
| Sim phong thủy × tên | "sim hợp tên [Tên]" | ~500K/tháng tổng | P1 (pSEO) |
| Gói data tên cụ thể | "gói D90N", "gói MAX Mobi" | ~95K/tháng tổng | P1 (pSEO) |
| eSIM quốc gia | "esim [20 nước hot]" | ~80K/tháng tổng | P1 |
| Nạp tiền branded | "nạp tiền qua MoMo" | ~50K/tháng | Defend (đã rank tốt) |
| So sánh nhà mạng / gói | "so sánh gói 100k các nhà mạng" | ~20K/tháng | P2 (blog) |

---

## Appendix C — Glossary

| Thuật ngữ | Định nghĩa |
|---|---|
| W2A | Web-to-App — tỷ lệ user từ web chuyển sang hoàn thành giao dịch trên app MoMo |
| pSEO | Programmatic SEO — tạo nhiều trang tương tự nhau theo template, mỗi trang unique content |
| Out-App Traffic | Traffic đến MoMo từ các kênh ngoài app (web, blog, organic search) |
| Nạp Âm Mệnh | Hệ thống phân loại mệnh ngũ hành theo năm sinh trong phong thủy Việt Nam |
| AI Giải Luận | Tính năng AI generate giải thích phong thủy unique cho từng tổ hợp tên × năm sinh × mệnh |
| Blog Embed Component | Widget sản phẩm nhúng vào bài blog để tăng conversion tại điểm intent cao nhất |
| MNP | Mobile Number Portability — chuyển mạng giữ nguyên số điện thoại |
| JTBD | Jobs-to-Be-Done — framework xác định "công việc" user thuê sản phẩm để thực hiện |
| CAC | Customer Acquisition Cost — chi phí để có được 1 user mớ