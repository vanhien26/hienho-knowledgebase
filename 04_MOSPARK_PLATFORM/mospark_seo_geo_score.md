# MoSpark - SEO/GEO Scoring System
Hệ thống tự động kiểm duyệt & chấm điểm SEO/GEO chất lượng nội dung

> - **Project Name:** MoSpark Web Platform
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Bảo
> - **PIC:** Trọng (Tech/API), Thuận (UI), Lộc (Access Control)
> - **Version:** 1.3.1 · June 2026


---

## 1. Executive Summary

### 1.1. Bối cảnh (Situation)
MoSpark cho phép Editor tự động hóa việc sinh nội dung qua GenAI và tạo trang nhanh chóng. Tuy nhiên, nếu thiếu đi một hệ thống kiểm duyệt chặt chẽ ngay tại điểm xuất bản (Publish Point), nền tảng rất dễ sản sinh ra rác dữ liệu, làm giảm điểm E-E-A-T và gây ảnh hưởng xấu tới toàn bộ domain `momo.vn`.

### 1.2. Vấn đề cốt lõi (Complication)
- **Thiếu Rào Cản Kỹ Thuật:** Lỗi On-page SEO, thiếu Schema hoặc Core Web Vitals (CWV) kém không được phát hiện kịp thời.
- **Rủi Ro YMYL:** MoMo là domain tài chính, Google áp chuẩn duyệt khắt khe. Bài viết thiếu Disclaimer hoặc cấu trúc lỏng lẻo sẽ bị phạt.
- **Tín Hiệu GEO Yếu:** Các AI Search Engines không tìm thấy đủ "Fact Density" hoặc Schema phù hợp để trích dẫn nội dung của MoMo.

### 1.3. Giải pháp (Resolution)
Tích hợp **SEO/GEO Checklist Scoring** trực tiếp vào **Section SEO** của MoSpark Admin để tự động chấm điểm và validate chất lượng mỗi page.
- Tạo một "trạm kiểm soát" (Governance Gate) với các điều kiện chặn cứng (Hard Block).
- Tính điểm tự động để phân loại (Pass/Warning/Blocked) trước khi bài viết được xuất bản ra ngoài.

---

## 2. Stakeholder (Nhóm người dùng chính)

| Vai trò | Trách nhiệm chính | Mục tiêu |
| :--- | :--- | :--- |
| **Content Editor** | Viết nội dung, nhập Metadata. | Nhập Primary Keyword, rà soát cảnh báo từ Score Panel và tối ưu bài viết đạt ngưỡng Pass. |
| **Web Product Lead** | Thiết kế bộ quy tắc Scoring. | Duy trì và nâng cấp các tiêu chuẩn SEO/GEO/CWV để phù hợp với thuật toán của Google/AI. |
| **Developer (Tech Team)** | Cài đặt logic parse DOM & check API. | Triển khai các thuật toán auto-check và tích hợp Lighthouse API cho CWV. |

---

## 3. Bài Toán Cần Giải & Success Metrics

### 3.1. Mục tiêu chiến lược (Objective & Scope)
- **Mục tiêu:** Tích hợp SEO/GEO Checklist Scoring trực tiếp vào Section SEO của MoSpark Admin để validate chất lượng của mỗi page trước khi Publish. Biến khu vực nhập dữ liệu SEO thành một "trạm kiểm soát" chất lượng, đảm bảo không có page nào được publish khi chưa đạt ngưỡng tối thiểu về Technical SEO, On-Page Content, và GEO readiness.
- **Áp dụng cho:** Tất cả page type trên MoSpark (Mini Web, Landing Page, Blog, Merchant Page).
- **Trigger:** Editor tạo page mới trên MoSpark, page ở trạng thái Draft, editor muốn Publish lần đầu.
- **Out of scope:** Post-publish monitoring, A/B test scoring, tracking parameter validation, xử lý noindex intentional.

