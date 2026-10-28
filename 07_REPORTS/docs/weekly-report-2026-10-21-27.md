# BÁO CÁO TIẾN ĐỘ TUẦN - WEB PLATFORM
Tuần 43 (19/10/2026 – 26/10/2026)  
Phạm vi: Kênh Web MoMo  

---

## I. TỔNG QUAN TIẾN ĐỘ & ĐIỂM NÓNG TRONG TUẦN

### 1. Ba cột mốc nổi bật trong tuần (Top 3 Big Wins)
- **Cinema Hub bù đắp toàn bộ lượng cắt giảm Paid Ads:** Traffic MTD đạt 916.708 lượt xem (+8.104 views so với cùng kỳ T9). Lượt xem tự nhiên trang cụm rạp tăng vọt +142.2% (từ 267K lên 577K views Organic), bù đắp sạch sẽ lượng sụt giảm do cắt 325K views Paid Ads ở các trang phim lẻ.
- **Financial Hub ra mắt cụm Tỷ giá lên Production:** Đưa 4 trang ngoại tệ (USD, EUR, GBP, AUD) kèm biểu đồ và công cụ quy đổi 2 chiều lên chạy thực tế; kéo traffic trang trung tâm tài chính tăng +444.9% (đạt 34K views). Đóng gói hoàn tất Quiz CIC 5 câu hỏi để dẫn phễu kiểm tra điểm tín dụng trên App.
- **Go-live Phase 1 Tìm kiếm Website (`/tim-kiem`):** Đưa thanh tìm kiếm nhanh tức thì, gợi ý từ khóa xu hướng và giao diện xử lý khi không có kết quả lên Production, mở rộng năng lực điều hướng nội bộ toàn Web.

### 2. Hai điểm nghẽn kỹ thuật cần tháo gỡ ngay (Top 2 Blockers)
- **Sự cố rớt thứ hạng lịch chiếu Cinema Hub:** Cụm lịch chiếu phim bị tụt thứ hạng ngày 23/10 do API dữ liệu ngoài phản hồi chậm khiến bot Google không render được nội dung. Cần hoàn tất ngay cơ chế cache tĩnh độc lập trong tuần tới.
- **Dữ liệu Gara & Hãng xe cần VTTI Cell Team nghiệm thu:** Cần VTTI hoàn tất rà soát chất lượng bộ dữ liệu 41 hãng xe và gara trước ngày 31/10 để mở rộng danh mục hiển thị trên Production.

### 3. Tóm tắt kết quả 12 dự án

**Nhóm Dự Án Dịch Vụ (Use Case / Hubs):**
- Cinema Hub: Traffic MTD đạt 916.708 lượt xem (+8.104 views). Trang rạp đối tác (Rio, Touch, Metiz) tăng +142.2%; cụm bài đón đầu phim chiếu rạp cuối năm giữ vững Top 1 tìm kiếm và được Google AI Overviews chọn làm nguồn trích dẫn; thử nghiệm mini game Tap-the-Target phát voucher rạp.
- Financial Hub: Traffic MTD đạt 223.206 lượt xem (+10.91%). Cụm Tỷ giá (+27.8K views) và Ví Trả Sau (+18.5K views) bù lại mức giảm của Vay Nhanh (-31.2K views do cắt Ads). Đưa 4 trang ngoại tệ và Quiz CIC lên Production; xong Staging trang Chứng chỉ quỹ (SIP) và Cổng thông tin 35 Ngân hàng liên kết.
- Vehicle Hub: Traffic MTD đạt 57.875 lượt xem (+3.3%). Tiện ích giao thông mới (10.1K views) và Giá xăng (4.1K views) bù đắp mức giảm của Phạt Nguội. Đưa hệ thống trang gara, 41 hãng xe, bản đồ Cây xăng & Trạm sạc lên Production; khôi phục hoạt động trang Phí không dừng.
- Insurtech Hub: Chuyển toàn bộ 13 trang bảo hiểm ô tô sang MoSpark CMS, bảo toàn 100% URL SEO và form báo giá. Đóng gói widget bảo hiểm dùng chung (ô tô đã live, y tế đã test xong). Hoàn thiện giao diện Trang chủ Bảo hiểm mới gom 9 nhóm sản phẩm.
- New User: Chạy thử trang tải app `/tai-app` (tự nhận diện mobile để vào thẳng store, desktop hiện mã QR). Thiết lập bóc tách riêng phễu Web-to-App giữa nguồn Organic và Paid Ads để kiểm soát đúng chất lượng tăng trưởng thực chất.
- Lottery Hub: Tối ưu hiển thị Vietlott 8 game dạng thẻ dọc; bảng Keno/Bingo18 gọn 20 bóng; XSKT 3 miền hiển thị trọn vẹn 27 giải không cần cuộn ngang. Tự động lấy kết quả mở thưởng từ trường quay và cache offline cho người dùng tra cứu tức thì.
- Dịch vụ mới & Nạp game: Hoàn thành landing page giới thiệu ChatGPT kèm component Bảng giá mới. Duy trì cổng nạp thẻ game chạy ổn định qua 4 nhà cung cấp.

**Nhóm Dự Án Nền Tảng (Platform Enablers):**
- MoSpark Core & Hệ thống AI: Hoàn thành 24 commits lớn, cập nhật 6 bản DB. Tái cấu trúc không gian viết bài sang kiến trúc MVVM 4 lớp; tích hợp mô hình LLM nội bộ MoMo song song với Gemini, Claude, OpenAI qua chuẩn xác thực Bearer JWT; tự động đưa khung tiêu đề H1/H2/H3 vào prompt AI; hoàn thiện CMS adapter xuất bản đa kênh.
- MoBase Design System: Đưa menu điều hướng 2 tầng (Header Advance) lên chạy thực tế tại Financial Hub. Đóng gói component Bảng giá dùng chung cho các trang dịch vụ số.
- CMS & Trình soạn thảo: Nâng cấp cơ chế nạp trang (loop render) giảm độ trễ khi biên tập danh mục lớn; hiển thị quy trình duyệt 4 cấp trên CMS in-app; thêm tính năng đọc bài dạng modal tại khối blog để giảm tỷ lệ thoát trang.
- Tìm kiếm Website: Go-live Phase 1 trên Production (`/tim-kiem`) với Thẻ chuyển tiền qua SĐT (nhận diện client-side bảo mật kèm nút OneLink) và Banner Bạn Mới `CHAOMOMO` 500K; nâng cấp Backend Search V3 tích hợp Custom Search Pages và sửa thuật toán phân trang/đếm tổng chống nhảy trang.
- Dữ liệu & Kiến trúc URL Catalog: Thiết kế kiến trúc Hồ Dữ Liệu Danh Mục URL Website (MoMo URL Knowledge Lake Architecture) quản lý SSOT toàn bộ URL `momo.vn`, phân loại 2 trục (PageType x ProjectIds) phục vụ Search V2, Sitemap SEO đa tầng, AI Feed cho Knowledge Base/RAG và quản trị liên kết mồ côi; hoàn thành kịch bản CSDL `tblWebsiteUrlCatalog`; đóng gói thẻ Coupon và Popup hướng dẫn từng bước chèn qua CKEditor In-App.

