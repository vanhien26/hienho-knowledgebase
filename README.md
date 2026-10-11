# HƯỚNG DẪN SỬ DỤNG KHO DỮ LIỆU & CÔNG CỤ WEB PLATFORM (MOMO WEB BASE)

Kho lưu trữ (repository) này là hệ thống **Single Source of Truth (SSOT)** và **Bộ công cụ tự động hóa** phục vụ toàn bộ hoạt động kỹ thuật, dữ liệu và quản trị sản phẩm của **Kênh Web MoMo (`momo.vn`)**.

---

## 1. BẮT ĐẦU NHANH (QUICK START)

### Cài đặt Môi trường
Kho lưu trữ sử dụng Python 3.9+ cho các công cụ tự động hóa, xử lý dữ liệu Excel và xuất bản báo cáo:

```bash
# Cài đặt thư viện phụ thuộc
pip install -r scripts/requirements.txt
```

### Các Lệnh Thường Dùng (CLI Commands)

```bash
# 1. Đồng bộ số liệu tracking MTD mới nhất từ file tải về trong Downloads
python3 scripts/sync_tracking_report.py

# 2. Xem danh sách công cụ tự động hóa đang hoạt động
python3 scripts/cli.py info

# 3. Xuất bản báo cáo Slide deck định dạng HTML responsive
python3 scripts/cli.py report-html 07_REPORTS/data/monthly_09_2026_mtd.json

# 4. Xuất bản slide thuyết trình PowerPoint (.pptx) chuẩn layout MoMo
python3 scripts/cli.py report-pptx 07_REPORTS/data/monthly_09_2026_mtd.json

# 5. Nén và chuẩn hóa định dạng Markdown toàn bộ thư mục
python3 scripts/cli.py md-process 05_HUBS
```

---

## 2. HƯỚNG DẪN DÀNH CHO SOFTWARE ENGINEER

Kỹ sư phát triển Web tham chiếu và thực hiện các tác vụ kỹ thuật theo các quy chuẩn sau:

### Tác vụ 1: Gắn Tracking cho Công Cụ Tiện Ích Mới (Lookup / Calculator / Tool)
- **Tài liệu quy chuẩn bắt buộc:** Mở file [`umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/umami_utility_tracking.md).
- **Quy tắc đặt tên sự kiện (Event Name):** Bắt buộc tuân thủ công thức:
  ```
  web_[mospark_tool_id]_[object]_[action]
  ```
  *Ví dụ:* `web_salary_calculator_calculate_click`, `web_traffic_fine_lookup_submit`.
- **Tham số payload gửi kèm:**
  - Luôn gửi: `provider` (tên đối tác/ngân hàng/hãng), `amount` (số tiền nguyên thủy nếu có), `source_page` (URL trang hiện tại).
  - **Quy tắc bảo mật Zero-PII:** Tuyệt đối không gửi số điện thoại, CCCD, biển số xe đầy đủ hoặc thông tin cá nhân vào payload Umami.

### Tác vụ 2: Tích Hợp Xác Thực Người Dùng & Phễu Chuyển Đổi Web-to-App
- **Đăng nhập ngoài Web:** Sử dụng hạ tầng `m.momo.vn` (Central Web Login) để người dùng quét QR qua App MoMo hoặc nhận OTP điện thoại. Tuyệt đối không tự viết form thu thập mật khẩu trực tiếp trên Web.
- **Gắn mã chuyển đổi Web-to-App (W2A OneLink):**
  - Đọc tài liệu [`04_MOSPARK_PLATFORM/mospark_user_identity_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/mospark_user_identity_tracking.md).
  - Mọi nút bấm mở App / tải App (OneLink) phải được gắn tự động tham số `?wui=[identityId]` lấy từ cookie Edge Middleware để AppsFlyer ghi nhận chuyển đổi.

