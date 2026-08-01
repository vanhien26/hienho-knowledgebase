# BÁO CÁO TÓM TẮT ĐỊNH HƯỚNG DỰ ÁN: VEHICLE HUB (WEB PLATFORM)

> **Mục đích:** Báo cáo tóm tắt tổng thể chiến lược định hướng, quy hoạch sitemap, mục tiêu KPI và khung triển khai phối hợp giữa **Khối Web Platform** và các Cell Teams (**VTTI & Insurtech**) xây dựng hệ sinh thái **Vehicle Hub - Tiện Ích Giao Thông** trên Kênh Web MoMo.

---

## I. BỐI CẢNH & TẦM NHÌN CHIẾN LƯỢC

### 1. Vấn Đề Cốt Lõi
Hàng triệu chủ xe ô tô và xe máy tại Việt Nam đang bị phân mảnh thông tin, phải chuyển qua lại giữa nhiều website rời rạc để tra cứu phạt nguội, theo dõi hạn đăng kiểm, tìm cây xăng, trạm sạc, cứu hộ và mua bảo hiểm. Nếu chỉ tập trung dịch vụ trong ứng dụng di động (In-App), MoMo sẽ lãng phí hơn **12.6 triệu lượt tìm kiếm tự nhiên/tháng** ngoài Open Web.

### 2. Tầm Nhìn & Phễu Tăng Trưởng (Product-Led Growth Funnel)
Vehicle Hub trên Web đóng vai trò là kênh thu hút người dùng có nhu cầu chủ động ngoài Open Web, sau đó điều hướng trải nghiệm và giữ chân người dùng trong hệ sinh thái MoMo theo phễu 4 bước:

$$\text{Search Demand (Google/AI)} \longrightarrow \text{Web Utility Page} \longrightarrow \text{Vehicle Hub In-App} \longrightarrow \text{Add Vehicle Profile / Transaction}$$

* **Kênh Web (Web Platform):** Thu hút Organic Traffic quy mô lớn, tạo điểm chạm đầu tiên và thu thập Biển số xe (Thẻ Xe Số Level 1).
* **In-App Vehicle Hub (VTTI):** Điểm đến trung tâm lưu trữ và tự động hóa quản lý phương tiện (Vehicle Profile Level 2).
* **Lớp Sản Phẩm Thương Mại (Insurtech & VTTI):** Tạo chuyển đổi doanh thu trực tiếp (Bảo hiểm Ô tô/Xe máy, Phí không dừng ePass/VETC, Phí nộp phạt DVC, Cứu hộ...).

---

## II. MỤC TIÊU KINH DOANH & BẢNG CHỈ TIÊU KPI

### 1. Bảng Chỉ Tiêu Proposal Của Mini App Vehicle Hub (Target Đến 31/12/2026)

| KPI | Mô tả | Target đề xuất (tính đến 31/12/2026) |
| :--- | :--- | :---: |
| **Saved Vehicle User (Level 1)** | Có biển số xe | **100.000 xe** (bao gồm ô tô và xe máy) |
| **Saved Vehicle User (Level 2)** | Có biển số, OCR cà vẹt xe | **140.000 xe** (bao gồm ô tô và xe máy) |
| **Saved Vehicle User (Level 3) - ô tô** | Có đầy đủ data xe (OCR cà vẹt, đăng kiểm) | **20.000 xe** (bao gồm ô tô và xe máy) |
| **Vehicle Hub 90-day Active Rate** | % user có xe quay lại/có hành động trong 90 ngày | **20%** |
| **Service attach rate/vehicle** | Trung bình số service active trên mỗi xe | **1,2 service/xe** |
| **Trigger-to-action rate** | Nhắc hạn/phạt/ETC $\rightarrow$ user xử lý | **15%** |
| **Data reuse rate** | % flow được auto-fill từ Vehicle Profile | **$\ge 40\%$ eligible sessions** |

---

