# 📄 Use Case Document
_use-case-document  
description: Tạo Web Growth Strategy Document cho bất kỳ Use Case nào của MoMo.vn.  
---

- Trigger khi user nhắc: web growth strategy, use case document, strategy doc,  
growth plan, zero to one, kick-off Use Case mới, master doc, tài liệu chiến lược. 
- category: strategy-document  
tags:  
- web-growth  
- strategy  
- use-case  
- momo  
- fintech  
- zero-to-one  
- web-to-app  
author: klaus-momo  
version: 3.0.0

# Use Case Document - MoMo Web Growth Strategy Generator

## Mục tiêu

Tạo một **Web Growth Strategy Document hoàn chỉnh** cho bất kỳ Use Case nào của MoMo - từ zero đến one.

Output đủ để:

1. Present cho stakeholders (Head of Growth, PO)
2. Làm playbook cho team thực thi hàng ngày
3. Làm baseline để đo lường và iterate
4. Replicate pattern sang Use Case khác

---
## MANDATORY - Pre-flight Check (KHÔNG ĐƯỢC BỎ QUA)

Trước khi generate document, hỏi user 6 câu sau. **Hỏi từng câu một, không hỏi cùng lúc.**

|#|Câu hỏi|Ghi chú|
|---|---|---|
|1|Use Case cụ thể là gì? (Cinema, Billpay, Credit, Insurance, OTA, eSIM, Telco)||
|2|Mục tiêu business? (New User Acquisition / MAU growth / Revenue / Market Entry)|Quyết định OKR|
|3|Maturity level? (Zero / Early / Growth)|Zero = chưa có web, Early = có page chưa optimize, Growth = đang scale|
|4|Timeline? (Q nào deliver? OKR cycle nào?)||
|5|Existing assets? (URL trên momo.vn? Data từ GSC/GA4?)|Phải scrape thật|
|6|KPI targets? (Traffic / New Users / CR)|Nếu không có → tự estimate từ market pool, ghi rõ [EST]|

**Rule**: Nếu thiếu câu trả lời → KHÔNG generate. Hỏi lại câu còn thiếu.

---

## Document Structure

```
Executive Summary (max 150 từ)
Part 1: Foundation (JTBD summary + Market)
Part 2: Strategy (OKR + Intent + Site Architecture + W2A)
Part 3: Build (PLG Utilities + Content Pipeline + GEO Checklist)
Part 4: Growth Loop (Measurement + Cross-sell + Experiments + Scaling)
Appendix (Keyword Universe + URL Inventory + Content Brief Templates)
```

**Mỗi phần tối đa 500 từ** - không fluff, không giải thích khái niệm.

---

## Part 1: Foundation

### 1.1 Use Case Overview (3-5 câu)

```markdown
**USE CASE:** [tên]
**CLUSTER:** [nhóm trong MoMo ecosystem]
**CELL TEAM:** [PO/Growth/Dev - hoặc [CẦN XÁC NHẬN]]
**BUSINESS MODEL:** [transaction fee / commission / lead gen]
**ECOSYSTEM POSITION:** [Discovery → Use Case → Transaction → Retention]
```

### 1.2 JTBD Analysis (Summary)

**ChỈ lấy từ output của skill `[[jtbd-analysis]]`.** Không tự phân tích.

Nếu chưa có → chạy `[[jtbd-analysis]]` trước, rồi import summary.

```markdown
**JOB STATEMENTS (2-3 cái):**
- "When [situation], I want to [motivation], so I can [outcome]."

**TOP 3 ANXIETIES** (cần xử lý trong content):
1. [Anxiety] → [cách xử lý]

**TOP 3 PUSH FORCES** (pain points để hook):
1. [Push force]
```

### 1.3 Market & Competitive Landscape

**BẮT BUỘC scrape SERP thật. Không được đoán.**

```markdown
**SEARCH DEMAND:**
- Total monthly volume: [X] [nguồn: Ahrefs/GSC]
- Trend: [Growing / Stable / Declining]

**TOP 3 COMPETITORS:**
| Domain | Positioning | Điểm mạnh |
|--------|-------------|-----------|
| [url] | [positioning] | [điểm mạnh] |

**SERP FEATURES:**
- AI Overview: [Có/Không] - [Brands được cite]
- Featured Snippet: [format thắng]
- PAA: [Top 3 questions]

**CONTENT GAP:**
- MoMo có mà competitor không: [...]
- Competitor có mà MoMo không: [...]
- Cả hai đều yếu: [...]
```

