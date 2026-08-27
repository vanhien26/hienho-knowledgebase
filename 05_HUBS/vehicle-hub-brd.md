# BRD: Vehicle Hub - Cổng Tiện Ích & Hồ Sơ Phương Tiện MoMo

> - **Project:** Vehicle Hub (Web Platform & Vehicle Profile Identity)
> - **Division:** Growth Platform Division (GPD)
> - **Owner:** Web Platform (Web Product Lead | Web Platform) x Cell Teams (VTTI & InsurTech)

---

## I. OVERVIEW

### 1.1 Scope & Objectives

#### A. Context & Goals
* **Thực trạng:** Chủ xe ô tô và xe máy tại Việt Nam phải sử dụng nhiều ứng dụng và trang web khác nhau để tra cứu phạt nguội, nạp tiền ETC, theo dõi hạn đăng kiểm, mua bảo hiểm và tìm cây xăng/bãi đỗ.
* **Mục tiêu:** Hợp nhất các tiện ích này trên website `momo.vn` để thu hút traffic tự nhiên từ kết quả tìm kiếm Google, khởi tạo Hồ sơ xe (Vehicle Profile) và điều hướng người dùng sang App MoMo để hoàn tất giao dịch.

#### B. Web vs In-App Scope

| Tiêu Chí So Sánh | Kênh Website (Web Vehicle Hub) | In-App Mini App (Vehicle Center) |
| :--- | :--- | :--- |
| **Tên Sản Phẩm** | Cổng Tiện Ích Giao Thông | Vehicle Center Mini App |
| **Nền Tảng / URL** | Website (`momo.vn/tien-ich-giao-thong`, `momo.vn/phat-nguoi`) | Ứng dụng di động MoMo (iOS & Android) |
| **Đơn Vị Phụ Trách** | Web Platform | VTTI x InsurTech |
| **Vai Trò Cốt Lõi** | Thu hút traffic tự nhiên & Khởi tạo Hồ sơ xe | Quản lý phương tiện, tự động hóa & thanh toán |
| **Trải Nghiệm (UX)** | Tra cứu công khai, không bắt buộc đăng nhập | Quản lý Thẻ Xe Số, nhận thông báo tự động, nộp phạt, mua bảo hiểm |
| **Cơ Chế Chuyển Đổi** | • Desktop: Dynamic QR Code<br>• Mobile: Onelink mở Mini App (Store nếu chưa cài) | Thanh toán trực tiếp qua Ví MoMo / Ví Trả Sau |
| **KPIs Cam Kết** | • Total Traffic: 500.000 (Phase 1 Pilot)<br>• CTR chuyển đổi Web-to-App: ≥ 5.0% - 10.0% | • MAU In-App: 250.000<br>• Hồ sơ xe mới: 100.000 |

---

### 1.2 Web-to-App Flywheel

Kênh Website vận hành dựa trên các tiện ích tra cứu miễn phí để thu hút người dùng từ Google Search, tạo đòn bẩy thu thập biển số xe và chuyển đổi sang App:

* **Chuỗi hành trình chuyển đổi (Web-to-App Flow):**
  `[Google Search Demand]` ➔ `[Website momo.vn (Tra cứu công khai)]` ➔ `[Trả kết quả + Đề xuất tiện ích]` ➔ `[Thu thập Biển số xe]` ➔ `[Chuyển đổi qua QR Code / Onelink]` ➔ `[App MoMo: Quản lý Thẻ Xe Số]`

| Bước | Giai Đoạn | Hành Động Của Người Dùng | Cơ Chế Phản Hồi Của Hệ Thống | Nền Tảng |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Tìm kiếm thông tin | Search từ khóa (Phạt nguội, Giá xăng, Phong thủy, Đăng kiểm) trên Google | Hiển thị kết quả tìm kiếm tự nhiên của momo.vn | Google Search |
| **2** | Trải nghiệm tiện ích | Truy cập trang Web, nhập biển số xe để tra cứu miễn phí | Trả kết quả tra cứu tốc độ cao, không yêu cầu đăng nhập | Website momo.vn |
| **3** | Nhận diện giá trị | Xem kết quả tra cứu và đề xuất gói ưu đãi đính kèm | Hiển thị nút CTA chuyển tiếp mở App MoMo để nhận nhắc lịch | Website momo.vn |
| **4** | Chuyển đổi kênh | Quét Dynamic QR Code (trên máy tính) hoặc bấm nút Onelink (trên điện thoại) | Hệ thống phân luồng mở ứng dụng MoMo hoặc chuyển về Store | QR / Onelink |
| **5** | Kích hoạt In-App | Đăng nhập ứng dụng MoMo | Lưu Thẻ Xe Số vào hồ sơ, nhận cảnh báo tự động & thanh toán | App MoMo |

#### Web Spoke Directory

* **Nhóm Tiện Ích Tra Cứu & Thu Hút Traffic (Traffic Magnets):**
  1. **Tiện ích Phạt Nguội (`/phat-nguoi`):** Tra cứu vi phạm giao thông theo biển số xe. Đặt khối bán chéo bảo hiểm và nút lưu biển số xe để nhận thông báo tự động hàng tuần.
  2. **Tiện ích Bảng Giá Xăng Dầu (`/tien-ich-giao-thong/gia-xang`):** Cập nhật bảng giá xăng dầu realtime kỳ điều hành và vị trí cây xăng Petrolimex/PVOil chấp nhận Ví MoMo.
  3. **Tiện ích Phong Thủy & Đấu Giá Biển Số (`/tien-ich-giao-thong/phong-thuy-bien-so`):** Giải mã ý nghĩa phong thủy 5 số cuối, tính số nút và tra cứu kết quả đấu giá biển số để thúc đẩy người dùng nhập biển số xe.
  4. **Tra Cứu Mức Phạt Giao Thông (`/tien-ich-giao-thong/tra-cuu-muc-phat`):** Danh bạ tra cứu mức tiền phạt & hình phạt tước GPLX theo Nghị định 100/123.
  5. **Tiện ích Đăng Kiểm Xe (`/tien-ich-giao-thong/dang-kiem`):** Tra cứu hạn kiểm định xe và đăng ký nhận thông báo nhắc lịch tự động qua App MoMo.

* **Nhóm Dịch Vụ Thanh Toán & Giao Dịch Cốt Lõi (Core Transactional Spokes):**
  6. **Bảo Hiểm Ô Tô & Xe Máy (`/bao-hiem-o-to`, `/bao-hiem-xe-may`):** Bán trực tuyến và gia hạn bảo hiểm TNDS bắt buộc & Bảo hiểm Thân vỏ ô tô cấp ấn chỉ điện tử tức thì.
  7. **Thu Phí Không Dừng (`/phi-khong-dung`):** Tra cứu số dư, hướng dẫn liên kết tài khoản ePass/VETC và kích hoạt tính năng tự động nạp tiền (Auto-Topup).

