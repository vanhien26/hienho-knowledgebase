# BRD: Merchant Page Profile - B2B2C & O2O

> - **Project:** Merchant Mini-site `/merchant` (O2O Strategy)
> - **Vision:** Chuyển dịch từ "Trang thông tin" sang "Merchant's Home on MoMo - Mini-site O2O & Tăng trưởng SME"
> - **Status:** Strategy & Ideation
> - **Đơn vị triển khai:** Web Platform (GPD) & Web Product Lead
> - **Đồng hành:** Inbound Team (BMC)
> - **SEO Score:** 58/100 | **Traffic:** 45K sessions/tháng | **W2A:** 3.2% | **Version:** 1.1 · Tháng 5/2026

---

> **Problem:** User tìm kiếm "{Merchant} có thanh toán MoMo không" nhưng không có trang MoMo nào trả lời trực tiếp - cơ hội O2O (OOH kích hoạt → web capture → offline convert) đang bị bỏ ngỏ hoàn toàn.
> **KPI Owned:** W2A (Web-to-App) ≥ 12.5% từ `momo.vn/merchant/{slug}` → attributed via Appsflyer
> **Conversion Flow:** OOH/Search trigger → `/merchant/{slug}` → Payment info + CTA → App open → Thanh toán MoMo tại cửa hàng → Transaction

---

## 1. Executive Summary

### Situation

MoMo đang chạy OOH tại hàng nghìn điểm bán trên toàn quốc - billboard, Soundbox, sticker tại quầy. Những điểm chạm offline này tạo ra awareness nhưng không tạo ra digital anchor: user thấy MoMo tại quán, về nhà search tên quán, không tìm thấy trang MoMo nào xác nhận quán đó có nhận MoMo/VTS không. O2O loop bị đứt gãy ngay tại bước quan trọng nhất.

### Complication

User search "{Merchant} có thanh toán Ví Trả Sau không" là nhóm đã có intent mua, đã chọn merchant, chỉ cần xác nhận phương thức thanh toán trước khi đến. Đây là traffic có conversion value cao nhất - nhưng MoMo không có sản phẩm web nào capture được. Traffic rơi vào bên thứ ba hoặc đứt gãy hoàn toàn. Mỗi lượt tìm kiếm bị bỏ lỡ là một giao dịch không xảy ra.

### Resolution

Mỗi `momo.vn/merchant/{slug}` là **digital anchor của O2O loop** - điểm kết nối giữa offline presence (OOH, Soundbox) và app conversion. Product job: user tìm đến, xác nhận trong 3 giây quán đó nhận MoMo/VTS, mở App, đến quán thanh toán. Không cần content dài. Không cần đọc nhiều. Product drives the loop - từ search intent đến offline transaction. MoMo trở thành BNPL-first merchant mini-site đầu tiên tại Việt Nam, đóng kín O2O loop mà không đối thủ nào đang làm.

---

## 2. Bối Cảnh Thị Trường

### Mô hình B2B2C & O2O

1. **B2B:** MoMo cung cấp giải pháp Soundbox, Quản lý doanh thu, Thuế và Vay vốn cho Merchant.
2. **B2C:** MoMo cung cấp giải pháp thanh toán (Ví MoMo, Ví Trả Sau) và hoàn tiền cho End-user.
3. **O2O (Online-to-Offline):** User tìm kiếm thông tin trên Web → Nhận ưu đãi/Thông tin → Đến cửa hàng vật lý để thanh toán qua Soundbox.

### Tình trạng hiện tại

| Hệ thống | Traffic | Vấn đề |
|---|---|---|
| Merchant Landing Pages (`/thanh-toan-momo-{merchant}`) | 18K/quý | Content cũ 5-7 năm, ưu đãi hết hạn vẫn hiển thị |
| Thổ Địa Ăn Uống (`/page/{id}`) | 67K/quý | Thin content quy mô lớn, quán đã đóng vẫn hiển thị |

