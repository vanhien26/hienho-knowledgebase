# MoSpark - Blog UI/UX Re-Design
Tiêu chuẩn và tối ưu hóa giao diện hiển thị hệ thống Blog

> - **Project Name:** MoSpark Web Platform
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Bảo
> - **PIC:** Tuấn (Design)
> - **Version:** 1.0 · June 2026

---

## 1. Executive Summary

### 1.1. Bối cảnh (Situation)
Blog của MoMo hiện đang phục vụ lượng lớn Out-App Traffic thông qua SEO và Social. Tuy nhiên, UI/UX hiện tại chưa được tối ưu triệt để để giữ chân người dùng (Retention), tạo dựng độ tin cậy chuyên gia (E-E-A-T), và tận dụng lượng traffic khổng lồ này để chuyển đổi về App (Web-to-App).

### 1.2. Mục tiêu (Objective)
Cải tổ toàn diện giao diện hiển thị của MoSpark Blog (Home & Detail) với 4 trọng tâm chính:
- **Monetization & Conversion:** Khai thác vị trí quảng cáo chiến lược.
- **AI-Powered UX:** Cá nhân hóa và tăng tốc độ tiếp thu thông tin bằng AI.
- **E-E-A-T Compliance:** Chuẩn hóa tín hiệu chuyên môn từ tác giả.
- **Performance:** Đảm bảo trải nghiệm đọc và tốc độ tải trang (Core Web Vitals).

---

## 2. Các Tính Năng Đề Xuất (Core Features)

### 2.1. Vị trí Quảng cáo (Ads Placements)
- **Mục tiêu:** Tăng chuyển đổi Web-to-App (W2A) từ traffic tự nhiên mà không phá vỡ trải nghiệm đọc.
- **Chi tiết UI/UX:**
  - **Trang Home (Listing):** Thiết kế dạng **Native In-feed Ads** (quảng cáo xen kẽ tự nhiên giữa các thẻ bài viết).
  - **Trang Detail (Chi tiết):**
    - **Mobile:** *Sticky Bottom Bar* (banner cố định ở mép dưới màn hình) hoặc *In-content banner* (banner tĩnh chèn giữa các thẻ Heading).
    - **Desktop:** *Floating Sidebar* (Banner trượt dọc theo nội dung ở cột phải).
- **Ràng buộc Kỹ thuật (Technical/CWV):**
  - Mọi vị trí Ads phải được quy hoạch không gian cứng (Skeleton loading) để tránh gây ra hiện tượng giật layout (Lỗi CLS - Cumulative Layout Shift).
  - Ads slot phải kết nối được với hệ thống `MoSpark Ads Manager`.

### 2.2. Tính năng AI Summarize (Tóm tắt nội dung)
- **Mục tiêu:** Phục vụ nhóm người dùng đọc lướt (Skimmers), tăng Time-on-site, và tối ưu cấu trúc dữ liệu cho AI Search (GEO).
- **Chi tiết UI/UX:**
  - **Vị trí:** Đặt ngay dưới Title/H1 và phần Metadata (Ngày tháng, tác giả).
  - **Visual:** Có thiết kế nổi bật mang hơi hướng công nghệ (Ví dụ: Icon ✦ Sparkles, background nhạt màu gradient hoặc badge "AI Tóm tắt") để làm nổi bật giá trị nền tảng MoMo.
  - **Tương tác:** Dạng Bullet points ngắn gọn (3-4 ý chính). Giao diện có thể mặc định thu gọn kèm nút "Click để xem tóm tắt" hoặc auto-expand.
- **Giá trị SEO/GEO:** AI Summarize tạo ra Mật độ Dữ kiện (Fact Density) cao, giúp Google AI Overviews và các công cụ AI khác dễ dàng trích dẫn nội dung của MoMo.

