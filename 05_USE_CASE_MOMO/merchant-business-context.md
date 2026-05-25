---
title: Business Context - Merchant Page MoMo
last_reviewed: 2026-05-25
next_review: 2026-08-25
---

# Business Context: Merchant Page MoMo

> - **Project:** Merchant Detail Page (SME Digital Presence + O2O Ecosystem)
> - **Main URL:** momo.vn/merchant
> - **Division:** GPD (Growth Platform Division)
> - **Use Case:** Merchant Pages / Đối tác
> - **Owner:** GPD - Out-App Traffic (Hiến)
> - **PIC Build:** Nhật (Build Lead) - Hoài Anh (MoSpark Architecture)
> - **Governance:** Văn Hiến (SEO & GEO Lead)
> - **Version:** 2.0 - May 2026 (aligned với BRD v2.0)
> - **Status:** Pilot Phase - Foundation Build (100-200 Merchants)
>
> - **Migration Flow:** Dùng /page/{id} làm reference → tạo thủ công trên MoSpark → set 308 Redirect
> - **Traffic kế thừa:** 85K/quý (2 legacy systems) | **W2A Target:** ≥12.5% | **Last updated:** 2026-05-25

---

### 1. Định danh sản phẩm

- **Tên sản phẩm:** Merchant Detail Page - SME Digital Presence Platform
- **URL Web:** `momo.vn/merchant` (Hub) / `momo.vn/merchant/{slug}` (Mini-site)
- **Slug pattern:** `{ten-merchant}-{id}` - tên merchant kebab-case không dấu, kết thúc bằng ID backend tự assign
  - Ví dụ thực tế: `momo.vn/merchant/bun-thit-nuong-chi-tuyen-44`
- **Kiến trúc 3 cấp + Sub-pages (Phase 2):**

| Cấp | URL Pattern | Số lượng | Vai trò |
|-----|------------|---------|---------|
| Hub | `momo.vn/merchant` | 1 | Discovery + Navigation |
| Category | `momo.vn/merchant/{ten-category}` | 15 | Consideration + Listing |
| Merchant Detail | `momo.vn/merchant/{slug}` | 100-200 (Pilot) → 1.000+ | Decision + O2O Conversion |
| Sub-pages | `momo.vn/merchant/{slug}/{sub-page}` | Phase 2 - TBD | Menu / Chi nhánh / Ưu đãi |

---

### 2. Mô hình doanh thu (Revenue Model)

Merchant Page là **O2O acquisition funnel** - không tạo doanh thu trực tiếp. Doanh thu phát sinh từ 3 sản phẩm O2O được kích hoạt qua trang:

| Sản phẩm O2O | Cơ chế doanh thu | Điều kiện hiển thị |
|-------------|-----------------|-------------------|
| VTS (Ví Trả Sau) | Phí 33.000đ/tháng + Spread tài chính | Merchant trong VTS list (PO verify) |
| Hoàn tiền (Cashback) | Tăng retention, kích thích transaction volume | Merchant đang chạy cashback campaign |
| Soundbox | Adoption fee + transaction cut | SME merchant được BD team xác nhận |
| Xu (Reward) | Long-term loyalty loop (TBD Q3+) | TBD |

**North Star Metric:** O2O Activations từ `momo.vn/merchant` (VTS activation + Soundbox adoption), attributed via Appsflyer + Umami.

**Conversion Flow:**

```
"{Merchant} có nhận MoMo không?" 
  → /merchant/{slug} 
  → O2O CTA click (VTS / Hoàn tiền / Soundbox) 
  → App open (Onelink) 
  → Activation / Transaction
```

**Value Exchange (SME angle):** MoMo tạo Digital Presence miễn phí cho SME → SME adopt O2O stack → Consumer trải nghiệm O2O tốt → Transaction volume tăng.

---

### 3. Giá trị cốt lõi (Value Propositions)

**Dual-sided product - 2 nhóm giá trị song song:**

