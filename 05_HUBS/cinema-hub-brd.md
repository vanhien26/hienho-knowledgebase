# BRD: Cinema Hub - Cổng Giải Trí & Điện Ảnh MoMo

> - **Project:** Cinema Hub (Web Platform & Cinema Ecosystem Strategy Q2-Q4/2026)
> - **Platform:** Web Platform (`momo.vn/cinema`, `momo.vn/lich-chieu-phim`, `momo.vn/phim-dang-chieu`)
> - **Division:** Marketing Distribution Services (MDS) / Web Platform
> - **Owner:** Web Platform Team (Hiến - Web Product Lead | Hùng - Lead Engineer) x BU Movies
> - **Version:** v3.0 - Tháng 7/2026
> - **Status:** Approved (Aligned with BU Movies)

---

## I. Executive Summary

### 1.1 Core Problems & Objectives
* **Vấn đề thực tế (Problem Statement):** Khách hàng khi có nhu cầu xem phim sẽ chủ động tìm kiếm lịch chiếu/suất chiếu trên Google. Tuy nhiên, MoMo chưa tối ưu hóa chuyên sâu về kỹ thuật và trải nghiệm Web trong các chu kỳ trước, dẫn đến việc bỏ lỡ các từ khóa top ngành (~280K search volume/tháng). Đồng thời, việc thiếu cổng thanh toán trực tiếp trên Web (Non-App payment barrier) khiến tỷ lệ chuyển đổi Web-to-App (W2A CR) giảm mạnh từ 12.10% xuống 4.37%, gây lãng phí lượng lớn cơ hội giao dịch.
* **Mục tiêu định lượng H2/2026:** Uplift **100% mọi chỉ số** so với H1/2026:
  * **Organic Traffic:** Đạt **>4.020.000 visits/H2** (so với 2.01M H1).
  * **Total Traffic:** Đạt **>8.070.000 visits/H2** (so với 4.03M H1).
  * **Booking Clicks:** Đạt **>1.740.000 clicks/H2** (so với 870K H1).
  * **Tickets Sold (Số vé bán):** Đạt **>214.292 vé/H2** (so với 107K H1).
  * **Target Conversion Rate (% W2A):** Khôi phục và nâng CR đạt **≥ 4.50%** nhờ triển khai luồng Native Web Payment.
* **Triết lý cốt lõi:** **"Một bộ phim - Trọn vẹn hành trình điện ảnh"**, biến Web `momo.vn/cinema` thành trung tâm kết nối tự động:
  1. **Tìm kiếm 0-Click, giữ chỗ realtime:** Search Google $\rightarrow$ Thấy ngay lịch chiếu rạp gần nhất trên Web MoMo mà không cần chuyển app hay nhập lại địa điểm.
  2. **Thanh toán liền mạch Native Web Payment:** Người dùng Non-App có thể hoàn tất mua vé và thanh toán trực tiếp trên Web hoặc chuyển tiếp sang App 1-click.
  3. **Vòng đời nội dung tự động (Lifecycle Automation):** Phim đang chiếu $\rightarrow$ Phim hết suất chiếu rạp tự động chuyển hướng sang các nền tảng xem phim OTT đối tác, đảm bảo không lãng phí bất kỳ lượt Traffic nào.

