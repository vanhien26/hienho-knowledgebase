# MoMo HTML Document Format Skill

**Team:** Out-App Traffic · GPD  
**Status:** Design System Standard  
**Last Updated:** April 2026

---

## Tổng Quan

Skill này định nghĩa toàn bộ design system, brand guideline, và convention cố định khi tạo HTML document nội bộ cho team **Out-App Traffic · GPD** tại MoMo.

**Quy tắc bắt buộc:** Áp dụng skill này bất cứ khi nào output là một file HTML nội bộ cho MoMo GPD/Out-App Traffic, đặc biệt khi tạo mới hoặc cập nhật HTML doc, strategy doc, project doc, use case document dạng HTML.

---

## Fixed Conventions (Non-negotiable)

### Metadata cố định

```
Team:    Out-App Traffic · GPD
<title>: [Tên Use Case] - [Loại Document] | MoMo
```

### File naming

Pattern: `[use-case]-[doc-type].html`

**Ví dụ:**
- `esim-du-lich-seo-geo-project.html`
- `vay-nhanh-geo-aeo-master-plan.html`

**Không dùng:** "Web Growth Strategy", "v2", "final", số version bất kỳ.

### Version Control

- Không hiển thị version number (bỏ hoàn toàn)
- Thay bằng: `Last updated: [Tháng/Năm]` ở sidebar footer

### Icon Policy

- **Không dùng emoji** làm decoration trong body content
- Card title: dùng colored dot hoặc left-border accent thay cho emoji prefix
- Nếu cần visual anchor cho section, dùng `kpi-box` left-border pattern
- **Ngoại lệ duy nhất:** checklist items dùng ký hiệu text (`✓`, `!`) trong `.cl-box`

---

## Typography System

### Font

Font duy nhất: **Be Vietnam Pro** (Google Fonts)

```html
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&display=swap" rel="stylesheet">
```

### Scale cố định

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| H1 hero | `clamp(22px, 4vw, 30px)` | 900 | Responsive scaling |
| Section title | `20px` | 800 | - |
| Card title | `13.5px` | 700 | - |
| Body | `14px` | 400 | `line-height: 1.6` |
| Table header / Label | `10px` | 700 | `letter-spacing: 1px`, uppercase |
| Metadata / footnote | `10px` | 400 | `--text-faint` color |

---

## Layout Structure

```
Sidebar:  252px fixed, scroll độc lập
Main:     margin-left 252px, padding 28px 28px 64px
Topbar:   height 50px, sticky top 0
Card:     padding 20px, margin-bottom 16px
Grid gaps: 12-14px
```

**Breakpoint duy nhất:** `768px` - sidebar collapse, hamburger hiện.

---

## CSS Variables (:root)

### Brand Colors

```css
/* ── Brand Pink ── */
--pink-core:   #F95396;
--pink-mid:    #FF9DBE;
--pink-light:  #FEC8DC;
--white:       #FFFFFF;

/* Derived pink */
--pink-dim:    rgba(249,83,150,0.10);
--pink-glow:   rgba(249,83,150,0.22);
--pink-border: rgba(249,83,150,0.28);
```

### Neutral Backgrounds

```css
/* ── Neutral Backgrounds ── */
--bg:          #FAFAFA;      /* page background */
--bg-white:    #FFFFFF;      /* card / sidebar surface */
--bg-soft:     #FFF5F8;      /* hover state, table header */
--bg-section:  #FFF0F5;      /* section tint */
--border:      #EAEAEA;
--border-soft: #F3E0E9;
```

### Text Hierarchy (4 cấp)

```css
/* ── Text Hierarchy ── */
--text-dark:   #18181B;      /* heading, title */
--text-body:   #3F3F46;      /* body text */
--text-muted:  #71717A;      /* secondary label */
--text-faint:  #A1A1AA;      /* metadata, footnote */
```

### Semantic Accents

```css
/* ── Semantic Accents ── */
--green:  #059669;
--amber:  #D97706;
--blue:   #2563EB;
--red:    #DC2626;

/* Semantic backgrounds (alpha) */
--green-bg:  rgba(5,150,105,0.07);
--amber-bg:  rgba(217,119,6,0.08);
--blue-bg:   rgba(37,99,235,0.07);
--red-bg:    rgba(220,38,38,0.07);
```

### Layout & Spacing

```css
/* ── Layout ── */
--sidebar-w: 252px;
--radius-sm: 6px;
--radius-md: 10px;
--radius-lg: 14px;
```

### Shadow System

```css
/* ── Shadows ── */
--shadow-sm:   0 1px 3px rgba(249,83,150,0.08), 0 1px 2px rgba(0,0,0,0.04);
--shadow-md:   0 4px 16px rgba(249,83,150,0.10), 0 2px 4px rgba(0,0,0,0.04);
--shadow-card: 0 1px 4px rgba(0,0,0,0.06);
```

**Quy tắc:** Shadow luôn có pink tinge ở layer đầu - không dùng shadow thuần black.

