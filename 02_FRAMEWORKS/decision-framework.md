# ⚖️ Decision Framework - Speed vs Quality

## 🎯 Mục tiêu
Giúp Agent và Team biết khi nào cần quyết định nhanh (Speed) và khi nào cần dừng lại để phân tích sâu (Quality). Mục đích cuối cùng là duy trì đà tăng trưởng (Momentum) mà không gây ra các lỗi chí mạng.

---

## 🧭 Quy trình: Loại 1 vs Loại 2 Decision

### 1. Quyết định Loại 2 (Two-way doors - Khả hồi)
Đây là các quyết định có thể sửa sai nhanh chóng, chi phí thấp, rủi ro thấp.
- **Ví dụ:** Đổi màu nút CTA, thay đổi tiêu đề bài viết, thử nghiệm một format nội dung mới.
- **Protocol:** **Decide Fast.** Không cần xin phép quá nhiều cấp, không cần phân tích quá sâu. Cứ thử nghiệm (A/B test), nếu sai thì quay lại (Revert).

### 2. Quyết định Loại 1 (One-way doors - Bất khả hồi)
Đây là các quyết định khó quay đầu, tốn kém nguồn lực lớn, hoặc ảnh hưởng trực tiếp đến uy tín/pháp lý.
- **Ví dụ:** Thay đổi cấu trúc URL (slug) của toàn bộ website, thay đổi chiến lược tracking (GA4/Appsflyer), quyết định ngưng một mảng sản phẩm.
- **Protocol:** **Decide Slow.** Cần áp dụng [[critical-thinking]], [[First-Principles]] và sự phê duyệt của Stakeholder (Văn Hiến).

---

## 🛠 Framework: WRAP (Để tránh bẫy tâm lý)
Khi gặp quyết định Loại 1, hãy dùng WRAP:
1.  **W**iden your options: Có phương án C nào không? Đừng chỉ chọn Yes/No.
2.  **R**eality-test your assumptions: Đã có data thực tế chưa? Hay chỉ là cảm tính?
3.  **A**ttain distance: Nếu 10 tháng nữa nhìn lại, mình sẽ nghĩ gì về quyết định này?
4.  **P**repare to be wrong: Nếu phương án này thất bại, kế hoạch B là gì?

---

## 💡 Ứng dụng tại MoMo Web

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Quyết định</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hành động (Action)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Viết 10 bài blog cho mảng eSIM.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loại 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thực hiện ngay, monitor traffic sau 2 tuần.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mua một Domain mới để làm satellite site.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loại 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần phân tích ROI, rủi ro SEO và xin ý kiến Lead.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chỉnh sửa giao diện Tool Phạt Nguội.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Loại 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Test trên 10% user, nếu ổn thì roll-out 100%.</td>
    </tr>
  </tbody>
</table>

---

## 🚦 Gate Check
- [ ] Quyết định này là "Cửa 1 chiều" hay "Cửa 2 chiều"?
- [ ] Nếu quyết định này sai, thiệt hại lớn nhất là gì? Có sửa được không?
- [ ] Bạn có đang quá cầu toàn cho những quyết định Loại 2 không?

## Liên kết
- Skill dùng trước: [[80-20-growth]] (để chọn việc cần quyết định)
- Skill dùng kèm: [[critical-thinking]] (cho quyết định Loại 1)
- Xem tổng thể: [[skill_registry]]