### 1.2 Situation - Complication - Resolution
* **Situation (Bối cảnh & Vị thế):** Cinema là Use Case trưởng thành và có tiềm năng giao dịch lớn nhất của Khối Web Platform (~1M organic/3 tháng Q1/2026, chiếm giữ Top 1 SERP cho từ khóa "vé xem phim"). Website đóng vai trò là **"cửa ngõ hứng nhu cầu và cổng dẫn dắt chuyển đổi"** cho hệ sinh thái vé xem phim MoMo.
* **Complication (Khó khăn & Thách thức):** Tỷ lệ chuyển đổi suy giảm do 4 vấn đề cốt lõi:
  1. *Drop-off ở luồng thanh toán:* Khách hàng Non-App bị chặn lại do bắt buộc tải App mới mua được vé.
  2. *Keyword Gap lớn:* Bỏ lỡ hơn 280K search volume/tháng từ các cụm từ khóa top ngành ("Phim chiếu rạp", "Rạp chiếu phim").
  3. *Rủi ro từ Google AI Overview (AIO):* Thiếu cấu trúc dữ liệu chuẩn Schema khiến Google AI trả về kết quả trực tiếp làm người dùng không click vào Web.
  4. *Nội dung lỗi thời do vận hành thủ công:* Phim hết suất chiếu rạp nhưng Web vẫn hiển thị "Đang chiếu", gây trải nghiệm tệ và lãng phí traffic.
* **Resolution (Giải pháp H2/2026):** Tái cấu trúc toàn diện và chuyển dịch hạ tầng sang nền tảng **MoSpark**, xây dựng **Cinema Hub** theo mô hình Product-Led Growth (PLG) & Hub-and-Spoke. Triển khai **Native Web Payment**, ứng dụng **GenAI Content** tự động hóa vòng đời phim và điều hướng sang các dịch vụ xem phim OTT.

### 1.3 Product-Led Growth (PLG) Drivers
Cơ chế PLG của Cinema Hub dựa trên 5 Phễu Mồi Câu (Acquisition & Engagement Hooks) giải quyết tức thời nhu cầu tìm kiếm trên Open Web:

1. **Phễu Tra Cứu Lịch Chiếu Realtime (Acquisition Gate):** Hứng nhu cầu tìm "lịch chiếu phim [tên phim] [tỉnh thành]" $\rightarrow$ Hiển thị suất chiếu của 8 chuỗi rạp đối tác (CGV, Lotte, Galaxy, BHD, Cinestar, Beta, Mega GS, Touch Cinema) theo vị trí GPS realtime.
2. **Phễu Báo Giá & Ưu Đãi Cụm Rạp (Retention Magnet):** Tra cứu bảng giá vé, chương trình khuyến mãi theo từng rạp $\rightarrow$ Gợi ý Combo Bỏng Nước & Thẻ quà tặng ưu đãi độc quyền MoMo.
3. **Phễu Bách Khoa Toàn Thư Điện Ảnh & Review (Topical Authority Hook):** Đón đầu nhu cầu tìm trailer, diễn viên, đạo diễn, điểm IMDb/Rotten Tomatoes $\rightarrow$ Kích hoạt tính năng đánh giá/review từ cộng đồng người xem MoMo.
4. **Phễu Native Web Payment (Conversion Hook):** Cho phép đặt ghế và thanh toán trực tiếp trên Web không cần mở App đối với khách hàng mới/Non-App.
5. **Phễu Chuyển Đổi Vòng Đời Phim sang OTT (Lifecycle Reminder Hook):** Tự động phát hiện phim đã hết suất chiếu rạp $\rightarrow$ Gợi ý link xem trực tuyến trên các nền tảng OTT đối tác (Netflix, VieON, Galaxy Play, FPT Play).

### 1.4 Key Metrics & Targets

#### Dual North Star Metrics

| Platform Layer | North Star Metric | Definition | Target H2/2026 | Strategic Role |
| :--- | :--- | :--- | :--- | :--- |
| **Web Platform** *(Primary Goal)* | **Total Organic Web Traffic** | Tổng số lượt truy cập tự nhiên từ Google Search và AI Search vào Cinema Hub trên Kênh Web mỗi tháng. | **>4.020.082 Visits/H2** *(Uplift 100%)* | Mục tiêu cốt lõi: Hứng trọn nhu cầu tìm kiếm điện ảnh ngoài Open Web, mở rộng tệp Acquisition. |
| **In-App & Web Booking** *(Secondary Layer)* | **Total Tickets Sold** | Tổng số lượng vé xem phim được xuất bản thành công qua luồng Web & Web-to-App. | **>214.292 Vé/H2** *(Uplift 100%)* | Đo lường hiệu quả chuyển đổi kinh doanh trực tiếp cho BU Movies và các chuỗi rạp đối tác. |

