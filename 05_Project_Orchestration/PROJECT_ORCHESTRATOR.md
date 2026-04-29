# PROJECT ORCHESTRATOR - MoMo Out-App Traffic

> **Role:** Master Controller / Project Lifecycle Engine
> **Purpose:** Điều phối việc áp dụng Principles, Methodologies và Skills vào 9 bước Web Build Workflow.
> **Owner:** Văn Hiến

---

## 1. Web Build Workflow Engine

Dưới đây là bản đồ điều hướng dự án. Agent phải xác định dự án đang ở bước nào để "load" các tài liệu tương ứng.

| Bước | Tên Giai Đoạn | Stakeholder Chủ Trì | Skill/Methodology | Gate Check (Core Principle) |
|:---:|---|---|---|---|
| **01** | **Research & Discovery** | Hiến + Inbound | [[jtbd-analysis]] | [ ] [[jtbd-analysis|JTBD Mapping]] |
| **02** | **Thiết lập Mục tiêu** | Hiến | [[brd-momo]] | [ ] [[pyramid-principle|Pyramid Principle]] |
| **03** | **Product Brief** | Hiến | [[momo-seo-content-brief]] | [ ] [[critical-thinking|Logic Check]] |
| **04** | **Sprint & Build** | Web Platform | [[momo-html-formatting-skill]] | [ ] Technical Standard |
| **05** | **Build Demo** | Web Platform | [[hienho-momo-master-doc]] | [ ] Internal Link Integrity |
| **06** | **SEO Review (Gate 1)** | Hiến | [[Seo-Geo-audit]] | [ ] **Gate 1: SEO/GEO Score** |
| **07** | **Sign-off (Gate 2)** | Hiến | [[Web2App-Pipeline]] | [ ] **Gate 2: Foundation Checklist** |
| **08** | **Roll Out & Content** | Inbound | [[use-case-document]] | [ ] [[mospark-seo-geo-score-brd|Publish Gate]] |
| **09** | **Monitoring** | Hiến + Inbound | [[web-tracking]] | [ ] Organic Traffic Growth |

---

## 2. Agent Execution Guide (SOP)

Khi tiếp nhận yêu cầu về dự án, Agent thực hiện theo quy trình sau:

1.  **Identify State**: Kiểm tra dự án thuộc `04_Execution_Use_Cases` đang ở bước nào (hoặc hỏi User).
2.  **Load Harness**:
    *   Đọc `00_Context_Identity` để nắm bối cảnh team.
    *   Đọc Skill tương ứng với bước hiện tại trong bảng trên.
    *   Luôn tuân thủ `01_Core_Principles` trong mọi phản hồi.
3.  **Execute**: Thực thi tác vụ (Viết BRD, Audit, Tạo HTML...).
4.  **Verify**: Tự kiểm tra kết quả dựa trên các **Gate Check** trước khi phản hồi User.

---

## 3. Active Pipeline Board

> *Phần này dùng để theo dõi các dự án đang chạy (Cần cập nhật thường xuyên)*

| Dự án | Giai đoạn hiện tại | PIC | Status | Link tài liệu |
|---|---|---|---|---|
| **Phạt Nguội** | Step 08: Roll Out | Hiến | P0 - Live đầu T5 | [phat-nguoi-brd.md](file:///Users/hienhv/HienHv/from%20Klaus/hovanhien_knowledgebase_momo/04_Execution_Use_Cases/Project-Instances/phat-nguoi-brd.md) |
| **Ads Manager** | Step 03: Product Brief | Thuận/Hiến | In Review | [ads-manager-brd-final.md](file:///Users/hienhv/Downloads/ads-manager-brd-final.md) |
| **VTS Merchant** | Step 01: Research | Hiến | Active | [doi-tac-brd.md](file:///Users/hienhv/HienHv/from%20Klaus/hovanhien_knowledgebase_momo/04_Execution_Use_Cases/Project-Instances/doi-tac-brd.md) |

---

## 4. Quality Gatekeeper (Audit Rules)

Mọi output từ Agent phải đi qua bộ lọc này:
*   **Accuracy**: Không Hallucinate dữ liệu (Source: GSC/Appsflyer).
*   **Logic**: Trình bày theo Pyramid Principle (Summary trước, Detail sau).
*   **Intent**: Luôn anchor vào JTBD của người dùng.
*   **Format**: Đúng chuẩn MoMo HTML Design System (nếu output là HTML).