**Rule**: Mọi số liệu phải có nguồn. Không source → ghi `[CẦN VERIFY]`.

---

## Part 2: Strategy

### 2.1 OKR (Outcome-based)

**MANDATORY**: "Tăng traffic 50%" là output, không phải outcome.

```markdown
**O1: [outcome-based objective]**
- KR1: [Metric] từ [baseline] → [target] trong [timeline]
- KR2: [Metric] từ [baseline] → [target] trong [timeline]
```

**Nếu user không có KPI** → estimate:

```
Organic traffic potential = total volume × CTR (Top 3: ~20%)
New users = organic traffic × 7% (fintech W2A benchmark)
Ghi rõ [EST]
```

### 2.2 Search Intent Architecture

```markdown
**INTENT MAP:**
| Intent | Page type |
|--------|-----------|
| Informational | Blog |
| Commercial Investigation | Comparison/Review |
| Transactional | Transaction pages + Utilities |

**PRIORITY KEYWORDS (tối đa 10, có ICE):**
| Keyword | Volume | Intent | Impact | Confidence | Ease | ICE |
```

### 2.3 Site Architecture

```markdown
**SITEMAP (tối đa 10 URLs):**
momo.vn/[use-case]/           → Hub
momo.vn/[use-case]/[topic]/   → Spoke (2-3 cái)
momo.vn/blog/[topic]/         → Blog (2-3 cái)

**URL NAMING:**
- Transaction: momo.vn/[use-case]/[action]
- Blog: momo.vn/blog/[slug]
```

### 2.4 Web-to-App Conversion

```markdown
**TOUCHPOINTS (tối đa 3):**
| Touchpoint | Trigger | CTA |
|------------|---------|-----|
| Smart Banner | scroll 50% | "Mở MoMo để [job]" |
| Inline CTA | sau info section | "So sánh xong? Mua ngay" |
| Sticky Bar | always on mobile | persistent deeplink |

**DEEPLINK:** Onelink + UTM + fallback
```

---

## Part 3: Product & Content Build

### 3.1 PLG Utilities (nếu có)

```markdown
**UTILITY #1:** [tên]
- Job served: [job statement]
- Input → Logic → Output
- Priority: ICE [X]
```

### 3.2 Content Production Pipeline

```markdown
**CONTENT ANGLES (2-3 angles, mỗi angle 2-3 topics):**
**Angle 1:** [tên] - [intent]
- Topics: [topic 1], [topic 2]
- Differentiation: [1 câu]

**CALENDAR (4 tuần đầu):**
| Week | Piece | Type | Keyword | Angle |
```

### 3.3 GEO/AEO Checklist - **GATE. KHÔNG PUBLISH NẾU KHÔNG PASS.**

```markdown
**PRE-PUBLISH (bắt buộc):**
- [ ] 50 từ đầu trả lời trực tiếp câu hỏi
- [ ] H1 phản ánh đúng search intent
- [ ] Schema: primary type + FAQPage + BreadcrumbList
- [ ] FAQ section với Q&A tự nhiên
- [ ] Internal links: Hub ↔ Spokes
- [ ] CTA đúng vị trí (hero + in-content + sticky)
- [ ] Mobile OK

**POST-PUBLISH:**
- [ ] GSC: request indexing
- [ ] GTM/GA4: events firing
- [ ] Deeplink test: CTA → App opens
- [ ] Baseline logged
```

**Rule**: Thiếu bất kỳ item pre-publish nào → KHÔNG PUBLISH.

### 3.4 Technical SEO Hygiene

```markdown
**ROUTINE:**
- Core Web Vitals: weekly monitor
- Zero-traffic URLs: monthly audit
- Sitemap: auto-update

**ESCALATION (cần Dev):**
- [list specific items]
```

---

## Part 4: Growth Loop

### 4.1 Measurement Framework

