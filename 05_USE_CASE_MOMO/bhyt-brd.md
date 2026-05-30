# BRD: Bảo Hiểm Y Tế - Web Growth (SEO/GEO Project)

> - **Project:** BHYT Web Growth - MiniWeb Expansion + Blog Production
> - **Main URL:** momo.vn/bao-hiem-y-te
> - **Division:** FS (Financial Services - InsurTech)
> - **Use Case:** Bảo Hiểm Y Tế
> - **Owner:** GPD - Out-App Traffic
> - **Governance:** Web Product Lead
> - **Version:** 1.1 - Tháng 5/2026
> - **Status:** On Track

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
- **Vấn đề cốt lõi:** Người dân mua/gia hạn BHYT tự nguyện rất cực, phải ra phường hoặc đợi đại lý thu tiền. Các trang web hướng dẫn thì toàn văn bản luật khô khan, không cho phép thanh toán.
- **Giải pháp (The "What"):** Biến MoMo thành "Đại lý BHYT Online quốc dân". Cung cấp công cụ tra cứu số thẻ/ước tính mức đóng và nút thanh toán gia hạn trực tiếp ngay trên trang.

### 1.2 Situation
BHYT là vertical có tổng search market lớn nhất trong các vertical MoMo đang khai thác, với tổng search volume toàn category đạt trung bình ~525K searches/tháng (2024-2025). MoMo đang cung cấp dịch vụ mua và gia hạn BHYT tự nguyện online tại `momo.vn/bao-hiem-y-te`. Trang hiện tại có công cụ tra cứu, đóng phí 3-6-12 tháng.

### Complication

Hiệu suất organic hiện tại còn rất thấp so với tiềm năng thị trường. Traffic từ tháng 8/2025 chỉ ở mức ~10K views/tháng. Dự báo không can thiệp chỉ đạt ~72K views tổng cả năm 2026 - không tương xứng với thị trường 525K+ searches/tháng. Nguyên nhân cốt lõi:

1. MiniWeb thiếu các trang phủ intent cao nhất: tra cứu số thẻ bằng CCCD (~18,100/tháng), tra cứu mã số (~12,100/tháng), tra cứu thời hạn (~25,000/tháng) - đây là các cluster user đang tìm kiếm nhiều nhất nhưng MoMo không có trang đích.
2. Blog content chưa đủ volume để bao phủ market pool (hiện 14 bài vs thị trường ~525K searches).
3. Tracking organic vs paid chưa sạch nên không đo được hiệu quả thực sự.

### Resolution

Dự án 2026 triển khai 2 workstream song song: (1) MiniWeb Expansion - build 3 trang utility mới phủ intent tra cứu cao nhất, và (2) Blog Production Scale-Up - từ 14 bài lên 60-150 bài/năm để phủ 20-40% market pool.

- **Base case target:** 110,236 views toàn năm 2026 (tăng ~52% vs trajectory không can thiệp)
- **Best case target:** 452,294 views (nếu scale blog lên 120-150 bài/năm kèm backlink)

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Trang `momo.vn/bao-hiem-y-te`

| Yếu tố | Hiện trạng |
|--------|------------|
| Chức năng trang | Tra cứu BHYT + Mua/gia hạn BHYT tự nguyện online |
| Đối tác | Bảo hiểm PVI (được BHXH VN ủy quyền thu) |
| Thời hạn mua | 3 tháng / 6 tháng / 12 tháng |
| Điểm mạnh UX | 93% khách nhận thẻ trong 4 ngày; xử lý hồ sơ online 5 phút |
| Traffic | ~10,477 views/tháng (tháng 8/2025) |
| Blog hiện có | 14 bài published |
| Trang utility bị thiếu | Tra cứu bằng CCCD, tra cứu mã số, tra cứu thời hạn |

### 2.2 Market Size & Search Demand

