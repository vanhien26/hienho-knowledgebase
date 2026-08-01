# PRODUCT REQUIREMENT DOCUMENT (PRD) - WEB CHANNEL

*Yêu cầu Cell Team điền đầy đủ thông tin cốt lõi dưới đây và gửi cho Web Platform Team trước khi triển khai.*

## 📋 THÔNG TIN CHUNG (Metadata)
> *   **Tên dự án / Sản phẩm (PRODUCT NAME):** Nền tảng Điều phối Chiến lược Nội dung MoSpark (MoSpark - PLG Project Platform)
> *   **Đầu mối Cell Team (PO & Tech Lead):** Trọng (Technical Owner) · Hiến HV (Product Lead)
> *   **Web Product Lead (Duyệt dự án):** Hien.ho
> *   **Trạng thái tài liệu (Document status):** DRAFT
> *   **Tiến độ dự kiến:** Go-Live Q4/2026
> *   **Loại yêu cầu:** [x] Tính năng mới | [ ] Cải tiến/Thay đổi cấu trúc

## I. TÀI LIỆU LIÊN QUAN (References)
*   **Figma Design:** [Chèn link thiết kế UI/UX Dashboard SEO/GEO tại đây]
*   **Tài liệu chiến lược SEO/GEO gốc:** [mospark_plg_project.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/mospark_plg_project.md)
*   **Bản đồ tài nguyên SEO:** [mospark_seo_inventory.md](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/04_MOSPARK_PLATFORM/mospark_seo_inventory.md)

---

## II. BỐI CẢNH & MỤC TIÊU (Why & What)

### 1. Bối cảnh & Vấn đề (Context & Pain points)
*   **Bối cảnh:** Hệ sinh thái Web MoMo (momo.vn) đang đón nhận hàng triệu traffic tự nhiên ngoài ứng dụng (Out-App Search Traffic). Để tối ưu hóa nguồn tài nguyên này và chuyển đổi thành người dùng hoạt động trong App (MAU), GPD xây dựng hạ tầng tăng trưởng Web MoSpark với "Tổng hành dinh" điều phối là **PLG Project Platform**.
*   **Vấn đề:**
    *   Quy trình lên kế hoạch từ khóa, theo dõi tiến độ viết bài và quản lý Topic Clusters trước đây thực hiện thủ công trên Excel/Google Sheets, gây phân mảnh dữ liệu.
    *   Tình trạng trùng lặp từ khóa (Keyword Cannibalization) xảy ra giữa các use case/BU khác nhau, làm giảm hiệu quả xếp hạng SEO trên Google Search.
    *   GenAI Content Engine thiếu bối cảnh nghiệp vụ (Business Context) và cấu hình prompt cục bộ cho từng dự án, dẫn đến việc sinh nội dung không chính xác hoặc vi phạm các từ cấm pháp lý (Blacklist).
    *   Cấu trúc phẳng hiện tại không đáp ứng được mô hình quản lý thực thể phân tán quy mô lớn (>10,000 đối tác) của Merchant O2O.

### 2. Mục tiêu dự án & Chỉ số đo lường (KPIs)
*   Thành công của dự án đo lường bằng việc tự động hóa quy trình quản lý từ khóa, lập kế hoạch nội dung và nâng cao hiệu năng vận hành & chuyển đổi W2A của Web Channel.

| Chỉ số (KPI) | Hiện tại (Baseline) | Mục tiêu (Target) | Thời gian đo |
| :--- | :--- | :--- | :--- |
| **Tỷ lệ bài viết trùng lặp từ khóa** | ~15% | 0% (Hệ thống tự động block trùng lặp từ đầu vào) | Q3/2026 |
| **Tốc độ phê duyệt Outline** | 20 phút / bài viết (Thủ công) | < 2 phút / bài viết (Nhấp duyệt trực tiếp trên UI) | Q3/2026 |
| **Khả năng quản lý đối tác (Merchant)** | Chỉ hỗ trợ trang tĩnh | Hỗ trợ quản lý >10,000 thực thể đối tác phân tán | Q4/2026 |
| **Lưu lượng traffic quản lý** | Phân mảnh trên nhiều file Excel | Quản lý tập trung >10M traffic/tháng trên Web | Q4/2026 |

---

## III. TRẢI NGHIỆM NGƯỜI DÙNG & TÍNH NĂNG (User Experience & Features)

### 1. Khách hàng mục tiêu & Nhu cầu (Target Users & Intent)
*   **Họ là ai?**
    *   **Admin (PM/Growth Lead):** Cần thiết lập dự án, cấu hình Business Context, tùy biến local prompt và quản lý API keys riêng biệt cho từng BU để kiểm soát chi phí và bảo mật.
    *   **Editor (Content Creator):** Cần xem danh sách Topic Clusters, quản lý tiến độ từ khóa, và thực hiện viết bài bằng GenAI qua 2 Layer mà không cần cấu hình hệ thống.
    *   **End-User (Khách hàng):** Cần tra cứu thông tin tiện ích (Phạt nguội, Giá vàng, Merchant...) ngoài App và dễ dàng chuyển đổi vào App MoMo qua các điểm chạm (W2A).

