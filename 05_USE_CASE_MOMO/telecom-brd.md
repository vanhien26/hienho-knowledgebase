# BRD: Viễn Thông - Web Growth (SEO/GEO Project)

> - **Project:** MoMo Telecom Growth - Sim Số Đẹp - Nạp Data - eSIM Du Lịch - Nạp Tiền ĐT
> - **Main URL:** momo.vn/vien-thong (hub) - /sim-so-dep - /nap-data - /esim-du-lich - /nap-tien-dien-thoai
> - **Division:** PS (Payment Services)
> - **Use Case:** Telco
> - **Owner:** GPD - Out-App Traffic
> - **Governance:** Web Product Lead
> - **Version:** 2.1 - 2026-05-24
> - **Status:** Active (Approved)

---

> **Problem:** Người Việt search "sim số đẹp hợp tuổi", "gói data Viettel", "esim Nhật Bản" hàng triệu lần mỗi tháng - MoMo có thể phục vụ cả 4 nhu cầu đó nhưng không có trang web nào xuất hiện khi họ tìm. Traffic và giao dịch đang chảy về TGDD, site phong thủy và eSIM providers quốc tế.
> **KPI Owned:** Số giao dịch Telco attributed từ organic web (Web-to-Transaction)
> **Conversion Flow:** Search "sim hợp tuổi 1990" / "gói D90N Viettel" / "esim Nhật Bản" → /sim-so-dep/{slug} / /nap-data/{slug} / /esim-du-lich/{slug} → Thông tin + CTA → Web transaction hoặc App MoMo → Purchase

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
- **Vấn đề cốt lõi:** Người dùng cần mua sim phong thủy, mua data gấp hoặc tìm eSIM đi du lịch, nhưng trải nghiệm mua online từ nhà mạng thì rời rạc, ra đại lý thì mất thời gian.
- **Giải pháp (The "What"):** Gom toàn bộ nhu cầu viễn thông vào 1 Hub duy nhất trên MoMo Web. Sử dụng AI Giải luận phong thủy để tạo "Aha moment" (Bữa tối gia đình test của CEO) và cho phép thanh toán trọn vẹn hành trình (Full Journey).

### 1.2 Situation & Complication
Mỗi ngày, hàng triệu người Việt search "sim số đẹp hợp tuổi", "gói data Viettel tháng này", "esim du lịch Nhật". Thị trường ước tính 500K-800K searches/tháng, intent rõ ràng, CAC = 0. Nhưng MoMo rank yếu hoặc không rank cho các nhóm từ khóa volume cao này, nhường sân chơi cho TGDD và các bên bán sim trung gian.

### 1.3 Resolution
Use Case Viễn Thông xây dựng hệ thống web content gồm: (1) Hub `/vien-thong` làm trang trung tâm; (2) pSEO engine tạo 10.000+ trang sim phong thủy với AI Widget; (3) eSIM landing cho 200+ quốc gia. Product drives transaction - từ search intent đến purchase trên web, không cần ra đại lý.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Sản Phẩm

| Sản phẩm | URL | Trạng thái web hiện tại | Organic traffic ước tính |
|---|---|---|---|
| Nạp Tiền ĐT | momo.vn/nap-tien-dien-thoai | Trang thông tin đơn thuần | ~30.000 sessions/tháng |
| Sim Số Đẹp | momo.vn/sim-so-dep | Đã triển khai trang chủ về luồng sản phẩm | ~5.000 sessions/tháng |
| Nạp Data | momo.vn/nap-data | Có homepage và 4 sub-page nhà mạng, chưa có luồng mua hàng đầy đủ | ~8.000 sessions/tháng |
| eSIM Du Lịch | momo.vn/esim-du-lich | Đã triển khai đủ luồng từ homepage đến trang khu vực chi tiết | ~2.000 sessions/tháng |

### 2.2 Search Demand Landscape

