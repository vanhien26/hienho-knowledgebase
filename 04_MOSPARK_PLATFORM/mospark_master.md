---
title: "MoSpark: AI-Powered Growth Platform - Product Vision & PRD"
description: >
  Master Document cho MoSpark Growth Platform.
  Product Vision, PRD hoàn chỉnh, kiến trúc kỹ thuật và quy trình vận hành.
version: v3.3
status: Active
owner: Văn Hiến (Web Product Lead)
last_updated: 2026-05-25
tags: [mospark, platform, growth-os, genai, seo, geo, prd, product-vision]
---

# MoSpark: AI-Powered Growth Platform
## Product Vision & PRD

> **Owner:** Văn Hiến (Web Product Lead) | **Version:** v3.3 | **Updated:** 2026-05-25

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

> **"MoSpark là nền tảng Growth Intelligence của momo.vn: CEO, VP và Head of BU thấy rõ Market Sizing từng Use Case để ra quyết định triển khai đúng - PM/PO tự chủ thực thi từ ý tưởng đến kết quả kinh doanh thực, không phụ thuộc Dev."**

> **Elegant Problem:** momo.vn không thể tăng trưởng organic bền vững khi PM phụ thuộc Dev cho mọi thứ, AI sản xuất content không có guardrail, và không ai biết MoMo đang chiếm bao nhiêu % thị trường tìm kiếm.

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

### 2.1. Mandate Chiến lược

momo.vn Website không còn là corporate site hay blog SEO đơn thuần. MoSpark được xây để hiện thực hóa 3 vai trò chiến lược:

| Vai trò | Định nghĩa | MoSpark đóng góp gì |
|---|---|---|
| **Financial & Payment Authority** | Điểm đến uy tín, tiếng nói có thẩm quyền trong ngành tài chính/thanh toán Việt Nam | Quality Gate bắt buộc, Named Author Policy, E-E-A-T content chuẩn YMYL |
| **Entry Point từ Search** | Điểm chạm đầu tiên đón traffic tìm kiếm tự nhiên - cả Google lẫn AI Search | SEO Inventory, GenAI Content Engine, llms.txt pipeline |
| **Ecosystem Support Layer** | Nền tảng hỗ trợ toàn bộ hệ sinh thái kinh doanh & thanh toán của MoMo | Use Case ID gắn kết mọi module, Ads Manager, Web-to-App attribution |

**Flow bất biến - mọi quyết định sản phẩm đều trace về đây:**
```
Content → Keywords → Ranking → Use Case → User Journey → App/Transaction (New User / MAU)
```

Mục tiêu không dừng ở pageview. Mục tiêu là kích hoạt hành vi chuyển đổi trong App.

### 2.2. 4 Growth Pillars - Kiến trúc Thị trường

momo.vn không tổ chức theo BU - tổ chức theo Product / Search Ecosystem. 4 Pillars là 4 growth engine độc lập, mỗi Pillar sở hữu một vertical thị trường để chiếm thị phần tìm kiếm:

| Pillar | Use Cases | Chiến lược Content | Ràng buộc bắt buộc |
|---|---|---|---|
| **P1 - Tài chính & Tín dụng** | CIC Score, Ví Trả Sau, Vay Nhanh | Hub-Spoke + Interactive Tools (tính lãi, mô phỏng CIC) | Named Author Policy - hard gate trước launch |
| **P2 - Bảo hiểm Công nghệ** | BH xe máy, BHYT, BHXH, BH ô tô | Neutral Aggregator - cổng so sánh trung lập | Không dùng geo-based URL cho bảo hiểm |
| **P3 - Dịch vụ Công & Tiện ích** | Phạt Nguội, Hóa đơn | API real-time + pSEO (63 tỉnh) | llms.txt mandatory trước rollout |
| **P4 - Đời sống & Merchant** | Cinema, OTA, eSIM, Merchant | Intent-first, Merchant Detail Page | 410 Gone mandatory cho URL hết hạn |