| Cluster | Keyword đại diện | Avg. Monthly Volume |
|---------|-----------------|---------------------|
| Tra cứu BHYT (core) | tra cứu bảo hiểm y tế | ~90,500 |
| Bảo hiểm y tế (brand) | bảo hiểm y tế | ~110,000 |
| Tra cứu bằng CCCD | tra cứu BHYT bằng CCCD | ~33,100 |
| Tra cứu thời hạn | tra cứu thời hạn BHYT | ~22,200 |
| Tra cứu số thẻ bằng CMND | tra số thẻ BHYT bằng CMND | ~18,100 |
| Mua BHYT online | mua bảo hiểm y tế online | ~12,100 |
| Tra cứu mã số | tra cứu mã số BHYT | ~12,100 |
| Gia hạn online | gia hạn BHYT online | ~5,400 |
| Giá BHYT | giá bảo hiểm y tế | ~5,400 |
| Clusters nhỏ hơn (50+ keywords) | chi trả, trái tuyến, học sinh, hộ gia đình | ~50,000+ tổng |

**Tổng thị trường (2025):** ~525,260 searches/tháng

**Trend:** Tăng trưởng ~3.1x từ 2022 (~168K/tháng) lên 2025 (~525K/tháng). Các keyword mới xuất hiện sau 2024 liên quan CCCD và Luật BHYT mới (Nghị định 188, Thông tư 20, Luật 2025) đang tăng tốc.

**Seasonality:** Đỉnh tháng 8-9 (năm học mới, học sinh sinh viên), đỉnh tháng 12 (gia hạn cuối năm), spike tháng 7/2025 liên quan thông tuyến.

### 2.3 Competitive Landscape

Các đối thủ chính trên SERP: baohiemxahoi.gov.vn, vneid.gov.vn, VSSID app, các site tin tức/giải thích BHYT. MoMo có lợi thế unique là điểm đến transaction trực tiếp (mua được ngay) nhưng yếu ở content informational - là nơi user bắt đầu hành trình tìm kiếm.

---

## 3. Định Hướng Dự Án

### 3.1 Dự Án Này Phục Vụ Điều Gì?

Tăng organic traffic vào `momo.vn/bao-hiem-y-te` và blog BHYT, từ đó drive Web-to-App conversion (user mua/gia hạn BHYT trên MoMo). Mục tiêu trung hạn: MoMo trở thành điểm đến số 1 khi người Việt search bất kỳ thông tin gì về BHYT - từ tra cứu, tìm hiểu chính sách đến mua/gia hạn.

**Đối tượng phục vụ:**
- Người lao động tự do, freelancer chưa có BHYT hoặc cần gia hạn định kỳ (3-6 tháng)
- Người con mua BHYT cho cha/mẹ ở quê qua MoMo
- Học sinh/sinh viên cần tra cứu BHYT
- Người muốn tra cứu thông tin thẻ BHYT (số thẻ, mã số, thời hạn) bằng CCCD/CMND

### 3.2 Dự Án Này KHÔNG Phải

- Không build BHYT bắt buộc (đây là sản phẩm của BHXH, không phải MoMo)
- Không xây dựng tính năng mobile app
- Không cover BHYT thương mại (BH sức khỏe tư nhân)

---

## 4. JTBD Analysis

### 4.1 Keyword Clusters & Intent Map

| JTBD | Cluster Keywords | Volume đại diện | Intent |
|------|-----------------|-----------------|--------|
| J1: Tra cứu thông tin thẻ | tra cứu BHYT, tra cứu bằng CCCD, tra mã số, tra thời hạn | ~170,000+/tháng | Know - Go |
| J2: Hiểu chi phí / giá BHYT | giá BHYT, BHYT bao nhiêu tiền, mức đóng | ~25,000/tháng | Know - Buy |
| J3: Mua / Gia hạn online | mua BHYT online, gia hạn BHYT online, đóng BHYT online | ~25,000/tháng | Buy |
| J4: Hiểu quyền lợi & chính sách | BHYT chi trả như thế nào, trái tuyến, 5 năm liên tục | ~15,000/tháng | Know |
| J5: Tìm kiếm cho nhóm đặc thù | BHYT học sinh, hộ gia đình, cho cha mẹ, trẻ em | ~15,000/tháng | Know - Buy |
| J6: Tra cứu pháp lý & luật mới | Luật BHYT 2025, Nghị định 188, thông tuyến trung ương | ~10,000/tháng | Know |

