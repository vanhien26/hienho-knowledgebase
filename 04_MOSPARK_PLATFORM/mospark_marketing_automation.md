# MoSpark - Web-to-App Marketing Automation & Retargeting
Hệ thống tự động hóa tiếp thị bám đuổi Web-to-App

> - **Project Name:** MoSpark Growth Platform - Phase 2
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Bảo
> - **PIC:** Thuận (Tech)
> - **Version:** 1.0 · June 2026

---

## 1. Executive Summary

### 1.1 Bối Cảnh
Hiện tại, MoSpark đo lường được tỷ lệ Web-to-App (W2A) Conversion thông qua Appsflyer và Umami. Tuy nhiên, hành trình của User thường bị ngắt quãng. Ví dụ: Khách hàng dùng điện thoại quét mã QR tại bàn, mở ra trang Merchant Page `momo.vn/merchant/{slug}`, đọc kỹ về Ví Trả Sau nhưng khi bấm vào nút "Kích hoạt", họ lại phân tâm (có điện thoại, đang nói chuyện) và thoát ra (Drop-off).
Với cấu trúc hiện tại, tập user có Intent cực cao này đang bị bỏ phí vì chúng ta không có cơ chế Remarketing tự động để "kéo" họ lại.

### 1.2 Giải Pháp
Hệ thống **Marketing Automation & Retargeting** sẽ kết nối trực tiếp hành vi trên Web với hạ tầng CRM của MoMo App. Dựa vào Identity Parsing (nhận diện ID người dùng từ Cookie hoặc QR Session), hệ thống sẽ kích hoạt các luồng Automation (Triggered Campaigns) qua 2 kênh chính:
1. **MoMo App Push Notification:** Gửi thông báo trực tiếp trên màn hình khóa.
2. **MoMo Zalo OA:** Gửi tin nhắn qua Zalo với format hấp dẫn, đính kèm deeplink.

*(Lưu ý: Không triển khai SMS vì chi phí cao và tỷ lệ convert thấp trong bối cảnh O2O; In-App Push và Zalo OA là 2 kênh "nhà trồng được", chi phí gần như bằng 0).*

---

## 2. Các Kịch Bản Bám Đuổi (Retargeting Scenarios)

### Scenario 1: Abandoned O2O Cart (Bỏ giỏ hàng O2O)
- **Hành vi (Trigger):** User vào trang Merchant bằng QR Code, có Click vào CTA "Thanh toán bằng Ví Trả Sau" nhưng hệ thống App ghi nhận User không hoàn tất định danh thẻ trong vòng 30 phút.
- **Action (Automation):**
  - **T+2 hours:** Gửi Push Notification: *"Bạn chưa kích hoạt xong Ví Trả Sau tại [Tên Quán]? Kích hoạt ngay để được hoàn 50K cho bữa ăn này nhé!"*
  - **T+24 hours:** Nếu vẫn chưa kích hoạt, gửi Zalo OA Message đính kèm hình ảnh Key Visual của quán và nút bấm mở App.

### Scenario 2: Merchant Discovery Retargeting
- **Hành vi (Trigger):** User search Google "Quán nướng ngon Quận 1", vào trang Category Hub của MoSpark nhưng không bấm vào bất kỳ Merchant nào và thoát ra.
- **Action (Automation):**
  - **T+1 day:** Vì chưa rõ quán cụ thể, hệ thống gửi Zalo OA: *"Thèm đồ nướng? Gợi ý bạn 3 quán nướng đang có Hoàn tiền 20% khi thanh toán MoMo tại Quận 1. Đặt bàn ngay!"*

### Scenario 3: Contextual Cross-sell (Bán chéo dịch vụ)
- **Hành vi (Trigger):** User đọc hết một bài viết SEO dài về "Bảo hiểm xe máy bồi thường ra sao" (Time-on-page > 2 phút) nhưng không bấm mua.
- **Action (Automation):**
  - **T+1 hour:** In-App Push: *"Mua bảo hiểm xe máy trên MoMo chỉ mất 2 phút. An tâm ra đường, miễn phí giao ấn chỉ!"*

---

## 3. Kiến Trúc Tích Hợp (Architecture)

1. **Event Capture (Umami / Data Layer):** Bắt các sự kiện Drop-off.
2. **Identity Linker:** Match Cookie ID (Web) với UID (App). Nếu là tập Anonymous chưa có UID, sẽ dựa trên Fingerprinting hoặc lưu tệp retargeting Pixel (Facebook/Google) để chạy Ads ngoài.
3. **MoMo CDP (Customer Data Platform):** Đẩy Event Real-time vào CDP của MoMo.
4. **Trigger Engine (Braze / Internal CRM):** Cấu hình Journey Builder (Canvas). Nhận event và phát lệnh gửi tin nhắn.

---

## 4. Yêu Cầu Chức Năng Của MoSpark
Để kết nối luồng này, MoSpark Editor phải bổ sung:
1. **Automation Panel:** Nơi PM/Editor chọn "Tag" cho bài viết/trang (Ví dụ: Tag `VTS_Dropoff_Intent`).
2. **Webhooks Setup:** Cho phép bắn Webhook real-time sang CDP nội bộ mỗi khi có Event quan trọng xảy ra trên trang.
3. **Opt-out Management:** Tuân thủ quy định chống Spam, cung cấp tùy chọn cho người dùng tắt theo dõi retargeting trên Web.

---

## 5. Metrics Đo Lường
- **Trigger Rate:** Tỷ lệ số lượng tin nhắn bám đuổi được gửi thành công trên tổng số Session bị Drop-off.
- **Open Rate / Click Rate:** Tỷ lệ User mở Push / Nhấn vào link Zalo.
- **Retargeting Conversion Rate:** Phần trăm User hoàn tất hành động (Mở thẻ / Thanh toán) *sau khi* nhận được tin nhắn bám đuổi.
- **Incremental W2A Conversions:** Tổng lượng chuyển đổi tăng thêm nhờ hệ thống Automation so với không có hệ thống.
