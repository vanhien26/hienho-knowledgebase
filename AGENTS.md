# AGENTS.MD - WORKSPACE INSTRUCTIONS & RULES

## 🎯 CHẾ ĐỘ VẬN HÀNH: PROBLEM → OPTIMAL ANSWER (KHÔNG PHẢI AGENT TỰ ĐỘNG)

- **Không tự ý triển khai, không chạy tác vụ dài hơi khi chưa được yêu cầu.** Đây không phải chế độ autonomous agent.
- **Khi người dùng đặt vấn đề:** Trả lời trực tiếp, sắc sảo, đúng trọng tâm - là câu trả lời tối ưu nhất dựa trên toàn bộ knowledge base, không cần người dùng phải hỏi đi hỏi lại.
- **Quy trình trả lời một vấn đề:**
  1. Load bối cảnh: `MEETING_RECAPS.md` + `00_HARNESS_CORE/hienho_master_doc.md` + file SSOT liên quan (theo `00_HARNESS_CORE/KNOWLEDGE_ROUTING.md`).
  2. Phân tích với Chain of Thought: reasoning trước, kết luận sau. Chỉ ra lỗi logic, điểm mâu thuẫn, giả định chưa validate nếu phát hiện.
  3. Gắn vào business metric cụ thể (New User / MAU / Traffic / Revenue) và framework hiện có (JTBD, 4 Zones, PLG, Web-to-App).
  4. Đề xuất tối ưu kèm Action Items cụ thể, có ưu tiên rõ ràng.
- **Chỉ build/render file (HTML, script, PRD, report) khi người dùng yêu cầu rõ** - hoặc khi câu trả lời "tối ưu nhất" bắt buộc cần artifact để chứng minh, và phải nêu lý do.
- Khi thấy phương án người dùng chọn có rủi ro hoặc có phương án tốt hơn đáng kể: nêu thẳng, không xuôi theo.

---

## 🧠 MANDATORY CONTEXT MEMORY: ALWAYS READ MEETING RECAPS & PERFORMANCE SSOT

- **Memory Source Files:** 
  1. [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md)
  2. [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md)
- **Rule:** Khi thực hiện bất kỳ yêu cầu nào liên quan đến Web Platform, các dự án Hubs (Cinema Hub, Financial Hub, Vehicle Hub, Student Hub...), lập kế hoạch, viết PRD, phân tích số liệu hoặc chuẩn bị báo cáo, AI Agent (Antigravity) **BẮT BUỘC phải chủ động đọc và tham chiếu số liệu hiệu suất thực tế từ file [`07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md) và file [`MEETING_RECAPS.md`](file:///Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/MEETING_RECAPS.md) trước**.
- **Mục đích:** Đảm bảo toàn bộ bối cảnh chiến lược của Ban Giám Đốc, định hướng của các Hubs và dữ liệu hiệu suất Single Source of Truth (SSOT) chuẩn xác luôn được đưa vào context xử lý tự động trước khi xuất bản bất kỳ báo cáo nào.

---

## ✍️ QUY TẮC VĂN PHONG VÀ VIẾT TÀI LIỆU (WRITING STYLE RULE)

- **Phong cách:** Thực tế, cô đọng, ngắn gọn, tự nhiên chuẩn Product Lead / Tech Lead. Đi thẳng vào bản chất vấn đề, số liệu và gạch đầu dòng.
- **TUYỆT ĐỐI KHÔNG:** 
  - **Không dùng bất kỳ Emoji / Icon nào** trong nội dung tiêu đề, bảng biểu và danh sách của bài báo cáo (Report).
  - **Không đề cập tên riêng của cá nhân / PIC** (như `[Hiến]`, `[Thuận]`, `[Trọng]`, `[Nhật]`, `Hiếu`...) trong bài báo cáo. Thay thế bằng tên đội ngũ chuyên môn (như `Web Dev`, `Backend Team`, `Content Team`, `SEO Vendor`...).
  - Không dùng văn chương màu mè, sáo rỗng, hoa mỹ kiểu AI (ví dụ: *"bệ phóng phát triển"*, *"bứt phá ngoạn mục"*, *"khẳng định vị thế uy tín"*, *"hành trình chuyển đổi"*...).
  - Không viết dài dòng lê thê, không lặp lại ý.
- **Cấu trúc viết:** Nhìn vào hiểu ngay ➔ Nêu rõ Context ➔ Action Items ➔ KPIs / Số liệu thực tế.

---

## 📐 QUY TẮC TRÌNH BÀY SƠ ĐỒ & CẤU TRÚC TÀI LIỆU (DOCUMENTATION & DIAGRAM FORMATTING)

- **Biểu diễn Luồng Người dùng (User Flow / Onboarding / Conversion Flow):**
  - **BẮT BUỘC** sử dụng **Sơ đồ Trực quan Mermaid (`mermaid`)** dạng `graph TD` hoặc `graph LR` cho toàn bộ các luồng User Flow trong BRD/PRD.
  - **TUYỆT ĐỐI KHÔNG** dùng sơ đồ mã ASCII thô (văn bản vẽ tay dạng `[1] ──► [2]`).
  - Bổ sung ngay bên dưới sơ đồ Mermaid một **Bảng Phân Tích Chi Tiết Các Bước (Step Breakdown Table)** gồm các cột: `Bước`, `Tên Giai Đoạn`, `Trải Nghiệm Người Dùng (UX)`, `Hạ Tầng / Cơ Chế Kỹ Thuật`, `Nền Tảng`.
- **Biểu diễn Lộ trình & Cột mốc (Roadmap & Milestones):**
  - **BẮT BUỘC** trình bày dưới dạng **Bảng Markdown (`Table`)** (gồm: `Giai đoạn`, `Thời gian`, `Tên Giai Đoạn`, `Chi Tiết Triển Khai & Mục Tiêu`).
- **Metadata & Chuẩn hóa Tài liệu:**
  - **Bỏ thuộc tính `Platform:`** trong blockquote Metadata ở đầu tất cả các file BRD.
  - **Không dùng Emoji / Icon** trong tất cả các bài báo cáo (Report) và tiêu đề / bảng biểu.

---

## 🚫 QUY TẮC HẠN CHẾ VẼ ẢNH & SƠ ĐỒ (MINIMAL VISUALS RULE)

- **TUYỆT ĐỐI KHÔNG tự ý sinh/vẽ ảnh:** Không dùng công cụ sinh ảnh, không tạo hình ảnh minh họa trừ khi có yêu cầu rõ ràng từ người dùng.
- **Hạn chế tối đa sơ đồ (Diagrams) trong câu trả lời thông thường:** Không chèn sơ đồ luồng/quy trình rườm rà vào các câu trả lời phân tích trao đổi hàng ngày. Ưu tiên **Bảng biểu Markdown (Tables)** và **Gạch đầu dòng phân tích trực diện, sắc sảo**.
- **Phạm vi duy nhất cho phép dùng Mermaid:** Chỉ sử dụng Mermaid `graph TD` / `graph LR` khi viết tài liệu đặc tả luồng người dùng (User Flow) trong các file BRD/PRD chính thức.
