# MoSpark - RAG Knowledge Base Architecture
Hệ thống Quản trị Tri thức Tập trung & Truy xuất Cơ sở Dữ liệu MoMo

> - **Project:** MoSpark Web Platform
> - **Division:** GPD (Growth Product Division)
> - **Product:** Web Growth Platform
> - **Governance:** Văn Hiến (Web Product Lead)
> - **Version:** 1.0 · June 2026
> - **Status:** Proposal - Core Knowledge Engine

---

## 1. Executive Summary

### 1.1. Tầm nhìn & Mục tiêu (Vision & Objectives)
Để các bài viết và trang nội dung do GenAI hoặc biên tập viên tạo ra trên MoSpark luôn đạt độ chính xác tối đa, không bị ảo giác thông tin (Hallucination), và đồng nhất với các chính sách của MoMo, hệ thống cần một **Cơ sở Tri thức Tập trung (RAG Knowledge Base)**. 

Thay vì quản lý ngữ cảnh phân mảnh ở từng dự án, RAG Knowledge Base hoạt động như một lớp hạ tầng độc lập. Nó lưu trữ toàn bộ dữ liệu sản phẩm, dịch vụ của MoMo, các quy chuẩn thương hiệu, và cả những nội dung lịch sử do GenAI tạo ra. Khi cần thiết, hệ thống sẽ sử dụng cơ chế **Truy xuất Thông tin tăng cường (Retrieval-Augmented Generation)** để cung cấp ngữ cảnh chuẩn xác nhất cho các tác vụ sinh nội dung hoặc giải đáp người dùng.

### 1.2. Mối quan hệ trong Hệ sinh thái MoSpark
RAG Knowledge Base đóng vai trò là "Kho tri thức gốc" (Source of Truth), liên kết trực tiếp với các cấu phần khác của MoSpark:
*   **GenAI Content Engine (Factory):** Truy xuất các quy chuẩn viết bài và thông tin sản phẩm để nhúng vào Prompt trước khi gọi LLM.
*   **Microsite / CMS Page Editor:** Đọc dữ liệu từ RAG để điền thông tin tự động (Auto-fill) hoặc gợi ý chèn liên kết chéo (Cross-linking).
*   **Chatbot & Assistant:** Sử dụng RAG để trả lời các câu hỏi thực tế của khách hàng về sản phẩm/dịch vụ trên các trang đối tác (Merchant) hoặc trang tiện ích.

---

## 2. Nguồn Dữ Liệu Nạp Vào (Knowledge Sources)

Hệ thống RAG được thiết kế để bao phủ toàn bộ tài sản dữ liệu tĩnh và động của MoMo, bao gồm 4 nhóm tài nguyên lớn:

```
+-------------------------------------------------------------------------+
|                        RAG KNOWLEDGE SOURCES                            |
+-------------------------------------------------------------------------+
|                                                                         |
| 1. Quy chuẩn toàn cục (Global Standards):                                |
|    - Brand Guideline (Tone of Voice, Xưng hô)                           |
|    - Design System (MoBase UI/UX Rules, Headings)                       |
|    - SEO & Content Principles (E-E-A-T, YMYL)                           |
|                                                                         |
| 2. Dữ liệu sản phẩm & dịch vụ (MoMo Product Catalogue):                 |
|    - Tài chính (Vay Nhanh, Ví Trả Sau, CIC, Tiết Kiệm)                  |
|    - Tiện ích (Thanh toán hóa đơn, Vé xem phim, Mua sắm)                |
|    - API Docs & Vận hành từ các Cell Teams                              |
|                                                                         |
| 3. Dữ liệu đối tác (Merchant Project):                                  |
|    - Địa chỉ, Giờ mở cửa, Tiện ích, Quy định thanh toán                 |
|                                                                         |
| 4. Dữ liệu sinh ra bởi GenAI (Historical Outputs):                      |
|    - Bài viết Blog, Landing Pages, FAQs đã được xuất bản                |
|                                                                         |
+-------------------------------------------------------------------------+
```

---

## 3. Kiến Trúc Kỹ Thuật & Luồng Xử Lý (RAG Processing Pipeline)