**Utility-First** là nguyên tắc vận hành: Interactive tools (calculator, simulator, checker) là core value thực sự - content là supporting layer tạo discoverability và giáo dục. Mỗi Use Case mới phải trả lời: "Utility tool của Use Case này là gì?"

### 2.3. Bối cảnh thị trường

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

### 3.4. MoSpark KHÔNG phải

Scope rõ không kém scope có. Dưới đây là những gì MoSpark không làm - để tránh scope creep và giữ đúng mandate:

| MoSpark KHÔNG phải | Lý do cần nói rõ |
|---|---|
| **Một CMS thụ động thay thế Admin Panel** | MoSpark là Growth OS có Quality Gate và AI Production tích hợp - không đơn thuần thay cái cũ bằng cái tương đương |
| **Công cụ tự publish không kiểm soát** | Mọi trang đều phải qua SEO/GEO Scoring Gate - không có ngoại lệ, không có bypass dù PM/PO tự làm |
| **Thay thế Dev hoàn toàn** | PM/PO tự làm LP và Ads Manager trong phạm vi đã build - module mới vẫn cần Dev theo spec |
| **Platform để AI tự publish YMYL content** | AI draft - con người review và sign-off trước publish, bắt buộc với nội dung tài chính |
| **Giải pháp mở rộng cho tất cả BU cùng lúc** | GTM bắt đầu từ User Growth - chứng minh giá trị trước, scale từng Pillar có dữ liệu sau |
| **Hệ thống tích hợp Payment trực tiếp** | Excluded scope do rào cản pháp lý và after-sale service - không phải roadmap |

---

## 4. Users & JTBD

### 4.1. Nhóm người dùng

| Persona | Ai | Pain point | Cần gì từ MoSpark |
|---|---|---|---|
| **PM/PO Cell Team** | PO Vay Nhanh, Cinema, Bảo Hiểm, Phạt Nguội... | Phụ thuộc Dev cho LP, Ads, content | Tự tạo LP, chạy Ads, nhập Business Context trong cùng ngày |
| **Content Writer / Inbound** | Mai, Agency content | Đăng nhập nhiều CMS, prompt AI mỗi người mỗi kiểu | 1 interface duy nhất, AI pipeline chuẩn hóa, không cần học lại |
| **Web Product Lead** | Văn Hiến | Audit thủ công từng trang, không có SoV visibility | Quality gate tự động, SoV dashboard, data để quyết định đầu tư Use Case nào |
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

**Web Product Lead cần:**
1. Block được nội dung kém chất lượng trước khi ảnh hưởng domain authority.
2. Thấy được AI engine đang cite MoMo như thế nào cho từng Use Case.
3. Ưu tiên Use Case nào đáng đầu tư dựa trên Market Volume và SoV gap thực tế.

---

## 5. Kiến trúc Platform

MoSpark vận hành theo 5 lớp, phủ kín toàn bộ lifecycle từ market research đến conversion, đo lường và tối ưu liên tục:

| Layer | Tên | Status | Modules | Vai trò |
|---|---|---|---|---|
| **L5** | Growth Intelligence | Phase 2-3 | GEO Citation Monitor, Experiment Engine, Revenue Attribution, Content Intelligence | Close feedback loop: đo lường toàn bộ vòng lặp, học hỏi, cải tiến compound |
| **L4** | Performance Loop | Phase 2 | GSC Auto-Refresh, SoV Tracker, Content Decay Detection, Health Alert, Semantic Linking | Feed data ngược lại để tối ưu tiếp |
| **L3** | Quality Gate | Active | SEO/GEO Scoring 100pt, Hard Block CWV, Legal Review, YMYL Guard | Block nội dung xấu trước publish |
| **L2** | Distribution & Conversion + PLG | Active - Scaling | Ads Manager, Widget Library, PLG Tool Builder, Onelink, Umami Attribution | Convert traffic thành App user + PLG Tools tạo data moat chống LLM |
| **L1** | Content Production | Active - Pilot | SEO Inventory, Business Context, 7-Step AI Workflow, Blog Editor | Sản xuất nội dung đạt chuẩn |
| **F** | Foundation - Use Case System | Always-on | Use Case ID, Market Map, Keyword Registry, URL Governance, PLG Tool Registry | Đơn vị gốc kết nối tất cả modules |

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
| M9 | PLG Tool Builder | Utility Tool Platform | Planning - Spec Phase | 2 | Bảo + Thuận + Hiến |
| M10 | Experiment Engine | Native AB Testing | Planning | 2 | Thuận + DA |
| M11 | Revenue Attribution | Web-to-App ROI Pipeline | Planning | 2 | Thuận + DA (Hải/Hoàng) |
| M12 | Content Intelligence | Decay Detection + Opportunity | Planning | 2→3 | Thuận + Hiến |
| M13 | GEO Citation Monitor | AI Engine Citation Tracking | Planning | 2 | Hiến (spec) + Thuận |

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
| 6 | Review chất lượng, SEO/GEO Score, sign-off | Verified Content | Web Product Lead |
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

