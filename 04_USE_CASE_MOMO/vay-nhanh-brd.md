# 📄 Vay Nhanh Brd
Nhanh Web Growth 2026
## Business Requirements Document (SEO/GEO Project)

**Dự án:** Vay Nhanh Web Growth & Conversion Platform  
**URL Hub:** momo.vn/vay-nhanh  
**Division:** FS (Financial Services)  
**Use Case:** Loan  
**Product:** FS - Loan  
**SEO/GEO Project ID:** `vay-nhanh`  
**Prepared by:** Out-App Traffic (GPD) · Inbound Marketing
**Governance:** Văn Hiến (SEO & GEO Lead)  
**Last updated:** 08/05/2026  
**Status:** In Progress - Execution Phase  
**Effort allocation:** Hiền (Product Support) · Inbound - Ngọc Hạnh under Mai (SEO Execution) · Web Platform / BU / BMC

---

## Status - Tháng 4/2026

| Item | Status | Ghi chú |
|------|--------|---------|
| Keyword research (11,345 KWs) | ✅ Done | CSV confirmed · 3.22M addressable vol |
| GSC baseline KPI (Q1/2026) | ✅ Done | 70,533 clicks · 2.66% CTR · 2.64M impressions |
| Keyword ranking baseline | ✅ Confirmed | vay nhanh: #2 · vay tiền online: #3 · vay tiền: #2 |
| Ranking targets EOY 2026 | ✅ Confirmed | Top 1 toàn bộ 10 head terms |
| Simulator spec | 🟡 In Progress | Amortization + deep link spec chờ Web Platform |
| Sub-page briefs | 🔵 In Progress | Ngọc Hạnh đang clone Money Pages để BU input content |
| Backlink plan 2026 | ✅ Done | Budget confirmed · Vendor: Hapodigital |
| Onelink / Web-to-App tracking | ✅ Done | DA (Hải/Hoàng) đã setup GA4 events. Hiến observe và support |
| BU/Legal content approval flow | 🟠 Pending | Cần confirm SLA |
| CMS platform cho blog | 🟠 Pending | Web Platform cần confirm |

> **Critical path:** Simulator revamp và 6 sub-pages Wave 1 là blockers cho Q2 GSC target. Nếu không launch trước tháng 6/2026, click target Q2 (80,467) sẽ miss.

---

## Executive Summary

Vay Nhanh (momo.vn/vay-nhanh) là sản phẩm tín dụng tiêu dùng không thế chấp cốt lõi của MoMo, hoạt động trên nền lending license qua đối tác MCash. Sản phẩm đã live trên App nhưng **Web channel đang underperform nghiêm trọng:** traffic giảm liên tục từ đỉnh 159K views/tháng (Jun 2024) xuống còn 47K (Jan 2026), tương đương mức CTR sụt từ 5.73% (Jan 2025) xuống còn 2.74% (Jan 2026).

Trong khi đó, search demand toàn ngành vay không giảm - 4.22M searches/tháng, MoMo addressable pool là **3.22M vol/tháng** (loại ngân hàng, CTTC, noise). MoMo hiện chỉ capture khoảng **2.2% pool này.**

Dự án này có hai mục tiêu song song, không tách rời:

- **SEO/GEO:** Recover và vượt ranking - đạt Top 1 cho 10 head terms trước EOY 2026, expand sang 12 sub-pages mid-tail
- **PLG Conversion:** Revamp Simulator thành conversion engine thực sự - truyền context từ web vào app qua Onelink, giảm friction Web-to-App

Thành công được đo bằng **Clicks từ 70,533 → 98,908** (Q4/2026), CTR **2.66% → 3.61%**, và Web-to-App Click-to-App rate recover về mức 2024 (~45-48% của traffic).

---

## 1. Bối cảnh & Cơ hội

### 1.1 Traffic Decline Analysis

Đây là vấn đề cốt lõi cần hiểu trước khi action. Data từ Excel (sheet 4.1 KPI 2026):

**Trendline traffic (Views - GA4):**

| Period | Monthly Peak | Monthly Low | Trend |
|--------|-------------|-------------|-------|
| 2024 | 159,454 (Jun) | 49,292 (Feb) | Peak mùa hè, tháng Tết thấp |
| 2025 | 91,860 (Jan) | 42,446 (Nov) | **Giảm đều -52% từ đỉnh 2024** |
| 2026 | 47,140 (Jan) | 32,263 (Feb) | Tiếp tục giảm, baseline thấp |

**CTR decline (GSC):**

| Period | CTR | Ghi chú |
|--------|-----|---------|
| Nov 2024 | 5.94% | Điểm tốt nhất có data |
| Jan 2025 | 5.73% | Vẫn healthy |
| Jun 2025 | 2.84% | Giảm mạnh |
| Dec 2025 | 2.42% | Tiếp tục giảm |
| Jan 2026 | 2.74% | Baseline hiện tại |

**Hypothesis - 3 nguyên nhân khả dĩ:**
1. **AI Overview (AIO) cannibalization:** Từ May/2025 Google AIO tăng mạnh tại VN - click giảm dù impression ổn định/tăng. CTR giảm từ 5.73% → 2.74% trong 12 tháng là signal của AIO.
2. **Content stagnation:** Không có content mới, không có sub-pages - MoMo đang defend bằng domain authority thôi, không có content moat.
3. **Competitor content investment:** FE Credit, Home Credit, Doctordong đầu tư content sub-pages nhiều hơn MoMo trong 12 tháng qua.

