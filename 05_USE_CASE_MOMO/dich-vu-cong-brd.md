# BRD: Dịch Vụ Công MoMo - Web Growth & Content Architecture

> - **Project:** Dịch Vụ Công MoMo (DVC) - Hướng Dẫn → Thanh Toán
> - **Main URL:** `momo.vn/dich-vu-cong` (Governance Hub) + 2 sản phẩm con
> - **Owner:** Văn Hiến (SEO & GEO Lead) | Project Lead: Bảo (Web Platform)
> - **Timeline:** Q1 2026 → Q4 2026
> - **Version:** 2.1 · Tháng 5/2026
> - **Status:** **DVC Chung** (Chưa triển khai/xúc tiến trên Website) | **Phạt Nguội** (Đã tách thành dự án riêng tại Phạt Nguội BRD)
>



---

## 1. Executive Summary

### Situation

Cổng Dịch vụ công Quốc gia (DVCQG) ghi nhận **15.7 triệu giao dịch** với tổng giá trị **10.4 nghìn tỷ VNĐ** trong 10 tháng đầu năm 2025 (năm trước). MoMo hiện chiếm **11.2% market share** (đứng thứ 3).

Thị trường tìm kiếm cực lớn: Research mới nhất (Tháng 5/2026) cho thấy cluster **Phạt Nguội** đơn lẻ đã đạt **~3.6 triệu searches/tháng**. Tổng volume toàn bộ mảng DVC (thủ tục hành chính, thuế, BHXH, hộ tịch...) vượt mức **5 triệu searches/tháng**. MoMo xác định đây là phễu traffic (Top of Funnel) khổng lồ để thúc đẩy tăng trưởng User mới (Acquisition) và MAU/MEU.

### Complication

MoMo hiện **không có bất kỳ trang web nào** phục vụ hành trình người dùng dịch vụ công - từ hướng dẫn thủ tục đến thanh toán phí/lệ phí. Toàn bộ organic traffic từ search engines cho segment DVC = **zero**. Điều này có nghĩa:

- **Mất hoàn toàn kênh acquisition organic** cho một trong những use case có demand cao nhất (15.7M giao dịch/năm trên DVCQG, 1.3M searches/tháng trên Google).
- **Không có touchpoint web** để educate user rằng MoMo hỗ trợ thanh toán DVC - user chỉ biết nếu đã có app hoặc tình cờ thấy trên Cổng DVCQG.
- **Đối thủ đang chiếm toàn bộ SERP**: VNExpress, Luatvietnam, các trang blog cá nhân thống trị top 10 cho hầu hết keywords DVC. Không đối thủ fintech nào có chiến lược web DVC nghiêm túc - đây là cửa sổ cơ hội.
- **Không có W2A funnel**: Không web → không deeplink → không convert organic traffic thành app user.

### Resolution

Dự án "Dịch Vụ Công MoMo" sẽ build **hệ thống web 30+ trang** bao phủ toàn bộ hành trình từ **Hướng dẫn → Thanh toán**, gồm:

1. **Governance Hub** (`/dich-vu-cong`) - trang trung tâm tập hợp tất cả DVC MoMo hỗ trợ
2. **Sản phẩm 1: Phạt Nguội** (`/phat-nguoi`) - Tra cứu & nộp phạt vi phạm giao thông (Một phần của hệ sinh thái DVC, được quản lý độc lập tại Phạt Nguội BRD).
3. **Sản phẩm 2: Dịch Vụ Công Online** (`/thu-tuc-hanh-chinh`) - Thủ tục hành chính phổ biến nhất

North Star: **500K organic visits/tháng** + **15% Web-to-App activation rate** cuối năm 2026.

---

## 2. Bối Cảnh Hiện Tại

### 2.1. Thị trường Dịch Vụ Công Số Việt Nam (Data từ Cổng DVCQG)

| Metric | Giá trị | Nguồn |
|---|---|---|
| Tổng giao dịch DVCQG (10 tháng năm trước) | 15,725,239 | File Cổng DVCQG Overview |
| Tổng giá trị giao dịch | ~10.4 nghìn tỷ VNĐ | File Cổng DVCQG Overview |
| Số loại TTHC thanh toán qua Cổng | 1,900+ | File Cổng DVCQG Overview |
| MoMo tổng giao dịch | ~1,462,714 (11.2% share) | Tính từ Chi tiết TTHC |
| MoMo đã triển khai (theo qty txns) | 98.55% | File Cổng DVCQG Overview |

### 2.2. Phân bổ giao dịch theo loại thanh toán

| Loại thanh toán | Qty giao dịch | Tỉ trọng | MoMo đã triển khai |
|---|---|---|---|
| Thu phí/Lệ phí | 13,037,270 | 82.9% | Có |
| Thu phạt | 2,010,384 | 12.8% | Có |
| Thu thuế đất | 388,106 | 2.5% | Có |
| Thu thuế Lệ phí trước bạ | 221,392 | 1.4% | Chưa |
| Thanh toán BHXH/BHYT | 61,148 | 0.4% | Có |
| Thanh toán án phí | 5,116 | 0.03% | Chưa |
| Thu thuế cá nhân | 1,689 | 0.01% | Chưa |

