# BÁO CÁO TIẾN ĐỘ TUẦN - WEB PLATFORM
Tuần 43 (19/10/2026 – 26/10/2026)  
Phạm vi: Kênh Web MoMo  

---

## I. TỔNG QUAN TIẾN ĐỘ & ĐIỂM NÓNG TRONG TUẦN

### 1. Tóm tắt kết quả theo 2 nhóm dự án

**Nhóm Dự Án Dịch Vụ (Use Case / Hubs):**
- Cinema Hub: Traffic MTD 26 ngày đạt 916.708 lượt xem (tăng +8.104 views so với 908.604 views cùng kỳ T9). Toàn bộ cụm bài đón đầu các phim chiếu rạp cuối năm (*Chị Chị Em Em 3*, *Bò Sữa Bay*, *Án Mạng Karaoke*, *Godzilla Trừ Không*) đều giữ Top 1 tìm kiếm và được Google AI Overviews chọn làm nguồn trích dẫn trực tiếp. Bàn giao mini game Tap-the-Target phát voucher rạp (game phim *Quỷ Ăn Tạng 4* có 166 lượt tham gia).
- Financial Hub: Traffic MTD 26 ngày đạt 223.206 lượt xem (tăng +21.963 views, tương đương +10.91% so với 201.243 views cùng kỳ T9). Cụm Tỷ giá & Trung tâm tài chính (+27.8K) và Ví Trả Sau (+18.5K) bứt phá mạnh, bù đắp cho phần sụt giảm của Vay Nhanh (-31.2K do cắt giảm Ads). Đưa 4 trang tỷ giá chủ lực (USD, EUR, GBP, AUD sang VND) lên Production kèm biểu đồ real-time và công cụ quy đổi 2 chiều. Lên demo staging trang Chứng chỉ quỹ và công cụ tính SIP; demo dev trang Ngân hàng liên kết và prototype game Săn điểm tín dụng. Hoàn tất kịch bản Quiz CIC (5 câu hỏi rẽ nhánh, đối soát khớp 58/58 case nghiệp vụ).
- Vehicle Hub: Traffic MTD 26 ngày đạt 57.875 lượt xem (tăng +1.826 views, tương đương +3.3% so với 56.049 views cùng kỳ T9). Nhóm tiện ích mới (Tiện ích giao thông, Giá xăng) và Bảo hiểm ô tô tăng trưởng mạnh bù đắp cho phần giảm của Phạt Nguội. Đưa lên Production hệ thống trang danh sách và chi tiết gara, hãng xe, mẫu xe; xử lý xong bộ lọc 41 hãng xe và ưu tiên gara đa hãng. Khôi phục trang Phí không dừng (`/phi-khong-dung`). Bản đồ Cây xăng & Trạm sạc đã live kèm ảnh thực tế, giờ mở cửa và nút chỉ đường.
- Insurtech Hub: Chuyển toàn bộ 13 trang bảo hiểm ô tô sang MoSpark CMS, bảo toàn 100% cấu trúc URL SEO và form báo giá. Đóng gói widget bảo hiểm dùng chung để nhúng đa trang (widget ô tô đã live, widget y tế đã test xong). Hoàn thiện trang chủ Bảo hiểm mới gom 9 nhóm dịch vụ.
- New User: Chạy thử trang tải app `/tai-app` (tự nhận diện mobile để vào thẳng store, hiện QR trên desktop). Thiết lập bóc tách riêng phễu Web-to-App giữa nguồn Organic và Paid Ads để kiểm soát đúng chất lượng tăng trưởng thực chất.
- Lottery Hub: Tối ưu hiển thị Vietlott 8 game sang dạng thẻ dọc cho mobile; bảng Keno/Bingo18 hiển thị gọn 20 bóng; XSKT 3 miền hiển thị trọn vẹn 27 giải không cần cuộn ngang. Tự động lấy kết quả mở thưởng từ trường quay và cache offline cho người dùng tra cứu tức thì.
- Dịch vụ mới & Nạp game: Hoàn thành landing page giới thiệu ChatGPT kèm component Bảng giá mới. Duy trì cổng nạp thẻ game chạy ổn định qua 4 nhà cung cấp.

