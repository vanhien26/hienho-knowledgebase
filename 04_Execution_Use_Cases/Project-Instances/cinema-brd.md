# BRD: Cinema - momo.vn/cinema (SEO/GEO Project)

> **Project:** Use Case Cinema - Web Growth Strategy Q2-Q4/2026
> **Main URL:** momo.vn/cinema
> **Division:** MDS (Merchant & Digital Services)
> **Use Case:** Cinema
> **Product:** MDS - Cinema
> **SEO/GEO Project ID:** `cinema`
> **Owner:** Văn Hiến (SEO & GEO Lead) - Out-App Traffic / GPD
> **Governance:** Văn Hiến (SEO & GEO Lead)
> **Cell Team:** MDS-MOVIE
> **Timeline:** Q2/2026 → Q4/2026 (9 tháng)
> **Version:** 1.1 · Tháng 4/2026
> **Status:** Draft - Division/Product Metadata - cần align PO Cell + Dev Lead

---

## Section 1: Executive Summary

**Situation.** Cinema là Use Case trưởng thành nhất của MoMo trong mảng Out-App Traffic: ~1M organic/3 tháng Q1/2026, Top 1 SERP cho "vé xem phim", Top 3-5 cho cluster rạp theo địa điểm. Business model là commission per transaction qua 8 partner chain (CGV, Lotte, Galaxy, BHD Star, Mega GS, Dcine, Cinestar, Beta). Ecosystem position: Discovery (SERP/AIO) → momo.vn/cinema → Transaction (App) → Retention (cross-sell).

**Complication.** Nhìn bề ngoài Cinema là traffic champion, nhưng có 2 root cause kéo ngược tăng trưởng bền vững: (1) **Bug kiến trúc URL Lifecycle** - 959 URLs zero-traffic (91% là phim detail + review đã hết chiếu), gây mất -7,945 sessions/tháng và tiếp tục tăng theo tốc độ phim mới ra rạp; cohort phim mới nhất (movie_id 20k+) chiếm 52% traffic lost (-4,109 sessions/tháng). (2) **W2A conversion chưa tối ưu** - Q1/2026 W2A rate chỉ 12.1% (baseline: 9,866 Traffic-to-App / 81,517 Booking clicks), thấp hơn đáng kể so với 2025 (29.6%). Khoảng cách này phản ánh deeplink/CTA chưa được calibrate per-page-type theo intent. Ngoài ra, AI Overview đã xuất hiện cho "mua vé xem phim" và "lịch chiếu CGV" - nếu không xây AEO moat, traffic organic sẽ bị erode từ 2026 trở đi.

**Resolution.** Chiến lược Q2-Q4/2026 vận hành 3 vector song song: (1) **URL Lifecycle System** - tự động hóa chuyển template theo 4 phases (Pre-release → Showing → Post-release → Archive), giữ link equity, ngăn zombie URL; (2) **Revenue-first W2A** - tối ưu CTA/deeplink per page type theo search intent, target +50% W2A CR; (3) **Programmatic Moat** - xây thêm 500+ URLs rạp × phim × lịch chiếu để tạo defensive long-tail layer trước khi AI Overview shift traffic.

---

## Section 2: Bối Cảnh Hiện Tại

### 2.1 Hiện trạng performance

| Metric | Q1/2026 (Baseline) | 2025 Full Year | So sánh |
|---|---|---|---|
| Organic Traffic | 1,066,000 | 6,387,700 | -83.3% YoY [cần verify - có thể chênh lệch period] |
| Total Traffic | 2,980,000 | 12,425,040 | -76% YoY |
| Booking Clicks | 81,517 | 266,258 | -69.4% YoY |
| Traffic to App | 9,866 | 78,735 | -87.5% YoY |
| %WebToApp | 12.1% | 29.6% | -58% relative |
| Transactions (via App) | 9,212 | 52,311 | -82.4% YoY |
| %CR (App Transaction/W2A) | 93.4% | 66.4% | +40.5% - tốt hơn, nhưng funnel trên mỏng |

*Nguồn: XLSX Sheet REPORT - dữ liệu thực tế Q1/2026 vs 2025.*

**Critical read:** YoY drop mạnh nhưng cần tách biệt (a) seasonal (Q1 vs full year), (b) thực sự mất traffic, hay (c) tracking gap sau migration. Nếu là (c) → W2A rate 12.1% là misleading. **[Cần verify với GA4 + Appsflyer - ưu tiên trước khi set target].**

