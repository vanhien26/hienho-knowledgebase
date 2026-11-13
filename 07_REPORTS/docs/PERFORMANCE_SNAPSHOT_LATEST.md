# BẢN GHI TÓM TẮT HIỆU SUẤT MỚI NHẤT (PERFORMANCE SNAPSHOT)

> **Cập nhật:** 13/11/2026 | **Kỳ dữ liệu:** Tháng 11/2026 (MTD 12 ngày: 01/11 - 12/11/2026, GA4 Data API, lọc chuẩn hostName == 'www.momo.vn')
> **Nguồn:** `07_REPORTS/data/monthly_11_2026_mtd_12d.json` & `07_REPORTS/data/summary.json`
> **Mục đích:** Bản ghi tinh gọn (Low-token) giúp AI Agents và quy trình tự động đọc số liệu nhanh mà không cần tải toàn bộ tài liệu lịch sử.
> **Lưu ý:** Mục 4 (GSC Technical SEO) còn giữ số liệu export kỳ 10/2026, chờ export GSC mới; không dùng kết luận mục này cho kỳ T11.

---

## 1. CHỈ SỐ TOÀN NỀN TẢNG (PLATFORM TOTALS)

| Chỉ số | Giá trị | Ghi chú & Đánh giá |
| :--- | :---: | :--- |
| **Target Tháng 11** | 3.829.155 PVs | Chỉ tiêu giao đầu tháng |
| **Thực tế Lũy kế MTD 12 ngày (Website momo.vn sạch)** | **866.188 PVs** | Đạt **22.62%** Target (sau 40.0% thời gian, đã khử vòng lặp GTM) |
| **Nhịp vận hành ngày (Daily Pace)** | **72.182 PV/ngày** | Cần đạt 164.609 PV/ngày trong 18 ngày tới để cán đích |
| **Forecast cuối tháng (Forecast 30d)** | **2.165.470 PVs** | Dự kiến đạt **56.55%** Target theo nhịp chạy tự nhiên |
| **Tháng 10 gần nhất (Last Full)** | 3.602.023 PVs | Hoàn thành ~98.3% Target Tháng 10 (3.665.607 PVs) |
| **Users / Sessions MTD 12d (www.momo.vn)** | 442.205 / 580.884 | Tỷ lệ PV/session đạt chuẩn 1.50 (đã loại bỏ 1,99 triệu PV ảo) |

---

## 2. CƠ CẤU NGUỒN LƯU LƯỢNG (NON-PAID VS. PAID DICHOTOMY)

> **Quy chuẩn chuẩn hóa:** Tách riêng 2 khối độc lập **Paid** (Marketing trả phí) và **Non-Paid** (Lưu lượng tự nhiên); trong đó Non-Paid gồm 4 kênh cốt lõi: Organic, Direct, AI Traffic (bóc tách từ GA4 AI Assistant) và Referral (đã gộp toàn bộ mạng xã hội tự nhiên, đối tác PR, Unassigned).

| Phân Loại Traffic Source | Lũy kế MTD 12d (PVs) | Tỷ trọng (%) | Xu hướng & Đánh giá Tín hiệu |
| :--- | :---: | :---: | :--- |
| **NON-PAID TRAFFIC** | **703.013** | **81.16%** | Động cơ tăng trưởng tự nhiên cốt lõi (T10: 3.128.542 PV, 86.9%) |
| -- Organic Traffic | 386.730 | 44.65% | Kênh chủ lực tự nhiên |
| -- Direct Traffic | 201.603 | 23.27% | Sức mạnh nhận diện thương hiệu |
| -- Referral *(đã gộp Phần còn lại)* | 114.680 | 13.24% | Đối tác/backlink, in-app, PR, Organic Social (34.308 Ref + 80.372 Others) |
| -- AI Traffic (GEO, tính trong Non-Paid) | 6.330 | 0.73% | Tăng trưởng từ ChatGPT, Gemini, Perplexity |
| **PAID TRAFFIC** | **163.175** | **18.84%** | Ngân sách Ads phục vụ chuyển đổi trọng điểm |
| **TỔNG LƯU LƯỢNG (momo.vn sạch)** | **866.188** | **100.00%** | Tổng chuẩn hóa: Paid + Non-Paid = 100% cân bằng |

---

## 3. CƠ CẤU THEO 4 ZONES & HUBS (HUBS-MOMO MAPPING)

| Zone Phân loại | Hub | Lũy kế MTD 12d (PVs) | Target Tháng 11 | % Đạt Target |
| :--- | :--- | :---: | :---: | :---: |
| **Performance** | **Cinema Hub** | 199.113 | 1.294.630 | **15.38%** |
| **Transformation** | **Financial Hub** | 85.522 | 700.000 | **12.22%** |
| **Transformation** | **Vehicle Hub** | 54.329 | 100.000 | **54.33% (Chưa về đích)** |
| **Transformation** | **New User Hub** | 24.068 | 300.000 | **8.02%** |
| **Incubator** | **Insurance Hub** | 20.863 | 50.000 | **41.73%** |
| **Incubator** | **Student Hub** | 756 | 100.000 | **0.76%** |

