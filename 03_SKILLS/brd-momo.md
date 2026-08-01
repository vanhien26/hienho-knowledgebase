# MoMo BRD Skill - CEO Standard

## Mục Tiêu

Từ 3 input (Business Context + Keyword Research CSV + Direction brief), skill khai thác đủ context để viết BRD hoàn chỉnh theo CEO standard. BRD phục vụ: PO, Eng Lead, Stakeholder/Management.

**BRD là tài liệu chiến lược - định nghĩa WHY và WHAT, không phải HOW.**

| BRD trả lời | BRD KHÔNG trả lời |
|---|---|
| Vấn đề là gì? (Problem Framing) | Thực hiện như thế nào? (Action Plan) |
| User đang cần làm gì? (JTBD) | Rủi ro khi execute ra sao? (Risk Assessment) |
| Product job cốt lõi là gì? | Event tracking cụ thể thế nào? (PRD) |
| Đo thành công bằng gì? | Content plan TOFU/MOFU/BOFU |
| Cần gì để build? (Dependencies) | AB Test design ra sao? |

Hỗ trợ **2 loại dự án:**
- **Use Case** (Vay Nhanh / Cinema / BHYT) - acquisition-focused, content-heavy
- **Project** (Merchant Page / CMS feature) - product/platform, limited scope

---

## I. CEO Standards - Tiêu Chuẩn Bắt Buộc

### 1. Elegant Problem Framing

#### Problem Statement Block

Bắt buộc ngay sau header metadata, trước Executive Summary.

```markdown
> **Problem:** [1-2 câu - bất kỳ ai đọc cũng đồng ý ngay]
> **KPI Owned:** [Metric MoMo cam kết own] → attributed via [Tool]
> **Conversion Flow:** [Search trigger] → [URL] → [Action] → [App open] → [Transaction]
```

**Nguyên tắc viết Problem:**
- Mô tả user experience problem, không phải business problem
- Ai đọc cũng gật đầu ngay - không cần giải thích thêm
- KHÔNG bắt đầu bằng số liệu, không list data ngay trong problem statement
- Define WHAT trước HOW

| Sai | Đúng |
|---|---|
| "MoMo cần tăng traffic organic và W2A để đạt KPI Q2 cho vertical BH xe máy." | "72 triệu xe máy bắt buộc có bảo hiểm nhưng không ai biết có thể mua trong 3 phút trên điện thoại." |
| "Dự án nhằm capture search traffic DVC để tăng install." | "Hàng triệu người search thủ tục hành chính mỗi ngày - không fintech nào đang serve intent này trên web." |

#### Executive Summary - S-C-R Format

**Situation:** User experience problem hiện tại. Bắt đầu bằng người dùng, không bắt đầu bằng MoMo hay số liệu thị trường.

**Complication:** Tại sao problem này tồn tại / tại sao khó giải quyết / tại sao urgent. Honest về constraints - không che giấu.

**Resolution:** Product job cốt lõi trong 2-3 câu. Business outcomes là phần phụ theo sau. Product job drives outcomes - không phải ngược lại.

**Giới hạn:** Toàn bộ S-C-R không quá 400 từ.

---

### 2. PLG - Product-Led Growth

#### Xác định PLG Hook

Mỗi BRD phải trả lời: **Product này có PLG hook không?**

PLG hook là tính năng khiến user tự convert mà không cần campaign hay push.

| Use Case | PLG Hook |
|---|---|
| Giá Vàng | Price Alert - user muốn tính năng → tự login MoMo |
| Merchant Page | VTS badge - user xác nhận quán nhận VTS → tự kích hoạt |
| Phạt Nguội | Widget tra cứu - user dùng xong → CTA nộp phạt |
| Vay Nhanh | Loan Calculator - user tính xong → CTA apply |

Nếu không có PLG hook tự nhiên → ghi rõ trong Section 3 và đề xuất W2A conversion path thay thế.

**Phân biệt PLG vs Campaign:**
- PLG: User convert vì product solves their job
- Campaign: User convert vì được push / incentivize

#### Product Job Cốt Lõi

Bắt buộc trong Section 3 - Định Hướng Dự Án.

**Format:** `[User làm gì] - [User nhận được gì] - [Điều gì xảy ra tiếp theo].`

