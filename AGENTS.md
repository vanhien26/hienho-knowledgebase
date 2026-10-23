# AGENTS.MD - WORKSPACE INSTRUCTIONS & RULES

## 🎯 CHẾ ĐỘ VẬN HÀNH: PROBLEM → OPTIMAL ANSWER (KHÔNG PHẢI AGENT TỰ ĐỘNG)

- **Không tự ý triển khai, không chạy tác vụ dài hơi khi chưa được yêu cầu.** Đây không phải chế độ autonomous agent.
- **Khi người dùng đặt vấn đề:** Trả lời trực tiếp, sắc sảo, đúng trọng tâm - là câu trả lời tối ưu nhất dựa trên toàn bộ knowledge base, không cần người dùng phải hỏi đi hỏi lại.
- **Quy trình trả lời một vấn đề (Lazy & Intent-Based Routing):**
  1. **Định tuyến nhanh (Fast Routing):** Phân loại ý định theo bảng Fast Routing Index bên dưới. Tuyệt đối KHÔNG tự ý đọc các file lớn (`MEETING_RECAPS.md`, `hienho_master_doc.md`, `WEB_PERFORMANCE_TRACKING_MASTER.md`) cho các câu hỏi kỹ thuật, code review, trao đổi logic hoặc tra cứu thông thường. Cần mảng nào chỉ đọc đúng 1 file SSOT của mảng đó.
  2. **Phân tích với Chain of Thought:** reasoning trước, kết luận sau. Chỉ ra lỗi logic, điểm mâu thuẫn, giả định chưa validate nếu phát hiện.
  3. **Gắn vào business metric (khi phù hợp):** New User / MAU / Traffic / Revenue và framework hiện có (JTBD, 4 Zones, PLG, Web-to-App).
  4. **Đề xuất tối ưu kèm Action Items cụ thể**, có ưu tiên rõ ràng.
- **Chỉ build/render file (HTML, script, PRD, report) khi người dùng yêu cầu rõ** - hoặc khi câu trả lời "tối ưu nhất" bắt buộc cần artifact để chứng minh, và phải nêu lý do.
- Khi thấy phương án người dùng chọn có rủi ro hoặc có phương án tốt hơn đáng kể: nêu thẳng, không xuôi theo.

### 🗺️ BẢNG ĐỊNH TUYẾN NHANH (FAST ROUTING INDEX SSOT)

