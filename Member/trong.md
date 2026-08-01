# **Senior Software Engineer — Strategic & OKRs H2 2026**

**Trọng — Senior Software Engineer (Front-End & Platform Dev) | Trục 1 - Web Platform Team**

---

## **I. STRATEGIC CONTEXT**

### **1.1. Bối cảnh & Vai trò**

Web Platform Division bước vào giai đoạn H2/2026 với 3 mandate chiến lược: **PLG Mandate** (Sản phẩm dẫn dắt tăng trưởng traffic & conversion), **JTBD Mandate** (Giải quyết đúng nhu cầu người dùng) và **AI-Powered Mandate** (Tích hợp AI toàn diện vào quy trình sản xuất & vận hành nội dung).

Với vai trò **Senior Software Engineer (Front-End & GenAI Platform Dev)** thuộc Web Platform Team, Trọng là PIC chịu trách nhiệm kỹ thuật chính (Tech Lead Build Partner) cho **MoSpark GenAI Content Engine**, hệ thống **SEO/GEO Quality Gate** và các **Logic/Text Nodes** trong hệ sinh thái MoSpark Multimodal Studio. 

Trọng làm việc trực tiếp với **Hiến (SEO & Product Lead)** để chuyển hóa các specification, framework SEO/GEO (Checklist, Prompts, Rule Engine) thành các tính năng sản phẩm hoàn chỉnh trên nền tảng MoSpark, phục vụ Content Writers, BU PMs và Cell Teams sáng tạo nội dung chuẩn SEO/GEO tự động với hiệu năng tối ưu.

---

### **1.2. Scope Phụ Trách Cốt Lõi**

| Mảng Công Việc | Nhiệm Vụ & Sản Phẩm Đảm Nhận | Tương Tác / Phối Hợp |
| :--- | :--- | :--- |
| **PLG Project Hub & Multi-Use Case Engine** | • **Giải pháp Kỹ thuật Hub & Multi-Use Cases:** Thiết kế kiến trúc phân cấp Master Hub → Sub-Use Cases (Vehicle Hub, Financial Hub, Student Hub...) trên MoSpark PLG Project.<br>• Quản trị URL Hierarchy (`/{hub}/{use-case}/...`), Cross-Internal Linker giữa các Use Case trong cùng Hub.<br>• Tự động hóa mapping Shared Global Context (của Hub) và Local Context (của Use Case) cho AI. | • Hiến (Web Product Lead)<br>• Duy (BE Data Model & Dynamic Routing)<br>• Thuận (Widget Integration & Tracking) |
| **GenAI Content & Model Routing** | • **Đã hoàn thành:** Tích hợp **OpenRouter API** cho phép sử dụng các AI Model Trung Quốc (Kimi/Moonshot, DeepSeek R1/V3, Qwen) bên cạnh Claude API & OpenAI.<br>• **Next Step (Focus):** Tích hợp và tạo **AI Actions (Video, Audio, Infographic Engine)** trong MoSpark Multimodal Studio.<br>• Lập trình Text & Logic Nodes, kết nối luồng AI Actions tự động.<br>• Xây dựng giao diện biên soạn dàn ý (AI Outline Selection - Hard Gate) và sinh nội dung đa phương tiện chuẩn SEO/GEO. | • Hiến (Product Spec & Prompts)<br>• Duy (Backend API & Model Routing)<br>• Thuận (Visual & Layout Nodes) |
| **SEO/GEO Quality Gate** | • Phát triển bộ công cụ rà quét và chấm điểm 5-Block (SEO Onpage, GEO Moat, Technical Performance, E-E-A-T, Conversion UI) real-time trên CMS Editor.<br>• Triển khai cơ chế **Hard Block** (chặn xuất bản khi chưa đạt ngưỡng điểm hoặc vi phạm lỗi kỹ thuật nghiêm trọng). | • Hiến (Scoring Rules & Weights)<br>• Hiếu (CI/CD Quality Gate) |
| **GEO Moat Tools** | • Phát triển module **AI Query Generator** (sinh 20 câu hỏi truy vấn theo Search Intent từ Primary Keyword).<br>• Tự động nén và đồng bộ dữ liệu bài viết xuất bản vào file `llms.txt` cho AI Crawlers (ChatGPT, Perplexity, Claude). | • Hiến (GEO Citation Strategy)<br>• Duy (Crawler & Storage) |
| **Knowledge Base & pSEO** | • Bóc tách dữ liệu có cấu trúc (Structured Data Extraction) từ bài viết và Keyword Tool ("Row") nạp vào Knowledge Space cho Chatbot Phạt Nguội & Merchant Editor.<br>• Tích hợp UI Bulk Generator qua CSV cho các chiến dịch pSEO (Phạt Nguội, eSIM). | • Duy (Vector DB / Knowledge Space)<br>• Lộc (Permission & User Roles) |

