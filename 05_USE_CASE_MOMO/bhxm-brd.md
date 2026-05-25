# BRD: Bảo Hiểm Xe Máy - Web Growth (SEO/GEO Project)

> - **Project:** Bảo Hiểm Xe Máy Web Growth
> - **Main URL:** momo.vn/bao-hiem-xe-may
> - **Division:** FS (Financial Services)
> - **Use Case:** InsurTech
> - **Owner:** GPD - Out-App Traffic
> - **Governance:** SEO & GEO Lead
> - **Version:** 1.1 - March 2026
> - **Status:** Draft
> - **SEO Score:** 65/100 | **Traffic:** 15K sessions/tháng | **W2A:** 8.5%

---

## 1. Executive Summary

### Situation

MoMo là một trong những kênh phân phối bảo hiểm xe máy trực tuyến lớn tại Việt Nam, đã phân phối hơn 2.3 triệu hợp đồng với đối tác là các nhà bảo hiểm uy tín (Bảo Việt, PVI, PTI, MIC, GIC, Liberty). Thị trường có nền tảng cầu tự nhiên rất cao: 72 triệu xe máy đang lưu hành, bảo hiểm TNDS bắt buộc theo pháp luật, và Nghị định 168/2024/NĐ-CP nâng mức phạt lên 200-300K đồng từ 1/1/2025 tạo spike tìm kiếm định kỳ đầu mỗi năm.

Dữ liệu keyword nội bộ ghi nhận 519 từ khoá, tổng volume ~67,540/tháng và đạt đỉnh ~76,460 vào tháng 3/2025. Nhu cầu tìm kiếm trải rộng 7 cluster khác nhau từ transactional (mua/giao dịch), informational (kiến thức/pháp lý), đến utility (tra cứu/giá), cho thấy user đang hiện diện ở tất cả các giai đoạn funnel.

### Complication

**Vấn đề cốt lõi: Traffic sụt 95% sau mỗi spike đầu năm.**

Dữ liệu internal cho thấy: Tháng 1 đạt 79K → Tháng 2: 16K → Tháng 3: 6.4K → Tháng 4: 5.1K → Tháng 5: 4K. Pattern này lặp lại mỗi năm, cho thấy MoMo chỉ đang tận dụng được spike theo mùa từ cluster "Phạt/Pháp lý" mà không xây được baseline traffic quanh năm.

6 trong 7 keyword cluster lớn (Giá, Tra cứu, Địa điểm, Nhà BH, Kiến thức, Xe máy điện) chưa có trang đích tương ứng trên momo.vn. Cụ thể:

- Cluster "Giá" (~8,500 vol/tháng): chưa có trang bảng giá theo phân khối với calculator
- Cluster "Tra cứu" (~2,500 vol/tháng): chưa có widget tra cứu biển số/số khung
- Cluster "Địa điểm" (~4,000 vol/tháng): user tìm kênh offline nhưng không được redirect sang online MoMo
- Cluster "Xe máy điện" (+40% YoY): whitespace ít cạnh tranh, MoMo chưa có trang riêng

Các đối thủ không bán hàng (royalhelmet.com.vn, ibaohiem.vn) đang chiếm Top 3-5 cluster Kiến thức và Giá. Các nhà BH trực tiếp (MIC, PVI, PTI) chiếm branded cluster của chính họ. Trang cha `/bao-hiem-xe-may` chỉ có content TOFU cơ bản, thiếu khoảng 15-20 trang so với sitemap mục tiêu.

### Resolution

Xây dựng cluster Bảo Hiểm Xe Máy theo kiến trúc Hub & Spoke đầy đủ: 1 trang cha đóng vai Hub, các spoke gồm trang sản phẩm, trang theo nhà BH, trang theo loại xe (bao gồm pSEO), và blog content hub. Song song, tối ưu GEO/AEO để MoMo được trích dẫn trong Google AI Overview, Gemini, và các AI assistant khi user hỏi về bảo hiểm xe máy. Mục tiêu: xây baseline 15-25K sessions/tháng quanh năm, spike 70-90K tháng 1 hàng năm.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Trang Cha `/bao-hiem-xe-may`

