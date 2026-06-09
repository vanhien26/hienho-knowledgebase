# PRD: MoSpark Widget Store Platform

> - **Document Version:** 1.0 (Refactored from BRD v3.3)
> - **Product Manager:** Hiến (Project Manager)
> - **Build Lead:** Hiếu
> - **Backend/API Lead:** Hoài Anh
> - **Target Release:** Q3/2026 (Phase 1)
> - **Status:** PRD Approved for Development

---

## 1. Product Overview (Tổng quan Sản phẩm)

### 1.1 Vấn đề (Problem Statement)
Các Business Unit (BU) cần các công cụ tương tác động (máy tính lãi suất, giả lập đầu tư, form khảo sát) trên Web để giữ chân khách hàng và tạo chuyển đổi Web-to-App (W2A). Hiện tại, mỗi công cụ phải được lập trình (hardcode) riêng lẻ, tốn nhiều tuần phát triển, không thể tái sử dụng, và rời rạc về mặt kiến trúc dữ liệu.

### 1.2 Giải pháp (Product Vision)
Xây dựng **Widget Store Platform** — một hệ sinh thái tiện ích tương tác tập trung được tích hợp thẳng vào MoSpark CMS. Sản phẩm cung cấp một "Widget Engine" dùng chung, cho phép phân phối (embed) các công cụ tài chính/đời sống động vào bất kỳ trang Web nào thông qua mã Shortcode, tự động hóa quy trình chuyển đổi người dùng từ Web sang App MoMo thông qua cơ chế Context-Passing và Smart CTA.

### 1.3 Success Metrics (KPIs)
*Dự án hiện chưa chốt con số KPI cụ thể cho các vi chỉ số tương tác. Web Platform thống nhất hướng đến các chỉ số tăng trưởng (Growth) lõi của MoMo:*
*   **MEU (Monthly Earning Users):** Tăng trưởng số lượng người dùng có phát sinh thu nhập/giao dịch tài chính thông qua Web-to-App.
*   **MAU (Monthly Active Users):** Đóng góp vào tổng lượng người dùng hoạt động hàng tháng của MoMo.
*   **New Users:** Thu hút người dùng mới cài đặt App thông qua các tiện ích SEO/GEO có giá trị cao.

---

## 2. User Roles & User Stories

### 2.1 End-User (Người dùng cuối)
*   **Persona:** Dân văn phòng, GenZ có nhu cầu tra cứu nhanh thông tin tài chính/đời sống trên Google.
*   **US1 (Discovery):** Là người dùng, tôi muốn sử dụng công cụ tính toán ngay trên trình duyệt di động mà không cần tải App từ đầu, để tôi có thể xem kết quả nhanh chóng.
*   **US2 (Contextual Onboarding):** Là người dùng, khi tôi tính toán số tiền tiết kiệm 50 triệu và click mở MoMo, tôi muốn App tự động gợi ý gói tiết kiệm 50 triệu tương ứng thay vì bắt tôi nhập lại từ đầu.

### 2.2 System Admin / PM (Người vận hành MoSpark)
*   **Persona:** Product Manager, Marketing Team của các BUs.
*   **US3 (Self-serve Creation):** Là PM, tôi muốn sử dụng MoSpark Editor để chọn một Widget có sẵn, tùy chỉnh tiêu đề/màu sắc và lấy mã Shortcode nhúng vào bài Blog chỉ trong 5 phút mà không cần nhờ Dev.
*   **US4 (A/B Testing):** Là PM, tôi muốn cấu hình thay đổi nút CTA (Call-to-Action) của Widget theo từng chiến dịch để test tỷ lệ chuyển đổi.

---

## 3. Functional Requirements (Yêu cầu chức năng - Frontend)

