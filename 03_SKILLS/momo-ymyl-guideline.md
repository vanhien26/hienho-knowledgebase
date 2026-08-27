
---
title: ⚖️ MoMo YMYL Guideline
description: |
  Tài liệu kỹ thuật quy chuẩn YMYL (Your Money Your Life) cho hệ thống nội dung momo.vn.
  Bao gồm các tiêu chuẩn kỹ thuật về chuẩn E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) theo tiêu chuẩn Google Search Quality.
tags:
  - ymyl
  - eeat
  - compliance
  - content
  - momo
version: 1.0.0
last_reviewed: 2026-05-15
next_review: 2026-08-15
---

# MoMo YMYL Content Guideline (E-E-A-T)

Tài liệu này là quy chuẩn kỹ thuật YMYL bắt buộc áp dụng cho hệ thống nội dung trên momo.vn. Các tiêu chuẩn kỹ thuật bắt buộc áp dụng bao gồm:

---

## 1. PHÂN LOẠI YMYL THEO MỨC ĐỘ

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Loại nội dung</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Use Case</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Yêu cầu tuân thủ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tài chính - Tín dụng</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay vốn, Tín dụng, CIC, Bảo hiểm nhân thọ, Đầu tư</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Disclaimer pháp lý + Nguồn chính thống + Author (khi có)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Bảo hiểm</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo hiểm xe máy/ô tô, BHYT, BHXH, Bảo hiểm sức khỏe</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Disclaimer pháp lý + Nguồn chính thống + Author (khi có)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Đầu tư & Tiết kiệm</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Chứng khoán, Chứng chỉ quỹ, Gửi tiết kiệm, QLCT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Disclaimer rút gọn + Nguồn chính thống</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Dịch vụ công & Thanh toán</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phạt nguội, BHXH tra cứu, Hóa đơn điện nước, Thanh toán</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Disclaimer rút gọn + Nguồn từ cơ quan nhà nước</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Giải trí & Lifestyle</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cinema, OTA, Du lịch, Ăn uống</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không cần disclaimer</td>
    </tr>
  </tbody>
</table>

**Cách hiển thị trong bài viết (cuối bài hoặc cuối disclaimer):**
```
Loại nội dung: [tên loại từ bảng trên]
Yêu cầu tuân thủ: [yêu cầu từ bảng trên]
```

---

## 2. E-E-A-T FRAMEWORK

### 2.1 Experience (Kinh nghiệm thực tế)
Content phải thể hiện được kinh nghiệm thực tế - không phải lý thuyết chung chung.

**Cách thể hiện:**
- Dùng data thực từ MoMo platform (số lượng user, tỷ lệ duyệt, thời gian xử lý thực tế)
- Screenshots quy trình thực trên App MoMo - không dùng mock-up hay stock image
- Ví dụ cụ thể từ sản phẩm MoMo, không ví dụ giả định

**Ví dụ đúng:**
> "Quy trình vay tại MoMo gồm 3 bước, thời gian giải ngân trung bình 15 phút sau khi được duyệt. [Kèm screenshot thực của app]"

**Ví dụ sai:**
> "Các ứng dụng vay tiền hiện nay thường có quy trình nhanh chóng và tiện lợi..."

### 2.2 Expertise (Chuyên môn)
Content phải thể hiện hiểu biết chuyên sâu về lĩnh vực tài chính.

**Yêu cầu:**
- Giải thích chính xác các khái niệm tài chính (lãi suất, APR, tín chấp, thế chấp...)
- Không đơn giản hóa sai sự thật để viết cho dễ hiểu
- Đề cập đúng quy định pháp luật hiện hành khi liên quan
- Nếu có thay đổi chính sách - cập nhật ngay, ghi rõ ngày cập nhật

