import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update total count
content = content.replace('28 URLs', '26 URLs')

# Use regex to remove the "8. Đối Tác Dịch Vụ (Partner Ecosystem)" section entirely
# It looks like:
# #### 8. Đối Tác Dịch Vụ (Partner Ecosystem)
# 
# | STT | URL | Mô Tả Chức Năng |
# | :---: | :--- | :--- |
# | 27 | `https://www.momo.vn/tien-ich-giao-thong/doi-tac` | Danh sách đối tác thuộc hệ sinh thái Giao thông MoMo. |
# | 28 | `https://www.momo.vn/tien-ich-giao-thong/doi-tac/[slug]` | Trang chi tiết thông tin thương hiệu đối tác liên kết. |
# 
# ---

# We can find the start of section 8 and cut it out up to the --- before section 9.
pattern = r'#### 8\. Đối Tác Dịch Vụ \(Partner Ecosystem\).*?(?=---)'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# Add Change Log
changelog_entry = """| **v8.3** | 2026-08-28 | Web Product Lead | **Loại Bỏ Nhóm Trang Đối Tác:** Hủy bỏ nhóm "Đối Tác Dịch Vụ" (`/doi-tac`, `/doi-tac/[slug]`) để tinh gọn cấu trúc. Sitemap nội khu vực hiện còn **26 URLs**. |
"""
content = content.replace('| **v8.2**', changelog_entry + '| **v8.2**')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed Partner pages successfully!")