* **Nhóm Tiện Ích Bản Đồ Local & Công Cụ Hỗ Trợ Lộ Trình (Local GEO & Calculators):**
  8. **Trạm Sạc Xe Điện (`/tien-ich-giao-thong/tram-sac`):** Định vị trạm sạc VinFast, V-Green theo vị trí GPS và đề xuất gói bảo hiểm xe điện.
  9. **Bản Đồ Garage & Bảo Dưỡng (`/tien-ich-giao-thong/tim-garage`):** Định vị garage sửa chữa ô tô/xe máy, trung tâm rửa xe & detailing gần nhất.
  10. **Bãi Đỗ Xe & Cứu Hộ Đường Bộ 24/7 (`/tien-ich-giao-thong/bai-do-xe`):** Bản đồ bãi đỗ xe ô tô, dịch vụ gọi xe cứu hộ sự cố khẩn cấp và công cụ dự toán chi phí nuôi xe/thuế trước bạ.

---

### 1.3 Metrics & Targets

#### North Star Metrics

| Tầng Đo Lường | Chỉ Số KPI Cốt Lõi | Định Nghĩa Chỉ Số | Target Phase 1 Pilot | Vai Trò Quản Trị |
| :--- | :--- | :--- | :--- | :--- |
| **Kênh Website** | **Total Traffic (Pageview)** | Tổng lượt truy cập vào các trang tiện ích giao thông trên website `momo.vn`. | **500.000** | Hứng tối đa nhu cầu tìm kiếm của chủ xe trên Google Search. |
| **Kênh Website** | **%CTR Chuyển Đổi (W2A)** | Tỷ lệ nhấp nút chuyển đổi từ website sang mở ứng dụng MoMo. | **≥ 5.0% - 10.0%** | Đo lường hiệu quả chuyển đổi từ kênh Web sang App. |
| **Kênh App** | **Logged-in MAU** | Số lượng người dùng định danh hoạt động hàng tháng trong ứng dụng. | **250.000** | Đo lường mức độ giữ chân người dùng trong ứng dụng. |
| **Kênh App** | **New Vehicle Profiles** | Số lượng Thẻ Xe Số (Hồ sơ xe) được khởi tạo mới thành công In-App. | **100.000** | Xây dựng kho dữ liệu phương tiện tập trung cho MoMo. |

#### Target & Run-Rate Alignment

> **Lưu ý về chỉ số:** Các chỉ số tổng Target Phase 1 Pilot (*Total Traffic 500.000, %CTR W2A ≥ 5.0% - 10.0%, Logged-in MAU 250.000, New Vehicle Profiles 100.000*) **đã được Ban Giám Đốc phê duyệt chính thức**. Kế hoạch phân rã Monthly Run-rate chi tiết theo từng tháng sẽ được tính toán và ban hành sau khi sản phẩm hoàn thiện go-live và đo đạc xong số liệu Baseline thực tế.

| Tầng Đo Lường | Chỉ Số KPI Cốt Lõi | Định Nghĩa Chỉ Số | Target Phase 1 Pilot (Đã Phê Duyệt) | Kế Hoạch Monthly Run-Rate |
| :--- | :--- | :--- | :--- | :--- |
| **Kênh Website** | **Total Traffic** | Tổng lượt truy cập từ kết quả tìm kiếm vào các tiện ích giao thông. | **500.000** | Xây dựng sau khi có số liệu Baseline go-live. |
| **Kênh Website** | **%CTR (W2A)** | Tỷ lệ nhấp nút chuyển đổi từ website sang mở App MoMo. | **≥ 5.0% - 10.0%** | Xây dựng sau khi có số liệu Baseline go-live. |
| **Kênh App** | **Logged-in MAU** | Số lượng người dùng định danh hoạt động hàng tháng trong ứng dụng. | **250.000** | Xây dựng sau khi có số liệu Baseline go-live. |
| **Kênh App** | **New Profiles** | Số lượng Thẻ Xe Số (Hồ sơ xe) được khởi tạo mới thành công. | **100.000** | Xây dựng sau khi có số liệu Baseline go-live. |

---

## II. MARKET DEMAND & COMPLIANCE

### 2.1 Search Demand

Theo phân tích dữ liệu thực tế từ bộ từ khóa giao thông và các tập tin nghiên cứu, tổng nhu cầu tìm kiếm tự nhiên của chủ xe đạt hơn **20.1 triệu lượt/tháng**, phân bổ qua 15 nhóm tiện ích chính:

| STT | Nhu Cầu / Use Case | Volume Search / Tháng | Ghi Chú Chiến Lược |
| :---: | :--- | :---: | :--- |
| **1** | **Giá Xăng Dầu** | 10.520.000 | Hứng traffic lặp lại hàng tuần theo kỳ điều hành giá xăng. |
| **2** | **Tra Cứu Phạt Nguội** | ~6.100.000 | Trang chủ lực thu hút traffic tra cứu vi phạm. |
| **3** | **Trạm Sạc Xe Điện (EV)** | 1.240.000 | Hứng tệp chủ xe điện VinFast, V-Green. |
| **4** | **Sửa Chữa & Bảo Dưỡng Xe** | 934.000 | Bản đồ tiệm sửa xe, garage bảo dưỡng ô tô/xe máy. |
| **5** | **Cây Xăng (Bản Đồ Local)** | 550.000 | Tìm cây xăng Petrolimex/PVOil chấp nhận MoMo. |
| **6** | **Rửa Xe & Chăm Sóc Xe** | 284.000 | Bản đồ tiệm rửa xe & trung tâm detailing. |
| **7** | **Đăng Kiểm Xe** | 182.000 | Tra cứu hạn kiểm định & nhắc lịch tự động. |
| **8** | **Bãi Đỗ Xe & Giữ Xe** | 180.000 | Bản đồ bãi đỗ xe & thanh toán VETC Parking. |
| **9** | **Cứu Hộ Đường Bộ 24/7** | 172.000 | Dịch vụ gọi xe cứu hộ sự cố khẩn cấp. |
| **10** | **Phí Không Dừng (ePass/VETC)** | 95.000 | Tra cứu số dư & cài đặt tự động nạp tiền. |
| **11** | **Phong Thủy & Đấu Giá Biển Số** | 56.220 | Giải mã phong thủy 5 số cuối, tra cứu giá đấu giá biển số. |
| **12** | **Thuế Trước Bạ** | 44.000 | Dự toán lệ phí trước bạ xe mới/cũ. |
| **13** | **Định Giá Xe Cũ** | 14.300 | Tra cứu khoảng giá thị trường xe cũ. |
| **14** | **Phí Đường Bộ** | 13.600 | Bài viết cẩm nang tra cứu biểu phí bảo trì đường bộ. |
| **15** | **Tra Cứu Mức Phạt Giao Thông** | 25.000 | Bảng tra cứu biểu phí phạt tiền & tước GPLX theo luật. |

### 2.2 Legal & Compliance

1. **Tuân Thủ Luật Biển Số Định Danh (Thông tư 24/2023/TT-BCA):**
   * Biển số xe gắn với mã định danh cá nhân (CCCD) của chủ xe và được giữ lại 5 năm khi bán xe.
   * Xây dựng tính năng quản lý danh sách biển số định danh thuộc sở hữu của người dùng theo CCCD trên App MoMo.