**Cho SME (merchant):**
- Digital Presence miễn phí trên momo.vn - không cần website, không cần ngân sách marketing.
- Xuất hiện trên Google Search và AI engine khi user tìm kiếm tên quán hoặc danh mục.
- QR code tại quầy/Soundbox kết nối offline → online, đóng vòng lặp O2O.
- MoMo tạo và maintain - merchant không cần tự build hay bảo trì.

**Cho Consumer (user):**
- Xác nhận ngay merchant nhận MoMo/VTS hay không - tránh bị từ chối tại quầy.
- Kích hoạt VTS tại chỗ (1-tap deeplink) không cần vào app tìm kiếm.
- Hưởng ưu đãi "Trả Sau Hoàn Sâu": Hoàn 50%, tối đa 10.000đ/giao dịch - 100.000đ/tháng tại SME Soundbox.
- Hướng dẫn step-by-step thanh toán tại từng merchant cụ thể.

**Cho MoMo (Business):**
- BNPL-first + SME Digital Presence platform - ZaloPay chưa khai thác cả 2 angle này.
- Consolidate 2 legacy systems (85K traffic/quý) về 1 architecture sạch - phục hồi site quality.
- GEO moat: FAQ + HowTo schema được cite trong Google AI Overview, ChatGPT, Perplexity.
- O2O Offline → Online: QR tại Soundbox → trang /merchant → kích hoạt sản phẩm.

---

### 4. Phân khúc khách hàng (Customer Segments)

**Phía Consumer (End User):**

**Persona 1 - Người xác nhận:** ~60% traffic
- Ai: User đã biết MoMo, đứng trước merchant hoặc chuẩn bị đi.
- Pain: Không biết merchant nhận VTS không. Ngại bị từ chối tại quầy.
- Trigger: "[tên merchant] có nhận MoMo không", "[tên merchant] ví trả sau"

**Persona 2 - Người khám phá:** ~30% traffic
- Ai: User thèm món, chưa biết quán cụ thể, muốn dùng VTS.
- Pain: Không biết quán nào gần đây có VTS.
- Trigger: "[tên món] ngon", "quán [danh mục] nhận MoMo"

**Persona 3 - Người kích hoạt:** ~10% traffic
- Ai: User chưa có VTS, đang ở merchant có Soundbox, thấy OOH "Hoàn 50%".
- Trigger: Scan QR trên Soundbox → vào trang → muốn kích hoạt ngay.

**User Deficit (Internal VTS data):**
- 54% đã đăng ký VTS - chưa bao giờ dùng tại SME.
- 57% đã dùng VTS tại SME - đã churn.
- 58% đã rời chương trình VTS.
- Root cause chung: Không biết quán nào nhận VTS + Không hiểu cơ chế hoàn tiền.

**Phía SME (Merchant):**
- Quán ăn, cà phê, tiệm nhỏ không có website, không có ngân sách digital.
- Đang dùng hoặc cân nhắc Soundbox MoMo.
- Muốn khách tìm thấy họ trên mạng khi search tên quán.

---

### 5. Đối tác chiến lược (Key Partners)

**Pilot Merchant Batches:**

**Batch 1 - Top Brand Chains (32 đối tác):**
- Siêu thị & CHTL: Bách Hóa Xanh, Coopmart, Emart, 7-11, GS25, Family Mart, Mega Market, Circle K, Go!, Lotte Mart, Ministop, Aeon
- F&B: Pizza 4P's, Katinat, Highlands Coffee, Phúc Long, Jollibee, Kichi Kichi, Manwah, Dookki, Gogi, Starbucks, Lotteria, Sasin
- Sức khỏe: Pharmacity, Long Châu | Bán lẻ: Lazada, Fahasa, Con Cưng, CellphoneS | Dịch vụ: Grab, TikTok

