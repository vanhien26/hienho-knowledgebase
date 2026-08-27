# KHUNG TƯ DUY PHÂN TÍCH VÀ ĐỊNH KHUNG BÀI TOÁN SẢN PHẨM (PROBLEM FRAMING CANVAS)

Khung tư duy phân tích bài toán (MITRE Problem Framing Canvas) giúp đội ngũ sản phẩm thấu hiểu toàn diện không gian bài toán (Problem Space) trước khi vội vã đưa ra giải pháp, tránh bẫy giải quyết sai vấn đề, thiên vị chủ quan và định kiến giải pháp ban đầu.

---

## 1. MỤC TIÊU VÀ NGUYÊN TẮC CỐT LÕI

- **Triết lý:** Dành 80% thời gian để hiểu đúng vấn đề và 20% thời gian cho giải pháp.
- **Tránh sai lầm:**
  - Nhầm lẫn triệu chứng (symptoms) với nguyên nhân gốc rễ (root cause).
  - Vội vã đưa ra giải pháp khi chưa hiểu bối cảnh người dùng.
  - Bỏ qua các đối tượng liên quan (stakeholders) bị ảnh hưởng gián tiếp.

---

## 2. QUY TRÌNH 3 GIAI ĐoẠN ĐỊNH KHUNG BÀI TOÁN

```
┌─────────────────────────────────────────────────────────────────┐
│ GIAI ĐOẠN 1: NHÌN VÀO TRONG (LOOK INWARD)                       │
│ - Triệu chứng vấn đề là gì?                                     │
│ - Tại sao chưa giải quyết được?                                 │
│ - Định kiến và giả định chủ quan của đội ngũ là gì?            │
├─────────────────────────────────────────────────────────────────┤
│ GIAI ĐOẠN 2: NHÌN RA NGOÀI (LOOK OUTWARD)                       │
│ - Ai thực sự gặp vấn đề này? Ai không gặp?                     │
│ - Ai hưởng lợi nếu vấn đề tồn tại?                              │
│ - Đối tượng nào bị bỏ quên?                                     │
├─────────────────────────────────────────────────────────────────┤
│ GIAI ĐOẠN 3: ĐỊNH KHUNG LẠI (REFRAME)                           │
│ - Tổng hợp insight thành Tuyên bố Bài toán (Problem Statement)   │
│ - Xây dựng câu hỏi gợi mở "Làm thế nào để..." (How Might We)    │
└─────────────────────────────────────────────────────────────────┘
```

### Giai đoạn 1: Nhìn vào trong (Look Inward)
- **Triệu chứng nhận biết:** Các hiện tượng bề nổi đang xảy ra (ví dụ: tỷ lệ người dùng rời bỏ trang đăng ký cao).
- **Phân tích lý do chưa xử lý:** Tại sao bài toán này trước đây chưa được giải quyết? (Do rào cản kỹ thuật, thiếu nguồn lực, hay chưa phải ưu tiên cao?).
- **Rà soát định kiến nội bộ:** Đội ngũ đang giả định điều gì? Giải pháp nào đang bị áp đặt trước khi nghiên cứu?

### Giai đoạn 2: Nhìn ra ngoài (Look Outward)
- **Xác định nhóm bị ảnh hưởng:** Ai là người chịu ảnh hưởng trực tiếp nặng nề nhất? Nhóm người dùng nào hoàn toàn không bị ảnh hưởng?
- **Phân tích động cơ hệ thống:** Sự tồn tại của vấn đề này có mang lại lợi ích cho ai không? (Ví dụ: quy trình thủ công phức tạp giúp một bộ phận duy trì quyền kiểm soát).
- **Nhận diện đối tượng bị bỏ sót:** Nhóm người dùng yếu thế hoặc nhóm người dùng rìa (Edge users) đang trải nghiệm vấn đề như thế nào?

### Giai đoạn 3: Định khung lại (Reframe)
- **Tuyên bố bài toán chuẩn hóa (Problem Statement):**
  - Cấu trúc: `[Nhóm người dùng] đang gặp khó khăn trong việc [Mục tiêu] bởi vì [Nguyên nhân cốt lõi], dẫn đến [Tác động tiêu cực/Chi phí].`
- **Câu hỏi định hướng sáng tạo (How Might We - HMW):**
  - Cấu trúc: `Làm thế nào để chúng ta giúp [Nhóm người dùng] đạt được [Mục tiêu] mà không gây ra [Hạn chế/Chi phí hiện tại]?`

---

## 3. BẢNG KIỂM TRA ĐỘ CHUẨN XÁC CỦA BÀI TOÁN (CHECKLIST)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Yếu tố kiểm tra</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Câu hỏi xác nhận</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trạng thái</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nguyên nhân gốc rễ</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đã tách biệt triệu chứng bề nổi khỏi bản chất bài toán chưa?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đạt / Chưa</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không bị gán giải pháp</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tuyên bố bài toán có chứa sẵn tên tính năng/công nghệ nào không?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đạt / Chưa</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tính đo lường</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Có số liệu hoặc bằng chứng thực tế bảo chứng cho bài toán không?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đạt / Chưa</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Giá trị người dùng</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nếu giải quyết xong, người dùng nhận được lợi ích cụ thể gì?</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Đạt / Chưa</td>
    </tr>
  </tbody>
</table>
