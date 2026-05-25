# BRD: Dịch Vụ Công MoMo - Web Growth & Content Architecture

> - **Project:** Dịch Vụ Công MoMo (DVC) - Governance Hub
> - **Main URL:** `momo.vn/dich-vu-cong` (Governance Hub) + kênh Web chiến lược (Phạt Nguội, ePass)
> - **Version:** 2.5 · Tháng 5/2026
> - **Status:** **DVC Chung** (Info hub - đề án Bộ Công An) | **Phạt Nguội** (BRD riêng, Phase 1 LIVE) | **ePass** (Build Foundation)

---

> **Problem:** Hàng triệu người search thủ tục hành chính, phạt nguội, BHXH mỗi ngày - không fintech nào đang serve intent này trên web. MoMo xử lý 11.2% giao dịch DVCQG nhưng không có một trang web nào giúp user biết điều đó, biết thủ tục cần làm, hay dẫn họ vào App để thanh toán.
> **KPI Owned:** MEU Utility (Web) + MAU % New to services (App)
> **Conversion Flow:** Search "thủ tục [X]" / "phạt nguội" → `/dich-vu-cong/{service}` → Hướng dẫn + CTA → App open → Nộp phí/đóng phạt → Transaction

---

## 1. Executive Summary

### Situation

User cần làm thủ tục hành chính, tra phạt nguội, gia hạn BHYT - họ search Google đầu tiên. Experience hiện tại: tìm thấy VNExpress, Luatvietnam, blog cá nhân - không có fintech nào. MoMo đang xử lý 11.2% giao dịch trên Cổng DVCQG (~1.46M giao dịch/năm) nhưng không có một trang web nào giúp user biết MoMo hỗ trợ gì, biết thủ tục cần làm, hay dẫn họ vào App để thanh toán.

### Complication

Không có touchpoint web = không có acquisition funnel cho segment có purchase intent cao nhất. User đã quyết định nộp phí/phạt, đang search để biết cách - nhưng MoMo không xuất hiện. Với ~5M searches/tháng trên toàn cluster DVC, đây là kênh acquisition organic lớn nhất chưa được khai thác trong toàn bộ portfolio GPD. Mỗi lượt search bị bỏ lỡ là một user không biết MoMo hỗ trợ, một giao dịch không xảy ra trên MoMo.

### Resolution

`momo.vn/dich-vu-cong` là **Governance Hub** - điểm vào duy nhất cho toàn bộ DVC trên web. Product job: user search thủ tục hành chính, phạt nguội, gia hạn BHXH → tìm thấy MoMo → nhận hướng dẫn đủ để hành động → mở App → hoàn thành giao dịch. 3 kênh web chiến lược:

1. **Governance Hub** (`/dich-vu-cong`) - Thông tin & hướng dẫn DVC; align đề án Bộ Công An
2. **Phạt Nguội** (`/phat-nguoi`) - Utility tra cứu; quản lý độc lập tại BRD riêng
3. **ePass/ETC** - Build Foundation; lane Payment (xem Section 1.2)

**North Star:** **MEU Utility (Web)** + **MAU % New to services (App)**. Organic sessions & W2A là Tier B (leading/operational).

### 1.1 BU Portfolio - 8 dịch vụ

| # | Dịch vụ | Vai trò MoMo | Web priority | Ghi chú |
|---|---------|--------------|--------------|---------| 
| 1 | Metro | TBD | Cân nhắc | Resources & strategy |
| 2 | Cổng DVC | Info / hướng dẫn | **Chiến lược** | Đề án Bộ Công An - đang triển khai |
| 3 | Bus (vé buýt công cộng) | TBD | Cân nhắc | |
| 4 | Thuế | TBD | Cân nhắc | |
| 5 | BHXH | TBD | Cân nhắc | Overlap với BHYT |
| 6 | Giáo dục | TBD | Cân nhắc | |
| 7 | Dịch vụ Y tế | TBD | Cân nhắc | |
| 8 | ePass/ETC | Payment Gateway | **Chiến lược** | Section 1.2 - tách lane Payment |

*Các sản phẩm ngoài 3 kênh chiến lược đang cân nhắc vì resources & strategy.*