---

### **1.3. Working Style & Quy Chuẩn Giao Việc (Input/Output Gate)**

* **Developer Mindset:** Cần Spec rõ ràng (Data Schema, Wireframe/Logic flow, Input/Output API contract) trước khi bắt tay làm (build).
* **Gate Input Bắt Buộc:** Mọi Yêu cầu / Task giao cho Trọng phải đi kèm PRD/Spec chi tiết từ Hiến (Product Lead) hoặc Bảo (Project Lead) bao gồm:
  1. Prompt Format & System Prompts (nếu là tính năng GenAI).
  2. Data Model & API Schema (kết nối Backend Duy).
  3. Acceptance Criteria (AC) & Scoring Rules cụ thể.
* **Output Standard:** Code sạch, bám sát Mobase Component Kits V2, xử lý mượt mà trên Puck Editor / Tiptap Editor, có Unit Test logic cốt lõi và không làm ảnh hưởng đến Core Web Vitals của momo.vn.

---

## **II. VISION CÁ NHÂN & PHƯƠNG CHÂM HÀNH ĐỘNG**

> *"Biến mọi quy trình sáng tạo nội dung phức tạp và checklist SEO/GEO khắt khe thành trải nghiệm AI-Native đơn giản, tự động và chuẩn xác trên MoSpark CMS — giúp người dùng tạo nội dung nhanh gấp 2x nhưng đạt 100% tiêu chuẩn chất lượng xuất bản."*

---

## **III. OKRS H2/2026**

### **Objective 1: Tích hợp OpenRouter & Phát triển AI Actions Đa Phương Tiện (Video, Audio, Infographic)**

***Focus:*** *Tận dụng hạ tầng OpenRouter (vừa hoàn thành cho DeepSeek, Kimi, Qwen) để phát triển bộ **AI Actions Nodes** sinh tài nguyên đa phương tiện (Video, Audio, Infographic/Diagram) tích hợp thẳng vào MoSpark Multimodal Studio.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Trọng (Senior FE/Platform Dev) |
| :---: | :--- | :--- | :--- |
| **KR 1.1 (Done)** | **OpenRouter Multi-Model Integration** | Tích hợp thành công OpenRouter API, hỗ trợ gọi linh hoạt các AI Models hàng đầu Trung Quốc (DeepSeek R1/V3, Kimi/Moonshot, Qwen) cho các tác vụ phân tích, lập luận và sinh văn bản tối ưu chi phí. | • Đã triển khai Model Router & API Handler cho OpenRouter trên MoSpark Platform.<br>• Phối hợp với Duy thử nghiệm benchmark chất lượng output. |
| **KR 1.2 (Next Step)** | **Multimodal AI Actions (Video, Audio, Infographic)** | Phát triển và đóng gói bộ **3 AI Action Nodes** cốt lõi trong MoSpark Multimodal Studio:<br>1. **Video Action Node:** Tự động sinh kịch bản & trigger AI Video Model (Runway/Sora/Pika).<br>2. **Audio Action Node:** Chuyển văn bản sang giọng đọc tự nhiên (TTS / Voiceover Engine).<br>3. **Infographic/Diagram Node:** Bóc tách data/quy trình render Infographic chuẩn MoMo Design System. | • Lập trình UI Component & Action Engine cho 3 loại Action Nodes.<br>• Xây dựng luồng nhận Input từ Text/Logic Node → trigger API Action → render Preview & lưu Media Assets vào CMS Storage. |
| **KR 1.3** | **AI Outline Selection & Workflow Integration** | Triển khai giao diện duyệt dàn ý phân tầng TOFU/MOFU/BOFU. Ép buộc Hard Gate: Bắt buộc PM/Writer bấm **Select Outline** trước khi push sang CMS Page Editor. | • Xây dựng UI Component duyệt Outline cho phép đóng/mở (expand/collapse) các cluster từ khóa.<br>• Triển khai Hard Gate check trên client-side và truyền Payload sang CMS Editor. |