### Tác vụ 3: Xây Dựng Giao Diện & Tiện Ích (Revised UI & Widgets)
- **Design System:** Sử dụng thư viện chuẩn `@momo-webplatform/mobase` cho các thành phần giao diện mới.
- **Nguyên tắc trải nghiệm:** Không chặn người dùng bằng popup bắt buộc đăng nhập (Zero-Gate) và không dùng CAPTCHA (0-CAPTCHA) trên các công cụ tra cứu công cộng.
- **Phân phối Widget:** Tham khảo tài liệu [`04_MOSPARK_PLATFORM/mospark_widget_store.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/mospark_widget_store.md) để đóng gói widget nhúng vào MoSpark CMS.

### Tác vụ 4: Sử Dụng Thư Viện Tiện Ích Codebase (`scripts/lib/`)
- Khi viết script thao tác file Excel: Sử dụng `from scripts.lib.excel_utils import load_workbook_safe, save_with_backup` để tự động tạo file sao lưu `.bak` trước khi ghi đè dữ liệu.
- Khi viết script thao tác Markdown: Sử dụng `from scripts.lib.md_utils import compress_markdown` để dọn dẹp khoảng trắng và comment thừa.

---

## 3. HƯỚNG DẪN DÀNH CHO PRODUCT MANAGER

Quản lý sản phẩm thực hiện tra cứu số liệu, quản lý danh mục và chuẩn bị tài liệu dự án:

### Tác vụ 1: Kiểm Tra Số Liệu Hiệu Suất Kênh Web Thực Tế
- **Nguồn dữ liệu chân lý duy nhất (SSOT):** Mở file [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md).
- **Cập nhật số liệu mới:** Khi nhận file tracking từ Data Team, tải file về máy và chạy script `python3 scripts/sync_tracking_report.py`. Hệ thống sẽ tự động cập nhật bảng master, tính toán số ngày lũy kế MTD T+1, nhịp chạy hàng ngày (Daily Pace) và dự phóng cả tháng (Run-rate).

### Tác vụ 2: Tra Cứu Kiến Trúc Danh Mục Hubs & Use Cases
- Mở file [`05_HUBS/WHAT_IS_HUB.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/WHAT_IS_HUB.md) để nắm:
  - Khung quản trị 3+1 Zones (Performance: Cinema Hub; Transformation: Financial Hub, Vehicle Hub; Incubation: Insurance, Travel, Student, Lottery, Payment, Game, Merchant, New User, Home Web).
  - Khái niệm mô hình Hub-and-Spoke và cấu trúc 4 khối thành phần của một Web Hub chuẩn.
- Đọc tài liệu đặc tả từng Hub chi tiết trong thư mục [`05_HUBS/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS).

### Tác vụ 3: Nắm Bắt Bối Cảnh Chỉ Đạo Chiến Lược & Quyết Định Quá Khứ
- **Chỉ đạo của Ban Giám Đốc:** Đọc [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md) trước mỗi cuộc họp hoặc trước khi lập kế hoạch mới.
- **Lịch sử các quyết định kiến trúc đã chốt:** Tra cứu tại [`08_DECISION_LOG/decision_log.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/08_DECISION_LOG/decision_log.md) để tránh thảo luận lại các vấn đề đã có kết luận thống nhất.

### Tác vụ 4: Soạn Thảo Tài Liệu BRD / PRD Mới
- Lấy mẫu khung chuẩn hóa tại [`09_PRD/_template-prd.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/09_PRD/_template-prd.md).
- Quy chuẩn bắt buộc khi viết tài liệu:
  - Luồng người dùng (User Flow) bắt buộc dùng sơ đồ Mermaid (`graph TD` hoặc `graph LR`) kèm bảng mô tả từng bước.
  - Lộ trình phát triển (Roadmap) bắt buộc dùng bảng Markdown (`Table`).
  - Không dùng Emoji / Icon trong nội dung tiêu đề, bảng biểu và danh sách.
  - Không đề cập tên riêng cá nhân/PIC (thay bằng tên đội ngũ chuyên môn như `Web Dev`, `Cell Team`, `Media Team`...).

---

## 4. BẢN ĐỒ TRA CỨU NHANH THEO NHU CẦU (CHEATSHEET)

| Bạn Cần Làm Gì? | Mở Tệp Tin / Thư Mục Nào? | Ghi Chú |
|---|---|---|
| Gắn mã tracking Umami cho tiện ích Web | [`umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/umami_utility_tracking.md) | SSOT quy chuẩn Event Tracking duy nhất |
| Xem dữ liệu hiệu suất MTD & lịch sử Traffic | [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md) | SSOT hiệu suất Kênh Web |
| Xem định nghĩa Hub & danh mục 10 Web Hubs | [`05_HUBS/WHAT_IS_HUB.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/WHAT_IS_HUB.md) | Khung kiến trúc và ma trận 3+1 Zones |
| Xem chỉ đạo của BOM trong các cuộc họp | [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md) | Nhật ký biên bản họp định kỳ |
| Tra cứu các quyết định kiến trúc đã chốt | [`08_DECISION_LOG/decision_log.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/08_DECISION_LOG/decision_log.md) | Bảng log Fork Points từ tháng 4/2026 đến nay |
| Tìm hiểu quy tắc vận hành dành cho AI Agent | [`AGENTS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/AGENTS.md) | Bộ luật xử lý thông tin và văn phong bắt buộc |
| Bản đồ định tuyến tri thức toàn hệ thống | [`00_HARNESS_CORE/KNOWLEDGE_ROUTING.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/00_HARNESS_CORE/KNOWLEDGE_ROUTING.md) | Quy trình định tuyến 5 tầng tri thức |
| Lấy mẫu viết đặc tả sản phẩm (PRD/BRD) | [`09_PRD/_template-prd.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/09_PRD/_template-prd.md) | Khung tài liệu chuẩn 4 phần |
| Chạy các công cụ xuất báo cáo và nén file | [`scripts/cli.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/cli.py) | Unified CLI Runner |

