# BRD: GenAI Content - SEO/GEO Project Module

> **Product Manager:** Anh Bảo (Web Platform Manager)       
> **Tech Lead:** Trần Công Hoàng Trọng (Software Engineer II)         
> **Integration Support:** Bùi Minh Nhật (Senior Software Engineer)       
> **Governance & Prompts:** Văn Hiến (SEO & GEO Lead) 
> **Start Date:** May 2026    
> **Status:** On Progress

---

## 1. Executive Summary

### 1.1. Bối cảnh (Situation)
MoSpark cần một "cỗ máy" sản xuất nội dung không chỉ nhanh mà phải **chuẩn hóa**. Hiện tại, việc sử dụng AI cá nhân (ChatGPT/Claude) đang bị phân mảnh, thiếu tính đồng bộ và không kiểm soát được chất lượng Prompt, dẫn đến đầu ra không nhất quán với thương hiệu MoMo.

### 1.2. Vấn đề cốt lõi (Complication)
- **Tốc độ vs Chất lượng:** Content Writer mất quá nhiều thời gian để "mớm" ngữ cảnh cho AI.
- **Prompt Fragmentation:** Mỗi người dùng AI theo một cách khác nhau, không có Guideline chung cho SEO, AEO (Answer Engine Optimization) và GEO.
- **Thiếu Source of Truth:** AI dễ bị ảo giác (hallucination) nếu không được bám sát vào mô tả sản phẩm và các URL tham chiếu cụ thể của dự án.

### 1.3. Giải pháp (Resolution)
Tạo ra **AI Content Creator** - một không gian quản lý tập trung:
- **Business Context:** Sử dụng mô tả dự án và URL làm ngữ cảnh toàn cục để định hướng AI.
- **Prompt Standardization:** Hệ thống quản trị Guideline (SEO/AEO/GEO) tự động áp dụng vào mọi bài viết.
- **Performance Intelligence:** Tích hợp tính năng đo lường **Share Of Voice (SOV)** để đánh giá mức độ xuất hiện của MoMo trong câu trả lời của AI.

---

## 2. Stakeholder (Nhóm người dùng chính)

| Vai trò | Trách nhiệm chính | Mục tiêu |
| :--- | :--- | :--- |
| **Content Writer** | Thực thi sản xuất bài viết | Tạo dự án, quản lý từ khóa, thêm dữ liệu tham khảo, chỉnh sửa dàn ý và tạo bản nháp bài viết tự động. |
| **Guideline Admin** | Quản trị tiêu chuẩn | Thiết lập và cập nhật hệ thống Prompt & Guidelines (SEO, AEO, GEO) để kiểm soát chất lượng đầu ra. |
| **SEO/GEO Lead** | Kiểm soát gate cuối | Review điểm Scoring và phê duyệt xuất bản (Sign-off). |

---

## 3. Bài Toán Cần Giải & Success Metrics

### 3.1. Mục tiêu chiến lược
Biến MoSpark thành "Production Lab" duy nhất, nơi nội dung được sản xuất với chi phí thấp nhất nhưng đạt tiêu chuẩn xuất bản cao nhất của MoMo.

### 3.2. Success Metrics (SMART)
- **Productivity:** Tăng năng suất sản xuất từ trung bình **10 bài/tháng** lên **20 bài/tháng** trên mỗi Content Writer.
- **Quality:** 100% bài viết AI sinh ra phải vượt qua Hard Block của bộ lọc SEO/GEO Scoring.
- **SOV Target:** Đạt mức độ trích dẫn (Citation) từ AI search cho các Primary Keyword của dự án tối thiểu 30%.

---

## 4. Các Giả định & Nền tảng (Assumptions)

- **Grounding Search:** Hệ thống mặc định tích hợp khả năng tìm kiếm web thực tế để AI cập nhật dữ liệu mới nhất và xác thực thông tin.
- **URL Context:** Tính năng đọc hiểu nội dung từ các liên kết (link) trong mô tả dự án được kích hoạt mặc định để làm "Source of Truth".
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
- **Thống kê:** Đếm số lần mỗi domain được trích dẫn và tính tỷ lệ phần trăm (%).
- **Công thức:** `SOV % = (Số lần domain MoMo được trích dẫn / Tổng số trích dẫn) * 100`.

