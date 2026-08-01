# MoSpark - Blog UI/UX Re-Design
Tiêu chuẩn và tối ưu hóa giao diện hiển thị hệ thống Blog

> - **Project Name:** MoSpark Web Platform
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Bảo
> - **PIC:** Hùng (FE/Design - Tiếp nhận sau khi Tuấn nghỉ)
> - **Version:** 1.0 · June 2026

---

## 1. Executive Summary

### 1.1. Bối cảnh (Situation)
Blog của MoMo hiện đang phục vụ lượng lớn Web Platform thông qua SEO và Social. Tuy nhiên, UI/UX hiện tại chưa được tối ưu triệt để để giữ chân người dùng (Retention), tạo dựng độ tin cậy chuyên gia (E-E-A-T), và tận dụng lượng traffic khổng lồ này để chuyển đổi về App (Web-to-App).

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

1. **Product Design (Hùng):** Chịu trách nhiệm thiết kế layout, UI components, responsive behavior (Desktop/Mobile) dựa trên brief này (Tiếp nhận và phụ trách sau khi Tuấn nghỉ).
2. **Web Product Lead (Văn Hiến):** Rà soát bản thiết kế để đảm bảo không vi phạm các rào cản về SEO (CWV, E-E-A-T) trước khi đưa sang đội Engineering.
3. **Engineering Team:** Dựng component và cấu hình liên kết (Schema mapping, Ads logic) trong MoSpark Editor. Tích hợp quản trị vòng đời trạng thái của bài viết (Draft -> Review -> Live -> Deleted) bám sát các tiêu chuẩn kỹ thuật (HTTP codes, Sitemap, Robots, Canonical) được định nghĩa tại [Mục 2.5 Quy Chuẩn Quản Trị Trạng Thái & CRUD Bài Viết](#2.5.-quy-chuẩn-quản-trị-trạng-thái--crud-bài-viết-seo--content).

---

## 4. Acceptance Criteria & JTBD Scorecard (Prototype)

**Prototype Link:** `08_PRD/blog-redesign/prototype-detail-page.html`

### 4.1. User Jobs & Features Mapping

| # | User Job (JTBD) | Nhu cầu người dùng | UI/Feature giải quyết | Vị trí trên trang |
|---|---|---|---|---|
| **J1** | **Chia sẻ bài viết** | Lan truyền nội dung hữu ích đến mạng lưới cá nhân nhanh chóng. | **Share Bar** | Sticky hoặc cạnh tiêu đề |
| **J2** | **Xác minh độ tin cậy** | Xác thực chuyên môn và danh tính tác giả đối với các nội dung YMYL. | **Author Box** | Đầu bài (mini) + Cuối bài (full) |
| **J3** | **Đọc nhanh trước khi đọc sâu** | Nắm bắt nhanh các ý chính của bài viết dài trong thời gian ngắn (Skimming). | **AI Summarize** | Ngay dưới H1 + Author mini |
| **J4** | **Điều hướng nội dung dài** | Định vị nhanh và chuyển hướng ngay đến các tiểu mục chứa thông tin quan tâm. | **TOC (Mục lục)** | Dưới AI Summary, sticky sidebar (desktop) |
| **J5** | **Khám phá sản phẩm MoMo** | Tiếp cận các sản phẩm, dịch vụ phù hợp được hệ thống gợi ý theo ngữ cảnh. | **Ads Placements** | In-feed, In-content, Sticky bottom, Floating sidebar |

### 4.2. Acceptance Criteria (Must-have) & Scorecard

**Mục tiêu bàn giao:** Prototype phải đạt tối thiểu 24/27 tiêu chí (≥ 89%) trước khi chuyển cho team Engineering.

| Job | Tiêu chí (Acceptance Criteria) | Trạng thái Prototype |
|---|---|---|
| **J1 - Share Bar** | 1. Có bộ nút Share (Copy Link, Facebook, Zalo, X)<br>2. Mobile: Icon share trên Header bar<br>3. Desktop: Icon share cạnh tiêu đề<br>4. Click Copy Link → hiện toast "Đã sao chép" | ✅ Đạt (4/4) |
| **J2 - Author Box** | 1. Mini (Đầu bài): Avatar 32px + Tên + Chức danh<br>2. Full (Cuối bài): Avatar 64px + Tên + Chức danh + Bio + Social icons<br>3. Tên tác giả có thể click (link/anchor)<br>4. Responsive: Không bị vỡ trên mobile 320px | ✅ Đạt (4/4) |
| **J3 - AI Summarize**| 1. Vị trí: Dưới Author Mini, trước TOC<br>2. Icon ✦ (Sparkles) + badge "AI Tóm tắt"<br>3. Background gradient nhạt hoặc nổi bật<br>4. Nội dung: 3-4 bullet points<br>5. Mobile: Có thể collapsible | ✅ Đạt (5/5) |
| **J4 - TOC** | 1. Tự động render từ các thẻ H2<br>2. Mobile: Collapsible box (mặc định đóng)<br>3. Desktop: Sticky sidebar, highlight mục đang đọc<br>4. Click → smooth scroll đến heading | ✅ Đạt (4/4) |
| **J5 - Ads Placements** | 1. In-content: 1 slot sau H2 đầu tiên (có skeleton)<br>2. Sticky Bottom (Mobile): Banner 60px có nút X đóng<br>3. Floating Sidebar (Desktop): Cột phải, cuộn theo nội dung<br>4. Tất cả ads slot phải có skeleton loading (tránh CLS)<br>5. Ads slot phải có kích thước cố định | ✅ Đạt (5/5) |
| **General** | 1. Hero Image: Edge-to-edge mobile, 16:9 ratio<br>2. In-post Image: Caption + Nguồn + Bo góc 8px<br>3. Font: Inter hoặc Roboto<br>4. Brand color: #A5006D (Primary)<br>5. Hiệu năng: Hero image tĩnh, không animation nặng | ✅ Đạt (5/5) |

**Kết quả đánh giá Prototype:** 27/27 (100%) - Đủ điều kiện bàn giao cho Dev.

---

## 5. Change Log
- **v1.0 (2026-06-01):** Khởi tạo tài liệu. Định nghĩa 4 tính năng cốt lõi cho đợt Re-Design: Ads Placements, AI Summarize, Author Box, và Image Display Optimization (Văn Hiến).
- **v1.1 (2026-06-09):** Tuấn hoàn thành bản vẽ thiết kế Figma đầu tiên; Văn Hiến thực hiện rà soát, đánh giá cấu trúc UX & SEO tiêu chuẩn (Văn Hiến).
- **v1.2 (2026-06-09):** Tích hợp quy chuẩn quản lý trạng thái xuất bản bài viết (Page Lifecycle Status Model) nhằm tối ưu kiểm duyệt và ngăn chặn lỗi SEO 404 trực tiếp tại Mục 2.5 của tài liệu này (Văn Hiến).
- **v1.3 (2026-06-14):** Bổ sung mục 4. Acceptance Criteria & JTBD Scorecard để làm tiêu chuẩn đánh giá Prototype trước khi bàn giao Dev (Văn Hiến).

---
*Maintained by: Văn Hiến (Web Product Lead) | Last updated: 2026-06-14*