### 6.10. M9 - PLG Tool Builder

**Mục đích:** Chuẩn hóa build và deploy Utility Tools trên momo.vn. PM/PO tự tạo Calculator, Checker và Comparison tool mà không cần Dev sprint. Mỗi tool tạo ra interaction data độc quyền - đây là anti-LLM moat thực sự của momo.vn.

**Trạng thái:** Planning - Spec Phase.

**Vì sao PLG Tool là core value, không phải nice-to-have:**

| Kênh | Cơ chế chuyển đổi | Số bước đến intent cao nhất |
|---|---|---|
| Content Blog | User đọc → có thể click CTA → có thể download App | 3-4 bước, intent decay theo mỗi bước |
| PLG Tool | User DÙNG tool để giải quyết việc → nhận kết quả → CTA sau result | 1-2 bước, intent ở đỉnh khi nhận kết quả |

Utility-First không phải slogan - đây là cơ chế chuyển đổi khác nhau về cấu trúc.

**4 Tests phân biệt PLG Tool thực sự với widget thông thường:**

| Test | Câu hỏi kiểm tra | Pass khi |
|---|---|---|
| **JTBD Test** | Tool giải quyết JTBD cụ thể mà không cần user download App trước? | User hoàn thành task trong 1 phiên trên web |
| **Data Test** | Tool tạo interaction data mà LLM không thể có từ nguồn khác? | Data là unique: usage patterns, regional distribution, real-time inputs |
| **1-2-3 Test** | User nhận kết quả trong 3 bước, không cần hướng dẫn? | No tutorial needed, no drop-off mid-flow |
| **Funnel Test** | CTA sau kết quả dẫn về App feature tương ứng một cách tự nhiên? | CTA xuất hiện sau result, không interrupt trước |

**3 Loại PLG Tool - Taxonomy:**

| Loại | Cơ chế | Ví dụ trên momo.vn | Pillar |
|---|---|---|---|
| **Type A - Calculator** | User nhập thông số → tính theo công thức → kết quả số | Tính lãi vay, Tính phí BH xe máy, Tính lãi tiết kiệm, Tính mức phạt theo lỗi vi phạm | P1, P2, P3 |
| **Type B - Checker / Lookup** | User nhập ID → query API real-time → kết quả cụ thể | Tra phạt nguội (biển số xe), Tra điểm tín dụng CIC, Tra BHXH eligibility | P1, P3 |
| **Type C - Comparison / Aggregator** | Platform pull data nhiều nguồn → user filter → bảng so sánh | So sánh gói BH xe máy, So sánh gói cước viễn thông, So sánh lãi suất tiết kiệm | P2, P4 |

**Mapping PLG Tools theo 4 Growth Pillars:**

