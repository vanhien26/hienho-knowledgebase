# BRD: MoSpark Migration - System Consolidation

> **Project Manager:** Anh Bảo (Web Platform Manager)
> **Governance & SEO Strategy:** Văn Hiến (SEO & GEO Lead)
> **System Architect / Migration Mapper:**  [Cần xác định] Người chịu trách nhiệm định nghĩa cấu trúc dữ liệu, sơ đồ chuyển dịch và liên kết hệ thống.
> **Lead Engineers:** Võ Minh Thuận, Lê Đăng Lộc
> **Status:** Active - Structure & Mapping Phase

---

## 1. Hệ thống hiện tại: Admin Panel Tool (CMS)
Đây là hệ thống CMS trung tâm phục vụ quản lý và vận hành toàn bộ nội dung và tính năng Mini Web, Landing Page, Blog, News, FAQ, Guide trên Web MoMo hiện nay. 
*   **Vai trò**: Nền tảng cốt lõi để các Division/Center quản trị nội dung độc lập.
*   **Các Module đang vận hành**:
    *   **CMS**: Quản lý và xuất bản Mini Web & Landing Page.
    *   **Ads Manager**: Quản lý và phân phối Ads Campaign.
    *   **FlexData Management**: Quản lý dữ liệu động cho các Mini Web.
    *   **Multilingual**: Hỗ trợ đa ngôn ngữ.

## 2. Nền tảng chiến lược: MoSpark (AI-powered Platform)
MoSpark không phải là một hệ thống build mới hoàn toàn mà là **bản nâng cấp thế hệ mới** của Admin Panel Tool với tech stack tương thích AI-powered tốt hơn.
*   **Triết lý**: Giữ lại những gì đang hoạt động tốt (Continuity), đồng thời mở ra khả năng mới về AI.
*   **Thành tựu bước đầu**: Module **Landing Page Builder** đã chứng minh tính đúng đắn, giúp PM/PO có thể tự thao tác trực quan mà không phụ thuộc Dev/Inbound.
*   **Vision**: Trở thành nền tảng AI-powered Web App/Content của MoMo giúp vận hành và tăng trưởng mọi sản phẩm Web - từ Landing Page đến Mini Web, từ Content đến Web Application.

## 3. Nguyên nhân (Causes)
*   **Legacy Architecture**: Hệ thống cũ được xây dựng theo nhu cầu bộc phát của từng thời kỳ, dẫn đến việc "vá" thêm Admin Tool để phục vụ các sản phẩm phức tạp.
*   **Silo Mindset**: Việc chia Cell Team ban đầu nhằm mục đích phân quyền, nhưng lại vô tình tạo ra các "ốc đảo" dữ liệu và vận hành tách biệt.

## 4. Hậu quả (Consequences)

### 3.1. Phân rã Vận hành (Operational Fragmentation)
*   **Nỗi đau của Inbound**: Đội ngũ Inbound (quản lý toàn bộ nội dung) phải thoát ra và đăng nhập vào từng Cell Team để đăng bài. Ví dụ: Để đăng 1 bài blog về Vay, họ không thể đăng từ giao diện chính mà phải vào Cell Team Vay.
*   **Inconsistency**: Giao diện, Menu Header/Footer và các thành phần UI có thể bị lệch nhau giữa các Cell Team do không có sự quản lý tập trung.

### 3.2. Phân rã SEO & URL (URL Fragmentation)
*   **Cấu trúc chồng chéo**: 
    *   Silo 1: `momo.vn/blog/*` (Hub content)
    *   Silo 2: `momo.vn/{use-case}/blog/*` (Vay, Cinema, Bảo hiểm...)
*   **Rủi ro SEO**: Keyword Cannibalization (các trang tự cạnh tranh lẫn nhau), phân tán sức mạnh domain (Link Equity) và gây khó khăn cho việc tối ưu Authority cho toàn site.
*   **Tracking**: Việc đo lường (GA4/Umami) bị phức tạp hóa do cấu trúc URL không thống nhất.

## 5. Phương hướng xử lý (Proposed Solutions)

