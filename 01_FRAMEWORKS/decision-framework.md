---
name: decision-framework
description: >
  Khung ra quyết định dựa trên tính khả hồi (reversibility) và tác động (impact). 
  Giúp tăng tốc độ thực thi và giảm thiểu rủi ro cho các quyết định quan trọng.
---

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

| Quyết định | Loại | Hành động (Action) |
|:--- |:--- |:--- |
| Viết 10 bài blog cho mảng eSIM. | Loại 2 | Thực hiện ngay, monitor traffic sau 2 tuần. |
| Mua một Domain mới để làm satellite site. | Loại 1 | Cần phân tích ROI, rủi ro SEO và xin ý kiến Lead. |
| Chỉnh sửa giao diện Tool Phạt Nguội. | Loại 2 | Test trên 10% user, nếu ổn thì roll-out 100%. |

---

## 🚦 Gate Check
- [ ] Quyết định này là "Cửa 1 chiều" hay "Cửa 2 chiều"?
- [ ] Nếu quyết định này sai, thiệt hại lớn nhất là gì? Có sửa được không?
- [ ] Bạn có đang quá cầu toàn cho những quyết định Loại 2 không?

## Liên kết
- Skill dùng trước: [[80-20-growth]] (để chọn việc cần quyết định)
- Skill dùng kèm: [[critical-thinking]] (cho quyết định Loại 1)
- Xem tổng thể: [[SKILL_REGISTRY]]
