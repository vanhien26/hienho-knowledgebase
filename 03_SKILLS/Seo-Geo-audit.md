---
title: "Kỹ năng Audit SEO/GEO MoMo"
description: >
  Skill chẩn đoán và kiểm soát chất lượng (QC) toàn diện cho hệ thống website MoMo.vn. 
  Đánh giá 4 trục: Technical, On-page, GEO Readiness và Authority bám sát North Star (MUA & W2A).
version: v2.1
status: Active
owner: Văn Hiến (SEO & GEO Lead)
last_updated: 2026-05-16
tags: [skill, seo, geo, audit, technical-seo, aeo, momo, web2app]
---

# 🧪 Kỹ năng Audit SEO/GEO MoMo

> **Trigger:** "audit page X", "check SEO/GEO của Use Case Y", "đánh giá tình trạng SEO", "GEO readiness check", hoặc khi cần baseline trước khi build content/strategy mới.

## 1. Phạm vi & Mục tiêu (Scope)

Skill này thực hiện chẩn đoán hiện trạng của 1 URL/Domain/Use Case trên 4 trục cốt lõi. **Mục tiêu duy nhất:** Tìm ra rào cản ngăn chặn việc đạt được North Star (6M MUA) và Tỷ lệ chuyển đổi Web-to-App (12.5%).

> [!IMPORTANT]
> **Nguyên tắc "Không Hallucination":** Không bịa số liệu. Nếu không có dữ liệu thực tế từ Ahrefs/GSC/PageSpeed, phải đánh dấu là `[Cần verify]`.

---

## 2. Bốn Trục Audit Chiến lược (4-Axis Framework)

### Trục 1: Technical SEO Foundation (Cơ sở Kỹ thuật)
Đảm bảo Crawler và AI Bots (GPTBot, ClaudeBot) có thể truy cập và hiểu trang.

| Chỉ số | Tiêu chuẩn Đạt (MoMo Baseline) |
| :--- | :--- |
| **HTTP Status** | 200 (Tuyệt đối không 3xx chain, 4xx, 5xx). |
| **Indexability** | Đã Index, không noindex, không bị block bởi robots.txt. |
| **Core Web Vitals** | LCP < 2.5s, INP < 200ms, CLS < 0.1 (Ưu tiên PageSpeed Mobile). |
| **Robots.txt** | Không block AI Bots. Đã cập nhật chính sách AI Crawler mới nhất. |
| **MoSpark Status** | Đã migrate sang MoSpark V2 (React/Next.js) chưa? |

### Trục 2: On-page SEO & Intent (Nội dung & Ý định)
Đảm bảo trang khớp hoàn hảo với Search Intent và JTBD của người dùng.

| Chỉ số | Tiêu chuẩn Đạt (MoMo Baseline) |
| :--- | :--- |
| **Title & H1** | Chứa Primary Keyword, có brand MoMo, khớp Search Intent. |
| **Search Intent** | Khớp định dạng: Transactional (Lookup tool), Informational (Blog), Navigation. |
| **Internal Link** | Tối thiểu 3 link trỏ vào (từ Hub/Pillar) và link ra các trang liên quan. |
| **W2A Layer** | Đã có Onelink (onelink.momo.vn) hoặc Ads Manager Balloon chưa? |

### Trục 3: GEO/AEO Readiness (Sẵn sàng cho AI Search)
Đảm bảo trang được các AI Engines trích dẫn và trả lời.

| Chỉ số | Tiêu chuẩn Đạt (MoMo Baseline) |
| :--- | :--- |
| **Answer-First** | Câu trả lời trực tiếp nằm trong 100 chữ đầu tiên. |
| **Structured Data** | FAQPage, Article, FinancialService, hoặc HowTo schema hợp lệ. |
| **E-E-A-T** | Có Author Byline, chuyên gia Review, ngày cập nhật và nguồn tham chiếu. |
| **Fact Clarity** | Thông tin dạng con số/sự thật rõ ràng, dễ để AI parse dữ liệu. |

### Trục 4: Authority & Trust (Uy tín & Thương hiệu)
Đảm bảo trang có đủ "sức nặng" để cạnh tranh thứ hạng.

