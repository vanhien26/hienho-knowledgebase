# BRD: Vay Nhanh - Web Growth & Conversion Platform 2026

> - **Project:** Vay Nhanh Web Growth & Conversion Platform
> - **Main URL:** momo.vn/vay-nhanh
> - **Division:** FS (Financial Services) - Loan
> - **Version:** 1.1 · Tháng 5/2026
> - **Status:** In Progress - Execution Phase

---

## Executive Summary

**Situation:** Vay Nhanh (momo.vn/vay-nhanh) là sản phẩm tín dụng tiêu dùng không thế chấp cốt lõi của MoMo, hoạt động trên nền lending license qua đối tác MCash. Web channel đang có nền tảng nhất định: Q1/2026 ghi nhận 70.533 clicks từ GSC, 2.64M impressions, ranking top 2-3 cho hầu hết head terms chính. Thị trường search lending tại Việt Nam đạt 4.22M searches/tháng — MoMo có thể tiếp cận 3.22M vol sau khi loại trừ ngân hàng, CTTC và noise.

**Complication:** Web channel đang underperform so với potential: traffic giảm từ đỉnh 159K views/tháng (Jun 2024) xuống 47K (Jan 2026), CTR sụt từ 5.73% (Jan 2025) xuống 2.74% (Jan 2026). Ba nguyên nhân chính: (1) AI Overview cannibalization từ Q2/2025 — click giảm dù impression ổn định; (2) Content stagnation — không có sub-pages theo segment, MoMo chỉ defend bằng domain authority; (3) Competitor đầu tư content sub-pages nhiều hơn trong 12 tháng qua. MoMo hiện chỉ capture ~2.2% của 3.22M addressable pool.

**Resolution:** Dự án có hai mục tiêu song song: (1) **SEO/GEO Recovery** — đạt Top 1 cho 10 head terms trước EOY 2026, expand sang 12 sub-pages mid-tail targeting segment-specific intent; (2) **PLG Conversion** — revamp Simulator thành conversion engine thực sự với amortization schedule và Onelink deep link truyền context từ web vào app. Thành công đo bằng Clicks từ 70.533 → 98.908 (Q4/2026), CTR từ 2.66% → 3.61%, và Web-to-App Onelink click rate ≥ 15% của sessions.

---

## 1. Bối Cảnh Thị Trường

### 1.1 Traffic Decline Analysis

| Period | Monthly Views | CTR (GSC) | Clicks (GSC) | Nhận xét |
|--------|--------------|-----------|--------------|---------|
| Jun 2024 | 159.454 (peak) | - | - | Đỉnh lịch sử |
| Jan 2025 | 91.860 | 5.73% | 33.249 | Vẫn healthy |
| Jun 2025 | 68.992 | 2.84% | 24.919 | Giảm mạnh |
| Dec 2025 | 44.785 | 2.42% | 21.956 | Tiếp tục giảm |
| Jan 2026 | 47.140 | 2.74% | 24.753 | Baseline hiện tại |
| **Q1/2026** | **~47K avg** | **2.66%** | **70.533** | **Baseline KPI** |
| **Q4/2026 Target** | - | **3.61%** | **98.908** | **+40.2%** |

**Key observation:** Click-to-App (~42% of Traffic trong 2025) là tỷ lệ ổn định — vấn đề cốt lõi là **Traffic đang giảm**, không phải Conversion đang giảm. Chiến lược đúng: recover Traffic trước (SEO/content), optimize Conversion sau (Simulator UX).

**Hypothesis 3 nguyên nhân Traffic decline:**
1. **AI Overview cannibalization:** Từ May/2025 Google AIO tăng mạnh tại VN — CTR giảm từ 5.73% → 2.74% trong 12 tháng là signal rõ của AIO.
2. **Content stagnation:** Không có content mới, không có sub-pages — MoMo defend bằng domain authority, không có content moat.
3. **Competitor content investment:** FE Credit, Home Credit, Doctordong đầu tư content sub-pages nhiều hơn trong 12 tháng qua.

### 1.2 Market Demand (từ Research 11.345 keywords)