### 5.1. Hợp nhất Nền tảng (Consolidation)
*   Chuyển toàn bộ dữ liệu từ CMS cũ và Admin Tool sang **MoSpark**.
*   **Single Interface**: Inbound Team chỉ cần một lối vào duy nhất để quản trị mọi nội dung.

### 5.2. Quản trị theo Project-based (Thay vì Cell Team)
*   Thay thế việc phân quyền theo "Cửa sổ Cell Team" bằng việc quản trị theo "Project".
*   Inbound Team có thể lọc nội dung theo Project ngay trên giao diện chính.

**Project System - Core Feature:**

MoSpark sử dụng **Project** như một cơ chế phân loại và phân phối nội dung đa năng. Mọi content (Blog, News, Landing Pages, Mini Web, Ads) đều được gán vào một Project để tự động hóa việc distribution và targeting.

**Lợi ích của Project System:**
1. **Content Distribution:** Tự động hiển thị Blog/News đúng Use Case trên Landing Page
2. **Ads Targeting:** Ads xuất hiện đúng segmentation dựa trên Project
3. **Unified Management:** Quản lý tất cả content của một Use Case từ 1 interface
4. **Cross-Content Linking:** Tự động gợi ý internal links cùng Project
5. **Analytics Segmentation:** Đo lường performance theo từng Project/Use Case

### 5.3. Blog Module - 2 Tiers Architecture

**Giải pháp tối ưu: Giữ nguyên URL structure, unify management interface.**

#### Tier 1: Basic Blog (Default)
*   **Path:** `momo.vn/blog/*`
*   **Scope:** General content, News, Guides, FAQ (đa số blog content)
*   **Management:** Unified CRUD interface trên MoSpark
*   **Project:** `General` (mặc định)

#### Tier 2: Advanced Blog (Special Cases)
*   **Path:** `momo.vn/{use-case}/blog/*`
*   **Scope:** 4 Use Cases đặc biệt (Vay Nhanh, Cinema, BH Ô tô, BH Xe máy)
*   **Management:** Same CRUD interface + custom path configuration
*   **Projects:** `VayNhanh`, `Cinema`, `BaoHiemOTo`, `BaoHiemXeMay`

**Lý do không consolidate về `/blog/`:**
*   **Zero traffic loss:** Không redirect → Không lost traffic, không lost ranking
*   **SEO preservation:** Giữ nguyên URL authority đã build
*   **No cannibalization:** Mỗi Use Case có URL space riêng
*   **Future-proof:** Dễ thêm special case mới

**User Flow:**
1. Editor tạo Blog Post → Chọn Project
2. System auto-determine URL dựa trên config
3. Publish → Content được tạo đúng URL pattern

### 5.4. Migration Strategy - Zero Redirect Approach

| Use Case | Current URL | MoSpark URL | Migration Action |
|----------|-------------|-------------|------------------|
| General | `/blog/*` | `/blog/*` | Direct migration (no URL change) |
| Vay Nhanh | `/vay-nhanh/blog/*` | `/vay-nhanh/blog/*` | Direct migration (no URL change) |
| Cinema | `/cinema/blog/*` | `/cinema/blog/*` | Direct migration (no URL change) |
| BH Ô tô | `/bao-hiem-o-to/blog/*` | `/bao-hiem-o-to/blog/*` | Direct migration (no URL change) |
| BH Xe máy | `/bao-hiem-xe-may/blog/*` | `/bao-hiem-xe-may/blog/*` | Direct migration (no URL change) |

**→ ZERO redirects needed!** Tất cả URLs được giữ nguyên.

---

## 6. Migration Mapping Framework (The "Structure" Layer)
Đây là tầng logic định nghĩa cách hệ thống được "xây lại" trên MoSpark. Người đảm nhiệm vai trò này phải trả lời 3 câu hỏi cốt lõi:

### 6.1. Move cái gì? (Inventory Audit)
*   **Content Assets**: Blog, News, Guide, FAQ, Landing Pages.
*   **Navigation Assets**: Menu Header/Footer theo từng Cell Team.
*   **Technical Assets**: Metadata, Schema, Redirect rules, Tracking codes.