### 1.2 ePass / ETC (Governance Strategic)

| Giai đoạn | Mô hình |
|-----------|---------| 
| **Before** | Nạp qua provider ETC |
| **After** | ePass liên kết Payment Gateway (MoMo) - 1 User ↔ 1 Payment Gateway |
| **Phase Web** | Governance Strategic → Build Foundation (education/foundation; full payment flow trên Web khi BU chốt) |

- **Lane đo lường:** Payment (MAU, % New to services) - khác Utility/Info của Cổng DVC.
- BRD chi tiết ePass: TBD (file riêng khi BU kick-off).

---

## 2. Bối Cảnh Thị Trường

### 2.1. Thị trường Dịch Vụ Công Số Việt Nam

| Metric | Giá trị | Nguồn |
|---|---|---|
| Tổng giao dịch DVCQG (10 tháng 2025) | 15,725,239 | Cổng DVCQG Overview |
| Tổng giá trị giao dịch | ~10.4 nghìn tỷ VNĐ | Cổng DVCQG Overview |
| Số loại TTHC thanh toán qua Cổng | 1,900+ | Cổng DVCQG Overview |
| MoMo tổng giao dịch | ~1,462,714 (11.2% share) | Tính từ Chi tiết TTHC |

### 2.2. Competitive Landscape - Đơn vị thanh toán trên DVCQG

| Đơn vị | Vị thế | Ghi chú |
|---|---|---|
| VNPT Pay | #1 volume | Chiếm ưu thế ở TTHC chứng thực, hộ tịch |
| NAPAS | #2 volume | Mạnh ở đất đai, doanh nghiệp |
| **MoMo** | **#3 volume (~11.2%)** | Dẫn đầu ở Xét tuyển ĐH (39%), Đổi GPLX (25%) |
| AgriBank | #4 | Mạnh ở vùng nông thôn, đất đai |
| ViettelPay | #5 | Phủ rộng nhưng share thấp |

**Gap chính:** Không đối thủ fintech nào có chiến lược web DVC nghiêm túc. VNExpress, Luatvietnam, blog cá nhân đang chiếm toàn bộ SERP - đây là cửa sổ cơ hội.

### 2.3. Search Market (Cập nhật T5/2026)

| Cluster | Volume/tháng | Ghi chú |
|---|---|---|
| Phạt Nguội | ~2,536,090 | Cluster lớn nhất - quản lý tại BRD Phạt Nguội |
| Phương Tiện (Giao thông) | ~510,910 | Tra cứu biển số xe, đăng ký xe |
| Đổi GPLX | ~230,810 | Thủ tục đổi bằng lái, gia hạn bằng lái |
| Hộ chiếu | ~222,610 | Làm hộ chiếu online, gia hạn hộ chiếu |
| Tạm trú | ~154,540 | Đăng ký tạm trú online |
| CCCD | ~145,690 | Đổi CCCD online, cấp lại CCCD bị mất |
| Thủ tục hành chính (general) | ~102,640 | Dịch vụ công online |
| Đăng ký kết hôn | ~89,420 | Thủ tục đăng ký kết hôn online |
| Đăng kiểm xe | ~76,870 | Thủ tục đăng kiểm online |
| Các cluster khác | ~500,000+ | Thuế, khai sinh, định danh, chứng thực... |
| **Tổng addressable** | **~5,000,000+** | Nguồn: Ahrefs T5/2026 |

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi

User search thủ tục hành chính hoặc phạt nguội - tìm thấy MoMo - nhận đủ thông tin để hành động (checklist, hướng dẫn, deadline) - mở App để hoàn thành giao dịch. Không cần content dài. Không cần đọc nhiều. Product drives the funnel từ search intent đến in-app transaction.

3 outcome phát sinh:

**Acquisition:** MoMo xuất hiện trong SERP khi user có purchase intent cao nhất - cần nộp phí, đóng phạt, gia hạn. Organic traffic là kênh acquisition có cost thấp nhất và intent cao nhất trong DVC vertical.

