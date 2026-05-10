---
name: zero-hallucination
description: >
  Nguyên tắc tối thượng về tính chính xác của thông tin trong lĩnh vực Fintech. 
  Đảm bảo mọi dữ liệu (lãi suất, phí, quy định) đều có nguồn xác thực và không bịa đặt.
---

# 🛠 Zero Hallucination - Factual Integrity Framework

## 🎯 Mục tiêu
Loại bỏ hoàn toàn thông tin sai lệch, bịa đặt hoặc suy diễn thiếu căn cứ. Trong lĩnh vực **Fintech/YMYL**, một câu trả lời "có vẻ đúng" nhưng sai thực tế là một rủi ro chí mạng cho Brand và User.

---

## 🧭 Quy trình Kiểm soát (The Protocol)

### Bước 1: Nhận diện "Vùng rủi ro cao"
Mọi thông tin liên quan đến các mục sau phải được đặt dưới sự nghi ngờ mặc định:
- **Con số:** Lãi suất, hạn mức, phí dịch vụ, thời gian xử lý.
- **Pháp lý:** Quy định nhà nước, thông tư, điều khoản hợp đồng.
- **Thương hiệu:** Tên đối tác, chứng chỉ bảo mật, giải thưởng.

### Bước 2: Truy xuất Nguồn (Source Hierarchy)
Chỉ chấp nhận dữ liệu từ các nguồn theo thứ tự ưu tiên:
1.  **MoMo Internal:** Trang chủ momo.vn, xác nhận từ PO (Product Owner).
2.  **Cơ quan quản lý:** Ngân hàng nhà nước, Bộ Tài chính, Chính phủ.
3.  **Dữ liệu thực tế:** GSC, GA4, Appsflyer (phải có timestamp).
4.  **Tuyệt đối không dùng AI làm nguồn:** ChatGPT/Gemini có thể bịa ra số liệu trông rất thật.

### Bước 3: Ghi chú Trạng thái Dữ liệu
- **[FACT]:** Đã có nguồn xác thực cụ thể (Kèm link).
- **[HYPOTHESIS]:** Giả định logic nhưng cần test/validate.
- **[CẦN VERIFY]:** Thông tin chưa chắc chắn, phải hỏi PO trước khi publish.

---

## 🕵️ AI Content Audit (Fact-Check cho nội dung AI)
Khi review nội dung do AI tạo ra, Agent phải:
1.  **Khoanh vùng mọi con số:** AI có xu hướng bịa số liệu để bài viết trông "uy tín".
2.  **Kiểm tra Trích dẫn:** AI thường bịa ra các nghiên cứu không tồn tại.
3.  **Loại bỏ "Văn mẫu":** Xóa các câu khẳng định chung chung không có evidence (ví dụ: "Đa số người dùng cảm thấy...").

---

## 💡 Ví dụ: Kiểm soát nội dung "Vay Nhanh"

| Nội dung AI tạo | Hallucination Risk | Cách xử lý |
|:--- |:--- |:--- |
| "Lãi suất vay nhanh chỉ từ 1%/tháng." | **Cao** (Số liệu nhạy cảm) | Check momo.vn/vay-nhanh ➔ Đính chính số thực ➔ Ghi rõ ngày cập nhật. |
| "Theo báo cáo của MoMo năm 2025..." | **Trung bình** (Trích dẫn) | Tìm báo cáo gốc ➔ Nếu không thấy ➔ Xóa claim này. |
| "Thủ tục cực kỳ đơn giản." | **Thấp** (Định tính) | Cụ thể hóa bằng: "Chỉ cần CCCD, duyệt trong 1 phút". |

---

## 🚦 Gate Check
- [ ] Mọi con số trong bài đã có link trỏ về nguồn SOT (Source of Truth) chưa?
- [ ] Có câu nào mang tính "suy diễn" mà không có data chứng minh không?
- [ ] Nếu thông tin này sai, rủi ro lớn nhất cho MoMo là gì?

## Liên kết
- Skill dùng trước: [[First-Principles]], [[critical-thinking]]
- Skill dùng kèm: [[Seo-Geo-audit]]
- Xem tổng thể: [[SKILL_REGISTRY]]