import re

urls = [
    "https://www.momo.vn/merchant/bun-thit-nuong-chi-tuyen-44",
    "https://www.momo.vn/merchant/com-tam-ong-khoi-dieu-45",
    "https://www.momo.vn/merchant/hu-tieu-my-tho-thanh-xuan-69",
    "https://www.momo.vn/merchant/banh-uot-cay-me-can-tho-48",
    "https://www.momo.vn/merchant/a-ty-mi-xao-gion-bot-chien-64",
    "https://www.momo.vn/merchant/quan-com-chu-lun-47",
    "https://www.momo.vn/merchant/huong-giang-bakery-bac-ninh-63",
    "https://www.momo.vn/merchant/hu-tieu-nam-vang-69-50",
    "https://www.momo.vn/merchant/cha-gio-phuong-dong-nai-56",
    "https://www.momo.vn/merchant/hai-san-ngo-tho-55",
    "https://www.momo.vn/merchant/cha-ruoi-hang-beo-51",
    "https://www.momo.vn/merchant/banh-mi-huu-liem-can-tho-49",
    "https://www.momo.vn/merchant/tiem-my-chu-cao-46",
    "https://www.momo.vn/merchant/tra-da-manh-nhay-bac-ninh-53",
    "https://www.momo.vn/merchant/xoi-truong-bac-ninh-52",
    "https://www.momo.vn/merchant/bun-cha-co-huong-58",
    "https://www.momo.vn/merchant/mi-cuong-thu-thanh-hoa-65",
    "https://www.momo.vn/merchant/tiem-che-huu-hoa-can-tho-66",
    "https://www.momo.vn/merchant/mien-ga-co-nhan-59",
    "https://www.momo.vn/merchant/com-tam-di-duc-57",
    "https://www.momo.vn/merchant/quan-co-hai-thuong-62",
    "https://www.momo.vn/merchant/hang-che-ba-thom-60",
    "https://www.momo.vn/merchant/bo-la-lot-chi-hang-68",
    "https://www.momo.vn/merchant/quan-luon-xuan-leo-61",
    "https://www.momo.vn/merchant/nem-chua-phuong-chi-le-67"
]

file_path = "/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/05_USE_CASE_MOMO/doi-tac-brd.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Helper function to remove diacritics
import unicodedata
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

table_10_1_pattern = r"(\| # \| Merchant \| Tỉnh/TP \| Volume/tháng \| URL cũ \(momo\.vn\) \| URL mới \| Action \| Status \|\n\|---\|---\|---\|---\|---\|---\|---\|---\|\n(?:\|.*?\|\n)+)"
match = re.search(table_10_1_pattern, content)
if not match:
    print("Table 10.1 not found")
    exit(1)

table_text = match.group(1)
lines = table_text.strip().split("\n")

new_lines = []
updated_count = 0

for i, line in enumerate(lines):
    if i < 2:
        new_lines.append(line)
        continue
    cols = line.split("|")
    if len(cols) < 9:
        new_lines.append(line)
        continue
    
    merchant_name = cols[2].strip()
    status = cols[8].strip()
    
    # Try to find a matching URL
    # Heuristic: the url slug contains words from the merchant name
    normalized_name = remove_accents(merchant_name)
    name_words = [w for w in re.split(r'[^a-z0-9]', normalized_name) if w]
    
    best_match_url = None
    max_matches = 0
    
    for url in urls:
        slug = url.split("/")[-1]
        slug_words = slug.split("-")
        
        matches = sum(1 for w in name_words if w in slug_words)
        # Extra mapping for "Cô Hai Thương" to "hai-thuong"
        if "hai" in name_words and "thuong" in name_words and "hai" in slug_words and "thuong" in slug_words:
            matches += 2
            
        # Extra mapping for "A Tỷ" to "a-ty"
        if "a" in name_words and "ty" in name_words and "a" in slug_words and "ty" in slug_words:
            matches += 2
            
        # extra mapping for Hàng Chè Bà Thơm
        if "ba" in name_words and "thom" in name_words and "ba" in slug_words and "thom" in slug_words:
            matches += 2

        if matches > max_matches:
            max_matches = matches
            best_match_url = url
            
    # Custom fallback for some tricky ones
    if "Cô Hai Thương" in merchant_name: best_match_url = "https://www.momo.vn/merchant/quan-co-hai-thuong-62"
    if "A Tỷ" in merchant_name: best_match_url = "https://www.momo.vn/merchant/a-ty-mi-xao-gion-bot-chien-64"
    if "Hương Giang" in merchant_name: best_match_url = "https://www.momo.vn/merchant/huong-giang-bakery-bac-ninh-63"
    if "Cường Thư" in merchant_name: best_match_url = "https://www.momo.vn/merchant/mi-cuong-thu-thanh-hoa-65"
    if "chị Hằng" in merchant_name: best_match_url = "https://www.momo.vn/merchant/bo-la-lot-chi-hang-68"

    if best_match_url and status != "**Live**":
        cols[6] = f" `{best_match_url}` "
        cols[8] = " **Live** "
        updated_count += 1
        print(f"Updated: {merchant_name} -> {best_match_url}")
    elif best_match_url and status == "**Live**":
        # Check if URL needs updating even if live
        current_url = cols[6].replace("`", "").strip()
        if current_url != best_match_url:
            cols[6] = f" `{best_match_url}` "
            print(f"Refined URL: {merchant_name} -> {best_match_url}")
            updated_count += 1

    new_lines.append("|".join(cols))

new_table_text = "\n".join(new_lines) + "\n"
new_content = content.replace(table_text, new_table_text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Total updated: {updated_count}")