#### Web Platform Metric Tree (Chi tiết H2/2026)

| Metric | 2025 Full Year | Q1/2026 (Baseline) | H1/2026 (Actual) | **H2/2026 (Target)** |
|---|---|---|---|---|
| Organic Traffic | 6,387,700 | 1,066,000 | 2,010,041 | **4,020,082** |
| Total Traffic | 12,425,040 | 2,980,000 | 4,035,028 | **8,070,056** |
| Booking Clicks | 266,258 | 81,517 | 870,467 | **1,740,934** |
| Traffic to App (W2A Users) | 78,735 | 9,866 | 38,079 | **76,158** |
| Transactions (via App/Web) | 52,311 | 9,212 | 48,830 | **97,660** |
| Tickets Sold (Số vé bán) | N/A | N/A | 107,146 | **214,292** |
| **% W2A (Conversion Rate)** | **29.57%** | **12.10%** | **4.37%** | **≥ 4.50%+** |

---

## II. Market Context & Strategy

### 2.1 Market Sizing & Opportunity
* **Quy mô thị trường rạp chiếu phim Việt Nam:** Doanh thu thị trường rạp chiếu phim Việt Nam tăng trưởng mạnh mẽ với hơn 45 triệu lượt vé bán ra hàng năm. 
* **Mạng lưới đối tác:** MoMo kết nối trực tiếp với 8 chuỗi rạp chiếu phim lớn nhất Việt Nam: **CGV, Lotte Cinema, Galaxy Cinema, BHD Star, Cinestar, Beta Cinemas, Mega GS, Touch Cinema**.
* **Xu hướng AI Search & Open Web:** Hơn 85% người xem phim thực hiện tìm kiếm "lịch chiếu phim", "review phim" trên Google trước khi quyết định ra rạp. Việc đón đầu Google AI Overview (AIO) giúp MoMo chiếm lĩnh vị thế Top-of-Mind.

### 2.2 Collaboration Model & Cross-BU Synergy

Dự án được vận hành dưới mô hình đối tác chiến lược giữa **BU Movies** và **Khối Web Platform**:

#### 1. BU Movies (Business Owner)
* **Business Ownership:** Nắm giữ quyền quyết định và chịu trách nhiệm toàn trình đối với kết quả kinh doanh (P&L, Doanh thu, New Users, MAU, Transactions, Số vé bán).
* **Domain Strategy:** Hoạch định chiến lược kinh doanh, đàm phán thương lượng thương mại và định hướng khai thác hệ sinh thái đối tác (8 chuỗi Rạp & Nền tảng OTT).

#### 2. Web Platform (Product & Tech Partner)
* **Product & Growth Ownership:** Sở hữu, định hướng và vận hành Trải nghiệm Sản phẩm (Web Product), Tỷ lệ Chuyển đổi (CR) và Tăng trưởng Organic Traffic.
* **Trọng tâm thực thi H2/2026:**
  * **Product-Led Growth (PLG):** Chuyển hóa luồng Booking thành hệ thống thu hút và giữ chân người dùng tự nhiên.
  * **MoSpark Migration:** Hiện đại hóa hạ tầng công nghệ, nâng cao khả năng chịu tải và tốc độ phát triển.
  * **GenAI Content:** Ứng dụng AI tự động hóa sản xuất nội dung theo Content Plan của BU Movies.

### 2.3 Search Demand & Keyword Gap Analysis

Theo phân tích dữ liệu Open Web, tổng nhu cầu tìm kiếm về điện ảnh vượt **15 triệu lượt/tháng**. Cinema Hub tập trung phủ trọn các nhóm từ khóa chính:

| STT | Cụm Từ Khóa / Use Case | Search Volume / Tháng | Đặc Điểm Ý Định Tìm Kiếm (Search Intent) & Vai Trò Trong Cinema Hub |
| :---: | :--- | :---: | :--- |
| **1** | **Lịch Chiếu Phim & Vé Xem Phim** | **~6.5M** | Intent giao dịch trực tiếp (High Intent). Phễu chọn rạp/suất chiếu & đặt vé ngay. |
| **2** | **Phim Chiếu Rạp / Phim Đang Chiếu**| **~3.2M** | Nhu cầu Discovery (tìm phim hay tuần này). Phễu xem trailer, review & chọn suất chiếu. |
| **3** | **Tên Cụm Rạp (CGV, Lotte, Galaxy...)**| **~2.8M** | Local GEO Search theo thương hiệu rạp gần nhà. Phễu dẫn đường & xem ưu đãi rạp. |
| **4** | **Phim Sắp Chiếu / Trailer Phim** | **~1.1M** | Nhu cầu đón đầu phim hot sắp ra mắt. Phễu đặt nhắc nhở lịch công chiếu (Notify Me). |
| **5** | **Review Phim & Điểm Đánh Giá** | **~850K** | Informational Intent. Phễu đọc nhận xét cộng đồng trước khi quyết định xuống tiền mua vé. |
| **6** | **Phim Xem Online / Phim OTT** | **~600K** | Nhu cầu xem phim tại nhà khi phim hết rạp. Phễu điều hướng sang đối tác OTT. |

### 2.4 Competitive Landscape & MoMo Advantage

| Competitor | Strengths | Weaknesses | MoMo Cinema Hub Advantage |
|---|---|---|---|
| **moveek.com** | Community review, long-tail phim indie | Không có transaction flow trực tiếp | Transaction liền mạch + Hệ sinh thái ưu đãi MoMo |
| **vnpay.vn** | Hạ tầng thanh toán tốt, hub lịch chiếu per chain | Traffic base nhỏ, brand recall yếu | Thương hiệu MoMo Top-of-mind, Organic Traffic khổng lồ |
| **cgv.vn, galaxycine.vn** | Authority gốc của chuỗi | User phải search từng chuỗi riêng biệt | **Aggregator Hub** - So sánh suất chiếu & giá của 8 chuỗi rạp |
| **rapchieuphim.com** | Content sâu, địa điểm long-tail | UX cũ, không có cổng thanh toán | End-to-end flow từ Search $\rightarrow$ Booking $\rightarrow$ Payment |

---

## III. Product Strategy & Core Flows

### 3.1 Multi-sided Value Proposition
* **Cho Người Xem Phim (Consumers):** Tìm kiếm suất chiếu của tất cả các rạp xung quanh trên 1 bản đồ duy nhất, đặt vé không cần tải app, nhận ưu đãi độc quyền combo bỏng nước.
* **Cho 8 Chuỗi Rạp Đối Tác (Cinema Merchants):** Tiếp cận tệp khách hàng mua vé dồi dào từ Open Web (Open Web Traffic Acquisition), tối ưu tỷ lệ lấp đầy ghế trống các suất chiếu.
* **Cho MoMo Platform:** Biến Web thành kênh thu hút người dùng mới (Acquisition Engine), tăng trưởng lượng giao dịch (Transactions) và tối ưu hóa LTV người dùng.

### 3.2 Web Onboarding & Booking Flow

```
[1. Tìm Phim/Lịch chiếu trên Google] → [2. Truy cập Web momo.vn/cinema (Tự động định vị Rạp gần nhất)]
                                                       │
                                                       ▼
[4. Nhận Vé Điện Tử In-App / Email] ◄── [3. Chọn Ghế & Thanh toán Native Web Payment / Mở App 1-Click]
```

