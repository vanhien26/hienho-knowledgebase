import re
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower().replace(" ", "-")

live_mapping = {
    "Bún thịt nướng Chị Tuyền": "https://www.momo.vn/merchant/bun-thit-nuong-chi-tuyen-44",
    "Cơm Tấm Ống Khói Điệu": "https://www.momo.vn/merchant/com-tam-ong-khoi-dieu-45",
    "Hủ tiếu Mỹ Tho Thanh Xuân": "https://www.momo.vn/merchant/hu-tieu-my-tho-thanh-xuan-69",
    "Bánh ướt Cây Me": "https://www.momo.vn/merchant/ban-uot-cay-me-can-tho-48", # I'll use the user provided one: banh-uot-cay-me-can-tho-48
    "Mì Xào Giòn A Tỷ": "https://www.momo.vn/merchant/a-ty-mi-xao-gion-bot-chien-64",
    "Quán Cơm Chú Lùn": "https://www.momo.vn/merchant/quan-com-chu-lun-47",
    "Hương Giang Bakery": "https://www.momo.vn/merchant/huong-giang-bakery-bac-ninh-63",
    "Hủ tiếu Nam Vang 69": "https://www.momo.vn/merchant/hu-tieu-nam-vang-69-50",
    "Chả giò Phượng": "https://www.momo.vn/merchant/cha-gio-phuong-dong-nai-56",
    "Hải sản Ngô Thơ": "https://www.momo.vn/merchant/hai-san-ngo-tho-55",
    "Chả rươi Hằng Béo": "https://www.momo.vn/merchant/cha-ruoi-hang-beo-51",
    "Bánh mì Hữu Liêm": "https://www.momo.vn/merchant/banh-mi-huu-liem-can-tho-49",
    "Tiệm Mỳ Chú Cao": "https://www.momo.vn/merchant/tiem-my-chu-cao-46",
    "Trà đá Mạnh Nháy": "https://www.momo.vn/merchant/tra-da-manh-nhay-bac-ninh-53",
    "Xôi Trường": "https://www.momo.vn/merchant/xoi-truong-bac-ninh-52",
    "Cô Hường Bún Chả": "https://www.momo.vn/merchant/bun-cha-co-huong-58",
    "Mỳ Cường Thư": "https://www.momo.vn/merchant/mi-cuong-thu-thanh-hoa-65",
    "Tiệm Chè Hữu Hòa": "https://www.momo.vn/merchant/tiem-che-huu-hoa-can-tho-66",
    "Miến Gà Cô Nhẫn": "https://www.momo.vn/merchant/mien-ga-co-nhan-59",
    "Cơm Tấm Dì Đức": "https://www.momo.vn/merchant/com-tam-di-duc-57",
    "Bánh Bèo Bánh Bột Lộc Cô Hai Thương": "https://www.momo.vn/merchant/quan-co-hai-thuong-62",
    "Hàng Chè Bà Thơm": "https://www.momo.vn/merchant/hang-che-ba-thom-60",
    "Bò lá lốt mỡ chài chị Hằng": "https://www.momo.vn/merchant/bo-la-lot-chi-hang-68",
    "Lươn Xuân Leo": "https://www.momo.vn/merchant/quan-luon-xuan-leo-61",
    "Nem Chua Phương Chi Lê": "https://www.momo.vn/merchant/nem-chua-phuong-chi-le-67"
}

# Fix typo in mapping dict above
live_mapping["Bánh ướt Cây Me"] = "https://www.momo.vn/merchant/banh-uot-cay-me-can-tho-48"

file_path = "/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/05_USE_CASE_MOMO/doi-tac-brd.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

table_10_1_pattern = r"(\| # \| Merchant \| Tỉnh/TP \| Volume/tháng \| URL cũ \(momo\.vn\) \| URL mới \| Action \| Status \|\n\|---\|---\|---\|---\|---\|---\|---\|---\|\n(?:\|.*?\|\n)+)"
match = re.search(table_10_1_pattern, content)
table_text = match.group(1)
lines = table_text.strip().split("\n")

new_lines = []
for i, line in enumerate(lines):
    if i < 2:
        new_lines.append(line)
        continue
    cols = line.split("|")
    if len(cols) < 9:
        new_lines.append(line)
        continue
    
    merchant_name = cols[2].strip()
    
    if merchant_name in live_mapping:
        cols[6] = f" `{live_mapping[merchant_name]}` "
        cols[8] = " **Live** "
    else:
        # Reset to pending state
        fallback_slug = remove_accents(merchant_name)
        fallback_slug = re.sub(r'[^a-z0-9\-]', '', fallback_slug)
        cols[6] = f" `https://www.momo.vn/merchant/{fallback_slug}-{{id}}` "
        cols[8] = " Chưa launch "
        
    new_lines.append("|".join(cols))

new_table_text = "\n".join(new_lines) + "\n"
new_content = content.replace(table_text, new_table_text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Fixed table mapping successfully.")
