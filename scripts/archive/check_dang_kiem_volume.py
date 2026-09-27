import openpyxl

file_cs = '/Users/hienhv/Downloads/[WP] Vehicle Hub - Content Strategy.xlsx'
file_inv = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/inventory.xlsx'

print("=== 1. CHECKING INVENTORY.XLSX ===")
wb_inv = openpyxl.load_workbook(file_inv, data_only=True)
ws_inv = wb_inv.active
for r in range(1, ws_inv.max_row + 1):
    vals = [str(ws_inv.cell(r, c).value) for c in range(1, ws_inv.max_column + 1)]
    if any('đăng kiểm' in v.lower() or 'kiểm định' in v.lower() for v in vals):
        print("  Row:", vals[:6])

print("\n=== 2. CHECKING [WP] Vehicle Hub - Content Strategy.xlsx (Sheet: Keyword) ===")
wb_cs = openpyxl.load_workbook(file_cs, data_only=True)
ws_kw = wb_cs['Keyword']

dk_keywords = []
for r in range(2, ws_kw.max_row + 1):
    kw = str(ws_kw.cell(r, 1).value or ws_kw.cell(r, 2).value or '').strip().lower()
    if 'đăng kiểm' in kw or 'dang kiem' in kw or 'kiểm định' in kw:
        vol = ws_kw.cell(r, 2).value or ws_kw.cell(r, 3).value or 0
        try:
            vol = float(vol)
        except:
            vol = 0
        intent = ws_kw.cell(r, 3).value or ''
        dk_keywords.append((kw, vol, intent))

# Sort by volume desc
dk_keywords.sort(key=lambda x: x[1], reverse=True)
print(f"Total 'đăng kiểm' keywords found: {len(dk_keywords)}")
total_vol = sum(x[1] for x in dk_keywords)
print(f"Total search volume of all 'đăng kiểm' keywords: {total_vol:,.0f}")

print("\nTop 30 keywords by Search Volume:")
for i, (k, v, intent) in enumerate(dk_keywords[:35], start=1):
    print(f"  {i}. {k}: {v:,.0f} (Intent: {intent})")

# Specifically check for location keywords (hà nội, tphcm, đà nẵng, sài gòn, quận...)
loc_keywords = [x for x in dk_keywords if any(c in x[0] for c in ['hà nội', 'hcm', 'sài gòn', 'đà nẵng', 'bình dương', 'đồng nai', 'quận'])]
print(f"\nLocation keywords found ({len(loc_keywords)} keywords):")
for k, v, intent in loc_keywords[:15]:
    print(f"  - {k}: {v:,.0f}")

