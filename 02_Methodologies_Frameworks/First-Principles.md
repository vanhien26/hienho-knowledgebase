
## Liên kết
- Skill này là một phần của hệ thống MoMo Web Growth
- Xem tổng thể: [[SKILL]]
- Workflow: [[SKILL#Workflow Chuẩn cho 1 Use Case Mới]]
- Skill trước: [[brainstorming]],
- Skill sau: [[jtbd-analysis]], [[use-case-document]]

---
name: first-principles
description: >
  Phân tích vấn đề từ gốc rễ bằng First-Principles Thinking, loại bỏ assumption mặc định
  và analogy không được kiểm chứng. Dùng khi: problem đã tồn tại lâu nhưng chưa giải quyết
  được, best practice không mang lại kết quả, team đang "chạy theo đối thủ" mà không rõ lý do,
  hoặc cần đặt lại vấn đề từ đầu trước khi giải pháp cũ tiếp tục thất bại. Trigger khi user
  nói: "tại sao chúng ta đang làm cái này?", "đã thử hết cách rồi", "best practice là X nhưng
  không hiệu quả", "competitor làm Y nên mình cũng làm", "hãy phân tích từ gốc", "first principles",
  "challenge assumption", "đặt lại vấn đề". Output là phân tích tầng gốc rễ và hướng giải quyết
  mới không dựa trên copycat.
category: strategy-research
tags:
  - first-principles
  - critical-thinking
  - strategy
  - problem-solving
  - momo
author: klaus-momo
version: 1.0.0
---

# First-Principles Thinking — Problem Deconstruction Skill

Based on the reasoning method used by Aristotle, Elon Musk, and other systematic problem solvers.

---

## Core Philosophy

> "I think it's important to reason from first principles rather than by analogy. The normal way we conduct our lives is we reason by analogy — we are doing this because it's like something else that was done, or it is like what other people are doing. With first principles, you boil things down to the most fundamental truths and say, 'What are we sure is true?' ... and then reason up from there."
> — Elon Musk

**First-principles thinking** = breaking down a problem into its fundamental, undeniable truths, then rebuilding solutions from the ground up.

**Analogy thinking** = copying patterns because "that's how it's always been done" or "that's what competitors do."

Trong bối cảnh MoMo Web Growth: Ngừng copy best practice SEO generic, ngừng chạy theo competitor vì họ làm vậy. Hỏi: "Điều gì là truth tuyệt đối trong context của MoMo và user của chúng ta?"

---

## Khi nào DÙNG First-Principles

| Dấu hiệu nhận biết | Áp dụng khi |
|---|---|
| **Problem đã tồn tại lâu, nhiều giải pháp thử nhưng không giải quyết được** | "Chúng ta đã thử A/B/C, vẫn không cải thiện Web-to-App CR" |
| **Team đang copy competitor mà không rõ lý do** | "Cinema page của VPBank có feature X, mình cũng làm" |
| **Best practice được nhắc đi nhắc lại nhưng không có evidence** | "Schema giúp tăng CTR" — có thật không? |
| **Assumption cũ đang được coi là truth** | "Người dùng không muốn click CTA ở đầu page" — ai nói? |
| **Cần thiết kế giải pháp cho vấn đề mới chưa có precedent** | Use Case mới chưa ai làm, không có benchmark |
| **Performance plateau — growth stuck** | Traffic/Conversion không tăng dù đã tối ưu mọi thứ |
| **Mâu thuẫn nội bộ — stakeholder disagreement** | "SEO muốn A, Product muốn B, UX muốn C" → quay về truth |

**Rule of thumb:** Nếu câu trả lời cho "tại sao chúng ta làm việc này?" là "vì ai đó cũng làm" hoặc "vì đây là best practice" — đó là signal để chạy first-principles.

---

## Khi nào KHÔNG DÙNG First-Principles

| Tình huống | Lý do |
|---|---|
| **Vấn đề đã có solution rõ ràng, low-risk** | Không cần deconstruct "thêm canonical tag" — đã được chứng minh |
| **Cần execution nhanh, không có thời gian** | First-principles tốn thời gian, không dùng cho hotfix |
| **User đã xác nhận assumption đúng** | Đã có data từ GSC/GA4/User interview → dùng data đó, không cần deconstruct |
| **Vấn đề là do lỗi kỹ thuật đơn thuần** | 404 page, broken links — fix thôi, không cần triết lý |

**First-principles là công cụ chiến lược, không phải operational default.**

---

## Liên kết với Skills khác

| Skill                     | Mối quan hệ                                              | Flow                                                                      |
| ------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------- |
| **[[brainstorming]]**     | First-principles cung cấp "truth base" cho brainstorming | First-principles → Truth statements → Brainstorm solutions từ truths đó   |
| **[[jtbd-analysis]]**     | JTBD là một dạng first-principles cho user behavior      | JTBD hỏi "user job là gì" (truth) trước khi hỏi "content gì" (solution)   |
| **[[use-case-document]]** | First-principles dùng trong Phase 1 Foundation           | Trước khi viết strategy, hỏi: "Use Case này dựa trên truth gì về user?"   |
| **[[pyramid-principle]]** | First-principles cung cấp logic cho governing idea       | Governing idea phải dựa trên truth, không phải assumption                 |

---

## The First-Principles Process (5 Steps)

### Step 1: Identify & List Current Assumptions

Viết ra tất cả assumptions đang được coi là "truth" trong vấn đề đang xử lý.

**Cách làm:**
- Hỏi: "Chúng ta đang giả định điều gì là đúng?"
- Hỏi: "Chúng ta đang làm việc này vì lý do gì?"
- Không đánh giá đúng/sai ở bước này — chỉ liệt kê.

**Output format:**
```markdown
## Current Assumptions (cần kiểm tra)
1. [Assumption 1] — VD: "Người dùng không muốn click CTA ở đầu trang vì chưa đủ trust"
2. [Assumption 2] — VD: "FAQ schema giúp tăng AI Overview citation"
3. [Assumption 3] — VD: "Content càng dài càng tốt cho SEO"
4. [Assumption 4] — VD: "Phải có smart banner thì mới convert web-to-app"
```

### Step 2: Break Down to Fundamental Truths

Hỏi liên tục "tại sao" và "có thật không" cho đến khi chạm đến điều không thể bác bỏ.

**Phương pháp Socratic questioning:**
- "Làm sao chúng ta biết điều này là đúng?"
- "Điều này có đúng trong mọi trường hợp không?"
- "Nếu điều ngược lại đúng thì sao?"
- "Điều này dựa trên bằng chứng hay giả định?"

**Fundamental truth criteria:**
- Không thể bác bỏ bằng logic hoặc dữ liệu
- Đúng trong mọi context của vấn đề
- Có thể chứng minh bằng thực tế (hoặc ít nhất là verified hypothesis)

**Output format:**
```markdown
## Fundamental Truths (verified hoặc không thể bác bỏ)
1. [Truth 1] — VD: "User đến trang web với một job cần hoàn thành. Nếu job không được serve, họ rời đi."
2. [Truth 2] — VD: "AI Overview citations dựa trên khả năng page trả lời câu hỏi một cách trực tiếp và đáng tin cậy."
3. [Truth 3] — VD: "Web-to-App conversion xảy ra khi user thấy value của việc mở app > friction của việc mở app."
4. [Truth 4] — VD: "Google xếp hạng page dựa trên khả năng đáp ứng search intent, không phải số lượng schema hay từ khóa."
```

**Cách phân biệt Truth vs Assumption:**

| Nếu câu trả lời là... | Thì đó là... |
|---|---|
| "Đã được chứng minh bằng data của MoMo" | Truth (có evidence) |
| "Được Google/Search Central xác nhận" | Truth (external authority) |
| "Logic không thể bác bỏ" | Truth (first-principles) |
| "Ai cũng biết thế" | Assumption — cần kiểm tra |
| "Best practice trong SEO" | Assumption — cần kiểm tra |
| "Competitor làm thế" | Assumption — cần kiểm tra |
| "Team SEO cũ nói thế" | Assumption — cần kiểm tra |

### Step 3: Identify Contradictions & Gaps

So sánh assumptions (Step 1) với fundamental truths (Step 2). Tìm chỗ nào assumption bị truth bác bỏ.

**Output format:**
```markdown
## Contradictions & Gaps

| Assumption | Fundamental Truth | Contradiction? | Implication |
|------------|------------------|----------------|-------------|
| "User không click CTA ở đầu page" | "User muốn hoàn thành job nhanh nhất có thể" | YES — nếu CTA ở đầu giúp hoàn thành job nhanh, user sẽ click | Cần A/B test CTA sớm, không assume auto-bad |
| "Schema = AI citation" | "AI citation dựa trên answer quality + trust signals" | PARTIAL — schema helps parsing nhưng không phải cause | Schema là điều kiện cần, không đủ. Content quality mới là truth |
| "Content dài = tốt" | "Google xếp hạng dựa trên intent match, không phải word count" | YES — nếu content dài nhưng không answer intent, vẫn fail | Focus on coverage, not length |

**Critical signal:** Nếu assumption và truth mâu thuẫn hoàn toàn → assumption sai, phải loại bỏ khỏi strategy.

### Step 4: Rebuild Solutions from Truths

Dựa trên fundamental truths (Step 2) và gaps (Step 3), thiết kế giải pháp mới KHÔNG dựa trên assumptions cũ.

**Nguyên tắc rebuild:**
- Mỗi solution phải trace được về ít nhất 1 fundamental truth
- Không đưa solution vào chỉ vì "nó là best practice"
- Nếu solution dựa trên assumption chưa verify → đánh dấu `[HYPOTHESIS - cần test]`

**Output format:**
```markdown
## Rebuilt Solutions

### Solution 1: [Tên]
**Based on truth(s):** [Truth #1], [Truth #2]
**What we stop doing (assumptions cũ):** [Mô tả]
**What we start doing:** [Mô tả]
**Hypothesis:** [Nếu X thì Y vì Z]
**Test method:** [Cách verify]
**Priority:** P0/P1/P2

### Solution 2: [Tên]
...
```

**Ví dụ cụ thể — Web-to-App Conversion:**

| Assumption cũ | Truth | Solution mới |
|---|---|---|
| "Phải có smart banner mới convert" | "Conversion xảy ra khi value > friction" | Thử contextual CTA ngay sau value proposition, không chờ scroll đến banner |
| "User không click CTA ở đầu" | "User muốn hoàn thành job nhanh" | A/B test CTA "Làm ngay" ở hero section với 1 variant |
| "Popup gây khó chịu, tránh dùng" | "Timing và relevance mới là vấn đề" | Test exit-intent popup chỉ khi user có scroll + time > 30s |

### Step 5: Test & Validate

First-principles không kết thúc ở lý thuyết. Mọi rebuilt solution phải được test.

**Testing hierarchy:**
1. **If truth đã có data từ MoMo** → implement trực tiếp, không cần test lại truth
2. **If truth từ external (Google, research)** → implement nhưng monitor để verify trong context MoMo
3. **If rebuilt solution dựa trên hypothesis** → phải A/B test hoặc validate bằng data trước khi scale

**Output format:**
```markdown
## Validation Plan

| Solution | Validation method | Success criteria | Timeline | Owner |
|----------|------------------|------------------|----------|-------|
| Solution 1 | A/B test (2 variants, 50/50) | CR tăng 15% với p < 0.05 | 2 weeks | Growth |
| Solution 2 | GSC analysis pre/post | CTR tăng 10% | 4 weeks | SEO |
| Solution 3 | User interview (n=10) | 7/10 confirm hypothesis | 1 week | UX |
```

---

## First-Principles in Action: MoMo Examples

### Example 1: "Schema Markup Strategy"

**Problem:** Team đang debate có nên implement schema trên mọi page không. "Best practice là phải có schema."

**Step 1 — Assumptions:**
1. Schema giúp tăng CTR
2. Schema giúp được AI Overview cite
3. Thiếu schema = Google đánh giá thấp hơn

**Step 2 — Truths:**
1. Google sử dụng schema để hiểu content, không phải để xếp hạng trực tiếp (Google Search Central đã confirm)
2. AI Overview citations dựa trên content quality + trust signals + answer-first format
3. Schema giúp AI parse structured data (fact, date, price) nhưng không guarantee citation

**Step 3 — Contradictions:**
- Assumption #2 bị bác bỏ một phần: schema helps nhưng không phải cause
- Assumption #3 sai hoàn toàn: Google không "đánh giá thấp" vì thiếu schema

**Step 4 — Rebuilt solution:**
- **Stop:** Implement schema vì "phải có"
- **Start:** Implement schema CHỈ KHI nó serve một job cụ thể (FAQ schema cho anxiety resolution, HowTo cho step-by-step, Product cho transaction page)
- **Truth-based:** Schema là công cụ, không phải mục tiêu

**Step 5 — Test:**
- Compare pages có schema vs không schema (cùng intent, cùng content quality) → có差異 gì trong AI Overview citation rate?

### Example 2: "Content Length for SEO"

**Problem:** Content team đang được yêu cầu viết bài 2000+ từ vì "content dài rank tốt hơn."

**Step 1 — Assumptions:**
1. Content dài = rank cao hơn
2. Competitor viết dài → mình phải dài hơn
3. User muốn đọc content dài

**Step 2 — Truths:**
1. Google rank dựa trên search intent match + content coverage, không phải word count
2. User có consumption job: "Tôi muốn tìm câu trả lời nhanh" hoặc "Tôi muốn deep dive" — tùy intent
3. Bounce rate và time on page phản ánh intent match

**Step 3 — Contradictions:**
- Assumption #1 sai: correlation không phải causation. Content dài thường đi kèm coverage tốt hơn, nhưng coverage mới là truth

**Step 4 — Rebuilt solution:**
- **Stop:** Set KPI theo word count
- **Start:** Set KPI theo "does this page answer the primary question in first 100 words?" + "does it cover all subtopics user needs?"
- **Truth-based:** Coverage > Length

**Step 5 — Test:**
- A/B test: short but comprehensive (800 words) vs long (2000 words) for same intent → compare rank + conversion

---

## Output Format (Full First-Principles Analysis)

```markdown
# FIRST-PRINCIPLES ANALYSIS: [Problem/Vertical/Decision]
Date: [Date]
Analyst: Klaus
Trigger: [User nói gì để kích hoạt skill này]

## PROBLEM STATEMENT
[1-2 câu mô tả vấn đề đang gặp phải]

## STEP 1: CURRENT ASSUMPTIONS
| # | Assumption | Source (ai nói/best practice/competitor) |
|---|-----------|------------------------------------------|
| 1 | ... | ... |
| 2 | ... | ... |

## STEP 2: FUNDAMENTAL TRUTHS
| # | Truth | Evidence (data/logic/external source) |
|---|-------|---------------------------------------|
| 1 | ... | ... |
| 2 | ... | ... |

## STEP 3: CONTRADICTIONS & GAPS
| Assumption | Truth | Contradiction? | Implication |
|------------|-------|----------------|-------------|
| ... | ... | Yes/Partial/No | ... |

## STEP 4: REBUILT SOLUTIONS
### Solution 1: [Name]
- **Based on truth(s):** Truth #...
- **Stop doing (assumptions cũ):** ...
- **Start doing:** ...
- **Hypothesis:** If [change] then [metric] because [reason]
- **Test method:** ...
- **Priority:** P0/P1/P2

### Solution 2: [Name]
...

## STEP 5: VALIDATION PLAN
| Solution | Method | Success criteria | Timeline | Owner |
|----------|--------|------------------|----------|-------|
| ... | ... | ... | ... | ... |

## RECOMMENDATION
[1-2 câu: nên làm gì, không nên làm gì, và tại sao]

## OPEN QUESTIONS / [CẦN VERIFY]
- [Câu hỏi chưa có câu trả lời, cần data thêm]

## RELATED SKILLS
- Feed into: [[use-case-document]] (nếu solution ảnh hưởng strategy)
- Feed into: [[JTBD.md]] (nếu cần hiểu user job sâu hơn)
- Feed into: [[brainstorming]] (nếu cần generate solution variants từ truths)
```

---

## Rules & Constraints

1. **Phân biệt rõ Assumption vs Truth.** Không được coi assumption là truth. Nếu không chắc → đánh dấu `[HYPOTHESIS]`

2. **Mỗi truth phải có evidence.** Evidence可以是:
   - Data từ MoMo (GSC/GA4/Appsflyer)
   - Xác nhận từ Google Search Central hoặc nguồn chính thống
   - Logic không thể bác bỏ (ví dụ: "user sẽ rời đi nếu không tìm thấy câu trả lời")

3. **Không dùng first-principles cho mọi quyết định.** Chỉ dùng khi problem thực sự stuck hoặc assumption đang gây sai lệch.

4. **Rebuilt solutions phải actionable.** Không dừng ở "nhận ra assumption sai" — phải có giải pháp thay thế cụ thể.

5. **Luôn có validation plan.** First-principles không phải "tôi nghĩ vậy nên đúng". Phải test.

6. **Challenge ngay cả "truth" của chính mình.** Truth hôm nay có thể sai khi context thay đổi. First-principles là quá trình, không phải đích đến.

7. **Không dùng để "thắng" tranh luận.** Mục đích là tìm giải pháp đúng, không phải chứng minh mình đúng.

---

## Anti-Patterns (đừng làm)

1. **Dùng first-principles để biện minh cho ý kiến cá nhân** — "Theo first-principles thì solution của tôi đúng" mà không qua Step 2 (fundamental truths)

2. **Bỏ qua evidence hiện có** — Có data từ GSC rồi mà vẫn deconstruct → phí thời gian

3. **Không phân biệt được assumption và truth** — "User thích content ngắn" là assumption, không phải truth

4. **Rebuild solution mà không test** — First-principles xong, implement ngay mà không validate → nguy cơ sai vẫn cao

5. **Áp dụng cho vấn đề quá nhỏ** — "Nên dùng H1 hay title tag nào trước" không cần first-principles

---

## Integration với MoMo Context

- **YMYL truth:** Trong tài chính, trust là fundamental truth. Mọi giải pháp phải tăng (hoặc ít nhất không giảm) trust signal.
- **Web-to-App truth:** User không muốn chuyển app nếu web đã solve được job. Đây là truth cốt lõi.
- **GEO truth:** AI Overview ưu tiên câu trả lời trực tiếp, ngắn gọn, có nguồn — không phải content dài.
- **Negative SEO truth:** momo.vn từng bị tấn công backlink → truth: "Cần monitor backlink profile thường xuyên" là truth, không phải "có backlink là tốt" (assumption cũ).

---

## Example Invocation

```
User: "Chúng ta đang làm schema cho mọi page vì best practice. Nhưng không thấy AI Overview citation tăng. Tại sao?"

Agent: [Chạy first-principles analysis]
→ Step 1: Liệt kê assumptions ("schema = AI citation", "càng nhiều schema càng tốt")
→ Step 2: Fundamental truths ("AI citation dựa trên content quality + answer-first format")
→ Step 3: Contradiction: assumption #1 sai
→ Step 4: Rebuilt solution: chỉ implement schema có mục đích (FAQ cho anxiety, HowTo cho process)
→ Step 5: Validation plan: compare pages with targeted schema vs generic schema
→ Output: Full analysis + recommendation
```