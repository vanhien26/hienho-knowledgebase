# 🧠 MoMo Thinking Protocol: ĐỌC - DÙNG - TRẢ

Mục tiêu của Protocol này là biến mọi câu trả lời từ một ý kiến cá nhân thành một giải pháp có hệ thống, dựa trên dữ liệu và bám sát chiến lược.

---

## 🔍 Bước 1: ĐỌC (Identify Context & Knowledge Routing)
Trước khi đưa ra bất kỳ nhận định nào, phải tra cứu và tuân thủ bảng định tuyến dữ liệu trong [[00_HARNESS_CORE/KNOWLEDGE_ROUTING.md|Knowledge Routing & Context Pipeline]] để xác định đúng nguồn tin cậy nhất (Single Source of Truth - SSOT):

1.  **Định tuyến Khái niệm & Từ khóa:** Tham chiếu [[00_HARNESS_CORE/KNOWLEDGE_ROUTING.md|Knowledge Routing Pipeline]] để phân biệt chính xác loại tài liệu (Ví dụ: `Townhall` = Chỉ đạo BOM vĩ mô vs `Monthly Report` = Báo cáo hiệu suất team).
2.  **Chiến lược (Strategic Plan):** Đọc [[01_STRATEGIC_PLAN/web-momo-okrs-2026|Web MoMo OKRs 2026]] để hiểu mục tiêu North Star.
3.  **Bối cảnh dự án (Business Context):** Đọc các file `business_context_*.md` hoặc [[04_MOSPARK_PLATFORM/mospark_genai_content#7. Business Context - Các trường bắt buộc|MoSpark Business Context Template]] để hiểu mô hình kinh doanh.
4.  **Thực thi (Implementation):** Đọc bản BRD mới nhất của Use Case đó trong folder [[06_USE_CASE_MOMO/dich-vu-cong-brd|06_USE_CASE_MOMO]].
5.  **Dữ liệu thực (Data):** Đọc các file báo cáo trong [[07_REPORTS/docs/report-thang-05-2026|07_REPORTS]] để lấy baseline thực tế.

**Câu hỏi tự kiểm tra:** "Tôi đã tham chiếu đúng Knowledge Routing chưa? Đã phân biệt đúng khái niệm (như Townhall vs Monthly Report) chưa?"

---

## 🛠️ Bước 2: DÙNG (Select Framework & Tools)
Xác định "vũ khí" tư duy sẽ sử dụng để giải quyết vấn đề:

1.  **Framework (Folder 02_FRAMEWORKS):**
    *   Cần phân tích ưu tiên? Dùng [[02_FRAMEWORKS/80-20-growth|80-20 Growth Framework]].
    *   Cần tìm hiểu insight khách hàng? Dùng [[02_FRAMEWORKS/jtbd-analysis|JTBD Analysis Framework]].
    *   Cần cấu trúc báo cáo sếp? Dùng [[02_FRAMEWORKS/pyramid-principle|Pyramid Principle]].
2.  **Skills & Guidelines (Folder 03_SKILLS):**
    *   Cần viết blog? Dùng [[03_SKILLS/momo-seo-geo-guideline|MoMo SEO & GEO Guidelines]].
    *   Cần audit tracking? Dùng [[03_SKILLS/web-tracking|Web Tracking Setup]].
3.  **Platform Specs (Folder 04_MOSPARK_PLATFORM):**
    *   Cần hiểu khả năng hệ thống? Tham chiếu [[04_MOSPARK_PLATFORM/mospark_master|MoSpark Master Specs]].

**Câu hỏi tự kiểm tra:** "Framework này có giải quyết đúng root cause không? Skill này đã được cập nhật chưa?"

---

## 📝 Bước 3: TRẢ (Structure Output)
Cấu trúc câu trả lời phải đảm bảo 3 yếu tố: **Chiến lược - Thực thi - Đo lường**.

1.  **Tóm tắt (Strategic Alignment):** Câu trả lời này giúp đạt được KR nào trong OKR 2026?
2.  **Nội dung chính (Actionable Steps):** Các bước cụ thể (P0, P1, P2). Không nói lý thuyết suông.
3.  **Dẫn chứng (Information Gain):** Trích dẫn số liệu hoặc logic đặc thù của MoMo.
4.  **Liên kết (Cross-linking):** Luôn trỏ link về các file tài liệu liên quan trong Vault để duy trì tính kết nối.

**Cấu trúc chuẩn của một phản hồi:**
> - **Mục tiêu:** [X]
> - **Dữ liệu đã đọc:** [Link file]
> - **Framework áp dụng:** [[Tên Framework]]
> - **Giải pháp cụ thể:** [Nội dung]

---

## 🚀 Áp dụng thực tế cho AI
Mỗi khi nhận được yêu cầu, AI phải thực hiện một bước "Suy nghĩ thầm" (Thought) dựa trên Protocol này trước khi xuất kết quả cuối cùng.

## ⚠️ Quy tắc Cốt lõi về Quản lý File (File Management Constraints)
*   **Không tự ý tạo file mới:** Tuyệt đối không tự động tạo bất kỳ file mới nào trong project (kể cả file báo cáo hay ghi chép) trừ khi có yêu cầu hoặc đề cập trực tiếp từ phía User. Mọi thông tin phản hồi, phân tích hoặc báo cáo phải được hiển thị trực tiếp trong phần trả lời hoặc cập nhật vào các file đã có trong dự án (nếu được phép).

