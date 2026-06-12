# MoSpark - GenAI Content Engine
Nền tảng sản xuất nội dung bằng AI

> - **Project Name:** MoSpark Web Platform
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Hiến
> - **PIC:** Trọng (Tech), Lộc (User Role)
> - **Version:** 4.5 · June 2026


---

## 1. Executive Summary

### 1.1. Bối cảnh (Situation)
MoSpark cần một "cỗ máy" sản xuất nội dung không chỉ nhanh mà phải **chuẩn hóa**. Hiện tại, việc sử dụng AI cá nhân (ChatGPT/Claude) đang bị phân mảnh, thiếu tính đồng bộ và không kiểm soát được chất lượng Prompt, dẫn đến đầu ra không nhất quán với thương hiệu MoMo.

### 1.2. Vấn đề cốt lõi (Complication)
- **Tốc độ vs Chất lượng:** Content Writer mất quá nhiều thời gian để "mớm" ngữ cảnh cho AI.
- **Prompt Fragmentation:** Mỗi người dùng AI theo một cách khác nhau, không có Guideline chung cho SEO, AEO (Answer Engine Optimization) và GEO.
- **Thiếu Source of Truth:** AI dễ bị ảo giác (hallucination) nếu không được bám sát vào mô tả sản phẩm và các URL tham chiếu cụ thể của dự án.

### 1.3. Giải pháp (Resolution)
Tạo ra **SEO/GEO Project Management Hub & AI Content Engine** - một không gian quản lý tập trung:
- **SEO/GEO Project Management:** Hoạt động như trung tâm quản trị dự án SEO/GEO, trong đó mỗi dự án bắt buộc phải ánh xạ 1-1 với một Microsite tương ứng nhằm kiểm soát đường dẫn URL.
- **Business Context:** Sử dụng mô tả Use Case và URL làm ngữ cảnh toàn cục để định hướng AI.
- **Prompt Standardization:** Hệ thống quản trị Guideline (SEO/AEO/GEO) tự động áp dụng vào mọi bài viết.
- **Performance Intelligence:** Tích hợp tính năng đo lường **Share Of Voice (SOV)** để đánh giá mức độ xuất hiện của MoMo trong câu trả lời của AI.

### 1.4. Tam giác Dữ liệu (The Data Triangle)
Kiến trúc của GenAI Content được thiết kế dựa trên sự phân tách và kết hợp rõ ràng của 3 nguồn lực:
1. **Business Context (Từ BU/PM):** Thông tin sản phẩm, USPs, định vị thương hiệu và rào cản pháp lý. Trả lời câu hỏi: *Viết cái gì cho đúng?*
2. **SEO Inventory (Từ Hiến - SEO Tools):** Số liệu định lượng (Volume, Keyword) phân tầng TOFU/MOFU/BOFU theo Customer Journey. Trả lời câu hỏi: *Viết cho ai, keyword nào, funnel stage nào?*
3. **GenAI Content Engine:** Tiếp nhận Primary Keyword (từ SEO Inventory) và viết Content chuẩn SEO/GEO bám sát Business Context. Output đi qua Outline Selection (hard gate) trước khi push sang CMS Page Editor. Tại đây, PM quyết định định dạng phân phối (Page Type: Blog, Landing Page, Merchant Page, FAQ, etc.).

**Luồng tương tác:**

| Input | Xử lý | Output | Gate |
|---|---|---|---|
| Business Context (PM) + SEO Inventory (Hiến) | GenAI Content Engine tiếp nhận context + keyword | AI Outline draft | - |
| PM xem TOFU/MOFU/BOFU (Expand/Collapse Cluster), chọn Primary Keyword | Hệ thống generate Outline | Outline draft | - |
| PM/Content review Outline | Chọn (Select) Outline phù hợp | **Outline Selected** | **Hard gate - bắt buộc** |
| Outline Selected + Chọn Page Type (Blog/LP/Merchant...) push sang CMS Page Editor | Content paste bài (A) hoặc click GenAI Detail (B) | Trang Content Final | SEO/GEO Score gate |

---

## 2. Stakeholder (Nhóm người dùng chính)

| Vai trò | Trách nhiệm chính | Mục tiêu |
| :--- | :--- | :--- |
| **Content Writer** | Thực thi sản xuất bài viết | Tạo Use Case, quản lý từ khóa, thêm dữ liệu tham khảo, chỉnh sửa dàn ý và tạo bản nháp bài viết tự động. |
| **Guideline Admin** | Quản trị tiêu chuẩn | Thiết lập và cập nhật hệ thống Prompt & Guidelines (SEO, AEO, GEO) để kiểm soát chất lượng đầu ra. |
| **Web Product Lead** | Kiểm soát gate cuối | Review điểm Scoring và phê duyệt xuất bản (Sign-off). |

---

## 3. Bài Toán Cần Giải & Success Metrics

### 3.1. Mục tiêu chiến lược
Biến MoSpark thành "Production Lab" duy nhất, nơi nội dung được sản xuất với chi phí thấp nhất nhưng đạt tiêu chuẩn xuất bản cao nhất của MoMo.

### 3.2. Success Metrics (SMART)
- **Productivity:** Tăng năng suất sản xuất từ trung bình **10 bài/tháng** lên **20 bài/tháng** trên mỗi Content Writer.
- **Quality:** 100% bài viết AI sinh ra phải vượt qua Hard Block của bộ lọc SEO/GEO Scoring.
- **SOV Target:** Đạt mức độ trích dẫn (Citation) từ AI search cho các Primary Keyword của Use Case tối thiểu 30%.

### 3.3. Tính năng cốt lõi (Key Features)
- **Microsite Mapping Hub (Strict 1-1):** Bắt buộc liên kết thực thể dự án SEO/GEO với duy nhất 1 Microsite đích, đóng vai trò là khung quản trị xương sống để phân bổ toàn bộ nội dung của dự án.
- **URL Routing Auto-governance:** Tự động cấu trúc đường dẫn bài viết Blog theo quy tắc: `/{use-case}/blog*` (ví dụ: `/vay-nhanh/blog/*`), kế thừa trực tiếp từ Microsite base path để đồng bộ hóa phân cấp URL.
- **Keyword Master Registry:** Quản lý tập trung Primary Keywords, đảm bảo tính duy nhất (Unique ID Check) trên toàn bộ hệ thống để ngăn chặn Keyword Cannibalization.
- **Double Entry Sync:** Cơ chế đồng bộ bài viết từ module Sản xuất sang module Quản trị (Editor).