### 2.3. Top 10 TTHC có lượng giao dịch cao nhất (chiếm 75.92%)

| TTHC | Qty giao dịch | GD TB/tháng | MoMo txns | MoMo share |
|---|---|---|---|---|
| Chứng thực bản sao từ bản chính | 4,442,917 | 444,292 | 423,413 | 9.5% |
| Chứng thực chữ ký | 1,250,910 | 125,091 | 99,580 | 8.0% |
| Đăng ký xét tuyển ĐH/CĐ | 820,722 | 82,072 | 319,932 | 39.0% |
| Cấp bản sao trích lục hộ tịch | 614,176 | 61,418 | 59,132 | 9.6% |
| Cấp bản sao khai sinh | 589,385 | 58,939 | 46,608 | 7.9% |
| Cấp giấy xác nhận tình trạng hôn nhân | 508,062 | 50,806 | 59,656 | 11.7% |
| Chứng thực bản sao (VN cấp) | 469,455 | 46,946 | 54,910 | 11.7% |
| Chứng thực hợp đồng/giao dịch đất đai | 443,126 | 44,313 | 34,783 | 7.8% |
| Đổi giấy phép lái xe | 400,937 | 40,094 | 100,237 | 25.0% |
| Thu nộp đảng phí | 358,347 | 35,835 | 21,099 | 5.9% |

### 2.4. Competitive Landscape - Đơn vị thanh toán trên DVCQG

| Đơn vị | Vị thế | Ghi chú |
|---|---|---|
| VNPT Pay | #1 volume | Chiếm ưu thế ở các TTHC chứng thực, hộ tịch |
| NAPAS | #2 volume | Mạnh ở đất đai, doanh nghiệp |
| **MoMo** | **#3 volume (~11.2%)** | Dẫn đầu ở Xét tuyển ĐH (39%), Đổi GPLX (25%) |
| AgriBank | #4 | Mạnh ở vùng nông thôn, đất đai |
| ViettelPay | #5 | Phủ rộng nhưng share thấp |

### 2.5. Search Market - Keyword Universe (Cập nhật T5/2026)

| Cluster | Volume/tháng | Focus Keywords |
|---|---|---|
| **Phạt Nguội (Core)** | **2,536,090** | tra cứu phạt nguội, kiểm tra phạt nguội |
| **Phương Tiện (Giao thông)** | **510,910** | tra cứu biển số xe, đăng ký xe |
| **Đăng Kiểm Xe** | **76,870** | thủ tục đăng kiểm, đăng kiểm xe online |
| **Thủ tục hành chính (general)** | 102,640 | dịch vụ công online, thủ tục ly hôn |
| **Bảo hiểm (BHXH, BHYT)** | 938,090 | gia hạn BHYT, đóng BHXH tự nguyện |
| **Thuế TNCN** | 17,220 | quyết toán thuế tncn |
| **Xét tuyển ĐH/CĐ** | [TBD] | nộp lệ phí xét tuyển, thanh toán lệ phí xét tuyển |
| **Chứng thực / Sao y** | [TBD] | chứng thực điện tử, sao y bản chính online |
| **Đất đai** | [TBD] | nộp thuế đất online, thủ tục sang tên sổ đỏ |
| **Hộ tịch (Kết hôn/Khai sinh)**| [TBD] | đăng ký kết hôn online, làm giấy khai sinh online |
| **Căn cước công dân (CCCD)** | [TBD] | đổi cccd online, làm lại cccd bị mất |
| **Hộ chiếu** | [TBD] | làm hộ chiếu online, gia hạn hộ chiếu online |
| **Đăng ký kinh doanh** | [TBD] | đăng ký hộ kinh doanh online, tra cứu mã số thuế |
| **Tổng addressable market** | **~5,000,000+** | |

**Lưu ý:** Chi tiết về chiến dịch, keyword cluster, và ngân sách SEM cho Phạt Nguội được tối ưu hóa riêng biệt tại Phạt Nguội BRD.

### 2.6. Hiện trạng MoMo Web cho DVC (Status: Active)

| Dimension | Status | Update |
|---|---|---|
| Landing pages DVC | Active | Governance Hub + Phạt Nguội Tool live |
| GenAI Pipeline | Live | Sản xuất 100% Blog qua MoSpark v2 |
| Tracking | Live | Umami (Real-time) + GA4 + Appsflyer |
| SEM Budget | 200M/mo | Focus Phạt Nguội cluster |
| AI Readiness | In Progress | Deployed llms.txt (pilot Phạt Nguội) |

---

## 3. Định Hướng Dự Án

### Dự án này phục vụ điều gì?
**Acquisition + Activation**: Thuút user mới từ organic search cho segment Dịch Vụ Công, giáo dục họ về khả năng thanh toán DVC qua MoMo, và convert sang app user.