| Sai | Đúng |
|---|---|
| "Dự án tăng organic traffic, W2A và acquire new users." | "User search thủ tục hành chính - tìm thấy MoMo - nhận đủ thông tin để hành động - mở App." |
| "Xây dựng cluster bảo hiểm để phủ 7 keyword clusters." | "User cần BH xe máy tìm thấy thông tin giá, tra cứu hạn trong 1 trang - mua xong trong 3 phút." |

Business outcomes là phần tiếp theo ("N outcomes phát sinh:"), KHÔNG phải phần chính.

---

### 3. User-Centric / Product Safety

#### Value Before Gate

User PHẢI nhận value trước khi được yêu cầu login hoặc convert.

| Đúng | Sai |
|---|---|
| Widget giá vàng xem được không cần login; login chỉ để cài price alert | Yêu cầu login để xem bảng giá |
| Tra cứu phạt nguội không cần tài khoản; nộp phạt mới cần mở App | Redirect thẳng sang App khi user mới vào trang |
| Widget tra cứu BH miễn phí; gia hạn BH mới cần vào App | Ẩn kết quả tra cứu sau login wall |

#### YMYL Standards

Bắt buộc với content tài chính, pháp luật, bảo hiểm, sức khỏe:
- Author byline hoặc "Reviewed by" có chức danh chuyên môn
- Cite nguồn chính thống với tên cụ thể (Nghị định 168/2024/NĐ-CP, không phải "theo nghị định")
- Ngày cập nhật visible (dd/mm/yyyy)
- KHÔNG dùng ngôn ngữ "khuyến nghị đầu tư" hay tư vấn tài chính cá nhân
- Legal review bắt buộc trước publish với mọi số liệu pháp lý

#### Pre-conditions Gate

Nếu có điều kiện PHẢI giải quyết trước khi build → đưa vào **Pre-conditions Gate** trong Section 3, KHÔNG phải Risk Assessment.

```markdown
### Pre-conditions - Phải Giải Quyết Trước Khi Commit Build

**Thiếu 1 trong [N] - dừng lại.**

| # | Pre-condition | Trạng thái | Owner giải quyết |
|---|---|---|---|
| P1 | [Điều kiện] | Chưa giải quyết | [Owner] |
```

**Pre-condition khác Risk:** Pre-condition = không có thì KHÔNG build. Risk = điều có thể xảy ra trong lúc build.

---

## II. Cấu Trúc BRD

### Sections Bắt Buộc

```
[Header Metadata]
[Problem Statement Block]
---
1. Executive Summary (Situation - Complication - Resolution)
2. Bối Cảnh Thị Trường
3. Định Hướng Dự Án (Product Job Cốt Lõi + KHÔNG phải + Pre-conditions nếu cần)
4. JTBD Analysis
5. Kiến Trúc Web / Phạm vi Build
6. Success Metrics (North Star + Tier B)
7. Dependencies & Constraints
[Change Log]
```

### Sections KHÔNG Được Có Trong BRD

| Section | Thuộc về |
|---|---|
| Risk Assessment | PRD / Action Plan |
| Tracking Event Schema | PRD / Action Plan |
| AB Test Hypothesis | PRD / Action Plan |
| Content Matrix (TOFU/MOFU/BOFU) | Action Plan |
| Keyword detail Tier 3+ | File keyword research riêng |
| Cross-sell Matrix | Action Plan |
| Data Verification Checklist | Action Plan / SOP |
| Next Steps / Deliverables | Action Plan |

---

### Header Metadata Format

```markdown
> - **Project:** [Tên dự án]
> - **Main URL:** [URL chính]
> - **Division:** [GPD / FS / etc.]
> - **Owner:** GPD - Web Platform
> - **Governance:** Web Product Lead
> - **Version:** [X.Y · Tháng MM/YYYY]
> - **Status:** [Draft / Active / On Track / LIVE / Chờ pre-conditions]
> - **Business Model:** [Chỉ thêm nếu cần làm rõ]
```

**Version numbering:**
- Thêm/xóa section, sửa nhỏ → bump minor (1.1 → 1.2)
- Rewrite Executive Summary, Product Job, thay đổi KPI → bump major (1.x → 2.0)

---

### Section 1: Executive Summary

