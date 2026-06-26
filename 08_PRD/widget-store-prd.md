# PRD: MoSpark Widget Store Platform

> - **Document Version:** 1.2 (Restructured & PLG Reoriented)
> - **Product Manager:** Hiến (Project Manager)
> - **Backend, API & Logic Builder:** Hiếu (Backend, API Config, Logic Code)
> - **Widget & Utility Manager:** Thuận (Đóng gói & quản trị Widget để phân phối qua Ads Manager)
> - **Target Release:** Q3/2026 (Phase 1)
> - **Status:** PRD Approved for Development

---

## 1. Product Overview & Core Definition (Tổng quan & Định nghĩa lõi)

### 1.1 Vấn đề (Problem Statement)
Các Business Unit (BU) cần các công cụ tương tác động (máy tính lãi suất, giả lập đầu tư, form khảo sát) trên Web để giữ chân khách hàng và tạo chuyển đổi Web-to-App (W2A). Hiện tại, mỗi công cụ phải được lập trình (hardcode) riêng lẻ, tốn nhiều tuần phát triển, không thể tái sử dụng, và rời rạc về mặt kiến trúc dữ liệu.

### 1.2 Giải pháp & Định nghĩa Widget (Product Vision & Widget Definition)
Xây dựng **PLG Growth Utilities Engine** — một thư viện các cấu phần tiện ích tương tác chuẩn hóa, được tối ưu hóa sâu về UX, SEO và chuyển đổi, tích hợp thẳng vào MoSpark CMS. 

#### 📌 Định nghĩa Widget trong Hệ thống:
**Widget (Tiện ích Tương tác Tăng trưởng)** là một thành phần tương tác hoàn chỉnh, khép kín về mặt giao diện (UI), logic nghiệp vụ (Logic) và dữ liệu (Data) chạy trực tiếp trên trình duyệt Web.
*   **Mục tiêu PLG**: Giải quyết trực tiếp một nhu cầu tra cứu/giả lập cụ thể của người dùng trên Web để cung cấp giá trị tức thì (*Aha! Moment*), thu hút lưu lượng tự nhiên (SEO/GEO) và chuyển đổi người dùng sang App MoMo (Web-to-App) thông qua cơ chế truyền tham số ngữ cảnh (Context-Passing) và Smart CTA.
*   **Nguyên tắc "3 Không & 3 Có"**:
    *   **3 Không**:
        *   **Không** phải là một UI component đơn lẻ (như Button, Slider) mà là tổ hợp tương tác hoàn chỉnh.
        *   **Không** cho phép BUs tùy biến giao diện tự do (để bảo vệ tính nhất quán của Design System).
        *   **Không** cho phép BUs tự cấu hình công thức tính toán nghiệp vụ (để bảo vệ tính tuân thủ pháp lý/tài chính YMYL).
    *   **3 Có**:
        *   **Có** logic tự tính toán độc lập (Offline calculation hoặc Online API fetching).
        *   **Có** cơ chế truyền/nhận dữ liệu qua URL parameters (`?prefill=`).
        *   **Có** cơ chế tự động chuyển đổi nút hành động theo ngữ cảnh dữ liệu nhập vào (Smart CTA).

### 1.3 Success Metrics (KPIs)
*Dự án hiện chưa chốt con số KPI cụ thể cho các vi chỉ số tương tác. Web Platform thống nhất hướng đến các chỉ số tăng trưởng (Growth) lõi của MoMo:*
*   **MEU (Monthly Earning Users):** Tăng trưởng số lượng người dùng có phát sinh thu nhập/giao dịch tài chính thông qua Web-to-App.
*   **MAU (Monthly Active Users):** Đóng góp vào tổng lượng người dùng hoạt động hàng tháng của MoMo.
*   **New Users:** Thu hút người dùng mới cài đặt App thông qua các tiện ích SEO/GEO có giá trị cao.

---

## 2. User Roles & JTBD Matrix (Vai trò người dùng & Ma trận JTBD)

