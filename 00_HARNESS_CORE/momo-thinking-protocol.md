---
title: "MoMo Thinking Protocol (Read-Use-Answer)"
description: "Quy trình tư duy hệ thống áp dụng cho AI và con người khi xử lý tác vụ trong MoMo Knowledge Base."
last_reviewed: 2026-05-18
next_review: 2026-08-18
---

# 🧠 MoMo Thinking Protocol: ĐỌC - DÙNG - TRẢ

Mục tiêu của Protocol này là biến mọi câu trả lời từ một ý kiến cá nhân thành một giải pháp có hệ thống, dựa trên dữ liệu và bám sát chiến lược.

---

## 🔍 Bước 1: ĐỌC (Identify Context)
Trước khi đưa ra bất kỳ nhận định nào, phải xác định được các nguồn tin cậy nhất (Single Source of Truth):

1.  **Chiến lược (Strategic Plan):** Đọc [[01_STRATEGIC_PLAN/web-momo-okrs-2026|Web MoMo OKRs 2026]] để hiểu mục tiêu North Star.
2.  **Bối cảnh dự án (Business Context):** Đọc các file `business_context_*.md` hoặc [[04_MOSPARK_PLATFORM/mospark_business_context|MoSpark Business Context Template]] để hiểu mô hình kinh doanh.
3.  **Thực thi (Implementation):** Đọc bản BRD mới nhất của Use Case đó trong folder [[05_USE_CASE_MOMO/dich-vu-cong-brd|05_USE_CASE_MOMO]].
4.  **Dữ liệu thực (Data):** Đọc các file báo cáo trong [[06_REPORTS/report-thang-05-2026|06_REPORTS]] để lấy baseline thực tế.

**Câu hỏi tự kiểm tra:** "Tôi đã đọc đúng file Master mới nhất chưa? Có thông tin nào mâu thuẫn trong Vault không?"

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
