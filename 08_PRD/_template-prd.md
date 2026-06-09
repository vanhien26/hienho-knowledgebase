# PRD: [Use Case Name] - Web Channel

> - **Use Case:** [slug]
> - **Main URL:** momo.vn/[slug]
> - **BRD Ref:** 05_USE_CASE_MOMO/[slug]-brd.md
> - **Owner:** Web Product Lead (Hiến)
> - **Engineering Lead:** [TBD]
> - **Design Lead:** [TBD]
> - **Version:** 0.1 - [YYYY-MM-DD]
> - **Status:** [DRAFT]

---

## 1. Overview

### 1.1 Problem Statement

> Copy từ BRD Section 1 - Executive Summary (Situation + Complication). Giữ ngắn gọn, focus vào product problem, không phải business case.

### 1.2 Objective

> Sản phẩm này cần làm được gì? Viết dưới dạng outcome, không phải feature list.

**Primary objective:** [1 câu]

**Success metrics:**

| Metric | Baseline | Target | Timeframe |
|---|---|---|---|
| [KPI 1] | [current] | [target] | [Q/month] |
| [KPI 2] | [current] | [target] | [Q/month] |

### 1.3 Scope

**In scope:**
- [feature / component 1]
- [feature / component 2]

**Out of scope:**
- [explicitly excluded]

---

## 2. User & Context

### 2.1 Target Users

> Lấy từ BRD - JTBD section. Map thành persona rõ ràng hơn.

| Segment | Mô tả | Job-to-be-done | Entry Point |
|---|---|---|---|
| [Segment A] | | | |
| [Segment B] | | | |

### 2.2 User Journey (Web Channel)

```
[Search / Discovery] -> [Landing Page] -> [Core Action] -> [W2A Trigger] -> [App Install / Open]
```

**Critical drop-off points:**
- [ ] [Step] - [Risk]

---

## 3. Feature Requirements

> Mỗi feature: User Story + Acceptance Criteria + Priority

### 3.1 [Feature Name]

**User Story:**
> As a [user type], I want to [action] so that [outcome].

**Acceptance Criteria:**
- [ ] AC1: ...
- [ ] AC2: ...
- [ ] AC3: ...

**Priority:** P0 / P1 / P2

**Notes:** [edge cases, constraints]

---

### 3.2 [Feature Name]

**User Story:**
> As a [user type], I want to [action] so that [outcome].

**Acceptance Criteria:**
- [ ] AC1: ...
- [ ] AC2: ...

**Priority:** P0 / P1 / P2

---

## 4. W2A Conversion Requirements

> Section bắt buộc - đây là output cuối cùng của Web channel.

### 4.1 W2A Trigger Points

| Trigger | Placement | CTA Text | Deep Link |
|---|---|---|---|
| [Post-action result] | [location on page] | [button text] | [momo://...] |
| [Scroll depth / time] | | | |

### 4.2 Non-MoMo User Flow

- [ ] App not installed: redirect to [App Store / CH Play / Universal Link]
- [ ] App installed: deep link to [in-app screen]
- [ ] UTM parameters: `utm_source=web&utm_medium=[medium]&utm_campaign=[use-case]`

---

## 5. SEO / GEO Technical Requirements

> Lấy từ BRD Technical Foundation section. Chỉ list requirements, không giải thích.

### 5.1 On-Page

- [ ] Title tag: `[format]`
- [ ] Meta description: `[format]`
- [ ] H1: `[format]`
- [ ] Canonical: `[URL]`

### 5.2 Structured Data

- [ ] Schema type: [FAQ / HowTo / WebApplication / ...]
- [ ] Required fields: [list]

### 5.3 Core Web Vitals Targets

| Metric | Target |
|---|---|
| LCP | < 2.5s |
| CLS | < 0.1 |
| INP | < 200ms |

---

## 6. API & Data Requirements

| API | Provider | Purpose | Auth | Rate Limit |
|---|---|---|---|---|
| [API name] | [provider] | [use] | [type] | [limit] |

**Data freshness requirement:** [real-time / 5min / daily]

**Fallback behavior when API down:** [describe]

---

## 7. Non-Functional Requirements

| Category | Requirement |
|---|---|
| Performance | Page load < [X]s on 3G |
| Availability | [uptime SLA] |
| Mobile | Responsive, primary breakpoint [px] |
| Browser support | Chrome, Safari, Samsung Internet (latest 2 versions) |
| Accessibility | WCAG 2.1 AA [relevant sections] |

---

## 8. Open Questions

> Track câu hỏi chưa có đáp án. Xóa khi đã resolve.

| # | Question | Owner | Due | Status |
|---|---|---|---|---|
| 1 | [question] | [name] | [date] | OPEN |

---

## 9. Dependencies

| Dependency | Team | Type | Status |
|---|---|---|---|
| [API / system / team] | [team] | Blocking / Non-blocking | [status] |

---

## 10. Release Plan

| Phase | Scope | Target Date | Exit Criteria |
|---|---|---|---|
| Phase 1 | [MVP] | [date] | [metric threshold] |
| Phase 2 | [scale] | [date] | [metric threshold] |

---

## Changelog

| Version | Date | Author | Note |
|---|---|---|---|
| 0.1 | [date] | Hiến | Initial draft |