### 4.2 JTBD Priority Reasoning

**Cao nhất - J3 + J1:** Mua/Gia hạn Online và Tra cứu thông tin thẻ là lõi của MiniWeb Expansion. User đang trong hành trình sử dụng BHYT, MoMo intercept và convert sang giao dịch gia hạn. Đây là workstream có conversion path rõ ràng nhất.

**Trung bình - J2 + J4:** Chi phí và Quyền lợi phục vụ nhóm user đang cân nhắc. Blog content phủ rộng các cluster này, nuture user về sau. Quan trọng cho E-E-A-T và authority.

**Bổ trợ - J5 + J6:** Nhóm đặc thù và pháp lý. Conversion thấp hơn nhưng cần thiết để phủ toàn bộ funnel và xây dựng trust signal YMYL.

### 4.3 User Journey

**Flow 1 - Tra cứu để mua:**
User search "tra cứu BHYT bằng CCCD" -> Trang utility MoMo (Live API) -> Tra cứu được thông tin thẻ -> CTA "Gia hạn BHYT tại đây" -> Conversion mua/gia hạn.

**Flow 2 - Mua trực tiếp:**
User search "mua BHYT online 2026" -> Landing page momo.vn/bao-hiem-y-te -> Thấy form tra cứu + mua -> Conversion.

**Flow 3 - Informational sang transactional:**
User search "BHYT chi trả bao nhiêu phần trăm" -> Blog MoMo -> Đọc bài viết -> Thấy CTA mua BHYT -> Awareness -> Intent -> Conversion sau đó.

---

## 5. Kiến Trúc Web

### 5.1 Sitemap Hub & Spoke

```
momo.vn/bao-hiem-y-te [Hub - Transaction + Utility]
│
├── TRANG UTILITY (MiniWeb Expansion)
│   ├── /bao-hiem-y-te/tra-cuu-so-the-bhyt    - Tra cứu bằng CCCD (~18K+ vol/tháng)
│   ├── /bao-hiem-y-te/tra-cuu-ma-so-bhyt     - Tra cứu mã số (~12K+ vol/tháng)
│   ├── /bao-hiem-y-te/thoi-han-mua-bhyt      - Tra cứu thời hạn (~25K+ vol/tháng)
│   └── **PLG Interactive Tool:** /bao-hiem-y-te/tinh-phi-bhyt - Công cụ ước tính phí BHYT Hộ gia đình (Nhập số người → Ra giá tiền cần đóng, pass "Bữa tối test").
│
├── TRANG THÔNG TIN (Giai đoạn tiếp theo)
│   └── /bao-hiem-y-te/benh-vien              - Top list bệnh viện ~500 tuyến tỉnh (pSEO)
│
└── BLOG CLUSTER (/bao-hiem-y-te/blog/)
    ├── Chi trả BHYT theo thủ thuật/xét nghiệm
    ├── Tra cứu hướng dẫn (CCCD, CMND, online)
    ├── Mua BHYT cho nhóm đặc thù (cha mẹ, HSSV, trẻ em)
    ├── Quyền lợi & chính sách (trái tuyến, 5 năm liên tục)
    └── Luật & pháp lý (Luật BHYT 2025, Nghị định 188)
```

### 5.2 Content Architecture - Schema & AEO

**Schema bắt buộc:** FAQPage - HowTo - Product - BreadcrumbList trên trang cha và trang utility.

**AEO/GEO Standard (VP GPD):** Triển khai file `llms.txt` tại `momo.vn/bao-hiem-y-te/llms.txt` chứa dữ liệu sạch về luật và mức đóng. Bắt buộc để chiếm vị trí trích dẫn số 1 (Source of Truth) trên Perplexity, ChatGPT và Google AI Overviews.

### 5.3 Content Strategy - YMYL Standards

BHYT là YMYL (Your Money or Your Life). Google yêu cầu E-E-A-T cao. Toàn bộ nội dung bắt buộc phải có thông tin kiểm duyệt (Author/Reviewer Profile từ PVI hoặc chuyên gia luật) và trích dẫn trực tiếp nguồn chính phủ.

