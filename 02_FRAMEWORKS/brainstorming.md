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

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phương án</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô tả giải pháp</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ưu điểm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhược điểm</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Khả năng thực thi (1-5)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>MVP</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Làm gì?]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhanh, rẻ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chưa tối ưu UX</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5/5</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Scale</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">[Làm gì?]</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bền vững, chuẩn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tốn Dev/Content</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3/5</td>
    </tr>
  </tbody>
</table>

---

## 🚦 Gate Check
- [ ] Bạn đã hiểu rõ User Job chưa? (Nếu chưa ➔ [[jtbd-analysis]])
- [ ] Bạn đã bóc tách vấn đề về mức cơ bản nhất chưa? (Nếu chưa ➔ [[First-Principles]])
- [ ] Phương án đề xuất có vi phạm nguyên tắc an toàn không? (Nếu nghi ngờ ➔ [[Zero-Hallucination]])

## Liên kết
- Skill dùng trước: [[First-Principles]], [[critical-thinking]]
- Skill dùng sau: [[pyramid-principle]] (để trình bày), [[brd-momo]] (để đóng gói)
- Xem tổng thể: [[skill_registry]]
