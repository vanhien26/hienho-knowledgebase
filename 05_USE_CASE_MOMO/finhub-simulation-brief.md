# PRD Discovery Brief: Finhub Simulation Tools

> **Dự án:** Các công cụ Simulation (Vay, Thuế, Chứng khoán giả lập, Tiết kiệm)
> **Khách hàng nội bộ:** BU FS (Finhub / Trung Tâm Tài Chính)
> **Tư vấn & Nền tảng:** Web Platform (Lead: Hiến)
> **Mục tiêu:** Thu thập Product Vision và Business KPI từ BU để làm đầu vào xây dựng trên nền tảng MoSpark.

---

## 1. Product Vision (Tầm nhìn Sản phẩm)

*Mục tiêu: Làm rõ giá trị cốt lõi của công cụ giả lập và lý do vì sao nó cần tồn tại trên Web.*

1. **JTBD (Job-to-be-done) chính của User khi tìm đến tool này là gì?**
   - Họ đang muốn giải quyết nỗi lo gì? (Ví dụ: Sợ tính sai thuế bị phạt? Sợ cháy tài khoản khi chơi chứng khoán? Không biết mỗi tháng trả góp vay bao nhiêu?)
   - "Aha! moment" (khoảnh khắc sung sướng nhất) của user sau khi dùng tool là gì?

2. **Tại sao lại là Web (momo.vn) mà không phải In-App?**
   - BU kỳ vọng đón lượng Organic Traffic từ Google Search (như từ khóa: *"cách tính thuế TNCN", "bảng tính lãi suất vay"*), hay dùng Web làm Landing Page để chạy Ads (Paid Traffic)?
   - *Góc nhìn Web Platform:* Web là phễu trên cùng (Top of Funnel) cực tốt để đón user chưa có app MoMo hoặc chưa từng dùng dịch vụ tài chính của MoMo.

3. **Cơ chế chuyển đổi (Web-to-App Loop) là gì?**
   - Sau khi user giả lập/tính toán xong, làm sao để kéo họ vào App? 
   - *Ví dụ:* Tính xong khoản vay -> "Đăng ký vay ngay trên MoMo với hạn mức tương đương". Chơi chứng khoán ảo có lãi -> "Mở tài khoản thật nhận ngay 100k".

## 2. Business KPI & North Star (Mục tiêu Kinh doanh)

*Mục tiêu: Đặt ra thước đo thành công để thiết kế luồng UI/UX tối ưu cho conversion.*

1. **North Star Metric (Chỉ số quan trọng nhất) của dự án này là gì?**
   - Số lượng Leads (SĐT) thu thập được?
   - Số lượng User click mở App (Deep-link / Onelink)?
   - Số lượng User thực sự hoàn tất mở tài khoản Tiết Kiệm/Chứng Khoán hoặc giải ngân Vay thành công từ nguồn Web?

2. **Micro-conversions (Chỉ số đo lường chất lượng Tool):**
   - Tỷ lệ hoàn thành (Completion Rate): Bao nhiêu % user vào trang và điền hết form giả lập để ra kết quả?
   - Thời gian trên trang (Time on page) & Số lần tương tác (Engagement) với bảng tính.

3. **Quy mô kỳ vọng & Ngân sách (Scale & Budget):**
   - BU kỳ vọng bao nhiêu traffic / tháng? 
   - Có sẵn ngân sách Media để buff lúc mới ra mắt không, hay phụ thuộc hoàn toàn vào SEO của Web Platform? (Nếu là SEO thì cần chiến lược nội dung vệ tinh đi kèm, không chỉ mỗi cái tool).

## 3. Data & Technical Constraints (Yêu cầu Kỹ thuật)

1. **Logic tính toán (Calculation Engine):**
   - Logic (ví dụ: công thức tính thuế, tính lãi vay) BU có sẵn API để Web gọi sang, hay Web tự build công thức ở Front-end?
2. **Dữ liệu realtime (Realtime Data):**
   - Với Chứng khoán giả lập: Giá cổ phiếu lấy từ nguồn nào? Độ trễ cho phép là bao nhiêu?
3. **Tính Pháp lý (Compliance):**
   - Có cần những dòng Disclaimer (miễn trừ trách nhiệm) kiểu "Bảng tính chỉ mang tính chất tham khảo" không? Ai (bộ phận nào) sẽ duyệt nội dung pháp lý này?

---
*Lưu ý cho Web Lead:* Sau khi có câu trả lời, Web Platform sẽ tư vấn **Bộ Component MoSpark** phù hợp (Form, Slider, Graph/Chart, CTA Onelink) để đóng gói thành 1 Web App hoàn chỉnh.
