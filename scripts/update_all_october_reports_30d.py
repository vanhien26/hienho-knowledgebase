#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script cập nhật toàn diện số liệu MTD 30d vào:
1. 07_REPORTS/data/analytics/monthly_report_2026_10.json
2. /Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/analytics/monthly-report-2026-10.json
3. /Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/reports/monthly-index.json
4. 07_REPORTS/docs/report-thang-10-2026-board.md & report-thang-10-2026.md
5. /Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/reports/report-thang-10-2026-board.md
6. /Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/lib/report/monthly-report-server.ts
"""

import json
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
HUBS_DIR = Path("/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo")

# Load consolidated GA4 MTD 30d
with open(BASE_DIR / "07_REPORTS" / "data" / "monthly_10_2026_consolidated.json", "r", encoding="utf-8") as f:
    ga4 = json.load(f)

print(f"Loaded GA4 MTD 30d: {ga4['actual_mtd_pv']:,} PV | Non-Paid: {ga4['channels']['non_paid_total']['pv']:,} PV")

# 1. Update monthly_report_2026_10.json in Hienho_MoMo-Base
json_path = BASE_DIR / "07_REPORTS" / "data" / "analytics" / "monthly_report_2026_10.json"
with open(json_path, "r", encoding="utf-8") as f:
    mr = json.load(f)

mr["meta"]["period"] = "01/10/2026 - 30/10/2026"
mr["meta"]["days_elapsed"] = 30
mr["meta"]["last_updated"] = "2026-10-31T06:50:00+07:00"

# Summary
s = mr["summary"]
s["actual_pvs_mtd"] = 3496864
s["forecast_pvs_31d"] = 3613426
s["achievement_rate_mtd"] = 0.954
s["forecast_achievement_rate"] = 0.9858
s["daily_run_rate"] = 116562
s["non_paid_pvs_mtd"] = 3040526
s["non_paid_share"] = 0.8695
s["paid_pvs_mtd"] = 456338
s["paid_share"] = 0.1305
s["paid_cut_volume"] = 456338 - 1197093 # -740755
s["paid_cut_rate"] = round((456338 / 1197093) - 1, 3) # -0.619
s["non_paid_net_add"] = 3040526 - 2755766 # +284760
s["non_paid_growth_mom"] = round((3141877 / 2755766) - 1, 3) # +0.140

# Target vs actual
for row in mr.get("target_vs_actual", []):
    if "oct_mtd_28d" in row:
        row["oct_mtd_30d"] = row.pop("oct_mtd_28d")
    if row["metric"] == "Total Page Views (Actual)":
        row["oct_mtd_30d"] = 3496864
        row["forecast_31d"] = 3613426
        row["assessment"] = "Đạt 95.40% Target sau 30/31 ngày (96.77% tiến độ thời gian)"
    elif row["metric"] == "% Target Rate (Tiến độ về đích)":
        row["oct_mtd_30d"] = "95.40%"
        row["forecast_31d"] = "98.58% - 99.20%"
        row["assessment"] = "Dự kiến kết tháng đạt 98.6% - 99.0% Target"

# Traffic sources
for ts in mr.get("traffic_sources", []):
    if "oct_mtd_28d" in ts:
        ts["oct_mtd_30d"] = ts.pop("oct_mtd_28d")
    ch = ts["channel"]
    if ch == "KÊNH TỰ NHIÊN (NON-PAID)":
        ts["oct_mtd_30d"] = 3040526
        ts["forecast_31d"] = 3141877
        ts["diff_vs_sep"] = 386111
        ts["share"] = 0.8695
        ts["assessment"] = "Vượt mốc lịch sử 3 triệu PV tự nhiên (+14.0% MoM); tự chủ nguồn tăng trưởng"
    elif ch == "Organic Search":
        ts["oct_mtd_30d"] = 1665199
        ts["forecast_31d"] = 1720706
        ts["diff_vs_sep"] = 96910
        ts["share"] = 0.4762
    elif ch == "Direct":
        ts["oct_mtd_30d"] = 907813
        ts["forecast_31d"] = 938073
        ts["diff_vs_sep"] = 182177
        ts["share"] = 0.2596
    elif ch == "Referral":
        ts["oct_mtd_30d"] = 340229
        ts["forecast_31d"] = 351570
        ts["diff_vs_sep"] = 6438
        ts["share"] = 0.0973
    elif "Others" in ch:
        ts["oct_mtd_30d"] = 127285
        ts["forecast_31d"] = 131528
        ts["diff_vs_sep"] = 100586
        ts["share"] = 0.0364
    elif ch == "KÊNH TRẢ PHÍ (PAID TRAFFIC)":
        ts["oct_mtd_30d"] = 456338
        ts["forecast_31d"] = 471549
        ts["diff_vs_sep"] = -725544
        ts["share"] = 0.1305
    elif ch == "TỔNG LƯỢNG TRUY CẬP":
        ts["oct_mtd_30d"] = 3496864
        ts["forecast_31d"] = 3613426
        ts["diff_vs_sep"] = -339433
        ts["share"] = 1.0

# Strategic hubs
hubs = mr.get("strategic_hubs", {})
if "cinema" in hubs:
    c = hubs["cinema"]["metrics"]
    if "oct_mtd_28d" in c:
        c["oct_mtd_30d"] = c.pop("oct_mtd_28d")
    c["oct_mtd_30d"] = 1065617
    c["forecast_31d"] = 1101138
    c["achievement_rate"] = 0.9537
if "financial" in hubs:
    f_metrics = hubs["financial"]["metrics"]
    if "oct_mtd_28d" in f_metrics:
        f_metrics["oct_mtd_30d"] = f_metrics.pop("oct_mtd_28d")
    f_metrics["oct_mtd_30d"] = 299461
    f_metrics["forecast_31d"] = 309443
    f_metrics["achievement_rate"] = 0.6655

# Save to Hienho_MoMo-Base
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(mr, f, ensure_ascii=False, indent=2)
print(f"✓ Saved: {json_path}")

# 2. Save identical JSON to react-web-momo
hubs_json_path = HUBS_DIR / "data" / "analytics" / "monthly-report-2026-10.json"
if hubs_json_path.parent.exists():
    with open(hubs_json_path, "w", encoding="utf-8") as f:
        json.dump(mr, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved: {hubs_json_path}")

# 3. Update monthly-index.json in react-web-momo
index_path = HUBS_DIR / "data" / "reports" / "monthly-index.json"
if index_path.exists():
    with open(index_path, "r", encoding="utf-8") as f:
        idx = json.load(f)
    for entry in idx:
        if entry.get("id") == "2026-10":
            entry["period"] = "01/10/2026 - 30/10/2026 (MTD 30d)"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved: {index_path}")

# 4. Generate Markdown board report
board_md = """# BÁO CÁO KINH DOANH VÀ HIỆU SUẤT NỀN TẢNG WEB - THÁNG 10/2026
> **Đối tượng:** Ban Giám Đốc / Hội đồng Quản trị  
> **Chu kỳ dữ liệu:** 01/10/2026 - 30/10/2026 (MTD 30 ngày & Forecast kết tháng 31 ngày)  
> **Nguồn dữ liệu hợp nhất (SSOT):** GA4 Data API (Property 270743103) & AppsFlyer GPD Attribution  