### 5.3. Tối ưu hóa vận hành
- Để tiết kiệm chi phí, hệ thống gom nhóm các Secondary Keywords khi thực hiện đo lường SOV (tối đa 6 API call cho mỗi cụm từ khóa chính).

---

## 6. Workflow Content - Double Entry Flow

### 6.0. Giải thích Thuật ngữ (Glossary)

Để đảm bảo sự thống nhất trong vận hành, các thuật ngữ dưới đây được định nghĩa như sau:

*   **Keyword Master Registry (Kho Định Danh Gốc):** Là "Sổ cái" trung tâm lưu trữ toàn bộ Primary Keywords của một Project. Mọi bài viết (dù tạo từ luồng nào) đều phải được đăng ký tại đây.
*   **Unique ID Check (Kiểm tra Định danh Duy nhất):** Quy trình hậu kiểm tự động. Hệ thống đối soát từ khóa mới với *Keyword Master Registry* để đảm bảo không có 2 bài viết trùng lặp nội dung/từ khóa trong cùng một Project.
*   **AI Enhance (Nâng cấp AI):** Tính năng cho phép "tái cấu trúc" một bài viết hiện có bằng sức mạnh của GenAI thông qua việc chuyển hướng về quy trình Draft Outline/Detail.
*   **Bottom-Up Sync (Đồng bộ ngược):** Cơ chế tự động tạo bản ghi tại *Keyword Master Registry* khi người dùng nhập Primary Keyword trong Blog Editor.
*   **Top-Down Sync (Đồng bộ xuôi):** Cơ chế tự động khởi tạo bài viết trong Blog Editor khi người dùng tạo Primary Keyword và Content trong module GenAI.

### 6.1. Entry Points & Operational Logic

Dự án vận hành dựa trên 2 luồng cơ bản (Double Entry) để đảm bảo tính linh hoạt giữa việc tạo mới thủ công và tạo bằng AI.

#### A. Luồng Tạo Mới (Create New)
Có 2 quy trình tách biệt hoàn toàn về cách sản xuất nội dung:

1.  **Tạo Mặc Định (Default/External Flow):** 
    - **Vận hành:** PM tự viết, thuê Freelancer, hoặc gửi Content Marketing viết bên ngoài hệ thống MoSpark.
    - **Quy trình:** Có Blog Detail sẵn -> Sử dụng tính năng "Create Blog" trong MoSpark -> Input nội dung vào Blog Editor -> Publish.
    - **Đặc điểm:** MoSpark đóng vai trò là công cụ Input & CMS.

2.  **Tạo qua GenAI Content (In-System AI Flow):**
    - **Vận hành:** Mọi bước sản xuất diễn ra 100% trên nền tảng MoSpark.
    - **Quy trình:** Nhập Từ Khóa -> AI Draft Outline -> Manual Edit Outline -> AI Draft Blog Detail -> Sync qua Blog Editor -> Publish.
    - **Đặc điểm:** MoSpark đóng vai trò là nền tảng sản xuất nội dung (Production Lab).

> [!IMPORTANT]
> **Định danh Unique:** Dù tạo bằng cách nào, hệ thống phải check trùng lặp Từ khóa. 1 Primary Keyword = 1 Blog Article.

#### B. Luồng Cập Nhật (Update)
Bài viết đã tồn tại (tạo từ bất kỳ nguồn nào) đều có thể được cập nhật theo 2 hướng:
1.  **Cập nhật thủ công:** Tự viết hoặc paste nội dung mới trực tiếp vào Blog Editor.
2.  **Enhance by GenAI Content:** Sử dụng nút bấm trong Blog Editor để chuyển hướng đến module GenAI Content của chính từ khóa đó để tối ưu hóa lại bằng AI.

### 6.1. Operational Flow - Creation Paths (Way 1 & Way 2)

Quy trình này tách biệt rõ ràng giữa việc **Nhập liệu thủ công (Way 1)** và **Sản xuất bằng AI (Way 2)** theo 7 bước chuẩn.

