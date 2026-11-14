# Khung Báo Cáo Định Kỳ Web Platform (Web Platform Reporting Framework)

> **Mục tiêu:** Bộ quy chuẩn toàn diện về phương pháp luận, cấu trúc slide, công thức hành văn (copywriting/texting) và mẫu báo cáo định kỳ dành cho Web Platform.
> **Đối tượng báo cáo:** 
> - **Weekly Report:** Báo cáo tuần gửi Executive Leadership (anh Công) - tập trung vào tiến độ thực thi, tháo gỡ điểm nghẽn và đo lường tác động nhanh.
> - **Monthly Report:** Báo cáo tháng gửi Ban Giám Đốc / Hội đồng Quản trị (anh Tường, anh Công) - tập trung vào sức khỏe động cơ tăng trưởng, danh mục 4 Zone, phân tích Cohort và tác động chiến lược vĩ mô.

---

## 1. NGUYÊN TẮC BẮT BUỘC (CORE COMPLIANCE RULES)

Theo chỉ dẫn tại `AGENTS.md`, mọi báo cáo của Web Platform bắt buộc tuân thủ:

1. **Tuyệt đối không sử dụng Emoji / Icon:** Không dùng bất kỳ biểu tượng cảm xúc hay icon trang trí nào trong toàn bộ tiêu đề, bảng biểu và danh sách của bài báo cáo.
2. **Không đề cập tên riêng cá nhân / PIC:** Thay thế toàn bộ tên riêng bằng tên đội ngũ chuyên môn tương ứng (`Web Dev`, `Backend Team`, `Content Team`, `SEO Vendor`, `Media Team`, `Risk Team`, `AI/ML Team`, `CX Team`, `BU Movies`, `VTTI BU`, `FS Team`...).
3. **Cấu trúc 3 khối chuẩn mực** (áp dụng cho báo cáo Tuần, và cho phần thân báo cáo Tháng):
   - Khối 1: `Điểm nổi bật & Tác động kinh doanh`
   - Khối 2: `Phối hợp liên phòng ban & Việc cần hỗ trợ`
   - Khối 3: `Ưu tiên 7/30 ngày tới`
   - Riêng slide `Executive Summary` của báo cáo Tháng dùng cấu trúc 2 khối theo quy chuẩn công ty: `Điểm nổi bật` và `Vấn đề cần cải thiện`. Khối thứ hai bắt buộc có nội dung; một báo cáo chỉ có tin tốt là lỗi về độ tin cậy.
4. **Hệ thống 2 tầng chỉ số song song:** Luôn đo lường đồng thời **Tầng Web Metrics** (Pageviews, Sessions, MEU, CTR) và **Tầng App Business Impact** (Login App, New Installs, Transactions, Saved Profiles).
5. **Định dạng biểu diễn trực quan:**
   - Luồng người dùng / Hành trình trải nghiệm: Bắt buộc dùng sơ đồ Mermaid (`graph TD` hoặc `graph LR`) kèm theo Bảng phân tích chi tiết các bước (Step Breakdown Table).
   - Lộ trình và Cột mốc: Bắt buộc dùng Bảng Markdown (`Table`).

---

## 2. PHÂN ĐỊNH BÁO CÁO WEEKLY (ANH CÔNG) VS. MONTHLY (ANH TƯỜNG)

| Tiêu Chí So Sánh | Báo Cáo Tuần (Weekly - Anh Công) | Báo Cáo Tháng (Monthly - Anh Tường) |
| :--- | :--- | :--- |
| **Nhịp độ & Khung thời gian** | 7 ngày (Tuần hiện tại & 7 ngày tới) | 30 ngày (Tháng hiện tại & 30-90 ngày tới) |
| **Trọng tâm quản trị** | Vận hành thực thi, tiến độ tính năng, tháo gỡ điểm nghẽn kỹ thuật, quản trị ngân sách và A/B testing. | Sức khỏe động cơ tăng trưởng, danh mục 4 Zone, phân tích Cohort giữ chân, thị phần và chiến lược điểm đến Web Destination. |
| **Mức độ chi tiết số liệu** | Biến động tuần (WoW), số lượng ticket CS, tốc độ tải P90, CVR từng biến thể A/B, tiến độ rollout tính năng. | Chuỗi thời gian 6-12 tháng, Cohort Retention (M0-M11), cơ cấu First-service 15+ dịch vụ, tiến độ 3 kịch bản Traffic (4M-5M-6M). |
| **Cấu trúc Ưu tiên (Priorities)** | 1. Sửa lỗi & Phát hành (Hotfix & Delivery)<br/>2. Đánh giá A/B Testing<br/>3. Phối hợp liên đội ngũ (Sync) | 1. Vùng Hiệu suất (Performance Scaling)<br/>2. Vùng Chuyển đổi & Ươm tạo (Transformation/Incubation)<br/>3. Nền tảng & AI (Platform & AI Adoption) |

