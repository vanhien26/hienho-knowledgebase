import re

filepath = "/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_ads_manager.md"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Section 4 Title & Overview
content = content.replace("## 4. Kiến Trúc Ba Module", "## 4. Kiến Trúc & Phased Rollout Strategy\n\nThay vì triển khai đồng loạt, Ads Manager được chia thành 3 Phase độc lập nhằm giảm tải cho Dev và ưu tiên chứng minh tỷ lệ chuyển đổi (W2A) sớm nhất.")

content = content.replace("### 4.1. Tổng quan lộ trình", "### 4.1. Tổng quan Phased Rollout")

old_tree = """```
Module 1 - Campaign Operations (Production)
Balloon Ads + Popup + URL targeting + A/B test
        |
        ↓ nền tảng cho
Module 2 - Traffic Inventory Management
Placement Registry + Conflict Resolution + Inventory Dashboard
        |
        ↓ nền tảng cho
Module 3 - Ads Distribution Platform
Multi-tenant per Division + Extended Formats + Umami Dashboard
```"""
new_tree = """```text
Phase 1 (MVP) - Core Operations & Native Widget
Tập trung chứng minh tỷ lệ chuyển đổi W2A với quy mô nhỏ
        |
        ↓ scale-up
Phase 2 - Traffic Inventory Management
Quản lý ad slot tập trung, tự động hóa Conflict Resolution
        |
        ↓ advanced
Phase 3 - Ads Distribution & Retargeting
Bám đuổi người dùng ẩn danh + Phân quyền Multi-tenant
```"""
content = content.replace(old_tree, new_tree)

# Replace Subheadings
content = content.replace("### 4.2. Module 1 - Campaign Operations (MVP Phase)", "### 4.2. Phase 1 (MVP) - Core Operations (Q2/2026)")
content = content.replace("### 4.3. Module 2 - Traffic Inventory Management", "### 4.3. Phase 2 - Traffic Inventory Management (Q3/2026)")
content = content.replace("### 4.4. Module 3 - Ads Distribution Platform", "### 4.4. Phase 3 - Advanced Automation & Retargeting (Q4/2026)")

# Handle Roadmap 2026
roadmap_start = content.find("## 10. Lộ Trình & Next Steps")
roadmap_end = content.find("---", roadmap_start)

old_roadmap = content[roadmap_start:roadmap_end]

new_roadmap = """## 10. Lộ Trình & Action Plan

### Roadmap 2026

| Phase | Timeline | Mục tiêu trọng tâm |
|---|---|---|
| **Phase 1: MVP & Core Ops** | **Q2/2026** | **Thư viện Widget nhúng vào bài viết (Phạt Nguội, BHYT) thông qua CMS Shortcode.** URL Targeting cơ bản. Tích hợp Umami cơ bản. |
| **Phase 2: Inventory Mgmt** | **Q3/2026** | Placement Registry MVP + Xử lý Conflict tự động + Ra mắt SEO Inventory Dashboard. |
| **Phase 3: Retargeting & Multi-tenant** | **Q4/2026** | Kích hoạt On-site Retargeting (bám đuổi qua Local Storage) + Phân quyền Division tự chạy Ads. |

### Action Plan (Chỉ focus Phase 1)

Nhằm tránh "ngộp" resource cho Tech team, danh sách dưới đây chỉ tập trung vào các công việc cần giải quyết dứt điểm trong Phase 1 (Q2/2026). Các task của Phase 2 và 3 đã được đẩy vào Backlog.

| Deliverable | Owner | Mục đích |
|---|---|---|
| Widget Library v1 | Thuận | Hoàn thiện code cho Widget Phạt Nguội & BHYT (nhúng qua CMS Shortcode) |
| PM/PO Playbook | Bảo + Hiến advise | Workflow, format guide, content checklist cho Division operator |
| Umami - URL Mapping | Thuận | Define URL pattern per Use Case (/phat-nguoi, /phat-nguoi/blog/*, etc.) |
| Umami - Reach Estimate | Thuận | Show Reach Estimate (28 days Visitor/Pageview) khi setup campaign |

### Backlog (Phase 2 & 3)
- PRD Phase 2 (Placement Registry schema, conflict logic)
- SEO Inventory (Database schema, Dashboard UI)
- Permission Model (Role definition per Division cho Phase 3)
- On-site Retargeting Module (Local storage read/write mechanism)

"""
content = content.replace(old_roadmap, new_roadmap)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
