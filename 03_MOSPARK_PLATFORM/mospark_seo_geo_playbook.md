---
name: mospark_seo_geo_playbook
description: >
  Tài liệu tổng hợp về Chiến lược (HubSpot Parity) và Vận hành (Operational Playbook) 
  cho các dự án SEO/GEO trên nền tảng MoSpark.
---

# 📘 MoSpark SEO/GEO Playbook: Strategy & Operations

Tài liệu này hợp nhất tầm nhìn chiến lược "HubSpot Parity" và quy trình thực thi thực tế để biến MoSpark thành một hệ điều hành tăng trưởng (Growth OS).

---

## 1. Tầm nhìn chiến lược: MoSpark vs HubSpot

Mục tiêu của MoSpark không phải là copy HubSpot, mà là **lấp đầy vùng MoSpark đang trống** (post-publish measurement) trong khi **giữ nguyên lợi thế MoSpark đang có** (pre-publish quality gate, GEO scoring, GenAI production).

### 1.1. Triết lý vận hành
| Chiều | HubSpot | MoSpark |
|---|---|---|
| **Mạnh nhất** | Đo lường & Giám sát sau xuất bản | Kiểm soát chất lượng & AI Production trước xuất bản |
| **Yêu nhất** | Content quality gate (không có hard block) | Visibility tracking sau khi nội dung live |
| **Triết lý** | "Đo xong mới biết cần làm gì" | "Chuẩn hóa trước khi ra ngoài" |

### 1.2. Bản đồ năng lực & Khoảng trống (Gap Analysis)
MoSpark đang hướng tới việc lấp đầy các Gap sau:
- **Nhóm A (Content Strategy):** Thiếu Cluster Map UI trực quan để PM quản lý độ phủ thị trường.
- **Nhóm B (SEO Recommendations):** Thiếu Per-article Analytics tích hợp trong Editor và cảnh báo Content Decay.
- **Nhóm C (GEO/AEO Monitoring):** Thiếu Dashboard đo lường SoV và Visibility tự động theo từng Use Case.

---

## 2. Quy trình vận hành (Project Workflow)

Mọi dự án tăng trưởng trên MoSpark phải tuân thủ quy trình khép kín dưới đây:

```mermaid
graph TD
    subgraph Phase_0_Analysis [Phase 0: Phân tích & Tìm Gap]
        A[Bắt đầu: Use Case/Market] --> B[SEO Inventory: Market Map]
        B --> C[Gap Analysis]
        C --> D[Umami: Performance Audit]
        D --> E{Start to Zero?}
        E -->|Yes| F[Xây mới hoàn toàn]
        E -->|No| G[Tính toán SoV hiện tại]
        G --> H{"SoV < 40%?"}
        H -->|Yes| I[Lập kế hoạch Scale/Optimize]
        H -->|No| J[Duy trì & Theo dõi]
    end

    subgraph Phase_1_Initiation [Phase 1: Thiết lập Context]
        F --> K[Business Context]
        I --> K
        K --> L[MoSpark CMS: Create Project]
        L --> M[Distribution Rules: Auto-link/Widgets]
    end

    subgraph Phase_2_Production [Phase 2: Thực thi GenAI]
        M --> N[Primary Keyword: From Inventory]
        N --> O[GenAI: Outline Prompt]
        O --> P[GenAI: Writer Prompt]
        P --> Q{"SEO/GEO Score >= 80?"}
        Q -->|No| P
        Q -->|Yes| R[Publish]
    end

    subgraph Phase_3_Growth_Loop [Phase 3: Vòng lặp tăng trưởng]
        R --> S[Umami & GSC Tracking]
        S --> T{"SoV Growth?"}
        T -->|Stagnant| U[Audit: Content Decay / AI Enhance]
        U --> O
        T -->|Growing| V[Scale to New Keywords]
    end

    style B fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
    style K fill:#dfd,stroke:#333,stroke-width:2px
    style Q fill:#ffcccb,stroke:#a00,stroke-width:2px
```

---

## 3. Chi tiết các giai đoạn thực thi

### Giai đoạn 0: Phân tích Tiền dự án (Pre-Project Analysis)
1. **Kiểm tra SEO Inventory (Market Potential):** Tra cứu **Total Market Volume** của Use Case tại tài liệu mospark_seo_inventory.
2. **Đo lường hiệu suất & Tính SoV (Umami Audit):** 
   - Lọc dữ liệu trên Umami theo **URL Path** của Cluster (ví dụ: `/blog/phat-nguoi/*`).
   - Lấy **Total Sessions (30 ngày gần nhất)**.
   - Tính **SoV (%) = (Sessions / Market Volume) * 100**.
