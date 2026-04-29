
---
name: zero-hallucination
description: >
  Nguyên tắc và checklist để đảm bảo mọi output (content, audit, analysis, strategy)
  KHÔNG chứa thông tin sai lệch, bịa đặt, hoặc suy diễn thiếu căn cứ. Áp dụng bắt buộc
  cho MỌI output trong lĩnh vực Fintech/Financial của MoMo.vn, đặc biệt các nội dung
  có tính YMYL (Your Money or Your Life). Trigger khi user yêu cầu: viết content,
  audit page, phân tích data, đề xuất chiến lược, hoặc bất kỳ output nào liên quan đến
  tài chính, bảo hiểm, vay mượn, thanh toán. Luôn chạy checklist này TRƯỚC khi publish
  bất kỳ nội dung nào.
category: quality-assurance
tags:
  - zero-hallucination
  - eeat
  - fintech
  - ymyl
  - quality
  - fact-check
  - momo
  - financial
author: klaus-momo
version: 1.0.0
---

# Zero-Hallucination - Fintech Factual Integrity Skill

## Liên kết
- Skill này là một phần của hệ thống MoMo Web Growth
- Xem tổng thể: [[SKILL]]
- Workflow: [[SKILL#Workflow Chuẩn cho 1 Use Case Mới]]
- Skill liên quan (phải dùng cùng):
  - [[Seo-Geo-audit]] - audit page có hallucination không
  - [[use-case-document]] - strategy document phải dựa trên truth
  - [[First-Principles.md]] - xác định truth trước khi viết
- Skill đầu ra (sau kiểm tra):
  - Content đã được fact-check → sẵn sàng publish
  - Audit report có xác nhận không hallucination
  - Strategy document có nguồn cho mọi số liệu

---

## Core Philosophy

> **"Không có gì tệ hơn một câu trả lời tự tin nhưng sai trong lĩnh vực tài chính."**

Zero-Hallucination = cam kết **không bịa đặt, không suy diễn, không "chắc là vậy"** khi chưa có bằng chứng.

Trong bối cảnh MoMo Fintech (YMYL - Your Money or Your Life):
- Một câu sai về lãi suất có thể khiến user quyết định sai
- Một số liệu bịa về phí có thể ảnh hưởng đến trust của toàn bộ super-app
- Một recommendation thiếu căn cứ có thể dẫn đến chiến lược sai, tốn hàng trăm triệu

**Rule số 1:** Nếu không chắc → nói "không biết" hoặc đánh dấu `[CẦN VERIFY]`. Không bao giờ "đoán" trong output chính thức.

**Rule số 2:** Mọi số liệu, ngày tháng, con số, tỷ lệ, quy định PHẢI có nguồn. Không có nguồn = không được đưa vào output.

---

## YMYL Context trong MoMo

MoMo.vn hoạt động trong lĩnh vực **Fintech**, thuộc nhóm YMYL (Your Money or Your Life) theo đánh giá của Google.

| YMYL Sub-category | MoMo Use Cases liên quan | Mức độ rủi ro nếu hallucination |
|-------------------|--------------------------|-------------------------------|
| **Financial Services** | Credit, Vay Nhanh, Vi Trả Sau | ⚠️ CRITICAL - sai lãi suất/điều khoản có thể gây thiệt hại tài chính |
| **Insurance** | Bảo hiểm xe máy, bảo hiểm sức khỏe | ⚠️ CRITICAL - sai quyền lợi/phạm vi bảo hiểm |
| **Banking/ Payments** | Billpay, Chuyển tiền, Nap tiền | ⚠️ HIGH - sai phí/thời gian xử lý |
| **Investment** | Chứng chỉ quỹ, Tài khoản đầu tư | ⚠️ CRITICAL - sai tỷ suất lợi nhuận/rủi ro |
| **Legal/Regulatory** | Điều khoản, Chính sách bảo mật | ⚠️ CRITICAL - sai quy định pháp lý |

**EEAT signals bắt buộc cho MoMo Fintech Content:**

| Signal | Yêu cầu | Áp dụng cho |
|--------|---------|-------------|
| **Author credentials** | Tác giả có chuyên môn tài chính | Mọi bài viết về financial advice |
| **Source citations** | Trích dẫn nguồn chính thống (Ngân hàng Nhà nước, Bộ Tài chính, MoMo chính thức) | Số liệu, quy định, lãi suất |
| **Last updated date** | Hiển thị rõ ngày cập nhật cuối | Mọi content (đặc biệt lãi suất, phí) |
| **Expert review** | Được chuyên gia tài chính review | Content YMYL cao (Vay, Bảo hiểm, Đầu tư) |
| **Official MoMo sources** | Link đến momo.vn chính thức | Mọi thông tin về sản phẩm/dịch vụ MoMo |
| **Regulatory references** | Trích dẫn văn bản pháp luật khi relevant | Phí, lãi suất, điều khoản |

**Skill liên quan:** Để audit EEAT signals trên page hiện tại, dùng `[[seo-geo-audit]]` Axis 3.

---

## Hallucination Types in Fintech (Nhận diện để tránh)

| Type | Mô tả | Ví dụ trong Fintech | Cách phát hiện |
|------|-------|---------------------|----------------|
| **Fact Hallucination** | Bịa ra số liệu, ngày tháng, sự kiện không có thật | "Lãi suất vay hiện tại là 1.5%/tháng" (thực tế 2.5%) | Check với nguồn chính thống |
| **Attribution Hallucination** | Gán một phát biểu/số liệu cho sai nguồn | "Theo Ngân hàng Nhà nước, phí chuyển tiền là 0.5%" (thực tế NHNN không nói vậy) | Kiểm tra lại nguồn gốc |
| **Reasoning Hallucination** | Suy luận sai logic nhưng kết luận có vẻ hợp lý | "Lãi suất giảm nên nên vay ngay" (không tính đến các yếu tố khác) | Dùng `[[critical-thinking]]` kiểm tra logic |
| **Implication Hallucination** | Suy diễn quá mức từ dữ liệu có thật | "Dữ liệu cho thấy 80% user hài lòng → MoMo là app tốt nhất VN" | Kiểm tra claim có được support bởi evidence không |
| **Citation Hallucination** | Bịa ra nghiên cứu, bài báo, tài liệu không tồn tại | "Theo nghiên cứu của McKinsey 2024..." (không có nghiên cứu đó) | Google search xem có tồn tại không |
| **Confidence Hallucination** | Nói chắc chắn về điều chưa được xác minh | "Chắc chắn Google sẽ ưu tiên content có schema" (chưa được xác nhận) | Đánh dấu `[HYPOTHESIS - cần test]` |
| **Omission Hallucination** | Bỏ qua thông tin quan trọng dẫn đến hiểu sai | "Vay nhanh chỉ từ 5 phút" (không đề cập điều kiện approval) | Kiểm tra coverage có đầy đủ không |

**Skill liên quan:** Để phát hiện reasoning hallucination, dùng `[[critical-thinking]]`. Để xác định truth tránh fact hallucination, dùng `[[first-principles]]`.

---

## Zero-Hallucination Checklist (BẮT BUỘC cho MỌI output)

Trước khi publish **bất kỳ** output nào (content, audit report, strategy document, analysis), phải chạy checklist này.

### Pre-Publish Gate
```

□ Mọi số liệu đều có nguồn? (URL, tài liệu, ngày tháng)  
→ Không có nguồn = không được đưa vào output

□ Mọi claim về sản phẩm/dịch vụ MoMo đều được xác nhận với thông tin chính thức?  
→ Nếu chưa xác nhận → đánh dấu [CẦN VERIFY VỚI PO]

□ Có bất kỳ câu nào bắt đầu bằng "có lẽ", "chắc là", "có thể", "thường thì" không?  
→ Nếu có → kiểm tra lại: đây có phải hallucination không?

□ Nếu output chứa recommendation, có dựa trên data thực (GSC/GA4/Ahrefs) không?  
→ Không có data → đánh dấu [HYPOTHESIS - cần test]

□ Có trích dẫn nghiên cứu/bài báo nào không? Nghiên cứu đó có thật không?  
→ Google search để verify sự tồn tại

□ Có số liệu về đối thủ cạnh tranh không? Nguồn từ đâu?  
→ Chỉ dùng Ahrefs/Semrush/SimilarWeb có timestamp

□ Có đề cập đến quy định pháp luật (lãi suất, phí, điều khoản) không?  
→ Phải trích dẫn văn bản cụ thể (số, năm, điều khoản)

□ Content có YMYL không? Nếu có → đã có EEAT signals chưa?  
→ Author, last updated, sources, expert review

□ Mọi internal link đã check trỏ đúng URL chưa?  
→ Click test hoặc manual verify

□ Có hình ảnh/infographic chứa số liệu không? Số liệu có khớp với nguồn không?  
→ Fact-check số liệu trong image

```

### Post-Publish Verification (trong vòng 24h)
```

□ Google Search Console: Kiểm tra page có bị flag là "misleading" không?

□ User feedback: Có complaint nào về thông tin sai không?

□ MoMo internal review: PO/Product có confirm thông tin chính xác không?

□ Số liệu có outdated không? (Đặc biệt lãi suất, phí thay đổi thường xuyên)

````

---

## Source Hierarchy (Thứ tự ưu tiên của nguồn)

Khi cần trích dẫn hoặc xác minh thông tin, ưu tiên theo thứ tự:

| Priority | Source Type | Ví dụ | Độ tin cậy |
|----------|-------------|-------|------------|
| **1** | MoMo chính thức | momo.vn, tài liệu nội bộ, PO confirmation | ✅ HIGHEST |
| **2** | Cơ quan quản lý nhà nước | Ngân hàng Nhà nước, Bộ Tài chính, Thông tư/Nghị định | ✅ HIGH |
| **3** | Google chính thống | Google Search Central, Google Developers Blog | ✅ HIGH |
| **4** | Dữ liệu first-party | GSC, GA4, Appsflyer (có timestamp) | ✅ HIGH |
| **5** | Third-party tools | Ahrefs, Semrush, SimilarWeb (ghi rõ ngày crawl) | ⚠️ MEDIUM |
| **6** | Báo chí uy tín | VnExpress, Reuters, Bloomberg (nguồn tài chính) | ⚠️ MEDIUM |
| **7** | Nghiên cứu ngành | McKinsey, Forrester, Gartner (ghi rõ năm) | ⚠️ MEDIUM |
| **8** | Competitor websites | Đối thủ (chỉ dùng để tham khảo, không dùng làm truth) | ❌ LOW |
| **9** | AI-generated (ChatGPT, Perplexity) | Tuyệt đối KHÔNG dùng làm nguồn | ❌ FORBIDDEN |

**Rule:** Không dùng AI-generated content làm nguồn để trích dẫn. AI có thể hallucinate. Nếu cần dùng số liệu từ AI, phải verify với nguồn cấp 1-2.

---

## Fact-Check Protocol cho từng loại nội dung

### 1. Content về sản phẩm tài chính (Vay, Bảo hiểm, Đầu tư)

```markdown
VERIFICATION STEPS:
1. Lấy thông tin từ source chính thức của MoMo (momo.vn/[product])
2. Confirm với PO/Product owner nếu thông tin không có trên web
3. Ghi rõ "Cập nhật lần cuối: [date]"
4. Nếu có số liệu (lãi suất, phí, thời gian xử lý) → trích dẫn URL cụ thể
5. KHÔNG tự suy diễn "thường thì", "đa số" cho sản phẩm có điều kiện

EXAMPLE:
✅ Đúng: "Theo momo.vn/vay-nhanh, lãi suất hiện tại từ 2.5%/tháng (cập nhật tháng 3/2026)."
❌ Sai: "Lãi suất vay nhanh thường khoảng 2-3%/tháng."
````

### 2. Content về SEO/GEO (Recommendations, Best practices)

```markdown
VERIFICATION STEPS:
1. Phân biệt "Google đã xác nhận" vs "SEO community nói"
2. Nếu chưa được Google xác nhận → đánh dấu [HYPOTHESIS - chưa được xác minh]
3. Nếu dựa trên data của MoMo → ghi rõ "Dựa trên phân tích data từ GSC tháng [month]"
4. Không nói chắc chắn về tương lai (Google sẽ thay đổi, AI Overview sẽ...)

EXAMPLE:
✅ Đúng: "Google Search Central đã xác nhận rằng schema giúp hiểu content nhưng không phải ranking factor."
✅ Đúng: "Data từ GSC của MoMo cho thấy page có schema FAQ có CTR cao hơn 15% (so sánh tháng 1-2/2026)."
❌ Sai: "Google sẽ ưu tiên page có schema trong tương lai." (không ai biết)
```

### 3. Phân tích cạnh tranh (Competitor analysis)

```markdown
VERIFICATION STEPS:
1. Ghi rõ nguồn số liệu (Ahrefs crawl ngày [date])
2. Không suy luận về chiến lược của đối thủ nếu không có bằng chứng
3. Phân biệt "quan sát" vs "kết luận"

EXAMPLE:
✅ Đúng: "Theo Ahrefs (crawl 15/03/2026), competitor X có 120 keywords top 3 cho cluster 'vay nhanh'."
✅ Đúng (quan sát): "Page của competitor Y có FAQ schema trong khi MoMo chưa có."
❌ Sai (suy luận thiếu bằng chứng): "Competitor Y đang tập trung vào GEO vì họ có FAQ schema."
```

### 4. Data analysis (GSC, GA4, Ahrefs)

```markdown
VERIFICATION STEPS:
1. Ghi rõ khoảng thời gian của data
2. Nếu sample size nhỏ (< 100 sessions) → đánh dấu [SAMPLE NHỎ - cần thận trọng]
3. Phân biệt correlation vs causation
4. Không kết luận "causal" nếu chưa có A/B test hoặc data đủ mạnh

EXAMPLE:
✅ Đúng: "Trong tháng 2/2026, page A có CTR 5.2% từ GSC, tăng 0.8% so với tháng trước. Tuy nhiên chưa thể kết luận nguyên nhân do thay đổi meta title hay do seasonal."
❌ Sai: "Thay đổi meta title đã làm tăng CTR 0.8%." (chưa có bằng chứng causal)
```

### 5. Chiến lược và recommendation

```markdown
VERIFICATION STEPS:
1. Mỗi recommendation phải dựa trên ít nhất 1 data point hoặc truth
2. Nếu dựa trên hypothesis → đánh dấu rõ [HYPOTHESIS - đề xuất A/B test]
3. Ghi rõ mức độ confidence: HIGH (có data MoMo), MEDIUM (có data industry), LOW (cần test)

EXAMPLE:
✅ Đúng: "[HYPOTHESIS - cần A/B test] Chuyển CTA lên above fold có thể tăng conversion rate. Dựa trên heatmap từ Clarity cho thấy 70% user không scroll đến CTA hiện tại."
❌ Sai: "Chuyển CTA lên trên sẽ tăng conversion." (không có evidence, không đánh dấu hypothesis)
```

---

## Source Citation Format (Định dạng trích dẫn chuẩn)

### Cho số liệu từ MoMo internal

```markdown
[Nguồn: GSC - momo.vn/insurance, khoảng thời gian 01/02/2026 - 29/02/2026]
[Nguồn: GA4 - event cta_click, 7 ngày gần nhất]
[Nguồn: Appsflyer - install attribution, tháng 2/2026]
[Nguồn: Xác nhận từ PO Nguyễn Văn A, ngày 15/03/2026]
```

### Cho số liệu từ third-party tools

```markdown
[Nguồn: Ahrefs Site Explorer, crawl ngày 10/03/2026]
[Nguồn: Semrush, domain momo.vn, tháng 2/2026]
[Nguồn: Google Search Console, property momo.vn, khoảng thời gian 28 ngày tính đến 15/03/2026]
```

### Cho thông tin từ cơ quan quản lý

```markdown
[Nguồn: Thông tư 39/2016/TT-NHNN, Điều 13, Khoản 2]
[Nguồn: Nghị định 91/2020/NĐ-CP về chống spam cuộc gọi, có hiệu lực từ 15/12/2020]
[Nguồn: Quyết định 2545/QĐ-NHNN ngày 31/12/2025 về lãi suất tái cấp vốn]
```

### Cho thông tin từ Google

```markdown
[Nguồn: Google Search Central, "Google's Core Web Vitals report", publish date 12/05/2021]
[Nguồn: Google Search Central Blog, "A new link spam fighting system", published 15/12/2023]
[Nguồn: Google SEO Office Hours, timestamp 25:30, YouTube, ngày 10/01/2026]
```

### Khi chưa có nguồn (phải dùng placeholder)

```markdown
[CẦN VERIFY - Liên hệ PO Nguyễn Văn A để xác nhận lãi suất hiện tại]
[CẦN VERIFY - Số liệu này cần được xác nhận từ Ahrefs crawl mới nhất]
[CẦN VERIFY - Chưa có data từ GSC cho page này]
```

---

## E-E-A-T Compliance Matrix cho MoMo Content

|Content Type|Experience|Expertise|Authoritativeness|Trustworthiness|
|---|---|---|---|---|
|**Transaction page (Vay, Insurance)**|User reviews, case studies|Chuyên gia tài chính review|Domain momo.vn, liên kết đến thông tin chính thức|Source citations, last updated, security badges|
|**Blog informational**|First-hand experience|Author byline với credentials|Backlinks từ domain uy tín, citations|Fact-checked, sources rõ ràng|
|**Comparison page**|Side-by-side analysis|Chuyên gia so sánh|Dẫn nguồn từ mỗi nhà cung cấp|Không thiên vị, tiêu chí rõ ràng|
|**How-to / Guide**|Step-by-step từ người dùng thực tế|Chuyên môn lĩnh vực|Được cite bởi AI Overview / Google|Cập nhật thường xuyên|
|**Legal / Terms pages**|N/A|Legal team review|Chính thức từ MoMo|Đúng quy định pháp luật|

**Skill liên quan:** Để audit E-E-A-T trên page hiện tại, dùng `[[seo-geo-audit]]` Axis 3.

---

## Zero-Hallucination trong AI-assisted Content

Khi dùng AI (ChatGPT, Claude, Perplexity) để hỗ trợ viết content:

### Rules:

1. **KHÔNG dùng AI-generated số liệu.** AI có thể hallucinate số liệu trông rất thật.
2. **KHÔNG dùng AI-generated trích dẫn nghiên cứu.** AI thường bịa ra tên nghiên cứu, tác giả, năm.
3. **LUÔN fact-check mọi output của AI** trước khi đưa vào content chính thức.
4. **LUÔN ghi rõ phần nào do AI viết** (nếu dùng) để reviewer biết cần check kỹ.

### AI Output Review Protocol:

```markdown
KHI NHẬN OUTPUT TỪ AI:
1. Khoanh vùng các phần có số liệu → verify từng số với nguồn cấp 1-2
2. Khoanh vùng các phần có trích dẫn → Google search xem có tồn tại không
3. Khoanh vùng các phần có "theo nghiên cứu", "theo báo cáo" → tìm báo cáo gốc
4. Nếu không tìm thấy nguồn → XÓA hoặc đánh dấu [CẦN VERIFY]
5. Kiểm tra logic (dùng [[critical-thinking]]) → phát hiện reasoning hallucination
```

---

## Khi phát hiện hallucination trong output cũ

### Response Protocol:

```markdown
1. XÁC NHẬN: "Phát hiện hallucination trong [tài liệu/page] tại [vị trí cụ thể]"
2. ĐÁNH GIÁ MỨC ĐỘ: Critical (ảnh hưởng quyết định tài chính) / High / Medium / Low
3. HÀNH ĐỘNG NGAY:
   - Critical → Gỡ page ngay, thông báo stakeholders
   - High → Update trong vòng 24h, đánh dấu đã sửa
   - Medium/Low → Update trong sprint hiện tại
4. GHI NHẬN: Lưu lại để tránh lặp lại trong tương lai
5. CẬP NHẬT CHECKLIST: Nếu hallucination chưa được cover bởi checklist hiện tại
```

---

## Output Format: Hallucination Audit Report

Khi được yêu cầu kiểm tra content/page có hallucination không:

```markdown
# HALLUCINATION AUDIT REPORT
**Content/Page:** [URL hoặc tên document]
**Audit date:** YYYY-MM-DD
**Auditor:** Klaus
**Severity:** Critical / High / Medium / Low / None

## SUMMARY
[1-2 câu: có hallucination không, mức độ nghiêm trọng, cần action gì]

## FINDINGS

| # | Location | Hallucination Type | Claim | Truth | Source | Severity | Fix |
|---|----------|-------------------|-------|-------|--------|----------|-----|
| 1 | Para 3 | Fact | "Lãi suất 1.5%" | Lãi suất 2.5% | momo.vn/vay | Critical | Update số |
| 2 | Para 7 | Citation | "Theo McKinsey 2024" | Không tồn tại | Google search | High | Remove hoặc tìm source thật |

## EEAT SIGNALS CHECK
| Signal | Status | Notes |
|--------|--------|-------|
| Author byline | ✅ Present | Nguyễn Văn A, Chuyên gia tài chính |
| Last updated date | ❌ Missing | Cần thêm |
| Source citations | ⚠️ Partial | 3/5 claims có source |
| Expert review | ❌ Missing | Nên có cho content YMYL này |

## RECOMMENDATIONS
1. [Critical] Fix #1 ngay lập tức
2. [High] Remove #2 hoặc tìm nguồn thay thế
3. [Medium] Thêm last updated date
4. [Low] Bổ sung source cho 2 claims còn lại

## VERIFICATION SOURCES
- [URL 1] - [ngày truy cập]
- [URL 2] - [ngày truy cập]
- [Xác nhận từ PO - ngày]
```

---

## Rules & Constraints

1. **Zero-Hallucination là mandatory, không phải optional.** Mọi output đều phải qua checklist.
    
2. **Nếu không có nguồn → không đưa vào output.** Không có ngoại lệ.
    
3. **YMYL content có threshold cao hơn.** Content về vay, bảo hiểm, đầu tư phải được fact-check kỹ gấp đôi.
    
4. **AI-generated content không được coi là nguồn.** Phải verify với nguồn cấp 1-2.
    
5. **Mọi số liệu phải có timestamp.** "Lãi suất 2.5%" không đủ. Phải ghi "cập nhật tháng 3/2026".
    
6. **Phân biệt rõ fact, hypothesis, và opinion.**
    
    - Fact = có nguồn xác nhận
    - Hypothesis = cần test, đánh dấu `[HYPOTHESIS]`
    - Opinion = quan điểm cá nhân, đánh dấu `[QUAN ĐIỂM CÁ NHÂN]`
7. **Nếu phát hiện hallucination trong output cũ → phải report và fix.** Không bỏ qua.
    
8. **Luôn dùng `[[critical-thinking]]` để kiểm tra logic trước khi kết luận.**
    
9. **Luôn dùng `[[first-principles]]` để xác định truth trước khi viết content mới.**
    
10. **Khi nghi ngờ → hỏi.** Không tự suy diễn. Ghi `[CẦN VERIFY VỚI PO]` hoặc `[CẦN CHECK DATA]`.
    

---

## Integration với các Skills khác

|Skill|Khi nào chain|Flow|
|---|---|---|
|`[[content-aeo]]`|Trước khi publish content|Viết content → Chạy zero-hallucination checklist → Publish|
|`[[seo-geo-audit]]`|Trong audit process|Audit page → Kiểm tra hallucination trong content → Ghi vào report|
|`[[momo-seo-content-brief]]`|Khi tạo brief|Brief phải include "factual integrity requirements" section|
|`[[use-case-document]]`|Khi viết strategy|Mọi số liệu trong strategy phải có source|
|`[[critical-thinking]]`|Để phát hiện reasoning hallucination|Dùng trước hoặc trong khi fact-check|
|`[[first-principles]]`|Để xác định truth trước khi viết|First-principles → Truth → Content không hallucination|
|`[[web-growth-analysis]]`|Khi phân tích data|Phân biệt correlation vs causation, không hallucinate causal claims|

---

## Example Invocation

```
User: "Viết bài về so sánh lãi suất vay giữa MoMo và đối thủ"

Agent:
1. [Chạy zero-hallucination checklist trước khi viết]
2. Xác định cần source cho:
   - Lãi suất MoMo → lấy từ momo.vn/vay-nhanh [cập nhật tháng 3/2026]
   - Lãi suất đối thủ → lấy từ Ahrefs crawl [ngày 15/03/2026] hoặc web đối thủ
3. Đánh dấu hypothesis: "[HYPOTHESIS - cần xác nhận với PO] Điều kiện vay của MoMo dễ hơn đối thủ"
4. Viết content → chạy checklist → publish
5. Output kèm source citations đầy đủ
```

```
User: "Audit page momo.vn/insurance xem có hallucination không"

Agent:
1. Fetch page momo.vn/insurance
2. Chạy zero-hallucination checklist từng mục
3. Xác định các claim cần verify
4. Đối chiếu với nguồn chính thức (momo.vn, xác nhận từ PO)
5. Output Hallucination Audit Report
```

---

## Glossary

|Term|Định nghĩa|
|---|---|
|**Hallucination**|Thông tin sai lệch, bịa đặt, không có căn cứ trong output|
|**YMYL**|Your Money or Your Life - nhóm chủ đề ảnh hưởng trực tiếp đến tài chính/sức khỏe/an toàn của người dùng|
|**E-E-A-T**|Experience, Expertise, Authoritativeness, Trustworthiness - tiêu chí đánh giá chất lượng của Google|
|**Fact-check**|Quá trình xác minh tính chính xác của thông tin|
|**Source**|Nguồn gốc của thông tin (URL, tài liệu, xác nhận)|
|**First-party data**|Dữ liệu thu thập trực tiếp từ MoMo (GSC, GA4, Appsflyer)|
|**Ground truth**|Sự thật cơ bản không thể bác bỏ, dùng làm căn cứ để fact-check|

```

---

## Tóm tắt nội dung chính:

1. **Core Philosophy** - Cam kết không hallucination trong lĩnh vực fintech YMYL
2. **YMYL Context** - Mapping MoMo Use Cases với mức độ rủi ro
3. **EEAT Signals** - Bắt buộc cho content tài chính
4. **7 Types of Hallucination** - Nhận diện để tránh
5. **Pre-Publish Checklist** - Gate bắt buộc
6. **Source Hierarchy** - Thứ tự ưu tiên nguồn
7. **Fact-Check Protocol** - Theo từng loại nội dung
8. **Citation Format** - Chuẩn trích dẫn
9. **EEAT Compliance Matrix**
10. **AI Content Rules** - Cách xử lý output từ AI
11. **Hallucination Audit Report** - Format kiểm tra
12. **Integration với các skill khác** - Đặc biệt critical-thinking, first-principles, seo-geo-audit
```