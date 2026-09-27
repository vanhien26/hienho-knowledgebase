with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    content = f.read()

target = "### 5.2 Cơ Chế Hợp Nhất Hệ Sinh Thái & Bảo Toàn Thẩm Quyền SEO"
insertion = """### 5.2 Cơ Chế Điều Hướng Trọng Tâm Đến 3 Sản Phẩm FinHub (Driven-Traffic Engine)

Toàn bộ các công cụ tính toán (Tools) và trang đích trên Kênh Web đóng vai trò là "Cỗ Máy Thu Hút Lưu Lượng" để phân luồng và đề xuất theo ngữ cảnh (Contextual Suggestion) trực tiếp vào **3 Sản Phẩm Trọng Điểm Cần Đẩy Của FinHub**:

1. **Sức Khỏe Tín Dụng (CIC & Điểm Tín Dụng MoMo):**
   - *Điểm chạm kích hoạt:* Công cụ Tính Lương, Mã Số Thuế, Tra Cứu CIC, Phân Bổ Ngân Sách, Quản Lý Dòng Tiền.
   - *Cơ chế điều hướng:* Sau khi người dùng tính toán thu nhập hoặc nợ ➔ Hệ thống tự động đo lường chỉ số an toàn đòn bẩy và hiển thị CTA *"Kiểm Tra Báo Cáo Tín Dụng CIC Miễn Phí 100% Trên MoMo"* để thẩm định hồ sơ trước khi vay.

2. **Tích Lũy An Toàn (Gửi Tiết Kiệm Online TKO - Bản Việt & VPBank):**
   - *Điểm chạm kích hoạt:* Bảng So Sánh Lãi Suất 30 Bank, Công Cụ Tính Lương Gross-Net, Quản Lý Dòng Tiền & Tiêu Dùng, Giá Vàng, Tỷ Giá Ngoại Tệ.
   - *Cơ chế điều hướng:* Khi công cụ tính toán ra Dòng Tiền Tự Do (Free Cash Flow), lương Net hoặc số tiền thặng dư ➔ Tự động tính tiền lãi sinh lời và đề xuất *"Gửi Tiết Kiệm Bản Việt / VPBank Trên MoMo (Nhận Thêm +0.2% Lãi Suất)"*.

3. **Tăng Trưởng Tài Sản (Chương Trình Thực Tập Sinh Đầu Tư - Chứng Khoán & Quỹ Mở SIP):**
   - *Điểm chạm kích hoạt:* Cổng Chứng Khoán, Tích Sản FIRE, Quy Đổi Vàng, Phân Bổ Lương 50/30/20.
   - *Cơ chế điều hướng:* Tab so sánh đối chiếu giữa *"Gửi Tiết Kiệm (5%/năm) vs Thực Tập Sinh Đầu Tư Quỹ Mở (10-15%/năm)"* ➔ Kích hoạt CTA *"Tham Gia Thực Tập Sinh Đầu Tư Chỉ Từ 10.000đ/Ngày"* giúp người dùng trẻ (F0) tích sản dài hạn.

"""

if target in content and "3 Sản Phẩm Trọng Điểm Cần Đẩy Của FinHub" not in content:
    content = content.replace(target, insertion + target)
    with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added 3 Hero Products Driven-Traffic Engine into financial-hub-brd.md!")
else:
    print("Already added or target not found.")