**Education & Trust:** User biết MoMo hỗ trợ DVC trước khi ra quyết định. Web là touchpoint duy nhất capture được user chưa cài app - không có web, không có education, không có acquisition.

**MEU Foundation:** Governance Hub + Phạt Nguội Tool build MEU Utility baseline - chứng minh web DVC có business value trước khi commit mở rộng toàn bộ portfolio.

### Dự án này KHÔNG phải

- Không build app features mới - Web landing & content; App do Product Owner/Mobile team own
- Không thay thế Cổng DVCQG - không xử lý hồ sơ TTHC trên Web
- Không cam kết full payment journey trên Web cho Cổng DVC - CTA/policy TBD (Define sau với BU)
- Không cover toàn bộ 1,900+ TTHC - focus top demand + 3 kênh Web chiến lược

### 3.2 KPI Framework

| Lane | Ý nghĩa | KPI cam kết | Ví dụ |
|------|---------|-------------|-------|
| **Utility** | Tương tác công cụ / tra cứu / info | **MEU** | Phạt nguội lookup, widget tra cứu |
| **Payment** | Giao dịch / nạp / thanh toán | **MAU + % New to services** | ePass PG, nộp phạt in-app |

**Chiến lược triển khai:** Kế thừa pilot Phạt Nguội (test → amplify). Không all-in DVC content trước Pilot review T6/2026. Roadmap điều chỉnh theo kết quả pilot.

---

## 4. Search Intent & URL Strategy

### 4.1 Head Terms (Volume 500K+/tháng)

| Keyword | Volume | Intent | Target URL |
|---|---|---|---|
| dịch vụ công online | 60,000 | TOFU | /dich-vu-cong |
| Keywords Phạt Nguội | ~2,536,090 | TOFU/MOFU | Chi tiết tại BRD Phạt Nguội |

### 4.2 High-Volume Clusters Chiến Lược (50K-500K/tháng)

| Cluster | Volume | Intent | Target URL |
|---|---|---|---|
| Đổi GPLX | 230,810 | BOFU | /dich-vu-cong/doi-bang-lai-xe |
| Hộ chiếu | 222,610 | BOFU | /dich-vu-cong/ho-chieu |
| Tạm trú | 154,540 | BOFU | /dich-vu-cong/tam-tru |
| CCCD | 145,690 | BOFU | /dich-vu-cong/gia-han-cccd |
| Đăng ký kết hôn | 89,420 | BOFU | /dich-vu-cong/ket-hon |
| Đăng kiểm xe | 76,870 | BOFU | /dich-vu-cong/dang-kiem |
| Quyết toán thuế | 50,570 | BOFU | /dich-vu-cong/nop-thue |
| Khai sinh | 44,490 | BOFU | /dich-vu-cong/khai-sinh |
| Định danh điện tử | 29,170 | TOFU | /dich-vu-cong/vneid-la-gi |
| Chứng thực | 27,670 | BOFU | /dich-vu-cong/chung-thuc |

---

## 5. JTBD Analysis

### Job #1: Tra cứu & Xử lý Vi phạm Giao thông (Phạt Nguội)

> Nhu cầu tra cứu vi phạm giao thông và nộp phạt trực tuyến nhanh chóng, bảo mật.
>
> *Job này được phân tích chi tiết tại BRD Phạt Nguội.*

### Job #2: Hoàn thành Thủ tục Hành chính Online

> "Tôi cần biết thủ tục [X] cần những gì, nộp ở đâu, mất bao lâu - và nộp phí/lệ phí online cho nhanh."

| Dimension | Nội dung |
|---|---|
| Functional | Biết checklist giấy tờ, quy trình từng bước, nơi nộp hồ sơ, thời gian xử lý, cách nộp phí online |
| Emotional | Sợ thiếu giấy tờ phải đi lại nhiều lần, muốn tiết kiệm thời gian |
| Social | Thủ tục cho sự kiện cuộc đời quan trọng (sinh con, kết hôn, mua nhà) - áp lực phải làm đúng |
| Trigger | Con mới sinh cần khai sinh, bằng lái sắp hết hạn, CCCD hết hạn/bị mất, sắp kết hôn |
| Search → App | "thủ tục đổi GPLX" → Service page → Checklist → CTA nộp phí → App MoMo |