---

## Color Usage Rules

| Màu | Dùng cho |
|-----|----------|
| `--pink-core` | CTA primary, active state, accent highlight, gradient text |
| `--pink-mid` | Gradient pair với pink-core, mid-tone accent |
| `--pink-dim` | Background tint cho active/selected state |
| `--pink-border` | Border khi element đang active/focused |
| `--green` | Positive status, target met, "On track", KR đạt |
| `--amber` | Warning, "Under discussion", cần chú ý, Pending |
| `--blue` | Informational, neutral data, Weekly metrics |
| `--red` | Error, critical, blocking issue |
| `--text-dark` | H1-H3, card-title, okr title |
| `--text-body` | Paragraph, table cell content |
| `--text-muted` | Section description, secondary label, nav item |
| `--text-faint` | Nav group label, table header, metadata, footnote |

**Rule:** Không dùng màu ngoài hệ thống này. Không mix semantic colors (ví dụ: dùng blue cho success).

---

## Component Rules & CSS

### Badge vs Chip - Phân biệt rõ

| Component | border-radius | Dùng khi |
|-----------|--------------|----------|
| `.badge` | 20px (pill) | Topbar status, trạng thái doc |
| `.chip` | 4px (square) | Inline label trong content |

Cả hai chỉ dùng 4 variants: `pink` / `green` / `amber` / `blue`.

#### Badge CSS

```css
.badge {
  display: inline-flex; align-items: center;
  padding: 2px 9px; border-radius: 20px;
  font-size: 10px; font-weight: 700;
  letter-spacing: 0.3px; white-space: nowrap;
}
.badge-pink  { background: var(--pink-dim);  color: var(--pink-core); border: 1px solid var(--pink-border); }
.badge-amber { background: var(--amber-bg);  color: var(--amber);     border: 1px solid rgba(217,119,6,0.2); }
.badge-green { background: var(--green-bg);  color: var(--green);     border: 1px solid rgba(5,150,105,0.2); }
.badge-blue  { background: var(--blue-bg);   color: var(--blue);      border: 1px solid rgba(37,99,235,0.2); }
```

#### Chip CSS

```css
.chip {
  display: inline-flex; padding: 2px 9px;
  border-radius: 4px; font-size: 11px; font-weight: 600;
  background: var(--bg-soft); color: var(--text-muted); border: 1px solid var(--border);
}
.chip.pink  { background: var(--pink-dim);  color: var(--pink-core); border-color: var(--pink-border); }
.chip.green { background: var(--green-bg);  color: var(--green);     border-color: rgba(5,150,105,0.2); }
.chip.amber { background: var(--amber-bg);  color: var(--amber);     border-color: rgba(217,119,6,0.2); }
.chip.blue  { background: var(--blue-bg);   color: var(--blue);      border-color: rgba(37,99,235,0.2); }
```

### Highlight Box (.hl)

Pattern cố định - không tự ý thay đổi:
- `<strong>`: tiêu đề callout, 10px uppercase, letter-spacing 1.5px
- Body: 12.5px, line-height 1.65
- Variants: `.hl.pink` / `.hl.green` / `.hl.amber` / `.hl.blue`

```css
.hl { 
  border-radius: var(--radius-sm); 
  padding: 14px 16px; 
  margin-bottom: 12px; 
  font-size: 12.5px; 
  line-height: 1.65; 
}
.hl strong { 
  display: block; 
  font-size: 10px; 
  font-weight: 800; 
  letter-spacing: 1.5px; 
  text-transform: uppercase; 
  margin-bottom: 5px; 
}
.hl.pink  { background: var(--pink-dim); border: 1px solid var(--pink-border); color: #7B1D4A; }
.hl.pink strong { color: var(--pink-core); }
.hl.green { background: var(--green-bg); border: 1px solid rgba(5,150,105,0.18); color: #065F46; }
.hl.green strong { color: var(--green); }
.hl.amber { background: var(--amber-bg); border: 1px solid rgba(217,119,6,0.18); color: #78350F; }
.hl.amber strong { color: var(--amber); }
.hl.blue  { background: var(--blue-bg);  border: 1px solid rgba(37,99,235,0.18); color: #1E3A8A; }
.hl.blue strong { color: var(--blue); }
```

### KPI Box

Left-border 3px màu semantic. Hierarchy bắt buộc:  
`kpi-label` (10px uppercase) → `kpi-value` (19px, weight 800) → `kpi-note` (11px muted)