| Khía cạnh | Mô tả |
|---|---|
| URL | momo.vn/bao-hiem-xe-may |
| Trạng thái | Đang hoạt động - có hero form mua BH, so sánh CÓ/KHÔNG BH, hướng dẫn bồi thường 4 bước |
| Content hiện có | TOFU cơ bản: hero + trust bar + so sánh + hướng dẫn quy trình |
| Thiếu | Bảng giá theo phân khối, widget tra cứu, cluster nhà BH, cluster loại xe, blog hub, FAQ schema, AggregateRating schema |
| Organic traffic | 4-79K sessions/tháng (biến động theo mùa, đỉnh tháng 1 do Nghị định 168) |
| Vấn đề cốt lõi | Không có evergreen content cluster - traffic sụt 95% sau spike tháng 1 |

### 2.2 Keyword Data - 7 Pillar Clusters

| Cluster | Vol ước tính | Trang đích hiện tại | Khoảng trống |
|---|---|---|---|
| Mua / Giao dịch Online | ~15,000/tháng | /bao-hiem-xe-may (hiện có) | Tối ưu UX/copy, thêm trust signals |
| Phạt / Bắt buộc / Pháp lý | ~12,000/tháng | Có blog mức phạt cũ | Update 2026, thêm biến thể FOMO |
| Giá / Chi phí | ~8,500/tháng | Chưa có | Cần /bao-hiem-xe-may/bang-gia + calculator |
| Địa điểm / Kênh mua offline | ~4,000/tháng | Chưa có | Bridge content chuyển offline sang online intent |
| Kiến thức / Giải thích | ~4,000/tháng | Rải rác, không có hub | Blog hub + FAQ schema |
| Tra cứu / Kiểm tra hạn | ~2,500/tháng | Chưa có | /bao-hiem-xe-may/tra-cuu + widget biển số |
| Nhà BH Branded | ~2,000/tháng | Chưa có | Landing page per nhà BH |
| Xe máy điện | +40% YoY | Chưa có | /bao-hiem-xe-may/xe-may-dien - whitespace ít cạnh tranh |

**Insight quan trọng:** Cluster "Phạt" có CPC = 0đ vào tháng 10/2025 - không ai bid, organic gần như free. ~60 biến thể keyword, tổng ~12,000 vol/tháng. Đây là nhóm FOMO conversion cao nhất, ranking dễ nhất - nên publish đầu tiên.

### 2.3 Phân Tích Cạnh Tranh

| Đối thủ | Cluster đang chiếm | Điểm yếu | Cơ hội MoMo |
|---|---|---|---|
| royalhelmet.com.vn | Phạt - Giá - Kiến thức (Top 3-5) | Không có sản phẩm - zero conversion | Cùng content depth + inline form. Thắng bằng trust 2.3M hợp đồng |
| ibaohiem.vn / tasco.vn / opes.com.vn | Kiến thức - Tra cứu (DA tốt) | UX kém, không mobile-first, không có widget tra cứu thực | Beat Core Web Vitals + widget tra cứu biển số thực tế |
| Điện Máy Xanh / TGDĐ | Mua + Địa điểm | BH chỉ là phụ trợ, không có cluster giá hay tra cứu | MoMo chuyên sâu hơn - tra cứu, tái tục, cluster giá 2/3 năm |
| MIC / PVI / PTI trực tiếp | Branded cluster của chính họ (~260-390/brand) | Chỉ push 1 nhà BH, không có trang so sánh đa bên | MoMo = trung lập đa nhà BH - trang so sánh capture toàn cluster branded |
| ZaloPay / ViettelMoney | Branded search nhỏ | Web SEO rất yếu, không có content cluster | Duy trì lợi thế content depth - tấn công thay vì phòng thủ |

### 2.4 Seasonality & Trend

**Spike định kỳ hàng năm:**
- Tháng 11-12: Cuối năm, nhiều người biết BH sắp hết hạn - "gia hạn bảo hiểm xe máy" tăng mạnh
- Tháng 1: Nghị định mới có hiệu lực, CSGT tăng cường - cluster Phạt/Mức phạt đỉnh điểm
- Tháng 4-5: Mùa mưa bắt đầu - cluster bồi thường, tai nạn tăng
- Tháng 6-7: Mùa học mới, học sinh/sinh viên mua xe - cluster 50cc/xe điện học sinh

