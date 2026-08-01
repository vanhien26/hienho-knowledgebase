# BRD: Merchant Hub - Cổng Thông Tin & Nền Tảng Đối Tác Merchant MoMo

> - **Project:** Merchant Hub (Web Platform & Merchant Profile Identity)
> - **Platform:** Web Platform (`momo.vn/merchant`, `momo.vn/cua-hang`)
> - **Division:** Growth Platform Division (GPD)
> - **Owner:** Web Platform Team (GPD)

---

## I. Executive Summary

### 1.1 Core Problems & Objectives
* **Vấn đề thực tế (Problem Statement):** Hàng triệu hộ kinh doanh cá thể, cửa hàng offline và chuỗi SME tại Việt Nam đang thiếu sự hiện diện số hóa chuẩn SEO trên Open Web (Google Search, Google Maps, AI Search). Họ đối mặt với chi phí quảng cáo đắt đỏ, khó tiếp cận khách hàng tiềm năng xung quanh khu vực (Local GEO), đồng thời gặp rào cản trong việc quản lý doanh thu, phòng tránh thất thoát khi nhận chuyển khoản và tiếp cận các giải pháp tài chính linh hoạt.
* **Mục tiêu định lượng:** Hợp nhất toàn bộ nhu cầu tìm kiếm địa điểm mua sắm, ăn uống O2O và kéo **>1.500.000 - 2.500.000 Organic Visits/tháng** về `momo.vn/merchant`, chuyển đổi lượng truy cập tự nhiên này thành giao dịch tại cửa hàng offline và tạo nguồn leads tư vấn thiết bị Loa báo chuyển tiền Soundbox.
* **Triết lý cốt lõi:** **"Một Cửa Hàng - Một Trang Định Danh Số"**, biến địa chỉ/thương hiệu của merchant thành trung tâm kết nối Online-to-Offline (O2O) tự động:
  1. **Một lần khai báo, số hóa chuẩn SEO trọn đời:** Đưa thông tin cửa hàng, menu/sản phẩm, địa chỉ Google Maps, giờ mở cửa và phương thức thanh toán MoMo lên Open Web chuẩn SEO chỉ trong 3 phút.
  2. **Chủ động thu hút, tự động chuyển đổi:** Tự động phát hành Voucher O2O 1-click trên Web, dẫn dắt khách hàng ghé shop quét mã MoMo / Ví Trả Sau, và giới thiệu giải pháp Loa báo chuyển tiền Soundbox chống thất thoát.
  3. **Một hệ sinh thái cho mọi hộ kinh doanh:** Kết nối chủ shop với toàn bộ tiện ích tài chính & tăng trưởng của MoMo (Ví Trả Sau, Loa Soundbox, QR Cửa hàng, MoMo Rewards).

### 1.2 Situation - Complication - Resolution
* **Situation (Bối cảnh & Vai trò Website):** Khi phát sinh nhu cầu ăn uống, mua sắm, tìm tiệm làm đẹp, dịch vụ sửa chữa hay siêu thị tiện lợi gần nhất, phản xạ tự nhiên của người dùng là tra cứu trên Google hoặc các công cụ AI Search (ChatGPT, Gemini, Perplexity). Website `momo.vn` đóng vai trò là **"cửa ngõ hứng nhu cầu O2O và cổng định danh Merchant"**. Bằng các tiện ích tra cứu địa điểm, menu, bảng giá và kho voucher O2O trực tuyến, Website giải quyết tức thời nhu cầu của người dùng, từ đó thu thập dữ liệu vị trí và thiết lập Hồ sơ Cửa hàng (Merchant Profile).
* **Complication (Khó khăn & Thách thức):** Nếu thông tin merchant chỉ nằm sâu trong ứng dụng di động đóng (App-only ecosystem), MoMo sẽ hoàn toàn vô hình trước hàng chục triệu lượt tìm kiếm tự nhiên ngoài Open Web. Hậu quả là lượng Traffic có ý định mua sắm cao (High purchase intent) sẽ chảy sang các nền tảng bên thứ ba (ShopeeFood, Grab, Foody), đồng thời việc ép người dùng tải App ngay lần đầu tìm kiếm địa điểm sẽ tạo ra rào cản đứt gãy lớn.
* **Resolution (Giải pháp):** Xây dựng **Merchant Hub** hoạt động theo mô hình Product-Led Growth (PLG) & Hub-and-Spoke: Hứng traffic tự nhiên từ Open Web qua các Utility Category Spoke Pages (Đồ ăn, Đồ uống, Bách hoá, Làm đẹp, Mua sắm...) $\rightarrow$ Khởi tạo Hồ sơ Cửa hàng (Merchant Profile) $\rightarrow$ Điều hướng Web-to-App (W2A) để thu thập Voucher O2O & thực hiện giao dịch quét QR thanh toán tại shop.

### 1.3 Product-Led Growth (PLG) Strategy
Cơ chế PLG của Merchant Hub dựa trên 5 "Phễu Mồi Câu" (Acquisition & Engagement Hooks) giải quyết nhu cầu tìm kiếm tức thì ngoài Open Web để dẫn dắt người dùng tự nguyện khám phá cửa hàng và chuyển đổi sang App (Web-to-Merchant-to-App Flywheel):