---

## 3. CÔNG THỨC HÀNH VĂN & MÔ TẢ (TEXTING & COPYWRITING FORMULA)

### 3.1. Công thức viết khối "Key Highlights & Business Impact"
**Giới hạn bắt buộc:** tối đa 5 ý, mỗi ý 1 dòng, mở đầu bằng con số (PV, % target, Install, ngày go-live) và kết bằng chỉ dẫn mục chi tiết ("Chi tiết mục III.2"). Khối này là bản tóm tắt cho cấp quản lý, không lặp lại phần mô tả của mục II-IV.
- Không đưa chi tiết build (tên tính năng con, URL, kiến trúc, quy trình nội bộ) vào đây; các chi tiết đó nằm ở mục Hub/Platform tương ứng.
- Nhiều việc go-live trong tuần gom chung vào một ý "Lên Production".
- Không kết luận vượt quá số liệu (ví dụ: tỷ trọng Non-Paid cao không có nghĩa "độc lập hoàn toàn với Paid").

Áp dụng công thức 4 thành tố liên kết:
$$\text{Số liệu đạt được (Biên độ WoW/MoM)} \longrightarrow \text{Nguyên nhân cốt lõi (Driver)} \longrightarrow \text{Tác động hệ sinh thái (Impact)} \longrightarrow \text{Hành động tiếp theo (Next Action)}$$

*Mẫu câu chuẩn cho Web Traffic & SEO/GEO:*
- "Lưu lượng truy cập đạt [Số] Pageviews ([+/-]% MoM) và [Số] MEU. Tỷ lệ Pageviews/MEU đạt [Số], phản ánh tệp người dùng có nhu cầu tìm kiếm thực (Intent Search) ổn định. Kênh Organic Search bứt phá (+[Số]% MoM) bù đắp cho phần sụt giảm của Paid Search sau khi chiến dịch Mega kết thúc."
- "Go-live [Số] trang nội dung chuẩn SEO/GEO; 100% đối tác xuất hiện trong Top 3-5 Google Search đối với cụm từ khóa thương hiệu; ghi nhận [Số] trích dẫn trên các công cụ AI Search (GEO đạt [Số]% Share of Authority)."

*Mẫu câu chuẩn cho Phễu Web-to-App & New User:*
- "Lượt cài đặt ứng dụng mới (New Install) duy trì đà tăng trưởng 3 tháng liên tiếp ([Số] $\rightarrow$ [Số] $\rightarrow$ [Số] installs), chứng minh nhóm người dùng mới được thu hút hiệu quả ngoài Web độc lập với biến động của tệp người dùng hiện hữu."
- "Tỷ lệ chuyển đổi MEU sang New Install cải thiện lên [Số]% (từ [Số]% tháng trước); gói quà chào mừng CHAOMOMO đóng góp [Số]% tổng lượt cài đặt nhờ giảm thiểu rào cản dùng thử."

*Mẫu câu chuẩn cho Năng lực Nền tảng & Công nghệ (MoSpark & GenAI):*
- "Tối ưu hóa luồng gọi API và tinh giản giao diện giúp cải thiện tốc độ tải trang P90 giảm [Số]%, thời gian đến khi nhấp chuột (Time to Click P90) giảm [Số]%, nâng điểm CSAT lên [Số]/5."
- "Triển khai GenAI Content Pipeline giúp rút ngắn thời gian sản xuất bài viết từ 1-2 ngày xuống còn 4-5 phút/bài, chi phí sản xuất giảm xuống 7.000 - 20.000 VNĐ/bài, giải phóng 90% thời gian vận hành thủ công."

---

### 3.2. Công thức viết khối "Cross-team Collaboration & Support Needed"
Bóc tách chi tiết rõ ràng theo từng đội ngũ đối tác kèm yêu cầu định lượng:

- **Đội ngũ Business Units (Cinema, VTTI, FS, SPS, Student Pass):**
  - "Phối hợp với BU tương ứng để chốt bộ quy tắc nghiệp vụ (Domain Knowledge), tích hợp API sản phẩm và thống nhất ngân sách truyền thông Off-page."
