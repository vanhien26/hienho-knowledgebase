# BRD: Vehicle Hub - Cổng Tiện Ích & Hồ Sơ Phương Tiện MoMo

> - **Project:** Vehicle Hub (Web Platform & Vehicle Profile Identity)
> - **Platform:** Web Platform (`momo.vn/tien-ich-giao-thong`, `momo.vn/phat-nguoi`)
> - **Division:** Growth Platform Division (GPD)
> - **Owner:** Web Platform Team (GPD)

## I. Executive Summary


### 1.1 Core Problems & Objectives
* **Vấn đề thực tế (Problem Statement):** Hàng triệu chủ xe ô tô và xe máy tại Việt Nam đang bị phân mảnh thông tin, phải chuyển qua lại giữa 5-7 ứng dụng và website độc lập chỉ để xử lý các nhu cầu thiết yếu: tra/nộp phạt nguội, nạp tiền ETC, theo dõi hạn đăng kiểm, mua bảo hiểm và tìm cây xăng/bãi đỗ.
* **Mục tiêu định lượng:** Hợp nhất toàn bộ nhu cầu phân mảnh này và **rút ngắn tổng thời gian quản lý một chiếc xe xuống dưới 3 phút** trên một nền tảng duy nhất (MoMo).
* **Triết lý cốt lõi:** **"Một chiếc xe - Một tài khoản dịch vụ"**, biến biển số xe của người dùng thành trung tâm kết nối tự động:
  1. **Một lần khai báo, đồng bộ trọn đời:** Nhập biển số xe 1 lần duy nhất, hệ thống tự động kết nối và theo dõi trạng thái pháp lý, bảo hiểm và tài khoản BOT của xe.
  2. **Chủ động cảnh báo, tự động xử lý:** Tự động cảnh báo khi phát sinh phạt nguội mới, nhắc lịch đăng kiểm trước 30/15/7 ngày, và tự nạp tiền ePass/VETC khi số dư dưới hạn mức.
  3. **Một cổng thanh toán cho mọi hành trình:** Kết nối tài khoản xe với mọi dịch vụ O2O dọc đường đi (tự động thanh toán đỗ xe, đổ xăng không tiền mặt Petrolimex/PVOil, gọi cứu hộ 24/7 trên hệ thống).

### 1.2 Situation - Complication - Resolution
* **Situation (Bối cảnh & Vai trò Website):** Khi phát sinh nhu cầu tức thời (lo bị phạt nguội sau khi đi tỉnh, giá xăng tăng, xe sắp hết hạn đăng kiểm), phản xạ tự nhiên của chủ xe là mở Google hoặc các công cụ AI Search tra cứu nhanh trên trình duyệt Web. Website `momo.vn` đóng vai trò là **"cửa ngõ hứng nhu cầu và cổng định danh"**. Bằng các tiện ích tra cứu trực tuyến (tra phạt nguội không CAPTCHA, bảng giá xăng thời gian thực), Website giải quyết nhu cầu của người dùng, từ đó thu thập biển số xe để thiết lập hồ sơ phương tiện ban đầu (Vehicle Profile).
* **Complication (Khó khăn & Thách thức):** Nếu các dịch vụ giao thông chỉ nằm sâu trong ứng dụng di động đóng (App-only ecosystem), MoMo sẽ hoàn toàn vô hình trước hàng triệu lượt tìm kiếm tự nhiên ngoài Open Web. Hậu quả là lượng Traffic có ý định giao dịch cao (High purchase intent) sẽ chảy sang các trang web bên thứ ba, đồng thời việc ép người dùng tải App ngay lần đầu tiếp cận sẽ tạo ra rào cản lớn đối với người dùng.
* **Resolution (Giải pháp):** Xây dựng **Vehicle Hub** hoạt động theo mô hình Product-Led Growth (PLG) & Hub-and-Spoke: Hứng traffic tự nhiên từ Open Web qua các Utility Spoke Pages $\rightarrow$ Khởi tạo Hồ sơ xe (Vehicle Profile) $\rightarrow$ Điều hướng Web-to-App (W2A) để tự động hóa quản lý phương tiện.

### 1.3 Product-Led Growth (PLG)
Cơ chế PLG của Vehicle Hub dựa trên 5 "Phễu Mồi Câu" (Acquisition & Engagement Hooks) giải quyết tức thời nhu cầu tìm kiếm trên Open Web để dẫn dắt người dùng tự nguyện định danh phương tiện và chuyển đổi sang App (Web-to-Vehicle-to-App Flywheel):

