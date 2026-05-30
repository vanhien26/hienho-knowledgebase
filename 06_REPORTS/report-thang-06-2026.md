# MONTHLY PLAN: THÁNG 6/2026 - GROWTH PLATFORM & SEO/GEO
> **Tháng:** 06/2026 | **Người thực hiện:** Văn Hiến - SEO & GEO Lead
> **Cập nhật lần cuối:** 2026-05-29

---

## 1. Bối Cảnh Đầu Tháng

### 1.1 Carry-forward từ tháng 5

**Thành tựu lớn cần ghi nhận:**

- Phạt Nguội rollout thành công, SEM CTR 7%, CPA < 1.000đ (xe máy).
- GenAI Content Engine v3.1 sản xuất 10 bài đầu tiên lên Production.
- Merchant Pages: **38 trang SME live** (vượt scope Batch 2 ban đầu là 24, mở rộng thêm 14 merchants). OOH đang chạy đã có digital anchor hứng search demand.
- robots.txt Lớp 1 deployed, explicit allow RAG bots.
- SEO Inventory 55 cụm thị trường hoàn thành mapping.
- Telecom BRD v2.1 done, strategy defined.

**Open items chưa close:**

| Item | PIC | Deadline đề xuất |
|------|-----|------------------|
| Bug P0: VTS module render loop trên merchant pages | Nhật | 06/06 |
| 308 Redirect 3 legacy /page/ URLs (Chị Tuyền, Hằng Béo, Bò nhúng 8 Còn) | Nhật/Trọng | 06/06 |
| Deploy `/phat-nguoi/llms.txt` lên `/public/` | Trọng | 10/06 |
| Verify GSC Coverage Report - 38 merchant pages indexing status | Hiến | 13/06 |
| Họp chốt BRD VTTI với Hằng Mỵ & Thơ Telco | Hiến + Bảo | 13/06 |
| Bàn giao UTM specs Telecom cho DA Team | Hiến | 13/06 |
| Confirm Review sync mechanism (Template A/C) với PO team | Hiến | 20/06 |
| GSC + Appsflyer integration close | DA Team | 20/06 |

### 1.2 Gap vs OKR 2026 (snapshot cuối T5)

| KR | Target | Hiện tại | Mức độ | Hành động ưu tiên |
|----|--------|----------|--------|-------------------|
| KR 1.1 - MUA | 6M | 3M (baseline) | Mid-year review | Evaluate after T6 |
| KR 1.3 - W2A Conversion | 12.5% | 8.2% | Miss -4.3pp | Activate triggers |
| KR 1.4 - AI Citation tracking | Established | 0 - chưa đo | Chưa bắt đầu | llms.txt + baseline |
| KR 3.3 - AI Citation report | Auto report | 0 | Chưa bắt đầu | Thiết lập pipeline |

**Observation:** KR 1.3 là gap lớn nhất và có thể tác động ngay trong T6 thông qua Merchant Pages (38 trang live + VTS CTA) và Phạt Nguội Inline Widget. Không cần resource mới - chỉ cần kích hoạt đúng chỗ.

---

## 2. Trọng Tâm Tháng 6

Tháng 6 là tháng **Measure - Optimize - Scale**. Không launch dự án mới lớn. Đóng nốt các open items tháng 5, thiết lập đo lường baseline, và đưa 2 dự án từ "Strategy" sang "Execution" (Telecom + Use Case tiếp theo cho GenAI Engine).

**4 trụ cột tháng 6:**

| # | Trụ cột | Mục tiêu T6 | KR liên quan |
|---|---------|-------------|--------------|
| 1 | Merchant Pages - Post-launch Optimize | Baseline W2A, fix bugs, indexing 100% | KR 1.3 |
| 2 | Phạt Nguội - Scale & Measure | 30 bài ngách, SoV tracking, AEO | KR 1.4 |
| 3 | W2A Conversion Activation | Inline widgets, tracking closure | KR 1.3 |
| 4 | Telecom to Execution + Next Use Case Decision | Sprint planning, GenAI Engine next target | KR 2.2 |

---

## 3. Kế Hoạch Chi Tiết Theo Tuần

---

### TUẦN 1 - từ 02/06 đến 08/06

**Priority: Close critical bugs + Kick off measurement**

#### ACTIONS

**Merchant Pages:**
- [ ] Fix P0: VTS module render loop trên toàn bộ 38 trang (PIC: Nhật). Verify trên ít nhất 5 merchants đại diện trước khi close.
- [ ] 308 Redirect 3 legacy /page/ URLs:
  - `/page/9819516` → `/merchant/bun-thit-nuong-chi-tuyen-44`
  - `/page/9843228` → `/merchant/cha-ruoi-hang-beo-51`
  - `/page/9949928` → `/merchant/lau-mam-ruoc-8-con-80`
  - PIC: Nhật/Trọng. Rule: Set redirect TRƯỚC hoặc CÙNG LÚC verify - không để gap.