| Nhóm từ khóa | Ví dụ keyword | Volume ước tính | Intent | Competitor ranking |
|---|---|---|---|---|
| Sim phong thủy × năm sinh | "sim số đẹp hợp tuổi 1990" | ~150K/tháng tổng (50 năm × 2-5K) | Buy | Các site phong thủy, TGDD |
| Sim phong thủy × tên | "sim hợp tên Minh", "sim tên Lan" | ~500K/tháng tổng (5.000 tên) | Buy | Yếu - cơ hội lớn cho MoMo |
| Gói data nhà mạng | "gói data Viettel", "gói D90N" | ~15K/tháng per nhà mạng | Buy | TGDD rank Top 1-3 |
| eSIM quốc gia | "esim Nhật Bản", "esim Hàn Quốc" | ~3.000-8.000/tháng per nước hot | Buy | eSIM providers quốc tế |
| Nạp tiền branded | "nạp tiền điện thoại qua MoMo" | ~20.000/tháng | Go | MoMo đang rank tốt |
| So sánh / hướng dẫn | "cách chọn sim hợp phong thủy" | ~5.000-10.000/tháng | Know | Blog site, TGDD |

### 2.3 Phân Tích Cạnh Tranh

| Đối thủ | Điểm mạnh | Điểm yếu | MoMo Advantage |
|---|---|---|---|
| Thế Giới Di Động | Domain authority cao, phủ sóng rộng gói cước + sim | Không có payment app tích hợp, không có phong thủy AI | MoMo Pay ecosystem, AI giải luận personalized |
| Các site sim phong thủy | Content depth về phong thủy, UX đơn giản | Không bán được sim online | MoMo có thể bán trực tiếp - zero friction |
| eSIM providers quốc tế | Phủ sóng toàn cầu | Không có tiếng Việt tốt, không có local payment | MoMo Pay + tiếng Việt native |
| Nhà mạng (Viettel, Mobi, Vina) | Brand awareness | Web UX kém, không aggregate cross-carrier | MoMo là neutral aggregator - so sánh được |

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi

**User search sim/data/eSIM/nạp tiền - tìm thấy momo.vn với đúng thông tin cần - chọn và hoàn thành giao dịch ngay trên web hoặc App - không cần ra đại lý, không cần nhờ người khác.**

Số giao dịch Telco tăng thêm từ kênh organic = zero incremental cost per transaction.

4 outcome phát sinh:

**① Telco Acquisition:** Capture intent đang bị đối thủ take từ organic - sim phong thủy, gói data, eSIM travel, nạp tiền.

**② Full Journey Web:** BU Telco yêu cầu end-to-end transaction trên web - không chỉ redirect về App. Product phải hoàn thành được giao dịch.

**③ PLG via pSEO:** AI Giải Luận widget tạo unique content per user query - không thể scrape, không thể replicate. Anti-LLM moat.

**④ Cross-sell Gateway:** Web hub Viễn Thông là điểm vào tự nhiên sang BH Du Lịch, eSIM, Credit cho traveling users.

### 3.2 Bối Cảnh Chiến Lược

**Thực trạng tăng trưởng:** Số lượng người dùng mới của dịch vụ Viễn thông (New to Service) đang đi ngang ở mức khoảng 120K. Viễn thông là dịch vụ tiện ích dạng "think fast" - người dùng phát sinh nhu cầu, truy cập mua nhanh rồi rời đi. Kênh tiếp cận chủ đạo bắt buộc phải là Out-App (Web/Search).

**Định hướng từ BU Telco:** Đẩy mạnh SEO/SEM Telco, yêu cầu người dùng mua hàng trực tiếp trên Web trọn vẹn hành trình (Full Journey). Phải có cơ chế đo lường tracking cụ thể. BU VTTI làm việc trực tiếp với Web Platform dựa trên BRD chi tiết.

### 3.3 Intent-based Filtering Framework (Trang Phạm Standard)
Phân loại rạch ròi luồng traffic dựa trên Search Intent để điều hướng vào đúng Product Lane, tránh dắt user đi lòng vòng:

