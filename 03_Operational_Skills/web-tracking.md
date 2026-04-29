---
name: web-tracking
description: "Hướng dẫn setup và audit tracking (GA4, GTM, Appsflyer) cho mọi Use Case trên momo.vn. Đảm bảo dữ liệu Web-to-App được đo lường chính xác."
category: technical
tags:
  - tracking
  - ga4
  - gtm
  - appsflyer
  - web-to-app
author: klaus-momo
version: 1.0.0
---

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

## Liên kết
- Skill liên quan: [[Web2App-Pipeline]]
- Workflow: [[PROJECT_ORCHESTRATOR]]
- Xem tổng thể: [[SKILL_REGISTRY]]
