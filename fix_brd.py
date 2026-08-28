import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's see if the heading is exactly there
idx1 = content.find('#### 8. Đối Tác Dịch Vụ')
idx2 = content.find('#### 9. Standalone Root Pages')

if idx1 != -1 and idx2 != -1:
    # also remove the '---' line just above section 9
    content_to_remove = content[idx1:idx2]
    content = content.replace(content_to_remove, '')
    # fix any double --- 
    content = content.replace('---\n\n\n#### 9', '---\n\n#### 9')
    content = content.replace('#### 9. Standalone', '#### 8. Standalone')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Not found", idx1, idx2)
