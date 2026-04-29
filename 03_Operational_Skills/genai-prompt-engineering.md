# Skill: GenAI Prompt Engineering (SEO/GEO Content)

> **Role:** Văn Hiến (SEO & GEO Lead)
> **Engine:** Claude API (Integrated in MoSpark)
> **Goal:** Tạo nội dung chuẩn SEO/GEO, đạt E-E-A-T và sẵn sàng cho AI Search Citation.

---

## 1. Nguyên tắc cốt lõi (Core Principles)
*   **Zero-Hallucination**: Luôn yêu cầu AI sử dụng dữ liệu thực tế (Pháp luật, số liệu từ BU).
*   **Context Injection**: Truyền bối cảnh dự án (Primary Keyword, Target Audience) vào Prompt.
*   **Structure-First**: Luôn yêu cầu AI tạo Outline trước khi viết nội dung chi tiết.

## 2. Framework Prompt cho Blog Content

### Phase A: Outline Generator
**Input**: Primary Keyword + Target Audience + Key Message.
**Prompt Master**: [[momo-blog-prompt-1-outline]]

### Phase B: Content Writer
**Input**: Outline từ Phase A + [[momo-seo-geo-guideline]] + [[momo-ymyl-guideline]].
**Prompt Master**: [[momo-blog-prompt-2-writer]]

## 3. Quality Gate (SEO/GEO Score)
Nội dung sau khi GenAI tạo ra phải được tự động chấm điểm qua [[mospark-seo-geo-score-brd]]. Các tiêu chí bắt buộc:
*   Mật độ từ khóa chính.
*   Sự hiện diện của FAQ Schema.
*   Độ dài và cấu trúc Heading.

---
## 🧭 Điều phối
*   **Project**: [[genai-content-brd]]
*   **Project**: [[phat-nguoi-brd]] (Pilot Use Case)
*   **Framework**: [[Seo-Geo-audit]]