---

## 4. Các Giả định & Nền tảng (Assumptions)

- **Grounding Search:** Hệ thống mặc định tích hợp khả năng tìm kiếm web thực tế để AI cập nhật dữ liệu mới nhất và xác thực thông tin.
- **URL Context:** Tính năng đọc hiểu nội dung từ các liên kết (link) trong mô tả Use Case được kích hoạt mặc định để làm "Source of Truth".
- **Human-in-the-loop:** Kết quả AI chỉ mang tính chất tham khảo; Content Writer chịu trách nhiệm rà soát, hiệu đính và chịu trách nhiệm cuối cùng về nội dung.
- **Standard Chữ thường:** Toàn bộ từ khóa được chuẩn hóa về chữ thường để đảm bảo tính nhất quán và duy nhất.

---

## 5. Giải pháp đo lường Share Of Voice (SOV)

Đây là tính năng quan trọng để đánh giá hiệu quả của dự án SEO/GEO:

### 5.1. Cơ chế thu thập dữ liệu
- Hệ thống sử dụng Primary Keyword để hỏi AI (kèm Grounding Search).
- AI trả về câu trả lời kèm danh sách các nguồn tham khảo (References).

### 5.2. Logic tính toán
- **Trích xuất Domain:** Hệ thống tự động tách domain từ các URL tham khảo.
- **Thống kê:** Đếm số lần mỗi domain được trích dẫn và tính tỷ lệ phần trăm (%) dựa trên thị trường.
- **Công thức:** `SOV % = (Số lần domain MoMo xuất hiện / Total Volume Search) * 100`.

### 5.3. Tối ưu hóa vận hành
- Để tiết kiệm chi phí, hệ thống gom nhóm các Secondary Keywords khi thực hiện đo lường SOV (tối đa 6 API call cho mỗi cụm từ khóa chính).

---

## 6. Workflow Content

### 6.0. Giải thích Thuật ngữ (Glossary)

Để đảm bảo sự thống nhất trong vận hành, các thuật ngữ dưới đây được định nghĩa như sau:

*   **Keyword Master Registry (Kho Định Danh Gốc):** Là "Sổ cái" trung tâm lưu trữ toàn bộ Primary Keywords của một Use Case. Mọi trang nội dung (dù tạo từ luồng nào) đều phải được đăng ký tại đây.
*   **Unique ID Check (Kiểm tra Định danh Duy nhất):** Quy trình hậu kiểm tự động. Hệ thống đối soát từ khóa mới với *Keyword Master Registry* để đảm bảo không có 2 trang trùng lặp nội dung/từ khóa trong cùng một Use Case.
*   **AI Enhance (Nâng cấp AI):** Tính năng cho phép "tái cấu trúc" một trang nội dung hiện có bằng sức mạnh của GenAI thông qua việc chuyển hướng về quy trình Draft Outline/Detail.
*   **Bottom-Up Sync (Đồng bộ ngược):** Cơ chế tự động tạo bản ghi tại *Keyword Master Registry* khi người dùng nhập Primary Keyword trong CMS Page Editor.
*   **Top-Down Sync (Đồng bộ xuôi):** Cơ chế tự động khởi tạo trang nội dung trong CMS Page Editor khi người dùng tạo Primary Keyword và Content trong module GenAI.

### 6.1. SEO/GEO Project làm Trung tâm Quản trị & Mapping Microsite

Mỗi dự án SEO/GEO (SEO/GEO Project) trên MoSpark không chỉ đơn thuần là công cụ tạo nội dung mà hoạt động như **Trung tâm Quản trị Dự án (Project Management Hub)** (Chi tiết xem tại: [[04_MOSPARK_PLATFORM/mospark_seo_geo_project|SEO/GEO Project Management]]).
- **Ràng buộc Mapping 1-1 cứng:** Mỗi SEO/GEO Project phải được thiết lập liên kết (mapping) bắt buộc với **chính xác 1 Microsite** (Use Case) tương ứng. Dự án không được phép hoạt động mồ côi (orphaned).
- **Cơ chế Định tuyến đường dẫn:** Việc mapping 1-1 này nhằm tuân thủ tuyệt đối cơ chế định tuyến SEO/GEO của MoSpark: mọi bài viết Blog, tài liệu thuộc dự án bắt buộc phải nằm dưới URL của Microsite đó theo cấu trúc: `/{use-case}/blog*` (Ví dụ: `/phat-nguoi/blog/quy-dinh-phat-nguoi-o-to`).
- **Phân tách thực thể:** Bản thân Microsite quản lý toàn bộ tài sản nội dung của Use Case đó. Blog, Landing Page, FAQ, Merchant Page... đều là các module phân phối thuộc Microsite - không phải các entity hoạt động độc lập:

| Component | Nội dung quản lý | Owner |
|---|---|---|
| **Sub-pages** | Hub page, Spoke pages, Landing pages | PM/PO |
| **Content** | Blog articles, Landing Pages, Merchant Pages, FAQs, Static content | PM/Content Team |
| **Meta data** | Title, Description, OG tags, Schema markup | MoSpark auto + SEO Lead review |
| **llms.txt** | AI crawler policy per Microsite | SEO Lead |
| **Dashboard** | Traffic, W2A, Keyword ranking, SEO Inventory per Use Case | PM/PO view |
| **Content management** | Toàn bộ pages (Blog/LP/Merchant...) thuộc Microsite | PM/Content Team |

