# ĐẶC TẢ YÊU CẦU SẢN PHẨM (PRD) - VEHICLE HUB (KÊNH WEB & HỒ SƠ PHƯƠNG TIỆN)

> **Mục đích:** Tài liệu Đặc tả Yêu cầu Sản phẩm Kênh Web (Web Product PRD) chính thức dành cho dự án **Vehicle Hub - Tiện Ích Giao Thông**, xây dựng theo chuẩn 4 Phần Tiêu Chuẩn: Overview, Market Research, Product Structure (Site, Content & Umami Touchpoints) và SEO/GEO On-Page.

---

## THÔNG TIN TỔNG QUAN (METADATA)

| Hạng Mục | Chi Tiết |
| :--- | :--- |
| **Tên Sản Phẩm / Use Case** | **Tiện Ích Giao Thông (Vehicle Hub Web Platform & Vehicle Identity)** |
| **Canonical Root URL** | `momo.vn/tien-ich-giao-thong/` & `momo.vn/phat-nguoi/` |
| **Trạng Thái Tài Liệu** | **APPROVED (Execution Phase)** |
| **Governance** | **Web Product Lead:** Hien.ho \| **Lead Engineer:** Web Platform Tech Lead \| **Business Owners:** VTTI Lead x Insurtech Lead |
| **Mốc Tiến Độ Dự Kiến** | Kick-off: `06/07/2026` $\rightarrow$ Build Phase 1: `01/08/2026` $\rightarrow$ Pilot: `01/09/2026` $\rightarrow$ Go-Live: `30/09/2026` |

---

## 1. PRODUCT OVERVIEW

### 1.1 Elegant Framing
Hàng triệu chủ xe ô tô và xe máy tại Việt Nam đang bị phân mảnh thông tin, phải chuyển qua lại giữa 5–7 ứng dụng và website rời rạc chỉ để xử lý các nhu cầu thiết yếu: tra phạt nguội, xem giá xăng, nạp tiền ETC, theo dõi hạn đăng kiểm, tìm trạm sạc và mua bảo hiểm. Nếu chỉ cung cấp dịch vụ trong ứng dụng di động đóng (App-only ecosystem), MoMo sẽ hoàn toàn vô hình trước hơn **12.6 triệu lượt tìm kiếm tự nhiên/tháng** ngoài Open Web.

**Vehicle Hub trên Web (`momo.vn/tien-ich-giao-thong`)** ra đời như một **"Cổng Định Danh & Điểm Đến Tiện Ích Xe Mở"**, biến Biển số xe thành chiếc Thẻ Xe Số kết nối lặp lại. Bằng cách cung cấp các tiện ích tra cứu công cộng tốc độ cao (0-CAPTCHA) kết hợp cùng **Nội dung bài viết GenAI Content (Dự án PLG Project)**, Kênh Web giải quyết tức thời nhu cầu của chủ xe ngoài Open Web, khởi tạo Hồ sơ phương tiện (Vehicle Profile) và điều hướng giữ chân người dùng trong hệ sinh thái MoMo.

### 1.2 Product Vision & PLG Funnel
Tầm nhìn dài hạn của dự án là hợp nhất toàn bộ nhu cầu phân mảnh về phương tiện và **rút ngắn tổng thời gian quản lý một chiếc xe xuống dưới 3 phút** trên một nền tảng duy nhất.

Sản phẩm vận hành theo phễu tăng trưởng Product-Led Growth (PLG) 4 bước:

$$\text{Search Demand (Google/AI)} \longrightarrow \text{Web Utility Page / Blog} \longrightarrow \text{Vehicle Hub In-App} \longrightarrow \text{Add Vehicle Profile / Transaction}$$

* **Kênh Web (Web Platform & Blog):** Thu hút Organic Traffic quy mô lớn từ Google & AI Search thông qua Công cụ Tra cứu và Nội dung bài viết GenAI Content (PLG Project).
* **In-App Vehicle Hub (VTTI):** Điểm đến trung tâm lưu trữ và tự động hóa quản lý phương tiện (Vehicle Profile Level 2/3).
* **Lớp Sản Phẩm Thương Mại (Insurtech & VTTI):** Tạo chuyển đổi doanh thu trực tiếp (Bảo hiểm Ô tô/Xe máy, Phí ETC ePass/VETC, Phí nộp phạt DVC, Cứu hộ 24/7).

---

## 2. MARKET RESEARCH

### 2.1 Market Sizing & Opportunity
* **Dung lượng thị trường phương tiện tại Việt Nam:**
  * **Ô tô:** Hơn 5,5 triệu ô tô lưu hành toàn quốc.
  * **Xe máy:** Hơn 72 triệu xe máy đăng ký.