2. **Đấu Giá Biển Số Xe (Nghị quyết 73/2022/QH15):**
   * Cho phép tra cứu kết quả đấu giá biển số chính thức và công cụ định giá tham khảo cho biển số đẹp.
3. **Quy Tắc Bảo Mật Thông Tin Trên Website (Web Compliance):**
   * Khi hiển thị kết quả trên website công cộng, **tuyệt đối không hiển thị thông tin cá nhân (CCCD, Họ tên, Địa chỉ), bảo hiểm tư nhân hoặc giá trị tài sản của chủ xe**. Thông tin chi tiết chỉ hiển thị sau khi người dùng đăng nhập xác thực trên App MoMo.

---

## III. PRODUCT SPEC

### 3.1 Value Exchange Mechanism
* **Biển số xe:** Là chiếc chìa khóa định danh kết nối phương tiện ngoài đời thực với tài khoản MoMo (Agent ID).
* **Cơ chế trao đổi giá trị:** Cung cấp miễn phí các công cụ tra cứu tốc độ cao (Phạt nguội, Giá xăng, Phong thủy, Hạn đăng kiểm) để người dùng tự nguyện nhập Biển số xe ➔ Khởi tạo Thẻ Xe Số (Vehicle Profile).
* **Công cụ kiểm tra thông tin trước khi xuất phát:** Kiểm tra 4 yếu tố trước khi di chuyển: Phạt nguội, Số dư ePass/VETC, Giá xăng và Hạn Đăng kiểm/Bảo hiểm.

---

### 3.2 Master Page Block Spec

* **Main Headline:** `Một chiếc xe – Một tài khoản quản lý tự động trên MoMo`
* **Sub-headline:** `Tự động hóa toàn bộ nhắc lịch, cảnh báo vi phạm và đơn giản hóa thủ tục xe cộ ngay trên App MoMo.`

| Cột | Tiêu Đề Thẻ | Nội Dung Mô Tả Chi Tiết |
| :---: | :--- | :--- |
| **Cột 1** | **Cảnh báo vi phạm tự động** | Tự động quét và phát thông báo lỗi phạt nguội mới vào thứ Hai hàng tuần, chủ động xử lý trước kỳ đăng kiểm. |
| **Cột 2** | **Nhắc lịch đăng kiểm & bảo hiểm** | Tự động thông báo nhắc hạn kiểm định xe và gia hạn bảo hiểm TNDS/Thân vỏ trước 30, 15 và 7 ngày. |
| **Cột 3** | **Tự động nạp phí ePass/VETC** | Tự động bù tiền vào tài khoản thu phí không dừng khi số dư dưới hạn mức, di chuyển thông suốt qua mọi trạm BOT. |

---

### 3.3 Header Navigation Menu Specification

Thanh Menu Header (Header Navigation Bar) xuất hiện đồng bộ trên Trang chủ Master Hub (`/tien-ich-giao-thong`) và toàn bộ các Subpages vệ tinh, đóng vai trò là khung điều hướng trải nghiệm người dùng và phân luồng traffic nội bộ:

#### A. Cấu Trúc Thành Phần Header (Header Component Hierarchy)

| Thành Phần | Định Dạng Hiển Thị | Cơ Chế Điều Hướng (Target URL) | Vai Trò & Trải Nghiệm Người Dùng (UX) |
| :--- | :--- | :--- | :--- |
| **Logo & Brand Anchor** | Logo MoMo + Chữ *"Tiện Ích Giao Thông"* | `momo.vn/tien-ich-giao-thong` | Điểm neo thương hiệu, nhấp để quay về Trang chủ Hub trung tâm. |
| **Menu 1: Tra Cứu Vi Phạm** | Dropdown Menu (Kèm nhãn *Hot*) | • Tra cứu phạt nguội: `/phat-nguoi`<br>• Biểu phí mức phạt: `/tien-ich-giao-thong/tra-cuu-muc-phat` | Dẫn luồng người dùng vào công cụ tra cứu vi phạm camera và bảng tra cứu mức phạt giao thông theo Nghị định 100/123. |
| **Menu 2: Nhiên Liệu & Trạm Sạc** | Dropdown Menu | • Bảng giá xăng dầu hôm nay: `/tien-ich-giao-thong/gia-xang`<br>• Cây xăng gần nhất: `/tien-ich-giao-thong/cay-xang`<br>• Trạm sạc xe điện EV: `/tien-ich-giao-thong/tram-sac` | Nhóm tiện ích hàng ngày, hỗ trợ kiểm tra biến động giá xăng dầu và định vị trạm tiếp nhiên liệu/trạm sạc theo vị trí GPS. |
| **Menu 3: Dịch Vụ & Bảo Dưỡng** | Dropdown Menu | • Garage & Sửa xe: `/tien-ich-giao-thong/tim-garage`<br>• Bãi đỗ xe & Cứu hộ 24/7: `/tien-ich-giao-thong/bai-do-xe`<br>• Tra cứu hạn đăng kiểm: `/tien-ich-giao-thong/dang-kiem` | Hỗ trợ tìm kiếm garage bảo dưỡng, gọi xe cứu hộ khẩn cấp và theo dõi chu kỳ kiểm định phương tiện. |
| **Menu 4: Bảo Hiểm Phương Tiện** | Dropdown Menu | • Bảo hiểm ô tô 9 hãng: `/bao-hiem-o-to`<br>• Bảo hiểm xe máy điện tử: `/bao-hiem-xe-may` | Dẫn sang các trang sản phẩm độc lập để so sánh quyền lợi và mua bảo hiểm bắt buộc TNDS / Thân vỏ trực tuyến. |
| **Menu 5: Thu Phí Không Dừng** | Link Đơn (Single Link) | • ePass / VETC: `/phi-khong-dung` | Hướng dẫn liên kết tài khoản thu phí tự động và kích hoạt tính năng nạp tiền tự động (Auto-Topup) khi qua trạm BOT. |
| **Menu 6: Tiện Ích Mở Rộng** | Link Đơn (Single Link) | • Phong thủy & Đấu giá biển số: `/tien-ich-giao-thong/phong-thuy-bien-so` | Công cụ giải mã ý nghĩa phong thủy 5 số cuối và tra cứu kết quả đấu giá biển số đẹp. |
| **Header CTA (Bên Phải)** | Nút Nổi Bật (Primary Button) | • **Desktop:** Kích hoạt Dynamic QR Code Modal<br>• **Mobile:** Kích hoạt Onelink mở App MoMo | Nút hành động kêu gọi chuyển đổi *"Mở Thẻ Xe Số"* / *"Quản Lý Xe Trên App"* nhằm tối đa hóa tỷ lệ W2A CTR. |

