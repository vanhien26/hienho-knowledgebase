# BRD: GenAI Content Platform (MoSpark Module)

> **Product Manager:** Anh Bảo (Web Platform Manager)
> **Tech Lead:** Trần Công Hoàng Trọng (Software Engineer II)
> **Integration Support:** Bùi Minh Nhật (Senior Software Engineer)
> **Governance & Prompts:** Văn Hiến (SEO & GEO Lead)
> **Start Date:** May 2026
> **Status:** Kicking Off - CEO Mandate (Phạt Nguội Pilot)

---

## 1. Mục tiêu (Goals)
Xây dựng pipeline sản xuất nội dung SEO/GEO chuẩn bằng AI thay thế quy trình viết tay thủ công:
*   **Scale**: Sản xuất hàng loạt bài viết chất lượng cao trong thời gian ngắn.
*   **Standard**: Đảm bảo 100% bài viết đạt tiêu chuẩn E-E-A-T và YMYL.
*   **SEO/GEO Ready**: Cấu trúc nội dung tối ưu cho việc trích dẫn (Citation) trên AI Search (Gemini, AI Overview).

## 2. Pilot Use Case: Phạt Nguội (CEO Mandate)
*   **Current State**: Đang triển khai tích hợp Claude API vào MoSpark. Đang xây dựng bộ **Content Skills** (Prompt templates) chuẩn hóa.
*   **Objective**: Đạt mục tiêu **Top of Mind** cho dự án Phạt Nguội.
*   **Deadline**: Foundation live trước đầu tháng 5/2026.

## 3. Tech Stack & Master Assets
Hệ thống sử dụng Claude API tích hợp MoSpark, vận hành dựa trên bộ "vũ khí" tiêu chuẩn của Hiến:

### 3.1. Kỹ năng Quản trị (Governance Skills)
*   **[[momo-seo-geo-guideline]]**: Tiêu chuẩn về mật độ từ khóa, cấu trúc AI Search và GEO Citation.
*   **[[momo-ymyl-guideline]]**: Quy tắc an toàn nội dung tài chính/pháp lý và tiêu chuẩn E-E-A-T.

### 3.2. Bộ Prompt thực thi (Execution Prompts)
*   **[[momo-blog-prompt-1-outline]]**: Điều khiển AI phân tích Intent và lên cấu trúc Outline chuẩn SEO/GEO.
*   **[[momo-blog-prompt-2-writer]]**: Điều khiển AI chấp bút nội dung chi tiết dựa trên Outline đã duyệt.

### 3.3. Quality Gate
Nội dung sau khi được AI sản xuất sẽ được kiểm tra tự động qua [[mospark-seo-geo-score-brd]] để đảm bảo không có sai sót trước khi xuất bản.

## 4. Vai trò & Trách nhiệm
*   **Trọng (Tech Lead)**: 
    *   Quản lý nội dung theo Primary Keyword.
    *   Tích hợp Claude API và đảm bảo hệ thống không phát sinh lỗi.
    *   Chuẩn hóa PRD cho module này.
*   **Nhật (Integration)**: 
    *   Hỗ trợ Trọng trong Pipeline xuất bản.
    *   Kết nối đầu ra của GenAI với module SEO/GEO Score.
*   **Hiến (Governance)**:
    *   Thiết kế quy trình triển khai (Workflow).
    *   Xây dựng và tối ưu bộ Skill/Prompt Standard cho AI.

## 5. Lộ trình (Roadmap)
1.  **Tuần 1 T5/2026**: Hoàn thiện Foundation cho dự án Phạt Nguội.
2.  **Tuần 2 T5/2026**: Test run và hiệu chỉnh Prompt dựa trên kết quả SEO/GEO Score thực tế.
3.  **Tuần 3 T5/2026**: Scale hàng loạt các Use Case khác trên MoSpark.

---
*Document: BRD-MoSpark-GenAI-Content · v1.0*