* **Tài sản dữ liệu sẵn có trên hệ thống MoMo:**
  * MoMo sở hữu dữ liệu phương tiện của **~600.000 ô tô** và **~2.000.000 xe máy** (trong đó có hơn **150.000+ ô tô** được định danh chi tiết bằng OCR Cà vẹt).
  * Tỷ lệ trùng lặp dữ liệu giữa mảng Bảo hiểm (FS) và Phạt nguội/ePass (VTTI) hiện rất thấp (**0,3% - 3%**), chứng minh dư địa bán chéo (Cross-sell) cực lớn khi hợp nhất dữ liệu vào Hồ sơ xe.

### 2.2 Competitor Gap Analysis
* **Thực trạng đối thủ bên thứ ba:**
  * Cổng thông tin Cục CSGT (`csgt.vn`) thường xuyên quá tải, chậm cập nhật và yêu cầu mã CAPTCHA phức tạp.
  * Các trang web tra cứu bên thứ ba (như `phatnguoi.com`) chứa nhiều quảng cáo rác, UX kém và **không có khả năng lưu hồ sơ xe hay kết nối thanh toán In-App**.
* **Cơ hội bứt phá của MoMo (MoMo Advantage):**
  * Tra cứu Phạt Nguội tốc độ cao **0-CAPTCHA** real-time.
  * Tích hợp kho bài viết chuẩn tư vấn luật giao thông và mẹo bảo dưỡng sinh tự động từ **GenAI Content Engine (PLG Project)**.
  * Trải nghiệm liền mạch **Web-to-App (W2A)**: Nhập biển số xe 1 lần trên Web $\rightarrow$ Tự động tạo Hồ sơ xe trong App và kích hoạt cảnh báo vi phạm mới qua MoMo.

### 2.3 User Pain Points & Search Demand Inventory

#### A. Nỗi đau lớn nhất của người dùng (User Pain Points)
1. **Trải nghiệm phân mảnh:** Phải gõ lại biển số xe và thông tin cá nhân nhiều lần trên nhiều website độc lập.
2. **Lo sợ vi phạm phạt nguội:** Không biết xe mình có bị dính lỗi phạt nguội hay không cho đến khi đi đăng kiểm.
3. **Thiếu thông tin tư vấn giao thông:** Thiếu nguồn bài viết tư vấn luật giao thông và mẹo bảo dưỡng xe đáng tin cậy.

#### B. Ma trận nhu cầu tìm kiếm trên Open Web (Search Demand Inventory)

| Nhóm Nhu Cầu (Search Cluster) | Mẫu Từ Khóa Tìm Kiếm (Query Examples) | Monthly Search Volume | Loại Intent (Search Intent) |
| :--- | :--- | :---: | :--- |
| **Tra Cứu Phạt Nguội** | `tra cứu phạt nguội`, `phạt nguội csgt`, `tra phạt nguội ô tô` | **6.100.000** | Transactional / High-Intent |
| **Giá Xăng Dầu** | `giá xăng hôm nay`, `giá xăng ron 95`, `kỳ điều hành giá xăng` | **10.100.000** | Freshness / Commercial |
| **Trạm Sạc Xe Điện EV** | `trạm sạc xe điện`, `trạm sạc vinfast gần đây`, `trạm sạc v-green` | **1.200.000** | Local GEO / High-ARPU |
| **Bảo Hiểm Phương Tiện** | `bảo hiểm ô tô`, `bảo hiểm xe máy online`, `bảo hiểm thân vỏ` | **1.130.000** | Commercial / High-Intent |
| **Cây Xăng Gần Đây** | `cây xăng gần đây`, `cây xăng petrolimex`, `cây xăng pvoil` | **550.000** | Local GEO / O2O |
| **Phí Không Dừng (ETC)** | `nạp tiền epass`, `nạp tiền vetc`, `kiểm tra số dư epass` | **320.000** | Utility / Transactional |
| **Garage & Cứu Hộ** | `garage sửa xe ô tô`, `cứu hộ ô tô 24/7`, `bãi đỗ xe ô tô` | **402.000** | Local GEO / Emergency |
| **Đăng Kiểm & Định Giá** | `đăng kiểm xe ô tô`, `định giá xe ô tô cũ`, `bảng giá xe ô tô` | **344.500** | Research / Financial Lead |

---

## 3. PRODUCT STRUCTURE

### 3.1 Site Structure (Silo Sitemap & Routing Rules)

Hệ thống URL Kênh Web Vehicle Hub được quy hoạch thành **2 Nhóm Cấu Trúc Rõ Ràng**:

```
                       ┌─────────────────────────────────────────┐
                       │  MASTER HUB: /tien-ich-giao-thong/      │
                       └────────────────────┬────────────────────┘
                                            │
        ┌───────────────────────────────────┼───────────────────────────────────┐
        ▼                                   ▼                                   ▼
┌───────────────────────────┐   ┌───────────────────────────┐   ┌───────────────────────────┐
│ GROUP A: SPOKE PAGES      │   │ GROUP A: LOCAL GEO PAGES  │   │ GROUP B: STANDALONE PAGES │
│ /gia-xang/                │   │ /tram-sac/                │   │ /phat-nguoi/              │
│ /dang-kiem/               │   │ /cay-xang/                │   │ /bao-hiem-o-to/           │
│ /hang-xe/                 │   │ /tim-garage/              │   │ /bao-hiem-xe-may/         │
│ /dinh-gia-xe/             │   │ /bai-do-xe/               │   │ /phi-khong-dung/          │
│ /cuu-ho/                  │   └─────────────┬─────────────┘   └───────────────────────────┘
│ /blog/ (GenAI Content)    │                 │
└───────────────────────────┘                 ▼
                                ┌───────────────────────────┐
                                │ MERCHANT DETAIL PAGES     │
                                │ /merchant/{merchant-slug}/│
                                └───────────────────────────┘
```

#### Nhóm A: Trang Chủ Hub & Các Spoke Pages Trực Thuộc (`/tien-ich-giao-thong/*`)

| STT | Tên Phân Hệ / Trang | URL Canonical | Phân Cấp Routing | Vai Trò & Chức Năng Trong Cấu Trúc |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Trang Chủ Vehicle Hub** | `/tien-ich-giao-thong/` | Master Hub Root | Cổng tổng điều hướng 360°, định danh Thẻ Xe Số |
| 2 | **Giá Xăng Dầu** | `/tien-ich-giao-thong/gia-xang/` | Spoke Sub-page | Cập nhật giá xăng Petrolimex/PVOil thời gian thực |
| 3 | **Trạm Sạc Xe Điện** | `/tien-ich-giao-thong/tram-sac/` | Spoke Sub-page | Bản đồ vị trí trạm sạc VinFast, V-Green toàn quốc |
| 4 | **Cây Xăng Gần Đây** | `/tien-ich-giao-thong/cay-xang/` | Spoke Sub-page | Bản đồ vị trí cây xăng Petrolimex/PVOil kết nối phễu M4B |
| 5 | **Garage Sửa Xe & Bảo Dưỡng**| `/tien-ich-giao-thong/tim-garage/` | Spoke Sub-page | Danh sách garage, trung tâm chăm sóc ô tô uy tín địa phương |
| 6 | **Đăng Kiểm Xe** | `/tien-ich-giao-thong/dang-kiem/` | Spoke Sub-page | Tra cứu hạn đăng kiểm, lịch hẹn trung tâm kiểm định |
| 7 | **Hãng Xe & Dòng Xe** | `/tien-ich-giao-thong/hang-xe/` | Spoke Sub-page | **Master Data 35 Hãng Xe & 264 Dòng Xe** (`/hang-xe/{brand}/{model}`). Thông số kỹ thuật, chi phí nuôi xe & phễu báo giá Bảo hiểm TNDS/Thân vỏ. |
| 8 | **Bãi Đỗ Xe & Giữ Xe** | `/tien-ich-giao-thong/bai-do-xe/` | Spoke Sub-page | Bản đồ điểm trông giữ xe ô tô / xe máy |
| 9 | **Cứu Hộ Đường Bộ 24/7** | `/tien-ich-giao-thong/cuu-ho/` | Spoke Sub-page | Tổng đài cứu hộ ô tô, cẩu xe, kích bình ắc quy khẩn cấp |
| 10 | **Định Giá Xe Cũ** | `/tien-ich-giao-thong/dinh-gia-xe/` | Spoke Sub-page | Công cụ định giá xe ô tô/xe máy cũ, phễu Vay & Bảo hiểm |
| 11 | **Blog Tiện Ích Giao Thông** | `/tien-ich-giao-thong/blog/` | Spoke Sub-page | **GenAI Content (PLG Project).** Kho bài viết tư vấn luật & mẹo bảo dưỡng xe |

#### Nhóm B: 4 Trang Use Case Độc Lập (Top-Level Standalone Canonical Pages)

| STT | Tên Use Case Standalone | URL Canonical | Phân Cấp Routing | Vai Trò & Điểm Khác Biệt Trong Cấu Trúc |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **Tra Cứu Phạt Nguội** | `/phat-nguoi/` | Root Standalone | Utility độc lập Top 1 Google, tra cứu 0-CAPTCHA real-time |
| 2 | **Bảo Hiểm Ô Tô** | `/bao-hiem-o-to/` | Root Standalone | Trang bán hàng độc lập cho Bảo hiểm TNDS & Thân vỏ ô tô |
| 3 | **Bảo Hiểm Xe Máy** | `/bao-hiem-xe-may/` | Root Standalone | Trang bán hàng độc lập cho Bảo hiểm TNDS xe máy online |
| 4 | **Phí Không Dừng (ETC)** | `/phi-khong-dung/` | Root Standalone | Trang tiện ích nạp tiền & kiểm tra số dư ePass / VETC |

---

### 3.2 Content Structure Từng Trang (Functions, Components & UI Specifications)