Content được tạo theo 2 con đường - cả 2 đều yêu cầu Primary Keyword phải đăng ký trong Keyword Master Registry trước khi publish:
- **Manual (CMS Page Editor trực tiếp):** Content paste bài viết vào CMS Page Editor, nhập Primary Keyword để trigger Unique ID Check.
- **GenAI Flow (luồng bắt buộc):** SEO/GEO Project (SEO Inventory Cluster) → Business Context → Outline (Selected) → Chọn định dạng phân phối (Page Type: Blog/LP/Merchant...) → CMS Page Editor.

**Content Management - List View:**

Hiển thị toàn bộ trang nội dung (Pages) của project, phân biệt rõ bằng badge loại hình và nguồn gốc:

| Loại nguồn | Badge nguồn | Badge định dạng | Columns hiển thị |
|---|---|---|---|
| **GenAI** | `GenAI` (tím) | `Blog` / `LP` / `FAQ` / `Merchant` | Title, Page Type, Primary Keyword, Status, Ngày tạo, Model, Cost |
| **Manual** | `Manual` (xám) | `Blog` / `LP` / `FAQ` / `Merchant` | Title, Page Type, Primary Keyword, Status, Ngày tạo |

**Content Management - Detail View (GenAI article/page):**

Khi click vào trang GenAI, hiển thị 2 panel:

| Panel | Nội dung |
|---|---|
| **Editor** | Full CMS page editor (phù hợp theo Page Type đã chọn) - chỉnh sửa nội dung, metadata, publish/unpublish |
| **AI Usage** | Usage (input tokens / output tokens), Cost (ước tính theo API pricing), Model (tên model đã dùng để generate) |

> **Lý do cần AI Usage panel:** PM/PO và Finance cần biết chi phí AI thực tế per trang và per Use Case để quản lý budget GenAI. Không có data này thì không thể scale có kiểm soát.

**Content Management - Detail View (Manual page):**

Chỉ hiển thị Editor - không có AI Usage panel vì không có API call.

### 6.2. Luồng GenAI → Content (Mandatory Flow)

**Điều kiện tiên quyết:** SEO/GEO Project đã tạo và mapped với Microsite trước khi bắt đầu.

| Bước | Hành động | Owner | Gate |
|---|---|---|---|
| **1** | SEO/GEO Project mapped vào Microsite | PM/PO | Prerequisite cứng - không bỏ qua |
| **2** | Nhập Business Context đầy đủ theo template | PM + SEO Lead validate | Bắt buộc hoàn thành trước khi tạo keyword |
| **3** | Xem SEO Inventory + Topic Cluster (Expand/Collapse UI) | PM chọn stage/cluster cần tấn công | TOFU/MOFU/BOFU hiển thị, PM mở rộng cluster để xem danh sách Primary Keywords |
| **4** | Chọn / Áp dụng Primary Keyword từ Cluster | PM / Content Team | Trực tiếp trigger tạo content cho keyword, chạy Unique ID Check tự động toàn hệ thống |
| **5** | AI generate Outline | Hệ thống | - |
| **6** | **OUTLINE SELECTED & CHỌN PAGE TYPE** | PM/Content | **Hard gate** - PM duyệt outline và chọn định dạng đầu ra (Blog, Landing Page, FAQ, Merchant Page...) |
| **7** | Outline & Page Type push sang CMS Page Editor | Tự động | CMS Page Editor khởi tạo giao diện tương ứng theo Page Type đã chọn |
| **8** | Review brief + Chọn cách tạo bài | PM + Content Team | PM review và chỉnh sửa lại dàn ý (brief) trong Page Editor nếu cần - sau đó chọn cách tạo nội dung |
| **9** | Review & SEO/GEO Score | Web Product Lead | Hard block nếu chưa pass bộ lọc SEO/GEO Score của Page Type tương ứng |
| **10** | Publish | Content Team | Live trang trên momo.vn |

**Bước 6 - Chọn Page Type (Định dạng phân phối):**
Tại bước chọn Outline, PM quyết định loại trang mà content này sẽ hiển thị:
- **Blog Article:** Phù hợp với cụm từ khóa cung cấp thông tin (TOFU), soft-sell.
- **Landing Page:** Phù hợp với cụm từ khóa có mục đích thương mại/giao dịch cao (MOFU/BOFU).
- **FAQ Page:** Giải đáp thắc mắc người dùng (`/hoi-dap`).
- **Merchant Page:** Trang giới thiệu đối tác (`/merchant`).

**Bước 8 - Flow trong CMS Page Editor (sau khi Outline đã push sang):**

**8.1 - PM review + edit brief:**
- PM đọc lại dàn ý (brief) vừa được push sang Page Editor.
- Chỉnh sửa nếu cần: thêm/xóa section, điều chỉnh góc nhìn, clarify heading.
- Đây là lần chỉnh sửa cuối trước khi nội dung được tạo - không quay lại step này sau khi đã chọn cách tạo bài.

**8.2 - Chọn cách tạo bài:**

| Lựa chọn | Cơ chế | Khi nào dùng |
|---|---|---|
| **A - Manual** | Paste bài từ AI cá nhân (ChatGPT, Claude riêng) hoặc tự viết theo brief đã review | Đã có draft sẵn, hoặc muốn kiểm soát toàn bộ quá trình viết |
| **B - GenAI Detail** | Click nút "GenAI Detail" trong CMS Page Editor - hệ thống AI generate full page content từ brief đã review | Chưa có draft, muốn AI của platform viết hoàn chỉnh từ brief |

**Bước 3 - PM thấy gì trong SEO Inventory (Control Panel):**

| Thông tin | Ý nghĩa với PM |
|---|---|
| Market Volume (total) | Market Sizing toàn Use Case - basis để set KPI và độ ưu tiên |
| Keyword cluster theo TOFU (Expandable) | Các cụm chủ đề thông tin - mở ra để xem toàn bộ Primary Keywords |
| Keyword cluster theo MOFU (Expandable) | Các cụm chủ đề so sánh/đánh giá - mở ra để xem toàn bộ Primary Keywords |
| Keyword cluster theo BOFU (Expandable) | Các cụm chủ đề giao dịch - mở ra để xem toàn bộ Primary Keywords |
| SoV MoMo hiện tại | MoMo đang chiếm bao nhiêu % thị trường - biết gap để set target |
| Nút "Apply / Write Outline" | Bấm trực tiếp cạnh Keyword đã cluster trong Inventory để tự động tạo outline mà không cần copy-paste |

