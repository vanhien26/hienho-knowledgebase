#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REBUILD PROJECTS DETAIL FLOW WITH INTERLEAVED CLICK ROWS
Chèn trực tiếp dòng 'Click [Project Name]' (màu xám #F1F3F4) xen kẽ ngay bên dưới mỗi dự án
trong sheet 'Projects Detail Flow' trên Google Sheets SSOT.
"""

import sys
import json
import urllib.request
import urllib.parse
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from scripts.sync_to_google_sheet_api import get_sheets_token, TARGET_SHEET_ID
from scripts.sync_ga4_to_hubs import get_access_token, run_ga4_report
import scripts.lib.url_project_resolver as upr

SHEET_TITLE = "Projects Detail Flow"
SHEET_ID = 316527624

def get_clicks_by_project(token, start_date, end_date):
    """Kéo số click onelink theo landing page từ GA4 và map sang Project Name."""
    rules = upr.load_rules()
    inferred = upr.load_inferred_rules(rules)
    
    res = run_ga4_report(token, {
        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
        "dimensions": [{"name": "landingPage"}],
        "dimensionFilter": {
            "andGroup": {
                "expressions": [
                    {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["click_to_app", "click_outbound_link"]}}},
                    {
                        "orGroup": {
                            "expressions": [
                                {"filter": {"fieldName": "customEvent:click_url", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}},
                                {"filter": {"fieldName": "linkUrl", "stringFilter": {"matchType": "CONTAINS", "value": "onelink"}}}
                            ]
                        }
                    }
                ]
            }
        },
        "metrics": [{"name": "eventCount"}],
        "limit": 10000
    })
    
    clicks = defaultdict(int)
    for r in res.get("rows", []):
        lp = r["dimensionValues"][0]["value"]
        cnt = int(r["metricValues"][0]["value"])
        p = upr.resolve_primary("https://www.momo.vn" + lp, rules, inferred)
        clicks[p] += cnt
    return clicks

def col_letter(idx):
    """0-indexed to column letter (0->A, 1->B, etc.)"""
    return chr(ord('A') + idx)

def run():
    print("[1/5] Kéo dữ liệu Onelink Clicks từ GA4 API...")
    ga4_token = get_access_token()
    oct_mtd = get_clicks_by_project(ga4_token, "2026-10-01", "2026-10-26")
    sep_mtd = get_clicks_by_project(ga4_token, "2026-09-01", "2026-09-26")
    sep_full = get_clicks_by_project(ga4_token, "2026-09-01", "2026-09-30")
    
    norm_oct = {k.lower(): v for k, v in oct_mtd.items()}
    norm_sep_m = {k.lower(): v for k, v in sep_mtd.items()}
    norm_sep_f = {k.lower(): v for k, v in sep_full.items()}

    print(f"  ✓ Oct MTD: {sum(oct_mtd.values()):,} clicks")
    print(f"  ✓ Sep MTD: {sum(sep_mtd.values()):,} clicks")
    print(f"  ✓ Sep Full: {sum(sep_full.values()):,} clicks")

    # 65 projects gốc theo thứ tự từ A8 đến A72
    raw_projects = [
        "Cinema Hub", "Cinema_Cineplex Page", "Cinema_Page", "Cinema_Blog",
        "Cinema_Home Page", "Cinema_News", "Cinema_Landing Page",
        "Home MoMo", "Tìm Kiếm", "Tiktok",
        "Financial Hub", "Vay Nhanh", "Điểm Tín Dụng", "Ví Trả Sau",
        "Túi Thần Tài", "Mở Thẻ Tín Dụng", "Quản Lý Chi Tiêu", "Trả Góp Apple",
        "Thanh Toán Khoản Vay", "Chứng Khoán", "Tiết Kiệm Online",
        "Thanh Toán Thẻ Tín Dụng", "Chứng Chỉ Quỹ", "Trung Tâm Tài Chính", "Sàn Đầu Tư",
        "Vehicle Hub", "Phạt nguội", "Bảo hiểm ô tô", "Bảo hiểm xe máy", "Tiện ích giao thông",
        "Vé Xe", "OTA", "Merchant", "Sim", "Sim", "Esim", "Game", "Bảo hiểm y tế",
        "Data", "Soundbox", "New User", "Hỏi đáp", "TnC", "Trust", "Guide",
        "Khuyến mãi", "Tin Tức", "Campaign", "Blog", "Application Store", "Vé số",
        "Dịch vụ liên kết", "Billpay", "P2P", "Điện", "Student Hub", "Student Pass",
        "Student Hub", "Cross Border", "Hoàn Tiền Mua Sắm", "Bảo Hiểm Sức Khỏe",
        "Mở tài khoản ngân hàng", "Download", "Nước", "Others"
    ]

    # Định nghĩa cấu trúc Hubs và các con (0-indexed trong raw_projects)
    hub_children = {
        0: list(range(1, 7)),       # Cinema Hub -> 1..6
        10: list(range(11, 25)),    # Financial Hub -> 11..24
        25: list(range(26, 30)),    # Vehicle Hub -> 26..29
        33: [34, 35],               # Sim -> 34, 35
        55: [56, 57]                # Student Hub -> 56, 57
    }

    # Các chỉ số con bị ẩn bởi người dùng: Cinema subpages (1..6), Vehicle subpages (26..29), Sim subpages (34..35)
    hidden_child_indices = set(range(1, 7)) | set(range(26, 30)) | {34, 35}

    # Bảng row mapping (1-based row numbers in sheet):
    # Mỗi item i chiếm 2 hàng: PV tại row (8 + 2*i), Click tại row (9 + 2*i)
    pv_rows = {}
    click_rows = {}
    for i in range(len(raw_projects)):
        pv_rows[i] = 8 + 2 * i
        click_rows[i] = 9 + 2 * i

    print("[2/5] Xây dựng dữ liệu và công thức 130 hàng dự án xen kẽ...")
    table_rows = []

    # Danh sách các cột tháng MTD và Full month
    mtd_cols = ["B", "C", "D", "E", "F", "G", "H", "I"]
    full_cols = ["L", "M", "N", "O", "P", "Q", "R", "S"]

    for i, p_name in enumerate(raw_projects):
        r_pv = pv_rows[i]
        r_click = click_rows[i]

        is_hub = i in hub_children
        children = hub_children.get(i, [])

        # HÀNG 1: PAGE VIEW ROW (r_pv)
        pv_row_data = [p_name]
        if is_hub:
            # Hub PV: Công thức sum các con tương ứng
            c_pv_rows = [pv_rows[c] for c in children]
            for col in mtd_cols:
                sum_args = ", ".join([f"{col}{cr}" for cr in c_pv_rows])
                pv_row_data.append(f"=SUM({sum_args})")
            # Col J: VS. SPLM
            pv_row_data.append(f"=G{r_pv}-F{r_pv}")
            # Col K: Blank
            pv_row_data.append("")
            # Col L..S: Full month sum
            for col in full_cols:
                sum_args = ", ".join([f"{col}{cr}" for cr in c_pv_rows])
                pv_row_data.append(f"=SUM({sum_args})")
            # Col T: VS. SPLM cùng kỳ
            pv_row_data.append(f"=G{r_pv}-F{r_pv}")
        else:
            # Child / Standalone PV: Công thức SUMPRODUCT từ Pivot
            for col in mtd_cols:
                pv_row_data.append(f"=SUMPRODUCT(('MTD Pivot'!$A$3:$A$400=$A${r_pv})*('MTD Pivot'!$D$2:$K$2={col}$2)*'MTD Pivot'!$D$3:$K$400)")
            # Col J: VS. SPLM
            pv_row_data.append(f"=G{r_pv}-F{r_pv}")
            # Col K: Blank
            pv_row_data.append("")
            # Col L..S: Full month SUMPRODUCT
            for col in full_cols:
                pv_row_data.append(f"=SUMPRODUCT(('Full month Pivot'!$A$3:$A$400=$A${r_pv})*('Full month Pivot'!$D$2:$K$2={col}$2)*'Full month Pivot'!$D$3:$K$400)")
            # Col T: VS. SPLM cùng kỳ
            pv_row_data.append(f"=G{r_pv}-F{r_pv}")

        table_rows.append(pv_row_data)

        # HÀNG 2: CLICK TO APP ROW (r_click)
        # Tên hiển thị dòng Click
        if is_hub:
            click_label = f"Click {p_name}"
            if p_name == "Cinema Hub":
                click_label = "Click Cinema"
            elif p_name == "Vehicle Hub":
                click_label = "Click Vehicle Hub"
            elif p_name == "Financial Hub":
                click_label = "Click Financial Hub"
            elif p_name == "Student Hub":
                click_label = "Click Student Hub"
            elif p_name == "Sim":
                click_label = "Click Sim"
        else:
            # Thụt lề nếu là con của Hub
            is_child = any(i in c_list for c_list in hub_children.values())
            indent = "    " if is_child else ""
            click_label = f"{indent}Click {p_name}"

        click_row_data = [click_label]
        # Col B..E (May..Aug MTD): ""
        click_row_data.extend(["", "", "", ""])

        if is_hub:
            c_click_rows = [click_rows[c] for c in children]
            # Col F (Sep 26 MTD): Sum child clicks
            sum_f = ", ".join([f"F{cr}" for cr in c_click_rows])
            click_row_data.append(f"=SUM({sum_f})")
            # Col G (Oct 26 MTD): Sum child clicks
            sum_g = ", ".join([f"G{cr}" for cr in c_click_rows])
            click_row_data.append(f"=SUM({sum_g})")
            # Col H, I: ""
            click_row_data.extend(["", ""])
            # Col J: VS. SPLM (=G - F)
            click_row_data.append(f"=G{r_click}-F{r_click}")
            # Col K: Oct CVR % (=Click / PV)
            click_row_data.append(f"=IF(G{r_pv}>0, G{r_click}/G{r_pv}, 0)")
            # Col L..O (May..Aug Full): ""
            click_row_data.extend(["", "", "", ""])
            # Col P (Sep Full): Sum child clicks
            sum_p = ", ".join([f"P{cr}" for cr in c_click_rows])
            click_row_data.append(f"=SUM({sum_p})")
            # Col Q (Oct Full): =G
            click_row_data.append(f"=G{r_click}")
            # Col R, S: ""
            click_row_data.extend(["", ""])
            # Col T: VS. SPLM cùng kỳ (=G - F)
            click_row_data.append(f"=G{r_click}-F{r_click}")
        else:
            c_oct = oct_mtd.get(p_name, norm_oct.get(p_name.lower(), 0))
            c_sep_m = sep_mtd.get(p_name, norm_sep_m.get(p_name.lower(), 0))
            c_sep_f = sep_full.get(p_name, norm_sep_f.get(p_name.lower(), 0))

            # Col F (Sep 26 MTD)
            click_row_data.append(c_sep_m)
            # Col G (Oct 26 MTD)
            click_row_data.append(c_oct)
            # Col H, I: ""
            click_row_data.extend(["", ""])
            # Col J: VS. SPLM
            click_row_data.append(f"=G{r_click}-F{r_click}")
            # Col K: Oct CVR %
            click_row_data.append(f"=IF(G{r_pv}>0, G{r_click}/G{r_pv}, 0)")
            # Col L..O: ""
            click_row_data.extend(["", "", "", ""])
            # Col P: Sep Full
            click_row_data.append(c_sep_f)
            # Col Q: Oct Full
            click_row_data.append(f"=G{r_click}")
            # Col R, S: ""
            click_row_data.extend(["", ""])
            # Col T: VS. SPLM cùng kỳ (=G - F)
            click_row_data.append(f"=G{r_click}-F{r_click}")

        table_rows.append(click_row_data)

    print(f"  ✓ Đã sinh {len(table_rows)} hàng (từ hàng 8 đến hàng {8 + len(table_rows) - 1})")

    # Row 138: Blank
    table_rows.append([""] * 20)

    # Row 139: Header %Page view by Project
    r_pct_header = 8 + len(table_rows) - 1
    table_rows.append(["%Page view by Project\n= PV project / PV total "] + [""] * 19)

    # Khối % Page view by Project (35 items gốc từ hàng 75 đến 108)
    pct_items = [
        ("%Cinema Hub", 0),             # item 0
        ("%Phạt nguội", 26),            # item 26
        ("%Home MoMo", 7),              # item 7
        ("%Tiktok", 9),                 # item 9
        ("%Financial Hub", 10),         # item 10
        ("%Vé Xe", 30),                 # item 30
        ("%OTA", 31),                   # item 31
        ("%OA", 32),                    # item 32 (Merchant)
        ("%Sim", 33),                   # item 33
        ("%Game", 36),                  # item 36
        ("%Bảo hiểm ô tô", 27),         # item 27
        ("%Bảo hiểm xe máy", 28),       # item 28
        ("%Bảo hiểm y tế", 37),         # item 37
        ("%Data", 38),                  # item 38
        ("%Soundbox", 39),              # item 39
        ("%New User", 40),              # item 40
        ("%Hỏi đáp", 41),               # item 41
        ("%TnC", 42),                   # item 42
        ("%Trust", 43),                 # item 43
        ("%Guide", 44),                 # item 44
        ("%Khuyến mãi", 45),            # item 45
        ("%Campaign", 47),              # item 47
        ("%Blog", 48),                  # item 48
        ("%Application Store", 49),     # item 49
        ("%Vé số", 50),                 # item 50
        ("%Dịch vụ liên kết", 51),      # item 51
        ("%Billpay", 52),               # item 52
        ("%P2P", 53),                   # item 53
        ("%Điện", 54),                  # item 54
        ("%Student Hub", 55),           # item 55
        ("%Cross Border", 58),          # item 58
        ("%Hoàn Tiền Mua Sắm", 59),     # item 59
        ("%Mở tài khoản ngân hàng", 61),# item 61
        ("%Others", 64)                 # item 64
    ]

    for label, it_idx in pct_items:
        target_pv_row = pv_rows[it_idx]
        pct_row = [label]
        for col in mtd_cols:
            pct_row.append(f'=IFERROR({col}{target_pv_row}/{col}$3, "-")')
        pct_row.append("") # Col J
        pct_row.append("") # Col K
        for col in full_cols:
            pct_row.append(f'=IFERROR({col}{target_pv_row}/{col}$3, "-")')
        pct_row.append(f'=G{8 + len(table_rows)}-F{8 + len(table_rows)}') # Col T: VS. SPLM cùng kỳ
        table_rows.append(pct_row)

    print(f"  ✓ Tổng số hàng cập nhật: {len(table_rows)} (Range A8:T{8 + len(table_rows) - 1})")

    # [3/5] Cập nhật công thức Row 3 (Page views Actual)
    # Danh sách các top-level PV rows cần sum:
    # item 0 (Cinema Hub)
    # item 7..10 (Home MoMo, Tìm Kiếm, Tiktok, Financial Hub)
    # item 25 (Vehicle Hub)
    # item 29 (Tiện ích giao thông - giữ đúng công thức gốc)
    # item 30..33 (Vé Xe, OTA, Merchant, Sim)
    # item 36..55 (Game .. Student Hub)
    # item 58..64 (Cross Border .. Others)
    top_items_idx = [0] + list(range(7, 11)) + [25, 29] + list(range(30, 34)) + list(range(36, 56)) + list(range(58, 65))
    top_pv_rows = [pv_rows[idx] for idx in top_items_idx]

    row3_formulas = []
    # B3..F3: =SUM(...)
    for col in ["B", "C", "D", "E", "F"]:
        sum_args = ", ".join([f"{col}{r}" for r in top_pv_rows])
        row3_formulas.append(f"=SUM({sum_args})")
    # G3: Giữ nguyên INDEX MATCH Pivot
    row3_formulas.append("=ARRAY_CONSTRAIN(ARRAYFORMULA(INDEX('MTD Pivot'!$D$3:$K$400, MATCH(\"Grand Total\", 'MTD Pivot'!$A$3:$A$400, 0), MATCH(G$2, 'MTD Pivot'!$D$2:$K$2, 0))), 1, 1)")
    # H3, I3:
    for col in ["H", "I"]:
        sum_args = ", ".join([f"{col}{r}" for r in top_pv_rows])
        row3_formulas.append(f"=SUM({sum_args})")
    # J3: =G3-F3
    row3_formulas.append("=G3-F3")
    # K3: Total Web W2A CVR
    top_click_rows = [click_rows[idx] for idx in top_items_idx]
    k3_sum = ", ".join([f"G{r}" for r in top_click_rows])
    row3_formulas.append(f"=SUM({k3_sum})/G3")
    # L3..P3:
    for col in ["L", "M", "N", "O", "P"]:
        sum_args = ", ".join([f"{col}{r}" for r in top_pv_rows])
        row3_formulas.append(f"=SUM({sum_args})")
    # Q3:
    row3_formulas.append("=ARRAY_CONSTRAIN(ARRAYFORMULA(INDEX('Full month Pivot'!$D$3:$K$400, MATCH(\"Grand Total\", 'Full month Pivot'!$A$3:$A$400, 0), MATCH(Q$2, 'Full month Pivot'!$D$2:$K$2, 0))), 1, 1)")
    # R3, S3:
    for col in ["R", "S"]:
        sum_args = ", ".join([f"{col}{r}" for r in top_pv_rows])
        row3_formulas.append(f"=SUM({sum_args})")
    # T3: =G3-F3 (so sánh cùng kỳ MTD)
    row3_formulas.append("=G3-F3")

    # [4/5] Ghi dữ liệu vào Google Sheets
    sheets_token = get_sheets_token()
    print("[4/5] Đang ghi dữ liệu và công thức vào Google Sheets...")

    # Ghi Row 3
    url_r3 = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{urllib.parse.quote(SHEET_TITLE + '!B3:T3')}?valueInputOption=USER_ENTERED"
    req_r3 = urllib.request.Request(
        url_r3,
        data=json.dumps({"range": f"{SHEET_TITLE}!B3:T3", "majorDimension": "ROWS", "values": [row3_formulas]}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req_r3) as resp:
        res_r3 = json.loads(resp.read().decode())
    print(f"  ✓ Đã cập nhật công thức Row 3 ({res_r3.get('updatedCells', 0)} ô)")

    # Ghi khối A8:T...
    end_row = 8 + len(table_rows) - 1
    range_target = urllib.parse.quote(f"{SHEET_TITLE}!A8:T{end_row}")
    url_table = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}/values/{range_target}?valueInputOption=USER_ENTERED"
    req_table = urllib.request.Request(
        url_table,
        data=json.dumps({"range": f"{SHEET_TITLE}!A8:T{end_row}", "majorDimension": "ROWS", "values": table_rows}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req_table) as resp:
        res_table = json.loads(resp.read().decode())
    print(f"  ✓ Đã cập nhật bảng dự án xen kẽ ({res_table.get('updatedCells', 0)} ô)")

    # [5/5] Định dạng styling: Background xám #F1F3F4, Font Italic, Number formats, và Hidden rows
    print("[5/5] Áp dụng định dạng (Nền xám #F1F3F4, NumberFormat, Hidden subpages)...")
    requests = []

    # 1. Format toàn bộ các hàng Click: Nền xám #F1F3F4, text color #3c4043, italic
    gray_color = {"red": 241/255, "green": 243/255, "blue": 244/255}
    text_color = {"red": 60/255, "green": 64/255, "blue": 67/255}

    for i in range(len(raw_projects)):
        r_c_0indexed = click_rows[i] - 1
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_c_0indexed,
                    "endRowIndex": r_c_0indexed + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 20
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": gray_color,
                        "textFormat": {
                            "foregroundColor": text_color,
                            "italic": True
                        }
                    }
                },
                "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat.foregroundColor,userEnteredFormat.textFormat.italic"
            }
        })

    # 2. Number format cho các cột Clicks: #,##0 cho cols 1..9 và 11..18
    # CVR %: 0.0% cho col 10 (K) và col 19 (T)
    for i in range(len(raw_projects)):
        r_c_0indexed = click_rows[i] - 1
        # Number #,##0
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_c_0indexed,
                    "endRowIndex": r_c_0indexed + 1,
                    "startColumnIndex": 1,
                    "endColumnIndex": 10
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "NUMBER", "pattern": "#,##0"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_c_0indexed,
                    "endRowIndex": r_c_0indexed + 1,
                    "startColumnIndex": 11,
                    "endColumnIndex": 19
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "NUMBER", "pattern": "#,##0"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        # CVR %
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_c_0indexed,
                    "endRowIndex": r_c_0indexed + 1,
                    "startColumnIndex": 10,
                    "endColumnIndex": 11
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "PERCENT", "pattern": "0.0%"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": SHEET_ID,
                    "startRowIndex": r_c_0indexed,
                    "endRowIndex": r_c_0indexed + 1,
                    "startColumnIndex": 19,
                    "endColumnIndex": 20
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {"type": "PERCENT", "pattern": "0.0%"}
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })

    # 3. Hidden rows:
    # Ẩn các hàng con của Cinema (items 1..6: pv + click), Vehicle (items 26..29: pv + click), Sim (items 34..35: pv + click)
    for hidden_it in sorted(hidden_child_indices):
        p_row_0 = pv_rows[hidden_it] - 1
        c_row_0 = click_rows[hidden_it] - 1
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": SHEET_ID,
                    "dimension": "ROWS",
                    "startIndex": p_row_0,
                    "endIndex": c_row_0 + 1
                },
                "properties": {
                    "hiddenByUser": True
                },
                "fields": "hiddenByUser"
            }
        })

    # Đảm bảo các hàng Hub Click (Row 9 Click Cinema, Row 59 Click Vehicle Hub, Row 75 Click Sim) KHÔNG bị ẩn!
    for hub_it in hub_children.keys():
        hub_c_0 = click_rows[hub_it] - 1
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": SHEET_ID,
                    "dimension": "ROWS",
                    "startIndex": hub_c_0,
                    "endIndex": hub_c_0 + 1
                },
                "properties": {
                    "hiddenByUser": False
                },
                "fields": "hiddenByUser"
            }
        })

    # 4. K1:K2 Merge & Header "W2A CVR"
    requests.append({
        "mergeCells": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 2,
                "startColumnIndex": 10,
                "endColumnIndex": 11
            },
            "mergeType": "MERGE_ALL"
        }
    })
    requests.append({
        "updateCells": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 10,
                "endColumnIndex": 11
            },
            "rows": [{
                "values": [{
                    "userEnteredValue": {"stringValue": "W2A CVR"},
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 1.0, "green": 0.8980392, "blue": 0.6},
                        "horizontalAlignment": "CENTER",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontFamily": "Arial",
                            "fontSize": 11,
                            "bold": True
                        }
                    }
                }]
            }],
            "fields": "userEnteredValue,userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)"
        }
    })

    # 5. K3 Number Format & Style
    requests.append({
        "repeatCell": {
            "range": {
                "sheetId": SHEET_ID,
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 10,
                "endColumnIndex": 11
            },
            "cell": {
                "userEnteredFormat": {
                    "numberFormat": {"type": "PERCENT", "pattern": "0.0%"},
                    "horizontalAlignment": "RIGHT",
                    "textFormat": {
                        "fontFamily": "Arial",
                        "fontSize": 11,
                        "bold": True
                    }
                }
            },
            "fields": "userEnteredFormat.numberFormat,userEnteredFormat.horizontalAlignment,userEnteredFormat.textFormat"
        }
    })

    # Gửi batchUpdate
    url_batch = f"https://sheets.googleapis.com/v4/spreadsheets/{TARGET_SHEET_ID}:batchUpdate"
    req_batch = urllib.request.Request(
        url_batch,
        data=json.dumps({"requests": requests}).encode("utf-8"),
        headers={"Authorization": f"Bearer {sheets_token}", "Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req_batch) as resp:
        res_batch = json.loads(resp.read().decode())
    print(f"  ✓ Hoàn tất áp dụng styling và cấu hình ẩn/hiện ({len(res_batch.get('replies', []))} thao tác)")

    print("\n[SUCCESS] Đã hoàn thành cấu trúc xen kẽ dòng Click to app (màu xám #F1F3F4) thành công 100%!")

if __name__ == "__main__":
    run()