- **Đội ngũ Media & Marketing:**
  - "Phối hợp phân bổ ngân sách Paid Search/Paid Social tập trung vào các cụm từ khóa có tỷ lệ chuyển đổi cao (High-intent KWs) cho gói quà chào mừng người dùng mới."
- **Đội ngũ Risk, Security & Compliance:**
  - "Thiết lập bộ lọc giám sát chất lượng tự động (Guardrails) trên MoSpark CMS để ngăn chặn xuất bản nội dung vi phạm tiêu chuẩn SEO/Compliance; hoàn thiện cơ chế phân quyền Admin Panel."
- **Đội ngũ App Platform & Analytics:**
  - "Chuẩn hóa hạ tầng tracking Full Funnel qua Onelink để bóc tách chính xác toàn bộ hành trình từ Web Pageviews sang App Install, Mapbank và First Transaction."
- **Đội ngũ AI/ML & Big Data:**
  - "Mở rộng thuật toán gợi ý dịch vụ thông minh (Service Recommendation) ngoài Web dựa trên phân tích hành vi tìm kiếm của người dùng."

---

### 3.3. Công thức viết khối "Priorities"

**Đối với Báo cáo Tuần (7 Days):**
- **Sửa lỗi & Tối ưu Giao diện (Hotfix & Delivery):** Hoàn thành phát hành bản vá [Tên tính năng], tối ưu hóa tốc độ tải trang trên thiết bị di động.
- **Thử nghiệm A/B (A/B Test Validation):** Đánh giá số liệu biến thể [Treatment] so với [Control] trên quy mô [Số] người dùng để quyết định mở rộng toàn phần (Roll mass).
- **Phối hợp liên đội ngũ (Cross-team Sync):** Tổ chức họp chuyên sâu chốt giải pháp tự phục vụ (Self-service) cho các BU.

**Đối với Báo cáo Tháng (30 Days):**
- **Vùng Hiệu suất (Performance Scaling):** Mở rộng quy mô các dịch vụ mang lại dòng tiền ổn định (như luồng đặt vé xem phim toàn quốc, thanh toán QR trực tiếp).
- **Vùng Chuyển đổi & Ươm tạo (Transformation & Incubation):** Đưa Master Page Tiện Ích Giao Thông và Financial Hub vào vận hành chính thức; mở rộng độ phủ Student Pass tại các cụm trường đại học.
- **Nền tảng & AI (Platform & AI Adoption):** Nâng cấp công suất GenAI Content Pipeline đạt mục tiêu [Số] bài/tháng; mở rộng công cụ Landing Page Builder cho các Cell Teams.

---

## 4. MẪU BÁO CÁO TUẦN CHUẨN INSURTECH DÀNH CHO ANH CÔNG (WEEKLY TEMPLATE)

> **Cập nhật quy chuẩn:** Áp dụng nguyên mẫu kiến trúc từ `[InsurTech] Web 2026 Performance.pptx` kết hợp cẩm nang `03_SKILLS/executive-presentation-playbook.md`:
> 1. Mỗi mục đều có Tiêu đề hành động mang kết luận trọn vẹn (Insight-Led Action Title).
> 2. Thẻ số liệu 3 tầng (Big Stat + Delta WoW/Baseline + Ý nghĩa kinh doanh).
> 3. Phễu chuyển đổi 4 bước (Traffic -> Giao dịch/W2A -> Leads -> Đơn/User mới).
> 4. Chỉ rõ Điểm nghẽn và rủi ro thực tế (Radical Candor / Lowlights).
> 5. Ma trận kết luận 3 cột: BÀI HỌC | BẰNG CHỨNG | NEXT ACTION.
> 6. Không En/Em dash, không gán nhãn mức độ ưu tiên, không chữ "SSOT", không tên riêng cá nhân.

