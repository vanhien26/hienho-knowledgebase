# Web-to-App Tracking Standard

## 1. Tracking Philosophy
Tại MoMo, chúng ta không chỉ đo "Page View". Chúng ta đo **"Conversion Flow"**.
Mọi Use Case phải track được:
`Traffic → Engagement → CTA Click → App Open → Completion`

---

## 2. GTM & GA4 Event Standard
Mọi page mới phải implement tối thiểu các event sau:

| Event Name | Parameter | Trigger |
|------------|-----------|---------|
| `page_view` | `page_type`, `use_case` | Mọi page load |
| `cta_click` | `cta_name`, `destination_url` | Click vào nút Onelink/CTA |
| `scroll_depth`| `percentage` | 25%, 50%, 75%, 90% |
| `form_start` | `form_id` | Khi user tương tác với widget/form |
| `geo_citation`| `ai_engine` | Khi phát hiện traffic từ AI Bots (Referrer check) |

---

## 3. Appsflyer Onelink Structure
Onelink là "xương sống" của Web-to-App. Tuyệt đối không dùng URL trần của App Store.

**Cấu trúc chuẩn:**
`https://momoapp.onelink.vn/[onelink_id]?pid=[channel]&c=[campaign]&af_dp=[deeplink]&af_web_dp=[fallback_url]`

- `pid`: Nguồn traffic (e.g. `seo`, `inbound`, `paid_ads`)
- `c`: Tên dự án (e.g. `vay-nhanh-seo-2026`)
- `af_dp`: Đường dẫn sâu vào app (e.g. `momo://app/insurance/motorcycle`)

---

## 4. Audit Checklist
- [ ] GTM Container đã được nhúng vào `<head>`?
- [ ] GA4 DebugView có nhận được event `cta_click` khi nhấn nút không?
- [ ] Appsflyer URL có chứa đủ UTM parameters không?
- [ ] Fallback URL có hoạt động khi mở trên Desktop không?

---
## 5. Current GTM OutApp Configuration (Audit Reference)

Dựa trên cấu trúc thực tế của Container `GTM-P9JDDJZ` (Cập nhật: 08/05/2026):

### 5.1 IDs & Core Config
- **GTM Container ID:** `GTM-P9JDDJZ`
- **GA4 Measurement ID:** `G-02G70QKZ26` (Tag ID 120)
- **Facebook Pixel:** `945741992230934` (Tag ID 4)
- **Clarity Project ID:** `b8khpz7pwz` (Tag ID 134)

### 5.2 Key Event Logic
Hệ thống đang sử dụng các Trigger đặc thù để bóc tách hành vi:
- **Click CTA (momo.vn):** Thu thập `Page URL`, `Click URL` và `Click Text` (UA Event - Tag 174).
- **Outbound Links Click:** Tự động track khi user click link ra ngoài domain MoMo.
- **Cinema Funnel:** Đã có sẵn bộ tag đo lường sâu: `Pick time`, `Pick seat`, `Pick popcorn`.
- **Copy Code:** Track hành vi copy mã khuyến mãi (Promotion Code).

### 5.3 Critical Variables (Dùng cho Filter & Report)
- `{{lookup-project_name}}`: Tự động map URL vào tên dự án (Phạt Nguội, Vay Nhanh, Cinema...).
- `{{JS_TrafficType}}`: Phân loại traffic nội bộ vs bên ngoài.
- `{{Hashtag URL}}`: Xử lý tracking cho các trang Single Page Application (SPA) dùng hashtag.


---
## 6. GTM Tag Inventory (Full Event Tracking List)

Dưới đây là danh mục toàn bộ các sự kiện đang được cấu hình trong GTM OutApp (`GTM-P9JDDJZ`). Agent và PO cần đối soát danh sách này trước khi yêu cầu tạo event mới.

### 6.1 Core Analytics & Performance
| Tag Name | Measurement ID / Key | Purpose |
|----------|----------------------|---------|
| `[GA4] - Config` | `G-02G70QKZ26` | Cấu hình gốc GA4, phân loại traffic & project. |
| `Facebook Ads` | `945741992230934` | Pixel đo lường chuyển đổi Facebook. |
| `[Clarity] - Heatmap` | `b8khpz7pwz` | Đo lường bản đồ nhiệt và session recording. |
| `Google Ads - MCC` | `AW-939435033` | Đo lường chuyển đổi Google Ads cấp tập đoàn. |
| `Hubspot` | `5558699` | Nhúng tracking Hubspot cho CRM. |

### 6.2 Generic Interactions (Global Tags)
- `GA Event - Click CTA (momo.vn)`: Track mọi cú click vào các nút có class CTA.
- `GA Event - Outbound Links Click`: Tự động ghi nhận khi user rời khỏi website MoMo.
- `GA Event - QR Code`: Đo lường lượt click/quét mã QR trên website.
- `[GA4] - Link URL`: Ghi nhận các link liên kết được click.
- `GA - Virtual Pageview`: Xử lý ảo hóa pageview cho các component popup/overlay.

### 6.3 Project Funnels (Use Case Specific)

#### **A. Cinema [CINE]**
- `[CINE] - Event - funnel_start`: User bắt đầu chọn phim.
- `[CINE] - Event - click_cta`: Click nút đặt vé (bao gồm cả QR Code).
- `[CINE] - Event - funnel_complete`: User hoàn thành chọn ghế/bắp nước và nhảy vào App.
- `Funnel Cinema - Click Time/Seat/Popcorn`: Đo lường chi tiết từng bước trong widget.

