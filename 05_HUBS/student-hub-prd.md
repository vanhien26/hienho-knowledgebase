# MoMo Student Hub - Product Requirements Document (PRD)

## I. DOCUMENT CONTROL & EXECUTIVE SUMMARY

### 1.1 Document Overview
* **Product Name:** MoMo Student Hub (Discovery Platform & Unified Student Gateway)
* **Target Platform:** Web Platform (`momo.vn/sinh-vien` - Unauthenticated Public Web Platform for SEO, AEO & Discovery). Hệ thống triển khai tập trung trên Web, không có trang Hub riêng trong App MoMo.
* **Document Version:** v1.0 Final (Production Ready - Strategic Alignment Version)
* **Product Ownership:** MoMo Web Platform & Student Acquisition Team
* **Platform Positioning:** Standing Platform vận hành dài hạn quanh năm, chuyển đổi từ trang Landing Page tĩnh "Student Pass" (lỗi thời từ 2024) thành **Hệ sinh thái Sản phẩm Product-Led Growth (PLG)** dành riêng cho Gen Z (lớp 12, tân sinh viên & sinh viên).

### 1.2 Strategic Context & Product Big Idea
* **Bối cảnh Chuyển đổi Chiến lược (Recap Alignment):** Thay thế Landing Page tĩnh "Student Pass" cũ kỹ từ năm 2024 thành một Hệ sinh thái Sản phẩm công nghệ dài hạn. Mục tiêu cốt lõi là dùng tiện ích thực tế thu hút lượng truy cập tự nhiên (Growth Hacking), giữ chân sinh viên và lồng ghép dịch vụ MoMo.
* **Product Vision:** Student Hub đóng vai trò là **lớp nội dung + điều hướng hợp nhất (Unified Content & Navigation Gateway)** cho toàn bộ tệp người dùng HSSV trên Web MoMo. Hệ thống kết nối từ thông tin trường học, kinh nghiệm sống xa nhà cho đến các dịch vụ tài chính sinh viên.
* **Big Idea Sản Phẩm:** *"Lần đầu tự lập, không phải tự lo"* - MoMo đồng hành cùng người trẻ qua từng cột mốc tài chính và học tập đầu đời.
* **Kiến trúc Không Authen trên Web & Chuyển Tiếp OneLink:**
  * Trang Web `momo.vn/sinh-vien` vận hành không yêu cầu đăng nhập (Unauthenticated Discovery).
  * Mọi nút bấm tương tác cá nhân hóa (Nộp học phí, Xác thực Thẻ Sinh Viên Số, Mở Ví Trả Sau, Vay Nhanh) sử dụng **OneLink điều hướng thẳng sang các màn hình/mini-app tương ứng sẵn có trong App MoMo**.

---

## II. 4 CORE STRATEGIC PILLARS (CHƯƠNG TRÌNH TRỌNG TÂM)

### 2.1 Trụ Cột 1: Xây Dựng Cổng Thông Tin Đại Học (Data & pSEO Engine)
* **File Dữ Liệu Đầu Vào Chính Thức (Official Data Matrix Input):** Toàn bộ cấu trúc nội dung 11 Section, Schema dữ liệu ngành học, học bổng, cổng đăng ký tín chỉ và bộ dữ liệu thực tế của 05 trường đại học thí điểm Phase 1 (UEH, FTU, TDTU, HCMUT, VLU) được đối soát và kế thừa trực tiếp từ file dữ liệu chuẩn: `/Users/hienhv/Downloads/Content Structure.xlsx`.
* **Thí điểm 05 Trường Đại học Trọng điểm Phase 1:** Bách Khoa TP.HCM (HCMUT), Kinh tế TP.HCM (UEH), Văn Lang (VLU), Ngoại thương (FTU), Tôn Đức Thắng (TDTU).
* **Cấu trúc Dữ liệu Chuẩn hóa (Schema Markup):** Thu thập và xác thực trực tiếp từ website chính thức của các trường ĐH:
  * Điểm chuẩn xét tuyển các năm (`22.8 - 27.7`).
  * Quy chế tuyển sinh & các phương thức xét tuyển.
  * Chi tiết ngành học, môn học tiêu biểu, lộ trình học theo học kỳ, chuẩn đầu ra & mức lương tốt nghiệp.
  * Điều kiện & giá trị các suất học bổng.