#### A. Cấu Trúc Nội Dung Trang Chủ Master Hub (`/tien-ich-giao-thong/`)

| STT | Tên Component / UI Section | Nhu Cầu Người Dùng (JTBD) | Giải Pháp Cấu Trúc (Solution) | Thành Phần UI (UI Components) & Functions Chi Tiết |
| :---: | :--- | :--- | :--- | :--- |
| 1 | **Hero & Master Utility Search Box** | "Tôi muốn tra phạt nguội hoặc tìm tiện ích xe ngay lập tức khi vừa vào trang." | Ô tìm kiếm thông minh 1-click đặt tại vị trí trung tâm Hero, tích hợp API phạt nguội 0-CAPTCHA. | • Tiêu đề Headline H1 chuẩn SEO.<br>• Selector chọn loại phương tiện: **Ô tô / Xe máy**.<br>• Input field nhập Biển số xe (BSX) tự động định dạng.<br>• Nút CTA *"Tra Cứu Phạt Nguội 0-CAPTCHA"* 1-click. |
| 2 | **Quick Utilities Grid (6 Spokes)** | "Tôi muốn truy cập nhanh các dịch vụ giao thông phổ biến nhất." | Grid 6 Card phím tắt chứa Icon & Tiêu đề điều hướng trực tiếp đến 6 Spoke cốt lõi. | • Grid 6 Card phím tắt: **Tra Phạt Nguội**, **Bảng Giá Xăng**, **Phí Không Dừng ePass**, **Trạm Sạc EV**, **Tìm Garage**, **Cứu Hộ 24/7**.<br>• Huy hiệu nhãn mác (Badge): *"Real-time"*, *"0-CAPTCHA"*. |
| 3 | **Live Fuel & Energy Real-time Feed** | "Tôi muốn xem ngay giá xăng dầu hôm nay và bản đồ trạm sạc gần tôi." | Widget Live Feed giá xăng Petrolimex/PVOil Vùng 1 & 2 kết hợp Mini Map GPS địa điểm lân cận. | • Bảng niêm yết giá xăng RON 95-III, E5 RON 92, Dầu Diesel.<br>• Mini Map GPS hiển thị 3 cây xăng/trạm sạc gần nhất.<br>• Form nhập SĐT nhận thông báo biến động giá xăng tự động. |
| 4 | **Vehicle Profile Value Proposition Cards** | "Tôi muốn hiểu rõ lợi ích của việc lưu Thẻ Xe Số trên App MoMo." | 3 Thẻ minh họa trực quan giá trị tự động hóa của Hồ sơ phương tiện (Vehicle Profile). | • Card 1: *Tự động quét & phát thông báo phạt nguội qua MoMo*.<br>• Card 2: *Nhắc lịch hạn đăng kiểm trước 30/15/7 ngày*.<br>• Card 3: *Cài đặt Auto-Topup tự động nạp tiền ePass/VETC*. |
| 5 | **Car Model Quick Selector (Master Data)** | "Tôi muốn tìm thông số, chi phí nuôi xe và giá bảo hiểm đúng dòng xe tôi đi." | Dropdown & Logo Grid chọn 35 Hãng xe & 264 Dòng xe dẫn đến các trang pSEO landing pages. | • Selector chọn Hãng xe (VinFast, Toyota, Hyundai, Honda...) $\rightarrow$ Chọn Dòng xe (VF8, Vios, Accent, City...).<br>• Nút CTA *"Xem Chi Phí & Báo Giá Bảo Hiểm Dòng Xe"*. |
| 6 | **Local GEO Location Selector** | "Tôi muốn lọc điểm sạc, cây xăng, garage tại khu vực tôi sắp di chuyển đến." | Dropdown bộ lọc 2 cấp Tỉnh/Thành $\rightarrow$ Quận/Huyện liên kết trực tiếp Sitemap GEO. | • Dropdown chọn Tỉnh/Thành phố $\rightarrow$ Chọn Quận/Huyện.<br>• Nút CTA *"Xem Bản Đồ Địa Điểm Tại Khu Vực"*. |
| 7 | **GenAI Blog & Cẩm Nang Featured Grid** | "Tôi muốn đọc các bài viết hướng dẫn luật giao thông và mẹo bảo dưỡng uy tín." | Grid 3 bài viết nổi bật được cấp bởi **GenAI Content Engine (PLG Project)**. | • Grid 3 Card bài viết: Ảnh đại diện, Tiêu đề H3, Sapo tóm tắt, Thẻ danh mục.<br>• Nút CTA *"Xem Tất Cả Bài Viết Cẩm Nang"*. |
| 8 | **FAQ Accordion & Structural Footer Block**| "Tôi muốn được giải đáp các thắc mắc thường gặp về quản lý xe trên MoMo." | Khối FAQ Accordion khai báo mã Schema `FAQPage` chuẩn Google AI Search. | • Accordion danh sách 5 câu hỏi thường gặp & câu trả lời chuẩn 25-40 từ.<br>• Footer Links liên kết sitemap nội bộ. |

