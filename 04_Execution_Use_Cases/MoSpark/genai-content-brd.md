# BRD: GenAI Content - SEO/GEO Project Module

> **Product Manager:** Anh Bảo (Web Platform Manager)
> **Tech Lead:** Trần Công Hoàng Trọng (Software Engineer II)
> **Integration Support:** Bùi Minh Nhật (Senior Software Engineer)
> **Governance & Prompts:** Văn Hiến (SEO & GEO Lead)
> **Start Date:** May 2026
> **Status:** Claude API on Production - Enhanced Prompts Live - MoSpark Blog Auto-Create Integrated

---

## 6. Workflow Content - 7 Bước + Role & Responsibility

### 6.0. Workflow Diagram - Horizontal Flow with 7 Steps

Xem diagram ở trên - 7 bước với 3 approval gates:
- **Gate 1:** Business Context Complete (Step 2)
- **Gate 2:** Outline Final (Step 5)
- **Gate 3:** Publish (Step 7)

### 6.1. Workflow Chi tiết

| Bước | Tên | Hành động | Input/Output | Owner | Role |
|------|-----|----------|-------------|----|------|
| 1 | Tạo Project | Nhập tên Use Case (ví dụ: "Vay Nhanh", "Ví Trả Sau") | Project ID + metadata | PM/Growth (Cell Team) | Khởi tạo & xác nhận |
| 2 | Business Context | Nhập Business Model, Target Audience, Value Prop, Promotion Scheme (11 fields bắt buộc). **PM/Growth chịu trách nhiệm về tính pháp lý & Information Gain liên quan sản phẩm/dịch vụ** | Context Layer - inject vào Prompt 1 & 2 | PM/Growth + SEO/GEO Lead | PM/Growth: Xác nhận nội dung. SEO/GEO: Validate framework |
| 3 | Create Primary Keyword | Nhập Primary keyword + Secondary keywords (5-10 từ) | Keyword mapping, intent analysis | Content Team | Triển khai keyword research |
| 4 | Draft Outline AI | Claude AI generate outline dựa trên Context + Keywords | Outline draft (3-5 sections) | AI (Claude API) | Auto-generate |
| 5 | Manual Edit Outline | **Content Team chỉnh sửa outline, điều chỉnh structure, add angle độc đáo. Outline final approval từ PM/Growth** | Outline final approved | Content Team + PM/Growth | Content: Edit & submit. PM/Growth: Approve |
| 6 | Blog Detail AI | Claude AI generate full Blog Detail từ Outline approved. Check SEO/GEO Scoring tự động | Blog Detail draft (ready for publish) | AI (Claude API) | Auto-generate & auto-check |
| 7 | Blog Editor (Publish) | **SEO/GEO verify Blog Detail, sync qua Blog Editor. Content Team click "Sync create" → Auto publish to momo.vn** | Blog live on momo.vn | Content Team + SEO/GEO Lead | Content: Click publish. SEO/GEO: Verify & sign-off |

**Key Enhancement:** Tách Blog Detail AI (Step 6) và Blog Editor Publish (Step 7) - rõ ràng hóa ownership verify (SEO/GEO) vs publish action (Content).

### 6.2. Role & Responsibility Detail

#### PM/Growth (Cell Team)
**Trách nhiệm chính:** Xác nhận nội dung, chịu trách nhiệm pháp lý, bổ sung thông tin sản phẩm/dịch vụ

- **Bước 1:** Khởi tạo Project (tên Use Case)
- **Bước 2:** **Xác nhận Business Context đầy đủ - chịu trách nhiệm pháp lý & Information Gain**
  - Confirm tất cả 11 fields: Value Prop, Trust Signals, Disclaimer, Blacklist terms
  - Verify không có information sai, không recommend competitor, không overpromise tính năng
  - Ensure tất cả "thông tin lợi ích" (benefit/gain) đều chính xác về sản phẩm/dịch vụ MoMo
- **Bước 5:** Approve Outline final trước khi Claude tạo Blog Detail
  - Review outline có align với strategy & positioning của Use Case
  - Từ chối outline nếu có sai lệch, request Content chỉnh sửa
  - Max 1 lần return - không quá 2 vòng lặp

#### Content Team
**Trách nhiệm chính:** Triển khai quy trình, tạo outline, chỉnh sửa, publish blog

- **Bước 3:** Create Primary Keyword + Secondary keywords (triển khai từ keyword research)
- **Bước 5:** Chỉnh sửa Outline
  - Adjust structure, add unique angle, verify keyword integration
  - Submit Outline final cho PM/Growth approve
- **Bước 7:** Publish Blog Detail
  - Kiểm tra Blog Detail từ AI (nhanh)
  - Nếu SEO/GEO pass gate → Click "Sync create" để publish to momo.vn
  - Nếu fail → Request SEO/GEO fix & verify lại

#### SEO/GEO Lead (Văn Hiến)
**Trách nhiệm chính:** Đảm bảo Skill/Prompt apply, verify quality, ownership publish gate

- **Bước 2:** Validate Business Context framework
  - Confirm 11 fields đầy đủ, context tương thích với Prompt
  - Alert nếu có risk về SEO/GEO impact
- **Bước 6:** Check SEO/GEO Scoring (auto tự động)
  - Monitor AI output quality
  - Flag nếu có issues: E-E-A-T fail, YMYL risk, content violation