**Nhóm Dự Án Nền Tảng (Platform Enablers):**
- MoSpark Core & Hệ thống AI: Hoàn thành 24 commits lớn, cập nhật 6 bản DB. Tái cấu trúc không gian viết bài sang kiến trúc MVVM 4 lớp để cô lập lỗi; tích hợp mô hình LLM nội bộ MoMo song song với Gemini, Claude, OpenAI qua xác thực an toàn Bearer JWT; tự động đẩy khung tiêu đề H1/H2/H3 vào prompt AI; hoàn thiện CMS adapter xuất bản đa kênh.
- MoBase Design System: Đưa menu điều hướng 2 tầng (Header Advance) lên chạy thực tế tại mục Tài chính. Đóng gói component Bảng giá dùng chung cho các trang dịch vụ số.
- CMS & Trình soạn thảo: Thêm tính năng đọc bài dạng modal tại khối blog để giữ chân người đọc; tối ưu cơ chế nạp trang (loop render) khi biên tập danh mục lớn; thêm quy trình duyệt 4 cấp (Người yêu cầu, Nội dung, Thiết kế, Pháp lý) trên CMS in-app.
- Tìm kiếm Website: Chính thức go-live giai đoạn 1 (Phase 1) trên Production (`/tim-kiem`), bao gồm thanh tìm kiếm nhanh tức thì, gợi ý từ khóa xu hướng và giao diện xử lý khi không có kết quả.
- Dữ liệu & Đo lường: Vận hành cơ chế đồng bộ số liệu tự động 1-2 giây; audit các trang không có hiển thị (zero-impression) trên Search Console; chuẩn hóa URL mapping đạt độ khớp 100% trên GA4/GSC, xóa sạch dữ liệu rác ở nhóm Others.

### 2. Điểm nghẽn kỹ thuật & Rủi ro cần tháo gỡ ngay
- Cụm lịch chiếu phim Cinema Hub bị tụt thứ hạng ngày 23/10 do API dữ liệu ngoài phản hồi chậm khiến bot Google không render được nội dung. Cần làm ngay cơ chế cache tĩnh độc lập cho toàn bộ dữ liệu lịch chiếu.
- Dữ liệu gara và hãng xe trên Vehicle Hub cần Cell Team (VTTI) review và QC đầy đủ để bảo đảm độ chính xác trước khi mở rộng danh mục hiển thị.

---

## II. BÁO CÁO HIỆU SUẤT TOÀN WEBSITE (WEB PLATFORM OVERVIEW)

**Báo cáo số liệu toàn Website (MTD cùng kỳ từ Tháng 7 đến Tháng 10/2026 - Master SSOT):**

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

- **Kết quả nổi bật:**
  - Lượt xem tự nhiên thư mục `/cinema` tăng trưởng +71% so với cùng kỳ.
  - Cụm bài đón đầu loạt phim chiếu rạp cuối năm (*Chị Chị Em Em 3*, *Bò Sữa Bay*, *Godzilla Trừ Không*, *Án Mạng Karaoke*) đều giữ vững Top 1 tìm kiếm tự nhiên và xuất hiện trực tiếp trong khung Google AI Overviews.
  - Hoàn thiện mini game phản xạ chạm hình (Tap-the-Target 8 ô) đạt 5 điểm nhận voucher rạp; game phim *Quỷ Ăn Tạng 4* ghi nhận 166 người tham gia thực tế.
  - Nâng cấp layout mới và tối ưu cấu trúc trang cho các cụm rạp đối tác Rio, Touch, Metiz.

**Báo cáo số liệu Cinema Hub (MTD cùng kỳ từ Tháng 7 đến Tháng 10/2026 - Master SSOT):**