### 3.2. Success Metrics (SMART)
- **Quality Assurance:** 100% trang mới trên MoSpark pass mức điểm tối thiểu 60/100 và không vi phạm lỗi Hard Block nào.
- **Performance:** 100% trang xuất bản vượt qua bài test LCP (≤ 2.5s) và CLS (≤ 0.1).
- **Automation:** Giảm 90% thời gian Review On-page của Web Product Lead do hệ thống đã tự động cảnh báo lỗi.

---

## 4. Workflow & User Flow

```mermaid
flowchart TD
    A([Bắt đầu: Keywords & Bài viết sync từ\nGenAI Content Engine]) --> B[Đẩy vào Blog/Merchant Editor\n(Trạng thái Draft)]
    B --> C{1. Kiểm tra\nĐiều kiện cứng}
    
    C -- "Thiếu Keyword / CWV / Hard Block" --> C1([CASE 1: CHẶN PUBLISH\n(Buộc Editor Review & Sửa)])
    
    C -- "Pass hết Điều kiện cứng" --> D[2. Tính điểm SEO/GEO]
    
    D --> E{3. Phân loại điểm?}
    
    E -- "Score < 60" --> C1
    
    E -- "Score 60 - 79" --> D1([CASE 2: CHO PHÉP PUBLISH\nTrạng thái: Cần tối ưu])
    
    E -- "Score ≥ 80" --> D2([CASE 3: CHO PHÉP PUBLISH\nTrạng thái: Tốt])
```

---

## 5. Input Model

Các field editor phải nhập trước khi Scoring chạy. Map với field hiện có trong MoSpark:

| Field | Source | Ghi chú |
|-------|--------|---------|
| Meta Title | Sinh từ Editor/GenAI | Dùng để check length, keyword placement |
| Meta Description | Sinh từ Editor/GenAI | Dùng để check length |
| **Primary Keyword** | Sync từ GenAI Content Engine | 1 từ khóa duy nhất. Nền tảng chặn Publish nếu trường này rỗng. |
| **Secondary Keywords** | Sync từ GenAI Content Engine | Danh sách từ khóa phụ. Optional. |

> **Lưu ý Data Flow:** Toàn bộ Keywords (Primary/Secondary) sẽ được hệ thống `GenAI Content Engine` tạo và map tự động dựa trên Keyword Master Registry, sau đó đẩy (push) trực tiếp sang Blog Editor dưới dạng Draft. Editor không cần nhập tay ở bước này. Tuy nhiên, trước khi bấm Publish, **hệ thống Score sẽ làm nhiệm vụ chặn (Hard Block) để Editor phải Review lại chất lượng bài sinh ra từ AI.**

### 5.1 Primary Keyword

**Định nghĩa:** **1 từ khóa duy nhất** mà page được thiết kế để rank chính. Đây là từ khóa có priority cao nhất, thường có search volume cao, intent rõ ràng, và value conversion cao nhất. (Ví dụ: "vay tiền", "bảo hiểm")

**Validation Rules (Review Phase):**
- **Bắt buộc:** Không được để trống.
- **Min length:** Tối thiểu 2 ký tự.
- **Max length:** Tối đa 50 ký tự.
- **Ký tự hợp lệ:** Tiếng Việt (có dấu), chữ, số, dấu cách. Không chứa ký tự đặc biệt.
- **Không phải toàn số:** Phải chứa ít nhất 1 ký tự chữ.

**UI/UX:** Label "Primary Keyword *", Text Input (đã auto-fill từ GenAI), Character counter (X/50), Real-time validation.

### 5.2 Secondary Keywords

**Định nghĩa:** Danh sách các từ khóa phụ, bổ trợ cho Primary để cover thêm keyword variants, long-tail searches. (Ví dụ: "vay nhanh, vay online")

