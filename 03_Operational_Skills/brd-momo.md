---
name: momo-brd-enhanced
description: "Viết Business Requirements Document (BRD) chuẩn cho Use Case / Project của MoMo Out-App Traffic / GPD. BRD define Why (bối cảnh, vấn đề, cơ hội từ keyword research + business insight), What (scope, JTBD, requirements, success metrics dựa trên organic traffic / W2A conversion / ranking keywords) để align stakeholder. Trigger: 'viết BRD', 'BRD cho dự án', 'kick-off use case', 'align stakeholder', hoặc user muốn đóng gói use case/project thành BRD chính thức. Skill hỏi khai thác trước khi viết - không tự viết ngay khi thiếu context. Input: Business Context (slide/text), Keyword CSV, Direction brief. Output: `.md` file."
---

# MoMo BRD Enhanced Skill

## Mục tiêu

Từ 3 input (Business Context + Keyword Research CSV + Direction brief), skill khai thác đủ context để viết BRD hoàn chỉnh. BRD power-driven bởi **[[jtbd-analysis|keyword research + search intent analysis]]** để định hình JTBD chính xác, và **define success metrics concrete** (Organic traffic via GSC, Web2app %CR via Onelink+Appsflyer, Ranking keywords high-volume). Sử dụng **[[pyramid-principle|Pyramid Principle]]** để cấu trúc nội dung. BRD phục vụ: PO, Eng Lead, Stakeholder/Management.

Hỗ trợ **2 loại dự án:**
- **Use Case** (Vay Nhanh / Cinema / Bus) - acquisition-focused, content-heavy
- **Project** (Merchant Page / CMS feature) - product/platform, limited scope

---

## Workflow (3 Bước)

### Bước 1: Xác định Input & Project Type

Trước khi hỏi user, kiểm tra conversation đã có:
- **File upload?** HTML / Slide / Doc / CSV → Đọc trước, extract thông tin
- **Text brief?** → Extract Business Context từ đó
- **Keyword CSV?** → Kiểm tra format (keyword, search volume, difficulty, intent...)

**Xác định Project Type:**
- **Use Case:** Vay Nhanh / Cinema / Bus / eSIM → acquisition-focused, SEO/GEO strategy, content hub
- **Project:** Merchant Page / CMS feature / Landing page / Tool → limited scope, product-driven

→ Project Type sẽ **điều khiển sections nào bắt buộc, cái nào optional**.

---

### Bước 2: Khai Thác Thông Tin (Interview)

Sau khi đọc input, xác định **gap** - thông tin còn thiếu. Hỏi **tối đa 1 lần**, gom tất cả câu hỏi vào 1 message.

**Thông tin bắt buộc phải có trước khi viết BRD:**

| Nhóm | Thông tin | Cách khai thác |
|---|---|---|
| **Identity** | Tên use case / project, URL / feature path, Owner, Timeframe | "Tên dự án? URL chính? Owner là ai? Timeframe mong muốn?" |
| **Business Context** | Value prop, đối tượng user, hiện trạng (nếu có baseline), vấn đề cốt lõi | "Value prop của [use case] là gì? Ai dùng? Baseline current state?" |
| **Keyword Research** | CSV file gồm keywords + volume (hoặc tôi sẽ ingest format) | "CSV có gồm keyword, search volume, intent hint không?" |
| **Direction Brief** | Chiến lược tăng trưởng, scope muốn build, OKR/target | "Chiến lược là gì? Build cái gì? Target org traffic / W2A rate / ranking keywords là bao nhiêu?" |
| **Baseline Metrics** | Current organic traffic (GSC), current W2A %CR (Onelink/Appsflyer), current ranking (SEO tool) | "Có baseline metrics nào không (GSC traffic, W2A rate, ranking)? Hoặc cần tôi tính từ đâu?" |

**Thông tin nice-to-have (ghi "[cần verify]" nếu thiếu):**
- Competitor analysis (search result landscape)
- User research / JTBD insights (nếu có)
- Technical constraints (tracking, compliance)
- Dependencies (PO Cell, Dev team, DA team status)

**→ Không hỏi những gì đã có trong input. Chỉ hỏi gap.**

---