---

## 5. SƠ ĐỒ CẤU TRÚC THƯ MỤC CODEBASE

```
.
├── README.md                           # Hướng dẫn sử dụng kho dữ liệu và công cụ (File này)
├── AGENTS.md                           # Bộ quy tắc vận hành bắt buộc dành cho AI Agent
├── MEETING_RECAPS.md                   # Nhật ký biên bản họp và chỉ đạo chiến lược của BOM
├── umami_utility_tracking.md           # SSOT: Quy chuẩn Event Tracking mọi công cụ tiện ích
│
├── 00_HARNESS_CORE/                    # Bản đồ định tuyến tri thức (KNOWLEDGE_ROUTING.md) & Master Doc
├── 01_STRATEGIC_PLAN/                  # Kế hoạch chiến lược tăng trưởng, OKRs và chính sách URL
├── 02_FRAMEWORKS/                      # Khung tư duy (First Principles, JTBD, SEO/GEO Playbook)
├── 03_SKILLS/                          # Bộ kỹ năng quản trị sản phẩm và chuẩn mực viết BRD
├── 04_MOSPARK_PLATFORM/                # Kiến trúc CMS MoSpark, Microsite, Identity, Widget Store
├── 05_HUBS/                            # Tài liệu đặc tả 10 Strategic Hubs (WHAT_IS_HUB.md, Cinema, Vehicle...)
├── 06_USE_CASE_MOMO/                   # Hồ sơ phân tích chi tiết từng Use Case & bài toán kinh doanh
├── 07_REPORTS/                         # SSOT Performance Tracking (Master Excel, Markdown Report & MTD Data)
├── 08_DECISION_LOG/                    # Nhật ký lưu vết các quyết định chiến lược (decision_log.md)
├── 09_PRD/                             # Kho lưu trữ đặc tả yêu cầu sản phẩm chi tiết (PRDs)
├── 10_LEADERSHIP_MINDSET/              # Tư duy quản trị và triết lý sản phẩm của Lãnh đạo
├── 11_NEWS_FEED/                       # Cổng tiếp nhận tin tức thị trường tự động (Gemini Spark)
└── scripts/                            # Bộ công cụ tự động hóa, sync tracking, export slide & CLI Engine
```

---

## 6. QUY TẮC BẮT BUỘC KHI ĐÓNG GÓP TÀI LIỆU (REPO STANDARDS)

1. **Thuật ngữ:** Tuyệt đối không dùng từ *"sàn Web"*. Bắt buộc dùng: *"nền tảng Web"*, *"Kênh Web"*, *"Web Platform"* hoặc *"Web"*.
2. **Hình thức:** Tuyệt đối không dùng Emoji / Icon trong nội dung tiêu đề, bảng biểu và danh sách của bài báo cáo.
3. **Định danh:** Tuyệt đối không đưa tên riêng cá nhân/PIC vào tài liệu báo cáo; sử dụng tên đội ngũ chuyên môn (`Web Dev`, `Web Product Lead`, `Cell Team`...).
4. **Định vị kinh doanh:** Organic Search là kênh cốt lõi mang lại giá trị bền vững; không tô điểm cho Paid Ads.
