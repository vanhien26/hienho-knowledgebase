# MASTER TEMPLATE: BÁO CÁO TÓM TẮT ĐỊNH HƯỚNG DỰ ÁN & USE CASE (WEB PLATFORM)

> **Mục đích:** Template chuẩn hóa dành cho **Web Platform** để lập Báo cáo tóm tắt định hướng dự án/use case, chốt quy hoạch sitemap, mục tiêu KPI và khung thực thi phối hợp với các **Cell Teams / Business Units (BUs)**.

---

## I. BỐI CẢNH & TẦM NHÌN CHIẾN LƯỢC

### 1. Vấn Đề Cốt Lõi
[Mô tả ngắn gọn 2-3 câu về pain point của thị trường/người dùng hiện tại và cơ hội tăng trưởng khi mở rộng kênh Web Out-App...]

### 2. Tầm Nhìn & Phễu Tăng Trưởng (Product-Led Growth Funnel)
[Dự án / Use Case] đóng vai trò là kênh thu hút người dùng có nhu cầu chủ động ngoài Open Web, sau đó điều hướng trải nghiệm và giữ chân người dùng trong hệ sinh thái MoMo theo phễu 4 bước:

$$\text{Search Demand (Google/AI)} \longrightarrow \text{Web Utility Page} \longrightarrow \text{In-App Product/Hub} \longrightarrow \text{User Acquisition / Transaction}$$

* **Kênh Web (Web Platform):** Thu hút Organic Traffic quy mô lớn, tạo điểm chạm đầu tiên và thu thập dữ liệu đầu vào.
* **In-App Product ([TÊN BU VẬN HÀNH]):** Điểm đến trung tâm lưu trữ và quản lý trải nghiệm sản phẩm sâu (Feature & Retention).
* **Lớp Sản Phẩm Thương Mại:** Tạo chuyển đổi doanh thu trực tiếp (Doanh thu bán hàng, Phí dịch vụ, GTV...).

---

## II. MỤC TIÊU KINH DOANH & BẢNG CHỈ TIÊU KPI

### Bảng Chỉ Tiêu Cam Kết [QUÝ/NĂM] & Long-Term Target

| Chỉ số (Metric) | Baseline ([Kỳ trước]) | Target Phase 1 / Short-term | Target Long-term / H2 | Ghi chú & Định hướng thực thi |
| :--- | :---: | :---: | :---: | :--- |
| **Organic Traffic** | [Số liệu] | **[Target Phase 1]** | **[Target Long-term]** | Search Capture Rate trên các Use Cases ưu tiên |
| **Qualified Conversion (W2A)** | [Số liệu %] | **[>= Target %]** | **[Target Long-term]** | Tỷ lệ từ Web Visit sang mở App hoặc Giao dịch |
| **New Users / Profiles** | [Số liệu] | **[Target Phase 1]** | **[Target Long-term]** | Số lượng người dùng/định danh tạo mới |
| **Transactions / Conversions**| [Số liệu] | **[Target Phase 1]** | **[Target Long-term]** | Sản lượng đơn hàng/giao dịch thực tế |
| **% Auto-fill / Completion CR**| [Số liệu %] | **[> Target %]** | **[Target Long-term]** | Tỷ lệ tự động điền dữ liệu & hoàn tất luồng |

---

## III. QUY HOẠCH SITEMAP VÀ CẤU TRÚC URL DỰ ÁN

Hệ sinh thái Kênh Web được chia làm **2 Nhóm Cấu Trúc Rõ Ràng**:

### Nhóm A: Trang Chủ & Các Spoke Pages Trực Thuộc Hub (`/[hub-slug]/*`)

