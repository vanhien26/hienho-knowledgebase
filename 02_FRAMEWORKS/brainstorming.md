# 🧠 Brainstorming - Problem Solving Protocol

## 🎯 Mục tiêu
Tìm ra 2-3 phương án giải quyết vấn đề (Approaches) với các đánh giá thiệt/hơn (Trade-offs) rõ ràng, giúp User đưa ra quyết định chính xác nhất.

---

## 🧭 Quy trình thực hiện (The Protocol)

### 1. Thu thập bối cảnh (Context Ingestion)
- Kiểm tra các file docs liên quan trong folder `03_MOSPARK_PLATFORM` hoặc `04_USE_CASE_MOMO`.
- Audit hiện trạng trên momo.vn (Fetch URL).
- Xem xét dữ liệu thực tế (GSC/GA4) nếu có.

### 2. Đặt câu hỏi làm rõ (Clarifying Questions)
Sử dụng [[critical-thinking]] để đặt tối đa 3-5 câu hỏi cho User nhằm xác định:
- Mục tiêu cuối cùng là gì? (Outcome)
- Rào cản kỹ thuật/pháp lý? (Constraints)
- Thời gian và nguồn lực cho phép? (Resources)

### 3. Đề xuất phương án (Propose Approaches)
Luôn đưa ra ít nhất 2 phương án để so sánh:
- **Phương án A (Quick Win/MVP):** Effort thấp nhất, đạt 80% kết quả, nhanh chóng validate.
- **Phương án B (Scale/Long-term):** Đầu tư bài bản, tối ưu trải nghiệm, giải quyết gốc rễ.
- **Phương án C (Creative/Edge):** Cách tiếp cận mới lạ, tận dụng công nghệ mới (AI/GEO).

### 4. Đánh giá Trade-offs
Với mỗi phương án, phải chỉ rõ:
- **Pros:** Điểm mạnh, lợi ích.
- **Cons:** Rủi ro, chi phí, thời gian.
- **MoMo Fit:** Có phù hợp với Core Mantra và OKR 2026 không?

---

## 🛠 Output Template: The Idea Matrix
Agent output bảng này cho User review:

| Phương án | Mô tả giải pháp | Ưu điểm | Nhược điểm | Khả năng thực thi (1-5) |
|:--- |:--- |:--- |:--- |:--- |
| **MVP** | [Làm gì?] | Nhanh, rẻ | Chưa tối ưu UX | 5/5 |
| **Scale** | [Làm gì?] | Bền vững, chuẩn | Tốn Dev/Content | 3/5 |

---

## 🚦 Gate Check
- [ ] Bạn đã hiểu rõ User Job chưa? (Nếu chưa ➔ [[jtbd-analysis]])
- [ ] Bạn đã bóc tách vấn đề về mức cơ bản nhất chưa? (Nếu chưa ➔ [[First-Principles]])
- [ ] Phương án đề xuất có vi phạm nguyên tắc an toàn không? (Nếu nghi ngờ ➔ [[Zero-Hallucination]])

## Liên kết
- Skill dùng trước: [[First-Principles]], [[critical-thinking]]
- Skill dùng sau: [[pyramid-principle]] (để trình bày), [[brd-momo]] (để đóng gói)
- Xem tổng thể: [[skill_registry]]