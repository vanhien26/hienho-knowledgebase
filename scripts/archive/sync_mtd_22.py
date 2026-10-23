#!/usr/bin/env python3
"""
Sync GA4 MTD 22 Data across Web Platform SSOT
- Snapshot: 07_REPORTS/data/monthly_10_2026_mtd_22d.json
- summary.json: 07_REPORTS/data/summary.json & Web Hubs
- Excel SSOTs:
    07_REPORTS/web_platform_performance.xlsx
    07_REPORTS/web_performance_tracking.xlsx
- Markdown SSOT: 07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md
"""

import os
import json
import zipfile
import re
import xml.etree.ElementTree as ET

BASE_DIR = "/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base"
SOURCE_ZIP = "/Users/hienhv/Downloads/Web Performance Tracking (1).xlsx"
EXCEL_FILES = [
    os.path.join(BASE_DIR, "07_REPORTS/web_platform_performance.xlsx"),
    os.path.join(BASE_DIR, "07_REPORTS/web_performance_tracking.xlsx")
]
MASTER_MD = os.path.join(BASE_DIR, "07_REPORTS/WEB_PERFORMANCE_TRACKING_MASTER.md")
SUMMARY_JSON = os.path.join(BASE_DIR, "07_REPORTS/data/summary.json")
HUBS_SUMMARY_JSON = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/analytics/summary.json"
SNAPSHOT_22D = os.path.join(BASE_DIR, "07_REPORTS/data/monthly_10_2026_mtd_22d.json")

# Data MTD 22d (2026-10-01 -> 2026-10-22)
TOTAL_PV = 2624335
TARGET_OCT = 3665607
DAYS_ELAPSED = 22
DAYS_IN_MONTH = 31

ORGANIC_PV = 1326764
DIRECT_PV = 675261
PAID_PV = 295998      # Paid Search (266,912) + Paid Social (15,141) + Cross-network (8,894) + Paid Other (5,051)
REFERRAL_PV = 109563
OTHERS_PV = 216749    # Unassigned (158,846) + Organic Social (45,398) + AI Assistant (11,257) + Video/Email/Shopping (1,248)
NON_PAID_PV = ORGANIC_PV + DIRECT_PV + REFERRAL_PV + OTHERS_PV # 2,328,337

TOTAL_USERS = 1320875
TOTAL_SESSIONS = 1763467

# Hubs breakdown MTD 22d
HUB_CINEMA = 865215
HUB_FINANCIAL = 154820
HUB_NEW_USER = 86510
HUB_VEHICLE = 42150
HUB_STUDENT = 1379
HUB_OTHERS = TOTAL_PV - (HUB_CINEMA + HUB_FINANCIAL + HUB_NEW_USER + HUB_VEHICLE + HUB_STUDENT) # 1,474,261

# Cinema sub-pages
CINEMA_RAP = 535584
CINEMA_PHIM = 301904
CINEMA_HOME = 26497
CINEMA_BLOG = 1170
CINEMA_NEWS = 60

NS_MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
ET.register_namespace("", NS_MAIN)

def update_cell(root, coord, formula=None, val=None):
    c = root.find(f".//{{{NS_MAIN}}}c[@r=\"{coord}\"]")
    if c is None:
        m = re.match(r"([A-Z]+)(\d+)", coord)
        if not m:
            return
        col_str, row_str = m.groups()
        row_el = root.find(f".//{{{NS_MAIN}}}row[@r=\"{row_str}\"]")
        if row_el is None:
            sheet_data = root.find(f".//{{{NS_MAIN}}}sheetData")
            row_el = ET.SubElement(sheet_data, f"{{{NS_MAIN}}}row", {"r": row_str})
        c = ET.SubElement(row_el, f"{{{NS_MAIN}}}c", {"r": coord})
    
    # Formula
    f_el = c.find(f"{{{NS_MAIN}}}f")
    if formula is not None:
        if formula == "":
            if f_el is not None:
                c.remove(f_el)
        else:
            if f_el is None:
                f_el = ET.Element(f"{{{NS_MAIN}}}f")
                c.insert(0, f_el)
            f_el.text = formula
            f_el.attrib.pop("t", None)
            f_el.attrib.pop("ref", None)
            
    # Value
    v_el = c.find(f"{{{NS_MAIN}}}v")
    if val is not None:
        if v_el is None:
            v_el = ET.SubElement(c, f"{{{NS_MAIN}}}v")
        v_el.text = str(val)
        val_str = str(val)
        if not val_str.replace("-", "").replace(".", "").isdigit():
            c.attrib["t"] = "str"
        elif "t" in c.attrib:
            del c.attrib["t"]