### 2. Luồng trải nghiệm & Đặc tả tính năng
*   **Quy trình Cài đặt & Vận hành Dự án:**
    *   *Bước 1:* Tạo tên dự án.
    *   *Bước 2:* PM nhập bối cảnh nghiệp vụ (Markdown), SEO Inventory, URL gốc và API Keys riêng biệt.
    *   *Bước 3:* PM upload tệp CSV chứa danh sách từ khóa phân vai trò (Primary/Secondary) và ánh xạ nội dung.
    *   *Bước 4:* PM thiết lập local prompt riêng (Outline & Writer Prompt) hoặc chọn template mẫu.
    *   *Bước 5:* Tiến hành viết bài qua 2 Layer (AI sinh Outline $\rightarrow$ PM sửa/duyệt $\rightarrow$ AI viết bài chi tiết).

| Tính năng / Widget | Mô tả chi tiết (User Story / Logic) | Luồng chuyển đổi sang App (CTA & Deeplink) |
| :--- | :--- | :--- |
| **Project Workspace (Cấu hình)** | PM cấu hình Business Context (Markdown), thiết lập local prompt riêng biệt và quản lý API keys riêng (Gemini key, Google Ads/GSC token...). API keys lưu trữ bắt buộc phải mã hóa và ẩn trên UI. | N/A (Trang quản trị nội bộ) |
| **Hierarchical Accordion Table Grid** | Giao diện cây thư mục 3 tầng (Topic -> Cluster -> Keyword). Dòng Cha (Merchant/Cluster) hiển thị tổng quan volume/trạng thái. Bảng Con hiển thị chi tiết từ khóa, vai trò (Primary/Secondary) và Mapping Type (`new_page` cho Primary hoặc `merge_page` cho Secondary để gộp thành H2/H3 tránh trùng lặp từ khóa). | N/A (Trang quản trị nội bộ) |
| **Outline Review Tool (Layer 1)** | Khi bấm `Sinh Outline`, AI tạo bộ khung dàn ý (Heading, bullet points). Editor có thể sửa Heading, thêm/bớt ý chính và chèn Business Instruction cho AI trước khi duyệt. | N/A (Trang quản trị nội bộ) |
| **GenAI Writer Engine (Layer 2)** | Sau khi Outline được duyệt, AI tự động viết bài viết chi tiết bám sát 100% dàn ý đã duyệt và xuất bản nháp lên Web. | N/A (Trang quản trị nội bộ) |
| **Merchant Page Pipeline** | Làm giàu dữ liệu đối tác: Tự động lấy dữ liệu từ M4B, cào Google Maps API (menu, reviews, amenities) tạo thành Merchant Context cho GenAI Content Engine. | Tích hợp QR code tại quầy mở Web Merchant; Trên Web chèn các nút CTA (W2A Trigger Points) chứa Deep Link mở App MoMo chính xác cửa hàng để thanh toán/trả sau (`momo://app/merchant?id={merchant_id}`). |

---

## IV. TÍCH HỢP KỸ THUẬT & VẬN HÀNH (Technical & Operations)

### 1. Dữ liệu & API tích hợp
*   **Vertex AI / Gemini API:** API chính để chạy GenAI Engine sinh Outline & bài viết.
*   **Google Ads API (Keyword Planner) & GSC API:** Đồng bộ tự động lượng tìm kiếm (Search Volume) hàng tháng và CTR/Thứ hạng của từ khóa.
*   **M4B API & Google Places API:** Đồng bộ thông tin cửa hàng thực tế, menu phục vụ dự án phân tán (Merchant).
*   **Phương án xử lý lỗi (Fallback Logic):**
    *   *API đối tác/Merchant:* Sử dụng dữ liệu tĩnh được sao lưu tại CMS nếu API đối tác bị nghẽn hoặc timeout > 3s.
    *   *API Google Ads:* Sử dụng API Ahrefs/Semrush làm kênh dự phòng để đồng bộ volume nếu API Google Ads bị Rate Limit.

### 2. Kênh vận hành & Rủi ro
*   **Đồng bộ dữ liệu nội dung:** [x] Đồng bộ lên AI Assistant / Chatbot | [x] Đồng bộ lên Help Center (FAQ) | [x] Hiển thị trên Web.
*   **Rủi ro chính & Cách khắc phục:**

| Rủi ro (Risk) | Mức độ | Phương án khắc phục | Người chịu trách nhiệm |
| :--- | :--- | :--- | :--- |
| **Xung đột URL giữa các Use Cases** | Cao | Áp dụng cấu trúc Silo URL nghiêm ngặt (`/{use-case}/blog/...`) tự động gán tiền tố theo Microsite mapping 1-1. | Tech Lead |
| **PM sửa Master Prompt làm lỗi hệ thống** | Cao | Áp dụng cơ chế clone cục bộ (Project-specific Localized Prompt). PM chỉ được sửa prompt cục bộ của dự án mình, cấm sửa Master Template. | System Admin |
| **API Google Ads bị quá tải / Rate Limit** | Trung bình | Tích hợp Ahrefs/Semrush làm fallback và đồng bộ định kỳ hàng tháng (Monthly Sync) thay vì real-time. | Tech Lead |
| **API Keys của từng dự án bị lộ** | Cao | Bắt buộc mã hóa API Keys dưới Database (Encryption at Rest) và hiển thị masked format trên UI. | Tech Lead |

---

## LỊCH SỬ THAY ĐỔI (Changelog)

| Phiên bản | Ngày cập nhật | Người thực hiện | Nội dung thay đổi |
| :--- | :--- | :--- | :--- |
| 2.0 | 2026-07-10 | Web Product Lead | Tái cấu trúc tài liệu từ file chiến lược `mospark_plg_project.md` sang định dạng PRD tinh gọn theo đúng mẫu `_template-prd.md`. |