#### B. Đặc Tả Chi Tiết Nội Dung Văn Bản (Content & Copywriting Specifications) Trang Chủ

1. **Hero Section Copy:**
   * **Thẻ H1:** `Tiện Ích Giao Thông MoMo - Cổng Quản Lý & Định Danh Xe 3 Phút`
   * **Đoạn Sapo Sub-headline:** `Tra cứu phạt nguội 0-CAPTCHA real-time, cập nhật giá xăng hôm nay, tìm vị trí trạm sạc xe điện & tự động hóa quản lý chiếc xe của bạn.`
   * **Nút Tra Cứu (CTA):** `"Tra Cứu Phạt Nguội 0-CAPTCHA (Miễn Phí)"`

2. **Khối 3 Card Giá Trị Thẻ Xe Số (Vehicle Profile Value Prop Copy):**
   * **Card 1 (Phạt Nguội):** `Tự Động Báo Phạt Nguội` $\rightarrow$ *"MoMo tự động quét dữ liệu CSGT hàng tuần cho biển số xe của bạn & phát thông báo ngay qua MoMo khi dính lỗi mới."*
   * **Card 2 (Đăng Kiểm):** `Nhắc Lịch Đăng Kiểm Smart` $\rightarrow$ *"Tự động theo dõi thời hạn kiểm định, cảnh báo sớm trước 30/15/7 ngày & hỗ trợ đặt lịch hẹn trung tâm đăng kiểm."*
   * **Card 3 (Phí BOT ePass):** `Auto-Topup ePass / VETC` $\rightarrow$ *"Tự động nạp tiền tài khoản giao thông khi số dư dưới 50k, di chuyển thông suốt không lo kẹt trạm thu phí."*

3. **Direct Answer Block (Dành cho Google AI Overview & Generative Search):**
   > **"Cổng tiện ích giao thông MoMo (momo.vn/tien-ich-giao-thong) cho phép chủ xe ô tô và xe máy tra cứu phạt nguội 0-CAPTCHA real-time từ Cục CSGT, theo dõi bảng giá xăng Petrolimex hôm nay, định vị trạm sạc xe điện VinFast/V-Green và mua bảo hiểm TNDS/Thân vỏ online với dữ liệu tự động điền trong 30 giây."**

4. **Nội Dung Accordion 5 Câu Hỏi Thường Gặp (FAQ Copy Spec - Schema `FAQPage`):**
   * **Q1:** *Làm thế nào để tra cứu phạt nguội không cần nhập mã CAPTCHA trên MoMo?*
     * **A1:** Bạn chỉ cần nhập biển số xe (ví dụ: 30F-12345) vào ô tra cứu trên trang Tiện ích giao thông MoMo. Hệ thống tự động kết nối dữ liệu Cục CSGT và trả kết quả tức thì trong 3 giây mà không yêu cầu nhập mã CAPTCHA.
   * **Q2:** *Tôi có thể nộp tiền phạt nguội online trực tiếp qua MoMo được không?*
     * **A2:** Có. Nếu kết quả tra cứu hiển thị lỗi vi phạm, bạn bấm nút "Nộp phạt ngay" để mở App MoMo, kiểm tra chi tiết quyết định xử phạt và thanh toán 1-click qua Ví MoMo hoặc Ví Trả Sau.
   * **Q3:** *Gói Cảnh Báo Phạt Nguội Tự Động 9k/năm của MoMo hoạt động như thế nào?*
     * **A3:** Khi đăng ký Gói 9.000đ/năm, MoMo sẽ tự động quét dữ liệu CSGT định kỳ hàng tuần cho biển số xe của bạn và phát thông báo trực tiếp qua App MoMo ngay khi phát sinh lỗi vi phạm mới.
   * **Q4:** *MoMo có hỗ trợ tự động điền thông tin khi mua bảo hiểm ô tô / xe máy không?*
     * **A4:** Có. Khi bạn đã lưu Thẻ Xe Số (Vehicle Profile), toàn bộ thông tin biển số, số khung, số máy và dòng xe sẽ được tự động điền (Auto-fill >80%) khi đăng ký mua bảo hiểm TNDS hoặc Thân vỏ.
   * **Q5:** *Làm sao để tìm vị trí cây xăng Petrolimex hoặc trạm sạc xe điện gần nhất?*
     * **A5:** Bạn truy cập chuyên trang Cây Xăng (`/cay-xang`) hoặc Trạm Sạc (`/tram-sac`), bật vị trí GPS. Hệ thống hiển thị bản đồ định vị các trạm gần bạn nhất kèm chỉ đường Google Maps.

---

#### C. Cấu Trúc Nội Dung Các Trang Spoke & Standalone Use Cases