* **Ma trận Nội dung theo Search Volume (Google Trends VN 12 tháng):** Sắp xếp ưu tiên hiển thị nội dung theo nhu cầu tìm kiếm thực tế của sinh viên (Điểm chuẩn, Học phí, Xe buýt, Việc làm sinh viên).

### 2.2 Trụ Cột 2: Phát Triển Hệ Sinh Thái Tiện Ích (Utility Tools Ecosystem)
Tích hợp các công cụ giải quyết trực tiếp "nỗi đau" hàng ngày của sinh viên:
1. **Công cụ Tài chính Cá nhân (Tuition & Budget Calculator):**
   * *Utility Tính Học Phí Theo Tín Chỉ:* Công cụ giả lập tính tổng tiền học phí theo số lượng tín chỉ sinh viên chọn (12 - 30 tín chỉ), phân rã chi tiết học phí và kích hoạt CTA *"Nộp học phí ngay"* dẫn qua OneLink sang phễu thanh toán In-App.
   * *Công cụ Quản lý Ngân sách / Thu nhập:* Giúp sinh viên tính toán tiền sinh hoạt hàng tháng, điều hướng mở **Túi Thần Tài** (tích lũy sinh lời) hoặc **Ví Trả Sau 0%** (chi tiêu thiết bị học tập).
2. **Bản đồ Tiện ích Vị trí (Location-Based Amenities Map 5km):**
   * Bản đồ tương tác hiển thị Nhà trọ, Quán ăn, Cà phê, Xe buýt, Siêu thị quanh campus (phân rã *Bên trong Campus* & *Bên ngoài Campus* bán kính 500m, 1km, 2km, 5km).
   * **Ưu tiên hiển thị cửa hàng SME chấp nhận thanh toán MoMo** kèm mã giảm giá O2O.
   * Tích hợp API Tuyến xe buýt (Google Transit API & dữ liệu GTFS miễn phí từ Sở GTVT).
3. **Cổng Việc Làm & Thực Tập (Jobs & Internship Gateway):**
   * Kết nối sinh viên tìm việc làm part-time / thực tập (hiển thị mức lương, địa điểm, đánh giá, CTA Ứng tuyển).
   * Xử lý "nỗi đau" thiếu hụt nhân sự của các chuỗi nhà hàng, F&B, siêu thị đối tác thương mại của MoMo.
4. **Hệ thống Đánh giá UGC & Sự kiện (Review & Event Meetup Module):**
   * Đồng bộ API luồng đánh giá trường học 5 sao đa tiêu chí từ trong App ra ngoài Web.
   * Phân hệ xem & đăng ký tham gia Webinar, AI talk, Workshop kỹ năng sinh viên (mô hình Meetup).

### 2.3 Trụ Cột 3: Số Hóa Chương Trình Đại Sứ Sinh Viên (Productized Ambassador Engine)
* **Sản phẩm hóa Ambassador (Tech-Enabled Ambassador System):** Chuyển đổi chiến dịch Social thủ công (TikTok, Threads) của 50 đại sứ hàng năm thành một **sản phẩm công nghệ độc lập**.
* **Tính năng Hệ thống Ambassador:**
  * Giao nhiệm vụ tự động (Daily/Weekly Quests).
  * Tích lũy điểm thưởng & Bảng xếp hạng Leaderboard.
  * Quản lý quyền lợi đại sứ: Mentorship 1-on-1, Workshop kỹ năng, Chứng nhận CV chính thức.
* **Tầm nhìn Mở rộng (Scale Roadmap):** Xây dựng hệ thống vững chắc để scale quy mô toàn quốc, kết nối trực tiếp nguồn nhân lực đại sứ sinh viên chất lượng cao vào chương trình **MoMo Talent Pipeline**.

