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

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nội dung AI tạo</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hallucination Risk</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cách xử lý</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Lãi suất vay nhanh chỉ từ 1%/tháng."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cao</strong> (Số liệu nhạy cảm)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Check momo.vn/vay-nhanh ➔ Đính chính số thực ➔ Ghi rõ ngày cập nhật.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Theo báo cáo của MoMo năm 2025..."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trung bình</strong> (Trích dẫn)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm báo cáo gốc ➔ Nếu không thấy ➔ Xóa claim này.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Thủ tục cực kỳ đơn giản."</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Thấp</strong> (Định tính)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cụ thể hóa bằng: "Chỉ cần CCCD, duyệt trong 1 phút".</td>
    </tr>
  </tbody>
</table>

---

## 🚦 Gate Check
- [ ] Mọi con số trong bài đã có link trỏ về nguồn SOT (Source of Truth) chưa?
- [ ] Có câu nào mang tính "suy diễn" mà không có data chứng minh không?
- [ ] Nếu thông tin này sai, rủi ro lớn nhất cho MoMo là gì?

## Liên kết
- Skill dùng trước: [[First-Principles]], [[critical-thinking]]
- Skill dùng kèm: [[Seo-Geo-audit]]
- Xem tổng thể: [[skill_registry]]
