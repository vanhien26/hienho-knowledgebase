# BRD: eSIM Du Lịch - Web Growth & Content Architecture

> - **Project:** eSIM Du Lịch — Web Growth & SEO/GEO
> - **Main URL:** momo.vn/esim-du-lich
> - **Division:** PS (Payment Services) - Telco
> - **Version:** 1.3 · Tháng 5/2026
> - **Status:** Draft - chờ review PO + Dev

---

## 1. Executive Summary

**Situation:** MoMo phân phối eSIM qua đối tác Gohub (150+ quốc gia), Xplori và Mobi Inbound. Thị trường SIM du lịch Việt Nam ước tính 1K–1.5K tỷ VNĐ/năm, tăng trưởng nhanh theo đà xuất cảnh (9 tháng 2025: 5.44 triệu lượt người Việt xuất cảnh, +33.1% YoY). MoMo có lợi thế distribution rõ ràng: 12.8M user A30, thanh toán seamless, trust cao — nhưng hiện không có touchpoint web để capture search demand. Keyword pool ~38.050 SV/tháng (380 keywords) đang bị bỏ ngỏ.

**Complication:** MoMo chưa được định vị trong đầu user là kênh mua SIM du lịch — mindshare thuộc Airalo, Klook, Gohub. Organic traffic hiện dao động 25–43K/tháng nhưng không có growth, phụ thuộc paid. Web contribution vào tổng Trans hiện tiệm cận 0%. Không có destination pages, không có blog layer, không có GEO FAQ layer — không intercept được user đang search Google theo quốc gia. GMV 2025: 16 tỷ VNĐ (~11% SAM); Target 2026: 48 tỷ VNĐ (+300%).

**Resolution:** Dự án xây dựng cluster web eSIM Du Lịch gồm 1 Hub page, 10 Destination pages, và ~10 blog theo keyword-driven architecture. Conversion path: Web → Deep link → App → Mua gói → Thanh toán ví MoMo. Web contribution target: 4% (T7/2026) → 10% (T9/2026) tổng Trans; Web GMV target: ~1.1 tỷ VNĐ (T9/2026). Lợi thế cạnh tranh của MoMo không nằm ở sản phẩm eSIM mà ở **distribution + payment seamless + trust** từ hệ sinh thái ví điện tử.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Thị trường

- eSIM global: $2.45B (2024), CAGR 14% đến 2032
- Thị trường SIM du lịch Việt Nam: 1K–1.5K tỷ VNĐ/năm, tăng trưởng nhanh
- 9 tháng đầu 2025: 5.44 triệu lượt người Việt xuất cảnh (+33.1% YoY)
- 22M+ thiết bị hỗ trợ eSIM tại Việt Nam
- Xu hướng người Việt mua eSIM trước chuyến đi phù hợp funnel digital của MoMo

### 2.2 Competitive Landscape

| Player | Điểm mạnh | Điểm yếu vs MoMo |
|---|---|---|
| **Gohub** (đối tác) | Dẫn đầu thị trường, 195+ quốc gia | Brand awareness thấp với user phổ thông |
| **Gloka** | B2C mạnh, SEO tốt | Không có siêu app distribution |
| **Airalo** | Global #1, brand quốc tế | Không bản địa hóa cho người Việt |
| **Klook** | OTA distribution, SV đáng kể | Không phải core product |
| **Traveloka** | OTA lớn, đông user Việt | SIM du lịch không phải core |
| **Sàn TMĐT** (Shopee, Lazada) | Đa dạng gói, giá cạnh tranh, review nhiều | CSKH yếu, không chuyên SIM |

**Strategic position:** MoMo không cạnh tranh trên sản phẩm eSIM — cạnh tranh trên **distribution, UX, và trust**. User MoMo sẵn có ví và thẻ liên kết — friction mua thấp hơn bất kỳ competitor nào.

**SWOT:**

| Strengths | Weaknesses |
|---|---|
| Tệp 12.8M A30 users, traffic tự nhiên cao | Chưa được định vị "chuyên du lịch" trong đầu user |
| Lợi thế thanh toán all-in-one | Chưa có USP khác biệt, dễ bị so sánh giá |
| Brand awareness cao | Chi phí marketing hạn chế |
| Danh mục rộng (105+ quốc gia), đa dạng khoảng giá | SIM phụ thuộc chính sách viễn thông đối tác |

| Opportunities | Threats |
|---|---|
| Người Việt xuất cảnh tăng >33% (2025) | Nhiều player lâu năm (Klook, Traveloka, Trip.com) |
| Xu hướng mua eSIM trước chuyến đi | Sàn TMĐT dễ cạnh tranh giá |
| 22M+ thiết bị hỗ trợ eSIM | Nhanh mất thị phần nếu không có chiến lược đặc biệt |

### 2.3 Keyword Opportunity (380 từ khóa, 38.050 SV/tháng)

