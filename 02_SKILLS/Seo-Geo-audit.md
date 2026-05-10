# 🧪 Seo Geo Audit
_Seo-Geo-audit
role: Audit & Quality Control
version: 1.1.0
---

## 🧭 Điều phối
- Tổng thể: [[SKILL_REGISTRY]]
- Quy trình: [[Orchestrator_Engine_Step_2]]
- Công cụ hỗ trợ: [[critical-thinking]]

Use this skill khi cần audit toàn diện một website/page MoMo (hoặc competitor) trên 4 trục

Technical SEO, On-page SEO, GEO/AEO readiness, và Authority/Backlink. Trigger khi user nói

"audit page X", "check SEO/GEO của Use Case Y", "đánh giá tình trạng SEO", "GEO readiness check",

hoặc khi cần baseline trước khi build content/strategy mới. Output là audit report có

classification (Critical/Warning/Pass), root cause, và prioritized action list bám North Star

Organic Traffic + Web2App.
category: marketing-sales

tags:
- seo
- geo
- audit
- technical-seo
- aeo
- momo
- web2app
author: klaus-momo
version: 1.0.0

# SEO/GEO Audit Skill

  

## Scope

  

Skill này thực hiện audit cấu trúc 4 trục cho 1 URL/domain/Use Case. **KHÔNG** viết content, **KHÔNG** thiết kế strategy mới - chỉ chẩn đoán hiện trạng và đề xuất action prioritized.

  

**Input:**

- 1 URL cụ thể, hoặc danh sách URL, hoặc 1 Use Case (ví dụ: QLCT, Vay Nhanh)

- Optional: target keywords, competitor reference, business goal
  

**Output:**

- Audit report 4 trục với classification

- Root cause analysis cho mỗi finding Critical/Warning


## Non-negotiable Principles


1. **Zero-Hallucination**: Không bịa số liệu. Mọi finding phải có data source rõ ràng (Ahrefs/GSC/PageSpeed/manual check). Không có data → mark `[cần verify]`

2. **North Star tied**: Mỗi action đề xuất phải trace được tới 1 trong 2 mục tiêu lõi (Organic Traffic hoặc Web2App conversion). Nếu không trace được → drop action đó

3. **Critical Thinking**: Challenge assumption mặc định. Ví dụ: "thiếu schema = xấu" - hỏi lại: schema có tác động thật tới AI citation cho query này không, hay chỉ là best practice generic?

4. **Use Case context**: Audit luôn đặt trong context Use Case của MoMo (Cinema, Billpay, QLCT, Insurance...) - không audit chung chung kiểu "website tốt/xấu"

5. **JTBD lens**: Đánh giá content qua lens "page này có serve được job người dùng không" trước khi đánh giá technical

6. **Vietnamese pro, không em dash**


## 4 Audit Axes

### Axis 1: Technical SEO Foundation

Mục đích: đảm bảo crawler + AI bot có thể access và hiểu được page.
  
| Check | Tool | Pass criteria |

|---|---|---|

| HTTP status | curl/Ahrefs Site Audit | 200 (không 3xx chain, 4xx, 5xx) |

| Indexability | GSC URL Inspection | Indexed, không noindex, không blocked robots.txt |

| Canonical | View source | Self-canonical hoặc trỏ đúng version chính |

| Crawl depth | Screaming Frog/Ahrefs | ≤ 4 clicks từ homepage |

| Internal links | Ahrefs | ≥ 3 internal links trỏ vào |

| Sitemap inclusion | sitemap.xml | Có mặt, lastmod cập nhật |

| Core Web Vitals | PageSpeed/CrUX | LCP < 2.5s, INP < 200ms, CLS < 0.1 |

| Mobile-friendly | GSC Mobile Usability | Pass |

| HTTPS | Browser | Valid cert, không mixed content |

| robots.txt | /robots.txt | Không block path quan trọng, không block AI bots cần thiết (GPTBot, PerplexityBot, ClaudeBot tùy strategy) |

  

**Critical** nếu: noindex, 404/5xx, blocked, LCP > 4s

**Warning** nếu: crawl depth > 4, < 3 internal links, INP 200-500ms

  

### Axis 2: On-page SEO

  

Mục đích: page match search intent và keyword target.

  

| Check | Method | Pass criteria |

|---|---|---|

| Title tag | View source | 50-60 chars, chứa primary keyword, có brand MoMo cuối |

| Meta description | View source | 140-160 chars, có CTA, không duplicate |