### 2.2 Zero-traffic URL audit

| Phân tích | Số liệu |
|---|---|
| Tổng URLs zero-traffic | 959 |
| Phim detail + review | ~918 (95.7%) |
| Traffic lost/tháng | ~7,945 sessions |
| Root cause #1 | Phim hết chiếu nhưng URL không transform → page trở thành zombie (không có showtime, CTA không relevant, intent shift) |
| Root cause #2 | Slug migration không 301 redirect (case: cgv-aeon-canary-16 → cgv-aeon-canary-binh-duong-16, mất -1,567 sessions/tháng, 226 keywords) |

**Cohort phân tích (by movie_id):**

| Cohort | URLs lost | Traffic lost | Priority |
|---|---|---|---|
| < 1,000 (phim 2015-2019) | 224 | 876 | Thấp - archive/consolidation |
| 1k-10k | 41 | 154 | Thấp |
| 20k+ (phim 3-6 tháng gần đây) | 184 | 4,109 | **Cao nhất - can thiệp ngay** |

### 2.3 Keyword ranking hiện tại (Top opportunities)

**Nhóm ưu tiên 1 - Rạp & Lịch chiếu (Search intent: Navigational + Transactional):**

| Keyword | Volume | Ranking hiện tại | URL |
|---|---|---|---|
| Lịch chiếu phim CGV | 135,000 | #4-10 (Range 04-10) | /cinema/rap/cgv |
| Lịch chiếu phim | 90,500 | #3 | /cinema/lich-chieu |
| Rạp chiếu phim | 74,000 | Not in Top 50 | /cinema/rap |
| Galaxy Cinema | 100,030 | Not in Top 50 | - |
| Giá vé CGV | 10,020 | #1 | /cinema/rap/cgv |
| Lịch chiếu phim Galaxy | 10,000 | #2-3 | /cinema/rap/galaxy-cinema |
| Lịch chiếu phim Lotte | 10,000 | #4 | /cinema/rap/lotte-cinema |
| Phim chiếu rạp | 102,820 | Not in Top 50 | - |

**Gap lớn nhất:** "Phim chiếu rạp" (102,820/tháng), "phim hay" (101,040/tháng), "rạp chiếu phim" (74,000/tháng) - tất cả Not in Top 50. Đây là volume lớn chưa capture được.

*Nguồn: XLSX Sheet RANKING - volume tháng 7/2024, ranking hiện tại.*

### 2.4 Competitive landscape

| Competitor | Strengths | Weaknesses | MoMo advantage |
|---|---|---|---|
| moveek.com | Community review, long-tail phim indie | Không có transaction flow | Transaction liền mạch + ưu đãi |
| vnpay.vn/ve-xem-phim | Similar payment infra, hub lịch chiếu per chain | Traffic base nhỏ, brand yếu ở entertainment | MoMo brand recall mạnh hơn |
| cgv.vn, galaxycine.vn | Authority gốc về chain của họ | Mỗi rạp 1 silo, user phải search từng chain | Hub aggregator - 1 điểm, nhiều chain |
| rapchieuphim.com | Content depth, long-tail location | Không có payment, UX cũ | End-to-end flow |

**Content gap MoMo chưa cover:** Review/community voice, hub rạp theo chain có depth (giá vé chi tiết, sơ đồ phòng), GEO/AEO cho queries "rạp có Dolby Atmos gần tôi", "phim hay cuối tuần".

---

## Section 3: Định Hướng Dự Án

**1. Dự án này phục vụ điều gì?**

Chuyển Cinema từ traffic champion → revenue engine: tăng transaction-driven sessions và W2A conversion, không chỉ giữ/tăng traffic thuần. Song song build defensibility trước AI Overview shift.

**Target user segments:**
- **Primary:** Người đi xem phim cuối tuần (18-35, đô thị, có habit mobile payment) - search "lịch chiếu + rạp", "phim đang chiếu"
- **Secondary:** Người discover phim (tìm gợi ý) - search "top phim hay", "review phim"
- **Tertiary:** Người lookup thông tin rạp (tên rạp cụ thể theo địa điểm) - search "CGV Aeon Canary"