Hệ thống RAG được triển khai dưới sự phụ trách của **Duy (Senior BE Developer)** với kiến trúc 4 bước tiêu chuẩn:

```
[Ingestion] (Markdown/PDF/APIs) 
     |
     v
[Chunking] (Semantic/Recursive, size: 512 tokens)
     |
     v
[Embedding] (text-embedding-3-small)
     |
     v
[Vector Database] (Supabase pgvector)
```

### 3.1. Phân mảnh Tài liệu (Semantic Chunking)
Hệ thống sử dụng giải thuật phân mảnh đệ quy (Recursive Character Text Splitter) kết hợp phân mảnh theo ngữ nghĩa (Semantic Chunking) để đảm bảo các khối dữ liệu (chunks) không bị mất ngữ cảnh gốc.
*   *Chunk Size tối ưu:* 512 tokens.
*   *Overlap Size:* 64 tokens (để nối ngữ cảnh giữa các đoạn liền kề).

### 3.2. Vector hóa & Lưu trữ (Embeddings & Database)
*   **Embedding Model:** Sử dụng model `text-embedding-3-small` (hoặc `cohere-embed-multilingual-v3`) để tối ưu hóa khả năng hiểu ngữ nghĩa tiếng Việt đa ngành hàng.
*   **Vector Database:** pgvector tích hợp trực tiếp trên Supabase database hiện tại của MoSpark để tối ưu hóa chi phí vận hành và đồng bộ dữ liệu nhanh với CMS.

---

## 4. Cơ Chế Truy Xuất Động (Retrieval & Query Orchestration)

Khi một tác vụ sinh nội dung (Outline/Detail Generator) hoặc một câu hỏi từ Chatbot được kích hoạt, hệ thống sẽ thực hiện quy trình truy xuất 3 lớp:

```
                  +-----------------------------------------+
                  |  Tác vụ sinh bài viết / Câu hỏi User    |
                  +-----------------------------------------+
                                       | (Trích xuất Keyword & Embedding)
                                       v
                  +-----------------------------------------+
                  |       Tìm kiếm độ tương đồng (RAG)      |
                  |          (Supabase pgvector)            |
                  +-----------------------------------------+
                                       |
                   +-------------------+-------------------+
                   | (Độ khớp > 0.75)                      | (Độ khớp < 0.75)
                   v                                       v
+-------------------------------------+  +-------------------------------------+
|    Lọc theo Metadata của Project    |  |       Fallback về Google Search     |
|   (Lấy Brand + Product Chunks)      |  |          (Grounding Search)         |
+-------------------------------------+  +-------------------------------------+
                   |                                       |
                   +-------------------+-------------------+
                                       v
                  +-----------------------------------------+
                  |   Bơm vào Context Layer gửi đến LLM    |
                  +-----------------------------------------+
```

### 4.1. Thuật toán tìm kiếm tương đồng (Similarity Search)
Hệ thống tính toán khoảng cách Cosine Similarity giữa Vector câu truy vấn và cơ sở dữ liệu Vector DB.
*   **Ngưỡng lọc (Threshold):** Đặt ở mức $0.75$. Các đoạn có điểm tương đồng dưới $0.75$ sẽ bị loại bỏ để tránh nạp dữ liệu rác.
*   **Giới hạn truy xuất (Top-K):** Lấy tối đa $Top-5$ chunks liên quan nhất cho mỗi lượt sinh nội dung.

### 4.2. Bơm Ngữ Cảnh Tự Động (Inference Context Injection)
Hệ thống biên dịch prompt động bằng cách gộp các chunks tìm được vào Prompt gửi sang LLM:
$$\text{Final System Prompt} = \text{Project-Specific System Prompt} + \text{RAG Brand Guideline Chunks}$$
$$\text{Final User Prompt} = \text{Business Context} + \text{RAG Product Specs Chunks} + \text{Primary Keyword}$$