### 3.3 Kick-off Alignment Rules & Web Compliance
1. **Chuyển đổi trạng thái phim tự động (Lifecycle Automation):** Phim khi hết suất chiếu rạp phải tự động chuyển trạng thái sang *"Đang chiếu Online"* và gợi ý link xem trên OTT đối tác, tuyệt đối không để trang trống hoặc báo lỗi 404.
2. **Đồng bộ sơ đồ ghế Realtime (Realtime Seat Map Sync):** Đảm bảo giữ ghế chính xác với API của 8 chuỗi rạp, không xảy ra tình trạng trùng ghế khi thanh toán qua Web.
3. **Web Payment Security Compliance:** Tuân thủ chuẩn bảo mật thanh toán PCI-DSS đối với luồng Native Web Payment, xác thực OTP SMS/Biometric khi thanh toán qua Ví MoMo/Thẻ ngân hàng.

### 3.4 Core Use Cases & KPIs Matrix

| # | Use Case (Trải Nghiệm Điện Ảnh) | Search Volume | Mô tả Chức Năng & Luồng Trải Nghiệm | KPIs Cam Kết H2/2026 |
|:---:|:---|:---:|:---|:---|
| 1 | **Tra Cứu Lịch Chiếu Rạp** | **~6.5M** | Tra cứu suất chiếu 8 chuỗi rạp theo vị trí GPS hoặc Tỉnh/Thành. | Top 1 Organic SERP; >4.0M Organic Traffic/H2. |
| 2 | **Đặt Vé Phim Chiếu Rạp** | **Direct Intent** | Luồng chọn ghế, chọn combo bỏng nước & thanh toán Native Web Payment. | >214.292 Vé bán ra; CR ≥ 4.50%. |
| 3 | **Phim Đang Chiếu / Sắp Chiếu**| **~3.2M** | Danh mục tổng hợp danh sách phim hot, trailer HD, thời lượng & độ tuổi. | CTR từ danh mục phim vào Booking >35%. |
| 4 | **Trang Chi Tiết Cụm Rạp** | **~2.8M** | Thông tin địa chỉ rạp, bảng giá vé theo ngày/giờ, hướng dẫn đường đi. | Hứng tệp từ khóa rạp local (CGV Landmark 81, Lotte Gò Vấp...). |
| 5 | **Review & Đánh Giá Phim** | **~850K** | Tổng hợp điểm chấm IMDb, Rotten Tomatoes & nhận xét từ cộng đồng MoMo. | >50k lượt đánh giá mới; rank Google AIO. |
| 6 | **Phim OTT & Xem Online** | **~600K** | Điều hướng người xem phim hết rạp sang nền tảng VieON, Netflix, Galaxy Play. | Kênh chuyển đổi đối tác OTT. |
| 7 | **Combo Bỏng Nước & Bắp Nước** | **Up-sell** | Đặt kèm bắp nước ưu đãi trực tiếp trong luồng mua vé. | Tỷ lệ đính kèm Combo Bắp nước >20% tổng đơn vé. |

### 3.5 Out of Scope
* Không tự vận hành cụm rạp chiếu phim vật lý.
* Không tự sản xuất phim điện ảnh thương mại.
* Không ôm kho vé cứng (chỉ kết nối API giữ vé realtime với các hệ thống Rạp đối tác).

---

## IV. Target Personas & JTBD

### 4.1 Target Personas
* **Persona 1: Gen Z / Bạn trẻ nghiện phim (Movie Buffs):** Thường xuyên tìm kiếm phim hot, xem review trước khi ra rạp, thích đặt vé nhanh không muốn tải thêm app rườm rà.
* **Persona 2: Cặp đôi & Gia đình đi xem phim cuối tuần:** Nhu cầu tìm rạp gần nhà, tiện đường đi ăn uống, chọn rạp có ghế đôi (Sweetbox) hoặc phòng chiếu trẻ em.
* **Persona 3: Người dùng tìm xem phim Online / Phim bộ:** Tìm kiếm các bộ phim đã rời rạp để xem lại trên các ứng dụng OTT tại nhà.