| Phân loại Trang / Tiện ích | T7/2026 (MTD) | T8/2026 (MTD) | T9/2026 (MTD) | T10/2026 (MTD 26d) | Tăng/Giảm vs. T9 (MTD) | Nhận định & Nguyên nhân Biến động |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Toàn bộ Cinema Hub** | **614.777** | **569.986** | **908.604** | **916.708** | **+8.104** | Duy trì đà tăng trưởng trên nền cao; cơ cấu lành mạnh khi Non-Paid bù đắp toàn bộ phần cắt giảm Ads |
| **Trang Rạp phim (Cinema_Cineplex)** | 303.374 | 290.123 | 299.756 | 726.016 | **+426.260** | Bứt phá mạnh (+142.2%) nhờ tối ưu layout cụm rạp đối tác (Rio, Touch, Metiz) và Organic tăng vọt từ 267K lên 577K views |
| **Trang phim chi tiết (Cinema_Page)** | 236.009 | 213.241 | 553.415 | 122.242 | **-431.173** | Giảm do cắt giảm ngân sách Ads (T9 chạy 331K views Ads, T10 chỉ còn 6K views); lưu lượng Organic cốt lõi vẫn giữ vững |
| **Blog Phim (Cinema_Blog)** | 42.502 | 38.369 | 33.617 | 42.977 | **+9.360** | Bật tăng trở lại (+27.8%) nhờ cụm bài phân tích, review đón sóng loạt phim rạp cuối năm giữ vị trí Top 1 tìm kiếm |
| **Trang chủ Cinema (Cinema_Home)** | 29.611 | 25.842 | 20.336 | 22.140 | **+1.804** | Tăng trưởng ổn định (+8.9%), hưởng lợi từ lưu lượng người dùng truy cập trang cụm rạp |
| **Landing Page (Cinema_LP)** | 60 | 79 | 60 | 2.689 | **+2.629** | Tăng vọt nhờ triển khai mini game Tap-the-Target phát voucher rạp (phim *Quỷ Ăn Tạng 4*) và các trang chiến dịch |
| **Tin tức (Cinema_News)** | 3.221 | 2.332 | 1.420 | 644 | **-776** | Giảm do tập trung điều hướng lưu lượng sang Blog chuyên sâu và trang chi tiết rạp |
- **Phối hợp:**
  - Làm việc với bên rạp phim chuẩn hóa cơ chế cấp mã ưu đãi từ mini game để kích thích người dùng đặt vé.
  - Làm việc với bên SEO đẩy bài và tăng độ uy tín (E-E-A-T) cho cụm trang phim đón sóng cuối năm.
- **Kế hoạch tuần tới:**
  - Triển khai bộ nhớ đệm tĩnh cho lịch chiếu rạp, bảo đảm bot tìm kiếm đọc dữ liệu ổn định ngay cả khi API ngoài bị nghẽn.
  - Ra mắt mini game phim *Bò Sữa Bay* có thêm bảng xếp hạng để tăng tỷ lệ quay lại.
  - Tự động lấy đánh giá từ Google Maps đưa lên các trang cụm rạp Starlight, Cinemax, Mega GS.

---

### 2. Financial Hub