| Cluster | SV/tháng | Ghi chú |
|---|---|---|
| eSIM Chung | 8.510 | Hub page |
| eSIM + SIM Trung Quốc | 7.850 | Trang lớn nhất - có GFW caveat |
| Sim Ngoại Quốc Chung | 4.100 | Hub + blog |
| Thái Lan | 3.930 | Destination page |
| Nhật Bản | 1.950 | Destination page |
| Singapore | 1.530 | Destination page |
| Cẩm nang / How-to | 1.430 | Blog cluster |
| Hàn Quốc | 1.160 | Destination page |
| Châu Âu | 1.090 | Destination page |
| Mỹ | 900 | Destination page |

**SEM keyword data (bổ sung):**

| Cluster SEM | Tổng SV | Keywords tiêu biểu |
|---|---|---|
| Sim Trung Quốc | 5.510 | `sim trung quốc` (1.600), `mua sim trung quốc` (1.000) |
| Travel Sim Overall | 4.080 | `esim du lịch` (1.300), `sim du lịch` (880) |
| Sim Hàn Quốc | 1.450 | `sim hàn quốc` (320), `esim hàn quốc` (320) |
| Sim Việt Nam (inbound) | 600 | `sim du lịch việt nam` (390) |

**4 Strategic Observations:**

1. **Intercept competitor intent:** `cách chuyển vùng quốc tế viettel` (1.000 SV) + `mobi` (260 SV) = 1.260 SV user đang tìm giải pháp thay thế — moment dễ convert nhất. Cần 1 bài blog comparison capture query này.
2. **Bilingual queries đáng kể:** `esim thailand` (480), `china esim` (170), `korea esim` (110) — người Việt search tiếng Anh khi biết rõ điểm đến. Xử lý bằng bilingual title tag + H2 trong body, không cần trang riêng.
3. **Loại keyword sai intent:** `mua sim trung quốc vĩnh viễn` (390 SV) — nhu cầu SIM vật lý dài hạn, không match eSIM du lịch. Loại khỏi danh sách.
4. **Branded competitor keywords:** `sim klook` (50), `esim gigago` (70) — chỉ intercept qua blog comparison, cần approval trước khi viết.

---

## 3. Business Context & Market Intelligence

### 3.1 User Funnel (A30 Base)

| Stage | Số lượng | % Base | CR sang stage tiếp |
|---|---|---|---|
| Tổng A30 Users | 12.8M | 100% | - |
| Du lịch nước ngoài (2025) | 771K | 6.0% | 6% |
| Dùng SIM kết nối mạng | 331K | 2.6% | 43% |
| Trực tiếp mua SIM | 159K | 1.2% | 48% |

*Lưu ý: Chỉ 48% người dùng SIM trực tiếp mua — phần còn lại mua hộ người khác hoặc 1 người phát hotspot cho cả nhó.*

### 3.2 Market Sizing

| Metric | Giá trị |
|---|---|
| TAM (tổng chi tiêu SIM du lịch A30) | ~171 tỷ VNĐ/năm |
| SAM (nhóm mua SIM online) | ~143.5 tỷ VNĐ/năm |
| MoMo GMV hiện tại (2025) | 16 tỷ VNĐ (~11% SAM) |
| Target GMV 2026 | 48 tỷ VNĐ (+300%) |

### 3.3 KPI Targets Q3/2026

| KPI | T7/2026 | T8/2026 (PEAK) | T9/2026 (PEAK) | Q3 Total | vs Q2 |
|---|---|---|---|---|---|
| MAU | 32.520 | 31.219 | 43.707 | 107.446 | +77% |
| Trans | 48.780 | 46.829 | 65.560 | 161.169 | +77% |
| GMV (VNĐ) | 8.29 tỷ | 7.96 tỷ | 11.15 tỷ | 27.4 tỷ | +77% |

### 3.4 Web Contribution Target

| Metric | T7/2026 | T8/2026 | T9/2026 |
|---|---|---|---|
| Web % contribution | 4% | 6% | 10% |
| Web Trans (absolute) | 1.951 | 2.810 | 6.556 |
| Web GMV | 331.7M VNĐ | 477.6M VNĐ | 1.114.5M VNĐ |

### 3.5 Destination Data - Lượt khách Việt xuất cảnh (2024)

| Quốc gia | Lượt khách VN | FIT ratio | Est. FIT | Audience chính |
|---|---|---|---|---|
| Trung Quốc | ~1.400.000 | 62% | 868.000 | FIT + GIT |
| Thái Lan | ~920.000 | 58% | 533.600 | FIT |
| Nhật Bản | ~710.000 | 35% | 248.500 | GIT |
| Hàn Quốc | ~615.000 | 62% | 381.300 | FIT |
| Singapore | ~480.000 | 75% | 360.000 | FIT |
| Malaysia | ~420.000 | 65% | 273.000 | FIT |