---

## II. BÁO CÁO HIỆU SUẤT TOÀN WEBSITE (WEB PLATFORM OVERVIEW)

**Báo cáo số liệu toàn Website (MTD cùng kỳ từ Tháng 7 đến Tháng 10/2026):**

| Chỉ tiêu Hiệu suất Toàn Web | T7/2026 (MTD) | T8/2026 (MTD) | T9/2026 (MTD) | T10/2026 (MTD 26d) | Tăng/Giảm vs. T9 (MTD) | Tỷ trọng T10 (%) | Nhận định & Đánh giá Xu hướng |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Tổng Lượt Xem (Actual)** | **3.168.174** | **3.479.048** | **3.952.859** | **3.076.791** | **-876.068** | **100.0%** | Đạt 83.9% mục tiêu tháng 10 (3.665.607 views); tiến độ 26 ngày giữ nhịp tốt dù cắt giảm mạnh ngân sách quảng cáo |
| **Mục tiêu Tháng (Target)** | 3.167.821 | 3.465.363 | 3.509.044 | 3.665.607 | +156.563 | - | Mục tiêu tăng trưởng thách thức (+4.46% so với T9) |
| **Tỷ lệ Hoàn thành Target** | 100.0% | 100.4% | 112.6% | 83.9% | - | - | Dự báo kết tháng cán mốc ~3.67M views (~100.1% target) |
| **Kênh Tự Nhiên (Non-Paid)** | **2.669.863** | **2.820.824** | **2.755.766** | **2.703.540** | **-52.226** | **87.9%** | Động lực tăng trưởng cốt lõi chiếm gần 88% toàn Web; duy trì ổn định quanh mốc 2.7M views/tháng |
| **Kênh Trả Phí (Paid Traffic)** | **497.958** | **644.539** | **1.197.093** | **373.251** | **-823.842** | **12.1%** | Giảm mạnh -68.8% sau chiến dịch Mega T9; Web chủ động giảm phụ thuộc vào Ads để tập trung tăng trưởng bền vững |

- **Nhận định chuyển dịch nguồn lưu lượng:**
  - Kênh tự nhiên (Non-Paid Traffic) đóng vai trò trụ cột khi chiếm 87.9% tổng lượt xem toàn Website, duy trì đều đặn trên 2.7 triệu lượt xem mỗi tháng, khẳng định nền tảng Web có nội lực tăng trưởng tự nhiên vững chắc.
  - Kênh trả phí (Paid Traffic) giảm mạnh từ 1.197.093 lượt xem (chiếm 30.3% ở T9) xuống còn 373.251 lượt xem (chiếm 12.1% ở T10), phản ánh việc chủ động cắt giảm ngân sách quảng cáo sau chiến dịch Mega T9 để tối ưu hiệu quả chi phí mà vẫn giữ vững tiến độ hoàn thành mục tiêu tháng.

---

## III. NHÓM DỰ ÁN DỊCH VỤ (USE CASE)

### 1. Cinema Hub

- **Key Owner:** Hoan
- **Kết quả & Tác động số liệu:**
  - **Traffic Non-Paid bù toàn bộ phần cắt Ads:** MTD 26 ngày đạt 916.708 views (tăng +8.104 views so với cùng kỳ T9). Điểm sáng lớn là trang cụm rạp đối tác (`Cinema_Cineplex`) tăng vọt +142.2% (từ 299K lên 726K views), trong đó Organic tăng từ 267K lên 577K views, bù đắp hoàn toàn lượng sụt giảm do cắt giảm 325K views Paid Ads ở các trang phim lẻ.
  - **Giữ Top 1 tìm kiếm loạt phim cuối năm:** Cụm bài đón đầu các phim chiếu rạp (*Chị Chị Em Em 3*, *Bò Sữa Bay*, *Án Mạng Karaoke*, *Godzilla Trừ Không*) đều giữ vị trí Top 1 tìm kiếm tự nhiên và được Google AI Overviews chọn làm nguồn trích dẫn trực tiếp.
  - **Thử nghiệm tương tác tăng giữ chân:** Hoàn thành mini game phản xạ chạm hình (Tap-the-Target 8 ô) phát voucher rạp; bước đầu thử nghiệm trên phim *Quỷ Ăn Tạng 4* có 166 lượt tham gia.
  - **Tối ưu hiển thị rạp đối tác:** Nâng cấp layout mới và cấu trúc trang cho các cụm rạp đối tác Rio, Touch, Metiz.

**Báo cáo số liệu Cinema Hub (MTD cùng kỳ từ Tháng 7 đến Tháng 10/2026):**