**Batch 2 - SME Soundbox Mega 2026 (24 đối tác - URGENT):**
- OOH đang chạy trên 11 tỉnh nhưng chưa có trang MoMo.
- Migration flow: Dùng /page/{id} làm reference → tạo thủ công trên MoSpark → set 308 Redirect.

| Status | Merchant | /page/ cũ | Tỉnh | Volume/tháng |
|--------|---------|----------|------|:---:|
| **Live** | Bún thịt nướng Chị Tuyền | /page/9819516 | HCM | 8.100 |
| Cần redirect | Chả rươi Hằng Béo | /page/9843228 | Hà Nội | 30 |
| Cần redirect | Bò nhúng Mắm ruốc 8 Còn | /page/9949928 | Bình Dương | 0 |
| Clean launch | Cơm tấm Ống Khói Diệu | - | An Giang | 4.400 |
| Clean launch | Hủ tiếu Mỹ Tho Thanh Xuân | - | HCM | 1.300 |
| Clean launch | Bánh ướt Cây Me | - | Cần Thơ | 480 |
| Clean launch | Bột chiên A Tỷ | - | Đồng Nai | 480 |
| Clean launch | Hủ tiếu Nam Vang Ông Hai Bầu | - | Đồng Nai | 390 |
| Clean launch | Quán Cơm Chú Lùn | - | Cần Thơ | 320 |
| Clean launch | Hương Giang Bakery | - | Bắc Ninh | 320 |
| Clean launch | + 13 merchants còn lại | - | Nhiều tỉnh | 0-110 |

**Đối tác nội bộ:**
- VTS PO team: Approve VTS data (blocker - YMYL).
- BD/Soundbox team: Xác nhận Soundbox merchants để hiển thị Soundbox CTA.
- Campaign team: Cung cấp Cashback data cho Promotion Module.
- DA team (Hải/Hoàng): Appsflyer attribution + Onelink deep links.
- Thuận: Setup Umami tracking trước launch.
- Nhật: Build Lead. Hoài Anh: MoSpark Architecture.

---

### 6. Vận hành & Nguồn lực (Core Operations)

**Migration Flow (Batch 2 - SME):**
1. Dùng /page/{id} làm reference → tra thông tin merchant hiện có.
2. Tạo thủ công trang mới trên MoSpark (Nhật/Hoài Anh).
3. Content team chạy Merchant Page Prompt → editorial review → publish.
4. Thuận set Umami tracking cho page mới.
5. Dev set 308 Permanent Redirect từ /page/{id} về /merchant/{slug}.
6. Update sitemap: thêm URL mới, xóa URL cũ.

**Template System - 4 Variants:**

| Template | KV | Review Sync | Target Merchant |
|---------|:--:|:-----------:|----------------|
| A - Premium | Có | Có | Brand chain lớn (Highlands, BHX) |
| B - Brand | Có | Không | Chain chưa có review sync |
| C - SME Review | Không | Có | SME trending, có review data |
| D - SME Basic | Không | Không | SME cơ bản, mới onboard |

**Note:** Review Sync source cần confirm (MoMo internal / Google Places API / other) - TBD với PO trước khi apply Template A/C.

**Content Production:**
- Platform: MoSpark (Landing Page Builder) - không custom dev.
- GenAI Pipeline: Merchant Page Prompt → editorial review → publish. Không auto-publish.
- VTS Module: Fixed Content inject từ template (PO VTS approve). Editor không được chỉnh.

**Tracking:**
- Umami: Page view, O2O CTA click (VTS/Hoàn tiền/Soundbox), QR scan, scroll depth.
- Appsflyer: App open, VTS activation, Soundbox adoption - via Onelink.
- GA4 + GSC: Organic performance, keyword ranking.

**2 Thành phần tách biệt trong mỗi Mini-site:**
- **Merchant Content (GenAI + editor review):** Story, FAQ, HowTo - phục vụ merchant story, không quảng cáo O2O thái quá.
- **Platform Modules (inject tự động):** Payment Methods + O2O Promotion Stack - fix cứng, đảm bảo tính pháp lý.