*FIT = Free Independent Traveler (tự đi, target chính cho eSIM online). GIT = Group Inclusive Tour (đi đoàn, thường guide lo SIM).*

### 3.6 Định vị MoMo cho SIM Du Lịch

> "MoMo là kênh mua SIM du lịch **nhanh - giá hợp lý - an tâm sử dụng**"

- **Mua nhanh - ít bước:** flow mua SIM đơn giản, chỉ 2 bước
- **Giá hợp lý:** đảm bảo không cao hơn thị trường quá 10–20K
- **An tâm sử dụng:** HDSD rõ ràng, hỗ trợ 24/7, đồng hành suốt chuyến đi

### 3.7 Định hướng tăng trưởng 2026

- **Product-led growth:** Cải tiến tập trung vào NHANH-TIỆN tạo khác biệt, tối đa CR
- **SKU & Promotion:** Đa dạng gói, giá cạnh tranh
- **Marketing & Communication:** Cross Border phục vụ toàn bộ hành trình du lịch, tập trung community/UGC/authentic review
- **Partnership:** Hợp tác chặt chẽ với Gohub
- **Source of Growth mới:** **Kênh Web** — dựa trên hành vi tìm kiếm Google của khách du lịch (đây là scope BRD này)

---

## 4. User Insight & Hành vi mua

### 4.1 Bản chất hành vi mua SIM du lịch (FCB Model)

SIM du lịch thuộc nhóm **Habitual** trong FCB Grid:
- **Low involvement + Thinking** → Do → Learn → Feel
- Quyết định nhanh, ít cân nhắc phức tạp; mua vì tiện, thường sát ngày đi (~1 tuần trước bay)

**Implication cho web content:**
- Destination pages phải siêu lean (<800 từ body) — user không muốn đọc nhiều
- CTA phải rõ ràng và immediate — giảm friction tối đa
- Blog cluster phục vụ AWARENESS stage, không phải decision stage
- Giá là tiêu chí loại trừ nhanh — phải hiển thị giá rõ ràng, competitive

### 4.2 Kênh mua & Phân bổ User

- **85% user** đã mua ít nhất 1 kênh online; 15% chỉ mua offline
- Trong nhóm online: **74% mua eSIM**, 26% SIM vật lý
- Trong nhóm offline: 38% eSIM, **62% SIM vật lý**

| Metric | Nhóm Online (85%) | Nhóm Offline (15%) |
|---|---|---|
| Profile | Nữ, trẻ, độc thân/chưa có con, đi DL thường xuyên | Nam, lớn tuổi, có con, ít đi DL |
| Số SIM/lần mua | Mean 2.13 SIM/người | Mean 1.78 SIM/người |
| Dung lượng | Mean 2.66 GB/ngày (1-3GB chủ yếu) | Mean 3.66 GB/ngày (>5GB) |
| Giá trung bình | 213.586 VNĐ/SIM | 284.381 VNĐ/SIM |
| Hành vi | Nhạy cảm giá, tối ưu gói phù hợp | Sẵn sàng chi, cần HDSD rõ ràng |

*Insight: Nhóm online mua trung bình 2+ SIM/lần (mua hộ). Web nên highlight combo/multi-buy. Dung lượng 1-3GB/ngày là sweet spot cho pricing display.*

### 4.3 Đánh giá kênh mua (User feedback)

| Kênh | Điểm hài lòng | Điểm không hài lòng |
|---|---|---|
| **MoMo** | Giao dịch nhanh & tiện, dễ thao tác, tin tưởng brand | Giá chưa rẻ nhất, ít voucher, thiếu HDSD kích hoạt |
| **Sàn TMĐT** | Đa dạng gói, giá tốt, nhiều review | CSKH kém, khó liên hệ shop |
| **App du lịch** | Tiện lợi, nhận eSIM nhanh | Ít khuyến mãi |
| **Website SIM** | Tư vấn hỗ trợ 24/7, dễ mua/sử dụng | - |

**Leverage cho web:** MoMo mạnh ở "giao dịch nhanh + trust" nhưng yếu ở "giá & hướng dẫn". Web content phải address cả hai: (1) Hướng dẫn kích hoạt rõ ràng trong How-to section; (2) Nhấn mạnh "giá hợp lý" thay vì "giá rẻ nhất" — tránh cuộc chiến giá.

---

## 5. Customer Journey & JTBD

### 5.1 Main JTBD

> "Khi tôi chuẩn bị cho một chuyến đi quốc tế và cần đảm bảo có internet xuyên suốt hành trình, tôi muốn có một giải pháp kết nối phù hợp với điểm đến — mua nhanh, kích hoạt dễ và dùng ổn định từ lúc hạ cánh đến khi về nước, để tôi có thể tự tin tận hưởng chuyến đi mà không lo phí roaming, không panic vì mất sóng và không bị động trước những tình huống cần kết nối ở nước ngoài."