### 1.2 Market Demand (từ CSV 11,345 keywords)

| Cluster | Vol/tháng | % Pool | MoMo Fit | Action |
|---------|-----------|--------|----------|--------|
| Vay (core) | 2,132,450 | 50.6% | ✅ Direct | Hub + sub-pages |
| Ứng dụng cho vay | 805,870 | 19.1% | ✅ Comparison | Blog comparison |
| Vay ngân hàng | 521,950 | 12.4% | ⚠️ Partial | Blog only |
| Nợ xấu / CIC | 326,600 | 7.7% | ⚠️ Informational | Blog CIC education |
| Công ty cho vay | 208,020 | 4.9% | ❌ Competitor | Skip |
| Định nghĩa + FAQ | 160,510 | 3.8% | ✅ TOFU/GEO | Blog + FAQ schema |
| Lãi suất vay | 90,850 | 2.2% | ✅ Calculator | Simulator SEO |
| MoMo branded | 46,940 | 1.1% | ✅ Navigational | Hub defend |
| **Total** | **4,218,610** | | | |
| **MoMo addressable** | **3,223,170** | | | (loại NH, CTTC, noise) |

**Volume distribution - implication cho sub-page strategy:**
- 46 head keywords = **1,548,700 vol (48%)** - priority số 1
- 496 mid-tail (1K–10K) = **1,296,200 vol** - 12 sub-pages + blog
- 8,305 long tail (<100 vol) - programmatic SEO, chưa ưu tiên

**Critical finding - Nợ xấu cluster bị misread:**
Tổng 326,600 vol nhưng **63% là informational** (check CIC, kiểm tra nợ xấu, cic.gov.vn). Chỉ có 8,770 vol (~3%) là transactional intent. Không build landing page vay ở đây - chỉ blog CIC education.

### 1.3 Competitive Landscape

**Brand search volume (từ CSV Market Overview):**

| Competitor | Brand vol/tháng | Điểm mạnh | Điểm yếu MoMo có thể exploit |
|-----------|-----------------|-----------|-------------------------------|
| Home Credit | 159,490 | Network, brand lớn | UX tệ, site chậm, content heavy |
| Doctordong | 128,940 | Digital-native, UX tốt | Không có hệ sinh thái app rộng |
| FE Credit | 98,790 | Volume content, 100+ landing pages | Mobile kém, không có super-app |
| Asset Credit | 67,510 | Lãi suất cạnh tranh | Brand nhỏ |
| **MoMo** | **65,240** | Super-app, 31M users, brand trust cao | Brand vol vay chỉ bằng 1/2 Home Credit |
| Mcredit | 51,970 | Agri/rural network | Digital yếu |

**MoMo chỉ cover 6% market share về Brand search** trong ngành vay - đây là structural gap dài hạn, không giải được bằng SEO content đơn thuần. Cần brand awareness investment song song.

**Ranking baseline hiện tại (T1/2026 → Target T12/2026):**

| Keyword | Vol | Position T1/2026 | Target T12/2026 |
|---------|-----|-----------------|-----------------|
| vay nhanh | 165,000 | **#2** | #1 |
| vay tiền online | 110,000 | **#3** | #1 |
| vay tiền nhanh | 60,500 | **#3** | #1 |
| vay tiền | 60,500 | **#2** | #1 |
| vay online | 60,500 | **#6** | #1 |
| vay online nhanh | 40,500 | **#3** | #1 |
| vay nhanh online | 22,200 | **#3** | #1 |
| vay tiền online nhanh | 12,100 | **#3** | #1 |
| vay tiền mặt | - | **#15** | #1 |
| vay trả góp | 27,100 | **#25** | #1 |

**Nhận xét:** MoMo đang ở #2-3 cho các head terms - đây là vị trí có thể push lên #1 trong 2026 nếu có content + authority investment. "Vay online" (#6) và "vay trả góp" (#25) là hai keyword cần effort lớn nhất.

### 1.4 International Benchmark

Nghiên cứu 4 đối thủ quốc tế để xác định best practice UX + GEO:

**Jiebei (借呗) - Ant Financial, China:**
- Integrated directly trong Alipay super-app - loan offer hiển thị dựa trên Sesame Credit score, không cần user chủ động apply
- Web landing page là educational, không phải conversion - vì người dùng đã trong app ecosystem
- **Implication cho MoMo:** User đã có tài khoản MoMo → web page nên focus vào "kiểm tra hạn mức" thay vì "apply vay" - lower commitment CTA

**Klarna - Buy Now Pay Later, EU:**
- Loan calculator là interactive element chiếm 50% viewport above fold
- Transparency là core design principle: hiển thị APR (Annual Percentage Rate) rõ ràng, không chỉ rate/tháng
- "No credit check for BNPL" - clear eligibility signal giảm anxiety
- **Implication cho MoMo:** Simulator phải hiển thị *tổng tiền trả* và *tổng lãi* rõ ràng - transparency = trust = conversion