```markdown
# BÁO CÁO TIẾN ĐỘ TUẦN [Số tuần] ([Từ ngày] - [Đến ngày]): WEB PLATFORM

> **Kỳ báo cáo:** Tuần [Số tuần] ([Từ ngày] - [Đến ngày]) | **Cập nhật:** [Ngày/Tháng/Năm]
> **Đội ngũ thực hiện:** Web Platform
> **Nguồn dữ liệu:** GA4 Data API (Property 270743103), BigQuery Data Warehouse, AppsFlyer GPD Attribution Engine, MoSpark CMS.

---

## I. TỔNG QUAN HIỆU SUẤT TUẦN & TÁC ĐỘNG KINH DOANH

### [ACTION TITLE]: [Chủ thể Kênh Web] + [Số liệu tuần & Tăng trưởng WoW/YoY] + [Ý nghĩa kinh doanh cốt lõi]
*(Ví dụ: Tuần 46: Kênh Web chạm mốc 1.18M PV lũy kế MTD, bứt phá nhờ đợt kích cầu 11.11 và bộ đôi tiện ích Thuế mới lên Production)*

#### 1. Bốn Thẻ Chỉ Số Trọng Tâm 3 Tầng (Key Performance Cards)
- **Quy mô lưu lượng (Pageviews):** **[Số PVs]** | `↑ [X]% vs Tuần trước: [Số PV cũ]` (hoặc `↑ [X]x`) | `[Ý nghĩa: % hoàn thành kế hoạch tháng / Đóng góp toàn sàn]`
- **Người dùng thực tế (Users):** **[Số Users]** | `↑ [X]% vs Tuần trước: [Số User cũ]` | `[+Số lượng user mới tăng thêm so với tuần trước]`
- **Chuyển tiếp Web-to-App (W2A Clicks):** **[Số Clicks]** | `[X]% CVR trên lượt truy cập` | `[Kênh đóng góp chính: Banner, Nút tương tác, OneLink]`
- **Khách hàng mới ngoài App MoMo:** **[Tỷ lệ % hoặc Số lượng]** | `[X]% người dùng chưa từng có ví/app MoMo` | `[Bảo chứng giá trị gia tăng độc quyền của Kênh Web]`

#### 2. Bảng Cơ Cấu Kênh Lưu Lượng Tuần (Non-Paid vs. Paid)

| Kênh lưu lượng | Tuần trước | Tuần này | Tỷ trọng tuần (%) | Biến động WoW (%) | Nhận định & Tín hiệu điều hành |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **KÊNH TỰ NHIÊN (NON-PAID)** | **[Số]** | **[Số]** | **[Tỷ trọng]%** | **[+/-]%** | Động cơ tăng trưởng tự nhiên cốt lõi |
| - Organic Search | [Số] | [Số] | [Tỷ trọng]% | [+/-]% | Lưu lượng tìm kiếm tự nhiên chủ lực |
| - Direct Traffic | [Số] | [Số] | [Tỷ trọng]% | [+/-]% | Nhận diện thương hiệu và thói quen quay lại |
| - Referral | [Số] | [Số] | [Tỷ trọng]% | [+/-]% | Liên kết đối tác, in-app và mạng xã hội |
| - AI Search (GEO) | [Số] | [Số] | [Tỷ trọng]% | [+/-]% | Tăng trưởng từ ChatGPT, Gemini, Perplexity |
| **KÊNH TRẢ PHÍ (PAID ADS)** | **[Số]** | **[Số]** | **[Tỷ trọng]%** | **[+/-]%** | Ngân sách quảng cáo có chọn lọc dẫn dòng chuyển đổi |
| **TỔNG LƯỢNG TRUY CẬP** | **[Số]** | **[Số]** | **100,0%** | **[+/-]%** | Nhịp ngày bình quân đạt [Số] PV/ngày |

---

## II. TIẾN ĐỘ THỰC TẾ CÁC DỰ ÁN CHIẾN LƯỢC (USE CASES DEEP-DIVE)

### 1. [Tên Dự Án / Hub Trọng Điểm 1] (Ví dụ: Cinema Hub)
> **[ACTION TITLE]:** [Câu kết luận về kết quả đạt được của Hub trong tuần]

#### a. Phễu Chuyển Đổi 4 Bước (4-Stage Funnel Grid)
- **Bước 1 (Traffic Web):** **[Số] PVs** | `↑ [X]% vs Tuần trước: [Số]` | `[Thị phần/Đóng góp toàn Hub]`
- **Bước 2 (Trang giao dịch/Lịch chiếu):** **[Số] PVs** | `[X]% traffic đi tiếp vào bước giao dịch` | `[So sánh với tuần trước]`
- **Bước 3 (Click đặt vé/W2A):** **[Số] Clicks** | `[X]% CTR trên trang giao dịch` | `[Số lượng chuyển tiếp sang app]`
- **Bước 4 (Đơn hàng/Chốt đơn):** **[Số] Đơn** | `[Tăng trưởng/Doanh thu GMV tạo ra]` | `[Khách hàng mới]`

#### b. 3 Thẻ Đánh Giá Chiến Lược & Điểm Nghẽn (Insights & Bottlenecks)
- **Thứ hạng tìm kiếm (Ranking SEO):** [Số lượng] từ khóa Top 1 - 3 Google Search; độ phủ từ khóa [ngành hàng].
- **Mức độ nhận diện mới (Awareness Lift):** [X]% người dùng tương tác là khách hàng chưa từng dùng dịch vụ trên app.
- **Điểm nghẽn cần tháo gỡ (Lowlights):** [Nêu thẳng thắn tỷ lệ rơi rớt, lỗi kỹ thuật, hoặc độ hụt traffic so với kỳ vọng kèm nguyên nhân gốc rễ].

---

### 2. [Tên Dự Án / Hub Trọng Điểm 2] (Ví dụ: Financial Hub / Vehicle Hub)
*(Áp dụng đồng nhất cấu trúc Phễu 4 bước và 3 Thẻ đánh giá như trên)*

---

## III. MA TRẬN KẾT LUẬN & KẾ HOẠCH HÀNH ĐỘNG TUẦN TỚI (ACTION MATRIX)

Thay thế danh sách gạch đầu dòng truyền thống bằng ma trận 3 cột khép kín quan hệ nhân quả:

| BÀI HỌC (Insight Vận Hành Tuần) | BẰNG CHỨNG (Data Proof Dữ Liệu Sạch) | NEXT ACTION (Hành Động Trọng Tâm 7 Ngày Tới) |
| :--- | :--- | :--- |
| **[Đúc kết nguyên lý 1]** | [Con số, tỷ lệ % thực chứng từ dữ liệu tuần] | **[Việc làm cụ thể của đội ngũ chuyên môn]** |
| **[Đúc kết nguyên lý 2]** | [Con số, tỷ lệ % thực chứng từ dữ liệu tuần] | **[Việc làm cụ thể của đội ngũ chuyên môn]** |
| **[Đúc kết nguyên lý 3 (Điểm nghẽn)]** | [Con số phản ánh sự sụt giảm hoặc tỷ lệ rơi rớt] | **[Giải pháp khắc phục, A/B test hoặc tối ưu kỹ thuật]** |

---

## IV. PHỐI HỢP LIÊN ĐỘI NGŨ & CHÂN TRANG ĐẦU TƯ (COLLABORATION & FOOTNOTE)

- **BU Movies / Financial Services / Đối tác:** [Nội dung cần thống nhất hoặc phê duyệt trong tuần tới].
- **Chân trang đầu tư (Footer):** Chi phí vận hành tuần (SEO/SEM nếu có) | Khung thời gian chốt số liệu: [Từ ngày] - [Đến ngày].
```