**Nguyên tắc Standalone Microsite:** Mỗi /merchant/{slug} tự hoàn chỉnh - không cross-link sang merchant khác, không hiển thị Related Merchants.

---

### 7. Lợi thế cạnh tranh (Competitive Advantage)

| Lợi thế | Chi tiết |
|---------|---------|
| SME Digital Presence | ZaloPay chưa có SME angle - chỉ có F&B chain lớn |
| BNPL-first | VTS angle + FAQ/HowTo schema cho AI citation - ZaloPay chưa khai thác |
| O2O Loop hoàn chỉnh | Soundbox QR → /merchant → App: vòng lặp Offline→Online khép kín |
| SoV 54% VTS | Market Leader trong VTS cluster (135K volume/tháng) |
| Super app ecosystem | 1-tap deeplink kích hoạt - user đã có MoMo không cần onboard lại |
| GEO moat | FAQPage + HowTo + LocalBusiness schema → AI Overview citation trước ZaloPay |

---

### 8. Chương trình ưu đãi (Promotion Schemes)

**O2O Promotion Stack (inject tự động theo điều kiện):**

| Module | Nội dung | Điều kiện inject |
|--------|---------|----------------|
| VTS Card | Hoàn 50% Mega 2026 + thông số VTS | Merchant trong VTS list |
| Hoàn tiền | Cashback offer hiện tại | Merchant đang chạy campaign |
| Soundbox CTA | "Đăng ký Soundbox miễn phí" | SME chưa có Soundbox (BD confirm) |

**Campaign Mega 2026 - "Trả Sau Hoàn Sâu" (Active):**
- Tagline: "Cứ trả sau là hoàn 50%"
- Hoàn 50%, tối đa 10.000đ/giao dịch - 100.000đ/tháng
- OOH: 37 billboards - 11 tỉnh - 37+ merchants

**VTS Core Terms (Fixed - YMYL - PO VTS approve):**

| Data point | Giá trị |
|-----------|---------|
| Lãi suất | 0% (không tính lãi) |
| Hạn mức | Đến 20.000.000đ |
| Phí dịch vụ | 33.000đ/tháng (không xài không mất phí) |
| Kỳ hạn | 2/3/6/9/12 tháng |
| Điều kiện | Xác thực CCCD + Liên kết ngân hàng |

⚠️ **YMYL Lock:** Các thông số VTS trên là Fixed Content. GenAI và editor không được thay đổi bất kỳ con số nào. Nếu PO VTS cập nhật terms → chỉnh template level, tự động apply toàn bộ pages.

---

### 9. Bằng chứng tin cậy (Trust Signals)

- **NHNN cấp phép:** MoMo là ví điện tử được Ngân hàng Nhà nước Việt Nam cấp phép.
- **PCI DSS:** Bảo mật giao dịch theo chuẩn quốc tế.
- **VTS Market Leader:** SoV 54% trong VTS cluster tại Việt Nam.
- **SME track record:** [DATA: Số lượng SME đang dùng Soundbox MoMo - cần SME BU cung cấp]
- **Merchant network:** 32 Top Brand Chains (Highlands, BHX, Pharmacity...) + hàng nghìn SME.

---

### 10. Pháp lý & Tuân thủ (Compliance & Disclaimer)

- **VTS là YMYL:** Lãi suất, hạn mức, phí phải chính xác tuyệt đối. Không chỉnh sửa tùy ý per merchant.
- **VTS badge:** Chỉ gắn sau khi PO VTS verify merchant trong danh sách - không dựa trên thông tin tự tìm.
- **Soundbox CTA:** Chỉ hiển thị với SME merchants được BD team xác nhận.
- **Disclaimer (nếu có nội dung tài chính trong Long Content):** "Thông tin mang tính tham khảo. Điều kiện và quyền lợi Ví Trả Sau có thể thay đổi. Vui lòng kiểm tra điều khoản mới nhất trên ứng dụng MoMo."
- **GenAI Content:** Phải qua editorial review trước publish. Không auto-publish.
- **Sub-pages (Phase 2):** Chỉ tạo khi có đủ data - không tạo sub-page placeholder rỗng.