### 4.2 Consumer Journey (4 Stages)
1. **Trigger:** Thấy bài PR/Trailer phim mới trên Facebook/TikTok hoặc có nhu cầu đi chơi cuối tuần.
2. **Search & Discovery:** Search Google *"lịch chiếu phim [tên phim]"* $\rightarrow$ Truy cập `momo.vn/cinema` hiển thị rạp gần nhất theo vị trí GPS.
3. **Booking & Payment:** Chọn rạp $\rightarrow$ Chọn suất chiếu & ghế đẹp $\rightarrow$ Thanh toán trực tiếp trên Web bằng Native Web Payment (hoặc mở App MoMo).
4. **Experience & Retention:** Nhận vé điện tử có mã QR check-in tại rạp $\rightarrow$ Nhận thông báo đánh giá phim sau khi xem $\rightarrow$ Gợi ý các phim cùng thể loại sắp ra mắt.

### 4.3 Multi-sided JTBD Matrix

| Đối tượng | Job-To-Be-Done chính (Job Statement) | Pain Points cần giải quyết | Thay đổi sau khi dùng Cinema Hub |
| :--- | :--- | :--- | :--- |
| **Người xem phim (Consumers)** | *"Giúp tôi tìm suất chiếu phim phù hợp nhất tại các rạp gần tôi và đặt vé nhanh chóng mà không cần tải nhiều app từng chuỗi rạp."* | - Phải tải app của từng rạp riêng lẻ (CGV app, Lotte app...).<br>- Bị đứt gãy luồng mua vé khi dùng Web do bắt tải App.<br>- Thông tin lịch chiếu rạp không cập nhật đúng realtime. | - Tất cả 8 chuỗi rạp trên 1 giao diện duy nhất.<br>- Mua vé & thanh toán mượt mà trên Native Web.<br>- Lịch chiếu tự động cập nhật chuẩn xác. |
| **Chuỗi Rạp Đối Tác (Cinemas)** | *"Giúp rạp của tôi tiếp cận lượng lớn khách hàng tìm kiếm tự nhiên trên Google để lấp đầy các suất chiếu còn trống."* | - Phụ thuộc vào kênh traffic tự có của app rạp.<br>- Chi phí quảng cáo tìm khách hàng mới trên Open Web đắt đỏ.<br>- Tỷ lệ hủy vé cao nếu luồng đặt vé rườm rà. | - Hứng hàng triệu lượt search tự nhiên từ MoMo Web.<br>- Đồng bộ ghế và bán vé tự động 24/7.<br>- Đẩy mạnh bán kèm Combo Bỏng nước tăng ARPU. |
| **Nền tảng (MoMo Platform)** | *"Giúp MoMo biến Web Cinema thành kênh thu hút người dùng mới, khôi phục CR và tối đa hóa số lượng vé bán ra."* | - CR luồng W2A suy giảm xuống 4.37% do rào cản ứng dụng.<br>- Bỏ lỡ tệp từ khóa ngành ~280K volume/tháng.<br>- Phim hết rạp không mang lại giá trị gia tăng. | - Tăng trưởng Traffic H2 đạt >8.07M.<br>- Khôi phục CR ≥ 4.50% nhờ Native Web Payment.<br>- Tận dụng traffic phim hết rạp để monetization qua OTT. |

---

## V. Site Structure & SEO/GEO

### 5.1 Hub-and-Spoke Sitemap Architecture