### Đối thủ đã đi trước

ZaloPay đã build merchant directory tại `zalopay.vn/doi-tac/{merchant}` cho các chuỗi F&B nhưng chưa khai thác BNPL angle. Các BNPL players quốc tế (Klarna, Afterpay, Affirm) đã có merchant directory tích hợp điều kiện BNPL per merchant.

MoMo có cơ hội là BNPL-first merchant directory đầu tiên tại Việt Nam.

---

## 3. Định Hướng Dự Án

### Dự án này phục vụ điều gì?

**Product job cốt lõi:** Đóng kín O2O loop - từ offline awareness (OOH, Soundbox) đến online confirmation (merchant mini-site) đến offline transaction (thanh toán tại quán). Mỗi bước trong loop phải friction-free: user không cần đọc nhiều, không cần navigate, không cần tìm kiếm thêm.

4 outcome phát sinh từ loop được đóng kín:

**① Inbound Acquisition:** Product xuất hiện đúng lúc user đang search tên quán sau khi tiếp xúc OOH - capture intent ở điểm nóng nhất.

**② VTS Activation:** VTS Module embedded trong product như một tính năng tự nhiên - không phải banner promotion. User biết quán nhận VTS → 1 tap kích hoạt. PLG: product converts, không phải campaign.

**③ GEO/AI Visibility:** FAQ + HowTo Schema cho phép mini-site trả lời trực tiếp trong AI Overview - MoMo là nguồn xác nhận merchant payment method đáng tin cậy nhất.

**④ Web Hygiene:** Consolidate legacy systems về 1 architecture sạch, giải phóng crawl budget, phục hồi site quality cho toàn domain momo.vn.

### Dự án này KHÔNG phải

- Không xây lại Thổ Địa Ăn Uống - store-level discovery ngoài scope
- Không là CMS cho merchant tự quản lý content
- Không phải store locator hay agent directory
- Không phải trang marketing/campaign

---

## 4. JTBD Analysis

### Job #1: Xác nhận merchant có nhận MoMo/VTS không

> "Tôi sắp đến {Merchant} và muốn biết có thanh toán Ví Trả Sau được không trước khi đi."

| Dimension | Nội dung |
|---|---|
| Functional | Xác nhận phương thức thanh toán được chấp nhận |
| Emotional | Tránh bất ngờ, chủ động kế hoạch chi tiêu |
| Trigger | Sắp đến cửa hàng, đang so sánh nơi mua hàng |
| Serve bằng | `momo.vn/merchant/{slug}` - Payment Methods + VTS highlight |

### Job #2: Tìm ưu đãi MoMo tại một merchant cụ thể

> "MoMo có ưu đãi gì tại {Merchant} không? Tôi muốn dùng VTS có lợi hơn không?"

| Dimension | Nội dung |
|---|---|
| Functional | Tìm ưu đãi cashback, deal, hoàn tiền |
| Emotional | Tối ưu chi tiêu, cảm giác thông minh tài chính |
| Trigger | Chuẩn bị mua sắm, thấy thông báo deal từ MoMo |
| Serve bằng | VTS Promotion module + dynamic deal block per merchant mini-site |

### Job #3: Khám phá merchant chấp nhận BNPL theo danh mục

> "Tôi muốn biết những đâu cho mua trước trả sau bằng Ví Trả Sau MoMo."

| Dimension | Nội dung |
|---|---|
| Functional | Duyệt merchant theo category, tìm nơi có VTS |
| Trigger | Muốn mua hàng nhưng chưa chọn nơi |
| Serve bằng | `momo.vn/merchant/{category}` - Category listing với VTS filter |

---

## 5. Kiến Trúc Web

### URL Architecture

| Cấp | URL Pattern | Vai trò |
|---|---|---|
| Hub | `momo.vn/merchant` | Discovery + Navigation |
| Category | `momo.vn/merchant/{ten-category}` | Consideration + Listing |
| Merchant Mini-site | `momo.vn/merchant/{ten-merchant}-{dia-diem}-{id}` | Decision + Conversion (VTS) |