| Nghiệp vụ / Chủ đề người dùng hỏi | File SSOT đích duy nhất (Target File) | Hành vi nạp file (Loading Policy) |
| :--- | :--- | :--- |
| **Hỏi nhanh, Kỹ thuật, Code, Review, Debug** | File code hoặc file văn bản liên quan trực tiếp | **Zero context file load**. Trả lời ngay, không đọc file bối cảnh. |
| **Tracking Umami, Event Name, Schema Params** | [`04_MOSPARK_PLATFORM/umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/umami_utility_tracking.md) | Chỉ đọc file này khi hỏi về tracking/sự kiện. |
| **Tra cứu Keyword Inventory Use Case** | [`05_HUBS/inventory/<hub-name>/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/) | Chỉ đọc đúng file CSV của Hub tương ứng. |
| **Paid Ads, Kênh Media, UTM Campaigns** | [`07_REPORTS/data/analytics/paid_ads_performance.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/paid_ads_performance.json) | Đọc file JSON SSOT hoặc chạy `./.venv/bin/python scripts/sync_paid_ads.py`. |
| **Lịch mùa vụ, Phân tích Google Trends** | [`07_REPORTS/data/theme_seasonality.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/theme_seasonality.json) | Đọc file JSON đã xuất bản hoặc chạy script cron. |
| **Báo cáo Tuần/Tháng, Hiệu suất MTD, Target** | [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md) | Chỉ đọc khi người dùng yêu cầu làm báo cáo/phân tích số liệu. |
| **Tra cứu Báo cáo Lịch sử (T1 -> T10, Hubs)** | [`07_REPORTS/docs/INDEX.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/INDEX.md) | Đọc index để mở đúng file báo cáo tháng hoặc chuyên đề cần tìm. |
| **Chỉ đạo Lãnh đạo, Quyết định chiến lược** | [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md) | Chỉ đọc section gần nhất khi lập kế hoạch chiến lược mới. |
| **Quy chuẩn viết, Văn phong, Format** | Trực tiếp trong `AGENTS.md` | Có sẵn trong bộ nhớ hệ thống, không đọc thêm file. |

---

## 🧠 MANDATORY CONTEXT MEMORY: ALWAYS READ MEETING RECAPS & PERFORMANCE SSOT

- **Memory Source Files:** 
  1. [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md)
  2. [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md)
- **Python Runtime & Environment SSOT Rule:** Toàn bộ pipeline và script Python trong repo (`scripts/*.py`) được quản lý tập trung qua môi trường ảo [`./.venv`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/.venv) (Python 3.12) và định nghĩa SSOT tại [`scripts/requirements.txt`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/requirements.txt). Khi AI Agent hoặc hệ thống chạy bất kỳ script Python nào, **BẮT BUỘC gọi trực tiếp `./.venv/bin/python <script_path>`** (ví dụ: `./.venv/bin/python scripts/sync_tracking_report.py`). Tuyệt đối không dùng lệnh `python3` trần để tránh việc macOS tự động fallback về Python 3.9 hệ thống gây thiếu thư viện (`underthesea`, `pytrends`).
- **Automated Tracking Report Trigger Rule:** Khi người dùng yêu cầu *"đọc tracking report mới nhất"* (hoặc bất kỳ câu lệnh tương tự về việc cập nhật/lấy số tracking), AI Agent **BẮT BUỘC tự động chạy script `./.venv/bin/python scripts/sync_tracking_report.py`** để:
  1. Quét tự động file `*Web Performance Tracking*.xlsx` mới nhất trong thư mục `/Users/hienhv/Downloads/`.
  2. Trích xuất chính xác số ngày lũy kế MTD (MTD Days), lưu bản ghi sạch vào SSOT [web_performance_tracking.xlsx](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/web_performance_tracking.xlsx) và tạo JSON snapshot.
  3. Đồng bộ báo cáo master và trình bày kết quả ngay lập tức theo phong cách Product Lead / Tech Lead.
- **Automated Paid Ads & UTM Trigger Rule:** Khi người dùng yêu cầu *"kiểm tra ads"*, *"web đang chạy ads gì"*, *"kênh media nào đang chạy ads"*, *"hiệu suất paid ads/UTM"*, AI Agent **BẮT BUỘC tự động chạy script `./.venv/bin/python scripts/sync_paid_ads.py`** để:
  1. Truy vấn trực tiếp GA4 Data API (Property 270743103) cho chu kỳ MTD.
  2. Tự động bóc tách landing pages, kênh media (`sessionSourceMedium`), chiến dịch và chuyển đổi Web-to-App.
  3. Xuất dữ liệu sạch sang SSOT [`07_REPORTS/data/analytics/paid_ads_performance.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/analytics/paid_ads_performance.json), cập nhật báo cáo [`07_REPORTS/docs/PAID_ADS_TRACKING_LATEST.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/docs/PAID_ADS_TRACKING_LATEST.md) và trình bày báo cáo trực diện.
- **Strategic Context Trigger Rule:** Khi người dùng yêu cầu **lập kế hoạch chiến lược cấp cao, viết PRD mới, chuẩn bị báo cáo tuần/tháng (WBR/MBR) hoặc phân tích số liệu hiệu suất Web Platform**, AI Agent mới chủ động tham chiếu số liệu thực tế từ file [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md) và mục recaps gần nhất từ [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md). Với các câu hỏi nghiệp vụ thông thường, hỏi kỹ thuật, tra cứu tiện ích hay review trao đổi, **TUYỆT ĐỐI KHÔNG tự ý đọc các file này** để tối ưu tốc độ phản hồi.
- **Utility Tracking SSOT Rule:** Khi Kỹ sư (Dev) hoặc người dùng hỏi về: gắn tracking, đo lường công cụ, sự kiện Umami, Event Name cho tool/widget/calculator, schema tham số (`provider`, `amount`) hoặc cách track cho bất kỳ tiện ích nào, AI Agent **BẮT BUỘC chỉ định và trích xuất trực tiếp từ file SSOT [`04_MOSPARK_PLATFORM/umami_utility_tracking.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/umami_utility_tracking.md)**.
- **Use Case Keyword Inventory SSOT Rule:** Khi người dùng yêu cầu *"tra cứu Inventory của 1 use case"* (hoặc bất kỳ câu lệnh liên quan đến kiểm tra dataset từ khóa, keyword clusters, market volume thô của một ngành/use case), AI Agent **BẮT BUỘC chỉ định và đọc trực tiếp từ thư mục SSOT [`05_HUBS/inventory/`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory/)** (gồm các phân khối: `Financial/`, `vehicle-hub/`, `insurtech/`, `ota/`, `telco/`, `hospital/`, `Lottery/`, `trust/`, `cinema/`, `student/`, `Entertainment/`, `other/`). Tuyệt đối không tự suy diễn số liệu từ khóa khi chưa quét các file CSV tương ứng trong thư mục này.
- **Seasonality & Google Trends Intelligence SSOT Rule:** Khi người dùng hoặc hệ thống yêu cầu tính toán, cập nhật lịch mùa vụ (Seasonality), phân tích xu hướng thị trường hoặc chuẩn bị dữ liệu xuất sang Web Hubs (`react-web-momo`):
  1. AI Agent **BẮT BUỘC chỉ định và sử dụng script [`scripts/cron_theme_seasonality.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/cron_theme_seasonality.py)** (chạy bằng `./.venv/bin/python`) để xuất bản file dữ liệu SSOT [`07_REPORTS/data/theme_seasonality.json`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/theme_seasonality.json).
  2. **Quy tắc Khung thời gian (Timeframe):** Tuyệt đối **KHÔNG dùng dữ liệu 12 tháng** của `theme_trends` để tính mùa vụ (vì 12 tháng chỉ là 1 năm đơn lẻ, dễ bị nhiễu bởi các biến động ngẫu nhiên). BẮT BUỘC phải lấy dữ liệu 5 năm (`timeframe="today 5-y"`) và tính trung bình theo từng tháng dương lịch (T1..T12) qua 5 năm.
  3. **Quy tắc Bắt buộc của Contract (theo schema `lib/content-plan/seasonality.ts`):**
     - Mảng `monthly` gồm đúng 12 số nguyên, theo thứ tự từ T1 đến T12, đã chuẩn hóa sao cho tháng cao nhất bằng 100.
     - `theme_id` phải trùng khớp chính xác `id` trong file cluster (`data/seo-clusters/*/*.json`).
     - Mỗi payload truy vấn chỉ chứa **duy nhất 1 keyword (pillar)**; không gộp nhiều keyword để tránh bị chuẩn hóa chéo làm méo dạng mùa vụ của keyword yếu hơn.
     - Cơ chế vận hành: Tích hợp Resume cache (không crawl lại các theme đã hoàn tất) và Exponential Backoff tự động khi gặp mã lỗi HTTP 429.
- **Vietnamese NLP SSOT Rule:** Mọi tác vụ tách từ / word segmentation / trích xuất n-gram tiếng Việt trong pipeline **BẮT BUỘC gọi qua gateway [`scripts/lib/vi_nlp.py`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/scripts/lib/vi_nlp.py)** (`segment()`, `segment_text()`) - KHÔNG import trực tiếp `underthesea`/`pyvi` rải rác trong script khác. Backend: underthesea 9.5+ (đã tích hợp trong `./.venv`), tự fallback pyvi rồi naive split khi thiếu lib (không crash). Chuẩn hóa teencode / lỗi dấu dùng `TELEX_FIXES` + `normalize_text()` trong `scripts/lib/keyword_intelligence.py` - KHÔNG dùng `text_normalize()` của underthesea (yếu với teencode). Entity/brand dùng `ENTITY_LEXICON` + `flashtext` trong `scripts/lib/keyword_extractor.py` - KHÔNG dùng NER của underthesea cho keyword fragment. Khi đọc CSV inventory trực tiếp, LUÔN bóc artifact Excel `="..."` bằng `clean_val()` trước khi xử lý.
- **Traffic Source Classification SSOT Rule (Non-Paid vs. Paid Dichotomy):** Khi phân tích, đo lường hoặc trình bày bất kỳ báo cáo nào (Weekly, Monthly, Ad-hoc) về nguồn lưu lượng (Traffic Source / Channels) của Web Platform:
  1. **BẮT BUỘC phân chia thành 2 nhóm lớn rõ rệt:**
     - **Non-Paid Traffic (Tất cả trừ Paid Traffic):** Bao gồm toàn bộ `Organic`, `Direct`, `Referral`, `Others`, `Cross`... Non-Paid là động cơ tăng trưởng tự nhiên bền vững, thể hiện chất lượng thực chất, giá trị SEO/GEO, sức mạnh thương hiệu và độ tin cậy của toàn Website.
     - **Paid Traffic (Paid Traffic):** Bao gồm `Paid Search`, `Google Ads`, `Campaign Ads`...
  2. **Quy tắc hiển thị bảng biểu:** Phân cấp rõ 2 dòng tổng **Non-Paid** vs. **Paid** (kèm tỷ trọng % tương ứng). Nếu cần chi tiết, các kênh con (`Organic`, `Direct`, `Referral`, `Others`) phải được đặt thụt dòng bên dưới nhóm **Non-Paid**. Tuyệt đối không liệt kê Paid nằm xen kẽ ngang hàng giữa các kênh tự nhiên.
- **Mục đích:** Đảm bảo toàn bộ bối cảnh chiến lược của Ban Giám Đốc, định hướng của các Hubs và dữ liệu hiệu suất Single Source of Truth (SSOT) chuẩn xác luôn được đưa vào context xử lý tự động trước khi xuất bản bất kỳ báo cáo nào.

---

## ✍️ QUY TẮC VĂN PHONG VÀ VIẾT TÀI LIỆU (WRITING STYLE RULE)

- **Phong cách:** Thực tế, cô đọng, ngắn gọn, tự nhiên chuẩn Product Lead / Tech Lead. Đi thẳng vào bản chất vấn đề, số liệu và gạch đầu dòng.
- **TUYỆT ĐỐI KHÔNG:** 
  - **TUYỆT ĐỐI KHÔNG dùng các từ "sàn", "sàn Web", "toàn sàn":** Bắt buộc chỉ dùng **"toàn Website"**, **"nền tảng Web"**, **"Kênh Web"**, **"Web Platform"** hoặc **"Web"**.
  - **Không dùng bất kỳ Emoji / Icon nào** trong nội dung tiêu đề, bảng biểu và danh sách của bài báo cáo (Report).
  - **Không đề cập tên riêng của cá nhân / PIC** (như `[Hiến]`, `[Thuận]`, `[Trọng]`, `[Nhật]`, `Hiếu`...) trong bài báo cáo. Thay thế bằng tên đội ngũ chuyên môn (như `Web Dev`, `Backend Team`, `Content Team`, `SEO Vendor`...).
  - Không dùng văn chương màu mè, sáo rỗng, hoa mỹ kiểu AI (ví dụ: *"bệ phóng phát triển"*, *"bứt phá ngoạn mục"*, *"khẳng định vị thế uy tín"*, *"hành trình chuyển đổi"*...).
  - Không viết dài dòng lê thê, không lặp lại ý.
- **Chuẩn hóa Thuật ngữ Kiến trúc Thông tin (Information Architecture Terminology):**
  - **Hub:** Bắt buộc dùng thay cho "Phân Khối Ngành", "Phân ngành", "Sector" (ví dụ: Cinema Hub, Financial Hub, Vehicle Hub, Insurtech Hub, OTA Hub, Lottery Hub...).
  - **Theme:** Bắt buộc dùng thay cho "Use Case", "Use case" (ví dụ: trong Financial Hub có các Themes: Tỷ giá, Giá vàng, Tiết kiệm ngân hàng, Vay tín chấp...).
  - Cấu trúc phân cấp 3 tầng chuẩn mực: **Hub ➔ Theme ➔ Cluster/Article**.
- **Cấu trúc viết:** Nhìn vào hiểu ngay ➔ Nêu rõ Context ➔ Action Items ➔ KPIs / Số liệu thực tế.

---

## 📐 QUY TẮC TRÌNH BÀY SƠ ĐỒ & CẤU TRÚC TÀI LIỆU (DOCUMENTATION & DIAGRAM FORMATTING)

- **Biểu diễn Luồng Người dùng (User Flow / Onboarding / Conversion Flow):**
  - **BẮT BUỘC** sử dụng **Sơ đồ Trực quan Mermaid (`mermaid`)** dạng `graph TD` hoặc `graph LR` cho toàn bộ các luồng User Flow trong BRD/PRD.
  - **TUYỆT ĐỐI KHÔNG** dùng sơ đồ mã ASCII thô (văn bản vẽ tay dạng `[1] ──► [2]`).
  - Bổ sung ngay bên dưới sơ đồ Mermaid một **Bảng Phân Tích Chi Tiết Các Bước (Step Breakdown Table)** gồm các cột: `Bước`, `Tên Giai Đoạn`, `Trải Nghiệm Người Dùng (UX)`, `Hạ Tầng / Cơ Chế Kỹ Thuật`, `Nền Tảng`.
- **Biểu diễn Lộ trình & Cột mốc (Roadmap & Milestones):**
  - **BẮT BUỘC** trình bày dưới dạng **Bảng Markdown (`Table`)** (gồm: `Giai đoạn`, `Thời gian`, `Tên Giai Đoạn`, `Chi Tiết Triển Khai & Mục Tiêu`).
- **Metadata & Chuẩn hóa Tài liệu:**
  - **Bỏ thuộc tính `Platform:`** trong blockquote Metadata ở đầu tất cả các file BRD.
  - **Không dùng Emoji / Icon** trong tất cả các bài báo cáo (Report) và tiêu đề / bảng biểu.

---

## 🚫 QUY TẮC HẠN CHẾ VẼ ẢNH & SƠ ĐỒ (MINIMAL VISUALS RULE)

- **TUYỆT ĐỐI KHÔNG tự ý sinh/vẽ ảnh:** Không dùng công cụ sinh ảnh, không tạo hình ảnh minh họa trừ khi có yêu cầu rõ ràng từ người dùng.
- **Hạn chế tối đa sơ đồ (Diagrams) trong câu trả lời thông thường:** Không chèn sơ đồ luồng/quy trình rườm rà vào các câu trả lời phân tích trao đổi hàng ngày. Ưu tiên **Bảng biểu Markdown (Tables)** và **Gạch đầu dòng phân tích trực diện, sắc sảo**.
- **Phạm vi duy nhất cho phép dùng Mermaid:** Chỉ sử dụng Mermaid `graph TD` / `graph LR` khi viết tài liệu đặc tả luồng người dùng (User Flow) trong các file BRD/PRD chính thức.

---

## 📊 QUY CHUẨN AGENDA BÁO CÁO THÁNG WEB PLATFORM (MONTHLY BUSINESS REVIEW STANDARD)

Khi người dùng yêu cầu viết **Monthly Report cho Web Platform**, AI Agent **BẮT BUỘC** áp dụng chính xác **Agenda 4 phần chuẩn** sau:

1. **Nguyên tắc vận hành:** *Report để cung cấp thông tin, Meeting để thảo luận và ra quyết định.* Phục vụ CEO và BOM nhận diện nhanh rủi ro trọng yếu và ra quyết định điều hành.
2. **Gắn nhãn phân loại:** 
   - `[R] – Reporting`: Cung cấp thông tin & kết quả hoạt động; dùng cho pre-read, không trình bày lại trong cuộc họp.
   - `[D] – Discussion`: Nội dung có vấn đề cần thảo luận, xin ý kiến alignment, cần hỗ trợ hoặc ra quyết định (trọng tâm cuộc họp).
3. **Agenda 4 phần chuẩn mực cho Web Platform:**
   - **Phần 1: Product & Business Performance `[R]`:** 
     - Bảng theo dõi mục tiêu và thực tế (Target vs. Actual) chuẩn 6 dòng chỉ số: `Total page views (target)`, `% Growth Rate (target)`, `Total page views (Actual)`, `Net add`, `% Growth Rate`, `% Target Rate`.
     - **Nguyên tắc "So What?" (Không đọc lại số liệu):** Tuyệt đối không diễn giải lại các con số người đọc đã nhìn thấy trong bảng. Phần phân tích bắt buộc tập trung vào kết quả thực chất: bản chất sự dịch chuyển lưu lượng, nguyên nhân cốt lõi đằng sau sự tăng/giảm, rủi ro đánh đổi và hành động điều chỉnh chiến lược.
   - **Phần 2: Cinema / Financial `[R]`:** 
     - Chi tiết hiệu suất của 2 dự án trọng điểm lớn nhất (Cinema Hub và Financial Hub).
     - Với từng dự án: Chi tiết số liệu hiệu suất, Key Highlights đạt được trong tháng, Next Actions cho tháng tới.
   - **Phần 3: New User `[R]`:** 
     - Mô tả luồng Ads (Paid Search, Ads Campaigns) và phễu Web-to-App.
     - Số lượng Installs, New Registered Users (New Reg), Mapbank, MAU bóc tách theo từng chiến dịch (dữ liệu AppsFlyer GPD).
   - **Phần 4: Discussion Topics `[D]`:** 
     - Các chủ đề trọng tâm cần đưa ra thảo luận trong cuộc họp (tối đa 0–2 topics).
     - Cấu trúc chuẩn 3 phần: `Problem Statement` ➔ `Status / Issues` (kèm số liệu data points) ➔ `Recommendations`.
4. **Quy định trình bày:**
   - Tuyệt đối không dùng Emoji/Icon; không dùng tên riêng cá nhân/PIC (thay bằng tên đội ngũ chuyên môn).
   - Không đưa phần CX, không đưa chỉ số kỹ thuật sâu (CWV, P90, 4xx/5xx), không đưa Ticket tồn đọng.
   - **Định vị kênh cốt lõi:** **Organic là kênh chủ lực và mang lại giá trị thực chất nhất của Web Platform**. Tuyệt đối **không tô điểm cho Paid**, không xem việc đốt tiền Paid là thành tích tăng trưởng. Paid tăng mà Organic giảm là tín hiệu cảnh báo rủi ro về độ lành mạnh của nền tảng Web.
   - **Tiêu đề gạch đầu dòng (Bullet Lead-ins):** Sử dụng thuật ngữ tiếng Anh ngắn gọn, chuẩn Product Lead (ví dụ: `Target Overachievement:`, `Direct Traffic & Brand Strength:`, `SEO to GEO Transition:`, `Key Highlights:`, `Next Actions:`...) để thay thế cho các câu mở đầu tiếng Việt dài dòng.
   - Không lặp lại số liệu thô; tập trung diễn giải ý nghĩa kinh doanh, bài học và quyết định vận hành.
   - Đảm bảo quyền truy cập cho Ban Giám Đốc và các đầu mối tổng hợp (`tuong.nguyen`, `tram.phan1`, `nga.nguyen1`).