1. **Phễu Tra Cứu Phạt Nguội (Acquisition Gate):** Tra cứu thông tin vi phạm giao thông không cần nhập CAPTCHA → Bấm "Lưu biển số xe" → Tự động khởi tạo Hồ sơ phương tiện (Vehicle Profile) & Dẫn dắt đăng ký Gói Cảnh báo Tự động (9k/năm) để tự động quét & phát thông báo vi phạm mới qua MoMo.
2. **Phễu Giá Xăng Dầu (Retention Magnet):** Tra cứu bảng giá xăng A95, E5, Diesel Vùng 1 & Vùng 2 realtime → Đăng ký nhận thông báo điều chỉnh giá chiều thứ 5 hàng tuần → Định vị cây xăng Petrolimex/PVOil gần nhất, cung cấp thông tin địa điểm, hướng dẫn chỉ đường & phương thức thanh toán không tiền mặt qua Ví MoMo.
3. **Phễu Trạm Sạc Xe Điện EV (High-ARPU Hook):** Định vị trạm sạc xe điện khả dụng theo vị trí (VinFast, V-Green & các đối tác) → Cung cấp thông tin địa điểm, hướng dẫn chỉ đường & Dẫn dắt mua Bảo hiểm xe điện / Tra cứu phạt nguội.
4. **Phễu Thu Phí Không Dừng ePass / VETC (Route & Travel Hook):** Tra cứu số dư tài khoản & Tính phí trạm thu phí theo lộ trình di chuyển → Khởi tạo liên kết tài khoản ePass → Kích hoạt tính năng Tự động nạp tiền (Auto-Topup) khi số dư dưới hạn mức.
5. **Phễu Cảnh Báo Hạn Đăng Kiểm (Lifecycle Reminder Hook):** Tra cứu thông tin kiểm định & Trạng thái ngăn chặn đăng kiểm → Đăng ký nhận nhắc lịch đăng kiểm tự động trước 30/15/7 ngày → Đặt lịch hẹn trung tâm đăng kiểm đối tác.

### 1.4 Key Metrics & Targets

#### Dual North Star Metrics

| Platform Layer | North Star Metric | Definition | Target | Strategic Role |
| :--- | :--- | :--- | :--- | :--- |
| **Web Platform** *(Primary Goal)* | **Total Organic Web Traffic** | Tổng số lượt truy cập tự nhiên từ Google Search và AI Search vào các tiện ích Vehicle Hub trên Kênh Web mỗi tháng. | **1.8M - 2.5M Visits/tháng** | Mục tiêu cốt lõi: Hứng tối đa nhu cầu tìm kiếm của chủ xe ngoài Open Web (trên tổng quy mô tìm kiếm ~18M+ volume/tháng). |
| **In-App Mini App** *(Secondary Layer)* | **Active Vehicle Users & Retention** | Tỷ lệ chủ xe quay lại phát sinh hành động In-App trong 90 ngày (90-day Active Rate) & Tổng xe hoạt động. | **Active Rate $\ge 20\%$**<br>*(Target Phase 2: $\ge 200.000$ Active Vehicles)* | Đo lường mức độ tự động hóa và tỷ lệ giữ chân chủ xe trong ứng dụng MoMo sau khi được điều hướng từ Web. |

#### Web Platform Metric Tree

1. **Organic Traffic & Search Reach**
   * **Tra Cứu Phạt Nguội:** Top 1 Organic Search Google, đạt **>2.500.000 lượt tra cứu/tháng**.
   * **Giá Xăng Dầu & Cây Xăng:** Hứng **>8.500.000 volume/tháng** giá xăng và địa điểm cây xăng Petrolimex/PVOil.
   * **Trạm Sạc Xe Điện EV:** Hứng **>1.200.000 volume/tháng** nhu cầu tìm trạm sạc VinFast & V-Green.
   * **Bãi Đỗ Xe & Cứu Hộ:** Hứng **>300.000 volume/tháng** tìm bãi đỗ xe ô tô và cứu hộ khẩn cấp 24/7.

2. **Web Engagement & Identification**
   * **Tỷ Lệ Nhập Biển Số Xe:** Đạt **8% - 12%** lượt truy cập tra cứu thực hiện nhập Biển số xe để khởi tạo Hồ sơ xe Level 1 trên Web.
   * **Tỷ Lệ Điều Hướng Web-to-App:** Đạt **>25%** lượt truy cập điều hướng mở App MoMo để nhận cảnh báo phạt nguội tự động hoặc cài Auto-Topup ePass.

3. **Commercial Conversion**
   * **Bảo Hiểm Ô Tô qua Web:** Đạt **335 đơn VCX + 707 đơn TNDS (Tổng 1.042 đơn H2/2026)** xuất bản qua Web với tỷ lệ tự động điền dữ liệu Auto-fill **>= 40%**.
   * **Bảo Hiểm Xe Máy qua Web:** Đạt thứ hạng **Top 1 - Top 10 Google Search** các cụm từ khóa chính (`mua bảo hiểm xe online`...).
   * **Service Attach Rate:** Đạt **1.2 service/xe**.

#### Mini App Vehicle Hub KPI Proposal (Target Đến 31/12/2026)

| KPI | Mô tả | Target đề xuất (tính đến 31/12/2026) |
| :--- | :--- | :---: |
| **Saved Vehicle User (Level 1)** | Có biển số xe | **100.000 xe** (bao gồm ô tô và xe máy) |
| **Saved Vehicle User (Level 2)** | Có biển số, OCR cà vẹt xe | **140.000 xe** (bao gồm ô tô và xe máy) |
| **Saved Vehicle User (Level 3) - ô tô** | Có đầy đủ data xe (OCR cà vẹt, đăng kiểm) | **20.000 xe** (bao gồm ô tô và xe máy) |
| **Vehicle Hub 90-day Active Rate** | % user có xe quay lại/có hành động trong 90 ngày | **20%** |
| **Service attach rate/vehicle** | Trung bình số service active trên mỗi xe | **1,2 service/xe** |
| **Trigger-to-action rate** | Nhắc hạn/phạt/ETC $\rightarrow$ user xử lý | **15%** |
| **Data reuse rate** | % flow được auto-fill từ Vehicle Profile | **$\ge 40\%$ eligible sessions** |