### 2. Bảng Chỉ Tiêu Cam Kết Kênh Web Phase 1 Pilot (T9 - T12/2026)

| STT | Chỉ Số (Key Metric) | Baseline (H1/2026) | Target Phase 1 Pilot (T9 - T12/2026) | Long-Term / H2/2026 Target | Ghi Chú & Định Hướng Thực Thi |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | **MoMo Web Organic Traffic** | 1.8M/tháng | **315.000 Visits** | **1.8M - 2.5M Visits/tháng** | Đạt Search Capture Rate 0.5% - 10% trên các cụm từ khóa cốt lõi |
| 2 | **Qualified Conversion (W2A)** | 12% | **>= 0.5% CVR** | **>25% W2A CR** | Tỷ lệ từ Web Visit sang Thêm xe thành công trong App hoặc Giao dịch |
| 3 | **New Vehicle Profiles (WVP)** | 150K xe | **1.575 Profiles** | **100.000 xe** | Tạo mới Hồ sơ phương tiện thành công trong App từ Kênh Web |
| 4 | **Transactions (Bảo hiểm Ô tô)** | 3.500 đơn | **335 đơn VCX + 707 đơn TNDS** | **1.042 đơn (H2/2026)** | Xuất bản hợp đồng bảo hiểm TNDS & Thân vỏ qua Web |
| 5 | **Transactions (Bảo hiểm Xe máy)**| - | **Top 1 - Top 10 Keywords** | **Top 1 - Top 10 Google** | Cấp ấn chỉ điện tử bảo hiểm TNDS xe máy trực tuyến |
| 6 | **% Auto-fill Completion Rate** | 45% | **>60% CR** | **>= 40% Sessions** | Tự động điền dữ liệu xe từ Vehicle Profile khi mua Bảo hiểm/Nạp ePass |

---

## III. QUY HOẠCH SITEMAP VÀ CẤU TRÚC URL DỰ ÁN

Hệ sinh thái Kênh Web được chia làm **2 Nhóm Cấu Trúc Rõ Ràng**:

### Nhóm A: Trang Chủ & Các Spoke Pages Trực Thuộc Hub (`/tien-ich-giao-thong/*`)

| STT | Tên Trang | URL Canonical | Volume Search/Tháng | Vai Trò & Mô Tả Chức Năng |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Trang Chủ Vehicle Hub** | `/tien-ich-giao-thong` | Master Hub | Cổng định danh Thẻ Xe Số, tích hợp tra phạt nguội & điều hướng 360° |
| 2 | **Giá Xăng Dầu** | `/tien-ich-giao-thong/gia-xang` | **10.100.000** | Cập nhật giá xăng Petrolimex/PVOil, biến động giá chiều Thứ 5 |
| 3 | **Trạm Sạc Xe Điện** | `/tien-ich-giao-thong/tram-sac` | **1.200.000** | Bản đồ vị trí trạm sạc VinFast, V-Green toàn quốc |
| 4 | **Cây Xăng Gần Đây** | `/tien-ich-giao-thong/cay-xang` | **550.000** | Bản đồ vị trí cây xăng Petrolimex/PVOil kết nối phễu thanh toán M4B |
| 5 | **Garage Sửa Xe & Bảo Dưỡng**| `/tien-ich-giao-thong/tim-garage` | **272.000** | Danh sách garage, trung tâm chăm sóc ô tô uy tín theo địa phương |
| 6 | **Đăng Kiểm Xe** | `/tien-ich-giao-thong/dang-kiem` | **180.000** | Tra cứu hạn đăng kiểm, lịch hẹn trung tâm kiểm định |
| 7 | **Hãng Xe & Dòng Xe** | `/tien-ich-giao-thong/hang-xe` | **150.000** | Thông số kỹ thuật, giá niêm yết và chi phí lăn bánh ô tô |
| 8 | **Bãi Đỗ Xe & Giữ Xe** | `/tien-ich-giao-thong/bai-do-xe` | **85.000** | Bản đồ điểm trông giữ xe ô tô / xe máy |
| 9 | **Cứu Hộ Đường Bộ 24/7** | `/tien-ich-giao-thong/cuu-ho` | **45.000** | Tổng đài cứu hộ ô tô, cẩu xe, kích bình ắc quy khẩn cấp |
| 10 | **Định Giá Xe Cũ** | `/tien-ich-giao-thong/dinh-gia-xe` | **14.500** | Công cụ định giá xe ô tô/xe máy cũ, phễu Vay & Bảo hiểm |
| 11 | **Blog Tiện Ích Giao Thông** | `/tien-ich-giao-thong/blog` | Long-tail SEO | Bài viết tư vấn luật giao thông, mẹo bảo dưỡng và kinh nghiệm lái xe |