1. **Phễu Tra Cứu Địa Điểm & Menu (Acquisition Gate):** Xem vị trí Google Maps, menu/bản giá sản phẩm và đánh giá cửa hàng gần đây không cần đăng nhập $\rightarrow$ Bấm "Thu thập Voucher O2O" $\rightarrow$ Dẫn dắt kích hoạt App MoMo.
2. **Phễu Săn Voucher O2O (Conversion Hook):** Nhận voucher giảm giá trực tiếp trên Web với 1-click $\rightarrow$ Thúc đẩy người dùng di chuyển đến cửa hàng offline quét mã MoMo / Ví Trả Sau để sử dụng voucher.
3. **Phễu Đăng Ký Loa Soundbox (B2B Merchant Lead Gen Hook):** Landing page & Widget giới thiệu thiết bị Loa báo chuyển tiền Soundbox cho chủ cửa hàng $\rightarrow$ Điền form tư vấn nhận cuộc gọi từ bộ phận kinh doanh M4B.
4. **Phễu Cửa Hàng Hỗ Trợ Ví Trả Sau (High-Value Intent Hook):** Tra cứu danh sách cửa hàng/chuỗi mua sắm chấp nhận thanh toán Ví Trả Sau 0% lãi suất $\rightarrow$ Dẫn dắt kích hoạt Ví Trả Sau và mua sắm đơn hàng giá trị cao.
5. **Phễu Đánh Giá & MoMo Rewards (Retention Hook):** Người dùng quét QR thanh toán tại merchant được tích điểm đổi quà MoMo Rewards $\rightarrow$ Khuyến khích người dùng quay lại đánh giá cửa hàng trên Web Platform.

### 1.4 Key Metrics & Targets

#### Dual North Star Metrics

| Platform Layer | North Star Metric | Definition | Target | Strategic Role |
| :--- | :--- | :--- | :--- | :--- |
| **Web Platform** *(Primary Goal)* | **Total Organic Web Traffic** | Tổng lượt truy cập tự nhiên từ Google Search và AI Search vào các trang Merchant Pages & Category Hubs mỗi tháng. | **1.5M - 2.5M Visits/tháng** | Mục tiêu cốt lõi: Hứng tối đa nhu cầu tìm kiếm địa điểm, ăn uống, mua sắm O2O ngoài Open Web (~15M+ volume/tháng). |
| **In-App & Merchant Layer** *(Secondary Layer)* | **Voucher Redemption Rate & Soundbox Leads** | Tỷ lệ đổi Voucher O2O thành công tại shop & Tổng số Leads tư vấn mua thiết bị Soundbox từ chủ shop. | **Voucher Redemption >35%**<br>**Soundbox Leads $\ge 15.000$/tháng** | Đo lường hiệu quả O2O chuyển đổi traffic Web thành giao dịch thực tế tại cửa hàng & doanh thu phần cứng/dịch vụ M4B. |

#### Web Platform Metric Tree

1. **Organic Traffic & Search Reach**
   * **Đồ Ăn & Nhà Hàng:** Top 1-3 Organic Search Google cụm từ khóa tìm kiếm địa điểm ăn uống, đạt **>600.000 visits/tháng**.
   * **Đồ Uống & Quán Cà Phê:** Hứng **>500.000 visits/tháng** nhu cầu tìm quán cà phê, trà sữa gần đây.
   * **Bách Hoá & Siêu Thị Mini:** Hứng **>350.000 visits/tháng** tìm tạp hoá, chợ truyền thống, cửa hàng tiện lợi.
   * **Làm Đẹp - Sức Khỏe & Mua Sắm:** Hứng **>400.000 visits/tháng** tìm spa, hair salon, cửa hàng thời trang, điện máy.

2. **Web Engagement & Identification**
   * **Tỷ Lệ Thu Thập Voucher (Claim Rate):** Đạt **15% - 20%** lượt truy cập trang Merchant thực hiện 1-click thu thập Voucher O2O.
   * **Tỷ Lệ Điều Hướng Web-to-App (W2A CVR):** Đạt **>30%** người dùng thu thập voucher thực hiện mở App MoMo để lưu voucher/thanh toán.
   * **Tỷ Lệ Đăng Ký Tư Vấn Soundbox:** Đạt **3% - 5%** chủ shop truy cập trang Soundbox điền thông tin tư vấn thành công.

3. **Commercial Conversion**
   * **O2O Transactions:** Đạt **>250.000 giao dịch QR thành công/tháng** tại merchant xuất phát từ các chiến dịch O2O Voucher trên Web.
   * **Ví Trả Sau Activation:** Đạt **>10.000 lượt kích hoạt/sử dụng Ví Trả Sau** tại các merchant thuộc danh mục Mua sắm & Điện máy.

#### Phase 1 Pilot Targets (Cell Team Alignment T9 - T12/2026)

| STT | Chỉ Số (Key Metric) | Baseline (H1/2026) | Target Phase 1 Pilot (T9 - T12/2026) | Ghi Chú Thực Thi |
| :---: | :--- | :---: | :---: | :--- |
| 1 | **Phase 1 Organic Traffic** | 450K/tháng | **1.500.000 Visits** | Mở rộng SEO Hub theo 14 nhóm ngành nghề chính & 53 ngành nghề phụ |
| 2 | **Web-to-App Conversion Rate (W2A CVR)** | 18% | **>= 30% CVR** | Tỷ lệ từ xem Web Merchant Page sang Thu thập Voucher / Mở App MoMo |
| 3 | **O2O Voucher Redemptions** | 35.000/tháng | **120.000 Redemptions** | Số lượt sử dụng voucher thành công khi quét QR thanh toán tại shop |
| 4 | **Soundbox Qualified Leads** | 2.100/tháng | **8.500 Leads/tháng** | Leads chủ cửa hàng đăng ký tư vấn mua thiết bị Loa Soundbox từ Web |
| 5 | **SEO Ranking (Merchant & Category Keywords)** | Top 15-30 | **Top 1 - Top 10 Keywords** | Đưa các cụm từ khóa địa điểm (`quán ăn gần đây`, `tiệm cà phê mo mo`...) lọt Top 1-10 |
| 6 | **Merchant Profile Verified Rate** | 5% | **>25% Verified** | Tỷ lệ chủ cửa hàng thực hiện xác minh quyền sở hữu trang Merchant Page |