---

### **Objective 2: Xây dựng Hệ thống SEO/GEO Quality Gate & GEO Moat Tools**

***Focus:*** *Đảm bảo 100% bài viết/trang web trước khi xuất bản phải vượt qua Hard Block về điểm SEO/GEO và tự động nuôi dưỡng AI Search Crawlers.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Trọng (Senior FE/Platform Dev) |
| :---: | :--- | :--- | :--- |
| **KR 2.1** | **Real-time 5-Block Scoring Engine & Hard Block** | Phát triển Widget chấm điểm real-time (100 điểm) trực tiếp trên CMS Editor. Tự động **Hard Block** nút Publish nếu tổng điểm `< 80` hoặc vi phạm các lỗi SEO/GEO Critical. | • Lập trình UI Widget Live Score trên thanh công cụ biên soạn bài viết.<br>• Viết logic Linter rà quét từ khóa, mật độ heading, internal link, alt tag, meta tag và trigger Hard Block. |
| **KR 2.2** | **AI Query Generator (GEO Moat)** | Tự động hóa việc sinh 20 query prompts giả lập Search Intent từ Primary Keyword ngay khi bài viết hoàn tất, lưu trữ sẵn vào DB phục vụ đo lường Citation Rate. | • Xây dựng nút trigger và luồng tự động gọi AI sinh 20 queries.<br>• Xây dựng màn hình xem & quản lý bộ AI Query Prompts theo từng bài viết/Use Case. |
| **KR 2.3** | **Auto-compressed llms.txt Sync** | Tự động trích xuất nội dung cốt lõi của bài viết mới xuất bản, nén và cập nhật vào file `llms.txt` của Microsite tương ứng. | • Viết parser trích xuất Markdown từ Rich Text Editor.<br>• Tự động gửi payload nén về hệ thống xuất file `llms.txt` định kỳ. |

---

### **Objective 3: Bóc tách Dữ liệu Cấu trúc (Knowledge Base) & Phục vụ pSEO Factory**

***Focus:*** *Chuẩn hóa dữ liệu bài viết cho Chatbot Knowledge Space và hỗ trợ các chiến dịch sản xuất trang hàng loạt qua CSV.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Trọng (Senior FE/Platform Dev) |
| :---: | :--- | :--- | :--- |
| **KR 3.1** | **Structured Knowledge Base Extraction** | Tự động bóc tách các thực thể (Entities), FAQ, bảng giá, quy trình từ bài viết thành JSON Schema có cấu trúc để nạp vào Vector DB cho Chatbot Phạt Nguội & Merchant. | • Phát triển parser trích xuất JSON-LD / Structured Data từ nội dung bài viết.<br>• Phối hợp với Duy đẩy dữ liệu chuẩn hóa sang Knowledge Space. |
| **KR 3.2** | **pSEO Bulk CSV Upload UI** | Phát triển màn hình Upload CSV & Preview Hàng Luồng Trang pSEO (cho các dự án Phạt Nguội 63 tỉnh thành, SIM Quốc Tế). | • Viết UI component parse CSV client-side, validate trường dữ liệu và hiển thị live preview 5 trang mẫu trước khi kích hoạt sinh trang hàng loạt. |

---

### **Objective 4: Giải Pháp Kiến Trúc PLG Project Cho Các Strategic Hubs Với Đa Use Cases**