#### Phase 1 Pilot Targets (Cell Team Alignment T9 - T12/2026)

| STT | Chỉ Số (Key Metric) | Baseline (H1/2026) | Target Phase 1 Pilot (T9 - T12/2026) | Ghi Chú Thực Thi |
| :---: | :--- | :---: | :---: | :--- |
| 1 | **Phase 1 Organic Traffic** | 1.8M/tháng | **315.000 Visits** | Search Capture Rate 0.5% trên 5 Use Cases ưu tiên Phase 1 |
| 2 | **Qualified Conversion Rate (W2A CVR)** | 12% | **>= 0.5% CVR** | Tỷ lệ từ Web Visit sang Thêm xe thành công trong App hoặc Giao dịch |
| 3 | **New Vehicle Profiles Created (WVP)** | 150K xe | **1.575 Profiles** | Tạo mới Hồ sơ phương tiện thành công trong App từ Kênh Web |
| 4 | **Transactions (Bảo Hiểm Ô Tô)** | 3.500 đơn | **335 đơn VCX + 707 đơn TNDS** | Xuất bản hợp đồng bảo hiểm Thân vỏ (VCX) & TNDS qua Web |
| 5 | **SEO Ranking (Bảo Hiểm Xe Máy)** | - | **Top 1 - Top 10 Keywords** | Đưa các cụm từ khóa cốt lõi (`mua bảo hiểm xe online`...) lọt Top 1-10 Google |
| 6 | **Auto-fill Completion Rate** | 45% | **>60% CR** | Tự động điền dữ liệu xe từ Vehicle Profile khi mua Bảo hiểm/Nạp ePass |





## II. Market Context & Strategy

### 2.1 Market Sizing & Opportunity
* **Quy mô thị trường phương tiện tại Việt Nam:**
  * **Ô tô:** Hơn 5,5 triệu ô tô lưu hành toàn quốc.
  * **Xe máy:** Hơn 72 triệu xe máy đăng ký.
* **Cơ hội O2O từ M4B:** Việc MoMo tích hợp thanh toán tại mạng lưới Petrolimex/PVOil mở ra vòng lặp O2O hoàn chỉnh: Quét mã đổ xăng $\rightarrow$ Lưu Profile xe $\rightarrow$ Nhắc nhở dịch vụ bảo dưỡng/bảo hiểm.

### 2.2 Cross-BU Synergy & Data Consolidation
MoMo sở hữu lợi thế tuyệt đối và nguồn dữ liệu tập trung khi kết hợp sức mạnh giữa **Web Platform**, **FS / Bảo hiểm** và **VTTI**:
1. **Quy mô kho dữ liệu phương tiện:** MoMo đang sở hữu tài sản dữ liệu khổng lồ với gần **2.000.000 xe máy** và khoảng **600.000 xe ô tô** (trong đó **150.000+ xe ô tô** đã được định danh chi tiết bằng OCR Cà vẹt xe).
2. **Tỷ lệ trùng lặp khách hàng (Customer Overlap):** Chỉ số overlap giữa tệp FS và VTTI hiện tại cực kỳ thấp (chỉ từ **0.3% đến 3%**, cao nhất là giữa bảo hiểm và tra cứu phạt nguội). Điều này chứng minh tiềm năng bán chéo (Cross-sell/Upsell) khổng lồ khi dữ liệu được hợp nhất vào Hồ sơ xe.
3. **Chiến lược cá nhân hóa tự động (Auto-Journey):** Nhận diện chính xác dòng xe từ biển số đã định danh để gửi thông điệp cá nhân hóa chính xác (Ví dụ: *"Phí bảo hiểm thân vỏ cho xe Honda CRV của bạn chỉ từ 6 triệu đồng"*).

### 2.3 Search Demand Analysis
Theo phân tích dữ liệu thực tế trên Open Web, tổng nhu cầu tìm kiếm tự nhiên của chủ xe ô tô và xe máy vượt **12.6 triệu lượt/tháng**. Đây là hệ thống 11 nhu cầu cốt lõi xung quanh chiếc xe mà MoMo tập trung hứng trọn qua mô hình Hub-and-Spoke:

| STT | Nhu Cầu / Use Case | Volume Search / Tháng | Đặc Điểm Ý Định Tìm Kiếm (Search Intent) & Vai Trò Trong Vehicle Hub |
| :---: | :--- | :---: | :--- |
| **1** | **Giá Xăng Dầu** | **10.1M** | Nhu cầu lớn nhất thị trường. Mồi câu kéo Traffic lặp lại định kỳ chiều thứ 5 hàng tuần. |
| **2** | **Trạm Sạc Xe Điện (EV)** | **1.24M** | Nhu cầu bùng nổ của tệp chủ xe điện (VinFast, V-Green), tệp khách hàng thu nhập & ARPU cao. |
| **3** | **Cây Xăng (Bản Đồ Local)** | **550K** | Định vị địa điểm (Local GEO), chuyển đổi O2O sang thanh toán quét mã Petrolimex/PVOil. |
| **4** | **Garage Sửa Xe & Garage Gần Đây** | **272K** *(201K + 71K)* | Nhu cầu bảo dưỡng, sửa chữa định kỳ & khẩn cấp tại local. Phễu liên kết mạng lưới garage M4B. |
| **5** | **Đăng Kiểm Xe** | **182K** | Nhu cầu tra cứu hạn kiểm định & trạm đăng kiểm. Phễu kích hoạt dịch vụ Đặt lịch/Đăng kiểm hộ. |
| **6** | **Phí Không Dừng (VETC/ePass)** | **95K** | Nhu cầu kiểm tra số dư & tính phí tuyến đường. Phễu kích hoạt Auto-Topup tự động nạp ePass. |
| **7** | **Bãi Đỗ & Giữ Xe** | **53K** | Local GEO tìm chỗ đỗ xe nội đô. Phễu kết nối thanh toán tự động VETC Parking / eParking. |
| **8** | **Thuế Trước Bạ** | **44K** | Nhu cầu tính chi phí lăn bánh & nộp thuế hành chính cho xe mới/chuyển nhượng. |
| **9** | **Cứu Hộ Ô Tô** | **41K** | Nhu cầu sự cố khẩn cấp trên đường (Event-driven). Kết nối dịch vụ cứu hộ 24/7 (Zuttoride). |
| **10**| **Định Giá Xe** | **11K** | Nhu cầu đánh giá giá trị xe cũ. Phễu tư vấn tài chính, hạn mức vay & sàn giao dịch xe. |
| **11**| **Tra Cứu Phạt Nguội** *(Kênh Cốt Lõi)* | **~6.1M** | Cửa ngõ định danh phương tiện 0-CAPTCHA, chuyển đổi 90% xe sạch sang Vehicle Profile. |

## III. Product Strategy & Core Flows



### 3.1 Multi-sided Value Proposition
* **Cho Chủ Xe Phương Tiện (Consumers):** Trải nghiệm tập trung hoàn thành mọi trách nhiệm với chiếc xe: tra/nộp phạt nguội tự động, nạp ePass chống ùn tắc, nhắc hạn đăng kiểm, mua bảo hiểm tự động điền (Auto-fill).
* **Cho Hệ Sinh Thái Dịch Vụ (Merchants & Partners):** Tiếp cận tệp chủ xe chất lượng cao (ARPU cao) được định danh rõ ràng theo chủng loại phương tiện. Mở rộng hiện diện số hóa Local GEO cho cây xăng (Petrolimex, PVOil), trạm thu phí (ePass), bãi đỗ xe (VETC Parking, eParking), trạm sạc điện (VinFast), công ty bảo hiểm (PVI, Bảo Việt, MIC), garage sửa chữa và đối tác cứu hộ (Zuttoride).
* **Cho MoMo (Acquisition & Monetization Engine):** Chuyển đổi Traffic vô danh trên Web thành tệp Hồ sơ xe định danh (Vehicle Profile), tạo dòng doanh thu liên tục từ bán chéo bảo hiểm, nạp ETC, phí giao dịch thanh toán.

### 3.2 Web Onboarding Flow
```
[1. Nhập Biển Số Xe trên Web momo.vn] → [2. Tra cứu Phạt Nguội (Không nhập CAPTCHA)]
                                                         │
                                                         ▼
[4. Auto-fill mua BH Ô tô/Xe máy & Nạp ETC] ◄── [3. Bấm "Lưu Hồ Sơ Xe & Nhắc Lịch Đăng Kiểm"]
```

### 3.3 Kick-off Alignment Rules & Web Compliance
1. **Khắc phục lãng phí Traffic Phạt Nguội (Quick-Win):** Đội FS & VTTI chèn trực tiếp các khối quảng cáo (Ads Blocks), chương trình ưu đãi bảo hiểm và thẻ quà tặng (Gift Cards) tại trang kết quả tra cứu Phạt Nguội để chuyển đổi ngay traffic.
2. **Nguyên tắc Bảo mật & Tuân thủ Pháp lý trên Web (Web Compliance Rule):** Khi hiển thị cá nhân hóa trên Web công cộng, **tuyệt đối không hiển thị thông tin bảo hiểm tư nhân, dữ liệu cá nhân (CCCD, Họ tên, Địa chỉ) hoặc định giá tài sản của User B khi User A nhập biển số xe của User B trên Web public**. Thông tin riêng tư chỉ hiển thị sau khi người dùng xác thực chính chủ trên App MoMo.
3. **Mô hình tiếp cận từng Use-case (Service-first Approach):** Tối ưu SEO cho từng Use-case cụ thể có search volume lớn trước (`/phat-nguoi`, `/gia-xang`, `/epass`), sau đó kết nối các Spoke này thành Web Hub hoàn chỉnh.

### 3.4 Core Use Cases & KPIs Matrix

