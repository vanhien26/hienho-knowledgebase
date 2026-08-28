import re

with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace misleading phrases
content = content.replace("mạng lưới 24 trang vệ tinh chuyên sâu", "hệ thống 11 Trang Dự Án & Bộ Tiện Ích Trọng Tâm (phủ 24 nhóm nhu cầu tìm kiếm)")
content = content.replace("24 trang dịch vụ chuyên sâu", "11 Trang Dự Án trọng tâm (phủ 24 nhóm nhu cầu thị trường)")
content = content.replace("Tầng 2 - 24 Trang Chuyên Sâu & Programmatic Hub (`/tai-chinh/[dich-vu]`)", "Tầng 2 - 11 Trang Dự Án Trọng Tâm & Programmatic Hub 34 Ngân Hàng")
content = content.replace("24 Spoke Pages", "11 Core Product Pages & Programmatic Hub")

with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully corrected terminology in 05_HUBS/financial-hub-brd.md!")