Viết theo cấu trúc **S-C-R (Situation - Complication - Resolution)**.

- **Situation:** User experience problem hiện tại. Bắt đầu bằng người dùng, không phải số liệu thị trường.
- **Complication:** Vấn đề cốt lõi. Tại sao hiện trạng chưa đủ? Gap là gì?
- **Resolution:** Product job cốt lõi trong 2-3 câu. Business outcomes là kết quả phụ.

*Giữ trong 3-5 đoạn. Stakeholder đọc đầu tiên - phải đủ sharp để hiểu toàn bộ Why.*

---

### Section 2: Bối Cảnh Thị Trường

Evidence cho Complication. Bao gồm:
- **Hiện trạng:** Table mô tả trạng thái hiện tại
- **Market size / Search demand:** Cluster-level, không keyword-level chi tiết
- **Competitive landscape:** Đối thủ đang làm gì? Gap là gì?
- **Trend / Seasonality (nếu relevant)**

*Mọi số liệu phải có nguồn hoặc ghi "[cần verify]".*

---

### Section 3: Định Hướng Dự Án

**3.1 Product Job Cốt Lõi**

2-3 câu từ góc nhìn user. Theo sau là N outcomes phát sinh (không phải primary motivations).

**3.2 Dự Án Này KHÔNG Phải**

Out of scope explicit. Quan trọng để tránh scope creep. Phải cụ thể, không mơ hồ.

**3.3 Pre-conditions Gate** *(chỉ thêm khi có hard blockers)*

Điều kiện phải giải quyết trước khi commit build. Thiếu 1 → dừng lại.

**3.4 KPI Framework** *(Use Case)*

Phân biệt lane Utility (MEU) vs Payment (MAU) nếu relevant.

---

### Section 4: JTBD Analysis

Từ keyword clusters, extract 3-6 Jobs có volume/impact cao nhất.

**Format chuẩn:**

```markdown
### Job #N: [Tên Job ngắn gọn]

> "[Quote mô tả nhu cầu user, viết ngôi thứ nhất]"

| Dimension | Nội dung |
|---|---|
| Functional | [User cần làm gì cụ thể] |
| Emotional | [Cảm xúc / lo lắng / mong muốn] |
| Social | [Áp lực xã hội / bối cảnh quan hệ] |
| Trigger | [Điều gì khiến user search ngay lúc đó] |
| Search → App | "[Query đại diện]" → [Page] → [Action] → App MoMo |

**Giải pháp:** [URL hoặc tính năng sẽ serve job này]
```

**Search → App là mandatory.** Map rõ hành trình từ discovery đến conversion. Thiếu = thiếu link giữa SEO strategy và product conversion.

**"Bữa tối test" (CEO):** Dimension Social phải đủ cụ thể để user kể lại cho gia đình.
- Tốt: "Anh cài alert trên MoMo, vàng lên 110 triệu rồi em ơi."
- Không đủ: "Muốn chia sẻ thông tin với người thân."

**Công thức extract JTBD từ Keyword:**
1. Lấy high-volume keyword cluster (≥500/month)
2. Analyze search intent: "người search từ này cần gì?" (functional) + "tại sao tìm?" (trigger)
3. Infer emotional/social từ context (product category, user segment)
4. Write job statement ngôi thứ nhất

**Số lượng JTBD:** 3-6 jobs. Ưu tiên high-volume clusters (80/20 rule).

---

### Section 5: Kiến Trúc Web / Phạm Vi Build

**Use Case (Content-heavy):**
- Sitemap Hub & Spoke: URL architecture, content cluster
- URL Architecture table: Cluster, URL, Ghi chú
- Component anatomy nếu có Hub page
- Schema requirements (FAQPage, HowTo, LocalBusiness, etc.)

**Project (Product/Feature):**
- User Flow: Entry point, main screens, conversion point
- Feature List với priority P1/P2/P3

**Priority rules:** P1 = launch blocker. P2 = quan trọng nhưng không block. P3 = nice-to-have.

---

### Section 6: Success Metrics

**North Star Metric:**
- Chỉ 1 metric duy nhất đo business value thực sự
- Phải trace được về New User / MAU / Revenue
- Phải có target cụ thể, kể cả "TBD post pilot [date]" - không được "TBD" không có timeline

