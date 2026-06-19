# PRD: MoSpark Ads Manager Setup Prototype

> - **Project Name:** MoSpark Ads Manager Setup Prototype
> - **Division:** GPD (Growth Platform Division)
> - **Owner:** Bảo (Platform Admin)
> - **PIC:** Thuận (Tech)
> - **Observer:** Hiến (Project Manager / SEO Advisor)
> - **Version:** 1.0 · June 2026
> - **Status:** Draft

---

## 1. Product Overview (Tổng quan Sản phẩm)

### 1.1 Vấn đề (Problem Statement)
MoSpark Ads Manager là hệ thống cốt lõi để phân phối quảng cáo và các Widget/Component tương tác trên hệ sinh thái Web MoMo nhằm thúc đẩy tỷ lệ chuyển đổi Web-to-App (W2A). Tuy nhiên:
- Khái niệm về **Targeting theo URL Context**, **CMS Tags**, và đặc biệt là cơ chế **Phân xử xung đột (Conflict Resolution)** khá trừu tượng đối với các PM/PO vận hành.
- Việc phát triển trực tiếp hệ thống quản trị (Admin Dashboard) trên môi trường production đòi hỏi nhiều thời gian thiết kế, kiểm thử và dễ gặp lỗi logic trong khâu phân xử độ ưu tiên hiển thị.
- Chưa có một môi trường giả lập (Sandbox) giúp PM/PO nhìn trực quan được: *"Ad của tôi sẽ hiển thị như thế nào trên mobile/desktop?", "Tại sao Ad của tôi không hiển thị trên URL này?"*.

### 1.2 Giải pháp (Product Vision)
Xây dựng một **MoSpark Ads Manager Setup Prototype** — một bản nguyên mẫu (prototype) web tương tác độc lập (Standalone Web Application). Prototype này đóng vai trò:
1. **Thiết lập Chiến dịch (Campaign Builder):** Giao diện từng bước (step-by-step) giúp PM/PO tự cấu hình quảng cáo/Widget mà không cần code.
2. **Trực quan hóa Phân phối (Live Preview):** Trình giả lập khung hình Điện thoại/Máy tính trực quan hóa cách hiển thị của Balloon, Popup, và Native Widget.
3. **Giả lập Phân xử (Conflict Engine Simulator):** Giúp PM/PO nhập một URL bất kỳ để xem hệ thống phân xử chiến dịch nào sẽ "chiến thắng" và hiển thị dựa trên Priority Score.

### 1.3 Success Metrics cho Prototype (KPIs)
*   **Trực quan hóa 100%:** Mô phỏng thành công 4 định dạng quảng cáo chính (Balloon, Popup, Calculator Widget, Purchase Component).
*   **Độ chính xác của Engine Simulator:** Phản ánh đúng logic tính điểm ưu tiên và luật giới hạn (Global Guardrails).
*   **Tốc độ Feedback Vận hành:** Giảm thời gian giải thích luồng hoạt động của Ads Manager cho các Division từ vài ngày xuống < 1 giờ trải nghiệm prototype.

---

## 2. User Roles & Scope

### 2.1 User Roles trong Prototype
*   **Division Operator (PM/PO):** Người vào trải nghiệm tạo chiến dịch quảng cáo, thiết lập A/B Test, và kiểm tra hiển thị.
*   **Platform Admin (Bảo/Thuận):** Người kiểm tra tính đúng đắn của logic phân xử xung đột, cấu hình Placement Registry toàn hệ thống.

### 2.2 Scope của Prototype

**In scope (Nằm trong phạm vi phát triển):**
1. **Module Cấu hình Campaign:** Form nhập thông tin Chiến dịch (Tên, Loại Format, Target URL Rules / CMS Tags, CTA Link, Priority Weight).
2. **Module Placement Registry (Mock):** Danh sách các vị trí quảng cáo đã đăng ký trên Web MoMo (Shared placements vs Use-case placements).
3. **Module Conflict Engine Simulator:** Nhập một URL bất kỳ và xem danh sách các chiến dịch trùng khớp, cách tính toán điểm số và hiển thị chiến dịch chiến thắng.
4. **Module Live Preview:** Hiển thị trực quan giao diện Ad/Widget trên một mô hình Web Mockup (Mobile/Desktop Frame).
5. **Module A/B Test Configurator:** Giao diện thiết lập thử nghiệm A/B cho Landing Page hoặc Creative quảng cáo.