### Cơ Cấu Sub-pages Cinema Hub (Quy Chuẩn Tracking Mới):
- **Trang Rạp phim (`Cinema_Cineplex`):** **336.496 PVs** (68.1% Hub)
- **Trang phim chi tiết (`Cinema_Page`):** **110.190 PVs** (22.3% Hub)
- **Cinema_Home Page (Trang chủ Cinema):** **31.387 PVs** (6.4% Hub)
- **Cinema_Blog:** **13.709 PVs** (2.8% Hub)
- **Cinema_Landing Page:** **1.963 PVs** (0.4% Hub)
- **Tin tức (`Cinema_News`):** **339 PVs** (0.1% Hub)

---

## 4. TÍN HIỆU KỸ THUẬT & HỒ SƠ TÊN MIỀN (TECHNICAL SEO SIGNALS)

> **Trạng thái:** Số liệu dưới đây là export kỳ **10/2026**, CHƯA có export GSC mới cho T11. Chỉ dùng tham chiếu xu hướng, không kết luận hiện trạng.

- **GSC Crawl Stats (01/10 - 06/10/2026):**
  * Tốc độ: **14.850 req/ngày** (sụt giảm **-29.7%** so với Tháng 9; Download giảm -72%).
  * Mã trạng thái: 200 OK đạt 94.11%; **404 Not Found chiếm 4.14%** (lãng phí ~860 req/ngày).
  * Mục đích: Refresh 95.97% / **Discovery chỉ 4.03%** (bị chèn ép nội dung mới).
  * Rủi ro: Lag 2-6 tuần; tác động sụt giảm crawl dự kiến bộc lộ vào Organic traffic cuối T10/đầu T11 - **cần kiểm chứng trên số liệu T11**.
- **GSC Backlink Profile (10/10/2026):**
  * Quy mô: 1.000 referring sites, 118.757 linking pages.
  * Tập trung cực đoan: Top 2 site (TopCV + CVS) chiếm **79.9%** linking pages.
  * Authority bẫy: 94.925 link trỏ vào 7-11 URL careers, 0 link trỏ vào Hub thương mại.
  * Disavow Audit: **147 domain candidate** (353 linking pages), trong đó có 67 site cờ bạc/casino (A1 Gambling).

---

## 5. PHỄU CHUYỂN ĐỔI WEB-TO-APP (NEW USER ACQUISITION - APPSFLYER GPD)

> **Nguồn:** `07_REPORTS/data/analytics/gpd_momo_web_nov_2026.csv` | **Kỳ dữ liệu:** 01/11/2026 - 10/11/2026 (MTD 10 ngày)

| Tầng Phễu Chuyển Đổi | Lũy Kế MTD 10d | Nhịp Ngày (Daily Pace) | Dự Báo 30 Ngày | So Với T10 (Full: 11.143) | Đánh Giá Tín Hiệu |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Cài đặt ứng dụng (App Install)** | **3.171** | 317 lượt/ngày | 9.513 | -14,6% vs T10 | Tải app ổn định, nhịp đạt 317 lượt/ngày |
| **2. Đăng ký tài khoản (New Reg)** | **864** | 86 user/ngày | 2.592 | -33,6% vs T10 | CVR Install -> REG đạt 27,2% |
| **3. Liên kết ngân hàng (Map Bank)** | **533** | 53 user/ngày | **1.599** | -33,1% vs T10 | CVR REG -> Map giữ vững 61,7% (tương đương T10: 61,2%) |
| **4. Người dùng kích hoạt (Active MAU)** | **314** | 31 user/ngày | 942 | -26,6% vs T10 | Tỷ lệ kích hoạt đạt 58,9% trên Map Bank |

### Cơ Cấu Phễu Theo Nhóm Chiến Dịch (Campaign Placement):
| Nhóm Kênh / Placement | Installs | Tỷ Trọng | REG | CVR REG | Map Bank | CVR Map | Active MAU | End-to-End CVR |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **C.CHAOMOMO (Banner đại trà)** | 2.763 | 87,1% | 772 | 27,9% | 479 | 62,0% | 275 | 10,0% |
| **Cinema Hub (Rạp phim & Lotte)** | 224 | 7,1% | 58 | 25,9% | 38 | 65,5% | 27 | 12,1% |
| **WEB_BRT_C.CHAOMOMO (Đổi quà)** | 58 | 1,8% | 16 | 27,6% | 8 | 50,0% | 5 | 8,6% |
| **Bảo Hiểm (InsurTech)** | 53 | 1,7% | 13 | 24,5% | 6 | 46,2% | 5 | 9,4% |
| **Merchant Hub (Đối tác)** | 42 | 1,3% | 3 | 7,1% | 1 | 33,3% | 1 | 2,4% |
| **Financial Health** | 31 | 1,0% | 2 | 6,5% | 1 | 50,0% | 1 | 3,2% |
| **TỔNG CỘNG MTD 10 NGÀY** | **3.171** | **100,0%** | **864** | **27,2%** | **533** | **61,7%** | **314** | **9,9%** |

- **Phân bổ theo hệ điều hành:** Android đạt 1.651 Installs (52,1%) / 238 Map Bank (CVR 53,8%); iOS đạt 1.520 Installs (47,9%) / 295 Map Bank (CVR 69,9%, End-to-End CVR đạt 12,2% so với Android là 7,8%).
- **Điểm sáng Cinema Hub:** End-to-End CVR đạt 12,1%, dẫn đầu toàn bộ các nhóm vị trí đặt.