### 5.2 Journey Map - Web Cluster Serves Giai đoạn 1-3

| Giai đoạn | JTBD | MoMo Serve | Pain Point |
|---|---|---|---|
| **1. Khám phá** | Hiểu nhanh nên dùng eSIM/SIM vật lý/roaming | Yếu - không có education layer | CAO |
| **2. Tìm quốc gia** | Xác nhận MoMo có gói cho điểm đến | Trung bình - search yếu, không suggest SKU | CAO |
| **3. Tìm gói** | So sánh nhanh để tìm gói phù hợp | Trung bình - thiếu comparison view, review | RẤT CAO |
| **4. Chọn gói** | Lock-in chính xác, tránh sai sót | Tốt - buy flow nhanh | TRUNG BÌNH |
| **5. Nhập thông tin** | Thông tin điền sẵn, giảm sai sót | Yếu - phải nhập lại mỗi lần | CAO |
| **6. Thanh toán** | Thanh toán 1 chạm, voucher tự động | Tốt - best-in-class fintech UX | THẤP-TB |
| **7. Kích hoạt** | Kích hoạt ngay trong app, hướng dẫn theo OS | Yếu - 5+ bước thủ công | RẤT CAO |
| **8. Sử dụng** | Xem data, nhận cảnh báo, top-up 1 chạm | Yếu - không có touchpoint native | CAO |
| **9. Sau về nước** | Dọn eSIM cũ, lưu trip history, referral | Yếu - không có retention loop | CAO |

**Web cluster serve chủ yếu Giai đoạn 1-3 (Trước giao dịch):**
- **GĐ 1:** Hub page + Blog education giải quyết knowledge gap
- **GĐ 2:** Destination Grid + Destination pages = country-first navigation
- **GĐ 3:** Product Table + FAQ giảm decision paralysis

*Hai pain point RẤT CAO: GĐ 3 (trust gap) và GĐ 7 (kích hoạt UX gap). Web cluster giải GĐ 3. GĐ 7 thuộc scope product team.*

### 5.3 Pain Points chi tiết liên quan đến Web Scope

**GĐ 1 - Khám phá:** MoMo không phải "first thought" cho SIM du lịch. User phải tự Google để hiểu eSIM vs SIM vs roaming. → Blog "eSIM là gì", "Chuyển vùng vs eSIM" capture search intent.

**GĐ 2 - Tìm quốc gia:** User nghĩ theo quốc gia trước, gói SIM sau (mental model). Search Google bằng "[quốc gia] + sim/esim" rất phổ biến. → Destination pages với URL pattern `/esim-du-lich/{country}`.

**GĐ 3 - Tìm gói:** Trust gap (không có review/rating/social proof); Decision paralysis (quá nhiều SKU giống nhau). → Product Table với highlight "Bán chạy nhất", FAQ giải đáp concerns, AEO content.

---

## 6. Định Hướng Dự Án

### Dự án phục vụ điều gì?

Xây dựng cluster web eSIM Du Lịch thành kênh organic acquisition hiệu quả, convert traffic thành lượt mở app và mua hàng, contribute vào target web 4–10% Trans từ T7/2026. Đây là Source of Growth mới dựa trên hành vi tìm kiếm Google của khách du lịch — touchpoint web hiện MoMo chưa có.

### Ai được phục vụ?

| User Segment | Nhu cầu chính | Volume indicator |
|---|---|---|
| FIT (tự đi, chuẩn bị trước) | Mua eSIM theo quốc gia trước chuyến đi | Cluster destination pages |
| Người so sánh giải pháp | eSIM vs roaming vs SIM vật lý | Blog comparison, hub FAQ |
| Người mua hộ cho nhóm | Mua 2+ SIM, cần hiểu rõ trước khi quyết định | Product table + FAQ |

### Trong scope

- Hub Page: `/esim-du-lich` — 1 trang, full component build
- Destination Pages: 10 trang theo URL `/esim-du-lich/{country-slug}`
- Blog Cluster: ~10 bài theo 3 tier (education, destination, comparison)
- Deep Link Integration: Web → MoMo App (iOS + Android), fallback App Store nếu chưa cài
- Schema Markup: FAQPage, HowTo, Product, AggregateOffer, BreadcrumbList trên tất cả trang
- Gohub API Integration: fetch giá và danh sách gói real-time (không hardcode)
- GA4 Event Tracking + UTM Framework chuẩn hóa

### Ngoài scope

- App-side UI/UX cho màn hình eSIM trong MoMo App
- Hệ thống inventory / fulfillment phía Gohub/Xplori/Mobi Inbound
- Social media / paid campaign cho eSIM cluster
- Đa ngôn ngữ (chỉ tiếng Việt + bilingual title/H2 khi cần)
- Trang so sánh competitor trực tiếp (cần approval riêng)
- Subdomain esim.momo.vn — dùng subdirectory `/esim-du-lich/` để giữ domain authority

