# MoSpark Operational Routine (SEO & GEO Lead)

> **Vision**: Vận hành MoSpark như một Growth Engine tự động hóa, đảm bảo 100% nội dung đạt chuẩn E-E-A-T và tối ưu tỷ lệ Web-to-App.

---

## 1. Daily Health Check (15-30 phút)
*Mục tiêu: Đảm bảo "mạch máu" dữ liệu và hệ thống luôn thông suốt.*

*   **Audit Real-time**: Kiểm tra nhanh các nội dung mới xuất bản qua biến `Project` trên MoSpark.
*   **Gatekeeper Alert**: Tiếp nhận các yêu cầu Review từ team Inbound/Agency thông qua SEO/GEO Scoring.
*   **Critical Monitoring**: Observe tình trạng Indexing và Search Console của các dự án P0 (Phạt Nguội, Vay Nhanh).
*   **AI Crawler Check**: Spot-check server logs cho OAI-SearchBot, Claude-SearchBot, PerplexityBot trên các page mới golive.

---

## 2. Weekly Orchestration (Vòng lặp 7 ngày)
*Mục tiêu: Điều phối nguồn lực và xử lý các nút thắt cổ chai.*

### Thứ 2: Planning & Alignment
*   Review **Project Orchestrator**: Cập nhật trạng thái Step 01-09 cho các dự án đang chạy.
*   Check-in với **Anh Bảo (Lead)**: Align về Roadmap tính năng mới của MoSpark (Simulation, API integration).

### Thứ 4: Quality Audit
*   Audit chuyên sâu 1 Use Case cụ thể (Ví dụ: Tuần 1: Cinema, Tuần 2: Vay Nhanh...).
*   Check lỗi Tech debt: Schema, Redirect 301, CWV (LCP < 2.5s).
*   Verify robots.txt đang allow đúng các AI search crawlers (OAI-SearchBot, Claude-SearchBot, PerplexityBot).

### Thứ 6: Governance & Support
*   Review bộ **GenAI Prompts**: Hiệu chỉnh Outline/Writer prompts dựa trên kết quả Ranking thực tế.
*   Support team **DA (Hải/Hoàng)**: Kiểm tra tính đúng đắn của Tracking Plan cho các Landing Page mới.
*   Check **llms.txt** các use case đang live: URLs có còn 200 OK không, có product mới cần add không.

---

## 3. Monthly Strategic Review (Vòng lặp 30 ngày)
*Mục tiêu: Đánh giá hiệu quả đầu tư và tối ưu hóa hệ thống.*

*   **SEO Inventory Audit**: Cập nhật SoV (Share of Voice) của MoMo so với đối thủ (Ví dụ: Vay Nhanh 6% -> Mục tiêu 10%).
*   **Migration Cleanup**: Rà soát các URLs cũ đã chuyển sang MoSpark, đảm bảo 100% Link Integrity.
*   **Standard Update**: Cập nhật **momo-seo-geo-guideline** và **YMYL Guideline** dựa trên các thuật toán mới của Google/AI Search.
*   **AI Citation Audit**: Test monthly - hỏi ChatGPT/Perplexity/Claude về các sản phẩm MoMo, kiểm tra AI đang describe đúng chưa. Nếu sai lệch → review llms.txt + Long Content nguồn.
*   **llms.txt Quarterly Review**: Verify toàn bộ URLs trong llms.txt trả về 200 OK. Update nếu có product mới hoặc URL thay đổi.

---

## 4. Workflow theo Dự án (Project-based Variable Logic)

Mỗi khi có một Use Case mới (Ví dụ: `Dịch vụ công`), Routine thực thi sẽ là:

1.  **Define Project**: Khởi tạo biến `Project: Dịch vụ công` trên MoSpark.
2.  **Mapping Hierarchy**: Phân bổ URL cho các cụm trang (Blog, News, Help, Guides...).
3.  **Prompt Setup**: Chọn bộ Skill/Prompt phù hợp cho Use Case đó (Finance vs Lifestyle).
4.  **Gate Check**: Chỉ Sign-off xuất bản khi điểm **SEO Score > 80** và **Foundation Checklist** đạt 100%.
5.  **Tracking Handoff**: Gửi Event Spec cho team DA và Observe kết quả.

---

## 5. Các "Nút bấm" Quyết định (Decision Gates)

| Tình huống | Quyết định của Hiến |
|------------|---------------------|
| Content Score < 80 | **Reject**: Yêu cầu Inbound/Agency sửa lại theo Guideline. |
| Use Case không có Search Demand | **Deprioritize**: Chuyển xuống hàng chờ, không đầu tư Resource. |
| Lỗi Tech/Platform | **Request**: Gửi yêu cầu cho Anh Bảo xử lý trong Roadmap. |
| Sai lệch Tracking | **Consult**: Support team DA tìm ra "Truth of Source". |

---
*Last Updated: 05/05/2026*
