# MOMO WEB PLATFORM — KNOWLEDGE BASE & TECH OPERATING SYSTEM

> Hệ thống Tri thức Single Source of Truth (SSOT) và Bộ công cụ Tự động hóa Kỹ thuật dành cho **SEO / GEO & Product Lead** phục vụ toàn bộ chiến lược tăng trưởng, tối ưu hóa công cụ tìm kiếm thế hệ mới và phễu chuyển đổi Web-to-App của Kênh Web MoMo (`momo.vn`).

---

## 1. TỔNG QUAN HỆ ĐIỀU HÀNH KỸ THUẬT

Kho lưu trữ này không phải là một tập tài liệu lưu trữ tĩnh, mà là **Hệ điều hành tri thức (Knowledge OS)** tích hợp trực tiếp giữa tư duy Quản trị Sản phẩm hướng tăng trưởng (Product-Led Growth) và Năng lực Kỹ thuật SEO / Generative Engine Optimization (GEO) chuyên sâu.

Hệ thống được thiết kế để giải quyết 3 bài toán cốt lõi:
1. **SEO to GEO Transformation:** Chuyển đổi cấu trúc thông tin từ SEO từ khóa truyền thống sang Semantic Topic Clustering, Direct Answers, Knowledge Graph và tối ưu hóa hiện diện trên các công cụ tìm kiếm AI (Google AI Overviews, Bing Copilot, Perplexity).
2. **Market Intelligence & Seasonality:** Tự động hóa phân tích dữ liệu thị trường từ hơn 3.7 triệu lượt tìm kiếm hàng tháng, giải mã chu kỳ mùa vụ 5 năm từ Google Trends để quy hoạch nội dung đón đầu nhu cầu người dùng.
3. **Product-Led Growth & Web-to-App Funnel:** Xây dựng các tiện ích công cộng tương tác cao (Utilities, Calculators, Lookups), áp dụng cơ chế Zero-Gate và 0-CAPTCHA để thu hút lưu lượng tự nhiên (Organic Traffic) và chuyển đổi thành người dùng Mobile App thông qua phễu đo lường bảo mật Zero-PII.

---

## 2. NĂNG LỰC KỸ THUẬT & CÁC BỘ CÔNG CỤ PYTHON (PYTHON SKILLS & ENGINES)

Toàn bộ logic xử lý dữ liệu, kiểm toán thuật toán và tự động hóa được đóng gói trong thư mục [`scripts/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/) với 4 phân hệ chuyên biệt:

### 2.1. Phân Hệ SEO & GEO Engineering Engine

| Tập tin Script | Chức năng Kỹ thuật & Nghiệp vụ | Đầu ra & Ứng dụng |
| :--- | :--- | :--- |
| [`scripts/simulate_pipeline_refactor.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/simulate_pipeline_refactor.py) | Động cơ gom cụm ngữ nghĩa (Semantic Clustering), triệt tiêu xung đột từ khóa (Zero Cannibalization), phân bổ lại từ khóa sai danh mục và sinh cấu trúc Silo URL động dựa trên ngưỡng Volume thực tế | [`07_REPORTS/CONTENT_PLAN_REFACTOR_REVIEW.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/CONTENT_PLAN_REFACTOR_REVIEW.md) |
| [`scripts/generate_content_plan.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/generate_content_plan.py) | Tự động lập kế hoạch nội dung 7 tầng chuẩn Product Lead: phân bổ Intent (TOFU/MOFU/BOFU), outline H2/H3 E-E-A-T, Schema JSON-LD, Silo Linking và CTA Hooks Web-to-App | [`06_USE_CASE_MOMO/content-plans/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/06_USE_CASE_MOMO/content-plans/) |
| [`scripts/cron_gsc_cannibalization.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/cron_gsc_cannibalization.py) | Quét API Google Search Console để phát hiện hiện tượng "ăn thịt từ khóa" giữa các URLs cùng nhắm một truy vấn tìm kiếm | Cảnh báo URL xung đột và đề xuất Canonical/301 Redirect |
| [`scripts/cron_gsc_keyword_ranking.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/cron_gsc_keyword_ranking.py) | Tự động hóa trích xuất biến động thứ hạng từ khóa trọng điểm, CTR và lượt hiển thị thực tế từ GSC API | Báo cáo biến động vị trí Top 3, Top 10 |
| [`scripts/ingest_bing_ai.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/ingest_bing_ai.py) | Đo lường GEO: Giám sát tần suất trích dẫn thương hiệu MoMo trên Bing Copilot và các câu trả lời tổng hợp AI | Đánh giá thị phần nhận diện AI Engine |
| [`scripts/google_suggest_expander.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/google_suggest_expander.py) | Mở rộng tập từ khóa ngữ nghĩa đường dài (Long-tail Keywords) thông qua Google Suggest API thời gian thực | Bộ từ khóa bổ trợ (Secondary Synonyms) |
| [`scripts/serp_competitor_analyzer.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/serp_competitor_analyzer.py) | Phân tích khoảng trống nội dung (Content Gap) so với đối thủ cạnh tranh trực tiếp trên SERP | Báo cáo cơ hội Quick Wins |