| Sản phẩm | Phân khúc Target | Đặc tính nhu cầu (Intent Filter) |
|---|---|---|
| Sim Số Đẹp / Sim Chính Chủ | Người kinh doanh, người duy tâm, người đổi sim phong thủy | Nghiên cứu kỹ trước mua - intent cao, giá trị giao dịch cao |
| eSIM Du Lịch | Du khách trẻ, hay di chuyển quốc tế, sử dụng smartphone cận cao cấp | Mua trước chuyến đi, cần cài nhanh, giá trị convenience cao |
| Nạp Data 4G/5G | Shipper, tài xế, game thủ, Gen Z tiêu thụ nhiều internet | Nhu cầu gấp hoặc so sánh gói, nhạy cảm về giá và dung lượng |
| Nạp Tiền Điện Thoại | Mọi người dùng di động trả trước, người nạp hộ người thân | Tốc độ tối thượng, 24/7, không muốn rào cản |

### 3.4 Dự Án Này KHÔNG Phải

- Không build mobile app feature
- Không quản lý inventory sim (trách nhiệm nhà mạng partner)
- Không làm CRM / retention cho user đã mua
- Không cover nạp tiền điện thoại bàn (landline)
- Không build telco aggregator đầy đủ với so sánh nhà mạng phức tạp

---

## 4. JTBD Analysis

### Job #SIM-01: Chọn Sim Hợp Phong Thủy

> "Tôi cần chọn số điện thoại mới hợp với mệnh, tuổi của mình để mang may mắn."

| Dimension | Nội dung |
|---|---|
| Functional | Tìm được sim có đuôi số hợp mệnh/năm sinh, mua online không cần ra đại lý |
| Emotional | An tâm đã chọn đúng, không lo dùng số "xấu" ảnh hưởng công việc, sức khỏe |
| Social | Người thân/đối tác thấy mình chỉn chu, am hiểu phong thủy |
| Trigger | Mua sim mới - Khai trương kinh doanh - Đầu năm mới - Chuyển mạng |
| Search → App | "sim số đẹp hợp tuổi 1990", "sim mệnh Mộc Viettel" → /sim-so-dep/phong-thuy/[menh] → AI Giải Luận gợi ý sim → "Mua ngay" → Web checkout / App MoMo |

**Giải pháp:** pSEO trang năm sinh × mệnh × nhà mạng + AI Giải Luận widget.

---

### Job #SIM-02: Tặng Sim Số Đẹp Làm Quà

> "Tôi muốn tặng sim số đẹp hợp tuổi người được tặng - quà độc đáo và thiết thực."

| Dimension | Nội dung |
|---|---|
| Functional | Nhập năm sinh người được tặng → AI gợi ý sim phù hợp → mua và giao nhận đúng dịp |
| Emotional | Cảm thấy đã chuẩn bị chu đáo, quà có ý nghĩa thay vì mua đại |
| Social | Người nhận cảm nhận được sự quan tâm cá nhân hóa - kể lại "bạn tặng sim hợp mệnh mình" |
| Trigger | Sinh nhật - Tết - Khai trương - Ra trường - Đám cưới |
| Search → App | "sim tặng sinh nhật", "sim số đẹp làm quà", "sim hợp tuổi người yêu" → /sim-so-dep/tang-sim-so-dep → Widget nhập năm sinh người được tặng → Chọn sim → Checkout |

**Giải pháp:** Landing /sim-so-dep/tang-sim-so-dep + Widget nhập năm sinh người được tặng.

---

### Job #SIM-03: Số Điện Thoại Kinh Doanh Đẹp, Dễ Nhớ

> "Số điện thoại là bộ mặt của doanh nghiệp - tôi cần số dễ nhớ, in được lên danh thiếp."

| Dimension | Nội dung |
|---|---|
| Functional | Filter được sim theo pattern (đuôi lặp, số đẹp), chọn nhà mạng, giá range |
| Emotional | Tự tin khi đưa số cho khách, cảm giác chuyên nghiệp |
| Social | Khách hàng nhớ ngay số, thấy chủ doanh nghiệp đầu tư nghiêm túc - kể cho nhau nghe về số hotline đẹp |
| Trigger | Mở cơ sở mới - Rebranding - Đổi số hotline |
| Search → App | "sim số đẹp kinh doanh", "sim hotline dễ nhớ", "sim 4 số cuối đẹp Viettel" → /sim-so-dep/sim-kinh-doanh → Filter pattern + nhà mạng → "Đặt sim ngay" → Checkout |