**Thuật ngữ cần định nghĩa chính xác (không được viết sai):**

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thuật ngữ</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Định nghĩa chuẩn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Lãi suất vay</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tỷ lệ % tính trên số tiền vay, theo tháng hoặc năm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tín chấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay không cần tài sản đảm bảo, dựa trên uy tín tín dụng</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Thế chấp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Vay có tài sản đảm bảo (nhà, xe...)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điểm CIC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Điểm tín dụng từ 300-850, do CIC (Trung tâm Thông tin Tín dụng NHNN) cấp</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BHYT</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo hiểm y tế - chi trả chi phí khám chữa bệnh</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">BHXH</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo hiểm xã hội - bảo vệ người lao động khi ốm đau, thai sản, hưu trí</td>
    </tr>
  </tbody>
</table>

### 2.3 Authoritativeness (Thẩm quyền)
MoMo là tổ chức tài chính được cấp phép - content phải thể hiện điều này.

**Author Policy (áp dụng khi có):**
- Tên tác giả: thành viên Legal Team hoặc chuyên gia tài chính được chỉ định (đang xin ý kiến lãnh đạo)
- Khi có author: ghi rõ tên, chức danh, số năm kinh nghiệm
- Khi chưa có author profile: bắt buộc có disclaimer thay thế (xem mục 3)

**Brand Authority Signals:**
- Luôn đề cập MoMo là ví điện tử được cấp phép bởi NHNN
- Khi có số liệu so sánh thị trường - cite nguồn chính thống (NHNN, VBSP, báo cáo ngành)
- Không tự nhận là "tốt nhất", "duy nhất", "số 1" nếu không có bằng chứng

### 2.4 Trustworthiness (Độ tin cậy)
Đây là yếu tố quan trọng nhất trong E-E-A-T theo Google.

**Yêu cầu bắt buộc:**
- Thông tin chính xác 100% - không đoán, không phỏng đoán
- Số liệu có nguồn rõ ràng (xem mục 4)
- Transparent về limitations của sản phẩm MoMo
- Có disclaimer tài chính (xem mục 3)
- Ghi rõ ngày publish và ngày cập nhật cuối

---

## 3. DISCLAIMER TEMPLATE

### 3.1 Disclaimer tài chính (Loại: Tài chính - Tín dụng / Đầu tư & Tiết kiệm)
Đặt cuối bài, font nhỏ hơn body text:

```
Thông tin trong bài viết này chỉ mang tính chất tham khảo và giáo dục tài chính,
không phải lời khuyên tài chính cá nhân. Lãi suất, điều kiện vay và các chính sách
sản phẩm có thể thay đổi. Vui lòng kiểm tra thông tin cập nhật nhất tại ứng dụng
MoMo hoặc liên hệ tổng đài hỗ trợ trước khi đưa ra quyết định tài chính.
Cập nhật lần cuối: [Ngày/Tháng/Năm].
```

### 3.2 Disclaimer bảo hiểm (Loại: Bảo hiểm - dùng kèm 3.1)
```
Thông tin về bảo hiểm trong bài viết chỉ mang tính chất tổng quan. Quyền lợi,
điều kiện và mức phí bảo hiểm thực tế phụ thuộc vào từng gói sản phẩm và hợp đồng
cụ thể. Vui lòng đọc kỹ điều khoản hợp đồng bảo hiểm trước khi ký kết.
```

### 3.3 Disclaimer pháp lý (Loại: Dịch vụ công & Thanh toán / khi đề cập quy định pháp luật)
```
Thông tin pháp lý trong bài viết dựa trên quy định hiện hành tại thời điểm đăng.
Pháp luật có thể thay đổi. Vui lòng tham khảo thông tin chính thức từ cơ quan
nhà nước có thẩm quyền để có thông tin chính xác nhất.
Cập nhật lần cuối: [Ngày/Tháng/Năm].
```

---

## 4. NGUỒN TRÍCH DẪN CHUẨN