### 2.2. Phân Hệ Phân Tích Thị Trường & Mùa Vụ (Market Intelligence & Seasonality)

| Tập tin Script | Chức năng Kỹ thuật & Nghiệp vụ | Đầu ra & Ứng dụng |
| :--- | :--- | :--- |
| [`scripts/cron_theme_seasonality.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/cron_theme_seasonality.py) | Khai thác dữ liệu lịch sử 5 năm (`today 5-y`) từ Google Trends, chuẩn hóa 12 tháng dương lịch (mảng 12 số nguyên, đỉnh bằng 100) có cơ chế Resume Cache và Exponential Backoff | [`07_REPORTS/data/theme_seasonality.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/theme_seasonality.json) |
| [`scripts/sync_inventory_to_hubs.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_inventory_to_hubs.py) | Đồng bộ dữ liệu Market Keyword Inventory từ 10 ngành kinh doanh vào các Web Hubs | Kho từ khóa SSOT tại [`05_HUBS/inventory/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/) |
| [`scripts/simulate_reallocation.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/simulate_reallocation.py) | Kiểm toán phân loại danh mục, tái cấu trúc các từ khóa thất lạc giữa các khối (Xổ số, Ngân hàng, Bảo hiểm, Xe) | Tối ưu hóa cấu trúc chuyên trang |

### 2.3. Phân Hệ Đo Lường Hiệu Suất Nền Tảng (Performance Tracking & Behavioral Analytics)

| Tập tin Script | Chức năng Kỹ thuật & Nghiệp vụ | Đầu ra & Ứng dụng |
| :--- | :--- | :--- |
| [`scripts/sync_tracking_report.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_tracking_report.py) | Tự động quét file tracking mới nhất trong Downloads, trích xuất số ngày lũy kế MTD T+1, nhịp chạy hàng ngày (Daily Pace), dự phóng Run-rate và cập nhật SSOT | [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md) |
| [`scripts/fetch_clarity.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/fetch_clarity.py) | Tích hợp Microsoft Clarity API để bóc tách hành vi người dùng, tỷ lệ Dead Clicks, Rage Clicks và độ sâu cuộn trang | Tối ưu hóa UX/UI cho các Web Hubs |
| [`scripts/sync_all_data.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/sync_all_data.py) | Đường ống đồng bộ hợp nhất: Clarity API, Performance Tracking, Google Trends và Bing Copilot | Đồng bộ toàn bộ dữ liệu chỉ với 1 lệnh |

### 2.4. Phân Hệ Báo Cáo Cấp Quản Trị (Executive Reporting & Deliverables)