### Bước 3: Process Keyword Research & Viết BRD

**Nếu user cung cấp Keyword CSV:**

1. **Ingest CSV** → Extract: keyword, search volume, intent hint (nếu có)
2. **Cluster keywords** theo intent tiers:
   - **Know intent:** "là gì", "định nghĩa", "cách", "hướng dẫn" → Educational JTBD
   - **Do intent:** "cách làm", "bước", "tools", "tutorial" → Action/Skill JTBD
   - **Go intent:** "trang web", "ứng dụng", "nơi", brand name → Navigation JTBD
   - **Buy intent:** "đánh giá", "so sánh", "giá", "mua", "vay", "bảo hiểm" → Decision/Transaction JTBD
3. **Map keyword clusters → JTBD** (3-6 Jobs, ưu tiên high-volume clusters)
4. **Infer search user context** từ keyword + Internet insights (competitor pages, product landscape)

**Viết BRD với sections tối ưu cho project type:**
- **Use Case** (Vay / Cinema / Bus): Full sections 1-10 (JTBD power-driven by keywords)
- **Project** (Merchant / CMS feature): Rút gọn sections 1-7 (skip 8-9 nếu không có dependencies/risks)

→ Viết file `.md` và save vào `/mnt/user-data/outputs/`

---

## Cấu Trúc BRD - 2 Variants

### **Variant A: Use Case BRD** (Vay Nhanh / Cinema / Bus / eSIM)
Dành cho acquisition-focused, content-heavy, long-term growth.

```
# BRD: [Use Case Name]

> Project: [Tên Use Case]
> Main URL: [URL hub/hub page]
> Owner: [Team/Người]
> Timeline: [Start date → Target completion]
> Version: [X.X · Tháng Năm]
> Status: [Draft / In Review / Approved]
```

**Sections bắt buộc:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
**Sections optional:** Appendix (nếu có growth tactics / data to verify)

---

### **Variant B: Project BRD** (Merchant Page / CMS feature / Landing page)
Dành cho product/platform, limited scope, shorter timeline.

```
# BRD: [Project Name]

> Project: [Tên Project]
> Main URL/Feature path: [URL hoặc feature ID]
> Owner: [Team/Người]
> Timeline: [Start date → Target completion]
> Version: [X.X · Tháng Năm]
> Status: [Draft / In Review / Approved]
```

**Sections bắt buộc:** 1, 2, 3, 4, 6, 7
**Sections rút gọn/skip:** 5 (JTBD), 8 (Dependencies - chỉ nếu có), 9 (Risk - chỉ nếu có)

---

## Cấu Trúc Section Chi Tiết

### Section 1: Executive Summary

Viết theo cấu trúc **SCR (Situation - Complication - Resolution)**:

- **Situation:** Bối cảnh hiện tại. Thị trường ra sao? MoMo đang ở đâu? Cơ hội/asset đang có là gì?
- **Complication:** Vấn đề cốt lõi. Tại sao hiện trạng chưa đủ? Số liệu chứng minh. Gap là gì?
- **Resolution:** Dự án này làm gì để giải quyết? Kết quả kỳ vọng ở mức cao.

*Giữ trong 3-5 đoạn. Đây là phần stakeholder đọc đầu tiên - phải đủ sharp để họ hiểu toàn bộ Why mà không cần đọc tiếp.*

---

### Section 2: Bối Cảnh Hiện Tại

Trình bày evidence cho Complication. Bao gồm:

- **Hiện trạng:** Table mô tả trạng thái hiện tại của dự án/tính năng/URL
- **Data/Metrics hiện có:** Số liệu baseline (traffic, conversion, volume, thị phần - tùy use case)
- **Phân tích cạnh tranh (nếu relevant):** Đối thủ đang làm gì? Cơ hội chênh lệch?
- **Trend/Seasonality (nếu relevant):** Dữ liệu thay đổi theo thời gian, emerging trend

*Mọi số liệu phải có nguồn hoặc ghi "[cần verify]". Không hallucinate data.*

---

### Section 3: Định Hướng Dự Án

Trả lời 3 câu:

1. **Dự án này phục vụ điều gì?** - Business objective cụ thể (Acquisition / Retention / Revenue / GEO...)
2. **Ai được phục vụ?** - User segment mục tiêu
3. **Dự án này KHÔNG phải là gì?** - Out of scope explicit. Quan trọng để tránh scope creep.

---

### Section 5: JTBD Analysis (Keyword-Driven)

**Chỉ bắt buộc cho Use Case. Project có thể skip nếu scope nhỏ.**

Từ **keyword clusters** (Do/Know/Go/Buy intent), extract **3-6 Jobs** có volume/impact cao nhất.

```
### Job #N: [Tên Job ngắn gọn]

**Search Intent Cluster:** [Ví dụ: "vay nhanh không thế chấp, xin vay online"]
**Volume:** [Tổng search volume cluster/month - từ CSV]

> Quote user insight: "Tôi cần [functional need]. Lý do: [emotional/social trigger]"

| Dimension | Nội dung |
|---|---|
| **Functional** | Họ cần làm gì cụ thể? Tại sao công cụ/dịch vụ hiện tại không đủ? |
| **Emotional** | Cảm xúc chính? (Tốc độ / An tâm / Tiết kiệm / Đơn giản / Độ tin tưởng) |
| **Social** | Muốn ẩn / công khai với ai? (Bí mật tài chính / Mang lại hình ảnh gì?) |
| **Trigger** | Situation nào khiến họ tìm kiếm? (Gấp tiền / Mua cái gì / Tính toán tài chính) |

**Serve bằng:**
- Content piece: [Tên page/content sẽ serve job này]
- Product feature: [Tính năng nào serve job này]
- User flow: [Quick reference đến section nào trong Architecture]
```

**Công thức extract JTBD từ Keyword:**
1. Lấy high-volume keyword cluster (≥500/month)
2. Analyze search intent: "người search từ này cần gì?" (functional) + "tại sao tìm?" (trigger)
3. Infer emotional/social từ context (product category, user segment, competitor search results)
4. Write job statement: "Tôi cần [functional] để [emotional trigger]"

**Số lượng JTBD:** 3-6 jobs. Ưu tiên high-volume clusters (80/20 rule).

---

### Section 6: Kiến Trúc & Scope Build

**Tùy loại dự án:**

#### **Nếu Use Case (Content-heavy):**
- **Sitemap / Content Structure:** URL architecture, content cluster (pillar + cluster pages)
- **Content Matrix:** Content type (Educational / Comparison / How-to), serving which Jobs, SEO intent, priority
- **GEO/AEO Strategy:** Location pages, entity coverage, local schema (nếu relevant)

**Format:**
```
| URL/Slug | Content Type | Primary Job | Priority | JTBD mapped | Tracking setup |
|---|---|---|---|---|---|
| `/vay-nhanh-online` | Pillar | Job #1, #2 | P1 | "Tôi cần vay nhanh" | GA4 event [content_viewed] |
| `/vay-nhanh-khong-the-chap` | Cluster | Job #1 | P1 | Functional: vay không cần tài sản | ... |
```

#### **Nếu Project (Product/Feature):**
- **User Flow / Screen Map:** Entry point, main screens, conversion point
- **Feature List:** Feature name, what job it serves, priority (P1/P2/P3)

**Format:**
```
| Feature | Description | Job/Trigger | Priority | 
|---|---|---|---|
| [Feature A] | [Mô tả] | [Job #N] | [P1/P2/P3] |
```

**Luôn phân loại:**
- **P1 (Launch blocker):** Bắt buộc có để launch
- **P2 (Core):** Quan trọng nhưng không block launch
- **P3 (Enhancement):** Nice-to-have, post-launch

---

### Section 6: Functional Requirements

Table format. Mỗi requirement có: Mô tả | Priority | Ghi chú.

Phân nhóm theo:
- Core requirements (bắt buộc để launch)
- Enhancement requirements (tốt hơn nhưng không block)
- Technical requirements (performance, tracking, schema...)

*Priority rules: P1 = block launch nếu thiếu. P2 = quan trọng nhưng không block. P3 = nice-to-have.*

---

### Section 7: Success Metrics (Keyword-Powered)

**3 KPIs bắt buộc:**