---

## 7. Kiến Trúc & Scope Build

### 7.1 URL Architecture

**Hub:**

| URL | SV/tháng | Content Type |
|---|---|---|
| /esim-du-lich | 8.510+ | Hub Pillar — navigation + education + AEO |

**Destination Pages (10 trang):**

| URL | SV/tháng | Ghi chú |
|---|---|---|
| /esim-du-lich/trung-quoc | 7.850 | GFW disclaimer bắt buộc — không publish trước khi confirm với Gohub |
| /esim-du-lich/thai-lan | 3.930 | |
| /esim-du-lich/nhat-ban | 1.950 | |
| /esim-du-lich/singapore | 1.530 | |
| /esim-du-lich/han-quoc | 1.160 | |
| /esim-du-lich/chau-au | 1.090 | 1 gói cover toàn Schengen |
| /esim-du-lich/my | 900 | |
| /esim-du-lich/uc | 790 | |
| /esim-du-lich/dai-loan | 700 | |
| /esim-du-lich/malaysia | 610 | |

**Blog Cluster:**

| URL | Target keyword | SV | Ghi chú |
|---|---|---|---|
| /blog/esim-la-gi | `esim du lịch là gì` | ~200 | AEO priority, HowTo schema |
| /blog/esim-vs-chuyen-vung | `cách chuyển vùng quốc tế viettel/mobi` | 1.260 | Intercept competitor query |
| /blog/cach-mua-esim-tren-momo | `mua esim du lịch` | ~200 | How-to focus |
| /blog/dien-thoai-ho-tro-esim-2026 | `điện thoại hỗ trợ esim` | ~50 | Update 6 tháng/lần |
| /blog/esim-trung-quoc-co-vao-google-khong | `esim trung quốc` | ~790 | Publish đồng thời với /trung-quoc |
| /blog/esim-thai-lan | `esim thailand`, `sim dtac thái lan` | ~530 | |
| /blog/kinh-nghiem-esim-nhat-ban | `esim nhật bản` | ~340 | |
| /blog/esim-chau-au | `esim du lịch châu âu` | ~220 | |
| /blog/klook-esim-vs-momo-esim | `klook esim` | - | Cần legal approval trước khi viết |
| /blog/airalo-vs-gohub-vs-momo-esim | `esim airalo` | - | Cần legal approval + verify giá đối thủ |

**URL Rules:**
- Lowercase, hyphenated, không dấu tiếng Việt
- Không query params trong URL cấu trúc
- Tối đa 75 ký tự (không tính domain)
- **Lưu ý SEM:** SEM sitelinks hiện dùng `/esim-du-lich/khu-vuc/{country}` — cần align hoặc redirect trước khi launch tránh duplicate content.

### 7.2 Hub Page Anatomy

| Section | Thành phần | Schema |
|---|---|---|
| Hero | H1 + 3 trust signals (QR · 150+ quốc gia · Hoàn tiền) + CTA Primary + CTA Secondary | WebPage, BreadcrumbList |
| Answer Block | "eSIM Du Lịch Là Gì?" — 60-80 từ + bảng so sánh 3 cột (eSIM/SIM vật lý/Roaming) | FAQPage |
| Destination Grid | 10 card: Flag + Quốc gia + Giá từ [X]đ + Link đến destination page | - |
| How-to 4 bước | Mở app → Chọn gói → Thanh toán → Nhận QR/kích hoạt | HowTo |
| FAQ Block | 8 câu AEO priority (xem Appendix A) | FAQPage |
| Cross-sell | Link Bảo hiểm du lịch + Blog cards | - |

### 7.3 Destination Page Anatomy

| Section | Thành phần | Schema |
|---|---|---|
| Hero | H1 pattern: "eSIM [Quốc Gia] ([EN Name]) - [Gói phổ biến] / Từ [Giá]đ" + Breadcrumb | Product, BreadcrumbList |
| Product Table | Thời hạn · Dung lượng · Tốc độ · Giá (từ API) · CTA "Mua Ngay" — highlight "Bán chạy nhất" | AggregateOffer, PriceSpecification |
| Country Context | 100-150 từ về đặc thù kết nối tại quốc gia | FAQPage |
| FAQ | 5-7 câu riêng theo quốc gia | FAQPage |
| Related Destinations | 3-4 trang liên quan về địa lý/trip pattern | - |
| Sticky CTA | Floating button visible toàn scroll: "[Flag] Mua eSIM [Quốc Gia]" | - |

**Bilingual title spec (địa chỉ bilingual queries):**