| Tập tin Script | Chức năng Kỹ thuật & Nghiệp vụ | Đầu ra & Ứng dụng |
| :--- | :--- | :--- |
| [`scripts/tools/generate_report_html.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/tools/generate_report_html.py) | Động cơ kết xuất báo cáo hiệu suất dạng trang Web HTML Responsive phục vụ trình chiếu trực quan | File HTML Interactive Report |
| [`scripts/tools/generate_pptx.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/tools/generate_pptx.py) | Tự động hóa tạo bộ Slide PowerPoint (.pptx) chuẩn layout MoMo cho các buổi Monthly Business Review | File thuyết trình Ban Giám Đốc |
| [`scripts/cli.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/cli.py) | Trình điều khiển dòng lệnh hợp nhất (Unified CLI) điều phối toàn bộ các công cụ trong hệ thống | CLI Runner tập trung |

---

## 3. CÁC LỆNH VẬN HÀNH DÒNG LỆNH (QUICK COMMANDS)

```bash
# 1. Cài đặt các thư viện phụ thuộc
pip install -r scripts/requirements.txt

# 2. Đồng bộ số liệu tracking MTD mới nhất từ file tải về trong thư mục Downloads
python3 scripts/sync_tracking_report.py

# 3. Đồng bộ toàn bộ dữ liệu nền tảng (Clarity, Tracking, Trends, Copilot)
python3 scripts/sync_all_data.py

# 4. Chạy kiểm toán và tái cấu trúc Topic Clusters / Silo URLs
python3 scripts/simulate_pipeline_refactor.py

# 5. Cập nhật dữ liệu mùa vụ Google Trends 5 năm cho các Themes
python3 scripts/cron_theme_seasonality.py

# 6. Kiểm tra xung đột ăn thịt từ khóa trên Google Search Console
python3 scripts/cron_gsc_cannibalization.py

# 7. Xuất bản báo cáo thuyết trình PowerPoint tháng mới nhất
python3 scripts/cli.py report-pptx 07_REPORTS/data/monthly_10_2026_consolidated.json
```

---

## 4. KHUNG CHIẾN LƯỢC & TƯ DUY QUẢN TRỊ SẢN PHẨM (PRODUCT & SEO FRAMEWORKS)

### 4.1. Định Vị Kênh Web MoMo: Web Destination & Organic Core
* **Organic Search là Kênh Chủ Lực:** Giá trị cốt lõi của Web Platform nằm ở khả năng thu hút lưu lượng tự nhiên dài hạn với chi phí cận biên bằng 0. Tuyệt đối không xem việc chi ngân sách Paid Ads là thành tích tăng trưởng thực chất.
* **Mô Hình Web Destination:** Chuyển đổi từ website giới thiệu tính năng một chiều sang hệ sinh thái các Điểm đến Thông tin (Web Hubs) cung cấp giá trị tra cứu trực tiếp trước khi người dùng cần tải App.
* **Nguyên Tắc Đo Lường Độc Lập:** Lưu lượng truy cập In-App Webview không được tính vào KPI tăng trưởng chung của toàn Website.

### 4.2. Ma Trận Kiến Trúc 3+1 Zones Quản Trị Danh Mục Hubs
Toàn bộ các phân hệ Web được phân bổ theo 4 nhóm chiến lược chi tiết tại [`05_HUBS/WHAT_IS_HUB.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/WHAT_IS_HUB.md):
1. **Performance Zone (Khai thác & Giữ nhịp):** Cinema Hub — Tối đa hóa lưu lượng tìm kiếm phim, lịch chiếu và đặt vé rạp.
2. **Transformation Zone (Chuyển đổi chiến lược):** Financial Hub (Lãi suất, Vay, CIC, Tỷ giá) và Vehicle Hub (Phạt nguội, Đăng kiểm, Giá xăng, Showroom).
3. **Incubation Zone (Ươm tạo & Mở rộng):** Insurance, Travel/OTA, Student Hub, Lottery, Payment, Game Hub.
4. **Foundation Zone (Hạ tầng nền tảng):** New User Experience, MoSpark CMS, Edge Middleware và Home Web.

### 4.3. Phễu Chuyển Đổi Web-to-App (PLG Funnel)
* **Zero-Gate & 0-CAPTCHA:** Mọi công cụ tiện ích (tính lãi tiết kiệm, tra cứu phạt nguội, tính bảo hiểm xã hội) đều mở công khai, giải quyết trọn vẹn nhu cầu tức thì của người dùng mà không bắt buộc đăng nhập hay giải mã captcha.
* **Identity Tracking & W2A Attribution:** Sử dụng định danh Web User ID qua cookie Edge Middleware kết hợp tham số OneLink (`?wui=[identityId]`) để phân bổ chính xác nguồn đóng góp người dùng mới từ Web sang App mà vẫn đảm bảo tiêu chuẩn an toàn thông tin Zero-PII.

---

## 5. BẢN ĐỒ KIẾN TRÚC TRI THỨC (KNOWLEDGE ROUTING ARCHITECTURE)

Hệ thống thư mục được tổ chức theo cấu trúc phân cấp chặt chẽ:

```
.
├── README.md                           # Bản đặc tả hệ điều hành tri thức & bộ công cụ (File này)
├── AGENTS.md                           # Bộ quy tắc vận hành và chuẩn mực phản hồi của AI Agent
├── MEETING_RECAPS.md                   # Nhật ký biên bản họp và chỉ đạo chiến lược của BOM
│
├── 00_HARNESS_CORE/                    # Lõi định tuyến tri thức (KNOWLEDGE_ROUTING.md) & Master Doc
├── 01_STRATEGIC_PLAN/                  # Chiến lược tăng trưởng, OKRs, Thesis SEO-to-GEO 2027
├── 02_FRAMEWORKS/                      # Khung tư duy (First Principles, JTBD, SEO/GEO Playbook)
├── 03_SKILLS/                          # Bộ kỹ năng quản trị sản phẩm và chuẩn mực viết BRD/PRD
├── 04_MOSPARK_PLATFORM/                # Kiến trúc CMS MoSpark, Microsites, Widget Store, Edge Identity
│   ├── umami_utility_tracking.md       # SSOT: Quy chuẩn Event Tracking cho toàn bộ tiện ích Web
├── 05_HUBS/                            # Tài liệu đặc tả Strategic Hubs & Kho Keyword Inventory (3.7M+ Vol)
│   ├── cinema/                         # Cinema Hub (Lịch chiếu, rạp phim, diễn viên)
│   ├── financial/                      # Financial Hub (Tiết kiệm, Vay, CIC, Tỷ giá, Vàng)
│   ├── vehicle/                        # Vehicle Hub (Phạt nguội, Đăng kiểm, Showroom, Model xe)
│   ├── student/                        # Student Hub (Đặc quyền sinh viên, cổng thông tin trường)
│   ├── inventory/                      # Kho dữ liệu từ khóa thô theo từng ngành (CSV Datasets)
│   └── WHAT_IS_HUB.md                  # Khung lý luận và phân vùng 3+1 Zones
├── 06_USE_CASE_MOMO/                   # Hồ sơ nghiên cứu Use Case & Content Plans chuẩn hóa chống ăn thịt
├── 07_REPORTS/                         # SSOT Performance Tracking (Master Excel, Markdown Report, MTD Data)
│   ├── WEB_PERFORMANCE_TRACKING_MASTER.md # Báo cáo hiệu suất Web Master cập nhật liên tục
│   ├── docs/                           # Kho báo cáo tháng chính thức (Tháng 01 đến Tháng 10/2026)
│   ├── data/                           # Dữ liệu snapshot JSON MTD, Seasonality và GSC Credentials
│   └── technical_seo/                  # Dữ liệu kiểm toán Backlink, Disavow và Crawl Stats
├── 08_DECISION_LOG/                    # Nhật ký lưu vết các quyết định kiến trúc then chốt (ADR)
├── 09_PRD/                             # Kho lưu trữ đặc tả yêu cầu sản phẩm chi tiết (PRD chuẩn mực)
├── 10_LEADERSHIP_MINDSET/              # Tư duy quản trị và triết lý sản phẩm của Lãnh đạo
├── 11_NEWS_FEED/                       # Cổng tiếp nhận tin tức thị trường tự động
├── 12_TASK_MANAGEMENT/                 # Quản trị tiến độ thực thi công việc theo từng tuần/tháng
├── 13_INTAKE/                          # Cổng tiếp nhận và phân loại dữ liệu đầu vào tự động
└── scripts/                            # Động cơ tự động hóa Python (SEO/GEO, Trends, Tracking, CLI)
    ├── lib/                            # Thư viện tiện ích xử lý Excel và Markdown an toàn
    └── tools/                          # Bộ công cụ sinh báo cáo HTML Responsive và PowerPoint Slide
```

---

## 6. QUY CHUẨN ĐO LƯỜNG & VẬN HÀNH BẮT BUỘC (STANDARDS & GOVERNANCE)

Mọi kỹ sư, quản lý sản phẩm và chuyên viên dữ liệu khi đóng góp vào hệ thống bắt buộc tuân thủ 4 nguyên tắc sau:

1. **Chuẩn Mực Đo Lường Tiện Ích (Utility Tracking Standard):**
   * Tham chiếu duy nhất tại [`04_MOSPARK_PLATFORM/umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/umami_utility_tracking.md).
   * Cú pháp sự kiện bắt buộc: `web_[mospark_tool_id]_[object]_[action]`.
   * Tuân thủ nguyên tắc Zero-PII: Tuyệt đối không gửi thông tin định danh cá nhân vào payload tracking.

2. **Chuẩn Mực Soạn Thảo Tài Liệu (Documentation Formatting):**
   * Luồng người dùng (User Flow) bắt buộc sử dụng sơ đồ trực quan Mermaid (`graph TD` hoặc `graph LR`) kèm Bảng Phân Tích Chi Tiết Các Bước.
   * Lộ trình phát triển (Roadmap) bắt buộc trình bày dưới dạng Bảng Markdown (`Table`).
   * Không sử dụng Emoji / Icon trong tiêu đề, bảng biểu và danh sách của tài liệu báo cáo.
   * Không sử dụng tên riêng cá nhân/PIC trong báo cáo; thay thế bằng tên đội ngũ chuyên môn (`Web Dev`, `Product Lead`, `SEO Team`...).

3. **Chuẩn Hóa Thuật Ngữ Kiến Trúc Thông Tin:**
   * **Cấu trúc phân cấp chuẩn:** `Hub ➔ Theme ➔ Cluster / Article`.
   * **Thuật ngữ nền tảng:** Tuyệt đối không dùng từ *"sàn Web"*. Bắt buộc dùng: *"toàn Website"*, *"nền tảng Web"*, *"Kênh Web"*, *"Web Platform"* hoặc *"Web"*.

4. **Nguyên Tắc Xử Lý Dữ Liệu Tracking:**
   * Mọi cập nhật số liệu hiệu suất Web Platform bắt buộc chạy qua script `python3 scripts/sync_tracking_report.py` để đảm bảo tính toàn vẹn và đồng bộ từ file gốc đến SSOT Markdown.