**Validation Rules (Review Phase):**
- **Optional:** Được phép để trống.
- **Format:** Cách nhau bởi dấu phẩy + space.
- **Max từ khóa:** Tối đa 10 từ khóa phụ.
- **Max length mỗi từ:** 50 ký tự.
- **Không trùng lặp:** Loại bỏ keyword trùng. Có cảnh báo nhẹ nếu chứa một phần Primary Keyword.

### 5.3 Integration với SEO/GEO Scoring
- **Primary Keyword:** Dùng check H1 (1.6), Density (2.2), Placement (2.3), Entity Context (3.4).
- **Secondary Keywords:** Check tần suất xuất hiện (2.4).
- **Behavior khi thay đổi:** Nếu thay đổi Keyword sau khi Run Score, điểm reset về "Chưa chạy" và yêu cầu Run lại.

### 5.4 Lưu ý cho Dev (Parsing)
Dev split `keywords` array từ field. Validate theo format regex.
Fallback: Nếu Publish mà Primary trống → nút Publish bị disable hoàn toàn.

---

## 6. Scoring Model (SEO/GEO Disciplines)

Để đảm bảo chuẩn thuật ngữ chuyên ngành và phân tách rõ ràng trách nhiệm tối ưu, checklist được chia thành 3 Blocks (Nhóm). Mỗi item trong nhóm sẽ có cờ `Hard Block`, nếu vi phạm sẽ khóa nút Publish.

### 6.1 Tổng điểm: 100 điểm (Cố định)

| Block / Nhóm | Điểm tối đa | Ghi chú |
|---|---|---|
| **Block 1 - Technical SEO & CWV** | **25** | Nền tảng kỹ thuật và hiệu năng bắt buộc. |
| **Block 2 - On-Page SEO** | **55** | Tối ưu hóa nội dung hiển thị và từ khóa. |
| **Block 3 - GEO & Entity Signals** | **20** | Tín hiệu cấu trúc dữ liệu cho AI Search. |
| **Tổng** | **100** | |

### 6.2 Ngưỡng Publish (Hard Gate)

| Case | Trạng thái | Điều kiện | Behavior của Nút Publish |
|--------|-----------|-----------|----------|
| **CASE 1** | **Blocked** | Vi phạm bất kỳ 1 lỗi `Hard Block` HOẶC Tổng điểm < 60 | `Disabled` hoàn toàn |
| **CASE 2** | **Warning** | Pass toàn bộ `Hard Block` VÀ Tổng điểm 60-79 | `Enabled` (Hiển thị badge "⚠ Cần tối ưu") |
| **CASE 3** | **Pass** | Pass toàn bộ `Hard Block` VÀ Tổng điểm ≥ 80 | `Enabled` (Trạng thái "Tốt") |

---

## 7. Chi tiết Checklist & Logic Tính Toán (Dành cho Editor & Dev)

### 7.1 Block 1: Technical SEO & Core Web Vitals (25 Điểm)
*Các yếu tố nền tảng để Googlebot thu thập dữ liệu và trải nghiệm người dùng.*

| # | Hạng mục | Điểm | Hard Block | Giải thích cho Editor | Thuật toán Tính toán (Computation for Dev) |
|---|----------|------|------------|-----------------------|-----------------------------------------|
| 1.1 | **Canonical Tag** | 5 | NO | Phải trỏ đúng URL chuẩn. | Parse `<head>` tìm `<link rel="canonical" href="...">`. Khớp giá trị `href` với URL thực tế. |
| 1.2 | **Robots Meta** | 5 | **YES** | Cho phép Google Bot đọc trang. | Parse `<head>` tìm `<meta name="robots">`. Giá trị bắt buộc chứa `index, follow`. |
| 1.3 | **CWV: LCP** | 5 | NO | Thời gian tải nội dung chính ≤ 2.5s. | Trigger API gọi Google PSI (thông qua Signed URL). Lấy `largest-contentful-paint`. Trả Fail nếu `> 2.5s`. |
| 1.4 | **CWV: INP** | 5 | NO | Độ trễ tương tác ≤ 200ms. | Lấy trường `interaction-to-next-paint` từ PSI. Trả Fail nếu `> 200ms`. |
| 1.5 | **CWV: CLS** | 5 | NO | Điểm giật lag Layout ≤ 0.1. | Lấy trường `cumulative-layout-shift` từ PSI. Trả Fail nếu `> 0.1`. |