| H1 | View source | 1 H1 duy nhất, match search intent |

| H-structure | View source | Logical hierarchy (H2 → H3), không skip level |

| Keyword usage | Manual + Ahrefs | Primary keyword trong title/H1/first 100 words/URL |

| Search Intent match | Manual SERP check | Page format phù hợp intent (transactional/informational/navigational) |

| Content depth | Word count + topical coverage | ≥ competitor median, cover các subtopic JTBD |

| Internal linking out | View source | Link tới ≥ 3 related pages, anchor text descriptive |

| Image alt | View source | Tất cả image quan trọng có alt mô tả |

| URL structure | URL bar | Ngắn, có keyword, không param thừa |

  

**Critical** nếu: thiếu H1, title duplicate, intent mismatch hoàn toàn

**Warning** nếu: title quá dài/ngắn, content depth < 50% competitor

  

### Axis 3: GEO/AEO Readiness

  

Mục đích: page được AI engines (Google AI Overview, ChatGPT, Perplexity, Claude) trích dẫn.

  

| Check | Method | Pass criteria |

|---|---|---|

| Answer-first structure | Manual | Câu trả lời trực tiếp trong 100 words đầu, không lead-in dài |

| Direct quote-ability | Manual | Có ít nhất 3 sentences ngắn (15-25 words) chứa fact + context, dễ trích nguyên văn |

| FAQ schema | View source | FAQPage schema cho Q&A blocks |

| Article/HowTo schema | View source | Schema phù hợp content type |

| Entity clarity | Manual | Brand/product/concept được name rõ ràng, không ambiguous |

| E-E-A-T signals | Manual | Có author byline, credentials, last updated date, sources |

| Information Gain | Manual + competitor compare | Có data/insight unique không tìm được ở competitor |

| Listicle/table format | View source | Có structured data dạng list/table cho comparison query |

| Citable stats | Manual | Số liệu có nguồn rõ, format dễ AI parse |

| llms.txt | /llms.txt | Có file (optional, signal forward) |

| AI bot accessibility | robots.txt | GPTBot/PerplexityBot/ClaudeBot không bị block (trừ khi strategy chống) |

  

**Critical** nếu: page không answer được question chính, không có entity clarity

**Warning** nếu: thiếu schema, không có author, không có updated date

  

### Axis 4: Authority & Backlink

  

Mục đích: domain/page có đủ trust signal để compete.

  

| Check | Tool | Pass criteria |

|---|---|---|

| Domain Rating (DR) | Ahrefs | ≥ ngưỡng competitor |

| URL Rating (UR) page | Ahrefs | > 0, có ít nhất 1 referring domain quality |

| Referring domains | Ahrefs | Diverse, không spike bất thường |

| Anchor text profile | Ahrefs | Natural, không over-optimize 1 anchor |

| Toxic backlinks | Ahrefs Site Explorer | Không có spike spam (negative SEO check) |

| Lost backlinks | Ahrefs | Track recent loss, root cause |

| Internal authority flow | Ahrefs | Page nhận internal link từ high-UR pages |

  

**Critical** nếu: backlink spike bất thường (negative SEO), toxic ratio cao, mất nhiều backlink quality gần đây

**Warning** nếu: anchor text over-optimized, internal link từ low-UR only

  

## Workflow

  

### Step 1: Scope & context gathering

- Xác nhận với user: URL/Use Case, mục tiêu audit (baseline mới hay troubleshoot vấn đề cụ thể), competitor reference

- Đọc Use Case context nếu có (link tới `03_Use-Cases/[name].md`)

- Identify primary keyword cluster + search intent

  

### Step 2: Data collection

- Trigger các tool calls cần thiết:

- Ahrefs MCP: domain rating, backlinks, organic keywords, site audit issues

- Web fetch: page content, view source, schema

- GSC (nếu có): indexation status, performance

- Document data sources cho mỗi finding

  

### Step 3: Audit theo 4 trục

- Chạy lần lượt Axis 1 → 4

- Mỗi check ghi: Pass / Warning / Critical + evidence + data source

- KHÔNG bỏ qua trục nào dù page có vẻ ổn ở trục khác

  

### Step 4: Root cause + prioritization

- Với mỗi Critical/Warning: phân tích root cause (không chỉ symptom)

- Map mỗi action vào ma trận Impact (High/Med/Low) × Effort (High/Med/Low)