| # | Use Case (Hệ Sinh Thái Chiếc Xe) | Search Volume | Mô tả Chức Năng & Luồng Trải Nghiệm | KPIs Cam Kết |
|:---:|:---|:---:|:---|:---|
| 1 | **Phạt Nguội** | **~6.1M** | Tra cứu thông tin vi phạm giao thông theo biển số xe không cần nhập CAPTCHA. | Top 1 Organic Search; >2.5M lượt tra cứu/tháng. |
| 2 | **Giá Xăng Dầu** | **10.1M** | Cập nhật bảng giá xăng A95, E5, Dầu Diesel Vùng 1 & Vùng 2 realtime theo kỳ điều hành. | Organic Clicks nhóm từ khóa Giá xăng dầu (~10.1M volume). |
| 3 | **Trạm Sạc Xe Điện** | **1.24M** | Bản đồ định vị & chỉ đường trạm sạc VinFast, V-Green khả dụng theo tọa độ GPS. | Hứng tệp chủ xe điện EV; >100k lượt tương tác chỉ đường/tháng. |
| 4 | **Cây Xăng (Bản Đồ)** | **550K** | Tìm kiếm trạm xăng Petrolimex/PVOil chấp nhận thanh toán MoMo/Ví Trả Sau gần nhất. | Chuyển đổi O2O quét mã thanh toán tại cột bơm. |
| 5 | **Garage Sửa Xe** | **272K** | Danh mục & bản đồ Local GEO garage sửa xe, trung tâm chăm sóc ô tô uy tín gần bạn. | >50k lượt xem cửa hàng & đặt lịch bảo dưỡng/tháng. |
| 6 | **Đăng Kiểm Xe** | **182K** | Tra cứu thời hạn kiểm định, cảnh báo từ Cục Đăng Kiểm & Đặt lịch hẹn trạm đăng kiểm. | 100% Hồ sơ xe được nhắc lịch trước 30/15/7 ngày. |
| 7 | **Phí Không Dừng (VETC/ePass)** | **95K** | Tra cứu số dư, tính phí BOT theo lộ trình & Cài đặt tự động nạp tiền Auto-Topup. | Tỷ lệ kích hoạt Auto-Topup ePass đạt >25% tệp người dùng. |
| 8 | **Bãi Đỗ & Giữ Xe** | **53K** | Bản đồ bãi đỗ xe ô tô nội đô phân cấp Tỉnh/Quận & Tự động trừ phí qua VETC Parking. | Chuyển đổi O2O đỗ xe tự động không tiền mặt. |
| 9 | **Thuế Trước Bạ** | **44K** | Công cụ dự toán phí trước bạ, chi phí lăn bánh ô tô/xe máy mới & Hướng dẫn nộp DVC. | Hứng tệp mua xe mới, phễu tư vấn Bảo hiểm Thân vỏ. |
| 10 | **Cứu Hộ Ô Tô** | **41K** | Dịch vụ gọi cứu hộ cẩu kéo sự cố 24/7 khẩn cấp theo vị trí GPS (Zuttoride). | Thời gian phản hồi cứu hộ <3 phút; Giải quyết sự cố 24/7. |
| 11 | **Định Giá Xe** | **11K** | Công cụ tra cứu khoảng giá thị trường xe cũ theo hãng xe, dòng xe và năm sản xuất. | Phễu tư vấn tài chính mua xe & Đăng ký gói vay. |
| 12 | **Bảo Hiểm Ô Tô & Xe Máy** | **Commercial** | So sánh báo giá & Mua bảo hiểm TNDS, Thân vỏ online, tự động cấp ấn chỉ điện tử. | 15.000 đơn BH Ô tô & 80.000 đơn BH Xe máy/năm. |
| 13 | **Hồ Sơ Phương Tiện (Vehicle Profile)** | **Master Core** | Quản lý thông tin xe 3 cấp độ (Basic, Vehicle, Verified), đồng bộ dữ liệu trọn đời. | >500.000 Hồ sơ xe lưu thành công trên hệ thống. |


### 3.5 DVC Fine Payment Integration Flows
1. **Luồng 1: Thanh toán qua Cổng DVCQG (Web DVCQG Handoff Flow - 6 Bước):**
   - *Bước 1:* Truy cập Cổng DVCQG (`dichvucong.gov.vn`).
   - *Bước 2:* Nhập Mã hồ sơ + Mã CAPTCHA.
   - *Bước 3:* Kiểm tra thông tin quyết định xử phạt.
   - *Bước 4:* Khai báo thông tin người nộp (Họ tên, CCCD, Địa chỉ).
   - *Bước 5:* Chọn phương thức thanh toán Ví MoMo.
   - *Bước 6:* Hoàn tất thanh toán và nhận Biên lai điện tử lưu tự động vào App MoMo.
2. **Luồng 2: Thanh toán NATIVE trực tiếp trên App MoMo (Native In-App Flow - 5 Bước W2A):**
   - *Bước 1 (Entrypoint):* Mở App MoMo $\rightarrow$ Chọn *Nộp phạt giao thông* (hoặc ấn OneLink từ Web `momo.vn/phat-nguoi`).
   - *Bước 2 (Input):* Nhập Số Quyết Định xử phạt + CAPTCHA.
   - *Bước 3 (Tra cứu):* Hệ thống hiển thị chi tiết quyết định xử phạt và số tiền phạt.
   - *Bước 4 (Thanh toán):* Xác nhận thanh toán bằng Ví MoMo hoặc Ví Trả Sau (Hỗ trợ nộp phạt trả góp 0%).
   - *Bước 5 (Biên lai):* Nhận Biên lai điện tử In-App MoMo, tự động gạch nợ & lưu vào Vehicle Profile.



## IV. Target Personas & JTBD


### 4.1 Target Personas
* **Persona 1: Chủ xe ô tô cá nhân di chuyển thường xuyên:** Di chuyển liên tỉnh thường xuyên, lịch trình bận rộn, ít theo dõi hạn đăng kiểm/bảo hiểm. Nhu cầu: tra phạt nguội trước khi đăng kiểm, tự nạp tiền ePass khi dưới hạn mức.
* **Persona 2: Người lái xe di chuyển nội đô:** Di chuyển hàng ngày trong thành phố, thường xuyên đổ xăng Petrolimex/PVOil. Nhu cầu: thanh toán xăng không tiền mặt, tìm garage bảo dưỡng và cứu hộ khẩn cấp gần nhất.
* **Persona 3: Chủ xe máy:** Mua bảo hiểm xe máy điện tử bắt buộc, tra cứu phạt nguội xe máy.

