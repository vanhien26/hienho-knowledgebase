name: jtbd-analysis
description: >
Phân tích Jobs-to-be-Done (JTBD) để kick-off bất kỳ dự án web nào cho MoMo.vn (Fintech & Financial

Assistant). Dùng khi cần hiểu động lực thực sự đằng sau hành vi người dùng trước khi lên brief,

thiết kế page, hoặc plan content. Trigger ngay khi user nhắc đến: JTBD, kick-off dự án mới,

phân tích vertical, user insight, search intent mapping, schema strategy, UX SEO, conversion design,

pain point, switch triggers, churn insight, SGE/AI Overview signals, content opportunity,

hoặc bất kỳ lúc nào cần "hiểu user trước khi làm". LUÔN scrape momo.vn và SERP thực tế trước khi

phân tích — không chấp nhận phân tích thuần lý thuyết. Nếu user cung cấp URL cụ thể, hỏi ngược

lại bằng tư duy Critical Thinking trước khi tiến hành. Cũng trigger khi cần: contextual schema

markup, UX SEO conversion wireframe, search intent clustering, SGE gap analysis.

category: strategy-research

tags:

- jtbd

- user-research

- growth

- plg

- content-strategy

- momo

- fintech

- schema

- ux-seo

- search-intent

- sge

- serp-scraping

author: klaus-momo

version: 2.0.0

  

# JTBD Analysis — MoMo Web Growth Edition v2.0

  

## Mục tiêu của Skill này

  

Biến "người dùng muốn gì" thành "tại sao người dùng hire/fire một giải pháp" — với output dùng trực tiếp để:

  

1. Brief content writer / AI content pipeline

2. Thiết kế Transaction Page copy, layout, và CTA

3. Justify prioritization với PO/Growth Cell

4. Feed vào Growth Experiments (A/B tests, landing page optimization)

5. Xây dựng Contextual Schema Markup theo từng Job

6. Thiết kế UX SEO Conversion Flow (wireframe-level)

7. Xây dựng topical authority map cho Hub & Spoke

  

Skill này **không phải user research tool thuần túy**. Nó là **strategic translation layer** giữa user insight và execution — kết hợp live data từ momo.vn, SERP, và SGE signals.

  

---

  

## MANDATORY: Critical Thinking Checkpoint (Chạy TRƯỚC mọi phase)

  

Nếu user cung cấp URL hoặc vertical cụ thể, thực hiện ngay Step 0A và 0B trước khi tiếp tục.

  

### Step 0A — Scrape & Audit momo.vn

  

Fetch URL user cung cấp (hoặc URL liên quan nhất trên momo.vn):

  

```

1. Fetch URL → đọc: H1, meta title, copy chính, CTA, schema hiện có

2. Quan sát:

- Page đang target keyword/intent gì thực sự?

- Conversion path hiện tại ra sao? Friction ở đâu?

- Schema markup đang dùng type gì? Hay chưa có?

- Content format: informational hay transactional hay hybrid?

- Internal linking: Hub & Spoke structure có chưa?

3. Flag ngay những điểm MISALIGNED với JTBD hypothesis

```

  

### Step 0B — Critical Thinking Interrogation

  

Sau khi đọc page, hỏi ngược lại user (chọn câu phù hợp, không hỏi hết một lúc):

  

```

"Page đang target [X intent], nhưng SERP top 3 đang serve [Y intent].

Đây là content gap hay misalignment chiến lược? Cần clarify trước."

"URL này hiện đang ở [stage] theo copy, nhưng keyword target có intent khác.

Có cần reposition không trước khi đi vào JTBD?"

"MoMo đang có [feature X] nhưng page không đề cập.

Gap về content hay gap về product? Cần confirm với PO không?"

"Vertical này có YMYL sensitivity không? E-E-A-T signals hiện tại

đủ mạnh chưa — Author, citation, trust signal ở đâu?"

```

  

**Rule**: Không tiếp tục Phase 1 cho đến khi có câu trả lời đủ để làm việc.

  

---

  

## Phase 1: Input Collection

  

### 1.1 Mandatory Inputs

  

|Input|Mô tả|Lấy từ đâu|

|---|---|---|

|**Vertical / Topic**|Tên sản phẩm hoặc chủ đề cần phân tích|User cung cấp|

