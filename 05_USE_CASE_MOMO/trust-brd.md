# BRD: Báo Cáo Lừa Đảo (Trust - Report Scam)

> - **Project:** Use Case Báo Cáo Lừa Đảo (Trust) - Web Growth & Inbound Web Platform
> - **Main URL:** momo.vn/report-scam
> - **Division:** Risk & Security (GPD Web Platform)
> - **Version:** 1.2 · Tháng 6/2026
> - **Status:** Active (Scope: Landing Page giới thiệu & Thu thập Báo cáo thủ công - S-P-A Framework)

---

> **Problem:** Mỗi tháng có hàng ngàn người dùng ngoài hệ sinh thái MoMo (Non-MoMo Users) bị lừa đảo trực tuyến tìm kiếm nơi tố giác kẻ lừa đảo hoặc cảnh báo cộng đồng. Tuy nhiên, họ gặp rào cản lớn khi phải tải app, đăng ký, đăng nhập tài khoản MoMo mới có thể gửi báo cáo trên Miniapp. Điều này làm lãng phí nguồn dữ liệu cảnh báo khổng lồ từ cộng đồng và làm tăng chi phí xử lý thủ công của CS (2.000–3.000 tickets/tháng).
> **KPI Owned:** Số lượng báo cáo lừa đảo ẩn danh được tiếp nhận thành công trên Web thông qua Landing Page (làm phong phú cơ sở dữ liệu cảnh báo cộng đồng và giảm tải vận hành CS).
> **Conversion Flow:** Người dùng truy cập Landing Page `/report-scam` (giới thiệu tính năng An toàn cùng MoMo) → Nhấn nút gửi báo cáo → Điền thông tin vào Form thu thập dữ liệu (nhập tay các trường cơ bản) → Người dùng gửi báo cáo → Submit thành công (Không yêu cầu đăng nhập/OTP, bảo đảm ẩn danh).

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
*   **Vấn đề cốt lõi:** Nạn nhân lừa đảo trực tuyến thường có tâm lý e ngại trình báo do thủ tục phức tạp, sợ bị lộ danh tính. Việc bắt buộc tải app MoMo và thực hiện KYC chỉ để gửi báo cáo là rào cản quá lớn đối với Non-MoMo users.
*   **Giải pháp (The "What"):** Xây dựng Landing Page tĩnh `/report-scam` nhằm giới thiệu tính năng cảnh báo và tiếp nhận báo cáo lừa đảo ẩn danh. Tích hợp một Form thu thập thông tin đơn giản cho phép người dùng tự điền tay (Manual Input) các trường cần thiết mà không cần đăng nhập/OTP, đảm bảo tính ẩn danh và tuân thủ pháp lý.

### 1.2 Situation
*   Hệ thống CS của MoMo tiếp nhận thủ công khoảng 2.000–3.000 ticket liên quan đến lừa đảo mỗi tháng.
*   Cần một Landing Page độc lập trên Web để giới thiệu các tính năng an toàn bảo mật của MoMo, tăng độ tin cậy thương hiệu (Trust Index), đồng thời kêu gọi người dùng đóng góp thông tin tố giác kẻ lừa đảo.

### 1.3 Complication
*   Người dùng có xu hướng bỏ dở điền form (drop rate cao) nếu form quá dài hoặc đòi hỏi xác thực OTP phức tạp.
*   Hệ thống cần thu thập tối giản các trường thông tin nhưng vẫn phải đảm bảo tính hợp lệ để Risk và CS có thể xác minh.