| Cluster | Vol/tháng | MoMo Fit | Action |
|---------|-----------|----------|--------|
| Vay (core) | 2.132.450 | Direct | Hub + sub-pages |
| Ứng dụng cho vay | 805.870 | Comparison | Blog comparison |
| Vay ngân hàng | 521.950 | Partial | Blog only |
| Nợ xấu / CIC | 326.600 | Informational | Blog CIC education |
| Công ty cho vay | 208.020 | Competitor | Skip |
| Định nghĩa + FAQ | 160.510 | TOFU/GEO | Blog + FAQ schema |
| Lãi suất vay | 90.850 | Calculator | Simulator SEO |
| MoMo branded | 46.940 | Navigational | Hub defend |
| **Total** | **4.218.610** | | |
| **MoMo addressable** | **3.223.170** | | Loại NH, CTTC, noise |

**Critical finding - Nợ xấu cluster:** Tổng 326.600 vol nhưng 63% là informational (check CIC, kiểm tra nợ xấu). Chỉ ~3% là transactional intent. Không build landing page vay ở cluster này — chỉ blog CIC education.

**Volume distribution → sub-page strategy:**
- 46 head keywords = 1.548.700 vol (48%) — priority số 1
- 496 mid-tail (1K-10K) = 1.296.200 vol — 12 sub-pages + blog
- 8.305 long tail (<100 vol) — programmatic SEO, chưa ưu tiên

### 1.3 Competitive Landscape

| Competitor | Brand vol/tháng | Điểm mạnh | Cơ hội MoMo khai thác |
|-----------|-----------------|-----------|----------------------|
| Home Credit | 159.490 | Network, brand lớn | UX tệ, site chậm, content heavy |
| Doctordong | 128.940 | Digital-native, UX tốt | Không có hệ sinh thái app rộng |
| FE Credit | 98.790 | Volume content, 100+ landing pages | Mobile kém, không có super-app |
| Asset Credit | 67.510 | Lãi suất cạnh tranh | Brand nhỏ |
| **MoMo** | **65.240** | Super-app, 31M users, brand trust cao | Brand vol vay chỉ bằng 1/2 Home Credit |
| Mcredit | 51.970 | Agri/rural network | Digital yếu |

**MoMo chỉ cover 6% market share về Brand search** trong ngành vay — structural gap dài hạn, không giải được bằng SEO content đơn thuần. Cần brand awareness investment song song.

**Ranking baseline (T1/2026) và Target EOY:**

| Keyword | Vol/tháng | Position T1/2026 | Target EOY 2026 |
|---------|-----------|-----------------|-----------------|
| vay nhanh | 165.000 | #2 | #1 |
| vay tiền online | 110.000 | #3 | #1 |
| vay tiền nhanh | 60.500 | #3 | #1 |
| vay tiền | 60.500 | #2 | #1 |
| vay online | 60.500 | #6 | #1 |
| vay online nhanh | 40.500 | #3 | #1 |
| vay nhanh online | 22.200 | #3 | #1 |
| vay tiền online nhanh | 12.100 | #3 | #1 |
| vay tiền mặt | - | #15 | #1 |
| vay trả góp | 27.100 | #25 | #1 |

### 1.4 International Benchmark

| Platform | Market | Key Learning | Implication cho MoMo |
|----------|--------|--------------|---------------------|
| Jiebei (Ant Financial) | China | Loan offer in-app dựa trên credit score, không cần user apply | Web page nên focus vào "kiểm tra hạn mức" thay vì "apply vay" — lower commitment CTA |
| Klarna | EU | Loan calculator chiếm 50% viewport above fold; APR minh bạch | Simulator phải hiển thị tổng tiền trả và tổng lãi rõ ràng — transparency = trust |
| Kredivo | Indonesia | Calculator embedded in hero, không cần scroll | Simulator phải visible ở fold 1 trên mobile — điểm quan trọng nhất hiện đang thiếu |
| Tonik Bank | Philippines | Result card design nổi bật; comparison table vs traditional bank | Result card design quan trọng hơn input form |