3. **Quyết định thực thi (Decision Matrix):**
   - **SoV < 1% (Start to Zero):** Dự án mới hoàn toàn ➔ Sản xuất nội dung mới ồ ạt.
   - **SoV 1% - 20% (High Gap):** Đã có traffic nhưng chưa tương xứng tiềm năng ➔ Tạo satellite content để bao phủ thêm từ khóa phụ.
   - **SoV 20% - 40% (Growth Phase):** Đang tăng trưởng ➔ Ưu tiên dùng tính năng **AI Enhance** để tối ưu hóa nội dung cũ lên Top 3.
   - **SoV > 40% (Dominating):** Vị thế dẫn đầu ➔ Chỉ cần duy trì và theo dõi Content Decay.

### Giai đoạn 1: Khởi tạo Project (Initiation)
1. **Business Context:** Điền đầy đủ bối cảnh tại mospark_business_context. Đây là "linh hồn" để AI viết đúng hướng.
2. **Cấu hình CMS:** Tạo Use Case, gán bối cảnh và thiết lập Distribution Rules (Auto-embed, Cross-linking).

### Giai đoạn 2: Sản xuất Nội dung (Production)
1. **GenAI Pipeline:** 
   - Lấy Primary Keyword từ Inventory.
   - Chạy luồng Outline ➔ Writer Prompt.
2. **Quality Gate:** Kiểm tra tại mospark_seo_geo_score. Đảm bảo đạt **80+ điểm** mới được Publish.

### Giai đoạn 3: Theo dõi & Tối ưu (Growth Loop)
1. **Performance Tracking:** Theo dõi Organic Sessions và Ranking hàng tuần.
2. **Self-Optimization:** Nếu traffic giảm (Content Decay), sử dụng tính năng **Enhance by AI** để cập nhật bài viết.

---

## 4. Cơ chế Tương tác Giữa các Module (System Interaction)

Để vận hành hiệu quả, hệ thống MoSpark chia tách rõ ràng giữa khâu **Chiến lược (Planning)** và khâu **Thực thi (Execution)**. Sơ đồ dưới đây mô tả cách thức module Quản lý Project tương tác với module GenAI Content:

```mermaid
graph LR
    %% Planning Module
    subgraph Planning [CHIẾN LƯỢC & INVENTORY]
        P1[SEO Inventory] --> P2[Create SEO/GEO Project]
        P2 --> P3[Input Business Context]
        P3 --> P4[(Keyword Master Registry)]
    end

    %% Execution Module
    subgraph Execution [THỰC THI & GENAI]
        E1[Article Creation] --> E2{Check Unique ID}
        P4 -.-> E2
        E2 -- "Hợp lệ" --> E3[Fetch Context from Project]
        E3 --> E4[GenAI 7-Step Workflow]
        E4 --> E5[Sync & Publish]
    end

    %% Legend
    P4 -- "1-1 Rule" --> E1
    
    style Planning fill:#e3f2fd,stroke:#1565c0
    style Execution fill:#f1f8e9,stroke:#2e7d32
    style P4 fill:#fce4ec,stroke:#c2185b,stroke-width:2px
```

---

## 5. Lộ trình nâng cấp (Roadmap to HubSpot Parity)

| Giai đoạn | Trọng tâm tính năng | Mục tiêu |
| :--- | :--- | :--- |
| **Tier 1 (Quick Win)** | Cluster Map UI, Per-article Analytics Embed | PM nhìn thấy độ phủ thị trường và hiệu suất bài viết ngay trong Editor. |
| **Tier 2 (Medium)** | Keyword Ranking Tracker, Content Decay Alert | Tự động cảnh báo khi từ khóa rớt hạng để kịp thời refresh. |
| **Tier 3 (Strategic)** | GEO Monitoring Dashboard, Citation Analysis | Đo lường mức độ AI trích dẫn MoMo so với đối thủ cạnh tranh. |

---

- [[mospark_business_context]]

---

### Quy tắc Dữ liệu Cốt lõi (Data Governance)
*   **Bắt buộc có Project:** Keyword không thể tồn tại nếu không gắn với Project (để lấy bối cảnh).
*   **Tính duy nhất (1-1):** Một Primary Keyword chỉ tương ứng với một bài viết duy nhất.
*   **Chủ sở hữu duy nhất:** Một Primary Keyword chỉ thuộc về một Project duy nhất (để quản lý URL).

---
*Document: mospark_seo_geo_playbook · v2.1 · Văn Hiến (SEO & GEO Lead)*