---

## 5. MẪU BÁO CÁO THÁNG DÀNH CHO ANH TƯỜNG (MONTHLY TEMPLATE)

```markdown
# BÁO CÁO TỔNG QUAN THÁNG - WEB PLATFORM
**Tháng:** [Tháng/Năm] | **Khung Mục Tiêu Năm 2026:** Kịch bản Cơ sở 5M MUV - Kịch bản Bùng nổ 6M MUV

## 1. SỨC KHỎE PHỄU TOÀN DIỆN (FULL-FUNNEL TRACKING - 6 MONTHS)

| Chỉ Số Đo Lường | Tháng 03 | Tháng 04 | Tháng 05 | Tháng 06 | Tháng 07 | MoM (%) | YoY (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TẦNG WEB METRICS** | | | | | | | |
| Page Views (Attention) | 3.221.705 | 2.699.883 | 3.273.707 | 3.311.429 | 3.167.821 | -4.3% | +18.5% |
| Sessions (Attention) | 2.347.190 | 1.859.048 | 2.330.499 | 2.451.799 | 2.617.774 | +6.7% | +24.1% |
| MEU (Interest) | 1.686.392 | 1.427.165 | 1.706.739 | 1.675.301 | 1.728.912 | +3.2% | +21.0% |
| Click-to-App (Desire) | -- | -- | 964.893 | 824.309 | 713.318 | -13.4% | -- |
| **TẦNG APP IMPACT** | | | | | | | |
| Login App (W2A Users) | -- | -- | 180.148 | 248.468 | 224.162 | -9.8% | +35.2% |
| New Install (Appsflyer) | -- | -- | 1.737 | 4.486 | 5.242 | +16.9% | +180.0% |
| CVR (MEU -> New Install) | -- | -- | 0.10% | 0.27% | 0.30% | +0.03pp | +0.20pp |

> **Observation:** 
> 1. Sessions tăng +6.7% và MEU tăng +3.2% chứng minh chất lượng lưu lượng truy cập cải thiện dù Pageviews giảm nhẹ; Organic Search tăng trưởng +14.5% bù đắp hiệu quả cho Paid Search.
> 2. Lượng cài đặt mới (New Install) tăng trưởng liên tục 3 tháng, đạt 5.242 lượt (+16.9% MoM) nhờ tối ưu hóa các điểm chạm dẫn dắt gói quà người dùng mới.
> 
> **Problem Statement:** 
> 1. Làm thế nào để mở rộng CVR từ MEU sang New Install từ mốc 0.30% lên mốc 1.00% (tương đương ~17.000 New Installs/tháng) thông qua mô hình "Trải nghiệm trước, Cài đặt sau"?
> 2. Làm thế nào để duy trì đà tăng trưởng tự nhiên (Organic) trong bối cảnh các công cụ tìm kiếm AI (AI Overview) làm sụt giảm CTR chung của thị trường?

---

## 2. TIẾN ĐỘ 5 DỰ ÁN CHIẾN LƯỢC THEO MÔ HÌNH 4 ZONE

| Phân Vùng | Dự Án Chiến Lược | Mục Tiêu Kênh Web | Mục Tiêu Tác Động App | Tình Trạng Thực Thi & Kết Quả |
| :--- | :--- | :--- | :--- | :--- |
| **Performance** | Cinema Hub | 8.0M Pageviews<br/>1.7M Clicks | 76K Login App<br/>214K Vé bán | Đang tái cấu trúc sang MoSpark; thử nghiệm luồng thanh toán QR trực tiếp ngoài Web. |
| **Transformation**| Vehicle Hub | 500K Traffic<br/>50% W2A CR | 250K Login App<br/>100K Hồ sơ xe | Phạt Nguội đạt 267K views; chuẩn bị ra mắt Master Page `/tien-ich-giao-thong` và Spoke Giá Xăng. |
| **Transformation**| Financial Hub | 1.0M Traffic<br/>50% W2A CR | 500K MEU In-App<br/>Đón sóng 8M CIC | Hoàn tất đóng gói 4 công cụ (CIC, Vay Nhanh, VTS, Bảo hiểm); chuẩn bị chiến dịch CIC toàn dân. |
| **Incubator** | Student Pass Hub | 500K Traffic (Peak) | 15K Sinh viên định danh | Xây dựng cổng cẩm nang trường đại học; triển khai thử nghiệm tại 5 trường trọng điểm TP.HCM. |
| **Incubator** | New User Hub | TBU | 30K New Installs/tháng | Vận hành mô hình Utility Store; kết hợp gói quà CHAOMOMO giảm rào cản chuyển đổi. |

---

## 3. NĂNG LỰC NỀN TẢNG MOSPARK & TỰ ĐỘNG HÓA VẬN HÀNH

- **GenAI Content Pipeline:** Sản xuất [Số] bài viết/tháng; thời gian sản xuất 4-5 phút/bài; chi phí 7.000 - 20.000 VNĐ/bài; giải phóng 90% thời gian vận hành thủ công so với trước đây.
- **Landing Page Builder & Self-serve:** Triển khai mô hình tự phục vụ cho các BU; chuẩn hóa [Số] mẫu template có sẵn (chiếm 37% nhu cầu); rút ngắn thời gian khởi tạo trang từ 1-2 tuần xuống còn 1-2 ngày.
- **Hệ Thống Kiểm Soát Chất Lượng (Guardrails):** Tích hợp bộ lọc tự động kiểm tra tiêu chuẩn SEO/Compliance trước khi cho phép xuất bản trang, bảo vệ uy tín tên miền `momo.vn`.

---

## 4. PHỐI HỢP LIÊN PHÒNG BAN & HỖ TRỢ CHIẾN LƯỢC (CROSS-TEAM COLLABORATION)

- **Executive Leadership / Ban Giám Đốc:** Định hướng phê duyệt chủ trương liên kết dữ liệu với C08 và Cổng Dịch vụ công Quốc gia để xử lý luồng nộp phạt vi phạm giao thông và xuất biên lai điện tử.
- **Inbound Team (BMC):** Tiếp nhận vai trò điều phối và chịu trách nhiệm toàn diện về chất lượng nội dung, phê duyệt xuất bản theo mô hình Agency nội bộ.
- **Các Business Units (BUs):** Đăng ký chỉ tiêu kinh doanh cụ thể (Single Ownership KPI) trước khi yêu cầu triển khai các dự án Custom Landing Page.

---

## 5. KẾ HOẠCH HÀNH ĐỘNG 30 NGÀY TỚI (PRIORITIES FOR NEXT 30 DAYS)

| Nhóm Dự Án | Thời Gian | Tên Hạng Mục | Chi Tiết Triển Khai & Mục Tiêu |
| :--- | :--- | :--- | :--- |
| **Performance** | Tháng 08/2026 | Tối ưu Cinema Booking | Mở rộng thanh toán QR Web trực tiếp; tích hợp Deep Linking cho lịch chiếu phim. |
| **Transformation** | Tháng 08/2026 | Ra mắt Master Giao Thông | Go-live `/tien-ich-giao-thong` và Spoke Giá Xăng; tích hợp khối bán chéo Bảo hiểm Ô tô/Xe máy. |
| **Transformation** | Tháng 08/2026 | Hoàn thiện Financial Hub | Tích hợp bộ giả lập tài chính vào các bài viết cẩm nang; thử nghiệm luồng tính điểm CIC. |
| **Incubator** | Tháng 08/2026 | Thử nghiệm Student Pass | Ra mắt chuyên trang Review Trường Học; kích hoạt mạng lưới đại sứ sinh viên. |
| **Platform & AI** | Tháng 08/2026 | Nâng cấp MoSpark Engine | Nâng công suất GenAI lên 150 bài/tháng; mở rộng phân quyền Self-serve cho Cell Teams. |
```