#### **1. Organic Traffic (via GSC)**
```
| Metric | Definition | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|---|
| Organic sessions (keyword cluster) | Sessions từ GSC, filtered by [keyword cluster filter/regex] | [X sessions/month] | [Y sessions/month] | [Timeline] | GSC API → GA4 dashboard |
| Avg ranking position (P1 keywords) | High-volume keywords (#1 trong keyword list), track avg position | [Current pos] | Top 3/5/10 | [Timeline] | SEO tool (Ahrefs/Semrush) |
```

**Logic baseline tính toán (nếu chưa có):**
- Nếu dự án NEW (chưa có landing): Baseline = 0 (cần note strategy cách tính expected ramp)
- Nếu dự án OPTIMIZE (có sẵn): Baseline = current GSC traffic (filtered by intent cluster)

**Logic target tính toán:**
- North Star: "Organic traffic từ [intent cluster] = [X% of search volume]"
  - Ví dụ: Keyword cluster "vay nhanh" tổng 50K/month search → Target 15% click-through = 7.5K sessions/month
  - Baseline hiện tại: 1K sessions/month → Target: 7.5K sessions/month (+650%)

#### **2. Web2App Conversion Rate**
```
| Metric | Definition | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|---|
| Traffic → Onelink CTA click % | (Sessions w/ Onelink CTA click) / (Sessions) | [X%] | [Y%] | [Timeline] | GA4: CTA click events / Session count |
| Onelink → Install %  | (Install via Onelink) / (Onelink clicks) | [X%] | [Y%] | [Timeline] | Appsflyer: onelink tracking |
| Install → Register+KYC → Cashin | (Cashin users from organic) / (Organic install) | [X%] | [Y%] | [Timeline] | Appsflyer → Cashin event (internal) |
| **W2A %CR (end-to-end)** | (Cashin users from organic) / (Organic sessions) | [X%] | [Y%] | [Timeline] | GA4 + Appsflyer funnel |
```

**Definition clarity:**
- **Organic session:** Session từ GSC, filtered by campaign/source/medium = organic
- **Onelink CTA click:** GA4 event "cta_click" + element contains "onelink" or "open_app"
- **Install:** Appsflyer event "install" with utm_source = "momo.vn" OR onelink tracking
- **KYC:** Appsflyer event "kyc_completed" (internal event setup)
- **Cashin:** Appsflyer event "first_transaction" (internal event setup)

**Target logic:**
- Benchmark W2A %CR: [user provides or calculate từ historical data]
- Example: Vay Nhanh current W2A = 2%, target = 3.5% (via improved CTA + mobile UX + Onelink tracking)

#### **3. Ranking Keywords (High-Volume)**
```
| Metric | Definition | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|---|
| Top 10 keywords (#) | # high-volume keywords ranking top 1-10 | [X] | [Y] | [Timeline] | SEO tool |
| Top 20 keywords (#) | # high-volume keywords ranking top 1-20 | [X] | [Y] | [Timeline] | SEO tool |
| Avg ranking position (P1 keyword set) | Avg position của [keyword list P1], weighted by volume | [X.X] | [Y.Y] | [Timeline] | SEO tool |
```

**Definition clarity:**
- **High-volume keywords:** Keywords trong CSV có search volume ≥ [threshold từ user input, default 500/month]
- **Ranking position:** Current rank từ SEO tool (Ahrefs/Semrush/internal tracking)
- **Top 10 / Top 20:** Position ≤ 10 / ≤ 20 (organic results, không ads)

#### **North Star Metric Selection**
```
Use Case type → North Star priority:

| Use Case | North Star | Secondary metrics |
|---|---|---|
| Acquisition (Vay/Cinema/Bus) | Organic sessions (traffic) | W2A %CR, ranking |
| Retention/Monetization (Features) | W2A %CR (conversion quality) | Organic traffic, feature adoption |
| SEO/Content (Brand presence) | Ranking (keyword coverage) | Organic traffic, brand search trend |
```

Choose **1 North Star** per BRD. Thường cho Use Case = Organic traffic (volume growth driver).

---

### Section 8: Dependencies & Constraints

**Bắt buộc cho Use Case, optional cho Project (skip nếu không có dependencies).**

