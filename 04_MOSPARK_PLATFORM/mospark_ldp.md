# MoSpark - Landing Page Builder (M1)
## Business Requirement Document (BRD)

> - **Owner:** Bảo / Web Platform
> - **Key Stakeholder:** Huy Lê (VP User Growth Platform)
> - **Version:** v2.0
> - **Updated:** 2026-06-03
> - **Status:** Draft

---

## 1. Elegant Problem Statement
**Vấn đề:** Các Growth Analysts và PM/PO cần tung hàng chục chiến dịch khuyến mãi mỗi tuần, nhưng phụ thuộc hoàn toàn vào Dev/Inbound để tạo Landing Page. Điều này gây thắt cổ chai, làm tăng Time-to-Market từ 1-2 ngày lên 1-2 tuần, lãng phí tài nguyên và làm giảm động lực testing.
**Giải pháp:** MoSpark Landing Page Builder định hình lại cách làm việc theo mô hình **Agentic Org**. Thay vì tự tay tạo trang, PM/PO đóng vai trò "người điều phối" (Orchestrator) ra lệnh cho các AI Agents tự động tạo trang, lắp ráp hình ảnh, viết Thể lệ (TnC) và tích hợp Scheme khuyến mãi. Trải nghiệm "One-click Publish" giúp rút ngắn thời gian launch xuống còn 1-2 ngày với sự kiểm soát chặt chẽ về Brand và Pháp lý.

## 2. Đối tượng sử dụng & Use Cases
Dự án phục vụ những người làm chủ kết quả (Outcome Owner):
- **Growth Analysts (Full-stack):** Người nắm logic chiến dịch, dữ liệu và chịu trách nhiệm trực tiếp về KPI.
- **Product Managers (PM/PO):** Nhóm "non-tech" cần công cụ hiện thực hóa ý tưởng nhanh chóng.

**Phân loại Use Cases:**
- **In-app:** Promotion Pages (Chiến dịch ngắn hạn), Feature Promotion (Giới thiệu tính năng App), T&C & Program Details (Lưu trữ điều khoản cho CS).
- **Out-app:** Growth Marketing (Landing page chạy Ads SEO/SEM), Service Pages (Always-on authority pages), Merchant Pages (Trang cho SME).

## 3. Job-To-Be-Done (JTBD) & Bối cảnh
- **Core JTBD:** *"Khi tôi chạy một chiến dịch, tôi cần một công cụ tự động hóa khâu tạo trang, gắn tracking và tích hợp thể lệ, để tôi có thể tập trung vào việc đo lường KPI (W2A) thay vì ngồi chờ Dev code."*
- Bối cảnh: 66.7% PM "ngại cái mới" và không dám cam kết KPI nếu không có công cụ hỗ trợ chuẩn. Do đó, Builder phải đi kèm với onboarding và template có sẵn.

## 4. Phạm vi tính năng cốt lõi (MVP Core Features)
- **AI-assisted Generation:** Nhập brief (mục tiêu, đối tượng, KPI) -> Builder Agent tự sinh cấu trúc và copy.
- **Asset Integration:** Asset Agent tự động lấy hình ảnh/banner từ thư viện chuẩn Brand MoMo (MoBase V2).
- **Scheme & PFM Integration:** Module quản lý Promotion Scheme độc lập được "plug" thẳng vào Builder, đảm bảo dữ liệu quà tặng luôn chính xác và đã duyệt trước.
- **WYSIWYG Editor:** Chỉnh sửa trực quan không cần code.
- **Traffic/Click Dashboard:** Dashboard đo lường theo thời gian thực (Traffic/Click/Source) cho từng trang.

