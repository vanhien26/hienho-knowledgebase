# BRD: Cinema

> - **Project:** Use Case Cinema - Web Growth Strategy Q2-Q4/2026
> - **Main URL:** momo.vn/cinema
> - **Division:** MDS (Marketing Distribution Services)
> - **Use Case:** Cinema
> - **Owner:** Web Platform
> - **Governance:** Web Product Lead (Hiến) | Lead Engineer (Hùng)
> - **Version:** 2.6 - Tháng 7/2026
> - **Status:** Approved (Aligned with BU Movies)

---

> **Vấn đề cốt lõi:** Khách hàng tìm lịch chiếu phim → Không thấy MoMo trên kết quả tìm kiếm → Lãng phí cơ hội thanh toán.
> **Mục tiêu dự án:** Tăng trưởng số lượng vé bán ra (Transactions) từ nguồn Web.
> **Hành trình mục tiêu:** Search Google → Vào Web MoMo → "Đặt vé ngay" → Thanh toán trực tiếp.

---

## 1. Executive Summary

### Situation
- **Vị thế:** Use Case trưởng thành và có tiềm năng lớn nhất của Web Platform.
- **Thực trạng & Định hướng:** Cinema là Use Case có tiềm năng giao dịch lớn, tuy nhiên chưa được tối ưu hóa chuyên sâu về mặt kỹ thuật và trải nghiệm trong các chu kỳ trước, dẫn đến sự suy giảm về hiệu suất. Trọng tâm H2/2026 là tái cấu trúc toàn diện và chuyển dịch hạ tầng sang nền tảng MoSpark nhằm phục hồi và thúc đẩy đà tăng trưởng.
- **Traffic:** ~1M organic/3 tháng Q1/2026. Top 1 SERP "vé xem phim", Top 3-5 cluster rạp.
- **Business Model:** Commission per transaction (8 partner chains: CGV, Lotte, Galaxy, v.v.).
- **Ecosystem Flow:** Discovery (SERP/AIO) → Web (momo.vn/cinema) → Transaction (App) → Retention.

### Complication
Mặc dù có Traffic lớn, tỷ lệ chuyển đổi hiện tại vẫn thấp do 4 vấn đề cốt lõi:
1. **Drop-off ở luồng Thanh toán:** Web chưa có cổng thanh toán trực tiếp. Tệp khách hàng Non-App bị giảm tỷ lệ chuyển đổi mạnh do rào cản yêu cầu tải ứng dụng.
2. **Keyword Gap quá lớn:** Bỏ lỡ hơn 280K search volume/tháng từ các từ khóa top ngành ("Phim chiếu rạp", "Rạp chiếu phim").
3. **Rủi ro từ Google AIO:** Nếu không tổ chức lại dữ liệu để Google AI đọc hiểu, MoMo sẽ mất lượng lớn Traffic do người dùng xem kết quả trực tiếp trên Google thay vì bấm vào Web.
4. **Nội dung lỗi thời do vận hành thủ công:** Trạng thái phim chưa được cập nhật tự động theo vòng đời. Phim hết suất chiếu rạp nhưng Web vẫn báo "Đang chiếu" gây trải nghiệm tệ. Hệ thống cần cơ chế tự động chuyển trạng thái và điều hướng người dùng sang các nền tảng OTT để không lãng phí Traffic.



---

## 2. Business Objectives

### 2.1 Hiện Trạng Performance

| Metric | 2025 Full Year | Q1/2026 (Baseline) | H1/2026 (Actual) | H2/2026 (Target) |
|---|---|---|---|---|
| Organic Traffic | 6,387,700 | 1,066,000 | 2,010,041 | 4,020,082 |
| Total Traffic | 12,425,040 | 2,980,000 | 4,035,028 | 8,070,056 |
| Booking Clicks | 266,258 | 81,517 | 870,467 | 1,740,934 |
| Traffic to App (W2A Users) | 78,735 | 9,866 | 38,079 | 76,158 |
| Transactions (via App) | 52,311 | 9,212 | 48,830 | 97,660 |
| Tickets Sold (Số vé bán) | N/A | N/A | 107,146 | 214,292 |
| **% W2A (CR)** | **29.57%** | **12.10%** | **4.37%** | **4.50%+** |

> **\* Ghi chú:**
> - **Mục tiêu:** Uplift 100% mọi chỉ số H2/2026.
> - **Thách thức:** W2A H1 giảm xuống 4.37% do thiếu luồng thanh toán Web. Giải pháp bắt buộc: Triển khai Native Web Payment để đạt target CR 4.50%+.

### 2.2 Competitive Landscape

| Competitor | Strengths | Weaknesses | MoMo Advantage |
|---|---|---|---|
| moveek.com | Community review, long-tail phim indie | Không có transaction flow | Transaction liền mạch + ưu đãi |
| vnpay.vn | Similar payment infra, hub lịch chiếu per chain | Traffic base nhỏ, brand yếu | MoMo brand recall mạnh hơn |
| cgv.vn, galaxycine.vn | Authority gốc của chuỗi | User phải search từng chuỗi riêng | Hub aggregator - Nhiều chuỗi rạp |
| rapchieuphim.com | Content depth, long-tail location | UX cũ, không có payment | End-to-end flow |

---

## 3. Web Product Strategy

Mục tiêu Uplift 100% H2/2026 dựa trên **3 trụ cột chiến lược**:

| # | Trụ Cột Chiến Lược | Trọng Tâm |
|---|---|---|
| **1** | **Expand Out-App Traffic** | Phủ sóng tìm kiếm Out-App (Phim rạp + OTT). Biến Web thành kênh Acquisition. |
| **2** | **Topical Authority (Movies)** | Xây dựng "Bách khoa toàn thư" điện ảnh. Phát triển content sâu để rank Google AI. |
| **3** | **Web Product** | Chuyển dịch sang MoSpark. Trọng tâm: UX liền mạch & Triển khai luồng Web Payment. |

---

## 4. Collaboration Model

Dự án được vận hành dưới mô hình đối tác chiến lược giữa BU Movies và khối Web Platform:

**1. BU Movies (Business Owner)**
- **Business Ownership:** Nắm giữ quyền quyết định và chịu trách nhiệm toàn trình đối với kết quả kinh doanh (P&L, Doanh thu, New Users, MAU, Transactions).
- **Domain Strategy:** Hoạch định chiến lược kinh doanh và định hướng khai thác hệ sinh thái đối tác (Rạp/OTT).

**2. Web Platform (Product & Tech Partner)**
- **Product & Growth Ownership:** Sở hữu, định hướng và vận hành Trải nghiệm Sản phẩm (Web Product), tỷ lệ Chuyển đổi (CR) và Tăng trưởng Organic Traffic.
- **Trọng tâm thực thi H2/2026:**
  - **Product-Led Growth:** Chuyển hóa luồng Booking thành hệ thống thu hút và giữ chân người dùng tự nhiên.
  - **MoSpark Migration:** Hiện đại hóa hạ tầng công nghệ, nâng cao khả năng chịu tải và tốc độ phát triển.
  - **GenAI Content:** Ứng dụng AI tự động hóa sản xuất nội dung theo Content Plan của BU Movies.