| Tên Spoke Page / Vai trò | Đường dẫn URL Gốc (Canonical / Top-level URL) | Năng lực pSEO & Local GEO Indexing | Mục tiêu SEO & User Intent |
| :--- | :--- | :--- | :--- |
| **Trang chủ Cinema Hub (Master Hub)** | `/cinema`<br>*(Alias: `/lich-chieu-phim`)* | Master Directory tổng hợp toàn bộ Phim đang chiếu, Rạp gần bạn & Widget tìm kiếm. | Định vị rạp gần nhất, cổng điều hướng tổng thể cho người mê phim. |
| **Spoke Phim Đang Chiếu** | `/phim-dang-chieu` | **Category pSEO Page:**<br>- `/phim-dang-chieu/{the-loai}` (Hành động, Tình cảm...)<br>- `/phim-dang-chieu/{quoc-gia}` (Phim Việt, Phim Hàn...) | Hứng nhu cầu xem danh sách phim chiếu rạp hot trong tuần. |
| **Spoke Phim Sắp Chiếu** | `/phim-sap-chieu` | **Category pSEO Page:**<br>- `/phim-sap-chieu/thang-{mm-yyyy}` | Hứng từ khóa phim công chiếu tháng tới $\rightarrow$ Kích hoạt phễu *"Nhắc tôi"*. |
| **Spoke Chi Tiết Phim** | `/phim/{movie-slug}` | **Movie Entity Page:**<br>- `/phim/{movie-slug}/lich-chieu`<br>- `/phim/{movie-slug}/review` | Hứng từ khóa tên phim cụ thể (Ví dụ: *"lịch chiếu phim Lật Mặt 7"*). |
| **Spoke Cụm Rạp & Địa Điểm** | `/rap-chieu-phim` | **Local GEO 3 Cấp:**<br>- `/rap-chieu-phim/{chuoi-rap}` (CGV, Lotte...)<br>- `/rap-chieu-phim/{chuoi-rap}/{tinh-thanh}`<br>- `/rap-chieu-phim/{rap-slug}` (CGV Vincom Đồng Khởi) | Hứng từ khóa rạp local theo Tỉnh/Thành & Quận/Huyện. |
| **Spoke Bách Khoa Điện Ảnh** | `/review-phim` | **Topical Authority pSEO:**<br>- `/dien-vien/{actor-slug}`<br>- `/dao-dien/{director-slug}` | Đón đầu nhu cầu tìm thông tin diễn viên, đạo diễn & review bài viết sâu. |
| **Spoke Phim OTT & Online** | `/xem-phim-online` | **Partner Monetization pSEO:**<br>- `/xem-phim-online/{doi-tac}` (VieON, Netflix...) | Chuyển đổi traffic phim hết rạp sang nền tảng xem phim trực tuyến. |

### 5.2 SEO & GEO Strategy
1. **Cấu trúc Dữ liệu Chuẩn Schema.org (Movie & ScreeningEvent):** Khai báo chi tiết dữ liệu thực thể phim, đạo diễn, diễn viên, thời gian chiếu và rạp chiếu giúp Google AI Overview (AIO) trích dẫn nguồn MoMo trực tiếp.
2. **Local GEO Search theo Cụm Rạp:** Cấu trúc URL 3 cấp độ (`/rap-chieu-phim/cgv/tp-hcm/cgv-landmark-81`) đảm bảo chiếm giữ Top 1-3 SERP khi người dùng tìm rạp theo quận/huyện.
3. **Tự động hóa Nội dung bằng GenAI (GenAI Content Pipeline):** Tự động sinh tóm tắt nội dung phim, phân tích điểm nổi bật và tạo bài tổng hợp theo Content Plan của BU Movies.

---

## VI. Gamification & Promotions

* **Vòng Quay Vé Xem Phim (Movie Spin Wheel):** Cơ hội trúng vé xem phim 0đ, Voucher Combo Bắp Nước hoặc Mã giảm giá 50% khi hoàn tất mua vé trên Web.
* **Tích Điểm Cụm Rạp:** Đồng bộ tích điểm thành viên cho các chuỗi rạp đối tác (CGV Cinema Member, Lotte Club...) trực tiếp khi đặt vé trên hệ thống MoMo.

---

## VII. Compliance & Risk Governance