| Dependency | Owner | Mô tả | Blocker? | Status |
|---|---|---|---|---|

**Phân biệt:**
- **Hard dependency** (Blocker = Yes): Không có → không launch được
- **Soft dependency** (Blocker = No): Không có → có fallback hoặc defer
- **Constraints** (giới hạn không thể thay đổi): Pháp lý, brand, kỹ thuật

**MoMo-specific dependency patterns:**

| Dependency Type | Owner | Examples |
|---|---|---|
| **PO Cell alignment** | PO Cell | Product feature availability, product roadmap, priority |
| **Dev / Engineering** | Dev Team | API readiness, GTM tracking setup, tracking implementation, schema deployment |
| **Data / Analytics** | DA Team | GA4 event setup, Appsflyer parameter config, BigQuery pipeline ready |
| **Inbound Content** | Inbound Team | Content calendar, editorial review, YMYL compliance, schema review |
| **Growth experiments** | Growth Team | A/B test infrastructure (PostHog, GTM), conversion test setup |
| **Tracking / GTM** | Web Platform / GTM Owner | Container update approval, tag deployment, QA |

---

### Section 9: Risk Assessment

**Bắt buộc cho Use Case, optional cho Project (skip nếu không có risks).**

| # | Rủi ro | Loại | Khả năng | Impact | Mitigation |
|---|---|---|---|---|---|

**MoMo Growth Project - Risk Patterns:**

| Risk Type | Common Risks | Mitigation Strategy |
|---|---|---|
| **Execution** | Timeline slip (content delay, dev delay), priority change, resource shortage | Weekly check-in, buffer timeline, clear ownership |
| **Data/Tracking** | GA4 event not firing, Onelink tracking incomplete, Appsflyer mapping error | QA tracking before launch, PostHog + GA4 dual-stack, weekly data audit |
| **Market** | Search volume lower than forecast, competitor outrank us faster, seasonality impact | Validation: compare GSC current rank vs target keyword list, monitor weekly rankings, seasonality factor in forecast |
| **Technical** | Schema not crawlable, mobile UX issue, page speed slow | Lighthouse score ≥ 90, Schema validation via Google Search Console, mobile test |
| **Product** | Feature not ready in time, API change, deprecation of Onelink | Confirm W2A funnel setup ASAP, fallback tracking method, coordinate with Appsflyer/Dev |

**Severity rule:** Nếu risk không có mitigation cụ thể → escalate ngay, không để "cần theo dõi".

---

### Section 10: Next Steps

| # | Deliverable | Owner | Description | Target date |
|---|---|---|---|---|

**Deliverables típico theo Use Case:**
- PRD (Content / Product) → describe pages, flows, content specs in detail
- Content Calendar + Editorial SOP → content production timeline, review process
- Tracking Setup Doc → GA4 events, Appsflyer parameters, PostHog dashboard
- GEO/AEO Checklist → if Use Case has location/entity angle
- QA Testing Plan → tracking QA, mobile UX, schema validation, W2A funnel test

**Deliverables típico theo Project:**
- PRD / Feature Spec → detailed product requirement
- Design Mockup / Wireframe → UI/UX
- Tracking Setup → GA4 events, schema (nếu có)
- QA Plan → feature testing, tracking test

---

### Appendix (optional)

Dùng khi có thông tin bổ sung không phù hợp đưa vào body BRD:
- **Appendix A:** Growth Tactics / đề xuất (nếu scope BRD không cover)
- **Appendix B:** Data tham khảo cần verify
- **Appendix C:** Glossary / định nghĩa thuật ngữ

---

## Quy Tắc Viết

### Tone & Format

- **Tiếng Việt chuyên nghiệp.** Giữ thuật ngữ kỹ thuật (SEO, JTBD, CTA, W2A, GSC, Appsflyer, P1...)
- **Senior-level, trực tiếp.** Không fluff, không mở đầu rườm rà. Mỗi câu phải có purpose.
- **Data-driven.** Mọi claim phải có source (GSC, Keyword research, competitor data)
- **Table > Prose.** Dùng table khi có 3+ items để so sánh hoặc list structured data (không bullet list dài)

### Về Data & Metrics