---

## II. Market Context & Strategy

### 2.1 Market Sizing & Opportunity
* **Quy mô thị trường Hộ kinh doanh & SME tại Việt Nam:**
  * **Hộ kinh doanh cá thể:** Hơn 5,2 triệu hộ kinh doanh cá thể đang hoạt động trên toàn quốc.
  * **Doanh nghiệp SME:** Hơn 900.000 doanh nghiệp vừa và nhỏ, trong đó nhóm bán lẻ và F&B chiếm hơn 45%.
* **Cơ hội O2O từ M4B & GPD:** Việc MoMo sở hữu mạng lưới hàng trăm ngàn merchant chấp nhận thanh toán QR kết hợp với năng lực thu hút traffic tự nhiên trên Web tạo ra vòng lặp O2O hoàn chỉnh: Tìm kiếm trên Google $\rightarrow$ Xem Merchant Page $\rightarrow$ Thu thập Voucher O2O $\rightarrow$ Ghé cửa hàng quét QR MoMo / Ví Trả Sau $\rightarrow$ Đăng ký Loa Soundbox chống thất thoát.

### 2.2 Cross-BU Synergy & Data Consolidation
MoMo sở hữu lợi thế cạnh tranh tuyệt đối khi kết hợp sức mạnh giữa **Web Platform (GPD)**, **M4B (Merchant Platform)**, **Ví Trả Sau (FS)** và **Loa Soundbox (VTTI/Hardware)**:
1. **Quy mô kho dữ liệu Merchant:** MoMo đang quản lý tệp dữ liệu hơn **500.000+ điểm chấp nhận thanh toán**, tạo tiền đề số hóa thành 500.000+ Merchant Pages chuẩn SEO trên Open Web mà không tốn chi phí khởi tạo nội dung ban đầu.
2. **Cơ chế Bán Chéo Dịch Vụ Tài Chính (Cross-sell Synergy):** Khách hàng tra cứu cửa hàng mua sắm/điện máy sẽ được gợi ý nhãn nhúng *"Hỗ trợ Ví Trả Sau - Mua trước trả sau 0%"*, thúc đẩy tăng trưởng nợ vay lành mạnh cho mảng FS. Đồng thời, chủ shop xem trang Merchant Page của chính mình sẽ được hệ thống gợi ý trang bị Loa Soundbox để tự động hóa việc nhận tiền chuyển khoản.
3. **Cá nhân hóa trải nghiệm theo Ngành nghề:** Dựa trên bộ danh mục 14 ngành nghề chính & 53 ngành nghề phụ để đề xuất chương trình khuyến mãi và giao diện Merchant Page tối ưu cho từng loại hình kinh doanh (Ví dụ: Ngành F&B hiển thị Menu/Bảng giá; Ngành Làm đẹp hiển thị Bảng giá dịch vụ & Đặt lịch; Ngành Bách hoá hiển thị danh mục ưu đãi O2O).

### 2.3 Search Demand Analysis
Theo phân tích dữ liệu thực tế trên Open Web tại Việt Nam, tổng nhu cầu tìm kiếm địa điểm ăn uống, mua sắm, dịch vụ local và giải pháp kinh doanh vượt **15.8 triệu lượt/tháng**. Đây là hệ thống nhu cầu cốt lõi mà Merchant Hub tập trung hứng trọn qua mô hình Hub-and-Spoke:

| STT | Nhu Cầu / Use Case / Ngành Nghề | Volume Search / Tháng | Đặc Điểm Ý Định Tìm Kiếm (Search Intent) & Vai Trò Trong Merchant Hub |
| :---: | :--- | :---: | :--- |
| **1** | **Đồ Ăn (Nhà hàng, Quán ăn, Fastfood)** | **5.200.000** | Nhu cầu F&B lớn nhất thị trường. Hứng từ khóa tìm quán ăn gần đây, tiệm bánh, nhà hàng buffet. |
| **2** | **Đồ Uống (Cà phê, Trà sữa, Sinh tố)** | **3.800.000** | Traffic có tần suất lặp lại cao hàng ngày. Phễu kéo người dùng trẻ săn Voucher O2O 1-click. |
| **3** | **Bách Hoá & Siêu Thị (Tạp hoá, Tiện lợi)** | **2.500.000** | Tìm siêu thị tiện lợi, tạp hoá gần đây, chợ truyền thống. Phễu đẩy thanh toán QR quét mã nhanh. |
| **4** | **Làm Đẹp - Sức Khỏe (Spa, Hair, Nail, Gym)**| **1.600.000** | Nhu cầu dịch vụ chăm sóc cá nhân có ARPU cao. Phễu tư vấn ưu đãi Ví Trả Sau & Đặt lịch. |
| **5** | **Mua Sắm (Thời trang, Điện máy, Mẹ & bé)** | **1.200.000** | Nhu cầu mua sắm sản phẩm giá trị lớn. Phễu chuyển đổi chính cho dịch vụ Ví Trả Sau 0%. |
| **6** | **Dịch Vụ Xe & Nhà Cửa (Rửa xe, Giặt ủi)** | **850.000** | Tìm tiệm sửa xe, rửa xe, giặt ủi, dọn dẹp nhà cửa tại địa phương (Local GEO intent). |
| **7** | **Loa Báo Chuyển Tiền / Soundbox** | **150.000** | Nhu cầu của chủ shop tìm giải pháp loa thông báo chuyển tiền tự động. Phễu B2B Lead Gen trực tiếp. |
| **8** | **Điểm Chấp Nhận Thanh Toán MoMo** | **280.000** | Khách hàng chủ động tra cứu địa điểm dùng Ví MoMo, Ví Trả Sau và săn khuyến mãi MoMo Rewards. |