| Destination | Title tag | H2 bilingual trong body |
|---|---|---|
| Thái Lan | "eSIM Thái Lan (Thailand eSIM) - Gói Cước & Mua Ngay" | "Thailand eSIM Plans for Vietnamese Travelers" |
| Trung Quốc | "eSIM Trung Quốc (China eSIM) - Kết Nối Không Giới Hạn" | "China eSIM - What You Need to Know" |
| Hàn Quốc | "eSIM Hàn Quốc (Korea eSIM) - Mua Nhanh Kích Hoạt Ngay" | "Korea eSIM - Compare Plans" |
| Singapore | "eSIM Singapore - Gói Data & Giá Tốt Nhất 2026" | "Singapore eSIM Options Compared" |
| Châu Âu | "eSIM Châu Âu (Europe eSIM) - 1 Gói Cho Cả Schengen" | "Europe eSIM - Cover Multiple Countries" |

### 7.4 Content Strategy

**Tone & Voice:** MoMo là người bạn hiểu công nghệ đang giúp chuẩn bị chuyến đi — không phải travel blogger, không phải sales rep. Thân thiện + có chuyên môn. Ngắn gọn nhưng đủ để quyết định (FCB Habitual).

**Rules bắt buộc:**
- Câu đầu mỗi đoạn = point chính (không warm-up)
- Claim phải có evidence (số liệu, so sánh giá cụ thể)
- Mỗi comparison section kết thúc bằng verdict 1 câu "Chọn X nếu... Chọn Y nếu..."
- Giá không hardcode nếu có thể thay đổi
- Tuyệt đối không address Great Firewall trong trang Trung Quốc nếu chưa confirm với Gohub

**Blog Tier:**

| Tier | Mô tả | Word count | Schema |
|---|---|---|---|
| Tier 1 | Education — phải có | 1.000-2.000 từ | Article, FAQPage, HowTo |
| Tier 2 | Destination-specific | 800-1.500 từ | Article, FAQPage |
| Tier 3 | Competitor comparison | 1.200-2.000 từ + bảng | Article, FAQPage + Legal approval |

### 7.5 SEM-SEO Feedback Loop

SEM đang live cho SIM Du Lịch. Dữ liệu SEM bổ sung liên tục cho SEO:

| Action | Mô tả |
|---|---|
| Top performing SEM queries → SEO target | Queries có CTR + conversion cao từ SEM ưu tiên trong SEO content |
| SEM landing page migration | Khi cluster live, redirect SEM destination URLs sang trang mới trong cluster |
| SEM negative keywords → SEO exclude | Keywords SEM đã loại vì sai intent → loại khỏi SEO target |
| SEM ad copy testing → SEO title/meta | Headlines SEM có CTR cao → test làm title tag/meta description |

**Organic traffic baseline (thực tế):**

| Metric | T1/2026 | T3/2026 | T6/2026 | T9/2026 (target) |
|---|---|---|---|---|
| Organic traffic | 25.724 | 31.992 | 27.391 | 42.907 |
| Paid traffic | 41.224 | 14.116 | 51.594 | 55.635 |
| CR MAU/Traffic | 4.98% | 8.23% | 6.64% | 7.85% |

*Insight: Organic traffic dao động 25-43K/tháng nhưng không growth. Web cluster cần tạo organic growth engine ổn định, giảm phụ thuộc paid.*

### 7.6 Technical Standards (Gate bắt buộc)

| Standard | Requirement |
|---|---|
| LCP | < 2.5s (mobile 4G) |
| CLS | < 0.1 — lưu ý khi API load async |
| INP | < 200ms |
| Schema validation | 0 error trên Google Rich Results Test trước publish |
| Deep link | Test pass iOS + Android, cả installed và not installed |
| Giá | Fetch từ Gohub API (không hardcode) — fallback "Xem giá trong app" nếu API timeout |
| Mobile CTA | Sticky button visible toàn scroll, không bị overlap bởi browser chrome (iOS Safari) |

### 7.7 Product Roadmap Alignment

Web cluster là một phần trong chiến lược tăng trưởng tổng thể. Các in-app features quan trọng cần track để align content:

**Wave 1 (May-Aug 2026) — Quick Wins:**
- Auto-fill + Save profile + Price breakdown
- Smart Feature Tags (Hotspot/App/Speed)
- Persistent Entry Point + Smart Search
- In-app eSIM Activation (pain point lớn nhất — sẽ giảm từ 5+ bước xuống 1 chạm)
- Smart Package Comparison

**Wave 2 (Aug-Nov 2026) — Growth Lever:**
- Cross-trigger từ Booking (vé, khách sạn)
- Social Proof Layer (review, rating)
- Data Usage Dashboard
- Pre-trip Reminder System

**Web ↔ Product Dependencies:**

