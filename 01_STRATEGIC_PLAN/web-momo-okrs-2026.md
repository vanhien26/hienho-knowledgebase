# 🎯 Web Momo Okrs 2026
- OKRs 2026

**Vision:** Scale MoMo to Vietnam's #1 financial destination (6M visitors) via an Agentic, SEO/GEO-first platform that turns underserved market needs into high-authority traffic.

---

## Objective 1: Accelerate MoMo’s Financial Authority to 6M Monthly Visitors
- **Focus:** Growth, scale, and market dominance.

### Key Results (KRs)

| KR | Mô tả | Target | Baseline | Nguồn đo lường (SSOT) |
|----|-------|--------|----------|-----------------------|
| **KR 1.1** | Tăng lượng khách truy cập duy nhất hàng tháng (MUA) | **6.0 M** | 3.0 M | GA4 Raw Data (BigQuery) |
| **KR 1.2** | Đạt thứ hạng cao cho 50+ "Financial Underserved Keywords" | **Top 3-5** | Đang đo | GSC API |
| **KR 1.3** | Tỷ lệ chuyển đổi Web-to-App (Deep-link/Open App) | **12.5%** | 8.2% (Baseline 15/05/2026) | GA4 + Appsflyer |
| **KR 1.4** | Lưu lượng truy cập từ AI Referral (ChatGPT, Gemini,...) | **Đo lường được** | 0 | Custom BQ Referrer Filter |

---

## Chiến lược hành động (Action Plan)

1.  **Cấu trúc Nền tảng (Platform Structure):**
    *   Xây dựng hệ thống sản xuất nội dung nhanh & chất lượng (SEO/GEO-first) qua MoSpark.
    *   Tối ưu hóa hạ tầng kỹ thuật để các AI Engine dễ dàng trích dẫn (GEO Optimization).
2.  **Hợp tác & Kết nối (Enablement):**
    *   Phối hợp với Growth Team quốc tế để thu hút user mới và tái kích hoạt (reactivation).
    *   Làm việc với các BUs tài chính để đồng bộ hóa nội dung có thẩm quyền cao (High-authority content).
3.  **Tự doanh Nội dung (Own Content Team):**
    *   Thử nghiệm qua các Niche Use Case (ví dụ: Phạt nguội, CIC) để kiểm chứng hiệu quả.
    *   Tiến hành cải tổ toàn diện (Revamp) website momo.vn để tối ưu trải nghiệm cho người dùng mới.

---

## Nguyên tắc đo lường & Hypothesis Tăng trưởng MUV

**Nguyên tắc cốt lõi:**
- **Single Source of Truth:** Mọi số liệu báo cáo lên sếp Công đều phải lấy từ **BigQuery** (tuyệt đối không dùng UI GA4 để tránh sai số sampling và thresholding).
- **Metric chính:** Monthly Unique Active Users (MUA) đếm dựa trên `user_pseudo_id` (định danh thiết bị/trình duyệt của người dùng ẩn danh).

**Giả thuyết (Hypothesis) về Đo lường & Tăng trưởng:**
> *"Nếu chúng ta chuẩn hóa bộ đo lường sang BigQuery bằng metric `user_pseudo_id` kết hợp với tín hiệu tương tác thực tế (`session_engaged = 1`), chúng ta sẽ nhìn thấy chính xác 100% tệp người dùng ẩn danh từ kênh Out-App mà không bị nhiễu dữ liệu (bot/bounce). Nền tảng dữ liệu minh bạch này sẽ giúp team tối ưu hóa chính xác hiệu suất của từng cụm nội dung/tiện ích, từ đó tạo ra động lực tăng trưởng thực chất để vươn tới mốc 6 triệu MUA."*

**3 Key Results (KRs) hỗ trợ Hypothesis:**
- **KR 1 (Data Accuracy):** Hoàn thiện 100% Data Pipeline tự động hóa báo cáo MUA hàng tháng lấy nguồn trực tiếp từ BigQuery bằng truy vấn `COUNT(DISTINCT user_pseudo_id)`.
- **KR 2 (Traffic Quality):** Đảm bảo chất lượng traffic thu về bằng cách duy trì tỷ lệ [X]% trong tổng số `user_pseudo_id` có phát sinh phiên hoạt động gắn kết (`session_engaged = 1`).
- **KR 3 (Growth Attribution):** Đo lường và phân bổ chính xác (Attribution) tỷ trọng đóng góp vào 6 triệu MUA từ các nhóm Use Case chiến lược (VD: Phạt Nguội, CIC, Ví Trả Sau) dựa hoàn toàn trên Raw Data.
- **Baseline Date:** Dữ liệu chuẩn bắt đầu từ **23/04/2026** (Full Funnel Pipeline Go-live).

---

## Liên kết vận hành
- Điều phối dự án: [[orchestrator_engine]] — Pipeline Board theo dõi tiến độ Use Cases
- Đo lường Web Layer: [[web-tracking]] — GTM Config, Umami, AI Traffic Mapping
- Chuyển đổi Web→App: [[Web2App-Pipeline]] — CTA Design, Deeplink, Funnel CR
- Quy trình hàng ngày: [[operational_routine]] — Daily/Weekly/Monthly cadence
- Master Context: [[hienho_master_doc]] — Mục 5 (Dự án đang triển kh