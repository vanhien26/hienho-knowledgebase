# MASTER WEB PRODUCT PRD TEMPLATE

> **Mục đích:** Template chuẩn hóa dành cho **Web Platform** để xây dựng Đặc tả Yêu cầu Sản phẩm Kênh Web (Web Product PRD) theo cấu trúc 4 Phần Tiêu Chuẩn: Overview, Market Research, Product Structure (Site, Content & Umami Tracking) và SEO/GEO On-Page.

---

## THÔNG TIN TỔNG QUAN (METADATA)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạng Mục</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi Tiết</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tên Sản Phẩm / Use Case</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Tên Sản Phẩm Web - Ví dụ: Vehicle Hub / Tra Cứu Phạt Nguội / Bảo Hiểm]</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Canonical Root URL</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/[product-slug]/</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trạng Thái Tài Liệu</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><em></em>[ ] DRAFT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[ ] UNDER REVIEW</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[ ] APPROVED</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[ ] IN BUILD</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[ ] LIVE<em></em></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Governance</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Product Lead:</strong> [Tên] \</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Lead Engineer:</strong> [Tên] \</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Business Owner:</strong> [Tên] \</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>PMM:</strong> [Tên]</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Mốc Tiến Độ Dự Kiến</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kick-off: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[DD/MM/YYYY]</code>  ➔  Dev Test: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[DD/MM/YYYY]</code>  ➔  Pilot: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[DD/MM/YYYY]</code>  ➔  Go-Live: <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[DD/MM/YYYY]</code></td>
    </tr>
  </tbody>
</table>

---

## 1. PRODUCT OVERVIEW

### 1.1 Elegant Framing
[Định vị sản phẩm bằng văn phong sắc bén, ngắn gọn, chỉ ra lý do tồn tại cốt lõi của Kênh Web. Giải thích tại sao sản phẩm này là điểm chạm quan trọng ngoài Open Web để tiếp cận tệp người dùng chưa tải App...]

### 1.2 Product Vision & PLG Funnel
Tầm nhìn dài hạn của sản phẩm và phễu tăng trưởng Product-Led Growth (PLG) 4 bước:

$$Search Demand (Google/AI)\longrightarrow Web Utility Page\longrightarrow In-App Product/Hub\longrightarrow User Acquisition / Transaction$

* **Kênh Web (Web Platform):** Thu hút Organic Traffic quy mô lớn, tạo điểm chạm đầu tiên giải quyết nhu cầu tìm kiếm tức thời và thu thập dữ liệu định danh đầu vào.
* **In-App Product (BU Owner):** Điểm đến lưu trữ, quản lý và tự động hóa trải nghiệm sản phẩm sâu (Retention & Engagement).
* **Lớp Sản Phẩm Thương Mại:** Tạo chuyển đổi doanh thu trực tiếp (Doanh thu bán hàng, Phí dịch vụ, GTV...).

---

## 2. MARKET RESEARCH

### 2.1 Market Sizing & Opportunity
* **Dung lượng thị trường (Addressable Market Size):** [Quy mô tổng quan thị trường, tệp người dùng mục tiêu và tài sản dữ liệu hiện có trên MoMo...]
* **Dung lượng từ khóa trên Kênh Web (Monthly Search Volume):** [Tổng lượng tìm kiếm hàng tháng của ngành/use case trên Open Web...]

### 2.2 Competitor Gap Analysis
* **Thực trạng đối thủ bên thứ ba:** [Phân tích điểm yếu của các website đối thủ hiện tại (Ví dụ: UX kém, bắt giải CAPTCHA phức tạp, chứa nhiều quảng cáo rác, thiếu cổng thanh toán)...]
* **Cơ hội bứt phá của MoMo (MoMo Advantage):** [Điểm khác biệt vượt trội của Kênh Web MoMo (0-CAPTCHA, UI/UX hiện đại, đồng bộ dữ liệu In-App, bảo chứng thương hiệu uy tín)...]

