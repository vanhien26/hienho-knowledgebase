# MoSpark Product Roadmap & Portfolio 2026

> **Vision**: Nền tảng AI-powered Web App/Content của MoMo giúp vận hành và tăng trưởng mọi sản phẩm Web.
> **Project Lead**: Anh Bảo (Web Platform Manager)

---

## 1. Operating & Developing Modules

### 1.1. Landing Page Builder (V1.0 Delivered)
*   **Status**: Q1 Delivered, Q2 Onboarding GPD.
*   **Capabilities**: 
    *   Tự tạo và preview Landing Page trực quan (momo.vn/ld/[slug]).
    *   Block Gift/Promotion phục vụ Marketing.
    *   Reactivation Hub Landing Page (Build trong 1 tuần).
*   **Goal**: PM/PO tự vận hành campaign mà không phụ thuộc Dev/Inbound.

### 1.2. Ads Manager (V1.2 Production)
*   **Status**: Pilot với User Growth.
*   **Capabilities**: 
    *   Balloon Ads (Deployed 01/04/2026), Popup, Bottom Sheet.
    *   Promotion Scheme & A/B testing.
*   **Roadmap**: Context-based targeting theo URL và tích hợp Appsflyer/Onelink để đo attribution.

### 1.3. GenAI Content (SEO/GEO Project Module)
*   **Status**: Pilot với dự án Phạt Nguội.
*   **Capabilities**: 
    *   Tích hợp Claude API vào MoSpark.
    *   Content Skills chuẩn hóa (Blog, FAQ, HowTo).
    *   Output đạt chuẩn E-E-A-T và GEO citation.
    *   **Business Context Integration**: Sử dụng context từ Project System để tạo nội dung phù hợp lĩnh vực.
*   **Future**: Google Search Console API integration để đánh giá hiệu suất bài viết theo Project.

### 1.4. Help Center (AI-powered Self-Help)
*   **Status**: Đăng ký Agentic Org Program.
*   **Goal**: Chuyển đổi FAQ tĩnh sang AI Agent tự phục vụ, giảm ticket hỗ trợ.

### 1.5. Chatbot / Knowledge Base (R&D)
*   **Status**: Nghiên cứu làm giàu Knowledge Base tự động từ Web content.
*   **Goal**: Rút ngắn thời gian triển khai Chatbot cho các Cell Team.

---

## 2. Core Infrastructure Roadmap

### 2.1. Authentication & Identity
*   **Current**: Google OAuth/SSO Production.
*   **Next**: Identity Platform, Identity Graph, Personalization & AI Context.

### 2.2. Mobase V2 (AI-Native Foundation)
*   **Status**: MVP live 04/2026.
*   **Roadmap**: llms.txt, MCP Server, Agent Skills phục vụ Vibe Code.

### 2.3. Project System (Core Infrastructure for SEO/GEO Projects)
*   **Status:** Core Logic Deployed - Nâng cấp theo 4 phases.
*   **Vision:** Hệ thống quản lý và phân phối nội dung tập trung - mọi content (Blog, News, Landing Pages, Mini Web, Ads) đều được gán Project để tự động hóa distribution và targeting.
*   **SEO/GEO Integration:** Project System cung cấp Business Context cho GenAI Content module, đảm bảo nội dung được tạo ra phù hợp với lĩnh vực và mục tiêu của từng Use Case (Phạt Nguội, Vay Nhanh, Cinema...).

#### Phase 1: Foundation (4-6 tuần)
*   **Project Management UI:** Interface tạo, edit, assign Projects
*   **Mandatory Project Assignment:** Bắt buộc chọn Project khi tạo content mới
*   **Project-based Filtering:** Lọc content theo Project trong admin dashboard
*   **Batch Project Tool:** Gán Project cho existing content
*   **Success Metric:** 100% content được gán Project

#### Phase 2: Content Distribution (6-8 tuần)
*   **Auto-embed on Landing Pages:** Blog/News tự động hiển thị trên Landing Page cùng Project
*   **Related Content Widget:** "Bài viết liên quan" dựa trên Project matching
*   **Cross-content Linking:** Tự động gợi ý internal links cùng Project
*   **Project-based Navigation:** Menu context thay đổi theo Project
*   **Success Metric:** >95% auto-distribution accuracy, +25% internal link CTR

#### Phase 3: Ads Manager Integration (4-6 tuần)
*   **Project-based Ad Targeting:** Ads chỉ hiển thị trên pages cùng Project
*   **Segmentation Rules:** Rule engine cho ad placement theo Project
*   **Cross-project Campaigns:** Support campaigns across multiple Projects
*   **Performance Tracking:** Analytics per Project cho Ads
*   **Success Metric:** +30% Ads CTR improvement

#### Phase 4: Analytics & Optimization (4 tuần)
*   **Project-based Analytics Dashboard:** Metrics riêng cho từng Project
*   **Cross-project Reporting:** Consolidated view across all Projects
*   **Project Performance Insights:** Phân tích hiệu quả của từng Project
*   **Automated Recommendations:** Gợi ý tối ưu dựa trên data
*   **Success Metric:** 50% reduction in management time

---

## 3. MoSpark Content & Page Architecture

Hệ thống hiện đang quản lý và vận hành 7 loại hình trang chiến lược:

| URL Pattern | Loại trang | Mục tiêu & Đặc điểm |
|-------------|------------|---------------------|
| `/blog*` | **Growth Articles** | Bài viết chuyên sâu phục vụ tăng trưởng cho các Use Case. |
| `/tin-tuc*` | **Communications** | Hạng mục truyền thông theo yêu cầu của PM/PO Cell Team. |
| `/hoi-dap*` | **Help Center** | Hệ thống tự phục vụ và giải đáp thắc mắc khách hàng. |
| `/huong-dan*` | **Interactive Guides** | Sử dụng Image Carousel để hướng dẫn sử dụng tính năng App. |
| `/doi-tac*` | **Merchant Page** | Thư viện thông tin và hệ sinh thái đối tác của MoMo. |
| `/{mini-web}` | **Basic Landing Page** | Giới thiệu sản phẩm (Chưa có Simulation/API PLG). |
| `/{mini-web}*` | **Advanced Mini Web** | Đa sub-page, tập trung thúc đẩy traffic và MAU quy mô lớn. |

---
*Last Updated: 30/04/2026*