**Emerging trends:**
- Xe máy điện: +40% YoY. VinFast, Yamaha Neo, Yadea tạo cluster keyword mới "xe máy điện có cần bảo hiểm không" - whitespace ít cạnh tranh, nên chiếm trước.
- GCN điện tử: Sau Nghị định 03/2021, hợp pháp 100% nhưng user vẫn search "giấy chứng nhận điện tử có hợp lệ không" - cần content trust-building.
- Mobile-first purchase: Search query ngày càng conversational hơn, MoMo là Super App có lợi thế tự nhiên.

---

## 3. Định Hướng Dự Án

### 3.1 Dự Án Này Phục Vụ Điều Gì?

**Xây dựng cluster Bảo Hiểm Xe Máy như một Organic Growth Engine phục vụ 3 mục tiêu:**

**Acquisition - Capture toàn bộ funnel bảo hiểm xe máy**

User đang search từ nhiều entry point (mua, giá, tra cứu, địa điểm, pháp lý) nhưng MoMo chỉ có 1 trang cha phủ được cluster transactional. Cần xây đủ 7 cluster để không để traffic rơi vào tay đối thủ không có conversion value.

**Retention & Renewal - Tra cứu và Gia hạn như utility**

User đã mua BH trên MoMo cần tra cứu hạn, gia hạn hàng năm. Xây `/bao-hiem-xe-may/tra-cuu` và `/bao-hiem-xe-may/gia-han` như utility tools - vừa phục vụ user hiện tại, vừa capture organic traffic từ user chưa mua trên MoMo.

**GEO/AI Visibility - Trở thành nguồn trích dẫn cho AI engines**

FAQ + HowTo + AggregateRating Schema trên trang cha và trang sản phẩm inject câu trả lời vào Google AI Overview, Gemini, Perplexity khi user hỏi "mua bảo hiểm xe máy ở đâu uy tín?" hay "bảo hiểm xe máy MoMo có tốt không?". Đây là GEO moat dài hạn vì cần entity authority mạnh (số hợp đồng, đối tác nhà BH, dữ liệu thực).

### 3.2 Dự Án Này KHÔNG Phải

- Không phải xây lại trang marketing campaign - đây là evergreen content cluster phục vụ organic traffic
- Không phải CMS cho nhà BH tự quản lý content
- Không phải store locator hay agent directory
- Không phải thay thế Deep Link / App flow - web chỉ là entry point, conversion vẫn xảy ra trong App

---

## 4. JTBD Analysis

### Job #1: Xác Nhận Nghĩa Vụ Pháp Lý

> "Tôi cần biết xe mình có bắt buộc mua bảo hiểm không, và không mua thì bị phạt bao nhiêu."

| Dimension | Nội dung |
|---|---|
| Functional | Xác nhận xe loại mình có bắt buộc mua BH không. Biết chính xác mức phạt hiện hành theo Nghị định mới nhất |
| Emotional | Tránh bị phạt bất ngờ, bị giữ xe. Cảm giác tuân thủ pháp luật, an tâm lưu thông |
| Social | Không muốn bị cảnh sát giao thông "làm khó" trước mặt người khác |
| Trigger | Thấy bạn bè bị phạt - Nghe tin mức phạt mới - CSGT đang kiểm tra đường mình đi |

**Giải pháp:** Blog cluster Phạt/Pháp lý - Bảng mức phạt 2026 cập nhật (Nghị định 168) - CTA mua ngay.

---

### Job #2: So Sánh Giá Và Lựa Chọn Nhà BH Phù Hợp

> "Bảo hiểm xe máy giá bao nhiêu? Mua Bảo Việt hay PVI hay MIC thì tốt hơn?"

| Dimension | Nội dung |
|---|---|
| Functional | Biết chính xác phí bảo hiểm theo phân khối xe. So sánh giữa các nhà BH. Tìm gói tự nguyện phù hợp |
| Emotional | Cảm giác mua đúng giá, không bị "chặt chém". Thông minh tài chính |
| Social | Chia sẻ thông tin BH tốt với gia đình, bạn bè có xe |
| Trigger | Chuẩn bị mua xe mới - BH sắp hết hạn - Đang so sánh trên điện thoại |

**Giải pháp:** /bao-hiem-xe-may/bang-gia + price calculator + landing page per nhà BH với điểm khác biệt.

---

### Job #3: Tra Cứu Hạn BH Và Gia Hạn Nhanh

> "Xe mình còn BH không? Hết hạn rồi thì gia hạn ở đâu nhanh nhất?"