| Topic Cluster | Keywords | Estimated Volume | YMYL & Compliance Rule |
|--------------|----------|-----------------|------------------------|
| Chi trả BHYT theo thủ thuật | chụp CT/MRI/nội soi có BHYT | ~10,000+/tháng | Trích dẫn danh mục chi trả của Bộ Y Tế |
| Tra cứu hướng dẫn | cách tra cứu BHYT, BHYT bằng CCCD | ~8,000+/tháng | Dùng screenshot UI/UX thực tế từ App/Web MoMo |
| Mua BHYT cho nhóm đặc thù | cha mẹ, người nghỉ việc, bà bầu, trẻ em | ~15,000+/tháng | Trích dẫn định nghĩa nhóm đối tượng theo Luật BHYT |
| Quyền lợi & chính sách | BHYT chi trả %, 5 năm liên tục, trái tuyến | ~15,000+/tháng | Legal review bắt buộc trước khi publish |
| Luật & pháp lý | Luật BHYT 2025, Nghị định 188, thông tuyến | ~10,000+/tháng | Link-out bắt buộc tới chinhphu.vn hoặc thuvienphapluat |
| Giá & chi phí | BHYT bao nhiêu tiền, bảng giá 2025-2026 | ~15,000+/tháng | So sánh rõ ràng mức phí giữa HSSV và Hộ gia đình |

---

## 6. Success Metrics

### 6.1 KPI Framework

| Metric | Baseline (Aug 2025) | Base Case Target (EOY 2026) | Best Case Target (EOY 2026) |
|--------|--------------------|-----------------------------|------------------------------|
| Monthly Web Views (organic) | ~10,477 | ~16,064/tháng (Dec 2026) | Scale tuyến tính với blog volume |
| Total Views 2026 | - | 110,236 | 452,294 |
| MiniWeb utility pages live | 0 | 3 trang | 3 trang + bệnh viện pSEO |
| Blog articles published | 14 bài | 60 bài | 120-150 bài |
| Keyword coverage Top 10 GSC | Đang đo baseline | +50 keywords mới Top 10 | +150 keywords mới Top 10 |
| W2A Conversion Rate | Đang đo baseline | Có baseline xác định | Tối ưu từ baseline |

**Rationale:** Base Case (+52% vs no-action trajectory) đạt được thông qua MiniWeb Expansion + 60 bài blog/năm. Best Case yêu cầu scale blog lên 120-150 bài/năm kèm backlink.

### 6.2 North Star Metric

**Organic Sessions từ cluster /bao-hiem-y-te** được attributed về transaction (mua/gia hạn BHYT).

**Funnel:**
```
Organic session -> Tra cứu/đọc blog -> Gia hạn / Mua ngay click -> App open -> Purchase
```

### 6.3 Mandatory Tracking & AB Test Hypothesis (MoSpark Standard)
- **Hypothesis:** Nếu đưa widget "Công cụ ước tính phí BHYT Hộ gia đình" lên màn hình đầu tiên (First fold), tỷ lệ W2A sẽ tăng 50% so với việc bắt user đọc một bài text về luật BHYT dài 2000 chữ.
- **Tracking Event Schema:** Gắn sự kiện `bhyt_calc_submit`, `bhyt_lookup_result`, `bhyt_gia_han_click` trên GA4 & Appsflyer.

---

## 7. Dependencies & Constraints

### 7.1 Go-to-Market: SPA Framework (Service Productization)
- **reSearch / Strategy:** Phân tích nhu cầu 525K searches/tháng, intent tra cứu thời hạn/CCCD là cao nhất.
- **Pilot / Plan (T6/2026):** Triển khai 3 trang Utility tra cứu + Công cụ tính phí BHYT hộ gia đình trên MoSpark.
- **Action / Amplify (Q3/2026):** Scale blog lên 60-150 bài để thống trị organic SOV.

### 7.2 Operational Constraints