### 2.4 Trụ Cột 4: Hành Động Thực Thi Ngắn Hạn (Landing Page Revamp & CMS Governance)
* **Xử lý Nội dung Lỗi thời:** Quét dọn và thay mới toàn bộ hình ảnh, video, voucher, CTAs cũ kỹ từ năm 2024 để chuẩn bị cho mùa Back to School.
* **Tối ưu UI/UX Mobile Webview:** Khắc phục triệt để lỗi font chữ quá nhỏ, hình ảnh bị vỡ/lệch khung hình khi hiển thị trên di động.
* **Bàn giao CMS Tự Chủ (MoSpark CMS / MS Park):** Thiết lập và bàn giao công cụ CMS cho đội ngũ Vận hành (Ops) tự chỉnh sửa nội dung, bật/tắt các khối UI Block trên Web mà không phụ thuộc vào lập trình viên.

---

## III. TARGET AUDIENCE & USER PERSONAS

### 3.1 Target User Base
* **Quy mô tệp sinh viên:** ~1,49 triệu sinh viên đại học/cao đẳng trên toàn quốc (~612.000 sinh viên đã xác thực trên App MoMo, chiếm ~41% thị phần).
* **Mục tiêu mở rộng:** Tiếp cận 100% tệp tân sinh viên nhập học hàng năm qua kênh Google Organic Search & mạng xã hội.

### 3.2 Core User Personas
| Persona | Mô tả & Nhu cầu Đặc thù | Touchpoint Ưu tiên trên Hub |
| :--- | :--- | :--- |
| **Tân Sinh Viên (Freshmen)** | Mới lên thành phố, lo lắng về chọn trường, học phí, an toàn phòng trọ, phương tiện đi lại (xe buýt), chưa có kinh nghiệm quản lý chi tiêu. | Hero Section Trường học, Bản đồ Tiện ích quanh trường 5km, FAQs Nhập học, Thẻ Sinh Viên Số. |
| **Sinh Viên Đang Học (Sophomores/Seniors)** | Nhu cầu nộp học phí hàng kỳ, tìm kiếm ưu đãi ăn uống, gia hạn Data 4G/5G, đăng ký công cụ AI (Gemini Student Offer), làm thêm & vay tiêu dùng ngắn hạn. | Utility Tính Học Phí Theo Tín Chỉ, Service Grid Icon, Top Ưu đãi Sinh viên, Cổng Việc làm Part-time. |
| **Phụ Huynh (Parents)** | Muốn tra cứu độ uy tín của trường, minh bạch mức học phí trung bình, tìm hiểu môi trường sống an toàn cho con xa nhà. | Thang điểm đánh giá uy tín (Parent Rating ⭐), Thông tin NAP, Bảng Học phí & Ngành học. |

---

## IV. MASTER SITE STRUCTURE & URL HIERARCHY

### 4.1 Master Site Structure (`/sinh-vien`)
Cấu trúc đường dẫn URL chuẩn phân cấp Subdirectory phân rã từ gốc `/sinh-vien`:

```
momo.vn/sinh-vien (Trang chủ Student Hub / Discovery Hub)
└── /sinh-vien/[ten-truong-ma-truong] (Trang chi tiết Trường ĐH - Ví dụ: /sinh-vien/ton-duc-thang-tdtu)
    ├── /sinh-vien/[ten-truong-ma-truong]/nha-tro (Trang danh sách & chi tiết Nhà trọ / KTX an toàn gần trường)
    ├── /sinh-vien/[ten-truong-ma-truong]/ambassador (Trang Đại sứ Sinh viên MoMo & Tuyển dụng Campus Ambassador)
    ├── /sinh-vien/[ten-truong-ma-truong]/workshop (Trang sự kiện, Webinar & Workshop kỹ năng/AI sinh viên)
    ├── /sinh-vien/[ten-truong-ma-truong]/review (Trang tổng hợp bài đánh giá Review & Rating UGC chi tiết)
    └── ?campus=[campus-id] (Bộ lọc xem bài Review & Địa điểm theo mã cơ sở chi nhánh)
```

