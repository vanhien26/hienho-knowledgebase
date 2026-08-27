# WEB PLATFORM x [BU_NAME] | [YEAR]

**Bối cảnh dự án:**
[Mô tả bối cảnh thị trường, mùa vụ, cơ hội và intent search của người dùng liên quan đến mảng sản phẩm. Ví dụ: H2/2026 là mùa Summer Camp, lễ 2/9...]

**Mục tiêu dự án:**
- Tăng cường khả năng hiển thị của [Use Case] trên các nền tảng Search Engine/AIO.
- Tăng trưởng X2 Total Traffic, trong đó trọng điểm là Organic Traffic.
- Tăng trưởng X2 các chỉ số cho luồng Web To App tác động đến MAU/Revenue.
- Xây dựng luồng tính năng [Tính năng Core - VD: đặt vé] và Thanh toán trực tiếp trên Web [Use Case].

---

## 1. Executive Summary

### Situation
- **Vị thế:** [Tên Web] có cấu trúc và tính năng sản phẩm đầy đủ của một Product Led Growth để trở thành một nền tảng giúp tăng trưởng.
- **Thực trạng & Định hướng:** Một thời gian dài, [Tên Web] chưa được đầu tư nâng cấp, tối ưu chuyên sâu về tính năng sản phẩm, nội dung và các hoạt động Offpage dẫn đến sự suy giảm về hiệu suất và không cạnh tranh được với các đối thủ. Trọng tâm [Timeframe] là tái cấu trúc toàn diện và chuyển dịch hạ tầng MoSpark Platform giúp khai thác các lợi thế AI-Powered nhằm phục hồi và thúc đẩy đà tăng trưởng.
- **Traffic:** [Số liệu Baseline Traffic]. Top [Rank] SERP "[Core Keyword]".
- **Ecosystem Flow:** Discovery (SERP/AIO) → Web (momo.vn/[slug]) → Transaction (App) → Retention.

### Complication
[Số lượng] vấn đề hiện trạng:
1. **Luồng Thanh toán (Payment Drop-off):** Thiếu cổng thanh toán trực tiếp trên Web. Tệp khách hàng chưa cài đặt MoMo (Non-App Users) sẽ drop hoàn toàn do rào cản tải ứng dụng.
2. **Search Market Gap:** Chưa tập trung mở rộng các từ khóa khám phá như [Keyword Category] (~[Volume] vol/tháng).
3. **AI Overview/AI Agent:** Chưa được tối ưu các hoạt động kỹ thuật và xây dựng [Entity] sẽ khó xuất hiện trong câu trả lời của LLM.
4. **[Product/Content] Life-Circle:** Đối với [Product item] đã hết [Life cycle] cần cơ chế xử lý và có thể tự động chuyển trạng thái, điều hướng người dùng sang các nền tảng/luồng khác để không lãng phí Traffic.

---

## 2. Business Objectives

### 2.1 Baseline & KPIs

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Metric</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">[Year-1] Full Year</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">[Qx/Year] (Baseline)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">[Hx/Year] (Actual)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">[Target Timeframe] (Target)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Organic Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Total Traffic</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Booking Clicks</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic to App (W2A Users)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Transactions (via App)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Specific Conversion Metric]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Value]</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>% W2A (CR)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Value]%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Value]%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Value]%</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>[Value]%+</strong></td>
    </tr>
  </tbody>
</table>

* **Ghi chú:**
- **Mục tiêu:** Uplift [X]% mọi chỉ số [Timeframe].
- **Thách thức:** W2A giảm xuống [X]% do thiếu luồng thanh toán Web. Giải pháp bắt buộc: Triển khai Native Web Payment để đạt target CR [X]%+.

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Competitor 1]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Strength]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Weakness]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Advantage]</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Competitor 2]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Strength]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Weakness]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Advantage]</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Competitor 3]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Strength]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Weakness]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Advantage]</td>
    </tr>
  </tbody>
</table>

---

## 3. Web Product Strategy

Mục tiêu Uplift [X]% [Timeframe] dựa trên 3 trụ cột chiến lược:

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
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phủ sóng tìm kiếm Out-App ([Keyword Domains]). Biến Web thành kênh Acquisition.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>2</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Topical Authority ([Domain])</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Xây dựng "Bách khoa toàn thư" [Domain]. Phát triển content sâu để rank Google AI.</td>
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

Dự án được vận hành dưới mô hình đối tác chiến lược giữa [BU_NAME] và khối Web Platform:

**1. [BU_NAME] (Business Owner)**
- **Business Ownership:** Nắm giữ quyền quyết định và chịu trách nhiệm toàn trình đối với kết quả kinh doanh (P&L, Doanh thu, New Users, MAU, Transactions).
- **Domain Strategy:** Hoạch định chiến lược kinh doanh và định hướng khai thác hệ sinh thái đối tác.
- **Exchange Link:** Làm việc với đối tác để trao đổi hoạt động truyền thông Off-Page.

**2. Web Platform (Product Development, Content Production & Growth Strategy)**
- **Product & Growth Ownership:** Sở hữu, định hướng và vận hành Trải nghiệm Sản phẩm (Web Product), tỷ lệ Chuyển đổi (CR) và Tăng trưởng Organic Traffic.
- **Trọng tâm thực thi [Timeframe]:**
  - **Product-Led Growth:** Triển khai PLG Framework cho [Use Case] Web trên nền tảng MoSpark.
  - **Product Migration:** Xây dựng và nâng cấp sản phẩm Web [Use Case] đáp ứng các tiêu chuẩn tối ưu được cập nhật mới về kiến trúc nền tảng, cấu trúc sản phẩm, tính năng kỹ thuật của Web Platform.
  - **Content Production:** Phối hợp xây dựng về chiến lược nội dung, sản xuất nội dung cho [Use Case] một cách tối ưu thời gian, chi phí thông qua việc áp dụng mạnh mẽ năng lực của AI-Powered trên MoSpark Platform.