**Tier B - Leading Indicators:**

Organic sessions, keyword ranking, W2A rate = Tier B, không phải North Star. Trừ khi business model là pure traffic play đã được leadership align.

**KPI Alignment Note:**

Nếu North Star của dự án KHÁC với metric leadership thường hỏi → ghi rõ alignment note.

Ví dụ: "KPI chính là Price Alert Sign-ups, không phải W2A. W2A sẽ thấp do intent bridge indirect - đây là đặc tính của use case. Cần align với leadership trước khi launch."

**Format:**

```markdown
| Metric | Lane | Target | Timeframe | Tracking |
|---|---|---|---|---|
| [North Star] | [Utility/Payment] | [Giá trị] | [Timeline] | [Tool] |
| Organic sessions | Tier B | [Giá trị] | [Timeline] | GSC → GA4 |
| W2A end-to-end | Tier B | [%] | [Timeline] | GA4 + Appsflyer |
```

---

### Section 7: Dependencies & Constraints

```markdown
| Dependency | Mô tả | Blocker? | Status |
|---|---|---|---|
```

**Phân biệt:**
- **Hard dependency** (Blocker = Có): Không có → không launch được
- **Soft dependency** (Blocker = Không): Không có → có fallback hoặc defer
- **Constraints:** Giới hạn không thể thay đổi (pháp lý, brand, kỹ thuật)

**Constraints section:** List dưới bảng dependency dưới dạng bullet points.

---

### Change Log Format

```markdown
## Change Log
- **Tháng MM/YYYY (vX.Y):** [Mô tả thay đổi - không quá 1 dòng]
```

Giữ tối đa 5 entries gần nhất.

---

## III. Workflow (3 Bước)

### Bước 1: Xác định Input & Project Type

Trước khi hỏi user, kiểm tra conversation đã có:
- **File upload?** HTML / Slide / Doc / CSV → Đọc trước, extract thông tin
- **Text brief?** → Extract Business Context từ đó
- **Keyword CSV?** → Kiểm tra format (keyword, search volume, difficulty, intent...)

**Xác định Project Type:**
- **Use Case:** Vay Nhanh / Cinema / BHYT → acquisition-focused, SEO/GEO strategy, content hub
- **Project:** Merchant Page / CMS feature / Tool → limited scope, product-driven

---

### Bước 2: Khai Thác Thông Tin

Sau khi đọc input, xác định gap. Hỏi **tối đa 1 lần**, gom tất cả vào 1 message.

| Nhóm | Thông tin | Cách khai thác |
|---|---|---|
| **Identity** | Tên use case, URL, Owner, Timeframe | "Tên dự án? URL chính? Owner? Timeframe?" |
| **Business Context** | Value prop, user target, hiện trạng, vấn đề cốt lõi | "Value prop là gì? Ai dùng? Baseline current state?" |
| **Keyword Research** | CSV file gồm keywords + volume | "CSV có gồm keyword, search volume, intent hint không?" |
| **Direction Brief** | Chiến lược, scope muốn build, KPI target | "Chiến lược là gì? Build cái gì? Target KPI?" |
| **PLG Angle** | Có PLG hook không? User tự convert bằng cách nào? | "Tính năng nào khiến user tự vào App mà không cần push?" |
| **Pre-conditions** | Có blocker cứng nào phải giải quyết trước? | "Có dependency nào không có thì không nên build không?" |

**Không hỏi những gì đã có trong input. Chỉ hỏi gap.**

---

### Bước 3: Process & Viết BRD

**Nếu user cung cấp Keyword CSV:**

1. **Ingest CSV** → Extract: keyword, search volume, intent hint
2. **Cluster keywords** theo intent:
   - Know intent: "là gì", "định nghĩa", "cách", "hướng dẫn"
   - Do intent: "cách làm", "bước", "tutorial"
   - Go intent: brand name, "trang web", "ứng dụng"
   - Buy intent: "giá", "mua", "vay", "bảo hiểm", "so sánh"
3. **Map keyword clusters → JTBD** (3-6 Jobs, ưu tiên high-volume clusters)
4. **Xác định PLG hook** từ product category + keyword context
5. **Viết theo thứ tự:** Problem Block → S-C-R → Market Context → Product Job → JTBD → Architecture → Metrics → Dependencies

