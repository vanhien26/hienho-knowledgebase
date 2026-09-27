with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    brd = f.read()

target = "* *Dịch vụ:* Vay Tín Chấp (Vay Nhanh), Trả Góp (Ví Trả Sau), Vay Thế Chấp (Mua Nhà), Tra Cứu CIC, Điểm Tín Dụng, Xóa Nợ Xấu."
replacement = "* *Dịch vụ:* Chuyên trang Điểm Tín Dụng & Tra Cứu CIC (`momo.vn/diem-tin-dung`), Vay Tín Chấp (Vay Nhanh), Trả Góp (Ví Trả Sau), Vay Thế Chấp (Mua Nhà), Xóa Nợ Xấu."

if target in brd:
    brd = brd.replace(target, replacement)
    with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
        f.write(brd)
    print("Successfully updated /diem-tin-dung in financial-hub-brd.md!")
else:
    print("Target string not found in BRD.")