**Luồng cập nhật trang đã có (Update Flow):**

Trang đã tồn tại có thể cập nhật theo 2 cách:
1. **Thủ công:** Sửa trực tiếp trong CMS Page Editor
2. **Enhance by GenAI:** Click nút trong CMS Page Editor - redirect về GenAI Content module của keyword đó để tối ưu lại bằng AI, sau đó sync ngược về Editor

### 6.3. Core Data Governance Rules (Xác nhận với Dev - Trọng)

Để đảm bảo tính toàn vẹn dữ liệu và tránh xung đột SEO (Cannibalization), hệ thống áp dụng các quy tắc cứng sau:

1.  **Project-First Requirement (Ràng buộc bối cảnh):** Mọi **Primary Keyword** bắt buộc phải thuộc về một **SEO/GEO Project** cụ thể. Keyword không được phép tồn tại "mồ côi" vì Project là nơi cung cấp *Business Context* và định nghĩa cấu trúc URL.
2.  **Strict 1-1 Mapping (Tính duy nhất):** Quy tắc **1 Bài viết ↔ 1 Primary Keyword**. Một Primary Keyword chỉ được đại diện cho một URL Master và một nội dung duy nhất. Nếu người dùng tạo trùng, hệ thống phải chặn và yêu cầu sử dụng luồng "Update/Enhance".
3.  **Single Ownership (Phân cấp URL):** Một Primary Keyword chỉ thuộc về **duy nhất 1 SEO/GEO Project**. Điều này đảm bảo sự nhất quán trong URL Hierarchy (ví dụ: `/phat-nguoi/` vs `/merchant/`) và tránh tranh chấp Authority giữa các Use Case.
4.  **Cross-Project Cannibalization Check (Kiểm soát Xung đột chéo):** Phạm vi quét của *Keyword Master Registry* phải mang tính **Global (Toàn cục)** toàn hệ thống MoSpark, không nằm cục bộ trong 1 Project. 
    - *Ví dụ:* Nếu Project "Phạt Nguội" đã sở hữu keyword `quy định ô tô`, thì Project "Bảo Hiểm" **không được phép** tạo mới URL với keyword này.
    - *Xử lý:* Thay vì tạo 2 URL triệt tiêu nhau, hệ thống yêu cầu sử dụng chung 1 bài viết Authority và thực hiện **Cross-linking** (Bài viết Phạt Nguội chèn Banner/CTA bán Bảo Hiểm).
5.  **Unique ID Check (Kho định danh):** Mọi Keyword khi nhập vào phải được đối soát với *Keyword Master Registry* của toàn hệ thống trước khi cho phép đi vào luồng sản xuất nội dung.
6.  **Strict 1-to-1 Project-to-Microsite Mapping (Đồng bộ cấu trúc định tuyến):** Mỗi SEO/GEO Project chỉ được phép liên kết với duy nhất 1 Microsite. Hệ thống Router và CMS Page Editor sẽ thực thi kiểm soát ở mức cơ sở dữ liệu: mọi URL con sinh ra từ Project (e.g. blog post, FAQs) sẽ tự động kế thừa tiền tố slug của Microsite được map (ví dụ: `/{use-case}/blog/{slug}`) để đảm bảo cấu trúc thư mục URL luôn chuẩn chỉnh.

---

### 6.4. Workflow Chi tiết - 10 Bước thực thi (GenAI Flow)

| Bước | Tên Bước | Hành động | Input/Output | Owner |
|---|---|---|---|---|
| **1** | **Map Microsite** | SEO/GEO Project mapping vào Microsite tương ứng | Project linked to Microsite | PM/PO |
| **2** | **Business Context** | Nhập đầy đủ 12 trường theo template (xem Section 7) | Context Layer - Source of Truth cho AI | PM/Growth + SEO Lead validate |
| **3** | **SEO Inventory** | Xem Market Sizing, mở rộng TOFU/MOFU/BOFU cluster (Expand/Collapse UI) | Bảng Keyword Strategy tích hợp Business Context | PM/Growth |
| **4** | **Keyword Apply** | Bấm nút **"Apply / Write Outline"** trực tiếp cạnh Keyword đã phân cụm | Keyword vào Master Registry, Unique ID Check tự động | PM / Content Team |
| **5** | **AI Outline** | AI generate dàn ý thô dựa trên Business Context + Primary Keyword | Outline Draft | Hệ thống |
| **6** | **OUTLINE SELECTED & PAGE TYPE** | PM/Content review, duyệt (Select) Outline **và chọn định dạng phân phối (Page Type)** | Outline & Page Type Confirmed | PM/Content - **Hard gate** |
| **7** | **Push sang CMS Editor** | Tự động chuyển Outline và cấu trúc giao diện theo Page Type đã chọn | CMS Page Editor nhận structure | Tự động |
| **8** | **Review & Edit Brief** | PM đọc lại dàn ý trong CMS Editor, chỉnh sửa nếu cần (lần review cuối trước khi viết) | Brief final trong CMS Page Editor | PM/Content Team |
| **8A** | **Manual** | Paste bài viết từ AI cá nhân hoặc tự viết theo brief đã review | Content Page draft | Content Team |
| **8B** | **GenAI Detail** | Click "GenAI Detail" trong CMS Editor - AI generate full page content từ brief | Content Page draft | AI (Claude API) |
| **9** | **Review Quality** | Kiểm tra E-E-A-T, YMYL, SEO/GEO Score - sign-off | Verified content page | Web Product Lead - Hard gate |
| **10** | **Publish** | Content Team publish từ CMS Page Editor | Live trên momo.vn (Blog/LP/FAQ...) | Content Team |