#### B. Quy Chuẩn Kỹ Thuật & Trải Nghiệm Responsive (UX Behavior)
* **Sticky Navigation:** Header cố định ở mép trên màn hình khi người dùng cuộn trang (Sticky Header), giúp điểm chạm chuyển đổi CTA và các menu tiện ích luôn sẵn sàng tương tác.
* **Hiển thị trên Mobile (Mobile Viewport):** Tự động thu gọn thành **Hamburger Menu (Icon 3 gạch)**; khi mở ra sẽ hiển thị dạng Accordion phân cấp theo từng nhóm tiện ích kèm nút CTA *"Mở App MoMo"* cố định ở chân menu trượt.
* **Tối ưu hóa SEO & Tracking:** Khai báo cấu trúc thẻ `<nav>` chuẩn HTML5 semantic, gắn mã tracking phân tích sự kiện `click_header_menu` và `click_header_cta` đồng bộ lên hệ thống GA4.

---

### 3.4 Sitemap Architecture (Tổng Hợp 32 URLs)

Hệ sinh thái Tiện Ích Giao Thông bao gồm **32 URLs** được phân bổ theo 8 nhóm chức năng cốt lõi:

#### 1. Trang Chủ Master Hub

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 1 | `https://www.momo.vn/tien-ich-giao-thong` | Master Hub trung tâm kết nối toàn bộ tiện ích & phân luồng phương tiện. |

#### 2. Dòng Xe & Hãng Xe (Auto Catalog pSEO)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 2 | `https://www.momo.vn/tien-ich-giao-thong/oto` | Chuyên trang tổng hợp ô tô, bảng giá xe & thông số kỹ thuật. |
| 3 | `https://www.momo.vn/tien-ich-giao-thong/xe-may` | Chuyên trang xe máy, xe tay ga, xe số & xe côn tay. |
| 4 | `https://www.momo.vn/tien-ich-giao-thong/xe-dien` | Chuyên trang xe máy điện, ô tô điện & xu hướng xanh. |
| 5 | `https://www.momo.vn/tien-ich-giao-thong/xe-tai` | Chuyên trang xe tải, xe bán tải & phương tiện thương mại. |
| 6 | `https://www.momo.vn/tien-ich-giao-thong/hang-xe/[brand]` | Danh sách dòng xe theo thương hiệu (Toyota, Honda, VinFast...). |
| 7 | `https://www.momo.vn/tien-ich-giao-thong/hang-xe/[brand]/[model]` | Chi tiết thông số, giá lăn bánh & phụ tùng từng mẫu xe cụ thể. |

#### 3. Phạt Nguội & Cẩm Nang Luật (Traffic Fines & Regulations)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 8 | `https://www.momo.vn/tien-ich-giao-thong/tra-cuu-muc-phat` | Từ điển tra cứu mức phạt giao thông ô tô/xe máy theo Nghị định. |
| 9 | `https://www.momo.vn/tien-ich-giao-thong/bien-bao-giao-thong` | Danh mục & ý nghĩa các loại biển báo đường bộ chuẩn QCVN. |
| 10 | `https://www.momo.vn/tien-ich-giao-thong/kinh-nghiem-lai-xe` | Cẩm nang mẹo lái xe an toàn, bảo dưỡng xe & luật giao thông mới. |

#### 4. Bản Đồ Tiện Ích & Nhiên Liệu (Maps & Fuel Stations)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 11 | `https://www.momo.vn/tien-ich-giao-thong/tram-sac` | Bản đồ & tìm kiếm trạm sạc xe điện toàn quốc theo GPS. |
| 12 | `https://www.momo.vn/tien-ich-giao-thong/tram-sac/vinfast` | Chuyên trang trạm sạc xe điện VinFast, V-Green. |
| 13 | `https://www.momo.vn/tien-ich-giao-thong/cay-xang` | Bản đồ tìm cây xăng gần nhất chấp nhận thanh toán MoMo. |
| 14 | `https://www.momo.vn/tien-ich-giao-thong/gia-xang` | Cập nhật bảng giá xăng dầu RON 95, E5, Diesel kỳ điều hành. |

#### 5. Công Cụ Tính Toán & So Sánh (Calculators & Comparison)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 15 | `https://www.momo.vn/tien-ich-giao-thong/lan-banh` | Tính chi phí lăn bánh ô tô (Thuế trước bạ, biển số, phí đường bộ). |
| 16 | `https://www.momo.vn/tien-ich-giao-thong/chi-phi-nuoi-xe` | Công cụ tính tổng chi phí vận hành & nuôi xe hàng tháng. |
| 17 | `https://www.momo.vn/tien-ich-giao-thong/so-sanh-xe` | So sánh thông số kỹ thuật & giá bán giữa 2-3 mẫu xe. |

#### 6. Pháp Lý, Đăng Kiểm & Hồ Sơ Xe (Vehicle Paperwork & Legal)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 18 | `https://www.momo.vn/tien-ich-giao-thong/dang-kiem` | Tra cứu hạn đăng kiểm & đặt lịch kiểm định xe. |
| 19 | `https://www.momo.vn/tien-ich-giao-thong/ho-so-xe` | Quản lý sổ Garage / Sổ tay thông tin xe cá nhân. |
| 20 | `https://www.momo.vn/tien-ich-giao-thong/diem-gplx` | Tra cứu điểm Giấy phép lái xe (12 điểm GPLX). |
| 21 | `https://www.momo.vn/tien-ich-giao-thong/sang-ten-xe` | Hướng dẫn thủ tục rút hồ sơ & sang tên đổi chủ xe. |
| 22 | `https://www.momo.vn/tien-ich-giao-thong/bien-so-xe` | Tra cứu mã tỉnh thành biển số xe trên toàn quốc. |
| 23 | `https://www.momo.vn/tien-ich-giao-thong/bien-so-dep` | Ý nghĩa phong thủy biển số xe & kết quả đấu giá biển đẹp. |
| 24 | `https://www.momo.vn/tien-ich-giao-thong/bao-hiem-o-to` | Mua & so sánh bảo hiểm TNDS, Thân vỏ xe 9 hãng. |

#### 7. Bãi Đỗ, Cứu Hộ, Bảo Dưỡng & Giao Thông (Mobility Services)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 25 | `https://www.momo.vn/tien-ich-giao-thong/bai-do-xe` | Tìm kiếm & đặt chỗ bãi đỗ ô tô / xe máy (VETC Parking). |
| 26 | `https://www.momo.vn/tien-ich-giao-thong/cuu-ho` | Gọi cứu hộ xe 24/7 (Kéo xe, vá lốp, kích bình). |
| 27 | `https://www.momo.vn/tien-ich-giao-thong/tram-thu-phi` | Tra cứu biểu phí ePass / VETC các trạm thu phí BOT. |
| 28 | `https://www.momo.vn/tien-ich-giao-thong/camera-giao-thong` | Xem camera giao thông quan sát điểm kẹt xe realtime. |
| 29 | `https://www.momo.vn/tien-ich-giao-thong/bao-duong` | Đặt lịch bảo dưỡng, rửa xe & chăm sóc xe (Detailing). |
| 30 | `https://www.momo.vn/tien-ich-giao-thong/chuyen-di` | Nhật ký chuyến đi & công cụ quản lý lộ trình. |