**Giải pháp:** Landing /sim-so-dep/sim-kinh-doanh + premium tier sim + Blog sim hotline theo ngành.

---

### Job #DATA-01: Đăng Ký Gói Data Khẩn Cấp

> "Điện thoại vừa thông báo hết data - tôi cần đăng ký gói ngay, nhanh nhất có thể."

| Dimension | Nội dung |
|---|---|
| Functional | Đăng ký gói trong 3 bước, thanh toán ví MoMo sẵn có, kích hoạt tức thì |
| Emotional | Không bị "chết internet" giữa chừng, không cần nhờ ai hay tìm wifi |
| Social | Vẫn available với công việc và mọi người xung quanh - không bị hỏi "sao không reply" |
| Trigger | Thông báo hết data - Mạng chậm đột ngột - Cuối tháng |
| Search → App | "gói data Viettel", "đăng ký gói D90N", "nạp data Viettel ngay" → /nap-data/viettel/[ten-goi] → 1-click đăng ký → Web payment / App MoMo → Kích hoạt tức thì |

**Giải pháp:** pSEO landing /nap-data/[nha-mang]/[ten-goi] rank Top 1 + badge "Kích hoạt tức thì".

---

### Job #DATA-02: So Sánh Và Chọn Gói Data Value Nhất

> "Tôi muốn biết gói nào cho nhiều GB nhất với giá tốt nhất trong tháng này."

| Dimension | Nội dung |
|---|---|
| Functional | So sánh được tất cả gói của nhà mạng, hiểu rõ data/ngày và tổng data |
| Emotional | Tự tin đã chọn gói "value nhất", không bị cảm giác bị thiệt |
| Social | Recommend được gói tốt cho bạn bè/đồng nghiệp - "tao đang dùng gói này, rẻ mà nhiều data lắm" |
| Trigger | Gói hết hiệu lực - Review chi phí hàng tháng - Thấy quảng cáo gói mới |
| Search → App | "so sánh gói data 100k các nhà mạng", "gói data nào nhiều GB nhất", "gói data Viettel tốt nhất" → /nap-data/[nha-mang] → Bảng so sánh + filter → Badge "Best Value" → Chọn và mua |

**Giải pháp:** Trang nhà mạng: bảng đầy đủ + filter + badge "Best Value".

---

### Job #ESIM-01: Internet Ngay Khi Hạ Cánh Nước Ngoài

> "Tôi muốn có internet ngay khi vừa hạ cánh - không phải xếp hàng ở sân bay."

| Dimension | Nội dung |
|---|---|
| Functional | Mua và cài eSIM trước khi đi, đến nơi chỉ bật lên là có mạng ngay |
| Emotional | An tâm hoàn toàn - không "tối tăm" khi vừa đến nơi lạ |
| Social | Update được ngay cho gia đình biết đã đến an toàn - không bị nhắn "đến chưa mà im vậy" |
| Trigger | Mua vé máy bay - 1-2 tuần trước chuyến đi - Check-in online |
| Search → App | "esim Nhật Bản", "esim du lịch Hàn Quốc", "mua esim trước khi đi nước ngoài" → /esim-du-lich/chau-a/nhat-ban → "Mua và cài trước khi đi" + Hướng dẫn → Web checkout / App MoMo |

**Giải pháp:** Hero copy "Internet ngay khi hạ cánh" + Hướng dẫn cài trước khi đi + Trust signal.

---

### Job #ESIM-02: Tránh Sốc Hóa Đơn Roaming

> "Lần trước tôi về nước mới biết bill roaming đến vài triệu - lần này tôi muốn biết trước."

| Dimension | Nội dung |
|---|---|
| Functional | Giá cố định đã biết trước, không có phí ẩn hay cước roaming bất ngờ |
| Emotional | Dùng internet thoải mái không phải dè xẻn, không lo về con số hóa đơn |
| Social | Chia sẻ được ảnh/video real-time cho bạn bè không cần đợi về nhà - kể lại "dùng eSIM MoMo tiết kiệm mấy triệu so với roaming" |
| Trigger | Đã từng bị bill roaming cao - Chuẩn bị cho chuyến đi dài ngày |
| Search → App | "esim có tốt hơn roaming không", "roaming Viettel Nhật giá bao nhiêu", "so sánh esim vs roaming" → /blog/esim-vs-roaming-tiet-kiem → So sánh + Calculator tiết kiệm → "Tiết kiệm [X]đ với eSIM MoMo" → Checkout |