**Out of scope (Nằm ngoài phạm vi prototype):**
*   Kết nối cơ sở dữ liệu thật (Sử dụng Local Storage của trình duyệt hoặc Memory State để lưu thông tin tạm thời).
*   Tích hợp thật với App MoMo, Athena, Appsflyer, hay Umami Analytics (chỉ mô phỏng dữ liệu phân tích).
*   Hệ thống phân quyền (Authentication/Authorization) thực tế.

---

## 3. Functional Requirements (Yêu cầu chức năng)

### 3.1 Module 1: Trình cấu hình Campaign (Campaign Builder)
Cho phép người dùng tạo một chiến dịch quảng cáo giả lập.

*   **FR1.1 - Nhập thông tin cơ bản:** Tên chiến dịch, Division sở hữu (Ví dụ: Insurance, BNPL, Vay Nhanh).
*   **FR1.2 - Chọn định dạng (Ad Format / PLG Tool):**
    *   *Balloon Ads / Float Icon*
    *   *Popup / Bottom Sheet*
    *   *Calculator Widget* (Ví dụ: Máy tính phí bảo hiểm)
    *   *Purchase Component* (Ví dụ: Form đăng ký mua nhanh)
*   **FR1.3 - Thiết lập Targeting (URL Context & Tags):**
    *   Nhập URL Pattern (ví dụ: `/blog/bao-hiem*`, `/vay-nhanh`).
    *   Chọn CMS Tags mục tiêu (ví dụ: `bao-hiem-xe-may`, `vay-tieu-dung`).
*   **FR1.4 - Cấu hình CTA & Tracking (Attribution):**
    *   Nhập URL đích (Landing Page hoặc Onelink).
    *   Tự động phát sinh UTM Parameters mẫu gắn vào CTA (ví dụ: `utm_source=mospark_ads&utm_medium=balloon&utm_campaign=campaign_name`).
*   **FR1.5 - Thiết lập Priority (Độ ưu tiên):**
    *   Chọn Campaign Weight (Global Priority: 100đ, Division Priority: 50đ).

### 3.2 Module 2: Quản lý Vị trí (Placement Registry Mockup)
Giao diện hiển thị danh sách các vị trí (placement slots) có sẵn trên hệ thống Web MoMo.

*   **FR2.1 - Hiển thị Registry:** Bảng danh sách các Placements gồm:
    *   *Placement Name* (ví dụ: Blog Right Balloon, Home Hero Banner).
    *   *URL Scope* (Phạm vi URL áp dụng).
    *   *Format Allowed* (Các định dạng được phép hiển thị).
    *   *Status* (Đang trống / Đã bị chiếm bởi campaign nào).
*   **FR2.2 - Cấu hình Placement (Mock):** Cho phép Admin bật/tắt hoặc chỉnh sửa luật của từng Placement trong bộ nhớ tạm.

### 3.3 Module 3: Công cụ Giả lập Phân xử (Conflict Engine Simulator)
Trái tim của prototype, giúp trực quan hóa thuật toán giải quyết xung đột khi nhiều quảng cáo cùng nhắm vào một URL.

*   **FR3.1 - Ô kiểm tra URL (URL Tester):** Một thanh nhập liệu giả lập URL (ví dụ: người dùng nhập `https://momo.vn/blog/kinh-nghiem-mua-bao-hiem-xe-may`).
*   **FR3.2 - Công thức tính điểm (Priority Calculator):**
    Khi nhấn "Kiểm tra", hệ thống giả lập sẽ hiển thị bảng phân tích:
    $$\text{Priority Score} = \text{Campaign Weight} + \text{Matching Weight} + \text{A/B Test Factor}$$
    *   *Campaign Weight:* Global (100) hoặc Division (50).
    *   *Matching Weight:* Retargeting (+50), CMS Tag Match (+30), URL Match (+10).
*   **FR3.3 - Hiển thị Campaign chiến thắng (Winning Campaign):**
    *   Hiển thị chiến dịch đạt điểm cao nhất sẽ được chọn để render.
    *   Nếu có conflict với các luật cứng (Global Guardrails):
        *   *Ví dụ:* Đã có 1 Popup hiển thị trong session này ➔ Chặn không cho hiện Popup thứ 2, tự động fallback xuống chiến dịch có điểm cao tiếp theo sử dụng định dạng Balloon hoặc Widget.

### 3.4 Module 4: Trình giả lập hiển thị (Live Preview Sandbox)
Giao diện chia đôi màn hình (Split screen): bên trái là Form cấu hình/Calculator, bên phải là thiết bị di động ảo (Virtual Device Sandbox).

