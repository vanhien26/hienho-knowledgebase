---
title: "MoSpark: AI-Powered Growth Platform - Product Vision & PRD"
description: >
  Master Document cho MoSpark Growth Platform.
  Product Vision, PRD hoàn chỉnh, kiến trúc kỹ thuật và quy trình vận hành.
version: v3.1
status: Active
owner: Văn Hiến (SEO & GEO Lead)
last_updated: 2026-05-25
tags: [mospark, platform, growth-os, genai, seo, geo, prd, product-vision]
---

# MoSpark: AI-Powered Growth Platform
## Product Vision & PRD

> **Owner:** Văn Hiến (SEO & GEO Lead) | **Version:** v3.1 | **Updated:** 2026-05-25

---

## MỤC LỤC

1. [Product Vision](#1-product-vision)
2. [Bối cảnh Chiến lược](#2-bối-cảnh-chiến-lược)
3. [Vấn đề cần giải](#3-vấn-đề-cần-giải)
4. [Users & JTBD](#4-users--jtbd)
5. [Kiến trúc Platform](#5-kiến-trúc-platform)
6. [Module Catalog](#6-module-catalog)
7. [North Star & KPIs](#7-north-star--kpis)
8. [Data Governance](#8-data-governance)
9. [Roadmap 2026](#9-roadmap-2026)
10. [Rủi ro & Giảm thiểu](#10-rủi-ro--giảm-thiểu)
11. [RACI & Collaboration](#11-raci--collaboration)
12. [Tài liệu Liên kết](#12-tài-liệu-liên-kết)
13. [Version Log](#13-version-log)

---

## 1. Product Vision

### 1.1. Phát biểu Tầm nhìn

> **"MoSpark là Growth Platform để momo.vn trở thành Financial & Payment Authority - nơi PM/PO tự tạo trang, tự chạy Ads, tự đo lường mà không cần đợi Dev; còn AI lo việc sản xuất và tối ưu nội dung ở quy mô lớn."**

MoSpark không phải là một CMS nâng cấp. Đây là nền tảng cho phép Web MoMo chủ động tăng trưởng - từ sản xuất nội dung, phân phối Ads đến chuyển đổi Web-to-App - theo một quy trình có thể lặp lại, đo lường được và ngày càng ít cần can thiệp thủ công.

### 1.2. Nguyên tắc vận hành

| Nguyên tắc | Ý nghĩa thực tế |
|---|---|
| **PM/PO self-service** | PM tạo Landing Page trong 1-2 ngày thay vì 1-2 tuần. Chạy Ads mà không cần nhờ Dev. |
| **Quality gate bắt buộc** | Không có trang nào được live khi chưa qua SEO/GEO Scoring. Publish phải đúng ngay từ đầu. |
| **Use Case là đơn vị gốc** | Mọi content, Ads, analytics đều gắn theo Use Case - không gắn theo Cell Team hay Division. |
| **1 Keyword = 1 URL** | Hệ thống tự block nếu tạo 2 bài cùng primary keyword. Không để cạnh tranh nội bộ. |
| **AI sản xuất, người chịu trách nhiệm** | AI draft, con người review và sign-off - đặc biệt với nội dung tài chính (YMYL). |

### 1.3. Định vị

| Chiều | CMS cũ (Admin Panel) | HubSpot | MoSpark |
|---|---|---|---|
| Mạnh nhất | Quản lý nội dung tĩnh | Đo lường sau publish | Quality gate + AI production trước publish |
| Yếu nhất | Phụ thuộc Dev cho mọi thứ | Không có hard block | Visibility tracking sau publish (đang build) |
| Phù hợp nhất | MoMo 2022-2024 | B2B Marketing platform | MoMo 2026+ - AI-native fintech growth |

---

## 2. Bối cảnh Chiến lược

> **Tổng hợp từ các cuộc họp chiến lược với Anh Công (VP GPD), Huy Lê (VP User Growth Platform) và A.Tường (CEO). Đây là nền tảng để hiểu tại sao MoSpark được ưu tiên đầu tư.**

### 2.1. Chỉ đạo từ cấp lãnh đạo

**Anh Công - VP GPD (19/05):**

MoMo Website cần dịch chuyển sang 3 vai trò mới, không còn là corporate site hay blog SEO đơn thuần:
- **Financial & Payment Authority:** Điểm đến uy tín, tiếng nói có thẩm quyền trong ngành tài chính/thanh toán Việt Nam.
- **Entry Point từ Search:** Điểm chạm đầu tiên đón traffic tìm kiếm tự nhiên - cả Google lẫn AI Search.
- **Ecosystem Support Layer:** Nền tảng hỗ trợ toàn bộ hệ sinh thái kinh doanh & thanh toán của MoMo.

Luồng chiến lược cốt lõi:
```
Content → Keywords → Ranking → Use Case → User Journey → App/Transaction (New User / MAU)
```

Mục tiêu không dừng ở pageview. Mục tiêu là kích hoạt hành vi chuyển đổi trong App.

Tư duy Use Case làm lõi: Search Intent → Nhu cầu thực tế → Hành trình người dùng → Giải pháp trong App. Mỗi Use Case là một động cơ tăng trưởng độc lập.

**Huy Lê - VP User Growth (22/05):**

- Quy trình cũ quá dài, thuần túy display, PM không thể prototype. PM viết requirement "bay bổng", thiếu thực tế về layout và interaction.
- MoSpark giải quyết bài toán này: 1 prompt ra Landing Page có Value Prop, hướng dẫn và CTA - từ 1-2 tuần xuống còn 1-2 ngày.
- PM "non-tech" cũng tự làm được bản prototype, thậm chí production-ready.
- Tracking và AB Testing phải tích hợp sẵn - "tốc độ ship mà không có AB test thì không thể cải tiến".
- Cần cơ chế guardrail để dù PM tự làm vẫn đảm bảo chuẩn Brand và SEO.

**A.Tường - CEO (qua Workshop JTBD):**

- Tiêu chuẩn sản phẩm: **An toàn - An tâm - Đơn giản - Dễ dùng**. Mọi tính năng phải "1-2-3 click là xong", không cần hướng dẫn thêm.
- "Elegant Problem": Vấn đề phải được phát biểu đơn giản đến mức ai cũng thấy đúng ngay.
- PLG: Web Platform là một sản phẩm nội bộ - PM dùng vì nó tốt và giải quyết được việc của họ, không phải vì bắt buộc.
- Đo lường là ưu tiên. Không có AB test = không thể cải tiến.

### 2.2. Bối cảnh thị trường

AI Search đang thay đổi cách người dùng tìm kiếm thông tin tài chính:
- Google searches/user giảm ~20% YoY năm 2025.
- ChatGPT: 700M weekly active users, tăng 2x trong 6 tháng.
- Perplexity: 780M queries/tháng, tăng 20%+ MoM.
- AI Overviews xuất hiện trên 13-30% queries - fintech là category trigger cao.
- Người dùng VN đang hỏi AI: *"ví điện tử nào tốt nhất"*, *"vay tiền online uy tín"*. Nếu MoMo không có structured context, AI trả lời theo nội dung của competitor.

MoMo đang tụt hậu trong GEO: 0% AI Chatbot referral so với Wise.com 40%+. Tính đến tháng 5/2026, chưa có major Vietnamese fintech nào (ZaloPay, VPBank, Cake) deploy llms.txt hay AI-native content pipeline - đây là window đang mở.

---

## 3. Vấn đề cần giải

### 3.1. PM/PO phụ thuộc Dev cho mọi thứ

- Tạo Landing Page: chờ Dev sprint, mất 1-2 tuần.
- Chạy Ads: nhờ Dev hardcode, mỗi campaign mất nhiều ngày.
- Thay đổi nội dung nhỏ: vẫn phải raise ticket.

Hậu quả: PM không prototype được, requirement "bay bổng" vì không thấy thực tế. Campaign chậm, missed opportunity.

### 3.2. Content production thiếu chuẩn hóa

- AI cá nhân (ChatGPT/Claude) dùng rời rạc, mỗi người prompt một kiểu khác nhau.
- Không có Business Context làm nền - AI dễ bịa thông tin sản phẩm.
- Không có gate chặn nội dung kém chất lượng trước khi publish. YMYL content tài chính có thể lên live không qua review.
- Không track được MoMo đang xuất hiện bao nhiêu % trong AI Search.

### 3.3. Quản lý Web đang theo Cell Team, không theo Use Case

- Inbound Team phải đăng nhập vào từng Cell Team (Vay, Cinema, Bảo hiểm...) để đăng 1 bài blog. Không có single interface.
- URL chồng chéo: `momo.vn/blog/*` và `momo.vn/{use-case}/blog/*` tồn tại song song, cạnh tranh lẫn nhau (Keyword Cannibalization).
- Analytics bị phức tạp hóa do URL structure không thống nhất.
- Ads conflict: nhiều Division muốn chạy Ads đồng thời trên cùng một trang, không có cơ chế quản lý.

---

## 4. Users & JTBD

### 4.1. Nhóm người dùng

| Persona | Ai | Pain point | Cần gì từ MoSpark |
|---|---|---|---|
| **PM/PO Cell Team** | PO Vay Nhanh, Cinema, Bảo Hiểm, Phạt Nguội... | Phụ thuộc Dev cho LP, Ads, content | Tự tạo LP, chạy Ads, nhập Business Context trong cùng ngày |
| **Content Writer / Inbound** | Mai, Agency content | Đăng nhập nhiều CMS, prompt AI mỗi người mỗi kiểu | 1 interface duy nhất, AI pipeline chuẩn hóa, không cần học lại |
| **SEO/GEO Lead** | Văn Hiến | Audit thủ công từng trang, không có SoV visibility | Quality gate tự động, SoV dashboard, data để quyết định đầu tư Use Case nào |
| **Platform Admin** | Bảo (Web Platform Manager) | Ads conflict giữa Division, không có inventory view | Placement Registry, enforce policy, không cần review từng campaign |

### 4.2. Jobs To Be Done cụ thể

**PM/PO cần:**
1. Tạo LP mới cho campaign mà không cần Dev - xong trong 1 ngày.
2. Biết Use Case của mình đang chiếm bao nhiêu % market (SoV) để justify budget đầu tư.
3. Chạy Ads đúng trang, đúng context, đo được click → install.
4. Nhập Business Context 1 lần, AI dùng làm nền cho tất cả bài blog sau đó.

**Content Writer cần:**
1. Viết bài đạt SEO/GEO E-E-A-T mà không phải nhớ hết các quy tắc.
2. Biết ngay primary keyword mình chọn đã có người dùng chưa - tránh viết trùng.
3. Biết bài đang thiếu gì để đạt điểm 80+.

**SEO/GEO Lead cần:**
1. Block được nội dung kém chất lượng trước khi ảnh hưởng domain authority.
2. Thấy được AI engine đang cite MoMo như thế nào cho từng Use Case.
3. Ưu tiên Use Case nào đáng đầu tư dựa trên Market Volume và SoV gap thực tế.

---

## 5. Kiến trúc Platform

MoSpark vận hành theo 4 lớp, phủ kín toàn bộ lifecycle từ market research đến conversion:

```
LAYER 4 - Performance Loop (Phase 2 - Q3+)
  GSC Auto-Refresh | SoV Tracker | Semantic Linking | Health Alert
  ↑ feed data ngược lại để tối ưu tiếp
  
LAYER 3 - Quality Gate (Active)
  SEO/GEO Scoring 100pt | Hard Block CWV | Legal Review | YMYL Guard
  ↑ block nội dung xấu trước publish
  
LAYER 2 - Distribution & Conversion (Active → Scaling)
  Ads Manager | Widget Library | Onelink | Umami Attribution
  ↑ convert traffic thành App user
  
LAYER 1 - Content Production (Active - Pilot)
  SEO Inventory | Business Context | 7-Step AI Workflow | Blog Editor
  ↑ sản xuất nội dung đạt chuẩn
  
FOUNDATION - Use Case System
  Use Case ID | Market Map | Keyword Registry | URL Governance
```

### 5.1. Layer 1 - Content Production

- **7-Step Workflow:** Market Selection → Business Context → Keyword Registry → AI Outline → Manual Edit → AI Blog Detail → SEO/GEO Score → Sync & Publish.
- **Engine:** Claude API với Grounding Search (luôn kiểm tra thông tin thực tế).
- **Chống Cannibalization:** Keyword Master Registry check trùng trước khi tạo bài. 1 keyword = 1 bài, không có ngoại lệ.
- **Business Context 12 fields** là source of truth - AI chỉ viết trong ranh giới PM đã xác nhận. Không bịa tính năng, không nhắc competitor.

### 5.2. Layer 2 - Distribution & Conversion

- **Ads Manager:** Core Ops (Widget/Balloon) → Traffic Inventory (Placement Registry) → Retargeting & Multi-tenant.
- **Native Widget (format chủ lực):** Nhúng shortcode `[widget:phat-nguoi]` trực tiếp vào bài blog. Trải nghiệm tự nhiên nhất, W2A conversion cao nhất, không interrupt SEO.
- **Attribution:** Umami (on-site) + Appsflyer/Onelink (Web-to-App) + GA4 (marketing).

### 5.3. Layer 3 - Quality Gate

- **5-Block Scoring (100 điểm):** Technical SEO+CWV (30pt) | On-Page Content (35pt) | Structured Data+GEO (20pt) | OG Tags (5pt) | Manual Review (10pt).
- **Hard Block:** Canonical sai, Robots=noindex, LCP>2.5s, INP>200ms, CLS>0.1, Không có CTA, Primary Keyword trống.
- **Ngưỡng Publish:** Score < 60 hoặc có Hard Block → Blocked hoàn toàn | 60-79 → Warning | ≥ 80 → Pass.

### 5.4. Layer 4 - Performance Loop (Phase 2+)

- **GSC Auto-Refresh:** Phát hiện content decay → kích hoạt AI Enhance.
- **SoV Dashboard:** Theo dõi AI citation rate theo Use Case trên ChatGPT, Perplexity, Google AI Overviews.
- **Health Alert:** Cảnh báo URL 404, traffic sụt bất thường.
- **Semantic Linking:** Gợi ý internal link dựa trên vector embeddings.

### 5.5. Danh mục 7 loại trang chiến lược

| URL Pattern | Loại trang | Vai trò SEO/GEO | Builder |
|---|---|---|---|
| `/{mini-web}` | Mini Web Use Case | Rank transactional keywords, capture intent mua hàng | Landing Page Builder |
| `/{mini-web}/blog/*` | Growth Blog (Use Case) | Satellite content, dồn Link Equity về Mini Web | GenAI Content |
| `/blog/*` | Growth Blog (General) | Informational keywords, Topical Authority | GenAI Content |
| `/doi-tac*` | Merchant Page | Cross-sell, Local SEO | LP Builder + Merchant Module |
| `/tin-tuc*` | News/Communications | Brand presence, PR | CMS |
| `/hoi-dap*` | Help Center | User support, Featured Snippets | Help Center Module |
| Landing Page | Campaign / Promotion | Conversion-focused, không cần rank dài hạn | LP Builder |

---

## 6. Module Catalog

### 6.1. Tổng quan

| # | Module | Tên | Status | Phase | Owner |
|---|---|---|---|---|---|
| M1 | Landing Page Builder | Tự tạo Landing Page | Production - Q2 Onboarding GPD | 1 | Bảo + Thuận |
| M2 | GenAI Content Engine | AI Content Production | Active - Pilot Phạt Nguội | 1 | Thuận (build), Hiến (govern) |
| M3 | Ads Manager | Web-to-App Conversion | V1.2 Production - Pilot User Growth | 1→2 | Thuận, Bảo |
| M4 | SEO/GEO Scoring Gate | Quality Control | Active - All Page Types | 1 | Thuận (build), Hiến (govern) |
| M5 | SEO Inventory | Market Map & SoV | Active (Manual) → Dashboard Integration | 1→2 | Thuận, Hiến |
| M6 | AI Crawler Policy | llms.txt + robots.txt | robots.txt L1 Deployed | 1 | Hiến (spec), Web Platform |
| M7 | Help Center Agentic | AI-powered FAQ | Registered - Agentic Org Program | 3 | TBD |
| M8 | Migration | Admin Panel → MoSpark | Structure & Mapping Phase | 1 | Bảo + Thuận + Lộc |

---

### 6.2. M1 - Landing Page Builder

**Mục đích:** PM/PO tự tạo Landing Page mà không cần Dev sprint.

**Trạng thái:** Production. Q2 onboarding GPD.

**Năng lực cốt lõi:**
- Block-based WYSIWYG builder.
- Template library theo Use Case (tài chính, bảo hiểm, BNPL).
- CTA + Onelink integration built-in.
- SEO/GEO Scoring Gate bắt buộc trước Publish.
- Mobile-first preview.

**Success Metrics:**
- Time-to-live LP: từ 1-2 tuần → dưới 1 ngày.
- 80%+ LP mới do PM/PO tự tạo, không qua Dev.

---

### 6.3. M2 - GenAI Content Engine

**Mục đích:** Chuẩn hóa quy trình sản xuất Blog/Mini Web bằng AI. Đảm bảo E-E-A-T, không có nội dung trùng keyword, sẵn sàng cho AI Search citation.

**Trạng thái:** Active. Pilot Phạt Nguội xong. Scale sang Financial products (Vay Nhanh, Ví Trả Sau, CIC).

**Tam giác dữ liệu:**
1. **Business Context (BU):** Value Prop, Trust Signals, Disclaimer, Blacklist Terms - 12 fields chuẩn. PM xác nhận và chịu trách nhiệm pháp lý.
2. **Market/Cluster (Hiến - SEO Tools):** Volume, Keyword, Intent - dữ liệu thị trường định lượng.
3. **GenAI Engine:** AI viết bài trong ranh giới Business Context + Keyword từ thị trường.

**7-Step Workflow:**

| Bước | Hành động | Output | Owner |
|---|---|---|---|
| 1 | Tạo Use Case + Project Mapping | Use Case ID | PM/Growth |
| 2 | Nhập Business Context 12 fields | Context Layer (Source of Truth) | PM/Growth + SEO Lead |
| 3 | Tạo Primary Keyword + Secondary, check trùng | Keyword Master Registry | Content Team |
| 4 | AI tạo dàn ý → Content edit → PM approve | Outline Final | Content + PM |
| 5 | AI viết bài chi tiết theo Outline đã approve | Blog Detail Draft | AI (Claude API) |
| 6 | Review chất lượng, SEO/GEO Score, sign-off | Verified Content | SEO/GEO Lead |
| 7 | Sync qua Blog Editor → Publish | Live on momo.vn | Content Team |

**3 Rules không được phá vỡ:**
- **Project-First:** Keyword không tồn tại nếu không gắn Use Case.
- **1-1 Mapping:** 1 Primary Keyword = 1 URL. Tạo trùng → bị block.
- **Single Ownership:** 1 Keyword chỉ thuộc 1 Project.

**Success Metrics:**
- Năng suất: 10 bài/tháng/writer → 20 bài/tháng/writer.
- Quality: 100% bài AI qua Hard Block của Scoring Gate.
- SOV Target: ≥ 30% citation rate cho Primary Keywords của Use Case.

---

### 6.4. M3 - Ads Manager

**Mục đích:** Phân phối nội dung khuyến mãi đúng trang, đúng context để chuyển đổi traffic Web thành App user hoặc reactivate MAU. PM/PO tự chạy, không cần Dev.

**Trạng thái:** V1.2 Production. Pilot User Growth. Trọng tâm đang chuyển sang Native Widget.

**So với Athena (In-App Ads):**

| Chiều | Athena (App) | Ads Manager (Web) |
|---|---|---|
| User identity | Đã định danh, có lịch sử giao dịch | Anonymous (Web chưa có Login) |
| Targeting | Audience Segment (behavioral) | URL context của trang (intent-based) |
| Bidding | Có - 3 chiến lược | Priority-based, không bidding |

**5 Ad Formats:**

| Format | Mức interrupt | Phù hợp với | Mục tiêu |
|---|---|---|---|
| **Native Widget (Shortcode)** | Rất thấp - PLG | Blog Article, Mini Web | W2A Conversion cao nhất |
| **Balloon / Float Icon** | Thấp | Tất cả trang | Traffic + Awareness |
| **Inline Banner** | Trung bình | Blog/News | Awareness |
| **Sticky Bar** | Trung bình | Landing Page | Traffic |
| **Popup** | Cao - *chỉ LP có promotion* | Landing Page | Traffic (hạn chế) |

**Phased Roadmap:**

**Phase 1 - MVP (Q2/2026 - Đang làm):**
- Widget Library: Phạt Nguội + BHYT embed qua CMS Shortcode `[widget:phat-nguoi]`.
- URL context targeting cơ bản.
- Umami Reach Estimate khi setup campaign (28-day visitors per Use Case).
- Auto-Publish cho PM/PO ở giai đoạn < 50 campaigns.

**Phase 2 - Inventory Management (Q3/2026):**
- **Placement Registry:** Toàn bộ ad slots đăng ký tập trung - Use Case Placements + Shared-source GPD.
- **Conflict Resolution:** Tự động detect và resolve khi nhiều campaign tranh cùng placement.
- **SEO Inventory Dashboard:** Market Volume per Use Case, bar chart breakdown.
- Global guardrail cứng: max 1 Popup/session, max 2 Balloon cùng lúc.

**Phase 3 - Retargeting & Multi-tenant (Q4/2026):**
- **On-site Retargeting:** Local Storage ghi vết intent, reactivate khi user vào trang dùng chung. Không cần Login, 100% anonymous.
- **Multi-tenant:** PM/PO Division tự tạo và vận hành campaign trong phạm vi Placement của Division.
- **Umami Dashboard per Division:** Impression, Click, CTR, Dismiss Rate.

**KPIs:**

| Phase | Metric | Baseline | Target |
|---|---|---|---|
| Phase 1 | CTR (Traffic campaigns) | 2.4% | 4%+ |
| Phase 1 | Dismiss Rate | 78.3% | < 65% |
| Phase 1 | Time-to-live campaign | Nhiều ngày | < 1 ngày |
| Phase 2 | Placement conflict rate | - | < 10% |
| Phase 3 | Division self-service rate | - | 80%+ |

---

### 6.5. M4 - SEO/GEO Scoring Gate

**Mục đích:** Block nội dung không đủ chuẩn trước khi Publish. Không có ngoại lệ, không có cách bypass.

**Trạng thái:** Active. Áp dụng cho tất cả Page Types.

**Scoring Model (100 điểm):**

| Block | Điểm | Kiểm tra gì |
|---|---|---|
| 1 - Technical SEO + CWV | 30 | Canonical, Robots, H1, LCP/INP/CLS |
| 2 - On-Page Content | 35 | Wordcount, Keyword density/placement, CTA |
| 3 - Structured Data + GEO Signals | 20 | Schema, FAQ, Entity, datePublished, Fact Density |
| 4 - OG/Social Meta | 5 | og:title, og:description, og:image |
| 5 - Manual Review | 10 | Preview, Mobile check, GSC status, Sitemap |
| **Tổng** | **100** | |

**Publish Gate:**
- Score < 60 hoặc có Hard Block → Nút Publish bị disable hoàn toàn.
- Score 60-79 → Publish với badge "⚠ Cần tối ưu".
- Score ≥ 80 → Publish bình thường.

**9 Hard Block Conditions:** Canonical không tồn tại | Canonical sai URL | Robots = noindex | LCP > 2.5s | INP > 200ms | CLS > 0.1 | Không có CTA | Primary Keyword trống | CWV chưa Run.

---

### 6.6. M5 - SEO Inventory

**Mục đích:** Là điểm khởi đầu của mọi dự án trên MoSpark. Quyết định Use Case nào đáng làm, Keyword nào nên sản xuất trước.

**Trạng thái:** Phase 1 Live (Manual - Excel). Phase 2 Planning (tích hợp Dashboard vào CMS).

**Luồng khởi tạo dự án:**

1. Xác định Use Case → tra Total Search Volume trong Inventory.
2. Hệ thống tự phân nhóm ưu tiên (4 tiers):
   - **Market Leader (SoV > 40%):** Duy trì, scale ngách.
   - **High Potential (SoV 20-40%):** Scale nội dung mạnh.
   - **Gap lớn (SoV < 20%):** Xây mới nền tảng.
   - **Mass Traffic:** Kéo user lớn về hệ sinh thái (Phạt Nguội, BHXH...).
3. PM nhập Business Context 12 fields.
4. Kick-off 7-Step GenAI Workflow.

**Priority Scoring (SEO-ICE):**
```
Opportunity Score = Search Volume × (Target SoV - MoMo SoV) × Expected W2A CR
Priority Score = Opportunity Score / Complexity (1-5)
```

**SoV Formula:**
```
SoV MoMo = Impression (GSC) / Total Volume Search
```

---

### 6.7. M6 - AI Crawler Policy

**Mục đích:** Kiểm soát cách AI systems hiểu và cite MoMo. Đây là foundation cho GEO - nếu robots.txt block nhầm search crawlers, mọi effort GEO đều vô nghĩa.

**Trạng thái:** robots.txt Layer 1 (`/*?` fix) đã Deploy. llms.txt chưa triển khai.

**3 loại AI crawler, 3 cách xử lý:**

| Loại | Ví dụ | Xử lý |
|---|---|---|
| Search/RAG crawler | OAI-SearchBot, Claude-SearchBot, PerplexityBot | **ALLOW** - phục vụ user queries real-time |
| Training crawler | GPTBot, ClaudeBot, Google-Extended | **Policy decision** - chờ Legal |
| Aggressive scraper | Bytespider, CCBot | **BLOCK** - không có referral benefit |

**llms.txt Architecture:**
- `momo.vn/llms.txt` - Master index (Layer 1 - cần làm).
- `momo.vn/{product}/llms-full.txt` - Full doc per product (Layer 2).
- Content rule: Giữ định nghĩa sản phẩm, điều kiện, quy trình. Loại bỏ lãi suất cụ thể, promotional copy, testimonials.

---

### 6.8. M7 - Help Center Agentic

**Mục đích:** Chuyển FAQ tĩnh thành AI Agent - user hỏi gì được trả lời ngay, giảm friction trước khi abandon.

**Trạng thái:** Đã đăng ký Agentic Org Program. Chờ phê duyệt.

---

### 6.9. M8 - Migration (Admin Panel → MoSpark)

**Mục đích:** Hợp nhất toàn bộ nội dung từ Admin Panel cũ sang MoSpark. Single Interface cho Inbound Team.

**Trạng thái:** Structure & Mapping Phase. Zero Redirect approach đã approve.

**Blog 2-Tier (giữ nguyên URL, không redirect):**

| Tier | URL | Use Cases |
|---|---|---|
| Tier 1 - Basic | `momo.vn/blog/*` | General, News, FAQ |
| Tier 2 - Advanced | `momo.vn/{use-case}/blog/*` | Vay Nhanh, Cinema, BH Ô tô, BH Xe máy |

**3 Migration Phases:** Foundation + `/blog/*` (4-6 tuần) → 4 special Use Case blogs (6-8 tuần) → Optimization + Decommission Admin Panel cũ (4 tuần).

**Success Gate:** Traffic retention > 98% | Indexation 100% trong 14 ngày | Zero redirect.

---

## 7. North Star & KPIs

### 7.1. North Star Metrics

MoSpark đóng góp vào 2 NSM của MoMo Web:

**New User Acquisition:**
```
Organic Traffic → Content/Tool → Ads Manager → Onelink → Install → Register → New User
```

**MAU Uplift:**
```
User trên Web → Ads (reactivation) → App Open → MAU
```

**GEO North Star (12 tháng):**
```
MoMo được cite trong top 3 AI engine responses cho 20 target PFM queries.
Engines: Google AI Overview, ChatGPT, Perplexity.
Current: 0% AI Chatbot referral vs Wise.com 40%+.
```

### 7.2. Platform KPIs

| KPI | Định nghĩa | Nguồn | Target 2026 |
|---|---|---|---|
| Organic Sessions | Sessions từ Organic | GA4 | Tăng trưởng YoY per Use Case |
| SoV per Use Case | Impression (GSC) / Total Volume Search | GSC + SEO Inventory | > 40% cho top 3 Use Case |
| W2A Conversion Rate | Click Onelink / Web Sessions | Appsflyer + Umami | Baseline → +2% per campaign |
| AI Citation Rate | MoMo được cite trong AI engine responses | Manual test + GA4 AI referral | 30% cho Primary Keywords |
| Content Quality Score | % bài đạt ≥ 80 SEO/GEO Score | MoSpark internal | 100% bài mới ≥ 80 |
| PM/PO Self-Service Rate | % LP/Campaign do PM/PO tự tạo | MoSpark logs | 80%+ |
| Time-to-Publish | Từ brief đến live | MoSpark logs | LP < 1 ngày, Blog < 3 ngày |
| Zero Hardcode Violation | Campaign bypass Ads Manager | Platform audit | 0 violations |

### 7.3. OKR Alignment 2026

| OKR | MoSpark đóng góp gì |
|---|---|
| O1: New User Growth via Organic & W2A | M2 (GenAI Content) + M3 (Ads Manager) → tăng organic traffic và W2A CR |
| O2: Platform Stability & Technical Readiness | M4 (Scoring Gate) + M6 (AI Crawler Policy) → không có bad pages live |
| O3: PLG/Utilities-Led SEO | M3 (Widget Library) + M2 (Tool content) → CIC checker, Loan calculator, Insurance tool |

---

## 8. Data Governance

### 8.1. Use Case là đơn vị gốc

Mọi entity trên MoSpark đều gắn vào `use_case_id`. Đây là sợi chỉ kết nối tất cả modules:

```
Use Case: Phạt Nguội
    ├── SEO Inventory: market_volume, momo_sov
    ├── Business Context: 12 fields, PM xác nhận
    ├── Keyword Registry: primary_keywords (unique)
    ├── Blog Content: /phat-nguoi/blog/*
    ├── Mini Web: /phat-nguoi
    ├── Ads Placements: Balloon + Widget
    └── Analytics: Umami URL group + GA4 segment
```

### 8.2. Chống Cannibalization - 3 lớp bảo vệ

- **Lớp 1 - SEO Inventory:** `primary_keyword` là UNIQUE trong database. Không cho 2 Use Case dùng cùng keyword.
- **Lớp 2 - GenAI Content:** Unique ID Check tại Keyword Master Registry trước mọi luồng sản xuất.
- **Lớp 3 - Blog Editor:** Bottom-Up Sync: khi Editor nhập Primary Keyword, tự check với Registry.

### 8.3. Quality Gate tổng hợp

| Gate | Điều kiện pass |
|---|---|
| Business Context Complete | Đủ 12 fields, PM xác nhận pháp lý - không thể proceed nếu thiếu |
| Outline Approval | PM approve outline trước khi AI viết bài |
| SEO/GEO Score ≥ 60 | Không có Hard Block - Publish bị disable nếu fail |
| CWV Pass | LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 - Hard Block |
| CTA Present | Field CTA không rỗng - Hard Block |

---

## 9. Roadmap 2026

### Phase 1: Foundation & Scale (Q2/2026 - Đang làm)

**Mục tiêu:** Stabilize production pipeline + chứng minh W2A conversion với Phạt Nguội pilot.

| Deliverable | Owner | Status |
|---|---|---|
| LP Builder - GPD Onboarding | Bảo | In Progress |
| GenAI Content: Scale Financial (Vay, VTS, CIC) | Thuận + Hiến | In Progress |
| Ads Manager Widget: Phạt Nguội + BHYT Shortcode | Thuận | In Progress |
| Umami Live - Phạt Nguội | Thuận | This week |
| SEO Inventory Dashboard v1 | Thuận (schema) + Hiến (data) | Planning |
| robots.txt Layer 2+3 | Hiến (spec) + Web Platform | Planning |

### Phase 2: Optimization Loops (Q3-Q4/2026)

**Mục tiêu:** Đóng vòng lặp tối ưu - từ publish đến measure đến improve.

| Deliverable | Timeline | Impact |
|---|---|---|
| Ads Manager Phase 2: Placement Registry + Conflict Resolution | Q3/2026 | Multi-Division song song |
| GSC Auto-Refresh: Phát hiện Content Decay | Q3/2026 | AI Enhance tự động |
| GEO SoV Dashboard: AI citation tracking per Use Case | Q3/2026 | Visibility vào AI Search |
| Ads Manager Phase 3: Retargeting + Multi-tenant | Q4/2026 | PM self-service hoàn chỉnh |
| llms.txt: Master index + per-product full doc | Q3/2026 | GEO first-mover |
| Interactive Blocks: Calculator, Simulator | Q4/2026 | PLG/Utilities SEO, anti-LLM moat |
| Health Alert: 404 + Traffic anomaly detection | Q4/2026 | Zero zero-traffic URL mới |

### Phase 3: Agentic Growth (2027+)

**Mục tiêu:** AI chủ động vận hành vòng lặp tăng trưởng, ít can thiệp thủ công.

| Capability | Mô tả |
|---|---|
| White Space Discovery | AI phát hiện ngách thị trường chưa có đối thủ, đề xuất Use Case mới. |
| Autonomous Campaign | AI lên plan, tạo content, setup Ads, monitor và optimize. |
| Personalized LP | Nội dung thay đổi theo hành vi và nguồn traffic từng user. |
| Agentic Help Center | AI Agent thay FAQ tĩnh, xử lý real-time support. |
| Semantic Linking Engine | Vector embeddings tự gợi ý và chèn internal link tối ưu. |

---

## 10. Rủi ro & Giảm thiểu

| # | Rủi ro | Khả năng | Impact | Cách xử lý |
|---|---|---|---|---|
| R1 | PM publish message sai trên trang tài chính YMYL | Trung bình | Cao | Business Context 12 fields + Legal Workflow + SEO Lead sign-off |
| R2 | Thuận overload khi deliver nhiều modules song song | Cao | Cao | Scope nhỏ theo Phase, gate rõ trước khi move module tiếp |
| R3 | Division bypass Ads Manager - nhờ Dev hardcode | Trung bình | Cao | "No hardcode" policy do Bảo enforce + training PM/PO trước khi access |
| R4 | Ads conflict giữa Division gây spam UX | Trung bình | Cao | Conflict Detection tự động (Phase 2) + Platform Admin resolve trước live |
| R5 | Ads ảnh hưởng SEO - bounce rate tăng | Thấp | Cao | Hiến monitor SEO signals; guardrail cứng (1 Popup/session) |
| R6 | Migration gây traffic drop | Thấp (Zero Redirect) | Rất cao | Monitor 2 tuần post-migration, rollback plan per phase |
| R7 | AI Citation Rate không cải thiện sau llms.txt | Trung bình | Trung bình | Treat như infrastructure; review sau 6 tháng với 3 signals |
| R8 | Cannibalization vẫn xảy ra qua edge cases | Thấp | Cao | Triple-layer prevention (Inventory + GenAI Registry + Blog Editor sync) |

---

## 11. RACI & Collaboration

### 11.1. Phân vai

| Vai trò | Trách nhiệm | Không làm |
|---|---|---|
| **Văn Hiến (SEO & GEO Lead)** | Set SEO/GEO standard, govern Quality Gate, input Market data, sign-off YMYL, audit AI Citation | Không execute tracking, không direct với Dev mà không có spec |
| **Bảo (Web Platform Manager)** | Product direction MoSpark, Placement Registry, enforce "no hardcode", PO Web Platform sprint | Không làm trực tiếp với Agency hay Inbound |
| **Thuận + Lộc (Developers)** | Build tất cả modules theo spec, Widget Library, database | Không tham gia campaign creation khi đã có self-service |
| **Mai (Inbound SEO Lead)** | Content production theo brief Hiến, điền Business Context cùng PM, off-page | Không làm trực tiếp với Web Platform - technical request qua Hiến |
| **PM/PO Cell Team** | Khởi tạo Use Case, xác nhận Business Context (chịu trách nhiệm pháp lý), approve Outline, tự tạo LP + Ads | Không chỉnh code hoặc nhờ Dev bypass MoSpark |

### 11.2. Escalation Path

Platform issues → Bảo → Hiến review (nếu SEO impact).
Content quality → Hiến → Mai (nếu Inbound cần training).
Resource/Policy → Hiến → Tuệ → Công (VP).

---

## 12. Tài liệu Liên kết

| Tài liệu | Nội dung | Link |
|---|---|---|
| SEO/GEO Playbook | Strategy + Operations workflow | [[04_MOSPARK_PLATFORM/mospark_seo_geo_playbook]] |
| Ads Manager BRD | Chi tiết 5 modules Ads | [[04_MOSPARK_PLATFORM/mospark_ads_manager]] |
| GenAI Content BRD | 7-step workflow + Governance | [[04_MOSPARK_PLATFORM/mospark_genai_content]] |
| SEO/GEO Scoring BRD | 100pt scoring model + Hard Block | [[04_MOSPARK_PLATFORM/mospark_seo_geo_score]] |
| SEO Inventory BRD | Market map + SoV + SEO-ICE | [[04_MOSPARK_PLATFORM/mospark_seo_inventory]] |
| Business Context Template | 12-field template | [[04_MOSPARK_PLATFORM/mospark_business_context]] |
| Migration BRD | Admin Panel → MoSpark | [[04_MOSPARK_PLATFORM/mospark_migration]] |
| AI Crawler Policy | llms.txt + robots.txt | [[04_MOSPARK_PLATFORM/mospark_llms_robots_txt]] |
| Chiến lược Nội dung | MoMo Content Strategy 2026 | [[01_STRATEGIC_PLAN/momo-content-plan-strategy]] |
| Master Context | Hienho Master Doc | [[00_HARNESS_CORE/hienho_master_doc]] |

---

## 13. Version Log

| Phiên bản | Ngày | Nội dung |
|---|---|---|
| v2.6 | 2026-05-12 | Khởi tạo cấu trúc Growth OS. |
| v2.7 | 2026-05-16 | Bổ sung GSC Loop & Semantic Linking. |
| v2.8 | 2026-05-16 | Tái cấu trúc footer + version log. |
| v3.0 | 2026-05-25 | Tái viết thành Product Vision + PRD đầy đủ. Tổng hợp 8 module. |
| v3.1 | 2026-05-25 | Viết lại ngôn ngữ cho rõ hơn, bỏ văn phong hàn lâm. Bổ sung Bối cảnh Chiến lược từ meetings (Anh Công, Huy Lê, A.Tường). |

---

*Owner: Văn Hiến (SEO & GEO Lead) | Version: v3.1 | Updated: 2026-05-25*
