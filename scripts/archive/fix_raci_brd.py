import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace outdated RACI rows
content = content.replace(
    '| 4.3 Tra Cứu Đăng Kiểm, 12 Điểm GPLX & Phong Thủy Biển Số |',
    '| 4.3 Xây Dựng Trang Tra Cứu Đăng Kiểm (`/dang-kiem`) |'
)

# Add Phat Nguoi to Group IV or II
# Let's put it in Group II
content = content.replace(
    '| 2.2 Phát triển Widget 3-in-1 Trước Khi Lăn Bánh | **A / R (Chủ trì)** | C (Góp ý phễu) | C (Cung cấp API) |',
    '| 2.2 Phát triển Widget 3-in-1 Trước Khi Lăn Bánh | **A / R (Chủ trì)** | C (Góp ý phễu) | C (Cung cấp API) |\n| 2.3 Cổng Phạt Nguội & Tối ưu Location Pages (`/phat-nguoi`) | **A / R (Chủ trì Web)** | C (Cross-sell BH) | C (Luật giao thông) |'
)

# Fix numbering
content = content.replace('| 2.3 Cấu hình Điểm Chạm Chuyển Đổi', '| 2.4 Cấu hình Điểm Chạm Chuyển Đổi')
content = content.replace('| 2.4 Xây dựng Bảng Giá Xăng', '| 2.5 Xây dựng Bảng Giá Xăng')

# Clean up duplicated change log entries if any (just in case, though the user didn't ask)
# We can use regex to remove repeated Change log headers and ---
content = re.sub(r'(---\n\n### 4\.4 Change Log\n\n\| Phiên Bản.*?\n\| :---: \| :---: \| :---: \| :---\n)(.*?\n)(---\n\n### 4\.4 Change Log\n\n\| Phiên Bản.*?\n\| :---: \| :---: \| :---: \| :---\n)', r'\1\2', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("RACI matrix updated and polished.")