### Job #3: Quản lý Nghĩa vụ Tài chính Cá nhân (Thuế, BHXH)

> "Tôi cần biết deadline, cách tính, và nộp thuế/BHXH online - không muốn bị phạt chậm nộp."

| Dimension | Nội dung |
|---|---|
| Functional | Tính thuế phải nộp, biết deadline, nộp tiền online, gia hạn BHYT |
| Emotional | Sợ bị phạt chậm nộp, bối rối với quy định phức tạp |
| Social | Nghĩa vụ pháp lý - không thể trì hoãn |
| Trigger | Mùa quyết toán thuế (T3-T4), BHYT sắp hết hạn, nhận thông báo thuế |
| Search → App | "nộp thuế TNCN online" → Calculator → CTA nộp → App MoMo |

### Job #4: Khám phá Toàn bộ DVC MoMo Hỗ trợ

> "MoMo làm được những dịch vụ công gì? Tôi muốn biết để dùng luôn thay vì ra UBND."

| Dimension | Nội dung |
|---|---|
| Functional | Tìm toàn bộ DVC MoMo hỗ trợ |
| Emotional | Tò mò, muốn tiết kiệm thời gian, trust vào Super App quen thuộc |
| Trigger | Lần đầu biết MoMo có DVC, đang cần 1 DVC cụ thể và muốn xem có gì thêm |
| Search → App | Hub /dich-vu-cong → Browse → Click service cần → App MoMo |

---

## 6. Kiến Trúc Web

### 6.1. URL Architecture

| Cluster | URL | Ghi chú |
|---|---|---|
| **Core Hubs** | `/dich-vu-cong` | Governance Hub |
| | `/thu-tuc-hanh-chinh` | TTHC Hub |
| **Phạt Nguội** | `/phat-nguoi` | Tool & Landing Page chính (BRD riêng) |
| **Giấy tờ tùy thân** | `/dich-vu-cong/gia-han-cccd` | CCCD |
| | `/dich-vu-cong/ho-chieu` | Hộ chiếu |
| **Cư trú** | `/dich-vu-cong/tam-tru` | Tạm trú |
| | `/dich-vu-cong/tam-vang` | Tạm vắng |
| **Hộ tịch** | `/dich-vu-cong/ket-hon` | Đăng ký kết hôn |
| | `/dich-vu-cong/khai-sinh` | Đăng ký khai sinh |
| **Giấy tờ xe** | `/dich-vu-cong/doi-bang-lai-xe` | Đổi GPLX |
| **Thuế** | `/dich-vu-cong/nop-thue` | Thuế TNCN / Quyết toán |
| **Chứng thực** | `/dich-vu-cong/chung-thuc` | Chứng thực / Sao y |
| **Kinh doanh** | `/dich-vu-cong/dang-ky-kinh-doanh` | Hộ kinh doanh |
| **Đất đai** | `/dich-vu-cong/dat-dai` | Sang tên, chuyển nhượng |
| **Knowledge Base** | `/dich-vu-cong/faq` | FAQ Schema Hub |
| | `/dich-vu-cong/vneid-la-gi` | Định danh điện tử / VNeID |

### 6.2. Governance Hub Anatomy (`/dich-vu-cong`)

| Section | Thành phần | Ghi chú |
|---|---|---|
| Hero | Search bar auto-suggest + "Mọi dịch vụ công trong 1 ứng dụng" + trust counter | LCP < 2.5s |
| Quick Actions | 6 icon dịch vụ phổ biến nhất (Phạt nguội, Đổi bằng lái, CCCD, Thuế, BHXH, Khai sinh) | Personalize nếu logged in |
| Service Grid | Map 8 dịch vụ BU: 3 kênh chiến lược nổi bật + các mảng cân nhắc | Schema: Service + ItemList |
| App CTA | Sticky bottom banner + QR + deep link | Firebase Dynamic Links |
| Blog Preview | 3 bài mới nhất | NewsArticle Schema |
| Social Proof | Counter lượt dùng + Rating App Store | AggregateRating Schema |

---

## 7. Success Metrics