### 4.2 URL Routing Matrix
| URL Pattern | Tên Loại Trang (Page Type) | Chức năng Chính & Trải nghiệm UX | Primary CTA (OneLink Web-to-App) |
| :--- | :--- | :--- | :--- |
| `momo.vn/sinh-vien` | **Hub Homepage** | Tổng quan Thẻ Sinh Viên Số, Banner ưu đãi hot, Widget Bạn đồng hành MoMo, Top Review Trường. | *Xác thực ngay / Nhận đặc quyền* |
| `momo.vn/sinh-vien/[ten-truong-ma-truong]` | **School Landing Page** | Trang trường chuyên biệt (VD: `/sinh-vien/ton-duc-thang-tdtu`), thông tin học phí, môi trường học, review tổng quan. | *Review ngay (Mở App)* |
| `momo.vn/sinh-vien/[ten-truong-ma-truong]/nha-tro` | **Sub-page Nhà trọ & KTX** | Danh sách phòng trọ an toàn, giá thuê KTX, bản đồ khoảng cách tới cơ sở trường ĐH. | *Xem nhà trọ / Tính tiền trọ* |
| `momo.vn/sinh-vien/[ten-truong-ma-truong]/ambassador` | **Sub-page Đại sứ Sinh viên (Ambassador)** | Chương trình tuyển dụng & hoạt động của Campus Ambassadors MoMo tại trường ĐH, cơ hội việc làm & đặc quyền thủ lĩnh. | *Đăng ký làm Ambassador* |
| `momo.vn/sinh-vien/[ten-truong-ma-truong]/workshop` | **Sub-page Workshop & Event** | Chuỗi bài viết & đăng ký tham gia Webinar "Career & AI Talk", sự kiện CLB trường ĐH. | *Đăng ký tham gia Workshop* |
| `momo.vn/sinh-vien/[ten-truong-ma-truong]/review` | **Sub-page Review UGC Chi Tiết** | Bài viết đánh giá 5 sao góc nhìn sinh viên thực tế theo từng cơ sở (Campus A, B, N). | *Viết Review (Mở App)* |

---

## V. DETAILED FEATURE SPECIFICATIONS & UI BLUEPRINT (FROM LIVE PROTOTYPE)

### 5.1 Top Strip & Site Navigation Bar
* **Top Announcement Strip:** Hiển thị thông báo khuyến mãi nổi bật: *"CHÀO MỪNG TÂN SINH VIÊN 2026 - MỞ THẺ SINH VIÊN SỐ NHẬN GÓI QUÀ 500K"*.
* **Header Components:**
  * Logo MoMo Student Hub + Dropdown danh sách trường ĐH (`nav-univ-dropdown`).
  * Khung tìm kiếm thông minh (`nav-search-inp`): Tìm kiếm trường ĐH, nhà trọ, ngành học.
  * **Kiến trúc Web:** Hệ thống Web `momo.vn/sinh-vien` vận hành không yêu cầu tài khoản đăng nhập hay xác thực (Unauthenticated Web Gateway). Người dùng truy cập nội dung tự do; các hành động cá nhân hóa hoặc giao dịch được điều hướng trực tiếp bằng OneLink sang màn hình/mini-app tính năng tương ứng trong App MoMo.

### 5.2 School Detail Hero Section (Airbnb-Style Layout)
Thiết kế theo bố cục Airbnb Mosaic hiện đại, tối ưu hiển thị thông tin trường học:
1. **Hero Header:**
   * Tên chính thức của trường ĐH kèm **dấu tick xác thực `✓`** đặt ngay bên cạnh tên trường.
   * Thông tin NAP (Name: Trường ĐH Tôn Đức Thắng, Address: 19 Nguyễn Hữu Thọ, Q.7, TP.HCM, Phone).
   * Thang điểm đánh giá uy tín (4.8★ Parent & Student Rating).
   * Chỉ số thống kê nhanh: Điểm chuẩn (`22.8 - 27.7`), Học phí TB (`30 - 60tr/năm`), Tỷ lệ có việc làm (`98.2%`).
2. **Campus Switcher Bar (Thanh Lọc Cơ Sở Chi Nhánh):**
   * Bộ lọc Tab chọn lọc theo từng chi nhánh cụ thể: `[Tất Cả Cơ Sở] | [Cơ Sở Tân Phong (Q7)] | [Cơ Sở Bảo Lộc] | [Cơ Sở Nha Trang]`.
   * Khi người dùng bấm chọn cơ sở, toàn bộ địa chỉ GPS, danh sách trọ và cửa hàng ăn uống sẽ tự động cập nhật theo cơ sở đó.