#### 8. Đối Tác Dịch Vụ (Partner Ecosystem)

| STT | URL | Mô Tả Chức Năng |
| :---: | :--- | :--- |
| 31 | `https://www.momo.vn/tien-ich-giao-thong/doi-tac` | Danh sách đối tác thuộc hệ sinh thái Giao thông MoMo. |
| 32 | `https://www.momo.vn/tien-ich-giao-thong/doi-tac/[slug]` | Trang chi tiết thông tin thương hiệu đối tác liên kết. |

---

#### 9. Standalone Root Pages Liên Kết Hệ Sinh Thái

Các trang sản phẩm độc lập có cấu trúc đường dẫn Root URL cấp 1 (`https://www.momo.vn/[slug]`), giữ nguyên vai trò SEO và giao dịch chuyên sâu, kết nối hai chiều với Master Hub theo Growth Strategy:

| Tên Trang Độc Lập | URL | Loại Trang | Mục Đích Tồn Tại & Cơ Chế Liên Kết Với Master Hub |
| :--- | :--- | :--- | :--- |
| **Tra Cứu Phạt Nguội** | `https://www.momo.vn/phat-nguoi` | Standalone Page (Root) | Cổng tra cứu vi phạm camera giao thông tốc độ cao (Top 1 Google, 6.1M traffic); giữ vai trò 'đầu phễu hút khách' lớn nhất để dẫn sang Master Hub lưu biển số và bán chéo bảo hiểm. |
| **Bảo Hiểm Ô Tô** | `https://www.momo.vn/bao-hiem-o-to` | Standalone Page (Root) | Trang so sánh quyền lợi và tính phí tự động của 9 hãng bảo hiểm; giúp chủ xe mua bảo hiểm TNDS & Thân vỏ online, nhận ấn chỉ điện tử sau 30 giây (nhận traffic từ Master Hub). |
| **Bảo Hiểm Xe Máy** | `https://www.momo.vn/bao-hiem-xe-may` | Standalone Page (Root) | Trang mua nhanh bảo hiểm bắt buộc xe máy 66k/năm bằng 1 chạm, nhận ngay giấy chứng nhận điện tử có mã QR để xuất trình CSGT (nhận traffic mua nhanh từ Master Hub). |
| **Thu Phí Không Dừng** | `https://www.momo.vn/phi-khong-dung` | Standalone Page (Root) | Hướng dẫn liên kết tài khoản và kích hoạt tính năng tự động nạp tiền ePass/VETC khi số dư dưới hạn mức, giúp tài xế qua trạm BOT thông suốt không bị kẹt xe. |

---

### 3.5 Web-to-App Entry Points & Routing Scope Boundaries

#### A. Ranh Giới Scope Web Platform vs App Product Team
* **Trách Nhiệm Kênh Web (Web Platform Scope):** Web Platform **chỉ chịu trách nhiệm khởi tạo và thiết lập các điểm chạm Entry Points trên Kênh Web** (`momo.vn`) để người dùng nhấp nút hoặc quét mã chuyển tiếp mở ứng dụng MoMo. Web Platform không gánh scope vận hành hay xây dựng luồng sản phẩm phía App.
  * **Trên thiết bị Desktop (Máy tính):** Web Platform thiết lập Entry Point dưới dạng **Dynamic QR Code Modal** chứa thông tin tra cứu / mã biển số.
  * **Trên thiết bị Mobile (Điện thoại/Tablet):** Web Platform thiết lập Entry Point dưới dạng **Nút bấm CTA / Banner** gắn đường dẫn Onelink tiêu chuẩn.
* **Trách Nhiệm Sản Phẩm Phía App (App Product Scope - Cell Teams / App Team):** Đội ngũ Sản phẩm phía App chịu trách nhiệm 100% về luồng sản phẩm In-App (App Product Flow), bao gồm: tiếp nhận luồng mở App từ Onelink/QR, điều hướng màn hình In-App (Internal Routing Schema), hiển thị màn hình Mini App / Vehicle Center và xử lý logic giao dịch.

#### B. Chuỗi Chuyển Tiếp & Phân Định Đỉnh Trạm Entry Points

* **Chuỗi phân luồng chuyển tiếp Entry Points:**
  `[Bấm nút Entry Point trên Web Mobile]` ➔ `[Kích hoạt đường dẫn Onelink tiêu chuẩn]` ➔ `[Hệ thống Onelink phân luồng: Đã cài App ➔ Mở App MoMo / Chưa cài App ➔ Điều hướng về App Store / Google Play]` ➔ `[Chuyển giao cho Luồng Sản Phẩm Phía App xử lý]`

| Bước | Tên Giai Đoạn | Trải Nghiệm Người Dùng (UX) | Hạ Tầng / Cơ Chế Kỹ Thuật | Phân Định Trách Nhiệm Scope |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Nhấp điểm chạm Entry Point trên Web | Bấm nút hành động ('Lưu biển số' / 'Nhận thông báo' / 'Mua ngay') | Bắt sự kiện Click trên Web, kích hoạt mở đường dẫn Onelink tiêu chuẩn | **100% Web Platform Scope (Entry Point)** |
| **2** | Phân luồng chuyển tiếp | Chuyển tiếp tức thì, không bị gián đoạn màn hình trắng | Onelink Engine (Appsflyer) xử lý định tuyến theo trạng thái thiết bị | **Web Platform x InsurTech / VTTI Scope** |
| **3A** | Mở ứng dụng In-App | Mở ứng dụng MoMo vào đúng màn hình tiện ích xe tương ứng | Luồng tiếp nhận schema và chuyển tiếp màn hình nội bộ trên App | **100% App Product Scope (InsurTech / VTTI)** |
| **3B** | Cài đặt ứng dụng | Chuyển đến trang tải ứng dụng MoMo trên Store | Điều hướng Store (App Store trên iOS / Google Play trên Android) | **Store Platform Scope** |

#### C. Phối Hợp Đội Ngũ (Team Alignment)
* **Web Platform:** Chủ trì thiết kế và phát triển Kênh Web, tối ưu lưu lượng tìm kiếm tự nhiên (500K Traffic) và tích hợp các điểm chạm Entry Points (nút bấm CTA, mã Dynamic QR, Onelink) dẫn dắt chuyển đổi W2A.
* **InsurTech Cell:** Đơn vị chủ trì chính về **Khung KPI, Mục tiêu Tăng trưởng (Growth) và Doanh thu Bảo hiểm**; vận hành luồng mua Bảo hiểm xe máy, Bảo hiểm ô tô và thúc đẩy tỷ lệ hoàn tất đơn hàng (+10% CR Uplift) qua cơ chế Auto-fill từ dữ liệu Web.
* **VTTI:** Đơn vị chủ trì và sở hữu toàn bộ **API Sản Phẩm và Dữ Liệu Đối Tác** (API Cây xăng, Trạm sạc EV, Garage, Biểu phí BOT, ePass); quản trị hạ tầng backend của tính năng Thẻ Xe Số (Vehicle Profile) In-App.
* **Content Team:** Chủ trì sản xuất bài viết cẩm nang và nội dung hướng dẫn giao thông.

