# Web Health & URL Governance Policy
## momo.vn - Platform Health Management

> **Version:** 2.0 | **Ngày tạo:** 2026-05-22 | **Ngày hiệu lực:** Sau khi VP phê duyệt
> **Policy Owner:** Văn Hiến - Web Product Lead, Out-App Traffic, GPD
> **Approver:** Công - VP, Growth Platform Division
> **Trạng thái:** Draft - Pending VP Approval
> **Chu kỳ review:** 6 tháng / khi có thay đổi platform lớn

---

## TÓM TẮT ĐIỀU HÀNH

Chính sách này thiết lập tiêu chuẩn bắt buộc về quản lý vòng đời URL trên www.momo.vn, nhằm bảo vệ hiệu suất SEO/GEO, ngăn ngừa rủi ro AI Search trích dẫn thông tin tài chính sai, và đảm bảo sức khoẻ toàn bộ domain trong dài hạn.

**Vấn đề cốt lõi:** Mô hình PLG của MoMo cho phép Cell Teams tự đưa sản phẩm lên web qua API, nhưng thiếu cơ chế quản lý vòng đời URL sau khi sản phẩm ngưng. Hệ quả là tích lũy crawl waste, pha loãng Topical Authority, và rủi ro AI Search engine trích dẫn thông tin lỗi thời gây hại cho người dùng.

**Giải pháp:** 4 cấp độ xử lý URL theo mức độ nghiêm trọng + quy trình 3 giai đoạn vận hành liên tục.

---

## MỤC LỤC