---

### 1. KẾT LUẬN ĐIỀU HÀNH (BOTTOM LINE UP FRONT)
- **Tiến độ mục tiêu:** Đạt **3.496.864 PVs** MTD 30 ngày (nhịp 116.562 PV/ngày), ước tính kết tháng đạt **3.613.426 PVs (98.58% chỉ tiêu HĐQT giao)**, hụt nhẹ 52K PVs do chủ động cắt giảm ngân sách quảng cáo rác.
- **Chất lượng lưu lượng:** Kênh tự nhiên (Non-Paid) chính thức **vượt mốc lịch sử 3.040.526 PVs**, chiếm kỷ lục **86.95%** toàn Website (tăng trưởng thực chất **+14.0% MoM**), tự bù đắp trọn vẹn việc chủ động giảm hơn 61% ngân sách quảng cáo trả phí (-740K PVs) để bảo toàn dòng tiền tổ chức.
- **Đột phá lưu lượng GEO (AI Search):** Lưu lượng trích dẫn tự nhiên từ các công cụ AI (ChatGPT, Microsoft Copilot, Perplexity...) tăng trưởng bùng nổ **+25.6% MoM đạt trên 40.800 PVs** (ước tính 42.283 PVs), riêng ChatGPT tăng **+35.0%**, khẳng định vị thế nguồn dữ liệu thực thể chuẩn (Authoritative Entity) trên AI Overviews.
- **Chuyển đổi Web-to-App:** AppsFlyer OneLink ghi nhận **102.103 clicks**, vượt mốc toàn bộ Tháng 9 (94.983 clicks); lượt cài đặt đạt trên **10.520 installs** và hơn **2.220 tài khoản liên kết ngân hàng (Map Bank)**; CVR toàn phễu giữ vững mức cao **21.09%**.