```mermaid
graph TD
    Start((BẮT ĐẦU)) --> Project[Bước 1: Tạo Project & Bước 2: Nhập Context]
    Project --> Choice{Chọn nguồn nội dung}

    %% Way 1 path
    Choice -- "CÓ SẴN BÀI VIẾT<br/>(Way 1)" --> W1_Step1[Dán nội dung vào Blog Editor]
    W1_Step1 --> W1_Step2[Nhập Primary Keyword]
    W1_Step2 --> Registry

    %% Way 2 path
    Choice -- "DÙNG AI SẢN XUẤT<br/>(Way 2)" --> W2_Step1[Bước 3: Nhập Primary Keyword]
    W2_Step1 --> Registry
    Registry -- "Hợp lệ" --> W2_Step2[Bước 4: AI Outline & Bước 5: AI Blog]
    W2_Step2 --> W2_Step3[Bước 6: Review & Sign-off]
    W2_Step3 --> W2_Step4[Bước 7: Sync MoSpark]

    %% Master Registry Hub
    subgraph Hub ["TRUNG TÂM KIỂM SOÁT (MASTER REGISTRY)"]
        Registry{"KIỂM TRA DUY NHẤT<br/>(Unique ID Check)"}
    end

    %% Convergence to Publish
    W2_Step4 --> Publish
    Registry -- "Trùng lặp" --> Error[Cảnh báo & Yêu cầu Update]
    
    W1_Step2 --> Publish([XUẤT BẢN - MOMO.VN])

    %% Styling
    style Hub fill:#f0f0f0,stroke:#333,stroke-dasharray: 5 5
    style Registry fill:#ff9ff3,stroke:#333,stroke-width:2px
    style Publish fill:#1dd1a1,color:#fff,stroke-width:3px
    style Error fill:#ff6b6b,color:#fff
```

### 6.2. Operational Flow - Update & Enhance Path

Sơ đồ mô tả quy trình cập nhật bài viết hiện có, đặc biệt là cơ chế **Enhance by GenAI**.

```mermaid
graph LR
    Existing[Bài viết đã tồn tại trong Editor] --> UpdateChoice{Chọn cách cập nhật}
    
    %% Manual Update
    UpdateChoice -- "Thủ công" --> Manual[Sửa trực tiếp trong Editor]
    Manual --> Publish([Re-Publish])
    
    %% AI Enhance
    UpdateChoice -- "Enhance by GenAI" --> Btn[Click Button Enhance]
    Btn --> Registry{"Unique ID Check<br/>(Kho Định Danh Gốc)"}
    Registry --> Redirect[Redirect to GenAI Content Step 4/5]
    Redirect --> AI_Refine[AI Optimize Outline/Detail]
    AI_Refine --> Sync[Sync back to Blog Editor]
    Sync --> Publish

    %% Styling
    style Existing fill:#f5f6fa,stroke:#dcdde1
    style Registry fill:#f9f,stroke:#333,stroke-width:2px
    style Publish fill:#00b894,color:#fff,stroke-width:2px
```

### 6.3. Workflow Chi tiết - 7 Bước thực thi

Để bắt đầu sử dụng GenAI Content, người dùng thực hiện theo quy trình chuẩn sau:

| Bước | Tên Bước | Hành động | Input/Output | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **Tạo Project** | Khởi tạo Project (Tên Use Case phải là **Duy nhất**) | Project Name (Unique) | PM/Growth |
| **2** | **Business Context** | Nhập bối cảnh theo template 11 fields tại [[business-context]] | Context Layer (Source of Truth) | PM/Growth + SEO Lead |
| **3** | **Keyword Creation** | Tạo Primary Keyword và bộ Secondary Keywords tương ứng | Keyword Master Registry | Content Team |
| **4** | **AI Outline** | AI generate dàn ý thô. Cho phép **Chỉnh sửa & Lưu (Edit & Save)** | Outline Draft -> Final | Content Team |
| **5** | **AI Blog Detail** | AI viết bài chi tiết dựa trên Dàn ý đã chốt ở bước 4 | Blog Detail Draft | AI (Claude API) |
| **6** | **Review Quality** | Kiểm tra chất lượng, SEO/GEO Score và tính chính xác | Verified Content | SEO/GEO Lead |
| **7** | **Sync MoSpark** | Đồng bộ dữ liệu qua Blog Editor của MoSpark để xuất bản | Live on momo.vn | Content Team |

> [!TIP]
> **Business Context** là linh hồn của bài viết. Việc nhập liệu kỹ lưỡng 11 fields ở Bước 2 giúp AI hiểu sâu về sản phẩm MoMo và giảm thiểu rủi ro sai lệch thông tin (Hallucination).

### 6.4. Role & Responsibility Detail

#### PM/Growth (Cell Team)
**Trách nhiệm chính:** Xác nhận nội dung, chịu trách nhiệm pháp lý, bổ sung thông tin sản phẩm/dịch vụ