### 6.2. Đặt ở đâu? (Mapping Schema)
**Blog Content - 2 Tiers:**
*   **Tier 1 - Basic Blog:** `momo.vn/blog/*` (General content, News, Guides, FAQ)
*   **Tier 2 - Advanced Blog:** `momo.vn/{use-case}/blog/*` (4 special cases: Vay Nhanh, Cinema, BH Ô tô, BH Xe máy)

**Product Content:**
*   Giữ nguyên cấu trúc `/vay-nhanh`, `/bao-hiem-xe-may`, `/cinema`, v.v.

**Documentation:**
*   Các trang hướng dẫn tập trung về `/guide/`

### 6.3. Liên kết đến cái gì? (Connectivity & Internal Link)
*   **Global Navigation:** Hợp nhất toàn bộ Menu Cell Team thành một **Master Menu** có khả năng thay đổi context theo Project.
*   **Contextual Linking:** Tự động gợi ý nội dung liên quan dựa trên Project (Ví dụ: Trang Vay Nhanh tự động link tới các Blog thuộc Project VayNhanh).
*   **Zero Redirect Strategy:** Không redirect vì URLs được giữ nguyên.

---

## 7. Migration Phases

### Phase 1: Foundation & Basic Blog (4-6 tuần)
**Mục tiêu:** Thiết lập infrastructure và migrate Basic Blog

| Task | Owner | Output |
|------|-------|--------|
| Setup MoSpark Blog Module (default path `/blog`) | Bảo/Web Platform | Blog CRUD interface |
| Implement Project Tag system | Bảo/Web Platform | Tag-based filtering |
| Migrate `/blog/*` content | Hiến + Inbound | All general blog posts |
| Validate: Traffic, ranking, indexation | Hiến | SEO audit report |

**Success Criteria:**
- 100% `/blog/*` content migrated
- Zero traffic drop
- All URLs indexed within 14 days

### Phase 2: Advanced Blog - Special Cases (6-8 tuần)
**Mục tiêu:** Migrate 4 Use Cases đặc biệt với custom paths

| Task | Owner | Output |
|------|-------|--------|
| Implement Blog Path Configuration | Bảo/Web Platform | Admin-configurable routing |
| Add 4 special cases to config | Hiến | Config schema |
| Migrate `/vay-nhanh/blog/*` | Hiến + Inbound | Vay Nhanh blog posts |
| Migrate `/cinema/blog/*` | Hiến + Inbound | Cinema blog posts |
| Migrate `/bao-hiem-o-to/blog/*` | Hiến + Inbound | BH Ô tô blog posts |
| Migrate `/bao-hiem-xe-may/blog/*` | Hiến + Inbound | BH Xe máy blog posts |
| Validate: Traffic retention per Use Case | Hiến | SEO audit report |

**Success Criteria:**
- 100% special case content migrated
- Zero traffic drop per Use Case
- All URLs retain ranking

### Phase 3: Optimization & Decommission (4 tuần)
**Mục tiêu:** Optimize cross-blog experience và deprecate hệ thống cũ

| Task | Owner | Output |
|------|-------|--------|
| Cross-blog internal linking | Bảo/Web Platform | Auto-suggest links |
| Unified search across all blog paths | Bảo/Web Platform | Global search |
| Analytics consolidation | DA (Hải/Hoàng) | Unified dashboard |
| Deprecate Admin Tool V1 | Bảo | Shutdown old system |

**Success Criteria:**
- Single interface for all blog management
- 50% reduction in content production time
- Old system fully decommissioned

---

## 8. Success Metrics (Migration Phase)

| Metric | Baseline | Target | Timeline |
|--------|----------|--------|----------|
| **Traffic Retention** | 100% | >98% | 30 days post-migration per phase |
| **Indexation Rate** | 0% | 100% | 14 days post-migration |
| **Ranking Stability** | Current positions | No drop >2 positions | Per Use Case |
| **Operational Speed** | X hours/week | 0.5X hours/week | 60 days post-migration |
| **SEO/GEO Score Compliance** | 0% | >80% | Ongoing |
| **Zero Redirect Success** | N/A | 100% URLs preserved | All phases |

---
*Document: BRD-MoSpark-Migration-2026 · v1.1*