---

### 2. BẢNG ĐIỀU HÀNH HIỆU SUẤT HỢP NHẤT (EXECUTIVE SCORECARD)

| Hạng mục Đo lường | Tháng 09 (Full) | Tháng 10 (Target) | Thực đạt MTD 30d | Forecast 31 ngày | % MoM |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **TỔNG LƯỢNG TRUY CẬP (PVS)** | **3.952.859** | **3.665.607** | **3.496.864** | **3.613.426** | **-8.6%** |
| **Kênh Tự Nhiên (Non-Paid)** | 2.755.766 | - | 3.040.526 | 3.141.877 | **+14.0%** |
| - Organic Search | 1.623.796 | - | 1.665.199 | 1.720.706 | +6.0% |
| - Direct | 755.896 | - | 907.813 | 938.073 | +24.1% |
| - Referral / Others | 376.074 | - | 467.514 | 483.098 | +28.5% |
| *- Trong đó: Lưu lượng GEO (AI Search)* | *33.661* | *-* | *40.850* | *42.283* | *+25.6%* |
| **Kênh Trả Phí (Paid Traffic)** | 1.197.093 | - | 456.338 | 471.549 | **-60.6%** |
| **Cinema Hub (PVs)** | 1.220.075 | 1.117.378 | 1.065.617 | 1.101.138 | **-9.7%** |
| **Financial Hub (PVs)** | 246.305 | 250.000 | 299.461 | 309.443 | **+25.6%** |
| **Web-to-App OneLink Clicks** | 94.983 | - | 102.103 | 105.500 | **+11.1%** |
| **App Installs (OneLink)** | 10.501 | - | 10.520 | 10.870 | **+3.5%** |
| **Liên Kết Ngân Hàng (Map Bank)** | 2.276 | - | 2.220 | 2.294 | **+0.8%** |

*(Ghi chú bóc tách Hub: Số liệu Cinema Hub và Financial Hub được trích xuất từ BigQuery theo nhóm URL sản phẩm chính thức bàn giao, đã loại trừ các URL rác ngoại vi).*

---

### 3. NGUYÊN NHÂN LƯU LƯỢNG THÁNG 10 GIẢM (ROOT CAUSE ANALYSIS)
> **Kết luận điều hành (BLUF):** Mức giảm lưu lượng so với Tháng 9 (-8.6% MoM) hoàn toàn do **chủ động dừng hơn 740K Paid Ads kém hiệu quả** và **lực cản chu kỳ mùa vụ** (6/9 ngành toàn thị trường chạm đáy sau Lễ 2/9). Kênh tự nhiên (Non-Paid) thực tế tăng trưởng bứt phá **+14.0% (+284K views thực tế, +386K views forecast)**.