---

## III. Product Strategy & Core Flows

### 3.1 Multi-sided Value Proposition
* **Cho Chủ Cửa Hàng / Merchant (B2B):** Sở hữu một trang thông tin doanh nghiệp chuẩn SEO chuyên nghiệp hoàn toàn miễn phí trên `momo.vn/merchant`, tiếp cận hàng triệu khách hàng tiềm năng xung quanh, tăng lượt ghé shop offline nhờ voucher O2O, và tiếp cận giải pháp phần cứng Loa Soundbox chống thất thoát doanh thu.
* **Cho Khách Hàng Tiêu Dùng (Consumers):** Tra cứu địa điểm ăn uống, mua sắm uy tín gần nhất; xem trước menu, bảng giá, giờ mở cửa và đánh giá thực tế; săn voucher giảm giá O2O 1-click và linh hoạt chọn phương thức thanh toán (Ví MoMo, Ví Trả Sau).
* **Cho Nền Tảng MoMo (Acquisition & Monetization Engine):** Thu hút dòng traffic tự nhiên giá rẻ khổng lồ từ Open Web (Zero-ad cost), mở rộng tệp Merchant M4B active, tạo dòng doanh thu từ bán thiết bị Loa Soundbox và kích hoạt hạn mức Ví Trả Sau.

### 3.2 Web Onboarding Flow
```
[1. Tìm trên Google "Quán ăn X / Cửa hàng Y gần đây"] ──► [2. Xem Merchant Page trên Web momo.vn]
                                                                        │
                                                                        ▼
[4. Quét QR Thanh toán MoMo / Ví Trả Sau tại Shop] ◄─── [3. Thu thập Voucher O2O 1-Click trên Web]
```

### 3.3 Kick-off Alignment Rules & Web Compliance
1. **Quy tắc Bảo mật & Tuân thủ Thông tin trên Web (Web Compliance Rule):** Khi hiển thị trang Merchant Page công khai trên Web, **chỉ hiển thị các thông tin doanh nghiệp/cửa hàng công khai** (Họ tên thương hiệu, Địa chỉ Google Maps, Giờ mở cửa, Menu/Sản phẩm public, Ưu đãi voucher công khai). Tuyệt đối **không hiển thị doanh thu cửa hàng, thông tin cá nhân chủ shop (CCCD, Số điện thoại riêng, Tài khoản ngân hàng liên kết)** trừ khi chủ shop đã đăng nhập và xác thực chính chủ.
2. **Nguyên tắc Chuyển đổi Thanh toán (NHNN Compliance):** Mọi thao tác thu thập voucher có giá trị quy đổi tiền mặt và giao dịch thanh toán bắt buộc được xử lý chuyển tiếp qua App MoMo đã KYC chính chủ. Web Platform đóng vai trò hiển thị thông tin, tối ưu SEO và thu thập leads.
3. **Mô hình tiếp cận theo Ngành nghề (Category-first Approach):** Tối ưu SEO Hub theo 14 nhóm ngành nghề chính trước, sau đó phát triển 53 trang ngành nghề phụ để phủ trọn toàn bộ cụm từ khóa tìm kiếm địa điểm local.

### 3.4 Core Use Cases & KPIs Matrix

| # | Use Case (Hệ Sinh Thái Merchant) | Search Volume | Mô tả Chức Năng & Luồng Trải Nghiệm | KPIs Cam Kết |
|:---:|:---|:---:|:---|:---|
| 1 | **Merchant Page chuẩn SEO** | **~5.2M** | Trang thông tin chi tiết cửa hàng (Địa chỉ Maps, Hotline, Giờ mở cửa, Menu, Đánh giá). | Top 1-3 Organic Search; Time-on-page >1.5 phút. |
| 2 | **O2O Voucher Claim Engine** | **~3.8M** | Thu thập voucher giảm giá O2O trên Web với 1-click để sử dụng khi quét QR thanh toán tại shop. | Tỷ lệ Claim Voucher >15%; Tỷ lệ sử dụng tại shop >35%. |
| 3 | **Soundbox Lead Gen** | **~150K** | Chủ shop xem tính năng Loa báo chuyển tiền Soundbox và điền form đăng ký tư vấn giải pháp. | >8.500 Leads tư vấn/tháng; Tỷ lệ chốt đơn >20%. |
| 4 | **Local GEO Merchant Search** | **~2.5M** | Bản đồ tra cứu điểm bán chấp nhận MoMo theo bán kính GPS (500m, 1km, 3km) và theo Tỉnh thành/Quận huyện. | Hứng tệp tìm kiếm local; >300k lượt chỉ đường/tháng. |
| 5 | **Ví Trả Sau Merchant Locator** | **~280K** | Bộ lọc chuyên biệt danh sách cửa hàng/chuỗi siêu thị cho phép thanh toán qua Ví Trả Sau 0% lãi suất. | >10.000 giao dịch Ví Trả Sau được kích hoạt/tháng. |
| 6 | **Menu & Product Explorer** | **~1.2M** | Khách hàng xem thực đơn, hình ảnh món ăn, bảng giá dịch vụ trước khi quyết định đến cửa hàng. | Tỷ lệ xem Menu >45% tổng lượt truy cập trang Merchant. |
| 7 | **Review & Rating Platform** | **~850K** | Xem đánh giá từ cộng đồng người dùng MoMo đã thực hiện giao dịch thực tế tại merchant. | >50.000 lượt đánh giá mới được gửi mỗi tháng. |
| 8 | **Merchant Verification (Claim Store)** | **Internal** | Chủ cửa hàng xác minh quyền sở hữu trang Merchant Page để tự cập nhật Menu & phát hành Voucher. | >25% Merchant Active hoàn tất xác minh trang. |

