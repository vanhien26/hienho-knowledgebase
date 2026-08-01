# WEB PLATFORM x BU TRAVEL | 2026

**Bối cảnh dự án:** 
H2/2026 là mùa cao điểm du lịch quốc tế (Mùa thu Châu Á như Nhật Bản, Hàn Quốc, Đài Loan và các kỳ nghỉ lễ cuối năm). Đây là giai đoạn có traffic intent search cực cao trên các nền tảng Search Engine Out-App liên quan đến việc chuẩn bị kết nối internet khi ra nước ngoài (eSIM du lịch, sim quốc tế, roaming).

**Mục tiêu dự án:** 
- Tăng cường khả năng hiển thị của **eSIM Du Lịch** trên các nền tảng Search Engine/AIO.
- Tăng trưởng X2 Total Traffic, trong đó trọng điểm là Organic Traffic.
- Tăng trưởng X2 các chỉ số cho luồng Web To App tác động đến MAU/Revenue.
- Xây dựng luồng tính năng **Chọn gói eSIM & Thanh toán trực tiếp** trên Web eSIM Du lịch.

---

## 1. Executive Summary

### Situation
- **Vị thế:** Web eSIM Du Lịch có cấu trúc và tính năng sản phẩm đầy đủ của một Product Led Growth để trở thành một nền tảng giúp tăng trưởng mảng viễn thông quốc tế.
- **Thực trạng & Định hướng:** Một thời gian dài, Web eSIM chưa được đầu tư nâng cấp, tối ưu chuyên sâu về tính năng sản phẩm, nội dung và các hoạt động Offpage dẫn đến sự suy giảm về hiệu suất và không cạnh tranh được với các đối thủ chuyên biệt (như Airalo, Gohub). Trọng tâm H2/2026 là tái cấu trúc toàn diện và chuyển dịch hạ tầng MoSpark Platform giúp khai thác các lợi thế AI-Powered nhằm phục hồi và thúc đẩy đà tăng trưởng.
- **Traffic:** ~8.900 users tự nhiên trong toàn bộ H1/2026 (mức rất thấp). Hiện tại chỉ đứng Top 1 cho các từ khóa ngách có chứa Brand (VD: "mua sim trên momo", "esim du lịch momo").
- **Ecosystem Flow:** Discovery (SERP/AIO) → Web (momo.vn/esim-du-lich) → Transaction (App/Web) → Retention.

### Complication
4 vấn đề hiện trạng:
1. **Luồng Thanh toán (Mobile Drop-off):** Đã có Web Payment nhưng trên giao diện Mobile Web chưa tích hợp luồng Open OneLink để gọi mở App thanh toán liền mạch. Sự đứt gãy trải nghiệm này khiến phần lớn user truy cập bằng điện thoại rớt phễu giữa chừng khi mua eSIM.
2. **Search Market Gap:** Bỏ lỡ hoàn toàn lượng tìm kiếm khổng lồ từ tệp khách hàng tự do (Non-brand) theo quốc gia đích (VD: "esim Thái Lan", "esim Nhật Bản", "sim du lịch Hàn Quốc"). Việc này khiến Web hiện tại chỉ đón được lượng traffic nhỏ (đã biết sẵn brand MoMo).
3. **Rủi ro AI Overview (AIO):** Chưa tối ưu cấu trúc dữ liệu FAQ. Các truy vấn như "cách cài đặt esim", "esim là gì" rất dễ bị Google AI trả lời trực tiếp khiến Web mất Traffic.
4. **Vòng đời Chuyến đi (Travel Life-Cycle):** Không có hệ thống nuôi dưỡng (nurture). User mua eSIM xong đi du lịch về là kết thúc hành trình, thiếu cơ chế tự động remarketing hoặc upsell các dịch vụ liên quan (Bảo hiểm du lịch, Vé máy bay lần sau) để không lãng phí Traffic.

---

## 2. Business Objectives

### 2.1 Baseline & KPIs (Trọng điểm Mùa cao điểm Q3/2026)

