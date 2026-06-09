# MoSpark - SEO/GEO Project
Trung tâm Điều phối Chiến lược Nội dung

> - **Project:** MoSpark Web Platform
> - **Division:** GPD (Growth Product Division)
> - **Product:** Web Growth Platform
> - **Document ID:** `mospark-seo-geo-project`
> - **Governance:** Văn Hiến (Web Product Lead)
> - **Version:** 1.0 · June 2026
> - **Status:** Active - Core Strategy Hub

---

## 1. Executive Summary

### 1.1. Tầm nhìn (Vision)
SEO/GEO Project đóng vai trò là "Tổng hành dinh" (Management Hub) của toàn bộ chiến dịch nội dung trên MoMo.vn. Đây là nơi tiếp nhận dữ liệu thị trường từ hệ thống SEO Inventory, cấu trúc lại thành chiến lược nội dung cụ thể, và điều phối quy trình sản xuất thông qua GenAI Content Engine.

### 1.2. Mối quan hệ kiến trúc (The Triad Architecture)
Hệ thống MoSpark vận hành dựa trên "kiềng 3 chân" được kết nối trực tiếp bởi SEO/GEO Project:

1. **[SEO Inventory](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_seo_inventory.md) (Data Source):** Nơi chứa Market Volume, SOV, và phân tích rào cản. Cung cấp dữ liệu "thô" về thị trường.
2. **SEO/GEO Project (The Brain):** Nơi tổ chức lại Market Data thành cấu trúc phân cấp, quy hoạch chiến lược (Topic -> Cluster -> Keyword) và thiết lập mapping 1-1 với Microsite.
3. **[GenAI Content Engine](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_genai_content.md) (The Factory):** Nơi nhận các từ khóa đã được chỉ định từ Hub này để bắt đầu sản xuất nội dung tự động.

---

## 2. Kiến trúc Phân cấp Nội dung (Content Strategy Structure)

Giao diện cốt lõi của SEO/GEO Project được thiết kế dưới dạng cây thư mục 3 tầng, giúp Product Manager (PM) dễ dàng quản lý khối lượng lớn nội dung:

### 2.1. Cấu trúc Topic -> Cluster -> Keyword
*   **Tầng 1: TOPIC (Chủ đề lớn)**
    *   *Định nghĩa:* Là các nhóm chủ đề cốt lõi, thường tương ứng với một góc độ sản phẩm hoặc một nhu cầu bao quát của người dùng (Customer Journey: TOFU/MOFU/BOFU).
    *   *Ví dụ:* `Phương Tiện`.
    *   *Thông số hiển thị:* Tổng Volume của toàn bộ Topic.

*   **Tầng 2: CLUSTER (Nhóm từ khóa)**
    *   *Định nghĩa:* Các cụm chủ đề con nằm trong Topic, tập trung giải quyết một Search Intent cụ thể. Các bài viết sinh ra từ một Cluster phải có sự liên kết nội bộ (Internal Link) chặt chẽ với nhau.
    *   *Ví dụ:* (Topic: Phương Tiện) -> Cluster: `Phạt nguội xe máy`, `Phạt nguội ô tô`.
    *   *Thông số hiển thị:* Tổng Volume của Cluster.

*   **Tầng 3: KEYWORD (Từ khóa mục tiêu)**
    *   *Định nghĩa:* Là hạt nhân cơ sở nhất. Mỗi Keyword tương ứng với **1 bài viết duy nhất** (bảo vệ bằng Unique ID Check) được sinh ra để xếp hạng trên Google/AI Search.
    *   *Ví dụ:* (Cluster: Phạt nguội xe máy) -> Keyword: `phạt nguội xe máy online`, `app phạt nguội xe máy`, `check phạt nguội xe máy`...
    *   *Thông số hiển thị chi tiết (Data Table):*
        *   **Trend (Biểu đồ):** Xu hướng tìm kiếm 12 tháng.
        *   **Trending (Tag):** Gắn cờ các từ khóa đang lên.
        *   **Volume:** Lượng tìm kiếm trung bình tháng.
        *   **CPC:** Giá thầu quảng cáo (phản ánh giá trị thương mại).
        *   **Word Count:** Độ dài trung bình của câu truy vấn.

### 2.2. Cơ chế Điều phối Từ khóa (Keyword Routing Mechanism)

Hệ thống phân loại và điều phối Keyword về đúng kênh sản xuất dựa trên **Search Intent (Ý định tìm kiếm)** và **Mức độ ưu tiên**.

#### A. Phân loại Cấp phát Trang đích (Destination Routing)
Mỗi Keyword sẽ được gán 1 trong 2 luồng định tuyến:

1.  **Luồng 1: Điều phối về Landing Page / Tool Page (LDP Builder M1)**
    *   *Tiêu chí:* Từ khóa mang tính **Giao dịch (Transactional)**, tìm kiếm công cụ, tính năng hoặc có tỷ lệ chuyển đổi Web-to-App cao. Đòi hỏi UI/UX tùy chỉnh.
    *   *Ví dụ:* `Kiểm tra phạt nguội ô tô`, `Tra cứu phạt nguội toàn quốc`.
    *   *Hành động:* Gửi tín hiệu đến Landing Page Builder. Trang này sẽ đóng vai trò là Hub (Trang đích chính) để hứng Traffic chuyển đổi.