#### **B. Insurance [OTO]**
- `[OTO] - 1.1_click_insurance_type`: Chọn loại bảo hiểm.
- `[OTO] - 1.3_click_get_quote`: Yêu cầu báo giá trong form.
- `[OTO] - 5.1_get_qr_link_success`: User lấy QR thanh toán thành công.
- `[OTO] - Event - funnel_start/complete`: Đo lường phễu tổng thể.

#### **C. Travel & Hotel [FLIGHT] [HOTEL]**
- `[FLIGHT] - Event - click_cta`: Click đặt vé máy bay.
- `[Hourly Hotel] - Funnel - 1_view_room`: Xem chi tiết phòng khách sạn.
- `[Hourly Hotel] - Funnel - 2_book_room`: Nhấn nút đặt phòng.

#### **D. Promotion & Engagement**
- `[UA] Event - Copy Code`: Ghi nhận user copy mã khuyến mãi.
- `Soju - GA Event - Youtube`: Đo lường tương tác video (Play/25%/50%/Finish).
- `GA Event - Click Engage - Search`: Track hành vi tìm kiếm trên trang chủ.


---
## 7. GTM Folder Mapping (Use Case Organization)

Để quản lý hàng trăm Tag hiệu quả, GTM OutApp được tổ chức theo cấu trúc Folder sau. Agent/PO khi kiểm tra tracking nên ưu tiên tìm trong các folder này:

### 7.1 Service Specific Folders `[S]`
- `[S] - VayNhanh`: Toàn bộ logic đo lường cho dự án Vay Nhanh.
- `[S] - Cinema`: Tracking chuyên sâu cho luồng đặt vé phim.
- `[S] - BHOTO / BHXM / BHYT`: Nhóm các dự án bảo hiểm.
- `[S] - Hourly Hotel`: Luồng đặt phòng khách sạn theo giờ.
- `[S] - TraGopApple`: Theo dõi chuyển đổi mua trả góp Apple.
- `[S] - Travel SIM / SIM`: Các dịch vụ viễn thông và du lịch.

### 7.2 Campaign Folders `[C]`
- `[C] - LACXI25`: Chiến dịch Lắc Xì 2025.
- `[C] - MEGA25`: Các chương trình khuyến mãi lớn năm 2025.
- `[C] - VTS`: Tracking cho đối tác Viettel Solutions.

### 7.3 Infrastructure & Global `[GA4] [UA]`
- `[GA4] - Settings`: Cấu hình base cho GA4.
- `[GA4] - Funnel`: Các tag đo lường phễu chuyển đổi chung.
- `[GA4] - Click CTA`: Các thẻ đo lường tương tác nút bấm.
- `CTA Tracking`: Nhóm các thẻ đo lường click-to-app (Legacy & New).


---
## 8. Advanced Tracking Setup

### 8.1 Parallel Tracking (Umami)
- **Tool:** Umami Analytics (PIC: Thuận).
- **Purpose:** Đối soát (Sanity Check) dữ liệu Pageview, Session, Visitor với GA4.
- **Key metrics:** So sánh tỉ lệ lệch (Variance) giữa GA4 và Umami để calibrate baseline 6M Visitors.
- **Visitor Definition (SSOT):** 1 Unique Visitor = 1 `user_pseudo_id` (GA4) trong 1 ngày.

### 8.2 GEO/AI Traffic Mapping (GA4)
Logic nhận diện AI Referral Traffic:
- **Target Domains:** `chatgpt.com`, `claude.ai`, `perplexity.ai`, `gemini.google.com`, `labs.google.com`, `poe.com`, `copilot.microsoft.com`.
- **GA4 Mapping:** Source = `ai_traffic`, Medium = `referral`.

### 8.3 BigQuery Data Filtering
Để đảm bảo dữ liệu "Web-attributed" chính xác, các truy vấn trên BQ cần áp dụng filter:
- **Condition:** `ref = 'website'`
- **Applied Tables:** `ONELINK_LOGGER_APP_GET_METADATA_V2` và `APP_EVENT.EVENTS`.

### 8.4 Website User ID (WUI) Tracking Integration (PIC: Hiếu)
Đây là dự án định danh người dùng xuyên suốt Web-to-App của MoSpark. Để xem sơ đồ kiến trúc và đặc tả chi tiết 5 Tầng xử lý, vui lòng tham chiếu tài liệu dự án: [mospark_user_identity_tracking.md](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_user_identity_tracking.md).

**Tóm tắt Luồng Xử Lý (5 Tầng):**
1.  **Tầng 1 (Identification):** Edge Middleware đọc HttpOnly Cookie khi user truy cập.
2.  **Tầng 2 (Identity Generation):** Khởi tạo Identity Object (Anonymous ID qua `generateAnonId()` hoặc Logged-in ID qua `hashed_uid`).
3.  **Tầng 3 (Analytics Tracking):** Đẩy Identity ID sang GA4 (`dataLayer.push`) và Umami (`umami.identify`) để stitch session.
4.  **Tầng 4 (CTA Distribution):** CTA Builder tự động gắn tham số `wui=<identityId>` vào toàn bộ link Appsflyer Onelink.
5.  **Tầng 5 (App Attribution):** App MoMo nhận diện `wui` từ Onelink để liên kết chéo với User ID trong App và đối chiếu dữ liệu MAU/MEU trên BigQuery.

---

## Liên kết
- Skill liên quan: [[Web2App-Pipeline]]
- Workflow: [[orchestrator_engine]]
- Mục tiêu chiến lược: [[web-momo-okrs-2026]] - KR 1.1 (6M MUA)
- Xem tổng thể: [[skill_registry]]
- **Baseline Date:** Dữ liệu chuẩn bắt đầu từ **23/04/2026