### 2.3 User Pain Points & Search Demand Inventory
* **User Pain Points:** [Mô tả chi tiết 3-4 nỗi đau lớn nhất của người dùng khi tìm kiếm và sử dụng dịch vụ trên Web...]
* **Search Demand Inventory:**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm Nhu Cầu (Search Cluster)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mẫu Từ Khóa Tìm Kiếm (Query Examples)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Monthly Search Volume</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại Intent (Search Intent)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nhóm 1: Core Utility</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Từ khóa 1]</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Từ khóa 2]</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">[Volume]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactional / High-Intent</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nhóm 2: Informational</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Từ khóa 3]</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Từ khóa 4]</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">[Volume]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Informational / Research</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nhóm 3: Local GEO</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Từ khóa 5]</code>, <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Từ khóa 6]</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">[Volume]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Local Intent / O2O</td>
    </tr>
  </tbody>
</table>

---

## 3. PRODUCT STRUCTURE

### 3.1 Site Structure (Silo Sitemap & Routing Rules)
Cấu trúc Kênh Web được chia thành **2 Nhóm Cấu Trúc Rõ Ràng**:

#### Nhóm A: Trang Chủ Hub & Các Spoke Pages Trực Thuộc (`/[hub-slug]/*`)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Trang / Sub-page</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Canonical</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Phân Cấp Routing</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai Trò Trong Cấu Trúc Sitemap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trang Chủ Hub</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/[hub-slug]/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Master Hub Root</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cổng tổng điều hướng 360°, tích hợp công cụ tra cứu trung tâm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Spoke Page 1]</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/[hub-slug]/[spoke-1]/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang tiện ích / thông tin chuyên sâu 1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Spoke Page 2]</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/[hub-slug]/[spoke-2]/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang bản đồ địa điểm GEO 2</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Blog / Cẩm Nang</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/[hub-slug]/blog/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Spoke Sub-page</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang bài viết tư vấn, hướng dẫn và thông tin ngành</td>
    </tr>
  </tbody>
</table>

#### Nhóm B: Các Trang Use Case Độc Lập (Top-Level Standalone Canonical URLs)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Use Case Standalone</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">URL Canonical</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Phân Cấp Routing</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Vai Trò & Điểm Khác Biệt Trong Cấu Trúc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Use Case Standalone 1]</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/[usecase-1-slug]/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Root Standalone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Utility/Landing độc lập Top 1 Google cho use case 1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Use Case Standalone 2]</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/[usecase-2-slug]/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Root Standalone</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Trang bán hàng độc lập phục vụ sản phẩm thương mại 2</td>
    </tr>
  </tbody>
</table>

#### Quy Chuẩn Routing URL Technical Rules:
1. **Case Sensitivity:** 100% URL viết chữ thường (lowercase).
2. **Trailing Slash:** Tất cả URL kết thúc bằng dấu gạch chéo `/`.
3. **Canonical Reference:** 100% trang bắt buộc có thẻ `<link rel="canonical" href="..." />` trỏ về chính URL chuẩn tuyệt đối.

---

### 3.2 Content Structure Từng Trang (Functions, Components & UI Specifications)

