# PROJECT ORCHESTRATOR - MoMo Out-App Traffic

> **Role:** Master Controller / Project Lifecycle Engine
> **Purpose:** Điều phối việc áp dụng Principles, Methodologies và Skills vào 9 bước Web Build Workflow.
> **Owner:** Văn Hiến
> **Operational Engine:** [[OPERATIONAL_ROUTINE]]

---

## 1. Web Build Workflow Engine

Dưới đây là bản đồ điều hướng dự án. Agent phải xác định dự án thuộc `04_Execution_Use_Cases` đang ở bước nào (hoặc hỏi User).

| Bước | Tên Giai Đoạn | Stakeholder Chủ Trì | Skill/Methodology | Gate Check (Core Principle) |
|:---:|---|---|---|---|
| **01** | **Research & Discovery** | Hiến + Inbound | [[jtbd-analysis]] | [ ] [[jtbd-analysis|JTBD Mapping]] |
| **02** | **Thiết lập Mục tiêu** | Hiến | [[brd-momo]] | [ ] [[pyramid-principle|Pyramid Principle]] |
| **03** | **Product Brief + Tracking Plan** | Hiến + PO Cell | [[genai-content-brd]] | [ ] [[critical-thinking|Logic Check]] |
| **03.5** | **Feasibility Sync với Cell Team** | Hiến + PO Cell | [[brd-momo]] | [ ] Scope v1 xác nhận |
| **05** | **Sprint Planning & Coding** | PO Cell + Dev | [[momo-html-formatting-skill]] | [ ] Technical Standard |
| **06** | **SEO Review + QA Testing (Gate 1)** | Hiến + Dev | [[Seo-Geo-audit]] | [ ] **Gate 1: SEO/GEO Score** |
| **07** | **Staging & Sign-off (Gate 2)** | Hiến + PO Cell + Dev | [[Web2App-Pipeline]] | [ ] **Gate 2: Foundation Checklist** |
| **08** | **Roll Out (Production)** | Hiến + Dev | [[use-case-document]] | [ ] [[mospark-seo-geo-score-brd|Publish Gate]] |
| **09** | **Post-Launch Monitoring** | Hải/Hoàng (DA) + Hiến | [[web-tracking]] | [ ] Organic Traffic Growth |

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
| **Phạt Nguội** | Step 08: Roll Out (Partial) | Hiến + Hùng (FE) + Hoài Anh (API) | **Trang chủ golive - đang index. Next: Tool tra cứu + Sub-pages (/o-to, /xe-may) + Sitemap + llms.txt** | [[phat-nguoi-brd]] |
| **Ads Manager** | Step 09: Monitoring | Thuận/Hiến | **Balloon Ads Deployed (Pilot)** | [[ads-manager-brd]] |
| **MoSpark Migration** | Step 01: Research | Bảo/Hiến | Active - Mapping Phase | [[mospark-migration-brd]] |
| **GenAI Content** | Step 03: Build | Trọng/Hiến | Claude API Integration | [[genai-content-brd]] |
| **LP Builder** | Step 09: Monitoring | Web Platform | Q2 Onboarding GPD | [[mospark-migration-brd]] |
| **LLMs.txt & Robots.txt** | Step 02: Thiết lập Mục tiêu | Hiến + Bảo | **BRD done - Pending: robots.txt nâng cấp + deploy llms.txt trước tiên trên Phạt Nguội** | [[llms-robots-txt-brd]] |
| **VTS/Đối Tác** | Step 01: Research | Hiến | Active - BRD done, chờ Legacy Audit + align VTS PO | [[doi-tac-brd]] |
| **Vay Nhanh** | Step 02: Thiết lập Mục tiêu | Hiến + Inbound | Pending stakeholder review - Keyword/GSC/Ranking baseline done | [[vay-nhanh-brd]] |
| **BHXM** | Step 01: Research | Hiến | Draft - chưa có growth plan post-spike | [[bhxm-brd]] |
| **eSIM Du Lịch** | Step 01: Research | Hiến | Draft - chờ PO + Dev review | [[esim-du-lich-brd]] |

---

## 4. Quality Gatekeeper (Audit Rules)

Mọi output từ Agent phải đi qua bộ lọc này:
*   **Accuracy**: Không Hallucinate dữ liệu (Source: GSC/Appsflyer).
*   **Logic**: Trình bày theo Pyramid Principle (Summary trước, Detail sau).
*   **Intent**: Luôn anchor vào JTBD của người dùng.
*   **Format**: Đúng chuẩn MoMo HTML Design System (nếu output là HTML).