**Đặc thù Phạt Nguội:** Được định vị là phễu Acquisition & Governance quan trọng. Do có quy mô và tính chất đặc thù, dự án Phạt Nguội đã được tách riêng để theo dõi và tối ưu chuyên sâu (Xem chi tiết tại Phạt Nguội BRD).

### Ai được phục vụ?

| User Segment | Nhu cầu chính | Volume indicator |
|---|---|---|
| Người vi phạm giao thông | Tra cứu & đóng phạt nguội | 200K+ searches/tháng (head terms) |
| Công dân cần thủ tục hành chính | Hướng dẫn + thanh toán lệ phí (CCCD, bằng lái, khai sinh, kết hôn...) | 100K+ searches/tháng |
| Người đóng thuế TNCN | Hướng dẫn quyết toán + nộp thuế online | 17K searches/tháng, seasonal peak T3-T4 |
| Người tham gia BHXH/BHYT | Gia hạn BHYT, tra cứu, đóng BHXH tự nguyện | 35K searches/tháng |
| Chủ hộ kinh doanh | Đăng ký, thay đổi nội dung đăng ký HKD | 15K searches/tháng |

### Dự án này KHÔNG phải là gì?

- **KHÔNG build app features mới** - dự án focus vào web landing pages & content. App features do PO Cell/Mobile team own.
- **KHÔNG thay thế Cổng DVCQG** - MoMo web chỉ hướng dẫn + thanh toán, không xử lý hồ sơ TTHC.
- **KHÔNG cover toàn bộ 1,900+ loại TTHC** - focus vào top 10-15 TTHC có volume cao nhất + search demand lớn nhất.

### Chiến lược Phát triển Dịch Vụ Công MoMo
Chiến lược tổng thể cho DVC MoMo sẽ kế thừa mô hình tăng trưởng từ pilot Phạt Nguội, đồng thời mở rộng ra các mảng dịch vụ công trực tuyến khác. 

*(Chi tiết lộ trình 3 giai đoạn của Phạt Nguội xem tại Phạt Nguội BRD)*

---

## 4. Search Intent Analysis & Keyword Strategy

### 4.1. Intent Tiers & URL Mapping

#### Tier 1: Head Terms (Volume 500K+/tháng)

| Keyword | Volume | Intent | Target URL | Priority |
|---|---|---|---|---|
| **dịch vụ công online** | 60,000 | TOFU | /dich-vu-cong | P1 |
| *Keywords Phạt Nguội* | *~3.56M* | *TOFU/MOFU* | */phat-nguoi* | *Chi tiết tại Phạt Nguội BRD* |

#### Tier 2: High-Volume Clusters (50K-500K/tháng)