### 4.3. Gợi ý Chèn Liên Kết Chéo (RAG Cross-linking Recommendation)
Khi viết một bài mới (ví dụ: *Cách đăng ký phạt nguội qua momo*), RAG Engine sẽ quét cơ sở dữ liệu các bài viết hiện hữu:
*   Phát hiện các bài liên quan (ví dụ: *Quy định nộp phạt nguội xe máy*, *Cách đăng ký Ví Trả Sau*).
*   Tự động xuất danh sách các URL gợi ý chèn Internal Link vào CMS Editor để PM phê duyệt. Điều này ngăn chặn việc bỏ sót link juice và tối ưu hóa SEO Silo Structure.

---

## 5. Yêu Cầu Giao Diện Quản Trị RAG trên Web (UI/UX Specification)

Nằm trong phân hệ cấu hình nâng cao của Admin Panel MoSpark:

### 5.1. Màn hình Quản lý Nguồn Tri thức (Knowledge Center Dashboard)
*   **Trình tải lên tài liệu (Ingestion Panel):** 
    *   Hỗ trợ kéo thả các file định dạng `.md`, `.pdf`, `.docx`.
    *   Ô nhập URL để crawl dữ liệu tự động từ các trang hướng dẫn của MoMo (ví dụ: `momo.vn/huong-dan-thanh-toan`).
*   **Trình kết nối API (API Connectors):** Nơi cấu hình để đồng bộ dữ liệu thời gian thực từ các Cell Teams.
*   **Bảng giám sát Chỉ mục (Vector Indexing Dashboard):**
    *   Hiển thị danh sách tài liệu đã index.
    *   Số lượng chunks được sinh ra từ mỗi tài liệu.
    *   Trạng thái index (Success / Pending / Error).

### 5.2. RAG Playground (Khu vực thử nghiệm)
*   Giao diện hộp chat giả lập để PM hoặc Developer gõ thử câu hỏi/từ khóa.
*   Hệ thống sẽ hiển thị danh sách các Chunks được truy xuất kèm theo điểm số tương đồng (Similarity Score) và nguồn gốc tài liệu (Source file/URL).
*   Giúp tối ưu hóa các tham số cắt đoạn (Chunk size) và ngưỡng lọc (Threshold) trước khi chạy thực tế.

---

## 6. Quy Tắc Kỹ Thuật & Bảo Mật Dữ Liệu (Technical & Security Constraints)

### 6.1. Quản lý Quyền Truy cập (RBAC Matrix)
*   **System Admin / Tech Lead (Duy/Bảo):** Quyền CRUD đối với tất cả Knowledge Sources, điều chỉnh cấu hình Chunking và Embedding.
*   **Product Manager (PM):** Xem danh sách tài liệu, chạy RAG Playground, upload tài liệu bổ sung cho dự án của mình (Project-level Knowledge).
*   **Content Writer:** Quyền đọc dữ liệu thông qua các prompt tự động, không có quyền upload trực tiếp tài liệu hệ thống.

### 6.2. Bảo Mật Thông Tin & Loại Bỏ Dữ Liệu Nhạy Cảm (Data Scrubbing)
*   **Nguyên tắc Zero PII (Personally Identifiable Information):** RAG Knowledge Base chỉ được lưu trữ thông tin sản phẩm, chính sách và cẩm nang thương hiệu. Tuyệt đối không lưu trữ thông tin khách hàng, số điện thoại, số tài khoản hoặc lịch sử giao dịch cá nhân.
*   **Hậu kiểm tự động:** Hệ thống chạy bộ lọc regex và các model NER (Named Entity Recognition) để tự động bóc tách/mã hóa các chuỗi ký tự nghi ngờ là thông tin cá nhân trước khi thực hiện vector hóa.

---

## 7. Tài liệu Liên kết (Related Documents)
*   **Platform Master:** [MoSpark Master Doc](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_master.md)
*   **SEO/GEO Project Hub:** [MoSpark SEO/GEO Project Hub](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_seo_geo_project.md)
*   **GenAI Production Lab:** [MoSpark GenAI Content Engine](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_genai_content.md)

---
*Maintained by: Văn Hiến (Web Product Lead) | Technical Lead: Duy (Senior BE Developer)*