| Pillar | Tools cần build | Data được tạo ra | Priority |
|---|---|---|---|
| **P1 - Tài chính & Tín dụng** | Loan calculator, CIC score simulator, VTS eligibility checker | Nhu cầu vay theo khu vực, phân phối credit score người dùng thực tế | P0 |
| **P2 - Bảo hiểm Công nghệ** | BH cost calculator (xe máy, ô tô, BHYT), Plan comparison | Phân phối mức phí thị trường, preference theo gói, demographic | P1 |
| **P3 - Dịch vụ Công & Tiện ích** | Phạt nguội lookup (LIVE - mở rộng), BHXH checker, Hóa đơn lookup | Volume tra cứu theo loại vi phạm, khu vực, thời điểm | LIVE - scale |
| **P4 - Đời sống & Merchant** | Merchant finder, Cinema showtime lookup | Demand theo khu vực, genre preference, payment pattern | P2 |

**Builder Requirements - PM/PO phải tự làm được không qua Dev:**

1. Chọn Tool Type (Calculator / Checker / Comparison)
2. Define inputs: tên field, data type, required/optional, validation rule
3. Configure logic: công thức tính (Type A) | API endpoint + params (Type B) | data source + filter columns (Type C)
4. Set result format: số đơn | bảng chi tiết | Yes/No + lý do | range
5. Add CTA sau result: text, Onelink deep link đến App feature cụ thể
6. Set tracking: submit_tool + view_result + click_cta - tự động, không config thêm
7. Embed via shortcode: `[tool:loan-calculator]` vào bất kỳ page nào trong MoSpark
8. Preview mobile/desktop → Publish

**Data Pipeline - Cách PLG Tools tạo anti-LLM Moat:**

```
User query → Tool interaction → Result served
                 ↓ (anonymous log, no PII)
         Aggregate weekly batch
                 ↓
    Unique Insights được publish:
    "Mức phạt vượt đèn đỏ trung bình tại HCM: Xđ (Y tra cứu, tháng Z/2026)"
    "Người VN vay trung bình Xtr, kỳ hạn Y tháng, lãi suất kỳ vọng Z%/năm"
                 ↓
    Data Articles → GEO Citation Signal → LLM-proof unique content
```

Không có competitor nào có data này. Không LLM nào có thể fabricate data này. Đây là moat duy nhất bền vững trong thời đại AI content.

**Success Metrics:**

| Metric | Định nghĩa | Target |
|---|---|---|
| Tool sessions/tháng | Lượt sử dụng per tool | > 100K/tool P0 trong 6 tháng live |
| Tool → CTA click rate | % user click CTA sau khi nhận result | > 15% |
| Tool → Onelink (W2A proxy) | Sessions từ tool có click Onelink | Baseline Q3/2026 |
| Data points collected | Anonymous interaction records | > 1M/tool/năm |
| AI citation từ tool data | AI engines cite MoMo data insights trong responses | Measure Q4/2026 |

---

### 6.11. M10 - Experiment Engine

**Mục đích:** Infrastructure để PM/PO chạy AB test trên Web mà không cần Dev. Section 7.4 mandates AB Test Hypothesis trong mọi spec - M10 là infrastructure để mandate đó có nghĩa thực tế thay vì chỉ là formality.

**Trạng thái:** Planning. Prerequisite trước khi scale M1 (LP Builder) ra toàn GPD.

**Gap hiện tại:** MoSpark track events nhưng không có infrastructure để *serve variants*. Mọi claim "cải tiến" sau publish là opinion, không phải data.

**Capabilities:**

| Capability | Mô tả |
|---|---|
| **Variant assignment** | URL-based (A/B routes riêng) hoặc component-based (in-page swap không reload) |
| **Traffic split** | PM set % phân chia, system assign ngẫu nhiên + consistent per session |
| **Statistical engine** | Tự tính significance khi đủ sample size. Alert khi p < 0.05 |
| **Auto-winner** | Winner xác định → notify PM → 1-click promote variant lên production |
| **Experiment log** | Full history: experiment ID, variants, duration, sample size, winner, uplift |

**Integration:** Events từ experiment tự động gắn `experiment_id` + `variant` vào Umami. Success metric lấy từ downstream: Install, KYC, Transaction (Appsflyer pipeline).

**Success Metrics:**
- Experiments launched per quarter: 10+
- % LP mới có ít nhất 1 completed experiment trước khi scale: 80%+
- Winner detection time trung bình: < 21 ngày