### 4.2 Consumer Journey (4 Stages)
1. **Giai đoạn 1 (Trigger):** Phát sinh nhu cầu khẩn cấp (lo bị phạt nguội sau chuyến đi tỉnh, hết tiền ETC, bảo hiểm sắp hết hạn).
2. **Giai đoạn 2 (Search & Discovery):** Tìm kiếm trên Google / AI Search ("tra phat nguoi oto", "gia xang hom nay") $\rightarrow$ Truy cập Utility Spoke Pages trên `momo.vn` không cần đăng nhập.
3. **Giai đoạn 3 (Utility & Identification):** Nhập biển số xe tra cứu phạt nguội không cần nhập CAPTCHA $\rightarrow$ Khởi tạo Vehicle Profile Level 1 (Basic Profile).
4. **Giai đoạn 4 (App Automation & Retention):** Chuyển đổi Web-to-App (W2A) để nộp phạt / mua bảo hiểm / cài Auto-Topup ePass $\rightarrow$ Nâng cấp Profile Level 2/3, chuyển từ thao tác thủ công sang tự động hóa quy trình quản lý.

### 4.3 Multi-sided JTBD Matrix

| Đối tượng | Job-To-Be-Done chính (Job Statement) | Pain Points cần giải quyết | Thay đổi sau khi dùng Vehicle Hub |
| :--- | :--- | :--- | :--- |
| **Chủ xe (Consumers)** | *"Giúp tôi quản lý và thực hiện đầy đủ các trách nhiệm pháp lý, chi phí của chiếc xe một cách tự động, nhanh chóng để tôi yên tâm di chuyển mà không mất thời gian suy nghĩ."* | - Quên hạn đăng kiểm, hạn bảo hiểm TNDS dẫn đến bị phạt.<br>- Kẹt trạm thu phí ETC vì hết tiền trong tài khoản ePass.<br>- Tra phạt nguội thủ công, nhập CAPTCHA phiền toái. | - Nhắc lịch tự động trước 30/15/7 ngày.<br>- Cài đặt Auto-Topup tự nạp tiền ETC.<br>- Quét phạt nguội tự động thứ Hai hàng tuần, báo vi phạm lập tức. |
| **Đối tác (Merchants / Partners)** | *"Giúp cơ sở của tôi tiếp cận tệp chủ xe có hành vi chi tiêu tốt xung quanh khu vực, tăng doanh số dịch vụ và tự động hóa quy trình nhận lịch hẹn."* | - Thiếu kênh marketing tiếp cận chủ xe trực tuyến tại địa phương (Local).<br>- Quy trình đặt lịch bảo dưỡng thủ công, chồng chéo thời gian.<br>- Khó bán chéo bảo hiểm, phụ kiện cao cấp. | - Hiển thị ưu tiên trên bản đồ tiện ích theo vị trí (Local SEO/GEO).<br>- Tích hợp hệ thống đặt lịch hẹn trực tiếp (Booking Engine).<br>- Nhận diện dòng xe qua Vehicle Profile để cá nhân hóa ưu đãi. |
| **Nền tảng (MoMo Platform)** | *"Giúp MoMo thu hút lượng lớn traffic tự nhiên giá rẻ từ Open Web, định danh phương tiện của người dùng để làm cơ sở bán chéo các gói dịch vụ tài chính có biên lợi nhuận cao."* | - Chi phí chạy ads tìm kiếm user mới quá đắt đỏ.<br>- Dữ liệu người dùng ô tô bị phân mảnh, không biết chính xác đời xe để tư vấn bảo hiểm.<br>- Tỷ lệ đứt gãy cao khi bắt người dùng tải app ngay lần đầu chạm. | - Hứng traffic tự nhiên qua pSEO & Utility Web (Zero-ad cost).<br>- Xây dựng database Vehicle Profile làm giàu dữ liệu để cross-sell.<br>- Luồng Web-to-Vehicle-to-App (W2V2A) tăng tỷ lệ kích hoạt app tự nhiên. |

## V. Site Structure & SEO/GEO


### 5.1 Hub-and-Spoke Sitemap Architecture

#### A. Nhóm Trang Spoke Thuộc Vehicle Hub (`/tien-ich-giao-thong/*`)