### 3.1 Cấu trúc Giao diện Chuẩn (6 Slots Framework)
Mỗi trang Landing Page chứa Widget phải tuân thủ layout 6 phần:
1.  **Header (Slot 1):** Tiêu đề H1, mô tả ngắn gọn, Rating Schema.
2.  **Input Form (Slot 2):** Khu vực nhập liệu (Input text, Dropdown, Slider kéo thả).
3.  **Result Dashboard (Slot 3):** Khu vực trả kết quả, có biểu đồ trực quan (Pie chart, Bar chart).
4.  **Context (Slot 4):** So sánh đa chiều (Ví dụ: So sánh gửi ngân hàng vs Mua chứng chỉ quỹ).
5.  **Smart CTA (Slot 5):** Banner động chứa Onelink để kích hoạt mở App.
6.  **SEO Hub (Slot 6):** Block FAQ (Schema) và Internal Links liên quan.

### 3.2 Năng lực Lõi (Core Capabilities)
*   **FR1 - Smart CTA (Điều hướng theo Intent):** 
    *   *Logic:* Widget tự động phân tích Input của người dùng để trả về CTA tương ứng. 
    *   *Rule ví dụ:* Nếu [Lương] < 15.000.000 ➔ Hiện CTA "Ví Trả Sau"; Nếu [Lương] > 40.000.000 ➔ Hiện CTA "Mở Thẻ Tín Dụng hạn mức cao".
*   **FR2 - Zero-Party Data Passing:**
    *   *Logic:* Dữ liệu người dùng nhập (Lương, số tiền muốn vay) sẽ được parse thành chuỗi Base64 hoặc JSON.
    *   *Hành động:* Nối chuỗi này vào URL Parameters của Onelink. Khi App mở, đọc params và fill tự động vào màn hình in-app.
*   **FR3 - B2B Widget Syndication (Mã nhúng):**
    *   *Logic:* Đóng gói Widget thành dạng `<script>` embed code hoặc `<iframe>`.
    *   *Rule:* Cho phép nhúng vào domain của bên thứ 3 (Báo chí, Affiliate) nhưng vẫn track được UTM source về MoMo.

### 3.3 Đặc tả Tính năng 14 Widgets (Phasing Pipeline)

#### Phase 1: Finhub Simulators (10 Widgets MVP)
1.  **Master Widget (Phân bổ lương):** Hub chính. Nhập tổng thu nhập ➔ Chia ra rổ chi tiêu, tiết kiệm. Tự động pass số dư sang các Widget con.
2.  **Gold Tracker:** Tích hợp API giá vàng Real-time, biểu đồ lịch sử ➔ CTA: Mua vàng.
3.  **Exchange Rate:** Quy đổi ngoại tệ ➔ CTA: Chuyển tiền quốc tế.
4.  **Gross-Net Tax:** Tính lương thực nhận, BHYT, BHXH ➔ CTA: Gửi tiết kiệm.
5.  **Lãi Tiết Kiệm:** Kéo slider chọn kỳ hạn, tính lãi cuối kỳ ➔ CTA: Mở sổ tiết kiệm MoMo.
6.  **Tính BHXH:** Tính mức đóng và mức hưởng 1 lần ➔ CTA: Tích lũy hưu trí.
7.  **Tính Lương hưu:** Tính tuổi nghỉ hưu, tỷ lệ hưởng ➔ CTA: Đầu tư dài hạn.
8.  **Đầu tư Chứng khoán/CCQ:** Kéo API lịch sử mã cổ phiếu (Ví dụ: FPT), giả lập lãi nếu đầu tư từ 1 năm trước ➔ CTA: Mở tài khoản Vietcap.
9.  **Tính phí BHSK+:** Thanh kéo mức độ nghiêm trọng rủi ro, đối chiếu chi phí phải trả tự túc vs có BHSK ➔ CTA: Mua MoMo Sức Khỏe+.
10. **Financial Quiz:** Trắc nghiệm vuốt (Tinder-style), trả kết quả "Chức danh" (Persona) ➔ CTA: Nhận Voucher (Instant Reward).

