# PROJECT ORCHESTRATOR - MoMo Out-App Traffic

> **Role:** Master Controller / Project Lifecycle Engine
> **Purpose:** Điều phối việc áp dụng Principles, Methodologies và Skills vào 9 bước Web Build Workflow.
> **Owner:** Văn Hiến

---

## 1. Web Build Workflow Engine

Dưới đây là bản đồ điều hướng dự án. Agent phải xác định dự án đang ở bước nào để "load" các tài liệu tương ứng.

| Bước | Tên Giai Đoạn | Skill/Methodology Cần Dùng | Output Cần Đạt | Gate Check (Core Principle) |
|:---:|---|---|---|---|
| **01** | **Research & Discovery** | `02_Methodologies_Frameworks/jtbd-analysis.md` | Keyword Map, Competitor Report | [ ] JTBD Mapping chính xác |
| **02** | **Thiết lập Mục tiêu** | `03_Operational_Skills/brd-momo.md` | KPI Doc: Traffic, W2A target | [ ] Pyramid Principle (SCR) |
| **03** | **Product Brief + Tracking** | `03_Operational_Skills/brd-momo.md` | Final BRD + Event Tracking Spec | [ ] Zero Hallucination (Data source) |
| **04** | **Build Demo Website** | `03_Operational_Skills/momo-html-formatting-skill.md` | Live Demo (Vercel/HTML) | [ ] MoMo Design Standard |
| **05** | **Coding & Sprint** | `00_Context_Identity/hienho-momo-master-doc.md` (Section 2) | Staging URL | [ ] Technical SEO Foundation |
| **06** | **SEO Review & QA** | `03_Operational_Skills/Seo-Geo-audit.md` | QA Report, SEO Checklist Pass | [ ] Mobile-First UX |
| **07** | **Staging & Sign-off** | `03_Operational_Skills/Web2App-Pipeline.md` | Tracking Verified, PO Sign-off | [ ] Attribution Chain Integrity |
| **08** | **Roll Out** | `03_Operational_Skills/use-case-document.md` | Production Live, Sitemap Submitted | [ ] URL Governance Level 1-4 |
| **09** | **Monitoring** | `00_Context_Identity/hienho-momo-master-doc.md` (Section 5) | 30/60/90 Days Report | [ ] Organic Traffic Growth |

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
