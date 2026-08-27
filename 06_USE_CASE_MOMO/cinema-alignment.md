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
- **Business Model:** Commission per transaction (13 partner chains (CGV, Lotte, Galaxy, BHD, Beta, Cinestar, Mega GS, Cinemax, DCINE, Starlight, Rio, Trung Tâm Chiếu Phim Quốc Gia, AEON Beta): CGV, Lotte, Galaxy, v.v.).
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

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">2025 Full Year</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Q1/2026 (Baseline)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">H1/2026 (Actual)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">H2/2026 (Target)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">6,387,700</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1,066,000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2,010,041</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4,020,082</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Total Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">12,425,040</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2,980,000</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4,035,028</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">8,070,056</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Booking Clicks</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">266,258</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">81,517</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">870,467</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1,740,934</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic to App (W2A Users)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">78,735</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9,866</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">38,079</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">76,158</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactions (via App)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">52,311</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">9,212</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">48,830</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">97,660</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tickets Sold (Số vé bán)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">N/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">N/A</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">107,146</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">214,292</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>% W2A (CR)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>29.57%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>12.10%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>4.37%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>4.50%+</strong></td>
    </tr>
  </tbody>
</table>

> **\* Ghi chú:**
> - **Mục tiêu:** Uplift 100% mọi chỉ số H2/2026.
> - **Thách thức:** W2A H1 giảm xuống 4.37% do thiếu luồng thanh toán Web. Giải pháp bắt buộc: Triển khai Native Web Payment để đạt target CR 4.50%+.

### 2.2 Competitive Landscape

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Competitor</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Strengths</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Weaknesses</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">MoMo Advantage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">moveek.com</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Community review, long-tail phim indie</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không có transaction flow</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transaction liền mạch + ưu đãi</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">vnpay.vn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Similar payment infra, hub lịch chiếu per chain</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic base nhỏ, brand yếu</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoMo brand recall mạnh hơn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">cgv.vn, galaxycine.vn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Authority gốc của chuỗi</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User phải search từng chuỗi riêng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hub aggregator - Nhiều chuỗi rạp</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">rapchieuphim.com</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Content depth, long-tail location</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">UX cũ, không có payment</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">End-to-end flow</td>
    </tr>
  </tbody>
</table>

---

## 3. Web Product Strategy

Mục tiêu Uplift 100% H2/2026 dựa trên **3 trụ cột chiến lược**:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">#</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trụ Cột Chiến Lược</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trọng Tâm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>1</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Expand Out-App Traffic</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phủ sóng tìm kiếm Out-App (Phim rạp + OTT). Biến Web thành kênh Acquisition.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Topical Authority (Movies)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xây dựng "Bách khoa toàn thư" điện ảnh. Phát triển content sâu để rank Google AI.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>3</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Web Product</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chuyển dịch sang MoSpark. Trọng tâm: UX liền mạch & Triển khai luồng Web Payment.</td>
    </tr>
  </tbody>
</table>

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