---

### 7.2 Block 2: On-Page SEO (55 Điểm)
*Tối ưu hóa trực tiếp trên nội dung bài viết.*

| # | Hạng mục | Điểm | Hard Block | Giải thích cho Editor | Thuật toán Tính toán (Computation for Dev) |
|---|----------|------|------------|-----------------------|-----------------------------------------|
| 2.1 | **Primary Keyword** | 10 | **YES** | Từ khóa chính không được trống. | Lấy array `keywords[0]`. Trả Fail nếu `length == 0` hoặc `< 2 chars`. |
| 2.2 | **Call-to-Action** | 5 | NO | Phải có ít nhất 1 nút bấm (W2A). | Trong Editor, track button component. Fallback: tìm `data-cta="true"` hoặc `<a class="momo-btn">`. |
| 2.3 | **H1 Tag** | 8 | NO | 1 thẻ H1 duy nhất, chứa từ khóa. | Đếm `<h1/>` trong body (`count == 1`). Dùng Regex `/keyword/i` check string bên trong thẻ. |
| 2.4 | **Meta Title** | 5 | NO | Độ dài 40-60 ký tự. | Đếm length của field Meta Title. Phải nằm trong Range `[40, 60]`. |
| 2.5 | **Meta Description** | 5 | NO | Độ dài 120-160 ký tự. | Đếm length của field Meta Description. Nằm trong Range `[120, 160]`. |
| 2.6 | **Wordcount** | 6 | NO | Độ dài text đủ chuẩn. | Strip HTML tags, split text bằng khoảng trắng. Trả Pass nếu length ≥ 800 (Mini-web) hoặc ≥ 300 (Landing). |
| 2.7 | **Keyword Density** | 8 | NO | Mật độ từ khóa chính 1-2%. | Đếm tổng keyword (regex `/\bkeyword\b/gi`) chia cho Wordcount tổng. Nằm trong `[0.01, 0.02]`. |
| 2.8 | **Image Alt Text** | 4 | NO | Ảnh có text chú thích. | Tìm thẻ `<img>`. Pass nếu 100% các thẻ có `alt` và length > 0. |
| 2.9 | **Encoding Error** | 4 | NO | Không lỗi font Tiếng Việt. | Regex check ký tự `/?|□/` do unicode lỗi. Trả Pass nếu count == 0. |

---

### 7.3 Block 3: GEO & Entity Signals (20 Điểm)
*Tối ưu hóa dữ liệu cấu trúc cho AI Search.*

| # | Hạng mục | Điểm | Hard Block | Giải thích cho Editor | Thuật toán Tính toán (Computation for Dev) |
|---|----------|------|------------|-----------------------|-----------------------------------------|
| 3.1 | **Schema JSON-LD** | 6 | NO | Khai báo chuẩn dữ liệu. | Regex tìm `<script type="application/ld+json">`. `JSON.parse` content, check tồn tại `@type`. |
| 3.2 | **Internal Links** | 5 | NO | Liên kết chéo về MoMo. | Parse `href` của `<a>`. Pass nếu có URL chứa `momo.vn`. |
| 3.3 | **Social Meta (OG)** | 4 | NO | Share Facebook/Zalo chuẩn. | Parse `<head>` tìm `meta property="og:..."`. Pass nếu đủ `title`, `description`, `url`, `image`. |
| 3.4 | **Fact Density** | 5 | NO | Tối thiểu 3 số liệu (%, tỷ, triệu). | Regex `/\b(\d+(?:\.\d+)?)\s*(%|triệu|tỷ|VNĐ)\b/g`. Đẩy mảng ra Modal UI. Editor xác nhận -> Pass. |