| Chỉ số | Tiêu chuẩn Đạt (MoMo Baseline) |
| :--- | :--- |
| **Domain Rating** | DR tương đương hoặc cao hơn đối thủ trong cùng Use Case. |
| **Toxic Backlink** | Không có dấu hiệu Spike bất thường hoặc Anchor text spam. |
| **Citation Signal** | Có được các báo chí Tier-1 (VnExpress, Cafef) hoặc AI trích dẫn không? |

---

## 3. Quy trình Thực thi (Workflow)

### Bước 1: Thu thập Dữ liệu
Sử dụng công cụ tương ứng cho từng trục:
- **Ahrefs:** DR, Backlinks, Organic Keywords, Competitor Gap.
- **Web Fetch:** Đọc nội dung, Schema, Cấu trúc Heading.
- **PageSpeed:** Đo Core Web Vitals thực tế.

### Bước 2: Phân tích Nguyên nhân (Root Cause)
Với mỗi lỗi **Critical (Đỏ)** hoặc **Warning (Vàng)**, không chỉ nêu hiện tượng mà phải chỉ ra nguyên nhân gốc rễ (ví dụ: do CMS cũ, do quy trình viết content thiếu bước audit, v.v.).

### Bước 3: Ưu tiên Hành động (Prioritization)
Sắp xếp Action List theo ma trận:
- **P0 (High Impact, Low Effort):** Sửa ngay (Ví dụ: Meta Title, chèn CTA Onelink).
- **P1 (High Impact, High Effort):** Cần lập kế hoạch (Ví dụ: Migrate sang MoSpark, viết lại Content Pillar).
- **P2 (Maintenance):** Theo dõi định kỳ.

---

## 4. Định dạng Báo cáo (Output Template)

Mọi báo cáo Audit phải tuân thủ **Nguyên tắc Kim tự tháp**: Kết luận quan trọng nhất lên đầu.

```markdown
# 🧪 SEO/GEO Audit Report: [Tên Use Case/URL]

## 1. Kết luận Tổng thể (TL;DR)
- **Trạng thái:** [Healthy / At-Risk / Critical]
- **Vấn đề lớn nhất:** [Ví dụ: Thiếu E-E-A-T nghiêm trọng gây sụt rank]
- **Action P0:** [Ví dụ: Bổ sung Author Bio và Update date]

## 2. Chi tiết 4 Trục Audit
| Trục | Đánh giá | Finding chính | Action đề xuất |
| :--- | :--- | :--- | :--- |
| **Technical** | 🟢 Pass | Tốc độ load tốt trên MoSpark V2 | Duy trì |
| **On-page** | 🟡 Warning | Keyword mật độ thấp, thiếu CTA | Bổ sung CTA Balloon |
| **GEO** | 🔴 Critical | Chưa có Schema FAQ & Author | Triển khai Schema ngay |
| **Authority** | 🟢 Pass | Backlink profile sạch | Tiếp tục Outreach |

## 3. Danh sách Hành động Ưu tiên (Action List)
| Priority | Action | Owner | North Star Tie |
| :--- | :--- | :--- | :--- |
| **P0** | Cập nhật Title & Onelink | Content | Web-to-App |
| **P1** | Triển khai FAQ Schema | Web Platform | Organic Traffic |
```

---

## 5. Nhật ký Thay đổi (Version Log)

| Phiên bản | Ngày | Nội dung thay đổi | Người thực hiện |
| :--- | :--- | :--- | :--- |
| **v1.0** | 2026-05-15 | Khởi tạo Skill Audit 4 trục. | Văn Hiến |
| **v2.0** | 2026-05-16 | Revised clean, MoMo-focused & standardized. | Văn Hiến |
| **v2.1** | 2026-05-16 | Tái cấu trúc: Chuyển tài liệu liên kết xuống cuối & thêm Version Log. | Văn Hiến |

---

## 6. Tài liệu Liên kết
- **Registry:** [[00_HARNESS_CORE/SKILL_REGISTRY|Skill Registry]]
- **Vận hành:** [[00_HARNESS_CORE/orchestrator_engine|Project Orchestrator]]
- **Chiến lược:** [[01_STRATEGIC_PLAN/momo-content-plan-strategy|MoMo Content Strategy]]
- **Nền tảng:** [[04_MOSPARK_PLATFORM/mospark_master|MoSpark Master Doc]]

---
*Maintained by: Văn Hiến (SEO & GEO Lead) | Last updated: 2026-05-16*