# 🗺️ Knowledge Routing & Context Pipeline (Bản Đồ Định Tuyến Dữ Liệu SSOT)

> **Mục đích:** Quy định nguyên tắc phân loại khái niệm, định tuyến từ khóa và chỉ định nguồn dữ liệu chuẩn mực (Single Source of Truth - SSOT) cho hệ thống và AI khi làm việc trong Knowledge Base MoMo.
> **Owner:** Văn Hiến - Web Product Lead
> **Cập nhật gần nhất:** 31/07/2026

---

## 📌 1. BẢNG ĐỊNH TUYẾN DỮ LIỆU & PHÂN BIỆT KHÁI NIỆM (SSOT ROUTING MATRIX)

| Khái niệm / Từ khóa | Phân loại & Bản chất khái niệm | Thư mục & File SSOT | Quy tắc Truy xuất & Tránh nhầm lẫn |
| :--- | :--- | :--- | :--- |
| **Townhall** | Buổi sinh hoạt toàn công ty định kỳ do **Ban Lãnh Đạo (BOM / C-Level)** chủ trì. Tập trung vào kết quả kinh doanh vĩ mô, chỉ số User Trust Index, định hướng chiến lược (Trust-led Growth), tư duy vận hành (Thuật toán 5 bước) và bài toán/điểm nghẽn toàn công ty. | 📂 `07_REPORTS/`<br>📄 `townhall-*.md`<br>📄 `leadership-mindset-log.md` | ❌ **KHÔNG** nhầm với báo cáo tháng của team (`report-thang-*.md`).<br>✅ **CHỈ** lấy chỉ đạo vĩ mô từ BOM và định hướng C-Level. |
| **Monthly Report** | Báo cáo hiệu suất kinh doanh, traffic, W2A, điểm nhấn dự án và tiến độ sprint hàng tháng của **Web Platform Team**. | 📂 `07_REPORTS/`<br>📄 `report-thang-MM-YYYY.md` | 🔍 Tìm đúng file theo tháng yêu cầu (Ví dụ: `report-thang-07-2026.md`). |
| **Strategic Plan & OKRs** | Định hướng chiến lược dài hạn H1/H2, mục tiêu North Star, cam kết chỉ số vĩ mô cho C-Level (6.0M MUA, W2A > 10%). | 📂 `01_STRATEGIC_PLAN/`<br>📄 `h2-2026-report.md` | Đọc để lấy khung chiến lược và cam kết KPI tổng thể. |
| **BRD (Business Requirements)** | Tài liệu đặc tả yêu cầu kinh doanh, bài toán Use Case và luồng trải nghiệm cho các dịch vụ MoMo (Phạt Nguội, Cinema, eSIM, Ví Trả Sau, Vay Nhanh...). | 📂 `05_HUBS/`<br>📂 `06_USE_CASE_MOMO/` | Đọc file BRD mới nhất của Use Case tương ứng. |
| **PRD (Product Requirements)** | Tài liệu đặc tả tính năng sản phẩm kỹ thuật chi tiết dành cho Đội ngũ Phát triển (Dev/Product). | 📂 `09_PRD/` | Tham chiếu khi cần chi tiết về tính năng/release. |
| **MoSpark Platform & Tech** | Kiến trúc hạ tầng MoSpark, GenAI Content Engine, Widget Store Registry, CMS Editor, FPT Cloud integration. | 📂 `04_MOSPARK_PLATFORM/` | Tham chiếu khi liên quan đến khả năng hệ thống Web Platform. |
| **Frameworks & Skills** | Hệ thống tư duy (80/20 Growth, JTBD, Pyramid Principle) và tiêu chuẩn SEO/GEO/AEO, YMYL Guidelines. | 📂 `02_FRAMEWORKS/`<br>📂 `03_SKILLS/` | Đọc để áp dụng đúng phương pháp luận khi phân tích & viết bài. |
| **Decision Log** | Nhật ký ghi nhận các quyết định kiến trúc, sản phẩm và chiến lược quan trọng đã được chốt. | 📂 `08_DECISION_LOG/` | Đọc để hiểu lý do lịch sử đằng sau các quyết định. |

---

## 🔍 2. PIPELINE XỬ LÝ KHI AI TIẾP NHẬN YÊU CẦU (AI RETRIEVAL PIPELINE)

Khi nhận một truy vấn từ người dùng, AI phải thực hiện định tuyến theo 3 bước:

```
[User Request] 
       ↓ 
1. Phân loại Ý định (Intent Classification): Tìm từ khóa thuộc nhóm nào trong Bảng Định Tuyến.
       ↓ 
2. Trỏ tới File SSOT: Chỉ mở và đọc file đúng thư mục chỉ định (Tránh đọc nhầm loại tài liệu).
       ↓ 
3. Kiểm tra ranh giới khái niệm (Boundary Check): Đối soát để chắc chắn thông tin trả ra đúng ngữ cảnh (E.g., Townhall ≠ Report).
```

---

## ⚠️ 3. CÁC NGUYÊN TẮC CỐT LÕI KHÁC (CORE CONSTRAINTS)

1. **Khái niệm Townhall:** Mọi truy vấn liên quan đến "Townhall", "Town Hall", "Chỉ đạo BOM", "BOM Mindset" bắt buộc chỉ trỏ về `07_REPORTS/townhall-*.md` và `leadership-mindset-log.md`.
2. **Single Source of Truth:** Không tự tạo giả định nếu thông tin chưa có trong Vault; nếu có thông tin mâu thuẫn giữa file cá nhân và file Master, ưu tiên file Master mới nhất tại thư mục quy định.
