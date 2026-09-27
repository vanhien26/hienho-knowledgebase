with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    brd = f.read()

replacement = """### 4.3 Cơ Chế Điều Hướng & Suggest Trọng Tâm (3 Hero Products Driven-Traffic Engine)

Toàn bộ các công cụ (Tools/Calculators) và bài viết nội dung trên Kênh Web không hoạt động độc lập mà đóng vai trò là cỗ máy hút lưu lượng tự nhiên (Traffic Magnet) để tự động gợi ý và chuyển đổi người dùng vào **3 Sản Phẩm Trọng Điểm Của FinHub**:

1. **Sức Khỏe Tín Dụng (CIC & Điểm Tín Dụng MoMo):**
   - *Điểm chạm kích hoạt:* Các công cụ Tính Lương, Mã Số Thuế, Tra Cứu CIC, Phân Bổ Ngân Sách.
   - *Cơ chế điều hướng:* Sau khi người dùng nhập dữ liệu thu nhập / nợ ➔ Widget tự động đo lường chỉ số an toàn đòn bẩy và đề xuất *"Kiểm Tra Báo Cáo Tín Dụng CIC Miễn Phí 100% Trên MoMo"* để thẩm định hồ sơ.

2. **Tích Lũy An Toàn (Gửi Tiết Kiệm Online TKO - Bản Việt & VPBank):**
   - *Điểm chạm kích hoạt:* Bảng So Sánh Lãi Suất 30 Bank, Công Cụ Tính Lương Gross-Net, Quản Lý Dòng Tiền, Giá Vàng, Tỷ Giá Ngoại Tệ.
   - *Cơ chế điều hướng:* Khi công cụ tính toán ra Dòng Tiền Tự Do / Lương Net / Tiền Thặng Dư ➔ Widget tự động tính số tiền lãi nhận được nếu gửi tiết kiệm và hiển thị CTA *"Gửi Tiết Kiệm Online Bản Việt & VPBank (Cộng thêm +0.2% Lãi Suất)"*.

3. **Tăng Trưởng Tài Sản (Chương Trình Thực Tập Sinh Đầu Tư - Chứng Khoán & Quỹ Mở SIP):**
   - *Điểm chạm kích hoạt:* Cổng Chứng Khoán, Tích Sản FIRE, Quy Đổi Vàng, Phân Bổ Lương 50/30/20.
   - *Cơ chế điều hướng:* Tab so sánh trực quan giữa *"Gửi Tiết Kiệm (5%/năm) vs Thực Tập Sinh Đầu Tư Quỹ Mở (10-15%/năm)"* ➔ Kích hoạt CTA *"Đăng Ký Thực Tập Sinh Đầu Tư Chỉ Từ 10.000đ/Ngày"* để kéo tệp người dùng trẻ tích sản dài hạn."""

if '### 4.3 Cơ Chế Điều Hướng Web-to-App (Cross-Sell Engine)' in brd:
    brd = brd.replace('### 4.3 Cơ Chế Điều Hướng Web-to-App (Cross-Sell Engine)', replacement)
    with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
        f.write(brd)
    print("Successfully updated BRD with 3 Hero Products Driven-Traffic Framework!")
else:
    print("Section 4.3 already updated or has different title.")