| Trang / Phân Hệ | Tên Component / Section | Nhu Cầu Người Dùng (JTBD) | Giải Pháp Cấu Trúc (Solution) | Thành Phần UI (UI Components) & Functions |
| :--- | :--- | :--- | :--- | :--- |
| **Tra Cứu Phạt Nguội**<br>`/phat-nguoi/` | **Hero & Tool Input** | "Tôi muốn kiểm tra lỗi phạt nguội tức thì." | Form tra cứu trực tiếp bằng Biển số xe không yêu cầu nhập CAPTCHA. | Selector Ô tô/Xe máy + Input Biển số xe + Nút Tra cứu 1-click |
| | **Result & Smart CTA** | "Tôi muốn xem chi tiết lỗi và nộp phạt online." | Output kết quả: Xe sạch $\rightarrow$ CTA lưu biển số & mua Gói Cảnh báo Tự động (9k/năm); Có lỗi $\rightarrow$ Nộp Phạt 1-Click. | Màn hình trả lỗi vi phạm + Banner CTA Universal Link mở App MoMo mua Gói Cảnh báo (9k/năm) / Đóng phạt |
| | **DVC Guide & SEO Block**| "Tôi muốn biết quy trình nộp phạt online chuẩn." | Bài viết hướng dẫn 4 bước nộp phạt qua Cổng DVCQG & App MoMo + Bảng tiền phạt. | Hướng dẫn nộp phạt online & Bảng tra cứu mức phạt lỗi phổ biến |
| **Blog & Cẩm Nang**<br>`/tien-ich-giao-thong/blog/` | **Content Index** | "Tôi muốn đọc các bài viết tư vấn luật và bảo dưỡng xe." | Kho bài viết được cung cấp bởi **GenAI Content Engine (PLG Project)**. | Danh mục bài viết + Grid bài viết + Banner CTA mở App |
| | **Article Detail** | "Tôi muốn đọc hướng dẫn luật/mẹo bảo dưỡng chi tiết." | Giao diện chi tiết bài viết tư vấn giao thông chuẩn SEO kèm CTA mở App MoMo. | Tiêu đề H1 + Nội dung bài viết GenAI + In-Article Smart W2A Widget |
| **Giá Xăng Dầu**<br>`/tien-ich-giao-thong/gia-xang/` | **Live Price Banner** | "Tôi muốn biết giá xăng hôm nay tăng hay giảm." | Banner tự động đồng bộ giá xăng Petrolimex/PVOil Vùng 1 & Vùng 2 thời gian thực. | Bảng giá xăng RON 95-III, E5 RON 92-II, Dầu Diesel hôm nay |
| | **Price History Chart** | "Tôi muốn xem lịch sử biến động giá xăng." | Biểu đồ tương tác theo dõi biến động giá xăng trong 3–6 tháng. | Biểu đồ tương tác biến động giá xăng 3-6 tháng gần nhất |
| | **Station Finder Map** | "Tôi muốn tìm cây xăng Petrolimex gần nhất." | Bản đồ GPS định vị cây xăng Petrolimex/PVOil nhận Ví MoMo. | Bản đồ tương tác + Danh sách cây xăng nhận MoMo gần bạn |
| | **Smart Push CTA** | "Tôi muốn nhận tin báo giá xăng trước khi điều chỉnh." | Form nhập SĐT nhận Push Notification trước kỳ điều hành 15 phút. | Form đăng ký nhận tin báo giá xăng tự động chiều thứ 5 |
| **GEO Local Pages**<br>`/tram-sac/`, `/tim-garage/` | **Filter Bar & Map View** | "Tôi muốn lọc trạm sạc/garage đúng nhu cầu." | Thanh lọc trạm sạc xe điện (VinFast, V-Green & các đối tác / công suất kW) hoặc garage. | Bộ lọc Tỉnh/Thành, Quận/Huyện, Loại trạm sạc hoặc Dịch vụ garage |
| | **Map & Location Grid** | "Tôi muốn xem bản đồ kèm khoảng cách thực tế." | Bản đồ tương tác đồng bộ danh sách địa điểm O2O kèm khoảng cách $km$. | Bản đồ tương tác + Danh sách địa điểm kèm khoảng cách ($km$), địa chỉ |
| | **Merchant Card Snippet**| "Tôi muốn chọn địa điểm uy tín và dẫn đường ngay." | Merchant Card gồm điểm rating, nhãn MoMo Verified, nút Dẫn đường & Đặt chỗ. | Thẻ địa điểm: Rating, Huy hiệu *"Chấp nhận Ví MoMo"*, nút Dẫn đường |
| **Bảo Hiểm Ô Tô**<br>`/bao-hiem-o-to/` | **Hero & Instant Quote** | "Tôi muốn tính nhanh phí bảo hiểm TNDS/Thân vỏ." | Form tính phí tức thì hỗ trợ tự động điền (Auto-fill) dữ liệu từ Vehicle Profile. | Form chọn gói bảo hiểm (TNDS / Thân vỏ), chọn Dòng xe |
| | **Comparison Matrix** | "Tôi muốn so sánh giá và quyền lợi 9 công ty bảo hiểm." | Bảng so sánh báo giá & quyền lợi trực quan từ PVI, Bảo Việt, MIC... | Bảng so sánh mức phí & quyền lợi bảo hiểm từ 9 nhà bảo hiểm |
| | **Purchase CTA & E-Card** | "Tôi muốn mua bảo hiểm nhận ấn chỉ điện tử ngay." | Nút "Mua Ngay - Cấp Ấn Chỉ Điện Tử Trong 30s" kết nối API nhà bảo hiểm. | Nút *"Mua Ngay - Cấp Ấn Chỉ Điện Tử Trong 30s"* |

