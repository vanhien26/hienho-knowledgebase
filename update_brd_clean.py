import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_urls = [
    '/tien-ich-giao-thong/oto`',
    '/tien-ich-giao-thong/xe-may`',
    '/tien-ich-giao-thong/xe-dien`',
    '/tien-ich-giao-thong/xe-tai`',
    '/tien-ich-giao-thong/doi-tac`',
    '/tien-ich-giao-thong/doi-tac/[slug]`'
]

stt_counter = 1
in_sitemap_section = False
skip_next_table_header = False

for line in lines:
    if '3.4 Sitemap Architecture' in line:
        line = line.replace('32 URLs', '26 URLs')
        in_sitemap_section = True
    
    if 'bao gồm **32 URLs**' in line:
        line = line.replace('32 URLs', '26 URLs')
        
    # Remove the section 8 heading
    if '#### 8. Đối Tác Dịch Vụ' in line:
        skip_next_table_header = True
        continue
        
    if skip_next_table_header and ('STT | URL' in line or ':---' in line):
        if ':---' in line:
            skip_next_table_header = False # last line of table header to skip
        continue
    
    if '#### 9. Standalone' in line:
        line = line.replace('#### 9. Standalone', '#### 8. Standalone')
    
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
changelog_entry = """| **v8.2** | 2026-08-28 | Web Product Lead | **Tinh Gọn Ecosystem (Loại bỏ Danh Mục Xe & Đối Tác):** Hủy bỏ 4 trang danh mục xe (`/oto`, `/xe-may`, `/xe-dien`, `/xe-tai`) và 2 trang danh mục đối tác (`/doi-tac`, `/doi-tac/[slug]`) để tập trung hoàn toàn vào luồng tiện ích giao thông và công cụ. Cập nhật Sitemap tổng nội khu vực xuống còn **26 URLs**. |
"""
final_content = final_content.replace('| **v8.1**', changelog_entry + '| **v8.1**')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Clean BRD update complete!")