1. [Mục đích & Phạm vi áp dụng](#1-mục-đích--phạm-vi-áp-dụng)
2. [Định nghĩa thuật ngữ](#2-định-nghĩa-thuật-ngữ)
3. [Chính sách lõi & Nguyên tắc bắt buộc](#3-chính-sách-lõi--nguyên-tắc-bắt-buộc)
4. [4 Cấp độ Xử lý URL](#4-4-cấp-độ-xử-lý-url)
5. [Pre-Launch Gate](#5-pre-launch-gate)
6. [Quy trình Vận hành](#6-quy-trình-vận-hành)
7. [Exception Management](#7-exception-management)
8. [Ma trận RACI & Ownership](#8-ma-trận-raci--ownership)
9. [Chế tài & Enforcement](#9-chế-tài--enforcement)
10. [KPIs & Reporting](#10-kpis--reporting)
11. [Review & Maintenance](#11-review--maintenance)
12. [Phụ lục A: Rủi ro Triển khai](#phụ-lục-a-rủi-ro-triển-khai)
- [Phê duyệt](#phê-duyệt)
- [Changelog](#changelog)

---

## 1. Mục đích & Phạm vi áp dụng

### 1.1 Mục đích

Chính sách này nhằm:
- Thiết lập tiêu chuẩn bắt buộc về chất lượng URL trên www.momo.vn
- Bảo vệ Crawl Budget và Topical Authority của domain
- Ngăn ngừa AI Search engine trích dẫn thông tin tài chính lỗi thời từ momo.vn
- Tạo cơ chế governance rõ ràng giữa Growth Platform và Cell Teams trong toàn bộ vòng đời URL

### 1.2 Phạm vi áp dụng

**Áp dụng cho:**
- Tất cả URL trên domain www.momo.vn và subdomain thuộc sở hữu MoMo
- Tất cả Cell Teams có sản phẩm hoặc tính năng hiển thị trên web
- Tất cả Dynamic Pages được tạo bởi API của Cell Teams
- Tất cả Landing Pages, Hub Pages, Blog Pages, Product Pages

**Không áp dụng cho:**
- Trang kỹ thuật nội bộ: robots.txt, sitemap.xml, các file config hệ thống
- Trang xác thực danh tính: login, register, OTP flow
- API endpoints không phục vụ người dùng cuối

### 1.3 Ngày hiệu lực

| Đối tượng | Ngày hiệu lực |
|----------|--------------|
| URL mới (chưa publish) | Ngay khi VP ký phê duyệt |
| URL hiện có | Theo lộ trình Zero-Traffic URL Audit Q2/2026 |
| Exception đã tồn tại | Review trong 30 ngày kể từ ngày hiệu lực |

---

## 2. Định nghĩa thuật ngữ

| Thuật ngữ | Định nghĩa |
|----------|-----------|
| **URL** | Địa chỉ trang web duy nhất trên momo.vn. Ví dụ: momo.vn/vay-nhanh |
| **Cell Team** | Nhóm sản phẩm nội bộ sở hữu một tính năng/Use Case cụ thể trên web MoMo |
| **Cell PO** | Product Owner của Cell Team - người chịu trách nhiệm quyết định và phản hồi về các trang web thuộc Use Case đó |
| **Hub Page** | Trang danh mục/tổng hợp của một nhóm sản phẩm. Ví dụ: momo.vn/bao-hiem là Hub Page của nhóm Bảo hiểm |
| **Dynamic Page** | Trang được tạo tự động từ API của Cell Team, nội dung thay đổi theo data. Ví dụ: trang merchant, trang rạp chiếu phim |
| **Life-cycle URL** | URL có vòng đời xác định trước: campaign ngắn hạn, event theo mùa, khuyến mãi có ngày kết thúc |
| **Zero-Traffic URL** | URL có dưới 100 organic sessions trong 90 ngày liên tiếp, đo bởi GA4 + GSC |
| **Organic Traffic** | Lượt truy cập từ kết quả tìm kiếm tự nhiên (Google, Bing, AI Search). Không bao gồm paid, direct, referral |
| **Tài chính cốt lõi** | Nhóm Use Case gắn trực tiếp với Revenue/User Acquisition: Vay Nhanh, Ví Trả Sau (BNPL), Bảo hiểm xe máy, Bảo hiểm ô tô, Bảo hiểm y tế, CIC Score, Tiết kiệm |
| **YMYL** | Your Money Your Life - nội dung có ảnh hưởng trực tiếp đến quyết định tài chính: lãi suất, phí, điều kiện vay, điều khoản bảo hiểm. Yêu cầu cập nhật bắt buộc mỗi 90 ngày |
| **Topical Authority** | Mức độ Google/AI đánh giá momo.vn là nguồn uy tín về một chủ đề. Bị pha loãng khi domain tồn tại quá nhiều trang chủ đề ngoài chuyên môn cốt lõi |
| **Crawl Budget** | Giới hạn số trang Googlebot crawl trên momo.vn trong một khoảng thời gian. Trang kém chất lượng tiêu tốn crawl budget không hiệu quả, kéo hiệu suất toàn domain xuống |
| **W2A (Web-to-App)** | Tỷ lệ chuyển đổi từ người dùng web sang người dùng App (Install hoặc Register), đo bởi Appsflyer/Onelink |
| **Noindex** | Chỉ thị kỹ thuật bằng meta tag hoặc HTTP header yêu cầu Google không đưa trang vào kết quả tìm kiếm |
| **Growth Platform** | Team Out-App Traffic - cụ thể là SEO Lead (Hiến) và Web Platform Manager (Bảo) |
| **Growth Plan** | Kế hoạch tăng trưởng tối thiểu 6 tháng bao gồm: target keyword cluster, traffic milestone, resource commit |

---

## 3. Chính sách lõi & Nguyên tắc bắt buộc

### 3.1 Tuyên bố chính sách

**Mọi URL trên www.momo.vn bắt buộc phải đáp ứng ít nhất 1 trong 3 tiêu chí sau:**

| Tiêu chí | Định nghĩa | Ngưỡng | Nguồn đo |
|---------|-----------|--------|---------|
| **Traffic** | Có organic traffic ổn định | Tối thiểu 100 sessions/90 ngày | GA4 + GSC |
| **Authority** | Thuộc tài chính cốt lõi hoặc có Exception approval | Danh sách tại mục 2 + Exception Log | Manual audit |
| **Plan** | Có Growth Plan được SEO Lead approve | Tối thiểu 6 tháng, đủ 3 thành phần bắt buộc | Growth Plan document |

**URL không đáp ứng bất kỳ tiêu chí nào bắt buộc phải được xử lý theo 4 cấp độ tại Mục 4.**

### 3.2 Nguyên tắc bắt buộc

1. **Không publish nếu chưa qua Pre-Launch Gate.** Mọi trang mới phải được SEO Lead approve trước khi đưa lên Production.
2. **Không để trang YMYL lỗi thời quá 90 ngày.** Cell Team bắt buộc cập nhật nội dung YMYL tối thiểu mỗi 3 tháng.
3. **Không redirect 308 về trang không liên quan nội dung.** Nghiêm cấm redirect về trang chủ khi không có Hub phù hợp - phải dùng Noindex (Cấp 3).
4. **Growth Platform có quyền áp dụng Cấp 1 không cần xin phép** khi Cell PO không phản hồi trong 10 ngày làm việc.
5. **Exception bắt buộc phải có VP approve.** SEO Lead không có thẩm quyền tự approve exception cho Use Case ngoài tài chính cốt lõi.

---

## 4. 4 Cấp độ Xử lý URL

### Tổng quan

| Cấp | Tên | Hành động kỹ thuật | Tính đảo ngược |
|-----|-----|-------------------|---------------|
| 1 | Giảm ưu tiên | Nofollow + Gỡ Sitemap | Có - dễ |
| 2 | Chuyển hướng | 308 Redirect về Hub | Có - khó |
| 3 | Ẩn khỏi Index | Noindex + Gỡ Sitemap | Có - dễ |
| 4 | Cập nhật bắt buộc | Content refresh | Không áp dụng |

---

### Cấp 1: Nofollow + Gỡ khỏi Sitemap

**Áp dụng khi URL rơi vào ít nhất 1 trường hợp:**
- Dưới 100 organic sessions/90 ngày, không đúng authority, và không có Growth Plan
- Cell PO không phản hồi trong 10 ngày làm việc kể từ thông báo
- Cấp 4 không được thực thi trong 14 ngày làm việc (fallback bắt buộc)

**Cơ chế kỹ thuật:**
- Thêm `rel="nofollow"` vào các internal links trỏ đến trang
- Gỡ URL khỏi sitemap.xml
- Trang vẫn tồn tại và người dùng truy cập được qua link trực tiếp

**Thời hạn với Cell Team:** 3 tháng để cải thiện chỉ số hoặc nộp Growth Plan đạt chuẩn. Hết 3 tháng không có tiến triển - Growth Platform chuyển Cấp 2 hoặc Cấp 3.

---

### Cấp 2: 308 Redirect về Hub Page

**Áp dụng khi:**
- Sản phẩm đã ngưng hoàn toàn VÀ còn tồn tại Hub Page liên quan đang hoạt động

**Cơ chế kỹ thuật:**
- Thiết lập HTTP 308 Permanent Redirect từ URL cũ về Hub Page gần nhất về chủ đề
- Giá trị SEO (link equity) được chuyển về Hub

**Ràng buộc bắt buộc:** Hub Page đích phải liên quan trực tiếp về nội dung. **Nghiêm cấm** redirect về trang chủ hoặc trang không cùng chủ đề.

| Trường hợp | Hợp lệ |
|-----------|--------|
| momo.vn/khuyen-mai/cinema-tet-2025 → momo.vn/cinema | ✅ |
| momo.vn/bao-hiem-xe-may/brand-xyz (ngưng bán) → momo.vn/bao-hiem-xe-may | ✅ |
| momo.vn/game/event-cu → momo.vn (trang chủ) | ❌ |

---

### Cấp 3: Noindex - Ẩn khỏi Google Index

**Áp dụng khi:**
- Sản phẩm đã ngưng hoàn toàn VÀ không có Hub Page phù hợp để chuyển hướng
- URL có Life-cycle xác định đã hết hạn (campaign, event, khuyến mãi)

**Cơ chế kỹ thuật:**
- Thêm `<meta name="robots" content="noindex, nofollow">` vào `<head>` của trang
- Hoặc HTTP header: `X-Robots-Tag: noindex, nofollow`
- Gỡ URL khỏi sitemap.xml
- Trang vẫn tồn tại trên server - người dùng có link trực tiếp vẫn truy cập được

**Lý do chọn Noindex thay vì 410 Gone:**
- Khả thi về nền tảng kỹ thuật: chỉ cần meta tag hoặc HTTP header, không cần server-level config
- Reversible: nếu sản phẩm được tái kích hoạt, xoá meta tag là đủ

---

### Cấp 4: Cập nhật nội dung bắt buộc

**Áp dụng khi:**
- URL có ít nhất 100 organic sessions/90 ngày VÀ nội dung YMYL đã lỗi thời (lãi suất, phí, điều kiện)
- URL đúng authority nhưng chưa cập nhật quá 90 ngày (YMYL) hoặc quá 180 ngày (non-YMYL)

**Thời hạn bắt buộc:** Cell Team có **14 ngày làm việc** để cập nhật kể từ ngày nhận thông báo.

**Fallback bắt buộc:** Quá 14 ngày không cập nhật - Growth Platform áp dụng Cấp 1 ngay lập tức. Cell Team vẫn có nghĩa vụ hoàn thành cập nhật.

---

## 5. Pre-Launch Gate

### Điều kiện publish

Mọi trang/sản phẩm mới **bắt buộc phải được SEO Lead approve** trước khi đưa lên Production. Trang không có approval không được publish.

### Checklist 5 tiêu chí

| # | Tiêu chí | Mô tả | Pass/Fail | Owner |
|---|---------|-------|-----------|-------|
| 1 | **Growth Plan** | Roadmap tối thiểu 6 tháng kèm keyword cluster, traffic milestone 3 tháng, tên người phụ trách content | SEO Lead approve | Cell PO |
| 2 | **Chất lượng nội dung** | Nội dung đầy đủ, chính xác. Không phải trang trống hoặc raw API data | SEO Lead review | Cell PO |
| 3 | **API ổn định** | API đã QA, có fallback UI rõ khi API lỗi. Không để trang trắng hoặc error message lộ ra người dùng | Dev/QC confirm | Dev |
| 4 | **Cam kết cập nhật** | YMYL: tối thiểu mỗi 90 ngày. Non-YMYL: tối thiểu mỗi 180 ngày. Cell PO ký xác nhận | Cell PO ký | Cell PO |
| 5 | **Cấu hình SEO** | Index strategy, schema markup, internal linking, canonical tag đã review và approve | SEO Lead approve | SEO Lead |

**Growth Plan tối thiểu phải bao gồm 3 thành phần:**
1. Target keyword cluster - tối thiểu 5 từ khóa chính
2. Traffic milestone sau 3 tháng - con số sessions cụ thể
3. Người phụ trách content - tên cá nhân, không phải tên team

**Kết quả Pre-Launch Gate:**
- Pass tất cả 5 tiêu chí: Được publish lên Production theo index strategy đã duyệt
- Fail bất kỳ 1 tiêu chí: Không được publish. Ngoại lệ - publish Cấp 1 (nofollow + không vào sitemap) nếu Cell Team có lý do kỹ thuật phải đặt URL sớm và được SEO Lead chấp thuận

---

## 6. Quy trình Vận hành

### Giai đoạn 1: Pre-Launch

Xem Mục 5. SEO Lead là gate duy nhất.

---

### Giai đoạn 2: Giám sát hàng tháng

Growth Platform thực hiện URL Health Scan vào **tuần đầu mỗi tháng** và gửi báo cáo cho từng Cell PO trong 5 ngày làm việc.

| Chỉ số | Định nghĩa | Ngưỡng cảnh báo | Nguồn dữ liệu |
|--------|-----------|----------------|---------------|
| Zero-Traffic | Dưới 100 organic sessions/90 ngày | 1 URL trở lên | GA4 + GSC |
| Lỗi API | Trang trả về nội dung trống hoặc error message hiển thị | 1 URL trở lên | Health check tự động |
| YMYL quá hạn | YMYL không cập nhật quá 90 ngày | 1 URL trở lên | CMS audit |
| Thin content | Dưới 300 từ nội dung unique, không tính navigation và footer | 1 URL trở lên | Crawl tự động |
| Index errors | URL submitted sitemap nhưng không được index | Trên 5% tổng submitted | GSC Coverage |

**Output bắt buộc:** Dashboard + email gửi Cell PO kèm danh sách URL vi phạm cụ thể, cấp độ đề xuất xử lý, và deadline phản hồi.

---

### Giai đoạn 3: Xử lý khi phát hiện vấn đề

```
Growth Platform phát hiện vấn đề
→ Gửi thông báo cho Cell PO (kèm danh sách URL + cấp độ đề xuất + deadline)
         |
         v
Cell PO phản hồi trong 10 ngày làm việc?
    |
    |-- KHÔNG → Growth Platform áp Cấp 1 ngay (không cần xin phép)
    |            → Báo cáo lên HoD của Cell Team
    |
    └-- CÓ → Xác định trạng thái sản phẩm
              |
              |-- Sản phẩm ĐANG HOẠT ĐỘNG
              |    |
              |    |-- Nội dung YMYL lỗi thời
              |    |   → Cấp 4: Cell Team có 14 ngày cập nhật
              |    |   → Quá hạn: Cấp 1 tự động
              |    |
              |    └-- Vấn đề khác (thin content, API lỗi, zero-traffic)
              |        → Cấp 1: Cell Team có 3 tháng cải thiện
              |        → Hết 3 tháng không tiến triển: chuyển Cấp 2 hoặc Cấp 3
              |
              └-- Sản phẩm ĐÃ NGƯNG / Không có kế hoạch
                   |
                   |-- Còn Hub Page liên quan đang hoạt động
                   |   → Cấp 2: 308 Redirect về Hub
                   |
                   └-- Không có Hub phù hợp
                       → Cấp 3: Noindex + Gỡ Sitemap
```

**SEO Lead** thực thi kỹ thuật. **Dev** hỗ trợ khi cần thay đổi ở server hoặc CMS level. Kết quả cập nhật vào báo cáo tháng tiếp theo.

---

## 7. Exception Management

### 7.1 Tiêu chí được xét exception

Use Case ngoài tài chính cốt lõi được giữ lại trên momo.vn nếu đồng thời đáp ứng **cả 2 tiêu chí:**

| Tiêu chí | Ngưỡng tối thiểu | Nguồn đo |
|---------|-----------------|---------|
| Organic Traffic | Trên 300,000 sessions/quý | GA4 - Organic channel |
| Web-to-App Rate | Trên 5% | Appsflyer/Onelink - Install hoặc Register |

*Ngưỡng này được xây dựng dựa trên benchmark Cinema - Use Case non-financial hiệu quả nhất hiện tại: >1M sessions/quý, W2A 12.1%.*

### 7.2 Quy trình nộp exception

| Bước | Hành động | Thời hạn | Owner |
|------|----------|---------|-------|
| 1 | Cell PO nộp Exception Request cho SEO Lead kèm: GA4 export 90 ngày, Appsflyer export 90 ngày, Growth Plan 6 tháng | - | Cell PO |
| 2 | SEO Lead review và đề xuất lên VP | 5 ngày làm việc | SEO Lead |
| 3 | VP approve hoặc reject | 5 ngày làm việc | VP (Công) |
| 4 | SEO Lead thông báo kết quả + ghi vào Exception Log | 2 ngày làm việc | SEO Lead |

### 7.3 Điều kiện duy trì exception

- Exception có hiệu lực **6 tháng** kể từ ngày VP approve
- Cell PO có trách nhiệm **tái xét** trước khi hết hạn để gia hạn
- Exception **tự động hết hạn** nếu chỉ số traffic hoặc W2A giảm dưới ngưỡng trong 2 quý liên tiếp mà không có kế hoạch phục hồi được VP approve

### 7.4 Exception Log hiện hành

| Use Case | Lý do | Ngày VP approve | Hết hạn | Trạng thái |
|---------|-------|----------------|---------|-----------|
| Cinema | Traffic >1M sessions/quý, W2A 12.1% | Pending | Pending | Chờ policy hiệu lực |

---

## 8. Ma trận RACI & Ownership

| Hoạt động | SEO Lead (Hiến) | Cell PO | Dev (Trọng) | DA Team | VP (Công) |
|-----------|----------------|---------|------------|---------|-----------|
| URL Health Scan hàng tháng | R/A | I | I | C | I |
| Phân loại cấp độ xử lý | R/A | C | I | I | I |
| Thực thi Cấp 1 (nofollow/sitemap) | R/A | I | C | I | I |
| Thực thi Cấp 2 (308 redirect) | R/A | I | R | I | I |
| Thực thi Cấp 3 (noindex) | R/A | I | C | I | I |
| Xác nhận trạng thái sản phẩm | I | R/A | I | I | I |
| Thực thi Cấp 4 (content update) | C | R/A | I | I | I |
| Pre-Launch Gate approve/reject | R/A | C | C | I | I |
| Exception Request - đề xuất | R | C | I | I | A |
| Escalate Cell PO không hợp tác | R | I | I | I | A |
| Monitoring dashboard | R/A | I | I | C | I |
| Policy review định kỳ | R | C | C | I | A |

*R = Responsible | A = Accountable | C = Consulted | I = Informed*

---

## 9. Chế tài & Enforcement

### 9.1 Quyền hạn của Growth Platform

**Growth Platform có quyền áp dụng ngay, không cần xin phép:**
- Cấp 1 khi Cell PO không phản hồi trong 10 ngày làm việc
- Cấp 1 khi Cấp 4 quá 14 ngày làm việc không được thực thi

**Growth Platform bắt buộc phải escalate lên VP trước khi thực thi:**
- Cấp 2 (308 Redirect) khi Cell PO phản đối
- Cấp 3 (Noindex) khi Cell PO phản đối
- Mọi trường hợp Cell PO từ chối phối hợp sau khi đã áp Cấp 1

### 9.2 Hậu quả không tuân thủ

| Vi phạm | Hậu quả ngay lập tức | Hậu quả leo thang |
|--------|--------------------|--------------------|
| Không phản hồi trong 10 ngày làm việc | Growth Platform áp Cấp 1 | Báo cáo lên HoD của Cell Team |
| Cấp 4 quá 14 ngày không thực thi | Cấp 1 tự động | Ghi nhận trong báo cáo quý gửi VP |
| Cell PO từ chối phối hợp sau Cấp 1 | Escalate VP | VP quyết định và chỉ đạo trực tiếp |
| Publish URL không qua Pre-Launch Gate | SEO Lead yêu cầu takedown hoặc áp Cấp 1 ngay | Báo cáo HoD + VP |

### 9.3 Dispute Resolution

Khi Cell PO không đồng ý với quyết định phân loại cấp độ của SEO Lead:

1. Cell PO nộp objection bằng văn bản cho SEO Lead trong **5 ngày làm việc** kể từ thông báo
2. SEO Lead và Cell PO họp trong **3 ngày làm việc** để align
3. Không đồng thuận: escalate lên VP (Công). **Quyết định của VP là cuối cùng.**

---

## 10. KPIs & Reporting

### 10.1 KPIs chính sách

| Metric | Mục tiêu | Chu kỳ đo | Nguồn |
|--------|---------|-----------|-------|
| Tỷ lệ URL indexed/submitted sitemap | Tăng so với baseline Q1/2026 | Hàng tháng | GSC Coverage |
| Crawl errors & Soft 404 | Giảm 20% mỗi quý | Hàng tháng | GSC Coverage |
| YMYL pages cập nhật đúng chu kỳ | 100% | Hàng tháng | CMS audit |
| URL đang ở Cấp 1 | Giảm dần, mục tiêu 0 sau 12 tháng | Hàng quý | Internal log |
| Thời gian xử lý từ phát hiện đến thực thi | Dưới 14 ngày làm việc | Hàng tháng | Internal log |

### 10.2 Lịch báo cáo

| Báo cáo | Tần suất | Gửi đến | Owner |
|--------|---------|--------|-------|
| URL Health Report | Hàng tháng, tuần đầu tháng | Cell POs + HoD liên quan | SEO Lead |
| Policy Compliance Summary | Hàng quý | VP (Công) | SEO Lead |
| Exception Log update | Khi có thay đổi | VP (Công) | SEO Lead |

---

## 11. Review & Maintenance

| Trigger | Chu kỳ review | Owner |
|--------|--------------|-------|
| Định kỳ | 6 tháng/lần | SEO Lead + VP |
| Google algorithm update lớn | Trong 30 ngày sau update | SEO Lead |
| Thay đổi platform MoSpark hoặc CMS lớn | Trước khi platform change deploy | SEO Lead + Dev |
| Zero-Traffic URL Audit Q2/2026 hoàn thành | Trong 30 ngày sau khi audit xong | SEO Lead |

**Mọi thay đổi nội dung chính sách bắt buộc phải được VP approve trước khi có hiệu lực.**
Thay đổi nhỏ về threshold và tiêu chí đo lường: SEO Lead có thể cập nhật và thông báo VP trong 5 ngày làm việc.

---

## Phụ lục A: Rủi ro Triển khai

*Tài liệu làm việc nội bộ - không phải nội dung governance chính thức.*

### A.1 Rủi ro còn mở

| Rủi ro | Mức độ | Khuyến nghị |
|--------|--------|------------|
| Thiếu automation cho monthly monitoring - SEO Lead dễ overload bandwidth khi carry nhiều workstream song song | Cao | Prioritize automation dashboard (Umami Module 5). Xem xét giao execution monitoring cho DA Team (Hải/Hoàng) |
| Cell PO từ chối phối hợp kéo dài - Growth Platform không có quyền force Cell Team không qua VP | Trung bình - Cao | Policy chỉ có răng khi VP mandate được giao rõ ràng và HoD các Cell Team được thông báo trước |
| Growth Plan template chưa formalize trong MoSpark flow - Cell PO có thể nộp kế hoạch chung chung | Trung bình | Tích hợp Growth Plan template vào MoSpark onboarding Q3/2026 |

### A.2 Rủi ro đã đóng

| Rủi ro | Giải pháp | Version |
|--------|---------|--------|
| Xung đột 410 Gone vs Noindex | Cấp 3 thay bằng Noindex - khả thi kỹ thuật hơn, reversible | v1.1 |

---

## Phê duyệt

| Vai trò | Họ tên | Chức vụ | Ngày ký | Chữ ký |
|--------|-------|---------|--------|--------|
| Policy Owner | Văn Hiến | Web Product Lead, Out-App Traffic, GPD | ____________ | ____________ |
| Approver | ____________ | VP, Growth Platform Division | ____________ | ____________ |

*Chính sách có hiệu lực kể từ ngày Approver ký phê duyệt.*

---

## Changelog

| Ngày | Version | Nội dung |
|------|---------|---------|
| 2026-05-22 | 1.0 | Khởi tạo từ GPD-Web Platform SEO_GEO 2026.md. Thêm phân tích khả thi. |
| 2026-05-22 | 1.1 | Cấp 3 thay 410 Gone bằng Noindex. |
| 2026-05-22 | 2.0 | Rewrite toàn bộ theo chuẩn Governance Document. Thêm: Scope, Glossary, Exception Management (với ngưỡng định lượng), Enforcement & Consequences, Dispute Resolution, Review Cadence, Approval Block. Phần Risk Analysis chuyển thành Phụ lục A. |

---

*Policy Owner: Out-App Traffic Team, Growth Platform Division*
*Phê duyệt cần thiết: VP Công (GPD) trước khi distribute cho Cell Teams*