*   **FR4.1 - Mô phỏng màn hình (Viewport Simulation):** Khung giả lập (Iframe hoặc HTML/CSS Mockup) mô phỏng trang Web momo.vn.
*   **FR4.2 - Render Ad Formats:**
    *   *Balloon:* Render một bong bóng quảng cáo nhỏ trượt nhẹ từ góc dưới màn hình.
    *   *Popup:* Hiện hộp thoại modal chiếm giữa màn hình kèm nút close (X).
    *   *Calculator Widget:* Render một form Calculator (nhập số tiền, hiển thị lãi suất ước tính) nhúng thẳng vào giữa bài blog mockup.
*   **FR4.3 - Interactive Action:** Khi người dùng click vào CTA trên thiết bị giả lập, hiển thị thông báo log: *"Redirecting to Universal Link: [URL] với UTM Parameters: [Params]"* để kiểm tra tính đúng đắn của tracking.

### 3.5 Module 5: Thiết lập A/B Testing
Mô phỏng quy trình chạy thử nghiệm phiên bản quảng cáo hoặc trang Landing Page.

*   **FR5.1 - Cấu hình A/B Test:**
    *   Nhập URL biến thể A (Variant A) và biến thể B (Variant B).
    *   Kéo thanh trượt Split Ratio (ví dụ: 50% - 50%, 80% - 20%).
*   **FR5.2 - Dashboard kết quả giả lập (Mock Analytics):**
    *   Hiển thị số liệu giả lập sau 7 ngày: Pageviews, Clicks, CTR, Dismiss Rate cho Variant A và Variant B.
    *   Nút bấm "Declare Winner" (Quyết định phiên bản chiến thắng) để áp dụng cấu hình của phiên bản đó làm chính thức.

---

## 4. UI/UX Design Requirements (Yêu cầu Giao diện)

Để tạo ấn tượng tốt và dễ sử dụng, giao diện Prototype cần tuân thủ các nguyên tắc sau:
1. **Thiết kế Chia đôi (Split-Panel Layout):**
   - **Bên trái (Control Center):** Nơi thiết lập chiến dịch, quản lý Registry và chạy simulator.
   - **Bên phải (Preview Window):** Màn hình điện thoại ảo hiển thị kết quả trực quan theo thời gian thực (Real-time update).
2. **Phong cách Dark Mode hiện đại:** Sử dụng nền tối sang trọng kết hợp màu hồng MoMo làm điểm nhấn (Accent color).
3. **Hiệu ứng mượt mà (Transitions & Micro-animations):** Các hiệu ứng xuất hiện của Popup, Balloon ads, hoặc kết quả phân xử xung đột cần có animation mượt mà để tăng trải nghiệm.

---

## 5. Technology Stack & Implementation (Định hướng Kỹ thuật)

Vì đây là một **Prototype trực quan**, ưu tiên hàng đầu là tốc độ triển khai và khả năng chạy trực tiếp trên trình duyệt mà không cần cài đặt backend phức tạp.

*   **Frontend Core:** HTML5, CSS3 (Vanilla CSS hoặc TailwindCSS), Javascript (ES6+) hoặc React/Vue (nếu muốn quản lý state tốt hơn).
*   **State Management:** Sử dụng bộ nhớ trong trang (React State hoặc Vanilla JS Object) và đồng bộ với **Local Storage** để lưu dữ liệu campaign khi người dùng reload trang.
*   **Hosting:** Có thể host tĩnh dễ dàng trên GitHub Pages, Vercel, hoặc Netlify để Bảo và Hiến có thể truy cập thử nghiệm ngay lập tức.

---

## 6. Lộ trình phát triển Prototype (Phasing)

*   **Tuần 1: Thiết kế UI & Module Preview**
    - Thiết kế khung sườn giao diện chia đôi (Split-panel).
    - Tạo các CSS Component mô phỏng Balloon, Popup và Calculator Widget trên thiết bị ảo.
*   **Tuần 2: Hoàn thiện Campaign Builder & Engine Phân xử**
    - Xây dựng form nhập liệu Campaign.
    - Lập trình thuật toán tính điểm Priority Score và logic giải quyết xung đột dựa trên URL nhập vào.
*   **Tuần 3: Tích hợp A/B Testing & Release**
    - Hoàn thiện bảng đo lường A/B test mockup.
    - Đóng gói và deploy sản phẩm lên môi trường web tĩnh để demo.

---
**[END OF PRD]**