| Tên Trang / Sub-page | Đường dẫn URL Gốc (Canonical URL) | Cấu Trúc URL Mở Rộng | Mục Tiêu SEO & Intent |
| :--- | :--- | :--- | :--- |
| **Trang chủ Vehicle Hub** | `/tien-ich-giao-thong` | Master Directory trang chủ | Định danh xe, làm cổng điều hướng tổng thể cho mọi chủ xe. |
| **Giá Xăng Dầu** | `/tien-ich-giao-thong/gia-xang` | `/tien-ich-giao-thong/gia-xang/{loai-xang}`<br>`/tien-ich-giao-thong/gia-xang/{tinh-thanh}` | Hứng **~10.1M volume/tháng**. Kéo traffic lặp lại hàng tuần theo kỳ điều hành giá xăng. |
| **Trạm Sạc Xe Điện** | `/tien-ich-giao-thong/tram-sac` | `/tien-ich-giao-thong/tram-sac` | Hứng **~1.2M volume/tháng** tệp chủ xe điện EV (VinFast, V-Green), phễu bán chéo bảo hiểm xe điện. |
| **Garage Sửa Xe & Bảo Dưỡng** | `/tien-ich-giao-thong/tim-garage` | `/tien-ich-giao-thong/tim-garage/{tinh-thanh}` | Hứng **~272K volume/tháng**. Tìm garage sửa xe & trung tâm bảo dưỡng ô tô 1 cấp theo tỉnh thành. |
| **Đăng Kiểm Xe** | `/tien-ich-giao-thong/dang-kiem` | `/tien-ich-giao-thong/dang-kiem` | Hứng **~182K volume/tháng**. Tra cứu hạn kiểm định & nhắc lịch tự động trước 30/15/7 ngày. |
| **Hãng Xe & Dòng Xe** | `/tien-ich-giao-thong/hang-xe` | `/tien-ich-giao-thong/hang-xe/{hang-xe}`<br>`/tien-ich-giao-thong/hang-xe/{hang-xe}/{dong-xe}` | Master Data **35 Hãng xe & 264 Dòng xe**. Hứng nhu cầu tìm chi phí nuôi xe, thông số & báo giá Bảo hiểm. |
| **Bãi Đỗ Xe & Giữ Xe** | `/tien-ich-giao-thong/bai-do-xe` | `/tien-ich-giao-thong/bai-do-xe` | Tra cứu điểm đỗ & bãi giữ xe ô tô/xe máy, kích hoạt thanh toán tự động VETC Parking/eParking. |
| **Cứu Hộ Đường Bộ 24/7** | `/tien-ich-giao-thong/cuu-ho` | `/tien-ich-giao-thong/cuu-ho/{loai-xe}` | Hứng **~41K volume/tháng**. Sự cố khẩn cấp trên đường (hỏng xe, cẩu kéo, cứu hộ Zuttoride 24/7). |
| **Định Giá Xe** | `/tien-ich-giao-thong/dinh-gia-xe` | `/tien-ich-giao-thong/dinh-gia-xe` | Hứng **~14.5K volume/tháng**. Tra cứu khoảng giá xe cũ, dự báo khấu hao & phễu kích hoạt gói vay / hạn mức Ví Trả Sau. |
| **Blog & Cẩm Nang Giao Thông** | `/tien-ich-giao-thong/blog` | `/tien-ich-giao-thong/blog/{category-slug}`<br>`/tien-ich-giao-thong/blog/{article-slug}` | Knowledge SEO, đón đầu AI Search (Gemini, Perplexity) và nuôi dưỡng nhận thức người dùng. |


#### B. Nhóm Các Trang Use Case Độc Lập (Canonical Top-level Spoke Pages)

| Tên Spoke Page / Use Case | Đường dẫn URL Gốc (Canonical URL) | Cấu Trúc URL Mở Rộng | Mục Tiêu SEO & Intent |
| :--- | :--- | :--- | :--- |
| **Tra Cứu Phạt Nguội** | `/phat-nguoi` | `/phat-nguoi/{tinh-thanh}` | Hứng **~6.1M volume/tháng**. Utility gate 1-click không CAPTCHA $\rightarrow$ Phễu nhập BSX & W2A. |
| **Bảo Hiểm Ô Tô** | `/bao-hiem-o-to` | `/bao-hiem-o-to/tnds`<br>`/bao-hiem-o-to/than-vo`<br>`/bao-hiem-o-to/doi-tac/{ten-doi-tac}` | Mua & tái tục bảo hiểm ô tô TNDS, Thân vỏ. Trang chi tiết theo 9 nhà bảo hiểm đối tác. |
| **Bảo Hiểm Xe Máy** | `/bao-hiem-xe-may` | `/bao-hiem-xe-may/tnds`<br>`/bao-hiem-xe-may/doi-tac/{ten-doi-tac}` | Mua bảo hiểm TNDS xe máy trực tuyến. Trang chi tiết theo đối tác nhà bảo hiểm. |
| **Phí Không Dừng (ePass / VETC)** | `/phi-khong-dung` | `/phi-khong-dung` | Hứng **~95K volume/tháng**. Tra cứu số dư & tự động nạp tiền tài khoản giao thông (VETC/ePass). |








### 5.2 SEO & GEO Strategy
1. **Bảo tồn Uy tín SEO của các Use-case Pages hiện hữu:** Giữ nguyên các URL top-level (`/phat-nguoi`, `/bao-hiem-o-to`, `/bao-hiem-xe-may`, `/gia-xang`, `/epass`) để duy trì thứ hạng Google.
2. **Hứng dòng tìm kiếm địa phương (Local GEO Search):** Cấu trúc phân cấp địa lý (Tỉnh thành > Quận huyện) ở các Spoke (Bãi đỗ xe, Cây xăng, Garage, Trạm sạc) đón đầu nhu cầu tìm kiếm thực tế xung quanh người dùng.
3. **Cá nhân hóa phễu thu thập Profile qua Car Model pSEO:** Hệ thống 1.500+ sub-pages cho từng dòng xe cụ thể (`/hang-xe/vinfast/vf8`, `/hang-xe/toyota/vios`) giải quyết chính xác nhu cầu tìm kiếm thông số và chi phí nuôi xe.
4. **Tối ưu hóa tìm kiếm AI (AI Search Engine Optimization - GEO):** Tổ chức dữ liệu thực thể chuẩn Schema.org giúp các AI Search Engine (Gemini, ChatGPT, Perplexity) trích dẫn nguồn MoMo khi trả lời người dùng.