def patch_excel(dest_path):
    print(f"-> Tạo và patch file Excel: {dest_path}")
    with zipfile.ZipFile(SOURCE_ZIP, "r") as z_in, zipfile.ZipFile(dest_path, "w", compression=zipfile.ZIP_DEFLATED) as z_out:
        for item in z_in.infolist():
            content = z_in.read(item.filename)
            
            # 1. Sheet visibility in xl/workbook.xml
            if item.filename == "xl/workbook.xml":
                root = ET.fromstring(content)
                sheets_el = root.find(f"{{{NS_MAIN}}}sheets")
                if sheets_el is not None:
                    for s in sheets_el:
                        name = s.attrib.get("name", "")
                        if any(p in name.lower() for p in ["pivot", "source", "structure", "details follow", "overall performance  "]):
                            s.attrib["state"] = "hidden"
                        else:
                            s.attrib["state"] = "visible"
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # 2. Sheet 3: Overall Performance
            elif item.filename == "xl/worksheets/sheet3.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val="Update to: 22")
                update_cell(root, "K5", formula="SUM(K9:K13)", val=str(TOTAL_PV))
                update_cell(root, "K6", formula="K5-J5", val=str(TOTAL_PV - 3764435))
                update_cell(root, "K7", formula="IFERROR((K5/J5)-1, 0)", val=str(round((TOTAL_PV / 3764435) - 1, 10)))
                update_cell(root, "K9", formula="", val=str(ORGANIC_PV))
                update_cell(root, "K10", formula="", val=str(PAID_PV))
                update_cell(root, "K11", formula="", val=str(DIRECT_PV))
                update_cell(root, "K12", formula="", val=str(REFERRAL_PV))
                update_cell(root, "K13", formula="", val=str(OTHERS_PV))
                update_cell(root, "T5", formula="SUM(T9:T13)", val=str(TOTAL_PV))
                update_cell(root, "T6", formula="T5-S5", val=str(TOTAL_PV - 2654786))
                update_cell(root, "T7", formula="IFERROR((T5/S5)-1, 0)", val=str(round((TOTAL_PV / 2654786) - 1, 10)))
                update_cell(root, "T9", formula="", val=str(ORGANIC_PV))
                update_cell(root, "T10", formula="", val=str(PAID_PV))
                update_cell(root, "T11", formula="", val=str(DIRECT_PV))
                update_cell(root, "T12", formula="", val=str(REFERRAL_PV))
                update_cell(root, "T13", formula="", val=str(OTHERS_PV))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # 3. Sheet 4: PaidNonPaid
            elif item.filename == "xl/worksheets/sheet4.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val="Update to: 22")
                update_cell(root, "K5", formula="'Overall Performance'!K5", val=str(TOTAL_PV))
                update_cell(root, "K6", formula="K5-J5", val=str(TOTAL_PV - 3764435))
                update_cell(root, "K7", formula="IFERROR((K5/J5)-1, 0)", val=str(round((TOTAL_PV / 3764435) - 1, 10)))
                update_cell(root, "K8", formula="SUM(K9:K12)", val=str(NON_PAID_PV))
                update_cell(root, "K9", formula="", val=str(ORGANIC_PV))
                update_cell(root, "K10", formula="", val=str(DIRECT_PV))
                update_cell(root, "K11", formula="", val=str(REFERRAL_PV))
                update_cell(root, "K12", formula="", val=str(OTHERS_PV))
                update_cell(root, "K13", formula="", val=str(PAID_PV))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # 4. Sheet 5: Target
            elif item.filename == "xl/worksheets/sheet5.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val="Update to: 22")
                update_cell(root, "K6", formula="'Overall Performance'!K5", val=str(TOTAL_PV))
                update_cell(root, "K7", formula="K6-J6", val=str(TOTAL_PV - 3764435))
                update_cell(root, "K8", formula="IFERROR((K6/J6)-1, 0)", val=str(round((TOTAL_PV / 3764435) - 1, 10)))
                prog_pct = round((TOTAL_PV / TARGET_OCT) * 100)
                update_cell(root, "K9", formula='IFERROR(REPT("█", ROUND(K6/K3*4,0)) & " " & TEXT(K6/K3,"0%"), "")', val=f"███ {prog_pct}%")
                update_cell(root, "K10", formula="", val=str(ORGANIC_PV))
                update_cell(root, "K11", formula="", val=str(PAID_PV))
                update_cell(root, "K12", formula="", val=str(DIRECT_PV))
                update_cell(root, "K13", formula="", val=str(REFERRAL_PV))
                update_cell(root, "K14", formula="", val=str(OTHERS_PV))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # 5. Sheet 8: Cinema
            elif item.filename == "xl/worksheets/sheet8.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val="Update to: 22")
                update_cell(root, "H3", formula="SUM(H9,H16,H23,H30,H37,H44)", val=str(HUB_CINEMA))
                update_cell(root, "H4", formula="H3-G3", val=str(HUB_CINEMA - 863885))
                update_cell(root, "H5", formula="(H3/G3)-1", val=str(round((HUB_CINEMA / 863885) - 1, 6)))
                update_cell(root, "H9", formula="", val=str(CINEMA_RAP))
                update_cell(root, "H16", formula="", val=str(CINEMA_PHIM))
                update_cell(root, "H23", formula="", val=str(CINEMA_HOME))
                update_cell(root, "H30", formula="", val=str(CINEMA_BLOG))
                update_cell(root, "H37", formula="", val=str(CINEMA_NEWS))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)
                
            # 6. Sheet 9: Financial
            elif item.filename == "xl/worksheets/sheet9.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val="Update to: 22")
                update_cell(root, "H3", formula="SUM(H8,H15,H22,H36,H29,H50,H43,H64,H71,H78,H85,H92)", val=str(HUB_FINANCIAL))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # 7. Sheet 11: Vehicle
            elif item.filename == "xl/worksheets/sheet11.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val="Update to: 22")
                update_cell(root, "H2", formula="SUM(H6,H13,H20,H27,H34)", val=str(HUB_VEHICLE))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # 8. Sheet 12: Student
            elif item.filename == "xl/worksheets/sheet12.xml":
                root = ET.fromstring(content)
                update_cell(root, "B1", formula='"Update to: " & DAY(NOW())', val="Update to: 22")
                update_cell(root, "H2", formula="SUM(H6,H13)", val=str(HUB_STUDENT))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            # 9. Sheet 10: New User
            elif item.filename == "xl/worksheets/sheet10.xml":
                root = ET.fromstring(content)
                update_cell(root, "A1", formula='"Update to: " & DAY(NOW())', val="Update to: 22")
                update_cell(root, "H3", formula="", val=str(HUB_NEW_USER))
                content = ET.tostring(root, encoding="utf-8", xml_declaration=True)

            z_out.writestr(item, content)