### 2.1 End-User (Người dùng cuối)
*   **Persona:** Dân văn phòng, GenZ có nhu cầu tra cứu nhanh thông tin tài chính/đời sống trên Google.
*   **US1 (Discovery - Active Lookup):** Là người dùng, tôi muốn sử dụng công cụ tính toán ngay trên trình duyệt di động mà không cần tải App từ đầu, để tôi có thể xem kết quả nhanh chóng.
*   **US2 (Contextual Onboarding):** Là người dùng, khi tôi tính toán số tiền tiết kiệm 50 triệu và click mở MoMo, tôi muốn App tự động gợi ý gói tiết kiệm 50 triệu tương ứng thay vì bắt tôi nhập lại từ đầu.

### 2.2 System Admin / PM (Người vận hành MoSpark)
*   **Persona:** Product Manager, Marketing Team của các BUs.
*   **US3 (Rapid Deployment & Setup):** Là PM/PO của BU, tôi muốn nhanh chóng chọn một Widget có sẵn (ví dụ: công cụ tính thuế) từ thư viện, cấu hình các tham số truyền cảnh (prefill) và liên kết điều hướng CTA thích hợp để nhúng vào bài viết/Landing Page thông qua CMS mà không cần nhờ Dev phát triển lại UI hay logic tính toán.
*   **US4 (A/B Testing):** Là PM, tôi muốn cấu hình thay đổi nút CTA (Call-to-Action) của Widget theo từng chiến dịch để test tỷ lệ chuyển đổi.

---

## 3. Layout Standards (Bố cục 6 Slots chuẩn hóa)

Mỗi trang Landing Page chứa Widget phải tuân thủ bố cục cấu trúc chuẩn hóa gồm 6 Slots dưới đây để đảm bảo trải nghiệm người dùng tối ưu và chuẩn SEO/GEO:
1.  **Header (Slot 1):** Tiêu đề H1, mô tả ngắn gọn, Rating Schema (Độ tin cậy từ chuyên gia).
2.  **Input Form (Slot 2):** Khu vực nhập liệu của Widget (Input text, Dropdown, Slider kéo thả) - không cho phép sửa đổi CSS tùy tiện bởi BUs.
3.  **Result Dashboard (Slot 3):** Khu vực trả kết quả của Widget, có biểu đồ trực quan (Pie chart, Bar chart).
4.  **Context (Slot 4):** So sánh đa chiều (Ví dụ: So sánh gửi ngân hàng vs Mua chứng chỉ quỹ).
5.  **Smart CTA (Slot 5):** Banner động chứa Onelink để kích hoạt mở App. Tự động nhận diện Intent của người dùng để trả về CTA tương ứng (Ví dụ: Lương < 15 triệu -> CTA "Ví Trả Sau"; Lương > 40 triệu -> CTA "Mở Thẻ Tín Dụng").
6.  **SEO Hub (Slot 6):** Block FAQ (Schema) và Internal Links liên quan từ các bài viết vệ tinh.

---

## 4. Technical Specifications & Core Capabilities (Thông số kỹ thuật & Năng lực lõi)

### 4.1 Widget Component Registry & Rendering Engine
*   **FR1 - Registry & Render Component:** MoSpark Engine hoạt động như một Registry lưu trữ danh sách các Component Widget tĩnh/động được phát triển bởi Core Team. Hệ thống nhận diện shortcode hoặc block nhúng trong CMS Editor và render đúng Component React tương ứng với các tham số truyền vào từ CMS (như default values, CTA URLs, prefill flags), giữ tính nhất quán về UX/UI và công thức tính toán.

### 4.2 API Integration & Governance Gateway
*   **FR2 - Online Fetching:** Các Widget (Vàng, Tỷ giá, Lãi tiết kiệm, Đầu tư) yêu cầu Backend thiết lập Gateway kết nối với API nội bộ của App MoMo để lấy dữ liệu realtime. Có cơ chế Cache (Redis) 15-30 phút để giảm tải.
*   **FR3 - Offline Calculation:** Các Widget (Thuế, BHXH, Lương hưu, BHSK+) hoạt động bằng công thức toán học nội bộ (Offline). Logic công thức được cấu hình trong các file JSON tĩnh trên server được kiểm duyệt pháp lý và triển khai tập trung bởi Core Growth Team (không cho phép PM/PO của BU tự ý chỉnh sửa công thức tính toán trên CMS để tránh rủi ro pháp lý/tài chính YMYL).

### 4.3 Zero-Party Data Passing
*   Dữ liệu người dùng nhập (Lương, số tiền muốn vay) sẽ được parse thành chuỗi Base64 hoặc JSON.
*   Nối chuỗi này vào URL Parameters của Onelink. Khi App mở, đọc params và điền tự động vào màn hình in-app.