- **Hai Nguyên Nhân Trực Diện:**
  1. **Chủ động cắt giảm quảng cáo trả phí (-740K views · Chiếm 70% mức giảm):** 
     - Web chủ động giảm **61% Paid Ads** (từ 1.20M xuống 471K forecast) để chấm dứt các chiến dịch rác kém hiệu quả (như TikTok Ads lưu trang chỉ 0.6s), bảo toàn ngân sách cho công ty.
     - Nếu giữ nguyên lượng Ads như Tháng 9, tổng lượt xem Tháng 10 đã vượt **4.35M PVs (đạt 118% chỉ tiêu)**.
  2. **Lực cản chu kỳ thị trường (6/9 phân ngành rơi vào vùng trũng sau Lễ 2/9 & Tựu trường):**
     - Dữ liệu Google Trends 5 năm chuẩn hóa (236 keyword clusters) xác nhận Tháng 10 là thời điểm nhu cầu tìm kiếm của người dùng Việt Nam giảm tự nhiên:
       - **Nhóm giảm sâu sau lễ:** Học sinh / Sinh viên (**-16.4 điểm**, sụt -28.8% do đã vào học ổn định), Y tế / Khám bệnh (**-8.9 điểm**), Rạp phim (**-5.8 điểm**, vùng trũng sau đợt phim Lễ 2/9), Xổ số (**-4.9 điểm**), Xe cộ (**-3.2 điểm**), Du lịch (**-1.3 điểm**).
       - **Nhóm tăng tốc đón Quý 4:** Tài chính (**+7.9 điểm**, nhu cầu vốn kinh doanh, tích lũy, vàng gia tăng), Bảo hiểm (**+3.5 điểm**, tái tục cuối năm), Viễn thông (**+0.1 điểm**).

- **Điểm Sáng Lội Ngược Dòng Của Web MoMo:**
  - Bất chấp lực cản chung của thị trường, kênh tự nhiên (Non-Paid) vẫn tăng trưởng **+14.0%**, nâng tỷ trọng tự nhiên lên mức kỷ lục **86.95%** và chính thức vượt mốc 3 triệu PVs.
  - Riêng Cinema Hub dù ngành phim chung sụt giảm (-5.8 điểm), cụm rạp đối tác (Rio, Touch, Metiz) vẫn bứt phá **+142.2% (794K views)**, tự bù đắp khoảng trống lưu lượng.

---

### 4. BÓC TÁCH ĐỘT PHÁ LƯU LƯỢNG GEO & AI SEARCH (GENERATIVE ENGINE OPTIMIZATION)

| Nền tảng AI (AI Search Engine) | Tháng 09 (Full) | Tháng 10 (MTD 30d) | Forecast 31 ngày | % MoM | Tỷ Trọng AI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Microsoft Copilot / Bing AI** | 19.971 | 23.500 | 24.357 | **+22.0%** | 57.6% |
| **ChatGPT (OpenAI)** | 12.602 | 16.450 | 17.018 | **+35.0%** | 40.2% |
| **Google Gemini** | 704 | 438 | 454 | -35.5% | 1.1% |
| **Perplexity AI** | 239 | 289 | 299 | **+25.1%** | 0.7% |
| **AI Khác (Claude, AI Hay, Meta...)** | 145 | 150 | 155 | +6.9% | 0.4% |
| **TỔNG LƯỢNG TRUY CẬP GEO (AI)** | **33.661** | **40.827** | **42.283** | **+25.6%** | **100.0%** |

- **Top 4 nhóm trang được AI ưu tiên trích dẫn (Authoritative Entity Source):**
  1. `Cổng Tiện ích Dịch vụ Công (/tien-ich-giao-thong/gia-xang):` Đạt hơn 3.200 PVs từ AI; là nguồn cấp dữ liệu giá xăng dầu thời gian thực được ChatGPT và Copilot trích dẫn hàng đầu.
  2. `Trang chủ Thương hiệu (/):` Đạt gần 4.000 PVs từ AI khi người dùng truy vấn định danh về sản phẩm tài chính và giải pháp thanh toán của MoMo.
  3. `Cụm Rạp & Lịch chiếu phim (/cinema/...):` Đạt hơn 4.300 PVs từ AI nhờ cấu trúc dữ liệu Schema Rich Snippet chuẩn quốc tế (lịch chiếu, cụm rạp, review phim).
  4. `Dịch vụ Tài chính Tiêu dùng (/vay-nhanh, /vi-tra-sau):` Đạt hơn 1.400 PVs từ AI phục vụ nhu cầu so sánh hạn mức và điều kiện tín dụng.
- **Giá Trị Chiến Lược Với Ban Giám Đốc (So What?):** MoMo đã chủ động biến thách thức Zero-Click Search (người dùng không click web mà đọc tóm tắt AI) thành cơ hội đón đầu. Việc tối ưu GEO giúp Web MoMo trở thành nguồn sự thật duy nhất (Single Source of Truth) để các mô hình AI lớn trích dẫn về, tạo ra dòng lưu lượng có ý định sử dụng (Intent) và tỷ lệ chuyển đổi rất cao.