| Keyword | Volume | Intent | Target URL | Priority |
|---|---|---|---|---|
| thủ tục đăng kiểm xe | **76,870** | BOFU | /dich-vu-cong/dang-kiem | P1 |
| gia hạn bằng lái xe online | 28,000 | BOFU | /dich-vu-cong/doi-bang-lai-xe | P1 |
| đổi cccd online | 24,000 | BOFU | /dich-vu-cong/gia-han-cccd | P1 |
| nộp thuế TNCN online | 20,000 | BOFU | /dich-vu-cong/nop-thue | P1 |
| đăng ký khai sinh online | 15,000 | BOFU | /dich-vu-cong/khai-sinh | P1 |
| *Keywords Phạt Nguội khác* | *Volume cao* | *MOFU/BOFU* | */phat-nguoi/* | *Chi tiết tại Phạt Nguội BRD* |

#### Tier 3: DVC Keywords từ CSV Research (Volume 1K-10K)

| Cluster | Keywords tiêu biểu | Volume range | Target Pages |
|---|---|---|---|
| Thủ tục đổi GPLX | thủ tục đổi giấy phép lái xe a1 online (5.4K), thủ tục đổi bằng lái xe ô tô (1.9K) | 1K-5.4K | /dich-vu-cong/doi-bang-lai-xe |
| Cấp lại CCCD | xin cấp lại CCCD online (9.9K), cấp lại CCCD bị mất (1.6K) | 1K-9.9K | /dich-vu-cong/gia-han-cccd |
| BHXH/BHYT | gia hạn BHYT online (5.4K), cách gia hạn BHYT trên VNeID (2.4K), cách gia hạn BHYT trên VssID (1.9K) | 1K-5.4K | /dich-vu-cong/bao-hiem |
| Đăng ký kết hôn | thủ tục đăng ký kết hôn (6.6K), đăng ký kết hôn online (1.6K) | 1K-6.6K | /dich-vu-cong/ket-hon |
| Đăng ký kinh doanh | đăng ký hộ kinh doanh (14.8K), đăng ký hộ kinh doanh online (6.6K) | 1K-14.8K | /dich-vu-cong/dang-ky-kinh-doanh |
| Khai sinh | thủ tục làm giấy khai sinh (2.4K), thủ tục làm giấy khai sinh online (1.9K) | 1K-2.4K | /dich-vu-cong/khai-sinh |
| Chứng thực | chứng thực điện tử (1.9K), chứng thực chữ ký (720) | 500-1.9K | /dich-vu-cong (Hub) |
| Nộp lệ phí online | nộp lệ phí trước bạ xe máy online (1.6K), nộp lệ phí trước bạ online (1.3K) | 500-1.6K | /dich-vu-cong/nop-thue |
| Hộ chiếu | thủ tục làm hộ chiếu (2.4K), thủ tục làm hộ chiếu online (1.9K), gia hạn hộ chiếu online (1.6K) | 1K-2.4K | /dich-vu-cong (Hub) |
| Đất đai | thủ tục sang tên sổ đỏ (2.9K), thủ tục chuyển nhượng QSDĐ (880) | 500-2.9K | /dich-vu-cong/dat-dai (P3) |

#### Tier 4: Long-tail Keywords (<1K/tháng, 2,790 keywords)

Tổng volume: ~214K/tháng. Serve bằng FAQ sections + blog content. Pattern chính: "cách làm thủ tục [X]", "hướng dẫn [X] online", "[X] cần giấy tờ gì", "[X] mất bao lâu".

---

## 5. JTBD Analysis (Keyword-Driven)

### Job #1: Tra cứu & Xử lý Vi phạm Giao thông (Phạt Nguội)

> Nhu cầu tra cứu vi phạm giao thông và nộp phạt trực tuyến nhanh chóng, bảo mật.
> 
> *Lưu ý: Job này được phân tích chi tiết và phục vụ chuyên biệt trong dự án độc lập Phạt Nguội BRD.*

### Job #2: Hoàn thành Thủ tục Hành chính Online

**Search Intent Cluster:** "thủ tục đổi giấy phép lái xe", "gia hạn cccd online", "thủ tục đăng ký kết hôn", "thủ tục làm giấy khai sinh online"
**Volume:** ~100K searches/tháng (combined TTHC clusters)

> "Tôi cần biết thủ tục [X] cần những gì, nộp ở đâu, mất bao lâu - và nộp phí/lệ phí online cho nhanh."

| Dimension | Nội dung |
|---|---|
| **Functional** | Biết checklist giấy tờ cần thiết, quy trình từng bước, nơi nộp hồ sơ, thời gian xử lý, cách nộp phí online |
| **Emotional** | Sợ thiếu giấy tờ phải đi lại nhiều lần, lo lắng quy trình phức tạp, muốn tiết kiệm thời gian |
| **Social** | Thủ tục cho các sự kiện cuộc đời quan trọng (sinh con, kết hôn, mua nhà) - áp lực phải làm đúng |
| **Trigger** | Con mới sinh cần khai sinh, bằng lái sắp hết hạn, CCCD hết hạn/bị mất, sắp kết hôn, mở hộ kinh doanh |

**Serve bằng:**
- Content: Service pages theo loại TTHC (`/dich-vu-cong/doi-bang-lai-xe`, `/dich-vu-cong/gia-han-cccd`...)
- Product: Checklist PDF download, calculator (thuế TNCN), CTA nộp lệ phí qua MoMo
- User flow: Hướng dẫn thủ tục → CTA nộp phí/lệ phí → Deep link app MoMo

### Job #3: Quản lý Nghĩa vụ Tài chính Cá nhân (Thuế, BHXH)

**Search Intent Cluster:** "nộp thuế TNCN online", "quyết toán thuế 2026", "gia hạn BHYT online", "đóng BHXH tự nguyện"
**Volume:** ~52K searches/tháng (Thuế 17K + BHXH/BHYT 35K)

> "Tôi cần biết deadline, cách tính, và nộp thuế/BHXH online - không muốn bị phạt chậm nộp."

| Dimension | Nội dung |
|---|---|
| **Functional** | Tính thuế phải nộp, biết deadline, nộp tiền online, gia hạn BHYT |
| **Emotional** | Sợ bị phạt chậm nộp, bối rối với quy định phức tạp, muốn xong nhanh |
| **Social** | Nghĩa vụ pháp lý - không thể trì hoãn |
| **Trigger** | Mùa quyết toán thuế (T3-T4), BHYT sắp hết hạn, nhận thông báo thuế |

**Serve bằng:**
- Content: `/dich-vu-cong/nop-thue` (calculator + calendar deadline), `/dich-vu-cong/bao-hiem`
- Product: Calculator thuế TNCN, CTA nộp thuế/BHXH qua MoMo
- User flow: Tính toán → CTA nộp → Deep link app MoMo

### Job #4: Khám phá Toàn bộ DVC MoMo Hỗ trợ

**Search Intent Cluster:** "dịch vụ công online", "momo dịch vụ công", "momo hỗ trợ dịch vụ công gì"
**Volume:** ~60K searches/tháng (head term)

> "MoMo làm được những dịch vụ công gì? Tôi muốn biết để dùng luôn thay vì ra UBND."

| Dimension | Nội dung |
|---|---|
| **Functional** | Tìm toàn bộ DVC MoMo hỗ trợ, so sánh với cách làm truyền thống |
| **Emotional** | Tò mò, muốn tiết kiệm thời gian, trust vào Super App quen thuộc |
| **Social** | Recommend cho người thân cũng dùng |
| **Trigger** | Lần đầu biết MoMo có DVC, đang cần 1 DVC cụ thể và muốn xem có gì thêm |

**Serve bằng:**
- Content: Governance Hub `/dich-vu-cong` với 8 nhóm dịch vụ
- Product: Search bar thông minh, service grid, cross-sell widgets
- User flow: Hub → Browse services → Click service cần → Deep link app

---

## 6. Kiến Trúc & Scope Build

### 6.1. URL Architecture (Clustered Model)

| Cluster | URL | Content Type | Priority |
|---|---|---|---|
| **Core Hubs** | `/dich-vu-cong` | Governance Hub (Main entry) | P1 |
| | `/thu-tuc-hanh-chinh` | TTHC Hub (Knowledge entry) | P1 |
| **Phạt Nguội (P0)** | `/phat-nguoi` | Tool & Landing Page chính (Chi tiết sub-pages xem tại Phạt Nguội BRD) | **P0** |
| **TTHC (P1)** | `/dich-vu-cong/doi-bang-lai-xe` | Service Page (GPLX) | P1 |
| | `/dich-vu-cong/gia-han-cccd` | Service Page (CCCD) | P1 |
| | `/dich-vu-cong/khai-sinh` | Service Page (Khai sinh) | P1 |
| | `/dich-vu-cong/dang-ky-kinh-doanh` | Service Page (Hộ kinh doanh) | P2 |
| **Bảo hiểm & Thuế** | `/dich-vu-cong/bao-hiem-xa-hoi` | Service Page (BHXH) | P1 |
| | `/dich-vu-cong/bao-hiem-y-te` | Service Page (BHYT) | P1 |
| | `/dich-vu-cong/nop-thue` | Tool + Guide (Thuế TNCN) | P1 |
| **Knowledge Base** | `/dich-vu-cong/faq` | FAQ Schema Hub | P2 |
| | `/dich-vu-cong/vneid-la-gi` | UX Guide (VNeID integration) | P2 |

### 6.2. Content Matrix

| Funnel Stage | Content Type | Pages | Serving Jobs | SEO Intent |
|---|---|---|---|---|
| TOFU | Blog pháp luật GT, hướng dẫn DVC, FAQ | 5+ | Job #1, #2, #4 | Know |
| MOFU | Bảng mức phạt, so sánh, tra cứu, sub-pages loại xe | 6+ | Job #1, #2 | Do |
| BOFU | Service pages theo TTHC, đóng phạt, nộp thuế | 10+ | Job #1, #2, #3 | Buy |
| CONVERT | CTA deep link app, calculator tools, thanh toán | Embedded | All Jobs | Go |

### 6.3. Governance Hub Anatomy (`/dich-vu-cong`)

| Section | Thành phần | Ghi chú |
|---|---|---|
| Hero | Search bar auto-suggest + "Mọi dịch vụ công trong 1 ứng dụng" + trust counter | LCP < 2.5s |
| Quick Actions | 6 icon dịch vụ phổ biến nhất (Phạt nguội, Đổi bằng lái, CCCD, Thuế, BHXH, Khai sinh) | Personalize nếu logged in |
| Service Grid | 8 nhóm dịch vụ: Phạt nguội, TTHC, Tiện ích, Y tế/BH, Đất đai, Hộ tịch, Kinh doanh, Khác | Schema: Service + ItemList |
| App CTA | Sticky bottom banner + QR + deep link | Firebase Dynamic Links |
| Blog Preview | 3 bài mới nhất | NewsArticle Schema |
| Social Proof | Counter lượt dùng + Rating App Store | AggregateRating Schema |

---

## 7. Success Metrics (Keyword-Powered)

### 7.1. Organic Traffic (via GSC)

| Metric | Baseline | Q2 2026 | Q4 2026 | EOY Target | Tracking |
|---|---|---|---|---|---|
| Organic sessions - Phạt Nguội cluster | 0 | 50K/tháng | 200K/tháng | 300K/tháng | GSC → GA4 |
| Organic sessions - DVC cluster | 0 | 30K/tháng | 100K/tháng | 200K/tháng | GSC → GA4 |
| Total organic sessions | 0 | 80K/tháng | 300K/tháng | **500K/tháng** | GSC → GA4 |

**Target logic:** Phạt Nguội cluster (~3.56M searches/tháng) + DVC clusters (~1.5M searches/tháng). Target **500K sessions/tháng** tương đương ~10% CTR trên tổng addressable search volume sau 12 tháng. Đây là con số khả thi dựa trên benchmark của các fintech leading global (Wise, Revolut) khi chiếm lĩnh các cụm từ khóa Utility. *(Lưu ý: Chỉ số và tracking chi tiết của cụm Phạt Nguội được quản lý đồng bộ tại Phạt Nguội BRD).*

### 7.2. Web2App Conversion Rate

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| Traffic → CTA click % | 0 | 25% | Q4 2026 | GA4: CTA click events |
| CTA click → App Install % | 0 | 30% | Q4 2026 | Appsflyer: onelink |
| Install → Register + KYC | 0 | 40% | Q4 2026 | Appsflyer |
| **W2A %CR (end-to-end)** | **0** | **15%** | **Q4 2026** | **GA4 + Appsflyer** |

**Target logic:** Benchmark W2A trong app fintech: 8-12%. Target 15% vì DVC user có intent rất cao (cần thanh toán ngay) + MoMo brand trust. Cần A/B test CTA placement & copy.

### 7.3. Ranking Keywords

| Metric | Baseline | Target | Timeframe | Tracking |
|---|---|---|---|---|
| Top 3 keywords - Phạt Nguội | 0 | *Theo dõi tại Phạt Nguội BRD* | Q3 2026 | Ahrefs |
| Top 5 keywords - DVC | 0 | 20 keywords | Q4 2026 | Ahrefs |
| Top 10 keywords (all DVC) | 0 | 50 keywords | Q4 2026 | Ahrefs |

#### North Star Metric: **Organic Sessions = 500K/tháng**

Lý do: Dự án start từ zero, volume growth là leading indicator. W2A rate và ranking là secondary metrics chứng minh quality.

---

## 8. Dependencies & Constraints

| Dependency | Owner | Mô tả | Blocker? | Status |
|---|---|---|---|---|
| **Web Platform (MoSpark)** | Bảo | Build & deploy toàn bộ web pages | Yes | **READY** (v2 Live) |
| **GenAI Content Engine** | Bảo + Hiến | Hệ thống sản xuất blog hỏa tốc | Yes | **LIVE** (Claude API) |
| **Widget tra cứu phạt nguội** | Hoài Anh | API tra cứu biển số (TTDK integration) | Yes | **LIVE (Chi tiết tại Phạt Nguội BRD)** |
| **Umami Tracking** | Thuận | Quản lý & triển khai real-time traffic | No | **LIVE** |
| **Onelink/Appsflyer setup** | Hiếu | Config deeplink cho từng DVC page | Yes | **ACTIVE** |
| **SEM Campaign** | Growth Team | SEM cho Phạt Nguội (Chi tiết tại Phạt Nguội BRD) | No | **RUNNING** |

### 8.1. Service Readiness Status (Cập nhật T5/2026)

| Dịch vụ | Status | Ghi chú |
|---|---|---|
| **Phạt Nguội** | **LIVE** | Triển khai độc lập (Chi tiết tại Phạt Nguội BRD) |
| **Bảo hiểm Y tế (BHYT)** | **ACTIVE** | Build/Optimize web hoàn tất |
| **Bảo hiểm Xã hội (BHXH)** | **SẮP RA MẮT** | Launch trong ~10 ngày (T5/2026) |
| **Bảo hiểm Ô tô** | **ACTIVE** | Target 200K traffic/năm |
| **Thủ tục Hành chính (TTHC)** | **PHASE 2** | Đang scale content |

**Hard blockers (3):** Web Platform, Widget tra cứu, Onelink setup. Không có 3 thứ này → không launch được.

---

## 9. Risk Assessment

| # | Rủi ro | Loại | Khả năng | Impact | Mitigation |
|---|---|---|---|---|---|
| 1 | Web Platform timeline delay | Execution | Cao | Cao | Buffer 1 tháng, weekly check-in với Web Platform team |
| 2 | Các Widget tiện ích DVC (tra cứu, tính toán) API không ready | Technical | Trung | Cao | Fallback: hướng dẫn thủ tục chi tiết trước, build widget sau |
| 3 | YMYL content inaccuracy (sai thông tin pháp luật) | Legal | Trung | Rất cao | Mandatory Legal review trước publish, cite nguồn chính thống, ghi rõ "tham khảo" |
| 4 | Search volume thực tế thấp hơn estimate | Market | Thấp | Trung | Validate bằng Ahrefs/SEMrush trước khi commit target, adjust quarterly |
| 5 | Competitor (VNExpress, gov sites) outrank | Market | Cao | Trung | Build topical authority nhanh, content depth + freshness advantage, schema markup |
| 6 | Onelink/Appsflyer tracking không hoàn chỉnh | Data | Trung | Cao | QA tracking trước launch, dual-stack GA4 + manual audit weekly |
| 7 | Content production chậm (Inbound/Agency bandwidth) | Execution | Trung | Trung | Phase rollout, P1 pages trước, P2/P3 theo capacity |
| 8 | Nghị định/luật thay đổi (NĐ 168 mới) | External | Thấp | Trung | Content update process: monitor + update trong 48h |
| 9 | MoSpark page speed chậm (LCP > 2.5s) | Technical | Trung | Cao | Lighthouse audit pre-launch, lazy load non-critical JS, WebP images |

---

## 10. Next Steps (30-Day Action Plan - T5/2026)

| # | Deliverable | Owner | Description | Target date |
|---|---|---|---|---|
| 1 | **Giai đoạn Launch** | Hiến + Inbound | Xuất bản 10 bài viết trọng điểm (Phương Tiện, Luật, Thủ tục hành chính) | Tuần 1 |
| 2 | **Schema & AEO** | Hiến | Gắn FAQ/HowTo schema cho các trang DVC chính | Tuần 1 |
| 3 | **Regional Scale** | Hùng + Inbound | Sản xuất 20-30 bài viết ngách cho các dịch vụ công ưu tiên | Tuần 2 |
| 4 | **SoV Tracking** | Thuận | Thiết lập dashboard Share of Voice cho các từ khóa DVC mục tiêu | Tuần 2 |
| 5 | **W2A Nudge** | Bảo + DA | Kích hoạt Balloon/Popup Ads trên các trang DVC có traffic | Tuần 3 |
| 6 | **Audit & Refresh** | Hiến | Dùng AI Enhance nâng cấp bài chưa lọt Top 10 | Tuần 4 |
| 7 | **Review Pilot** | Công + Hiến | Tổng kết hiệu quả Pilot Phạt Nguội (Tham chiếu từ Phạt Nguội BRD) để áp dụng cho DVC | Tuần 4 |

### 10.2. High-level Roadmap (Q3 - Q4 2026)

| Phase | Timeline | Focus | Key Deliverables |
|---|---|---|---|
| **Phase 2 (Scale)** | T5 - T7 | DVC Content Scaling | pSEO cho các DVC ưu tiên, scale blog content |
| **Phase 3 (Growth)** | T8 - T10 | TTHC Expansion | Calculator tools (Thuế, BHXH), Hub optimization |
| **Phase 4 (Trust)** | T11 - T12 | Authority & E-E-A-T | VNeID integration, Named authors, PR placements |

---

## Appendix A: Cross-sell Matrix (Tham khảo từ Strategy Doc)

| Touchpoint | Tiện ích Điện/Nước | BHXH/BHYT | Tài khoản MoMo | Pay Later |
|---|---|---|---|---|
| Trang Phạt Nguội | Banner "Đóng điện sau khi nộp phạt" | - | CTA tạo tài khoản | *(Chi tiết tại Phạt Nguội BRD)* |
| Sau Đóng Phạt | Post-purchase banner | Nhắc gia hạn BHYT | Nếu chưa đăng ký | - |
| DVC (CCCD/Bằng lái) | - | Banner BHYT liên kết CCCD | CTA kết nối VNeID + MoMo | - |
| Trang Nộp Thuế | - | Nhắc đóng BHXH tự nguyện | - | - |

---

## Appendix B: Data cần Verify

| Item | Hiện tại | Cần verify bằng | Responsible |
|---|---|---|---|
| Search volume Phạt Nguội | **VERIFIED: ~3.6M** | GSC / Ahrefs monthly audit | SEO Lead |
| MoMo exact transaction count per service | Tính từ DVCQG Overview file | MoMo internal data / BI team | DA Team |
| W2A benchmark ngành DVC | Target 15% | Appsflyer flow audit | Growth Team |
| Competitor ranking positions | **AUDITED (May 2026)** | Ahrefs monthly tracking | SEO Lead |
| MoSpark technical capabilities | **VERIFIED: v2 Ready** | MoSpark GenAI Pipeline docs | Web Platform |

---

## Appendix D: Chi tiết Lưu trữ Pilot Phạt Nguội (Từ v2.0)

> [!NOTE]
> Phần phụ lục này lưu trữ lại các chi tiết triển khai ban đầu của dự án Pilot Phạt Nguội từ phiên bản v2.0 trước khi tách hoàn toàn sang file dự án độc lập [[05_USE_CASE_MOMO/phat-nguoi-brd|Phạt Nguội BRD]]. 

### 1. Chiến lược 3 Giai đoạn của Pilot Phạt Nguội
1. **Phase 1 (Foundation):** Build Mini Web (`/phat-nguoi`, `/o-to`, `/xe-may`) + API TTDK Real-time + 20 Pillar Blogs. **[DONE]**
2. **Phase 2 (Scale):** Regional pSEO (63 tỉnh thành) + Scale blog + SEM 200M/mo (Dành riêng cho Phạt Nguội). **[IN PROGRESS]**
3. **Phase 3 (Growth):** Camera AI Map + Viral Share Loops + Safe Driver Rewards.

### 2. Chi tiết Keywords & Phân bổ URLs của Phạt Nguội
- **Từ khóa Head Terms (Volume 500K+/tháng):**
  - `tra cứu phạt nguội` (2,536,090 searches/tháng, TOFU, URL: `/phat-nguoi`, Priority: P0)
  - `phạt nguội` (Core cluster, TOFU, URL: `/phat-nguoi`, Priority: P0)
- **Từ khóa High-Volume Clusters (50K-500K/tháng):**
  - `kiểm tra phạt nguội xe máy` (510,910 searches/tháng, MOFU, URL: `/phat-nguoi/xe-may`, Priority: P0)
  - `mức phạt vi phạm giao thông 2026` (137,250 searches/tháng, TOFU, URL: `/phat-nguoi/muc-phat-2026`, Priority: P0)
  - `tra cứu phạt nguội theo tỉnh` (131,720 searches/tháng, MOFU, URL: `/phat-nguoi/[tỉnh-thành]`, Priority: P0)
  - `đóng phạt nguội online` (22,000 searches/tháng, BOFU, URL: `/phat-nguoi/dong-phat-online`, Priority: P0)
  - `nộp phạt giao thông qua momo` (12,000 searches/tháng, BOFU, URL: `/phat-nguoi/dong-phat-online`, Priority: P0 Brand)

### 3. Chi tiết Job-to-be-Done (JTBD) của Phạt Nguội
- **Job Statement:** *"Tôi cần kiểm tra nhanh xe tôi có bị phạt nguội không, và nộp phạt ngay nếu có - không muốn ra phường xếp hàng."* (Volume ~3,557,750 searches/tháng).
- **Phân tích Khía cạnh:**
  - **Functional:** Tra cứu vi phạm theo biển số xe, xem mức phạt cụ thể, nộp phạt online.
  - **Emotional:** Lo lắng bị phạt mà không biết, muốn giải quyết nhanh gọn, an tâm khi xử lý xong.
  - **Social:** Không muốn bị mất thời gian ra cơ quan công quyền, thể hiện am hiểu công nghệ.
  - **Trigger:** Nhận thông báo phạt nguội, sắp đăng kiểm/sang tên xe, nghe tin thay đổi luật giao thông (NĐ 168).
- **Quy trình phục vụ:**
  - *Content:* Landing `/phat-nguoi` + sub-pages xe máy, ô tô, bảng mức phạt.
  - *Product:* Widget tra cứu biển số (Dữ liệu chính thống từ TTDK) + CTA đóng phạt qua MoMo.
  - *User flow:* Tra cứu → Xem kết quả (Trust build) → CTA đăng ký thông báo real-time → Deep link app MoMo.

### 4. Chi tiết Kế hoạch hành động 30 ngày của Phạt Nguội (v2.0)
- **Giai đoạn Launch (Tuần 1):** Xuất bản 10 bài viết trọng điểm (Phạt Nguội, Phương Tiện, Luật) + Gắn FAQ/HowTo schema + deploy llms.txt.
- **Regional Scale (Tuần 2):** Sản xuất 20-30 bài viết ngách Tỉnh/Thành & Camera (pSEO) + Thiết lập dashboard Share of Voice cho 50 từ khóa mục tiêu.
- **W2A Nudge (Tuần 3):** Kích hoạt Balloon/Popup Ads trên 100+ URL Phạt Nguội.
- **Review Pilot (Tuần 4):** Tổng kết hiệu quả Pilot Phạt Nguội (Traffic, Indexing, W2A).

---

## Appendix C: Glossary

| Thuật ngữ | Định nghĩa |
|---|---|
| DVC | Dịch vụ công |
| DVCQG | Cổng Dịch vụ công Quốc gia (dichvucong.gov.vn) |
| TTHC | Thủ tục hành chính |
| NĐ 168 | Nghị định 168/2024/NĐ-CP về xử phạt vi phạm giao thông |
| W2A | Web-to-App (conversion từ web visitor sang app user) |
| Governance Hub | Trang trung tâm tập hợp & điều hướng toàn bộ DVC |
| YMYL | Your Money Your Life - tiêu chuẩn Google cho content tài chính/pháp luật |
| MoSpark | Web platform nội bộ MoMo |
| VNeID | Ứng dụng định danh điện tử quốc gia |

---

### 🔗 Reference & Alignment
- **Strategic Vision:** [[01_STRATEGIC_PLAN/web_growth_strategy_brd|Web Growth Strategy BRD]] & [[01_STRATEGIC_PLAN/web-momo-okrs-2026|Web OKRs 2026]]
- **Operational Direction:** [[01_STRATEGIC_PLAN/seo-geo-direction|SEO & GEO Direction]]
- **Content Playbook:** [[01_STRATEGIC_PLAN/momo-content-plan-strategy|Content Strategy Plan (Utility Layer)]]
- **Technical Platform:** [[04_MOSPARK_PLATFORM/mospark_master|MoSpark Master]] & [[04_MOSPARK_PLATFORM/mospark_genai_content|GenAI Content Engine]]
- **Execution Tracking:** [[04_MOSPARK_PLATFORM/mospark_seo_geo_playbook|SEO/GEO Playbook]]
- **Pilot Project:** [[05_USE_CASE_MOMO/phat-nguoi-brd|Phạt Nguội BRD]]
- **Related Use Cases:** [[05_USE_CASE_MOMO/bhyt-brd|Bảo hiểm Y tế BRD]] & [[05_USE_CASE_MOMO/bhxm-brd|Bảo hiểm Xe máy BRD]]


---

## Change Log
- **Tháng 5/2026:** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.
- **Tháng 5/2026 (v2.1):** Tách biệt và tối giản hóa các phần chi tiết của dự án Phạt Nguội sang file [[05_USE_CASE_MOMO/phat-nguoi-brd|Phạt Nguội BRD]], chỉ giữ lại định vị tổng quan trong mảng DVC chung. Đồng thời đồng bộ toàn bộ các liên kết tài liệu liên quan xuống cuối bài (Reference & Alignment).