> **Quy tắc Scale điểm Block 3:** 
> - **Trang Blog & Mini Web:** Áp dụng toàn bộ (20đ).
> - **Trang Landing Page & Merchant Page:** Bỏ qua kiểm tra `3.4 Fact Density`. Backend tự Scale điểm: `Block3_Score = (Điểm_Thực_Đạt / 15) * 20` (Làm tròn toán học).

---

## 8. CWV Integration - Performance Tooling (Offline)

### Lý do tích hợp
Core Web Vitals (LCP, INP, CLS) là yếu tố xếp hạng quan trọng của Google. Mặc dù không còn bị xem là **Hard Block** để tránh gây khó khăn cho Editor, nhưng điểm số sẽ bị trừ rất nặng nếu tải trang chậm, khiến bài viết khó đạt ngưỡng "Tốt" (≥ 80 điểm). Việc tích hợp công cụ đo đạc tại bước này giúp phát hiện Regression Layout trước khi trang Live.

### Implementation Method (Draft Signed URL)
- Vì trang đang ở chế độ Draft (chưa Live), có cơ chế Auth bảo vệ, Google PageSpeed Insights (PSI) API không thể truy cập trực tiếp URL.
- **Giải pháp (Bypass Auth):** 
  1. Khi user click `Run CWV Check`, Backend cấp tốc sinh ra 1 Temporary Signed URL (Ví dụ: `momo.vn/draft/abc?token=xyz...`) cho phép bypass Authentication, TTL (Time-to-live) là 3 phút.
  2. Backend call Google PSI API với URL này.
  3. Nhận kết quả Lab Data và render về Score Panel. Hết 3 phút Token tự hủy.
- **Reset State:** Cứ mỗi lần Editor ấn `Save Draft` (làm thay đổi nội dung), điểm số CWV tự động reset về `0` (Trạng thái "Chưa kiểm tra"). Editor buộc phải `Run CWV Check` lại trước khi Publish.

---

## 9. UI Requirements (Score Panel)

Score Panel tích hợp trực tiếp bên dưới các trường nhập liệu SEO, phản ánh đúng cấu trúc Technical, On-Page và GEO.

```text
┌──────────────────────────────────────────────┐
│  SEO/GEO Score                               │
│                                              │
│  ████████████████░░░░  78/100                │
│  Status: ⚠ WARNING - Cần tối ưu thêm         │
│                                              │
│  ▼ Block 1 - Technical SEO (10/25) ⚠          │
│    [✗] Core Web Vitals (LCP chậm)            │
│    [✓] Canonical & Robots hợp lệ (Bắt buộc)  │
│                                              │
│  ▼ Block 2 - On-Page SEO (43/55)  ⚠          │
│    [✓] Có Primary Keyword (Bắt buộc)         │
│    [✓] Có Call-to-Action                     │
│    [✓] H1 chứa từ khóa                       │
│    [✗] Meta Title & Description chưa chuẩn   │
│    [✓] Độ dài nội dung (Wordcount)           │
│    [✓] Mật độ từ khóa (Density)              │
│    [✗] Thiếu Alt Text hình ảnh               │
│                                              │
│  ▼ Block 3 - GEO & Entity (10/20) ⚠          │
│    [✓] Schema JSON-LD                        │
│    [✓] Internal Links                        │
│    [✗] Thiếu Social Meta (OG Tags)           │
│    [✗] Fact Density (Thiếu số liệu)          │
│                                              │
│  [Run CWV Check]                             │
│                                              │
│  [Save Draft]          [⚠ Publish - Warning] │
└──────────────────────────────────────────────┘
```
> **Trường hợp Hard Block Fail:** UI progress bar chuyển sang màu Đỏ. Hiển thị dòng Text: `🛑 Bị chặn: Vi phạm [Tên Lỗi]. Vui lòng khắc phục!`. Nút Publish bị mờ (Disabled).

