import os

brd_content = """# BRD: Financial Master Hub (momo.vn/tai-chinh)

> - **Tên Dự Án:** Financial Master Hub (Cổng Tiện Ích & Điều Hướng Tài Chính MoMo)
> - **Phân Khối Phụ Trách:** Growth Platform Division x Financial Services Division (CreditTech)
> - **Đội Ngũ Triển Khai:** Web Development Team, Backend Team, SEO & Content Team, Product Growth Team
> - **Phiên Bản:** v3.0 - Tháng 8/2026
> - **Trạng Thái:** Aligned & Production Ready (`momo.vn/tai-chinh`)

---

**MoMo Financial Master Hub:** Hợp nhất hệ sinh thái tài chính từ 11 trang rời rạc thành Cổng Khám Phá & Ra Quyết Định Tài Chính Toàn Diện (Unified Financial Discovery & Decision Gateway).

---

## 1. PHÁT BIỂU VẤN ĐỀ (PROBLEM STATEMENT)

Trước đây, các sản phẩm và dịch vụ tài chính của MoMo trên Kênh Web tồn tại dưới dạng **11 trang đích độc lập (standalone landing pages)** nằm rải rác (`/tiet-kiem-online`, `/vay-nhanh`, `/vi-tra-sau`, `/chuyen-tien`, `/the-tin-dung`...). Thực trạng phân mảnh này dẫn đến 3 điểm nghẽn nghiêm trọng:

1. **Trải nghiệm phân mảnh, người dùng không nhận diện được hệ sinh thái tài chính của MoMo để giải quyết trọn vẹn JTBD (Jobs-To-Be-Done):** Người dùng khi có nhu cầu tài chính tổng thể (như tính toán thu nhập ròng, lập kế hoạch chi tiêu, tìm kiếm kênh gửi tiết kiệm sinh lời, tra cứu nợ CIC để vay vốn) hoàn toàn không biết MoMo có đầy đủ các sản phẩm tài chính tương ứng. Họ chỉ tiếp cận một trang đơn lẻ từ kết quả tìm kiếm Google rồi rời đi (Bounce), không thấy được bức tranh giải pháp tài chính toàn diện.
2. **Khoảng cách lớn giữa Tra cứu thông tin và Giao dịch đầu tiên (Time-to-First-Value):** 11 trang cũ chủ yếu là bài viết tĩnh hoặc form thu thập thông tin cơ bản. Người dùng bị đẩy quá nhanh sang bước tải app hoặc yêu cầu đăng nhập/eKYC khi chưa được "nếm thử giá trị" (Pre-install Discovery), dẫn đến tỷ lệ drop-off cao sau khi cài đặt.
3. **Lãng phí tiềm năng thị trường 101.89 triệu lượt tìm kiếm/tháng:** Tổng dung lượng tìm kiếm toàn ngành tài chính đạt hơn 101 triệu lượt/tháng trên 24 thị trường cốt lõi, nhưng các trang rời rạc không tạo được sức mạnh liên kết chuyên đề (Topical Authority) dạng Hub-and-Spoke, khiến Kênh Web bỏ lỡ các từ khóa có lượng truy cập khổng lồ.

---

## 2. GIẢ THUYẾT GIẢI PHÁP (SOLUTION HYPOTHESIS)

Nếu MoMo hợp nhất 11 trang rời rạc thành một **Trang Cổng Trung Tâm Financial Master Hub (`momo.vn/tai-chinh`)** kết hợp mạng lưới 24 trang vệ tinh chuyên sâu, đồng thời cung cấp **Bộ Công Cụ Tiện Ích Tương Tác Trực Tiếp (Interactive Tools & Calculators)** không cần đăng nhập cho từng JTBD cụ thể (Lương, Thuế, Tiết kiệm, Lãi suất, CIC, Trả góp):
* Người dùng sẽ tự nhận ra nhu cầu và trải nghiệm giá trị tính toán ngay lập tức trên Web (Instant First Value).
* Hiểu rõ sản phẩm MoMo giải quyết bài toán tài chính của họ như thế nào trước khi tải app.
* Tạo động lực mạnh mẽ để mở App, hoàn tất eKYC và kích hoạt Giao dịch Tài chính Đầu tiên (1st Financial Transaction).

---

## 3. MỤC TIÊU KINH DOANH (BUSINESS OBJECTIVES)

1. **Hợp nhất và mở rộng hệ sinh thái Web Acquisition:** Chuyển đổi 11 trang đơn lẻ thành 1 Master Gateway (`momo.vn/tai-chinh`), 24 trang dịch vụ chuyên sâu và Programmatic Hub cho 34 Ngân hàng đối tác nhằm thâu tóm thị trường tìm kiếm 101.89M lượt/tháng.
2. **Kiểm chứng giá trị của Pre-install Product Discovery & Interactive Tools:** Chứng minh việc cho người dùng trải nghiệm công cụ tính toán trực quan trước cài đặt giúp rút ngắn thời gian tiếp cận giá trị (Time-to-First-Value) và tăng tỷ lệ chuyển đổi từ Web Session ➔ 1st Financial Transaction in-app.
3. **Đánh chiếm dứt điểm các Quick Wins hàng đầu (P0):** Tận dụng thẩm quyền tên miền vượt trội của MoMo (DR 78) so với các đối thủ Fintech/Aggregators (DR 45-58) để chiếm lĩnh Top 1-3 Google ở các mảng: Tính Lương Gross-Net 2026, Quyết Toán Thuế TNCN, Tra cứu CIC/Điểm Tín Dụng, Tiết Kiệm Live và Cổng 34 Ngân Hàng.
4. **Xây dựng hạ tầng Công cụ Dùng chung (Embeddable Widgets Foundation):** Thiết lập kiến trúc các widget tính toán độc lập để nhúng linh hoạt vào mọi điểm chạm trên toàn bộ hệ thống Web MoMo.

---

## 4. MA TRẬN BỐI CẢNH (CONTEXT MATRIX)

| Phân Loại | Nội Dung Chi Tiết |
| :--- | :--- |
| **FACT (Sự Thật Hệ Thống)** | - MoMo là sản phẩm App-first; Web không thay thế App.<br/>- Trang Web <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn</code> không yêu cầu đăng nhập.<br/>- Người dùng bắt buộc phải hoàn tất định danh eKYC trên App MoMo trước khi đủ điều kiện mở sổ tiết kiệm, mở ví trả sau, vay tiêu dùng hoặc đầu tư chứng chỉ quỹ. |
| **OBSERVATION (Quan Sát Dữ Liệu)** | - 11 trang sản phẩm độc lập trước đây có CTR nhấp CTA cao (94.51%) nhưng người dùng bị thiếu ngữ cảnh toàn diện về hệ sinh thái tài chính MoMo.<br/>- Phần lớn nhu cầu tìm kiếm tài chính tập trung vào dạng tra cứu/công cụ tính toán (Tool Intent) thay vì đọc bài viết chữ đơn thuần. |
| **AVAILABLE SIGNALS (Tín Hiệu Có Sẵn)** | - Nguồn truy cập (Source / Referrer / UTM Campaign).<br/>- Chủ đề tìm kiếm (Search Query / Topic Cluster).<br/>- Dữ liệu người dùng tự nhập trên công cụ Web (Mức lương, Số tiền gửi, Số tiền vay, Nhóm nợ tín dụng).<br/>- Thiết bị và bối cảnh truy cập (Mobile vs Desktop). |
| **ASSUMPTION (Giả Định Cần Test)** | - Cung cấp công cụ tính toán miễn phí không cần đăng nhập (No-login Tool) trên Web sẽ tạo ra nhóm người dùng tải app có ý định sử dụng (Intent) và độ gắn kết sản phẩm cao hơn đáng kể so với việc chỉ hiển thị bài viết giới thiệu tĩnh. |

---

## 5. TỔNG QUAN SẢN PHẨM & LUỒNG TRẢI NGHIỆM (PRODUCT OVERVIEW & USER FLOW)

### 5.1 Kiến Trúc Sản Phẩm 2 Tầng (Hub-and-Spoke Architecture)

Financial Hub được tổ chức thành 2 tầng rõ rệt:
* **Tầng 1 - Master Gateway (`momo.vn/tai-chinh`):** Đóng vai trò là đầu mối phân luồng, hiển thị Dashboard thị trường trực quan (Giá vàng, Tỷ giá, Lãi suất ngân hàng), Hero Widget tính lãi tiết kiệm và danh mục các giải pháp tài chính theo từng nhóm nhu cầu (JTBD).
* **Tầng 2 - 24 Trang Chuyên Sâu & Programmatic Hub (`/tai-chinh/[dich-vu]`):** Giải quyết chi tiết từng bài toán nghiệp vụ với công cụ tính toán tương tác riêng biệt (Tính lương Gross-Net, Quyết toán thuế, Giả lập lãi suất vay, Tra cứu CIC, So sánh 34 ngân hàng).

### 5.2 Sơ Đồ Luồng Trải Nghiệm Người Dùng (Visual User Flow)

```mermaid
graph TD
    A["1. Nhu Cầu Tìm Kiếm / Khám Phá<br/>(Google Search / Social / Referral / QR)"] --> B["2. Tiếp Cận Financial Master Hub<br/>(momo.vn/tai-chinh hoặc Trang Dịch Vụ)"]
    B --> C["3. Nhận Diện Nhu Cầu & Tương Tác Công Cụ<br/>(Kéo trượt Tính Lương / Lãi Tiết Kiệm / Tra Cứu CIC)"]
    C --> D["4. Nhận Kết Quả Tính Toán Tức Thì & Giải Pháp MoMo<br/>(Hiển thị số tiền thực nhận, lãi suất tối ưu & Gói ưu đãi)"]
    D --> E["5. Kích Hoạt Hành Động Web-to-App (W2A CTA)<br/>(Quét QR / Nhấp OneLink mở App MoMo)"]
    E --> F["6. Hoàn Tất Onboarding & eKYC In-App<br/>(Xác thực tài khoản & Nhận gói quà đối tác)"]
    F --> G["7. Giao Dịch Tài Chính Đầu Tiên (1st Value Achieved)<br/>(Mở sổ tiết kiệm / Nhận lương ứng / Kích hoạt Ví Trả Sau)"]
```

### 5.3 Bảng Phân Tích Chi Tiết Các Bước Trải Nghiệm

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.85em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Bước</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Tên Giai Đoạn</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Trải Nghiệm Người Dùng (UX)</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Hạ Tầng / Cơ Chế Kỹ Thuật</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Nền Tảng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Tìm Kiếm & Tiếp Cận</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Tìm kiếm từ khóa nhu cầu trên Google (ví dụ: "tính lương net", "lãi suất tiết kiệm cao nhất", "tra cứu cic") và click vào kết quả MoMo.</td>
      <td style="border:1px solid #94a3b8; padding:6px;">SEO Hub-and-Spoke, Schema Markup, Programmatic SEO.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Web</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Khám Phá & Tương Tác</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Sử dụng ngay các công cụ tính toán trực quan, kéo thanh trượt chọn số tiền/kỳ hạn mà không bị chặn bởi màn hình đăng nhập.</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Client-side Javascript Widgets, Mobase Component System, Zero-Latency UI.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Web</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Nhận Diện Giá Trị</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Xem kết quả chi tiết kèm đề xuất giải pháp tài chính MoMo phù hợp (lãi suất gửi tiết kiệm 7.0%, hạn mức Ví Trả Sau 20 triệu).</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Dynamic Recommendation Engine, Dynamic CTA Rendering.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Web</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Chuyển Đổi Web-to-App</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Nhấp nút CTA hoặc quét mã QR để mở thẳng màn hình tính năng tương ứng trên App MoMo.</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Appsflyer OneLink, Deep Linking, UTM Context Passing.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Web ➔ App</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">5</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Kích Hoạt Giá Trị Đầu Tiên</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Hoàn tất eKYC và thực hiện giao dịch tài chính đầu tiên (mở sổ, rút tiền ứng, thanh toán hóa đơn).</td>
      <td style="border:1px solid #94a3b8; padding:6px;">In-App Onboarding Flow, Financial Partner Core Banking APIs.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">App MoMo</td>
    </tr>
  </tbody>
</table>

---

## 6. ĐỐI SOÁT BENCHMARK QUỐC TẾ (REFERENCE & BENCHMARK)

* **NerdWallet & Bankrate (Hoa Kỳ):** Mô hình thành công điển hình trong việc chuyển đổi traffic tìm kiếm tài chính thành khách hàng sử dụng dịch vụ thông qua hệ thống **Interactive Calculators** và **So sánh đa đối tác minh bạch**. Người dùng khám phá giá trị qua công cụ trước, sau đó mới đăng ký mở thẻ/khoản vay.
* **Revolut (<18 & Financial Hub):** Tiếp cận người dùng bằng định vị giải pháp theo từng phân khúc (Segment Proposition), giải thích rõ năng lực sản phẩm (Product Capabilities) trước khi dùng phần thưởng (Reward) để thúc đẩy hoàn tất cài đặt và định danh.

---

## 7. CƠ SỞ ĐẶT CƯỢC SẢN PHẨM (WHY BETTING ON THIS MVP)

* **`[HYPOTHESIS]`** Một phần lớn tỷ lệ drop-off sau cài đặt bắt nguồn từ việc người dùng chưa thấy đủ sự liên quan của sản phẩm (Product Relevance) trước khi phải đầu tư công sức vào quy trình eKYC phức tạp.
* **`[HYPOTHESIS]`** Hợp nhất 11 trang rời rạc thành mô hình Hub-and-Spoke sẽ gia tăng thẩm quyền chuyên đề (Topical Authority), giúp website MoMo vượt mặt các bài viết tĩnh của đối thủ và chiếm lĩnh Top 1-3 Google.
* **`[HYPOTHESIS]`** Việc triển khai công cụ tính toán không cần đăng nhập (No-login Client-side Tools) sẽ giữ chân người dùng lâu hơn gấp 3-5 lần (Dwell time) và thúc đẩy tỷ lệ nhấp chuyển đổi sang App có chủ đích cao hơn.
* **`[RECOMMENDATION]`** Tập trung toàn lực triển khai **4 Cụm Quick Win** (Tính Lương, Thuế TNCN, Tra cứu CIC, Tiết Kiệm Live, Programmatic 34 Bank) trong Sprint 1 & 2 để gặt hái kết quả tăng trưởng MAU ngay lập tức trước khi đầu tư hạ tầng Realtime phức tạp cho các Big Bet (Giá Vàng, Tỷ Giá).

---

## 8. KẾT QUẢ KỲ VỌNG & KHUNG CHỈ SỐ ĐO LƯỜNG (EXPECTED OUTCOME & TARGET METRICS)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.85em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Tầng Chỉ Số</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Tên Chỉ Số Cốt Lõi</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Mục Tiêu Cam Kết (Targets)</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Ý Nghĩa Nghiệp Vụ & Đo Lường</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Kênh Web (Top-of-Funnel)</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Monthly Pageviews (MPV)</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;"><strong>≥ 1.000.000 lượt/tháng</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Quy mô truy cập toàn bộ hệ thống Financial Hub (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/tai-chinh</code> và các trang vệ tinh).</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Kênh Web (Engagement)</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Utility Engagement Rate</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;"><strong>≥ 25% tổng session</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Tỷ lệ người dùng thực hiện tính toán trên các công cụ (Tính Lương, Thuế, Lãi Tiết Kiệm, CIC).</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Kênh Web (Conversion)</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Web-to-App CTR</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;"><strong>15% - 25%</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Tỷ lệ người dùng nhấp nút CTA chuyển đổi mở App MoMo sau khi sử dụng công cụ.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>In-App (Downstream)</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Web-to-App Activated Users</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;"><strong>Tăng trưởng 30% MoM</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Số lượng người dùng mở App thành công và hoàn tất eKYC định danh qua liên kết Web.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>In-App (Business Value)</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>1st Financial Transactions</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;"><strong>Tăng trưởng 25% MoM</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Số lượng giao dịch tài chính đầu tiên được kích hoạt (Mở sổ tiết kiệm, Mở Ví Trả Sau, Vay Nhanh, Đầu tư Quỹ Mở).</td>
    </tr>
  </tbody>
</table>

---

## 9. MA TRẬN 24 DỊCH VỤ CREDITTECH & ĐỘ KHÓ ĐÁNH CHIẾM

Tổng hợp toàn bộ 24 thị trường dịch vụ của Phân khối CreditTech (đã khử trùng lặp và tính điểm theo 8 tiêu chí chuẩn):

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.82em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">STT</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Thị Trường / Dịch Vụ</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Khối Nghiệp Vụ</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:right; font-weight:700;">Search Volume / Tháng</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Độ Khó (1-10)</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Xếp Loại Độ Khó</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Điểm QW Index</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Phân Nhóm Chiến Lược</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Mức Độ Ưu Tiên</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">1</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Giá Vàng</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Đầu Tư & Tích Sản</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>78,879,270</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">7.95</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Rất Khó</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">10.6</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Big Bet</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">2</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Tỷ Giá</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tiền Tệ & Ngoại Hối</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>8,516,910</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">7.65</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Rất Khó</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">10.3</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Big Bet</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">3</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Ngân Hàng</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Ngân Hàng & Thẻ</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>6,629,420</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6.08</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">14.8</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Big Bet (Programmatic)</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">4</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Chứng Khoán</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Đầu Tư & Tích Sản</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>3,026,340</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">7.28</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Khó</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">11.8</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Big Bet</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Lãi Suất</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tiết Kiệm & Lãi Suất</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>1,246,620</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6.78</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Khó</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">12.7</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Big Bet</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Thuế (TNCN)</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Thu Nhập & Thuế</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>1,159,450</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.80</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">13.8</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">High-Impact Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">7</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Cổ Phiếu</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Đầu Tư & Tích Sản</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>1,077,540</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">7.13</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Khó</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">11.2</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Big Bet</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">8</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Ngoại Tệ</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tiền Tệ & Ngoại Hối</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>959,340</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6.33</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Khó</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">11.1</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Standard Feature</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P2</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">9</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Crypto</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tài Sản Số</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>469,420</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.90</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6.4</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Low Priority</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P2</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">10</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Thẻ Tín Dụng</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Ngân Hàng & Thẻ</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>394,590</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6.38</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Khó</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">12.9</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Big Bet</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">11</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Vay Tín Chấp</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tín Dụng & Vay Vốn</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>389,820</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6.65</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Khó</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">12.3</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Big Bet</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">12</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Thẻ Visa</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Ngân Hàng & Thẻ</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>243,110</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.27</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">13.5</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Core Driver</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">13</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Gửi Tiết Kiệm</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tiết Kiệm & Lãi Suất</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>230,110</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.67</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">14.5</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">High-Impact Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">14</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Tính Lương</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Thu Nhập & Thuế</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>190,690</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.13</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">13.1</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Top Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">15</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Vay Thế Chấp</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tín Dụng & Vay Vốn</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>125,960</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6.00</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">11.2</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Core Driver</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">16</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Trả Góp</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tín Dụng & Vay Vốn</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>116,390</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.23</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">13.8</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Top Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">17</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Tiền Số & Tiền Ảo</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tài Sản Số</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>104,500</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.03</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">6.0</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Low Priority</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P2</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">18</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>CIC (Điểm tín dụng)</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tín Dụng & Vay Vốn</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>95,630</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">4.65</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Dễ (Low)</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">14.6</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Top Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">19</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Trái Phiếu</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Đầu Tư & Tích Sản</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>79,580</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.65</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">9.0</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Standard Feature</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P2</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">20</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Thẻ Ghi Nợ (ATM)</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Ngân Hàng & Thẻ</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>73,290</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">4.50</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Dễ (Low)</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">13.8</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Top Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">21</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Nợ Xấu</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Tín Dụng & Vay Vốn</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>59,890</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">4.90</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Dễ (Low)</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">12.7</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Top Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">22</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Napas</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Ngân Hàng & Thẻ</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>51,100</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">4.33</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Dễ (Low)</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">14.3</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Top Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">23</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Chứng Chỉ Quỹ</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Đầu Tư & Tích Sản</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>25,790</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">5.00</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Trung Bình</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#1e40af;">12.6</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Top Quick Win</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">24</td>
      <td style="border:1px solid #94a3b8; padding:5px;"><strong>Mastercard</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px;">Ngân Hàng & Thẻ</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:right;"><strong>18,630</strong></td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">4.85</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center; font-weight:700; color:#15803d;">Dễ (Low)</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">10.9</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">Core Driver</td>
      <td style="border:1px solid #94a3b8; padding:5px; text-align:center;">P1</td>
    </tr>
    <tr style="background-color:#f1f5f9; font-weight:700;">
      <td style="border:1.5px solid #64748b; padding:6px; text-align:center;" colspan="3">TỔNG CREDITTECH (DEDUPLICATED)</td>
      <td style="border:1.5px solid #64748b; padding:6px; text-align:right;"><strong>101,896,660</strong></td>
      <td style="border:1.5px solid #64748b; padding:6px; text-align:center;">—</td>
      <td style="border:1.5px solid #64748b; padding:6px; text-align:center;">—</td>
      <td style="border:1.5px solid #64748b; padding:6px; text-align:center;">—</td>
      <td style="border:1.5px solid #64748b; padding:6px; text-align:center;">58,164 Unique Keywords</td>
      <td style="border:1.5px solid #64748b; padding:6px; text-align:center;">Master SSOT</td>
    </tr>
  </tbody>
</table>

---

## 10. LỘ TRÌNH TRIỂN KHAI 11 DỰ ÁN CỐT LÕI (ROADMAP & MILESTONES)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.85em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Giai Đoạn</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Thời Gian</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Tên Giai Đoạn</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Chi Tiết Triển Khai & Mục Tiêu Cốt Lõi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;"><strong>Phase 1</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 8 - 9/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Đánh Chiếm Quick Wins & Hạ Tầng Master Hub</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">
        - Ra mắt Master Gateway <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/tai-chinh</code> với Hero Widget Tính Lãi Tiết Kiệm Live.<br/>
        - Triển khai Bộ Đôi Công Cụ Thu Nhập & Thuế 2026 (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tai-chinh/tinh-luong</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tai-chinh/thue-tncn</code>).<br/>
        - Ra mắt Cổng Tra Cứu CIC & Điểm Tín Dụng (<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tai-chinh/tra-cuu-cic</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tai-chinh/xoa-no-xau</code>).<br/>
        - Xuất bản Programmatic Hub cho 34 Ngân Hàng đối tác và Cổng Napas 247.
      </td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;"><strong>Phase 2</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 10 - 11/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Mở Rộng Core Drivers & Tích Hợp Realtime Feeds</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">
        - Tích hợp Engine dữ liệu Giá Vàng SJC/9999 & Tỷ Giá Ngoại Tệ Realtime.<br/>
        - Ra mắt Ma Trận So Sánh Thẻ Tín Dụng & Thẻ Quốc Tế Visa/Mastercard.<br/>
        - Phát triển Máy Tính Trả Góp 0% và Cổng Đăng Ký Vay Nhanh / Vay Mua Nhà.<br/>
        - Xây dựng Bộ Giả Lập Đầu Tư Quỹ Mở / Tích Lũy SIP từ 10.000đ.
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;"><strong>Phase 3</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tháng 12/2026 - Q1/2027</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Cá Nhân Hóa Tự Động & Scale Toàn Ngành</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">
        - Triển khai Real-time Personalization dựa trên dữ liệu người dùng tự khai báo trên Web.<br/>
        - Đóng gói toàn bộ Embeddable Widgets cho các đối tác ngoài (Affiliate & Partner Web).<br/>
        - Tối ưu hóa phễu chuyển đổi Web-to-App cho phân khúc Sinh Viên (U18 - U23) và Nhà Đầu Tư Mới (F0).
      </td>
    </tr>
  </tbody>
</table>
"""

with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
    f.write(brd_content)

print("Successfully rewritten 05_HUBS/financial-hub-brd.md according to the Golden BRD Framework!")