---

### 6.12. M11 - Revenue Attribution Pipeline

**Mục đích:** Trace đầy đủ từ Web content/tool → Web-to-App → New User / MAU / Transaction. Business Owner mindset yêu cầu PM và Hiến biết ROI của từng Use Case - hiện tại không có cách đo end-to-end.

**Trạng thái:** Planning. Cần Umami + Appsflyer ổn định trước khi build unified layer.

**Pipeline 4 lớp:**

| Layer | Track gì | Tool | Output |
|---|---|---|---|
| Web behavior | Session → Page → Content → Tool → CTA click | Umami per URL group | Content attribution |
| Click | Onelink click → source URL → device | Appsflyer + Umami | Channel attribution |
| Install funnel | Install → Register → KYC → Cashin | Appsflyer Track 2 | User funnel |
| Revenue proxy | Transaction type + frequency per cohort | App event → BigQuery | Revenue signal |

**Unified View per Use Case:**
```
Use Case: Vay Nhanh [tháng X/2026]
├── Organic sessions: 120,000
├── Onelink clicks: 4,200 (3.5% CTR)
├── Installs: 1,260 (30% click → install)
├── KYC completed: 630 (50% install → KYC)
├── First loan: 189 (30% KYC → transaction)
└── CAC proxy: [total web cost / New User attributed]
```

**Success Metrics:**
- Full attribution pipeline live cho top 5 Use Cases: Q3/2026
- % Use Cases có ROI dashboard đủ để justify continued investment: 100% Q4/2026
- CAC per Use Case tracked và có trend line improving QoQ

---

### 6.13. M12 - Content Intelligence Loop

**Mục đích:** Phát hiện content decay trước khi thành zero-traffic URL. Surface keyword opportunities chưa được cover. Đóng feedback loop giữa publish và optimize - thứ hiện tại bị đứt hoàn toàn sau bước publish.

**Trạng thái:** Planning. Phase 2. Context: 3,670 zero-traffic URLs hiện tại là hậu quả trực tiếp của việc thiếu module này.

**12a. Content Decay Detection:**

| Signal | Threshold | Action |
|---|---|---|
| Traffic giảm > 20% trong 4 tuần liên tiếp | Warning | Alert Hiến + Mai |
| Traffic giảm > 50% trong 8 tuần | Critical | AI Enhancement queue - draft re-write |
| Zero traffic > 90 ngày | Zero-traffic | URL audit: 410 Gone / Redirect / Rewrite decision |

GSC integration: weekly pull impression + click per URL. Dashboard severity: Warning / Critical / Zero count by Use Case và Pillar.

**12b. Keyword Opportunity Surfacing:**
- **Near miss list:** GSC queries MoMo rank position 4-15 × volume > 1K/tháng → sorted by (Volume × Position Gap). Brief content update được auto-generate.
- **White space:** keyword cluster có volume nhưng 0 URL của MoMo → new content brief tự động đưa vào GenAI queue.
- **Cluster gap:** so sánh keyword coverage hiện có với SEO Inventory target per Use Case.

**Success Metrics:**
- Zero-traffic URL mới sau khi M12 live: 0/tháng
- Near miss keywords promoted lên top 3 per quarter: 20+
- Decay detection coverage: 100% URLs đang live được monitor weekly

---

### 6.14. M13 - GEO Citation Monitor

**Mục đích:** Đo North Star GEO: MoMo được cite trong top 3 AI engine responses cho 20 target PFM queries. Hiện không có cách đo tự động - đây là blocker để biết GEO strategy có work không và llms.txt có effect gì.

**Trạng thái:** Planning. Build song song với M6 (llms.txt rollout).

**Monitoring Setup:**

| AI Engine | Method | Frequency |
|---|---|---|
| ChatGPT (GPT-4o) | OpenAI API query + parse response | Weekly |
| Perplexity | Perplexity API query + source detection | Weekly |
| Google AI Overview | GSC AI referral data + manual sampling | Weekly |

**Query Library - 20 Seed Queries × 4 Pillars:**