---

## IV. Target Personas & JTBD

### 4.1 Target Personas
* **Persona 1: Chủ hộ kinh doanh cá thể & Chuỗi SME (Merchant B2B):** Sở hữu cửa hàng ăn uống, tạp hoá, tiệm làm đẹp hoặc chuỗi cửa hàng bán lẻ. Bận rộn, ít kiến thức kỹ thuật, muốn tăng lượng khách ghé shop nhưng không có ngân sách chạy quảng cáo đắt đỏ; cần giải pháp nhận tiền chuyển khoản minh bạch, không lo bị lừa đảo giả mạo biên lai.
* **Persona 2: Khách hàng tiêu dùng O2O (Consumer End-User):** Người dùng trẻ di chuyển thường xuyên, thích khám phá quán ăn, tiệm cà phê mới; có thói quen gõ Google tra cứu địa điểm trước khi đi; muốn săn voucher ưu đãi và thích thanh toán không dùng tiền mặt (MoMo, Ví Trả Sau).
* **Persona 3: Chủ chuỗi thương hiệu lớn / Doanh nghiệp đối tác (Enterprise Partner):** Các chuỗi F&B, chuỗi siêu thị tiện lợi (KFC, Highlands, Circle K, WinMart). Nhu cầu: phủ sóng thương hiệu số lượng lớn, đẩy các chiến dịch Marketing O2O quy mô toàn quốc.

### 4.2 Consumer Journey (4 Stages)
1. **Giai đoạn 1 (Trigger):** Phát sinh nhu cầu ăn uống, mua sắm hoặc tìm dịch vụ gần vị trí hiện tại ("tìm quán cà phê đẹp gần đây", "tiệm giặt ủi quận 1").
2. **Giai đoạn 2 (Search & Discovery):** Tìm kiếm trên Google / AI Search $\rightarrow$ Truyc cập trang Category Hub hoặc Merchant Page trên `momo.vn/merchant` không cần đăng nhập.
3. **Giai đoạn 3 (Utility & Identification):** Xem menu, địa chỉ Google Maps, đánh giá $\rightarrow$ Bấm 1-click "Thu thập Voucher O2O" $\rightarrow$ Khởi tạo liên kết định danh trên Web.
4. **Giai đoạn 4 (App Automation & Retention):** Chuyển đổi Web-to-App (W2A) mở App MoMo $\rightarrow$ Đến shop quét QR thanh toán sử dụng voucher $\rightarrow$ Tích điểm MoMo Rewards & Đánh giá cửa hàng.

### 4.3 Multi-sided JTBD Matrix

| Đối tượng | Job-To-Be-Done chính (Job Statement) | Pain Points cần giải quyết | Thay đổi sau khi dùng Merchant Hub |
| :--- | :--- | :--- | :--- |
| **Chủ cửa hàng (Merchants)** | *"Giúp cửa hàng của tôi xuất hiện chuyên nghiệp trên Google, thu hút thêm nhiều khách hàng quanh khu vực ghé shop và tự động hóa việc nhận tiền chuyển khoản để tôi yên tâm kinh doanh."* | - Không có website riêng, chi phí làm SEO quá đắt.<br>- Khó thu hút khách mới xung quanh.<br>- Lo bị lãng quên hoặc bị lừa chuyển khoản giả. | - Có trang Merchant Page chuẩn SEO miễn phí.<br>- Tiếp cận tệp khách MoMo qua Voucher O2O.<br>- Trang bị Loa Soundbox đọc tiền tự động. |
| **Khách hàng (Consumers)** | *"Giúp tôi nhanh chóng tìm được địa điểm ăn uống, mua sắm uy tín gần nhất với đầy đủ thông tin menu, bảng giá và voucher giảm giá để tiết kiệm thời gian và chi phí."* | - Thông tin cửa hàng trên mạng thiếu chính xác.<br>- Không biết cửa hàng có nhận thanh toán MoMo/Ví Trả Sau không.<br>- Bỏ lỡ các ưu đãi giảm giá tại shop. | - Tra cứu chuẩn xác menu/địa chỉ trên Web.<br>- Biết rõ điểm nhận MoMo & Ví Trả Sau.<br>- Săn Voucher O2O 1-click tiện lợi. |
| **Nền tảng (MoMo Platform)** | *"Giúp MoMo hứng trọn lượng traffic tìm kiếm địa điểm O2O khổng lồ từ Open Web, chuyển đổi người dùng Web thành giao dịch tại shop và bán chéo giải pháp Soundbox/Ví Trả Sau."* | - Chi phí thu hút người dùng mới (CAC) ngày càng cao.<br>- Merchant M4B thiếu công cụ kéo traffic O2O.<br>- Nguồn leads bán phần cứng Soundbox bị hạn chế. | - Hứng traffic tự nhiên từ SEO Hub (Zero-ad cost).<br>- Tăng sản lượng giao dịch QR O2O In-App.<br>- Tạo nguồn leads bán Loa Soundbox liên tục. |

---

## V. Site Structure & SEO/GEO Strategy

