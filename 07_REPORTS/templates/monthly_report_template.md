# BÁO CÁO KINH DOANH & HIỆU SUẤT THÁNG [MM/YYYY] - WEB PLATFORM

> **Phân loại:** Monthly Business Review (Pre-read: `[R]`, Thảo luận: `[D]`)  
> **Nguyên tắc:** Report để cung cấp thông tin, Meeting để thảo luận và ra quyết định.  
> **Thời gian dữ liệu:** [01/MM] – [DD/MM/YYYY] (MTD [X] ngày)  
> **Nguồn SSOT:** `07_REPORTS/data/summary.json` & `07_REPORTS/web_performance_tracking.xlsx` (Sync với hubs-momo)  

---

## 1. TỔNG QUAN HIỆU SUẤT NỀN TẢNG (PLATFORM SUMMARY) `[R]`

| Chỉ số Cốt lõi | Tháng Trước (Full) | Tháng Này (Target) | Lũy Kế MTD ([X]d) | Dự Phóng Cuối Tháng | Đánh Giá Tỷ Lệ Đạt |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Total Pageviews** | [pv_prev] | [target_month] | [actual_mtd] | [forecast_month] | **[%_target]** |
| **Tốc Độ Ngày (Pace)** | [pace_prev]/ngày | [req_pace]/ngày | [daily_pace]/ngày | - | [pace_status] |
| **Chênh Lệch (Net Add)** | - | - | - | [gap_pv] | [so_what_net_add] |

### Phân Bổ Kênh Lưu Lượng (Channels Split):
- **Organic:** [pv_org] ([%_org]%) — [Đánh giá sức khỏe lưu lượng tự nhiên]
- **Direct:** [pv_dir] ([%_dir]%) — [Đánh giá lượng truy cập tiện ích trực tiếp]
- **Referral:** [pv_ref] ([%_ref]%) — [Đánh giá luồng giới thiệu đối tác]
- **Paid:** [pv_paid] ([%_paid]%) — [Đánh giá hiệu quả ngân sách quảng cáo/co-marketing]
- **Others:** [pv_oth] ([%_oth]%)

---

## 2. HIỆU SUẤT THEO 4 ZONES CHIẾN LƯỢC (HUBS-MOMO MAPPING) `[R]`

### A. Performance Zone: Cinema Hub
- **Lưu lượng MTD:** [pv_cinema] PVs / Target [target_cinema] PVs (Dự phóng: [fc_cinema] PVs - **[%_cinema]%**)
- **Key Highlights:** [Tối ưu CWV LCP, Mini Game tương tác, tiến độ migration rạp]
- **Next Shipments:** [Đầu việc cam kết ship trong tuần kế tiếp]

### B. Transformation Zone: Financial, Vehicle & New User Hubs
- **Financial Hub:** [pv_fin] PVs / Target [target_fin] PVs (Dự phóng: [fc_fin] PVs - **[%_fin]%**)
  * *Tiến độ công cụ:* [Trang chủ /tai-chinh, sub-pages tỷ giá, giá vàng, tích hợp API CCQ & tiết kiệm]
- **Vehicle Hub:** [pv_veh] PVs / Target [target_veh] PVs (Dự phóng: [fc_veh] PVs - **[%_veh]%**)
  * *Tiến độ:* [Trang Model xe Vinfast, API Phạt Nguội, Database Garage Cell Team]
- **New User Hub:** [pv_nu] PVs / Target [target_nu] PVs (Dự phóng: [fc_nu] PVs - **[%_nu]%**)
  * *Phễu Web-to-App:* [Game Quýt 2D/3D, cải tiến trang Download & Bonbon]

### C. Foundation Zone: Payment Hub
- **Lưu lượng MTD:** [pv_payment] PVs — [Game, Tiktok, Billpay, P2P, Data...] vận hành ổn định.

### D. Incubator Zone: Student & Travel Hubs
- **Student Hub:** [pv_student] PVs / Target [target_student] PVs — [Tiến độ gói hội viên sinh viên]
- **Travel Hub:** [pv_travel] PVs — [Tiến độ vé máy bay, vé tàu, khách sạn, eSIM]

---

## 3. TÍN HIỆU KỸ THUẬT & TÊN MIỀN (TECHNICAL SIGNALS) `[R]`

- **GSC Crawl Budget:** [req_per_day] req/ngày (Biến động: [delta_vs_last_month]%). Mã 200 OK đạt [pct_200]%; lãng phí 404 là [pct_404]% (~[wasted_req]/ngày). Tỷ lệ Discovery: [pct_discovery]%.
- **Backlink Authority:** [total_linking_pages] pages từ [total_ref_domains] domains. Nồng độ Top 2 site: [pct_top2]%. Danh mục toxic link cần disavow: [total_disavow_candidates] domains.

---

## 4. CHỦ ĐỀ THẢO LUẬN BAN GIÁM ĐỐC (DISCUSSION TOPICS) `[D]`

### Chủ Đề 1: [Vấn Đề Trọng Yếu 1 - Crawl / Technical / Gap Target]
- **Problem Statement:** [Mô tả ngắn gọn bản chất vấn đề]
- **Data Points:** [Số liệu minh chứng cụ thể]
- **Recommendations:** [Đề xuất giải pháp và quyết định cần BOM phê duyệt]

### Chủ Đề 2: [Vấn Đề Trọng Yếu 2 - Action Priorities Tuần Tới]
- **Problem Statement:** [Mô tả ngắn gọn]
- **Data Points:** [Số liệu minh chứng]
- **Recommendations:** [Đề xuất hành động]