- [ ] Submit 38 merchant URLs vào Sitemap (nếu chưa). Xóa 3 /page/ URLs khỏi sitemap cùng lúc set redirect.
- [ ] Setup Umami tracking cho 38 trang: page_view, O2O_cta_click, qr_scan. PIC: Thuận.

**Phạt Nguội:**
- [ ] Deploy `/phat-nguoi/llms.txt` lên `/public/phat-nguoi/`. Nội dung: structured summary tool tra cứu + entity data cho AI search.
- [ ] Bắt đầu production 20 bài ngách cụm Tỉnh/Thành: ưu tiên top 10 tỉnh có volume cao nhất.

**Tracking:**
- [ ] Sync với DA Team (Hải/Hoàng): set deadline hard cho GSC + Appsflyer integration. Target: done trước 20/06.

---

### TUẦN 2 - từ 09/06 đến 15/06

**Priority: Indexing verification + VTTI BRD lock**

#### ACTIONS

**Merchant Pages:**
- [ ] Verify GSC Coverage Report: 38 merchants đã được index chưa? Flag bất kỳ trang nào "Discovered - currently not indexed" hoặc "Crawled - currently not indexed".
- [ ] Check Search Performance trên GSC cho branded queries: "[tên merchant] momo", "[tên merchant] ví trả sau". Ghi nhận baseline rank.
- [ ] Confirm Review sync mechanism với PO team - chọn source (MoMo internal / Google Places). Quyết định này unlock Template A/C cho Batch 1.

**Telecom:**
- [ ] Họp chốt BRD Telecom với Hằng Mỵ (VTTI Head) & Thơ (Telco Lead) + Bảo. Output bắt buộc: BRD sign-off, timeline sprint Q3/2026 confirmed.
- [ ] Bàn giao UTM specs cho DA Team: UTM structure cho 4 Persona × 4 product (Sim Số Đẹp, Nạp Data, eSIM, Nạp Tiền ĐT).
- [ ] Setup keyword filter trên GSC cho 4 tệp Persona Telecom - baseline capture bắt đầu từ T6.

**Phạt Nguội:**
- [ ] Hoàn thành 20 bài ngách cụm Tỉnh/Thành, submit cho Gatekeeper review.
- [ ] Bắt đầu production 10 bài cụm Camera (speed camera, camera phạt nguội theo tỉnh).

---

### TUẦN 3 - từ 16/06 đến 22/06

**Priority: Activate W2A triggers + Measure baseline**

#### ACTIONS

**W2A Conversion Activation (KR 1.3):**
- [ ] Phạt Nguội - Inline Lookup Widget: Nhúng widget tra cứu phạt nguội trực tiếp trong body bài blog (không dùng Smart Banner/Popup - đã quyết định 21/05). Test trên 3 bài cao nhất trước.
- [ ] Merchant Pages - VTS CTA Audit: Verify CTA "Kích hoạt Ví Trả Sau" đang hoạt động đúng Onelink attribution trên 38 trang. Check Appsflyer attribution đang ghi nhận đúng source `merchant_page`.
- [ ] Measure W2A rate tuần đầu từ merchant pages: số click CTA / page views. Ghi nhận làm baseline T6.

**SoV Tracking - Phạt Nguội:**
- [ ] Thiết lập tracking tự động cho 50 từ khóa mục tiêu cụm Phạt Nguội. Tool: có thể dùng GSC + sheet tự động hoặc Ahrefs rank tracker.
- [ ] Ghi nhận baseline rank cho 50 keywords. Target end-of-T6: Top 10 cho ≥ 60% từ khóa đã deploy content.

**GEO/AEO Foundation:**
- [ ] Manual check AI responses: Query 10 target queries trong ChatGPT, Perplexity, Google AI Overview. Check MoMo có được cite không. Ghi nhận làm AI Citation Baseline.
- [ ] Thiết lập tracking quy trình: checklist manual hàng tháng cho AI citation audit (đến khi có automated pipeline).

**Merchant - Batch 1 Planning:**
- [ ] Audit legacy URLs Batch 1 (32 brand chains): chạy `site:momo.vn` cho từng brand, list `/thanh-toan-momo-{merchant}` đang index. Ước tính: ~18 URLs cần 308 redirect.
- [ ] Confirm template eligibility: brands nào đủ KV (có logo/banner chất lượng) → Template A/B. Brands nào chưa → Template D.

---

### TUẦN 4 - từ 23/06 đến 30/06

**Priority: T6 Tổng kết + T7 Direction set**

#### ACTIONS