### 5.1 Hub-and-Spoke Sitemap Architecture

Tích hợp trọn vẹn bộ danh mục **14 Ngành nghề chính** và **53 Ngành nghề phụ** từ dữ liệu chuẩn ngành nghề MoMo:

#### A. Nhóm Trang Category Hubs & Spoke Pages (`/merchant/*`)

| Ngành nghề chính (Level 1) | URL Category Canonical | Danh sách Ngành nghề phụ (Level 2) & URL Mở Rộng | Mục Tiêu SEO & Intent |
| :--- | :--- | :--- | :--- |
| **1. Đồ ăn** | `/merchant/do-an` | Khu ẩm thực (`/do-an/khu-am-thuc`)<br>Nhà hàng (`/do-an/nha-hang`)<br>Quán ăn đường phố (`/do-an/quan-an-duong-pho`)<br>Quán ăn nhanh (`/do-an/quan-an-nhanh`)<br>Tiệm ăn (`/do-an/tiem-an`)<br>Tiệm bánh kẹo (`/do-an/tiem-banh-keo`) | Hứng **~5.2M volume/tháng**. SEO các từ khóa địa điểm ăn uống, nhà hàng, quán ăn gần đây. |
| **2. Đồ uống** | `/merchant/do-uong` | Cà phê (`/do-uong/ca-phe`)<br>Sinh tố (`/do-uong/sinh-to`)<br>Trà sữa (`/do-uong/tra-sua`) | Hứng **~3.8M volume/tháng**. SEO từ khóa tiệm cà phê, trà sữa, sinh tố gần bạn. |
| **3. Bách hoá** | `/merchant/bach-hoa` | Chợ truyền thống (`/bach-hoa/cho-truyen-thong`)<br>Cửa hàng thực phẩm (`/bach-hoa/cua-hang-thuc-pham`)<br>Cửa hàng tiện lợi (`/bach-hoa/cua-hang-tien-loi`)<br>Máy bán hàng tự động (`/bach-hoa/may-ban-hang-tu-dong`)<br>Siêu thị (`/bach-hoa/sieu-thi`)<br>Tạp hóa (`/bach-hoa/tap-hoa`)<br>Trung tâm thương mại (`/bach-hoa/trung-tam-thuong-mai`) | Hứng **~2.5M volume/tháng**. SEO từ khóa siêu thị mini, tiệm tạp hoá, cửa hàng tiện lợi 24/7. |
| **4. Làm đẹp - Sức khỏe** | `/merchant/lam-dep-suc-khoe` | Dịch vụ làm móng (`/lam-dep-suc-khoe/nail`)<br>Dịch vụ làm tóc (`/lam-dep-suc-khoe/lam-toc`)<br>Dịch vụ massage, spa (`/lam-dep-suc-khoe/massage-spa`)<br>Dịch vụ thẩm mỹ (`/lam-dep-suc-khoe/tham-my`)<br>Gym & Fitness (`/lam-dep-suc-khoe/gym-fitness`) | Hứng **~1.6M volume/tháng**. SEO các cụm từ khóa làm đẹp, spa, thẩm mỹ viện, phòng gym. |
| **5. Mua sắm** | `/merchant/mua-sam` | Cửa hàng mẹ và bé (`/mua-sam/me-va-be`)<br>Cửa hàng thể thao (`/mua-sam/the-thao`)<br>Điện thoại/Máy tính (`/mua-sam/dien-thoai-may-tinh`)<br>Đồ lót (`/mua-sam/do-lot`)<br>Gia dụng khác (`/mua-sam/gia-dung`)<br>Giày dép (`/mua-sam/giay-dep`)<br>Hạt giống/cây kiểng (`/mua-sam/cay-kieng`)<br>Nhà sách/Đồ chơi (`/mua-sam/nha-sach-do-choi`)<br>Nội thất (`/mua-sam/noi-that`)<br>Phụ kiện thời trang (`/mua-sam/phu-kien-thoi-trang`)<br>Quần áo (`/mua-sam/quan-ao`)<br>Siêu thị điện máy (`/mua-sam/sieu-thi-dien-may`)<br>Thiết bị điện (`/mua-sam/thiet-bi-dien`)<br>Thiết bị y tế (`/mua-sam/thiet-bi-y-te`)<br>Trang sức (`/mua-sam/trang-suc`)<br>Văn phòng phẩm (`/mua-sam/van-phong-pham`)<br>Vật liệu xây dựng (`/mua-sam/vat-lieu-xay-dung`) | Hứng **~1.2M volume/tháng**. Phễu chính tư vấn thanh toán Ví Trả Sau 0% lãi suất. |
| **6. Dịch vụ ô tô/xe máy** | `/merchant/dich-vu-o-to-xe-may` | Rửa xe (`/dich-vu-o-to-xe-may/rua-xe`)<br>Sửa chữa ô tô/xe máy (`/dich-vu-o-to-xe-may/sua-xe`) | Hứng **~550K volume/tháng**. Kết nối hệ sinh thái Vehicle Hub & M4B Garage. |
| **7. Đặt dịch vụ & Vận chuyển** | `/merchant/dat-dich-vu-van-chuyen` | Đại lý du lịch (`/dat-dich-vu-van-chuyen/dai-ly-du-lich`)<br>Taxi/Xe máy (`/dat-dich-vu-van-chuyen/taxi-xe-may`)<br>Vé máy bay (`/dat-dich-vu-van-chuyen/ve-may-bay`)<br>Vé tàu hỏa (`/dat-dich-vu-van-chuyen/ve-tau-hoa`) | SEO dịch vụ du lịch, đại lý vé và vận tải liên kết MoMo. |
| **8. Giải trí** | `/merchant/giai-tri` | Bar Club (`/giai-tri/bar-club`) | SEO dịch vụ giải trí về đêm, bar club chấp nhận MoMo. |
| **9. Giáo dục** | `/merchant/giao-duc` | Giáo dục khác (`/giao-duc/trung-tam-hoc-tap`) | SEO các trung tâm đào tạo, trường học đóng học phí MoMo. |
| **10. Hoạt động thể thao, vui chơi** | `/merchant/hoat-dong-the-thao` | Hoạt động thể thao (`/hoat-dong-the-thao/san-tap`)<br>Khu vui chơi giải trí (`/hoat-dong-the-thao/khu-vui-choi`) | SEO các địa điểm vui chơi giải trí gia đình, sân tập thể thao. |
| **11. Nhà cửa & Bảo trì** | `/merchant/nha-cua-bao-tri` | Dịch vụ dọn dẹp (`/nha-cua-bao-tri/don-dep`)<br>Giặt ủi (`/nha-cua-bao-tri/giat-ui`)<br>Sửa chữa thiết bị, nội thất (`/nha-cua-bao-tri/sua-chua-noi-that`) | Hứng **~300K volume/tháng**. SEO tiệm giặt ủi, sửa đồ gia dụng tại địa phương. |
| **12. Dịch vụ thú y** | `/merchant/dich-vu-thu-y` | Chăm sóc thú cưng (`/dich-vu-thu-y/pet-shop`) | SEO tiệm thú y, spa thú cưng, pet shop chấp nhận MoMo. |
| **13. Bán lẻ** | `/merchant/ban-le` | Mua sắm/Bán hàng khác (`/ban-le/khac`) | Trang tổng hợp ngành bán lẻ chung. |
| **14. Viễn thông** | `/merchant/vien-thong` | Mua thẻ cào điện thoại (`/vien-thong/the-cao`) | SEO điểm nạp tiền & đại lý viễn thông. |

