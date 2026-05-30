# BRD: Finhub Simulation Mini Web

> - **Project:** Finhub Simulation Mini Web (v2)
> - **Channel:** Điểm chạm số (Web/SEO & AI Search)
> - **Division:** Finhub (Trung Tâm Tài Chính)
> - **Status:** Đang triển khai (MVP Tháng 6/2026)
> - **Last Updated:** 28/05/2026

---

## 1. Executive Summary & Objective

Dự án xây dựng chuỗi công cụ giả lập (Simulation) trên nền tảng Web cho hệ sinh thái Finhub. Thay vì chỉ là các bài viết tĩnh, Web sẽ đóng vai trò như một "phễu hứng" (Top-of-funnel) thông qua các công cụ tính toán tương tác, giúp user giải quyết các bài toán tài chính cá nhân cụ thể.

**Mục tiêu (Objectives):**
1. **Update & Upgrade:** Cập nhật text, visual cho các zone đã present ở Ver 1 (bản demo). Không thay đổi structure lớn.
2. **Direction Shift:** Chuyển dịch định hướng Landing page Finhub từ "chỉ tập trung vào SEO truyền thống" sang **"AI Citation"** kết hợp với **Simulation**. Tối ưu hóa để các AI Bots (như ChatGPT, Gemini, Perplexity) có thể đọc, trích dẫn và điều hướng người dùng về trang.

## 2. Strategic Context & User Insight

**Định vị sản phẩm (FinHub Positioning):**
FinHub được định vị là Trung Tâm Tài Chính giúp người dùng quản lý và tối ưu tài chính cá nhân. Tại miniapp này, user có thể:
- Quản lý tổng tài sản và biến động
- Quản lý từng sản phẩm tài chính đang sử dụng
- Khám phá các sản phẩm tài chính khác
- Nhận mẹo gợi ý để tối ưu tiền của bạn

**Vấn đề (The Gap) & Giải pháp (The Hook):**
- Hiện tại, Monthly Active Users (MEU) của FinHub chiếm khoảng **~60% MAU của toàn app MoMo**. Mặc dù tỷ lệ này rất tốt, nhưng bài toán tăng trưởng yêu cầu phải mở rộng ra các kênh **out-app** để tiếp cận nhóm user "non-app" (người dùng chưa cài MoMo hoặc chưa từng dùng dịch vụ tài chính trên MoMo).
- Đây là những usecase gồm hot keywords liên quan đến chủ đề quản lý tài chính và tài chính cá nhân: *thu nhập sau thuế, vay/tín dụng, lãi tiết kiệm…*
- **Learning Case:** Dựa vào thành công từ mô hình tính lương Gross-Net của TopCV - dùng tool tiện ích làm phễu đầu vào để phục vụ nhu cầu của mass user.

## 3. Product Features: The 5 Core Simulations

**JTBD Cốt lõi của User:** 
Trong những component này, mục tiêu trước hết là cho user biết FinHub là một ecosystem tài chính, giúp họ nắm rõ cơ hội tối ưu tài chính cá nhân.

Hệ thống bao gồm 5 components được sắp xếp theo mức độ ưu tiên (Priority) dựa trên Keyword Research (mức độ attractive):

| Priority | Component (Simulation) | Nhu cầu (JTBD) & Lợi ích mang lại | Technical Note |
|:---:|---|---|---|
| **1** | **Thu nhập sau thuế** | User biết mình có thực nhận bao nhiêu tiền, có thể chi tiêu bao nhiêu, nên phân bổ như thế nào. | Làm tương tự `topcv.vn/tinh-luong-gross-net` |
| **2** | **Lãi Tiết kiệm** | User biết có thể được hưởng lợi bao nhiêu từ khoản không dùng, có thể gửi tiết kiệm. | Fix |
| **3** | **Vay nhanh** | User biết cơ hội khoản dự phòng khi cần trong trường hợp khẩn cấp. | Đã có web, Copy/Paste |
| **4** | **Đầu tư** | User biết cơ hội tăng tài sản cụ thể với số tiền họ có, với một mã cổ phiếu cụ thể, trong khoảng thời gian, dựa vào giá chính xác của thị trường. | Kéo API giá thị trường |
| **5** | **BHSK+** | User có bức tranh rõ ràng về việc cần phân bổ bao nhiêu cho bảo hiểm mỗi tháng, lợi ích thế nào cho từng usecase. | Fix |

*=> Việc chia 5 components này để đảm bảo cover được các usecase mà user quan tâm, mở phễu đầu vào. Simulation giúp user hình dung chính xác lợi ích của từng sản phẩm. Kéo vào Trung Tâm Tài Chính để khám phá và trải nghiệm hệ sinh thái tài chính tại MoMo.*

## 4. Technical & AI Citation Direction

Để đón đầu xu hướng tìm kiếm AI (Generative Engine Optimization - GEO), cấu trúc kỹ thuật của hệ thống Simulation phải tuân thủ nghiêm ngặt các quy tắc sau:

### 4.1 AI Citation Strategy (Tối ưu cho AI Bots)
- **Content Framework:** Tối ưu hóa SEO truyền thống vẫn là nền tảng, nhưng cấu trúc bài viết (Heading, List, Table) phải mạch lạc để LLM dễ đọc hiểu.
- **Technical Schema:** Bắt buộc cài đặt Schema Markup (VD: `SoftwareApplication`, `FinancialProduct`, `FAQPage`) cho từng công cụ.
- **Bot Accessibility:** Tuyệt đối không chặn các bot của AI (như `GPTBot`, `Google-Extended`, `Claude-Web`) trong file `robots.txt` hoặc Header Firewall.
- **Action Item:** Web Team tư vấn thêm về technical requirement và định dạng trình bày để Inbound Team triển khai nội dung chuẩn AI.

### 4.2 Data & API Integration
- 4/5 Simulation yêu cầu Data/API từ backend để đảm bảo tính chính xác (ví dụ: Công thức tính thuế mới nhất, Lãi suất tiết kiệm realtime, Giá cổ phiếu thị trường).
- PO Cell Team cần cung cấp Docs API chuẩn để Web Dev tiến hành Research tech feasibility và Implementation approach.

## 5. Timeline & Next Steps

**Timeline:** Rollout MVP trong **tháng 6/2026** (Ưu tiên các usecase theo bảng Priority và Feasibility của resource).

**Action Items:**
- [x] **Finhub/PO:** Cung cấp chi tiết insight rationale, expected outcome, reference landscape cho 5 components.
- [ ] **PO Cell Team:** Gửi lại docs API cho Web Team.
- [ ] **Web Team:** Research Tech feasibility, định hướng UI, chốt implementation approach.
- [ ] **Web Team:** Evaluate pilot scope, chốt priority direction align với BU.
- [ ] **Finhub (Inbound Team):** Work với Web Team để chốt Content framework chuẩn AI Citation.