---

## 7. BỘ FRAMEWORK QUẢN TRỊ KỊCH BẢN 4M PAGE VIEWS & BỘ CHỈ SỐ QUẢN TRỊ

> **Mục tiêu North Star:** Kịch bản bứt phá tổng lưu lượng Web Platform về mốc **4.000.000 Page Views vào Tháng 12/2026**.
> **Mẫu bảng tính tham khảo:** [full_month_performance_template.csv](../07_REPORTS/templates/sheets/full_month_performance_template.csv). Workbook framework cũ đã được loại bỏ, không còn là nguồn bắt buộc.

Mọi bài báo cáo Weekly cho Executive Leadership và Monthly cho Ban Giám Đốc **BẮT BUỘC phải áp dụng bộ chỉ số phễu 3 tầng hoàn chỉnh**:

### 7.1. Bộ Chỉ Số Phễu 3 Tầng Chuẩn (Full-Funnel Metric Framework)

| Tầng Phễu | Tên Chỉ Số (Key Metrics) | Công Thức / Nguồn GA4 & AppsFlyer | Ý Nghĩa Quản Trị & Đánh Giá |
| :--- | :--- | :--- | :--- |
| **Đầu Phễu (Traffic & Audience)** | **1. Tổng Page Views** | Tổng lượt xem trang từ TẤT CẢ các nguồn. | Quy mô lưu lượng toàn sàn. |
| | **2. Total Users (Unique Visitors)** | Số người dùng duy nhất (`totalUsers` từ GA4). | Quy mô khách thực tế tiếp cận được (tránh ảo số do 1 người F5 tải lại nhiều lần). |
| | **3. PV / User (Độ Sâu Tương Tác)** | `= Tổng Page Views / Total Users` | Mức độ tương tác trung bình (healthy: 1.5 - 2.5 trang/người). |
| | **4. Net Add (Lưu Lượng Mới)** | `Current Month PV - Previous Month PV` | Chỉ báo nỗ lực tạo ra giá trị tăng trưởng mới. |
| | **5. Growth Rate (%)** | `Net Add / Previous Month PV` | Tốc độ tăng trưởng MoM/WoW. |
| | **6. Phân Bổ Kênh (Source Breakdown)** | Tỷ trọng các nhóm kênh: Non-Paid (Organic Search, Direct, Referral, AI Traffic) và Paid Ads. | Phân định kênh sức mạnh chủ lực và kênh suy giảm. |
| | **7. Cơ Cấu Theo Dự Án / Use Case** | Phân bổ theo Cinema Hub, Financial Hub, Vehicle Hub, Home Page, TikTok... | Xác định use case tạo lực đẩy và use case cần tối ưu. |
| **Giữa Phễu (Intent & CTA)** | **8. Click-to-App** | Tổng lượt nhấp vào các nút CTA mở App MoMo. | Đo lường ý định chuyển đổi sang ứng dụng. |
| | **9. Tỷ Lệ %CTR** | `= Click-to-App / Tổng Page Views` | Hiệu quả của thông điệp và vị trí nút bấm CTA. |
| **Cuối Phễu (App Conversion & Growth)** | **10. Login App (Khách Cũ)** | Sự kiện xác thực mở App thành công từ Web. | Mức độ tái kích hoạt người dùng hiện hữu. |
| | **11. Install App** | Lượt tải và cài đặt ứng dụng mới từ Web. | Năng lực kéo người dùng mới ngoài App. |
| | **12. New Registered Users (Mới Tinh)** | Tracking qua AppsFlyer / BigQuery (`first_open` + eKYC). | **KPI Cốt Lõi:** Số người dùng mới hoàn tất đăng ký MoMo lần đầu từ nguồn Web. |
| | **13. Re-install Users (Cài Lại)** | `= Install App - New Registered Users` | Khách cũ từng xóa App nay cài đặt lại. |