---

### 11. Giới hạn & Từ ngữ cấm (Constraints & Blacklist)

**Sản phẩm KHÔNG phải:**
- Không phải Thổ Địa Ăn Uống (review local).
- Không phải CMS để merchant tự quản lý.
- Không phải store locator (merchant-level, không phải branch-level).
- Không phải Google Business Profile replica - MoMo value-add là O2O stack.
- Không phải landing page campaign - đây là evergreen content + platform.

**Ràng buộc kỹ thuật:**
- Content production trên MoSpark - không custom development.
- Schema inject qua MoSpark template - không hardcode.
- Không cross-link giữa các merchant pages (Standalone Microsite).
- Sub-pages chỉ tạo khi có đủ data.
- Inbound không làm việc trực tiếp với Web Platform - mọi technical request qua Hiến.

**Blacklist từ ngữ:**
- Tên đối thủ: ZaloPay, Moca, ShopeePay (không so sánh trực tiếp).
- Cam kết tuyệt đối về tài chính: "chắc chắn hoàn tiền", "100% được duyệt VTS".
- Thông số VTS tự nghĩ: Bất kỳ con số nào về lãi suất/phí/hạn mức không từ PO VTS.

---

### 12. Số liệu & Case Study (MoMo Data)

**Search Demand:**

| Cluster | Volume/tháng | Vai trò |
|---------|:---:|---------|
| SME Soundbox branded (24 merchants) | 16.120 | Demand có sẵn - OOH đang khuếch đại |
| Generic food mapped Soundbox | 28.580 | Top-of-funnel |
| **Tổng addressable (Mega 2026)** | **~44.800** | Mục tiêu hứng trọn |
| VTS cluster tổng thị trường | 135.000 | SoV MoMo 54% - Market Leader |
| Legacy traffic (2 systems) | 85K/quý | Kế thừa sau consolidation |

**Campaign KPIs:**
- Business Target Mega 2026: 700K users thanh toán VTS tại SME.
- OOH: 37 billboards - 11 tỉnh thành.
- W2A Conversion target: ≥12.5%.
- VTS Module CTR target: 3% baseline từ Pilot.

**User Deficit (Internal):**
- 54% đăng ký VTS - chưa dùng tại SME.
- 57% đã dùng - đã churn.
- 58% đã rời chương trình.

**Expansion Opportunity:**
- 66.300/tháng generic food search chưa có SME Soundbox tương ứng.
- 474.810/tháng top F&B brand search chưa có Soundbox - sales pitch data.

---

## Danh mục tham chiếu

- [[doi-tac-brd]] - BRD đầy đủ dự án Merchant Page (v2.0)
- [[mega26-vts-sme-spa]] - SPA chiến dịch Mega 2026 "Trả Sau Hoàn Sâu"
- [[momo-merchant-page-prompt]] - Prompt GenAI viết nội dung Merchant Page
- [[mospark_genai_content]] - Quy trình GenAI content production
- [[mospark_master]] - MoSpark platform documentation

---

## Change Log

- **Tháng 5/2026 (v2.0):** Refactor toàn bộ theo BRD v2.0. Thêm SME Digital Presence angle, Dual-sided value prop, O2O Stack (VTS + Hoàn tiền + Soundbox + Xu), Template 4 variants, Standalone Microsite principle, Migration Flow (/page ID reference → MoSpark thủ công → 308 Redirect), Sub-pages Phase 2. Cập nhật North Star sang O2O Activations.
- **Tháng 5/2026 (v1.0):** Khởi tạo từ BRD v1.7 + mega26-vts-sme-spa.md v2.3.
