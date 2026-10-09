# MOMO WEB PLATFORM KNOWLEDGE BASE & SSOT

Repository này lưu trữ toàn bộ tài liệu kiến trúc kỹ thuật, chiến lược sản phẩm (PRD/BRD), chuẩn mực vận hành và dữ liệu hiệu suất (SSOT) của **Kênh Web MoMo (`momo.vn`)** thuộc Growth Platform Division (GPD).

---

## 1. DÀNH CHO KỸ SƯ WEB FRONTEND (DEVELOPER QUICK START)

Khi triển khai tính năng hoặc gắn tracking trên Web, Kỹ sư tham chiếu trực tiếp các tài liệu quy chuẩn sau:

* **QUY CHUẨN EVENT TRACKING TIỆN ÍCH WEB (UMAMI SSOT):**
  $\rightarrow$ [`umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/umami_utility_tracking.md)  
  *Quy chuẩn bắt buộc cho mọi công cụ tiện ích (Utility Tools, Calculators, Lookups). Định danh theo công thức `web_[mospark_tool_id]_[object]_[action]`, chuẩn hóa tham số `provider` & `amount`, và nguyên tắc bảo mật Zero-PII.*

* **KIẾN TRÚC ĐỊNH DANH NGƯỜI DÙNG & WEB-TO-APP (W2A ATTRIBUTION):**
  $\rightarrow$ [`04_MOSPARK_PLATFORM/mospark_user_identity_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/mospark_user_identity_tracking.md)  
  *Đặc tả kỹ thuật định danh `identityId`, Edge Middleware, gắn tham số `?wui=` vào OneLink và liên kết dữ liệu với AppsFlyer.*

* **NỀN TẢNG WIDGET STORE & MOSPARK COMPONENT REGISTRY:**
  $\rightarrow$ [`09_PRD/widget-store-prd.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/09_PRD/widget-store-prd.md)  
  *Hạ tầng Registry quản lý, kết xuất động (Next.js) và phân phối các PLG Utility Tools trên CMS MoSpark.*

---

## 2. CẤU TRÚC THƯ MỤC HỆ THỐNG (REPOSITORY STRUCTURE)

```
.
├── umami_utility_tracking.md           # SSOT: Quy chuẩn Event Tracking mọi Utility Tools
├── AGENTS.md                           # Bộ quy tắc vận hành bắt buộc dành cho AI Agent
├── MEETING_RECAPS.md                   # Nhật ký biên bản họp và chỉ đạo chiến lược của BOM
├── 00_HARNESS_CORE/                    # Bản đồ định tuyến tri thức (KNOWLEDGE_ROUTING.md) & Master Doc
├── 01_STRATEGIC_PLAN/                  # Kế hoạch chiến lược & mục tiêu OKRs Web Platform
├── 02_FRAMEWORKS/                      # Khung làm việc (SPA, SEO/GEO Playbook)
├── 03_SKILLS/                          # Bộ kỹ năng sản phẩm và văn phong
├── 04_MOSPARK_PLATFORM/                # Kiến trúc CMS MoSpark, Microsite, Identity, Ads Manager
├── 05_HUBS/                            # Tài liệu đặc tả 5 Strategic Hubs (Cinema, Vehicle, Financial...)
├── 06_USE_CASE_MOMO/                   # Hồ sơ phân tích Use Case & JTBD
├── 07_REPORTS/                         # Master Data Tracking hiệu suất thực tế & Báo cáo MTD
├── 08_DECISION_LOG/                    # Nhật ký quyết định kiến trúc và sản phẩm
├── 09_PRD/                             # Đặc tả yêu cầu sản phẩm chi tiết (PRDs)
├── 10_LEADERSHIP_MINDSET/              # Tư duy quản trị và triết lý sản phẩm
└── 11_NEWS_FEED/                       # Cổng tiếp nhận tin tức thị trường (Gemini Spark)
```

---

## 3. NGUYÊN TẮC ĐỊNH TUYẾN DÀNH CHO AI AGENT (AI ASSISTANT ROUTING)

Mọi công cụ AI Assistant (Antigravity, Cursor, Windsurf, Claude Code, GitHub Copilot) khi mở repo này bắt buộc phải nạp quy tắc tại [`AGENTS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/AGENTS.md) và định tuyến theo [`00_HARNESS_CORE/KNOWLEDGE_ROUTING.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/KNOWLEDGE_ROUTING.md).