---

## 10. Technical Notes & API Hooks (Dành cho Trọng)

- **Integration Target:** Toàn bộ logic Block và CWV Check áp dụng chung cho cả `Blog Editor` và `Merchant Editor`. Khác biệt duy nhất nằm ở hàm Scale điểm Block 3.
- **Trigger Event:** Score Calculator sẽ tự động chạy ngầm mỗi khi user nhập text xong (Debounce 2s) đối với các lỗi On-Page và GEO (trừ CWV).
- **Publish Hook Gate:** Backend chỉ mở API Endpoint `/api/v1/publish` nếu check database (hoặc Redis Session) thỏa mãn: `Hard_Blocks_Failed == 0`. Nếu front-end bypass mở khóa nút Publish bằng inspect element, request bắn lên Backend vẫn sẽ trả mã lỗi `403 Forbidden` kèm thông báo chặn Publish.

---

## 11. Giải thích Thuật ngữ (Glossary)

| Thuật ngữ | Giải thích |
|-----------|-----------|
| **Hard Block** | Điều kiện chặn cứng - nếu item này fail, nút Publish bị vô hiệu hóa hoàn toàn, bất kể tổng điểm bao nhiêu. |
| **Draft** | Bản nháp - trạng thái trang đã được lưu nhưng chưa live, chưa ảnh hưởng trang đang chạy. |
| **Publish** | Hành động đưa trang mới lên live lần đầu tiên. |
| **Score Panel** | Bảng chấm điểm SEO/GEO tích hợp trong MoSpark Admin. |
| **CWV (Core Web Vitals)** | Bộ 3 chỉ số hiệu năng trang web cốt lõi của Google: LCP, INP, CLS - ảnh hưởng trực tiếp đến thứ hạng tìm kiếm. |
| **LCP** | Largest Contentful Paint - thời gian tải phần nội dung lớn nhất hiển thị lên màn hình. Ngưỡng tốt: ≤ 2.5s. |
| **INP** | Interaction to Next Paint - thời gian phản hồi khi người dùng tương tác (click, gõ phím). Ngưỡng tốt: ≤ 200ms. |
| **CLS** | Cumulative Layout Shift - mức độ giật layout bất ngờ khi trang tải. Ngưỡng tốt: ≤ 0.1. |
| **FCP** | First Contentful Paint - thời gian xuất hiện nội dung đầu tiên. Ngưỡng tốt: ≤ 1.8s. |
| **TTFB** | Time to First Byte - thời gian server phản hồi byte đầu tiên. Ngưỡng tốt: ≤ 800ms. |
| **SEO** | Search Engine Optimization - tối ưu hóa để trang được tìm thấy trên Google và các công cụ tìm kiếm. |
| **GEO** | Generative Engine Optimization - tối ưu hóa để nội dung được trích dẫn bởi AI (ChatGPT, Perplexity, Google AI Overviews). |
| **E-E-A-T** | Experience, Expertise, Authoritativeness, Trustworthiness - bộ tiêu chí Google dùng để đánh giá chất lượng nội dung. |
| **YMYL** | Your Money Your Life - nhóm nội dung nhạy cảm (tài chính, sức khỏe, pháp lý) bị Google đánh giá khắt khe hơn. |
| **Canonical tag** | Thẻ HTML khai báo URL "chính thống" của trang, giúp Google không bị confuse khi có nhiều URL tương tự. |
| **Robots meta** | Thẻ HTML chỉ định Google có được phép crawl và index trang hay không. Giá trị chuẩn: `index, follow`. |
| **DOM** | Document Object Model - cấu trúc HTML được dựng lên trong trình duyệt. System "parse DOM" nghĩa là đọc và phân tích cấu trúc HTML đó. |
| **JSON-LD** | JavaScript Object Notation for Linked Data - định dạng khai báo Schema (dữ liệu có cấu trúc) trong thẻ `<script>` của trang. |
| **Schema / Structured Data** | Dữ liệu có cấu trúc - thông tin được đánh dấu theo chuẩn Schema.org để AI và Google hiểu rõ nội dung trang hơn. |
| **SERP** | Search Engine Results Page - trang kết quả tìm kiếm của Google. |
| **GSC** | Google Search Console - công cụ miễn phí của Google để theo dõi hiệu suất tìm kiếm và phát hiện lỗi kỹ thuật. |
| **Orphan page** | Trang mồ côi - trang không được link đến từ bất kỳ trang nào khác trên site, Googlebot khó tìm thấy. |
| **Fact Density** | Mật độ số liệu - mức độ xuất hiện của số liệu, thống kê, dữ kiện cụ thể trong nội dung. AI engine ưu tiên trích dẫn nội dung có fact density cao. |
| **Topical Authority** | Thẩm quyền chủ đề - mức độ Google/AI đánh giá một site là nguồn đáng tin cậy về một chủ đề cụ thể. |
| **Disclaimer** | Tuyên bố từ chối trách nhiệm - đoạn văn bắt buộc trên nội dung tài chính, nhắc người đọc rằng nội dung chỉ mang tính thông tin, không phải tư vấn đầu tư. |
| **Lab data** | Dữ liệu đo lường trong môi trường kiểm soát (Lighthouse headless) - đo trên máy chủ, không phải dữ liệu thực từ người dùng. |
| **Field data** | Dữ liệu thực tế từ người dùng thật (Chrome UX Report) - chính xác hơn lab data nhưng chỉ có với trang đã có traffic. |
| **Signed URL** | URL tạm thời có gắn token bảo mật, cho phép truy cập trang Draft không cần đăng nhập trong thời gian giới hạn. |
| **Headless Chrome** | Trình duyệt Chrome chạy không có giao diện (ẩn), dùng để tự động hóa việc mở trang và đo hiệu năng trên server. |
| **Internal link** | Liên kết nội bộ - link từ một trang trên momo.vn trỏ đến một trang khác cũng trên momo.vn. |