***Focus:*** *Thiết lập kiến trúc Hub-and-Spoke phân cấp trên MoSpark PLG Project Hub, hỗ trợ các Hub lớn (Vehicle Hub, Financial Hub, Student Hub, Cinema Hub...) quản lý và sinh nội dung/tiện ích cho nhiều Use Cases bên trong mà không làm vỡ cấu trúc SEO/GEO.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Trọng (Senior FE/Platform Dev) |
| :---: | :--- | :--- | :--- |
| **KR 4.1** | **Master Hub & Sub-Use Cases Hierarchy Schema** | Xây dựng Data Model & UI quản trị phân cấp: 1 Master Hub Project (ví dụ: `Vehicle Hub`) chứa $N$ Sub-Use Cases (`Phạt nguội`, `Giá xăng`, `Trạm sạc EV`, `Đăng kiểm`, `ePass`...). | • Lập trình giao diện tạo và quản lý Hub-and-Spoke Structure trên PLG Project Hub.<br>• Phối hợp với Duy mở rộng Database Schema hỗ trợ Parent-Child Project Relational Mapping. |
| **KR 4.2** | **Context Cascading (Global Hub Context + Local Use Case Context)** | Kế thừa bối cảnh kinh doanh 2 tầng (Cascading Grounding Context): AI Content Generator tự động hòa trộn Shared Global Context từ Master Hub với Local Context của từng Use Case con. | • Viết Context Inheritance Engine trên Frontend trước khi gửi payload sang GenAI Engine.<br>• Tránh trùng lặp USP và đảm bảo đúng định vị thương hiệu của từng Use Case. |
| **KR 4.3** | **Unified Dynamic Routing & Cross-Spoke Internal Linker** | Tự động hóa định tuyến URL 3 cấp: `/{hub_slug}/{usecase_slug}/{content_slug}`. Tự động sinh mạng lưới liên kết nội bộ (Internal Linker) giữa các Use Cases trong cùng 1 Hub. | • Viết Dynamic Routing Component kế thừa Slug từ Master Hub.<br>• Tích hợp Auto Internal Linker gợi ý bài viết/tiện ích chéo trong cùng Hub (ví dụ: Bài Phạt nguội gợi ý Nạp ePass hoặc Mua bảo hiểm xe). |

---

## **IV. KẾ HOẠCH THỰC THI CHI TIẾT (ACTION PLAN H2/2026)**

### **Lộ Trình Triển Khai Kỹ Thuật (H2/2026)**

| Giai Đoạn | Hạng Mục Công Việc | Trạng Thái / Mục Tiêu |
| :--- | :--- | :--- |
| **Sprint 1-2 (Tháng 8)** | • **Done:** OpenRouter API (Kimi, DeepSeek R1/V3, Qwen)<br>• **Active (Next Step):** Multimodal AI Actions (Video, Audio, Infographic Node)<br>• AI Outline Selection Hard Gate | Tích hợp hạ tầng AI Actions & Hard Gate kiểm soát chất lượng |
| **Sprint 3-4 (Tháng 9)** | • 5-Block SEO/GEO Real-time Scoring Widget<br>• Publishing Hard Block Enforcement | Kiểm soát tiêu chuẩn xuất bản và chặn lỗi kỹ thuật |
| **Sprint 5-6 (Tháng 10)** | • AI Query Generator (20 Prompts GEO)<br>• llms.txt Auto-compress & Sync Engine | Xây dựng GEO Moat & tối ưu cho AI Crawlers |
| **Sprint 7-8 (Tháng 11-12)** | • Structured Knowledge Base Extractor (Chatbot)<br>• pSEO Bulk CSV Generator UI | Phục vụ Chatbot Phạt Nguội & chiến dịch pSEO quy mô lớn |

### **Chi Tiết Công Việc Giao Theo Sprint**