Bảng đặc tả cấu trúc nội dung chi tiết từng khối thành phần cho từng loại trang:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trang / Phân Hệ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Component / Section</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhu Cầu Người Dùng (JTBD)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải Pháp Cấu Trúc (Solution)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thành Phần UI (UI Components) & Functions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Master Hub</strong><br><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/[hub-slug]/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hero & Master Search</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn tra cứu/sử dụng tiện ích ngay lập tức."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Ô nhập liệu thông minh 1-click + Button Action.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Headline H1 + Input Field + Nút Action 1-click</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Quick Utilities Grid</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn truy cập nhanh các tiện ích phổ biến."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Grid 6 Card phím tắt điều hướng 6 Spoke cốt lõi.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Grid 6 Card phím tắt tiện ích</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Real-time Data Feed</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn xem dữ liệu biến động thời gian thực."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dynamic Feed dữ liệu cập nhật thời gian thực.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảng dữ liệu / Map Widget vị trí lân cận</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Local GEO Selector</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn lọc địa điểm tại khu vực sắp di chuyển đến."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dropdown lọc Tỉnh/Thành  ➔  Quận/Huyện.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Dropdown chọn Tỉnh/Thành  ➔  Quận/Huyện</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>FAQ Accordion Block</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn giải đáp thắc mắc thường gặp."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Accordion Q&A gắn Schema <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">FAQPage</code>.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Accordion list các câu hỏi & câu trả lời</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Standalone Page]</strong><br><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/[usecase-slug]/</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hero & Tool Input</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn sử dụng công cụ tra cứu/báo giá ngay."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Form nhập liệu trực tiếp bypass CAPTCHA.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Form nhập thông tin + Nút Tra cứu / Báo giá</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Result & Smart CTA</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn xem kết quả và thực hiện giao dịch."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Output màn hình kết quả + Smart CTA mở App MoMo.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khối hiển thị kết quả + Banner CTA Web-to-App</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>SEO Explanatory Block</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Tôi muốn đọc hướng dẫn và bảng tra chi tiết."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nội dung bài viết tư vấn chuẩn SEO 800-1200 từ.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bài viết hướng dẫn từng bước & Bảng tra chi tiết</td>
    </tr>
  </tbody>
</table>

---

### 3.3 Umami Event Tracking theo Touchpoint

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Touchpoint / Vị Trí Tương Tác</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành Động Người Dùng (User Action)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Umami Event Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Hero Search Form</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm nút Tra cứu / Tìm kiếm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">search_submit</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Smart W2A CTA Banner</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm nút điều hướng mở App MoMo</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">w2a_click</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Quick Utilities Grid</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm phím tắt dịch vụ trên Hub</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">utility_click</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>GEO Filter Bar</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chọn bộ lọc Tỉnh/Thành, Quận/Huyện, Loại danh mục</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">filter_select</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Merchant Card Snippet</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm vào thẻ địa điểm chi tiết</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">merchant_click</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Form Báo Giá / Mua Hàng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bấm nút xem báo giá / mua sản phẩm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">form_submit</code></td>
    </tr>
  </tbody>
</table>

---

## 4. SEO / GEO ONPAGE

### 4.1 Meta Data (Title, Description, Headings, OpenGraph & Social Cards)

#### A. Công Thức Meta Tag Standards

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại Trang</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Công Thức Tag <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><title></code> (Max 60 chars)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Công Thức <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;"><meta description></code> (150-160 chars)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Master Hub</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Tên Hub] MoMo - [Lợi ích cốt lõi] 3 Phút</code></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Mô tả tổng quan hệ sinh thái + danh sách tiện ích chính + Call-to-action trên MoMo.]</code></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Standalone Use Case</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">`[Tên Use Case] Online (Không CAPTCHA)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo`</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Mô tả ngắn chứa từ khóa chính + tính năng nổi bật + Lời kêu gọi hành động.]</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Spoke GEO Page</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">`Bản Đồ [Tên Tiện Ích] Gần Đây</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo`</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">[Mô tả tìm vị trí trạm/garage gần nhất + bộ lọc địa phương + chỉ đường Google Maps.]</code></td>
    </tr>
  </tbody>
</table>