#### B. Nhóm Trang Landing Pages Use Case Độc Lập

| Tên Trang / Use Case Page | URL Canonical | Cấu Trúc URL Mở Rộng | Mục Tiêu SEO & Intent |
| :--- | :--- | :--- | :--- |
| **Trang Chủ Merchant Hub** | `/merchant` | `/merchant` | Cổng tổng hợp tra cứu địa điểm & cửa hàng MoMo toàn quốc. |
| **Loa Soundbox MoMo** | `/merchant/soundbox` | `/merchant/soundbox/dang-ky` | Landing page giới thiệu Loa báo chuyển tiền Soundbox & Form tư vấn B2B. |
| **Ví Trả Sau Merchant Directory**| `/merchant/vi-tra-sau` | `/merchant/vi-tra-sau/{category-slug}` | Danh mục cửa hàng chấp nhận thanh toán Ví Trả Sau 0%. |
| **Kho Voucher O2O** | `/merchant/voucher-o2o` | `/merchant/voucher-o2o/{tinh-thanh}` | Tổng hợp mã giảm giá & voucher O2O claim 1-click trên Web. |
| **Merchant Detail Page** | `/merchant/{store-slug}` | `/merchant/{tinh-thanh}/{store-slug}` | Trang thông tin chi tiết từng cửa hàng chuẩn SEO JSON-LD. |

### 5.2 SEO & GEO Strategy & Schema Matrix
1. **Cấu trúc URL Địa lý Phân cấp (Local GEO pSEO):** Kết hợp Cấu trúc Ngành nghề + Tỉnh thành/Quận huyện để phủ trọn các cụm từ khóa tìm kiếm local:
   * `momo.vn/merchant/do-an/nha-hang/tp-ho-chi-minh`
   * `momo.vn/merchant/do-uong/ca-phe/ha-noi/cau-giay`
2. **Chuẩn hóa Dữ liệu Thực thể Schema.org Matrix (Structured Data):**

| Ngành nghề chính | Schema.org `@type` tương ứng | Đã khai báo thuộc tính JSON-LD |
| :--- | :--- | :--- |
| **Đồ ăn / Đồ uống** | `FoodEstablishment`, `Restaurant`, `CafeOrCoffeeShop`, `Bakery` | `name`, `image`, `address`, `geo` (latitude, longitude), `telephone`, `priceRange`, `openingHoursSpecification`, `menu`, `acceptsReservations` |
| **Làm đẹp - Sức khỏe** | `BeautySalon`, `HairSalon`, `HealthClub`, `DaySpa` | `name`, `address`, `geo`, `telephone`, `priceRange`, `openingHoursSpecification` |
| **Bách hoá / Mua sắm** | `Store`, `ConvenienceStore`, `DepartmentStore`, `GroceryStore` | `name`, `address`, `geo`, `telephone`, `priceRange`, `paymentAccepted` |
| **Dịch vụ ô tô/xe máy** | `AutomotiveBusiness`, `AutoRepair`, `AutoWash` | `name`, `address`, `geo`, `telephone`, `priceRange` |
| **Cửa hàng chung** | `LocalBusiness` | `name`, `address`, `geo`, `telephone`, `sameAs`, `hasMap` |

3. **Tối ưu hóa Tìm kiếm AI (Generative Engine Optimization - GEO):** Xây dựng mục FAQ chuẩn hóa câu trả lời tự nhiên (Ví dụ: *"Quán cà phê ABC có nhận thanh toán MoMo và Ví Trả Sau không?"*) giúp các công cụ AI Search (ChatGPT, Gemini, Perplexity) trích dẫn nguồn `momo.vn/merchant` khi trả lời người dùng.

---