**Giải pháp:** So sánh eSIM MoMo vs roaming Viettel/Mobi + Calculator tiết kiệm.

---

### Job #NAP-01: Nạp Tiền Điện Thoại Khẩn Cấp

> "Điện thoại vừa báo sắp hết tiền - tôi cần nạp ngay trước khi bị cắt cuộc gọi."

| Dimension | Nội dung |
|---|---|
| Functional | Nạp trong 10 giây, nhận xác nhận ngay, 24/7 không cần ra cửa hàng |
| Emotional | Không lo bị cắt cuộc gọi quan trọng, không cần dè xẻn từng tin nhắn |
| Social | Luôn available cho gia đình, đồng nghiệp, khách hàng - không bị "gọi không nghe, nhắn không reply" |
| Trigger | SMS "tài khoản sắp hết" - Cuộc gọi bị ngắt - Cuối tháng |
| Search → App | "nạp tiền điện thoại Viettel nhanh", "nạp tiền MoMo", "nạp thẻ điện thoại online" → /nap-tien-dien-thoai/viettel → Form nạp above-the-fold → Nhập số + Nạp ngay → Web payment / App confirm |

**Giải pháp:** Form nạp above-the-fold + "Nạp trong 5 giây" badge + Auto-detect nhà mạng từ đầu số.

---

## 5. Kiến Trúc Web

### 5.1 Sitemap Hub & Spoke

```
momo.vn/vien-thong [Hub - 4 sản phẩm]
│
├── SIM SỐ ĐẸP
│   ├── /sim-so-dep/[nha-mang]                    (6 nhà mạng)
│   ├── /sim-so-dep/phong-thuy/[loai]             (8 loại phong thủy)
│   ├── /sim-so-dep/tang-sim-so-dep               (Quà tặng)
│   ├── /sim-so-dep/sim-kinh-doanh                (B2B)
│   └── /sim-so-dep/[ten] / /sim-so-dep/[nam-sinh] (pSEO - 10.000+ trang)
│
├── NẠP DATA
│   ├── /nap-data/[nha-mang]                      (6 nhà mạng)
│   └── /nap-data/[nha-mang]/[ten-goi]            (pSEO - 330+ gói)
│
├── ESIM DU LỊCH
│   ├── /esim-du-lich/[khu-vuc]                   (Châu Á, Châu Âu...)
│   └── /esim-du-lich/[khu-vuc]/[quoc-gia]        (200 quốc gia)
│
├── NẠP TIỀN ĐIỆN THOẠI
│   └── /nap-tien-dien-thoai/[nha-mang]           (6 nhà mạng)
│
└── BLOG CLUSTER (momo.vn/blog - nhúng Blog Embed Components)
└── BLOG CLUSTER (momo.vn/blog - nhúng Blog Embed Components)
```

**AEO/GEO Standard:** `momo.vn/vien-thong/llms.txt` (Bắt buộc theo quy chuẩn VP GPD để chuẩn hóa AI citation cho các câu hỏi phong thủy/gói data).

**Schema bắt buộc:** FAQPage - HowTo - Product - ItemList - BreadcrumbList - AggregateRating per sản phẩm.

### 5.2 Scope Triển Khai

**Giai đoạn cốt lõi (Launch Blockers):**
- Telecom Hub `/vien-thong` với 4 sản phẩm
- Sim hub + 6 nhà mạng + 8 trang phong thủy loại
- Nạp Data hub + 6 nhà mạng với bảng gói đầy đủ
- eSIM hub + 20 quốc gia có demand cao nhất (JP, KR, TH, SG, US...)
- Nạp Tiền hub + 6 nhà mạng
- Schema markup toàn bộ
- Blog Embed Components (6 loại widget nhúng vào blog)

