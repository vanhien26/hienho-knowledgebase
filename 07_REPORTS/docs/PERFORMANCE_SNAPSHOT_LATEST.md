# BẢN GHI TÓM TẮT HIỆU SUẤT MỚI NHẤT (PERFORMANCE SNAPSHOT)

> **Cập nhật:** 14/11/2026 | **Kỳ dữ liệu:** Tháng 11/2026 (MTD 13 ngày: 01/11 - 13/11/2026, GA4 Data API, lọc chuẩn hostName == 'www.momo.vn')
> **Chính sách dữ liệu:** Đã loại bỏ hoàn toàn domain đối tác napthengay.vn (bao gồm toàn bộ các trang /order); giữ nguyên số liệu hiển thị thực tế trên website momo.vn.
> **Nguồn:** `07_REPORTS/data/monthly_11_2026_mtd_13d.json` & `07_REPORTS/data/summary.json`
> **Mục đích:** Bản ghi tinh gọn (Low-token) giúp AI Agents và quy trình tự động đọc số liệu nhanh mà không cần tải toàn bộ tài liệu lịch sử.

---

## 1. CHỈ SỐ TOÀN NỀN TẢNG (PLATFORM TOTALS)

| Chỉ số | Giá trị | Ghi chú & Đánh giá |
| :--- | :---: | :--- |
| **Target Tháng 11** | 3.829.155 PVs | Chỉ tiêu giao đầu tháng |
| **Thực tế Lũy kế MTD 13 ngày (Website momo.vn)** | **3.083.024 PVs** | Đạt **80.51%** Target (sau 43.3% thời gian) |
| **Nhịp vận hành ngày (Daily Pace)** | **237.156 PV/ngày** | Vượt tốc độ hoàn thành kế hoạch tháng |
| **Forecast cuối tháng (Forecast 30d)** | **7.114.671 PVs** | Dự báo đạt **185.80%** Target |
| **Tháng 10 gần nhất (Last Full)** | 3.602.023 PVs | Hoàn thành ~98.3% Target Tháng 10 (3.665.607 PVs) |
| **Users / Sessions MTD 13d (www.momo.vn)** | 665.881 / 881.738 | Tỷ lệ sessions/user ~1.32 |

---

## 2. CƠ CẤU NGUỒN LƯU LƯỢNG (NON-PAID VS. PAID DICHOTOMY)

> **Quy chuẩn chuẩn hóa:** Tách riêng 2 khối độc lập **Paid** (Marketing trả phí) và **Non-Paid** (Lưu lượng tự nhiên); trong đó Non-Paid gồm 4 kênh cốt lõi: Organic, Direct, AI Traffic (bóc tách từ GA4 AI Assistant) và Referral (đã gộp toàn bộ mạng xã hội tự nhiên, đối tác PR, Unassigned).

| Phân Loại Traffic Source | Lũy kế MTD 13d (PVs) | Tỷ trọng (%) | Xu hướng & Đánh giá Tín hiệu |
| :--- | :---: | :---: | :--- |
| **NON-PAID TRAFFIC** | **2.418.079** | **78.43%** | Động cơ tăng trưởng cốt lõi trên website momo.vn |
| -- Organic Traffic | 1.433.257 | 46.49% | Kênh tìm kiếm tự nhiên chủ lực |
| -- Direct Traffic | 775.066 | 25.14% | Lượng truy cập trực tiếp |
| -- Referral *(đã gộp Phần còn lại)* | 209.756 | 6.80% | Đối tác/backlink, in-app, PR, Organic Social (128.288 Ref + 81.468 Others) |
| -- AI Traffic (GEO, tính trong Non-Paid) | 23.139 | 0.75% | Lượng truy cập từ các nền tảng AI |
| **PAID TRAFFIC** | **659.848** | **21.40%** | Ngân sách Ads trên website momo.vn |
| **TỔNG LƯU LƯỢNG (momo.vn)** | **3.083.024** | **100.00%** | Đã loại trừ hoàn toàn napthengay.vn |

---

## 3. CƠ CẤU THEO 4 ZONES & HUBS (HUBS-MOMO MAPPING)

| Zone Phân loại | Hub | Lũy kế MTD 13d (PVs) | Target Tháng 11 | % Đạt Target |
| :--- | :--- | :---: | :---: | :---: |
| **Performance** | **Cinema Hub** | 745.200 | 1.294.630 | **57.56%** |
| **Transformation** | **Financial Hub** | 328.170 | 700.000 | **46.88%** |
| **Transformation** | **Vehicle Hub** | 229.148 | 100.000 | **229.15%** |
| **Transformation** | **New User Hub** | 96.738 | 300.000 | **32.25%** |
| **Incubator** | **Insurance Hub** | 79.506 | 50.000 | **159.01%** |
| **Incubator** | **Student Hub** | 2.699 | 100.000 | **2.70%** |

### Cơ Cấu Sub-pages Cinema Hub (Quy Chuẩn Tracking Mới):
- **Trang Rạp phim (`Cinema_Cineplex`):** **506.133 PVs** (67.9% Hub)
- **Trang phim chi tiết (`Cinema_Page`):** **167.540 PVs** (22.5% Hub)
- **Cinema_Home Page (Trang chủ Cinema):** **47.094 PVs** (6.3% Hub)
- **Cinema_Blog:** **21.243 PVs** (2.9% Hub)
- **Cinema_Landing Page:** **2.629 PVs** (0.4% Hub)
- **Tin tức (`Cinema_News`):** **561 PVs** (0.1% Hub)

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