| Pillar | Ví dụ seed queries |
|---|---|
| P1 - Tài chính | "vay tiền online uy tín VN", "check điểm tín dụng miễn phí", "ví điện tử có BNPL VN" |
| P2 - Bảo hiểm | "bảo hiểm xe máy bắt buộc là gì", "so sánh gói bảo hiểm sức khỏe VN" |
| P3 - Tiện ích | "tra cứu phạt nguội online", "kiểm tra BHXH còn bao nhiêu tháng" |
| P4 - Đời sống | "thanh toán vé CGV bằng ví điện tử", "mua esim du lịch Thái Lan giá rẻ" |

**Dashboard Metrics:**

| Metric | Định nghĩa | Hiện tại | Target Year 1 |
|---|---|---|---|
| Citation Rate | % queries MoMo xuất hiện trong response | 0% | 30%+ (bắt đầu từ P3) |
| Citation Position | Thứ tự xuất hiện trong response | N/A | Top 3 |
| Citation Accuracy | Claim MoMo được cite có đúng không | N/A | 100% accurate |
| Weekly trend | Change after llms.txt events | - | Positive correlation |

**Trigger:** Citation Rate giảm đột ngột → check llms.txt status + content freshness + competitor action.

**Success Metrics:**
- 20 target queries tracked weekly: Q3/2026
- Citation Rate > 30% cho P3 queries (data-rich, easiest entry point): Q4/2026
- Citation Rate > 20% across all 4 Pillars: End 2027

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

### 7.4. Measurement-First - Bắt buộc với mọi Spec

"Tốc độ ship mà không có AB test thì không thể cải tiến." MoSpark không chỉ là nơi tạo trang - là nơi học hỏi và cải tiến liên tục. Mọi spec/BRD gửi cho Web Platform phải có 2 field bắt buộc trước khi bắt đầu build:

| Field | Yêu cầu | PIC |
|---|---|---|
| **Tracking Event Schema** | List event cần track: event name, properties, trigger condition. Không skip với lý do "sẽ làm sau" | Hiến define standard, DA execute |
| **AB Test Hypothesis** | Variant A (baseline) vs Variant B (thay đổi) + success metric cụ thể. Không phải "test xem sao" | PM/PO của Use Case đó |
| **Success Metric trace về NSM** | Metric chính phải trace về New User / MAU / W2A CR - không chỉ pageview hay session | Hiến sign-off |

Thiếu Tracking Event Schema hoặc AB Test Hypothesis - spec chưa complete, Web Platform không bắt đầu build.

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
| **Văn Hiến (Web Product Lead)** | Set SEO/GEO standard, govern Quality Gate, input Market data, sign-off YMYL, audit AI Citation | Không execute tracking, không direct với Dev mà không có spec |
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
| Microsite Management (Product + Dev Spec) | Quản lý Mini Web - Product Spec + Data model, API, Acceptance Criteria cho Hoài Anh | [[04_MOSPARK_PLATFORM/mospark_microsite_management]] |
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
| v3.2 | 2026-05-25 | Redesign Section 2: xóa meeting-transcript style, thay bằng Mandate Chiến lược (2.1) + 4 Growth Pillars (2.2) + đổi tên 2.2 cũ thành 2.3. Bổ sung Elegant Problem Statement (Section 1.1), MoSpark KHÔNG phải (Section 3.4), Measurement-First bắt buộc (Section 7.4). |
| v3.3 | 2026-05-25 | Bổ sung 5 modules mới M9-M13: PLG Tool Builder (full spec với 4-test framework + 3 tool types + data pipeline), Experiment Engine, Revenue Attribution Pipeline, Content Intelligence Loop, GEO Citation Monitor. Update kiến trúc platform lên 5 lớp. Update Module Catalog table. Thêm 3 Mermaid diagrams cho M9: 4-Test Decision Framework, Tool Types + Pillar Mapping, Data Pipeline → GEO Moat. |

---

*Owner: Văn Hiến (Web Product Lead) | Version: v3.3 | Updated: 2026-05-25*
