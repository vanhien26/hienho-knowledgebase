#!/usr/bin/env python3
"""
build_templated_pptx.py
========================
Builds the official Web Platform Monthly Report PPTX by directly cloning
and populating the official MoMo template:
/Users/hienhv/Downloads/MoMo Reporting Guidelines & Templates.pptx .pptx

Exact 8-slide structure matching MoMo C-Suite standards:
- Slide 1: Cover Slide (Template Slide 7)
- Slide 2: Discussion Topics Overview [D] (Template Slide 10)
- Slide 3: Đề Xuất 1 Deep-Dive [D] - Tái Cấu Trúc Ngân Sách Ads & Nghiệm Thu Map Bank (Template Slide 12)
- Slide 4: Đề Xuất 2 Deep-Dive [D] - Gói Pilot SEO Cinema Hub 125 Tr VNĐ (Template Slide 12 Clone)
- Slide 5: Overall Performance & Non-Paid vs Paid [R] (Template Slide 14)
- Slide 6: Hubs & Category Breakdown [R] (Template Slide 15)
- Slide 7: Product / OneLink W2A Funnel & Utilities [R] (Template Slide 20)
- Slide 8: Project Milestones & Support Tracker [R] (Template Slide 21)

Strict MoMo executive rules:
- ZERO conversational words ('đón sóng', 'bứt phá', 'bùng nổ', 'chạm đáy', 'lội ngược dòng', 'rác')
- ZERO forbidden words ('động cơ', 'toàn sàn', 'sàn Web')
- Action titles only
- STRICT table formatting: explicit font sizes (8.5 - 9.5 pt), tight cell margins, zero overlapping shapes!
"""

import os
import copy
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

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