| Web Feature | Phụ thuộc Product Feature | Ghi chú |
|---|---|---|
| Highlight "Bán chạy nhất" trong Product Table | Smart Package Comparison | Dùng cùng logic "most popular" |
| Blog "Cách kích hoạt eSIM" | In-app eSIM Activation | Cập nhật content khi tính năng live |
| FAQ "Mua eSIM ở đâu uy tín" | Social Proof Layer | Bổ sung data khi feature live |
| Cross-sell Block trên Hub | Cross-trigger Booking | Align danh sách cross-sell |

---

## 8. Success Metrics

### Objective
Xây dựng cluster web eSIM Du Lịch thành kênh organic acquisition hiệu quả, contribute 4–10% Trans từ T7/2026.

### Key Results

| KR | Metric | Target | Tracking |
|---|---|---|---|
| KR1 | Organic Clicks — `/esim-du-lich/*` | +40% vs baseline | GSC |
| KR2 | Average Position — top 5 keywords | Top 10 | GSC |
| KR3 | AI Overview Appearances | ≥ 3 FAQ queries cited | GSC / Manual audit |
| KR4 | Click-to-App Rate (web → app, mobile) | > 3% | GA4 + Appsflyer |
| KR5 | New Users từ eSIM Funnel | Grow MoM | Appsflyer |
| KR6 | FAQ Schema Eligibility | 0 error, ≥ 5 FAQ indexed/trang | GSC Enhancements |
| **KR7** | **Web Trans contribution** | **4% T7 → 10% T9/2026** | **GA4 + Appsflyer** |
| **KR8** | **Web GMV** | **≥ 1.1 tỷ VNĐ (T9/2026)** | **GA4 + Internal** |

*Baseline measurement: đo toàn bộ metrics ngay sau khi publish Hub + 2 destination pages đầu tiên.*

### GA4 Events

| Event | Trigger | Key Parameters |
|---|---|---|
| `esim_cta_click` | Click bất kỳ CTA trong cluster | page_type, country, cta_position |
| `esim_deeplink_click` | Click deep link → app | country, source_page |
| `esim_faq_expand` | Expand FAQ accordion | question_id, page_type |
| `esim_product_view` | User scroll đến product table | country, packages_loaded |
| `esim_blog_cta_click` | Click CTA trong blog | blog_slug, cta_position |

---

## 9. Dependencies & Constraints

| Dependency | Mô tả | Blocker? |
|---|---|---|
| Gohub API spec (endpoint, auth, response format) | Cần trước khi Dev build product table | Yes |
| Gohub xác nhận gói VPN cho trang Trung Quốc | Không publish `/esim-du-lich/trung-quoc` trước khi có thông tin này | Yes |
| Deep link scheme từ App team | CTA trên web không hoạt động nếu thiếu | Yes |
| CMS support schema injection | Xác nhận trước khi build để plan effort | Yes |
| Legal approval cho Blog Tier 3 (comparison) | Blog comparison bị delay nếu không có sớm | No |
| SEM URL migration alignment | Cần quyết định URL pattern `/khu-vuc/` vs `/` trước khi build | Yes |
| DA Team — GA4 events setup | Phải có trước khi publish để có baseline | Yes |

**Constraints:**
- Gói eSIM Trung Quốc: không publish trang nếu chưa xác nhận khả năng bypass GFW từ Gohub.
- Giá không được hardcode bất kỳ đâu — phải fetch từ API.
- Không tạo subdomain — dùng subdirectory `/esim-du-lich/` để giữ domain authority.
- Blog comparison competitor cần legal approval và verify giá đối thủ trước khi publish.

---

## 10. Risk Assessment

| # | Rủi ro | Khả năng | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Gohub API không stable, timeout thường xuyên | Medium | High | Fallback "Xem giá trong app" + cache 15 phút |
| R2 | Gói eSIM TQ không bypass GFW — user disappointed | High | High | Disclaimer rõ ràng bắt buộc, xác nhận với Gohub trước publish |
| R3 | CMS không support schema injection | Medium | Medium | Dev inject qua code thay vì CMS plugin |
| R4 | Deep link fail trên device cụ thể | Low | Medium | Test matrix đủ device, có fallback URL |
| R5 | Competitor publish trang tốt hơn trong thời gian build | Medium | Medium | Ưu tiên Hub + TQ + Thái Lan live trước |
| R6 | SEM/SEO URL conflict tạo duplicate content | Medium | Medium | Quyết định URL pattern trước khi build, redirect cái còn lại |
| R7 | Web cluster launch delay → miss web contribution target T7 | Medium | High | Scope tối thiểu khả thi: Hub + 1 Destination + 1 Blog |

---

## Appendix A: 8 AEO Priority Questions (Hub FAQ)

*Format: 40-60 từ per answer, câu đầu = answer trực tiếp.*

**Q1. eSIM du lịch là gì? Khác SIM vật lý thế nào?**
eSIM (embedded SIM) là SIM điện tử tích hợp sẵn trong điện thoại, kích hoạt qua QR code mà không cần cắm SIM vật lý. Khi đi du lịch, bạn mua eSIM online, nhận QR code, quét là có mạng ngay khi xuống máy bay — không cần xếp hàng mua SIM tại sân bay.

