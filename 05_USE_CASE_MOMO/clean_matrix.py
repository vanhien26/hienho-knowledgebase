import re

file_path = "/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/05_USE_CASE_MOMO/doi-tac-brd.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove the table in 10.0
# The table looks like:
# #### Scope Batch 2 - Merchants cần OA-ID bridge
# 
# | # | PAGE_ID | Merchant | Slug đề xuất | Status |
# ...
# | 3 | `/page/9949928` | Bò nhúng Mắm ruốc 8 Còn | `/merchant/bo-nhung-mam-ruoc-8-con-{id}` | Pending OA-ID |

table_10_0_pattern = r"(#### Scope Batch 2 - Merchants cần OA-ID bridge\n\n\| # \| PAGE_ID \| Merchant \| Slug đề xuất \| Status \|\n\|---\|---\|---\|---\|---\|\n(?:\|.*?\|\n)+)"
content = re.sub(table_10_0_pattern, "#### Scope Batch 2 - Merchants cần OA-ID bridge\n\n> Đã gộp toàn bộ vào bảng Tracking Matrix (Mục 10.1) bên dưới.\n\n", content)

# Now find the table in 10.1
# It starts with | # | Merchant | Tỉnh/TP | Volume/tháng | URL cũ (momo.vn) | URL mới | Action | Status |
table_10_1_pattern = r"(\| # \| Merchant \| Tỉnh/TP \| Volume/tháng \| URL cũ \(momo\.vn\) \| URL mới \| Action \| Status \|\n\|---\|---\|---\|---\|---\|---\|---\|---\|\n(?:\|.*?\|\n)+)"
match = re.search(table_10_1_pattern, content)
if not match:
    print("Could not find table 10.1")
    exit(1)

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
    
    url_moi = cols[6].strip()
    
    # Ensure URL mới has full domain
    if "`" in url_moi:
        inner = url_moi.strip("` ")
        if inner.startswith("/merchant/"):
            inner = "https://www.momo.vn" + inner
        url_moi = f"`{inner}`"
    else:
        if url_moi.startswith("/merchant/"):
            url_moi = "https://www.momo.vn" + url_moi
            
    cols[6] = " " + url_moi + " "
    
    # Optional: re-index the numbers to be perfectly sequential (1 to 38)
    cols[1] = f" {i-1} "
    
    new_lines.append("|".join(cols))

new_table_text = "\n".join(new_lines) + "\n"

new_content = content.replace(table_text, new_table_text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Cleaned and updated matrix successfully.")