**North Star:** **MEU Utility (Web)** + **MAU % New to services (App)** - hai metric này cam kết với BU + Web Platform. Organic sessions & W2A là Tier B (leading indicators).

| Metric | Lane | Target | Tracking |
|--------|------|--------|----------|
| MEU Utility | Utility | TBD post Pilot T6/2026 | DA + Appsflyer |
| MAU % New to services | Payment | TBD | BU internal / Onelink |
| Organic sessions EOY | Tier B | 500K/tháng | GSC → GA4 |
| Top 5 keywords DVC | Tier B | 20 keywords | Ahrefs |
| W2A end-to-end | Tier B | 15% | GA4 + Appsflyer |

---

## 8. Dependencies & Constraints

| Dependency | Mô tả | Blocker? | Status |
|---|---|---|---|
| Web Platform (MoSpark) | Build & deploy toàn bộ web pages | Có | READY (v2 Live) |
| GenAI Content Engine | Hệ thống sản xuất blog | Có | LIVE (Claude API) |
| Widget tra cứu phạt nguội | API tra cứu biển số (TTDK integration) | Có | LIVE (BRD Phạt Nguội) |
| Analytics Stack | Real-time traffic & attribution | Không | LIVE (Umami + GA4) |
| Onelink/Appsflyer setup | Config deeplink cho từng DVC page | Có | ACTIVE |
| SEM Campaign | SEM cho Phạt Nguội | Không | RUNNING |

**Hard blockers (3):** Web Platform, Widget tra cứu, Onelink setup. Thiếu 1 trong 3 - không launch được.

### 8.1. Service Readiness (T5/2026)

| Dịch vụ | Status | Ghi chú |
|---|---|---|
| **Phạt Nguội** | **LIVE** | Triển khai độc lập (BRD riêng) |
| **Thủ tục Hành chính (TTHC)** | **IN PROGRESS** | Đang scale content |

---

## Appendix: Glossary

| Thuật ngữ | Định nghĩa |
|---|---|
| DVC | Dịch vụ công |
| DVCQG | Cổng Dịch vụ công Quốc gia (dichvucong.gov.vn) |
| TTHC | Thủ tục hành chính |
| NĐ 168 | Nghị định 168/2024/NĐ-CP về xử phạt vi phạm giao thông |
| W2A | Web-to-App (conversion từ web visitor sang app user) |
| MEU | Monthly Engagement User - tương tác Utility; metric commit Web Utility |
| Utility lane | Đo bằng MEU - engagement công cụ/info |
| Payment lane | Đo bằng MAU, % New to services - giao dịch in-app |
| Governance Hub | Trang trung tâm tập hợp & điều hướng portfolio DVC |
| ePass | Trạm thu phí - liên kết Payment Gateway MoMo (1 User ↔ 1 PG) |
| YMYL | Your Money Your Life - tiêu chuẩn Google cho content tài chính/pháp luật |
| MoSpark | Web platform nội bộ MoMo |
| VNeID | Ứng dụng định danh điện tử quốc gia |

---

## Change Log

- **Tháng 5/2026 (v2.5):** Xóa BHYT và BHXH khỏi Search Market, URL Architecture, Service Readiness - đã có BRD riêng (bhyt-brd.md, bhxm-brd.md).
- **Tháng 5/2026 (v2.4):** Rewrite theo chuẩn BRD - xóa Risk Assessment, Content Matrix, Appendix Cross-sell, Data Verification; trim keyword detail về Tier 1+2 only; thêm Problem Statement block + Product Job Cốt Lõi; rewrite Executive Summary theo Problem Framing.
- **Tháng 5/2026 (v2.3):** Chuẩn hóa tài liệu - loại bỏ liên kết nội bộ, thông tin vận hành, tên nhân sự.
- **Tháng 5/2026 (v2.2):** Portfolio 8 dịch vụ BU; 3 kênh Web chiến lược; ePass Build Foundation; KPI Utility (MEU) vs Payment (MAU).
- **Tháng 5/2026 (v2.1):** Tách biệt Phạt Nguội sang BRD riêng.
- **Tháng 5/2026:** Khởi tạo tài liệu.