**Q2. Nên mua eSIM hay chuyển vùng quốc tế?**
eSIM du lịch rẻ hơn chuyển vùng từ 60-80% và không cần đăng ký hay hủy gói sau chuyến đi. Chuyển vùng quốc tế phù hợp nếu bạn chỉ đi 1-2 ngày và cần giữ số điện thoại Việt Nam để nhận OTP liên tục.

**Q3. Điện thoại nào hỗ trợ eSIM?**
iPhone XS (2018) trở lên, Samsung Galaxy S21 trở lên, Google Pixel 3 trở lên đều hỗ trợ eSIM. Đến 2025-2026, hầu hết flagship đều tương thích. Kiểm tra nhanh: vào Cài đặt → Thông tin điện thoại → xem có mục "eSIM" hay không.

**Q4. Mua eSIM bao lâu trước chuyến đi?**
Nên mua eSIM trước 1-3 ngày để có thời gian cài đặt và test kết nối. eSIM MoMo giao trong vài phút qua QR code — nhưng không nên để sát giờ bay vì cần kiểm tra thiết bị tương thích.

**Q5. eSIM Trung Quốc có dùng được Google, Facebook không?**
Trung Quốc chặn Google, Facebook, Instagram (Great Firewall). eSIM thông thường không bypass được trừ khi gói eSIM đó có tích hợp VPN. Trước khi mua, xác nhận với nhà cung cấp gói có support VPN hay không.

**Q6. 1 eSIM dùng được mấy máy?**
Mỗi eSIM du lịch chỉ dùng được cho 1 thiết bị. Sau khi quét QR code và cài vào máy, mã QR đó không thể dùng lại trên máy khác. Nếu đi cùng nhiều người, mỗi người cần mua 1 gói riêng.

**Q7. Mua eSIM du lịch ở đâu uy tín?**
Có thể mua qua MoMo, Airalo, Gohub, Klook. MoMo cung cấp eSIM qua đối tác Gohub, hỗ trợ 150+ quốc gia, thanh toán bằng ví MoMo, hoàn tiền nếu không kết nối được.

**Q8. Cách kích hoạt eSIM như thế nào?**
Sau khi mua: (1) Vào Cài đặt → Điện thoại → Thêm eSIM; (2) Chọn "Quét QR code"; (3) Quét mã nhận được sau khi mua; (4) Xác nhận cài đặt. Toàn bộ quá trình mất khoảng 2-3 phút. Nên kích hoạt khi còn ở Việt Nam để test trước.

---

## Appendix B: Destination FAQ Samples

### `/esim-du-lich/trung-quoc`
- eSIM Trung Quốc có bypass được Great Firewall (Google, Facebook) không?
- Gói nào trên MoMo có hỗ trợ VPN tại Trung Quốc?
- Tôi có thể dùng Google Maps ở TQ với eSIM này không?
- Nên tải VPN trước khi đi hay sau khi đến TQ?

### `/esim-du-lich/thai-lan`
- eSIM Thái Lan gói Unlimited có thực sự không giới hạn không?
- AIS hay True Move H - gói nào tốt hơn?
- eSIM có dùng được ở đảo Koh Samui, Koh Phangan không?
- Có thể chia sẻ hotspot (tethering) từ eSIM Thái Lan không?

### `/esim-du-lich/nhat-ban`
- eSIM Nhật Bản có nhắn tin SMS về Việt Nam được không?
- Coverage ở Hokkaido và vùng nông thôn có ổn không?
- eSIM có dùng được trên Shinkansen không?
- Gói nào phù hợp cho chuyến 10 ngày Tokyo-Osaka-Kyoto?

### `/esim-du-lich/chau-au`
- 1 gói eSIM Châu Âu dùng được bao nhiêu nước?
- Croatia, Albania, Montenegro có nằm trong vùng phủ sóng không?
- Tôi đi 3 tuần qua 6 nước Schengen - nên mua 1 gói hay mua từng nước?
- eSIM có hoạt động ở Anh (UK) sau Brexit không?

---

## Change Log
- **Tháng 5/2026 (v1.0):** Khởi tạo — keyword research, competitive analysis, URL architecture.
- **Tháng 5/2026 (v1.2):** Bổ sung Business Context & Market Intelligence, User Insight, Customer Journey & JTBD, SEM-SEO Feedback Loop, Product Roadmap Alignment.
- **Tháng 5/2026 (v1.3):** Chuẩn hóa tài liệu — loại bỏ liên kết nội bộ, tên nhân sự, code blocks kỹ thuật, FR codes, Sprint Plan, Definition of Done; chuẩn bị cho Head of BU / C-Level review.
