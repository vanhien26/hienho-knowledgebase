# BRD: Financial Hub (Finhub) - Trung Tâm Công Cụ Tài Chính

> - **Project:** Financial Hub / Finhub (Cổng Tra Cứu & Giả Lập Tài Chính MoMo)
> - **Platform:** Web Platform (`momo.vn/finhub`, `momo.vn/tra-gop`)
> - **Division:** Growth Platform Division (GPD)
> - **Owner:** Web Platform Team (GPD)

---

## 1. BUSINESS CONTEXT & PRODUCT OVERVIEW

### 1.0 Executive Overview & Product Statement
**Financial Hub (Finhub)** là trung tâm công cụ tra cứu và giả lập tài chính cá nhân trên Web Platform  thuộc Web Platform (GPD). Finhub đáp ứng nhu cầu tính toán lãi suất, số tiền trả góp hàng tháng, kiểm tra điểm tín dụng CIC và theo dõi giá vàng của người dùng trước khi ra quyết định, tạo niềm tin và chuyển đổi người dùng đăng ký Ví Trả Sau & Vay Nhanh trên App MoMo.


### 1.1 Market Sizing & Target Audience
* **Bối cảnh:** Người dùng có thói quen tìm kiếm công cụ tính toán thử lãi suất, số tiền trả góp hàng tháng và kiểm tra nợ xấu CIC trước khi đăng ký dịch vụ tài chính.
* **Đối tượng:** Người dùng có nhu cầu tra cứu, tính toán lãi suất/phí trả góp, kiểm tra điểm tín dụng và đăng ký sản phẩm tài chính.

### 1.2 Product Vision & Statement
**Financial Hub (Finhub)** là trung tâm giả lập và tính toán tài chính cá nhân trên Web Platform  do Web Platform (GPD) làm chủ. Finhub hỗ trợ công cụ tính toán minh bạch, tạo niềm tin và dẫn dắt người dùng đăng ký các sản phẩm tài chính trên App MoMo.

### 1.3 Product-Led Growth (PLG) Strategy
* **Dùng công cụ không cần đăng nhập:** Người dùng kéo thanh trượt chọn giá trị món hàng, kỳ hạn trả góp để xem tiền trả mỗi tháng mà không cần đăng nhập. Khi đồng ý phương án ──► Bấm *"Đăng ký mở Ví Trả Sau / Vay Nhanh trên App MoMo"*.

### 1.4 Goals & Key Metrics
* **Financial Leads:** Chuyển đổi >100.000 lượt tính toán calculator thành hồ sơ đăng ký Ví Trả Sau & Vay Nhanh.
* **SEO Traffic:** Top 3 Organic Search từ khóa *"Tính phí trả góp"*, *"Vay nhanh calculator"*, *"Giá vàng hôm nay"*, *"Tra cứu CIC"*.

---

## 2. TARGET PERSONAS & JTBD

### 2.1 Target Personas
1. **Người mua sắm trả góp:** Cần cân đối số tiền trả góp hàng tháng vừa ngân sách cá nhân.
2. **Người vay tiêu dùng:** Cần thông tin rõ ràng về tổng gốc + lãi trả mỗi tháng trước khi nộp đơn vay.
3. **Người theo dõi thị trường:** Theo dõi biểu đồ giá vàng SJC/9999 hàng ngày để chọn thời điểm tích lũy.

### 2.2 Jobs-to-be-Done (JTBD) & Pain Points
| Nhóm người dùng | Pain Points | MoMo Solution |
| :--- | :--- | :--- |
| **Khách mua trả góp** | Lo lắng phí ẩn, lãi suất mập mờ | Máy tính Trả góp minh bạch từng tháng theo kỳ hạn 3, 6, 9, 12 tháng. |
| **Khách vay tiêu dùng** | Lo sợ bẫy tín dụng đen; Lo nợ xấu | Vay Nhanh Calculator tính rõ lịch trả nợ + Tra cứu điểm tín dụng CIC. |

---

## 3. USER FLOWS & ARCHITECTURE

### 3.1 Web Onboarding Flow
```
[1. Nhập Số Tiền & Kỳ Hạn trên Web Platform] ──► [2. Xem Kết Quả Máy Tính Lãi & Trả Góp Minh Bạch]
                                                                        │
                                                                        ▼
[4. Nhận Hạn Mức & Giải Ngân Trên App MoMo] ◄── [3. Bấm "Mở Ví Trả Sau / Vay Nhanh"]
```

---

## 4. DETAILED USE CASES & KPIS

| # | Use Case | Mô tả & Luồng sử dụng | KPIs Cam kết |
|---|---|---|---|
| 1 | **Trả Góp Calculator** | Nhập giá trị món hàng, chọn kỳ hạn (3-12 tháng) để tính tiền trả mỗi tháng qua Ví Trả Sau. | Lượt dùng máy tính trả góp; Tỷ lệ chuyển đổi Ví Trả Sau. |
| 2 | **Vay Nhanh Calculator** | Giả lập khoản vay, xem chi tiết tiền gốc + lãi trả hàng tháng theo dư nợ giảm dần. | Lượt giả lập vay; Số hồ sơ Vay Nhanh nộp thành công qua Web. |
| 3 | **Tra Cứu Điểm Tín Dụng CIC** | Tra cứu hạng tín dụng cá nhân, kiểm tra lịch sử nợ xấu và nhận hướng dẫn nâng điểm uy tín. | Organic traffic từ khóa "Tra cứu CIC"; Lượt đăng ký sản phẩm tín dụng. |
| 4 | **Theo Dõi Giá Vàng 24/7** | Biểu đồ cập nhật giá vàng SJC, nhẫn 9999, PNJ, Doji trong nước và thế giới thời gian thực. | Top 3 Organic Search "Giá vàng hôm nay"; Tỷ lệ chuyển đổi Tiết kiệm/Đầu tư. |

---

## 5. CONTENT & SEO/GEO STRATEGY

* **SEO Tài chính:** Phủ từ khóa tính toán tài chính có ý định chuyển đổi cao.
* **Tối ưu GEO (AI Search):** Biên soạn bài viết *"Cách tính lãi suất trả góp chuẩn nhất"* hỗ trợ công cụ AI Search trích dẫn nguồn Finhub MoMo.

---

## 6. GAMIFICATION & PROMOTIONS

* **Đấu trường Tri thức Tài chính:** Trắc nghiệm kiến thức tài chính nhận Xu MoMo hoặc Voucher giảm phí Ví Trả Sau.

---

## 7. COMPLIANCE & RISK MANAGEMENT

* **Minh bạch thông tin:** Hiển thị khuyến cáo *"Kết quả tính toán mang tính tham khảo, hạn mức thực tế phê duyệt trên App MoMo"*.
* **Bảo mật:** Không lưu trữ thông tin nhạy cảm khi dùng công cụ giả lập công khai trên Web.

---
