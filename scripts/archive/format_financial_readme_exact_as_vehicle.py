import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')

# Styling tokens matching vehicle-hub-roadmap.xlsx exactly
color_pink_brand = "A50064" # MoMo Pink/Plum for Section Titles
color_slate_dark = "1E293B" # Slate 800 for body text
thin_side = Side(style='thin', color='CBD5E1')
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

font_note = Font(name='Arial', size=10.0, bold=True, color='000000')
font_section = Font(name='Arial', size=10.5, bold=True, color=color_pink_brand)
font_label_bold = Font(name='Arial', size=9.5, bold=True, color=color_slate_dark)
font_label_regular = Font(name='Arial', size=9.5, bold=False, color=color_slate_dark)
font_val_regular = Font(name='Arial', size=9.5, bold=False, color=color_slate_dark)

# Delete existing Readme and recreate at index 0
if 'Readme' in wb.sheetnames:
    del wb['Readme']

ws_rm = wb.create_sheet('Readme', index=0)
ws_rm.column_dimensions['A'].width = 46.0
ws_rm.column_dimensions['B'].width = 85.0

# Define full content for Financial Hub matching the vehicle-hub-roadmap structure
readme_sections = [
    # (Type, Val1, Val2)
    ("NOTE", "Note: Do not share access to all materials without project manager's permission", ""),
    ("BLANK", "", ""),

    ("SECTION", "Quy Trình Hợp Tác Chiến Lược Mới (Web Platform x Financial Services / CreditTech)", ""),
    ("ROW_BOLD", "Tôn Chỉ Hợp Tác", "Phát triển Financial Master Hub (momo.vn/tai-chinh) làm Cổng Khám Phá & Ra Quyết Định Tài Chính Toàn Diện, dẫn dắt chuyển đổi sang App MoMo"),
    ("ROW_BOLD", "1. Đồng Sở Hữu KPI (KPI Co-ownership)", "Web Product đồng sở hữu KPI với FS / CreditTech (Target: 1.000.000 MPV/tháng, 500K MEU Active, W2A CTR 15-25%, Tăng trưởng 25% 1st Financial Transactions)"),
    ("ROW_BOLD", "2. Quản Lý Dự Án Bài Bản (Single SSOT)", "Sử dụng file này làm công cụ SSOT quản lý lộ trình phát triển Web Product (Timeline, Checklist, 24 Thị trường CreditTech, Danh bạ 34 Bank và Đặc tả Tiện ích Web)"),
    ("ROW_BOLD", "3. Vận Hành Sprint 1 Tháng (Cadence)", "Họp lập kế hoạch (Sprint Planning) đầu tháng; Rà soát tiến độ (Check-in) định kỳ 2 tuần/lần (giữa và cuối tháng)"),
    ("ROW_BOLD", "4. Trách Nhiệm Giải Trình (Accountability)", "Báo cáo tiến độ minh bạch hàng tháng cho IVP Leadership. Nếu BU trễ 1-2 tháng, Web Platform sẽ bàn giao lại dự án và chuyển tài nguyên sang BU khác"),
    ("BLANK", "", ""),

    ("SECTION", "Project Management Docs", ""),
    ("ROW_REG", "BRD (Master Specification)", "[Web Platform] Financial Master Hub - Master BRD (SSOT - 05_HUBS/financial-hub-brd.md)"),
    ("ROW_REG", "Roadmap & Monthly Sprint Plan", "[Web Platform] Financial Hub - Roadmap 2026 (05_HUBS/financial-hub-roadmap.xlsx)"),
    ("ROW_REG", "Content Strategy & Keyword Plan", "[WP] Financial Hub - Content Strategy & MoSpark AI Pipeline (58.1K KWs)"),
    ("ROW_REG", "Tracking & Onelink Plan (W2A)", "Web Platform x Financial Services - Appsflyer Onelink & W2A Tracking Spec"),
    ("ROW_REG", "Market Sizing & Search Demand", "Financial Hub - Master Inventory Sizing (102.14M (24 Thị Trường) Search/Tháng - 05_HUBS/inventory.xlsx)"),
    ("ROW_REG", "Budget & Resource Tracker", "2026_WebPlatform_FinancialHub_Tracker"),
    ("BLANK", "", ""),

    ("SECTION", "Design & UX/UI (Figma)", ""),
    ("ROW_REG", "Master Design Board (Figma)", "https://www.figma.com/design/momo-financial-hub-2026"),
    ("ROW_REG", "Design System & UI Kit", "@momo-webplatform/mobase"),
    ("ROW_REG", "Responsive Prototype (Web & Mobile)", "https://www.figma.com/proto/momo-financial-hub-prototype"),
    ("ROW_REG", "Asset Library (Brand Logos, Icons)", "MoMo Financial Hub & 34 Partner Banks Asset Library"),
    ("BLANK", "", ""),

    ("SECTION", "Environments & Testing (UAT / Staging / Live)", ""),
    ("ROW_REG", "Môi Trường UAT / Staging", "https://staging-web.momo.vn/tai-chinh"),
    ("ROW_REG", "Môi Trường Production (Live)", "https://www.momo.vn/tai-chinh"),
    ("ROW_REG", "Cổng Quản Trị Nội Dung (CMS)", "https://mospark.mservice.io/financial-hub"),
    ("ROW_REG", "Hạ Tầng Data Connectors & APIs", "Realtime Feeds Connectors (Giá Vàng SJC, Tỷ Giá Ngoại Tệ, Lãi Suất Tiết Kiệm 34 Bank)"),
    ("BLANK", "", ""),

    ("SECTION", "Materials & Marketing Deliverables", ""),
    ("ROW_REG", "Quick snapshot of users' Insights", "Personal Finance User Pain Points & Pre-install Discovery Demand 2026"),
    ("ROW_REG", "Value Exchange Concept (Interactive Tools)", "No-Login Value First: Trải nghiệm công cụ tính toán trước ➔ Mở App eKYC nhận giải pháp MoMo"),
    ("ROW_REG", "QR Code dẫn về trang Hub in-app", "Dynamic QR Code Generator for Desktop Web (Universal OneLink)"),
    ("ROW_REG", "RefId / Tracking QR / Onelink", "Appsflyer Onelink Config (pid=web_hub, c=financial_master_2026, af_dp=momo://finance)"),
    ("BLANK", "", ""),

    ("SECTION", "Legal & Compliance", ""),
    ("ROW_REG", "File đưa legal check", "Financial Hub - Data Privacy, YMYL E-E-A-T & Financial Disclaimers"),
    ("ROW_REG", "Quy tắc bảo mật thông tin (0-PII)", "Ẩn 100% thông tin cá nhân & PII trên public web; Không lưu trữ lịch sử nợ xấu/CIC trên client"),
    ("BLANK", "", ""),

    ("SECTION", "Working Board & Alignment", ""),
    ("ROW_REG", "Monthly Sprint Planning & Check-in", "Lập kế hoạch đầu tháng | Review tiến độ ngày 15 & 30 hàng tháng"),
    ("ROW_REG", "Báo Cáo Tiến Độ (IVP Leadership)", "Báo cáo minh bạch hàng tháng gửi Ban Lãnh Đạo IVP (Theo chuẩn Key Highlights & Business Impact)")
]