| Phân loại Trang / Tiện ích | T7/2026 (MTD) | T8/2026 (MTD) | T9/2026 (MTD) | T10/2026 (MTD 26d) | Tăng/Giảm vs. T9 (MTD) | Nhận định & Nguyên nhân Biến động |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Cinema Hub** | **614.777** | **569.986** | **908.604** | **916.708** | **+8.104** | Duy trì đà tăng trưởng trên nền cao; cơ cấu lành mạnh khi Non-Paid bù đắp toàn bộ phần cắt giảm Ads |
| **Trang Rạp phim (Cinema_Cineplex)** | 303.374 | 290.123 | 299.756 | 726.016 | **+426.260** | Bứt phá mạnh (+142.2%) nhờ tối ưu layout cụm rạp đối tác (Rio, Touch, Metiz) và Organic tăng vọt từ 267K lên 577K views |
| **Trang phim chi tiết (Cinema_Page)** | 236.009 | 213.241 | 553.415 | 122.242 | **-431.173** | Giảm do cắt giảm ngân sách Ads (T9 chạy 331K views Ads, T10 chỉ còn 6K views); lưu lượng Organic cốt lõi vẫn giữ vững |
| **Blog Phim (Cinema_Blog)** | 42.502 | 38.369 | 33.617 | 42.977 | **+9.360** | Bật tăng trở lại (+27.8%) nhờ cụm bài phân tích, review đón sóng loạt phim rạp cuối năm giữ vị trí Top 1 tìm kiếm |
| **Trang chủ Cinema (Cinema_Home)** | 29.611 | 25.842 | 20.336 | 22.140 | **+1.804** | Tăng trưởng ổn định (+8.9%), hưởng lợi từ lưu lượng người dùng truy cập trang cụm rạp |
| **Landing Page (Cinema_LP)** | 60 | 79 | 60 | 2.689 | **+2.629** | Tăng vọt nhờ triển khai mini game Tap-the-Target phát voucher rạp (phim *Quỷ Ăn Tạng 4*) và các trang chiến dịch |
| **Tin tức (Cinema_News)** | 3.221 | 2.332 | 1.420 | 644 | **-776** | Giảm do tập trung điều hướng lưu lượng sang Blog chuyên sâu và trang chi tiết rạp |

- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đối tác rạp phim:** Thống nhất cơ chế cấp mã ưu đãi từ mini game để kích thích người dùng đặt vé qua app.
  - **Đội ngũ SEO:** Tiếp tục đẩy mạnh liên kết nội bộ và tối ưu độ uy tín (E-E-A-T) cho cụm bài viết đón đầu các phim lớn cuối năm.
- **Kế hoạch tuần tới:**
  - Triển khai bộ nhớ đệm tĩnh (static cache) cho lịch chiếu rạp, xử lý triệt để nguy cơ tụt thứ hạng khi API ngoài phản hồi chậm.
  - Ra mắt mini game phim *Bò Sữa Bay* bổ sung bảng xếp hạng để tăng tỷ lệ quay lại của người dùng.
  - Tự động lấy đánh giá từ Google Maps hiển thị lên trang cụm rạp Starlight, Cinemax, Mega GS.

---

### 2. Financial Hub