## VI. Gamification & Promotions

* **Tích Điểm Merchant (MoMo Rewards Integration):** Người dùng quét QR thanh toán tại merchant được tích điểm đổi quà trên MoMo Rewards $\rightarrow$ Hiển thị tiến trình tích điểm trực tiếp trên Merchant Page để khuyến khích người dùng quay lại shop.
* **Gói Quà Tặng Mở Cửa Hàng (Merchant Onboarding Package):** Tài trợ 100.000đ Voucher O2O cho 1.000 chủ shop mới tạo và xác minh trang Merchant Page đầu tiên.
* **Vòng Quay May Mắn Soundbox (Soundbox Lucky Spin):** Chủ cửa hàng đăng ký tư vấn Loa Soundbox trên Web có cơ hội trúng 100% voucher miễn phí phí thuê loa 3 tháng.

---

## VII. Compliance & Risk Governance

### 7.1 Security & PDPD Compliance
* **Nghị định 13/2023/NĐ-CP (PDPD):** Tuân thủ nghiêm ngặt quy định bảo vệ dữ liệu cá nhân. Trên Web public, tuyệt đối không công khai số điện thoại cá nhân của chủ shop, tài khoản ngân hàng cá nhân hay doanh thu cửa hàng. Thông tin chủ shop chỉ được chỉnh sửa trong cổng quản trị App M4B đã xác thực.
* **Quy định Ngân hàng Nhà nước (NHNN):** Mọi voucher quy đổi giá trị tiền mặt và giao dịch quét QR thanh toán bắt buộc được thực hiện trên ứng dụng MoMo đã hoàn tất xác thực KYC. Web Platform đóng vai trò hiển thị thông tin và thu thập leads.

### 7.2 Risk Management Matrix

| Rủi ro tiềm tàng | Mức độ | Phương án xử lý | Đơn vị chịu trách nhiệm |
|---|:---:|---|---|
| **Thông tin cửa hàng bị sai lệch** (Địa chỉ, Giờ mở cửa) do chủ shop thay đổi không báo. | Trung bình | Tích hợp nút *"Báo sai thông tin"* trên Web; cho phép cộng đồng người dùng đóng góp chỉnh sửa & tự động nhắc chủ shop qua App M4B. | Operations Team & M4B |
| **Spam / Leads ảo đăng ký tư vấn Soundbox** từ form công khai trên Web. | Cao | Tích hợp reCAPTCHA v3, OTP xác thực số điện thoại chủ shop trước khi gửi Lead về CRM. | Technical Team & Sales M4B |
| **Merchant lạm dụng phát hành Voucher O2O** để trục lợi gian lận. | Cao | Thiết lập hạn mức phát hành voucher tối đa/ngày; kiểm soát tự động qua hệ thống Fraud Detection của MoMo. | Risk Management & Financial Services |
| **Quá tải truy cập trang Merchant** trong các chiến dịch khuyến mãi lớn. | Thấp | Tối ưu Caching CDN (Cloudflare/Akamai), Server-side Rendering (SSR) nhẹ giúp tốc độ tải trang di động <1.5s. | Web Platform Team |

---

## VIII. Growth Roadmap & Changelog

### 8.1 5-Phase Growth Roadmap
* **Phase 1: Merchant Acquisition & Web Hub Launch (T9 - T12/2026):** Mở rộng `momo.vn/merchant` theo 14 nhóm ngành nghề chính & 53 ngành nghề phụ; kích hoạt luồng Web-to-App Claim Voucher O2O; chuẩn hóa 500.000 Merchant Pages.
* **Phase 2: Soundbox & FS Monetization Engine (Q1/2027):** Đẩy mạnh Landing Page Loa Soundbox; hiển thị nhãn Ví Trả Sau badge trên Merchant Pages; triển khai luồng Merchant Verification (Claim Store).
* **Phase 3: Merchant Commerce & Engagement Engine (Q2/2027):** Ra mắt tính năng Đánh giá & Review từ người dùng MoMo; tích hợp Booking/Menu order trước; mở Cổng phát hành Voucher O2O cho chủ shop trên App M4B.
* **Phase 4: AI Merchant Assistant & Hyper-Local GEO (Q3/2027):** Trợ lý AI gợi ý chương trình khuyến mãi cho chủ shop dựa trên dữ liệu ngành nghề; cá nhân hóa vị trí hiển thị cửa hàng theo hành vi người dùng.
* **Phase 5: Merchant Financial Ecosystem (Q4/2027):** Mở rộng hệ sinh thái tài chính cho Merchant: Gói vay hộ kinh doanh, Bảo hiểm cửa hàng, B2B Procurement Marketplace mua hàng giá sỉ.

### 8.2 Change Log

| Phiên bản | Ngày cập nhật | Người thực hiện | Nội dung thay đổi |
|---|---|---|---|
| **v2.0** | 2026-07-31 | Web Product Lead (GPD) | **Master BRD Upgrade:** Đại tu toàn bộ Merchant Hub BRD theo chuẩn cấu trúc `vehicle-hub-brd.md`. Bổ sung SCR Framework, PLG 5 Phễu Mồi Câu, Dual North Star Metrics, Bảng Phân Tích Nhu Cầu Tìm Kiếm (Search Demand Analysis), Tích hợp Bộ Taxonomy 14 Ngành nghề chính & 53 Ngành nghề phụ từ CSV, Schema.org Matrix, PDPD Compliance và Risk Management Matrix. |
| **v1.0** | 2026-07-15 | Web Platform Team | Khởi tạo tài liệu BRD ban đầu cho dự án Merchant Hub (MoMo Merchant Page cho SME). |