def set_cell(cell, text, font_size=9.0, bold=False, color=None, align=PP_ALIGN.LEFT):
    cell.margin_left = Inches(0.04)
    cell.margin_right = Inches(0.04)
    cell.margin_top = Inches(0.04)
    cell.margin_bottom = Inches(0.04)
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
        if s.has_text_frame and s.text_frame.text.strip().startswith("Mục đích:"):
            to_remove.append(s)
        elif s.has_text_frame and "Finance cung cấp — BU dán nguyên bảng" in s.text_frame.text:
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

    # 2. Duplicate Slide 12 (currently at index 2) to create Slide 4 (Proposal 2)
    slide12 = prs.slides[2]
    new_slide = prs.slides.add_slide(slide12.slide_layout)
    for shape in slide12.shapes:
        new_el = copy.deepcopy(shape._element)
        new_slide.shapes._spTree.append(new_el)

    # Move new_slide from last index to index 3 (right after slide12)
    sldIdLst = prs.slides._sldIdLst
    cloned_sldId = sldIdLst[len(sldIdLst) - 1]
    sldIdLst.remove(cloned_sldId)
    sldIdLst.insert(3, cloned_sldId)

    print(f"Total slides after duplicating Slide 12: {len(prs.slides)}")

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
        if "[Tên BU/Division/Project]" in txt:
            set_text(s, "Web Platform — Báo Cáo Tháng 10/2026", font_size=28, bold=True, color=COLOR_TEXT_MAIN)
        elif "Report để cung cấp thông tin" in txt:
            set_text(s, "Report để cung cấp thông tin  •  Meeting để thảo luận và ra quyết định", font_size=13, color=COLOR_TEXT_MUTED)
        elif txt.startswith("Note:"):
            set_text(s, "Note: Kỳ dữ liệu từ 01/10/2026 đến 28/10/2026 (MTD 28 ngày & ước tính 31 ngày). Nguồn: GA4 (Property 270743103) & AppsFlyer GPD Attribution.", font_size=10, color=COLOR_TEXT_MUTED)

    # =========================================================================
    # SLIDE 2: Discussion Topics Overview [D] (Original Slide 10)
    # =========================================================================
    s2 = prs.slides[1]
    for s in s2.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if "Discussion Topics —" in txt:
                set_text(s, "Discussion Topics — 2 Chủ Đề Trọng Tâm: 0 Discuss, 2 Approve", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 & AppsFlyer   |   Owner: Web Platform   |   Chốt số liệu: 28/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["2", "2 / 7", "2 / 8"]:
                set_text(s, "2 / 8", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Mỗi chủ đề chỉ 1 dòng" in txt or txt.startswith("Mỗi chủ đề"):
                content = (
                    "• 01. Cổng Web-to-App tập trung: Ban hành quy chuẩn bắt buộc mọi luồng tải app trên Web qua gateway /tai-app để gom 100% attribution và đạt 30.000 install Q4.\n"
                    "• 02. Gói Pilot SEO Cinema Hub: Phê duyệt 125 triệu VNĐ (3 tháng) đưa cụm rạp đối tác đạt Top 5.5 Google trước mùa phim Tết 2027.\n"
                    "• 03. Kỷ luật phê duyệt: Hoàn tất phê duyệt trước 05/11/2026 để kịp ký kết hợp đồng đối tác báo chí và hoàn thành tuyển dụng nhân sự in-house."
                )
                set_text(s, content, font_size=10.0, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table

            # Remove rows 4 and 3 to eliminate empty rows that push table into takeaway box!
            tr_elements = tbl._tbl.xpath("./a:tr")
            if len(tr_elements) > 3:
                for tr in tr_elements[3:]:
                    tbl._tbl.remove(tr)

            # Set explicit column widths for Slide 2 Table (total = 9.30 in)
            col_widths = [
                Inches(0.35),  # 0: #
                Inches(2.10),  # 1: Chủ đề
                Inches(0.85),  # 2: Loại (Approve)
                Inches(2.50),  # 3: Cần CEO/BOM quyết định
                Inches(1.45),  # 4: Tác động
                Inches(0.65),  # 5: Hạn (31/10, 05/11)
                Inches(0.65),  # 6: Ưu tiên (CAO)
                Inches(0.75),  # 7: Chi tiết (Slide 3, Slide 4)
            ]
            for i, w in enumerate(col_widths):
                tbl.columns[i].width = w

            # Set explicit row heights: compact and clean
            tbl.rows[0].height = Inches(0.28)
            tbl.rows[1].height = Inches(0.70)
            tbl.rows[2].height = Inches(0.70)
            s.top = Inches(1.10)

            # Re-format header with clean font size and center alignment
            headers = ["#", "Chủ đề", "Loại", "Cần CEO/BOM quyết định / hỗ trợ gì", "Tác động", "Hạn", "Ưu tiên", "Chi tiết"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [0, 2, 5, 6, 7] else PP_ALIGN.LEFT)

            # Row 1: Web-to-App Gateway Standard
            set_cell(tbl.cell(1, 0), "1", font_size=9.0, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 1), "Chuẩn Hóa Cổng Chuyển Đổi Web-to-App (/tai-app) & Đo Lường OneLink", font_size=9.0, bold=True)
            set_cell(tbl.cell(1, 2), "Approve", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 3), "Ban hành quy chuẩn kỹ thuật bắt buộc: Toàn bộ nút bấm, banner tải app trên Web (momo.vn) phải đi qua gateway /tai-app và gắn OneLink chuẩn; không dùng link Store trực tiếp.", font_size=8.5)
            set_cell(tbl.cell(1, 4), "Bảo toàn 100% attribution; duy trì CVR tải app 21.1%; bảo đảm cán đích 30.000 install Q4", font_size=8.5, color=COLOR_GREEN)
            set_cell(tbl.cell(1, 5), "31/10", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 6), "CAO", font_size=8.5, bold=True, color=COLOR_ROSE, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 7), "Slide 3", font_size=8.5, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)

            # Row 2: Cinema Hub SEO Pilot
            set_cell(tbl.cell(2, 0), "2", font_size=9.0, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(2, 1), "Phê Duyệt Gói Pilot Off-Page SEO Cinema Hub (125 Triệu VNĐ)", font_size=9.0, bold=True)
            set_cell(tbl.cell(2, 2), "Approve", font_size=8.0, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(2, 3), "Phê duyệt ngân sách 125 triệu VNĐ (3 tháng), ký trực tiếp mạng lưới đối tác báo chí lớn; giao HR & Pháp chế hỗ trợ thủ tục trước 05/11.", font_size=8.5)
            set_cell(tbl.cell(2, 4), "Đưa cụm rạp đạt Top 5.5 Google và tối ưu thứ hạng AI Search trước Tết 2027", font_size=8.5, color=COLOR_INDIGO)
            set_cell(tbl.cell(2, 5), "05/11", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(2, 6), "CAO", font_size=8.5, bold=True, color=COLOR_ROSE, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(2, 7), "Slide 4", font_size=8.5, bold=True, color=COLOR_PINK, align=PP_ALIGN.CENTER)

    # =========================================================================
    # SLIDE 3: Đề Xuất 1 Deep-Dive [D] (Web-to-App Gateway Standard)
    # =========================================================================
    s3 = prs.slides[2]
    for s in s3.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("[Chủ đề]:") or "Chi Tiết Đề Xuất:" in txt or "Đề Xuất 1:" in txt:
                set_text(s, "Đề Xuất 1: Chuẩn Hóa Cổng Web-to-App (/tai-app) & Quy Chuẩn Đo Lường OneLink Toàn Web", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 & AppsFlyer   |   Owner: Web Platform   |   Chốt số liệu: 28/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["3", "3 / 7", "3 / 8"]:
                set_text(s, "3 / 8", font_size=9, color=COLOR_TEXT_MUTED)
            elif "[Vấn đề là gì" in txt or "Chiến dịch TikTok Ads" in txt or "Nhiều landing page" in txt:
                set_text(s, "Nhiều landing page của các BU và chiến dịch truyền thông vẫn sử dụng link trực tiếp dẫn vào Store hoặc link rút gọn không chuẩn. Hệ quả là đứt gãy luồng Smart Device Routing, thất thoát từ 15% - 25% dữ liệu attribution trên AppsFlyer, và không đo lường được tỷ lệ người dùng liên kết ngân hàng (Map Bank).", font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "[Vì sao xảy ra" in txt or "Tháng 10 chủ động" in txt or "Kỹ sư Platform" in txt:
                set_text(s, "Kỹ sư Platform đã chính thức đưa cổng /tai-app lên Production với công nghệ Smart Routing (tự mở Store theo OS, hiển thị Dynamic QR trên Desktop). Tháng 10 ghi nhận 9.824 lượt cài app qua OneLink (CVR đạt 21.1%). Chuẩn hóa cổng tập trung sẽ bảo đảm Web đóng góp trọn vẹn 30.000 installs trong Quý 4/2026 theo chỉ đạo của CEO anh Tường.", font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "[Revenue / cost" in txt or "Bảo toàn ~40%" in txt or "Bảo toàn 100%" in txt:
                set_text(s, "Bảo toàn 100% dữ liệu attribution chuyển đổi Web-to-App; duy trì tỷ lệ cài đặt app 21.1% và tỷ lệ liên kết ngân hàng 21.09%; hoàn thành chỉ tiêu 30.000 install được BOM giao cho Quý 4/2026.", font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "Discuss / Approve:" in txt or "Khuyến nghị của BU" in txt or "Nội dung xin phê duyệt" in txt:
                set_text(s, "Nội dung xin phê duyệt (Approve): Ban hành quy chuẩn kỹ thuật bắt buộc: Kể từ ngày 01/11/2026, toàn bộ các luồng dẫn tải ứng dụng trên Kênh Web (momo.vn) bắt buộc tích hợp qua Gateway /tai-app và chuẩn tham số OneLink do Web Platform quản lý.\nKhuyến nghị của BU: Chọn Phương án A để chuẩn hóa hạ tầng tăng trưởng.", font_size=10.0, color=COLOR_TEXT_MAIN)
            elif txt == "Nếu không quyết định":
                set_text(s, "Rủi ro khi chậm quyết định", font_size=8.5, bold=True, color=COLOR_WHITE)
            elif "[Hệ quả lượng hóa]" in txt or "Rủi ro khi chậm" in txt or "Lãng phí thêm 50" in txt or "Dữ liệu cài đặt" in txt:
                set_text(s, "Rủi ro khi chậm phê duyệt (sau 31/10): Dữ liệu cài đặt app tiếp tục bị phân mảnh, thất thoát hàng nghìn lượt cài đặt không được ghi nhận cho Kênh Web, đe dọa trực tiếp khả năng nghiệm thu mục tiêu 30.000 install Q4 được BOM giao.", font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table
            headers = ["Phương Án", "Nội Dung Triển Khai", "Tác Động Lượng Hóa", "Đánh Giá Rủi Ro"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 0 else PP_ALIGN.LEFT)

            set_cell(tbl.cell(1, 0), "Phương Án A\n(Khuyến nghị)", font_size=8.5, bold=True, color=COLOR_GREEN, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 1), "Ban hành quy định bắt buộc: 100% điểm chạm kêu gọi cài app trên domain momo.vn phải đi qua gateway /tai-app và cấu hình OneLink chuẩn từ 01/11/2026.", font_size=8.5)
            set_cell(tbl.cell(1, 2), "Gom 100% attribution, kiểm soát CVR toàn phễu đạt 21.1%, bảo đảm cán đích 30.000 install Q4.", font_size=8.5, color=COLOR_GREEN)
            set_cell(tbl.cell(1, 3), "Rủi ro thấp: Hạ tầng /tai-app đã chạy ổn định trên Production.", font_size=8.5)

            set_cell(tbl.cell(2, 0), "Phương Án B\n(Hiện trạng)", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(2, 1), "Tiếp tục cho phép các squad tự do gắn link Store trực tiếp hoặc link phân tán không chuẩn.", font_size=8.5)
            set_cell(tbl.cell(2, 2), "Tiếp tục thất thoát 15% - 25% số liệu cài app, sai lệch báo cáo attribution của công ty.", font_size=8.5, color=COLOR_ROSE)
            set_cell(tbl.cell(2, 3), "Rủi ro cao: Nguy cơ không đạt và không chứng minh được chỉ tiêu 30K install Q4.", font_size=8.5)

    # =========================================================================
    # SLIDE 4: Đề Xuất 2 Deep-Dive [D] (Pilot Off-Page SEO Cinema Hub)
    # =========================================================================
    s4 = prs.slides[3]
    for s in s4.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if txt.startswith("[Chủ đề]:") or "Đề Xuất 1:" in txt or "Đề Xuất 2:" in txt:
                set_text(s, "Đề Xuất 2: Phê Duyệt Gói Pilot Off-Page SEO Cinema Hub (125 Triệu VNĐ / 3 Tháng)", font_size=18, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4, AppsFlyer & BU Cinema   |   Owner: Web Platform   |   Chốt số liệu: 28/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["3", "3 / 8", "4", "4 / 8"]:
                set_text(s, "4 / 8", font_size=9, color=COLOR_TEXT_MUTED)
            elif "[Vấn đề là gì" in txt or "MoMo hiện chiếm" in txt or "Chiến dịch TikTok Ads" in txt:
                set_text(s, "MoMo hiện chiếm 50% thị phần bán vé xem phim toàn quốc nhưng lưu lượng tìm kiếm nội dung review và cụm rạp mới đạt khoảng 20%. Mùa phim Tết 2027 bắt đầu từ tháng 12/2026, cần gia tăng thứ hạng tìm kiếm ngay từ tháng 11/2026.", font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "[Vì sao xảy ra" in txt or "Lưu lượng cụm rạp" in txt or "Tháng 10 chủ động" in txt:
                set_text(s, "Lưu lượng cụm rạp tăng +142.2% MoM (726K views), CVR Map Bank đạt 25.33% nhưng toàn bộ liên kết đều là On-Page tự nhiên, thiếu sức mạnh Backlinks uy tín để giữ Top 5.5 Google Search trước đối thủ.", font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "[Revenue / cost" in txt or "Đưa 18 cụm rạp" in txt or "Bảo toàn ~40%" in txt:
                set_text(s, "Đưa 18 cụm rạp đối tác (Lotte, BHD, Beta, Cinestar) đạt Top 5.5 Google Search; tối ưu trích dẫn AI Overviews (GEO); đóng góp thêm 2.500 - 3.500 Installs mỗi tháng.", font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "Discuss / Approve:" in txt or "Khuyến nghị của BU" in txt or "Nội dung xin phê duyệt" in txt or "Đề nghị CEO/BOM duyệt:" in txt:
                set_text(s, "Nội dung xin phê duyệt (Approve): Ngân sách thử nghiệm 125 triệu VNĐ (3 tháng) cho Cinema Hub; HR hoàn tất tuyển dụng 1 Senior SEO Technical in-house và Pháp chế hỗ trợ thủ tục trước 05/11/2026.\nKhuyến nghị của BU: Chọn Phương án A để xây dựng năng lực in-house.", font_size=10.0, color=COLOR_TEXT_MAIN)
            elif txt == "Nếu không quyết định":
                set_text(s, "Rủi ro khi chậm quyết định", font_size=8.5, bold=True, color=COLOR_WHITE)
            elif "[Hệ quả lượng hóa]" in txt or "Rủi ro khi chậm" in txt or "Bỏ lỡ thời điểm" in txt:
                set_text(s, "Rủi ro khi chậm phê duyệt (sau 05/11): Không kịp thời gian triển khai 4 tuần để đưa các trang cụm rạp lên Top 5.5 Google trước mùa phim Tết 2027 (bắt đầu từ tháng 12/2026), làm mất thị phần bán vé vào tay đối thủ.", font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table
            headers = ["Phương Án", "Nội Dung Triển Khai", "Chi Phí & Lợi Ích", "Đánh Giá Rủi Ro"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 0 else PP_ALIGN.LEFT)

            set_cell(tbl.cell(1, 0), "Phương Án A\n(Khuyến nghị)", font_size=8.5, bold=True, color=COLOR_GREEN, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(1, 1), "Ký trực tiếp mạng lưới đối tác báo chí lớn; in-house kiểm soát chất lượng nội dung E-E-A-T và chuẩn SEO Entity.", font_size=8.5)
            set_cell(tbl.cell(1, 2), "125 Tr VNĐ (tiết kiệm 50 - 75 Tr so với thuê ngoài). Đưa cụm rạp đạt Top 5.5 Google.", font_size=8.5, color=COLOR_GREEN)
            set_cell(tbl.cell(1, 3), "Kiểm soát 100% chất lượng bài viết và an toàn thương hiệu.", font_size=8.5)

            set_cell(tbl.cell(2, 0), "Phương Án B\n(Agency ngoài)", font_size=8.5, bold=True, align=PP_ALIGN.CENTER)
            set_cell(tbl.cell(2, 1), "Thuê ngoài Agency trung gian triển khai trọn gói.", font_size=8.5)
            set_cell(tbl.cell(2, 2), "Chi phí cao: 180 - 200 Tr VNĐ; chất lượng liên kết không đồng đều.", font_size=8.5, color=COLOR_ROSE)
            set_cell(tbl.cell(2, 3), "Rủi ro khó kiểm soát bài đăng và thuật toán Google phạt.", font_size=8.5)

    # =========================================================================
    # SLIDE 5: Overall Performance & Non-Paid vs Paid [R] (Original Slide 14)
    # =========================================================================
    s5 = prs.slides[4]
    for s in s5.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if "Doanh thu [±x]% MoM" in txt or "Kênh Tự Nhiên Đạt" in txt:
                set_text(s, "Kênh Tự Nhiên Đạt 2.87M Lượt Xem (+15.1% MoM), Tự Bù Đắp 733K Ads Cắt Giảm Và Đạt 99.2% Kế Hoạch", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 (Property 270743103) & AppsFlyer   |   Owner: Web Platform   |   Chốt số liệu: 28/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["6", "4 / 7", "5 / 8"]:
                set_text(s, "5 / 8", font_size=9, color=COLOR_TEXT_MUTED)
            elif "MAU [x]M" in txt or "Kênh tự nhiên (Non-Paid) tăng trưởng" in txt:
                content = (
                    "• Kênh tự nhiên (Non-Paid) tăng trưởng +15.1% MoM (+416K views), chiếm 87.2% toàn Web (tháng 9: 69.7%).\n"
                    "• Việc chủ động giảm 61.2% Paid Ads (-733K views) giúp tiết kiệm đáng kể chi phí mà tổng lượt xem vẫn đạt 99.2% kế hoạch (3.28M MTD, forecast 3.64M).\n"
                    "• Tỷ lệ chuyển đổi cài app từ Non-Paid đạt 25.33%, cao gấp 5.4 lần so với nguồn quảng cáo trả phí."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "[Use case] thấp hơn Target" in txt or "Rủi ro: Lưu lượng phụ thuộc" in txt:
                content = (
                    "• Rủi ro: Lưu lượng phụ thuộc lớn vào thuật toán Google Search; tỷ lệ chuyển đổi Paid Ads hiện rất thấp (CVR 4.7%).\n"
                    "• Hướng xử lý: Chuyển toàn bộ ngân sách Paid Ads sang cơ chế nghiệm thu Map Bank; tập trung SEO kỹ thuật và GEO trích dẫn AI."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table

            # Remove rows after index 5 (keep header + 5 rows = 6 rows total)
            tr_elements = tbl._tbl.xpath("./a:tr")
            if len(tr_elements) > 6:
                for tr in tr_elements[6:]:
                    tbl._tbl.remove(tr)

            # Remove columns after index 6 (keep 7 columns total)
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

            headers = ["Chỉ tiêu hiệu suất", "T9 Thực tế", "T10 MTD", "MoM (%)", "Kế hoạch T10", "% Kế hoạch", "Đánh giá"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=8.5, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c > 0 else PP_ALIGN.LEFT)

            rows_data = [
                ["Tổng lượt xem (PVs)", "3.570.627", "3.284.285", "-8.0%", "3.310.000", "99.2%", "Đạt tiến độ"],
                ["• Kênh tự nhiên (Non-Paid)", "2.489.102", "2.865.064", "+15.1%", "2.700.000", "106.1%", "Vượt kế hoạch"],
                ["• Quảng cáo trả phí (Paid)", "1.081.525", "419.221", "-61.2%", "610.000", "68.7%", "Chủ động giảm"],
                ["Lượt cài app qua OneLink", "9.480", "9.824", "+3.6%", "10.000", "98.2%", "Tăng trưởng"],
                ["User liên kết ngân hàng", "1.810", "2.072", "+14.5%", "2.000", "103.6%", "Chất lượng cao"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.5, bold=(r_idx in [1, 2]), align=PP_ALIGN.CENTER if c_idx in [1, 2, 3, 4, 5, 6] else PP_ALIGN.LEFT)

    # =========================================================================
    # SLIDE 6: Hubs & Category Breakdown [R] (Original Slide 15)
    # =========================================================================
    s6 = prs.slides[5]
    for s in s6.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if "[Category] [vượt/hụt]" in txt or "Cinema Hub Dẫn Đầu" in txt:
                set_text(s, "Cinema Hub Dẫn Đầu Tăng Trưởng (+142.2% Cụm Rạp); Financial Hub Tăng Trưởng Cụm Tỷ Giá (+444.9% MoM)", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: GA4 & BigQuery   |   Owner: Web Platform   |   Chốt số liệu: 28/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["7", "5 / 7", "6 / 8"]:
                set_text(s, "6 / 8", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Ý chính 1:" in txt:
                content = (
                    "• Ý chính 1: Cinema Hub đạt 726K views cụm rạp (+142.2%), đóng góp 1.8K cài app OneLink (CVR Map Bank đạt 25.33%).\n"
                    "• Ý chính 2: Financial Hub đạt 223K views (+10.9%), riêng cụm Tỷ giá tăng +444.9%, bù đắp phần giảm của Vay Nhanh do cắt Ads.\n"
                    "• Ý chính 3: Mở rộng cụm tiện ích tài chính (Thuế TNCN, Lương Gross-Net) chuẩn bị phục vụ cao điểm tra cứu cuối năm."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif txt == "x.xM":
                set_text(s, "726.8K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
            elif txt == "▲ +x% MoM":
                set_text(s, "▲ +142.2% MoM", font_size=10, bold=True, color=COLOR_GREEN)
            elif txt == "xx% vs Budget":
                set_text(s, "102% vs Kế hoạch", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt == "xx.xB":
                set_text(s, "223.2K", font_size=20, bold=True, color=COLOR_TEXT_MAIN)
            elif txt == "MAU đạt [x]M":
                content = (
                    "• Cinema Hub: Tăng mạnh nhờ mở rộng mạng lưới 18 cụm rạp đối tác và bảng giá vé real-time; chiếm 45% tổng OneLink Installs toàn Web.\n"
                    "• Financial Hub: Cụm Tỷ giá USD, EUR, Vàng tăng mạnh (+27.8K views); Ví Trả Sau tăng +18.5K views."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "[Chỉ số] đi ngang" in txt:
                content = (
                    "• Vay Nhanh giảm -31.2K views do cắt Paid Ads -> Cần đẩy mạnh SEO On-Page và liên kết nội bộ từ các tiện ích tài chính."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)

    # =========================================================================
    # SLIDE 7: Product / OneLink W2A Funnel [R] (Original Slide 20)
    # =========================================================================
    s7 = prs.slides[6]
    for s in s7.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if "[Vấn đề trọng yếu]" in txt or "Phễu AppsFlyer Đạt" in txt:
                set_text(s, "Phễu AppsFlyer Đạt 9.8K Installs, CVR End-to-End Đạt 21.1% Với 2.072 Tài Khoản Liên Kết Ngân Hàng", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: AppsFlyer GPD Attribution   |   Owner: Web Platform   |   Chốt số liệu: 28/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["9", "6 / 7", "7 / 8"]:
                set_text(s, "7 / 8", font_size=9, color=COLOR_TEXT_MUTED)
            elif "Ý chính 1:" in txt:
                content = (
                    "• Ý chính 1: Tổng lượt click nút OneLink đạt 46.5K, chuyển đổi thành 9.824 lượt cài app (CVR Click-to-Install đạt 21.1%).\n"
                    "• Ý chính 2: 2.072 người dùng mới hoàn tất liên kết ngân hàng (Map Bank) trong 24h đầu; chi phí bình quân giảm 34% so với tháng 9."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "Chỉ số product chính [x]% MoM" in txt:
                content = (
                    "• Người dùng đến từ các tiện ích tính toán và cụm rạp có tỷ lệ liên kết ngân hàng cao nhất (25.33%).\n"
                    "• Quảng cáo TikTok có tỷ lệ chuyển đổi Click-to-Install chỉ đạt 4.7%, xác nhận cần ngưng ngân sách để bảo toàn dòng tiền."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
            elif "Vấn đề cần quyết định/hỗ trợ" in txt:
                content = (
                    "• Triển khai bộ đo lường Umami sâu cho các widget mới để tối ưu điểm rơi CTA OneLink trên từng bước thao tác người dùng."
                )
                set_text(s, content, font_size=9.5, color=COLOR_TEXT_MAIN)
        elif s.has_table:
            tbl = s.table
            headers = ["Bước phễu OneLink", "Tháng 9 (MTD)", "Tháng 10 (MTD)", "CVR Chuyển đổi", "Đánh giá chất lượng"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c in [1, 2, 3] else PP_ALIGN.LEFT)

            rows_data = [
                ["1. OneLink Clicks", "43.200", "46.550", "1.42% (trên PVs)", "Tăng trưởng tự nhiên"],
                ["2. App Installs", "9.480", "9.824", "21.10% (trên Clicks)", "Chất lượng ổn định"],
                ["3. Map Bank Accounts", "1.810", "2.072", "21.09% (trên Installs)", "Tăng +14.5% MoM"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.5, bold=(c_idx == 0), align=PP_ALIGN.CENTER if c_idx in [1, 2, 3] else PP_ALIGN.LEFT)

    # =========================================================================
    # SLIDE 8: Project Milestones & Support Tracker [R] (Original Slide 21)
    # =========================================================================
    s8 = prs.slides[7]
    for s in s8.shapes:
        if s.has_text_frame:
            txt = s.text_frame.text.strip()
            if "Dự án C chậm 2 tuần" in txt or "Lộ Trình Quý 4:" in txt:
                set_text(s, "Lộ Trình Quý 4: Đưa 4 Tiện Ích Thuế & Tính Lương Lên Production, Chuẩn Bị Toàn Diện Cho Cao Điểm Tết 2027", font_size=17, bold=True, color=COLOR_TEXT_MAIN)
            elif "Nguồn:" in txt:
                set_text(s, "Nguồn: Jira & Web Platform Roadmap   |   Owner: Web Platform   |   Chốt số liệu: 28/10/2026", font_size=9, color=COLOR_TEXT_MUTED)
            elif txt in ["7", "8", "8 / 8"]:
                set_text(s, "8 / 8", font_size=9, color=COLOR_TEXT_MUTED)
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
            elif "Việc đầu tiên quyết định" in txt:
                set_text(s, "Lưu ý: Việc phê duyệt ngân sách và ký kết hợp đồng trước 05/11 quyết định khả năng đạt vị thế Top 5.5 Google trước mùa phim Tết 2027.", font_size=9.5, color=COLOR_TEXT_MUTED)
        elif s.has_table:
            tbl = s.table
            headers = ["Việc cần hỗ trợ", "Bên liên quan / Owner", "Hạn hoàn thành"]
            for c, h in enumerate(headers):
                set_cell(tbl.cell(0, c), h, font_size=9.0, bold=True, color=COLOR_WHITE, align=PP_ALIGN.CENTER if c == 2 else PP_ALIGN.LEFT)

            rows_data = [
                ["Phê duyệt ngân sách 125 triệu VNĐ gói Pilot SEO Cinema", "BOM / Finance", "05/11"],
                ["Hỗ trợ ký kết hợp đồng mạng lưới báo chí và đối tác dữ liệu", "Pháp chế & Mua hàng", "08/11"],
                ["Hoàn tất tuyển dụng 1 nhân sự Senior SEO Technical in-house", "HR Talent Acquisition", "15/11"],
            ]
            for r_idx, r_data in enumerate(rows_data, 1):
                for c_idx, val in enumerate(r_data):
                    set_cell(tbl.cell(r_idx, c_idx), val, font_size=8.5, bold=(c_idx == 0), align=PP_ALIGN.CENTER if c_idx == 2 else PP_ALIGN.LEFT)

    # Save to all destination paths
    for p in OUT_PATHS:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        prs.save(p)
        print(f"Successfully generated PPTX: {p}")

if __name__ == "__main__":
    main()