3. **Photo Mosaic Gallery:** Lưới hình ảnh khuôn viên trường, cơ sở vật chất, thư viện, canteen.
4. **Primary CTA:** Nút *"Đánh giá trường này"* kích hoạt OneLink mở phễu đánh giá trong App MoMo.

### 5.3 Service Icon Grid (6 Micro-Features)
Lưới 6 icon điều hướng 1-touch truy cập nhanh các dịch vụ trọng tâm:
1. **Đóng học phí:** Tra cứu mã sinh viên & thanh toán học phí trực tuyến.
2. **Đăng ký tín chỉ:** Mẹo săn tín chỉ & nhắc lịch nộp tiền tín chỉ.
3. **Vay nhanh:** Giả lập khoản vay tiêu dùng sinh viên (10M - 100M) lãi suất ưu đãi.
4. **Ví Trả Sau 0%:** Mở hạn mức tín dụng sinh viên mua sắm thiết bị học tập.
5. **Túi Thần Tài:** Tích lũy sinh lời hàng ngày cho tiền chi tiêu sinh viên.
6. **Student Pass:** Xác thực Thẻ Sinh Viên Số nhận đặc quyền.

### 5.4 Interactive Nearby Merchant Discovery Widget (Bản Đồ Cửa Hàng & Tuyến Xe Buýt 5km)
* **Bản đồ tương tác (Leaflet / Google Maps API):** Tích hợp bản đồ GPS quanh cơ sở trường ĐH.
* **Bộ lọc vị trí (Radius Filter):**
  * `Bên trong Campus` (Canteen, Tiệm photocopy, Máy bán nước tự động).
  * `Bên ngoài Campus` với bán kính tùy chọn: `500m | 1km | 2km | 5km`.
* **Danh mục địa điểm:** Ưu tiên hiển thị các cửa hàng SME chấp nhận MoMo (Nhà trọ & KTX, Quán ăn, Trà sữa, Xe buýt, Siêu thị, Trung tâm Tiếng Anh).
* **Tích hợp API Tuyến Xe Buýt (Public Transit Bus API):**
  * Hiển thị danh sách tuyến bus đi qua trường (VD: tuyến **139, 34, 38, 56...**), thời gian di chuyển (36 phút), trạm đón/trả và giá vé ước tính (6.000đ).
  * **Chiến lược Tối ưu Chi phí 0 VNĐ:** Phase 1 import dữ liệu GTFS miễn phí từ Sở GTVT vào Database nội bộ MoMo; Phase 2 mở rộng Google Maps Transit API với lớp Caching 24h.

### 5.5 Interactive Credit-Based Tuition Calculator (Utility Tính Học Phí Theo Tín Chỉ)
* **Thanh trượt tín chỉ linh hoạt (Credit Slider):** Sinh viên kéo chọn số lượng tín chỉ muốn học trong học kỳ (từ 12 đến 30 tín chỉ).
* **Bảng phân rã chi phí dự kiến:** Tự động tính tổng tiền học phí (`~12.600.000đ`), chi phí cơ sở vật chất và bảo hiểm.
* **CTA Chuyển đổi trực tiếp:** Nút *"Nộp học phí ngay"* dẫn dắt trực tiếp qua OneLink sang phễu Nộp học phí In-App.
* **Khối thông tin Học bổng:** Hiển thị danh sách học bổng của trường (Học bổng Xuất sắc 23.4 triệu, Học bổng Toàn phần 15.6 triệu) kèm điều kiện xét tuyển.

### 5.6 Cổng Việc Làm & Thực Tập (Jobs & Internship Board)
* Hiển thị danh sách vị trí việc làm part-time và thực tập sinh từ các chuỗi F&B, siêu thị, cửa hàng đối tác của MoMo.
* Thông tin minh bạch: Mức lương theo giờ/tháng, địa điểm làm việc, đánh giá môi trường làm việc, nút CTA *"Ứng tuyển ngay"*.