---

## 2. Định Hướng Dự Án

### Dự án phục vụ điều gì?

Hai mục tiêu song song, không tách rời:

1. **SEO/GEO Recovery:** Recover và vượt ranking — Top 1 cho 10 head terms trước EOY 2026, expand sang 12 sub-pages mid-tail.
2. **PLG Conversion:** Revamp Simulator thành conversion engine thực sự — truyền context từ web vào app qua Onelink, giảm friction Web-to-App.

### Ai được phục vụ?

**Segment 1 — Emergency Borrower (BOFU · High urgency):**
Freelancer / công nhân / hộ kinh doanh nhỏ 25-40 tuổi, cần tiền trong ngày. Bị push bởi: ngân hàng hẹn 3-5 ngày, vay người thân ngại, app khác không tin tưởng. Pull bởi: duyệt 5 phút, chỉ cần CCCD, giải ngân vào ví ngay. Anxiety chính: lãi suất thực sự bao nhiêu, có bị lộ data không.

**Segment 2 — Comparison Researcher (MOFU):**
28-45 tuổi, thu nhập ổn định, đang cân nhắc vay tiêu dùng, search Google để research. Anxiety cao nhất: "2.72%/tháng flat rate nghĩa là gì? Tổng tôi trả bao nhiêu?"

**Segment 3 — Rejected Borrower / CIC Concerned (MOFU · Sensitive):**
Đã bị ngân hàng từ chối hoặc lo ngại về CIC score. Cần lựa chọn uy tín khi không đủ điều kiện ngân hàng. **YMYL red line:** Không claim "bỏ qua CIC" hay "hỗ trợ nợ xấu" nếu MoMo vẫn check CIC.

**Segment 4 — First-time Digital Borrower (TOFU):**
Lần đầu nghĩ đến vay online, chưa có kinh nghiệm. Pull bởi: MoMo brand quen từ thanh toán, App Store rating tốt, 31M users social proof.

### Dự án này KHÔNG phải là gì?

- KHÔNG cover loan underwriting decisions và credit policy — BU Credit team.
- KHÔNG cover App UX flow sau khi user click Onelink — App Product Owner.
- KHÔNG quản lý SEM campaign cho vay nhanh keywords — Media team.
- KHÔNG cover pricing và interest rate decisions — BU/Finance.
- KHÔNG cover paid influencer hoặc TikTok content — BMC.

---

## 3. JTBD Analysis

### Job #VN-01 — Vay Khẩn Cấp (Urgency Borrower)

> "Khi tôi cần tiền gấp, tôi muốn vay online uy tín không cần đến ngân hàng, để giải quyết vấn đề ngay hôm nay."

| Dimension | Nội dung |
|---|---|
| **Functional** | Hoàn tất apply và nhận tiền trong ngày, chỉ cần CCCD, không phải đến chi nhánh |
| **Emotional** | Không stress khi gấp tiền, tự giải quyết được vấn đề, không phải xin tiền ai |
| **Social** | Giữ được hình ảnh tự chủ tài chính, không ai biết mình cần tiền gấp |
| **Trigger** | Chi phí y tế đột xuất · Sửa xe · Tiền nhà cuối tháng · Cơ hội kinh doanh ngắn hạn |

**Serve bằng:** Hub page với Simulator fold 1, friction tối thiểu, CTA "Vay ngay" · /vay-nhanh/khan-cap

### Job #VN-02 — Nghiên cứu Trước Khi Vay (Comparison Researcher)

> "Khi tôi đang cân nhắc vay, tôi muốn hiểu rõ lãi suất và so sánh các lựa chọn, để ra quyết định mà không bị lừa."

| Dimension | Nội dung |
|---|---|
| **Functional** | Tính được tổng chi phí thực sự, so sánh các lựa chọn, hiểu rõ điều kiện |
| **Emotional** | An tâm rằng mình chọn thông minh, không bị lừa bởi lãi suất ẩn |
| **Social** | Là người tiêu dùng thông minh, biết quản lý tài chính |
| **Trigger** | Thấy quảng cáo vay nhưng nghi ngờ · Cần vay số tiền lớn · Đang compare nhiều options |