```css
.kpi-box { 
  background: var(--white); 
  border: 1px solid var(--border); 
  border-radius: var(--radius-md); 
  padding: 16px 18px; 
  box-shadow: var(--shadow-card); 
}
.kpi-box .kpi-label { 
  font-size: 10px; 
  font-weight: 700; 
  color: var(--text-faint); 
  text-transform: uppercase; 
  letter-spacing: 1px; 
  margin-bottom: 6px; 
}
.kpi-box .kpi-value { 
  font-size: 19px; 
  font-weight: 800; 
  color: var(--text-dark); 
  line-height: 1.2; 
}
.kpi-box .kpi-note  { 
  font-size: 11px; 
  color: var(--text-muted); 
  margin-top: 4px; 
  line-height: 1.5; 
}
.kpi-box.pink  { border-left: 3px solid var(--pink-core); }
.kpi-box.green { border-left: 3px solid var(--green); }
.kpi-box.amber { border-left: 3px solid var(--amber); }
.kpi-box.blue  { border-left: 3px solid var(--blue); }
```

### Card

```css
.card { 
  background: var(--white); 
  border: 1px solid var(--border); 
  border-radius: var(--radius-md); 
  padding: 20px; 
  margin-bottom: 16px; 
  box-shadow: var(--shadow-card); 
}
.card-title { 
  font-size: 13.5px; 
  font-weight: 700; 
  color: var(--text-dark); 
  margin-bottom: 3px; 
  display: flex; 
  align-items: center; 
  gap: 7px; 
}
.card-sub   { 
  font-size: 11.5px; 
  color: var(--text-faint); 
  margin-bottom: 16px; 
}
```

### Tables

- Header: `--bg-soft`, `--text-faint`, uppercase 10px
- Row hover: `--bg-soft`
- Wrap trong `.table-wrap` để có `overflow-x: auto`

```css
.table-wrap { 
  overflow-x: auto; 
  border-radius: var(--radius-sm); 
  border: 1px solid var(--border); 
}
table.dt { 
  width: 100%; 
  border-collapse: collapse; 
  font-size: 12.5px; 
  min-width: 520px; 
}
table.dt th { 
  background: var(--bg-soft); 
  color: var(--text-faint); 
  font-weight: 700; 
  font-size: 10px; 
  letter-spacing: 1px; 
  text-transform: uppercase; 
  padding: 10px 14px; 
  text-align: left; 
  border-bottom: 1px solid var(--border-soft); 
  white-space: nowrap; 
}
table.dt td { 
  padding: 10px 14px; 
  color: var(--text-body); 
  border-bottom: 1px solid #F5F5F5; 
  vertical-align: top; 
  line-height: 1.55; 
}
table.dt tr:last-child td { border-bottom: none; }
table.dt tr:hover td { background: var(--bg-soft); }
```

### Grid System

```css
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
```

### Navigation Active State

```css
color: var(--pink-core);
background: var(--pink-dim);
border-left: 2px solid var(--pink-core);
font-weight: 600;
```

---

## Animation System

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

## Border Radius Reference

| Token | Value | Dùng cho |
|-------|-------|----------|
| `--radius-sm` | 6px | Table wrap, chip, highlight box |
| `--radius-md` | 10px | Card, kpi-box, okr-block |
| `--radius-lg` | 14px | Hero banner |
| pill | 20px | Badge, tag-pill (hardcode, không dùng token) |

---

## Template Components

### Sidebar Footer Template

```html
<div class="sidebar-footer">
  Out-App Traffic · GPD<br>
  Last updated: [Tháng/Năm]<br>
  MoMo — momo.vn
</div>
```

### Hero Banner Template

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

**Styling H1 span:** Dùng gradient text: `linear-gradient(135deg, var(--pink-core), var(--pink-mid))` với `-webkit-background-clip: text`.

---

## Checklist khi tạo mới document

- [ ] Font Be Vietnam Pro đã import
- [ ] Tất cả CSS variables khai báo trong `:root`
- [ ] Title format: `[Use Case] - [Doc Type] | MoMo`
- [ ] Sidebar footer: team name + last updated (không có version)
- [ ] Không có emoji trong card content
- [ ] Badge dùng pill (20px), chip dùng square (4px)
- [ ] Shadow có pink tinge
- [ ] Mobile breakpoint 768px có hamburger + overlay
- [ ] Responsive layout kiểm tra trên mobile (width < 768px)
- [ ] Tất cả interactive state đã styled rõ ràng
- [ ] Color contrast đủ tiêu chuẩn accessibility

---

## Implementation Rules (Final)

1. **Consistency:** Mọi document theo skill này phải giống nhau về:
   - Color palette (dùng CSS variables)
   - Typography scale (dùng px cố định, không rem)
   - Component pattern (badge/chip/kpi/card tuyệt đối không thay đổi)
   - Layout structure (sidebar 252px, main padding 28px)

2. **No Deviation:** Nếu tìm thấy nhu cầu để thay đổi format, phải thảo luận với team trước - không được tự ý sáng tạo.

3. **Maintenance:** Khi skill này cập nhật, tất cả documents cũ phải được audit lại để compliance.

4. **Mobile First:** Kiểm tra luôn responsive behavior ở 768px breakpoint - đây là điểm gãy duy nhất.

---

**Skill này là "source of truth" cho toàn bộ HTML documentation MoMo Out-App Traffic. Bất kỳ câu hỏi về design/layout/color, đều được giải quyết qua tài liệu này.**