```markdown
**NORTH STAR:** [New Users from Organic / Web-to-App Conversions]

**FUNNEL METRICS:**
| Stage | Metric | Tool |
|-------|--------|------|
| Impression | GSC Impressions | GSC |
| Click | GSC Clicks + CTR | GSC |
| Landing | Sessions | GA4 |
| Engage | CTA Click Rate | GA4 |
| Convert | Deeplink Fire Rate | GA4+AF |
| Activate | App Open Rate | Appsflyer |

**DASHBOARD:** Looker Studio (GSC + GA4 + Appsflyer)
```

### 4.2 Cross-sell

```markdown
**CROSS-LINK (2-3 connections):**
| From | To | Logic |
|------|-----|-------|
| [UC hiện tại] | [UC khác] | [lý do trong user journey] |
```

### 4.3 Growth Experiments (tối đa 3)

```markdown
**HYPOTHESIS #1:**
"Nếu [change X] trên [Y] thì [metric Z] tăng [target%] vì [reason]"
Success criteria: p < 0.05
```

### 4.4 Iteration Cycle

```markdown
**WEEKLY:** Content performance, fix tracking
**MONTHLY:** Content audit, utility review
**QUARTERLY:** OKR check, strategy review
```

### 4.5 Scaling Playbook

```markdown
**WHEN THRESHOLD REACHED:**
1. Document winning patterns
2. Extract reusable templates
3. Note UC-specific vs universal

**REPLICATION TO NEW UC:**
1. Swap JTBD
2. Swap keyword universe
3. Reuse component library
4. Run GEO checklist
```

Đúng. Tôi bổ sung Programmatic SEO vào `use-case-document`.

Chèn vào **Part 3** (sau 3.2 Content Pipeline hoặc trước 3.3 GEO Checklist) hoặc **Part 4** (sau 4.5 Scaling Playbook). Tôi chọn Part 4.5.5 vì programmatic là một cách scaling.

Thêm section mới:

```markdown
### 4.6 Programmatic SEO

**KHI NÀO DÙNG:**
- Use Case có dữ liệu có cấu trúc (structured data) theo nhiều biến số
- Có thể tạo hàng trăm/thousands trang từ template + data source
- Mỗi trang có search demand riêng (dù nhỏ) nhưng tổng thể large

**VÍ DỤ ĐIỂN HÌNH TẠI MOMO:**

| Use Case | Biến số | Số lượng trang tiềm năng |
|----------|---------|-------------------------|
| Cinema | Tỉnh/thành phố × cụm rạp × phim đang chiếu | 200-500 |
| Insurance | Loại xe (xe máy/ô tô) × hãng xe × dòng xe | 300-1000 |
| Billpay | Nhà cung cấp (điện/nước/internet) × khu vực | 100-300 |
| eSIM | Quốc gia × gói data × thời gian | 150-200 |
| OTA | Điểm đến × khách sạn × thời gian | 500-5000 |

**ĐIỀU KIỆN ÁP DỤNG:**
1. Data source ổn định (API hoặc static data có thể refresh)
2. Template page đã được validate (có conversion)
3. Schema có thể automated (mỗi page có schema riêng)
4. Internal linking có thể generated (từ category → city → specific)

**TECH STACK:**
```
Data source (API/CSV) → Generator script → Static HTML files (or SSG)
                              ↓
                        Sitemap index (chia nhỏ nếu >50k URLs)
                              ↓
                        Internal links tự động giữa các pages
```

**GEO REQUIREMENTS CHO PROGRAMMATIC:**
Mỗi page phải có đủ các elements để không bị coi là "thin content":

```
BẮT BUỘC:
- [ ] Unique H1 (không chỉ swap city name vào template)
- [ ] 200-300 từ unique content (giới thiệu + context)
- [ ] FAQ section (có thể generated từ common Q&A + specific variables)
- [ ] Schema: Product/Service + FAQPage + BreadcrumbList
- [ ] Internal links: lên Hub + sang pages liên quan (cùng category)

NÊN CÓ:
- [ ] User-generated content (reviews, comments) nếu có
- [ ] Real-time data (giá hiện tại, availability)
- [ ] So sánh với các pages khác trong cùng cluster
```

**PROGRAMMATIC CHECKLIST TRƯỚC KHI LAUNCH:**

```markdown
**DATA SOURCE:**
- [ ] Data có thể refresh định kỳ không? (nếu có, tần suất?)
- [ ] Data coverage có đủ để tạo số lượng pages đã cam kết?
- [ ] Fallback data khi API down?