|**Analysis Goal**|Output dùng để làm gì?|User cung cấp|

|**Target Segment**|Người dùng nào?|User cung cấp hoặc suy luận từ GSC|

|**URL đang / sẽ triển khai**|momo.vn URL cụ thể|User cung cấp → Agent phải fetch|

  

### 1.2 Optional Inputs (hỏi nếu thiếu)

  

|Input|Default nếu thiếu|

|---|---|

|GSC queries top 50|Agent crawl SERP + suy luận|

|GA4 event data|Agent suy luận từ funnel stage|

|Competitor URLs|Agent tìm top 3 từ SERP|

|Funnel stage focus|Agent cover toàn bộ funnel|

  

---

  

## Phase 2: JTBD Decomposition

  

### 2.1 The Job Statement

  

Viết Job Statement theo format Ulwick/Klement:

  

```

"When [situation / trigger moment],

I want to [motivation / functional job],

So I can [desired outcome — emotional or social]."

```

  

Dùng placeholder generic — không hardcode ví dụ cho một vertical cụ thể. Một vertical có thể có **2-4 Job Statements** (các segment khác nhau). Label `[HYPOTHESIS]` nếu chưa có data validate.

  

### 2.2 Four Job Dimensions

  

```

FUNCTIONAL JOB: Họ đang cố làm GÌ?

EMOTIONAL JOB: Họ muốn CẢM THẤY gì?

SOCIAL JOB: Người khác sẽ NGHĨ GÌ về họ?

CONSUMPTION JOB: Họ muốn QUÁ TRÌNH diễn ra như thế nào?

```

  

### 2.3 Switch Triggers (Push/Pull Forces)

  

```

PUSH → Điều gì khiến họ không hài lòng với giải pháp cũ?

PULL → Điều gì hấp dẫn họ về MoMo?

ANXIETIES → Điều gì khiến họ DO DỰ không chuyển sang?

HABITS → Thói quen nào giữ họ ở giải pháp cũ?

```

  

Content Rule: Mỗi ANXIETY = objection cần xử lý trong content. Mỗi PUSH = pain point cần nhắc đầu bài.

  

### 2.4 Desired Outcomes (ODI Framework)

  

List **5-10 outcomes** theo format: `[Direction] + [Metric] + [Object] + [Context]`

  

---

  

## Phase 3: Search Intent Scraping & Clustering

  

### 3.1 Intent Scraping Protocol

  

Với mỗi Job Statement, formulate **3-5 likely search queries** → fetch SERP:

  

```

For each query:

1. web_search → observe top 10 results

2. Identify: loại kết quả rank? (Blog, TX page, Forum, YouTube, SGE box)

3. Record: Top 3 URLs + page type + content format

4. Note: Featured snippet, People Also Ask, SGE/AI Overview nếu có

```

  

### 3.2 Intent Clustering Matrix

  

Cluster queries theo Job Statement và Intent Type:

  

|Cluster|Query đại diện|Intent Type|SERP Format thắng|Mapped Job|MoMo Coverage|

|---|---|---|---|---|---|

|[A]|[...]|Informational|Blog dài|Job #1|Missing/Weak/Strong|

|[B]|[...]|Transactional|TX page + price|Job #2|Missing/Weak/Strong|

|[C]|[...]|Investigational|Comparison|Job #3|Missing/Weak/Strong|

  

### 3.3 SGE / AI Overview Gap Analysis

  

```

1. Query ChatGPT / Perplexity với câu hỏi tương ứng Job Statement

2. Ghi nhận:

- Ai được cite? → brand đang win Job này trong AI search

- Format nào được cite? (FAQ, list, comparison, definition)

- MoMo có được cite không?

3. Map gap → Content action cần làm để được AI Overview cite

```

  

**SGE Gap Output per Job:**

  

```

Job: [Statement]

AI Query tested: "[query]"

Brands cited: [list]

MoMo cited: Yes / No

Winning format: [format]

GEO fix needed: [specific action]

```

  

---

  

## Phase 4: MoMo Opportunity Mapping

  

### 4.1 JTBD ↔ MoMo Product Fit

  

|Functional Job|Mức độ giải quyết|Tính năng MoMo liên quan|Gap còn lại|

|---|---|---|---|

|[Job 1]|High/Medium/Low|[Feature]|[VERIFY WITH PO]|

  