### Nhóm B: 4 Trang Use Case Độc Lập (Top-Level Standalone Canonical Pages)

| STT | Tên Use Case Standalone | URL Canonical | Volume Search/Tháng | Vai Trò & Điểm Khác Biệt |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Tra Cứu Phạt Nguội** | `/phat-nguoi` | **6.100.000** | Utility độc lập Top 1 Google, tra cứu 0-CAPTCHA real-time |
| 2 | **Bảo Hiểm Ô Tô** | `/bao-hiem-o-to` | **450.000** | Trang bán hàng độc lập cho Bảo hiểm TNDS & Thân vỏ ô tô |
| 3 | **Bảo Hiểm Xe Máy** | `/bao-hiem-xe-may` | **680.000** | Trang bán hàng độc lập cho Bảo hiểm TNDS xe máy online |
| 4 | **Phí Không Dừng (ETC)** | `/phi-khong-dung` | **320.000** | Trang tiện ích nạp tiền & kiểm tra số dư tài khoản ePass / VETC |

---

## IV. KHUNG TRIỂN KHAI PHASE 1: BUILD FOUNDATION (THÁNG 8 - 9/2026)

Song song với kế hoạch go-live Tiện ích Giao thông In-App, 3 Cell Teams (**Web Platform, VTTI & Insurtech**) thống nhất tập trung toàn bộ nguồn lực Phase 1 vào **"Build Foundation"** với 3 Trụ cột cốt lõi:

```
                     ┌───────────────────────────────────────────────┐
                     │     PHASE 1: BUILD FOUNDATION (T8 - T9/2026)  │
                     └───────────────────────┬───────────────────────┘
                                             │
      ┌──────────────────────────────────────┼──────────────────────────────────────┐
      ▼                                      ▼                                      ▼
┌───────────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────┐
│ TRỤ CỘT 1: MOSPARK & GENAI│  │ TRỤ CỘT 2: MASTER HUB PAGE│  │ TRỤ CỘT 3: CORE PILLARS   │
│ Migration Bảo Hiểm Ô Tô/XM│  │ Landing /tien-ich-giao-thong│  │ Chuyên Trang Giá Xăng Dầu │
│ Kích hoạt GenAI Engine    │  │ Tích hợp Tra Phạt Nguội & │  │ Bản Đồ Cây Xăng Gần Đây   │
│ Phủ Keyword Thương Mại    │  │ Xoay quanh Biển Số Xe     │  │ (10.6M Search Volume)     │
└───────────────────────────┘  └───────────────────────────┘  └───────────────────────────┘
```

### 1. Trụ Cột 1: Chuyển Dịch Bảo Hiểm Ô Tô / Xe Máy Sang MoSpark & Kích Hoạt GenAI Engine
* Move 100% hệ thống trang Bảo hiểm Ô tô (`/bao-hiem-o-to`) và Bảo hiểm Xe máy (`/bao-hiem-xe-may`) sang hạ tầng **MoSpark**.
* Kích hoạt **GenAI Content Engine (MoSpark CMS + Claude 3.5)** để tự động sản xuất bài viết pSEO/AIO chuyên sâu, phủ các trang đối tác `/bao-hiem-o-to/doi-tac/{ten-doi-tac}` và bài viết chuẩn SEO/GEO.
* Nâng cao tốc độ nạp trang (<1.5s), chuẩn hóa Schema structured data và tích hợp luồng **Auto-fill dữ liệu từ Vehicle Profile** để tối ưu hóa tỷ lệ chuyển đổi mua bảo hiểm.

