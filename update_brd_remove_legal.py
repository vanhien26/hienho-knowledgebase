import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_urls = [
    '/tien-ich-giao-thong/ho-so-xe`',
    '/tien-ich-giao-thong/diem-gplx`',
    '/tien-ich-giao-thong/sang-ten-xe`',
    '/tien-ich-giao-thong/bien-so-xe`',
    '/tien-ich-giao-thong/bien-so-dep`'
]

stt_counter = 1
in_sitemap_section = False

for line in lines:
    if '3.4 Sitemap Architecture' in line:
        line = line.replace('26 URLs', '21 URLs')
        in_sitemap_section = True
    
    if 'bao gồm **26 URLs**' in line:
        line = line.replace('26 URLs', '21 URLs')
        
    if in_sitemap_section and line.startswith('| '):
        if 'STT' in line or ':---' in line or 'Tên Trang Độc Lập' in line:
            new_lines.append(line)
            continue
            
        should_skip = any(url in line for url in skip_urls)
        if should_skip:
            continue
            
        parts = line.split('|')
        if len(parts) > 2 and parts[1].strip().isdigit():
            parts[1] = f' {stt_counter} '
            line = '|'.join(parts)
            stt_counter += 1
            
    if '4.4 Change Log' in line:
        in_sitemap_section = False
        
    new_lines.append(line)

final_content = ''.join(new_lines)
changelog_entry = """| **v8.3** | 2026-08-28 | Web Product Lead | **Tiếp Tục Tinh Gọn Kênh Pháp Lý & Biển Số:** Lược bỏ 5 trang tiện ích ngách (`/ho-so-xe`, `/diem-gplx`, `/sang-ten-xe`, `/bien-so-xe`, `/bien-so-dep`) để dồn trọng tâm vào luồng chuyển đổi lõi. Sitemap tổng nội khu vực giảm xuống còn **21 URLs**. |
"""
final_content = final_content.replace('| **v8.2**', changelog_entry + '| **v8.2**')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("BRD updated successfully down to 21 URLs!")
