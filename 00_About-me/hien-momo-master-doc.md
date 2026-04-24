# MASTER DOC - Văn Hiến @ MoMo
> Version: 1.2 | Last updated: 2026-04-15 | Maintained by: Văn Hiến

---

## MỤC LỤC

1. [Thông tin cá nhân & Bộ phận](#1-thông-tin-cá-nhân--bộ-phận)
2. [Các Team làm việc chung](#2-các-team-làm-việc-chung)
3. [Mục tiêu Team & Doanh nghiệp](#3-mục-tiêu-team--doanh-nghiệp)
4. [Quy trình làm việc](#4-quy-trình-làm-việc)
5. [Dự án đang triển khai](#5-dự-án-đang-triển-khai)
6. [Leadership Intelligence](#6-leadership-intelligence)
7. [Changelog](#7-changelog)

---

## 1. THÔNG TIN CÁ NHÂN & BỘ PHẬN

### 1.1 Profile

| Field | Detail |
|-------|--------|
| Tên | Văn Hiến |
| Vai trò | SEO & GEO Lead |
| Bộ phận | Out-App Traffic Team |
| Division | Growth Platform Division (GPD) |
| Domain sở hữu | momo.vn (web channel) |
| Kinh nghiệm | 7 năm (Web Construction, SEO/GEO, Product Growth) |
| Background | Fintech |

### 1.2 Trách nhiệm lõi

**Platform Health & Governance (Lõi):**
- Đảm bảo momo.vn khỏe mạnh, sạch sẽ về Technical SEO và Content Foundation
- Set standard và audit mọi hoạt động SEO/GEO trên web - dù ai thực hiện (Inbound, Agency qua Inbound)
- Hiến là người **set standard và audit**, không phải người **execute** trực tiếp
- Agency không access trực tiếp momo.vn - mọi hoạt động đều qua Inbound Review & Execution
- Hiến đảm bảo Tech Foundation và Content Foundation được tuân thủ chặt chẽ

**Scope quản lý:**
- Technical Foundation: On-page, Technical SEO, Schema, URL governance, Crawl quality, Sitemap
- Content Foundation: Foundation Checklist, SEO/GEO Guideline, YMYL Guideline - áp dụng cho Inbound và Agency (qua Inbound)
- Tracking: GTM/GA4/Appsflyer setup chuẩn cho mọi Use Case

**Dự án chiến lược (từ Công):**
- Web Platform (Bảo) và Out-App Traffic (Hiến) cùng chủ động triển khai
- Mọi hoạt động vẫn phải tuân theo Tech Foundation và Content Foundation do Hiến set
- Boundary với Inbound: không overlap với dự án Inbound/Agency đang triển khai
- Lý do: nhân lực Out-App Traffic có giới hạn - không ôm execution của Inbound

**KPIs:**
- Organic Traffic, Keyword Ranking, New User, MAU, MEU từ web channel (momo.vn)
- Web-to-App pipeline: Organic Traffic → Onelink → App Install → Register → KYC → Cashin → MAU
- GEO/AEO: MoMo được cite trong Google AI Overview, ChatGPT, Perplexity cho target queries tài chính

### 1.3 Ownership map

| Nhóm hoạt động | Ownership | Ghi chú |
|----------------|-----------|---------|
| SEO/GEO strategy & governance | Văn Hiến | Set standard, audit - không execute trực tiếp |
| Technical Foundation (audit & standard) | Văn Hiến | On-page, Schema, URL governance, Crawl quality, Sitemap |
| Content Foundation Checklist - sign-off | Văn Hiến | Gate bắt buộc trước khi publish, kể cả content của Inbound/Agency |
| SEO/GEO consult cho Cell Team | Văn Hiến | Tư vấn Sitemap, Content Structure, pSEO |
| Foundation Checklist training cho Inbound | Văn Hiến | Đảm bảo Inbound hiểu và tuân thủ chuẩn |
| Tracking (setup & execute) | DA | Hiến set tracking standard, DA chịu trách nhiệm setup đến execute |
| Web-to-App conversion optimization | Văn Hiến | |
| Web Platform liaison (technical request) | Văn Hiến → align trực tiếp Bảo | |
| SEO Inventory - chuẩn đánh giá market share | Văn Hiến | |

### 1.4 Prioritization Framework

Khi có nhiều workstream cạnh tranh bandwidth, Hiến ưu tiên theo 2 tiêu chí:

1. **Market Search Potential** - Use Case có search demand đủ lớn, đáng đầu tư
2. **Company Direction (Financial)** - Gắn với chiến lược tài chính của MoMo (Credit, Insurance, BNPL)

### 1.5 Stack & Tools

| Nhóm | Tools |
|------|-------|
| Analytics | GA4 (G-02G70QKZ26), GSC, Looker Studio |
| Tag Management | GTM OutApp (GTM-P9JDDJZ), GTM InApp (GTM-5TCGRPX) |
| Attribution | Appsflyer (momoapp.onelink.vn) |
| Product Analytics | PostHog (momovn-dev.mservice.io) |
| CMS | [CẦN ĐIỀN] |
| Deployment | GitHub Org + Vercel Team, Google Apps Script Web App |
| Tracking standard | Dual-Stack: GA4+GTM (marketing attribution) + PostHog (product behavior, session replay, A/B test) |

---

## 2. CÁC TEAM LÀM VIỆC CHUNG

### 2.1 Org Chart - GPD

```
Công (Vice President)
├── Tuệ (Head of User Engagement) -> Nghỉ phép tháng 4
│   └── Văn Hiến (SEO & GEO Lead - Out-App Traffic) -> Báo cáo trực tiếp Bảo (trong T4)
└── Bảo (Production Manager - Web Platform)
    └── Back-end & Front-end Dev
```

**Lưu ý quan hệ (Tháng 4/2026):**
- Trong tháng 4, Tuệ take break 1 tháng nên Hiến báo cáo trực tiếp cho Bảo.
- Hiến align trực tiếp với Bảo cho technical issues, new requests, SEO/GEO potential projects - không cần escalate qua Tuệ
- Khi cần resource/priority từ Web Platform ở level lớn hơn → align Tuệ (khi back) → Công

### 2.2 Out-App Traffic (Hiến sở hữu)

| Field | Detail |
|-------|--------|
| Scope | Platform Health & Governance: Set standard, audit và kiểm soát mọi hoạt động SEO/GEO trên momo.vn dù ai thực hiện. Bổ sung T4: Quản lý mảng SEO/GEO từ Internal và Inbound |
| Model hoạt động | **Govern, không Execute** - Hiến set standard và audit. Inbound/Agency execute qua Inbound |
| Hoạt động | Technical Foundation audit, Content Foundation governance, Tracking setup, Strategic projects |
| KPI chính | Organic Traffic, Keyword Ranking, New User, MAU, MEU |
| Quan hệ với Web Platform | Hiến gửi technical request / SEO potential project → Bảo implement |
| Quan hệ với Inbound | Hiến là đầu mối - Inbound không làm việc trực tiếp với Web Platform |

### 2.3 Web Platform (Bảo)

| Field | Detail |
|-------|--------|
| Lead | Bảo (Production Manager) |
| Reporting | Trực tiếp Công (VP) |
| Scope | Quản lý, tư vấn Cell Team xây dựng sản phẩm trên Web theo tiêu chuẩn product design |
| Trách nhiệm | Vận hành nền tảng web, tăng trưởng Web-to-App, standardize tracking (truth of source) |
| Tools | Xây dựng công cụ cho Out-App Traffic / Cell Team / Inbound vận hành nội dung |
| KPI chính | Web-to-App conversion, New User, MAU, MEU (chung với GPD) |

### 2.4 Inbound Marketing (Mai - thuộc BMC)

| Field | Detail |
|-------|--------|
| Lead | Mai (SEO & Inbound Team Leader) |
| Division | BMC (Brand & Marketing Center) - không thuộc GPD |
| Scope | SEO tư vấn (Plan / Blog / Off-page) - tiền thân của Out-App Traffic |
| Cơ chế | BU reach tới Inbound để tư vấn, Inbound chọn Use Case theo chiến lược BMC |
| KPI | SLA và KPI riêng theo cam kết với từng BU |
| Boundary với Hiến | Inbound không làm việc trực tiếp với Web Platform - phải thông qua Hiến |
| Foundation Checklist | Inbound phải tuân thủ - đây cũng là checklist Inbound input và cung cấp. Sign-off: Hiến |
| FS commitment | Vay Nhanh / Ví Trả Sau / CIC: Inbound cam kết Traffic/Ranking |

### 2.5 Cell Team Matrix (theo Business Unit)

Mỗi Cell Team tiếp cận Hiến theo framework: **Research → Build Web/Function → Content Production → Tracking → Evaluation**

| BU | Use Case | Workstream với Hiến | Workstream với Inbound | Status |
|----|----------|--------------------|-----------------------|--------|
| FS | Vay Nhanh | Tech Web (Build/Revamp) + SEO/GEO consult | SEO Ranking cam kết | Active |
| FS | Ví Trả Sau | Tech Web + SEO/GEO consult | SEO Ranking cam kết | Active |
| FS | CIC | Tech Web + SEO/GEO consult | SEO Ranking cam kết | Active |
| FS - Insurtech | BH xe máy | Build/optimize web - tăng GMV + SEO/GEO consult | Off-page ranking | Active |
| FS - Insurtech | BH ô tô vật chất | Build/optimize web - tăng GMV + SEO/GEO consult | Off-page ranking | Active |
| FS - Insurtech | BH y tế (BHYT) | Build/optimize web + SEO/GEO consult | Off-page ranking | Active |
| FS - Insurtech | BH xã hội (BHXH) | Chuẩn bị landing page + tracking trước launch | - | Sắp ra mắt (~10 ngày) |
| MDS | Movies (Cinema) | Monitor kỹ thuật + hiệu suất | - | Passive |
| MDS | Bus (OTA) | Monitor kỹ thuật + hiệu suất | - | Passive |
| PS - UTI | Sim số đẹp / eSIM du lịch | Đã roll out, chưa có growth plan | - | Pending |
| PS - UTI | Tra cứu phạt nguội | Build Mini Web (có tra cứu) + Blog Content | - | Active |
| GPD Internal | QLCT (Quản Lý Chi Tiêu) | SEO/GEO - tăng ranking/traffic | - | Active |

**Cell Team structure (mỗi team):**

| Role | Nhiệm vụ |
|------|----------|
| PO (Product Owner) | Roadmap, prioritization, stakeholder alignment |
| Growth/Business | KPI ownership, experiment design, business case |
| Dev | Technical implementation, feature deployment |
| DA (Data Analyst) | Data pipeline, reporting, SQL/BigQuery |
| Legal | Review nội dung tài chính, compliance YMYL |

### 2.6 Danh mục sản phẩm MoMo trên Web (theo SEO Inventory)

> Dùng làm reference khi consult Cell Team hoặc đánh giá market share.

| Nhóm | Sản phẩm | Loại | SoV MoMo | Market Volume/tháng |
|------|----------|------|----------|---------------------|
| Vay & Cho vay | Vay Nhanh | Chủ lực | 6% | 4.375.800 |
| BNPL | Ví Trả Sau | Chủ lực - Market Leader | 54% | 135.290 |
| Bảo hiểm | BH xe máy | Chủ lực - Mua trực tiếp | 38% | 58.810 |
| Bảo hiểm | BH ô tô vật chất | Chủ lực - Mua trực tiếp | - | 74.000 |
| Bảo hiểm | BH y tế (BHYT) | Chủ lực - Mua trực tiếp | - | 1.415.740 |
| Bảo hiểm | BH xã hội (BHXH) | Chủ lực - Sắp ra mắt | - | 938.090 |
| Bảo hiểm | BH nhân thọ & các loại khác | Cổng thanh toán | - | ~19.780 |
| Tín dụng | Mở thẻ tín dụng | Sản phẩm phụ | - | 600.900 |
| CIC | CIC Score / Điểm tín dụng | Đang xây dựng | - | 96.790 |
| Đầu tư | Chứng khoán (hợp tác CVS) | Chủ lực - Mini App + Landing page | - | 3.000.000 |
| Đầu tư | Chứng chỉ quỹ | Chủ lực | - | ~12.000 |
| Tiết kiệm | Gửi tiết kiệm (Bản Việt) | Chủ lực | - | 209.000 |
| Dịch vụ công | Phạt nguội | Cổng thanh toán - Tiềm năng traffic | - | ~1.500.000 |

---

## 3. MỤC TIÊU TEAM & DOANH NGHIỆP

### 3.1 OKR 2026 - Out-App Traffic Team

#### O1 - New User Growth via Organic & Web2App

- **Outcome:** Tăng trưởng New User install từ web channel
- **Priority Use Cases:** Credit, Insurance, BNPL, Telco, Cinema, OTA, eSIM
- **Key Lever:** Use Case mini-webs với product flows + Utilities-Led SEO (simulators, tools)
- **Tracking:** momoapp.onelink.vn → Store → Install → Register → KYC → Cashin → MAU

#### O2 - Platform Stability & Technical Readiness

- **Outcome:** Tracking infrastructure vận hành ổn định, zero crawl waste, GEO/AEO-ready
- **Key Results (dự kiến):**
  - Zero-Traffic URL Audit hoàn thành (3,670 URLs / 16 Use Cases)
  - Schema tech debt resolved
  - GA4/GTM infrastructure refactored (17 project folders, 43 parameters, 13 wasted slots fixed)
  - GEO Checklist deployed as publishing gate

#### O3 - PLG/Utilities-Led SEO Products

- **Outcome:** DLU/MAU/MEU growth từ tool-based web pages
- **Key Results (dự kiến):**
  - CIC credit score checker launched
  - Loan calculator live
  - Insurance comparison tool live
- **North Star:** Users giải quyết được nhu cầu tài chính trên web trước khi cần vào App

### 3.2 GEO North Star

> MoMo được cite trong top 3 AI engine responses cho 20 target PFM queries trong vòng 12 tháng

- **Engines target:** Google AI Overview, ChatGPT, Perplexity
- **Current gap:** 0% AI Chatbot referral traffic vs Wise.com: 40%+
- **Decision blockers:** Named author approval, Legal review cadence, Dev resource cho tool portfolio

### 3.3 MoMo Business KPIs liên quan đến Web

| KPI | Định nghĩa | Nguồn tracking |
|-----|-----------|----------------|
| New User | Install → Register | momoapp.onelink.vn funnel |
| MAU | Monthly Active User - Cashin event | Onelink MoMo |
| MEU | Monthly Engagement User - tương tác tính năng trong app (tra cứu, like post...) | Onelink MoMo |
| DLU | Daily Line User | PLG tool engagement |
| Organic Traffic | Sessions từ Organic channel | GA4 |
| AI Citation Rate | MoMo được cite trong AI engine responses | Manual / GEO monitoring tool |
| SoV (Search Share of Voice) | % brand search của MoMo / tổng brand search trong thị trường | Keyword tool - đo theo từng Use Case |

---

## 4. QUY TRÌNH LÀM VIỆC

### 4.1 Workflow Chain (Skill-based)

```
use-case-document
    → jtbd-analysis
    → momo-seo-content-brief
    → content-aeo
    → web-tracking
    → web-growth-analysis
```

### 4.2 Cell Team Engagement Flow

Khi Cell Team tiếp cận Hiến:

```
Research (Hiến consult: Sitemap, Content Structure, pSEO, JTBD)
    → Build Web / Function (Hiến → Bảo: technical request)
    → Content Production (Hiến brief → Inbound execute nếu applicable)
    → Tracking (Hiến setup GTM/GA4/Appsflyer)
    → Evaluation (Hiến + DA: monitoring, experiment)
```

### 4.3 Web Growth Process (9 bước)

| Bước | Hoạt động | Owner |
|------|-----------|-------|
| 1 | Use Case scoping + JTBD mapping | Hiến + PO |
| 2 | Keyword/Query research + Intent clustering | Hiến |
| 3 | Content angle governance (tránh overlap Inbound/GPD) | Hiến |
| 4 | Content brief writing | Hiến |
| 5 | On-page SEO/GEO production | Inbound (brief từ Hiến) |
| 6 | GEO Checklist review - GATE trước publish | Hiến (sign-off) |
| 7 | Tracking setup (GTM/GA4/Appsflyer) | Hiến + DA |
| 8 | Web Ads (Balloon/Popup) deployment | Hiến + Dev |
| 9 | Post-publish monitoring + experiment | Hiến + DA |

### 4.4 Tracking Architecture

**Onelink Tracks:**

| Track | URL | Dùng cho | Events tracked |
|-------|-----|----------|----------------|
| Track 1 | onelink.momo.vn | Existing users | Open + Action |
| Track 2 | momoapp.onelink.vn | New users | Store → Install → Register → KYC → Cashin → MAU |

**Web Ads Event Schema (GA4):**

| Event | Parameters |
|-------|-----------|
| `webads_impression` | variant, use_case, webads_campaign |
| `webads_cta_click` | variant, use_case, webads_campaign |
| `webads_dismiss` | variant, use_case, webads_campaign |

**UTM Pattern (Web Ads):** `creative_id = {format}-{use_case}-{date}`

### 4.5 URL Governance - Intervention Framework

| Level | Action | Trigger |
|-------|--------|---------|
| 1 | Nofollow + Sitemap removal | Low-value pages, crawl waste |
| 2 | 308 Redirect | Consolidation, topical dilution |
| 3 | 410 Gone | Non-financial Use Cases gây dilution |
| 4 | Mandatory content update | Outdated YMYL content, AI Overview citation risk |

### 4.6 A/B Testing Standard

- **Assignment:** Cookie-based variant assignment (14-day TTL, keyed by Use Case slug)
- **Rationale:** Tránh round-robin contamination
- **Tracking:** GA4 event schema với variant parameter

### 4.7 SEO Inventory - Tiêu chuẩn đánh giá Market Share

Dùng để đánh giá định kỳ (quarterly) mức độ tham chiến của MoMo trong từng thị trường tìm kiếm:

| Chỉ số | Định nghĩa | Nguồn |
|--------|-----------|-------|
| Total Search Volume | Tổng lượt tìm kiếm hàng tháng của thị trường | Keyword tool |
| SoV MoMo | % brand search MoMo / tổng brand search trong thị trường | Keyword tool |
| Priority tier | CAO / TRUNG BÌNH / DUY TRÌ / THAM CHIẾU | Đánh giá tổng hợp |

**Ngưỡng SoV tham chiếu:**
- Trên 40%: Market Leader - duy trì và mở rộng
- 20-40%: Trung bình - có cơ hội tăng trưởng
- Dưới 20%: Thấp - gap lớn, cần đầu tư

---

## 5. DỰ ÁN ĐANG TRIỂN KHAI

### 5.1 Status Board Q1-Q2/2026

| Dự án | Status | Owner | Ghi chú |
|-------|--------|-------|---------|
| Balloon Ads | Done | Hiến | - |
| Popup Ads - Billpay | Done | Hiến | 22 pages, tiered placement |
| Zero-Traffic URL Audit | On Track | Hiến | 3,670 URLs / 16 Use Cases |
| Web2App Tracking + PostHog | On Track | Hiến + DA | Dual-stack model |
| Onelink Standardization | Discuss | Hiến | Legacy link audit needed |
| PLG High-CTR Products | Pending | Hiến | CIC checker, Loan calc, Insurance comparison |
| GEO/AEO QLCT Pillar/Cluster + GEO Checklist | Brainstorming | Hiến | v2 HTML master plan built |
| MoMo Credit Ecosystem (Vay Nhanh/Ví Trả Sau/CIC) | Active | Hiến + Inbound | KPI committed: Top 1 / 10 seed keywords |
| Auto Insurance (Bảo Hiểm Ô Tô Vật Chất) | Active | Hiến | Target: 200K organic traffic 2026 |
| SEO Inventory - Financial & Payment | In Progress | Hiến | Deadline thứ 5, v3 đã build |
| SEO/GEO Content AI Platform | Planning | Hiến | Chuẩn hóa Content Production cho Inbound & Out-App |
| Phạt Nguội (Traffic fines) | Active | Hiến | Xây dựng Mini Web tra cứu & Blog Content |

---

### 5.2 Dự án: GEO/AEO QLCT (Quản Lý Chi Tiêu)

**Vision:** Case Study GEO/AEO đầu tiên tại MoMo - replicable framework cho Cinema, Billpay, Insurance, Telco

**North Star Metric:** MoMo được cite trong top 3 AI engine responses cho 20 target PFM queries trong 12 tháng

**Framework (3 Trục):**

| Trục | Nội dung | Mục tiêu |
|------|----------|----------|
| Trục A | Web Content/Architecture | Topical authority cho PFM domain |
| Trục B | Utility Tools (simulators, calculators) | Anti-LLM moat - tạo unique data không scrape được |
| Trục C | Off-Web Entity/Brand Signals | Entity graph, citations, PR mentions |

**Decision Blockers:**
1. Named author policy (byline tác giả cho YMYL content)
2. Legal review cadence (SLA review nội dung tài chính)
3. Dev resource cho tool portfolio (Trục B)

**Meeting log:**
> [CẦN BỔ SUNG]

---

### 5.3 Dự án: Web2App Tracking + PostHog

**Vision:** Dual-Stack tracking model - không phụ thuộc hoàn toàn vào GA4

**North Star Metric:** 100% Use Case pages có đủ event tracking (impression → CTA click → App install)

**Framework:**
- GA4 + GTM: Marketing attribution, channel performance
- PostHog: Product behavior, session replay, A/B testing (demo: momovn-dev.mservice.io)

**Infrastructure đã giải quyết:**
- GA4 custom dimension naming collision (fixed: `webads_campaign` rename)
- Looker SQL bugs (Homepage regex, NULL elimination, CR >100% bug)
**Meeting log:**

**[2026-04-16] - Weekly Sync với Công**
- Participants: Công, Hiến
- Key decisions:
  - Ghi nhận đã track được Full Flow cho người dùng đã có App (Existing Users) qua Onelink.
  - Vấn đề: Phần Install (New User) chưa track được chính xác. Phía DA (Data Analyst) đang bị challenge về tính xác thực/logic của data này.
- Action items:
  - Hiến + DA: Review lại attribution logic của Appsflyer/Onelink cho flow Install [Cần xử lý]

---

### 5.4 Dự án: Zero-Traffic URL Audit

**Vision:** Loại bỏ crawl waste, tăng crawl budget efficiency, nâng topical authority cho financial domain

**North Star Metric:** Giảm zero-traffic URLs xuống < [CẦN ĐIỀN target %] trong Q2/2026

**Scope:** 3,670 URLs / 16 Use Cases

**Framework:** Xem mục 4.5 (4 levels)

**Meeting log:**
> [CẦN BỔ SUNG]

---

### 5.5 Dự án: Popup Ads - Billpay

**Status:** Done

**Vision:** Web Ads system với tracking chuẩn Appsflyer attribution cho New User acquisition

**North Star Metric:** New User install từ Billpay popup (Store → Install → Register)

**Scope:** 22 pages, tiered placement strategy

**Framework:**
- Cookie-based A/B testing (14-day TTL)
- GA4 event schema: impression, CTA click, dismiss
- UTM: `{format}-{use_case}-{date}`

**Meeting log:**
> [CẦN BỔ SUNG]

---

### 5.6 Dự án: MoMo Credit Ecosystem (Vay Nhanh + Ví Trả Sau + CIC)

**Vision:** Content ecosystem cho tín dụng tiêu dùng - cross-product ranking và internal link automation

**North Star Metric:** Top 1 ranking cho 10 seed keywords (Vay nhanh, Vay tiền online, Vay tiền nhanh, Vay tiền, Vay online, Vay online nhanh, Vay trả góp, Vay nhanh online, Vay tiền online nhanh, Vay tiền mặt)

**Scope:**
- Vay Nhanh (Personal Loan)
- Ví Trả Sau (BNPL)
- Điểm Tín Dụng CIC (score range 300-850, 6 landing pages theo band)

**Framework:**
- Expansion Mini Web: Sub-pages có Simulation (Vay nhanh)
- Cross-Service cho cả 3 sản phẩm
- Revamp Mini Web: Ví Trả Sau, Vay Nhanh, CIC
- Build Content Production cover thị trường
- Build Off-page plan & Entity cho financial domain
- Interactive CIC simulator (HTML widget - built)

**Meeting log:**

**[2026-04-13] - Sync BU FS - Vay Nhanh**
- Participants: Hiến, Mai (Inbound/BMC), BU FS team
- Key decisions:
  - KPI commit: Top 1 cho 10 seed keywords. Milestone: ít nhất Top 3 vào tháng 9, Top 1 vào tháng 12
  - BU cần đẩy nhanh tiến độ - cần Inbound (BMC) phối hợp cùng BU thực hiện các action cần thiết
  - Đánh giá lại nhu cầu nguồn lực và resource → back lại cho BU
- Action items:
  - Agency: Back báo cáo ranking report tuần này → họp đề xuất solution nếu ranking chưa khôi phục [Agency]
  - Mai: Audit competitor, review plan điều chỉnh theo thuật toán mới [Mai]
  - BU FS: Audit page /vay-nhanh → xác định nội dung cần bổ sung để tăng unique content [BU FS]
  - BU FS: Review + bổ sung GEO prompts cho Vay Nhanh [BU FS]
  - BMC: Triển khai monthly report và project tracker để team theo dõi định kỳ [Mai]
  - BU FS: Chuẩn bị content golive new pages (Vay theo đối tượng, vay theo mục đích, blogs) [BU FS]
  - Hiến + Mai: Phản hồi content directions và template UI cho new pages [Hiến + Mai - tuần này]
  - Hiến: Back lại phần revamp mới của website [Hiến - tuần này]
- Blockers surfaced:
  - Ranking chưa khôi phục - đang chờ agency report
  - New pages cần content direction trước khi BU bắt đầu làm
- Hoạt động đang chạy:
  - Off-page: Backlink với agency
  - On-page: Technical + Content production + Revamp website (tăng Time on Site + CR vào app)

---

### 5.7 Dự án: Auto Insurance (Bảo Hiểm Ô Tô Vật Chất)

**Vision:** Organic traffic leadership cho Insurance trong fintech

**North Star Metric:** 200K organic traffic/năm 2026 (baseline Q1: ~19K)

**Key decisions đã lock:**
- Không dùng geo-based URL clusters
- Consolidate sitemap via JTBD cross-reference
- Thêm trang `/vat-chat/gia-han` (renewal - missing)
- Blog: informational intent only. Transaction Landing Pages: transactional intent only

**Deliverables đã có:** HTML MasterDoc v2, Growth Tactics doc, PRD docx

**Meeting log:**
> [CẦN BỔ SUNG]

---

### 5.8 Dự án: Content Governance Framework

**Vision:** Ngăn overlap content angles giữa Inbound và GPD. Định nghĩa rõ ownership theo page type và GEO objective.

**North Star Metric:** 0 content conflict incidents per quarter

**Scope:**
- Phân loại content ownership (Inbound vs GPD)
- GEO/AEO objectives per Use Case
- AI Mention / Cited Pages tracking across Google AI Overview, ChatGPT, Perplexity

**Status:** Đang xây dựng framework

**Meeting log:**
> [CẦN BỔ SUNG]

---

### 5.9 Task: SEO Inventory - Financial & Payment Market

**Loại:** Task nội bộ GPD - tiêu chuẩn đánh giá market share định kỳ

**Giao từ:** Công (VP)

**Vision:** Xây dựng bức tranh tổng quan thị trường tìm kiếm tài chính và thanh toán - xác định MoMo đang ở đâu, thị trường nào tiềm năng, thị trường nào chưa khai thác.

**North Star:** Trở thành công cụ đánh giá market share chuẩn, cập nhật định kỳ hàng quý - phục vụ direction của leadership và prioritization của Out-App Traffic.

**Framework 3 trục:**
1. Market Size - Total Search Volume (proxy đo quy mô thị trường)
2. MoMo Position - SoV % trong từng thị trường
3. Priority Assessment - CAO / TRUNG BÌNH / DUY TRÌ / THAM CHIẾU

**Scope hiện tại:** Financial (Vay, Tín dụng, BNPL, Bảo hiểm, Đầu tư, Tiết kiệm) + Dịch vụ công (Phạt nguội)

**Deadline:** Thứ 5 (tuần này)

**Status:** In Progress - v3 đã build (docx landscape)

**SoV đã có:**
- Vay Nhanh: 6%
- Ví Trả Sau: 54%
- BH xe máy: 38%
- Còn lại: chưa đo (sản phẩm chưa triển khai đủ)

**Data còn thiếu cho Phase 2:**
- SoV: BH y tế, BH ô tô, Chứng khoán, Gửi tiết kiệm, CIC
- BHXH: breakdown intent mua vs tra cứu
- Phạt nguội: phân tích intent và khả năng conversion
- eSIM/Telco: chưa có market sizing
- GSC overlay: Organic Impressions thực tế theo từng thị trường

**Meeting log:**

**[2026-04-16] - Weekly Sync với Công**
- Participants: Công, Hiến
- Key decisions:
  - Mở rộng Scope: Không chỉ dừng lại ở mảng Tài chính, cần đánh giá Potential Market Sizing tổng thể hơn cho cả mảng Thanh toán (Giải trí, dịch vụ...).
  - Deep Dive: Đánh giá chi tiết các dịch vụ MoMo đang làm (hiệu suất thực tế, Gap so với thị trường/đối thủ) và thống kê số lượng Blog/Content đang triển khai cho từng dịch vụ đó.
- Action items:
  - Hiến: Update SEO Inventory v4 bao gồm mảng Thanh toán & Giải trí [Tuần tới]

---

### 5.10 Dự án: SEO/GEO Content AI Platform (Project by AI)

**Vision:** Công cụ ứng dụng AI Foundation (Claude/Gemini) để chuẩn hóa hoạt động Content Production trên Website cho cả Inbound (BMC) và Out-App Traffic (GPD).

**Owner:**
- Web Platform: Trọng (PIC build công cụ)
- Out-App Traffic: Hiến (owner Skill/Prompt Hub - SEO/GEO layer)

**Scope & Workflow:**
- Quản lý BU Input: Lưu trữ các thông tin dự án, Business Model, Target Audience, Value Prop, Promotion,... (tự động update theo thời gian thực)
- Workflow Content: Keyword → Secondary keyword → Draft Outline by AI → Manual edit → Content Detail by AI → Manual Edit on Demo → Public
- AI Skill Hub: Hiến own - gồm 2 thành phần:
  - SEO/GEO Checklist Skills: source từ https://momo-geo-scoring.vercel.app/
  - Prompt với Role viết Blog: [CẦN BỔ SUNG - Hiến update sau]
- Dashboard Output: Quản trị nội dung và pull Ranking/Impression từ GSC API

**Status:** Đang lên kế hoạch kiến trúc và thiết kế hệ thống.

**Roadmap theo Batch:**

| Batch | Nội dung | Status |
|-------|----------|--------|
| Batch 1 | SEO/GEO Guideline + YMYL Guideline + Blog Prompt (Outline + Writer) | Done - sẵn sàng integrate |
| Batch 2 | Business Context Layer: Business Model, Target Audience, Value Proposition, Promotion Scheme theo từng Use Case/Project — mỗi lần Create New Article sẽ tự động pull context này để output chính xác hơn | Planned |

---

### 5.11 Dự án: Phạt Nguội (Traffic Fines)

**Vision:** Cung cấp công cụ tra cứu phạt nguội trên Mini Web kết hợp nội dung Blog thu hút User qua kênh Out-App.
**Status:** Active (Tháng 4/2026).
**Scope:**
- Xây dựng Mini Web có chức năng tra cứu vi phạm.
- Sản xuất Blog Content liên quan đến lĩnh vực Giao thông/Phạt nguội.

**Meeting log:**

**[2026-04-18] - Họp tháng 4 với Bảo (Web Platform)**
- Participants: Hiến, Bảo
- Key decisions:
  - Tuệ nghỉ phép 1 tháng, cấu trúc báo cáo của Hiến chuyển trực tiếp sang Bảo trong T4.
  - Nhiệm vụ thay đổi/bổ sung trong tháng 4: SEO/GEO Management các dự án SEO/GEO được triển khai trên Web từ Internal và Inbound.
  - Triển khai kickoff dự án Phạt Nguội.
- Action items:
  - Hiến: Lên kế hoạch/wireframe cho Mini Web tra cứu và Blog Content chiến lược cho Phạt Nguội.

---

## 6. LEADERSHIP INTELLIGENCE

> Lưu trữ behavior patterns, decision style, priorities và triggers của lãnh đạo trực tiếp để tối ưu stakeholder management.

### 6.1 Tuệ - Head of User Engagement

| Field | Detail |
|-------|--------|
| Tên | Tuệ |
| Vai trò | Head of User Engagement |
| Reporting line | Under Công (VP) |
| Quản lý | Văn Hiến (Out-App Traffic) |
| KPI quan tâm nhất | MAU uplift, DLU uplift (chưa có baseline số cụ thể cho 2026) |
| Decision style | Framework-oriented: cần package dự án thành case study mới thuyết phục được |
| Communication preference | Doc hoặc slide report |
| Trigger tích cực | Kết quả đóng gói thành case study replicable; số liệu rõ ràng |
| Trigger tiêu cực | [CẦN BỔ SUNG] |
| Thói quen ra quyết định | [CẦN BỔ SUNG] |
| Ý định chiến lược 2026 | Uplift MAU/DLU từ Web channel thông qua Out-App Traffic |
| Ghi chú | Escalation path: Hiến → Tuệ → Công cho policy/resource decisions |

### 6.2 Công - Vice President

| Field | Detail |
|-------|--------|
| Tên | Công |
| Vai trò | Vice President (GPD) |
| Quản lý trực tiếp | Tuệ, Bảo |
| Decision style | High-level direction - giao task dạng framework, không spec chi tiết. Expect output là bức tranh tổng thể để ra direction |
| KPI quan tâm nhất | Web là trusted source về tài chính - đóng góp vào Organic Traffic và Web-to-App |
| Communication preference | Framework + case study có thể scale (giống Tuệ) |
| Trigger tích cực | Dự án được đóng gói thành case study replicable; bức tranh thị trường rõ ràng có con số |
| Trigger tiêu cực | [CẦN BỔ SUNG] |
| Ghi chú | Hiến không direct với Công - mọi escalation đi qua Tuệ |

### 6.3 Bảo - Production Manager (Web Platform)

| Field | Detail |
|-------|--------|
| Tên | Bảo |
| Vai trò | Production Manager - Web Platform |
| Reporting line | Under Công (VP) trực tiếp |
| Quan hệ với Hiến | Đồng cấp GPD - align trực tiếp, không qua Tuệ |
| Touchpoint | Technical issues, new web requests, SEO/GEO potential projects |
| Working style | [CẦN BỔ SUNG] |
| Priority trigger | [CẦN BỔ SUNG] |

---

## 7. CHANGELOG

| Date | Version | Nội dung thay đổi |
|------|---------|-------------------|
| 2026-04-13 | 1.0 | Init document |
| 2026-04-14 | 1.1 | Chuẩn hóa tên Văn Hiến; bổ sung org chart thực tế; rewrite mục 2 theo 3 mảng; thêm Cell Team matrix; thêm prioritization framework; update Leadership Intelligence; fix typo webads_closse; bổ sung meeting recap 13/04 vào 5.6; thêm MEU definition; thêm Cell Team Engagement Flow |
| 2026-04-15 | 1.2 | Tách Insurance thành BU FS Insurtech với 4 Use Case riêng (BH xe máy, ô tô, BHYT, BHXH sắp ra mắt); thêm mục 2.6 Danh mục sản phẩm MoMo với SoV; thêm SoV vào KPI table (3.3); thêm mục 4.7 SEO Inventory standard; thêm task 5.9 SEO Inventory; bổ sung KPI và decision style của Công từ context SEO Inventory |
| 2026-04-16 | 1.3 | Cập nhật recap meeting Weekly với Công: Mở rộng scope SEO Inventory (mảng Thanh toán/Giải trí); cập nhật tình trạng tracking Web-to-App (Existing users OK, Install issue) |
| 2026-04-17 | 1.4 | Bổ sung dự án SEO/GEO Content AI Platform vào Mục 5.10 để chuẩn hóa Content Production cho Inbound & Out-App Traffic |
| 2026-04-18 | 1.5 | Cập nhật Org Chart (Tuệ nghỉ phép, report cho Bảo trong T4). Mở rộng Scope quản lý SEO/GEO cho Internal + Inbound. Đưa dự án Phạt Nguội (Mini Web + Blog) vào tracking |
| 2026-04-18 | 1.6 | Update 5.10: bổ sung PIC Trọng (Web Platform), Hiến own AI Skill Hub gồm SEO/GEO Checklist (source: momo-geo-scoring.vercel.app) + Blog Prompt Role (pending) |
| 2026-04-18 | 1.7 | Update 5.10: bổ sung Batch roadmap - Batch 1 Done (Skills + Prompts), Batch 2 Planned (Business Context Layer: Target Audience, Value Prop, Promotion Scheme theo Project/Use Case) |
| 2026-04-19 | 1.8 | Clarify vai trò lõi: Hiến là Govern không Execute. Agency không access trực tiếp momo.vn, mọi hoạt động qua Inbound. Update Ownership map và Out-App Traffic scope |
| 2026-04-19 | 1.9 | Tracking ownership chuyển sang DA (setup đến execute), Hiến chỉ set standard. Dự án chiến lược từ Công: Web Platform + Out-App Traffic cùng triển khai, vẫn phải tuân theo Tech & Content Foundation của Hiến |

---

## HƯỚNG DẪN CẬP NHẬT

**Sau mỗi cuộc họp - paste vào chat:**
> "Họp xong [tên dự án] hôm nay. Recap: [nội dung]. Bổ sung vào master doc."

**Format meeting log chuẩn:**
```
**[YYYY-MM-DD] - [Tên cuộc họp]**
- Participants: [tên, vai trò]
- Key decisions: [bullet]
- Action items: [owner - deadline]
- Blockers surfaced: [nếu có]
- Thay đổi direction so với trước: [nếu có]
```

**Checklist các mục còn trống:**
- [ ] CMS tool name (1.5)
- [ ] MEU tracking source (3.3)
- [ ] Zero-Traffic Audit target % (5.4)
- [ ] Tuệ: trigger tiêu cực, thói quen ra quyết định (6.1)
- [ ] Công: trigger tiêu cực (6.2)
- [ ] Bảo: working style, priority trigger (6.3)
- [ ] SoV cho: BH y tế, BH ô tô, Chứng khoán, Gửi tiết kiệm, CIC (2.6 + 5.9)