```mermaid
graph TD
    A[Map Microsite] --> B[Nhập Business Context]
    B --> C[Xem SEO Inventory - Expand Cluster]
    C --> D[Apply Keyword / Click Write Outline]
    D --> E[Hệ thống tự động tạo Outline]
    E --> F{PM Select Outline & Chọn Page Type?}
    F -- Không --> E
    F -- Có --> G[Push sang CMS Editor theo Page Type]
    G --> H[Review & Edit Brief]
    H --> I{Chọn cách tạo bài?}
    I -- Manual --> J[Paste bài / Tự viết]
    I -- GenAI --> K[Click GenAI Detail]
    J --> L[Review Quality & Score]
    K --> L
    L --> M((Publish))
```

> **Business Context (Bước 2) là điều kiện để AI viết đúng.** Nhập thiếu = AI thiếu context = output hallucinate hoặc sai sản phẩm. PM chịu trách nhiệm pháp lý về nội dung Business Context nhập vào.

---

### 6.5. Role & Responsibility Detail

#### PM/Growth (Cell Team)
**Trách nhiệm chính:** Map Microsite, nhập Business Context, chọn keyword từ Inventory, duyệt Outline & quyết định loại hình phân phối (Page Type)

- **Bước 1:** Map SEO/GEO Project vào đúng Microsite
- **Bước 2:** **Nhập Business Context đầy đủ - chịu trách nhiệm pháp lý về nội dung nhập vào**
  - Confirm tất cả 12 trường theo template: Value Prop, Trust Signals, Disclaimer, Blacklist terms
  - Verify không có thông tin sai, không recommend competitor, không overpromise tính năng
- **Bước 3-4:** Xem SEO Inventory, mở rộng các Topic Clusters (Expand/Collapse), chọn và bấm **Apply** Primary Keyword cần triển khai.
- **Bước 6:** **SELECT Outline & CHỌN PAGE TYPE - hard gate, không thể skip**
  - Review outline để đảm bảo đi đúng strategy & positioning.
  - Chọn định dạng phân phối (Blog, Landing Page, FAQ, Merchant Page...) để hệ thống khởi tạo giao diện CMS Editor phù hợp.
- **Bước 8:** **Review + edit brief trong CMS Page Editor trước khi chọn cách tạo bài**
  - Đọc lại dàn ý vừa push sang Page Editor.
  - Chỉnh sửa nếu cần (thêm/bớt section, clarify heading, điều chỉnh angle).
  - Đây là lần review cuối - sau khi xác nhận mới chọn GenAI Detail hoặc Manual.

#### Content Team
**Trách nhiệm chính:** Đề xuất điều chỉnh dàn ý, viết chi tiết nội dung, publish

- **Bước 4:** Chọn Primary Keyword + bộ Secondary keywords từ SEO Inventory hoặc tạo thủ công nếu thuộc ngách mới.
- **Bước 5-6:** Chỉnh sửa Outline draft, submit để PM duyệt.
- **Bước 8:** Review + chỉnh sửa brief trong CMS Page Editor.
- **Bước 8A hoặc 8B:** Chọn cách tạo nội dung (Manual paste hoặc click GenAI Detail).
- **Bước 10:** Kiểm tra lần cuối giao diện, Click Publish sau khi Web Product Lead sign-off.

#### Web Product Lead (Văn Hiến)
**Trách nhiệm chính:** Validate Business Context, đảm bảo tiêu chuẩn SEO/GEO, sign-off trước publish

- **Bước 2:** Validate Business Context framework - confirm đủ trường, bối cảnh chính xác.
- **Bước 9:** **Review Quality & SEO/GEO Scoring - Sign-off Publish**
  - Check điểm Scoring tự động theo bộ tiêu chuẩn của loại trang tương ứng (Blog, LP...).
  - Flag nếu có issues: E-E-A-T fail, YMYL risk, content vi phạm thương hiệu.
  - Sign-off = content được phép chuyển sang Bước 10 Publish.

---

### 6.6. Approval Gates

| Gate | Bước | Owner | Condition | Consequence nếu fail |
|---|---|---|---|---|
| **Business Context Complete** | 2 | PM/Growth + Web Product Lead | Đủ 12 trường, chính xác, pháp lý clear | Block - không tạo được keyword |
| **Outline Selected & Page Type Chosen** | 6 | PM/Content | PM bắt buộc click Select Outline và chọn Page Type đầu ra | Hard block - không push sang CMS Page Editor được |
| **SEO/GEO Score Pass** | 9 | Web Product Lead | Bài viết/trang pass toàn bộ scoring criteria của Page Type đó, sign-off | Hard block - không publish được |

---

### 6.7. Synchronization & Keyword Master Registry Logic

Hệ thống quản lý nội dung dựa trên nguyên tắc **GenAI Content là Keyword Master Registry (Kho lưu trữ gốc)** của toàn bộ Primary Keywords trong một Project.

```mermaid
sequenceDiagram
    participant Editor as CMS Page Editor
    participant Registry as Keyword Master Registry
    participant GenAI as GenAI Module

    Note over Editor,Registry: Luồng Bottom-Up (Viết tay)
    Editor->>Registry: Nhập Primary Keyword
    alt Đã tồn tại
        Registry-->>Editor: Block (Cannibalization Error)
    else Hợp lệ
        Registry-->>Editor: OK
        Registry->>GenAI: Tạo record rỗng chờ Enhance
    end
    
    Note over GenAI,Editor: Luồng Top-Down (GenAI)
    GenAI->>Registry: Tạo Primary Keyword
    Registry->>Editor: Khởi tạo Draft Page (theo Page Type)
    GenAI->>Editor: Push Outline / Content đè lên Draft
```

1.  **Cơ chế Đồng bộ từ Luồng Mặc Định (Bottom-Up Sync):**
    - Ở CMS Page Editor, PM không nhập "Primary Keyword" ngay từ đầu quy trình tạo.
    - Tuy nhiên, để đạt điểm **SEO/GEO Score**, PM buộc phải nhập **Primary Keyword** (trước đây là Meta Keyword).
    - **Hành động hệ thống:** Ngay khi Primary Keyword được nhập, MoSpark sẽ tự động tạo một bản ghi (Record) tương ứng trong module GenAI Content với Keyword này.
    - Điều này đảm bảo mọi trang viết tay đều có một đại diện trong GenAI để sẵn sàng cho tính năng AI Enhance.