**Serve bằng:** Simulator với amortization schedule · Blog "Lãi suất vay tiêu dùng tính thế nào" · /vay-nhanh/tinh-lai

### Job #VN-03 — Tìm Lựa Chọn Khi Bị Từ Chối (Rejected Borrower)

> "Khi tôi không đủ điều kiện vay ngân hàng, tôi muốn biết còn lựa chọn uy tín nào, để vay mà không bị lợi dụng."

| Dimension | Nội dung |
|---|---|
| **Functional** | Tìm được giải pháp vay không yêu cầu CIC sạch hoặc thu nhập cố định |
| **Emotional** | Cảm thấy vẫn có lựa chọn, không bị loại trừ, không bị lợi dụng khi đang khó |
| **Social** | Muốn giải quyết kín đáo, không để người thân biết |
| **Trigger** | Bị ngân hàng từ chối · Không có hợp đồng lao động · Cần tiền nhưng có nợ xấu |

**Serve bằng:** Blog CIC education (không phải landing page vay) · CTA sang tra cứu CIC trong app

### Job #VN-04 — Tìm Hiểu Vay Online Lần Đầu (First-time Borrower)

> "Khi tôi lần đầu muốn vay online, tôi muốn hiểu quy trình và trust platform, để vay mà không lo rủi ro."

| Dimension | Nội dung |
|---|---|
| **Functional** | Hiểu quy trình vay, biết cần chuẩn bị gì, tin được platform |
| **Emotional** | An tâm về bảo mật thông tin, không sợ bị lừa đảo |
| **Social** | Muốn được tư vấn như người dùng lần đầu, không bị phán xét |
| **Trigger** | Lần đầu nghe đến vay app · Bạn bè đã dùng giới thiệu · Thấy quảng cáo MoMo |

**Serve bằng:** Blog "App vay tiền online uy tín 2026" → internal link về hub page

---

## 4. Kiến Trúc & Scope Build

### 4.1 URL Architecture

**Hub:**

| URL | Vol/tháng | Content Type | Mục tiêu |
|-----|-----------|--------------|---------|
| /vay-nhanh | 165.000+ | Pillar Hub | Anchor toàn bộ cluster, Simulator fold 1 |

**Sub-pages - Đợt 1 (ưu tiên cao):**

| URL | Vol/tháng | Segment | Mục tiêu |
|-----|-----------|---------|---------|
| /vay-nhanh/chi-can-cmnd | 21.000 | Emergency + Underbanked | USP rõ nhất của MoMo |
| /vay-nhanh/khan-cap | ~8.100 | Emergency | BOFU urgency |
| /vay-nhanh/tieu-dung | 8.900 | Comparison | Vay tiêu dùng segment |
| /vay-nhanh/tinh-lai | - | Simulator SEO standalone | Job #VN-02 |

**Sub-pages - Đợt 2:**

| URL | Vol/tháng | Segment |
|-----|-----------|---------|
| /vay-nhanh/sinh-vien | ~9.200 | Student |
| /vay-nhanh/cong-nhan | ~9.600 | Blue-collar worker |
| /vay-nhanh/freelancer | ~5.500 | Freelancer |
| /vay-nhanh/5-trieu | ~3.100 | Small amount |
| /vay-nhanh/dieu-kien | - | Eligibility info |

**Blog cluster:**

| URL | Vol/tháng | Intent | JTBD |
|-----|-----------|--------|------|
| /blog/cic-la-gi-kiem-tra-no-xau | 21K+15K+13K cluster | Informational | Job #VN-03 |
| /blog/lai-suat-vay-tieu-dung | 90.000 cluster | Commercial | Job #VN-02 |
| /blog/app-vay-tien-online-uy-tin | ~18.100 | Informational/Comparison | Job #VN-04 |
| /blog/vay-tin-chap-la-gi | 11.000 | Informational | Job #VN-04 |
| /blog/tat-toan-la-gi | 8.000 | Informational/GEO | Job #VN-02 |