## 5. Quy trình Đưa sản phẩm ra Production (Agentic Workflow)
Chuyển dịch từ việc "tự làm" sang "điều phối AI". Quy trình 7 bước (rút ngắn từ 2 tuần xuống 1-2 ngày):
1. **Khởi tạo (Briefing):** Analyst/PM nhập bối cảnh kinh doanh, mục tiêu và KPI vào AI.
2. **AI Sản xuất (Drafting & Asset):** Builder Agent tạo trang từ template; Asset Agent chèn media chuẩn Brand.
3. **Tích hợp dữ liệu (Integration):** Tự động liên kết các Scheme khuyến mãi hoặc luồng PFM.
4. **Gate A - Review & Edit (Con người):** Analyst chỉnh sửa WYSIWYG (nếu cần), duyệt bản nháp. (QA Agent chạy ngầm check lỗi link, tracking, PII).
5. **Gate B - Phê duyệt (Compliance):** 
   - Content: Team Nội dung (BMC) duyệt.
   - Legal: Kiểm tra pháp lý & TnC.
   - Design: Đảm bảo chuẩn Brand.
   *(Lưu ý: Nếu Scheme/TnC đã được duyệt trước offline, bước này có thể Bypass để đẩy nhanh tốc độ).*
6. **Xuất bản (One-click Publish):** Đẩy lên Production, tự động kích hoạt tracking.
7. **Theo dõi (Monitor):** Analytics Agent stream data về Dashboard theo thời gian thực.

## 6. Điểm Tối ưu & Guardrails (Rào cản kiểm soát)
- **Tự động hóa Business Constraints:** Build "ẩn" các ràng buộc Brand/SEO vào trong công cụ. PM chỉ cần prompt, kết quả tự động đúng chuẩn.
- **Cơ chế Phê duyệt Tinh gọn:** Giảm tải thủ công bằng các "Guardrails" quét tự động (Quality Gate).
- **Economic Mechanism (Token Economy):** Cấp Token theo Tier/Ngân sách BU để kiểm soát chi phí gọi AI API.
- **Life-cycle Management (Auto-Sunset):** Tránh "Zombie URLs" bằng tính năng nuôi trang hoặc tự động đóng/chuyển hướng (301/410) trang cũ để giữ vững Topical Authority.

## 7. Key Success Metrics (Chỉ số đo lường)
- **Time-to-launch:** Thời gian từ Brief -> Live Page (Mục tiêu: < 1-2 ngày).
- **Self-serve rate:** % trang campaign được tạo không cần raise ticket cho Inbound.
- **KPI-committed pages:** % trang có gắn mục tiêu KPI rõ ràng (Chuyển đổi từ Requester sang Owner).
- **Cost avoided:** Số giờ Dev/Inbound tiết kiệm được (Đóng góp vào bài toán Build-vs-Buy).
- *Guardrail Metric:* Tỷ lệ vi phạm Compliance/Brand bị từ chối tại Gate B.

## 8. Lộ trình Phát triển & Go-To-Market (Next Steps)
Chiến lược tiếp cận "Beachhead": Bắt đầu từ nhóm 15% PM "Serious" có nhu cầu cao (3-5 trang/tháng) làm Design Partners.
- **P0 - Validate & Funding:** Giải quyết bài toán Build-vs-Buy (chi phí), chuẩn hóa TCO.
- **P1 - MVP Build:** Tập trung xây dựng tính năng Core (4A) và Workflow đơn lẻ (5A).
- **P2 - Assisted Rollout:** Đưa bộ Starter Template và quy trình Onboarding để phá vỡ rào cản 66.7% PM "ngại cái mới".
- **P3 - Scale & Integrate:** Scale lên workflow tự động hóa hàng loạt (Variant fan-out, A/B Testing, Multi-tenant) và tích hợp sâu PFM data.

## 9. Open Considerations (Các vấn đề cần chốt)
- **Build-vs-buy economics:** Cần số liệu chi phí TCO thực tế để xin Funding (Đang chờ xác minh).
- **Tính pháp lý của Data-capture:** Tính năng thu thập SĐT cần qua bài test về Privacy/Consent (PII) trước khi live.
- **Where pages live:** Quyết định chiến lược hạ tầng (Own domain, Webview hay In-app).
- **Replace vs Complement:** Công cụ này sẽ thay thế hoàn toàn hay chỉ bổ trợ cho luồng in-app promotion hiện tại? (Sẽ thay đổi toàn bộ câu chuyện Value Story).