- **Bước 7:** **OWNERSHIP - Verify & Sign-off Publish**
  - Final verify content đạt tiêu chuẩn E-E-A-T, YMYL, SEO/GEO
  - Ensure OnPage chuẩn bị (metadata, structured data, CTA placement)
  - Sync Blog Detail vào Blog Editor nếu cần chỉnh sửa OnPage
  - Sign-off → Content Team proceed to publish
  - Chịu trách nhiệm chất lượng final output

### 6.3. Approval Gates

| Gate | Step | Owner | Condition |
|------|------|-------|-----------
| **Business Context Complete** | 2 | PM/Growth + SEO/GEO | Đủ 11 fields, information verify, pháp lý clear, no red flags |
| **Outline Final** | 5 | PM/Growth | Content submit → PM/Growth approve (max 1 return, không > 2 vòng) |
| **Publish** | 7 | SEO/GEO Lead | Blog Detail pass SEO/GEO scoring + E-E-A-T/YMYL check → SEO/GEO sign-off → Content click "Sync create" → auto publish momo.vn |

---

## 7. Business/Product Context - 11 Fields bắt buộc

> **Owner:** Văn Hiến
> **Thời điểm nhập:** Bắt buộc hoàn thành TRƯỚC khi generate bất kỳ bài viết nào trong Project
> **Mục đích:** Làm nền tảng context cho cả Prompt 1 (Outline) và Prompt 2 (Writer) - đảm bảo AI luôn viết đúng về sản phẩm MoMo, không recommend competitor, không bịa đặt tính năng

### 7.1. 11 Fields bắt buộc

1. **Tên sản phẩm** - Tên chính xác như hiển thị trong App/Web
2. **URL Web** - URL canonical của trang chính
3. **Mô tả sản phẩm** - 3-5 câu, phân biệt Web vs App
4. **Đối tượng sử dụng** - Persona chính (ai, ở đâu, job gì)
5. **Đối tác** - Tên đối tác cung cấp data/dịch vụ (nếu có)
6. **Điều kiện sử dụng** - Giới hạn, yêu cầu user cần biết
7. **Value Prop / USPs** - Danh sách điểm giá trị nổi bật (AI phải integrate tự nhiên)
8. **Trust Signals** - Yếu tố tạo độ tin cậy so với competitor
9. **Khác biệt vs đối thủ** - So sánh trực tiếp, honest (bao gồm cả điểm chưa bằng)
10. **Disclaimer** - Pháp lý/tài chính (theo YMYL guideline)
11. **Từ ngữ bị cấm** - Blacklist terms (sai sản phẩm, pháp lý risk, competitor)

---

## 8. Lộ trình (Roadmap)

### Phase 1: Foundation & Scaling (May 2026)
1. ✅ **7-Step Workflow live:** Blog Detail AI + Blog Editor Publish separation
2. ✅ **Phạt Nguội pilot:** Foundation complete
3. ✅ **Scale Financial products:** Vay Nhanh, Ví Trả Sau, CIC

### Phase 2: Performance Tracking & Optimization (June 2026+)
- **Google Search Console API Integration:** Theo dõi hiệu suất per Project
- **Metrics per Project:** Organic traffic, impressions, CTR, avg position
- **Automated Insights:** Gợi ý tối ưu nội dung dựa trên data
- **Content Refresh Automation:** Identify underperforming articles - suggest updates

---

*Document: BRD-MoSpark-GenAI-Content · v3.5 (Integrated Prompt Engineering Skill)*

---

## 9. GenAI Operational Standards & Prompt Strategy (Integrated Skill)

> **Role:** Văn Hiến (SEO & GEO Lead)
> **Engine:** Claude API (Integrated in MoSpark)
> **Goal:** Tạo nội dung chuẩn SEO/GEO, đạt E-E-A-T và sẵn sàng cho AI Search Citation.

### 9.1. Nguyên tắc cốt lõi (Core Principles)
*   **Zero-Hallucination**: Luôn yêu cầu AI sử dụng dữ liệu thực tế (Pháp luật, số liệu từ BU).
*   **Context Injection**: Truyền bối cảnh dự án (Primary Keyword, Target Audience) vào Prompt.
*   **Structure-First**: Luôn yêu cầu AI tạo Outline trước khi viết nội dung chi tiết.

### 9.2. Framework Prompt cho Blog Content
Quy trình này khớp với **Bước 4 & Bước 6** trong Workflow hệ thống:

*   **Phase A: Outline Generator (Step 4)**
    *   **Input**: Primary Keyword + Target Audience + Key Message.
    *   **Prompt Master**: [[momo-blog-prompt-1-outline]]
*   **Phase B: Content Writer (Step 6)**
    *   **Input**: Outline từ Phase A + [[momo-seo-geo-guideline]] + [[momo-ymyl-guideline]].
    *   **Prompt Master**: [[momo-blog-prompt-2-writer]]

### 9.3. Quality Gate Standards (SEO/GEO Score)
Nội dung sau khi GenAI tạo ra phải được tự động chấm điểm qua [[mospark-seo-geo-score-brd]]. Các tiêu chí bắt buộc:
*   Mật độ từ khóa chính.
*   Sự hiện diện của FAQ Schema.
*   Độ dài và cấu trúc Heading.