#### Phase 2: Lifestyle & Travel Widgets (4 Widgets Tăng trưởng)
11. **The Latte Factor (Trà sữa):** Tính chi phí uống trà sữa 1 năm vs Đầu tư sinh lời ➔ CTA: Túi Thần Tài.
12. **Trip Budget Planner:** Tính chi phí du lịch dựa trên API MoMo Travel, chia tiền nhóm ➔ CTA: Đặt vé / Tạo Quỹ nhóm.
13. **Traffic Fine Simulator:** Tính mức phạt vi phạm giao thông theo Nghị định 100 ➔ CTA: Tra cứu & Đóng phạt nguội.
14. **Rent vs Buy (Thuê hay Mua nhà):** So sánh dòng tiền 20 năm ➔ CTA: Vay mua nhà / Đầu tư.

---

## 4. Functional Requirements (Yêu cầu chức năng - Backend CMS)

### 4.1 Shortcode Engine
*   **FR4 - Render Widget:** MoSpark Engine phải nhận diện chuỗi `[widget:{id} parameter="value"]` trong nội dung Rich Text và render thành component React tương ứng.

### 4.2 API Integration Gateway
*   **FR5 - Online Fetching:** Các Widget (Vàng, Tỷ giá, Lãi tiết kiệm, Đầu tư, Du lịch) yêu cầu Backend thiết lập Gateway kết nối với API nội bộ của App MoMo để lấy dữ liệu realtime. Có cơ chế Cache (Redis) 15-30 phút để giảm tải.
*   **FR6 - Offline Calculation:** Các Widget (Thuế, BHXH, Phạt giao thông) hoạt động bằng công thức toán học nội bộ (Offline). Cho phép Admin cập nhật file cấu hình JSON (chứa tỷ lệ thuế, mức phạt) thông qua CMS mà không cần deploy lại code.

---

## 5. Non-Functional Requirements (Yêu cầu Phi chức năng)

### 5.1 Performance (Hiệu năng)
*   **Core Web Vitals:** Do Widget nhúng vào Landing Page, thời gian render (LCP) phải < 2.5s. Tốc độ phản hồi khi kéo slider (INP) < 200ms.
*   **Bundle Size:** JS bundle của mỗi Widget không được vượt quá 100KB (Gzipped) để không làm chậm trang đích.

### 5.2 SEO & Semantic
*   Hệ thống bắt buộc tự động render thẻ JSON-LD `SoftwareApplication` và `FinancialProduct` cho trang chứa Widget.
*   Tuân thủ chuẩn Accessibility (ARIA tags cho các Slider/Input) để bot AI có thể cào dữ liệu công cụ.

### 5.3 Legal & Security
*   **Disclaimer:** Mọi kết quả từ Widget (đặc biệt là Thuế, Vay, Đầu tư) phải luôn đi kèm dòng chữ: *"Kết quả mang tính chất tham khảo. MoMo không chịu trách nhiệm pháp lý..."*
*   **Data Privacy:** Zero-Party data truyền qua URL Parameters không được chứa PII (Thông tin định danh cá nhân) dạng plain text, phải hash/encode.

---

## 6. Phasing & Release Plan (Lộ trình phát hành)

*   **Phase 1 (MVP - Q3/2026):** Hoàn thiện Widget Engine, Master Widget, và 10 Tiện ích Finhub. Tích hợp Onelink cơ bản.
*   **Phase 2 (Scale - Q4/2026):** Ra mắt 4 Tiện ích Lifestyle. Triển khai tính năng Smart CTA và B2B Widget Syndication (<iframe>).
*   **Phase 3 (Platformization - 2027):** Mở khóa **KOL/KOC Marketplace** (Công cụ Low-code cho phép các chuyên gia tài chính tự build Widget mang thương hiệu của họ).

---
**[END OF PRD]**