**Tổng kết Pilot Phạt Nguội (Decision Gate):**
- [ ] Tổng hợp số liệu 30 ngày post-launch: Traffic, Indexing rate, CTR, W2A Conversion, SoV top 10 keywords.
- [ ] Quyết định Use Case tiếp theo cho GenAI Engine: **Vay Nhanh** hay **BH ô tô**?
  - Criteria: Search volume, Competitive gap, Internal readiness (BRD status, PO alignment).
  - Vay Nhanh: BRD v1.1 done, traffic đang giảm cần recover. SoV thấp (2.2% của 3.22M addressable).
  - BH ô tô: BRD pending, SoV = 0%, 74.000 vol/tháng. Thị trường xanh hơn.
- [ ] Brief kế hoạch GenAI Engine cho Use Case tiếp theo: keyword map, content structure, production timeline.

**Merchant - Batch 1 Kick-off:**
- [ ] Finalize redirect matrix Batch 1 (32 brands). Assign PIC và timeline.
- [ ] Content production plan: 32 brand chain pages cần Template A/B. GenAI content framework đã có từ Batch 2 - adapt.

**Tracking Closure:**
- [ ] GSC + Appsflyer integration: verify live trước 30/06. Nếu chưa done → escalate.
- [ ] Appsflyer W2A attribution: confirm merchant_page source đang ghi nhận đúng trong dashboard.

**Monthly Report Prep:**
- [ ] Tổng hợp số liệu T6: Merchant Pages indexing %, W2A baseline, Phạt Nguội SoV %, AI Citation baseline.
- [ ] Chuẩn bị slide/doc update cho anh Công/Tuệ về tiến độ Q2 2026.

---

## 4. KPI Theo Dõi Tháng 6

| Metric | Baseline (cuối T5) | Target T6 | Source |
|--------|-------------------|-----------|--------|
| Merchant Pages Indexed | 1/38 (ước tính) | 38/38 (100%) | GSC Coverage |
| Merchant Pages - Brand Rank | Chưa đo | Top 5 cho 80% branded queries | GSC |
| Merchant VTS CTA Click rate | Chưa đo (baseline T6) | Ghi nhận baseline | Umami |
| W2A từ Merchant | Chưa đo | Ghi nhận baseline (KR 1.3 material) | Appsflyer |
| Phạt Nguội - Content live | 10 bài | 40 bài (+ 30 bài ngách) | CMS |
| Phạt Nguội - SoV Top 10 | Chưa đo | ≥ 60% trong 50 keywords | Ahrefs/GSC |
| AI Citation count | 0 | Baseline documented | Manual audit |
| Telecom BRD Status | Active (v2.1) | Sprint Planning locked | Internal |

---

## 5. RACI Tháng 6

| Việc | Hiến | Bảo | Nhật | Trọng | Hoài Anh | Thuận | DA Team |
|------|------|-----|------|-------|----------|-------|---------|
| Fix P0 VTS bug | C | A | R | - | - | - | - |
| 308 Redirects | A | - | R | R | - | - | - |
| llms.txt deploy | A | - | - | R | - | - | - |
| Umami tracking setup | A | - | - | - | - | R | - |
| Telecom BRD meeting | R/A | R | - | - | - | - | - |
| Content production T6 | A | - | - | R | - | - | - |
| Keyword tracking setup | R/A | - | - | - | - | R | - |
| GSC+Appsflyer close | C | A | - | - | - | - | R |
| Merchant Batch 1 plan | A | C | R | - | R | - | - |

---

## 6. Rủi Ro Cần Theo Dõi

| Rủi ro | Mức độ | Dấu hiệu cảnh báo | Biện pháp |
|--------|--------|-------------------|-----------|
| 38 merchant pages index chậm | CAO | Sau 2 tuần < 50% indexed | Force crawl qua GSC, check Internal Linking từ hub |
| VTS bug P0 kéo dài > 1 tuần | CAO | Nhật báo cáo blockers kỹ thuật | Escalate lên Bảo, xem xét hotfix |
| Telecom BRD meeting không chốt được | TRUNG BINH | Hằng Mỵ/Thơ delay | Push sang cuối T6, không để sang T7 |
| W2A Merchant = 0 sau 2 tuần | TRUNG BINH | Umami không ghi nhận click CTA | Debug Onelink attribution, check CTA placement |
| GSC+Appsflyer chưa done cuối T6 | TRUNG BINH | DA Team báo cáo blockers | Escalate, set hard deadline với Bảo |

---

## 7. Không Làm Trong Tháng 6

- Không launch thêm Use Case mới (trừ khi Decision Gate Phạt Nguội xác nhận ready).
- Không bắt đầu build BH ô tô hay Vay Nhanh nếu chưa có keyword map xong.
- Không scale Telecom content trước khi BRD sign-off.
- Không auto-publish merchant content - mọi GenAI content phải qua review.
- Không start Merchant Sub-pages (Phase 2) - chưa trong scope T6.
- Không tạo thêm merchant pages cho Batch 1 trước khi audit legacy URLs hoàn tất.

---

*Confidential | Out-App Traffic Team | Cập nhật: 2026-05-29*