### 7.2. Phương Pháp Luận So Sánh Đối Soát (Benchmark Methods)

* **SPLM (Same Period Last Month):** So sánh tuần/tháng hiện tại với cùng kỳ tháng trước (`Vs. SPLM`) để triệt tiêu yếu tố mùa vụ (Seasonal factors), tránh đưa ra nhận định sai lầm do biến động thị trường.
* **FULL MONTH:** Đánh giá bức tranh toàn cảnh cả tháng, đối soát song song giữa số liệu tích lũy lũy kế MTD, số chạy dự báo (Run-rate Forecast) và Target cam kết với BU.

---

## 8. DANH MỤC KIỂM TRA CHẤT LƯỢNG BÁO CÁO (QUALITY CHECKLIST)

Trước khi gửi báo cáo Weekly cho Executive Leadership hoặc Monthly cho Ban Giám Đốc, bắt buộc rà soát hai nhóm.

### Nhóm A: Quy chuẩn công ty (theo [`03_SKILLS/momo-reporting-guidelines.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/03_SKILLS/momo-reporting-guidelines.md))

1. **Mục đích:** Mỗi slide/mục có dòng `Mục đích` nói được trong một câu slide này giúp ai hiểu hoặc quyết định điều gì chưa?
2. **Title:** Chỉ đọc lần lượt các tiêu đề có nắm được toàn bộ câu chuyện báo cáo chưa? Tiêu đề là kết luận kèm số, không phải tên chủ đề, và viết sentence case?
3. **Số ý chính:** Mỗi slide 1-2 ý, tối đa 3 ý chưa? Nhiều hơn thì đã tách slide chưa?
4. **Tag:** Đã gắn `[R]` / `[D]` / `[F]` cho mọi slide chưa? Slide `[D]` có thật sự cần quyết định không?
5. **Độ tin cậy:** Mỗi số liệu có mốc so sánh (Target, kỳ trước), có việc tiếp theo, có nguồn và owner chưa?
6. **Thứ tự deck:** Discussion Topics đứng đầu, có slide Follow-up, Executive Summary có khối `Vấn đề cần cải thiện` chưa?
7. **Ngôn ngữ và cỡ chữ:** Toàn bộ báo cáo một ngôn ngữ, mọi tiêu đề cùng cỡ, mọi nội dung chính cùng cỡ chưa?
8. **Màu số liệu:** Đã tô theo mức đạt Target (xanh >= 100%, cam 90-99%, đỏ < 90%) chứ không tô theo biến động MoM chưa?

### Nhóm B: Đặc thù Web Platform

1. Đã xóa bỏ 100% Emoji / Icon trong toàn bộ tiêu đề, bảng biểu và danh sách chưa?
2. Đã thay thế toàn bộ tên riêng cá nhân/PIC bằng tên đội ngũ chuyên môn chưa?
3. Đã có đầy đủ 3 khối chuẩn: `Key Highlights & Business Impact`, `Collaboration`, `Priority` chưa?
4. Đã áp dụng Bộ Chỉ Số Phễu 3 Tầng (`Total PV`, `Total Users`, `PV/User`, `Click-to-App`, `Login`, `Install`, `New Registered Users`) chưa?
5. Đã tuân thủ chuẩn 4 kênh Non-Paid (Organic Search, Direct, Referral, AI Traffic) và gộp toàn bộ nguồn vãng lai vào Referral mà không tách dòng `Others` chưa?
6. Đã đối chiếu số liệu theo 2 tầng: Kênh Web và Tác động App chưa?
7. Các bảng số liệu lớn đã có 2 khối `Observation` và `Problem Statement` ở chân trang chưa?
8. Kế hoạch hành động đã được phân loại theo đúng nhóm phân vùng (Performance / Transformation / Incubator) chưa?