---

### 3.6 Technical SEO, Local GEO & Data Sync

* **Tối ưu hóa Technical SEO & Local GEO Sản Phẩm:**
  * **Cấu trúc dữ liệu có cấu trúc (Schema Markup JSON-LD):** Nhúng toàn diện các Schema chuẩn Google (`AutoRental`, `LocalBusiness`, `GeoCoordinates`, `ItemList`, `FAQPage`) giúp tăng tỷ lệ xuất hiện Rich Snippets và Google AI Overview (AIO).
  * **Tối ưu Local GEO & GPS Maps:** Định vị tọa độ địa lý chuẩn xác cho mạng lưới Cây xăng, Trạm sạc EV và Garage sửa xe theo vị trí thời gian thực của người dùng và hệ thống bộ lọc Top 5 tỉnh/thành phố lớn (Hà Nội, TP.HCM, Đà Nẵng, Hải Phòng, Cần Thơ).
  * **Tối ưu tốc độ tải trang:** Tối ưu hóa cấu trúc mã nguồn, nén ảnh và tài nguyên tĩnh đảm bảo tốc độ phản hồi nhanh trên nền tảng Next.js / MoSpark CMS.
* **Cơ chế lưu và cập nhật dữ liệu (CDN Cache):**
  * Trang Web chỉ đọc dữ liệu tĩnh từ CDN Cache, không gọi API trực tiếp vào máy chủ giao dịch In-App.
  * **Bảng giá xăng:** Cập nhật tự động lúc 15:00 thứ Năm hàng tuần theo kỳ điều hành của Bộ Công Thương.
  * **Bản đồ cây xăng & Trạm sạc EV:** Nhận file dữ liệu nạp vào CDN 1 lần/tuần (tiếp nhận ngày 11/09/2026).

---

## IV. RISK & ROADMAP

### 4.1 Risk Management

| Rủi Ro Tiềm Tàng | Mức Độ | Phương Án Dự Phòng (Fallback Plan) | Đội Ngũ Phụ Trách |
| :--- | :---: | :--- | :--- |
| **API Cục Đăng Kiểm bảo trì / gián đoạn** | Cao | Chuyển sang luồng **Tự khai báo ngày hết hạn đăng kiểm** trên Web để đăng ký nhận nhắc lịch qua App MoMo. | Web Platform |
| **API Cây xăng / Garage quá tải hoặc chậm tiến độ** | Trung bình | Áp dụng **cơ chế Batch Sync định kỳ** (đồng bộ danh sách cây xăng/garage theo tuần, giá xăng theo kỳ công văn) để tránh quá tải API Backend; Điều chỉnh mốc API sang **11/09/2026** do nghỉ lễ 2/9. | Web Platform x VTTI |
| **Lộ thông tin cá nhân chủ xe trên Web public** | Cao | Áp dụng quy tắc Web Compliance: Ẩn 100% PII, thông tin bảo hiểm và định giá xe khi tra cứu public trên Web. | Web Product Lead |

---

### 4.2 Roadmap

| Giai Đoạn | Thời Gian | Tên Giai Đoạn | Chi Tiết Triển Khai (Web Platform) & Mục Tiêu |
| :--- | :---: | :--- | :--- |
| **Phase 1 (Build-Up)** | 25/08 - 25/09/2026 | **Build Master Hub & 5 Tiện Ích Lõi** | • Dựng khung HTML/CSS **Trang chủ `/tien-ich-giao-thong`** và **5 Tiện ích: ePass (`/epass`), Giá Xăng (`/gia-xang`), Cây Xăng (`/cay-xang`), Trạm Sạc (`/tram-sac`), Garage (`/tim-garage`)** theo thiết kế (hạn 25/08).<br>• Tối ưu hiệu năng tải trang và khả năng tiếp cận người dùng (Schema JSON-LD, định vị GPS Cây xăng/Trạm sạc/Garage).<br>• Tiếp nhận dữ liệu cây xăng/trạm sạc theo cơ chế Batch Sync (11/09).<br>• **CHÍNH THỨC GO-LIVE TRANG CHỦ & 5 TIỆN ÍCH LÕI (25/09/2026).** |
| **Phase 2 (Expansion)** | Tháng 10/2026 | **Mở Rộng Dịch Vụ & Pháp Lý** | • Triển khai tiếp các Tiện ích con: Phong Thủy & Đấu Giá (`/phong-thuy-bien-so`), Tra Cứu Mức Phạt (`/tra-cuu-muc-phat`), Đăng Kiểm (`/dang-kiem`).<br>• Liên kết luồng hai chiều giữa Master Hub và các trang độc lập (`/phat-nguoi`, `/bao-hiem`, `/phi-khong-dung`).<br>• Tối ưu hóa chuyển đổi W2A CTR đạt mốc mục tiêu **8.0% - 10.0%**.<br>• Tự động hóa bài viết cẩm nang giao thông qua GenAI Content Pipeline. |
| **Phase 3 (Scale-Up)** | Tháng 11 - 12/2026 | **Mở Rộng Quy Mô Dữ Liệu & Thẻ Xe Số** | • Mở rộng quy mô cơ sở dữ liệu động Top 5 tỉnh/thành lớn cho Trạm sạc EV và Garage sửa xe.<br>• Thu thập dữ liệu biển số xe từ phễu Web để khởi tạo Thẻ Xe Số In-App.<br>• Hỗ trợ Auto-fill thông tin xe khi mua bảo hiểm In-App (CR uplift +10%). |

---

### 4.3 RACI Matrix (16 Hạng Mục Chi Tiết Phối Hợp)