### 5.7 Student Pass Digital Card Verification Flow
* **Quy trình xác thực 100% In-App (kích hoạt qua OneLink):**
  1. Nhập Họ tên & Mã số sinh viên (MSSV).
  2. Tải ảnh Thẻ sinh viên / Giấy xác nhận nhập học hoặc xác thực VNeID.
  3. Hệ thống AI OCR tự động đối soát trong 3 giây.
* **Hiển thị Thẻ Sinh Viên Số (Visual Digital Pass):**
  * Thẻ ảo thiết kế hiệu ứng kim loại sang trọng kèm MoMo Chip, mã Barcode và thông tin sinh viên.
  * Mở khóa chuỗi đặc quyền: Giảm 50% xem phim, Hoàn 10% vé xe buýt/Grab, Gói Data 4G giá rẻ.

### 5.8 Octalysis Gamification & Daily Quests (Thử Thách Hàng Ngày)
* **Daily Login Streak:** Điểm danh ngọn lửa Streak nhận Xu thưởng MoMo.
* **Cửa hàng Đổi Quà (Coins Reward Shop):** Đổi Xu lấy voucher ăn uống, vé xem phim, Data 4G.
* **Thử thách Sinh viên:** *"Xác thực thẻ SV"*, *"Thanh toán 1 đơn hàng quanh trường"*, *"Viết review trường"*.

### 5.9 Multi-Campus Review & Rating Module (Đánh Giá 5 Sao Multi-Campus)
* **Phân rã 5 tiêu chí đánh giá:**
  1. Khuôn viên & Cảnh quan trường ⭐⭐⭐⭐⭐
  2. Thư viện & Thiết bị học tập ⭐⭐⭐⭐⭐
  3. Canteen & Giá cả ăn uống ⭐⭐⭐⭐☆
  4. An ninh & Bãi đỗ xe ⭐⭐⭐⭐⭐
  5. Khoảng cách Trọ / KTX ⭐⭐⭐⭐☆
* **Bài viết Review UGC từ sinh viên thật:** Hiển thị bài viết gắn nhãn Gen Z (*"Peak vi-ci-eo"*, *"Tinh hoa hội tụ"*...).

### 5.10 Student Privileges & AI Tools
* Gợi ý gói **Google Gemini Student Offer**, voucher mua Laptop sinh viên, ưu đãi Data 4G/5G.
* Khối câu hỏi thường gặp **FAQs Sinh Viên** (Học vụ: *Nợ môn, Rớt môn, Điểm rèn luyện, Đăng ký tín chỉ, Thẻ SV*).

---

## VI. CONTENT STRATEGY & SEARCH INTENT PRIORITY MATRIX

### 6.1 41-Keyword Search Intent Prioritization (From Content Plan PDF)
Nội dung hiển thị trên Hub được sắp xếp thứ tự ưu tiên dựa trên nghiên cứu 41 từ khóa đại diện (Google Trends VN 12 tháng + traffic nền tảng):
* **Nhóm Mức Độ Quan Tâm Rất Cao (70-100):** Điểm chuẩn đại học, du học, văn bằng 2, trung tâm tiếng Anh, giải trí $
ightarrow$ *Ưu tiên đặt tại vị trí đầu trang.*
* **Nhóm Mức Độ Quan Tâm Cao (40-69):** Tuyến xe buýt, quán ăn, siêu thị, học phí đại học, ngành đào tạo, việc làm sinh viên.
* **Nhóm Mức Độ Quan Tâm Trung Bình (20-39):** Đăng ký tín chỉ, thực tập sinh viên, nhà trọ, quán cà phê.
* **Nguyên tắc Lồng ghép Sản phẩm MoMo:** Các từ khóa tính năng sản phẩm (*Đóng học phí, Ví trả sau, Vay sinh viên*) dù có lượt tìm kiếm tự nhiên thấp vẫn được **giữ lại và lồng ghép nổi bật** dưới dạng Grid Icon Dịch Vụ.

