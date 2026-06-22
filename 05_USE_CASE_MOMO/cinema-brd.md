# BRD: Cinema

> - **Project:** Use Case Cinema - Web Growth Strategy Q2-Q4/2026
> - **Main URL:** momo.vn/cinema
> - **Division:** MDS (Marketing Distribution Services)
> - **Use Case:** Cinema
> - **Owner:** Web Platform
> - **Governance:** Web Product Lead (Hiến)
> - **Version:** 2.1 - Tháng 5/2026
> - **Status:** Draft - Cần align PO Cell + Dev Lead

---

> **Problem:** Hàng triệu user tìm lịch chiếu phim mỗi tháng - nhưng không tìm thấy MoMo, dù MoMo chính là nơi họ sẽ mua vé.
> **KPI Owned:** Transactions (số vé bán) từ /cinema/* → attributed via Appsflyer
> **Conversion Flow:** "lịch chiếu CGV" → /cinema/rap/cgv/{slug} → "Đặt vé ngay" → App open → Transaction confirmed

---

## 1. Executive Summary

### Situation

Cinema là Use Case trưởng thành nhất của MoMo trong mảng Out-App Traffic: ~1M organic/3 tháng Q1/2026, Top 1 SERP cho "vé xem phim", Top 3-5 cho cluster rạp theo địa điểm. Business model là commission per transaction qua 8 partner chain (CGV, Lotte, Galaxy, BHD Star, Mega GS, Dcine, Cinestar, Beta). Ecosystem position: Discovery (SERP/AIO) → momo.vn/cinema → Transaction (App) → Retention (cross-sell).

### Complication

Traffic lớn nhưng MoMo chỉ đang khai thác được một phần nhỏ thị trường Cinema trên web - 3 vấn đề chiến lược cần giải quyết để bứt lên tier tiếp theo:

1. **Keyword gap lớn chưa capture** - "Phim chiếu rạp" (102,820/tháng), "Rạp chiếu phim" (74,000/tháng), "Galaxy Cinema" (100,030/tháng) - tất cả ngoài Top 50. MoMo đang top cho branded queries của chain cụ thể nhưng bỏ lỡ toàn bộ discovery queries có volume cao nhất thị trường.
2. **AI Overview threat** - Google AI Overview đã xuất hiện cho "mua vé xem phim" và "lịch chiếu CGV". Nếu không xây structured data đầy đủ theo từng phase, MoMo sẽ bị squeeze khỏi top-of-page result từ 2026 trở đi.
3. **Content lifecycle chưa có system** - Cinema là use case realtime cao, phim liên tục ra rạp và hết rạp. Nếu không có system tự động manage content theo trạng thái phim, content sẽ outdated nhanh và mất ranking theo thời gian.

### Resolution

Chiến lược Q2-Q4/2026 vận hành 3 vector song song: (1) **URL Lifecycle System** - tự động hóa quản lý content theo 4 phases (Pre-release → Showing → Post-release → Archive), đảm bảo content luôn relevant với intent user tại từng giai đoạn, giữ link equity; (2) **Programmatic Scale** - xây 500+ URLs rạp × phim × lịch chiếu để capture keyword gap và tạo defensive long-tail layer; (3) **AEO/GEO Moat** - schema đầy đủ per phase để được cite trong AI Overview trước khi AI traffic thay thế organic.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Performance

| Metric | Q1/2026 (Baseline) | 2025 Full Year |
|---|---|---|
| Organic Traffic | 1,066,000 | 6,387,700 |
| Total Traffic | 2,980,000 | 12,425,040 |
| Booking Clicks | 81,517 | 266,258 |
| Traffic to App | 9,866 | 78,735 |
| Transactions (via App) | 9,212 | 52,311 |
| %CR (App Transaction/W2A) | 93.4% | 66.4% |

### 2.2 Keyword Ranking Hiện Tại

**Nhóm Rạp & Lịch chiếu (intent: Navigational + Transactional):**

| Keyword | Volume | Ranking hiện tại |
|---|---|---|
| Lịch chiếu phim CGV | 135,000 | #4-10 |
| Lịch chiếu phim | 90,500 | #3 |
| Phim chiếu rạp | 102,820 | Ngoài Top 50 |
| Galaxy Cinema | 100,030 | Ngoài Top 50 |
| Rạp chiếu phim | 74,000 | Ngoài Top 50 |
| Lịch chiếu phim Galaxy | 10,000 | #2-3 |
| Giá vé CGV | 10,020 | #1 |

**Gap lớn nhất:** "Phim chiếu rạp" (102,820/tháng), "Rạp chiếu phim" (74,000/tháng), "Galaxy Cinema" (100,030/tháng) - tổng ~280K/tháng ngoài Top 50. Đây là discovery queries có volume cao nhất thị trường chưa được capture.

### 2.3 Competitive Landscape

| Competitor | Strengths | Weaknesses | MoMo Advantage |
|---|---|---|---|
| moveek.com | Community review, long-tail phim indie | Không có transaction flow | Transaction liền mạch + ưu đãi |
| vnpay.vn | Similar payment infra, hub lịch chiếu per chain | Traffic base nhỏ, brand yếu ở entertainment | MoMo brand recall mạnh hơn |
| cgv.vn, galaxycine.vn | Authority gốc về chain của họ | Mỗi rạp 1 silo, user phải search từng chain | Hub aggregator - 1 điểm, nhiều chain |
| rapchieuphim.com | Content depth, long-tail location | Không có payment, UX cũ | End-to-end flow |

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi

User tìm phim đang chiếu hoặc lịch chiếu theo rạp - tìm thấy thông tin realtime chính xác trên momo.vn - mua vé ngay trong 1 flow mà không cần rời trang tìm kiếm.

**PLG Hook:** Booking flow là PLG hook tự nhiên - user đến với commercial intent cao, product chỉ cần serve đúng intent thì tự convert, không cần campaign hay push. "Nhắc tôi khi mở bán" (Phase 1) là PLG hook bổ sung tạo repeat engagement khi phim chưa ra rạp.

3 outcomes phát sinh tự nhiên khi product job được giải quyết đúng:
- **Transaction revenue:** Commission per ticket - North Star của dự án
- **Programmatic moat:** 500+ URLs rạp × phim capture toàn bộ keyword gap
- **Defensive AEO:** Schema đầy đủ bảo vệ traffic trước AI Overview shift dài hạn

### 3.2 Dự Án Này KHÔNG Phải

- Không build mobile app - scope của Mobile/MDS team
- Không xây platform streaming hay video-on-demand
- Không bao gồm SEO cho MoMo blog general - chỉ /cinema/*
- Không cover performance marketing hay paid media
- Không bao gồm backend partner API negotiation

**Target user:**
- User đi xem phim cuối tuần (18-35, đô thị, mobile payment habit) - search "lịch chiếu + rạp", "phim đang chiếu"
- User discover phim - search "top phim hay", "review phim"
- User lookup thông tin rạp cụ thể - search "CGV Aeon Canary lịch chiếu"

---

## 4. JTBD Analysis

### Job #1: Transact - "Tôi cần đặt vé ngay"

> "Khi tôi đã chọn được phim + rạp + suất chiếu, tôi cần mua vé nhanh gọn với giá tốt nhất có thể."

| Dimension | Nội dung |
|---|---|
| Functional | Xem lịch chiếu theo rạp/ngày, chọn suất, thanh toán trong 1 flow |
| Emotional | Không mất thời gian, không lo hết chỗ đẹp, an tâm về giá |
| Social | "Anh đặt vé CGV tối thứ 7 rồi, em chọn ghế đi" - chủ động với bạn bè/gia đình |
| Trigger | Cuối tuần, bộ phim vừa ra, thấy trailer hot trên social |
| Search → App | "lịch chiếu phim CGV hôm nay" → /cinema/rap/cgv/{slug} → "Đặt vé ngay" (sticky deeplink) → App MoMo → Transaction confirmed |

**Giải pháp:** /cinema/lich-chieu, /cinema/rap/{chain}/{theater-slug}, /cinema/{movie-slug} Phase 2 (Showing). CTA "Đặt vé ngay" sticky + Onelink deeplink.

---

### Job #2: Plan - "Tôi muốn tìm phim hay để xem"

> "Khi tôi rảnh và muốn có gợi ý, tôi cần xem top phim hay đang chiếu và review đáng tin."

| Dimension | Nội dung |
|---|---|
| Functional | Danh sách phim kèm rating, trailer, synopsis ngắn, lịch chiếu theo rạp |
| Emotional | Tự tin khi chọn phim, không bị bạn bè chê "phim gì mà không hay vậy" |
| Social | "Phim này 7/10 trên MoMo, mọi người review rồi - mình đi xem đi mấy bạn" |
| Trigger | Cuối tuần, dịp lễ, phim viral trên social |
| Search → App | "phim hay đang chiếu 2026" → /cinema/top-phim/{topic-slug} → "Xem lịch chiếu" → /cinema/{movie-slug} Phase 2 → "Đặt vé ngay" → App MoMo |

**Giải pháp:** /cinema/top-phim/{topic-slug}, /cinema/{movie-slug}/review Phase 3 (Post-release). CTA "Xem phim này ở đâu?" dẫn đến lịch chiếu gần nhất.

---

### Job #3: Navigate - "Tôi cần thông tin về rạp cụ thể"

> "Khi tôi đã có ý định đến rạp cụ thể, tôi cần thông tin chính xác về địa chỉ, lịch chiếu hôm nay, giá vé."

| Dimension | Nội dung |
|---|---|
| Functional | Địa chỉ, giờ mở cửa, lịch chiếu realtime, giá vé, sơ đồ chỗ ngồi |
| Emotional | Tiết kiệm thời gian, không bị ngạc nhiên khi đến rạp |
| Social | "CGV Aeon Canary tối nay còn vé không, mình đi 4 người" - confirm trước khi kéo cả nhóm |
| Trigger | Trước khi xuất phát, đang trên đường, hoặc cần confirm với bạn bè cùng đi |
| Search → App | "CGV Aeon Canary lịch chiếu hôm nay" → /cinema/rap/cgv/cgv-aeon-canary-{id} → Chọn suất → "Đặt vé ngay" → App MoMo |

**Giải pháp:** /cinema/rap/{chain}/{theater-slug} (Programmatic layer - 200-500 URLs).

---

### Job #4: Archive - "Tôi muốn xem lại phim cũ / tìm phim đã hết rạp"

> "Khi tôi nhớ lại hoặc nghe người khác nói về một bộ phim đã hết chiếu, tôi cần biết có thể xem ở đâu hoặc tìm phim tương tự đang chiếu."

| Dimension | Nội dung |
|---|---|
| Functional | Xem thông tin phim cũ, synopsis, trailer; tìm link xem online hoặc phim tương tự đang chiếu |
| Emotional | Nostalgic; hoặc không muốn out of loop khi bạn bè đang nói về phim đó |
| Social | "Phim đó hay lắm nhưng hết rạp rồi, tìm xem trên đâu được không mấy bạn?" |
| Trigger | Bạn bè recommend phim, thấy clip viral, anniversary phim |
| Search → App | "[Tên phim] review" → /cinema/{movie-slug} Phase 3/4 → "Xem phim tương tự đang chiếu" → /cinema/{similar-movie} Phase 2 → "Đặt vé ngay" → App MoMo |

**Giải pháp:** /cinema/{movie-slug} Phase 3-4 (Post-release + Archive), /cinema/archive/{movie-slug}. Giữ link equity, cross-sell phim tương tự đang chiếu.

---

## 5. Kiến Trúc Web

### 5.1 Site Architecture

```
momo.vn/cinema/                             [Hub - Transactional + Informational]
├── lich-chieu/                             [Spoke - Transactional]
│   ├── phim-dang-chieu/
│   ├── phim-sap-chieu/
│   └── phim-chieu-hom-nay/                 (programmatic theo ngày)
├── rap/                                    [Spoke - Navigational hub]
│   ├── {chain}/                            (cgv, lotte, galaxy, bhd, mega-gs...)
│   └── {chain}/{theater-slug}-{id}/        (Programmatic - 200-500 URLs)
├── {movie-slug}-{id}/                      [Phim detail - LIFECYCLE]
│   └── review/
├── top-phim/                               [Evergreen listing]
│   └── {topic-slug}/                       (phim-han-quoc-hay-2026, phim-hay-cuoi-tuan...)
└── archive/
    └── {movie-slug}/
```

**Schema bắt buộc:** Movie + ScreeningEvent + Offer + FAQPage per phase - đây là AEO signal cho AI Overview.

### 5.2 URL Lifecycle System

Hệ thống tự động chuyển template theo trạng thái phim, chạy bằng nightly cron. Đảm bảo content luôn relevant với intent user tại từng giai đoạn - không cần Content team can thiệp per-movie.

| Phase | Trigger | Template | Primary CTA | Schema |
|---|---|---|---|---|
| Phase 1: Pre-release | Chưa có lịch chiếu, release date trong tương lai | Trailer + info + "Nhắc tôi khi mở bán" | "Đăng ký nhận lịch chiếu" | Movie + Event (releaseDate) |
| Phase 2: Showing | Có lịch chiếu trong 7 ngày tới | Lịch chiếu theo rạp + ngày + chọn chỗ | "Đặt vé ngay" (sticky) | Movie + ScreeningEvent + Offer |
| Phase 3: Post-release | Hết lịch chiếu, dưới 90 ngày | Review + "Xem ở đâu?" + Similar movies đang chiếu | Cross-sell: "Xem phim tương tự đang chiếu" | Movie + Review + ItemList |
| Phase 4: Archive | Hết lịch chiếu, trên 90 ngày | Lightweight: summary + "Xem trên {platform}" | Outbound + cross-sell deals | Movie + VideoOnDemand |

### 5.3 Content & Functional Scope

| Requirement | Mô tả |
|---|---|
| Lifecycle State Machine | Dev xây nightly cron, tự động chuyển phase dựa trên showtime data |
| 301 Redirect SOP cho slug migration | Bất kỳ slug change nào đều phải trigger 301 auto - không merge code nếu thiếu |
| phim-chieu-hom-nay programmatic page | Dynamic page theo ngày, dùng showtime API |
| Phim detail Phase 2: sticky CTA "Đặt vé ngay" | Deeplink + tracking Onelink |
| Phim detail Phase 3: cross-sell template | "Top phim tương tự đang chiếu" component |
| Schema Movie + ScreeningEvent + Offer | Structured data cho AI Overview cite |
| Rạp detail depth: giá vé + sơ đồ phòng | Gap so với competitor Moveek |
| top-phim/{topic-slug} evergreen pages | Phim Hàn, Phim hay cuối tuần, theo thể loại |
| Archive landing /cinema/archive/{slug} | Redirect with context, giữ link equity |
| GEO format pages: rạp IMAX/4DX × thành phố | URL pattern mới, target navigational queries |

---

## 6. Success Metrics

### 6.1 North Star Metric

**Transactions (số vé bán) từ /cinema/* via App** - Commission per transaction là revenue output thực sự của use case.

| Metric | Lane | Baseline (Q1/2026) | Target | Timeframe | Tracking |
|---|---|---|---|---|---|
| **[NS] Transactions từ /cinema/** | Revenue | ~3,070/tháng (9,212/Q1) | TBD - align PO Cell | Q4/2026 | Appsflyer |
| Organic sessions /cinema/* | Tier B | ~355K/tháng | +30% = 462K | Q4/2026 | GSC → GA4 |
| Top 10 keywords (rạp + lịch chiếu) | Tier B | ~12 keywords | 18+ keywords | Q4/2026 | GSC |
| Keyword "phim chiếu rạp" (102K vol) | Tier B | Ngoài Top 50 | Top 10 | Q4/2026 | GSC |
| AI Overview cited queries | Tier B | ~0 | 10/20 target queries | Q4/2026 | Manual audit |
| Programmatic URLs indexed | Tier B | ~200-300 | 500+ URLs | Q3/2026 | GSC |

### 6.2 Conversion Funnel

```
Search → /cinema/* → Booking click → App open (deeplink) → Transaction confirmed
```

**Target logic cho "lịch chiếu phim":** Volume 90,500/tháng, MoMo đang ranking #3 (CTR ~7-10% = ~6,300-9,050 clicks/tháng). Nếu đẩy lên #1 (CTR ~28%) = ~25,000 clicks/tháng (+2.8x từ keyword đơn này). Scale tương tự với toàn cluster.

---

## 7. Dependencies & Constraints

| Dependency | Mô tả | Blocker? | Status |
|---|---|---|---|
| URL Lifecycle State Machine | Dev xây nightly cron, state machine logic, template swap - cần estimate effort sớm | Có | Chưa estimate |
| Partner Showtime API SLA | CGV/Lotte/Galaxy API cần SLA ổn định để feed programmatic phase 2-3 | Có | Chưa confirm với partner |
| 301 Redirect SOP deploy | Rule auto-redirect khi slug change - phải có trước khi bất kỳ slug nào thay đổi | Có | Pending |
| Deeplink/Onelink tracking per page type | GA4 events + Appsflyer mapping theo phase - không có thì không đo được conversion per page type | Có | Pending |
| PO Cell (MDS-MOVIE) alignment | Confirm scope, roadmap priority, product feature availability | Có | Chưa sync |
| Schema deployment | Movie + ScreeningEvent + Offer + FAQPage per phase | Không | Backlog |
| Content team capacity | Calendar cho top-phim pages, review template, archive landing | Không | Phase 2 |

**Constraints cứng:**
- Không sử dụng data user cá nhân trong programmatic content (PDPA compliance)
- Outbound links (streaming platforms) phải review với Legal trước khi deploy Phase 4
- Giá vé realtime phải đến từ partner API - không hardcode (ToS risk)
- Slug migration bắt buộc có 301 redirect - không được bỏ qua dù với lý do nào

---

## 8. Chiến dịch: Summer Camp 2026 (20/06 - 05/09/2026)

Chiến dịch tương tác quy mô lớn dành cho 4 bộ phim trọng điểm: Minions, Conan, Spider Man, Nghỉ Hè Sợ Nghỉ Hưu.

### 8.1. Mục tiêu Chiến dịch (Priorities)
1. **GMV / Market Share (Ưu tiên 1):** Push user mua vé trực tiếp trên MoMo.
2. **Rating / Review (Ưu tiên 2):** Tăng tỷ lệ user "đã mua vé" để lại review phim trên hệ thống MoMo.
3. **Community (Ưu tiên 3):** Tăng lượng user tham gia cộng đồng In-app và khởi tạo (launch) new community Out-app.

### 8.2. Landing Page Gamification (Vai trò của Web Platform)
- **Hub Chính:** Landing Page đóng vai trò là Hub chính của chiến dịch.
- **Nhiệm vụ "Show" không "Thực thi":** Landing page chỉ có vai trò **hiển thị nhiệm vụ (Show Mission)**. Người dùng sẽ click từ Web để dẫn (Deeplink) vào thực hiện nhiệm vụ thông qua các bài post minigame In-app.
- **Tracking độc lập:** Luồng thực thi và tracking tiến độ user làm nhiệm vụ do hệ thống Minigame in-app (BU Movies) đảm nhận. Web Platform KHÔNG cần xử lý luồng API CheckTicket hay Verify Review Gate.

### 8.3. Cơ chế Nhiệm vụ (Missions Logic)
- **Mở theo chu kỳ phim:** Mỗi bộ phim có 3-5 nhiệm vụ, chia theo cycle: Trước khi chiếu -> Tuần khởi chiếu -> Hậu khởi chiếu.
- **Mở theo ngày:** Nhiệm vụ được mở theo mốc thời gian bộ phim khởi chiếu.
- **Không ràng buộc Level:** User có thể làm nhiệm vụ bất kỳ, không yêu cầu vượt qua Level trước đó -> Giải quyết triệt để tình trạng user drop journey.

### 8.4. Next Steps & Handoff
- **On-air Target:** 25/06/2026.
- **BU Movies cần bàn giao cho Web Team:**
  - Bản thiết kế Master KV.
  - Danh sách Mission Game.
  - Yêu cầu cụ thể về cấu trúc Landing Page (nội dung text, size block...).

---

## Appendix A: Keyword Universe

**3 nhóm theo volume:**

| Nhóm | Volume ước tính | MoMo hiện tại | Strategy |
|---|---|---|---|
| Rạp & Lịch chiếu | ~650,000/tháng | Top 1-5 cho CGV/Galaxy/Lotte chain pages | Giữ vị trí hiện có; capture gap "rạp chiếu phim" (74K) và "galaxy cinema" (100K) |
| Thể loại phim | ~500,000+/tháng | Hầu hết ngoài Top 50 | top-phim pages evergreen per thể loại |
| Tên phim (volatile) | Biến động theo release | Lifecycle System phủ | Phụ thuộc vào Lifecycle System hoạt động đúng |

**Top service keywords (volume tháng 7/2024):**

| Keyword | Volume | URL target |
|---|---|---|
| Lịch chiếu phim CGV | 135,000 | /cinema/rap/cgv |
| Lịch chiếu phim | 90,500 | /cinema/lich-chieu |
| Rạp chiếu phim | 74,000 | /cinema/rap |
| Beta Thanh Xuân | 40,500 | /cinema/rap/beta-cinemas/beta-thanh-xuan-203 |
| Beta Giải Phóng | 27,100 | /cinema/rap/beta-cinemas/beta-giai-phong-208 |
| Phim đang chiếu | 6,600 | /cinema/phim-dang-chieu |
| Phim sắp chiếu | 5,400 | /cinema/phim-sap-chieu |

---

## Change Log

- **Tháng 5/2026 (v2.1):** Reframe về BRD chiến lược tổng thể: bỏ framing bug fix và W2A tactical issues, rewrite Complication (3 strategic challenges), rewrite Resolution (URL Lifecycle là product feature, không phải bug fix), bỏ Section 2.2 Zero-Traffic URL Audit, renumber 2.3→2.2 và 2.4→2.3, bỏ W2A Rate row và W2A tracking audit dependency.
- **Tháng 5/2026 (v2.0):** Apply BRD CEO Standard: thêm Problem Statement Block, restructure Section 3, thêm Search→App vào JTBD, fix North Star, thêm Lane/Tracking/Status columns, remove Risk Assessment.
- **Tháng 4/2026 (v1.1):** Khởi tạo tài liệu. Bổ sung phân tích zero-traffic URL audit và URL Lifecycle System.
