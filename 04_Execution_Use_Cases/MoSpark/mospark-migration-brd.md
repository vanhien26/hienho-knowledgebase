# BRD: MoSpark Migration - System Consolidation

> **Project Manager:** Anh Bảo (Web Platform Manager)
> **Governance & SEO Strategy:** Văn Hiến (SEO & GEO Lead)
> **System Architect / Migration Mapper:** [Cần xác định - Hiến & Thuận] - Người chịu trách nhiệm định nghĩa cấu trúc dữ liệu, sơ đồ chuyển dịch và liên kết hệ thống.
> **Lead Engineers:** Võ Minh Thuận, Lê Đăng Lộc
> **Status:** Active - Structure & Mapping Phase

---

## 1. Hệ thống hiện tại: Admin Panel Tool (CMS)
Đây là hệ thống CMS trung tâm phục vụ quản lý và vận hành toàn bộ nội dung và tính năng Mini Web, Landing Page, Blog, News, FAQ, Guide trên Web MoMo hiện nay. 
*   **Vai trò**: Nền tảng cốt lõi để các Division/Center quản trị nội dung độc lập.
*   **Các Module đang vận hành**:
    *   **CMS**: Quản lý và xuất bản Mini Web & Landing Page.
    *   **Ads Manager**: Quản lý và phân phối Ads Campaign.
    *   **FlexData Management**: Quản lý dữ liệu động cho các Mini Web.
    *   **Multilingual**: Hỗ trợ đa ngôn ngữ.

## 2. Nền tảng chiến lược: MoSpark (AI-powered Platform)
MoSpark không phải là một hệ thống build mới hoàn toàn mà là **bản nâng cấp thế hệ mới** của Admin Panel Tool với tech stack tương thích AI-powered tốt hơn.
*   **Triết lý**: Giữ lại những gì đang hoạt động tốt (Continuity), đồng thời mở ra khả năng mới về AI.
*   **Thành tựu bước đầu**: Module **Landing Page Builder** đã chứng minh tính đúng đắn, giúp PM/PO có thể tự thao tác trực quan mà không phụ thuộc Dev/Inbound.
*   **Vision**: Trở thành nền tảng AI-powered Web App/Content của MoMo giúp vận hành và tăng trưởng mọi sản phẩm Web — từ Landing Page đến Mini Web, từ Content đến Web Application.

## 3. Nguyên nhân (Causes)
*   **Legacy Architecture**: Hệ thống cũ được xây dựng theo nhu cầu bộc phát của từng thời kỳ, dẫn đến việc "vá" thêm Admin Tool để phục vụ các sản phẩm phức tạp.
*   **Silo Mindset**: Việc chia Cell Team ban đầu nhằm mục đích phân quyền, nhưng lại vô tình tạo ra các "ốc đảo" dữ liệu và vận hành tách biệt.

## 4. Hậu quả (Consequences)

### 3.1. Phân rã Vận hành (Operational Fragmentation)
*   **Nỗi đau của Inbound**: Đội ngũ Inbound (quản lý toàn bộ nội dung) phải thoát ra và đăng nhập vào từng Cell Team để đăng bài. Ví dụ: Để đăng 1 bài blog về Vay, họ không thể đăng từ giao diện chính mà phải vào Cell Team Vay.
*   **Inconsistency**: Giao diện, Menu Header/Footer và các thành phần UI có thể bị lệch nhau giữa các Cell Team do không có sự quản lý tập trung.

### 3.2. Phân rã SEO & URL (URL Fragmentation)
*   **Cấu trúc chồng chéo**: 
    *   Silo 1: `momo.vn/blog/*` (Hub content)
    *   Silo 2: `momo.vn/{use-case}/blog/*` (Vay, Cinema, Bảo hiểm...)