### 4.2 JTBD → Content Type Mapping

  

|Job Statement|Funnel Stage|Content Type|URL Structure|

|---|---|---|---|

|[Job 1]|Awareness|Blog informational|momo.vn/blog/[topic]|

|[Job 2]|Consideration|Blog + Comparison|momo.vn/blog/[so-sanh]|

|[Job 3]|Decision|Transaction Page|momo.vn/[vertical]/[action]|

  

### 4.3 Priority Matrix

  

```

HIGH (Làm ngay): Search demand cao + MoMo fit tốt + Content gap rõ

MEDIUM (Q tới): Search demand cao nhưng cần cải thiện product/content

LOW (Backlog): Search demand thấp hoặc MoMo không có lợi thế

```

  

---

  

## Phase 5: Contextual Schema Markup Design

  

### 5.1 JTBD → Schema Type Matrix

  

|Job Type|Funnel Stage|Schema Recommended|Rationale|

|---|---|---|---|

|Informational / Awareness|Top|FAQPage, Article, HowTo|AI Overview eligibility|

|Comparison / Research|Mid|ItemList, Table, Review|SERP rich snippets|

|Transactional / Decision|Bottom|Product, Offer, FinancialProduct|Trust + conversion|

|Process / Step-by-step|Mid|HowTo với steps|Featured Snippet|

  

### 5.2 Schema Blueprint Format

  

```json

{

"page_url": "momo.vn/[vertical]/[slug]",

"primary_job": "[Job Statement summary]",

"schema_stack": [

{

"type": "[Primary Schema]",

"rationale": "[Tại sao match Job này]",

"critical_fields": ["field1", "field2"],

"momo_specific": "[Map field với MoMo data thực tế]"

},

{

"type": "FAQPage",

"rationale": "Anxiety handling → FAQ schema → AI Overview eligibility",

"questions": ["[FAQ từ Anxiety #1]", "[FAQ từ Anxiety #2]"]

}

],

"schema_gaps_vs_current": "[So với schema hiện có từ Step 0A]"

}

```

  

### 5.3 Schema Rules cho MoMo Fintech

  

```

YMYL Verticals (Insurance, Credit, Loans):

→ Mandatory: Organization + FinancialProduct + FAQPage

→ E-E-A-T: Author schema với credentials

Transaction Pages:

→ Mandatory: Product + Offer + BreadcrumbList

→ Optional: AggregateRating nếu có review data

Blog / Informational:

→ Mandatory: Article + BreadcrumbList + FAQPage

→ Optional: HowTo nếu có step-by-step

Comparison Pages:

→ Mandatory: ItemList hoặc Table markup

```

  

---

  

## Phase 6: UX SEO Conversion Design

  

### 6.1 Page Layout Blueprint (Theo JTBD)

  

```

PAGE LAYOUT: [Blog / Transaction / Hub]

Primary Job: [Job Statement]

Conversion Goal: [App install / Form submit / CTA click]

ABOVE THE FOLD:

H1: [Phản ánh Functional Job — không nhồi nhét keyword]

Sub: [Address top Anxiety]

CTA: [Action verb + Outcome — e.g. "Đăng ký ngay — 3 phút là xong"]

Trust: [User count / Partner logos / Rating]

SECTION 1 — PAIN AGITATION:

Hook: [Nhắc Pain = Push Force]

Bridge: [Giải pháp MoMo = Pull Force]

SECTION 2 — SOLUTION SHOWCASE:

Content: [Functional Job satisfaction]

Format: [HowTo step-by-step / Feature table / Comparison]

Schema: [HowTo / ItemList]

SECTION 3 — TRUST & ANXIETY RESOLUTION:

Content: [Address top 2-3 Anxieties với proof points]

Format: [FAQ accordion → FAQPage schema]

Proof: [Certification / Data / Testimonial / Guarantee]

SECTION 4 — CONVERSION BLOCK:

CTA: [Contextual — match Consumption Job]

Micro-copy: [Reduce friction]

Deep link: [app://momo → Web-to-App trigger]

FOOTER:

Related: [Hub & Spoke links — same Job cluster]

Schema: [BreadcrumbList]

```

  

### 6.2 CTA Design Matrix

  

|Job Type|CTA Direction|Micro-copy Direction|

|---|---|---|