**2. Dự án này KHÔNG phải là gì?**
- KHÔNG build mobile app (scope của Mobile/MDS team)
- KHÔNG xây platform streaming (không phải Netflix competitor)
- KHÔNG bao gồm SEO cho MoMo blog general (chỉ /cinema/*)
- KHÔNG cover performance marketing / paid media (scope của Growth/Marketing)
- KHÔNG bao gồm backend partner API negotiation (scope của MDS Business)

---

## Section 4: OKR Q2-Q4/2026

### O1: Biến Cinema thành Revenue Engine - shift từ traffic-first sang conversion-first

**KR1:** Transaction-driven sessions từ Web Cinema: baseline [CẦN MEASURE từ GA4 deeplink fire rate] → **+30%** cuối Q4/2026

**KR2:** W2A Conversion Rate trên phim detail page: baseline 12.1% (Q1/2026, nhưng cần verify) → **target +50% relative** = ~18% W2A rate (click CTA → App open với deeplink)

**KR3:** New Users từ Cinema organic (tracked via momoapp.onelink.vn): baseline [CẦN MEASURE từ Appsflyer] → **+25%** cuối Q4/2026

### O2: Giải quyết root cause Traffic Leak - URL Lifecycle System

**KR1:** Zero-traffic URLs giảm từ **959 → dưới 200** cuối Q3/2026 (loại trừ phim pre-release/archive intentional)

**KR2:** Traffic recovery từ URL migration (case cgv-aeon-canary-16): khôi phục **≥70%** traffic cũ (+1,100 sessions/tháng)

**KR3:** URL Lifecycle SOP được Dev + PO approve và deploy **trước cuối Q2/2026**

### O3: Xây moat GEO/AEO trước khi AI Overview shift traffic

**KR1:** MoMo được cited trong AI Overview cho **≥10/20 target queries** ("mua vé xem phim online", "lịch chiếu CGV hôm nay", v.v.)

**KR2:** Programmatic pages (rạp × phim × lịch chiếu) go-live với **≥500 URLs indexed**, CTR ≥3%

**KR3:** AI Traffic (ChatGPT, Perplexity, Gemini): baseline ~0 → **≥5% total organic** cuối Q4/2026

---

## Section 5: JTBD Analysis (Keyword-Driven)

### Job #1: Transact - "Tôi cần đặt vé ngay"

**Search Intent Cluster:** "lịch chiếu CGV", "đặt vé CGV online", "lịch chiếu phim hôm nay", "phim đang chiếu"
**Volume cluster:** ~350,000+/tháng (aggregate: lịch chiếu CGV 135K + lịch chiếu phim 90K + rạp chiếu phim 74K)

> "Khi tôi đã chọn được phim + rạp + suất chiếu, tôi cần mua vé nhanh gọn với giá tốt nhất có thể, để không bị hết ghế và tiết kiệm được qua ưu đãi."

| Dimension | Nội dung |
|---|---|
| Functional | Xem lịch chiếu theo rạp/ngày, chọn suất, thanh toán 1 flow |
| Emotional | Không mất thời gian, không lo hết chỗ đẹp, an tâm về giá |
| Social | Đặt trước để chủ động với bạn bè/gia đình |
| Trigger | Cuối tuần, bộ phim vừa ra, thấy trailer hot |

**Serve bằng:** /cinema/lich-chieu, /cinema/rap/{chain}/{theater-slug}, /cinema/{movie-slug} Phase 2 (Showing)
**CTA:** "Đặt vé ngay" sticky + deeplink Onelink

---

### Job #2: Plan - "Tôi muốn tìm phim hay để xem"

**Search Intent Cluster:** "phim hay 2026", "top phim hay đang chiếu", "phim Hàn Quốc hay 2026", "review phim"
**Volume cluster:** ~200,000+/tháng (review phim 100K + phim hay nhóm + top-phim queries)

> "Khi tôi rảnh và muốn có gợi ý, tôi cần xem top phim hay đang chiếu và review đáng tin, để không phí tiền + thời gian vào phim dở."

| Dimension | Nội dung |
|---|---|
| Functional | Danh sách phim kèm rating, trailer, synopsis ngắn |
| Emotional | Tự tin khi chọn phim, không bị bạn bè chê |
| Social | Muốn xem phim cùng group - cần đồng thuận về lựa chọn |
| Trigger | Cuối tuần, dịp lễ, phim viral trên social |

**Serve bằng:** /cinema/top-phim/{topic-slug}, /cinema/{movie-slug}/review Phase 3 (Post-release)
**CTA:** "Xem phim này ở đâu?" → link đến lịch chiếu gần nhất

---

### Job #3: Navigate - "Tôi cần thông tin về rạp cụ thể"

**Search Intent Cluster:** "CGV Aeon Canary", "Lotte Cinema Đà Nẵng", "Galaxy Tân Bình", "rạp chiếu phim gần đây"
**Volume cluster:** ~300,000+/tháng (aggregate tổng các rạp individual - data từ SERVICE KEYWORDS sheet)

> "Khi tôi đã có ý định đến rạp cụ thể, tôi cần thông tin chính xác về địa chỉ, lịch chiếu hôm nay, giá vé, để không mất công đến rạp nhưng không có suất hoặc phim tôi muốn."

| Dimension | Nội dung |
|---|---|
| Functional | Địa chỉ, giờ mở cửa, lịch chiếu realtime, giá vé, sơ đồ chỗ ngồi |
| Emotional | Tiết kiệm thời gian, không bị ngạc nhiên khi đến |
| Social | Confirm thông tin để nói với bạn bè cùng đi |
| Trigger | Trước khi xuất phát, đang trên đường |

**Serve bằng:** /cinema/rap/{chain}/{theater-slug} (Programmatic layer)

---

### Job #4: Archive - "Tôi muốn xem lại phim cũ / tìm phim đã hết rạp"

**Search Intent Cluster:** "xem {phim cũ} ở đâu", "review miss fortune", keyword phim đã hết chiếu
**Volume cluster:** ~50,000+/tháng (959 URLs × avg residual traffic khi phase chuyển đúng)

> "Khi tôi nhớ lại hoặc nghe người khác nói về một bộ phim đã hết chiếu, tôi cần biết xem ở đâu hoặc tìm phim tương tự đang chiếu, để thỏa mãn nhu cầu giải trí hiện tại."

**Serve bằng:** /cinema/{movie-slug} Phase 3-4 (Post-release + Archive), /cinema/archive/{movie-slug}

---

## Section 6: Kiến Trúc & Scope Build

### 6.1 Site Architecture Target

```
momo.vn/cinema/                                    [Hub · Transactional + Informational]
├── lich-chieu/                                    [Spoke · Transactional]
│   ├── phim-dang-chieu/                           [Existing - enhance]
│   ├── phim-sap-chieu/                            [Existing - enhance]
│   └── phim-chieu-hom-nay/                        [MỚI - programmatic theo ngày · P1]
├── rap/                                           [Spoke · Navigational hub]
│   ├── {chain}/                                   (cgv, lotte, galaxy, bhd, mega-gs, dcine, cinestar, beta)
│   └── {chain}/{theater-slug}-{id}/               [Programmatic · 200-500 URLs · P1]
│       └── {format-slug}-{city}/                  [MỚI: rạp IMAX Hà Nội, rạp 4DX TP.HCM · P2]
├── phim-chieu/                                    [Info hub phim · Existing]
├── {movie-slug}-{id}/                             [Phim detail · LIFECYCLE · P1]
│   └── review/                                    [Review · LIFECYCLE · P1]
├── top-phim/                                      [Evergreen listing · P2]
│   └── {topic-slug}/                              (phim-han-quoc-hay-2026, phim-hay-cuoi-tuan...)
├── blog/                                          [Content · Informational · P2]
└── archive/                                       [MỚI - Landing cho phim hết chiếu · P2]
    └── {movie-slug}/
```

### 6.2 URL Lifecycle System (Core Intervention)

| Phase | Trigger | Template | Primary CTA | Schema |
|---|---|---|---|---|
| Phase 1: Pre-release | `showtime_count==0 AND release_date > today` | Trailer + info + "Nhắc tôi khi mở bán" | "Đăng ký nhận lịch chiếu" | Movie + Event (releaseDate) |
| Phase 2: Showing | `showtime_count > 0 for next 7 days` | Lịch chiếu theo rạp + ngày + chọn chỗ | **"Đặt vé ngay"** (sticky) | Movie + ScreeningEvent + Offer |
| Phase 3: Post-release | `last_showtime < today AND last_showtime > today - 90d` | Review + "Xem ở đâu?" + Similar movies đang chiếu | Cross-sell: "Xem phim tương tự đang chiếu" | Movie + Review + ItemList |
| Phase 4: Archive | `last_showtime < today - 90d OR streaming IS NOT NULL` | Lightweight: summary + "Xem trên {platform}" | Outbound + cross-sell deals | Movie + VideoOnDemand |

**State machine logic (Dev spec):**
```
IF (showtime_count == 0 AND release_date > today) → PRE_RELEASE
ELSE IF (showtime_count > 0 for next 7 days)      → SHOWING
ELSE IF (last_showtime < today AND > today - 90d)  → POST_RELEASE
ELSE IF (last_showtime < today - 90d OR streaming IS NOT NULL) → ARCHIVE
```
Implementation: nightly cron job. Template swap tự động. Không cần Content team can thiệp per-movie.

### 6.3 Content & Functional Requirements

| Requirement | Priority | Description | Owner |
|---|---|---|---|
| **Lifecycle State Machine** | P1 | Dev xây nightly cron, tự động chuyển phase | Dev Team |
| **301 Redirect SOP cho slug migration** | P1 | Bất kỳ slug change nào đều phải trigger 301 auto | Dev Team |
| **phim-chieu-hom-nay programmatic page** | P1 | Dynamic page theo ngày, dùng showtime API | Dev Team |
| **Phim detail Phase 2: sticky CTA "Đặt vé ngay"** | P1 | Deeplink + tracking Onelink | Dev + Tracking |
| **Phim detail Phase 3: cross-sell template** | P1 | "Top phim tương tự đang chiếu" component | Dev + Content |
| **Schema Movie + ScreeningEvent + Offer** | P1 | Structured data cho AI Overview cite | Dev/SEO |
| **Rạp detail depth: giá vé + sơ đồ phòng** | P2 | Gap so với competitor Moveek | Dev + MDS |
| **top-phim/{topic-slug} evergreen pages** | P2 | Phim Hàn, Phim hay cuối tuần, theo thể loại | Content + Dev |
| **Archive landing /cinema/archive/{slug}** | P2 | Redirect with context, giữ link equity | Dev |
| **GEO format pages: rạp IMAX/4DX × thành phố** | P2 | New URL pattern, target navigational queries | Dev + Content |
| **FAQ schema per page type** | P2 | AEO signal cho AI Overview | Content/SEO |
| **Tracking: deeplink fire rate per page type** | P1 | Setup GA4 events + Appsflyer mapping | DA + Dev |

---

## Section 7: Success Metrics

**North Star:** Organic sessions từ Cinema web (transaction-intent cluster) - đo bằng GSC filtered by intent cluster

### 7.1 Organic Traffic (GSC)

| Metric | Definition | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|---|
| Organic sessions | GSC - all /cinema/* | 1,066,000/Q1 (~355K/tháng) | +30% = 462K/tháng | Q4/2026 | GSC + GA4 |
| Zero-traffic URLs | URLs /cinema/* không có impression trong 90 ngày | 959 | < 200 | Q3/2026 | GSC URL crawl |
| Top 10 keywords (P1 cluster) | Keywords từ Rạp + Lịch chiếu cluster ranking top 1-10 | ~12 keywords (giá vé CGV #1, lịch chiếu phim #3, ...) | +50% = 18+ keywords | Q4/2026 | Ahrefs/internal SEO tool |
| Keyword "phim chiếu rạp" (102K vol) | Position hiện tại | Not in Top 50 | Top 10 | Q4/2026 | SEO tool |
| Keyword "rạp chiếu phim" (74K vol) | Position hiện tại | Not in Top 50 | Top 10 | Q4/2026 | SEO tool |

**Target logic:** "lịch chiếu phim" có 90,500 search/tháng, MoMo hiện ranking #3. CTR position #3 ~7-10% → ~6,300-9,050 clicks/tháng. Nếu đẩy lên #1 (CTR ~28%) → ~25,000 clicks/tháng, tức +2.8x từ keyword đơn này. Scale tương tự với toàn cluster.

### 7.2 Web-to-App Conversion Rate

| Metric | Definition | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|---|
| Traffic → Booking Click % | Booking clicks / Organic sessions | 81,517 / 1,066,000 = 7.6% | +20% = 9.2% | Q4/2026 | GA4 click event |
| W2A Rate (Traffic → App) | Traffic to App / Total Traffic | 9,866 / 2,980,000 = 0.33% | [CẦN verify baseline trước khi set] | Q4/2026 | GA4 + Appsflyer |
| W2A Rate trên Phim detail Phase 2 | CTA click "Đặt vé ngay" / Sessions trên phim detail đang chiếu | [CẦN MEASURE] | +50% relative | Q4/2026 | GA4 event per page type |
| New Organic Installs | Appsflyer: install với utm_source = momo.vn cinema pages | [CẦN MEASURE] | +25% | Q4/2026 | Appsflyer |

**Note quan trọng:** W2A rate Q1/2026 (12.1%) vs 2025 (29.6%) drop mạnh - phải verify là thực hay tracking gap trước khi dùng làm baseline.

### 7.3 GEO/AEO Metrics

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| AI Overview cited queries | ~0 (chưa audit) | ≥10/20 target queries | Q4/2026 | Manual SERP audit + AI traffic GA4 |
| AI Referral sessions | ~0 | ≥5% total organic | Q4/2026 | GA4 Custom Channel Group (AI Referrals) |
| Programmatic URLs indexed | ~200-300 (rạp hiện tại) | ≥500 URLs | Q3/2026 | GSC Coverage report |

---

## Section 8: Dependencies & Constraints

| Dependency | Owner | Mô tả | Blocker? | Status |
|---|---|---|---|---|
| **URL Lifecycle State Machine** | Dev Team (MDS) | Nightly cron, state machine logic, template swap | **Yes - P1** | Chưa start [cần estimate effort] |
| **Partner Showtime API SLA** | MDS Business / Partners | CGV/Lotte/Galaxy API có SLA đủ stable để feed programmatic phase 2-3 | **Yes** | [Cần verify với MDS] |
| **301 Redirect SOP deploy** | Dev Team + Web Platform | Rule auto-redirect khi slug change | **Yes - P1** | Chưa có |
| **Deeplink/Onelink tracking per page type** | DA Team + Dev | GA4 events + Appsflyer mapping theo phase | **Yes** | Chưa setup đủ |
| **PO Cell (MDS-MOVIE) alignment** | PO MDS-MOVIE | Confirm scope, roadmap priority, product feature availability | **Yes** | Chưa align chính thức |
| **Inbound Content team** | Inbound Lead | Content calendar cho top-phim pages, review template, archive landing | No (P2 scope) | Chưa brief |
| **GTM Container update** | Web Platform / GTM Owner | Tag deployment cho Lifecycle tracking events | No | Pending |
| **Schema deployment** | Dev/SEO | Movie + ScreeningEvent + Offer + FAQPage per phase | No | Chưa có |

**Constraints cứng:**
- Không sử dụng data user cá nhân trong programmatic content (PDPA compliance)
- Outbound links (streaming platforms) phải review với Legal trước khi deploy Phase 4
- Giá vé realtime phải đến từ partner API - không hardcode (ToS risk)

---

## Section 9: Risk Assessment

| # | Rủi ro | Loại | Khả năng | Impact | Mitigation |
|---|---|---|---|---|---|
| R1 | Partner API không ổn định → programmatic pages hiển thị sai lịch chiếu | Technical | Trung bình | Cao | SLA clarification với partner trước launch; fallback: ẩn section nếu API timeout >3s |
| R2 | Dev capacity không đủ để build Lifecycle System trong Q2 | Execution | Cao | Cao | Estimate effort ngay tuần 1; phân tách: Phase 2 (Showing) CTA có thể deploy nhanh hơn toàn bộ state machine |
| R3 | W2A tracking gap (Q1 drop 12.1% vs 29.6% 2025) chưa được clarify → set target sai | Data | Cao | Trung bình | Audit tracking trước khi lock target; không set W2A KR cho đến khi baseline clean |
| R4 | AI Overview shift traffic mạnh hơn dự báo, CTR organic giảm trước khi MoMo được cite | Market | Trung bình | Cao | Ưu tiên schema + AEO ngay Q2; theo dõi AI traffic weekly từ tháng 5 |
| R5 | Content team chưa có capacity/process cho top-phim + review pages | Execution | Trung bình | Thấp | P2 timeline buffer; brief Content team ngay khi P1 scope đã locked |
| R6 | 301 redirect SOP cho slug migration bị bỏ qua với rạp mới mở/đổi tên | Technical | Cao (đã xảy ra) | Trung bình | Bắt buộc checklist 301 trong deploy process - không merge PR nếu thiếu |

---

## Section 10: Next Steps

| # | Deliverable | Owner | Description | Target date |
|---|---|---|---|---|
| 1 | **Tracking Audit Report** | DA Team + SEO Lead | Verify W2A drop Q1/2026: tracking gap hay thực sự mất conversion? Audit GA4 deeplink events + Appsflyer mapping | Tuần 1-2, Q2 |
| 2 | **Lifecycle SOP + Dev Estimate** | Dev Lead + SEO Lead | Viết spec chi tiết cho state machine (4 phases), estimate effort, gắn vào sprint Q2 | Tuần 2, Q2 |
| 3 | **301 Redirect SOP** | Dev Team | Document + deploy rule auto-redirect khi slug change. Include checklist cho deploy process | Tuần 3, Q2 |
| 4 | **PO Cell Alignment session** | SEO Lead + PO MDS-MOVIE | Align scope, OKR, roadmap priority. Confirm Partner API SLA | Tuần 1, Q2 |
| 5 | **Deeplink Tracking Setup Doc** | DA Team | GA4 event spec per page type + Lifecycle phase; Appsflyer parameter mapping | Tuần 3, Q2 |
| 6 | **Programmatic URLs Audit** | SEO Lead | Xác định danh sách 200-300 rạp detail pages hiện tại, gap cần create, URL naming standards | Tuần 2, Q2 |
| 7 | **Content Brief: top-phim P1 batch** | SEO Lead + Content | Brief 5-10 top-phim pages ưu tiên (Hàn Quốc, Cuối tuần, theo thể loại top volume) | Q2/2026 |
| 8 | **Schema Deployment Plan** | Dev + SEO | Deploy Movie + ScreeningEvent + Offer + FAQPage. Validate via GSC | Q2/2026 |
| 9 | **AI Overview Audit** | SEO Lead | Audit 20 target queries, xác định MoMo cite rate hiện tại, điểm thiếu về structured data | Tuần 1, Q2 |

---

## Appendix A: Keyword Universe Summary

**3 nhóm ưu tiên từ XLSX:**

- **Ưu tiên 1 - Rạp & Lịch chiếu:** Tổng estimated volume ~650,000/tháng. MoMo đang Top 1-5 cho CGV/Galaxy/Lotte chain pages. Gap: "rạp chiếu phim" (74K), "galaxy cinema" (100K) chưa capture.
- **Ưu tiên 2 - Thể loại phim:** Tổng ~500,000+/tháng (phim hàn quốc 100K, phim việt nam 100K, phim hay 101K...). Cần top-phim pages evergreen. Hầu hết Not in Top 50.
- **Ưu tiên 3 - Tên phim:** Highly volatile theo release schedule. Serve bằng phim detail pages + Lifecycle System.

**Service Keywords top volume (từ XLSX Sheet SERVICE KEYWORDS):**

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

## Appendix B: Validate Checklist trước khi Execute

Trước khi chuyển sang Execution phase, cần close những điểm sau:

1. **Baseline metrics** - Fill [CẦN MEASURE] từ GA4 + Appsflyer: W2A rate per page type, deeplink fire rate, New Users từ Cinema organic
2. **Tracking gap investigation** - Giải thích drop W2A từ 29.6% (2025) → 12.1% (Q1/2026)
3. **PO Cell alignment** - Confirm đầu mối Cinema Cell (PO/Growth/Dev) để align Lifecycle state machine specs
4. **Partner API availability** - Verify showtime API từ CGV/Lotte/Galaxy có SLA đủ để build programmatic
5. **Dev capacity** - Lifecycle state machine + programmatic engine cần estimate effort + timeline từ Dev Lead
6. **JTBD validation** - Chạy `jtbd-analysis` skill với live scraping để confirm job statements + anxieties với data thực tế

---

*BRD này là Draft v1.0. Document phục vụ mục đích align PO Cell, Dev Lead, và Management trước khi kick-off execution. Mọi số liệu có ghi [CẦN VERIFY/MEASURE] cần được fill trước khi lock OKR targets.*