- **Bước 1:** Khởi tạo Project (tên Use Case - Duy nhất)
- **Bước 2:** **Xác nhận Business Context đầy đủ - chịu trách nhiệm pháp lý & Information Gain**
  - Confirm tất cả 11 fields theo template: Value Prop, Trust Signals, Disclaimer, Blacklist terms
  - Verify không có information sai, không recommend competitor, không overpromise tính năng
  - Ensure tất cả "thông tin lợi ích" (benefit/gain) đều chính xác về sản phẩm/dịch vụ MoMo
- **Bước 4:** Approve Outline final trước khi AI tạo Blog Detail
  - Review outline có align với strategy & positioning của Use Case
  - Từ chối outline nếu có sai lệch, request Content chỉnh sửa

#### Content Team
**Trách nhiệm chính:** Triển khai quy trình, tạo keyword, chỉnh sửa dàn ý, đồng bộ bài viết

- **Bước 3:** Create Primary Keyword + bộ Secondary keywords
- **Bước 4:** Chỉnh sửa Outline
  - Adjust structure, add unique angle, verify keyword integration
  - Lưu và submit Outline final cho PM/Growth approve
- **Bước 7:** Sync MoSpark
  - Thực hiện đồng bộ nội dung từ GenAI qua Blog Editor của MoSpark
  - Kiểm tra lần cuối giao diện hiển thị trước khi Click Publish

#### SEO/GEO Lead (Văn Hiến)
**Trách nhiệm chính:** Đảm bảo tiêu chuẩn SEO/GEO, verify chất lượng trước khi đồng bộ

- **Bước 2:** Validate Business Context framework
  - Confirm 11 fields đầy đủ, context tương thích với Prompt
- **Bước 6:** **Review Quality & SEO/GEO Scoring**
  - Monitor AI output quality, check điểm Scoring tự động
  - Flag nếu có issues: E-E-A-T fail, YMYL risk, content violation
  - **OWNERSHIP - Sign-off Publish:** Xác nhận nội dung đạt chuẩn để chuyển sang bước 7.

### 6.5. Approval Gates

| Gate | Step | Owner | Condition |
|------|------|-------|-----------
| **Business Context Complete** | 2 | PM/Growth + SEO/GEO | Đủ 11 fields, thông tin chính xác, pháp lý clear |
| **Outline Final** | 4 | PM/Growth | Content Team lưu dàn ý -> PM/Growth approve |
| **Content Review** | 6 | SEO/GEO Lead | Bài viết pass SEO/GEO Score -> Sign-off để Sync |

### 6.6. Synchronization & Keyword Master Registry Logic

Hệ thống quản lý nội dung dựa trên nguyên tắc **GenAI Content là Keyword Master Registry (Kho lưu trữ gốc)** của toàn bộ Primary Keywords trong một Project.

1.  **Cơ chế Đồng bộ từ Luồng Mặc Định (Bottom-Up Sync):**
    - Ở Blog Editor, PM không nhập "Primary Keyword" ngay từ đầu quy trình tạo.
    - Tuy nhiên, để đạt điểm **SEO/GEO Score**, PM buộc phải nhập **Primary Keyword** (trước đây là Meta Keyword).
    - **Hành động hệ thống:** Ngay khi Primary Keyword được nhập, MoSpark sẽ tự động tạo một bản ghi (Record) tương ứng trong module GenAI Content với Keyword này.
    - Điều này đảm bảo mọi bài viết "viết tay" đều có một đại diện trong GenAI để sẵn sàng cho tính năng AI Enhance.

2.  **Cơ chế Từ Luồng GenAI Content (Top-Down Sync):**
    - Khi PM tạo một Primary Keyword trong module GenAI, hệ thống sẽ tự động khởi tạo và liên kết (Link) với một bài blog trong Editor.
    - Mọi thay đổi về nội dung từ GenAI (Step 6) sẽ được đồng bộ (Sync) đè lên hoặc cập nhật vào bài blog này.

3.  **Quản lý Tính Unique (Unique ID Check):**
    - **Vị trí kiểm soát:** Duy nhất tại module GenAI Content.
    - **Logic:** Dù bài viết đến từ luồng nào, Primary Keyword (từ Editor hoặc từ GenAI) đều phải "check-in" tại Keyword Master Registry. 
    - Nếu Keyword đã tồn tại, hệ thống sẽ ngăn chặn việc tạo mới và yêu cầu user sử dụng bài viết hiện có để tránh "Content Cannibalization".