### 2. Trụ Cột 2: Master Landing Page `/tien-ich-giao-thong` Tích Hợp Phạt Nguội & Hiển Thị Xoay Quanh Biển Số Xe
* Phát triển Master Landing Page `/tien-ich-giao-thong` làm cổng điều hướng trung tâm.
* Tích hợp công cụ **Tra Cứu Phạt Nguội 0-CAPTCHA** trực tiếp tại Hero Section làm ô nhập liệu chính.
* Xây dựng giao diện **Hiển thị Tiện ích Phương tiện Xoay Quanh Biển Số Xe (Vehicle-Centric Service Promotion / Thẻ Xe Số)**: Ngay sau khi nhập Biển số xe, hệ thống vừa trả ra kết quả phạt nguội, vừa tự động hiển thị trạng thái các dịch vụ xung quanh xe (Bảo hiểm, Hạn đăng kiểm, Định giá xe, Số dư ETC) nhằm thúc đẩy người dùng mở App MoMo để **Thêm phương tiện (Add Vehicle Profile)**.

### 3. Trụ Cột 3: Xây Dựng Các Trang Traffic Pillar Cốt Lõi Chi Cụm Quanh Master Hub
* **Chuyên trang Giá Xăng Dầu (`/tien-ich-giao-thong/gia-xang`):** Hứng **10.1M search/tháng**, tạo thói quen quay lại định kỳ mỗi chiều Thứ 5 hàng tuần.
* **Local GEO Cây Xăng Gần Đây (`/tien-ich-giao-thong/cay-xang`):** Hứng **550K search/tháng**, kết nối trực tiếp phễu O2O quét mã thanh toán Petrolimex/PVOil qua MoMo.

---

## V. MÔ HÌNH PHỐI HỢP GIỮA CÁC CELL TEAMS

Dự án được vận hành theo mô hình phối hợp 3 bên chặt chẽ:

### 1. Business Owners (Cell Teams VTTI & Insurtech)
* **Business Ownership:** Nắm giữ quyền quyết định và chịu trách nhiệm toàn trình đối với kết quả kinh doanh (Doanh thu Bảo hiểm, GTV nạp ePass, Phí dịch vụ nộp phạt DVC, Số lượng đơn hàng).
* **Domain Strategy:** Hoạch định chiến lược kinh doanh dịch vụ giao thông & bảo hiểm, quản lý đối tác (PVI, Bảo Việt, MIC, ePass, VETC, Petrolimex, VinFast) và cung cấp Deeplink W2A tự động truyền tham số Biển số xe.

### 2. Web Platform (Product & Tech Partner)
* **Product & Growth Ownership:** Sở hữu, định hướng và vận hành Kênh Web (`/tien-ich-giao-thong`), Tỷ lệ Chuyển đổi (CR), Hạ tầng Kỹ thuật (MoSpark) và Tăng trưởng Organic Traffic.
* **Trọng tâm thực thi:**
  * **Product-Led Growth (PLG):** Xây dựng luồng Web-to-Vehicle-to-App (W2V2A) biến Traffic tự nhiên ngoài Open Web thành tệp Hồ sơ xe định danh.
  * **MoSpark Infrastructure Migration:** Chuyển đổi hệ thống Web sang MoSpark để chịu tải lớn và nâng cao tốc độ ra mắt tính năng.
  * **GenAI Automation Engine:** Ứng dụng AI tự động hóa sản xuất và tối ưu hóa nội dung pSEO/AIO theo Content Plan.