---

## 5. Phase 1 Pilot Specifications (Đặc tả 10 Tiện ích MVP)

1.  **Master Widget (Phân bổ lương):** Hub chính. Nhập tổng thu nhập ➔ Chia ra rổ chi tiêu, tiết kiệm. Tự động truyền tham số (prefill) sang các Widget con.
2.  **Gold Tracker:** Tích hợp API giá vàng Real-time, biểu đồ lịch sử ➔ CTA: Mua vàng.
3.  **Exchange Rate:** Quy đổi ngoại tệ ➔ CTA: Chuyển tiền quốc tế.
4.  **Gross-Net Tax:** Tính lương thực nhận, BHYT, BHXH ➔ CTA: Gửi tiết kiệm / Ví Trả Sau.
5.  **Lãi Tiết Kiệm:** Kéo slider chọn kỳ hạn, tính lãi cuối kỳ ➔ CTA: Mở sổ tiết kiệm MoMo.
6.  **Tính BHXH:** Tính mức đóng và mức hưởng 1 lần ➔ CTA: Tích lũy hưu trí.
7.  **Tính Lương hưu:** Tính tuổi nghỉ hưu, tỷ lệ hưởng ➔ CTA: Đầu tư dài hạn.
8.  **Đầu tư Chứng khoán/CCQ:** Kéo API lịch sử mã cổ phiếu (Ví dụ: FPT), giả lập lãi nếu đầu tư từ 1 năm trước ➔ CTA: Mở tài khoản Vietcap.
9.  **Tính phí BHSK+:** Thanh kéo mức độ nghiêm trọng rủi ro, đối chiếu chi phí phải trả tự túc vs có BHSK ➔ CTA: Mua MoMo Sức Khỏe+.
10. **Financial Quiz:** Trắc nghiệm vuốt (Tinder-style), trả kết quả "Chức danh" (Persona) ➔ CTA: Nhận Voucher (Instant Reward).

---

## 6. Phasing & Release Plan (Lộ trình phát hành)

*   **Phase 1 (MVP - Q3/2026):** Hoàn thiện Widget Engine, Master Widget, và 10 Tiện ích Finhub. Tích hợp Onelink cơ bản.
*   **Phase 2 (Scale - Q4/2026):** Mở rộng tích hợp các Widget mới từ Bảo hiểm, Du lịch & Đi lại (tính giá vé, gợi ý tour) hoặc tiện ích đời sống. Triển khai tính năng Smart CTA.
*   **Phase 3 (Advanced PLG Scaling - 2027):** Phát triển các tính năng PLG nâng cao bao gồm Programmatic pSEO Lookups ở quy mô lớn (tự động tạo hàng ngàn trang tra cứu địa phương hóa), AI Intent-based routing cho Smart CTA, và phát triển B2B Syndication (cung cấp các widget chuẩn để nhúng trên các trang báo chí, đối tác ngoài để kéo traffic ngược về MoMo).

---

## 7. Non-Functional Requirements (Yêu cầu Phi chức năng)

### 7.1 Performance & Speed
*   **Core Web Vitals:** Do Widget nhúng vào Landing Page, thời gian render (LCP) phải < 2.5s. Tốc độ phản hồi khi kéo slider (INP) < 200ms.
*   **Bundle Size:** JS bundle của mỗi Widget không được vượt quá 100KB (Gzipped) để không làm chậm trang đích.

### 7.2 SEO & Semantic
*   Hệ thống bắt buộc tự động render thẻ JSON-LD `SoftwareApplication` và `FinancialProduct` cho trang chứa Widget.
*   Tuân thủ chuẩn Accessibility (ARIA tags cho các Slider/Input) để bot AI có thể cào dữ liệu công cụ.

### 7.3 Legal & Security
*   **Disclaimer:** Mọi kết quả từ Widget (đặc biệt là Thuế, Vay, Đầu tư) phải luôn đi kèm dòng chữ: *"Kết quả mang tính chất tham khảo. MoMo không chịu trách nhiệm pháp lý..."*
*   **Data Privacy:** Zero-Party data truyền qua URL Parameters không được chứa PII (Thông tin định danh cá nhân) dạng plain text, phải hash/encode.

---
**[END OF PRD]**
