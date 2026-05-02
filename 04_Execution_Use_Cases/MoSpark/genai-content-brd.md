# BRD: GenAI Content - SEO/GEO Project Module

> **Product Manager:** Anh Bảo (Web Platform Manager)
> **Tech Lead:** Trần Công Hoàng Trọng (Software Engineer II)
> **Integration Support:** Bùi Minh Nhật (Senior Software Engineer)
> **Governance & Prompts:** Văn Hiến (SEO & GEO Lead)
> **Start Date:** May 2026
> **Status:** Kicking Off - CEO Mandate (Phạt Nguội Pilot)

---

## 1. Tổng quan Kiến trúc (Architecture Overview)

**GenAI Content** là một module trong hệ sinh thái **SEO/GEO Project** của MoSpark, đảm nhận vai trò sản xuất nội dung tự động từ Keyword và Business Context.

### 1.1. Mối quan hệ với SEO/GEO Project

```
┌─────────────────────────────────────────────────────────────┐
│                    SEO/GEO Project                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Business Context                        │   │
│  │  (Mô tả lĩnh vực, mục tiêu, đối tượng của Project)  │   │
│  └──────────────────────┬──────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           GenAI Content Module                       │   │
│  │  ┌─────────────┐    ┌─────────────┐                 │   │
│  │  │  Outline    │───▶│   Writer    │                 │   │
│  │  │  (Claude)   │    │  (Claude)   │                 │   │
│  │  └─────────────┘    └─────────────┘                 │   │
│  └──────────────────────┬──────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Blog Editor                             │   │
│  │         (Xuất bản & Quản lý bài viết)               │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │         Google Search Console API                    │   │
│  │         (Performance Tracking - Future)             │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 1.2. Một SEO/GEO Project = Một Use Case

Mỗi Project tương ứng với một Use Case (Phạt Nguội, Vay Nhanh, Cinema...) gồm:
- **Nhiều bài viết** (nhiều keywords) được tổng hợp từ Business Context
- **Kiến thức lĩnh vực** làm đầu vào cho AI xử lý đúng thông tin
- **Hệ thống phân phối** nội dung qua Project System

---

## 2. Mục tiêu (Goals)

Xây dựng pipeline sản xuất nội dung SEO/GEO chuẩn bằng AI thay thế quy trình viết tay thủ công:
*   **Scale**: Sản xuất hàng loạt bài viết chất lượng cao trong thời gian ngắn.
*   **Standard**: Đảm bảo 100% bài viết đạt tiêu chuẩn E-E-A-T và YMYL.
*   **SEO/GEO Ready**: Cấu trúc nội dung tối ưu cho việc trích dẫn (Citation) trên AI Search (Gemini, AI Overview).
*   **Context-Aware**: Nội dung được tạo ra phải phù hợp với Business Context của Project.

---

## 3. Pilot Use Case: Phạt Nguội (CEO Mandate)

*   **Current State**: Đang triển khai tích hợp Claude API vào MoSpark. Đang xây dựng bộ **Content Skills** (Prompt templates) chuẩn hóa.
*   **Objective**: Đạt mục tiêu **Top of Mind** cho dự án Phạt Nguội.
*   **Deadline**: Foundation live trước đầu tháng 5/2026.

---

## 4. Tech Stack & Master Assets

Hệ thống sử dụng Claude API tích hợp MoSpark, vận hành dựa trên bộ "vũ khí" tiêu chuẩn của Hiến:

### 4.1. Kỹ năng Quản trị (Governance Skills)
*   **[[momo-seo-geo-guideline]]**: Tiêu chuẩn về mật độ từ khóa, cấu trúc AI Search và GEO Citation.
*   **[[momo-ymyl-guideline]]**: Quy tắc an toàn nội dung tài chính/pháp lý và tiêu chuẩn E-E-A-T.

### 4.2. Bộ Prompt thực thi (Execution Prompts)
*   **[[momo-blog-prompt-1-outline]]**: Điều khiển AI phân tích Intent và lên cấu trúc Outline chuẩn SEO/GEO.
*   **[[momo-blog-prompt-2-writer]]**: Điều khiển AI chấp bút nội dung chi tiết dựa trên Outline đã duyệt.

### 4.3. Quality Gate
Nội dung sau khi được AI sản xuất sẽ được kiểm tra tự động qua [[mospark-seo-geo-score-brd]] để đảm bảo không có sai sót trước khi xuất bản.

---

## 5. Vai trò & Trách nhiệm

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

---

## 6. Lộ trình (Roadmap)

### Phase 1: Foundation (Hiện tại)
1.  **Tuần 1 T5/2026**: Hoàn thiện Foundation cho dự án Phạt Nguội.
2.  **Tuần 2 T5/2026**: Test run và hiệu chỉnh Prompt dựa trên kết quả SEO/GEO Score thực tế.
3.  **Tuần 3 T5/2026**: Scale hàng loạt các Use Case khác trên MoSpark.

### Phase 2: Performance Tracking (Future)
*   **Google Search Console API Integration**: Kết nối để theo dõi hiệu suất bài viết theo Project
*   **Metrics per Project**: Organic traffic, impressions, CTR, average position cho từng Project
*   **Automated Insights**: Gợi ý tối ưu nội dung dựa trên performance data

---

*Document: BRD-MoSpark-GenAI-Content · v2.0*