### 2.3. Author Box (Thông tin Tác giả & Social)
- **Mục tiêu:** Đáp ứng triệt để tiêu chuẩn **E-E-A-T** (Experience, Expertise, Authoritativeness, Trustworthiness) của Google đối với nội dung YMYL (Tài chính).
- **Chi tiết UI/UX:**
  - **Top of Page (Đầu bài):** Mini-profile gọn nhẹ gồm Avatar nhỏ, Tên tác giả, và Chức danh chuyên môn (VD: *Chuyên gia Tài chính Cá nhân*).
  - **Bottom of Page (Cuối bài):** Full Author Box với Avatar lớn gọn gàng, Bio tóm tắt (2-3 dòng), và kèm theo các icon Social (như LinkedIn/Facebook) trỏ về profile thực của tác giả.
- **Ràng buộc Kỹ thuật:** UI này sẽ được map tự động với `Person Schema` trong source code.

### 2.4. Hiển thị Hình ảnh (Hero Image & In-post)
- **Mục tiêu:** Nâng cấp cảm quan (Look & Feel) theo chuẩn báo chí/tạp chí tài chính cao cấp và bảo vệ điểm hiệu năng (LCP).
- **Chi tiết UI/UX:**
  - **Hero Image (Ảnh bìa):** 
    - Hiển thị tràn viền (Edge-to-edge) trên Mobile.
    - Cố định tỷ lệ khung hình (Aspect Ratio), ví dụ 16:9 hoặc 2:1, để tránh việc ảnh bị cắt lệch trọng tâm khi Editor upload kích thước tùy ý.
  - **In-post Image (Ảnh trong bài):**
    - Phải có thiết kế UI cho **Caption** (Chú thích ảnh) và **Source** (Nguồn ảnh).
    - Viền ảnh bo góc nhẹ (rounded corners) theo chuẩn UI System của MoMo.
- **Ràng buộc Kỹ thuật:** Khu vực Hero Image ưu tiên sử dụng ảnh tĩnh hoặc tối ưu siêu nhẹ (WebP), không dùng các hiệu ứng animation phức tạp để giữ điểm LCP ≤ 2.5s.

## 2.5. Quy Chuẩn Quản Trị Trạng Thái & CRUD Bài Viết (SEO & Content)

Để tối ưu hóa trải nghiệm quản trị (CMS UI) và phân quyền triển khai, vòng đời trạng thái của bài viết Blog (Blog Article Page) được rút gọn về **đúng 4 trạng thái chính**: **Draft** -> **Review** -> **Live** -> **Deleted**.

#### A. Ma Trận Cấu Hình SEO & Server Response

| Trạng thái (CMS Status) | HTTP Code | Robots Meta Directive | Sitemap XML | Canonical URL | Indexing API Ping | Mô tả trải nghiệm người dùng & SEO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Draft** (Bản nháp) | `404 Not Found` hoặc `403 Forbidden` | `noindex, nofollow` | Loại bỏ (Exclude) | Không có | Không gửi | **Creator:** Viết nội dung thô (GenAI Outline/Detail).<br>**Public user:** Lỗi 404. |
| **2. Review** (UAT / Demo) | `404 Not Found` hoặc `403 Forbidden` | `noindex, nofollow` | Loại bỏ (Exclude) | Không có | Không gửi | **Creator/QC:** Xem trước giao diện bài viết, duyệt E-E-A-T.<br>**Public user:** Lỗi 404. |
| **3. Live** (Hoạt động) | `200 OK` | `index, follow` | Khai báo (Include) | Self-referencing (Trỏ về chính nó) | Gửi Indexing API (Google & IndexNow) | **Public user:** Xem và đọc bài viết đầy đủ. |
| **4. Deleted** (Xóa/Gỡ bỏ) | `404 Not Found` hoặc `410 Gone` | `noindex, nofollow` | Loại bỏ (Exclude) | Không có | Gửi API yêu cầu xóa index (Remove URL) | **Public user:** Lỗi 404/410.<br>*Hỗ trợ cấu hình Redirect 301/308 (gộp) hoặc 302/307 (tạm ẩn).* |

#### B. Cơ Chế Xử Lý SEO & Nghiệp Vụ Tối Giản

1. **Kiểm duyệt E-E-A-T tại trạng thái Review:**
   * Bài viết chỉ được duyệt chuyển sang trạng thái **Live** khi đã vượt qua bộ lọc chất lượng tại màn hình **Review**: Đã gắn thẻ Tác giả (Person Schema) có Author Box hợp lệ, và đã sinh nội dung tóm tắt AI Summarize đầy đủ.