#### **Tháng 8/2026: OpenRouter & Multimodal AI Actions Engine (Trọng tâm)**
1. **Task 1.1 (Đã xong):** Tích hợp OpenRouter Router API cho các model Kimi, DeepSeek R1/V3, Qwen.
2. **Task 1.2 (Next Step - Priority 1):** Triển khai **Multimodal AI Action Nodes**:
   - **Video Action Node:** Nhận prompt/script từ Text Node → trigger API Video Generation → render video player preview trên Editor.
   - **Audio Action Node:** Chuyển văn bản bài viết thành file Audio Voiceover (TTS) phát trực tiếp ở đầu bài blog.
   - **Infographic/Diagram Node:** Tự động trích xuất bảng biểu/quy trình từ bài viết thành đồ họa trực quan (Infographic SVG/HTML) theo Mobase UI.
3. **Task 1.3:** Xây dựng màn hình **AI Outline Selection** & Hard Gate kiểm soát chất lượng trước khi xuất bản.

#### **Tháng 9/2026: SEO/GEO Quality Gate & Publishing Control**
1. **Task 2.1:** Xây dựng Widget **Real-time Live Score (5-Block)** gắn trên Sidebar của CMS Editor.
2. **Task 2.2:** Cài đặt logic **Hard Block**: Vô hiệu hóa nút "Publish / Xuất bản" nếu bài viết không vượt qua Checklist (Score < 80 hoặc vi phạm từ khóa YMYL/bảo mật).

#### **Tháng 10/2026: GEO Moat Engine & llms.txt Sync**
1. **Task 3.1:** Phát triển tính năng **AI Query Generator**: Sinh 20 câu hỏi dựa trên intent từ khóa chính và đẩy vào DB theo dõi GEO Citation.
2. **Task 3.2:** Phát triển module nén nội dung chuẩn Markdown và tự động sync vào file `llms.txt` tại root path của Microsite.

#### **Tháng 11 - 12/2026: Knowledge Space & pSEO CSV Generator**
1. **Task 4.1:** Viết parser tự động bóc tách FAQ/JSON-LD từ bài viết blog gửi sang Knowledge Space cho Chatbot Phạt Nguội.
2. **Task 4.2:** Hoàn thiện giao diện Upload & Validate file CSV cho chiến dịch pSEO Phạt Nguội / eSIM.

---

## **V. QUY TRÌNH PHỐI HỢP & MA TRẬN RACI**

### **5.1. Ma Trận Trách Nhiệm (RACI Matrix)**

| Dự Án / Tính Năng | Hiến (SEO/Product) | Trọng (FE Dev) | Duy (BE Dev) | Hùng (FE Lead) | Thuận / Lộc |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **GenAI Workflow Spec & Prompts** | **Accountable (A)** | Responsible (R) | Consulted (C) | Informed (I) | Consulted (C) |
| **GenAI FE & Text/Logic Nodes Build** | Consulted (C) | **Responsible (R)** | Consulted (C) | **Accountable (A)** | Support (S) |
| **Backend API & Multi-Model Routing** | Informed (I) | Consulted (C) | **Responsible (R)** | Informed (I) | - |
| **SEO/GEO Scoring Rules & Hard Block** | **Accountable (A)** | **Responsible (R)** | Consulted (C) | Informed (I) | - |
| **GEO Citation & llms.txt Engine** | Accountable (A) | **Responsible (R)** | Support (S) | Informed (I) | - |
| **Knowledge Base Extraction UI** | Consulted (C) | **Responsible (R)** | Accountable (A) | Informed (I) | - |

---

### **5.2. Escalation Path & Kênh Align**

* **Align Yêu Cầu & Spec:** Align 1-1 với Hiến (SEO Lead) trên Jira/Figma hoặc meeting trước khi bắt đầu Sprint.
* **Align Kiến Trúc Code & Code Review:** Submit PR qua Hùng (FE Lead) trước khi merge vào repo chính.
* **Escalation Path:** Khi có vướng mắc về API Schema với Backend (Duy) hoặc lệch spec với Product (Hiến), escalate trực tiếp tới Bảo (Project Lead) hoặc Hiếu (Tech Lead) để thống nhất hướng xử lý trong vòng 24h.

---
*Tài liệu được khởi tạo và lưu trữ chính thức tại `Member/trong.md` thuộc MoMo Web Platform Base.*