**Loại khỏi scope:** /vay-nhanh/30-trieu, /50-trieu (vol < 900 riêng lẻ); /vay-nhanh/ho-tro-no-xau (YMYL risk, không phù hợp positioning).

### 4.2 PLG Tool - Simulator v2 Requirements

Simulator là conversion engine cốt lõi — cần revamp từ công cụ tính cơ bản thành trải nghiệm tư vấn tài chính.

**Vấn đề hiện tại:** Tính toán cơ bản, không có amortization, không truyền context qua Onelink, không visible ở fold 1 trên mobile.

**Yêu cầu Simulator v2:**
- Input: Slider số tiền vay (6M-100M VNĐ) + quick-select chips; Lựa chọn kỳ hạn (6/9/12/15/18/24 tháng)
- Logic: Flat rate 2.72%/tháng (hiển thị disclaimer); Amortization schedule (reducing balance method)
- Output - Result Card: Tiền trả mỗi tháng (dominant); Tương đương X.XXXđ/ngày; Tổng tiền trả / Tổng tiền lãi; CTA → Onelink với full context (số tiền + kỳ hạn + UTM)
- Output - Amortization Table: Collapsible toggle; Từng tháng: Trả gốc / Tiền lãi / Tổng trả / Dư nợ
- Pre-fill theo sub-page: /vay-nhanh → 20tr/18th; /khan-cap → 10tr/6th; /sinh-vien → 6tr/15th; /cong-nhan → 10tr/12th
- **Mobile requirement (hard gate):** Simulator visible hoàn toàn ở fold 1 trên viewport < 600px. Đây là blocker — không launch nếu không đạt.

### 4.3 Deeplink & Attribution Architecture

**Onelink setup:** Mỗi CTA từ web → app truyền đủ context: số tiền, kỳ hạn, source page, UTM campaign. Fallback: App Store (new user) / mở in-app VayNhanh feature (existing user) / QR code (desktop).

**GA4 Events cần setup:**

| Event | Trigger |
|-------|---------|
| `simulator_interaction` | User thay đổi số tiền hoặc kỳ hạn |
| `amortization_expanded` | User mở bảng amortization |
| `onelink_click` | User click CTA → Onelink (kèm amount, term, page) |
| `sticky_cta_click` | Click sticky bar mobile |

### 4.4 Hub Page Structure

| Section | Thành phần | Ghi chú |
|---|---|---|
| Fold 1 | Simulator v2 (amount + term + result card + Onelink CTA) | Above fold mobile — hard requirement |
| Trust strip | NHNN badge · App Store rating · "31M users" · "Duyệt trong 5 phút" | |
| Quy trình | 3 bước: Chụp CCCD → Kết quả 5' → Nhận tiền ví | |
| Điều kiện vay | Transparent checklist | YMYL bắt buộc |
| Service grid | Card links đến từng sub-page segment | |
| FAQ | 10-15 câu standalone, FAQPage schema, PAA-matched | |
| Disclaimer | Lãi suất tham khảo + NHNN license reference | |

**Schema required:** LoanProduct (name, loanType, amount range, termDuration, annualPercentageRate) · FAQPage · BreadcrumbList

### 4.5 Content Strategy

**4 Content Pillars:**

| Pillar | Target | Pages | JTBD |
|--------|--------|-------|------|
| Transactional Landing Pages (BOFU) | "vay nhanh" core cluster (165K+ vol) | Hub + /chi-can-cmnd + /khan-cap | Job #1 |
| Segment Pages (MOFU) | Audience + purpose mid-tail | /sinh-vien, /cong-nhan, /freelancer, /tieu-dung | Job #1, #2 |
| Financial Education Blog (TOFU) | Informational clusters | CIC, lãi suất, app comparison, tất toán | Job #3, #4 |
| GEO/AEO Structured Answers | AI Overview, ChatGPT, Gemini citation | FAQ answers ≤ 2 paragraphs, standalone | All Jobs |

**GEO — Target Queries:**

