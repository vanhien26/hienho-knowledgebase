# Web MoMo - OKRs 2026

**Vision:** Scale MoMo to Vietnam's #1 financial destination (6M visitors) via an Agentic, SEO/GEO-first platform that turns underserved market needs into high-authority traffic.

---

## Objective 1: Accelerate MoMo’s Financial Authority to 6M Monthly Visitors
- **Focus:** Growth, scale, and market dominance.

### Key Results (KRs)

| KR | Mô tả | Target | Baseline | Nguồn đo lường (SSOT) |
|----|-------|--------|----------|-----------------------|
| **KR 1.1** | Tăng lượng khách truy cập duy nhất hàng tháng (MUA) | **6.0 M** | 3.0 M | GA4 Raw Data (BigQuery) |
| **KR 1.2** | Đạt thứ hạng cao cho 50+ "Financial Underserved Keywords" | **Top 3-5** | Đang đo | GSC API |
| **KR 1.3** | Tỷ lệ chuyển đổi Web-to-App (Deep-link/Open App) | **[xx]%** | TBD (23/04) | GA4 + Appsflyer |
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

## Nguyên tắc đo lường
- **Single Source of Truth:** Mọi số liệu báo cáo lên sếp Công đều phải lấy từ **BigQuery** (không dùng UI GA4 để tránh sai số sampling).
- **Metric chính:** Monthly Unique Active Users (MUA) dựa trên `user_pseudo_id`.
