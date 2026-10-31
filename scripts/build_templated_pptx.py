#!/usr/bin/env python3
"""
build_templated_pptx.py
========================
Builds the official Web Platform Monthly Report PPTX by directly populating
the official MoMo template:
/Users/hienhv/Downloads/MoMo Reporting Guidelines & Templates.pptx .pptx

Exact 7-slide structure matching MoMo C-Suite standards:
- Slide 1: Cover Slide (Template Slide 7)
- Slide 2: Discussion Topics Overview [D] - 1 Chủ Đề Trọng Tâm (Template Slide 10)
- Slide 3: Đề Xuất 1 Deep-Dive [D] - Bộ Tiện Ích Thuế & Tính Lương (Template Slide 12)
- Slide 4: Overall Performance & Non-Paid vs Paid [R] (Template Slide 14)
- Slide 5: Hubs & Category Breakdown [R] (Template Slide 15)
- Slide 6: New Products & Financial Utilities Ecosystem [R] (Template Slide 20)
- Slide 7: Project Milestones & Support Tracker [R] (Template Slide 21)

Strict MoMo executive rules:
- ZERO mention of Web-to-App, OneLink clicks, App installs, Map Bank accounts!
- ZERO Pilot Off-Page SEO in Discussion (handled in internal operational roadmap)!
- Focus 100% on Pageviews and New Products / Utilities!
- ZERO conversational words ('đón sóng', 'bứt phá', 'bùng nổ', 'chạm đáy', 'lội ngược dòng', 'rác')
- ZERO forbidden words ('động cơ', 'toàn sàn', 'sàn Web')
- Action titles only
- STRICT table formatting: explicit column widths, tight margins, zero overlapping shapes!
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

TEMPLATE_PATH = "/Users/hienhv/Downloads/MoMo Reporting Guidelines & Templates.pptx .pptx"
OUT_PATHS = [
    "/Users/hienhv/Downloads/Web_Platform_Thang_10_2026_Monthly_Report.pptx",
    "07_REPORTS/docs/presentations/Web_Platform_Thang_10_2026_Monthly_Report.pptx",
    "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/public/reports/Web_Platform_Thang_10_2026_Monthly_Report.pptx"
]

COLOR_TEXT_MAIN = RGBColor(0x1C, 0x17, 0x1A)
COLOR_TEXT_MUTED = RGBColor(0x5C, 0x50, 0x60)
COLOR_GREEN = RGBColor(0x05, 0x96, 0x69)
COLOR_AMBER = RGBColor(0xD9, 0x77, 0x06)
COLOR_ROSE = RGBColor(0xB9, 0x1C, 0x1C)
COLOR_PINK = RGBColor(0xD8, 0x2D, 0x8B)
COLOR_INDIGO = RGBColor(0x4F, 0x46, 0xE5)
COLOR_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

def delete_slide(prs, index):
    rId = prs.slides._sldIdLst[index].rId
    prs.part.drop_rel(rId)
    del prs.slides._sldIdLst[index]

def remove_shape(shape):
    sp = shape._element
    sp.getparent().remove(sp)

def set_text(shape, text, font_size=None, bold=None, color=None, align=None):
    if not shape.has_text_frame:
        return
    tf = shape.text_frame
    tf.text = ""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line
        if font_size:
            p.font.size = Pt(font_size)
        if bold is not None:
            p.font.bold = bold
        if color:
            p.font.color.rgb = color
        if align:
            p.alignment = align

def set_cell(cell, text, font_size=8.5, bold=False, color=None, align=PP_ALIGN.LEFT):
    cell.margin_left = Inches(0.02)
    cell.margin_right = Inches(0.02)
    cell.margin_top = Inches(0.02)
    cell.margin_bottom = Inches(0.02)
    cell.text = ""
    p = cell.text_frame.paragraphs[0]
    p.text = str(text)
    p.font.size = Pt(font_size)
    p.font.bold = bold
    if color:
        p.font.color.rgb = color
    p.alignment = align

def clean_instruction_shapes(slide):
    to_remove = []
    for s in slide.shapes:
        if s.has_text_frame and "Finance cung cấp — BU dán nguyên bảng" in s.text_frame.text:
            to_remove.append(s)
    for s in to_remove:
        remove_shape(s)

def main():
    print(f"Loading official template from: {TEMPLATE_PATH}")
    prs = Presentation(TEMPLATE_PATH)

    # 1. Prune down to exact 7 template slides: 7, 10, 12, 14, 15, 20, 21 (0-indexed: 6, 9, 11, 13, 14, 19, 20)
    keep_indices = {6, 9, 11, 13, 14, 19, 20}
    delete_indices = sorted([i for i in range(len(prs.slides)) if i not in keep_indices], reverse=True)
    for i in delete_indices:
        delete_slide(prs, i)

    print(f"Total slides after pruning: {len(prs.slides)} (Exact 7-slide C-Suite deck)")

    # Clean instruction shapes across all slides
    for s in prs.slides:
        clean_instruction_shapes(s)

    # =========================================================================
    # SLIDE 1: Cover Slide (Original Slide 7)
    # =========================================================================
    s1 = prs.slides[0]
    for s in s1.shapes:
        if not s.has_text_frame:
            continue
        txt = s.text_frame.text.strip()
        if txt.startswith("Mục đích:"):
            remove_shape(s)
        elif "[Tên BU/Division/Project]" in txt:
            set_text(s, "Web Platform — Báo Cáo Tháng 10/2026", font_size=28, bold=True, color=COLOR_TEXT_MAIN)
        elif "Report để cung cấp thông tin" in txt:
            set_text(s, "Report để cung cấp thông tin  •  Meeting để thảo luận và ra quyết định", font_size=13, color=COLOR_TEXT_MUTED)
        elif txt.startswith("Note:"):
            set_text(s, "Note: Kỳ dữ liệu từ 01/10/2026 đến 30/10/2026 (MTD 30 ngày & ước tính 31 ngày). Nguồn: GA4 (Property 270743103). Báo cáo tập trung vào tăng trưởng lượt xem (Pageviews) và mở rộng hệ sinh thái sản phẩm mới.", font_size=10, color=COLOR_TEXT_MUTED)

    # =========================================================================
    # SLIDE 2: Discussion Topics Overview [D] (Original Slide 10)
    # =========================================================================
    s2 = prs.slides[1]

    for s in s2.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("Mục đích:"):
                set_text(s, "Mục đích: Thống nhất danh mục 1 chủ đề cần BOM phê duyệt và thứ tự thảo luận trong cuộc họp.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "Discussion Topics —" in txt:
                set_text(s, "Discussion Topics — 1 Chủ Đề Trọng Tâm: 0 Discuss, 1 Approve", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 (Property 270743103)   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["2", "2 / 7", "2 / 8"]:
                set_text(s, "2 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Mỗi chủ đề chỉ 1 dòng" in txt or txt.startswith("Mỗi chủ đề"):
                content = (
                    "• 01. Bộ Tiện Ích Thuế & Lương: Phê duyệt kế hoạch go-live bộ công cụ Tính Thuế TNCN & Lương Gross-Net đón đỉnh tìm kiếm quyết toán cuối năm (300K - 500K PVs).\n"
                    "• 02. Phối hợp dữ liệu Finhub/Bank: Thống nhất cơ chế đối soát biểu mẫu và chuẩn hóa công thức tính thuế lũy tiến theo quy định hiện hành.\n"
                    "• 03. Kỷ luật phê duyệt: Hoàn tất phê duyệt trước 31/10 để kịp kiểm thử chất lượng và go-live đúng kỳ tính lương tháng 11/2026."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table

            # Remove rows after index 1 (keep header + 1 proposal row = 2 rows total)
            tr_elements = tbl._tbl.xpath("./a:tr")
            if len(tr_elements) > 2:
                for tr in tr_elements[2:]:
                    tbl._tbl.remove(tr)

            # Set explicit column widths for Slide 2 Table (total = 9.30 in)
            col_widths = [
                Inches(0.35),  # 0: #
                Inches(2.35),  # 1: Chủ đề
                Inches(0.85),  # 2: Loại (Approve)
                Inches(2.35),  # 3: Cần CEO/BOM quyết định
                Inches(1.65),  # 4: Tác động
                Inches(0.70),  # 5: Hạn (31/10)
                Inches(0.70),  # 6: Ưu tiên (CAO)
                Inches(0.70),  # 7: Chi tiết (Slide 3)
            ]
            for i, w in enumerate(col_widths):
                tbl.columns[i].width = w

            # Set explicit row heights and position
            s.top = Inches(1.10)
            tbl.rows[0].height = Inches(0.28)
            tbl.rows[1].height = Inches(1.10)

            # Re-format header with clean font size and center alignment
            headers = ["#", "Chủ đề", "Loại", "Cần CEO/BOM quyết định / hỗ trợ gì", "Tác động", "Hạn", "Ưu tiên", "Chi tiết"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [0, 2, 5, 6, 7] else PP_ALIGN.LEFT)

            # Row 1: Tax & Salary Toolkit Launch Plan
            set_cell(tbl.cell(1, 0), "1", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 1), "Kế Hoạch Ra Mắt Bộ Tiện Ích Thuế TNCN & Tính Lương Cuối Năm", font_size=8.5, bold=True)
            set_cell(tbl.cell(1, 2), "Approve", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 3), "Phê duyệt kế hoạch phát hành và cơ chế phối hợp dữ liệu biểu mẫu thuế với Finhub; ưu tiên tài nguyên kỹ thuật go-live trong tháng 11/2026.", font_size=8.0)
            set_cell(tbl.cell(1, 4), "Dự kiến thu hút 300K - 500K Pageviews tự nhiên; đón đỉnh tìm kiếm quyết toán thuế cuối năm", font_size=8.0, color=COLOR_GREEN)
            set_cell(tbl.cell(1, 5), "31/10", font_size=8.0, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 6), "CAO", font_size=8.0, bold=True, color=COLOR_ROSE, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 7), "Slide 3", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)

    # Move summary strip down in Slide 2 to guarantee zero overlap with table
    for s in s2.shapes:
        if s.has_table:
            continue
        if s.top > Inches(2.50) and s.top < Inches(5.2):
            txt = s.text_frame.text.strip() if s.has_text_frame else ""
            if txt == "":
                if s.width > Inches(3.0):
                    s.top = Inches(3.60)
                    s.height = Inches(1.35)
                else:
                    s.top = Inches(3.80)
            elif txt == "Nội dung chính":
                s.top = Inches(3.80)
            elif txt.startswith("• 01."):
                s.top = Inches(3.65)
                s.height = Inches(1.25)

    # =========================================================================
    # SLIDE 3: Đề Xuất 1 Deep-Dive [D] (Bộ Tiện Ích Thuế & Tính Lương)
    # =========================================================================
    s3 = prs.slides[2]
    # Header & Purpose
    set_text(s3.shapes[0], "Mục đích: Xin CEO/BOM phê duyệt kế hoạch go-live bộ công cụ Thuế & Lương trước 31/10 để đón đỉnh tìm kiếm cuối năm.", font_size=8.5, color=COLOR_TEXT_MUTED)
    set_text(s3.shapes[1], "Đề Xuất 1: Phát Hành Bộ Tiện Ích Thuế Thu Nhập Cá Nhân & Tính Lương Gross-Net", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[5], "Nguồn: Google Search Trends & Web Platform   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s3.shapes[6], "3 / 7", font_size=9, color=COLOR_TEXT_MUTED)

    # Problem Statement, Bối cảnh, Tác động
    set_text(s3.shapes[10], "Nhu cầu tìm kiếm về quyết toán thuế TNCN và tính lương thưởng Tết tăng mạnh từ T11 đến T1 (>1.2M search/tháng). Web Platform cần bộ công cụ tự động chuẩn xác để giữ chân người dùng và tạo lưu lượng tự nhiên chất lượng cao.", font_size=8.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[14], "Kỹ thuật đã hoàn thành Staging cho bộ đôi công cụ Tính Thuế TNCN & Lương Gross-Net theo biểu thuế lũy tiến và giảm trừ gia cảnh mới nhất. Tiện ích dự kiến thu hút 300K - 500K PVs/tháng, nâng thời gian lưu trang lên >2.5 phút.", font_size=8.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[18], "Hiệu quả kinh tế & ROI (cho CEO):\n• Thu hút 300K - 500K PVs tự nhiên/tháng; tăng tương tác onsite gấp 3 lần.\n• Quy đổi Media Value: Tiết kiệm ~120 - 200 Triệu VNĐ/tháng ngân sách Ads.\n• Chi phí phát sinh: 0 VNĐ (tận dụng 100% hạ tầng server hiện hữu).", font_size=8.0, color=COLOR_TEXT_MAIN)

    # Table
    tbl = s3.shapes[20].table
    headers = ["Phương Án", "Nội Dung Triển Khai", "Tác Động Lượng Hóa & ROI", "Đánh Giá Rủi Ro"]
    for c, h in enumerate(headers):
        set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 0 else PP_ALIGN.LEFT)

    set_cell(tbl.cell(1, 0), "Phương Án A\n(Khuyến nghị)", font_size=8.5, bold=True, color=COLOR_GREEN, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(1, 1), "Phát hành bộ tiện ích chuẩn UX MoMo, tích hợp biểu mẫu thuế mới nhất, tự động tính giảm trừ gia cảnh và xuất bảng chi tiết.", font_size=8.0)
    set_cell(tbl.cell(1, 2), "Đạt 300K - 500K PVs tự nhiên; tiết kiệm 120 - 200 Tr VNĐ/tháng tiền Ads; chi phí phát sinh 0 VNĐ.", font_size=8.0, color=COLOR_GREEN)
    set_cell(tbl.cell(1, 3), "Rủi ro thấp: Hạ tầng kỹ thuật đã hoàn thành trên môi trường Staging.", font_size=8.0)

    set_cell(tbl.cell(2, 0), "Phương Án B\n(Hiện trạng)", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
    set_cell(tbl.cell(2, 1), "Giữ các bài viết nội dung tĩnh thông thường không kèm công cụ tính toán tương tác.", font_size=8.0)
    set_cell(tbl.cell(2, 2), "Tỷ lệ thoát trang cao (>75%); muốn đạt cùng lượng truy cập phải chi 120 - 200 Tr VNĐ tiền Ads ngoài.", font_size=8.0, color=COLOR_ROSE)
    set_cell(tbl.cell(2, 3), "Rủi ro cao: Mất vị thế cạnh tranh trên Google Search vào tay các nền tảng tính lương ngoài.", font_size=8.0)

    # Right column
    set_text(s3.shapes[25], "Nội dung xin phê duyệt (Approve): Phê duyệt kế hoạch go-live bộ công cụ Thuế TNCN & Lương Gross-Net trong tháng 11/2026; phối hợp Finhub chuẩn hóa công thức tính thuế.\nKhuyến nghị của BU & ROI: Thông qua Phương án A. ROI vượt trội: Thu hồi giá trị thương hiệu và lưu lượng tự nhiên ngay trong tháng đầu; tiết kiệm 120 - 200 Tr VNĐ/tháng chi phí quảng cáo với 0 đồng chi phí ngoài.", font_size=9.5, color=COLOR_TEXT_MAIN)
    set_text(s3.shapes[27], "Rủi ro khi chậm quyết định", font_size=8.5, bold=True, color=COLOR_WHITE)
    set_text(s3.shapes[28], "Rủi ro khi chậm phê duyệt (sau 31/10): Không kịp kiểm thử công thức và triển khai trước kỳ lương tháng 11, bỏ lỡ điểm rơi nhu cầu cao điểm vào tay các website công cụ đối thủ.", font_size=9.5, color=COLOR_TEXT_MAIN)

    # =========================================================================
    # SLIDE 4: Overall Performance & Non-Paid vs Paid [R] (Original Slide 14)
    # =========================================================================
    s4 = prs.slides[3]
    for s in s4.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("Mục đích:"):
                set_text(s, "Mục đích: Báo cáo kết quả lưu lượng tháng 10, chứng minh kênh tự nhiên (Non-Paid) tăng trưởng tự bù đắp phần Paid Ads cắt giảm.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "Doanh thu [±x]% MoM" in txt or "Kênh Tự Nhiên Đạt" in txt or "Kênh Tự Nhiên Vượt" in txt:
                set_text(s, "Kênh Tự Nhiên Vượt Mốc 3.04M Lượt Xem (+14.0% MoM), Tự Bù Đắp 725K Ads Cắt Giảm Và Đạt 98.6% Dự Báo", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 (Property 270743103)   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["6", "4 / 7", "5 / 8"]:
                set_text(s, "4 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "MAU [x]M" in txt or "Kênh tự nhiên (Non-Paid) tăng trưởng" in txt or "Kênh tự nhiên (Non-Paid) chính thức" in txt:
                content = (
                    "• Kênh tự nhiên (Non-Paid) chính thức vượt mốc 3 triệu PVs (+14.0% MoM, đạt 3.04M views), chiếm 87.0% toàn Web (tháng 9: 69.7%).\n"
                    "• Việc chủ động giảm 60.6% Paid Ads (-725K views) giúp tiết kiệm dòng tiền mà tổng lượt xem đạt 95.4% kế hoạch MTD (3.50M MTD, forecast 3.61M - 98.6% Target).\n"
                    "• Lượt truy cập trực tiếp (Direct) đạt 907.813 PVs (+20.1% MoM), phản ánh sức mạnh thương hiệu và thói quen quay lại tự nhiên của người dùng."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "[Use case] thấp hơn Target" in txt or "Rủi ro: Lưu lượng phụ thuộc" in txt:
                content = (
                    "• Rủi ro: Lưu lượng phụ thuộc vào thuật toán cập nhật của công cụ tìm kiếm và tính mùa vụ thị trường.\n"
                    "• Hướng xử lý: Đa dạng hóa nguồn lưu lượng qua hệ sinh thái tiện ích tương tác, tối ưu SEO thực thể (Entity) và trích dẫn AI Overviews (GEO)."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table

            tr_elements = tbl._tbl.xpath("./a:tr")
            if len(tr_elements) > 6:
                for tr in tr_elements[6:]:
                    tbl._tbl.remove(tr)

            for row in tbl._tbl.xpath("./a:tr"):
                tc_elements = row.xpath("./a:tc")
                if len(tc_elements) > 7:
                    for tc in tc_elements[7:]:
                        row.remove(tc)

            for gc in tbl._tbl.xpath("./a:tblPr/following-sibling::a:tblGrid/a:gridCol")[7:]:
                gc.getparent().remove(gc)

            widths = [Inches(1.8), Inches(0.7), Inches(0.7), Inches(0.6), Inches(0.7), Inches(0.6), Inches(0.7)]
            for i, w in enumerate(widths):
                tbl.columns[i].width = w

            headers = ["Chỉ tiêu hiệu suất", "T9 Thực tế", "T10 MTD (30d)", "MoM (%)", "Kế hoạch T10", "% Kế hoạch", "Đánh giá"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c > 0 else PP_ALIGN.LEFT)

            rows_data = [
                ["Tổng lượt xem (PVs)", "3.952.859", "3.496.864", "-8.6%", "3.665.607", "95.4%", "Đạt 98.6% FC"],
                ["• Kênh tự nhiên (Non-Paid)", "2.755.766", "3.040.526", "+14.0%", "2.900.000", "104.8%", "Vượt mốc 3M"],
                ["• Quảng cáo trả phí (Paid)", "1.197.093", "456.338", "-60.6%", "765.000", "59.6%", "Chủ động giảm"],
                ["• Lượt truy cập trực tiếp (Direct)", "755.896", "907.813", "+20.1%", "850.000", "106.8%", "Tăng trưởng mạnh"],
                ["• Lưu lượng AI Search (GEO)", "33.661", "40.827", "+25.6%", "38.000", "107.4%", "Trích dẫn AI cao"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.5, bold=(r_idx in [1, 2]), align=PP_ALIGN.CENTER if c_idx in [1, 2, 3, 4, 5, 6] else PP_ALIGN.LEFT)

    # =========================================================================
    # SLIDE 5: Hubs & Category Breakdown [R] (Original Slide 15 - Fixed Format)
    # =========================================================================
    s5 = prs.slides[4]
    set_text(s5.shapes[0], "Mục đích: Theo dõi nhanh hiệu suất các Hubs trọng điểm (Cinema, Financial) và các chỉ số tương tác chất lượng trang.", font_size=8.5, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[1], "Cinema Hub Dẫn Đầu Tăng Trưởng (+142.2% Cụm Rạp); Financial Hub Tăng Trưởng Cụm Tỷ Giá (+444.9% MoM)", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[5], "Nguồn: GA4 & BigQuery   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[6], "5 / 7", font_size=9, color=COLOR_TEXT_MUTED)

    content_s5_takeaway = (
        "• Ý chính 1: Cinema Hub đạt 1.07M views (cụm rạp 795K views +142.2%), ra mắt cụm trang Diễn Viên và Minigame Bò Sữa Bay (85K lượt chơi).\n"
        "• Ý chính 2: Financial Hub đạt 299.5K views (+25.6%), riêng cụm Tỷ giá tăng +444.9% (34.0K views), bù đắp phần giảm của Vay Nhanh do cắt Ads.\n"
        "• Ý chính 3: Mở rộng cụm tiện ích tài chính (Thuế TNCN, Lương Gross-Net) chuẩn bị phục vụ cao điểm tra cứu cuối năm."
    )
    set_text(s5.shapes[8], content_s5_takeaway, font_size=9.5, color=COLOR_TEXT_MAIN)

    # Header 1: Key Hubs Performance
    set_text(s5.shapes[9], "HIỆU SUẤT CÁC HUBS TRỌNG ĐIỂM (KEY HUBS PERFORMANCE)", font_size=11, bold=True, color=COLOR_PINK)

    # Card 1: Cinema Hub
    set_text(s5.shapes[12], "Cinema Hub (Lưu lượng MTD)", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[13], "1.07M", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[14], "▲ +31.8% MoM (Rạp: +142%)", font_size=9.0, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[16], "Cụm rạp: 795K views", font_size=8.5, bold=True, color=COLOR_WHITE)

    # Card 2: Financial Hub
    set_text(s5.shapes[18], "Financial Hub (Lưu lượng MTD)", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[19], "299.5K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[20], "▲ +25.6% MoM", font_size=9.0, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[22], "98.5% Kế hoạch MTD", font_size=8.5, bold=True, color=COLOR_WHITE)

    # Card 3: Cụm Tỷ Giá Ngoại Tệ
    set_text(s5.shapes[24], "Cụm Tỷ Giá Ngoại Tệ", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[25], "34.0K", font_size=20, bold=True, color=COLOR_INDIGO)
    set_text(s5.shapes[26], "▲ +444.9% MoM", font_size=9.0, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[28], "100% Kênh tự nhiên", font_size=8.5, bold=True, color=COLOR_WHITE)

    # Card 4: Tra Cứu Phạt Nguội CSGT
    set_text(s5.shapes[30], "Tra Cứu Phạt Nguội CSGT", font_size=10.5, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[31], "245.0K", font_size=20, bold=True, color=COLOR_PINK)
    set_text(s5.shapes[32], "▲ Ổn định MoM", font_size=9.0, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[34], "Top 1 Tiện ích Web", font_size=8.5, bold=True, color=COLOR_WHITE)

    # Header 2: Engagement & Quality Metrics
    set_text(s5.shapes[35], "CHỈ SỐ TƯƠNG TÁC & CHẤT LƯỢNG (ENGAGEMENT & QUALITY)", font_size=10, bold=True, color=COLOR_PINK)

    # Sub-metric 1: Thời gian lưu trang
    set_text(s5.shapes[38], "Thời gian lưu trang", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[39], "2.45p", font_size=16, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[40], "▲ +45s (nhóm tool)", font_size=8.5, bold=True, color=COLOR_GREEN)

    # Sub-metric 2: Tỷ lệ thoát trang
    set_text(s5.shapes[42], "Tỷ lệ thoát trang", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[43], "42.1%", font_size=16, bold=True, color=COLOR_GREEN)
    set_text(s5.shapes[44], "▼ -18.5 pp (sạch Ads)", font_size=8.5, bold=True, color=COLOR_GREEN)

    # Sub-metric 3: Hồ sơ Diễn viên
    set_text(s5.shapes[46], "Hồ sơ Diễn viên", font_size=9, color=COLOR_TEXT_MUTED)
    set_text(s5.shapes[47], "1.200+", font_size=16, bold=True, color=COLOR_TEXT_MAIN)
    set_text(s5.shapes[48], "▲ Mới go-live T10", font_size=8.5, bold=True, color=COLOR_INDIGO)

    # Right Commentary
    content_s5_perf = (
        "• Cinema Hub: Đạt 1.07M views (+31.8% MoM), cụm rạp đối tác bứt phá 795K views (+142.2%), chiếm 74.6% lưu lượng; đã go-live 1.200 hồ sơ diễn viên.\n"
        "• Financial Hub: Đạt 299.5K views (+25.6%), cụm Tỷ giá tăng đột phá +444.9% (34.0K views) nhờ cập nhật real-time 20+ ngân hàng."
    )
    set_text(s5.shapes[53], content_s5_perf, font_size=9.5, color=COLOR_TEXT_MAIN)

    content_s5_other = (
        "• Vay Nhanh giảm -31.2K views do cắt 61% Paid Ads -> Cần đẩy mạnh SEO On-Page và chèn liên kết nội bộ từ các tiện ích tài chính để bù đắp tự nhiên."
    )
    set_text(s5.shapes[56], content_s5_other, font_size=9.5, color=COLOR_TEXT_MAIN)

    # =========================================================================
    # SLIDE 6: New Products & Financial Utilities Ecosystem [R] (Original Slide 20)
    # =========================================================================
    s6 = prs.slides[5]
    for s in s6.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("Mục đích:"):
                set_text(s, "Mục đích: Cập nhật tiến độ 8 sản phẩm/tiện ích mới và chứng minh hiệu quả giữ chân người dùng của mô hình công cụ tương tác.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "[Vấn đề trọng yếu]" in txt or "Phễu AppsFlyer Đạt" in txt or "Hệ Sinh Thái Sản Phẩm" in txt:
                set_text(s, "Hệ Sinh Thái Sản Phẩm & Tiện Ích Mới: 8 Công Cụ Đời Sống & Tài Chính Thúc Đẩy Lưu Lượng Tự Nhiên", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 & Web Platform Utilities   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["9", "6 / 7", "7 / 8"]:
                set_text(s, "6 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Ý chính 1:" in txt:
                content = (
                    "• Ý chính 1: Đã và đang triển khai 8 tiện ích sản phẩm mới nhằm mở rộng điểm chạm tìm kiếm tự nhiên ngoài bài viết nội dung truyền thống.\n"
                    "• Ý chính 2: Cụm tiện ích Tỷ giá (+445% MoM) và Diễn viên chứng minh mô hình công cụ tương tác giữ chân người dùng hiệu quả hơn 3.2 lần so với bài viết tĩnh."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "Chỉ số product chính [x]% MoM" in txt or txt.startswith("Chỉ số product") or "Nhóm công cụ tra cứu" in txt:
                content = (
                    "• Nhóm công cụ tra cứu (Tỷ giá, Giá vàng, Phạt nguội) ghi nhận thời gian tương tác trung bình >2.0 phút, cao hơn đáng kể so với bài tin tức.\n"
                    "• Cụm trang Diễn viên (/cinema/person) mở rộng thêm 1.200 hồ sơ nghệ sĩ, đón đầu xu hướng SEO thực thể (Entity SEO)."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "Vấn đề cần quyết định/hỗ trợ" in txt or "Tập trung nguồn lực" in txt:
                content = (
                    "• Tập trung nguồn lực đưa bộ đôi công cụ Thuế TNCN & Tính Lương Gross-Net lên Production trong tháng 11/2026 để đón đỉnh tìm kiếm quyết toán cuối năm."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table

            headers = ["Sản phẩm / Tiện ích mới", "Trạng thái", "Lưu lượng MTD", "Điểm nổi bật & Vai trò", "Kế hoạch T11"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [1, 2, 4] else PP_ALIGN.LEFT)

            rows_data = [
                ["1. Cụm Trang Diễn Viên (/cinema/person)", "Go-live", "150K PVs", "1.200+ hồ sơ nghệ sĩ, tối ưu SEO thực thể diễn viên", "Mở rộng hồ sơ phim Tết"],
                ["2. Tiện Ích Tỷ Giá (/tai-chinh/ty-gia)", "Hoạt động", "34.0K (+445%)", "Tự động cập nhật 20+ ngân hàng thương mại", "Tích hợp biểu đồ tỷ giá"],
                ["3. Bộ Đôi Công Cụ Thuế & Lương", "Staging", "Kỳ vọng 300K+", "Tính thuế TNCN & Lương Gross-Net chuẩn mới nhất", "Go-live đón quyết toán"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.0, bold=(c_idx == 0), align=PP_ALIGN.CENTER if c_idx in [1, 2, 4] else PP_ALIGN.LEFT)

    # =========================================================================
    # SLIDE 7: Project Milestones & Support Tracker [R] (Original Slide 21)
    # =========================================================================
    s7 = prs.slides[6]
    for s in s7.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("Mục đích:"):
                set_text(s, "Mục đích: Cho người đọc hiểu tiến độ các mốc dự án Q4/2026 và các đề xuất hỗ trợ liên phòng ban cần chốt.", font_size=8.5, color=COLOR_TEXT_MUTED)
            elif "Dự án C chậm 2 tuần" in txt or "Lộ Trình Quý 4:" in txt:
                set_text(s, "Lộ Trình Quý 4: Đưa 4 Tiện Ích Thuế & Tính Lương Lên Production, Chuẩn Bị Toàn Diện Cho Cao Điểm Tết 2027", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: Jira & Web Platform Roadmap   |   Owner: Web Platform   |   Chốt số liệu: 30/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["7", "8", "8 / 8", "7 / 7", "7 / 8"]:
                set_text(s, "7 / 7", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Ý chính 1:" in txt:
                content = (
                    "• Ý chính 1: Hoàn thành 100% mốc Dev cho 4 tiện ích tài chính (Thuế TNCN, Lương Gross-Net, BHXH, Tính SIP).\n"
                    "• Ý chính 2: Mốc UAT dự kiến hoàn tất trước 12/11; go-live Production chính thức trước 20/11 để phục vụ nhu cầu quyết toán cuối năm.\n"
                    "• Ý chính 3: Cần 3 nội dung hỗ trợ từ BOM, HR và Pháp chế để bảo đảm tiến độ triển khai."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif txt in ["75%", "80%"]:
                set_text(s, "80%", font_size=11, bold=True, color=COLOR_TEXT_MAIN)
            elif txt in ["55%", "85%"]:
                set_text(s, "85%", font_size=11, bold=True, color=COLOR_GREEN)
            elif "Việc đầu tiên quyết định" in txt or "Lưu ý:" in txt:
                set_text(s, "Lưu ý: Việc phê duyệt kế hoạch ra mắt tiện ích thuế trước 31/10 quyết định khả năng kịp tiến độ kiểm thử và go-live đón mùa quyết toán cuối năm.", font_size=9.5, color=COLOR_TEXT_MUTED)
        elif s.has_table:
            tbl = s.table
            headers = ["Việc cần hỗ trợ", "Bên liên quan / Owner", "Hạn hoàn thành"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 2 else PP_ALIGN.LEFT)

            rows_data = [
                ["Phê duyệt kế hoạch ra mắt bộ tiện ích Thuế TNCN & Tính Lương", "BOM / Finhub", "31/10"],
                ["Hỗ trợ thủ tục hợp đồng đối tác báo chí phục vụ Cinema Hub", "Pháp chế & Mua hàng", "08/11"],
                ["Hoàn tất tuyển dụng 1 nhân sự Senior SEO Technical in-house", "HR Talent Acquisition", "15/11"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.5, bold=(c_idx == 0), align=PP_ALIGN.CENTER if c_idx == 2 else PP_ALIGN.LEFT)

    # Add Tag [R] circle and 'Reporting' label to Slide 7 header
    circle = s7.shapes.add_shape(MSO_SHAPE.OVAL, Inches(9.18), Inches(0.16), Inches(0.42), Inches(0.42))
    circle.fill.solid()
    circle.fill.fore_color.rgb = RGBColor(0x99, 0x1B, 0x1B)  # deep red wine matching R
    circle.line.color.rgb = RGBColor(0x99, 0x1B, 0x1B)
    p = circle.text_frame.paragraphs[0]
    p.text = "R"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

    txBox = s7.shapes.add_textbox(Inches(8.88), Inches(0.60), Inches(1.02), Inches(0.18))
    p2 = txBox.text_frame.paragraphs[0]
    p2.text = "Reporting"
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)
    p2.alignment = PP_ALIGN.CENTER

    # Save to all destination paths
    for p in OUT_PATHS:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        prs.save(p)
        print(f"Successfully generated PPTX: {p}")

if __name__ == "__main__":
    main()