| Target Query | Vol | Target |
|-------------|-----|--------|
| "vay tiền online uy tín ở đâu 2026" | ~18K | Q3/2026 |
| "lãi suất vay MoMo bao nhiêu" | ~5K | Q2/2026 |
| "vay MoMo cần điều kiện gì" | ~3K | Q2/2026 |
| "CIC là gì" | 21K | Q3/2026 |
| "vay tín chấp là gì" | 18.1K | Q3/2026 |

**GEO Answer format mẫu - "Lãi suất vay MoMo bao nhiêu?":**
> "Lãi suất Vay Nhanh MoMo tham khảo là 2.72%/tháng tính theo phương pháp flat rate — nghĩa là lãi được tính trên số tiền gốc ban đầu suốt kỳ vay. Mức lãi suất thực tế phụ thuộc vào lịch sử giao dịch MoMo và hồ sơ tín dụng của từng khách hàng. Ví dụ: vay 20 triệu đồng trong 18 tháng, tổng tiền lãi ước tính khoảng 9.8 triệu đồng."

### 4.6 YMYL Content Gates

Bắt buộc với mọi page Vay Nhanh trước publish:

- LoanProduct schema với đầy đủ fields, validate Rich Results Test (0 errors)
- FAQPage schema cho FAQ section
- Disclaimer lãi suất tham khảo + ghi nguồn
- NHNN license reference (hoặc MCash lending entity)
- Ngày publish + ngày cập nhật hiển thị
- Không claim "không CIC" / "bỏ qua nợ xấu" khi thực tế vẫn check
- Simulator visible fold 1 trên mobile (viewport < 600px)
- Onelink CTA có amount + term + UTM
- FAQ answers standalone (không dùng "như đề cập ở trên")
- FAQ primary match PAA phrasing từ SERP thực

### 4.7 Off-page Strategy

**Approach:** Duy trì textlink homepage trên 2 báo lớn (DA ≥ 60); bổ sung PR articles khi launch sub-pages đợt 1. Ưu tiên anchor text đa dạng (không all "vay nhanh") để tránh penalty. Coordinate với SEM — deploy backlink đồng thời với SEM campaign để maximize SOV.

**Existing backlinks đã live (2025):** tienphong.vn · kinhtedothi.vn · vietnambiz.vn · thuonghieucongluan.com.vn · thethaovanhoa.vn · tuoitrexahoi.vn · baolamdong.vn · nghean24h.vn · baothanhhoa.vn · vietnammoi.vn

### 4.8 Cross-sell & Ecosystem Map

| Trigger | Cross-sell | Rationale |
|---------|-----------|-----------|
| Simulator kết quả < 5 triệu | Suggest Ví Trả Sau (BNPL alternative, không lãi đến 45 ngày) | Amount nhỏ phù hợp VTS hơn |
| Simulator kết quả > 50 triệu | Disclaimer: xem xét Vay Ngân Hàng | Honest UX, không push ngoài khả năng |
| Blog CIC education | CTA: Tra Cứu CIC trong app (không push vay) | User chưa sẵn sàng convert |
| /blog/lai-suat-vay | Internal link → /vay-nhanh/tinh-lai → Hub | Funnel dẫn đến Simulator |

---

## 5. Success Metrics

### 5.1 North Star Metric