### 6.2 4 Core Content Pillars
1. **Cách chi tiêu cho sinh viên:** Kỹ năng quản lý tài chính cá nhân, "1 ngày sinh viên tiêu bao nhiêu", "Sống ổn với 3 triệu/tháng".
2. **Những điều cần biết khi xa nhà:** An toàn thuê trọ, cảnh báo lừa đảo phòng trọ/việc làm/đa cấp, thủ tục nhập học.
3. **Kỹ năng sống & AI:** Phương pháp học tập hiệu quả, ứng dụng AI trong học tập/việc làm, chuỗi **Webinar "Career & AI Talk"** đồng hành cùng diễn giả kinh nghiệm.
4. **Giải trí & Review Trường học:** Review "bóc trần" trường ĐH theo cơ sở, Video ngắn, Study With Me, giải trí Gen Z.

---

## VII. TECHNICAL ARCHITECTURE, ANALYTICS & CMS GOVERNANCE

### 7.1 Analytics & Attribution Tech Stack
* **Umami Analytics (Web Behavior Tracking):** Đo lường 100% hành vi trên Web (`momo.vn/sinh-vien`): lượt xem trang (Pageviews), luồng chuyển dịch (User Flow), độ sâu cuộn (Scroll Depth), click CTA, tương tác công cụ tính học phí và xem bài review.
* **OneLink / AppsFlyer (Web-to-App Attribution):** Xử lý luồng chuyển tiếp từ Web sang App MoMo, đo lường tỷ lệ Open App, Install App và Attribution lượt xác thực Thẻ Sinh Viên Số & giao dịch In-App.

### 7.2 CMS Governance (MoSpark CMS / MS Park)
* Bàn giao công cụ **MoSpark CMS** cho đội ngũ Operations (Vận hành):
  * Tự do quản lý bài viết, tạo mới trang trường học theo mẫu chuẩn pSEO Schema.
  * Chủ động bật/tắt các khối UI Block (Banner, Grid Icon, Widget Cửa hàng gần đây, Khối Việc làm) mà không cần can thiệp lập trình viên.

### 7.3 Regulatory Compliance & Risk Governance
* **Tuân thủ quy định NHNN (Thông tư 23 & 40/2024/TT-NHNN):** Mọi giao dịch tài chính, hoàn tiền, giải ngân Ví Trả Sau **100% thực hiện trong App MoMo đã KYC**. Web Platform (`momo.vn/sinh-vien`) đóng vai trò là kênh hiển thị nội dung công khai và điều hướng về App qua OneLink.
* **Quy Chuẩn Kỹ Thuật & Kiến Trúc API Xe Buýt 0 VNĐ (Public Transit GTFS & PostGIS Spec):**
  * **Phase 1 (MVP - Chi phí 0 VNĐ & Tốc độ < 50ms):**
    * Import dữ liệu chuẩn mở GTFS (`routes.txt`, `stops.txt`, `stop_times.txt`) từ Sở GTVT TP.HCM (`ebus.buyttphcm.com.vn`) & Hà Nội (`timbus.vn`) vào Database nội bộ MoMo (`PostgreSQL` + `PostGIS`).
    * Sử dụng truy vấn không gian PostGIS `ST_DWithin` để quét chính xác các trạm bus và tuyến bus chủ lực trong bán kính 500m - 1km quanh tọa độ GPS của từng cơ sở trường ĐH với **tốc độ phản hồi < 50ms và chi phí API 0 VNĐ**.
  * **Tích hợp Direct REST API Endpoints Nhà Nước:**
    * API Danh sách tuyến TP.HCM: `GET http://ebus.buyttphcm.com.vn/api/Route/GetAll`
    * API Trạm dừng theo tuyến: `GET http://ebus.buyttphcm.com.vn/api/Route/GetRouteDetail?routeId={route_id}`
    * API Trạm dừng quanh tọa độ: `GET http://ebus.buyttphcm.com.vn/api/Stop/GetStopsByBound`
    * AJAX Endpoints từ `timbus.vn` (Hà Nội).
  * **Phase 2 (Real-time Tracking & Dynamic Walking Directions):**
    * Tích hợp Google Maps Transit Directions API với lớp **Redis Cache 24h** tận dụng $200 credit miễn phí hàng tháng của Google Cloud giúp tiết kiệm 99% chi phí API phát sinh.
* **Hiệu năng kỹ thuật:** Thiết kế chuẩn **Mobile-First**, tốc độ tải trang dưới 1,5 giây.