---

### 3.3 Umami Event Tracking theo Luồng Tương Tác (User Journey Events)

Đặc tả các sự kiện Umami bắn về hệ thống theo đúng luồng trải nghiệm người dùng (Touchpoint Journey):

#### A. Luồng Tra Cứu Phạt Nguội & Nộp Phạt (Core Journey on `/tien-ich-giao-thong/` & `/phat-nguoi/`)

| Bước (Step) | Touchpoint / Vị Trí | Hành Động Người Dùng | Umami Event Name |
| :---: | :--- | :--- | :--- |
| **Step 1** | Vehicle Type Selector | Chọn loại phương tiện (Ô tô / Xe máy) | `select_vehicle_type` |
| **Step 2** | Input & Submit Button | Nhập Biển số xe (BSX) & Bấm Tra cứu | `submit_license_plate` |
| **Step 3A** | Result Screen (Xe Sạch) | Hiển thị màn hình kết quả: Không có lỗi vi phạm | `view_result_clean` |
| **Step 3B** | Result Screen (Vi Phạm)| Hiển thị màn hình kết quả: Có lỗi vi phạm phạt nguội | `view_result_violation` |
| **Step 4** | Action CTA Button | Bấm Nộp phạt online / Mở App MoMo xử lý | `click_pay_fine` |

#### B. Các Luồng Tương Tác Tính Năng Phụ (Secondary Feature Touchpoints)

| Phân Hệ / Page | Touchpoint / Vị Trí | Hành Động Người Dùng | Umami Event Name |
| :--- | :--- | :--- | :--- |
| **Quick Grid** | Utility Cards | Bấm phím tắt chuyển đến các Spoke Pages | `click_utility_item` |
| **Blog & Cẩm Nang**| In-Article Smart CTA | Bấm CTA trong bài viết blog mở App MoMo | `click_blog_cta` |
| **Giá Xăng** | Subscribe Form | Bấm nút đăng ký nhận tin báo giá xăng tự động | `subscribe_gas_price` |
| **Trạm Sạc / Garage**| GEO Filter Bar | Chọn Tỉnh/Thành, Quận/Huyện hoặc Loại trạm | `select_geo_filter` |
| **Trạm Sạc / Garage**| Merchant Card | Bấm thẻ địa điểm để chỉ đường hoặc đặt chỗ | `click_merchant_item` |
| **Bảo Hiểm** | Quote / Purchase Button | Bấm xem báo giá / Mua bảo hiểm Ô tô, Xe máy | `click_buy_insurance` |
| **Cứu Hộ 24/7** | Hotline Button | Bấm nút gọi tổng đài Cứu hộ 24/7 | `click_call_rescue` |

---

## 4. SEO / GEO ONPAGE

### 4.1 Meta Data (Title, Description, Headings, OpenGraph & Social Cards)

#### A. Bảng Công Thức Meta Tag Standards

| Loại Trang | Công Thức Tag `<title>` (Max 60 chars) | Công Thức `<meta description>` (150-160 chars) |
| :--- | :--- | :--- |
| **Master Hub** | `Tiện Ích Giao Thông MoMo - Tra Cứu & Quản Lý Xe 3 Phút` | `Cổng tiện ích giao thông MoMo: Tra cứu phạt nguội 0-CAPTCHA, xem giá xăng hôm nay, vị trí trạm sạc VinFast, cây xăng Petrolimex và mua bảo hiểm ô tô online.` |
| **Phạt Nguội** | `Tra Cứu Phạt Nguội CSGT Toàn Quốc (Không CAPTCHA) | MoMo` | `Tra cứu phạt nguội ô tô, xe máy toàn quốc không cần nhập CAPTCHA. Cập nhật dữ liệu từ Cục CSGT real-time. Hướng dẫn nộp phạt online nhanh gọn qua MoMo.` |
| **Blog Article Page**| `[Tiêu Đề Bài Viết] | Cẩm Nang Giao Thông MoMo` | `[Mô tả tóm tắt bài viết 150 ký tự chứa từ khóa chính.]` |
| **Giá Xăng** | `Bảng Giá Xăng Dầu Hôm Nay (Mới Nhất Vùng 1 & 2) | MoMo` | `Cập nhật bảng giá xăng dầu RON 95-III, E5 RON 92, Dầu Diesel hôm nay mới nhất theo kỳ điều hành. Danh sách cây xăng Petrolimex/PVOil chấp nhận Ví MoMo.` |
| **Trạm Sạc EV** | `Bản Đồ Trạm Sạc Xe Điện VinFast & V-Green Gần Đấu | MoMo` | `Định vị trạm sạc xe điện VinFast, V-Green gần nhất. Lọc theo cổng sạc, công suất kW, giờ mở cửa và chỉ đường Google Maps nhanh chóng qua MoMo.` |
| **Bảo Hiểm Ô Tô** | `Bảo Hiểm Ô Tô Online (TNDS & Thân Vỏ) - Mua Ngay | MoMo` | `Mua bảo hiểm ô tô TNDS bắt buộc và bảo hiểm thân vỏ online. Báo giá từ 9 công ty bảo hiểm uy tín (PVI, Bảo Việt, MIC), cấp ấn chỉ điện tử tức thì qua MoMo.` |

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