- Prioritize: High Impact + Low Effort = P0, High Impact + High Effort = P1, ...
### Step 5: Output report

Format theo Pyramid Principle (xem `pyramid-principle` skill):

- Top: 1 câu kết luận về tình trạng tổng thể (Healthy/At-risk/Critical)

- 3-5 key findings đứng đầu

- Detailed audit table 4 trục

- Prioritized action list với owner gợi ý (Self/Dev/Content/PO)

- Risks + open questions

  

## Output Template

  

```markdown

# SEO/GEO Audit Report - [Page/Use Case name]

  

**Date**: YYYY-MM-DD

**Scope**: [URL hoặc Use Case]

**Auditor**: Klaus

**Data sources**: [Ahrefs date, GSC date, manual check date]

  

## TL;DR

[1 câu: tình trạng tổng thể + 1 câu: critical issue lớn nhất + 1 câu: P0 action]

  

## Top 5 Findings

1. **[Critical/Warning]** [Finding] → Impact: [Organic Traffic / Web2App / Both]

2. ...

  

## Audit Detail

  

### Axis 1: Technical SEO

| Check | Status | Evidence | Action |

|---|---|---|---|

| ... | 🔴/🟡/🟢 | [data] | [if not pass] |

  

### Axis 2: On-page SEO

[same format]

  

### Axis 3: GEO/AEO Readiness

[same format]

  

### Axis 4: Authority & Backlink

[same format]

  

## Root Cause Analysis

- [Finding] → root cause: [...] → systemic hay isolated?

  

## Prioritized Action List

  

| Priority | Action | Impact | Effort | North Star tie | Owner |

|---|---|---|---|---|---|

| P0 | ... | High | Low | Organic Traffic | Self |

| P1 | ... | High | High | Web2App | Dev |

| P2 | ... | Med | Low | Both | Content |

  

## Open Questions / [cần verify]

- ...

  

## Related

- Use Case: [[03_Use-Cases/...]]

- Skills feed-in: [[JTBD.md]] (nếu cần đào sâu intent)

- Skills feed-out: [[brd-momo|content-brief]] (nếu cần rewrite), [[use-case-document]] (nếu cần update strategy)

```

  

## Anti-patterns (đừng làm)

  

1. **Audit kiểu checklist máy móc** - chạy hết 40 checks rồi liệt kê pass/fail mà không phân tích root cause hay context Use Case

2. **Generic recommendation** - "thêm schema", "tăng tốc độ" mà không nói schema gì, target metric nào, impact ra sao

3. **Ignore business context** - flag warning cho những thứ technically đúng nhưng không impact Organic Traffic hay Web2App

4. **Bỏ Axis 3 (GEO/AEO)** - đây là North Star 2026, không được skip dù Axis 1-2 còn nhiều việc

5. **Không challenge data** - Ahrefs nói DR 50, không hỏi DR đó relative tới competitor cụ thể nào trong Use Case này

6. **Action không có owner** - mọi action phải gợi ý owner để actionable

7. **Quên Web2App layer** - audit xong content nhưng không check Onelink/CTA app dẫn về App Store

  

## Calibration với MoMo context

  

- **YMYL caution**: MoMo là fintech, mọi page financial advice phải có author + credentials + sources, không chỉ là nice-to-have

- **Use Case naming**: Dùng "Use Case" không "vertical" trong report

- **Language**: Audit report viết Tiếng Việt chuyên nghiệp, technical term giữ nguyên Tiếng Anh

- **Brand**: MoMo pink #d82d8b / #A50064, primary domain momo.vn

- **AI bot policy**: Check với strategy hiện tại của team về việc allow/block GPTBot, PerplexityBot, ClaudeBot - không assume default

- **Negative SEO awareness**: Luôn check Axis 4 với extra attention vì momo.vn từng có backlink anomaly

- **Web2App track**: Mọi audit page cần check có Onelink (onelink.momo.vn hoặc momoapp.onelink.vn) đặt đúng vị trí không

  

## Inputs / Outputs trong workflow chain

  

**Inputs from:**

- [[jtbd-analysis]] (optional - nếu cần hiểu sâu user job trước khi đánh giá content)

  

**Outputs to:**

- [[use-case-document]] (nếu finding impact strategy level)

- Project notes (nếu là one-off audit)

  

## Frameworks áp dụng

  

- [[jtbd-analysis]] - đánh giá content match job

- [[First-Principles]] - challenge "best practice" không có evidence

- [[pyramid-principle]] - structure output rep