*   **Rủi ro SEO**: Keyword Cannibalization (các trang tự cạnh tranh lẫn nhau), phân tán sức mạnh domain (Link Equity) và gây khó khăn cho việc tối ưu Authority cho toàn site.
*   **Tracking**: Việc đo lường (GA4/Umami) bị phức tạp hóa do cấu trúc URL không thống nhất.

## 5. Phương hướng xử lý (Proposed Solutions)

### 4.1. Hợp nhất Nền tảng (Consolidation)
*   Chuyển toàn bộ dữ liệu từ CMS cũ và Admin Tool sang **MoSpark**.
*   **Single Interface**: Inbound Team chỉ cần một lối vào duy nhất để quản trị mọi nội dung.

### 4.2. Quản trị theo Tag-based (Thay vì Cell Team)
*   Thay thế việc phân quyền theo "Cửa sổ Cell Team" bằng việc quản trị theo "Project Tags".
*   Inbound Team có thể lọc nội dung theo Tag dự án ngay trên giao diện chính.

### 4.3. Chuẩn hóa URL Slug
*   **Lựa chọn chiến lược**: Hợp nhất về `momo.vn/blog/` hoặc có quy tắc Redirect 301 rõ ràng cho các sub-folder blog cũ.
*   Đảm bảo tính nhất quán của URL trên toàn hệ thống MoSpark.

---

## 6. Migration Mapping Framework (The "Structure" Layer)
Đây là tầng logic định nghĩa cách hệ thống được "xây lại" trên MoSpark. Người đảm nhiệm vai trò này phải trả lời 3 câu hỏi cốt lõi:

### 6.1. Move cái gì? (Inventory Audit)
*   **Content Assets**: Blog, News, Guide, FAQ, Landing Pages.
*   **Navigation Assets**: Menu Header/Footer theo từng Cell Team.
*   **Technical Assets**: Metadata, Schema, Redirect rules, Tracking codes.

### 6.2. Đặt ở đâu? (Mapping Schema)
Sử dụng mô hình **Unified Folder Structure** để xóa bỏ sự phân rã:
*   **Hub Content**: Tất cả blog chuyển về `/blog/` (Sử dụng Tag để phân loại thay vì folder).
*   **Product Content**: Các trang sản phẩm giữ cấu trúc `/vay-nhanh`, `/bao-hiem-xe-may`.
*   **Documentation**: Các trang hướng dẫn tập trung về `/guide/`.

### 6.3. Liên kết đến cái gì? (Connectivity & Internal Link)
*   **Global Navigation**: Hợp nhất toàn bộ Menu Cell Team thành một **Master Menu** có khả năng thay đổi context theo Tag.
*   **Contextual Linking**: Tự động gợi ý nội dung liên quan dựa trên Project Tags (Ví dụ: Trang Vay Nhanh tự động link tới các Blog có tag #VayNhanh).
*   **Redirect 301 Map**: Bảng đối soát URL cũ -> URL mới để bảo toàn link equity.

## 7. Kế hoạch hành động (Next Steps)
1.  **Inventory Audit**: Thuận và Lộc rà soát toàn bộ DB của CMS cũ và Admin Tool.
2.  **Mapping Design**: Hiến & Thuận định nghĩa cấu trúc URL đích và các quy tắc chuyển hướng (301 Redirect).
3.  **Structure Setup**: Thiết lập hệ thống Tag-based trên MoSpark.
4.  **Migration Sprint**: Thực hiện chuyển đổi dữ liệu theo từng Use Case.
5.  **Quality Gate**: Sử dụng [[mospark-seo-geo-score-brd]] để kiểm tra chất lượng sau khi chuyển đổi.

## 8. Success Metrics (Migration Phase)
*   **Traffic Retention**: Giữ được >95% traffic từ các URL cũ sau khi redirect.
*   **Indexation**: 100% URL mới được index trong 2 tuần.
*   **Operational Speed**: Giảm 50% thời gian đăng bài cho team Inbound.

---
*Document: BRD-MoSpark-Migration-2026 · v1.1*