**TEMPLATE:**
- [ ] Template đã được A/B test trên 1 page mẫu?
- [ ] Conversion rate của page mẫu ≥ benchmark?
- [ ] Mobile performance OK (LCP < 2.5s)?

**SCALE:**
- [ ] Tổng số pages dự kiến: [X]
- [ ] Crawl budget có đủ để index tất cả? (nếu >10k pages)
- [ ] Sitemap có được chunk đúng cách? (tối đa 50k URLs/sitemap)

**SEO:**
- [ ] Mỗi page có canonical trỏ về chính nó (tránh duplicate)
- [ ] Pagination có rel=prev/next nếu có list pages
- [ ] Noindex cho pages có content quá thấp (dưới 200 từ)
- [ ] Internal links có giới hạn số lượng trên 1 page (tránh thin navigation)
```

**MEASUREMENT:**

```markdown
**BULK METRICS (theo dõi theo cohort):**
- Total indexed pages / Total generated pages (tỷ lệ index)
- Total organic traffic từ programmatic pages
- Conversion rate trung bình (so với manual pages)
- Click per page trung bình (để phát hiện pages kém quality)

**ALERT:**
Khi phát hiện cluster pages có CTR thấp bất thường → audit template
Khi phát hiện tỷ lệ index < 50% → check crawl budget + internal linking
```

**WHEN NOT TO USE:**
- Data source không ổn định hoặc 1-time use
- Không đủ resource để maintain (refresh data, fix template bugs)
- Search demand cho mỗi page quá thấp (< 10 searches/month) và không có long tail aggregation
- Template chưa được validate (chưa có page mẫu convert)

**SCALING PATH:**
```
Phase 1: Manual pages cho top 10 cities/providers (validate template)
Phase 2: Programmatic cho top 50 (test crawl & index)
Phase 3: Scale to full data set (monitor quality metrics)
Phase 4: Auto-refresh data (daily/weekly)
```
---

## Appendix (bắt buộc)

```markdown
## A. Keyword Universe (tối đa 20 keywords)
| Keyword | Volume | Intent | Priority |
|---------|--------|--------|----------|

## B. URL Inventory
| URL | Type | Angle | Target keyword |
|-----|------|-------|----------------|

## C. Content Brief Template
**Title:** [H1]
**Target keyword:** [keyword]
**Intent:** [type]
**JTBD:** [job statement]
**GEO:** 50-word answer + FAQ + Schema
**Internal links:** Hub + Spokes
**CTA:** hero + in-content + sticky
```

---

## Output Format

```markdown
# WEB GROWTH STRATEGY: [USE CASE NAME]
Version: 1.0 | Date: [Date] | Status: Draft

## Executive Summary
[max 150 từ]

## Part 1: Foundation
[content]

## Part 2: Strategy
[content]

## Part 3: Product & Content Build
[content]

## Part 4: Growth Loop & Optimization
[content]

## Appendix
A. Keyword Universe
B. URL Inventory
C. Content Brief Template
```

---

## Rules & Constraints

1. **Hỏi 6 câu pre-flight trước** - không generate nếu thiếu
2. **Scrape SERP và momo.vn thật** - không lý thuyết
3. **Số liệu phải có nguồn** - không source → `[CẦN VERIFY]`
4. **OKR outcome-based** - output-based không được chấp nhận
5. **GEO checklist là GATE** - thiếu item = không publish
6. **Mỗi phần tối đa 500 từ** - cắt fluff
7. **Dùng "Use Case"** - không dùng "Vertical"
8. **Không giải thích khái niệm** - nếu user không biết, họ sẽ hỏi
9. **Không chào hỏi rườm rà** - đi thẳng vào vấn đề

---

## Integration

| Skill               | Khi nào                          |
| ------------------- | -------------------------------- |
| `jtbd-analysis`     | Part 1.2 - import summary        |
| `pyramid-principle` | Executive summary & presentation |
| `web-tracking`      | Tracking spec riêng              |

	**Workflow:** brainstorming → jtbd-analysis → use-case-document → pyramid-principle → web-tracking  



## Liên kết
- Skill này là một phần của hệ thống MoMo Web Growth
- Skill trước: [[jtbd-analysis]]
- Skill sau: [[pyramid-principl