| Dimension | Nội dung |
|---|---|
| Functional | Nhập biển số - biết ngay xe còn hạn không. Gia hạn ngay trong 1-2 click nếu hết hạn |
| Emotional | Tránh lo lắng, không chắc xe còn hạn không trước khi lên đường. Tự tin khi ra đường |
| Social | Trách nhiệm với gia đình - không để xe hết BH mà không biết |
| Trigger | Chuẩn bị đi xa - CSGT đang kiểm tra - Nhớ ra BH có thể hết hạn rồi |

**Giải pháp:** /bao-hiem-xe-may/tra-cuu (widget biển số, kết quả contextual: Còn hạn → "Gia hạn", Hết hạn → "Mua ngay").

---

### Job #4: Mua BH Nhanh, Không Cần Ra Ngoài

> "Tôi biết cần mua rồi - làm sao mua online nhanh nhất, nhận GCN ngay?"

| Dimension | Nội dung |
|---|---|
| Functional | Mua xong trong dưới 3 phút, trên điện thoại. Nhận GCN điện tử hợp lệ ngay sau thanh toán |
| Emotional | Không mất thời gian ra bưu điện, đại lý. Cảm giác hiệu quả, tiện lợi |
| Social | MoMo là Super App - mua BH ở đây như các việc khác: nhanh và tin |
| Trigger | Đang cầm điện thoại, sắp đi ra đường - Bạn bị phạt vừa nhắc nhở |

**Giải pháp:** Trang cha /bao-hiem-xe-may (hero form) + Blog "Không cần ra bưu điện" bridge content.

---

### Job #5: Được Bồi Thường Đúng Khi Xảy Ra Tai Nạn

> "Bị tai nạn rồi - làm thế nào để được nhà BH bồi thường? Cần giấy tờ gì?"

| Dimension | Nội dung |
|---|---|
| Functional | Biết chính xác quy trình bồi thường step-by-step. Biết cần giấy tờ gì, nộp ở đâu |
| Emotional | Giảm stress trong lúc hoảng loạn sau tai nạn. Cảm giác được hỗ trợ, không bị bỏ mặc |
| Social | Chứng minh BH mua trên MoMo "là thật", được bồi thường đàng hoàng |
| Trigger | Vừa xảy ra tai nạn - Người thân bị tai nạn - Tìm hiểu trước khi mua |

**Giải pháp:** /bao-hiem-xe-may/boi-thuong (hướng dẫn 4 bước + schema) + blog bồi thường chi tiết.

---

## 5. Kiến Trúc Web

### 5.1 Sitemap Hub & Spoke

```
momo.vn/bao-hiem-xe-may [Hub]
│
├── TRANG SẢN PHẨM
│   ├── /bao-hiem-xe-may/bat-buoc           - BH TNDS bắt buộc
│   ├── /bao-hiem-xe-may/tu-nguyen          - BH tự nguyện/vật chất
│   ├── /bao-hiem-xe-may/gia-han            - Gia hạn / Tái tục
│   ├── /bao-hiem-xe-may/boi-thuong         - Hướng dẫn bồi thường
│   ├── /bao-hiem-xe-may/tra-cuu            - Widget tra cứu biển số
│   └── /bao-hiem-xe-may/bang-gia           - Bảng giá + calculator
│
├── LANDING PAGE THEO NHÀ BH
│   ├── /bao-hiem-xe-may/bao-viet
│   ├── /bao-hiem-xe-may/pvi
│   ├── /bao-hiem-xe-may/pti
│   ├── /bao-hiem-xe-may/mic
│   ├── /bao-hiem-xe-may/gic
│   └── /bao-hiem-xe-may/liberty
│
├── LANDING PAGE THEO LOẠI XE (pSEO)
│   ├── /bao-hiem-xe-may/xe-may-dien        - Trend +40% YoY
│   ├── /bao-hiem-xe-may/duoi-50cc
│   ├── /bao-hiem-xe-may/50-175cc
│   ├── /bao-hiem-xe-may/tren-175cc
│   ├── /bao-hiem-xe-may/honda-wave
│   └── /bao-hiem-xe-may/yamaha-exciter
│
└── BLOG & CẨM NANG HUB
    ├── /blog/muc-phat-khong-bao-hiem-2026  - Pillar FOMO
    ├── /blog/gcn-bao-hiem-dien-tu
    ├── /blog/huong-dan-mua-bao-hiem-xe-may
    ├── /blog/bao-hiem-xe-may-dien
    ├── /blog/bh-bat-buoc-vs-tu-nguyen
    ├── /blog/mua-bao-hiem-online-vs-offline - Bridge offline intent
    ├── /blog/huong-dan-boi-thuong-tai-nan
    ├── /blog/sinh-vien-mua-bao-hiem-lan-dau
    └── /blog/checklist-xe-truoc-tet         - Seasonal
```