---

### 4.2 Schema.org JSON-LD Specifications

Mỗi loại trang bắt buộc khai báo mã JSON-LD chuẩn trong thẻ `<head>`:

#### A. Master Hub Page (`/tien-ich-giao-thong/`)
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
        { "@type": "ListItem", "position": 2, "name": "Tiện ích giao thông", "item": "https://momo.vn/tien-ich-giao-thong/" }
      ]
    }
  ]
}
```

#### B. Blog Article Page (`/tien-ich-giao-thong/blog/{article-slug}/`)
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "[Tiêu đề bài viết]",
  "image": "https://img.mservice.io/vehicle-hub/blog-[article-slug].jpg",
  "author": { "@type": "Organization", "name": "MoMo Vehicle Hub Team" },
  "publisher": { "@type": "Organization", "name": "MoMo", "logo": { "@type": "ImageObject", "url": "https://img.mservice.io/logo.png" } },
  "datePublished": "2026-08-01",
  "description": "[Mô tả bài viết]"
}
```

---

### 4.3 Sitemap & Technical SEO

1. **Cấu trúc Sub-Sitemaps Index (`sitemap_index.xml`):**
   * `sitemap-vehicle-hub.xml`: Trang chủ `/tien-ich-giao-thong/` và các Spoke Pages (`/gia-xang/`, `/tram-sac/`, `/cay-xang/`, `/tim-garage/`) (`priority: 1.0`, `changefreq: daily`).
   * `sitemap-phat-nguoi.xml`: Trang Tra Cứu Phạt Nguội (`/phat-nguoi/`) (`priority: 0.9`, `changefreq: daily`).
   * `sitemap-blog.xml`: Bài viết cẩm nang giao thông (`priority: 0.8`, `changefreq: daily`).
   * `sitemap-bao-hiem.xml`: Trang Bảo Hiểm Ô Tô (`/bao-hiem-o-to/`) & Xe Máy (`/bao-hiem-xe-may/`) (`priority: 0.9`, `changefreq: weekly`).
   * `sitemap-merchant.xml`: Các trang chi tiết Merchant đối tác (`priority: 0.6`, `changefreq: weekly`).
2. **Quy tắc Quản lý Crawl Budget:** Trả mã HTTP `410 Gone` và xóa khỏi Sitemap đối với các trang Merchant ngưng hoạt động.
3. **Canonical Rules:** 100% trang có thẻ canonical tự tham chiếu tuyệt đối.

---

### 4.4 GEO / AIO (Generative Engine Optimization cho AI Search)

Để tối ưu khả năng xuất hiện trên Google AI Overview, ChatGPT, Perplexity và Gemini:

1. **Direct Answer Block (25 - 40 từ):** Ngay dưới mỗi tiêu đề `<h2>` của khối FAQ hoặc Hướng dẫn, bắt buộc chứa 1 câu trả lời tóm tắt trực tiếp định dạng Entity-Attribute-Value:
   * *Ví dụ:* **"Tra cứu phạt nguội trên MoMo cho phép người dùng kiểm tra lỗi vi phạm giao thông bằng biển số xe trực tiếp 0-CAPTCHA trong 3 giây, tự động đồng bộ dữ liệu từ Cục CSGT."**
2. **Minified HTML Tables:** Đóng gói toàn bộ dữ liệu so sánh phí bảo hiểm, giá xăng dầu, bảng tiền phạt vi phạm bằng thẻ `<table>` HTML chuẩn với `<thead>` và `<tbody>` rõ ràng để AI Bot dễ trích xuất.
3. **Authoritative Citations:** Chèn dẫn nguồn tham chiếu trực tiếp đến các cổng thông tin chính phủ / văn bản pháp luật / đối tác chính thức (Nghị định 100/2019/NĐ-CP, Cục CSGT, Cổng DVCQG).
