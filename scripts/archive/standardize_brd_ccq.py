with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    brd = f.read()

# Replace Quỹ mở SIP where it refers to product name with Chứng Chỉ Quỹ (kèm phương thức tích sản định kỳ SIP)
brd = brd.replace('Chứng Khoán & Quỹ Mở SIP', 'Chứng Khoán & Chứng Chỉ Quỹ (SIP)')
brd = brd.replace('Quỹ Mở SIP', 'Chứng Chỉ Quỹ (SIP)')
brd = brd.replace('Quỹ mở SIP', 'Chứng Chỉ Quỹ (SIP)')

with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
    f.write(brd)
print("Successfully standardized 'Chứng Chỉ Quỹ' in financial-hub-brd.md!")