- **Kết quả nổi bật:**
  - Trang chủ `/tai-chinh` tăng +80% lượt xem tự nhiên so với cùng kỳ.
  - Đưa lên Production cụm 4 trang tỷ giá ngoại tệ chủ lực (AUD, EUR, USD, GBP sang VND) có chart biến động real-time, công cụ đổi tiền 2 chiều và bảng so sánh đa ngân hàng (Link Prod: [momo.vn/tai-chinh](https://www.momo.vn/tai-chinh)).
  - Chạy thử chuyên trang Chứng chỉ quỹ (`/tai-chinh/chung-chi-quy`) và công cụ tính tích sản định kỳ SIP; bổ sung bảng so sánh các quỹ mở (Link demo staging: [momo-stg.mservice.io/tai-chinh/chung-chi-quy](https://momo-stg.mservice.io/tai-chinh/chung-chi-quy), đang chờ ngành hàng nghiệm thu).
  - Xây dựng trang tổng hợp Ngân hàng liên kết (`/tai-chinh/ngan-hang`) và hệ thống trang chi tiết từng ngân hàng; đưa lên MoSpark CMS để bên ngành hàng tự cập nhật nội dung (Link demo dev: [momovn-dev.mservice.io/tai-chinh/ngan-hang](https://momovn-dev.mservice.io/tai-chinh/ngan-hang)).
  - Làm lại công cụ so sánh thẻ tín dụng: mở rộng lên 35 thẻ ngân hàng, đổi luồng lọc theo ngân hàng trước rồi mới so sánh điều kiện, lồng ghép kịch bản giới thiệu mở Ví Trả Sau.
  - Bổ sung chỉ số thị trường real-time vào khối Gợi ý MoMo để hỗ trợ người dùng ra quyết định.
  - Xây dựng prototype game "Săn điểm tín dụng" phục vụ định hướng truyền thông về điểm tín dụng qua gamification (Link prototype: [claude.ai/artifact/MxUbSrbGRT4Np5tjFXiM4F](https://claude.ai/artifact/MxUbSrbGRT4Np5tjFXiM4F), chờ review nội bộ trước khi gửi ngành hàng).
  - Hoàn thành Quiz ước tính điểm CIC: 5 câu hỏi rẽ nhánh, đối soát 58 kịch bản khớp chính xác với bảng tính nghiệp vụ, đồng thời đóng gói thành tool tạo Quiz linh hoạt cho các dịch vụ khác (Link Prod: [momo.vn/diem-tin-dung](https://www.momo.vn/diem-tin-dung)).
  - Gắn trợ lý MoMo AI vào 100% công cụ tính toán và hoàn thiện tracking đo lường chi tiết hành vi người dùng.

**Báo cáo số liệu các mảng tài chính (MTD cùng kỳ từ Tháng 7 đến Tháng 10/2026 - Master SSOT):**

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

- **Phối hợp:**
  - BU Bank review UI/UX trang chi tiết ngân hàng (Bank Detail).
  - Finhub triển khai các hoạt động truyền thông (Comm), kiểm soát chất lượng (QC) công cụ Chứng Chỉ Quỹ và cung cấp API kết nối các Quỹ mở.
- **Kế hoạch tuần tới:**
  - Tiếp tục đẩy mạnh sản xuất nội dung (Content Production đạt 5 bài/ngày).
  - Nhúng Quiz tương tác trực tiếp vào trong các bài viết Blog.
  - Triển khai tính năng Gợi Ý MoMo phiên bản AI (MoMo Gợi Ý - AI Version).
  - Triển khai kịch bản game hóa điểm tín dụng (CIC Gamification).

---

### 3. Vehicle Hub

- **Kết quả nổi bật:**
  - Đưa lên Production hệ thống trang danh sách và chi tiết gara, hãng xe, mẫu xe; cho phép lọc gara chuẩn xác theo đúng 41 hãng xe và ưu tiên hiển thị gara đa hãng (Link Prod: [momo.vn/tien-ich-giao-thong](https://www.momo.vn/tien-ich-giao-thong) · Link Staging: [momo-stg.mservice.io/tien-ich-giao-thong](https://momo-stg.mservice.io/tien-ich-giao-thong); trang gara: [momo.vn/tien-ich-giao-thong/garage](https://www.momo.vn/tien-ich-giao-thong/garage), trang hãng xe VinFast: [momo.vn/tien-ich-giao-thong/hang-xe/vinfast](https://www.momo.vn/tien-ich-giao-thong/hang-xe/vinfast)).
  - Hệ thống tự động nhận diện hãng xe từ tệp dữ liệu đối tác với độ chính xác 99%, chuẩn hóa 135 biến thể viết tự do của tên hãng, cho phép quản trị viên thao tác ẩn/hiện hoặc bật/tắt hàng loạt.
  - Đưa lên Production bản đồ Cây xăng & Trạm sạc: hiển thị ảnh thực tế, giờ mở cửa, nút gọi điện thoại và chỉ đường bản đồ.
  - Đặt công cụ báo giá bảo hiểm ô tô trực tiếp trên trang chủ Vehicle Hub tạo điểm chạm dịch vụ ngay tại khối tiện ích.
  - Khôi phục hoạt động trang Phí không dừng (`/phi-khong-dung`) bình thường sau thời gian gián đoạn (Link Prod: [momo.vn/tien-ich-giao-thong/phi-khong-dung](https://www.momo.vn/tien-ich-giao-thong/phi-khong-dung)).
  - Triển khai menu điều hướng riêng cho từng dịch vụ: phạt nguội (đã chạy), bảo hiểm ô tô và xe máy (đang cấu hình).
  - Vận hành dữ liệu phạt nguội: cho phép quản lý khu vực, camera và từ điển phân loại lỗi vi phạm trên CMS.

**Báo cáo số liệu Vehicle Hub (MTD cùng kỳ từ Tháng 7 đến Tháng 10/2026 - Master SSOT):**

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
- **Phối hợp:**
  - Cell Team (VTTI) review và kiểm soát chất lượng (QC) đầy đủ bộ dữ liệu gara, hãng xe và mẫu xe.
  - VTTI review trang Nộp Phạt và cung cấp danh sách (listing) Trụ Sở Công An để xây dựng tính năng Tìm điểm nộp phạt (API tra cứu Phạt Nguội đã hoàn thiện kết nối độc lập).
- **Kế hoạch tuần tới:**
  - Xây dựng Tool Khấu Chi cho người sở hữu xe.
  - Hoàn thiện Mega Menu cho toàn bộ Vehicle Hub.
  - Triển khai mở rộng thêm các hãng xe và dòng xe mới.

---

### 4. Insurtech Hub

- **Kết quả nổi bật:**
  - Chuyển đổi toàn diện 13 trang bảo hiểm ô tô sang MoSpark CMS: gồm 3 trang chủ lực (Trang chủ, Thân vỏ, Bắt buộc TNDS) và 9 trang đối tác (PVI, GIC, MIC, PJICO, Bảo Long, Liberty, PTI, Bảo Việt, DBV) (Link Prod: [momo.vn/bao-hiem-o-to](https://www.momo.vn/bao-hiem-o-to) · Link Staging: [momo-stg.mservice.io/bao-hiem-o-to](https://momo-stg.mservice.io/bao-hiem-o-to)).
  - Bảo toàn 100% cấu trúc URL SEO, tiêu đề, mô tả và toàn bộ nội dung; giữ nguyên form báo giá hoạt động ổn định có lớp chống bot tự động.
  - Đóng gói widget bảo hiểm dùng chung: hỗ trợ nhúng widget mua bảo hiểm ô tô, y tế, xe máy vào bất kỳ trang nào trên Web. Widget ô tô đã live, widget y tế đã test xong chờ phát hành, widget xe máy đang lập phương án kỹ thuật.
  - Hoàn thiện Trang chủ Bảo hiểm mới (`momo.vn/bao-hiem`): gom 9 nhóm sản phẩm bảo hiểm theo phân mục rõ ràng, ưu tiên bảo hiểm y tế, xã hội và ô tô lên đầu, nhúng sẵn công cụ tra cứu BHYT trực tiếp (Link Prod: [momo.vn/bao-hiem](https://www.momo.vn/bao-hiem), đã hoàn thiện giao diện, chờ ngành hàng duyệt phát hành).
- **Phối hợp:**
  - Rà soát nội dung 13 trang bảo hiểm ô tô và layout trang chủ Bảo hiểm mới với bên ngành hàng.
  - Kiểm tra luồng gửi form báo giá bảo hiểm bảo đảm dữ liệu chuyển đổi thông suốt.
- **Kế hoạch tuần tới:**
  - Đưa Trang chủ Bảo hiểm mới (`/bao-hiem`) và công cụ tra cứu BHYT lên Production.
  - Hoàn thiện widget mua bảo hiểm xe máy để nhúng vào các trang liên quan.
  - Sửa 2 lỗi nội dung cũ trên trang đối tác PTI và PJICO theo phản hồi từ đối tác.

---

### 5. New User

- **Kết quả nổi bật:**
  - Bám sát mục tiêu 30.000 lượt tải app/tháng trong Q4/2026 và mục tiêu dài hạn Web đóng góp 30.000 - 50.000 user mới/tháng từ nguồn tự nhiên, giảm phụ thuộc vào quảng cáo trả phí.
  - Chạy thử trang tải app `/tai-app`: tự nhận diện thiết bị mobile để chuyển thẳng vào App Store / Google Play, còn desktop hiển thị mã QR cài đặt kèm hướng dẫn xử lý lỗi khi tải app (Link Staging: [momo-stg.mservice.io/tai-app](https://momo-stg.mservice.io/tai-app) · Link Prod: [momo.vn/tai-app](https://www.momo.vn/tai-app), đang thử nghiệm nội bộ).
  - Thiết lập hệ thống bóc tách riêng dữ liệu chuyển đổi Web-to-App giữa nguồn tự nhiên (Non-Paid) và quảng cáo (Paid Ads) để đánh giá đúng chất lượng tăng trưởng thực chất.
- **Phối hợp:**
  - Thống nhất các kịch bản test A/B tỷ lệ tải app với bên tăng trưởng người dùng mới.
  - Rà soát các chiến dịch Paid Ads và kiểm tra lại tracking chuyển đổi trên các trang đích.
- **Kế hoạch tuần tới:**
  - Nghiệm thu đo lường và kiểm thử trang `/tai-app` trên nhiều trình duyệt, sẵn sàng go-live chính thức.
  - Tối ưu nút chuyển đổi (CTA) sang app từ các mini game và công cụ tính toán.
  - Rà soát và tối ưu trang chiến dịch Bonbon chuẩn bị cho cao điểm cuối năm.

---

### 6. Lottery Hub

- **Kết quả nổi bật:**
  - Mảng Vietlott: chuyển bảng so sánh thể lệ 8 game sang dạng thẻ dọc dễ xem trên mobile, hiển thị hàng 6 bóng số co giãn linh hoạt, tích hợp tool dò vé tự động có tính thuế thu nhập cá nhân, thêm tiện ích tạo dãy số may mắn theo bản mệnh ngũ hành, ngày kỷ niệm hoặc ngẫu nhiên.
  - Keno và Bingo18: layout bảng kết quả hiển thị gọn 20 bóng vừa màn hình mobile, tóm tắt rõ chẵn/lẻ và lớn/nhỏ, bộ chọn kỳ quay nhanh.
  - Xổ số kiến thiết 3 miền: Miền Bắc hiển thị trọn vẹn 27 giải không cần cuộn ngang, Miền Nam/Trung có thanh trượt ngang; có 3 chế độ xem số (đầy đủ, 2 số cuối, 3 số cuối); tool dò vé tự động nhận diện quy cách từng miền; ma trận Lô tô 10x10 theo đầu - đuôi từ 00 đến 99; tự lọc đúng 41 đài phát hành theo ngày quay.
  - Tự động lấy kết quả mở thưởng từ trường quay và lưu tạm bộ nhớ đệm trên thiết bị giúp tra cứu tức thì.
- **Phối hợp:**
  - Ổn định luồng kết nối dữ liệu kết quả mở thưởng từ trường quay để giảm thiểu độ trễ.
  - Hoàn thiện nội dung cẩm nang cơ cấu giải thưởng và bảng minh họa khấu trừ thuế.
- **Kế hoạch tuần tới:**
  - Theo dõi độ ổn định của hệ thống cập nhật kết quả vào hai khung giờ quay cao điểm (16h30 và 18h00).
  - Đánh giá tỷ lệ người dùng tính năng dò vé tự động và bổ sung nút dẫn sang mua vé trên app MoMo.

---

### 7. Dịch vụ mới & Nạp game

- **Kết quả nổi bật:**
  - Hoàn thành giao diện landing page giới thiệu dịch vụ ChatGPT trên Web, có component Bảng giá mới trực quan hóa các gói dịch vụ và nút thanh toán nhanh.
  - Duy trì cổng nạp thẻ game chạy ổn định qua 4 nhà cung cấp, bảo đảm giao dịch thông suốt.
- **Phối hợp:**
  - Kiểm tra luồng thanh toán và cơ chế cấp tài khoản tự động với bên đối tác.
- **Kế hoạch tuần tới:**
  - Thu thập phản hồi người dùng để hoàn tất kịch bản thanh toán cho dịch vụ ChatGPT.
  - Tối ưu giao diện nạp thẻ game trên mobile để nâng tỷ lệ hoàn tất giao dịch.

---

## IV. NHÓM DỰ ÁN NỀN TẢNG (PLATFORM)

### 1. MoSpark Core & Hệ thống AI

- **Kết quả nổi bật:**
  - Hoàn thành 24 commits lớn (11 commits ở MoSpark CMS và 13 commits ở MoSpark Services), ban hành 6 bản cập nhật cơ sở dữ liệu.
  - Tái cấu trúc khu vực viết bài tự động sang mô hình MVVM 4 lớp độc lập: tách biệt dịch vụ dữ liệu, luồng xử lý, bộ lưu trữ trạng thái và giao diện; cô lập lỗi và kiểm soát chặt quy trình từ chọn chủ đề, duyệt dàn ý đến xuất bản.
  - Quản lý loại bài viết và hạn mức: thiết lập hạn mức xuất bản cho từng dự án, thêm thanh cảnh báo đánh giá dàn ý và giao diện duyệt dàn ý chuyên biệt (`ReviewOutlineDrawer`).
  - Kết nối AI đa mô hình: tích hợp mô hình LLM nội bộ MoMo song song với Google Gemini, Claude, OpenAI; chuyển sang cơ chế xác thực an toàn bằng Bearer JWT.
  - Tự động hiển thị cây tiêu đề bài viết (H1/H2/H3) và đưa trực tiếp vào prompt sinh nội dung của AI.
  - Xây dựng hệ thống adapter cắm rút linh hoạt (`cms-adapters/`) để xuất bản nội dung sang nhiều kênh (blog, landing page microsite, bên thứ ba). Sửa dứt điểm lỗi hiển thị thanh thông báo trên các hộp thoại.
- **Phối hợp:**
  - Kiểm thử mô hình AI nội bộ để từng bước thay thế các dịch vụ trả phí bên ngoài.
  - Chốt quy trình tạo và duyệt dàn ý bài viết tự động với bên nội dung.
- **Kế hoạch tuần tới:**
  - Đưa tính năng phân loại bài viết và giao diện duyệt dàn ý lên Production.
  - Triển khai các cổng xuất bản tự động ra trang chiến dịch và đối tác.

---

### 2. MoBase Design System

- **Kết quả nổi bật:**
  - Đưa thanh điều hướng nâng cao 2 tầng (Header Advance) lên chạy thực tế trên toàn bộ Financial Hub (`/tai-chinh`), hiển thị mượt mà trên cả mobile và desktop.
  - Chuẩn hóa cấu hình Header và Footer trên MoSpark, bảo đảm chuyển đổi linh hoạt giữa menu thường và menu nâng cao.
  - Phát triển component Bảng giá dùng chung cho các trang dịch vụ số.
- **Phối hợp:**
  - Thống nhất quy chuẩn hiển thị trên các kích cỡ màn hình với bên thiết kế.
  - Chuẩn bị kế hoạch áp dụng menu mới cho các Hub tiếp theo.
- **Kế hoạch tuần tới:**
  - Mở rộng thanh điều hướng 2 tầng sang Cinema Hub và Vehicle Hub.
  - Đóng gói tài liệu hướng dẫn sử dụng và component mới trong bản phát hành MoBase tiếp theo.

---

### 3. CMS & Trình soạn thảo

- **Kết quả nổi bật:**
  - Tối ưu tốc độ tải và bộ nhớ đệm trên MoSpark CMS (cơ chế loop render), giảm độ trễ khi thao tác và biên tập danh mục nội dung lớn.
  - Quản trị bài viết in-app: kiểm soát quyền truy cập, hiển thị rõ thông tin 4 cấp phê duyệt (Người yêu cầu, Nội dung, Thiết kế, Pháp lý) ngay trên giao diện xem bài viết; giữ nguyên màn hình hiện tại sau khi tải bài lên thành công.
  - Sửa lỗi tìm kiếm bài viết hướng dẫn; tinh gọn còn đúng 2 danh mục chuẩn (Nhóm hướng dẫn & Bài hướng dẫn); chỉ gợi ý các bài đã xuất bản chính thức.
  - Thêm tính năng đọc bài trực tiếp trong cửa sổ modal tại khối blog, giúp người dùng xem nhanh mà không phải chuyển trang, giảm tỷ lệ thoát trang.
- **Phối hợp:**
  - Thống nhất quy chuẩn hiển thị thông tin duyệt bài với bên pháp lý và kiểm duyệt nội dung.
  - Hướng dẫn đội ngũ biên tập áp dụng quy trình soạn thảo mới.
- **Kế hoạch tuần tới:**
  - Theo dõi phản hồi về hiệu năng nạp trang của hệ thống quản trị sau đợt nâng cấp.
  - Rà soát và chuyển đổi toàn bộ bài viết hướng dẫn cũ về đúng 2 danh mục chuẩn.

---

### 4. Tìm kiếm Website (`/tim-kiem`)

- **Kết quả nổi bật:**
  - Chính thức go-live Giai đoạn 1 (Phase 1) của trang Tìm kiếm Website (`/tim-kiem`) trên Production (Link Prod: [momo.vn/tim-kiem](https://www.momo.vn/tim-kiem)).
  - Vận hành đầy đủ các cấu phần: thanh tìm kiếm nhanh tức thì, danh sách từ khóa xu hướng (trending keywords), gợi ý tìm kiếm phổ biến và giao diện xử lý thông minh khi không có kết quả.
- **Phối hợp:**
  - Kết nối và duy trì ổn định nguồn dữ liệu từ khóa xu hướng theo thời gian thực.
- **Kế hoạch tuần tới:**
  - Theo dõi hiệu năng, tỷ lệ tương tác (CTR) và hành vi tìm kiếm thực tế của người dùng sau khi go-live.
  - Cấu hình ưu tiên hiển thị các trang công cụ tiện ích và bài viết chuyên sâu lên đầu kết quả tìm kiếm.

---

### 5. Dữ liệu & Tự động hóa vận hành

- **Kết quả nổi bật:**
  - Vận hành cơ chế đồng bộ dữ liệu báo cáo tự động Cloud-to-Cloud lên bảng quản trị tập trung trong 1-2 giây, tự lưu lịch sử các phiên bản.
  - Tự động hóa bóc tách số liệu Paid Ads theo từng kênh phân phối, chiến dịch và tỷ lệ chuyển đổi Web-to-App để kiểm soát chất lượng tăng trưởng tự nhiên.
  - Quét Search Console kiểm toán danh sách các trang không có lượt hiển thị (zero-impression audit) để lên phương án phục hồi chỉ mục.
  - Cập nhật bộ quy tắc phân loại URL và chuẩn hóa bảng DIM: nhận diện chính xác 100% dữ liệu GA4 MTD và Google Search Console, xóa sạch tình trạng trang rơi vào nhóm Chưa phân loại (Others).
  - Hợp nhất và chuẩn hóa ma trận phân bổ 73 dự án thành phần vào 15 Hubs trên dashboard quản trị.
- **Phối hợp:**
  - Thống nhất định nghĩa phân loại nguồn truy cập và quy chuẩn đặt tên chiến dịch với bên dữ liệu và bên truyền thông.
- **Kế hoạch tuần tới:**
  - Xử lý các trang web trong nhóm không có lượt hiển thị (bổ sung liên kết nội bộ, tối ưu lại thẻ tiêu đề hoặc chuyển hướng).
  - Tự động hóa cơ chế gửi cảnh báo khi phát sinh biến động bất thường về tỷ lệ chuyển đổi Web-to-App.

---

## V. TỔNG HỢP PHỐI HỢP CẦN XỬ LÝ

**Với các nhóm ngành hàng / dịch vụ:**
- Phim ảnh: Chốt cơ chế trả thưởng voucher rạp từ mini game; ra mắt mini game phim *Bò Sữa Bay*.
- Tài chính (Finhub & BU Bank): BU Bank review UI/UX trang chi tiết ngân hàng (Bank Detail); Finhub triển khai hoạt động truyền thông (Comm), kiểm soát chất lượng (QC) công cụ Chứng Chỉ Quỹ và cung cấp API các Quỹ mở.
- Giao thông (VTTI Cell Team): Review và QC đầy đủ bộ dữ liệu hãng xe, gara; review trang Nộp Phạt và cung cấp danh sách (listing) Trụ Sở Công An để làm tính năng Tìm điểm nộp phạt (API tra cứu Phạt Nguội đã hoàn thiện).
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
- Xử lý danh sách các trang web không có lượt hiển thị từ Search Console (thêm link nội bộ, sửa tiêu đề, chuyển hướng).
- Mở rộng thanh điều hướng 2 tầng sang Cinema Hub và Vehicle Hub.
- Triển khai các cổng xuất bản tự động của MoSpark ra trang chiến dịch và đối tác.
- Theo dõi hiệu năng, tỷ lệ tương tác và tối ưu thứ tự hiển thị tiện ích/bài viết trên trang tìm kiếm (`/tim-kiem`) sau đợt go-live Phase 1.
- Theo dõi phản hồi về tốc độ của trang quản trị CMS sau khi tối ưu cơ chế nạp trang.
- Tự động hóa cảnh báo khi tỷ lệ chuyển đổi sang app bị sụt giảm bất thường.
- Chuyển nốt các bài viết hướng dẫn cũ về đúng 2 danh mục chuẩn.
- Đóng gói tài liệu hướng dẫn và component Bảng giá trong bản phát hành MoBase tiếp theo.