2.  **Luồng 2: Điều phối về Blog Article (GenAI Content Engine M2)**
    *   *Tiêu chí:* Từ khóa mang tính **Thông tin (Informational)**, giáo dục, giải đáp. Phục vụ mục đích kéo Traffic dải rộng.
    *   *Ví dụ:* `Lỗi vượt đèn đỏ phạt bao nhiêu`, `Phân biệt lỗi sai làn`.
    *   *Hành động:* Gửi lệnh sản xuất hàng loạt sang GenAI Content Engine. Các trang này đóng vai trò là Spoke (Trang vệ tinh) bắn Internal Link về Hub.

#### B. Tiêu chuẩn Hóa Prompt (Single SEO/GEO Prompt)
Để tối ưu hóa tốc độ vận hành và đảm bảo chất lượng đầu ra luôn đồng nhất, hệ thống **không yêu cầu** PM/PO phải cấu hình phức tạp (chọn Format, Funnel hay Tone giọng) cho từng Keyword. 

Thay vào đó, tất cả các Keyword được điều phối về luồng Blog sẽ sử dụng **1 Prompt Template Tiêu chuẩn duy nhất (Universal SEO/GEO Prompt)**. 

*   *Cơ chế hoạt động:* Prompt duy nhất này đã được đội ngũ Content & SEO "Hard-code" sẵn các nguyên tắc khắt khe nhất (cách đặt Heading, mật độ từ khóa, cách chèn Internal Link). GenAI Engine sẽ tự động phân tích Keyword được truyền vào để linh hoạt điều chỉnh văn phong và định dạng bài viết.
*   *Lợi ích:* 
    *   Trải nghiệm "1-Click": PM chỉ cần chọn Keyword và bấm tạo, không cần thiết lập Parameter.
    *   Đảm bảo 100% bài viết sinh ra đều pass qua vòng chấm điểm của hệ thống SEO/GEO Scoring System.

---

## 3. Quản trị Định tuyến và Microsite Mapping

SEO/GEO Project đóng vai trò gác cổng (Gatekeeper) đối với hệ thống URL của MoSpark. 

### 3.1. Ràng buộc Mapping 1-1
Mỗi SEO/GEO Project bắt buộc phải được gắn với **chính xác 1 Microsite** (ví dụ: `mospark-vay-nhanh` gắn với Microsite Vay Nhanh). 

### 3.2. Thực thi URL Routing (`/{use-case}/blog*`)
*   Toàn bộ Keyword được chọn để sản xuất bài viết từ Project này sẽ tự động được gán tiền tố đường dẫn kế thừa từ Microsite.
*   *Ví dụ:* Từ khóa `điều kiện vay nhanh` sinh ra bài viết sẽ có URL tự động là `/vay-nhanh/blog/dieu-kien-vay-nhanh`.
*   *Mục đích:* Tránh xung đột URL giữa các Use Case, giữ cấu trúc Silo chuẩn SEO.

---

## 4. Luồng Vận hành Sản xuất (The 2-Layer Generation Flow)

Để kiểm soát chất lượng tuyệt đối và định hướng nội dung đúng mục tiêu kinh doanh, bất kỳ một Keyword nào khi chạy qua GenAI đều bị ép buộc tuân thủ quy trình **"Human-in-the-loop" (Có bàn tay con người can thiệp)** qua 2 Layer sản xuất:

### Bước 1: Setup Strategy (Thiết lập ban đầu)
1.  PM tiếp nhận dữ liệu báo cáo từ **SEO Inventory**.
2.  Quy hoạch các Keyword vào cấu trúc **Topic -> Cluster**.

### Bước 2: Layer 1 - Sinh Dàn bài (Outline Generation)
1.  PM chọn các Keyword cần triển khai trong Sprint.
2.  Kích hoạt lệnh `Generate Outline`.
3.  GenAI Engine sử dụng Universal Prompt để phân tích Keyword và trả về một bộ Khung Dàn ý (Heading 2, Heading 3, các Bullet point ý chính). *Quá trình này diễn ra rất nhanh và tốn ít Token.*

### Bước 3: Human Gate - Con người kiểm duyệt (Edit by Human)
1.  Trạng thái Keyword lúc này chuyển thành `Pending Outline Review`.
2.  PM hoặc Content Creator vào xem bản Outline do AI đề xuất. Tại đây, con người đóng vai trò là "Tổng biên tập":
    *   Sửa lại các tiêu đề (Heading) cho thu hút hơn.
    *   Cắt bỏ các ý AI vẽ hươu vẽ vượn không cần thiết.
    *   **Quan trọng nhất:** Chèn thêm các ý định hướng Business (Ví dụ: "Nhớ nhắc đến tính năng trả góp của MoMo ở đoạn này").
3.  Người dùng bấm `Approve Outline` để chốt dàn bài.

### Bước 4: Layer 2 - Sinh Nội dung chi tiết (Content Detail Generation)
1.  Chỉ khi Outline được Approve, hệ thống mới kích hoạt Layer 2: `Generate Content Detail`.
2.  GenAI Engine sẽ bám **chính xác 100%** vào bộ Outline đã được con người duyệt để "đắp thịt" (sinh ra đoạn văn chi tiết, chèn bảng biểu, Internal Link).
3.  Bài viết hoàn thiện được trả về trạng thái `Ready to Publish` trên bảng quản lý của Project.

---

## 5. Tài liệu Liên kết
*   **Data Source:** [MoSpark SEO Keyword Inventory](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_seo_inventory.md)
*   **Production Engine:** [MoSpark GenAI Content Engine](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_genai_content.md)

---
*Maintained by: Văn Hiến (Web Product Lead) | Last updated: 2026-06-07*