- **Số liệu bắt buộc có nguồn:** GSC (organic traffic), Appsflyer (W2A), SEO tool (ranking)
- **Baseline & Target phải có logic rõ ràng.** Không đặt target random - phải explain "tại sao target này?"
  - Ví dụ: "GSC hiện tại 1K sessions/month từ keyword cluster 'vay nhanh'. Keyword cluster này có tổng 50K search/month. Target 15% CTR = 7.5K sessions (150% growth)"
- **Nếu chưa có data → ghi rõ "[cần đo]" hoặc "[cần verify]".** Không hallucinate metrics.

### Về JTBD & Search Intent

- **JTBD phải anchor từ keyword research.** Không generic "user muốn trải nghiệm tốt"
- **Functional JTBD = gì mà user search?** Trigger JTBD = tại sao search lúc này?
- **Nếu không có user research → ghi "Hypothesis - cần validate với user testing"**
- **Emotional/Social infer từ product context:** Finance products → trust, speed, simplicity, privacy are key

### Về Scope & Out of Scope

- **Out of scope phải explicit, không mơ hồ.** Ví dụ: "KHÔNG build mobile app (app build by Mobile team)" không "KHÔNG cover mobile experience"
- **Nếu overlap với dự án khác → ghi rõ relationship.** Ví dụ: "Depends on PO Cell's 'W2A tracking' PRD"

### Về Priority

- **P1 = launch blocker.** Nếu không có toàn bộ P1 items → không nên launch
- **Không để toàn bộ là P1 - dấu hiệu chưa prioritize.** Rule of thumb: 40% P1, 40% P2, 20% P3
- **P3 mà không có timeline → cân nhắc move ra Appendix hoặc skip**

---

## Edge Cases & Handling

| Tình huống | Xử lý |
|---|---|
| **Keyword CSV format không chuẩn** | Hỏi user: "CSV có column nào? (keyword, volume, difficulty, intent?)" → Map vào standard format (keyword, search_volume, [difficulty], [intent_hint]) |
| **User không có baseline metrics** | Hỏi: "Có GSC access? Hay tôi tính estimate từ keyword volume?" → Ghi "[cần measure]" + define tracking method |
| **Use Case NEW (chưa tồn tại)** | Baseline = 0 nhưng phải explain ramp strategy: "Build từ scratch, expect ramp 3-6 months để reach target 5K sessions/month" |
| **Project quá nhỏ (1 page, 1 feature)** | Viết BRD rút gọn: bỏ Section 5 (JTBD), Section 8-9 nếu không có deps/risks |
| **Use Case quá lớn (toàn bộ Finance cluster)** | Viết BRD cluster-level (không per-page), detail sẽ trong PRD. Hoặc chia thành multi-BRD per sub-use-case |
| **User cung cấp slide + text + CSV mixed** | Đọc tất cả, extract thông tin, fill gaps với khai thác từ user. Không duplicate hỏi. |
| **W2A funnel không setup sẵn** | BRD sẽ include "W2A tracking setup" trong Dependencies hoặc Section 10 (Next Steps) - note blocker level |
| **Competitor có ranking cao, user không biết tại sao** | Suggest: "Analyze competitor content (content depth, freshness, backlinks). Add to Section 2 (Context)" → inform JTBD & content strategy |
| **Seasonality / event impact lớn** | Flag trong Risk + Success Metrics (adjust baseline/target for seasonality factor). Ví dụ: "Cinema traffic peak Dec → target adjusted +50% for that month" |

---

## Output & Delivery

- **File format:** `.md` (Markdown)
- **File name:** `[use-case-or-project-name]-brd.md`
- **File location:** `/mnt/user-data/outputs/`
- **After creation:** Dùng `present_files` tool giao file cho user + summary (max 5 dòng):
  - Tên file + Use Case / Project type
  - Số sections + keywords processed
  - Điểm cần user verify / bổ sung
  - Recommend next step (PRD / Content Calendar / Tracking Setup)

**Never output BRD as:**
- Inline markdown trong chat (file quá dài, khó edit)
- HTML (dùng `.md`, user có thể convert sau nếu cần)
- Google Doc / Notion link (tất cả output phải download-able từ Claude)