2. **Xử lý Chuyển hướng và Tạm ẩn bài viết (trực thuộc trạng thái Deleted):**
   * Khi chuyển bài viết sang trạng thái **Deleted**, CMS bắt buộc cung cấp tùy chọn nhập **`Redirect URL`** và loại redirect:
     * **Nếu gộp bài viết (Archived/Merged):** Chọn redirect **301 Moved Permanently** hoặc **308** trỏ về bài viết mới (Epic Content) để bảo toàn dòng chảy Link Juice.
     * **Nếu bài viết thời vụ/chiến dịch hết hạn (Temporary Inactive):** Chọn redirect **302 Found** hoặc **307** trỏ về chuyên mục cha `/blog/` để thu hứng traffic tạm thời.
     * **Nếu xóa vĩnh viễn (Deleted):** Không điền redirect, máy chủ trả về **410 Gone** để Googlebot nhanh chóng xóa index và tiết kiệm Crawl Budget.

#### C. Phân Quyền Vai Trò Chuyển Đổi Trạng Thái (Transition RBAC Gates)

| Từ Trạng thái | Sang Trạng thái | Editor (Creator) | QC Lead / Admin | Tech Lead |
| :--- | :--- | :---: | :---: | :---: |
| **Draft** | **Review** | ✔ (Cho phép) | ✔ (Cho phép) | ✔ (Cho phép) |
| **Review** | **Live** | ❌ (Bị khóa) | ✔ (Cho phép) | ✔ (Cho phép) |
| **Review** | **Draft** (Reject) | ✔ (Cho phép) | ✔ (Cho phép) | ✔ (Cho phép) |
| **Live** | **Deleted** | ❌ (Bị khóa) | ✔ (Cho phép) | ✔ (Cho phép) |
| **Live** | **Review** (Sửa lớn) | ✔ (Cho phép) | ✔ (Cho phép) | ✔ (Cho phép) |

---

## 3. Workflow Phối hợp

1. **Product Design (Tuấn):** Chịu trách nhiệm thiết kế layout, UI components, responsive behavior (Desktop/Mobile) dựa trên brief này. Bàn giao thiết kế trên Figma.
2. **Web Product Lead (Văn Hiến):** Rà soát bản thiết kế để đảm bảo không vi phạm các rào cản về SEO (CWV, E-E-A-T) trước khi đưa sang đội Engineering.
3. **Engineering Team:** Dựng component và cấu hình liên kết (Schema mapping, Ads logic) trong MoSpark Editor. Tích hợp quản trị vòng đời trạng thái của bài viết (Draft -> Review -> Live -> Deleted) bám sát các tiêu chuẩn kỹ thuật (HTTP codes, Sitemap, Robots, Canonical) được định nghĩa tại [Mục 2.5 Quy Chuẩn Quản Trị Trạng Thái & CRUD Bài Viết](#2.5.-quy-chuẩn-quản-trị-trạng-thái--crud-bài-viết-seo--content).

---

## 4. Change Log
- **v1.0 (2026-06-01):** Khởi tạo tài liệu. Định nghĩa 4 tính năng cốt lõi cho đợt Re-Design: Ads Placements, AI Summarize, Author Box, và Image Display Optimization (Văn Hiến).
- **v1.1 (2026-06-09):** Tuấn hoàn thành bản vẽ thiết kế Figma đầu tiên; Văn Hiến thực hiện rà soát, đánh giá cấu trúc UX & SEO tiêu chuẩn (Văn Hiến).
- **v1.2 (2026-06-09):** Tích hợp quy chuẩn quản lý trạng thái xuất bản bài viết (Page Lifecycle Status Model) nhằm tối ưu kiểm duyệt và ngăn chặn lỗi SEO 404 trực tiếp tại Mục 2.5 của tài liệu này (Văn Hiến).

---
*Maintained by: Văn Hiến (Web Product Lead) | Last updated: 2026-06-09*