| Metric | Q2/2026 (Baseline) | Q3/2026 (Target) | Growth (QoQ) |
|---|---|---|---|
| Tổng lượng Khách hàng (MAU) | ~60,700 | **107,446** | ▲ +77% |
| Tổng Giao dịch (Transactions) | ~91,000 | **161,169** | ▲ +77% |
| Tổng Doanh thu (GMV) | ~15,4 tỷ VND | **27,4 tỷ VND** | ▲ +77% |
| Đóng góp Giao dịch từ Web (Web Contribution) | N/A | **11,317** | N/A |
| Đóng góp Doanh thu từ Web (Web GMV) | N/A | **~1,92 tỷ VND** | N/A |
| **Tỷ trọng Web / Tổng Giao dịch** | **< 2%** | **4% ➔ 6% ➔ 10%** *(Tăng dần T7-T9)* | N/A |

* **Ghi chú:**
- **Mục tiêu:** Tăng trưởng đột phá trong quý cao điểm du lịch (Q3/2026).
- **Thách thức:** Kênh Web chưa đóng góp tỷ trọng tương xứng (Target cuối Q3 phải đạt 10%). Giải pháp bắt buộc: Tích hợp luồng Open OneLink chuyển tiếp mượt mà từ Mobile Web sang App và đẩy mạnh bán chéo (Trip Kit).

### 2.2 Competitive Landscape

| Competitor | Strengths | Weaknesses | MoMo Advantage |
|---|---|---|---|
| Airalo / Gohub | Chuyên biệt eSIM, thương hiệu global/địa phương mạnh | Thanh toán qua thẻ quốc tế phức tạp, phí chuyển đổi ngoại tệ | Thanh toán nội địa MoMo siêu tốc |
| Các đại lý bán Sim Shopee | Giá rẻ, đa dạng lựa chọn sim vật lý | Giao hàng chậm, rủi ro sim lỗi không ai hỗ trợ | Nhận QR Code eSIM tức thì, tin cậy tuyệt đối |
| Nhà mạng VN (Viettel/Mobi) | Gói Roaming tiện lợi, không cần đổi sim | Chi phí Roaming cực kỳ đắt đỏ | Giá eSIM MoMo cạnh tranh, dung lượng cao |

---

## 3. Web Product Strategy

Mục tiêu Uplift 100% H2/2026 dựa trên 3 trụ cột chiến lược:

| # | Trụ Cột Chiến Lược | Trọng Tâm |
|---|---|---|
| **1** | **Expand Out-App Traffic** | Phủ sóng tìm kiếm Out-App theo các Điểm đến (Destination-based SEO). Biến Web thành kênh Acquisition. |
| **2** | **Topical Authority (Travel Hub)** | Xây dựng "Bách khoa toàn thư" du lịch số (Bí kíp du lịch các nước, cách dùng eSIM). Phát triển content sâu để rank Google AI. |
| **3** | **Web Product** | Chuyển dịch sang MoSpark. Trọng tâm: UX chọn gói dung lượng liền mạch & Triển khai luồng Web Payment. |

---

## 4. Collaboration Model

Dự án được vận hành dưới mô hình đối tác chiến lược giữa BU Travel và khối Web Platform:

**1. BU Travel (Business Owner)**
- **Business Ownership:** Nắm giữ quyền quyết định và chịu trách nhiệm toàn trình đối với kết quả kinh doanh (P&L, Doanh thu, New Users, MAU, Transactions).
- **Domain Strategy:** Hoạch định chiến lược kinh doanh và định hướng khai thác hệ sinh thái đối tác viễn thông quốc tế.
- **Exchange Link:** Làm việc với đối tác để trao đổi hoạt động truyền thông Off-Page.

**2. Web Platform (Product Development, Content Production & Growth Strategy)**
- **Product & Growth Ownership:** Sở hữu, định hướng và vận hành Trải nghiệm Sản phẩm (Web Product), tỷ lệ Chuyển đổi (CR) và Tăng trưởng Organic Traffic.
- **Trọng tâm thực thi H2/2026:**
  - **Product-Led Growth:** Triển khai PLG Framework cho eSIM Web trên nền tảng MoSpark.
  - **Product Migration:** Xây dựng và nâng cấp sản phẩm Web eSIM đáp ứng các tiêu chuẩn tối ưu được cập nhật mới về kiến trúc nền tảng, cấu trúc sản phẩm, tính năng kỹ thuật của Web Platform.
  - **Content Production:** Phối hợp xây dựng chiến lược nội dung, sản xuất hàng loạt bài viết theo quốc gia/điểm đến một cách tối ưu thông qua việc áp dụng mạnh mẽ năng lực GenAI trên MoSpark Platform.