| STT | Tên Trang | URL Canonical | Volume Search/Tháng | Vai Trò & Mô Tả Chức Năng |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Trang Chủ Hub** | `/[hub-slug]` | Master Hub | Cổng tổng điều hướng 360°, tích hợp công cụ tra cứu trung tâm |
| 2 | **[Tên Spoke Page 1]** | `/[hub-slug]/[spoke-1]` | [Volume Search] | [Chức năng & Phễu chuyển đổi của Spoke 1] |
| 3 | **[Tên Spoke Page 2]** | `/[hub-slug]/[spoke-2]` | [Volume Search] | [Chức năng & Phễu chuyển đổi của Spoke 2] |
| 4 | **Blog / Cẩm Nang** | `/[hub-slug]/blog` | Long-tail SEO | Bài viết tư vấn chuyên sâu, hướng dẫn và thông tin ngành |

### Nhóm B: Các Trang Use Case Độc Lập (Top-Level Standalone Canonical Pages)

| STT | Tên Use Case Standalone | URL Canonical | Volume Search/Tháng | Vai Trò & Điểm Khác Biệt |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **[Use Case Standalone 1]** | `/[usecase-1-slug]` | [Volume Search] | Utility/Landing độc lập Top 1 Google cho use case 1 |
| 2 | **[Use Case Standalone 2]** | `/[usecase-2-slug]` | [Volume Search] | Trang bán hàng độc lập phục vụ sản phẩm thương mại 2 |

---

## IV. KHUNG TRIỂN KHAI PHASE 1: BUILD FOUNDATION

Tập trung nguồn lực giai đoạn đầu vào việc **"Build Foundation"** với 3 Trụ cột cốt lõi:

### 1. Trụ Cột 1: [Tên Trụ Cột 1 - Ví dụ: MoSpark Infrastructure & GenAI Engine]
* Move/xây dựng hệ thống trang trên hạ tầng **MoSpark**.
* Kích hoạt **GenAI Content Engine** để tự động sản xuất bài viết pSEO/AIO chuyên sâu.
* Nâng cao tốc độ nạp trang (<1.5s) và tối ưu hóa luồng chuyển đổi.

### 2. Trụ Cột 2: [Tên Trụ Cột 2 - Ví dụ: Master Landing Page & Core Input Engine]
* Phát triển Master Landing Page làm cổng điều hướng trung tâm.
* Tích hợp công cụ tra cứu cốt lõi tại Hero Section làm "tín hiệu đầu vào".
* Xây dựng giao diện hiển thị dịch vụ đính kèm để đẩy chuyển đổi sang App.

### 3. Trụ Cột 3: [Tên Trụ Cột 3 - Ví dụ: High-Traffic Core Pillar Pages]
* Triển khai các chuyên trang Spoke có search volume lớn bao quanh Hub.
* Kết nối trực tiếp phễu O2O và giao dịch thực tế trên MoMo.

---

## V. MÔ HÌNH PHỐI HỢP GIỮA CÁC CELL TEAMS

Dự án được vận hành theo mô hình đối tác chiến lược giữa **[TÊN BU VẬN HÀNH]** và **Khối Web Platform**:

### 1. Business Owners ([TÊN BU VẬN HÀNH])
* **Business Ownership:** Nắm giữ quyền quyết định và chịu trách nhiệm toàn trình đối với kết quả kinh doanh (P&L, Doanh thu, New Users, Transactions).
* **Domain Strategy:** Hoạch định chiến lược kinh doanh ngành, quản lý hệ sinh thái đối tác và cung cấp Deeplink/API tích hợp.

### 2. Web Platform (Product & Tech Partner)
* **Product & Growth Ownership:** Sở hữu, định hướng và vận hành Kênh Web (`/[hub-slug]`), Tỷ lệ Chuyển đổi (CR), Hạ tầng Kỹ thuật (MoSpark) và Tăng trưởng Organic Traffic.
* **Trọng tâm thực thi:**
  * **Product-Led Growth (PLG):** Xây dựng luồng Web-to-App biến Traffic tự nhiên ngoài Open Web thành tệp người dùng định danh.
  * **MoSpark Infrastructure Migration:** Hiện đại hóa hạ tầng Web sang MoSpark để chịu tải lớn và tăng tốc độ ra mắt tính năng.
  * **GenAI Automation Engine:** Ứng dụng AI tự động hóa sản xuất và tối ưu hóa nội dung pSEO/AIO.