**Slug pattern:** `{ten-merchant}-{dia-diem}-{id}` cho phép differentiate merchant cùng tên ở nhiều địa điểm. Ví dụ: `momo.vn/merchant/bo-la-lot-ca-loc-nuong-nga-5-43`.

### Danh mục (15 nhóm)

F&B (Nhà hàng, Quán ăn, Cà phê, Trà sữa) - Bách hóa, Cửa hàng tiện lợi, Siêu thị - Giáo dục, Tài chính & Bảo hiểm, Giải trí, Du lịch & Đi lại - Mua sắm, Làm đẹp & Sức khỏe.

### Cấu trúc Merchant Page

| Thành phần | Loại | Mô tả |
|---|---|---|
| NAP (Merchant Data) | Platform Data | Logo, tên, category, địa chỉ |
| VTS Card | Platform Module - Fixed | Thông tin ưu đãi, lợi ích VTS, CTA kích hoạt |
| Long Content | GenAI Content | Giới thiệu chuyên sâu về merchant (150-300 từ) |
| FAQ & Hướng dẫn | Platform Module - Fixed | Câu hỏi thường gặp, hướng dẫn thanh toán |
| Đối tác liên quan | Platform Module | Danh sách merchant cùng danh mục |

### Schema Requirements

| Cấp trang | Schema bắt buộc |
|---|---|
| Hub `/merchant` | ItemList, FAQPage, Organization, BreadcrumbList |
| Category `/merchant/{cat}` | ItemList, FAQPage, HowTo, BreadcrumbList |
| Merchant `/merchant/{slug}` | LocalBusiness, FAQPage, HowTo, Offer, BreadcrumbList |

---

## 6. Success Metrics

**North Star Metric:** VTS Activations từ `/doi-tac` (attributed via Appsflyer)

| Metric | Target (90 ngày post-launch) | Source |
|---|---|---|
| Organic Traffic | Duy trì ≥ 85K/quý (không giảm net) | GSC |
| VTS Module CTR | ≥ 3% | Analytics |
| Merchant Pages rank Top 5 cho P1 queries | ≥ 80% | GSC |

**Conversion Funnel:**
```
/merchant/{slug} page view → payment_cta_click → App open → MoMo payment at store → Transaction
```

---

## 7. Dependencies & Constraints

| Dependency | Mô tả | Blocker? |
|---|---|---|
| VTS merchant list (updated) | List merchants chấp nhận VTS chính xác | Có - quyết định VTS badge |
| VTS Terms Data | Data lãi suất, hạn mức, phí, điều kiện từ VTS PO. YMYL - sai data = legal risk | Có |
| PAGE_ID → Merchant mapping | Export từ Thổ Địa DB cho audit | Có - cần cho legacy audit |
| Web Platform readiness | Landing Page Builder sẵn sàng cho /doi-tac | Có |
| Deep Link specs per merchant | Onelink URLs cho CTA vào đúng merchant flow | Có |

### Constraints

- Content production trên Landing Page Builder - không custom development
- GenAI Content phải qua review trước publish - không auto-publish
- VTS badge chỉ được gắn sau khi verify với VTS Product team
- Schema markup inject qua platform template, không hardcode

---

## Change Log
- **Tháng 5/2026 (v1.4):** Xóa Tracking Event Schema + AB Test Hypothesis - thuộc PRD/Action Plan, không phải BRD.
- **Tháng 5/2026 (v1.3):** Xóa Risk Assessment - thuộc PRD/Action Plan, không phải BRD.
- **Tháng 5/2026 (v1.2):** Reframe Executive Summary theo Problem Framing + PLG mindset. Thêm Tracking Event Schema + AB Test Hypothesis. Cập nhật URL /merchant và mini-site concept.
- **Tháng 5/2026 (v1.1):** Khởi tạo tài liệu, chuẩn hóa framework.
