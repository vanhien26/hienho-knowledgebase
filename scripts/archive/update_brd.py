import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_urls = [
    '/tien-ich-giao-thong/oto`',
    '/tien-ich-giao-thong/xe-may`',
    '/tien-ich-giao-thong/xe-dien`',
    '/tien-ich-giao-thong/xe-tai`'
]

stt_counter = 1
in_sitemap_section = False

for line in lines:
    if '3.4 Sitemap Architecture' in line:
        line = line.replace('32 URLs', '28 URLs')
        in_sitemap_section = True
    
    if 'bao gồm **32 URLs**' in line:
        line = line.replace('32 URLs', '28 URLs')
    
    if in_sitemap_section and line.startswith('| '):
        # Check if it's a header or divider
        if 'STT' in line or ':---' in line or 'Tên Trang Độc Lập' in line:
            new_lines.append(line)
            continue
            
        # Check if it's one of the rows to skip
        should_skip = any(url in line for url in skip_urls)
        if should_skip:
            continue
            
        # If it's a valid data row with a number in the first column, re-number it
        parts = line.split('|')
        if len(parts) > 2 and parts[1].strip().isdigit():
            parts[1] = f' {stt_counter} '
            line = '|'.join(parts)
            stt_counter += 1
            
    if '4.4 Change Log' in line:
        in_sitemap_section = False # Stop renumbering if we reach here (just in case)
        
    new_lines.append(line)

# Add change log entry
final_content = ''.join(new_lines)
changelog_entry = """| **v8.2** | 2026-08-28 | Web Product Lead | **Loại Bỏ Trang Danh Mục Xe:** Loại bỏ 4 chuyên trang danh mục xe (`/oto`, `/xe-may`, `/xe-dien`, `/xe-tai`) để tập trung vào luồng tiện ích giao thông lõi. Chuẩn hóa lại Sitemap còn **28 URLs** nội khu vực. |
"""
final_content = final_content.replace('| **v8.1**', changelog_entry + '| **v8.1**')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)
print("BRD updated successfully!")