- **Key Owner:** Bùi Minh Nhật
- **Kết quả & Tác động số liệu:**
  - **Traffic Non-Paid bù phần cắt Ads:** Traffic MTD 26 ngày đạt 223.206 views (+10.9% MoM). Điểm sáng là nhóm Non-Paid tăng tốt (+27.8K views từ cụm Tỷ giá, +18.5K views từ Ví Trả Sau), bù lại 31.2K views giảm của Vay Nhanh do cắt ngân sách Ads.
  - **Cụm Tỷ giá lên Production:** Đưa 4 trang ngoại tệ chủ lực (USD, EUR, GBP, AUD sang VND) có biểu đồ và công cụ đổi tiền 2 chiều lên chạy thực tế; kéo traffic trang trung tâm tài chính tăng +444.9% (đạt 34K views) (Link Prod: [momo.vn/tai-chinh](https://www.momo.vn/tai-chinh)).
  - **Đóng gói Quiz CIC dẫn phễu App:** Đã lên Production công cụ 5 câu hỏi (xử lý chuẩn 58 nhánh logic nghiệp vụ) để dẫn người dùng từ Web vào kiểm tra điểm tín dụng trên App (Link Prod: [momo.vn/diem-tin-dung](https://www.momo.vn/diem-tin-dung)).
  - **Hoàn thành Staging 2 sản phẩm mới:** Hoàn thiện chuyên trang Chứng chỉ quỹ (kèm công cụ tính SIP) và Cổng thông tin 35 Ngân hàng liên kết; hiện đang chờ ngành hàng nghiệm thu dữ liệu (Link demo staging: [momo-stg.mservice.io/tai-chinh/chung-chi-quy](https://momo-stg.mservice.io/tai-chinh/chung-chi-quy) · Link demo dev: [momovn-dev.mservice.io/tai-chinh/ngan-hang](https://momovn-dev.mservice.io/tai-chinh/ngan-hang)).
  - **Nâng cấp công cụ so sánh thẻ tín dụng:** Mở rộng danh mục lên 35 thẻ ngân hàng, đổi luồng lọc theo ngân hàng trước rồi mới so sánh điều kiện, lồng ghép kịch bản mở Ví Trả Sau.

**Báo cáo số liệu các mảng tài chính (MTD cùng kỳ từ Tháng 7 đến Tháng 10/2026):**

| Phân nhóm Dịch vụ Tài chính | T7/2026 (MTD) | T8/2026 (MTD) | T9/2026 (MTD) | T10/2026 (MTD 26d) | Tăng/Giảm vs. T9 (MTD) | Nhận định & Nguyên nhân |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Financial Hub** | 88.578 | 190.284 | 201.243 | 223.206 | **+21.963** | Tăng trưởng +10.91% MTD; Tỷ giá và Ví Trả Sau bứt phá bù đắp phần giảm của Vay Nhanh |
| **Điểm Tín Dụng** | 16.131 | 68.814 | 63.027 | 68.324 | **+5.297** | Tăng trưởng ổn định, chuẩn bị mở rộng lưu lượng qua Quiz CIC |
| **Vay Nhanh** | 38.969 | 84.745 | 86.024 | 54.849 | **-31.175** | Sụt giảm do cắt giảm ngân sách Ads, cần bù bằng SEO và Quiz |
| **Ví Trả Sau** | 18.617 | 14.601 | 32.398 | 50.854 | **+18.456** | Bứt phá mạnh (+57.0%) từ nguồn tìm kiếm tự nhiên |
| **Tài Chính (Hub) / Trung Tâm** | 4.741 | 6.589 | 6.250 | 34.056 | **+27.806** | Tăng trưởng đột biến (+444.9%) nhờ đưa vào vận hành cụm Tỷ giá và trang trung tâm |
| **Mở Thẻ Tín Dụng** | 1.254 | 1.064 | 1.126 | 2.901 | **+1.775** | Tăng trưởng từ công cụ so sánh thẻ tín dụng mới |
| **Túi Thần Tài** | 1.786 | 1.809 | 1.645 | 1.828 | **+183** | Giữ vững lưu lượng ổn định |
| **Quỹ Nhóm** | 2.780 | 8.588 | 5.865 | 1.708 | **-4.157** | Giảm sau giai đoạn cao điểm hoạt động nhóm |
| **Chứng Khoán** | 553 | 470 | 383 | 1.645 | **+1.262** | Tăng trưởng nhờ bổ sung content plan kiến thức đầu tư |
| **Tiết Kiệm Online** | 440 | 389 | 394 | 1.347 | **+953** | Tiếp cận tốt qua bảng lãi suất tiết kiệm ngân hàng |
| **Tỷ Giá (FX Rates)** | 0 | 0 | 101 | 963 | **+862** | Đang mở rộng lưu lượng nhanh từ cụm trang ngoại tệ mới |
| **Nhận Tiền Quốc Tế** | 958 | 994 | 872 | 818 | **-54** | Đi ngang |
| **Lãi Suất (Interest Rates)** | 0 | 0 | 77 | 809 | **+732** | Tăng trưởng nhờ trang so sánh lãi suất ngân hàng |
| **Quản Lý Chi Tiêu** | 906 | 959 | 1.002 | 792 | **-210** | Ổn định quanh mức 800 - 1.000 views |
| **Tiệm Vàng Online** | 0 | 0 | 705 | 651 | **-54** | Duy trì ổn định |
| **Trả Góp Apple** | 852 | 800 | 995 | 457 | **-538** | Hạ nhiệt sau đợt mở bán iPhone 16 |
| **Thanh Toán Thẻ Tín Dụng** | 370 | 305 | 171 | 397 | **+226** | Hồi phục nhẹ |
| **Chứng Chỉ Quỹ** | 202 | 140 | 123 | 395 | **+272** | Bắt đầu đón nhận traffic tự nhiên trước đợt go-live chính thức |
| **Giá Vàng (Gold Price)** | 0 | 0 | 59 | 387 | **+328** | Tăng trưởng nhờ trang tra cứu giá vàng trong nước |
| **Sàn đầu tư** | 19 | 17 | 26 | 25 | **-1** | Duy trì mức cơ bản |

- **Phối hợp & Điểm nghẽn cần chốt:**
  - **BU Bank:** Review UI/UX trang chi tiết ngân hàng (Bank Detail) trước ngày 30/10 để xuất bản tiếp hệ thống trang các ngân hàng đối tác.
  - **Finhub:** Cung cấp API bảng giá NAV các Quỹ mở, triển khai hoạt động truyền thông (Comm) và QC công cụ Chứng chỉ quỹ để đưa lên Production.
- **Kế hoạch tuần tới:**
  - Nhúng Quiz CIC vào 10 bài blog tài chính có traffic cao nhất để dẫn luồng kiểm tra điểm tín dụng về App.
  - Triển khai MoMo Gợi Ý (phiên bản AI) trong blog để tăng thời gian đọc trang và điều hướng chéo giữa các dịch vụ tài chính.
  - Duy trì sản xuất nội dung 5 bài/ngày, ưu tiên nhóm từ khóa Thẻ tín dụng và Chứng chỉ quỹ.
  - Triển khai tiếp bản prototype game hóa điểm tín dụng (CIC Gamification) sau khi BU duyệt kịch bản (Link prototype: [claude.ai/artifact/MxUbSrbGRT4Np5tjFXiM4F](https://claude.ai/artifact/MxUbSrbGRT4Np5tjFXiM4F)).

---

### 3. Vehicle Hub

- **Key Owner:** Võ Minh Thuận
- **Kết quả & Tác động số liệu:**
  - **Tiện ích mới bù đắp Phạt Nguội:** Traffic MTD 26 ngày đạt 57.875 views (+3.3% MoM). Nhóm tiện ích mới (Trang trung tâm giao thông đạt 10.1K views, Giá xăng đạt 4.1K views) và Bảo hiểm ô tô (+4.8K views) tăng trưởng tốt, bù đắp phần sụt giảm của Phạt Nguội sau cao điểm tra cứu vi phạm.
  - **Đưa hệ thống Gara & Hãng xe lên Production:** Hoàn thành hệ thống trang danh mục và chi tiết gara, hãng xe, mẫu xe; bộ lọc chuẩn xác 41 hãng xe và ưu tiên gara đa hãng (Link Prod: [momo.vn/tien-ich-giao-thong](https://www.momo.vn/tien-ich-giao-thong) · Link Staging: [momo-stg.mservice.io/tien-ich-giao-thong](https://momo-stg.mservice.io/tien-ich-giao-thong); gara: [momo.vn/tien-ich-giao-thong/garage](https://www.momo.vn/tien-ich-giao-thong/garage), hãng xe VinFast: [momo.vn/tien-ich-giao-thong/hang-xe/vinfast](https://www.momo.vn/tien-ich-giao-thong/hang-xe/vinfast)).
  - **Chuẩn hóa dữ liệu hãng xe:** Tự động nhận diện 135 biến thể tên hãng với độ chính xác 99%, hỗ trợ quản trị viên thao tác bật/tắt hoặc ẩn/hiện danh mục hàng loạt trên CMS.
  - **Live bản đồ Cây xăng & Trạm sạc:** Đưa lên Production bản đồ cây xăng và trạm sạc có ảnh thực tế, giờ mở cửa, số điện thoại và nút chỉ đường bản đồ (traffic Cây xăng tăng +201.1%).
  - **Khôi phục trang Phí không dừng:** Đưa trang `/phi-khong-dung` hoạt động bình thường trở lại sau gián đoạn kỹ thuật (Link Prod: [momo.vn/tien-ich-giao-thong/phi-khong-dung](https://www.momo.vn/tien-ich-giao-thong/phi-khong-dung)).

**Báo cáo số liệu Vehicle Hub (MTD cùng kỳ từ Tháng 7 đến Tháng 10/2026):**

| Phân loại Dịch vụ / Tiện ích | T7/2026 (MTD) | T8/2026 (MTD) | T9/2026 (MTD) | T10/2026 (MTD 26d) | Tăng/Giảm vs. T9 (MTD) | Nhận định & Nguyên nhân Biến động |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Vehicle Hub** | **115.153** | **211.102** | **56.049** | **57.875** | **+1.826** | Tăng trưởng +3.3% MTD; cụm tiện ích mới và Bảo hiểm ô tô bù đắp cho phần giảm của Phạt Nguội |
| **Bảo Hiểm Ô Tô** | 8.839 | 9.967 | 14.292 | 19.074 | **+4.782** | Tăng trưởng liên tục 4 tháng (+115.8% từ T7 đến T10) nhờ đưa widget báo giá lên trang chủ và tối ưu 13 trang bảo hiểm |
| **Phạt Nguội** | 102.701 | 195.667 | 34.670 | 19.009 | **-15.661** | Hạ nhiệt sau cao điểm tra cứu vi phạm; đang hoàn thiện từ điển lỗi vi phạm và kết nối camera để kéo lại Organic |
| **Tiện Ích Giao Thông (Trang trung tâm)** | 0 | 0 | 496 | 10.161 | **+9.665** | Bứt phá mạnh sau khi go-live trang trung tâm giao thông, đón nhận lưu lượng lớn từ Direct và điều hướng nội bộ |
| **Giá Xăng** | 0 | 0 | 193 | 4.166 | **+3.973** | Tăng trưởng nhanh nhờ trang cập nhật biến động giá xăng dầu theo kỳ điều hành thu hút người dùng tra cứu |
| **Bảo Hiểm Xe Máy** | 3.613 | 5.468 | 5.330 | 3.829 | **-1.501** | Giảm nhẹ theo chu kỳ mùa vụ; đang chuẩn bị đóng gói widget mua bảo hiểm xe máy nhúng đa trang |
| **Phí Không Dừng** | 0 | 0 | 826 | 859 | **+33** | Khôi phục hoạt động bình thường (`/phi-khong-dung`) và duy trì lưu lượng ổn định |
| **Cây Xăng** | 0 | 0 | 187 | 563 | **+376** | Tăng trưởng +201.1% sau khi đưa lên Production bản đồ cây xăng có ảnh thực tế, giờ mở cửa và nút chỉ đường |
| **Hãng Xe (VinFast & các hãng)** | 0 | 0 | 0 | 96 | **+96** | Bắt đầu ghi nhận lượt truy cập tự nhiên sau khi go-live cụm trang thông tin hãng xe và mẫu xe |
| **Garage** | 0 | 0 | 0 | 82 | **+82** | Bắt đầu có lưu lượng; đang chờ duyệt gộp 885 gara trùng lặp và kích hoạt lại nhãn bảo hiểm |
| **Trạm Sạc** | 0 | 0 | 55 | 36 | **-19** | Duy trì ở mức cơ bản, cần cập nhật thêm mạng lưới trạm sạc xe điện các hãng |

- **Phối hợp & Điểm nghẽn cần chốt:**
  - **VTTI Cell Team:** Review và kiểm soát chất lượng (QC) toàn bộ dữ liệu gara, hãng xe, mẫu xe trước khi mở rộng danh mục hiển thị.
  - **VTTI Cell Team:** Review trang Nộp Phạt và cung cấp danh sách Trụ Sở Công An để xây dựng tính năng Tìm điểm nộp phạt (API tra cứu Phạt Nguội đã hoàn thiện kết nối độc lập).
- **Kế hoạch tuần tới:**
  - Xây dựng công cụ Tính khấu chi cho chủ sở hữu ô tô.
  - Hoàn thiện Mega Menu điều hướng cho toàn bộ Vehicle Hub.
  - Mở rộng thêm dữ liệu các dòng xe và hãng xe mới.

---

### 4. Insurtech Hub

- **Key Owner:** Võ Minh Thuận
- **Kết quả & Tác động số liệu:**
  - **Chuyển đổi sạch 13 trang bảo hiểm ô tô sang MoSpark CMS:** Gồm 3 trang chủ lực (Trang chủ, Thân vỏ, Bắt buộc TNDS) và 9 trang đối tác (PVI, GIC, MIC, PJICO, Bảo Long, Liberty, PTI, Bảo Việt, DBV), bảo toàn 100% URL SEO, meta tag và form báo giá có lớp chống bot (Link Prod: [momo.vn/bao-hiem-o-to](https://www.momo.vn/bao-hiem-o-to) · Link Staging: [momo-stg.mservice.io/bao-hiem-o-to](https://momo-stg.mservice.io/bao-hiem-o-to)).
  - **Đóng gói widget mua bảo hiểm dùng chung:** Hỗ trợ nhúng form mua bảo hiểm vào bất kỳ trang nào trên Web. Widget ô tô đã live, widget y tế đã kiểm thử xong, widget xe máy đang lên phương án kỹ thuật.
  - **Hoàn thiện Trang chủ Bảo hiểm mới:** Gom 9 nhóm sản phẩm bảo hiểm có phân mục rõ ràng, ưu tiên bảo hiểm y tế, xã hội, ô tô và nhúng trực tiếp công cụ tra cứu BHYT (Link Prod: [momo.vn/bao-hiem](https://www.momo.vn/bao-hiem), chờ ngành hàng duyệt phát hành).
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Ngành hàng Bảo hiểm:** Duyệt nghiệm thu nội dung 13 trang bảo hiểm ô tô và bố cục trang chủ Bảo hiểm mới để phát hành chính thức.
  - **Ngành hàng Bảo hiểm:** Kiểm tra luồng gửi form báo giá bảo hiểm bảo đảm dữ liệu chuyển đổi về hệ thống đối tác thông suốt.
- **Kế hoạch tuần tới:**
  - Đưa Trang chủ Bảo hiểm mới (`/bao-hiem`) và công cụ tra cứu BHYT lên Production.
  - Hoàn thiện đóng gói widget mua bảo hiểm xe máy để nhúng vào các trang bài viết liên quan.
  - Xử lý 2 lỗi nội dung cũ trên trang đối tác PTI và PJICO theo phản hồi từ đối tác.

---

### 5. New User

- **Key Owner:** Võ Minh Thuận
- **Kết quả & Tác động số liệu:**
  - **Chạy thử trang tải app tập trung (`/tai-app`):** Tự động nhận diện thiết bị mobile để chuyển thẳng vào App Store / Google Play, còn desktop hiển thị mã QR cài đặt kèm hướng dẫn xử lý lỗi khi tải app (Link Staging: [momo-stg.mservice.io/tai-app](https://momo-stg.mservice.io/tai-app) · Link Prod: [momo.vn/tai-app](https://www.momo.vn/tai-app), đang thử nghiệm nội bộ).
  - **Bóc tách chuẩn phễu chuyển đổi Web-to-App:** Thiết lập hệ thống đo lường riêng biệt giữa nguồn tự nhiên (Non-Paid) và quảng cáo trả phí (Paid Ads) để đánh giá đúng chất lượng tăng trưởng thực chất, bám sát mục tiêu 30.000 lượt tải app/tháng trong Q4/2026.
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đội ngũ Tăng trưởng Người dùng mới:** Thống nhất các kịch bản thử nghiệm A/B tỷ lệ tải app và rà soát tracking chuyển đổi trên các trang đích Paid Ads.
- **Kế hoạch tuần tới:**
  - Nghiệm thu đo lường và kiểm thử trang `/tai-app` trên nhiều trình duyệt, sẵn sàng go-live chính thức.
  - Tối ưu nút chuyển đổi (CTA) sang app từ các mini game và công cụ tính toán tài chính/xe.
  - Rà soát và tối ưu trang chiến dịch Bonbon chuẩn bị cho cao điểm cuối năm.

---

### 6. Lottery Hub

- **Key Owner:** Duy Trần
- **Kết quả & Tác động số liệu:**
  - **Tối ưu hiển thị Vietlott 8 game trên mobile:** Chuyển bảng so sánh thể lệ sang dạng thẻ dọc, hàng bóng số co giãn linh hoạt, tích hợp công cụ dò vé tự động có tính thuế TNCN và tiện ích tạo số may mắn.
  - **Nâng cấp giao diện Keno, Bingo18 và XSKT 3 miền:** Bảng Keno/Bingo18 hiển thị gọn 20 bóng vừa màn hình mobile; XSKT Miền Bắc hiển thị trọn vẹn 27 giải không cần cuộn ngang; hỗ trợ 3 chế độ xem số và ma trận Lô tô 10x10.
  - **Tự động cập nhật kết quả mở thưởng:** Kết nối dữ liệu trường quay và lưu tạm bộ nhớ đệm trên thiết bị người dùng, giúp tra cứu tức thì không bị phụ thuộc độ trễ mạng.
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đội ngũ Hệ thống:** Giám sát và tối ưu luồng dữ liệu kết quả mở thưởng từ trường quay trong hai khung giờ cao điểm (16h30 và 18h00) để chống nghẽn mạng.
- **Kế hoạch tuần tới:**
  - Theo dõi độ ổn định của hệ thống cập nhật kết quả vào khung giờ quay cao điểm.
  - Đánh giá tỷ lệ người dùng công cụ dò vé tự động và bổ sung nút điều hướng sang mua vé trên app MoMo.

---

### 7. Dịch vụ mới & Nạp game

- **Key Owner:** Nguyễn Việt Hùng
- **Kết quả & Tác động số liệu:**
  - **Hoàn thành landing page giới thiệu ChatGPT:** Thiết kế giao diện giới thiệu dịch vụ ChatGPT trên Web, tích hợp component Bảng giá mới trực quan hóa các gói cước và nút thanh toán nhanh.
  - **Duy trì ổn định cổng nạp thẻ game:** Cổng nạp thẻ game vận hành ổn định qua 4 nhà cung cấp, đảm bảo giao dịch không bị gián đoạn.
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đối tác dịch vụ:** Kiểm tra luồng thanh toán và cơ chế cấp tài khoản tự động cho dịch vụ ChatGPT.
- **Kế hoạch tuần tới:**
  - Thu thập phản hồi người dùng để hoàn thiện kịch bản thanh toán cho dịch vụ ChatGPT.
  - Tối ưu giao diện nạp thẻ game trên mobile để nâng tỷ lệ hoàn tất giao dịch.

---

## IV. NHÓM DỰ ÁN NỀN TẢNG (PLATFORM)

### 1. MoSpark Core & Hệ thống AI

- **Key Owner:** Trần Công Hoàng Trọng
- **Kết quả & Tác động số liệu:**
  - **Nâng cấp kiến trúc và độ ổn định:** Hoàn thành 24 commits lớn và ban hành 6 bản cập nhật cơ sở dữ liệu. Tái cấu trúc khu vực viết bài sang mô hình MVVM 4 lớp độc lập (tách biệt dịch vụ dữ liệu, xử lý nghiệp vụ, lưu trữ trạng thái và giao diện) giúp cô lập lỗi và kiểm soát chặt quy trình từ chọn chủ đề, duyệt dàn ý đến xuất bản.
  - **Tích hợp mô hình AI nội bộ:** Kết nối mô hình LLM nội bộ MoMo song song với Google Gemini, Claude, OpenAI qua chuẩn xác thực an toàn Bearer JWT.
  - **Tự động hóa sinh nội dung theo cấu trúc:** Tự động trích xuất khung tiêu đề (H1/H2/H3) đưa vào prompt sinh nội dung của AI; hoàn thiện hệ thống adapter (`cms-adapters/`) để xuất bản nội dung đa kênh.
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đội ngũ Nội dung & SEO:** Kiểm thử chất lượng sinh bài của mô hình AI nội bộ để từng bước thay thế các API trả phí bên ngoài; chốt quy trình duyệt dàn ý tự động.
- **Kế hoạch tuần tới:**
  - Đưa tính năng phân loại bài viết, hạn mức xuất bản và giao diện duyệt dàn ý (`ReviewOutlineDrawer`) lên Production.
  - Triển khai các cổng xuất bản tự động ra các trang chiến dịch và đối tác.

---

### 2. MoBase Design System

- **Key Owner:** Nguyễn Việt Hùng
- **Kết quả & Tác động số liệu:**
  - **Đưa thanh điều hướng 2 tầng (Header Advance) lên Production:** Đã kích hoạt chạy thực tế trên toàn bộ Financial Hub (`/tai-chinh`), tối ưu hiển thị mượt mà trên cả mobile và desktop.
  - **Chuẩn hóa cấu hình điều hướng:** Hoàn thiện cơ chế cấu hình Header và Footer trên MoSpark CMS, cho phép chuyển đổi linh hoạt giữa menu thường và menu nâng cao.
  - **Đóng gói component dùng chung:** Phát triển component Bảng giá dùng chung cho các trang dịch vụ số (ChatGPT, nạp game).
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đội ngũ Thiết kế (UI/UX):** Thống nhất quy chuẩn hiển thị menu 2 tầng trên các kích thước màn hình trước khi nhân rộng.
- **Kế hoạch tuần tới:**
  - Mở rộng thanh điều hướng 2 tầng sang Cinema Hub và Vehicle Hub.
  - Đóng gói tài liệu hướng dẫn và component mới trong bản phát hành MoBase tiếp theo.

---

### 3. CMS & Trình soạn thảo

- **Key Owner:** Duy Trần
- **Kết quả & Tác động số liệu:**
  - **Tối ưu tốc độ tải và biên tập nội dung:** Nâng cấp cơ chế nạp trang (loop render) trên MoSpark CMS, giảm đáng kể độ trễ khi thao tác và biên dịch các danh mục nội dung lớn.
  - **Minh bạch quy trình phê duyệt in-app:** Hiển thị trực tiếp thông tin 4 cấp phê duyệt (Người yêu cầu, Nội dung, Thiết kế, Pháp lý) trên giao diện quản trị bài viết; giữ nguyên vị trí màn hình sau khi tải bài lên thành công.
  - **Thêm tính năng đọc bài dạng modal:** Cho phép người dùng đọc nhanh bài viết ngay trong cửa sổ modal tại khối blog mà không phải rời trang, giúp giảm tỷ lệ thoát trang.
  - **Chuẩn hóa danh mục hướng dẫn:** Tinh gọn hệ thống còn 2 danh mục chuẩn (Nhóm hướng dẫn & Bài hướng dẫn); sửa lỗi tìm kiếm và chỉ gợi ý các bài đã xuất bản chính thức.
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đội ngũ Pháp lý & Biên tập:** Thống nhất quy chuẩn hiển thị thông tin duyệt bài và hướng dẫn biên tập viên áp dụng quy trình soạn thảo mới.
- **Kế hoạch tuần tới:**
  - Theo dõi phản hồi về hiệu năng của hệ thống quản trị CMS sau đợt tối ưu nạp trang.
  - Rà soát và chuyển đổi toàn bộ bài viết hướng dẫn cũ về đúng 2 danh mục chuẩn.

---

### 4. Tìm kiếm Website (`/tim-kiem`)

- **Key Owner:** Nguyễn Lý Chí Hiếu
- **Kết quả & Tác động số liệu:**
  - **Nâng cấp Backend Tìm kiếm MoMo Search V3 (`SearchService`):** Tích hợp `CustomSearchPages.json` cho phép ghim linh hoạt các trang đích (Landing Pages) và công cụ tiện ích lên đầu danh sách kết quả theo từ khóa cấu hình; chuẩn hóa dữ liệu hiển thị đa thực thể (QA, Blog, Dịch vụ).
  - **Xử lý dứt điểm lỗi phân trang & nhảy trang:** Tự động tính gộp bản ghi ưu tiên vào tổng số (`Total`), tính toán lại `PageCount` và chỉ mục `LastIdx`, ngăn chặn hoàn toàn tình trạng trùng lặp kết quả hoặc nhảy trang khi người dùng cuộn xem thêm.
  - **Ra mắt Thẻ Chuyển tiền qua Số điện thoại (Phone Transfer Card):** Tự động nhận diện chuỗi 10–11 chữ số tại client-side (không gửi số lên server để bảo mật), che mask số điện thoại (`0901****890`) và hiển thị thẻ thông tin kèm nút OneLink "Chuyển tiền ngay" mở App MoMo (Link Prod: [momo.vn/tim-kiem](https://www.momo.vn/tim-kiem)).
  - **Tích hợp phễu Người dùng mới tại luồng Zero-Result:** Hiển thị Banner Chào Bạn Mới với mã quà tặng `CHAOMOMO` 500K khi người dùng tra cứu SĐT hoặc khi từ khóa không có kết quả tìm kiếm. Nâng cấp `@momo-webplatform/mobase` lên phiên bản `0.2.122`.
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đội ngũ Dữ liệu & Tìm kiếm:** Duy trì kết nối ổn định nguồn dữ liệu từ khóa xu hướng và danh mục trang ưu tiên theo thời gian thực.
- **Kế hoạch tuần tới:**
  - Theo dõi hiệu năng, tỷ lệ CTR vào Thẻ chuyển tiền và hành vi tìm kiếm thực tế của người dùng sau khi go-live.
  - Tối ưu trọng số thuật toán để ưu tiên các trang công cụ tiện ích và bài viết chuyên sâu lên đầu bảng kết quả.

---

### 5. Dữ liệu & Kiến trúc URL Catalog

- **Key Owner:** Nguyễn Lý Chí Hiếu
- **Kết quả & Tác động số liệu:**
  - **Thiết kế Kiến trúc Hồ Dữ Liệu Danh Mục URL Website (MoMo URL Knowledge Lake Architecture):** Thiết lập giải pháp Master URL Catalog tập trung (Single Source of Truth) quản lý toàn bộ URL, metadata, cấu trúc phân cấp và thuộc tính nghiệp vụ của toàn bộ website `momo.vn`.
  - **Phục vụ đồng bộ 4 mục tiêu chiến lược của Web Platform:**
    1. *Bộ máy tìm kiếm:* Cung cấp nguồn dữ liệu URL sạch và chuẩn hóa cho `SearchService V2`.
    2. *Tối ưu hóa SEO Google:* Tự động hóa sinh hệ thống Sitemap đa tầng phân rã theo từng dự án (`ProjectIds`).
    3. *AI Knowledge Base & RAG:* Cung cấp URL Directory Feed cập nhật liên tục để các mô hình AI tự động crawl/nạp kiến thức phục vụ AI Engine độc lập.
    4. *Quản trị chất lượng liên kết:* Kiểm soát trang mồ côi (orphan pages), phát hiện link hỏng và giám sát mã trạng thái HTTP toàn trang.
  - **Hoàn thành Cơ sở Dữ liệu & Phân loại Taxonomy 2 trục:** Xây dựng hệ thống phân loại theo loại trang (`PageType`: Service, Miniweb, UtilityTool, Hub, Blog, Guide...) và theo dự án (`ProjectIds`); viết xong kịch bản DDL `tblWebsiteUrlCatalog` với Full-text/Trigram Index, URL Unique Index và trigger tự động cập nhật thời gian.
  - **Đóng gói component nội dung In-App:** Xây dựng khối Thẻ Coupon nhập mã (`momo-coupon-card`) và Mockup điện thoại 540x1168 tương tác từng bước (`cas-htu-popup`) cho phép chèn linh hoạt qua trình soạn thảo CKEditor.
- **Phối hợp & Điểm nghẽn cần chốt:**
  - **Đội ngũ AI & SEO:** Thống nhất định dạng URL Directory Feed và cấu trúc Sitemap phân tầng trước khi chạy cơ chế đồng bộ tự động.
- **Kế hoạch tuần tới:**
  - Triển khai chạy kịch bản tạo bảng `tblWebsiteUrlCatalog` trên môi trường Staging và kết nối thử nghiệm nguồn dữ liệu từ CMS.
  - Xây dựng quy trình tự động cập nhật URL mới vào Knowledge Lake khi biên tập viên xuất bản bài viết hoặc trang tiện ích mới.

---

## V. TỔNG HỢP PHỐI HỢP CẦN XỬ LÝ

**Với các nhóm ngành hàng / dịch vụ:**
- Phim ảnh: Chốt cơ chế trả thưởng voucher rạp từ mini game; ra mắt mini game phim *Bò Sữa Bay*.
- Tài chính (Finhub & BU Bank): BU Bank review UI/UX trang chi tiết ngân hàng (Bank Detail); Finhub triển khai hoạt động truyền thông (Comm), kiểm soát chất lượng (QC) công cụ Chứng Chỉ Quỹ và cung cấp API các Quỹ mở.
- Giao thông (VTTI Cell Team): Review và QC đầy đủ bộ dữ liệu hãng xe, gara; review trang Nộp Phạt và cung cấp danh sách Trụ Sở Công An để làm tính năng Tìm điểm nộp phạt (API tra cứu Phạt Nguội đã hoàn thiện).
- Bảo hiểm: Duyệt phát hành Trang chủ Bảo hiểm mới (`/bao-hiem`) và widget tra cứu BHYT.

**Với các bên kỹ thuật & vận hành:**
- Đối tác SEO: Mở rộng cụm bài viết đón đầu mùa phim cuối năm; tiếp tục kiểm thử mô hình AI nội bộ.
- Đội ngũ hệ thống: Tối ưu đường truyền kết quả xổ số giờ cao điểm; triển khai cache tĩnh lịch chiếu phim.
- Đội ngũ tăng trưởng & truyền thông: Kiểm thử trang tải app `/tai-app` trước khi chạy chiến dịch Q4; rà soát trang Bonbon.
- Pháp lý & kiểm duyệt: Rà soát tuân thủ cho các trang tiện ích tài chính mới và kiểm tra quy trình duyệt bài in-app.

---

## VI. KẾ HOẠCH HÀNH ĐỘNG TUẦN TỚI

### 1. Nhóm Dự Án Dịch Vụ (Use Case)
- Làm bộ nhớ đệm tĩnh cho lịch chiếu rạp tại Cinema Hub để không bị tụt thứ hạng khi API ngoài bị nghẽn.
- Ra mắt mini game phim *Bò Sữa Bay* có thêm bảng xếp hạng tích điểm.
- Xây dựng Tool Khấu Chi cho Vehicle Hub.
- Hoàn thiện Mega Menu cho Vehicle Hub.
- Triển khai mở rộng thêm các hãng xe và dòng xe mới.
- Đưa Trang chủ Bảo hiểm mới (`/bao-hiem`) và công cụ tra cứu BHYT lên Production.
- Nghiệm thu đo lường và kiểm thử trang tải app `/tai-app` trên nhiều trình duyệt, sẵn sàng go-live.
- Tiếp tục đẩy mạnh sản xuất nội dung chuyên sâu Financial Hub (Content Production đạt 5 bài/ngày).
- Nhúng Quiz tương tác trực tiếp vào trong các bài viết Blog tài chính.
- Triển khai tính năng Gợi Ý MoMo phiên bản AI (MoMo Gợi Ý - AI Version).
- Triển khai kịch bản game hóa điểm tín dụng (CIC Gamification).
- Giám sát hệ thống cập nhật kết quả xổ số vào hai khung giờ cao điểm (16h30 và 18h00).
- Rà soát và tối ưu trang chiến dịch Bonbon chuẩn bị cho cao điểm cuối năm.

### 2. Nhóm Dự Án Nền Tảng (Platform)
- Đưa tính năng phân loại bài viết, hạn mức và giao diện duyệt dàn ý của MoSpark lên Production.
- Triển khai chạy kịch bản tạo bảng `tblWebsiteUrlCatalog` trên Staging và kết nối thử nghiệm nguồn dữ liệu từ CMS.
- Xây dựng quy trình tự động cập nhật URL mới vào Knowledge Lake khi xuất bản bài viết hoặc trang tiện ích mới.
- Mở rộng thanh điều hướng 2 tầng sang Cinema Hub và Vehicle Hub.
- Triển khai các cổng xuất bản tự động của MoSpark ra trang chiến dịch và đối tác.
- Theo dõi hiệu năng, tỷ lệ CTR vào Thẻ chuyển tiền và hành vi tìm kiếm thực tế trên `/tim-kiem` sau đợt go-live Phase 1.
- Theo dõi phản hồi về tốc độ của trang quản trị CMS sau khi tối ưu cơ chế nạp trang.
- Chuyển nốt các bài viết hướng dẫn cũ về đúng 2 danh mục chuẩn.
- Đóng gói tài liệu hướng dẫn và component Bảng giá trong bản phát hành MoBase tiếp theo.