**Giai đoạn mở rộng:**
- pSEO sim phong thủy × tên (500 trang batch 1, scale lên 10.000 trang)
- pSEO sim × năm sinh (100 trang)
- pSEO gói cước (330 gói × 6 nhà mạng)
- eSIM mở rộng 100-200 quốc gia
- Blog content (20 bài TOFU) + Cross-sell engine (telecom → BH du lịch)

**Giai đoạn tối ưu & chiếm lĩnh:**
- pSEO sim full scale 10.000 trang
- AI chatbot tư vấn sim phong thủy
- Review system (AggregateRating schema)
- eSIM Travel Planner AI itinerary
- Loyalty hub - MoMo Điểm telecom

### 5.3 pSEO Architecture - Sim Phong Thủy

**AI Giải Luận Widget:** Input: tên + năm sinh → AI 5-layer logic → Output: mệnh + số cát + gợi ý 3 sim + giải thích 200+ chữ unique per combination. Tạo unique content không scrape được - đây là anti-LLM moat và core SEO differentiator so với đối thủ.

---

## 6. Success Metrics

### 6.1 North Star Metric

**Organic Sessions - Web-to-Transaction** = Số giao dịch Telco (nạp tiền/mua data/sim/eSIM) được attributed từ organic traffic web.

**Funnel:**
```
Search → Landing Page Telco → Giao dịch trực tiếp trên Web (Full Journey) hoặc W2A → Purchase
```

### 6.2 KPI Framework

| Metric | Baseline (hiện tại) | Target EOY 2026 | Source |
|---|---|---|---|
| Organic sessions/tháng (toàn Telco cluster) | ~45K (tổng 4 sản phẩm ước tính) | 270.000+ sessions/tháng | GSC + GA4 |
| Nạp tiền ĐT organic sessions | ~30.000/tháng | 50.000+/tháng | GSC |
| Sim Số Đẹp organic sessions | ~5.000/tháng | 80.000+/tháng (pSEO scale) | GSC |
| Nạp Data organic sessions | ~8.000/tháng | 80.000+/tháng | GSC |
| eSIM Du Lịch organic sessions | ~2.000/tháng | 60.000+/tháng | GSC |
| pSEO pages indexed (sim phong thủy) | 0 | 10.000+ | GSC |
| pSEO pages indexed (gói cước) | 0 | 330+ | GSC |
| eSIM quốc gia pages | 20 | 200 | Site audit |

### 6.3 Mandatory Tracking & AB Test Hypothesis (MoSpark Standard)
- **Hypothesis:** Nếu dùng "AI Giải Luận Widget" nhập năm sinh ngay trên màn hình đầu tiên (thay vì bắt user tự cuộn tìm số), Conversion Rate (Web-to-Transaction) sẽ tăng 60% vì giải quyết triệt để nhu cầu cá nhân hóa.
- **Tracking Event Schema:** Gắn tracking DA & Appsflyer cho các sự kiện: `telco_ai_input` (Nhập năm sinh), `telco_package_select` (Chọn gói data/eSIM), `telco_checkout_success`.

---

## 7. Dependencies & Constraints

| Dependency | Mô tả | Blocker? |
|---|---|---|
| API gói cước real-time từ nhà mạng | Bảng gói data cần cập nhật real-time. Không có API = trang tĩnh lỗi thời, mất tin cậy | Có - cho Nạp Data |
| API sim inventory từ Cellteam | Trang sim cần hiển thị sim còn hàng, giá real-time | Có - cho Sim Số Đẹp |
| Deep Link per sản phẩm và per gói | CTA "Mua ngay" cần deep link đúng destination trong App | Có - cho tất cả sản phẩm |
| Phong Thủy Data validation | Bảng mệnh ngũ hành theo năm sinh cần được consultant phong thủy review trước khi public ở production | Có - trust signal |
| Blog Embed Component build | 6 loại widget cần Web Platform build trước khi blog có thể sử dụng | Có - cho content strategy |
| GA4 + Appsflyer W2A tracking | Track conversion từ web sang app per sản phẩm Telco | Có - đo KPI |

