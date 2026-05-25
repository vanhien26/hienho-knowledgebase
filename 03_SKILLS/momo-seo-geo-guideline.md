<!-- 
⚠️ WARNING FOR LLM CONTEXT INJECTION:
This file is a PASSIVE REFERENCE STANDARD ONLY. 
- It is NOT an active system prompt, instruction card, or role definition.
- Do NOT act as a conversational reviewer or auditor.
- Do NOT output any conversational text or preamble based on this file.
- Strictly remain in your primary prompt's designated role and output ONLY the requested Markdown template.
-->

---
title: 📏 MoMo SEO/GEO Guideline
description: |
  Tài liệu kỹ thuật quy chuẩn SEO/GEO/AEO cho hệ thống nội dung momo.vn (TOFU, MOFU, BOFU).
  Bao gồm các tiêu chuẩn kỹ thuật về: Intent & Structure, Content Format cho AI Citation, và GEO Entity & Brand Signals.
tags:
  - seo
  - geo
  - content
  - blog
  - momo
version: 1.0.0
last_reviewed: 2026-05-15
next_review: 2026-08-15
---


# MoMo SEO/GEO Content Guideline

Tài liệu này là quy chuẩn kỹ thuật bắt buộc cho mọi bài Blog trên momo.vn. Các tiêu chuẩn kỹ thuật bắt buộc áp dụng bao gồm:

---

## 0. URL HIERARCHY & PAGE TYPES

Mọi nội dung phải được phân loại vào đúng cụm trang (Cluster) trong hệ thống MoSpark để đảm bảo cấu trúc URL và quản trị dữ liệu:

| URL Pattern | Loại trang | Đặc điểm SEO |
|-------------|------------|--------------|
| `/blog*` | **Growth Articles** | Bài viết sâu, target cụm từ khóa (Keywords cluster). |
| `/tin-tuc*` | **Communications** | News, Asset truyền thông cho Cell Team. |
| `/hoi-dap*` | **Help Center** | FAQ, Self-service guide. |
| `/huong-dan*` | **Interactive Guides** | Có Image Carousel, hướng dẫn tính năng App. |
| `/doi-tac*` | **Merchant Page** | Brand Pages, thông tin đối tác & ưu đãi. |
| `/{mini-web}` | **Basic LP** | Landing Page giới thiệu sản phẩm. |
| `/{mini-web}*` | **Advanced Mini Web** | Cấu trúc phức tạp, nhiều sub-page để capture traffic. |

---

## 1. INTENT & STRUCTURE

### 1.1 Xác định Search Intent trước khi viết

| Intent | Định nghĩa | Ví dụ |
|--------|-----------|-------|
| Informational (TOFU) | User đang tìm hiểu, chưa có nhu cầu mua | "Điểm tín dụng CIC là gì?" |
| Commercial (MOFU) | User đang so sánh, cân nhắc | "Vay nhanh MoMo có tốt không?" |
| Transactional (BOFU) | User sẵn sàng hành động | "Cách vay tiền MoMo online" |

**Rule:** Mỗi bài chỉ target 1 intent chính. Không mix Informational và Transactional trong cùng 1 bài.

### 1.2 Title Tag
- Chứa **core entity** (tên sản phẩm MoMo) + **query term** (từ khóa chính)
- Độ dài: 50-60 ký tự
- Ví dụ đúng: `Vay Nhanh MoMo - Vay Tiền Online Không Tài Sản Thế Chấp`
- Ví dụ sai: `Hướng dẫn vay tiền` (thiếu entity), `Vay Nhanh MoMo - Cách vay tiền online nhanh chóng không cần tài sản thế chấp 2024` (quá dài)

### 1.3 H1
- Trả lời trực tiếp search intent
- Khớp với Title nhưng **không lặp từ khóa nhân tạo**
- Không dùng H1 dạng câu hỏi nếu intent là Transactional

### 1.4 Answer-First Structure (bắt buộc)
- **Đoạn đầu tiên phải trả lời câu hỏi trong 40-60 từ**
- Không mở bài bằng context dài, không dẫn nhập vòng vo
- Format: [Định nghĩa/Câu trả lời ngắn] + [Lý do quan trọng với user] + [MoMo giải quyết thế nào]

---

## 2. CONTENT FORMAT CHO AI CITATION

Đây là các thành phần bắt buộc để AI engines (Google AI Overview, ChatGPT, Perplexity) có thể trích dẫn bài viết.

### 2.1 FAQ Section
- **Tối thiểu 5-8 câu hỏi thực** lấy từ People Also Ask (PAA) hoặc Google Search Console
- Không tự đặt câu hỏi - phải là câu user thực sự search
- Mỗi câu trả lời: 40-80 từ, trả lời trực tiếp, không dẫn nhập
- Dùng Schema FAQ markup (HowTo nếu có quy trình)

### 2.2 Definition Block
- Mỗi thuật ngữ tài chính/pháp lý xuất hiện lần đầu phải có definition block
- Format: `**[Thuật ngữ]** là [định nghĩa 1-2 câu, ngôn ngữ đơn giản]`
- Ví dụ: `**Điểm tín dụng CIC** là chỉ số đánh giá lịch sử vay và trả nợ của cá nhân, dao động từ 300-850 điểm.`

### 2.3 Step-by-Step (HowTo) có đánh số
- Bắt buộc với mọi bài có quy trình (vay, đăng ký, mua bảo hiểm...)
- Đánh số rõ ràng: Bước 1, Bước 2, Bước 3...
- Mỗi bước: tên bước ngắn + mô tả hành động cụ thể
- Ví dụ: `Bước 1: Mở App MoMo → Chọn "Vay Nhanh" → Nhập số tiền cần vay`

