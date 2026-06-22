# BRD: Báo Cáo Lừa Đảo (Trust - Report Scam)

> - **Project:** Use Case Báo Cáo Lừa Đảo (Trust) - Web Growth & Inbound SEO/GEO
> - **Main URL:** momo.vn/report-scam
> - **Division:** Risk & Security (GPD Web Platform)
> - **Version:** 1.0 · Tháng 6/2026
> - **Status:** Active

---

> **Problem:** Mỗi tháng có hàng ngàn người dùng ngoài hệ sinh thái MoMo (Non-MoMo Users) bị lừa đảo trực tuyến tìm kiếm trên Google cách kiểm tra uy tín số tài khoản/số điện thoại hoặc tố giác kẻ lừa đảo. Tuy nhiên, họ gặp rào cản lớn khi phải tải app, đăng ký, đăng nhập tài khoản MoMo mới có thể gửi báo cáo trên Miniapp. Điều này làm lãng phí nguồn dữ liệu cảnh báo khổng lồ từ cộng đồng và làm tăng chi phí xử lý thủ công của CS (2.000–3.000 tickets/tháng).
> **KPI Owned:** Số lượng báo cáo lừa đảo ẩn danh được tiếp nhận và xác minh thành công trên Web (làm phong phú cơ sở dữ liệu cảnh báo cộng đồng và AI Scoring).
> **Conversion Flow:** Search "số điện thoại [SĐT] lừa đảo" / "số tài khoản [STK] lừa đảo" / "cách tố cáo lừa đảo qua mạng" → `/report-scam` hoặc `/report-scam/tra-cuu/{slug}` → Xem chỉ số tín nhiệm / Nhập mô tả kịch bản lừa đảo → AI tự động bóc tách thực thể và điền form (Autofill) → Submit thành công (Không yêu cầu đăng nhập/OTP).

---

## 1. Executive Summary

### 1.1 Elegant Problem Framing
*   **Vấn đề cốt lõi:** Nạn nhân lừa đảo trực tuyến thường có tâm lý e ngại trình báo do thủ tục phức tạp, sợ bị lộ danh tính và cảm thấy bất lực vì không biết báo cáo ở đâu. Việc bắt buộc tải app MoMo và thực hiện KYC chỉ để gửi báo cáo là rào cản quá lớn đối với Non-MoMo users.
*   **Giải pháp (The "What"):** Xây dựng Website tiếp nhận báo cáo lừa đảo không cần đăng nhập trên Web. Áp dụng công nghệ GenAI (Gemini) tự động nhận diện và điền form từ kịch bản văn bản tự do của người dùng để rút ngắn quy trình xuống còn dưới 2 phút, đảm bảo tính ẩn danh và tuân thủ pháp lý.

### 1.2 Situation
*   Mỗi tháng, hệ thống CS của MoMo tiếp nhận thủ công khoảng 2.000–3.000 ticket liên quan đến phản ánh lừa đảo.
*   Người dùng khi nghi ngờ một số điện thoại hoặc số tài khoản ngân hàng lạ thường tìm kiếm trên Google trước khi giao dịch, nhưng MoMo chưa có trang Web nào xuất hiện để cảnh báo và tiếp nhận thông tin từ nhóm đối tượng có ý định giao dịch này.

### 1.3 Complication
*   Hành vi lừa đảo tài chính qua mạng ngày càng tinh vi và thay đổi kịch bản liên tục (giả danh cơ quan công quyền, việc nhẹ lương cao, giả mạo biên lai chuyển tiền).
*   Việc thu thập dữ liệu thủ công qua form điền truyền thống có tỷ lệ bỏ dở (drop rate) rất cao do người dùng phải nhớ và tự tay nhập quá nhiều thông tin chi tiết.

### 1.4 Resolution
*   Build Landing Page `/report-scam` cho phép báo cáo ẩn danh 1 chạm.
*   Tích hợp AI Engine bóc tách thông tin tự động từ kịch bản văn bản tự do của người dùng để tự động điền form (Autofill).
*   Hợp tác với Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05 - Bộ Công an) để xây dựng Central Hub chia sẻ dữ liệu lừa đảo quốc gia.
*   Tự động sinh các trang tra cứu lừa đảo động (pSEO) theo số điện thoại/số tài khoản đã bị cảnh báo để đón đầu traffic tìm kiếm từ Google.

---

## 2. Bối Cảnh Hiện Tại

### 2.1 Hiện trạng Web Assets