---

## 12. Change Log

- **v2.0 (2026-06-01):** Tái cấu trúc (Re-architect) hoàn toàn mô hình điểm từ dạng Blocks sang dạng Tiers (Mandatory -> Basic -> Advanced). Nhúng thẳng thuật toán Computation Logic vào bảng để Tech Team làm Spec API.


- **v1.3.1 (2026-06-01):** Di chuyển Bảng Thuật Ngữ (Glossary) xuống cuối trang, trước Change Log, để ưu tiên luồng đọc Workflow và Input Model lên trên. Re-number các Heading tương ứng.
- **v1.3 (2026-06-01):** Chuẩn hóa toàn bộ cấu trúc tài liệu theo template của `mospark_genai_content.md`. Phục hồi các phần cốt lõi: Executive Summary, Stakeholders, và Bài toán cần giải. Re-format Headers và Bullet points.
- **v1.2 (2026-06-01):** Bổ sung chi tiết toàn bộ các quy chuẩn từ bản gốc: Bảng thuật ngữ, Input Model Validation, Chi tiết CWV Integration, Technical Notes cho Dev và Hard Block Summary.
- **v1.1 (2026-05-31):** Tái cấu trúc format presentation chuẩn hóa theo template của MoSpark GenAI Content Engine. Gom nhóm Header, Executive Summary, Roadmap và Tài liệu liên kết.
- **v1.0 (2026-04-15):** Khởi tạo tài liệu MVP Checklist.

---
*Maintained by: Văn Hiến (Web Product Lead) | Last updated: 2026-06-01*