| Nhóm & Hạng Mục Công Việc Chi Tiết | Web Platform (Web & W2A) | InsurTech Cell (KPI & Bảo Hiểm) | VTTI (API & Giao Thông) |
| :--- | :---: | :---: | :---: |
| **I. CHIẾN LƯỢC, CHỈ SỐ & KẾ HOẠCH VẬN HÀNH** | | | |
| 1.1 Thống nhất Mục tiêu & Khung KPI Đồng Sở Hữu | **A / R (Chủ trì Web)** | **A / R (Đồng sở hữu)** | **A / R (Đồng sở hữu)** |
| 1.2 Lập Kế Hoạch Sprint 1 Tháng & Check-in 2 Tuần/Lần | **A / R (Chủ trì)** | **A / R (Đồng chủ trì)** | R (Tham gia API) |
| **II. GIAO DIỆN WEB & PHỄU CHUYỂN ĐỔI (W2A)** | | | |
| 2.1 Xây dựng Trang Chủ Master Hub (`/tien-ich-giao-thong`) | **A / R (Chủ trì)** | C (Góp ý phễu BH) | C (Cung cấp API) |
| 2.2 Phát triển Widget 3-in-1 Trước Khi Lăn Bánh | **A / R (Chủ trì)** | C (Góp ý phễu) | C (Cung cấp API) |
| 2.3 Cấu hình Điểm Chạm Chuyển Đổi (Onelink & Dynamic QR) | **A / R (Chủ trì)** | C (Góp ý luồng BH) | C (Cung cấp Schema API) |
| 2.4 Xây dựng Bảng Giá Xăng & Máy Tính Đầy Bình (`/gia-xang`) | **A / R (Chủ trì Web)** | I (Theo dõi) | C (Cung cấp Data API) |
| **III. QUẢN TRỊ DỮ LIỆU ĐỊA ĐIỂM & BẢN ĐỒ TIỆN ÍCH** | | | |
| 3.1 Cung cấp Danh sách Cây Xăng Toàn Quốc (API / Sheet) | A (Nghiệm thu Web) | I (Theo dõi) | **A / R (Chủ trì API & Data)** |
| 3.2 Cung cấp Danh mục Trạm Sạc Xe Điện EV (VinFast, V-Green) | A (Nghiệm thu Web) | I (Theo dõi) | **A / R (Chủ trì API & Data)** |
| 3.3 Cung cấp Mạng Lưới Garage, Vá Lốp & Cứu Hộ | A (Nghiệm thu Web) | I (Theo dõi) | **A / R (Chủ trì API & Data)** |
| 3.4 Xây dựng Bản Đồ Tìm Kiếm Địa Điểm GPS trên Web | **A / R (Chủ trì)** | I (Theo dõi) | C (Hỗ trợ API) |
| **IV. BỘ CÔNG CỤ DỰ TOÁN CHI PHÍ & CHUYỂN TIẾP LEAD BẢO HIỂM** | | | |
| 4.1 Tra Cứu Biểu Phí BOT & Nút Mở App Nạp ePass (`/tram-thu-phi`) | **A / R (Xây Web & CTA)** | I (Theo dõi) | **A / R (Cung cấp API ePass)** |
| 4.2 Máy Tính Chi Phí Lăn Bánh, Nuôi Xe & Dự Toán Phí BH | **A / R (Chủ trì Web Tool)** | C (Góp ý công thức BH) | I (Theo dõi) |
| 4.3 Tra Cứu Đăng Kiểm, 12 Điểm GPLX & Phong Thủy Biển Số | **A / R (Chủ trì Web)** | C (Góp ý nghiệp vụ) | C (Góp ý luật GT) |
| 4.4 Bắt & Chuyển Tiếp Dữ Liệu Biển Số Xe Cho InsurTech | **A / R (Bắt Lead Web)** | **A / R (Nhận Auto-fill)** | C (Hỗ trợ Data xe) |
| **V. CẨM NANG HƯỚNG DẪN TRÊN WEB & BÁO CÁO GIẢI TRÌNH** | | | |
| 5.1 Cổng Cẩm Nang Giao Thông, FAQ & Giải Đáp Luật Trên Web | **A / R (Chủ trì Web)** | C (Duyệt luật BH) | C (Duyệt luật GT) |
| 5.2 Báo Cáo Tiến Độ Sản Phẩm Web & Hiệu Quả W2A (IVP) | **A / R (Chủ trì tổng hợp)** | **A / R (Đồng chủ trì Báo cáo)** | R (Báo cáo API) |

---

### 4.4 Change Log

| Phiên Bản | Ngày Cập Nhật | Đội Ngũ Thực Hiện | Nội Dung Thay Đổi Chi Tiết |
| :---: | :---: | :---: | :--- |
| **v8.2** | 2026-08-26 | Web Product Lead | **Tinh Gọn Ma Trận RACI Chỉ Gồm 3 Đơn Vị Nòng Cốt:** Bỏ Content Team khỏi ma trận RACI; quy hoạch toàn bộ ma trận chỉ gồm **3 đơn vị nòng cốt: Web Platform, InsurTech Cell và VTTI**; Web Platform chủ trì xây dựng cổng cẩm nang giao thông & FAQ trên Web. |
| **v8.1** | 2026-08-26 | Web Product Lead | **Loại Bỏ Tiện Ích Metro Khỏi Phạm Vi Vehicle Hub:** Loại bỏ trang `/metro` (Lịch trình & Giá vé Metro) và từ khóa liên quan; chuẩn hóa Sitemap toàn bộ hệ sinh thái thành **32 URLs** và dung lượng tìm kiếm toàn thị trường thành **20.106.020 lượt/tháng (20 Chủ đề)**. |

---

### 4.4 Change Log