|Speed / Urgency|"Làm ngay trong X phút"|"Không cần chờ, không cần giấy tờ"|

|Comparison / Research|"Xem và so sánh miễn phí"|"Không cam kết, xem thoải mái"|

|Trust / Anxiety|"Tìm hiểu thêm → rồi quyết định"|"[X triệu] người tin tưởng"|

|Social Proof|"Xem đánh giá thực tế"|"[N] người thực hiện tuần này"|

  

### 6.3 Web-to-App Conversion Touchpoints

  

```

AWARENESS: Smart Banner sau 10s hoặc 50% scroll

Copy: "Mở MoMo để [complete the job]"

CONSIDERATION: Contextual CTA sau comparison section

Copy: "So sánh xong? Mua ngay trên app — nhanh hơn"

DECISION: Sticky CTA bar — luôn hiển thị khi scroll

Deep link → mở thẳng flow trong app

Fallback: App store redirect nếu chưa cài

```

  

---

  

## Phase 7: Output Format (Full JTBD Map)

  

```markdown

# JTBD MAP: [Vertical Name]

Date: [Date] | Version: 1.0

Analysis Goal: [Description]

URL Analyzed: [momo.vn URL — đã scrape Step 0A]

Critical Thinking Flags: [Issues phát hiện từ Step 0B]

## SEGMENT OVERVIEW

| Segment | Job Statement | Priority |

|---------|--------------|----------|

| [Seg A] | When... I want... so I can... | High |

## DETAILED JTBD ANALYSIS

[Per segment: Job Statement + 4 Dimensions + Switch Triggers + ODI + MoMo Fit]

## SEARCH INTENT CLUSTER MAP

[Cluster table + SGE Gap per Job]

## SCHEMA BLUEPRINT

[Schema stack per page]

## UX SEO CONVERSION BLUEPRINT

[Layout + CTA matrix + Web-to-App touchpoints]

## CONTENT OPPORTUNITY MAP

| # | Job | Funnel | Type | URL | Priority | Schema |

|---|-----|--------|------|-----|----------|--------|

## ANXIETIES & OBJECTION HANDLING

| Anxiety | Root cause | Content fix | Proof | Schema element |

|---------|------------|-------------|-------|----------------|

## NEXT ACTIONS

1. Immediate: Feed vào momo-seo-content-brief

2. Sprint: Implement Schema blueprint — verify với Dev

3. Next sprint: A/B test CTA theo JTBD matrix

4. Quarter: Validate [HYPOTHESIS] với user interview / GSC

```

  

---

  

## Rules & Constraints

  

1. **Luôn scrape momo.vn trước khi phân tích**. Không analysis lý thuyết khi có URL cụ thể.

2. **Critical Thinking trước khi execute**. Misaligned URL/strategy → hỏi ngược lại trước.

3. **JTBD phải dựa trên evidence**. Hypothesis được, nhưng phải label `[HYPOTHESIS]`.

4. **Phân biệt User Job vs. MoMo Business Job**. Focus User Job — nhưng map về business outcome.

5. **Một page = một primary Job**. Nhiều Jobs cho một URL → signal tách page. Flag PO.

6. **Schema phải contextual**. Mỗi field map về JTBD dimension cụ thể. Không dùng generic schema.

7. **UX layout follow JTBD order**: Above fold = Functional Job → Mid = Anxiety resolution → CTA = Consumption Job.

8. **Anxieties luôn phải có counter-evidence**. Không có proof → `[VERIFY WITH PO/BUSINESS]`.

9. **Không hardcode ví dụ cho một vertical cụ thể** trong hướng dẫn. Dùng placeholder để tránh bias.

  

---

  

## Khi nào KHÔNG dùng Skill này

  

- Đã có JTBD map → skip sang `momo-seo-content-brief`

- Cần keyword research thuần túy → làm trước, mang cluster vào đây validate

- Cần viết bài → `content-aeo`

  

---

  

## Integration với Skills khác

  

| Skill | Khi nào chain | Flow |

| ------------------------ | -------------------------- | -------------------------------- |

| `momo-seo-content-brief` | Sau khi JTBD Map xong | JTBD Map → feed Phase 2 brief |

| `content-aeo` | Sau khi brief approve | JTBD → Brief → Full content |

| `web-growth-analysis` | Validate traffic potential | JTBD Opportunity → Growth sizing |