2.  **Cơ chế Từ Luồng GenAI Content (Top-Down Sync):**
    - Khi PM tạo một Primary Keyword trong module GenAI, hệ thống sẽ tự động khởi tạo và liên kết (Link) với một trang nháp tương ứng với Page Type đã chọn trong CMS Page Editor.
    - Mọi thay đổi về nội dung từ GenAI (Step 6) sẽ được đồng bộ (Sync) đè lên hoặc cập nhật vào trang này.

3.  **Quản lý Tính Unique (Unique ID Check):**
    - **Vị trí kiểm soát:** Duy nhất tại module GenAI Content.
    - **Logic:** Dù nội dung đến từ luồng nào, Primary Keyword (từ CMS Editor hoặc từ GenAI) đều phải "check-in" tại Keyword Master Registry. 
    - Nếu Keyword đã tồn tại, hệ thống sẽ ngăn chặn việc tạo mới và yêu cầu user sử dụng trang hiện có để tránh "Content Cannibalization".

---

## 7. Business Context - Các trường bắt buộc

> **Owner:** Văn Hiến
> **Thời điểm nhập:** Bắt buộc hoàn thành TRƯỚC khi generate bất kỳ bài viết nào trong Use Case
> **Mục đích:** Làm nền tảng context cho cả Prompt 1 (Outline) và Prompt 2 (Writer) - đảm bảo AI luôn viết đúng về sản phẩm MoMo, không recommend competitor, không bịa đặt tính năng

Dưới đây là mẫu chuẩn để mô tả trọn vẹn một Business Model của Use Case MoMo (gồm 12 trường thông tin bắt buộc). Hãy nhập đầy đủ thông tin này cho mỗi dự án/Use Case để làm Context Layer cho AI.

```markdown
### 1. Định danh sản phẩm
*   **Tên sản phẩm:** [Ví dụ: MoMo Cinema, Tra cứu Phạt nguội]
*   **URL Web:** [URL chính thức trên momo.vn]

### 2. Mô hình doanh thu (Revenue Model)
[Mô tả cách sản phẩm tạo ra giá trị kinh tế. Ví dụ: Hoa hồng trên mỗi giao dịch thành công (Commission), phí dịch vụ hàng tháng (Subscription), hay doanh thu từ quảng cáo/đối tác]

### 3. Giá trị cốt lõi (Value Propositions)
[Danh sách các điểm giá trị (USPs) giải quyết nỗi đau của khách hàng mà đối thủ không có hoặc làm chưa tốt]

### 4. Phân khúc khách hàng (Customer Segments)
[Persona chính: Họ là ai? Đang gặp vấn đề (Pain points) gì? Mong muốn (Gains) gì?]

### 5. Đối tác chiến lược (Key Partners)
[Các đơn vị cung cấp dữ liệu, hạ tầng hoặc dịch vụ đi kèm. Ví dụ: Cục CSGT, các cụm rạp CGV/Lotte, Ngân hàng đối tác]

### 6. Vận hành & Nguồn lực (Core Operations)
[Mô tả cách hệ thống vận hành phía sau. Ví dụ: Kết nối API thời gian thực với đối tác, hệ thống đối soát tự động, công nghệ bảo mật]

### 7. Lợi thế cạnh tranh (Competitive Advantage)
[Điểm khác biệt giúp MoMo duy trì vị thế: Data độc quyền, lượng user lớn, hệ sinh thái siêu ứng dụng...]

### 8. Chương trình ưu đãi (Promotion Schemes)
[Các cơ chế thúc đẩy tăng trưởng hiện hành: Cashback, Voucher, MoMo Rewards, các gói combo đặc biệt]

### 9. Bằng chứng tin cậy (Trust Signals)
[Giấy phép NHNN, chứng chỉ bảo mật, giải thưởng ngành, các chứng nhận uy tín]

### 10. Pháp lý & Tuân thủ (Compliance & Disclaimer)
[Các quy định bắt buộc phải tuân thủ và nội dung miễn trừ trách nhiệm pháp lý cho người dùng]

### 11. Giới hạn & Từ ngữ cấm (Constraints & Blacklist)
[Những gì sản phẩm KHÔNG làm được và danh sách từ ngữ nhạy cảm/tên đối thủ tuyệt đối không được nhắc tới]

### 12. Số liệu & Case Study (MoMo Data)
[Dữ liệu thực tế: Số lượng user đang dùng, Market share, các câu chuyện thành công (Success Stories) hoặc các con số biết nói để làm bằng chứng (Information Gain)]
```

### 7.2. Hướng dẫn điền thông tin (Best Practices)

1. **Dữ liệu thực tế:** Ưu tiên các con số cụ thể (ví dụ: "Tăng trưởng 20%/tháng" thay vì "Tăng trưởng tốt").
2. **Tư duy Business Model:** Hãy trả lời câu hỏi "Tại sao khách hàng chọn mình thay vì đối thủ?" và "MoMo kiếm tiền bền vững từ đây như thế nào?".
3. **Cập nhật định kỳ:** Thông tin về đối tác và ưu đãi (Scheme) cần được cập nhật ngay khi có thay đổi để các tài liệu tham chiếu (BRD) không bị lỗi thời.

---

## 8. Lộ trình Triển khai (Implementation Roadmap)

Dự án GenAI Content được chia làm 2 giai đoạn chính để đảm bảo tính ổn định của hệ thống trước khi mở rộng tính năng đo lường:

### Giai đoạn 1: Technical Flow & Workflow Standardization (May 2026)
**Trọng tâm:** Hoàn thiện hạ tầng kỹ thuật và quy trình sản xuất nội dung.
- Triển khai toàn bộ **Technical Flow** (Project Mapping, Business Context, Keyword Registry).
- Hoàn thiện 3 luồng vận hành (**Flow 1, 2, 3**) tích hợp với MoSpark Blog Editor.
- Tích hợp Claude API và hệ thống Prompt Master.
- Pilot thành công cho dự án **Phạt Nguội** và **Merchant Directory**.
- ✅ **7-Step Workflow live:** Blog Detail AI + Blog Editor Publish separation
- ✅ **Phạt Nguội pilot:** Foundation complete - **Target T5/2026: 10 bài/tuần, PM execute theo GenAI Flow**
- ✅ **Scale Financial products:** Vay Nhanh, Ví Trả Sau, CIC

