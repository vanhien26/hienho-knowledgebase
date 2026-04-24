---
name: momo-html-doc-format
description: Áp dụng MoMo HTML Document Design System khi tạo hoặc chỉnh sửa bất kỳ HTML strategy/project document nào cho team Out-App Traffic. Trigger khi user yêu cầu tạo mới hoặc cập nhật HTML doc, strategy doc, project doc, use case document dạng HTML, hoặc khi cần đảm bảo consistency với format chuẩn của team. Bắt buộc dùng skill này bất cứ khi nào output là một file HTML nội bộ cho MoMo GPD/Out-App Traffic.
---

# MoMo HTML Document Format Skill

Skill này định nghĩa toàn bộ design system, brand guideline, và convention cố định khi tạo HTML document nội bộ cho team **Out-App Traffic · GPD** tại MoMo.

Đọc `references/tokens.md` để lấy đầy đủ CSS variables và component patterns trước khi viết bất kỳ dòng CSS nào.

---

## Fixed Conventions (Non-negotiable)

### Metadata cố định
```
Team:    Out-App Traffic · GPD
<title>: [Tên Use Case] - [Loại Document] | MoMo
```

### File naming
Pattern: `[use-case]-[doc-type].html`
Ví dụ: `esim-du-lich-seo-geo-project.html`, `vay-nhanh-geo-aeo-master-plan.html`

Không dùng: "Web Growth Strategy", "v2", "final", số version bất kỳ.

### Version
- Không hiển thị version number (bỏ hoàn toàn)
- Thay bằng: `Last updated: [Tháng/Năm]` ở sidebar footer

### Icon policy
- **Không dùng emoji** làm decoration trong body content
- Card title: dùng colored dot hoặc left-border accent thay cho emoji prefix
- Nếu cần visual anchor cho section, dùng `kpi-box` left-border pattern
- Ngoại lệ duy nhất: checklist items dùng ký hiệu text (`✓`, `!`) trong `.cl-box`

---

## Typography

Font duy nhất: **Be Vietnam Pro** (Google Fonts)
```html
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&display=swap" rel="stylesheet">
```

Scale cố định:
- H1 hero: `clamp(22px, 4vw, 30px)`, weight 900
- Section title: `20px`, weight 800
- Card title: `13.5px`, weight 700
- Body: `14px`, `line-height: 1.6`
- Table header / Label: `10px`, weight 700, `letter-spacing: 1px`, uppercase
- Metadata / footnote: `10px`, `--text-faint`

---

## Layout

```
Sidebar: 252px fixed, scroll độc lập
Main: margin-left 252px, padding 28px 28px 64px
Topbar: height 50px, sticky top 0
Card: padding 20px, margin-bottom 16px
Grid gaps: 12-14px
```

Breakpoint duy nhất: `768px` - sidebar collapse, hamburger hiện.

---

## Component Rules

### Badges vs Chips - phân biệt rõ
| Component | border-radius | Dùng khi |
|-----------|--------------|----------|
| `.badge`  | 20px (pill)  | Topbar status, trạng thái doc |
| `.chip`   | 4px (square) | Inline label trong content |

Cả hai chỉ dùng 4 variants: `pink` / `green` / `amber` / `blue`.

### KPI Box
Left-border 3px màu semantic. Hierarchy bắt buộc:
`kpi-label` (10px uppercase) → `kpi-value` (19px, weight 800) → `kpi-note` (11px muted)

### Highlight Box `.hl`
Pattern cố định - không tự ý thay đổi:
- `<strong>`: tiêu đề callout, 10px uppercase, letter-spacing 1.5px
- Body: 12.5px, line-height 1.65
- Variants: `.hl.pink` / `.hl.green` / `.hl.amber` / `.hl.blue`

### Tables
- Header: `--bg-soft`, `--text-faint`, uppercase 10px
- Row hover: `--bg-soft`
- Wrap trong `.table-wrap` để có `overflow-x: auto`

### Navigation active state
```css
color: var(--pink-core);
background: var(--pink-dim);
border-left: 2px solid var(--pink-core);
font-weight: 600;
```

---

## Shadow System

```css
--shadow-sm:   0 1px 3px rgba(249,83,150,0.08), 0 1px 2px rgba(0,0,0,0.04);
--shadow-md:   0 4px 16px rgba(249,83,150,0.10), 0 2px 4px rgba(0,0,0,0.04);
--shadow-card: 0 1px 4px rgba(0,0,0,0.06);
```
Shadow luôn có pink tinge ở layer đầu - không dùng shadow thuần black.

---

## Animation

```css
/* Section transition */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
/* duration: 0.2s ease */

/* Nav/hover: 0.14s */
/* Sidebar slide: 0.28s cubic-bezier(0.4,0,0.2,1) */
```

---

## Sidebar Footer Template

```html
<div class="sidebar-footer">
  Out-App Traffic · GPD<br>
  Last updated: [Tháng/Năm]<br>
  MoMo — momo.vn
</div>
```

---

## Hero Banner Template

```html
<div class="hero-banner">
  <div class="hero-uc-tag">◆ USE CASE · [TÊN USE CASE]</div>
  <h1>[Tiêu đề chính] <span>[Từ khóa highlight]</span></h1>
  <p class="hero-sub">[Mô tả ngắn mục tiêu]</p>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="val">[Số liệu]</div>
      <div class="lbl">[Label]</div>
    </div>
  </div>
</div>
```
H1 span dùng gradient text: `linear-gradient(135deg, var(--pink-core), var(--pink-mid))` với `-webkit-background-clip: text`.

---

## Checklist khi tạo mới doc

- [ ] Font Be Vietnam Pro đã import
- [ ] Tất cả CSS variables khai báo trong `:root`
- [ ] Title format: `[Use Case] - [Doc Type] | MoMo`
- [ ] Sidebar footer: team name + last updated (không có version)
- [ ] Không có emoji trong card content
- [ ] Badge dùng pill (20px), chip dùng square (4px)
- [ ] Shadow có pink tinge
- [ ] Mobile breakpoint 768px có hamburger + overlay

Xem đầy đủ color tokens tại `references/tokens.md`.