### 7.1 Compliance & Security Rules
* **Tuân thủ Bảo vệ Dữ liệu Cá nhân (PDPD - NĐ 13/2023/NĐ-CP):** Bảo mật thông tin giao dịch, SĐT và Email của khách hàng mua vé trên Web.
* **Xử lý Sự cố Ghế Trùng / Lỗi API Rạp:** Trường hợp API hệ thống rạp gặp sự cố không cấp được vé, hệ thống tự động hoàn tiền 100% về tài khoản người dùng trong vòng 5 phút và gửi SMS thông báo kèm Voucher đền bù.

### 7.2 Risk Management Matrix

| Rủi ro tiềm tàng | Mức độ | Phương án xử lý | Đơn vị chịu trách nhiệm |
|---|:---:|---|---|
| **API Chuỗi Rạp bị nghẽn** vào khung giờ cao điểm mở bán phim bom tấn. | Cao | Triển khai cơ chế Caching lịch chiếu MoSpark & Queue giữ chỗ tạm thời trong 5 phút. | Technical Team (Lead Eng: Hùng) |
| **Người dùng hủy vé / Muốn đổi suất chiếu** sau khi thanh toán trên Web. | Trung bình | Hiển thị rõ quy định hủy vé của từng chuỗi rạp trước khi bấm thanh toán. | Product Team & Operations |
| **Phim bị hoãn/hủy công chiếu** từ phía nhà phát hành. | Thấp | Tự động quét cập nhật trạng thái phim từ hệ thống rạp và thông báo hoàn tiền tự động. | Operations Team & BU Movies |

---

## VIII. Growth Roadmap & Changelog

### 8.1 5-Phase Growth Roadmap

* **Phase 1: MoSpark Migration & Utility SEO Hub (Tháng 7-8/2026):** Tái cấu trúc hạ tầng Cinema Hub sang MoSpark, khắc phục lỗi hiển thị phim hết suất chiếu, tối ưu hóa các trang Lịch chiếu rạp & Cụm rạp.
* **Phase 2: Native Web Payment & Automated Lifecycle (Tháng 8-9/2026):** Ra mắt luồng thanh toán Native Web Payment cho khách hàng Non-App. Tự động hóa chuyển đổi phim hết rạp sang danh mục OTT.
* **Phase 3: GenAI Content & Topical Authority (Tháng 9-10/2026):** Phủ sóng hệ thống Bách khoa toàn thư điện ảnh, tự động tạo bài viết review & thông tin diễn viên bằng AI.
* **Phase 4: Community Review & Personalization (Tháng 10-11/2026):** Ra mắt tính năng chấm điểm/review từ cộng đồng người xem MoMo, cá nhân hóa gợi ý phim theo sở thích.
* **Phase 5: Entertainment Aggregator (Tháng 11-12/2026):** Mở rộng kết nối toàn diện với các dịch vụ giải trí, sự kiện âm nhạc, sân khấu kịch & đối tác OTT.

### 8.2 Change Log

| Phiên bản | Ngày cập nhật | Người thực hiện | Nội dung thay đổi |
|---|---|---|---|
| **v3.0** | 2026-07-30 | Web Product Lead (Hiến) | **Chuyển đổi sang Cinema Hub Master BRD:** Tái cấu trúc toàn bộ nội dung từ `06_USE_CASE_MOMO/cinema-alignment.md` theo định dạng Hub chuẩn (`05_HUBS`). Bổ sung 5 Phễu PLG, Native Web Payment Flow, Hub-and-Spoke Sitemap, Schema.org Matrix và 5-Phase Roadmap H2/2026. |
| **v2.6** | 2026-07-22 | Web Product Lead x BU Movies | Thống nhất Kế hoạch H2/2026: Cam kết Uplift 100% các chỉ số (Organic Traffic 4.02M, Total Traffic 8.07M, Tickets Sold 214K vé), phân định Collaboration Model giữa BU Movies & Web Platform. |