### 1.4 Resolution (S-P-A Framework Implementation)
*   **reSearch (Giai đoạn 1):** Nghiên cứu giao diện và cấu trúc Landing Page mẫu [An Toan MoMo - Landing](file:///Users/hienhv/Downloads/An%20Toan%20MoMo%20-%20Landing%20%28standalone%29%20%281%29.html). Định hình bộ trường dữ liệu tối thiểu cần thu thập trong Form (SĐT kẻ lừa đảo, STK ngân hàng, Tên ngân hàng thụ hưởng, Số tiền tổn thất, kịch bản mô tả, và ảnh chụp bằng chứng). Nghiên cứu giải pháp tuân thủ pháp lý về thu thập dữ liệu cá nhân tự nguyện (Nghị định 13/2023/NĐ-CP).
*   **Pilot (Giai đoạn 2):** Triển khai Landing Page giới thiệu tĩnh tại `/report-scam` tích hợp Form báo cáo thủ công đơn giản (không có AI, không đăng nhập). Chạy thử nghiệm trong nội bộ hoặc quy mô nhỏ để kiểm tra tính ổn định của luồng submit và đo lường tỷ lệ điền hết form (Completion Rate).
*   **Action (Giai đoạn 3):** Vận hành Landing Page chính thức rộng rãi. Kết nối API Gateway để đẩy dữ liệu form trực tiếp về cơ sở dữ liệu của Risk Team và phân phối tạo ticket tự động cho CS xử lý.

---

## 2. Bối Cảnh Hiện Tại

### 2.1 Hiện trạng Web Assets

| Asset | URL | Trạng thái | Ghi chú |
|---|---|---|---|
| Hub page | /report-scam | Chưa build | Landing page giới thiệu và thu thập báo cáo lừa đảo ẩn danh (Form nhập tay) |
| AEO/GEO Document | /report-scam/llms.txt | Chưa build | Chuẩn hóa thông tin cảnh báo an toàn cho AI Search Engines |

### 2.2 Phạm vi dự án (Scope & Out-of-Scope)
*   **In-Scope:**
    *   Phát triển Landing Page `/report-scam` dựa trên giao diện mẫu giới thiệu về tính năng "An Toàn Cùng MoMo".
    *   Tích hợp Form thu thập báo cáo lừa đảo đơn giản với các trường nhập tay:
        *   Thông tin kẻ lừa đảo (SĐT hoặc Số tài khoản + Ngân hàng thụ hưởng).
        *   Số tiền bị lừa.
        *   Hình ảnh/Tệp đính kèm bằng chứng (chụp màn hình chat, hóa đơn chuyển tiền).
        *   Nội dung mô tả ngắn kịch bản lừa đảo.
    *   Cơ chế gửi ẩn danh hoàn toàn (các trường SĐT/Email của người gửi là tùy chọn và đi kèm checkbox đồng thuận tuân thủ Nghị định 13).
*   **Out-of-Scope (Các phase tiếp theo):**
    *   Tích hợp GenAI bóc tách thực thể (Autofill) từ văn bản tự do.
    *   SEO Planning diện rộng, các trang tra cứu lừa đảo động (pSEO) `/report-scam/tra-cuu/*`.
    *   Đồng bộ API tự động với các đối tác ngoài (như A05).

---

## 3. Quy Trình S-P-A (reSearch ➔ Pilot ➔ Action)

### 3.1 Giai đoạn 1: reSearch (Khảo sát & Thiết kế)
*   **Nhiệm vụ chi tiết:**
    1.  **Phân tích Landing Page Mẫu:** Khảo sát cấu trúc giao diện file mẫu [An Toan MoMo - Landing](file:///Users/hienhv/Downloads/An%20Toan%20MoMo%20-%20Landing%20%28standalone%29%20%281%29.html) để đồng nhất ngôn ngữ thiết kế thương hiệu (Brand Guidelines), các thành phần Call-to-Action (CTA) kêu gọi gửi thông tin.
    2.  **Chuẩn hóa các trường thông tin Form:** Thống nhất với Risk và CS về các trường dữ liệu tối thiểu bắt buộc để có thể thực hiện hậu kiểm (ví dụ: SĐT/STK kẻ lừa đảo, Tên ngân hàng). Các trường khác như Số tiền, nội dung mô tả sẽ ở dạng tùy chọn để giảm ma sát điền form.
    3.  **Compliance Legal:** Thiết kế nội dung tuyên bố miễn trừ trách nhiệm và các điều khoản đồng thuận tự nguyện theo Nghị định 13/2023/NĐ-CP khi người dùng gửi báo cáo ẩn danh.

### 3.2 Giai đoạn 2: Pilot (Thử nghiệm MVP)
*   **Nhiệm vụ chi tiết:**
    1.  **Xây dựng Landing Page MVP:** Phát triển Landing Page giới thiệu tĩnh tích hợp Form nhập liệu tĩnh trực tiếp tại đường dẫn `/report-scam`.
    2.  **Kiểm thử luồng submit:** Kết nối submit form về endpoint API tạm thời để kiểm tra tính ổn định của luồng truyền nhận file bằng chứng (ảnh chụp màn hình) và dữ liệu dạng text.
    3.  **Đo lường Pilot:** Chạy thử nghiệm trên nhóm nhỏ người dùng mẫu (~50-100 người) để đo lường tỷ lệ điền hết form (Completion Rate) và thu thập phản hồi về các rào cản trải nghiệm (UX Friction).

### 3.3 Giai đoạn 3: Action (Vận hành Rộng rãi)
*   **Nhiệm vụ chi tiết:**
    1.  **Go-live Landing Page:** Triển khai chính thức Landing Page rộng rãi trên hạ tầng Web Platform.
    2.  **Đồng bộ DB Risk & CS:** Đẩy dữ liệu báo cáo hoàn thành về Risk DB để làm giàu tập dữ liệu phòng chống gian lận và tạo ticket tự động cho bộ phận nghiệp vụ CS tiến hành hậu kiểm.
    3.  **Đo lường & Tối ưu:** Theo dõi tỷ lệ chuyển đổi (Conversion Rate) của Landing Page, thiết lập nền tảng đo lường để chuẩn bị cho các phase nâng cấp tiếp theo (ví dụ: bổ sung GenAI Autofill hoặc các trang tra cứu pSEO sau này).

---

## 4. JTBD (Jobs-to-be-Done) Analysis

### Job #TRUST-02 - Tố cáo nhanh chóng không cần đăng nhập (Scam Victim)
*   > "Tôi muốn tố cáo nhanh thông tin kẻ lừa đảo mà không muốn mất thời gian tải app MoMo hay đăng ký tài khoản, để tôi có thể cảnh báo cộng đồng và hạn chế thiệt hại mà không gặp rào cản công nghệ."

| Dimension | Nội dung |
|---|---|
| **Functional** | - Đọc và hiểu tính năng giới thiệu an toàn của MoMo.<br>- Điền nhanh các trường thông tin cơ bản về kẻ lừa đảo (SĐT/STK, hình ảnh bằng chứng) và nhấn gửi ẩn danh hoàn tất dưới 2 phút. |
| **Emotional** | - Cảm thấy an tâm vì không bắt buộc để lại danh tính thực.<br>- Giải tỏa tâm lý muốn tố cáo nhanh khi vừa bị lừa đảo. |
| **Social** | - Đóng góp thông tin hữu ích giúp bảo vệ cộng đồng khỏi kẻ lừa đảo. |
| **Trigger** | - Người dùng (Non-MoMo) vừa phát hiện hoặc bị lừa đảo chuyển khoản qua tài khoản ví MoMo/Ngân hàng. |

---

## 5. Success Metrics

Do dự án tập trung vào Landing Page giới thiệu và thu thập thủ công tĩnh, các chỉ số thành công sẽ tập trung vào hiệu suất Landing Page và tỷ lệ hoàn thành form:

*   **Landing Page Conversion Rate (CTR to Form):** Đạt >= 40% (Tỷ lệ người dùng truy cập Landing Page nhấn vào nút gửi báo cáo).
*   **Form Completion Rate:** Đạt >= 70% (Tỷ lệ người dùng mở Form hoàn thành việc điền thông tin và bấm Submit thành công).
*   **Average Submission Time:** Dưới 120 giây (Thời gian trung bình người dùng hoàn tất điền form thủ công).
*   **CS Ticket Generation Success Rate:** 100% dữ liệu submit hợp lệ được tạo ticket tự động thành công trên hệ thống nghiệp vụ CS.

---

## 6. Dependencies & Constraints

| Dependency | Bộ phận | Vai trò | Trạng thái |
|---|---|---|---|
| **Risk & Security Team** | Risk | Duyệt các trường dữ liệu tối thiểu và logic xác thực báo cáo lừa đảo thủ công. | Pending |
| **Legal & Compliance** | Legal | Duyệt nội dung điều khoản miễn trừ trách nhiệm và tuân thủ Nghị định 13. | Pending |
| **Frontend/Backend Dev** | Tech | Triển khai giao diện tĩnh theo file thiết kế mẫu và API tiếp nhận submit form. | Active |

---

## Change Log
- **Tháng 6/2026 (v1.0):** Khởi tạo dự thảo tài liệu BRD.
- **22/06/2026 (v1.1):** Thu hẹp scope tập trung vào Landing Page và GenAI Autofill (S-P-A Framework).
- **22/06/2026 (v1.2):** Cập nhật thu hẹp scope tối đa theo file thiết kế mẫu [An Toan MoMo - Landing](file:///Users/hienhv/Downloads/An%20Toan%20MoMo%20-%20Landing%20%28standalone%29%20%281%29.html). **Chỉ xây dựng Landing Page giới thiệu và Form thu thập báo cáo nhập tay (thủ công)**. Loại bỏ toàn bộ GenAI Autofill, pSEO tra cứu, và kết nối A05 khỏi scope hiện tại, chuyển chúng thành kế hoạch dài hạn.