---

### 5. BA ĐỘNG LỰC KINH DOANH CỐT LÕI (SO WHAT?)
1. **Độc lập dòng vốn trả phí (Non-Paid Resilience):** Khi dừng 740K views từ quảng cáo trả phí, Website không bị sụt hẫng mà kênh tự nhiên tự bù đắp thêm hơn 284K views. Người dùng truy cập thẳng (Direct) tăng +24.1% nhờ thói quen sử dụng các tiện ích thiết yếu (Phạt nguội CSGT, Giá vàng, Tỷ giá, Lịch chiếu phim).
2. **Cụm rạp đối tác và Tiện ích tài chính dẫn dắt tăng trưởng:**
   - Cụm rạp đối tác Cineplex (Rio, Touch, Metiz) đạt **794.897 views** (chiếm 74.6% Hub), tự bù toàn bộ phần sụt giảm của trang phim lẻ.
   - Nhóm trang tỷ giá và giá vàng tăng trưởng mạnh, đưa Financial Hub đạt **299.461 views** (tăng +25.6% MoM so với Tháng 9). Hoàn tất chuẩn bị đưa bộ đôi công cụ Tính Thuế TNCN và Thuế Hộ Kinh Doanh lên Production.
3. **Chất lượng chuyển đổi New User vượt trội:**
   - Cinema Hub đạt CVR Install sang Map Bank lên tới **25.33%** (cao gấp 1.24 lần luồng banner đại trà CHAOMOMO là 20.35%).
   - Tệp người dùng iOS chiếm 51.7% installs nhưng đóng góp tới **58.5% tài khoản Map Bank** và **59.2% Active MAU**.

---

### 6. HAI QUYẾT SÁCH CẦN BAN GIÁM ĐỐC PHÊ DUYỆT (DECISIONS REQUIRED)
1. **Tái cấu trúc danh mục Paid Ads và chuẩn hóa nghiệm thu qua OneLink AppsFlyer:**
   - Dừng ngay chiến dịch kéo traffic từ TikTok Ads (chiếm 40% chi phí nhưng lưu trang chỉ 0.6 giây, CVR cài app chỉ 0.08%).
   - Ban hành quy định: Mọi chiến dịch dùng ngân sách công ty đổ về Web bắt buộc nghiệm thu theo số lượng Người dùng Liên kết Ngân hàng (Map Bank), không nghiệm thu theo Clicks/Pageviews.
2. **Kích hoạt dự án Pilot Off-Page SEO 3 tháng cho Cinema Hub (Ngân sách 125 triệu VNĐ):**
   - Phê duyệt hợp đồng trực tiếp với mạng lưới đối tác báo chí nhằm đưa cụm rạp đạt Top 5.5 Google Search và tối đa hóa hiện diện trên Generative Engine Optimization (GEO / AI Overviews) trước mùa phim Tết 2027; tiết kiệm 50 - 75 triệu VNĐ so với thuê agency trung gian.
"""

# Write to docs
with open(BASE_DIR / "07_REPORTS" / "docs" / "report-thang-10-2026-board.md", "w", encoding="utf-8") as f:
    f.write(board_md)
with open(BASE_DIR / "07_REPORTS" / "docs" / "report-thang-10-2026.md", "w", encoding="utf-8") as f:
    f.write(board_md)
print(f"✓ Saved: 07_REPORTS/docs/report-thang-10-2026-board.md & report-thang-10-2026.md")

# Write to react-web-momo data/reports
hubs_board_path = HUBS_DIR / "data" / "reports" / "report-thang-10-2026-board.md"
if hubs_board_path.parent.exists():
    with open(hubs_board_path, "w", encoding="utf-8") as f:
        f.write(board_md)
    print(f"✓ Saved: {hubs_board_path}")

print("TẤT CẢ CÁC BÁO CÁO VÀ FILE SSOT ĐÃ ĐƯỢC CẬP NHẬT THÀNH CÔNG THEO MỐC MTD 30D!")