### 4.1 Nguồn được chấp nhận (ưu tiên theo thứ tự)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ưu tiên</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nguồn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Ví dụ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Văn bản pháp luật chính thức</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nghị định, Thông tư NHNN, Luật Kinh doanh Bảo hiểm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cơ quan nhà nước</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">NHNN, Bộ Tài chính, VBSP, Cục Quản lý Bảo hiểm</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Data nội bộ MoMo (được phép dùng)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">"Theo dữ liệu MoMo Q1/2026..."</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tổ chức tài chính uy tín</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">World Bank, IMF, báo cáo ngân hàng lớn</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">5</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Báo chí tài chính chính thống</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">CafeF, VnEconomy, Nhịp cầu Đầu tư</td>
    </tr>
  </tbody>
</table>

### 4.2 Nguồn không được dùng
- Blog cá nhân không rõ tác giả
- Forum, mạng xã hội (Facebook, Zalo group...)
- Số liệu không có năm/quý cụ thể
- Nguồn không truy cập được / link chết

### 4.3 Format trích dẫn chuẩn
```
Theo [Tên nguồn] ([Tháng/Năm nếu có]), [nội dung trích dẫn].
```
Ví dụ: `Theo NHNN (Q3/2024), tổng dư nợ tín dụng tiêu dùng đạt 2.8 triệu tỷ đồng.`

---

## 5. ACCURACY CHECKLIST

Chạy checklist này cho mọi content YMYL trước khi publish:

**Tính chính xác**
- [ ] Tất cả số liệu có nguồn rõ ràng, nguồn thuộc danh sách được chấp nhận
- [ ] Lãi suất/phí/điều kiện sản phẩm khớp với thông tin hiện tại trên App MoMo
- [ ] Không có tuyên bố tuyệt đối ("tốt nhất", "duy nhất") nếu không có bằng chứng
- [ ] Các thuật ngữ tài chính được định nghĩa đúng

**E-E-A-T**
- [ ] Có ít nhất 1 element thể hiện Experience thực tế (screenshot, data MoMo)
- [ ] Expertise: không có khái niệm tài chính nào bị giải thích sai
- [ ] Authority: đề cập MoMo là ví điện tử được NHNN cấp phép (Tier 1 & 2)
- [ ] Trust: có disclaimer phù hợp với Tier của content

**Disclaimer**
- [ ] Tier 1 & 2: có disclaimer tài chính chuẩn
- [ ] Content về bảo hiểm: có thêm disclaimer bảo hiểm
- [ ] Content đề cập pháp luật: có thêm disclaimer pháp lý
- [ ] Ghi rõ ngày cập nhật cuối

**Ngày tháng**
- [ ] Ghi ngày publish
- [ ] Ghi ngày cập nhật cuối (nếu khác ngày publish)
- [ ] Tất cả số liệu có năm/quý cụ thể

---

## 6. CÁC TRƯỜNG HỢP ĐẶC BIỆT

### 6.1 Khi thông tin thay đổi (lãi suất, chính sách)
- Cập nhật ngay khi có thông tin mới
- Thêm banner đầu bài: `[Cập nhật: Tháng X/202X] Nội dung bài viết đã được cập nhật theo chính sách mới nhất.`
- Không xóa thông tin cũ nếu vẫn còn giá trị lịch sử - ghi chú rõ

### 6.2 Khi không chắc chắn về thông tin
- Không đăng nếu chưa verify
- Nếu bắt buộc đăng: ghi rõ `[Cần xác minh thêm]` và contact Legal/Product để confirm
- Không dùng từ như "có thể", "có lẽ", "nghe nói" cho thông tin tài chính quan trọng

### 6.3 Khi đề cập đối thủ cạnh tranh
- Chỉ so sánh trên data công khai, có nguồn rõ ràng
- Không đưa ra nhận xét tiêu cực về đối thủ nếu không có bằng chứng
- Comparison table phải honest - bao gồm cả điểm MoMo chưa bằng đối