**Constraints:**
- Full Journey trên Web (End-to-End) là yêu cầu của BU Telco - không chỉ là landing page redirect về App
- Trang sim phong thủy phải có disclaimer rõ ràng về tính chất tham khảo của phong thủy
- pSEO content phải unique - không được duplicate content giữa các trang (AI Giải Luận giải quyết điều này)
- eSIM chỉ áp dụng cho thiết bị hỗ trợ eSIM - cần filter và thông báo rõ trong UX

### 7.1 Go-to-Market: SPA Framework (Service Productization)
- **reSearch / Strategy:** Phân tích nhu cầu 800K searches/tháng (Sim, eSIM, Data) và các insight phong thủy.
- **Pilot / Plan (T6/2026):** Rollout Nạp Data & eSIM hub + AI Giải luận phong thủy MVP.
- **Action / Amplify (Q3/2026):** pSEO 10.000+ trang Sim Phong Thủy (x tên x tuổi) để thống trị organic SOV.

---

## Appendix A: Phong Thủy Logic Reference - Mệnh Ngũ Hành Theo Năm Sinh

*Bảng seed cho AI Giải Luận Engine - cần consultant phong thủy validate trước production.*

| Năm sinh | Can Chi | Mệnh | Số cát (đuôi) | Số kỵ | Nhà mạng gợi ý |
|---|---|---|---|---|---|
| 1984-1985 | Giáp Tý / Ất Sửu | Kim | 1, 6, 7 | 2, 3, 8 | Viettel 086, 096 |
| 1986-1987 | Bính Dần / Đinh Mão | Hỏa | 2, 7, 9 | 1, 6, 4 | MobiFone 090, 089 |
| 1988-1989 | Mậu Thìn / Kỷ Tỵ | Mộc | 3, 4, 8 | 1, 6, 7 | Vinaphone 081, 082 |
| 1990-1991 | Canh Ngọ / Tân Mùi | Thổ | 2, 5, 8 | 3, 4, 9 | Viettel 086, Vina 094 |
| 1992-1993 | Nhâm Thân / Quý Dậu | Kim | 1, 6, 7 | 2, 3, 8 | Viettel 096, 097 |
| 1994-1995 | Giáp Tuất / Ất Hợi | Hỏa | 2, 7, 9 | 1, 6, 4 | MobiFone 079, Viettel 038 |

---

## Appendix B: Glossary

| Thuật ngữ | Định nghĩa |
|---|---|
| W2A | Web-to-App - tỷ lệ user từ web chuyển sang hoàn thành giao dịch trên app MoMo |
| pSEO | Programmatic SEO - tạo nhiều trang tương tự nhau theo template, mỗi trang unique content |
| Out-App Traffic | Traffic đến MoMo từ các kênh ngoài app (web, blog, organic search) |
| Nạp Âm Mệnh | Hệ thống phân loại mệnh ngũ hành theo năm sinh trong phong thủy Việt Nam |
| AI Giải Luận | Tính năng AI generate giải thích phong thủy unique cho từng tổ hợp tên × năm sinh × mệnh |
| Blog Embed Component | Widget sản phẩm nhúng vào bài blog để tăng conversion tại điểm intent cao nhất |
| JTBD | Jobs-to-Be-Done - framework xác định "công việc" user thuê sản phẩm để thực hiện |
| CAC | Customer Acquisition Cost - chi phí để có được 1 user mới |

---

## Change Log

- **2026-05-24 (v2.1):** Apply CEO BRD Standard: Thêm Problem Statement block, rewrite Situation theo user-centric, thêm Product Job Cốt Lõi (Section 3.1), renumber Section 3, thêm Search → App vào tất cả 8 JTBD. Xóa Risk Assessment (Section 8). Xóa Appendix B Keyword Clusters (giữ Appendix A Phong Thủy Logic + Appendix B Glossary, renumber).
- **2026-05-19 (v2.0):** Tích hợp chiến lược Intent-Based Audience Filtering. Tích hợp 4 phân khúc người dùng mapped với 8 JTBD cốt lõi. Xây dựng content plan theo keyword cluster.
- **Tháng 5/2026 (v1.2):** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.