### Giai đoạn 2: Share of Voice (SoV) & Visibility Tracking (June 2026+)
**Trọng tâm:** Đo lường hiệu quả và tối ưu hóa tăng trưởng.
- Tích hợp Dashboard đo lường **SoV (Share of Voice)** theo từng Use Case.
- Theo dõi **Visibility Index** của các bài viết GenAI trên Google Search & AI Search.
- Hệ thống cảnh báo **Content Decay** (Nội dung giảm sút hiệu quả).
- Tự động gợi ý từ khóa mới dựa trên Gap Analysis (SEO Inventory).
- **Market Inventory UI (by Trọng):** Hiển thị danh sách Cluster & Volume của Market tương ứng ngay trong giao diện SEO/GEO Project để PM chọn Primary Keyword.
- **Google Search Console API Integration:** Theo dõi hiệu suất per Use Case
- **Metrics per Use Case:** Organic traffic, impressions, CTR, avg position
- **Automated Insights:** Gợi ý tối ưu nội dung dựa trên data
- **Content Refresh Automation:** Identify underperforming articles - suggest updates

---

## 9. GenAI Operational Standards & Prompt Strategy

> **Role:** Văn Hiến (Web Product Lead)
> **Engine:** Claude API (Integrated in MoSpark)
> **Goal:** Tạo nội dung chuẩn SEO/GEO, đạt E-E-A-T và sẵn sàng cho AI Search Citation.

### 9.1. Nguyên tắc cốt lõi (Core Principles)
*   **Zero-Hallucination**: Luôn yêu cầu AI sử dụng dữ liệu thực tế (Pháp luật, số liệu từ BU).
*   **Context Injection**: Truyền bối cảnh Use Case (Primary Keyword, Target Audience) vào Prompt.
*   **Structure-First**: Luôn yêu cầu AI tạo Outline trước khi viết nội dung chi tiết.

### 9.2. Framework Prompt cho Blog Content
Quy trình này khớp với **Bước 5 (AI Outline) và Bước 8B (GenAI Detail)** trong Workflow 10 bước, sử dụng cơ chế nhân bản (Cloning) để cô lập prompt theo từng dự án:

*   **Cơ chế liên kết:** Các Prompt Master trong thư viện đóng vai trò là **Master Prompt Templates**. Khi tạo Project mới, hệ thống tự động clone các template này về Project làm **Project-Specific Localized Prompts**. PM/Content Lead có thể chỉnh sửa bản clone này tại cấp độ Project.
*   **Phase A: Outline Generator (Bước 5)**
    *   **Input**: Primary Keyword + Business Context (từ Bước 2) + Target Audience + Key Message.
    *   **Prompt Template nguồn:** [[03_SKILLS/momo-blog-prompt-1-outline|GenAI Blog Prompt 1 (Outline)]] (Được clone về làm `project_outline_prompt` của Project).
*   **Phase B: Content Writer (Bước 8B - GenAI Detail)**
    *   **Trigger**: PM/Content click "GenAI Detail" trong Blog Editor sau khi Outline đã Selected (Bước 6).
    *   **Input**: Outline từ Phase A + [[03_SKILLS/momo-seo-geo-guideline|MoMo SEO & GEO Prompt Guidelines]] + [[03_SKILLS/momo-ymyl-guideline|MoMo YMYL Guidelines]].
    *   **Prompt Template nguồn:** [[03_SKILLS/momo-blog-prompt-2-writer|GenAI Blog Prompt 2 (Writer)]] (Được clone về làm `project_writer_prompt` của Project).