---

## 7. Business/Product Context - 11 Fields bắt buộc

> **Owner:** Văn Hiến
> **Thời điểm nhập:** Bắt buộc hoàn thành TRƯỚC khi generate bất kỳ bài viết nào trong Project
> **Mục đích:** Làm nền tảng context cho cả Prompt 1 (Outline) và Prompt 2 (Writer) - đảm bảo AI luôn viết đúng về sản phẩm MoMo, không recommend competitor, không bịa đặt tính năng

### 7.1. 11 Fields bắt buộc

1. **Tên sản phẩm** - Tên chính xác như hiển thị trong App/Web
2. **URL Web** - URL canonical của trang chính
3. **Mô tả sản phẩm** - 3-5 câu, phân biệt Web vs App
4. **Đối tượng sử dụng** - Persona chính (ai, ở đâu, job gì)
5. **Đối tác** - Tên đối tác cung cấp data/dịch vụ (nếu có)
6. **Điều kiện sử dụng** - Giới hạn, yêu cầu user cần biết
7. **Value Prop / USPs** - Danh sách điểm giá trị nổi bật (AI phải integrate tự nhiên)
8. **Trust Signals** - Yếu tố tạo độ tin cậy so với competitor
9. **Khác biệt vs đối thủ** - So sánh trực tiếp, honest (bao gồm cả điểm chưa bằng)
10. **Disclaimer** - Pháp lý/tài chính (theo YMYL guideline)
11. **Từ ngữ bị cấm** - Blacklist terms (sai sản phẩm, pháp lý risk, competitor)

---

## 8. Lộ trình (Roadmap)

### Phase 1: Foundation & Scaling (May 2026)
1. ✅ **7-Step Workflow live:** Blog Detail AI + Blog Editor Publish separation
2. ✅ **Phạt Nguội pilot:** Foundation complete
3. ✅ **Scale Financial products:** Vay Nhanh, Ví Trả Sau, CIC

### Phase 2: Performance Tracking & Optimization (June 2026+)
- **Google Search Console API Integration:** Theo dõi hiệu suất per Project
- **Metrics per Project:** Organic traffic, impressions, CTR, avg position
- **Automated Insights:** Gợi ý tối ưu nội dung dựa trên data
- **Content Refresh Automation:** Identify underperforming articles - suggest updates

---

*Document: BRD-MoSpark-GenAI-Content · v3.5 (Integrated Prompt Engineering Skill)*

---

## 9. GenAI Operational Standards & Prompt Strategy (Integrated Skill)

> **Role:** Văn Hiến (SEO & GEO Lead)
> **Engine:** Claude API (Integrated in MoSpark)
> **Goal:** Tạo nội dung chuẩn SEO/GEO, đạt E-E-A-T và sẵn sàng cho AI Search Citation.

### 9.1. Nguyên tắc cốt lõi (Core Principles)
*   **Zero-Hallucination**: Luôn yêu cầu AI sử dụng dữ liệu thực tế (Pháp luật, số liệu từ BU).
*   **Context Injection**: Truyền bối cảnh dự án (Primary Keyword, Target Audience) vào Prompt.
*   **Structure-First**: Luôn yêu cầu AI tạo Outline trước khi viết nội dung chi tiết.

### 9.2. Framework Prompt cho Blog Content
Quy trình này khớp với **Bước 4 & Bước 6** trong Workflow hệ thống:

*   **Phase A: Outline Generator (Step 4)**
    *   **Input**: Primary Keyword + Target Audience + Key Message.
    *   **Prompt Master**: [[momo-blog-prompt-1-outline]]
*   **Phase B: Content Writer (Step 6)**
    *   **Input**: Outline từ Phase A + [[momo-seo-geo-guideline]] + [[momo-ymyl-guideline]].
    *   **Prompt Master**: [[momo-blog-prompt-2-writer]]

### 9.3. Quality Gate Standards (SEO/GEO Score)
Nội dung sau khi GenAI tạo ra phải được tự động chấm điểm qua [[mospark-seo-geo-score-brd]]. Các tiêu chí bắt buộc:
*   Mật độ từ khóa chính.
*   Sự hiện diện của FAQ Schema.
*   Độ dài và cấu trúc Heading.