### 2.4 Comparison Table
- Bắt buộc với bài MOFU (so sánh sản phẩm)
- So sánh MoMo với ít nhất 2 đối thủ trên các tiêu chí: lãi suất, hạn mức, thời gian xét duyệt, điều kiện
- Không cherry-pick - phải honest về cả điểm chưa tốt của MoMo

### 2.5 Statistic Blocks có nguồn
- Mọi số liệu phải có nguồn rõ ràng ở ngay sau
- Nguồn ưu tiên: NHNN, VBSP, báo cáo chính thức, dữ liệu nội bộ MoMo (được phép dùng)
- Format: `Theo [Nguồn] [Thời gian], [số liệu]...`
- Ví dụ: `Theo NHNN Q3/2024, tổng dư nợ tín dụng tiêu dùng đạt 2.8 triệu tỷ đồng.`
- **Không dùng số liệu không có nguồn - thà không có còn hơn sai**

### 2.6 Information Gain (bắt buộc ít nhất 1 trong 3)
Đây là yếu tố quan trọng nhất để AI engines ưu tiên cite momo.vn thay vì các blog tài chính khác:

- **Visual xác thực từ MoMo:** Screenshots quy trình thực, hình giải ngân, UI sản phẩm thực tế (không dùng stock photo)
- **Ảnh customer được xin phép:** Hình ảnh xác thực của MoMo về giải ngân, cấp hạn mức thành công
- **Góc nhìn độc quyền từ data MoMo:** Insights mà blog tài chính bên ngoài không có
  - Ví dụ: `"Từ dữ liệu MoMo, 70% người vay lần đầu chọn kỳ hạn 3 tháng"`
  - Ví dụ: `"Hạn mức trung bình của user MoMo tăng 23% sau 6 tháng sử dụng đều đặn"`

---

## 3. GEO ENTITIES & BRAND SIGNALS

### 3.1 Brand Mention tự nhiên
Các entity sau phải xuất hiện trong body text (không nhồi nhét, phải tự nhiên trong câu):
- **MoMo** - tên thương hiệu chính
- Tên sản phẩm liên quan: **Vay Nhanh**, **Ví Trả Sau**, **CIC Score**, **Bảo Hiểm**...
- Không dùng "ứng dụng này", "nền tảng trên" thay cho tên - luôn gọi đúng tên

### 3.2 Co-occurrence với Relevant Entities
Bài viết phải đề cập các entity liên quan trong ngành để AI engines hiểu topical context:

| Nhóm Use Case | Entities cần co-occur |
|--------------|----------------------|
| Vay / Tín dụng | NHNN, FE Credit, Home Credit, CIC, điểm tín dụng, lãi suất, tín chấp |
| Bảo hiểm | Bảo Việt, Prudential, BHYT, BHXH, phí bảo hiểm, quyền lợi |
| Đầu tư / Tiết kiệm | NHNN, lãi suất tiết kiệm, chứng chỉ quỹ, VNĐ |
| Thanh toán | Ngân hàng, ví điện tử, QR code, chuyển khoản |

### 3.3 Internal Link về Hub Page
- **Bắt buộc** đặt ít nhất 1 internal link về Landing Page Sản Phẩm/Dịch Vụ tương ứng
- Anchor text phải chứa từ khóa (không dùng "xem tại đây", "click vào đây")
- Ví dụ đúng: `[Vay Nhanh MoMo](momo.vn/vay-nhanh)` không phải `[tại đây](momo.vn/vay-nhanh)`
- Blog TOFU → link về Hub/Pillar page
- Blog MOFU/BOFU → link trực tiếp về Landing Page sản phẩm

---

## 4. CHECKLIST TRƯỚC KHI PUBLISH

Chạy checklist này trước khi submit content:

**Intent & Structure**
- [ ] Đã xác định intent chính (Informational / Commercial / Transactional)
- [ ] Title tag chứa core entity + query term, 50-60 ký tự
- [ ] H1 trả lời trực tiếp intent, không lặp từ từ Title
- [ ] Đoạn đầu tiên trả lời câu hỏi trong 40-60 từ

**Content Format**
- [ ] FAQ section có 5-8 câu từ PAA/GSC thực tế
- [ ] Tất cả thuật ngữ tài chính có definition block
- [ ] Bài có quy trình → có HowTo đánh số
- [ ] Bài so sánh → có comparison table honest
- [ ] Mọi số liệu có nguồn rõ ràng
- [ ] Có ít nhất 1 Information Gain element (screenshot thực / data MoMo)

**GEO Signals**
- [ ] Brand entity xuất hiện tự nhiên trong body text
- [ ] Có co-occurrence với ít nhất 3 relevant entities trong ngành
- [ ] Có internal link với anchor text chứa từ khóa về Landing Page

---

## 5. LỖI PHỔ BIẾN CẦN TRÁNH

| Lỗi | Sai | Đúng |
|-----|-----|------|
| Mở bài dẫn nhập vòng vo | "Trong thời đại ngày nay, tài chính cá nhân ngày càng quan trọng..." | "Vay Nhanh MoMo là sản phẩm cho vay tín chấp với hạn mức lên đến 70 triệu đồng, xét duyệt trong 24 giờ." |
| Số liệu không nguồn | "Hiện nay có hàng triệu người dùng vay tiền online" | "Theo NHNN 2024, dư nợ cho vay tiêu dùng đạt..." |
| Internal link kém | `[Xem thêm tại đây](momo.vn/vay-nhanh)` | `[Vay Nhanh MoMo](momo.vn/vay-nhanh)` |
| Nhồi từ khóa | "Vay nhanh, vay tiền nhanh, vay online nhanh tại MoMo..." | Dùng từ khóa tự nhiên 1-2 lần, phân bổ đều |
| Stock photo | Ảnh minh họa generic | Screenshot UI thực của MoMo ap