## VI. Gamification & Promotions

* **Vòng Quay May Mắn (Vehicle Spin Wheel):** Nhận voucher rửa xe miễn phí, thay dầu nhớt hoặc mã giảm giá bảo hiểm khi khởi tạo và lưu Hồ sơ xe (Vehicle Profile Level 1/2) thành công.
* **Gói Bảo Hồi Xe:** Miễn phí bảo hiểm TNDS xe máy 1 năm cho người dùng kích hoạt tiện ích giao thông và hoàn tất lưu thông tin xe.

## VII. Compliance & Risk Governance

### 7.1 Security & PDPD Compliance
* **Nghị định 13/2023/NĐ-CP (PDPD):** Tuân thủ quy định bảo vệ dữ liệu cá nhân khi xử lý thông tin biển số xe, số khung, số máy. Yêu cầu hiển thị Consent Checkbox chấp thuận điều khoản bảo mật trước khi lưu Profile.
* **Quy định Ngân hàng Nhà nước (NHNN):** Mọi giao dịch nạp tiền ETC (ePass/VETC) và mua bảo hiểm được xử lý trực tiếp qua tài khoản MoMo đã hoàn tất xác thực KYC.

### 7.2 Risk Management Matrix

| Rủi ro tiềm tàng | Mức độ | Phương án xử lý | Đơn vị chịu trách nhiệm |
|---|:---:|---|---|
| **Gián đoạn kết nối thanh toán tại trạm xăng** do mạng chập chờn. | Cao | Thiết lập cơ chế thanh toán Offline/Pre-auth, tối ưu dung lượng Mini App dưới 1MB. | Technical Team & M4B |
| **Người dùng từ chối cấp quyền vị trí (GPS)** khi tìm cây xăng/garage. | Trung bình | Tối ưu thông điệp hướng dẫn: *"Cấp quyền vị trí để hiển thị trạm xăng và garage gần nhất"*. | UI/UX Team |
| **Thông tin phạt nguội bị lệch** do dữ liệu chậm cập nhật từ CSGT. | Thấp | Bổ sung tính năng *"Gửi báo cáo phản hồi"* kèm ảnh biên lai đóng phạt để lưu ghi nhận trên hệ thống MoMo. | Operations Team |

## VIII. Growth Roadmap & Changelog


### 8.1 5-Phase Growth Roadmap
* **Phase 1: Vehicle Acquisition Engine (Xây dựng móng hút traffic):** Ra mắt Vehicle Hub, nâng cấp & tích hợp trang Phạt nguội hiện có (`momo.vn/phat-nguoi`), Bảng Giá xăng, Bản đồ Trạm xăng/địa điểm. Kích hoạt cơ chế W2A và lưu hồ sơ xe cơ bản.
* **Phase 2: Vehicle Lifecycle Engine (Động cơ vòng đời):** Triển khai tính năng Nhắc đăng kiểm, Auto-Topup ePass, xây dựng "My Vehicle Web".
* **Phase 3: Vehicle Commerce Engine (Thương mại hóa dịch vụ):** Mở rộng hệ sinh thái Garage bảo dưỡng, VETC Parking, Mua gói Vietmap. Sàn giao dịch Bảo hiểm với Flow e-Claim.
* **Phase 4: Vehicle Intelligence Engine (AI Cá nhân hóa):** Trợ lý AI phân tích thói quen lái xe, tối ưu chi phí, dự báo thời điểm bảo dưỡng.
* **Phase 5: Vehicle Marketplace (Tối đa hóa LTV):** Triển khai Chợ xe cũ, Định giá xe, Vay vốn mua xe.

### 8.2 Change Log

| Phiên bản | Ngày cập nhật | Người thực hiện | Nội dung thay đổi |
|---|---|---|---|
| **v6.1** | 2026-07-29 | Web Product Lead x FS x VTTI | **Combined Master BRD:** Hợp nhất toàn bộ nội dung chi tiết từ `06_USE_CASE_MOMO/vehicle-brd.md` (v6.0) và `05_HUBS/02_Vehicle_Hub/vehicle-hub-brd.md` (v2.4). Bổ sung đầy đủ 6 Use Cases Matrix, Gamification, Compliance PDPD/NHNN và 10 Spoke Pages SEO Architecture. |
| **v6.0** | 2026-07-22 | Web Platform x FS x VTTI | Cập nhật thống nhất Biên bản Kick-off: Bổ sung 3 Phase Timeline, Quy tắc Bảo mật Web Compliance, Quick-win Ads/Giftcard Phạt nguội, và Overlap 0.3-3%. |
| **v5.0** | 2026-07-09 | Web Product Lead | Đại tu hoàn toàn cấu trúc BRD theo chuẩn định dạng Doi-Tac (Header Meta, JTBD Deep-dive, URL Architecture Table, Schema Matrix). |
| **v4.0** | 2026-07-09 | Web Product Lead | Cập nhật cấu trúc toàn diện theo Growth Thesis: Web-to-Vehicle-to-App Flywheel, đổi NSM sang MAV, 7 Layers Architecture. |