**Kredivo - Indonesia:**
- Calculator embedded in hero, không cần scroll. "Approved in 5 minutes" ngay above fold
- Comparison table vs competitor giá trị cao với user đang research
- **Implication cho MoMo:** Simulator phải ở fold 1 trên mobile - đây là điểm quan trọng nhất hiện tại đang thiếu

**Tonik Bank - Philippines:**
- Dark card result panel tạo contrast mạnh - kết quả nổi bật hơn form input
- "Rate comparison table: vs Traditional Bank" - xây trust bằng transparency thay vì claim
- **Implication cho MoMo:** Result card design quan trọng hơn input form - user muốn thấy kết quả, không muốn nhập form

---

## 2. Problem Statement

### 2.1 User Problem

Người dùng tiêu dùng tại Việt Nam đang đối mặt với 4 vấn đề cốt lõi:

1. **Không biết mình có vay được không** - điều kiện từ ngân hàng và CTTC không minh bạch, nhiều người bị từ chối mà không hiểu lý do
2. **Không biết tổng chi phí thực sự** - lãi suất flat rate 2%/tháng nghe có vẻ thấp nhưng tổng trả cuối kỳ là bao nhiêu? Không có công cụ tính rõ ràng
3. **Không tin tưởng vào app vay online** - thị trường có nhiều app cho vay nặng lãi, scam, lộ data - user cần brand trust trước khi apply
4. **Friction cao khi chuyển từ research sang action** - user research trên Web nhưng phải vào App để apply, không có context carryover

### 2.2 Business Problem

Out-App Traffic team đang đối mặt với 3 vấn đề cùng lúc:

1. **Traffic decline:** -52% từ peak 2024, CTR giảm từ 5.73% → 2.74% - likely do AI Overview cannibalization và content stagnation song song
2. **Conversion gap:** Click-to-App rate từng đạt 48-52% của traffic (2024) nhưng nay không có baseline rõ ràng do thiếu event tracking
3. **Content architecture thiếu:** Chỉ có hub page - không có sub-pages theo segment, không có blog layer, không có GEO FAQ layer - không thể defend search demand expansion

---

## 3. Goals & Success Criteria

### 3.1 Business Goals

| Goal | Metric | Q1/2026 Baseline | Q4/2026 Target |
|------|--------|-----------------|----------------|
| Organic traffic growth | GSC Clicks | 70,533 | **98,908** (+40.2%) |
| CTR improvement | GSC CTR | 2.66% | **3.61%** (+0.95pp) |
| Impression pool | GSC Impressions | 2,648,592 | **2,738,777** (+3.4%) |
| Ranking TOM | Top 1 cho head terms | 0/10 keywords | **10/10** EOY 2026 |
| Web-to-App activation | Click-to-App / Traffic | ~42% (2025 avg) | **Recover 45%+** |
| Content scale | Sub-pages live | 0 | **12 sub-pages** |
| GEO layer | AI citation cho target queries | 0 | **5+ queries** cited |

### 3.2 North Star Metric