#### B. Quy Chuẩn Heading Hierarchy (H1 - H4)
* **Quy tắc H1:** Mỗi trang có duy nhất **1 thẻ `<h1>`** đặt tại Hero Section chứa từ khóa chính.
* **Cấu trúc phân cấp chuẩn:**
  ```text
  H1: [Từ khóa chính trang]
     ├── H2: [Tính năng / Công cụ tra cứu cốt lõi]
     ├── H2: [Bảng thông tin / Dữ liệu thời gian thực]
     ├── H2: [Hướng dẫn chi tiết luồng sử dụng]
     │      ├── H3: [Bước 1: ...]
     │      └── H3: [Bước 2: ...]
     └── H2: [Câu hỏi thường gặp (FAQ Accordion)]
  ```

#### C. Social Share Cards Structure (OpenGraph & Twitter)
```html
<meta property="og:type" content="website" />
<meta property="og:title" content="[Title Social Share]" />
<meta property="og:description" content="[Description Social Share]" />
<meta property="og:image" content="https://img.mservice.io/[product-slug]/og-[page-slug].jpg" />
<meta property="og:url" content="https://momo.vn/[product-slug]/[page-slug]/" />
<meta name="twitter:card" content="summary_large_image" />
```

---

### 4.2 Schema.org JSON-LD Specifications

Mỗi loại trang bắt buộc khai báo mã JSON-LD chuẩn trong thẻ `<head>`:

#### A. Master Hub Page (`/[hub-slug]/`)
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://momo.vn/#website",
      "url": "https://momo.vn/",
      "name": "MoMo"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://momo.vn/" },
        { "@type": "ListItem", "position": 2, "name": "[Tên Hub]", "item": "https://momo.vn/[hub-slug]/" }
      ]
    }
  ]
}
```

#### B. Standalone Utility Page (`/[usecase-slug]/`)
Khai báo Schema `@type`: `WebApplication`, `GovernmentService` (nếu có), `FAQPage`.

#### C. GEO Local Pages (`/tram-sac/`, `/tim-garage/`, `/bai-do-xe/`)
Khai báo Schema `@type`: `LocalBusiness` / `AutomotiveBusiness` / `EVChargingStation` / `ParkingFacility`.

---

### 4.3 Sitemap & Technical SEO

1. **Cấu trúc Sub-Sitemaps Index (`sitemap_index.xml`):**
   * `sitemap-[product]-hub.xml`: Trang chủ Hub & các Spoke Pages (`priority: 1.0`, `changefreq: daily`).
   * `sitemap-[product]-standalone.xml`: Các trang Standalone Root-Level (`priority: 0.9`, `changefreq: daily`).
   * `sitemap-merchant.xml`: Các trang chi tiết Merchant đối tác (`priority: 0.6`, `changefreq: weekly`).
2. **Quy tắc Quản lý Crawl Budget:** Trả mã HTTP `410 Gone` và xóa khỏi Sitemap đối với các trang Merchant ngưng hoạt động.
3. **Canonical Rules:** 100% trang có thẻ canonical tự tham chiếu tuyệt đối.

---

### 4.4 GEO / AIO (Generative Engine Optimization cho AI Search)

Để tối ưu khả năng xuất hiện trên Google AI Overview, ChatGPT, Perplexity và Gemini:

1. **Direct Answer Block (25 - 40 từ):** Ngay dưới mỗi tiêu đề `<h2>` của khối FAQ hoặc Hướng dẫn, bắt buộc chứa 1 câu trả lời tóm tắt trực tiếp định dạng Entity-Attribute-Value:
   * *Ví dụ:* **"[Tên dịch vụ] trên MoMo cho phép người dùng [Hành động] trực tuyến trong 1 phút bằng cách [Các bước chính] mà không cần [Rào cản cũ]."**
2. **Minified HTML Tables:** Đóng gói toàn bộ dữ liệu so sánh, bảng giá, bảng tra cứu bằng thẻ `<table>` HTML chuẩn với `<thead>` và `<tbody>` rõ ràng để AI Bot dễ trích xuất.
3. **Authoritative Citations:** Chèn dẫn nguồn tham chiếu trực tiếp đến các cổng thông tin chính phủ / văn bản pháp luật / đối tác chính thức.