| Phiên Bản | Ngày Cập Nhật | Đội Ngũ Thực Hiện | Nội Dung Thay Đổi Chi Tiết |
| :---: | :---: | :---: | :--- |
| **v8.1** | 2026-08-26 | Web Product Lead | **Loại Bỏ Tiện Ích Metro Khỏi Phạm Vi Vehicle Hub:** Loại bỏ trang `/metro` (Lịch trình & Giá vé Metro) và từ khóa liên quan; chuẩn hóa Sitemap toàn bộ hệ sinh thái thành **32 URLs** và dung lượng tìm kiếm toàn thị trường thành **20.106.020 lượt/tháng (20 Chủ đề)**. |
| **v8.0** | 2026-08-26 | Web Product Lead | **Loại Bỏ Hoàn Toàn FS/FinHub & Chuẩn Hóa Nhóm IV Cho InsurTech:** Khẳng định dự án chỉ gồm **3 đơn vị nòng cốt: Web Platform, InsurTech Cell (Bảo hiểm) và VTTI (Giao thông/ePass)** (phối hợp Content Team); Nhóm IV quy hoạch thành **Bộ công cụ dự toán chi phí & chuyển tiếp Lead cho InsurTech** (Auto-fill Bảo hiểm Thân vỏ & TNDS). |
| **v7.9** | 2026-08-26 | Web Product Lead | **Xác Lập Vai Trò Nòng Cốt Giữa FS & VTTI:** Chuẩn hóa quyền sở hữu: **FS (Financial Services / InsurTech) là chủ sở hữu chính về Khung KPI, Mục tiêu Tăng trưởng (Growth) và Doanh thu bán chéo**; **VTTI là chủ sở hữu các API Sản phẩm và Dữ liệu Đối tác** (ePass, Cây xăng, Trạm sạc EV, Garage); **Web Platform chủ trì Kênh Web và phễu W2A**. |
| **v7.8** | 2026-08-26 | Web Product Lead | **Phân Rã Ma Trận RACI Chi Tiết:** Phân rã toàn bộ ma trận phối hợp thành **16 hạng mục công việc cụ thể phân bổ trong 5 nhóm rõ ràng**; loại bỏ hoàn toàn các thuật ngữ học thuật phức tạp, chuẩn hóa ngôn ngữ thực tế và đồng bộ giữa BRD và file Excel Master. |
| **v7.7** | 2026-08-26 | Web Product Lead | **Chuẩn Hóa Đội Ngũ Nòng Cốt:** Loại bỏ User Growth; chuẩn hóa cơ cấu hợp tác trực tiếp giữa **3 đơn vị nòng cốt: Web Platform, InsurTech Cell và VTTI** (phối hợp Content Team); nâng cấp ma trận RACI thành 7 Dòng Hoạt Động Product & Growth. |
| **v7.5** | 2026-08-24 | Web Product Lead | **Chuẩn Hóa Toàn Bộ Sitemap 33 URLs:** Cập nhật bảng tổng hợp Sitemap toàn bộ 33 URLs thuộc hệ sinh thái Tiện Ích Giao Thông theo 8 nhóm chức năng chính; chuẩn hóa định dạng cột `STT`, `URL` (sử dụng domain chuẩn `https://www.momo.vn/`), `Mô Tả Chức Năng` và loại bỏ cột Router. |
| **v7.4** | 2026-08-20 | Web Product Lead | **Cập Nhật Scope Go-Live Tháng 8 & Quản Trị Dữ Liệu Algify:** Thống nhất danh mục 5 Subpages Go-live Tháng 8 gồm **ePass (`/epass`), Giá xăng (`/gia-xang`), Cây xăng (`/cay-xang`), Trạm sạc EV (`/tram-sac`), Garage (`/tim-garage`)**. Đóng gói 3 Sheet dữ liệu (Garage, Cây xăng, Trạm sạc) dùng chung Web & App qua hạ tầng Algify. Cập nhật giao diện Hero Section (3 promotions cố định), nhãn Badge danh mục (show all), quy chuẩn logo Cây xăng (PVOil, Comeco chính thức, cây khác dùng default logo), bộ lọc hãng Trạm sạc EV và hạ tầng Captcha Bảo hiểm Ô tô. |
| **v7.3** | 2026-08-20 | Web Product Lead | **Tinh Gọn Phối Hợp Đội Ngũ (Mục 3.5.C):** Cô đọng phần Team Alignment chỉ đề cập các hạng mục công việc lớn của từng đội ngũ (User Growth: hạ tầng Onelink & tracking; Web Platform: thiết lập Entry Points trên Web; App Product Team/Cell Teams: quản trị luồng sản phẩm In-App), không sa đà vào các tham số hay kỹ thuật triển khai chi tiết. |
| **v7.2** | 2026-08-20 | Web Product Lead | **Chuẩn Hóa Phân Định Scope Web-to-App Routing (Mục 3.5):** Quy định rõ ranh giới trách nhiệm của Web Platform là **chỉ chịu trách nhiệm thiết lập các điểm chạm Entry Points trên Kênh Web** (`momo.vn`) như Nút CTA, Dynamic QR Code (Desktop), Onelink (Mobile). Toàn bộ luồng sản phẩm phía App (In-App Product Flow) và điều hướng màn hình nội bộ App thuộc trách nhiệm quản trị 100% của Đội ngũ Sản phẩm phía App (App Product Team / Cell Teams). |
| **v7.1** | 2026-08-20 | Web Product Lead | **Cập Nhật Search Volume Tra Cứu Mức Phạt:** Cập nhật dung lượng tìm kiếm thực tế cho tiện ích Tra Cứu Mức Phạt Giao Thông (STT 15 - Mục 2.1) đạt **25.000 lượt/tháng**. |
| **v7.0** | 2026-08-19 | Web Product Lead | **Chuẩn Hóa Luồng Kết Quả Phạt Nguội & Cẩm Nang Inline Block:** Tái cấu trúc trang Phạt nguội (`/phat-nguoi`), loại bỏ popup; phân 2 nhánh trả kết quả (Có vi phạm: Nộp phạt In-App + Inline Content Block giải thích lỗi theo Nghị định; Không vi phạm: Cross-sell Bảo hiểm & Gói đăng ký nhận thông báo phạt nguội tự động qua Mini App MoMo). |
| **v6.9** | 2026-08-17 | Web Product Lead | **Bổ sung Quy chuẩn Menu Header:** Thêm Mục 3.3 quy định chi tiết cấu trúc thanh điều hướng Header Navigation (Logo, 6 cụm menu dropdown/spokes, Nút hành động CTA chuyển đổi Dynamic QR / Onelink và cơ chế hiển thị Sticky Responsive Mobile). |
| **v6.8** | 2026-08-16 | Web Product Lead | **Xác lập Scope Web Platform Tháng 8:** Quy định rõ phạm vi xây dựng trong Tháng 8 (Phase 1.1) gồm **Trang chủ Master Hub `/tien-ich-giao-thong` + 4 Subpages tiện ích trọng tâm: Giá Xăng (`/gia-xang`), Cây Xăng (`/cay-xang`), Trạm Sạc EV (`/tram-sac`), Garage (`/tim-garage`)**. Cập nhật mốc Go-live 25/09/2026 cho toàn bộ cụm 5 trang này. |
| **v6.7** | 2026-08-16 | Web Product Lead | Chuẩn hóa toàn bộ Heading tiếng Anh ngắn gọn: Cập nhật các đề mục chính và phụ sang tiếng Anh chuẩn Product Design/PRD (`Overview`, `Market Demand & Compliance`, `Product Spec`, `Risk & Roadmap`, `Scope & Objectives`, `Web-to-App Flywheel`, `Sitemap Architecture`, `RACI Matrix`...). |
| **v6.6** | 2026-08-16 | Web Product Lead | Bổ sung Quy chuẩn An ninh & Ma trận RACI: Thêm Mục 3.5 quy định Invisible Captcha và cơ chế Data Batch Sync định kỳ vào MoSpark CDN bảo vệ Core Backend. Thêm Mục 4.3 Ma trận phân định trách nhiệm RACI Matrix. |
| **v6.5** | 2026-08-16 | Web Product Lead | Loại bỏ tư tưởng Deeplink trên Web: Quy chuẩn 100% các điểm chạm CTA chuyển đổi sang App sử dụng Onelink tiêu chuẩn (Mobile) và Dynamic QR Code (Desktop) do User Growth cấp. Thay thế sơ đồ Mermaid bằng Chuỗi luồng trực quan và Bảng Markdown phân tích các bước tương thích hoàn hảo Google Docs. Tách riêng bảng Sitemap Master Hub (/tien-ich-giao-thong/*) và bảng Standalone Root Pages kèm cột Mục đích tạo trang. |
| **v6.4** | 2026-08-14 | Web Product Lead | Đại tu toàn bộ văn phong & Chuẩn hóa Bảng biểu Markdown. Bổ sung chi tiết Spoke Utilities: Phong Thủy & Đấu Giá Biển Số, Tra Cứu Mức Phạt NĐ 100/123, Luật Biển số định danh Thông tư 24. |
| **v6.3** | 2026-08-14 | Web Product Lead | Cập nhật Spoke Utilities Phong Thủy/Đấu giá biển số và Tra Cứu Mức Phạt Giao Thông. |
| **v6.2** | 2026-08-04 | Web Product Lead | Cập nhật bộ 11.104 từ khóa độc lập và phễu Kênh Website Reach ~20.1 triệu lượt/tháng. |