def sync_all():
    # 1. Update Excel files
    for p in EXCEL_FILES:
        patch_excel(p)
        
    # 2. Update snapshot JSON
    daily_pace = round(TOTAL_PV / DAYS_ELAPSED, 2)
    forecast_31d = round(daily_pace * DAYS_IN_MONTH, 2)
    forecast_pct = round((forecast_31d / TARGET_OCT) * 100, 2)
    progress_pct = round((TOTAL_PV / TARGET_OCT) * 100, 2)

    snapshot_data = {
        "file_source": "GA4 Data API (Property 270743103)",
        "read_timestamp": "2026-10-23 09:25:00",
        "report_type": f"MTD {DAYS_ELAPSED} Ngày (01/10 - {DAYS_ELAPSED}/10/2026 - Lũy Kế {DAYS_ELAPSED} Ngày Tháng 10)",
        "days_elapsed": DAYS_ELAPSED,
        "days_in_month": DAYS_IN_MONTH,
        "target_oct_pv": TARGET_OCT,
        "actual_mtd_pv": TOTAL_PV,
        "progress_pct": progress_pct,
        "daily_pace": daily_pace,
        "forecast_31d": forecast_31d,
        "forecast_pct": forecast_pct,
        "users": TOTAL_USERS,
        "sessions": TOTAL_SESSIONS,
        "channels": {
            "organic": {"pv": ORGANIC_PV, "pct": round(ORGANIC_PV / TOTAL_PV * 100, 2)},
            "direct": {"pv": DIRECT_PV, "pct": round(DIRECT_PV / TOTAL_PV * 100, 2)},
            "paid": {"pv": PAID_PV, "pct": round(PAID_PV / TOTAL_PV * 100, 2)},
            "referral": {"pv": REFERRAL_PV, "pct": round(REFERRAL_PV / TOTAL_PV * 100, 2)},
            "others": {"pv": OTHERS_PV, "pct": round(OTHERS_PV / TOTAL_PV * 100, 2)},
            "non_paid_total": {"pv": NON_PAID_PV, "pct": round(NON_PAID_PV / TOTAL_PV * 100, 2)}
        },
        "hubs": {
            "cinema": {"pv": HUB_CINEMA, "target": 1117378, "pct": round(HUB_CINEMA / 1117378 * 100, 2), "forecast": round(HUB_CINEMA / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "financial": {"pv": HUB_FINANCIAL, "target": 450000, "pct": round(HUB_FINANCIAL / 450000 * 100, 2), "forecast": round(HUB_FINANCIAL / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "new_user": {"pv": HUB_NEW_USER, "target": 300000, "pct": round(HUB_NEW_USER / 300000 * 100, 2), "forecast": round(HUB_NEW_USER / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "vehicle": {"pv": HUB_VEHICLE, "target": 100000, "pct": round(HUB_VEHICLE / 100000 * 100, 2), "forecast": round(HUB_VEHICLE / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "student": {"pv": HUB_STUDENT, "target": 100000, "pct": round(HUB_STUDENT / 100000 * 100, 2), "forecast": round(HUB_STUDENT / DAYS_ELAPSED * DAYS_IN_MONTH, 2)},
            "others": {"pv": HUB_OTHERS, "target": 0, "pct": 0, "forecast": round(HUB_OTHERS / DAYS_ELAPSED * DAYS_IN_MONTH, 2)}
        }
    }
    
    with open(SNAPSHOT_22D, "w", encoding="utf-8") as f:
        json.dump(snapshot_data, f, indent=2, ensure_ascii=False)
    print(f"✓ Đã lưu snapshot MTD 22d: {SNAPSHOT_22D}")
    
    # 3. Update summary.json
    summary = {
        "lastFull": {
            "month": "2026-09",
            "pv": 3952859,
            "prevPv": 3465363,
            "target": 3509044
        },
        "running": {
            "month": "2026-10",
            "daysElapsed": DAYS_ELAPSED,
            "daysInMonth": DAYS_IN_MONTH,
            "report": "monthly_10_2026_mtd_22d.json",
            "pv": TOTAL_PV,
            "target": TARGET_OCT,
            "dailyPace": daily_pace,
            "forecast31d": forecast_31d,
            "forecastPct": forecast_pct
        },
        "channels": {
            "organic": ORGANIC_PV,
            "direct": DIRECT_PV,
            "referral": REFERRAL_PV,
            "paid": PAID_PV,
            "others": OTHERS_PV
        },
        "hubs": [
            {"id": "cinema", "name": "Cinema Hub", "pv": HUB_CINEMA, "target": 1117378},
            {"id": "financial", "name": "Financial Hub", "pv": HUB_FINANCIAL, "target": 450000},
            {"id": "new_user", "name": "New User Hub", "pv": HUB_NEW_USER, "target": 300000},
            {"id": "vehicle", "name": "Vehicle Hub", "pv": HUB_VEHICLE, "target": 100000},
            {"id": "student", "name": "Student Hub", "pv": HUB_STUDENT, "target": 100000}
        ]
    }
    with open(SUMMARY_JSON, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"✓ Đã cập nhật summary.json: {SUMMARY_JSON}")
    
    if os.path.exists(os.path.dirname(HUBS_SUMMARY_JSON)):
        with open(HUBS_SUMMARY_JSON, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(f"✓ Đã đồng bộ sang Web Hubs: {HUBS_SUMMARY_JSON}")

if __name__ == "__main__":
    sync_all()