**Viết BRD với cấu trúc theo project type:**
- **Use Case:** Sections 1-7 đầy đủ
- **Project:** Sections 1-7 rút gọn (shorten JTBD nếu scope nhỏ)

**Không được đưa vào BRD:** Risk Assessment, Tracking Event Schema, AB Test, Content Matrix, Next Steps/Deliverables.

---

## IV. Quy Tắc Viết

### Tone & Format

- **Tiếng Việt chuyên nghiệp.** Giữ thuật ngữ kỹ thuật (SEO, JTBD, CTA, W2A, GSC, Appsflyer, P1...)
- **Senior-level, trực tiếp.** Không fluff, không mở đầu rườm rà. Mỗi câu phải có purpose.
- **Data-driven.** Mọi claim phải có source (GSC, Keyword research, competitor data)
- **Table > Prose.** Dùng table khi có 3+ items để so sánh hoặc list structured data

### Về Data & Metrics

- **Số liệu bắt buộc có nguồn:** GSC (organic traffic), Appsflyer (W2A), SEO tool (ranking)
- **Baseline & Target phải có logic rõ ràng.** Không đặt target random - phải explain tại sao
- **Nếu chưa có data → ghi rõ "[cần đo]" hoặc "[cần verify]".** Không hallucinate metrics.

### Về JTBD

- **JTBD phải anchor từ keyword research.** Không generic "user muốn trải nghiệm tốt"
- **Functional JTBD = gì mà user search?** Trigger JTBD = tại sao search lúc này?
- **Search → App flow là bắt buộc** cho mọi Job - map rõ từ query đến in-app action
- **Bữa tối test:** Social dimension đủ cụ thể để kể lại được

### Về Scope

- **Out of scope phải explicit, không mơ hồ.** Ví dụ: "KHÔNG build mobile app" không phải "KHÔNG cover mobile experience"
- **Nếu overlap với dự án khác → ghi rõ relationship và BRD riêng tương ứng**

---

## V. Edge Cases & Handling

| Tình huống | Xử lý |
|---|---|
| **Keyword CSV format không chuẩn** | Hỏi: "CSV có column nào? (keyword, volume, difficulty, intent?)" → Map vào standard format |
| **User không có baseline metrics** | Hỏi: "Có GSC access?" → Ghi "[cần measure]" + define tracking method |
| **Use Case NEW (chưa tồn tại)** | Baseline = 0 nhưng phải explain ramp strategy: "Expect ramp 3-6 months để reach target" |
| **Project quá nhỏ (1 page, 1 feature)** | Viết BRD rút gọn: shorten JTBD, giữ Problem Block + S-C-R + Dependencies |
| **Use Case quá lớn (toàn Finance cluster)** | Viết BRD cluster-level. Hoặc chia multi-BRD per sub-use-case |
| **User cung cấp slide + text + CSV mixed** | Đọc tất cả, extract thông tin, fill gaps. Không duplicate hỏi |
| **W2A funnel không setup sẵn** | Ghi trong Dependencies - note blocker level. Không giả định W2A là North Star |
| **Có hard blocker chưa giải quyết** | Đưa vào Pre-conditions Gate trong Section 3 |
| **User muốn thêm Risk Assessment** | "Risk Assessment thuộc PRD/Action Plan. Sẽ tách ra khi viết PRD." |
| **Seasonality / event impact lớn** | Flag trong Success Metrics - adjust target theo seasonality. Không đưa vào Risk |
| **Competitor có ranking cao, user không biết tại sao** | Suggest: "Analyze competitor content depth, freshness, backlinks → đưa vào Section 2" |

---

## VI. Output & Delivery

- **File format:** `.md` (Markdown)
- **File name:** `[use-case-name]-brd.md`
- **File location:** `/mnt/user-data/outputs/`
- **After creation:** Summary tối đa 5 dòng:
  - Tên file + Use Case / Project type
  - Số sections + keywords processed
  - PLG hook đã xác định (nếu có)
  - Điểm cần user verify / bổ sung
  - Recommend next step (PRD / Content Calendar / Tracking Setup)

**Never output BRD as:**
- Inline markdown trong chat (file quá dài, khó edit)
- HTML (dùng `.md`, user convert sau nếu cần)

---