**Nguyên tắc internal linking:**
- Hub -> Spoke: Trang cha link ra tất cả trang sản phẩm, nhà BH, loại xe
- Spoke -> Hub: Mỗi trang con có breadcrumb + CTA về trang cha
- Spoke -> Spoke: Trang xe điện link sang trang dưới 50cc; trang Bảo Việt link sang trang PVI (comparison)
- Không để trang nào bị orphan

### 5.2 Content Structure - Trang Cha `/bao-hiem-xe-may`

| # | Component | Ghi chú |
|---|---|---|
| 1 | Hero Section | H1 + Form chọn phân khối - CTA "Mua ngay". Tối ưu UX copy |
| 2 | Trust Bar | 2.3M hợp đồng - các nhà BH uy tín - GCN điện tử hợp pháp - Nhắc gia hạn tự động |
| 3 | So sánh CÓ vs KHÔNG mua BH | 2 cột: FOMO + benefit |
| 4 | Grid nhà BH | Logo + tên 6 nhà BH + CTA link tới trang riêng |
| 5 | Hướng dẫn 3 bước (HowTo) | Chọn phân khối - Chọn nhà BH - Thanh toán & nhận GCN điện tử. HowTo Schema |
| 6 | Hướng dẫn bồi thường 4 bước | CTA link sang /bao-hiem-xe-may/boi-thuong |
| 7 | Blog feed | 6 bài mới nhất |
| 8 | FAQ 10+ câu | Accordion, FAQPage Schema bắt buộc |
| 9 | Review / Đánh giá | Tối thiểu 10 reviews thực. AggregateRating Schema (4.x/5 sao) - quan trọng cho E-E-A-T và GEO |

**Schema bắt buộc trang cha:** FAQPage - HowTo - Product - AggregateRating - BreadcrumbList

### 5.3 GEO/AEO Strategy

Bảo hiểm xe máy là YMYL - Google yêu cầu E-E-A-T cao. Các AI engines (Google AI Overview, Gemini, Perplexity) ưu tiên cite nguồn có structured data, FAQ rõ ràng, và authority signals.

| Nền tảng AI | Behavior | Chiến lược tối ưu |
|---|---|---|
| Google AI Overview (SGE) | Tổng hợp từ 3-5 nguồn, hiển thị trước organic | FAQPage Schema bắt buộc, câu trả lời direct dưới 50 từ, cấu trúc H2/H3 rõ |
| Gemini (Google) | Real-time web access, ưu tiên nguồn authority | Cập nhật content sau mỗi Nghị định mới, structured data đầy đủ |
| ChatGPT / Copilot | Cite từ training data, volume content indexed nhiều | Blog chất lượng cao, được index và share nhiều |
| TikTok / YouTube Search | Gen Z tìm qua video | Embed video guide ngắn trong trang hướng dẫn mua |

**E-E-A-T signals cần có:**
- Author byline với chức danh chuyên môn
- Ngày cập nhật visible (dd/mm/yyyy), Last reviewed date
- Cite đúng số Nghị định (Nghị định 168/2024/NĐ-CP, Nghị định 67/2023)
- Link tới văn bản pháp luật chính thức
- Số liệu thực: 2.3M hợp đồng, tên đối tác BH cụ thể

---

## 6. Success Metrics

### 6.1 KPI Framework

| Metric | Baseline | Target (90 ngày post-launch) | Source |
|---|---|---|---|
| Organic sessions /bao-hiem-xe-may cluster | ~4-5K/tháng (ngoài mùa) | 15K/tháng (quanh năm) | GSC + GA4 |
| Organic sessions spike tháng 1/2027 | 79K (tháng 1/2025) | 90K | GSC |
| Trang mới trong Top 10 GSC | 0 trang mới | 10 trang mới | GSC |
| Click-to-app từ cluster BH xe máy | Đang đo baseline | Có baseline xác định | GA4 + Appsflyer |
| Blog time on page | Đang đo baseline | 2:30 phút | GA4 |
| AI Overview citations cho BH xe máy queries | Đang audit | 5 queries được cite | Manual monitoring |
| AggregateRating Schema indexing | 0 | Xuất hiện Rich Results | GSC Rich Results |
| Cross-sell CTR (post-purchase) | 0% | 8% | GA4 events |