**Web-to-App Activated Users từ Organic** - đo qua Onelink clicks (GA4) được attributed từ momo.vn/vay-nhanh/*. Không phải traffic, không phải ranking - là user đến web, interact với Simulator, bấm Onelink.

### 3.3 Non-Goals (Ngoài scope dự án này)

- Loan underwriting decisions và credit policy - BU Credit Cell
- App UX flow sau khi user click Onelink - App PO
- SEM campaign management cho vay nhanh keywords - Media team
- Pricing và interest rate decisions - BU/Finance
- Paid influencer hoặc TikTok content - BMC

---

## 4. User Personas & JTBD

### Persona 1 - Emergency Borrower (BOFU · High urgency)

- **Who:** 25–40 tuổi, freelancer / công nhân / hộ kinh doanh nhỏ, cần tiền trong ngày
- **Job:** *"Khi tôi cần tiền gấp, tôi muốn vay online uy tín không cần đến ngân hàng, để giải quyết vấn đề ngay hôm nay."*
- **PUSH:** Ngân hàng yêu cầu hẹn 3-5 ngày · vay người thân ngại · app khác không tin tưởng
- **PULL:** MoMo duyệt 5 phút · chỉ cần CCCD · giải ngân vào ví ngay
- **ANXIETY:** Lãi suất thực sự bao nhiêu? · Có bị lộ data không? · Không trả được thì sao?
- **Content fit:** `/vay-nhanh/khan-cap` - Simulator fold 1, friction tối thiểu, trust strip NHNN

### Persona 2 - Comparison Researcher (MOFU)

- **Who:** 28–45 tuổi, có thu nhập ổn định, đang cân nhắc vay tiêu dùng, search Google để research
- **Job:** *"Khi tôi đang cân nhắc vay, tôi muốn hiểu rõ lãi suất và so sánh các lựa chọn, để ra quyết định mà không bị lừa."*
- **ANXIETY cao nhất:** "2.72%/tháng flat rate nghĩa là gì? Tổng tôi trả bao nhiêu?"
- **Content fit:** Blog "Lãi suất vay tiêu dùng tính thế nào" + Simulator với amortization schedule

### Persona 3 - Rejected Borrower / CIC Concerned (MOFU · Sensitive)

- **Who:** Đã bị ngân hàng từ chối hoặc lo ngại về CIC score của mình
- **Job:** *"Khi tôi không đủ điều kiện vay ngân hàng, tôi muốn biết còn lựa chọn uy tín nào, để vay mà không bị lợi dụng."*
- **YMYL red line:** Không claim "bỏ qua CIC" hay "hỗ trợ nợ xấu" nếu MoMo vẫn check CIC
- **Content fit:** Blog `/blog/cic-la-gi-kiem-tra-no-xau` → CTA sang Tra Cứu CIC trong app (không phải CTA vay)

### Persona 4 - First-time Digital Borrower (TOFU)

- **Who:** Lần đầu nghĩ đến vay online, chưa có kinh nghiệm, đang tìm hiểu
- **Job:** *"Khi tôi lần đầu muốn vay online, tôi muốn hiểu quy trình và trust platform, để vay mà không lo rủi ro."*
- **PULL:** MoMo brand quen từ thanh toán · App Store rating tốt · 31M users social proof
- **Content fit:** Blog "App vay tiền online uy tín 2026" → internal link về hub page

---

## 5. Product Scope

### 5.1 PLG Tool - Simulator Revamp (P0)

**Vấn đề với Simulator hiện tại:** Tính toán cơ bản, không có amortization, không có deep link context, không fold 1 trên mobile.

**Simulator v2.0 - Functional Spec:**

```
INPUT:
  - Số tiền vay: Slider 6M – 100M VNĐ
    Quick-select chips: 10tr / 20tr / 30tr / 50tr
  - Kỳ hạn: 6 / 9 / 12 / 15 / 18 / 24 tháng

LOGIC:
  - Flat rate: 2.72%/tháng (tham khảo, hiển thị disclaimer)
  - Monthly payment = Principal/Term + Principal × Rate
  - Amortization: từng tháng = gốc thực tế + lãi (reducing balance method cho accuracy)

OUTPUT (Result Card):
  - Tiền trả mỗi tháng (dominant display)
  - Tương đương X.XXXđ/ngày
  - Tổng tiền trả / Tổng tiền lãi
  - Pre-approval signal: "Bạn có thể đủ điều kiện - kiểm tra miễn phí"
  - CTA → Onelink với full context

OUTPUT (Amortization Table):
  - Collapsible toggle
  - Mỗi row: Tháng / Trả gốc / Tiền lãi / Tổng trả / Dư nợ còn lại

PRE-FILL LOGIC (từ sub-page URL param):
  /vay-nhanh/           → default: 20tr · 18th
  /vay-nhanh/khan-cap   → 10tr · 6th
  /vay-nhanh/sinh-vien  → 6tr · 15th
  /vay-nhanh/cong-nhan  → 10tr · 12th
  /vay-nhanh/chi-can-cmnd → 15tr · 12th
```

**Mobile requirement:** Simulator phải visible hoàn toàn ở fold 1 trên viewport < 600px. Không scroll để thấy Simulator. Đây là P0 blocker.

### 5.2 Deeplink Architecture - Onelink Integration

```
Onelink template: onelink.momo.vn/vay-nhanh (confirm với BU)

Format: onelink.momo.vn/vay-nhanh
        ?amount={amount}
        &term={term}
        &utm_source=web
        &utm_medium={page_type}
        &utm_campaign=vay-nhanh-2026
        &utm_content={sub-page-slug}

Page types: hub / spoke-cmnd / spoke-khan-cap / spoke-sinh-vien /
            spoke-cong-nhan / blog-cic / blog-lai-suat / simulator

Fallback:
  → New user: App Store (iOS) / Play Store (Android)
  → Existing user: Deep open /vay-nhanh feature trong app
  → Desktop: momo.vn/download QR
```

**GA4 Events cần setup (hiện đang thiếu hoàn toàn):**

| Event | Trigger | Properties |
|-------|---------|-----------|
| `simulator_amount_changed` | User kéo slider / click chip | amount, page_type |
| `simulator_term_changed` | User click kỳ hạn | term, page_type |
| `amortization_expanded` | User mở bảng amortization | page_type |
| `onelink_click` | User click CTA → Onelink | amount, term, page_type, cta_position |
| `sticky_cta_click` | Click sticky bar mobile | page_type |

### 5.3 Sitemap & URL Architecture

```
momo.vn/vay-nhanh/                   → Hub · "vay nhanh" 165K · P0

WAVE 1 - Q2/2026 (volume evidence từ CSV):
  /vay-nhanh/chi-can-cmnd            → 21,000 vol · MoMo USP rõ nhất · P1
  /vay-nhanh/khan-cap                → ~8,100 vol · BOFU urgency · P1
  /vay-nhanh/tieu-dung               → 8,900 vol · "vay tiêu dùng" · P1
  /vay-nhanh/tinh-lai                → Simulator SEO standalone · P1

  Blog:
  /blog/cic-la-gi-kiem-tra-no-xau    → 21K + 15K + 13K cluster · P1
  /blog/lai-suat-vay-tieu-dung       → 90K Lãi Suất Vay cluster · P1

WAVE 2 - Q3/2026:
  /vay-nhanh/sinh-vien               → ~9,200 vol · P2
  /vay-nhanh/cong-nhan               → ~9,600 vol · P2
  /vay-nhanh/freelancer              → ~5,500 vol · P2
  /vay-nhanh/5-trieu                 → "vay nhanh 500k" 3,100 vol · P2
  /vay-nhanh/dieu-kien               → điều kiện vay · P2

  Blog:
  /blog/app-vay-tien-online-uy-tin   → 18,100 cluster · Comparison · P2
  /blog/vay-tin-chap-la-gi           → 18,100 vol · Featured Snippet opp · P2
  /blog/tat-toan-la-gi               → 8,000 vol · GEO low competition · P2

LOẠI KHỎI SCOPE (không có volume evidence):
  × /vay-nhanh/30-trieu, /vay-nhanh/50-trieu  (vol < 900 riêng lẻ)
  × /vay-nhanh/ho-tro-no-xau                  (đã confirm bỏ - chỉ blog CIC)
```

### 5.4 On-page Architecture - Hub Page

```
URL: momo.vn/vay-nhanh
H1: "Vay Nhanh MoMo - Duyệt 5 Phút, Nhận Tiền Vào Ví Ngay"

[FOLD 1] Simulator v2 - amount + term + result card + Onelink CTA
[Section 2] Trust strip: NHNN badge · App Store rating · "31M users" · "Duyệt trong 5'"
[Section 3] Quy trình 3 bước: Chụp CCCD → Kết quả 5' → Nhận tiền ví
[Section 4] Điều kiện vay (transparent checklist - YMYL)
[Section 5] "Vay theo nhu cầu" → Card grid links to spokes
[Section 6] FAQ (10–15 câu standalone, FAQPage schema, PAA-matched)
[Section 7] Disclaimer tài chính + NHNN license reference

Schema required:
  LoanProduct (name, loanType, amount range, termDuration, annualPercentageRate)
  FAQPage
  BreadcrumbList
```

### 5.5 On-page Architecture - Spoke Pages

```
Template chung cho mọi sub-page:

[50 từ đầu] Direct answer - standalone cho AI Overview
  VD /chi-can-cmnd: "MoMo Vay Nhanh cho phép vay từ 6 đến 100 triệu
  chỉ cần CCCD/CMND, không yêu cầu hợp đồng lao động hay sao kê ngân hàng..."

[Section 1] Hero: H1 + 3 trust bullets + Onelink CTA (secondary, above fold)
[Section 2] Simulator pre-filled theo segment
[Section 3] Quy trình chi tiết theo segment (3-4 bước)
[Section 4] Điều kiện cụ thể cho segment này
[Section 5] FAQ segment-specific (4–6 câu, standalone answers)
[Section 6] Related spokes + back to hub

Schema: LoanProduct + FAQPage + BreadcrumbList
```

---

## 6. Content Strategy

### 6.1 4 Content Pillars

**Pillar 1 - Transactional Landing Pages (BOFU)**
Target: "vay nhanh" core cluster (165K+ vol). Simulator fold 1, friction tối thiểu, CTA dominant. Pages: Hub + /chi-can-cmnd + /khan-cap + số tiền.

**Pillar 2 - Segment Pages (MOFU)**
Target: audience + purpose mid-tail. Pre-fill Simulator theo segment. Pages: /sinh-vien, /cong-nhan, /freelancer, /tieu-dung.

**Pillar 3 - Financial Education Blog (TOFU)**
Target: informational clusters. High depth, FAQ schema, cite NHNN. CTA soft - internal link về hub. Pages: CIC, lãi suất, app comparison, tất toán, vay tín chấp.

**Pillar 4 - GEO/AEO Structured Answers**
Target: AI Overview, ChatGPT, Gemini citation. Format: standalone FAQ answers ≤ 2 paragraphs, cite NHNN data, match PAA phrasing. Không reference "phần trên".

### 6.2 GEO - Target Queries & Answer Templates

| Target Query | Vol | Current MoMo Citation | Target |
|-------------|-----|----------------------|--------|
| "vay tiền online uy tín ở đâu 2026" | ~18K | ❌ Không | Q3/2026 |
| "lãi suất vay MoMo bao nhiêu" | ~5K | ❌ Không | Q2/2026 |
| "vay MoMo cần điều kiện gì" | ~3K | ❌ Không | Q2/2026 |
| "CIC là gì" | 21K | ❌ Không | Q3/2026 |
| "vay tín chấp là gì" | 18.1K | ❌ Không | Q3/2026 |

**GEO Answer format mẫu - "Lãi suất vay MoMo bao nhiêu?":**
> "Lãi suất Vay Nhanh MoMo tham khảo là 2.72%/tháng tính theo phương pháp flat rate - nghĩa là lãi được tính trên số tiền gốc ban đầu suốt kỳ vay. Mức lãi suất thực tế phụ thuộc vào lịch sử giao dịch MoMo và hồ sơ tín dụng của từng khách hàng. Ví dụ: vay 20 triệu đồng trong 18 tháng, tổng tiền lãi ước tính khoảng 9.8 triệu đồng."

### 6.3 YMYL Checklist - Gate trước publish

**P0 - Auto-fail nếu thiếu:**
- [ ] LoanProduct schema với đầy đủ fields · validate Rich Results Test - 0 errors
- [ ] FAQPage schema cho FAQ section
- [ ] Disclaimer lãi suất tham khảo + ghi nguồn
- [ ] NHNN license reference (hoặc MCash lending entity)
- [ ] Ngày publish + ngày cập nhật hiển thị
- [ ] Không claim "không CIC" / "bỏ qua nợ xấu" khi thực tế vẫn check
- [ ] Simulator visible fold 1 trên mobile (viewport < 600px)
- [ ] Onelink CTA có amount + term + UTM

**P1 - Should have:**
- [ ] FAQ answers standalone (không dùng "như đề cập ở trên")
- [ ] Primary FAQ match PAA phrasing từ SERP thực
- [ ] Duplicate check < 40% vs page khác (Siteliner)
- [ ] BreadcrumbList schema
- [ ] Author bio có credential tài chính (cho blog articles)

---

## 7. Backlink & Off-page Plan

**Budget 2026 - từ Excel (sheet 6 Backlink Plan):**

| Hạng mục | Vendor | Budget (incl. VAT) | Ghi chú |
|---------|--------|--------------------|---------|
| Textlink Homepage (2 báo × 12 tháng) | Hapodigital | 11,200,000 VNĐ | baophapluat.vn (DA66) + hanoimoi.vn (DA64) |
| Báo PR (10 bài) | Hapodigital | ~31,885,000 VNĐ | tienphong, kinhtedothi, vietnambiz,... |
| Big Combo 10 Báo | Hapodigital | ~10,560,000 VNĐ | (after 40% discount) |
| **Tổng** | | **~57,936,600 VNĐ** | |

**Existing backlinks đã live (2025):**
- tienphong.vn · kinhtedothi.vn · vietnambiz.vn · thuonghieucongluan.com.vn · thethaovanhoa.vn · tuoitrexahoi.vn · baolamdong.vn · nghean24h.vn · baothanhhoa.vn · vietnammoi.vn

**2026 strategy:** Duy trì textlink homepage, bổ sung PR bài mới cho sub-pages khi launch Wave 1. Ưu tiên anchor text đa dạng (không all "vay nhanh") để tránh penalty. Coordinate với SEM team - deploy backlink đồng thời với SEM campaign để maximize SOV.

---

## 8. Measurement & Tracking

### 8.1 Funnel Metrics

| Stage | Metric | Tool | Baseline | Target |
|-------|--------|------|----------|--------|
| Impression | GSC Impressions/tháng | GSC | 2,648,592 (Q1 avg) | 2,738,777 (Q4) |
| Click | GSC Clicks/tháng | GSC | 70,533 (Q1) | 98,908 (Q4) |
| CTR | GSC CTR | GSC | 2.66% (Q1) | 3.61% (Q4) |
| Ranking | Top 1 cho head terms | GSC / SERPbot | 0/10 (T1/2026) | 10/10 (T12/2026) |
| Landing | Sessions, Bounce Rate | GA4 | [Cần đo] | - |
| Simulator | Interaction rate | GA4 custom event | [Cần setup] | >40% |
| Convert | Onelink click rate | GA4 | [Cần setup] | >15% |
| Activate | App open từ Onelink | BU / Appsflyer | [Cần setup] | - |

### 8.2 Reporting Cadence

- **Weekly:** GSC clicks + CTR top 10 keywords (by SEO Lead)
- **Monthly:** Full funnel report: Impression → Click → Onelink → App activation (cross-functional với BU)
- **Quarterly:** OKR review: Clicks target vs actual · Sub-pages live · GEO citation audit

---

## 9. OKR Framework 2026

```
O1: Chiếm TOM Organic cho cluster Vay Nhanh
    - đưa MoMo lên Top 1 cho 10 head terms EOY 2026

  KR1: Clicks từ 70,533 (Q1) → 98,908 (Q4/2026)  [+40.2%]
       Lever: Sub-page launch (mid-tail capture) + CTR optimization

  KR2: CTR từ 2.66% → 3.61% (+0.95pp EOY)
       Lever: Title tag rewrite power words + số cụ thể
              A/B test meta description · FAQPage structured snippet

  KR3: Đạt Top 1 cho 10/10 head terms đến T12/2026
       (vay nhanh, vay tiền online, vay tiền nhanh, vay tiền, vay online,
       vay online nhanh, vay nhanh online, vay tiền online nhanh, vay trả góp, vay tiền mặt)
       Lever: Content depth + E-E-A-T + internal link architecture + backlink deployment


O2: Biến momo.vn/vay-nhanh thành PLG conversion engine

  KR1: Launch 12 sub-pages đủ volume evidence từ CSV - Q3/2026
       Lever: Brief → Dev → Launch pipeline, 3 pages/sprint

  KR2: Simulator v2 live: amortization + pre-fill + Onelink deep link - Q2/2026
       Lever: Spec finalize → Web Platform sprint

  KR3: Web-to-App Onelink click rate ≥ 15% của sessions trên /vay-nhanh/*
       Lever: Simulator fold 1 · sticky CTA mobile · CTA copy optimization
       [Cần GA4 event setup trước khi đo được]


O3: MoMo được cite trong AI Search cho 5+ target lending queries

  KR1: FAQPage schema deploy trên hub + tất cả sub-pages - Q2/2026
  KR2: 15+ GEO-optimized standalone FAQ answers published - Q3/2026
  KR3: Confirm MoMo citation trong AI Overview (Google) + Gemini cho
       "vay tiền online uy tín", "lãi suất vay MoMo", "vay MoMo điều kiện gì" - Q4/2026
```

---

## 10. Roadmap & Timeline

### Phase 1 - Foundation (Q1/2026 · Done)

| Item | Status |
|------|--------|
| Keyword research 11,345 KWs | ✅ Done |
| GSC KPI baseline confirm | ✅ Done |
| Ranking targets confirm | ✅ Done |
| Simulator spec v1 | ✅ Done |
| Competitive audit (FE Credit, Home Credit, Doctordong) | ✅ Done |
| Backlink plan + budget confirm | ✅ Done |
| Sub-page briefs: 6/12 complete | 🟡 In Progress |

### Phase 2 - Core Build (Q2/2026 · Priority)

**Critical Path - Simulator Revamp:**

| Task | Owner | Deadline | Blocker |
|------|-------|----------|---------|
| Finalize Simulator spec (amortization + Onelink) | Out-App Traffic | T4/2026 | - |
| Dev estimate + sprint planning | Web Platform | T4/2026 | Simulator spec done |
| GA4 event tracking setup | Out-App Traffic + Dev | T4/2026 | - |
| Simulator live + QA | Web Platform | T5/2026 end | - |

**Wave 1 Sub-pages:**

| Page | Vol | Target live | Brief status |
|------|-----|------------|--------------|
| /vay-nhanh/chi-can-cmnd | 21,000 | T5/2026 | 🟡 Draft |
| /vay-nhanh/khan-cap | ~8,100 | T5/2026 | 🟠 Pending |
| /vay-nhanh/tieu-dung | 8,900 | T6/2026 | 🟠 Pending |
| /vay-nhanh/tinh-lai | Simulator SEO | T6/2026 | 🟠 Pending |
| /blog/cic-la-gi | 21K+15K+13K | T5/2026 | 🟠 Pending |
| /blog/lai-suat-vay | 90K cluster | T6/2026 | 🟠 Pending |

### Phase 3 - Scale (Q3/2026)

Wave 2 sub-pages: /sinh-vien · /cong-nhan · /freelancer · /5-trieu · /dieu-kien  
Blog Wave 2: app comparison · vay tín chấp · tất toán  
GEO layer activation: FAQ schema toàn bộ + AI citation monitoring  
Backlink deployment đợt 2 + PR articles cho sub-pages

### Phase 4 - Optimize (Q4/2026)

CTR optimization sprint: A/B test title tags cho top 10 keywords  
Training + SOP handoff cho Inbound team  
Quarterly OKR review + 2027 roadmap planning  
GEO citation audit và confirm targets

---

## 11. Cross-functional Dependencies

| Dependency | Owner | Impact nếu delay |
|-----------|-------|-----------------|
| Simulator v2 dev | Web Platform (Bảo) | Blocker cho Q2 Clicks target |
| GA4 event tracking | Out-App Traffic + Dev | Không đo được Onelink CR |
| Onelink setup với context params | BU Credit | Deep link không truyền context |
| Content BU/Legal approval | BU · Legal | Sub-pages không thể publish |
| Blog CMS platform confirm | Web Platform | Blog content không deploy được |
| Backlink PR articles | Inbound · BMC | Off-page authority không tăng |

---

## 12. Cross-sell & Ecosystem Map

```
Trong Vay Nhanh Web:
  Amount < 5tr → Suggest Ví Trả Sau (BNPL alternative, không lãi đến 45 ngày)
  Amount > 50tr → Disclaimer: xem xét Vay Ngân Hàng (out of scope nhưng honest UX)
  Blog CIC → CTA: Tra Cứu CIC trong app (không push vay - user chưa sẵn sàng)

Post-application (App, out of scope Web):
  After loan disbursed → Suggest Bảo hiểm khoản vay
  After 3 months good payment → CIC score improvement story → Ví Trả Sau upsell

Internal link flows:
  /blog/cic-la-gi → Tra Cứu CIC app (Onelink)
  /blog/lai-suat-vay → /vay-nhanh/tinh-lai → Hub
  /vay-nhanh/* → Hub (bidirectional)
  Hub → /vi-tra-sau (cross-use-case, amount < 5tr Simulator result)
```

---

## 13. Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| AI Overview tiếp tục cannibalize clicks dù rank #1 | Cao | Cao | Build GEO layer song song - capture AIO cite thay vì chống lại |
| Web Platform sprint không available Q2 | Trung bình | Cao | Escalate to GPD leadership nếu không có resource trong T4/2026 |
| BU/Legal approval delay sub-page content | Cao | Trung bình | Establish SLA trong T4/2026, brief format chuẩn để tăng tốc review |
| Lãi suất MoMo thay đổi - hardcode trong Simulator | Thấp | Cao | Simulator lấy rate từ config, không hardcode - cần confirm với dev |
| MoMo brand vol vay vẫn thấp vs competitor | Cao | Trung bình | Acknowledge trong OKR: brand awareness là long-term play, không giải được bằng SEO |
| CTR tiếp tục giảm dù impressions tăng | Trung bình | Cao | Title tag A/B test Q4 · Rich snippet optimization |

---

## 14. Open Questions

| # | Question | Owner | Deadline |
|---|----------|-------|----------|
| 1 | Onelink template ID cho Vay Nhanh Web - đã có chưa? | BU Credit | T4/2026 |
| 2 | GA4 events hiện tại có tracking gì cho /vay-nhanh không? | Analytics / Dev | T4/2026 |
| 3 | Rate 2.72%/tháng còn current không? Config dynamic hay static? | BU Credit | T4/2026 |
| 4 | CMS platform cho blog - current CMS hay Next.js standalone? | Web Platform | T4/2026 |
| 5 | BU/Legal content approval SLA - bao nhiêu ngày per brief? | BU · Legal | T5/2026 |
| 6 | MoMo có hiển thị pre-approval signal trên web được không (xử lý data gì)? | BU · Legal | T5/2026 |

---

## Appendix A - Keyword Priority Matrix (Top 30)

| Keyword | Vol | Position (T1/2026) | Intent | Target Page | Priority |
|---------|-----|--------------------|--------|------------|----------|
| vay nhanh | 165,000 | #2 | Transactional | /vay-nhanh | P0 |
| vay tiền online | 110,000 | #3 | Transactional | /vay-nhanh | P0 |
| vay tiền nhanh | 60,500 | #3 | Transactional | /vay-nhanh | P0 |
| vay online | 60,500 | #6 | Transactional | /vay-nhanh | P0 |
| vay tiền | 60,500 | #2 | Transactional | /vay-nhanh | P0 |
| vay tiền online chuyển khoản ngay | 49,500 | - | Transactional | /vay-nhanh | P1 |
| vay online nhanh | 40,500 | #3 | Transactional | /vay-nhanh | P0 |
| vay tiền góp | 27,100 | - | Transactional | /vay-nhanh | P1 |
| vay trả góp | 27,100 | #25 | Transactional | /vay-nhanh | P0 |
| vay nhanh momo | 22,200 | - | Navigational | /vay-nhanh | P0 (defend) |
| vay tiền nhanh chỉ cần cmnd | 21,000 | - | Transactional | /vay-nhanh/chi-can-cmnd | P1 |
| cic là gì | 21,000 | - | Informational | /blog/cic-la-gi | P1 |
| vay nhanh online | 22,200 | #3 | Transactional | /vay-nhanh | P0 |
| app vay tiền online uy tín | 18,100 | - | Informational | /blog/app-vay-tien-uy-tin | P2 |
| vay tín chấp là gì | 11,000 | - | Informational | /blog/vay-tin-chap-la-gi | P2 |
| vay tiêu dùng | 8,900 | - | Commercial | /vay-nhanh/tieu-dung | P1 |
| tất toán là gì | 8,000 | - | Informational | /blog/tat-toan-la-gi | P2 |
| vay sinh viên | 4,400 | - | Transactional | /vay-nhanh/sinh-vien | P2 |
| vay công nhân | 9,600 | - | Transactional | /vay-nhanh/cong-nhan | P2 |
| công thức tính lãi kép | 15,000 | - | Commercial | /blog/lai-suat-vay + Simulator | P2 |
| kiểm tra nợ xấu | 13,000 | - | Informational | /blog/cic-la-gi | P1 |
| check cic | 15,000 | - | Informational | /blog/cic-la-gi | P1 |
| vay nhanh 500k | 3,100 | - | Transactional | /vay-nhanh/5-trieu | P2 |
| vay tiền app | 18,100 | - | Informational | /blog/app-vay-tien-uy-tin | P2 |
| tính lãi suất vay | 2,400 | - | Commercial | /vay-nhanh/tinh-lai | P2 |

---

## Appendix B - Traffic & KPI History

| Period | Traffic (Views) | Click to App | CTR (GSC) | Clicks (GSC) |
|--------|----------------|-------------|-----------|-------------|
| Jan 2024 | 75,757 | 37,194 | - | - |
| Apr 2024 | 145,943 | 49,258 | - | - |
| Jun 2024 | **159,454** | **52,404** | - | - |
| Dec 2024 | 116,672 | 37,676 | 5.47% | 37,099 |
| Jan 2025 | 91,860 | 33,655 | **5.73%** | 33,249 |
| Jun 2025 | 68,992 | 24,341 | 2.84% | 24,919 |
| Dec 2025 | 44,785 | 17,932 | 2.42% | 21,956 |
| Jan 2026 | 47,140 | 19,770 | 2.74% | 24,753 |
| Feb 2026 | 32,263 | 13,905 | 2.31% | 18,312 |
| **Q1/2026** | **~47K avg** | **~18K avg** | **2.66%** | **70,533** |
| **Q4/2026 Target** | - | - | **3.61%** | **98,908** |

> **Key observation:** Click-to-App (~42% of Traffic trong 2025) là tỷ lệ ổn định. Vấn đề cốt lõi là **Traffic đang giảm**, không phải Conversion đang giảm. Chiến lược đúng là recover Traffic trước (SEO/content), rồi optimize Conversion sau (Simulator UX).

---

*Out-App Traffic · GPD · MoMo momo.vn*  
*Document: BRD-Vay-Nhanh-Web-Growth-2026 · v1.0 · Tháng 4/2026*  
*Next review: Sau khi close Open Questions - dự kiến T5/20