| Dependency | Mô tả | Blocker? | Status |
|------------|-------|----------|--------|
| MiniWeb 3 trang utility | Build trang tra cứu CCCD, mã số, thời hạn - cần API từ BHXH VN hoặc PVI | Có | API đã live, đang build UI |
| API tra cứu BHYT | API để trang utility hoạt động thực tế | Có | Live |
| Blog Production capacity | 5-15 bài/tháng | Không | Đang vận hành |
| Blog Plan 2026 chi tiết | Keyword plan và content calendar cho blog cluster | Có | Đang cập nhật |
| GA4 + GSC tracking sạch | Phân tách organic vs paid traffic trước khi đo KPI | Có | Đang chuẩn hóa |
| Appsflyer W2A tracking | Track conversion từ web sang app cho BHYT flow | Có | Đang đo baseline |

**Hard Constraints (VP GPD Standard):**
- **Không dùng Geo-URL:** Tuyệt đối KHÔNG tạo các trang kiểu `/bao-hiem-y-te-ha-noi` hay `/bao-hiem-y-te-tphcm`. BHYT là chính sách quốc gia dùng chung 1 bảng giá trị, việc tạo pSEO theo tỉnh thành là tạo duplicate content rác.
- Trang phải comply với quy định bảo mật thông tin BHXH - user input CCCD/CMND phải xử lý đúng luật
- Content BHYT thuộc YMYL - cần review chính sách, không được thông tin sai về quyền lợi pháp lý
- Đối tác thu hộ hiện tại là PVI - mọi claim về dịch vụ phải align với scope PVI được ủy quyền
- Content về quyền lợi, mức đóng, chi trả bắt buộc có legal sign-off trước khi publish

---

## 8. Risk Assessment

| # | Rủi ro | Khả năng | Impact | Mitigation |
|---|--------|----------|--------|------------|
| R1 | Blog production không đủ volume -> không đạt target | Thấp | Cao | Content calendar rõ ràng, vendor đang vận hành |
| R2 | MiniWeb utility không có API -> 3 trang quan trọng không launch được | Trung bình | Rất cao | API đã live; nếu unstable, làm trang hướng dẫn tĩnh làm fallback |
| R3 | Tracking organic vs paid chưa sạch -> KPI không đo được chính xác | Cao | Cao | Ưu tiên phân tách GA4 source/medium trước khi launch |
| R4 | Gov site, news site outrank do domain authority cao hơn | Cao | Trung bình | Focus keyword long-tail trước, tích lũy content volume và backlink |
| R5 | Search intent shift sau khi Luật BHYT mới hiệu lực (thông tuyến) | Đã xảy ra | Trung bình | Refresh keyword research định kỳ; ưu tiên content về thông tuyến và chính sách mới |
| R6 | Content sai thông tin pháp lý -> vi phạm YMYL, Google penalty | Thấp | Rất cao | Legal review bắt buộc cho mọi content về quyền lợi, mức đóng, chi trả |

---

## Appendix A: Top 15 Keywords Theo Volume

| Keyword | Avg. Monthly Volume |
|---------|---------------------|
| bảo hiểm y tế | 110,000 |
| tra cứu bảo hiểm y tế | 90,500 |
| tra cứu bảo hiểm y tế bằng cccd | 33,100 |
| tra cứu thời hạn bảo hiểm y tế | 22,200 |
| tra số thẻ bảo hiểm y tế bằng cmnd | 18,100 |
| tra bảo hiểm y tế | 14,800 |
| mua bảo hiểm y tế online | 12,100 |
| tra cứu mã số bảo hiểm y tế | 12,100 |
| kiểm tra bảo hiểm y tế | 9,900 |
| mua bảo hiểm y tế ở đâu | 8,100 |
| mua bảo hiểm y tế | 6,600 |
| mã thẻ bảo hiểm y tế | 6,600 |
| gia hạn bảo hiểm y tế online | 5,400 |
| giá bảo hiểm y tế | 5,400 |
| tra mã bảo hiểm y tế | 5,400 |

**Tổng thị trường addressable (sau khi loại keyword gov-only):** Ước tính 60-70% total, ~315-370K/tháng.

---

## Change Log

- **Tháng 5/2026 (v1.1):** Cập nhật trạng thái API Tra cứu BHYT thành Live. Bổ sung tiêu chuẩn E-E-A-T (YMYL), chiến thuật AEO (llms.txt), và cập nhật cấu trúc Hub & Spoke.