### 6.2 North Star Metric

**Organic-attributed Insurance Purchases từ cluster /bao-hiem-xe-may** = số hợp đồng BH xe máy được attributed từ organic traffic web.

**Funnel:**

```
Organic session → Mua ngay click → App open → Purchase (via Appsflyer)
```

---

## 7. Dependencies & Constraints

| Dependency | Owner | Mô tả | Blocker? |
|---|---|---|---|
| Widget tra cứu biển số - API kết nối CSDL BH | BH Product team + BE | Cần API để widget /tra-cuu hoạt động thực. Không có API - fallback hướng dẫn tra cứu thủ công | Có - cho /tra-cuu |
| Dữ liệu phí bảo hiểm chính xác per nhà BH | BH Product team | Phí BH bắt buộc = quy định nhà nước. Phí tự nguyện khác nhau per nhà BH - cần data thực | Có - cho /bang-gia |
| Deep Link per nhà BH và per phân khối xe | App team | CTA "Mua ngay" cần deep link đúng destination trong App | Có - cho landing page nhà BH |
| AggregateRating data (rating + số review thực) | BH Product team | Cần số liệu rating thực từ hợp đồng đã mua. Không được dùng rating không có nguồn gốc | Có - YMYL + legal |
| Review / Approve nội dung pháp lý | Legal team | Mọi số liệu mức phạt, mức bồi thường, điều kiện bắt buộc phải có legal sign-off | Có - YMYL |
| Số liệu trust bar (số hợp đồng, đối tác BH) | BH Product team | Cần xác nhận số liệu chính xác nhất tính đến ngày publish | Không - có thể update sau |
| Content production | SEO team | 9 blog posts + 15+ landing pages | Không - team tự build |

**Constraints:**
- Content pháp lý (mức phạt, điều kiện BH, mức bồi thường) PHẢI qua legal review trước khi publish - không auto-publish
- AggregateRating Schema chỉ được dùng khi có data review thực - không dùng fake rating
- Số liệu Nghị định phải cite đúng số hiệu và năm ban hành
- Widget tra cứu biển số không được lưu trữ biển số sau query - privacy constraint
- Khi có Nghị định mới về mức phạt hoặc phí BH - update content trong vòng 7 ngày

---

## 8. Risk Assessment

| # | Rủi ro | Khả năng | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Content pháp lý lỗi thời sau khi có Nghị định mới - Google penalize hoặc user complaint | Cao | Cao | Quy trình review định kỳ, alert khi có Nghị định mới, update trong 7 ngày |
| R2 | API tra cứu biển số không khả dụng hoặc delay - trang /tra-cuu không có giá trị thực | Trung | Trung | Fallback: hướng dẫn 4 cách tra cứu thủ công thay thế. Không block launch trang cha |
| R3 | Rating/Review data không đủ hoặc chất lượng thấp - không implement được AggregateRating Schema đúng chuẩn | Trung | Trung | Gate: chỉ implement schema khi có đủ 10+ reviews thực. Không dùng placeholder |
| R4 | Content production bottleneck - 15+ trang cần viết đồng thời gây delay launch | Cao | Trung | Phân giai đoạn: 3-4 trang cốt lõi launch trước, phần còn lại follow sau 4-6 tuần |
| R5 | Keyword "xe máy điện" đang tăng - đối thủ build trang trước MoMo | Trung | Trung | Speed-to-market: /xe-may-dien là trang ưu tiên đầu tiên |
| R6 | Deep link per nhà BH chưa sẵn sàng - landing page nhà BH không có CTA đúng | Thấp | Thấp | Fallback: CTA link về trang cha trong khi chờ deep link |
| R7 | Blog posts YMYL không đạt E-E-A-T - không rank hoặc bị manual action | Thấp | Cao | Template strict: cite Nghị định, author byline, legal review bắt buộc |

---

## Change Log

- **Tháng 5/2026:** Khởi tạo tài liệu và chuẩn hóa cấu trúc thư mục.