for item_type, val1, val2 in readme_sections:
    if item_type == "NOTE":
        ws_rm.append([val1, val2])
        r = ws_rm.max_row
        ws_rm.row_dimensions[r].height = 24.0
        ws_rm.cell(row=r, column=1).font = font_note
        ws_rm.cell(row=r, column=1).alignment = Alignment(horizontal='left', vertical='center')
    elif item_type == "BLANK":
        ws_rm.append(["", ""])
        r = ws_rm.max_row
        ws_rm.row_dimensions[r].height = 10.0
    elif item_type == "SECTION":
        ws_rm.append([val1, val2])
        r = ws_rm.max_row
        ws_rm.row_dimensions[r].height = 22.0
        ws_rm.cell(row=r, column=1).font = font_section
        ws_rm.cell(row=r, column=1).alignment = Alignment(horizontal='left', vertical='center')
    elif item_type in ["ROW_BOLD", "ROW_REG"]:
        ws_rm.append([val1, val2])
        r = ws_rm.max_row
        ws_rm.row_dimensions[r].height = 20.0
        c1 = ws_rm.cell(row=r, column=1)
        c2 = ws_rm.cell(row=r, column=2)
        c1.font = font_label_bold if item_type == "ROW_BOLD" else font_label_regular
        c2.font = font_val_regular
        c1.alignment = Alignment(horizontal='left', vertical='center')
        c2.alignment = Alignment(horizontal='left', vertical='center')
        c1.border = thin_border
        c2.border = thin_border

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully reformatted Readme sheet in 05_HUBS/financial-hub-roadmap.xlsx to match 05_HUBS/vehicle-hub-roadmap.xlsx 100%!")