**Web-to-App Activated Users từ Organic** — Số user đến web, interact với Simulator, bấm Onelink và activate vay trong app. Đo qua Onelink clicks (GA4) được attributed từ momo.vn/vay-nhanh/*.

### 5.2 Organic Performance (GSC)

| Metric | Q1/2026 Baseline | Q4/2026 Target | Tracking |
|--------|-----------------|----------------|---------|
| GSC Clicks/tháng | 70.533 | **98.908** (+40.2%) | GSC |
| GSC CTR | 2.66% | **3.61%** (+0.95pp) | GSC |
| GSC Impressions/tháng | 2.648.592 | **2.738.777** (+3.4%) | GSC |
| Top 1 cho head terms | 0/10 keywords | **10/10** EOY 2026 | GSC / Ahrefs |

**Target logic:** Head terms cluster ~560K vol/tháng hiện ở #2-3 — cần content depth + E-E-A-T + backlink investment để push lên #1. "Vay online" (#6) và "vay trả góp" (#25) cần effort lớn nhất.

### 5.3 Web-to-App Conversion

| Metric | Baseline | Target | Timeframe | Tracking |
|--------|----------|--------|-----------|---------|
| Simulator interaction rate | TBD | >40% sessions | Q3/2026 | GA4 events |
| Onelink click rate | TBD | ≥ 15% sessions | Q3/2026 | GA4 events |
| Click-to-App rate | ~42% of Traffic | Recover 45%+ | Q4/2026 | Appsflyer |

### 5.4 Content Scale

| Metric | Baseline | Target | Timeframe |
|--------|----------|--------|-----------|
| Sub-pages live | 0 | 12 sub-pages | Q3/2026 |
| Blog posts live | ~3-5 | 15+ bài | Q4/2026 |
| GEO citation cho target queries | 0 | 5+ queries cited | Q4/2026 |

---

## 6. Dependencies & Constraints

| Dependency | Mô tả | Blocker? | Status |
|---|---|---|---|
| Web Platform — Simulator v2 build | Revamp Simulator: amortization + Onelink deep link + mobile fold 1 | Yes | Pending sprint |
| BU Credit — Onelink template & loan rate config | Confirm Onelink template ID, rate config dynamic vs static | Yes | Cần confirm |
| DA Team — GA4 events + Appsflyer setup | Events: simulator_interaction, onelink_click; Appsflyer VN activation mapping | Yes | Cần setup trước launch |
| BU/Legal — Content YMYL approval | Duyệt sub-pages và blog YMYL trước publish. Cần SLA rõ (5-7 ngày/bài) | Yes | Chưa có SLA |
| Web Platform — Blog CMS platform | Confirm CMS platform cho blog layer (current vs Next.js standalone) | Yes | Pending |
| Inbound team — Blog 15+ bài | Viết theo keyword brief, qua BU/Legal duyệt | No | Phụ thuộc capacity + Legal SLA |
| Off-page campaign | Backlink deployment coordinate với sub-page launch | No | Planning |
| SEM Team — Campaign phối hợp | Deploy SEM đồng thời với backlink push để maximize SOV | No | Phối hợp theo phase |

**Constraints:**
- Mọi content tài chính phải qua Legal review trước publish (YMYL compliance).
- Inbound không làm việc trực tiếp với Web Platform — mọi request kỹ thuật qua SEO Lead.
- Simulator rate không hardcode — phải lấy từ config để update khi BU thay đổi.
- URL structure giữ nguyên momo.vn — không thay đổi domain/subdomain.

---

## 7. Risk Assessment

| # | Rủi ro | Loại | Khả năng | Impact | Mitigation |
|---|---|---|---|---|---|
| R1 | AI Overview tiếp tục cannibalize clicks dù rank #1 | Market | Cao | Cao | Build GEO layer song song — capture AIO citation thay vì chống lại |
| R2 | Web Platform sprint không available Q2 | Execution | Trung bình | Cao | Escalate sớm nếu không có resource; Simulator là critical path |
| R3 | BU/Legal approval delay sub-page content | Execution | Cao | Trung bình | Establish SLA sớm, brief format chuẩn để tăng tốc review |
| R4 | Lãi suất MoMo thay đổi — hardcode trong Simulator | Technical | Thấp | Cao | Simulator lấy rate từ config, không hardcode |
| R5 | MoMo brand vol vay vẫn thấp vs competitor | Market | Cao | Trung bình | Brand awareness là long-term play, không giải được bằng SEO — acknowledge trong KPI |
| R6 | CTR tiếp tục giảm dù impressions tăng | Market | Trung bình | Cao | Title tag A/B test; Rich snippet optimization; FAQPage structured snippet |
| R7 | Onelink tracking không setup kịp → mất data | Data | Trung bình | Cao | Không launch sub-pages nếu tracking chưa có — data loss không phục hồi |

---

## Appendix A: Keyword Priority Matrix (Top 25)

| Keyword | Vol/tháng | Position (T1/2026) | Intent | Target Page |
|---------|-----------|-------------------|--------|------------|
| vay nhanh | 165.000 | #2 | Transactional | /vay-nhanh |
| vay tiền online | 110.000 | #3 | Transactional | /vay-nhanh |
| vay tiền nhanh | 60.500 | #3 | Transactional | /vay-nhanh |
| vay online | 60.500 | #6 | Transactional | /vay-nhanh |
| vay tiền | 60.500 | #2 | Transactional | /vay-nhanh |
| vay tiền online chuyển khoản ngay | 49.500 | - | Transactional | /vay-nhanh |
| vay online nhanh | 40.500 | #3 | Transactional | /vay-nhanh |
| vay tiền góp | 27.100 | - | Transactional | /vay-nhanh |
| vay trả góp | 27.100 | #25 | Transactional | /vay-nhanh |
| vay nhanh momo | 22.200 | - | Navigational | /vay-nhanh |
| vay tiền nhanh chỉ cần cmnd | 21.000 | - | Transactional | /vay-nhanh/chi-can-cmnd |
| cic là gì | 21.000 | - | Informational | /blog/cic-la-gi |
| vay nhanh online | 22.200 | #3 | Transactional | /vay-nhanh |
| app vay tiền online uy tín | 18.100 | - | Informational | /blog/app-vay-tien-uy-tin |
| vay tín chấp là gì | 11.000 | - | Informational | /blog/vay-tin-chap-la-gi |
| vay tiêu dùng | 8.900 | - | Commercial | /vay-nhanh/tieu-dung |
| tất toán là gì | 8.000 | - | Informational | /blog/tat-toan-la-gi |
| vay công nhân | 9.600 | - | Transactional | /vay-nhanh/cong-nhan |
| vay sinh viên | 4.400 | - | Transactional | /vay-nhanh/sinh-vien |
| công thức tính lãi kép | 15.000 | - | Commercial | /blog/lai-suat-vay + Simulator |
| kiểm tra nợ xấu | 13.000 | - | Informational | /blog/cic-la-gi |
| check cic | 15.000 | - | Informational | /blog/cic-la-gi |
| vay nhanh 500k | 3.100 | - | Transactional | /vay-nhanh/5-trieu |
| vay tiền app | 18.100 | - | Informational | /blog/app-vay-tien-uy-tin |
| tính lãi suất vay | 2.400 | - | Commercial | /vay-nhanh/tinh-lai |

---

## Appendix B: Traffic & KPI History

| Period | Traffic (Views) | Click to App | CTR (GSC) | Clicks (GSC) |
|--------|----------------|-------------|-----------|-------------|
| Jan 2024 | 75.757 | 37.194 | - | - |
| Apr 2024 | 145.943 | 49.258 | - | - |
| Jun 2024 | **159.454** | **52.404** | - | - |
| Dec 2024 | 116.672 | 37.676 | 5.47% | 37.099 |
| Jan 2025 | 91.860 | 33.655 | **5.73%** | 33.249 |
| Jun 2025 | 68.992 | 24.341 | 2.84% | 24.919 |
| Dec 2025 | 44.785 | 17.932 | 2.42% | 21.956 |
| Jan 2026 | 47.140 | 19.770 | 2.74% | 24.753 |
| Feb 2026 | 32.263 | 13.905 | 2.31% | 18.312 |
| **Q1/2026** | **~47K avg** | **~18K avg** | **2.66%** | **70.533** |
| **Q4/2026 Target** | - | - | **3.61%** | **98.908** |

---

## Change Log
- **Tháng 4/2026 (v1.0):** Khởi tạo tài liệu — keyword research, competitive analysis, Simulator spec, sub-page architecture.
- **Tháng 5/2026 (v1.1):** Chuẩn hóa tài liệu — loại bỏ thông tin vận hành, tên nhân sự, code blocks kỹ thuật, budget cụ thể; chuẩn bị cho Head of BU / C-Level review.