| Asset | URL | Trạng thái | Ghi chú |
|---|---|---|---|
| Hub page | /report-scam | Chưa build | Landing page tiếp nhận báo cáo lừa đảo không cần đăng nhập |
| pSEO Search page | /report-scam/tra-cuu/* | Chưa build | Trang tra cứu độ uy tín của số điện thoại/số tài khoản |
| AEO/GEO Document | /report-scam/llms.txt | Chưa build | Chuẩn hóa thông tin cảnh báo an toàn cho AI Search Engines |

### 2.2 Market Size & SOV Baseline

| Thị trường | TAM (SV/tháng) | SOV Hiện tại | SOV Mục tiêu | Ghi chú |
|---|---|---|---|---|
| Tra cứu số điện thoại lừa đảo | ~12.000 | 0% | 50% | Target chính của pSEO |
| Tra cứu số tài khoản lừa đảo | ~5.000 | 0% | 40% | Kết nối dữ liệu ngân hàng đối tác |
| Tố cáo lừa đảo trực tuyến | ~3.000 | 0% | 60% | Hướng về trang tiếp nhận ẩn danh |

---

## 3. Định Hướng Dự Án

### 3.1 Product Job Cốt Lõi
*   **User nghi ngờ giao dịch lừa đảo hoặc đã là nạn nhân -> Truy cập Web MoMo không cần đăng nhập -> Gõ kịch bản lừa đảo bằng ngôn ngữ tự nhiên -> AI tự động bóc tách và điền form thông tin -> Gửi báo cáo ẩn danh hoàn tất trong 2 phút để bảo vệ bản thân và cảnh báo cộng đồng.**

### 3.2 Đối Tượng Phục Vụ
*   **Segment 1 - Nạn nhân lừa đảo (Scam Victim):** Đã bị mất tiền hoặc suýt mất tiền, muốn cảnh báo cộng đồng nhanh chóng mà không cần phơi bày danh tính hoặc thực hiện các bước KYC phức tạp.
*   **Segment 2 - Người cảnh giác (Vigilant Spender):** Nghi ngờ một số điện thoại hoặc số tài khoản lạ trước khi thực hiện giao dịch, cần tra cứu nhanh độ uy tín của thông tin đó.
*   **Segment 3 - Non-MoMo Users:** Những người dùng ngân hàng truyền thống hoặc ví điện tử khác bị lừa đảo tài chính qua tài khoản MoMo giả mạo, cần một kênh trình báo trung lập.

### 3.3 Dự Án Này KHÔNG Phải
*   KHÔNG build tính năng bên trong App MoMo (đã có Miniapp phụ trách).
*   KHÔNG cam kết bồi hoàn tài chính tự động (phải đi theo luồng CS khiếu nại riêng).
*   KHÔNG cam kết phong tỏa tài khoản ngân hàng/ví ngay lập tức khi vừa nhận báo cáo (cần qua quy trình đối soát và xác minh rủi ro).

---

## 4. Phân Tích Thị Trường & Keyword Research

### 4.1 Opportunity Map - Keyword Cluster → URL

| Cluster | SV/tháng | Intent | Target URL | Content angle |
|---|---|---|---|---|
| kiểm tra số điện thoại lừa đảo | 3.600 | Commercial | /report-scam/tra-cuu | Công cụ check độ uy tín SĐT trực tuyến |
| số tài khoản [STK] lừa đảo | 2.200 | Trans/BOFU | /report-scam/tra-cuu/[stk] | Lịch sử cảnh báo báo cáo lừa đảo của tài khoản |
| tố cáo lừa đảo qua mạng ở đâu | 1.800 | Info/MOFU | /report-scam | Hướng dẫn báo cáo ẩn danh nhanh trong 2 phút |
| báo cáo tài khoản MoMo lừa đảo | 900 | Nav/BOFU | /report-scam | Tiếp nhận báo cáo lừa đảo ẩn danh không cần đăng nhập |

---

## 5. JTBD (Jobs-to-be-Done) Analysis

### Job #SCAM-01 - Ẩn danh Tố cáo (Scam Victim)
*   *Search cluster:* "tố cáo lừa đảo ẩn danh", "báo cáo tài khoản lừa đảo qua mạng"
*   > "Tôi muốn gửi báo cáo lừa đảo để ngăn chặn kẻ xấu tiếp tục lừa người khác, nhưng tôi không muốn phải để lộ thông tin cá nhân hay trải qua các bước KYC rườm rà."

| Dimension | Nội dung |
|---|---|
| Functional | Gửi báo cáo thành công kèm bằng chứng (ảnh chụp, SĐT, STK) trong vòng 2 phút, ẩn danh hoàn toàn |
| Emotional | Cảm thấy bớt bất lực, đóng góp giá trị cho cộng đồng, không sợ bị trả thù hoặc làm lộ thông tin cá nhân |
| Social | Trở thành người có trách nhiệm bảo vệ an toàn thông tin cộng đồng |
| Trigger | Vừa bị lừa đảo chuyển khoản qua mạng |

**Giải pháp:** Landing Page `/report-scam` tích hợp AI Autofill từ văn bản mô tả tự do, lược bỏ bước OTP/đăng nhập.

---

## 6. Kiến Trúc & Scope Build

### 6.1 URL Architecture

| URL | Content Type | Mục tiêu |
|---|---|---|
| /report-scam | Hub - Pillar page | Landing page tiếp nhận báo cáo lừa đảo ẩn danh, hướng dẫn quy trình |
| /report-scam/tra-cuu | Search page | Công cụ tìm kiếm nhanh độ uy tín của SĐT/STK |
| /report-scam/tra-cuu/[sdt-stk] | pSEO Location | Trang chi tiết cảnh báo cho từng số điện thoại/số tài khoản cụ thể |
| /report-scam/llms.txt | AEO/GEO Standard | Chuẩn hóa thông tin an toàn bảo mật phục vụ các mô hình AI Search |

### 6.2 Scope Build - Core Deliverables

| Deliverable | Mô tả | Mục tiêu |
|---|---|---|
| Landing Page `/report-scam` | Giao diện thu gọn, ô nhập kịch bản tự do ở màn hình đầu tiên, không bắt buộc đăng nhập | Tăng tỷ lệ gửi báo cáo lừa đảo thành công từ web |
| **GenAI Autofill Pipeline** | AI tự động bóc tách các trường thông tin (SĐT, STK, Ngân hàng, Số tiền, Kịch bản) từ văn bản tự do của người dùng và điền sẵn vào màn hình xác nhận thông tin | Giảm ma sát điền form, hoàn thành báo cáo dưới 2 phút |
| pSEO Search Engine | Tự động sinh trang chi tiết cảnh báo cho các số điện thoại/số tài khoản đã có lịch sử bị báo cáo lừa đảo và được xác thực | Đón đầu lượng traffic tìm kiếm nghi vấn từ Google |
| A05 Central Hub Sync | API kết nối đồng bộ dữ liệu cảnh báo thời gian thực với Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao | Tăng tính xác thực dữ liệu và độ uy tín (E-E-A-T) của trang |

---

## 7. Success Metrics

### 7.1 North Star Metric
*   **Số lượng báo cáo lừa đảo ẩn danh được xác minh thành công từ Web:** Lượng báo cáo lừa đảo hợp lệ được gửi từ Website `/report-scam` mà không qua đăng nhập, được hệ thống Risk kiểm soát và ghi nhận thành công vào DB cảnh báo.

### 7.2 Organic Traffic Targets
*   **Organic Sessions:** Đạt 50K sessions/tháng sau 90 ngày launch nhờ hệ thống pSEO tra cứu số điện thoại/số tài khoản lừa đảo.
*   **CTR tới CTA báo cáo:** Đạt >= 25% người dùng truy cập trang `/report-scam` hoàn thành bước gửi báo cáo.

---

## 8. Dependencies & Constraints

### 8.1 Operational Constraints

| Dependency | Mô tả | Blocker? | Status |
|---|---|---|---|
| Risk & Security Team | Phê duyệt và cung cấp bộ quy tắc xác minh thông tin báo cáo tự động | Yes | Pending |
| A05 Connection | Đồng thuận kết nối API và chia sẻ dữ liệu Central Hub với Cục An ninh mạng | Yes | Pending |
| Legal / Compliance | Duyệt cơ chế bảo vệ dữ liệu cá nhân (Nghị định 13) cho người dùng ẩn danh | Yes | Pending |
| GenAI API Gateway | Đảm bảo hạn mức (Rate Limit) và chi phí API Gemini 1.5 Flash cho tác vụ bóc tách | No | Active |

---

## Change Log
- **Tháng 6/2026 (v1.0):** Khởi tạo tài liệu BRD Use Case Báo Cáo Lừa Đảo (Trust - Report Scam) theo quy chuẩn Web Platform.
