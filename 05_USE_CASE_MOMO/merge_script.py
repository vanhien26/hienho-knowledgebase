import re
import os

file_path = "/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/05_USE_CASE_MOMO/doi-tac-brd.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract Table 1
table1_regex = r"(\| # \| Merchant \| Tỉnh/TP \| Danh mục \| Organic Volume/tháng \| Trending \|\n\|---\|---\|---\|---\|---\|---\|\n.*?\| \| \*\*Tổng Batch 2\*\* \| \*\*11 tỉnh/TP\*\* \| F&B \| \*\*16\.120\*\* \| \|\n)"
table1_match = re.search(table1_regex, content, re.DOTALL)

if not table1_match:
    print("Table 1 not found")
    exit(1)

table1_str = table1_match.group(1)
table1_lines = table1_str.strip().split('\n')

table1_data = {}
for line in table1_lines:
    if "Tổng Batch 2" in line or "---" in line or "Danh mục" in line:
        continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) >= 5:
        merchant_name = cols[1]
        volume = cols[4]
        table1_data[merchant_name.lower()] = volume

# Extract Table 2
table2_regex = r"(\| # \| Merchant \| Tỉnh/TP \| URL cũ \(momo\.vn\) \| URL mới \(thực tế / đề xuất\) \| Action \| Status \|\n\|---\|---\|---\|---\|---\|---\|---\|\n.*?\n)(?=\n### 10\.3)"
table2_match = re.search(table2_regex, content, re.DOTALL)
if not table2_match:
    print("Table 2 not found")
    exit(1)

table2_str = table2_match.group(1)
table2_lines = table2_str.strip().split('\n')

merged_rows = []
merged_rows.append("| # | Merchant | Tỉnh/TP | Volume/tháng | URL cũ (momo.vn) | URL mới | Action | Status |")
merged_rows.append("|---|---|---|---|---|---|---|---|")

for idx, line in enumerate(table2_lines):
    if "---" in line or "URL cũ" in line: continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) < 7: continue
    merchant_name = cols[1]
    tinh = cols[2]
    url_cu = cols[3]
    url_moi = cols[4]
    action = cols[5]
    status = cols[6]
    
    vol = table1_data.get(merchant_name.lower(), "0")
    
    merged_rows.append(f"| {idx} | {merchant_name} | {tinh} | {vol} | {url_cu} | {url_moi} | {action} | {status} |")

merged_table_str = "\n".join(merged_rows) + "\n"

# Replace Table 2 with merged table
new_content = content.replace(table2_str, merged_table_str)

# Remove Table 1 since it's merged, but keep the surrounding text
new_content = new_content.replace(table1_str, "> **Đã gộp bảng dữ liệu vào Section 10.1 (SME Batch 2 Matrix) bên dưới.**\n")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Merged successfully!")