*   **Chi tiết quản trị & vận hành:** Xem thêm tại [MoSpark SEO/GEO Project Hub - Phần 3. Kiến trúc Quản trị Prompt & Guideline](file:///Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/04_MOSPARK_PLATFORM/mospark_seo_geo_project.md#3-kien-truc-quan-tri-prompt--guideline-dinh-huong-theo-du-an-project-specific-localized-prompt-management).

### 9.3. Quality Gate Standards (SEO/GEO Score)
Nội dung sau khi GenAI tạo ra phải được tự động chấm điểm qua [[04_MOSPARK_PLATFORM/mospark_seo_geo_score|SEO/GEO Scoring System]]. Các tiêu chí bắt buộc:
*   Mật độ từ khóa chính.
*   Sự hiện diện của FAQ Schema.
*   Độ dài và cấu trúc Heading.

### 9.4. Định giá Model & Quy hoạch Ngân sách (Model Benchmarks & Budgeting)
Hệ thống hiện tại đang tích hợp API của hãng Anthropic (Claude) để thực hiện quy trình sản xuất nội dung gồm 2 giai đoạn (Tạo Outline dàn ý & Viết Blog Detail chi tiết) với các thông số đo lường hiệu năng và chi phí thực tế:

*   **Claude 3 Haiku (Model tối giản - Scale lớn):**
    *   *Thời gian sản xuất:* ~55 giây / bài (bao gồm cả Outline & Blog Detail).
    *   *Chi phí (API Cost):* ~7.000đ / bài viết hoàn chỉnh.
    *   *Mục đích:* Thích hợp cho các bài viết số lượng lớn (Scale), nhóm bài ngách địa phương (pSEO) hoặc các BU có ngân sách tối giản.
*   **Claude 3.5 Sonnet (Model cao cấp - Chất lượng chuyên sâu):**
    *   *Thời gian sản xuất:* ~140 giây / bài (bao gồm cả Outline & Blog Detail).
    *   *Chi phí (API Cost):* ~20.000đ / bài viết hoàn chỉnh.
    *   *Mục đích:* Dành cho các bài viết trụ cột (TOFU/BOFU Hub), yêu cầu học thuật cao, kiểm soát chặt chẽ tiêu chuẩn E-E-A-T và YMYL.

**Quản lý & Hoạch định Ngân sách (Budget Planning):**
Việc xác định rõ đơn giá cố định trên từng bài viết giúp PM/PO dễ dàng dự toán ngân sách chi tiết dựa trên số lượng bài viết của Content Plan.
*   *Ví dụ:* Content Plan cho Use Case yêu cầu **40 bài viết**:
    *   Nếu chọn chạy 100% bằng **Haiku**: 40 bài x 7.000đ = 280.000 VNĐ.
    *   Nếu chọn chạy 100% bằng **Sonnet**: 40 bài x 20.000đ = 800.000 VNĐ.

**Định hướng & Lộ trình sắp tới:**
1.  **Đa dạng hóa Model (Multi-Model Selector):** Tích hợp thêm các mô hình ngôn ngữ hàng đầu khác (GPT-4o, Gemini 1.5 Pro, Llama 3, v.v.) trực tiếp trên giao diện CMS MoSpark để PM chủ động lựa chọn tùy theo tính chất nội dung và ngân sách.
2.  **Cơ chế tích hợp API Key theo BU (Custom BU API Key Integration):** Cho phép các đơn vị kinh doanh (BUs) chủ động cấu hình API Key riêng của BU mình vào hệ thống. Chi phí API call phát sinh sẽ được tự động trừ trực tiếp vào ngân sách phân bổ riêng của BU đó, giải quyết triệt để bài toán phân bổ chi phí giữa các phòng ban.

---

## 10. Danh mục Use Cases triển khai (Pipeline)

Hệ thống GenAI Content sẽ phục vụ sản xuất nội dung cho các dự án chiến lược sau:

1. **Dự án Phạt Nguội (Pilot):** Sản xuất 20+ bài viết Blog chuẩn E-E-A-T và pSEO địa phương.
2. **Dự án Merchant Directory (`/merchant`):** 
   - Sản xuất tự động **Thông tin mô tả Merchant** (Intro).
   - Tạo bộ **FAQ & HowTo thanh toán** cho từng Merchant (Ví dụ: "Highlands Coffee có nhận MoMo không?").
   - Đảm bảo tính nhất quán của thông tin ưu đãi và phương thức thanh toán (VTS/QR).

---



## 11. Tài liệu Liên kết
*   **Master Strategy:** [[04_MOSPARK_PLATFORM/mospark_master|MoSpark Master Doc]]
*   **SEO/GEO Project Hub:** [[04_MOSPARK_PLATFORM/mospark_seo_geo_project|MoSpark SEO/GEO Project Management]]
*   **Dữ liệu Thị trường:** [[04_MOSPARK_PLATFORM/mospark_seo_inventory|MoSpark SEO Keyword Inventory]]

## 12. Change Log
- **v4.5 (2026-06-07):** Nâng cấp tài liệu định nghĩa GenAI Content Engine thành Trung tâm Quản trị Dự án SEO/GEO (SEO/GEO Project Management Hub). Quy định ràng buộc mapping 1-1 bắt buộc với Microsite và cơ chế định tuyến tự động `/{use-case}/blog*` ở mức Database và Router (Hiến).
- **v4.4 (2026-06-05):** Chuyển đổi mô hình từ sản xuất Blog đơn thuần sang chiến lược đa dạng hóa trang phân phối (Content Strategy với Page Type: Blog, LP, FAQ, Merchant Page). Tích hợp giao diện SEO Inventory có Topic Cluster (Expand/Collapse) để PM chọn trực tiếp Primary Keyword và click tạo Outline/Detail. (Hiến).
- **v4.3 (2026-05-31):** Bổ sung Tech Ownership rõ ràng cho 3 Dev: Trọng (AI Tool/Model/Workflow - lõi engine sinh content), Thuận (GenAI Hình - đang quản lý MoMo Gallery), Lộc (phân quyền User access GenAI trong MoSpark). Governance: Hiến (Skill Hub).
- **v4.2 (2026-05-27):** Cập nhật Section 9.4: Bổ sung đơn giá và thời gian benchmark chi tiết cho Claude 3 Haiku (7.000đ - 55s) & Claude 3.5 Sonnet (20.000đ - 140s). Quy hoạch cơ chế dự toán chi phí theo Content Plan và định hướng lộ trình Multi-model Selector + tích hợp API Key theo BU (Văn Hiến).
- **v4.1 (2026-05-26):** Cập nhật Bước 8 trong workflow: bổ sung explicit step PM review + edit brief trong Blog Editor trước khi chọn cách tạo bài (GenAI Detail hoặc Manual). Phản ánh luồng thực tế Trọng đang implement. Section 6.2, 6.4, 6.5 đồng bộ. Phạt Nguội T5/2026: target 10 bài/tuần.
- **v4.0 (2026-05-26):** Tái kiến trúc toàn bộ workflow: (1) Microsite là đơn vị quản lý cấp trên - Blog là module trong Microsite; (2) Bỏ Double Entry Flow, thay bằng Mandatory GenAI Flow 10 bước với Outline Selected là hard gate; (3) TOFU/MOFU/BOFU visible trong SEO Inventory ở Bước 3; (4) Blog Editor nhận 2 lựa chọn sau khi Outline push sang: Manual paste hoặc GenAI Detail; (5) Xóa toàn bộ mermaid blocks (Hiến).
- **v3.9 (2026-05-18):** Phục hồi toàn bộ nội dung chi tiết bị mất trong quá trình di dời thư mục và chuẩn hóa liên kết Obsidian (Hiến).
- **v3.8 (2026-05-16):** Tái cấu trúc: Footer Links & Version Log. Nhấn mạnh cơ chế chống Cannibalization (Hiến).
- **v3.7 (2026-05-15):** Tích hợp đo lường Share of Voice (SoV) cho AI Search (Hiến).
- **v3.6 (2026-05-07):** Cập nhật luồng Double Entry Flow & 7-step workflow (Hiến).

---
*Maintained by: Văn Hiến (Web Product Lead) | Last updated: 2026-06-07*
