import re

with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any mention of forcing sub-paths under /tai-chinh
content = content.replace("`/tai-chinh/[dich-vu]`", "các Trang Sản Phẩm Độc Lập")
content = content.replace("/tai-chinh/tinh-luong", "/tinh-luong")
content = content.replace("/tai-chinh/thue-tncn", "/thue-tncn")
content = content.replace("/tai-chinh/tra-cuu-cic", "/tra-cuu-cic")
content = content.replace("/tai-chinh/xoa-no-xau", "/xoa-no-xau")
content = content.replace("/tai-chinh/tiet-kiem-online", "/tiet-kiem-online")
content = content.replace("/tai-chinh/tra-gop", "/tra-gop")
content = content.replace("/tai-chinh/gia-vang", "/gia-vang")
content = content.replace("/tai-chinh/ty-gia", "/ty-gia")
content = content.replace("/tai-chinh/lai-suat-ngan-hang", "/lai-suat-ngan-hang")
content = content.replace("/tai-chinh/vay-tin-chap", "/vay-tin-chap")
content = content.replace("/tai-chinh/the-tin-dung", "/the-tin-dung")
content = content.replace("/tai-chinh/dau-tu/chung-khoan", "/chung-khoan")
content = content.replace("/tai-chinh/the-visa", "/the-visa")
content = content.replace("/tai-chinh/the-ghi-no", "/the-ghi-no")
content = content.replace("/tai-chinh/napas", "/napas")
content = content.replace("/tai-chinh/tien-so", "/tien-so")
content = content.replace("/tai-chinh/the-mastercard", "/the-mastercard")
content = content.replace("/tai-chinh/vay-the-chap", "/vay-the-chap")
content = content.replace("/tai-chinh/ngoai-te", "/ngoai-te")
content = content.replace("/tai-chinh/crypto", "/crypto")
content = content.replace("/tai-chinh/dau-tu/co-phieu", "/co-phieu")
content = content.replace("/tai-chinh/dau-tu/trai-phieu", "/trai-phieu")
content = content.replace("/tai-chinh/dau-tu/chung-chi-quy", "/chung-chi-quy")
content = content.replace("/tai-chinh/ngan-hang/[slug]", "/ngan-hang/[slug]")

# Add explicit Section 5.1 Architecture clarification
old_arch = "### 5.1 Kiến Trúc Sản Phẩm 2 Tầng (Hub-and-Spoke Architecture)"
new_arch = """### 5.1 Nguyên Tắc Bảo Toàn Thẩm Quyền SEO & Cơ Chế Hợp Nhất (Centralization Mechanism)

Để **bảo vệ 100% thẩm quyền SEO, thứ hạng từ khóa và hồ sơ backlink hiện có**, hệ thống **KHÔNG thay đổi cấu trúc URL hay chuyển các trang sản phẩm độc lập về thư mục con `/tai-chinh/`**. 

Toàn bộ quá trình Hợp Nhất Trải Nghiệm (Centralization) được thực thi thông qua **4 Cơ Chế Điều Hướng & Bán Chéo (Cross-sell & Navigation Engines)**:

1. **Trang Cổng Master Gateway (`momo.vn/tai-chinh`):** Đóng vai trò là "Mặt tiền tổng hợp", hiển thị bảng dữ liệu thị trường trực quan (Giá vàng, Tỷ giá, Lãi suất) và phân luồng người dùng đến đúng trang sản phẩm theo từng JTBD.
2. **Thanh Điều Hướng Tài Chính Thống Nhất (Global Financial Navigation Bar):** Xuất hiện đồng bộ trên tất cả các trang sản phẩm độc lập (`/tiet-kiem-online`, `/vay-nhanh`, `/vi-tra-sau`...), cho phép người dùng chuyển đổi tức thì giữa các dịch vụ tài chính MoMo mà không bị đứt gãy trải nghiệm.
3. **Cơ Chế Bán Chéo Theo Ngữ Cảnh (Contextual Cross-Sell Engine):** Nhúng các khối gợi ý giải pháp tài chính liên quan ngay sau khi người dùng tương tác công cụ (Ví dụ: Tính lương tại `/tinh-luong` ➔ Gợi ý mở hạn mức tại `/vi-tra-sau` hoặc tích lũy tại `/tiet-kiem-online`).
4. **Hệ Thống Liên Kết Nội Bộ Chuẩn SEO (Topical Internal Linking):** Thiết lập mạng lưới liên kết ngữ nghĩa giữa Master Hub và các trang độc lập, giúp Google nhận diện toàn bộ website là một thực thể tài chính vững mạnh mà không cần thay đổi đường dẫn URL gốc."""

if old_arch in content:
    content = content.replace(old_arch, new_arch)

with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated 05_HUBS/financial-hub-brd.md with SEO URL Preservation & Cross-sell Centralization strategy!")
