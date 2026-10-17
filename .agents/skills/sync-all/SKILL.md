---
name: sync-all
description: Đồng bộ toàn bộ dữ liệu Web Platform (Microsoft Clarity API, Web Performance Tracking MTD, Google Trends, Bing Copilot, Web Hubs Distribution).
---

# SKILL: MASTER DATA & API SYNCHRONIZATION PIPELINE (/sync-all)

## 1. MỤC TIÊU & TRIGGER
Kích hoạt khi người dùng gõ `/sync-all`, `/sync` hoặc đưa ra các yêu cầu tương tự:
- *"Sync toàn bộ dữ liệu"*
- *"Chạy đồng bộ tất cả các luồng API"*
- *"Cập nhật toàn bộ data Web Platform"*

## 2. QUY TRÌNH THỰC THI TỰ ĐỘNG (AUTOMATED WORKFLOW)

Khi nhận lệnh, AI Agent tự động thực thi script điều phối Master:
```bash
python3 scripts/sync_all_data.py
```

### Các Luồng Dữ Liệu Được Đồng Bộ:
1. **Web Performance Tracking MTD:**
   - Quét file Excel tracking mới nhất từ `/Users/hienhv/Downloads/`.
   - Trích xuất số ngày lũy kế MTD, lưu SSOT vào `07_REPORTS/web_performance_tracking.xlsx`.
   - Đẩy dữ liệu sang Web Hubs (`react-web-momo`) cho cả `/dashboard` và `/bang-tin`.
2. **Microsoft Clarity Data Export API:**
   - Kéo 4 requests: URL, Source/Medium, Channel, URL/Source.
   - Nhận diện traffic AI (`chatgpt.com`, `perplexity.ai`, `duck.ai`...), kênh `AiPlatform`.
   - Đo lường 5 chỉ số hành vi (Scroll Depth, Engagement Time, Dead Clicks, Rage Clicks, Quickbacks).
   - Cập nhật snapshot ngày và file SSOT `07_REPORTS/data/clarity/clarity_latest.json`.
3. **Google Trends Demand Validation:**
   - Quét rolling top themes ngành Tài Chính (Giá vàng, Tỷ giá, Vay tín chấp, Ví Trả Sau, Gửi tiết kiệm).
   - Cập nhật địa bàn tìm kiếm (Geo-intent) và các truy vấn tăng đột biến (Rising queries) vào `07_REPORTS/data/google_trends_validation.json`.
4. **Bing AI Performance Ingest:**
   - Tự động nhận diện và nạp các lượt trích dẫn Microsoft Copilot nếu có file export mới trong `Downloads/`.
5. **Web Hubs Distribution:**
   - Đồng bộ kho từ khóa Use Cases (`05_HUBS/inventory/`) sang repo giao diện `react-web-momo`.

## 3. TRÌNH BÀY BÁO CÁO TỔNG HỢP CHO NGƯỜI DÙNG (EXECUTIVE REPORT)
Sau khi script hoàn thành, trình bày bảng tóm tắt kết quả chuẩn Tech Lead / Product Lead:
- **Bảng trạng thái các luồng:** `Tên luồng` | `Trạng thái` | `Thời gian thực thi`.
- **Chỉ số hiệu suất Kênh Web:** Actual MTD PVs, % Target, Run-rate Forecast.
- **Chỉ số Traffic AI & Trải nghiệm:** Tổng AI Sessions, Top URL nhận traffic AI, Kênh AI phát hiện.
- **Quy chuẩn văn phong:** **KHÔNG dùng Emoji/Icon**, **KHÔNG nêu tên riêng cá nhân**, sử dụng **Markdown Tables** và gạch đầu dòng phân tích trực diện.
