#!/usr/bin/env python3
"""
Generate Web Platform Monthly Business Review PPTX (7 Slides)
Standardized 100% against MoMo Reporting Guidelines & Templates (23 slides).
Aspect ratio: 16:9 (10.0 x 5.625 inches)
"""

import os
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ── Color Palette ──
C_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
C_DARK = RGBColor(0x1C, 0x17, 0x1A)
C_BODY = RGBColor(0x3D, 0x33, 0x40)
C_MUTED = RGBColor(0x7A, 0x6E, 0x7F)
C_LIGHT_BG = RGBColor(0xFA, 0xF7, 0xFC)
C_BORDER = RGBColor(0xE8, 0xE2, 0xEC)

# Brand & Status Colors
C_PINK = RGBColor(0xD8, 0x2D, 0x8B)
C_PINK_BG = RGBColor(0xFD, 0xF2, 0xF7)
C_AMBER = RGBColor(0xD9, 0x77, 0x06)
C_AMBER_BG = RGBColor(0xFE, 0xF3, 0xC7)
C_GREEN = RGBColor(0x05, 0x96, 0x69)
C_GREEN_BG = RGBColor(0xD1, 0xFA, 0xE5)
C_INDIGO = RGBColor(0x4F, 0x46, 0xE5)
C_INDIGO_BG = RGBColor(0xEE, 0xF2, 0xFF)
C_ROSE = RGBColor(0xE1, 0x1D, 0x48)
C_ROSE_BG = RGBColor(0xFF, 0xE4, 0xE6)

FONT_HEADING = 'Arial'
FONT_BODY = 'Arial'

TOTAL_SLIDES = 7

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(10.0)
    prs.slide_height = Inches(5.625)
    blank_layout = prs.slide_layouts[6] if len(prs.slide_layouts) > 6 else prs.slide_layouts[0]

    # ── Helper Functions ──
    def add_blank_slide():
        slide = prs.slides.add_slide(blank_layout)
        # Clear default shapes if any
        for shp in list(slide.shapes):
            sp = shp._element
            sp.getparent().remove(sp)
        # Background fill white
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = C_WHITE
        return slide

    def add_footer(slide, current_idx, source="GA4 (Property 270743103) & AppsFlyer GPD Attribution"):
        # Footer line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.52), Inches(5.20), Inches(8.96), Inches(0.01))
        line.fill.solid()
        line.fill.fore_color.rgb = C_BORDER
        line.line.color.rgb = C_BORDER

        # Footer Text
        tb = slide.shapes.add_textbox(Inches(0.52), Inches(5.24), Inches(7.5), Inches(0.28))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.font.name = FONT_BODY
        p.font.size = Pt(8.5)
        p.font.color.rgb = C_MUTED
        
        r1 = p.add_run()
        r1.text = f"Nguon: {source}   |   Owner: Web Platform   |   Chot so lieu: 28/10/2026"

        # Slide Number
        tb_num = slide.shapes.add_textbox(Inches(8.2), Inches(5.24), Inches(1.28), Inches(0.28))
        tf_num = tb_num.text_frame
        tf_num.margin_left = tf_num.margin_top = tf_num.margin_right = tf_num.margin_bottom = 0
        p_num = tf_num.paragraphs[0]
        p_num.alignment = PP_ALIGN.RIGHT
        p_num.font.name = FONT_BODY
        p_num.font.size = Pt(8.5)
        p_num.font.bold = True
        p_num.font.color.rgb = C_MUTED
        p_num.text = f"Slide {current_idx} / {TOTAL_SLIDES}"

    def add_slide_header(slide, tag_type, tag_desc, action_title):
        """Standard MoMo Header: Tag pill + Desc + Action Title"""
        is_discussion = (tag_type == 'D')
        tag_color = C_AMBER if is_discussion else C_GREEN
        tag_label = "[D] DISCUSSION" if is_discussion else "[R] REPORTING"

        # Header tag pill
        tb_tag = slide.shapes.add_textbox(Inches(0.52), Inches(0.22), Inches(8.96), Inches(0.24))
        tf_tag = tb_tag.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]

        r_tag = p_tag.add_run()
        r_tag.text = tag_label + "   "
        r_tag.font.name = FONT_HEADING
        r_tag.font.size = Pt(9.5)
        r_tag.font.bold = True
        r_tag.font.color.rgb = tag_color

        r_desc = p_tag.add_run()
        r_desc.text = tag_desc
        r_desc.font.name = FONT_BODY
        r_desc.font.size = Pt(9)
        r_desc.font.color.rgb = C_MUTED

        # Action Title
        tb_title = slide.shapes.add_textbox(Inches(0.52), Inches(0.48), Inches(8.96), Inches(0.48))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.font.name = FONT_HEADING
        p_title.font.size = Pt(15.5)
        p_title.font.bold = True
        p_title.font.color.rgb = C_DARK
        p_title.text = action_title

        # Divider line
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.52), Inches(0.98), Inches(8.96), Inches(0.01))
        div.fill.solid()
        div.fill.fore_color.rgb = C_BORDER
        div.line.color.rgb = C_BORDER

    # =========================================================================
    # SLIDE 1: COVER SLIDE (Chuẩn Slide 7 MoMo Guidelines)
    # =========================================================================
    s1 = add_blank_slide()

    # Category breadcrumb
    tb1_bc = s1.shapes.add_textbox(Inches(0.52), Inches(0.55), Inches(8.96), Inches(0.3))
    tf1_bc = tb1_bc.text_frame
    tf1_bc.margin_left = tf1_bc.margin_top = tf1_bc.margin_right = tf1_bc.margin_bottom = 0
    p1_bc = tf1_bc.paragraphs[0]
    r1_bc = p1_bc.add_run()
    r1_bc.text = "WEB PLATFORM · MONTHLY BUSINESS REVIEW  •  THÁNG 10/2026"
    r1_bc.font.name = FONT_HEADING
    r1_bc.font.size = Pt(11)
    r1_bc.font.bold = True
    r1_bc.font.color.rgb = C_PINK

    # Main Title
    tb1_t = s1.shapes.add_textbox(Inches(0.52), Inches(0.95), Inches(8.96), Inches(0.85))
    tf1_t = tb1_t.text_frame
    tf1_t.word_wrap = True
    tf1_t.margin_left = tf1_t.margin_top = tf1_t.margin_right = tf1_t.margin_bottom = 0
    p1_t = tf1_t.paragraphs[0]
    p1_t.text = "Báo Cáo Hiệu Suất Nền Tảng Web"
    p1_t.font.name = FONT_HEADING
    p1_t.font.size = Pt(30)
    p1_t.font.bold = True
    p1_t.font.color.rgb = C_DARK

    # Subtitle
    tb1_sub = s1.shapes.add_textbox(Inches(0.52), Inches(1.85), Inches(8.96), Inches(0.35))
    tf1_sub = tb1_sub.text_frame
    tf1_sub.margin_left = tf1_sub.margin_top = tf1_sub.margin_right = tf1_sub.margin_bottom = 0
    p1_sub = tf1_sub.paragraphs[0]
    p1_sub.text = "Report để cung cấp thông tin  •  Meeting để thảo luận và ra quyết định"
    p1_sub.font.name = FONT_BODY
    p1_sub.font.size = Pt(13)
    p1_sub.font.color.rgb = C_BODY

    # Meta line
    tb1_meta = s1.shapes.add_textbox(Inches(0.52), Inches(2.25), Inches(8.96), Inches(0.35))
    tf1_meta = tb1_meta.text_frame
    tf1_meta.margin_left = tf1_meta.margin_top = tf1_meta.margin_right = tf1_meta.margin_bottom = 0
    p1_meta = tf1_meta.paragraphs[0]
    p1_meta.font.name = FONT_BODY
    p1_meta.font.size = Pt(9.5)
    p1_meta.font.color.rgb = C_MUTED
    p1_meta.text = "Kỳ số liệu: 01/10 - 28/10/2026 (MTD 28 ngày & Forecast 31 ngày)   |   [D] Thảo luận & Phê duyệt   |   [R] Báo cáo Pre-read"

    # 4 Scorecard Cards
    kpis = [
        ("Tổng lượt xem (forecast)", "3.636.173", "MTD 3.284.285 · 99.2% Target", C_DARK),
        ("Tỷ trọng tự nhiên", "87.2%", "2.865.064 PV (+15.1% MoM)", C_GREEN),
        ("Cài app qua OneLink (MTD)", "9.824", "Forecast 10.876 (+3.6% MoM)", C_PINK),
        ("CVR Toàn phễu", "21.1%", "2.072 tài khoản Map Bank", C_GREEN),
    ]

    card_w = Inches(2.12)
    card_gap = Inches(0.16)
    card_h = Inches(1.85)
    start_y = Inches(2.95)

    for i, (label, val, note, val_color) in enumerate(kpis):
        x = Inches(0.52) + i * (card_w + card_gap)
        box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, start_y, card_w, card_h)
        box.fill.solid()
        box.fill.fore_color.rgb = C_LIGHT_BG
        box.line.color.rgb = C_BORDER
        box.line.width = Pt(1)

        tb = s1.shapes.add_textbox(x + Inches(0.14), start_y + Inches(0.16), card_w - Inches(0.28), card_h - Inches(0.32))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_lbl = tf.paragraphs[0]
        p_lbl.text = label
        p_lbl.font.name = FONT_BODY
        p_lbl.font.size = Pt(9.5)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = C_MUTED

        p_val = tf.add_paragraph()
        p_val.space_before = Pt(8)
        p_val.text = val
        p_val.font.name = FONT_HEADING
        p_val.font.size = Pt(21)
        p_val.font.bold = True
        p_val.font.color.rgb = val_color

        p_nt = tf.add_paragraph()
        p_nt.space_before = Pt(8)
        p_nt.text = note
        p_nt.font.name = FONT_BODY
        p_nt.font.size = Pt(8.5)
        p_nt.font.color.rgb = C_GREEN if "Target" in note or "MoM" in note or "Bank" in note else C_MUTED

    add_footer(s1, 1)

    # =========================================================================
    # SLIDE 2: DISCUSSION TOPICS OVERVIEW [D] (Chuẩn Slide 10 Guidelines)
    # =========================================================================
    s2 = add_blank_slide()
    add_slide_header(s2, 'D', "Trọng tâm cuộc họp · Cần thảo luận & phê duyệt",
                     "Discussion Topics: 2 Đề Xuất Phê Duyệt Về Tái Cấu Trúc Ads & Kích Hoạt SEO Cinema")

    # Rule of Three Takeaway Strip
    strip_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.52), Inches(1.10), Inches(8.96), Inches(0.78))
    strip_box.fill.solid()
    strip_box.fill.fore_color.rgb = C_AMBER_BG
    strip_box.line.color.rgb = C_AMBER
    strip_box.line.width = Pt(0.75)

    takeaways = [
        ("01", "Tái cấu trúc ngân sách Ads: ", "Dừng TikTok Ads lưu trang 0.6s; chuyển 100% sang nghiệm thu người dùng Map Bank qua AppsFlyer."),
        ("02", "Gói Pilot Off-Page SEO: ", "Phê duyệt 125 triệu VNĐ (3 tháng) cho Cinema Hub để đưa cụm rạp đạt Top 5.5 Google trước Tết 2027."),
        ("03", "Kỷ luật ra quyết định: ", "Chốt phê duyệt trước 05/11 để kịp ký hợp đồng đối tác báo chí và hoàn thành tuyển dụng in-house."),
    ]
    col_w = Inches(2.90)
    for j, (num, bold_txt, norm_txt) in enumerate(takeaways):
        tx = Inches(0.60) + j * Inches(2.98)
        tb_tk = s2.shapes.add_textbox(tx, Inches(1.16), col_w, Inches(0.66))
        tf_tk = tb_tk.text_frame
        tf_tk.word_wrap = True
        tf_tk.margin_left = tf_tk.margin_top = tf_tk.margin_right = tf_tk.margin_bottom = 0
        p_tk = tf_tk.paragraphs[0]
        p_tk.font.size = Pt(8.5)
        p_tk.font.name = FONT_BODY

        r_num = p_tk.add_run()
        r_num.text = f"[{num}] "
        r_num.font.bold = True
        r_num.font.color.rgb = C_AMBER

        r_bold = p_tk.add_run()
        r_bold.text = bold_txt
        r_bold.font.bold = True
        r_bold.font.color.rgb = C_DARK

        r_norm = p_tk.add_run()
        r_norm.text = norm_txt
        r_norm.font.color.rgb = C_BODY

    # Table: 8 columns (Chuẩn cấu trúc Slide 10 MoMo)
    t_rows, t_cols = 3, 8
    t_shape = s2.shapes.add_table(t_rows, t_cols, Inches(0.52), Inches(2.02), Inches(8.96), Inches(2.95))
    tbl = t_shape.table

    col_widths = [Inches(0.35), Inches(1.70), Inches(0.70), Inches(2.55), Inches(1.70), Inches(0.55), Inches(0.65), Inches(0.76)]
    for c_idx, w in enumerate(col_widths):
        tbl.columns[c_idx].width = w

    headers = ["#", "Chủ đề", "Loại", "Cần CEO / BOM quyết định gì", "Tác động lượng hóa", "Hạn", "Ưu tiên", "Chi tiết"]
    for c_idx, h in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(0xF3, 0xEE, 0xF6)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER if c_idx in [0, 2, 5, 6, 7] else PP_ALIGN.LEFT
        r = p.add_run()
        r.text = h
        r.font.name = FONT_HEADING
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = C_DARK

    table_data = [
        ("1", "Tối Ưu Ngân Sách Paid Media & Chuẩn Hóa Đo Lường OneLink", "Approve",
         "Ban hành quy định: Mọi chiến dịch dùng ngân sách đổ về Web bắt buộc nghiệm thu theo User Map Bank qua AppsFlyer; dừng TikTok Ads rác.",
         "Bảo toàn ~40% chi phí Ads; CVR cài app đạt 4.7% - 18.4%", "31/10", "CAO", "Slide 3 →"),
        ("2", "Phê Duyệt Gói Pilot Off-Page SEO Cinema Hub (125 Triệu VNĐ)", "Approve",
         "Phê duyệt ngân sách 125 triệu VNĐ (3 tháng), ký trực tiếp mạng lưới đối tác báo chí lớn; giao HR & Pháp chế hỗ trợ thủ tục trước 05/11.",
         "Đưa cụm rạp đạt Top 5.5 Google & đón lưu lượng trước Tết 2027", "05/11", "CAO", "Slide 3 →")
    ]

    for r_idx, row in enumerate(table_data):
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if r_idx % 2 == 0 else C_LIGHT_BG
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if c_idx in [0, 2, 5, 6, 7] else PP_ALIGN.LEFT
            r = p.add_run()
            r.text = val
            r.font.name = FONT_BODY
            r.font.size = Pt(8)
            if c_idx == 0:
                r.font.bold = True
                r.font.color.rgb = C_AMBER
            elif c_idx == 1:
                r.font.bold = True
                r.font.color.rgb = C_DARK
            elif c_idx == 2:
                r.font.bold = True
                r.font.color.rgb = C_AMBER
            elif c_idx == 4:
                r.font.bold = True
                r.font.color.rgb = C_GREEN if r_idx == 0 else C_INDIGO
            elif c_idx == 6:
                r.font.bold = True
                r.font.color.rgb = C_ROSE
            elif c_idx == 7:
                r.font.bold = True
                r.font.color.rgb = C_PINK
            else:
                r.font.color.rgb = C_BODY

    add_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: DEEP-DIVE 2 ĐỀ XUẤT QUYẾT ĐỊNH [D] (Chuẩn Slide 12 & 22 Guidelines)
    # =========================================================================
    s3 = add_blank_slide()
    add_slide_header(s3, 'D', "Đề xuất quyết nghị chi tiết · Phương án lựa chọn A vs B",
                     "Chi Tiết Đề Xuất: Tái Cấu Trúc Ngân Sách Ads & Phê Duyệt Gói Pilot SEO Cinema (125 Tr VNĐ)")

    # 2 Proposal Cards Side-by-Side
    prop_w = Inches(4.38)
    prop_h = Inches(4.00)
    prop_y = Inches(1.10)

    # Card 1: Paid Media Optimization
    x1 = Inches(0.52)
    box1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x1, prop_y, prop_w, prop_h)
    box1.fill.solid()
    box1.fill.fore_color.rgb = C_WHITE
    box1.line.color.rgb = C_AMBER
    box1.line.width = Pt(1)

    tb_p1 = s3.shapes.add_textbox(x1 + Inches(0.18), prop_y + Inches(0.16), prop_w - Inches(0.36), prop_h - Inches(0.32))
    tf_p1 = tb_p1.text_frame
    tf_p1.word_wrap = True
    tf_p1.margin_left = tf_p1.margin_top = tf_p1.margin_right = tf_p1.margin_bottom = 0

    p_p1_tag = tf_p1.paragraphs[0]
    p_p1_tag.text = "ĐỀ XUẤT 1 · PHÊ DUYỆT (Hạn: 31/10)"
    p_p1_tag.font.name = FONT_HEADING
    p_p1_tag.font.size = Pt(9)
    p_p1_tag.font.bold = True
    p_p1_tag.font.color.rgb = C_AMBER

    p_p1_t = tf_p1.add_paragraph()
    p_p1_t.space_before = Pt(4)
    p_p1_t.text = "Tối Ưu Ngân Sách Paid Media & Chuẩn Hóa Đo Lường OneLink"
    p_p1_t.font.name = FONT_HEADING
    p_p1_t.font.size = Pt(11)
    p_p1_t.font.bold = True
    p_p1_t.font.color.rgb = C_DARK

    p_p1_prob = tf_p1.add_paragraph()
    p_p1_prob.space_before = Pt(6)
    r = p_p1_prob.add_run()
    r.text = "Problem Statement: "
    r.font.bold = True
    r.font.size = Pt(8.5)
    r.font.color.rgb = C_DARK
    r2 = p_p1_prob.add_run()
    r2.text = "Chiến dịch TikTok Ads chiếm 40% chi phí nhưng onsite chỉ 0.6s, CVR cài app chỉ 0.08%; trong khi Google Search Intent & FB Lookalike đạt CVR 4.7% - 18.4%."
    r2.font.size = Pt(8.5)
    r2.font.color.rgb = C_BODY

    p_p1_tbl = tf_p1.add_paragraph()
    p_p1_tbl.space_before = Pt(8)
    p_p1_tbl.text = "BẢNG SO SÁNH PHƯƠNG ÁN (A vs B):"
    p_p1_tbl.font.bold = True
    p_p1_tbl.font.size = Pt(8.5)
    p_p1_tbl.font.color.rgb = C_MUTED

    p_optA = tf_p1.add_paragraph()
    p_optA.space_before = Pt(4)
    r_a1 = p_optA.add_run()
    r_a1.text = "• Phương án A (BU chọn): "
    r_a1.font.bold = True
    r_a1.font.size = Pt(8.5)
    r_a1.font.color.rgb = C_GREEN
    r_a2 = p_optA.add_run()
    r_a2.text = "Dừng TikTok Ads, dồn ngân sách vào Google Search & FB Lookalike; nghiệm thu theo Map Bank -> Tiết kiệm chi phí, tăng trưởng sạch."
    r_a2.font.size = Pt(8.5)
    r_a2.font.color.rgb = C_BODY

    p_optB = tf_p1.add_paragraph()
    p_optB.space_before = Pt(4)
    r_b1 = p_optB.add_run()
    r_b1.text = "• Phương án B: "
    r_b1.font.bold = True
    r_b1.font.size = Pt(8.5)
    r_b1.font.color.rgb = C_MUTED
    r_b2 = p_optB.add_run()
    r_b2.text = "Tiếp tục nghiệm thu theo Pageviews -> Lãng phí 50 - 80 triệu VNĐ/tháng vào traffic rác."
    r_b2.font.size = Pt(8.5)
    r_b2.font.color.rgb = C_ROSE

    p_req = tf_p1.add_paragraph()
    p_req.space_before = Pt(10)
    r_req1 = p_req.add_run()
    r_req1.text = "Đề nghị BOM: "
    r_req1.font.bold = True
    r_req1.font.size = Pt(8.5)
    r_req1.font.color.rgb = C_GREEN
    r_req2 = p_req.add_run()
    r_req2.text = "Phê duyệt quy định bắt buộc nghiệm thu qua Map Bank từ 01/11/2026."
    r_req2.font.size = Pt(8.5)
    r_req2.font.color.rgb = C_DARK

    p_risk = tf_p1.add_paragraph()
    p_risk.space_before = Pt(4)
    r_rk1 = p_risk.add_run()
    r_rk1.text = "Nếu không quyết định: "
    r_rk1.font.bold = True
    r_rk1.font.size = Pt(8.5)
    r_rk1.font.color.rgb = C_ROSE
    r_rk2 = p_risk.add_run()
    r_rk2.text = "Lãng phí thêm dòng tiền vào nguồn traffic không chuyển đổi."
    r_rk2.font.size = Pt(8.5)
    r_rk2.font.color.rgb = C_BODY

    # Card 2: Pilot Off-Page SEO Cinema Hub
    x2 = Inches(5.10)
    box2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x2, prop_y, prop_w, prop_h)
    box2.fill.solid()
    box2.fill.fore_color.rgb = C_WHITE
    box2.line.color.rgb = C_INDIGO
    box2.line.width = Pt(1)

    tb_p2 = s3.shapes.add_textbox(x2 + Inches(0.18), prop_y + Inches(0.16), prop_w - Inches(0.36), prop_h - Inches(0.32))
    tf_p2 = tb_p2.text_frame
    tf_p2.word_wrap = True
    tf_p2.margin_left = tf_p2.margin_top = tf_p2.margin_right = tf_p2.margin_bottom = 0

    p_p2_tag = tf_p2.paragraphs[0]
    p_p2_tag.text = "ĐỀ XUẤT 2 · PHÊ DUYỆT (Hạn: 05/11)"
    p_p2_tag.font.name = FONT_HEADING
    p_p2_tag.font.size = Pt(9)
    p_p2_tag.font.bold = True
    p_p2_tag.font.color.rgb = C_INDIGO

    p_p2_t = tf_p2.add_paragraph()
    p_p2_t.space_before = Pt(4)
    p_p2_t.text = "Kích Hoạt Gói Pilot Off-Page SEO Cinema Hub (125 Triệu VNĐ)"
    p_p2_t.font.name = FONT_HEADING
    p_p2_t.font.size = Pt(11)
    p_p2_t.font.bold = True
    p_p2_t.font.color.rgb = C_DARK

    p_p2_prob = tf_p2.add_paragraph()
    p_p2_prob.space_before = Pt(6)
    r = p_p2_prob.add_run()
    r.text = "Problem Statement: "
    r.font.bold = True
    r.font.size = Pt(8.5)
    r.font.color.rgb = C_DARK
    r2 = p_p2_prob.add_run()
    r2.text = "MoMo chiếm 50% thị phần bán vé nhưng lưu lượng bài review/rạp mới đạt 20%. Mùa phim Tết 2027 bắt đầu từ tháng 12/2026, cần chiếm lĩnh thứ hạng sớm."
    r2.font.size = Pt(8.5)
    r2.font.color.rgb = C_BODY

    p_p2_tbl = tf_p2.add_paragraph()
    p_p2_tbl.space_before = Pt(8)
    p_p2_tbl.text = "BẢNG SO SÁNH PHƯƠNG ÁN (A vs B):"
    p_p2_tbl.font.bold = True
    p_p2_tbl.font.size = Pt(8.5)
    p_p2_tbl.font.color.rgb = C_MUTED

    p2_optA = tf_p2.add_paragraph()
    p2_optA.space_before = Pt(4)
    r_a1 = p2_optA.add_run()
    r_a1.text = "• Phương án A (BU chọn): "
    r_a1.font.bold = True
    r_a1.font.size = Pt(8.5)
    r_a1.font.color.rgb = C_GREEN
    r_a2 = p2_optA.add_run()
    r_a2.text = "Ký trực tiếp mạng lưới báo chí lớn; in-house kiểm soát chất lượng E-E-A-T -> Chi phí 125 Tr VNĐ (tiết kiệm 50 - 75 Tr)."
    r_a2.font.size = Pt(8.5)
    r_a2.font.color.rgb = C_BODY

    p2_optB = tf_p2.add_paragraph()
    p2_optB.space_before = Pt(4)
    r_b1 = p2_optB.add_run()
    r_b1.text = "• Phương án B: "
    r_b1.font.bold = True
    r_b1.font.size = Pt(8.5)
    r_b1.font.color.rgb = C_MUTED
    r_b2 = p2_optB.add_run()
    r_b2.text = "Thuê Agency trung gian trọn gói -> 180 - 200 Tr VNĐ; khó kiểm soát chất lượng link."
    r_b2.font.size = Pt(8.5)
    r_b2.font.color.rgb = C_ROSE

    p2_req = tf_p2.add_paragraph()
    p2_req.space_before = Pt(10)
    r_req1 = p2_req.add_run()
    r_req1.text = "Đề nghị BOM: "
    r_req1.font.bold = True
    r_req1.font.size = Pt(8.5)
    r_req1.font.color.rgb = C_INDIGO
    r_req2 = p2_req.add_run()
    r_req2.text = "Phê duyệt Phương án A (125 tr VNĐ / 3 tháng), giao HR & Pháp chế hỗ trợ trước 05/11."
    r_req2.font.size = Pt(8.5)
    r_req2.font.color.rgb = C_DARK

    p2_risk = tf_p2.add_paragraph()
    p2_risk.space_before = Pt(4)
    r_rk1 = p2_risk.add_run()
    r_rk1.text = "Nếu không quyết định: "
    r_rk1.font.bold = True
    r_rk1.font.size = Pt(8.5)
    r_rk1.font.color.rgb = C_ROSE
    r_rk2 = p2_risk.add_run()
    r_rk2.text = "Mất cơ hội vàng chiếm lĩnh Top 5.5 Google Search trước đợt phim Tết 2027."
    r_rk2.font.size = Pt(8.5)
    r_rk2.font.color.rgb = C_BODY

    add_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: EXECUTIVE SUMMARY [R] (Chuẩn Slide 9 Guidelines)
    # =========================================================================
    s4 = add_blank_slide()
    add_slide_header(s4, 'R', "Executive Summary · Pre-read, không trình bày lại trong cuộc họp",
                     "Non-Paid Đạt 2.87M PVs (+15.1% MoM), Bù Đắp 733K Ads Cắt Giảm Và Đạt 99.2% Kế Hoạch")

    # 3 Pillars Grid
    pil_w = Inches(2.90)
    pil_h = Inches(4.00)
    pil_y = Inches(1.10)

    pillars = [
        ("Key Highlights & Impact", C_GREEN, C_GREEN_BG, [
            ("Lưu lượng tự nhiên (Non-Paid): ", "Đạt 2.865.064 PVs (+15.1% MoM), tự bù đắp khoảng trống khi dừng 61.2% Paid Ads."),
            ("Cụm rạp đối tác bứt phá: ", "Rio, Touch, Metiz tăng +142.2% (726K views), cân bằng sụt giảm lưu lượng phim lẻ sau lễ."),
            ("Chuyển đổi OneLink AppsFlyer: ", "Đạt 9.824 lượt cài app mới và 2.072 tài khoản liên kết ngân hàng (CVR toàn phễu 21.1%).")
        ]),
        ("Cross-team Collaboration", C_INDIGO, C_INDIGO_BG, [
            ("Hợp nhất dữ liệu BigQuery x GA4: ", "Tự động đối soát số liệu cùng kỳ và Net Add ngày mới phục vụ điều hành."),
            ("Phối hợp BU Movies: ", "Thống nhất cơ chế hợp tác bán vé xem phim, chia sẻ inventory và minigame tương tác."),
            ("Phối hợp Financial Services: ", "Hoàn thành QC và chuẩn bị phát hành 2 công cụ tính Thuế TNCN & Hộ kinh doanh online.")
        ]),
        ("Priorities for Next 30 Days", C_PINK, C_PINK_BG, [
            ("Triển khai SEO Off-Page Cinema: ", "Ký hợp đồng đối tác báo chí lớn, đưa cụm rạp đạt Top 5.5 Google trước mùa phim Tết 2027."),
            ("Go-live Công Cụ Thuế: ", "Phát hành công cụ Thuế TNCN và Hộ kinh doanh đón đầu mùa quyết toán thuế cuối năm."),
            ("Nghiệm thu Ads qua Map Bank: ", "Ban hành quy định bắt buộc nghiệm thu ngân sách Ads theo tài khoản liên kết ngân hàng.")
        ])
    ]

    for p_idx, (p_title, p_color, p_bg, p_items) in enumerate(pillars):
        px = Inches(0.52) + p_idx * Inches(3.03)
        p_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, pil_y, pil_w, pil_h)
        p_box.fill.solid()
        p_box.fill.fore_color.rgb = p_bg
        p_box.line.color.rgb = p_color
        p_box.line.width = Pt(1)

        p_tb = s4.shapes.add_textbox(px + Inches(0.16), pil_y + Inches(0.18), pil_w - Inches(0.32), pil_h - Inches(0.36))
        p_tf = p_tb.text_frame
        p_tf.word_wrap = True
        p_tf.margin_left = p_tf.margin_top = p_tf.margin_right = p_tf.margin_bottom = 0

        p_hdr = p_tf.paragraphs[0]
        p_hdr.text = p_title.upper()
        p_hdr.font.name = FONT_HEADING
        p_hdr.font.size = Pt(10)
        p_hdr.font.bold = True
        p_hdr.font.color.rgb = p_color

        for item_lead, item_body in p_items:
            p_item = p_tf.add_paragraph()
            p_item.space_before = Pt(12)
            r_lead = p_item.add_run()
            r_lead.text = "• " + item_lead
            r_lead.font.name = FONT_BODY
            r_lead.font.bold = True
            r_lead.font.size = Pt(8.5)
            r_lead.font.color.rgb = C_DARK

            r_body = p_item.add_run()
            r_body.text = item_body
            r_body.font.name = FONT_BODY
            r_body.font.size = Pt(8.5)
            r_body.font.color.rgb = C_BODY

    add_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: HIỆU SUẤT TỔNG THỂ & NGUYÊN NHÂN LƯU LƯỢNG GIẢM [R] (Slide 14 & 15)
    # =========================================================================
    s5 = add_blank_slide()
    add_slide_header(s5, 'R', "Hiệu Suất Tổng Thể & Cơ Cấu Lưu Lượng · Pre-read",
                     "Lưu Lượng Tháng 10 Giảm 8.0% MoM Do Cắt Giảm 61% Paid Ads; Kênh Tự Nhiên Duy Trì 87.2%")

    # Table: Non-Paid vs Paid
    st_rows, st_cols = 4, 7
    st_shape = s5.shapes.add_table(st_rows, st_cols, Inches(0.52), Inches(1.10), Inches(8.96), Inches(1.85))
    s_tbl = st_shape.table

    s_col_w = [Inches(2.10), Inches(0.95), Inches(0.95), Inches(0.95), Inches(0.90), Inches(0.70), Inches(2.41)]
    for c_i, w in enumerate(s_col_w):
        s_tbl.columns[c_i].width = w

    s_headers = ["Kênh Lưu Lượng", "T9/2026", "T10 MTD (28d)", "Forecast 31d", "Chênh lệch", "% MoM", "Đánh giá bản chất kinh doanh"]
    for c_i, h in enumerate(s_headers):
        c = s_tbl.cell(0, c_i)
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor(0xF3, 0xEE, 0xF6)
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = c.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT if c_i in [1, 2, 3, 4, 5] else PP_ALIGN.LEFT
        r = p.add_run()
        r.text = h
        r.font.name = FONT_HEADING
        r.font.bold = True
        r.font.size = Pt(8)
        r.font.color.rgb = C_DARK

    s_data = [
        ("KÊNH TỰ NHIÊN (NON-PAID)", "2.755.766", "2.865.064", "3.172.000", "+416.234", "+15.1%", "Trụ cột tăng trưởng tự nhiên bền vững; chiếm kỷ lục 87.2% toàn Web"),
        ("KÊNH TRẢ PHÍ (PAID ADS)", "1.197.093", "419.221", "464.000", "-733.093", "-61.2%", "Chủ động cắt Ads rác (TikTok lưu trang 0.6s) để bảo toàn dòng tiền"),
        ("TỔNG LƯỢNG TRUY CẬP", "3.952.859", "3.284.285", "3.636.173", "-316.686", "-8.0%", "Đạt 99.2% Target tháng; toàn Web vận hành trong trạng thái sạch nhất")
    ]

    for r_i, row in enumerate(s_data):
        for c_i, val in enumerate(row):
            c = s_tbl.cell(r_i + 1, c_i)
            c.fill.solid()
            if r_i == 0:
                c.fill.fore_color.rgb = C_GREEN_BG
            elif r_i == 1:
                c.fill.fore_color.rgb = C_AMBER_BG
            else:
                c.fill.fore_color.rgb = C_LIGHT_BG
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = c.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.RIGHT if c_i in [1, 2, 3, 4, 5] else PP_ALIGN.LEFT
            r = p.add_run()
            r.text = val
            r.font.name = FONT_BODY
            r.font.size = Pt(7.5)
            if c_i == 0:
                r.font.bold = True
                r.font.color.rgb = C_GREEN if r_i == 0 else (C_AMBER if r_i == 1 else C_DARK)
            elif c_i == 4 or c_i == 5:
                r.font.bold = True
                r.font.color.rgb = C_GREEN if "+" in val else C_ROSE
            elif r_i == 2:
                r.font.bold = True
                r.font.color.rgb = C_DARK
            else:
                r.font.color.rgb = C_BODY

    # 3 Executive Cause Cards
    causes = [
        ("Nguyên nhân 1 (Chủ động - 70% mức giảm)", "Dừng 733K Paid Ads Kém Hiệu Quả",
         "Cắt giảm 61% ngân sách quảng cáo. Nếu giữ nguyên Ads như T9, toàn Web đã đạt 4.37M PVs (119% Target).", C_AMBER, C_AMBER_BG),
        ("Nguyên nhân 2 (Khách quan - Vùng trũng thị trường)", "6 Trên 9 Nhóm Ngành Sụt Giảm Do Chu Kỳ Sau Lễ 2/9",
         "Google Trends 5 năm xác nhận T10 là vùng trũng sau 2/9: Học sinh sụt -16.4đ, Y tế -8.9đ, Rạp phim -5.8đ.", C_ROSE, C_ROSE_BG),
        ("Điểm sáng · Tăng trưởng bù đắp", "Kênh Tự Nhiên Tăng +416K Views (+15.1%)",
         "Lưu lượng tự nhiên tự bù đắp khoảng trống; rạp đối tác tăng +142.2%, Financial Hub tăng +7.2% bất chấp suy giảm toàn ngành.", C_GREEN, C_GREEN_BG)
    ]

    card_y = Inches(3.15)
    card_h = Inches(1.90)
    for c_idx, (c_tag, c_title, c_desc, c_color, c_bg) in enumerate(causes):
        cx = Inches(0.52) + c_idx * Inches(3.03)
        c_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, Inches(2.90), card_h)
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = c_bg
        c_box.line.color.rgb = c_color
        c_box.line.width = Pt(1)

        c_tb = s5.shapes.add_textbox(cx + Inches(0.14), card_y + Inches(0.14), Inches(2.62), card_h - Inches(0.28))
        c_tf = c_tb.text_frame
        c_tf.word_wrap = True
        c_tf.margin_left = c_tf.margin_top = c_tf.margin_right = c_tf.margin_bottom = 0

        p1 = c_tf.paragraphs[0]
        p1.text = c_tag.upper()
        p1.font.name = FONT_BODY
        p1.font.size = Pt(8)
        p1.font.bold = True
        p1.font.color.rgb = c_color

        p2 = c_tf.add_paragraph()
        p2.space_before = Pt(4)
        p2.text = c_title
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = C_DARK

        p3 = c_tf.add_paragraph()
        p3.space_before = Pt(6)
        p3.text = c_desc
        p3.font.name = FONT_BODY
        p3.font.size = Pt(8)
        p3.font.color.rgb = C_BODY

    add_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: HAI DỰ ÁN TRỌNG ĐIỂM: CINEMA HUB & FINANCIAL HUB [R] (Slide 20 & 21)
    # =========================================================================
    s6 = add_blank_slide()
    add_slide_header(s6, 'R', "Tiến Độ Dự Án Trọng Điểm · Pre-read",
                     "Cinema Hub Đạt 1.8K Installs (+142% Cụm Rạp); Financial Hub Tăng Trưởng Cụm Tỷ Giá (+445% MoM)")

    # 2 Focus Hub Cards Side-by-Side
    h_w = Inches(4.38)
    h_h = Inches(4.00)
    h_y = Inches(1.10)

    # Cinema Hub Card
    hx1 = Inches(0.52)
    h_box1 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, hx1, h_y, h_w, h_h)
    h_box1.fill.solid()
    h_box1.fill.fore_color.rgb = C_WHITE
    h_box1.line.color.rgb = C_PINK
    h_box1.line.width = Pt(1)

    h_tb1 = s6.shapes.add_textbox(hx1 + Inches(0.18), h_y + Inches(0.16), h_w - Inches(0.36), h_h - Inches(0.32))
    h_tf1 = h_tb1.text_frame
    h_tf1.word_wrap = True
    h_tf1.margin_left = h_tf1.margin_top = h_tf1.margin_right = h_tf1.margin_bottom = 0

    p_c_tag = h_tf1.paragraphs[0]
    p_c_tag.text = "CINEMA HUB  •  THU HÚT NEW USER SỐ 1 WEB"
    p_c_tag.font.name = FONT_HEADING
    p_c_tag.font.size = Pt(9.5)
    p_c_tag.font.bold = True
    p_c_tag.font.color.rgb = C_PINK

    # 3 Stats in row
    p_c_stat = h_tf1.add_paragraph()
    p_c_stat.space_before = Pt(6)
    p_c_stat.text = "W2A Installs: 1.808   |   Map Bank: 458 (CVR 25.3%)   |   Pilot Off-Page: 125 Tr"
    p_c_stat.font.name = FONT_HEADING
    p_c_stat.font.size = Pt(9)
    p_c_stat.font.bold = True
    p_c_stat.font.color.rgb = C_DARK

    p_c_desc1 = h_tf1.add_paragraph()
    p_c_desc1.space_before = Pt(8)
    p_c_desc1.text = "• Cụm rạp đối tác (Rio, Touch, Metiz): Tăng tự nhiên +142.2% (726K views), tự bù 325K views phim lẻ sụt giảm sau lễ."
    p_c_desc1.font.name = FONT_BODY
    p_c_desc1.font.size = Pt(8.5)
    p_c_desc1.font.color.rgb = C_BODY

    p_c_desc2 = h_tf1.add_paragraph()
    p_c_desc2.space_before = Pt(4)
    p_c_desc2.text = "• Chất lượng chuyển đổi: CVR Install sang Map Bank đạt 25.33% (gấp 1.24x CHAOMOMO), mang về 1.808 installs chất lượng cao."
    p_c_desc2.font.name = FONT_BODY
    p_c_desc2.font.size = Pt(8.5)
    p_c_desc2.font.color.rgb = C_BODY

    p_c_desc3 = h_tf1.add_paragraph()
    p_c_desc3.space_before = Pt(4)
    p_c_desc3.text = "• Cam kết Pilot Off-Page: Đưa cụm rạp đạt Top 5.5 Google trước mùa phim Tết 2027; tự chủ năng lực SEO in-house."
    p_c_desc3.font.name = FONT_BODY
    p_c_desc3.font.size = Pt(8.5)
    p_c_desc3.font.color.rgb = C_BODY

    p_c_mile = h_tf1.add_paragraph()
    p_c_mile.space_before = Pt(12)
    r_m1 = p_c_mile.add_run()
    r_m1.text = "Mốc tiến độ: "
    r_m1.font.bold = True
    r_m1.font.size = Pt(8.5)
    r_m1.font.color.rgb = C_PINK
    r_m2 = p_c_mile.add_run()
    r_m2.text = "Đàm phán xong báo chí → Ký hợp đồng trước 05/11 → Triển khai SEO Off-Page → Go-live UI Rạp mới toàn quốc."
    r_m2.font.size = Pt(8.5)
    r_m2.font.color.rgb = C_DARK

    # Financial Hub Card
    hx2 = Inches(5.10)
    h_box2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, hx2, h_y, h_w, h_h)
    h_box2.fill.solid()
    h_box2.fill.fore_color.rgb = C_WHITE
    h_box2.line.color.rgb = C_INDIGO
    h_box2.line.width = Pt(1)

    h_tb2 = s6.shapes.add_textbox(hx2 + Inches(0.18), h_y + Inches(0.16), h_w - Inches(0.36), h_h - Inches(0.32))
    h_tf2 = h_tb2.text_frame
    h_tf2.word_wrap = True
    h_tf2.margin_left = h_tf2.margin_top = h_tf2.margin_right = h_tf2.margin_bottom = 0

    p_f_tag = h_tf2.paragraphs[0]
    p_f_tag.text = "FINANCIAL HUB  •  GHI NHẬN TÍN HIỆU SỚM TÍCH CỰC"
    p_f_tag.font.name = FONT_HEADING
    p_f_tag.font.size = Pt(9.5)
    p_f_tag.font.bold = True
    p_f_tag.font.color.rgb = C_INDIGO

    p_f_stat = h_tf2.add_paragraph()
    p_f_stat.space_before = Pt(6)
    p_f_stat.text = "Lưu lượng MTD: 238.5K   |   Cụm Tỷ Giá: +445%   |   Tỷ lệ tự nhiên: 92.1%"
    p_f_stat.font.name = FONT_HEADING
    p_f_stat.font.size = Pt(9)
    p_f_stat.font.bold = True
    p_f_stat.font.color.rgb = C_DARK

    p_f_desc1 = h_tf2.add_paragraph()
    p_f_desc1.space_before = Pt(8)
    p_f_desc1.text = "• Bùng nổ cụm Tỷ giá (+444.9% MoM): 4 trang ngoại tệ (USD, JPY, EUR, KRW) đạt 34.0K views hoàn toàn tự nhiên không dùng Ads."
    p_f_desc1.font.name = FONT_BODY
    p_f_desc1.font.size = Pt(8.5)
    p_f_desc1.font.color.rgb = C_BODY

    p_f_desc2 = h_tf2.add_paragraph()
    p_f_desc2.space_before = Pt(4)
    p_f_desc2.text = "• Tín dụng & Ví Trả Sau: Điểm CIC đạt 68.3K views, Ví Trả Sau đạt 50.9K views (+57% MoM)."
    p_f_desc2.font.name = FONT_BODY
    p_f_desc2.font.size = Pt(8.5)
    p_f_desc2.font.color.rgb = C_BODY

    p_f_desc3 = h_tf2.add_paragraph()
    p_f_desc3.space_before = Pt(4)
    p_f_desc3.text = "• Chuẩn bị phát hành 2 công cụ Thuế: Tính Thuế TNCN và Thuế Hộ Kinh Doanh online đón mùa quyết toán cuối năm."
    p_f_desc3.font.name = FONT_BODY
    p_f_desc3.font.size = Pt(8.5)
    p_f_desc3.font.color.rgb = C_BODY

    p_f_mile = h_tf2.add_paragraph()
    p_f_mile.space_before = Pt(12)
    r_fm1 = p_f_mile.add_run()
    r_fm1.text = "Mốc tiến độ: "
    r_fm1.font.bold = True
    r_fm1.font.size = Pt(8.5)
    r_fm1.font.color.rgb = C_INDIGO
    r_fm2 = p_f_mile.add_run()
    r_fm2.text = "Hoàn thiện QC công cụ Thuế → Nghiệm thu UI Bank Detail 30/10 → Go-live Thuế TNCN & Hộ KD tháng 11/2026."
    r_fm2.font.size = Pt(8.5)
    r_fm2.font.color.rgb = C_DARK

    add_footer(s6, 6)

    # =========================================================================
    # SLIDE 7: PHỄU CHUYỂN ĐỔI WEB-TO-APP & KHO TIỆN ÍCH [R] (Slide 20 Guidelines)
    # =========================================================================
    s7 = add_blank_slide()
    add_slide_header(s7, 'R', "Phễu Chuyển Đổi Web-to-App & Kho Tiện Ích · Pre-read",
                     "Phễu AppsFlyer Đạt 9.8K Installs, CVR End-to-End Đạt 21.1% Với 2.072 User Map Bank Mới")

    # 4 Funnel Cards
    fn_cards = [
        ("TẦNG 1 · WEB PAGEVIEWS", "3.284.285", "PVs", "Nhịp 117.3K/ngày", C_DARK, C_LIGHT_BG),
        ("TẦNG 2 · ONELINK CLICKS", "14.196", "clicks", "CTR Onsite 0.43%", C_INDIGO, C_INDIGO_BG),
        ("TẦNG 3 · APP INSTALLS", "9.824", "cài mới", "Click-to-Install 69.2%", C_PINK, C_PINK_BG),
        ("TẦNG 4 · MAP BANK USERS", "2.072", "Map Bank", "CVR Toàn Phễu 21.09%", C_GREEN, C_GREEN_BG)
    ]

    fn_w = Inches(2.12)
    fn_gap = Inches(0.16)
    fn_h = Inches(1.80)
    fn_y = Inches(1.10)

    for idx, (label, val, unit, note, color, bg) in enumerate(fn_cards):
        fx = Inches(0.52) + idx * (fn_w + fn_gap)
        f_box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, fx, fn_y, fn_w, fn_h)
        f_box.fill.solid()
        f_box.fill.fore_color.rgb = bg
        f_box.line.color.rgb = color
        f_box.line.width = Pt(1)

        f_tb = s7.shapes.add_textbox(fx + Inches(0.14), fn_y + Inches(0.14), fn_w - Inches(0.28), fn_h - Inches(0.28))
        f_tf = f_tb.text_frame
        f_tf.word_wrap = True
        f_tf.margin_left = f_tf.margin_top = f_tf.margin_right = f_tf.margin_bottom = 0

        p1 = f_tf.paragraphs[0]
        p1.text = label
        p1.font.name = FONT_BODY
        p1.font.size = Pt(8)
        p1.font.bold = True
        p1.font.color.rgb = C_MUTED

        p2 = f_tf.add_paragraph()
        p2.space_before = Pt(8)
        r_v = p2.add_run()
        r_v.text = val + " "
        r_v.font.name = FONT_HEADING
        r_v.font.size = Pt(18)
        r_v.font.bold = True
        r_v.font.color.rgb = color

        r_u = p2.add_run()
        r_u.text = unit
        r_u.font.name = FONT_BODY
        r_u.font.size = Pt(8.5)
        r_u.font.color.rgb = C_MUTED

        p3 = f_tf.add_paragraph()
        p3.space_before = Pt(8)
        p3.text = note
        p3.font.name = FONT_BODY
        p3.font.size = Pt(8)
        p3.font.bold = True
        p3.font.color.rgb = color

    # 4 Online Utilities Cards
    util_cards = [
        ("Phạt Nguội CSGT", "245K views · Cửa ngõ mở App nộp phạt vi phạm giao thông", C_PINK),
        ("Tỷ Giá Ngoại Tệ", "34.0K views (+445%) · Tra cứu tỷ giá & chuyển tiền quốc tế", C_INDIGO),
        ("Giá Vàng Trực Tuyến", "18.5K views · Cập nhật biến động & tích lũy Túi Thần Tài", C_AMBER),
        ("Tính Thuế TNCN & Hộ KD", "Sắp ra mắt T11/2026 · Đón mùa quyết toán thuế cuối năm", C_GREEN),
    ]

    u_w = Inches(2.12)
    u_h = Inches(1.85)
    u_y = Inches(3.15)

    for idx, (u_title, u_desc, u_color) in enumerate(util_cards):
        ux = Inches(0.52) + idx * (u_w + fn_gap)
        u_box = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ux, u_y, u_w, u_h)
        u_box.fill.solid()
        u_box.fill.fore_color.rgb = C_WHITE
        u_box.line.color.rgb = C_BORDER
        u_box.line.width = Pt(1)

        u_tb = s7.shapes.add_textbox(ux + Inches(0.14), u_y + Inches(0.16), u_w - Inches(0.28), u_h - Inches(0.32))
        u_tf = u_tb.text_frame
        u_tf.word_wrap = True
        u_tf.margin_left = u_tf.margin_top = u_tf.margin_right = u_tf.margin_bottom = 0

        p1 = u_tf.paragraphs[0]
        p1.text = u_title
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = C_DARK

        p2 = u_tf.add_paragraph()
        p2.space_before = Pt(8)
        p2.text = u_desc
        p2.font.name = FONT_BODY
        p2.font.size = Pt(8)
        p2.font.color.rgb = C_BODY

    add_footer(s7, 7)

    return prs

def main():
    print("Generating Web Platform Monthly Report PPTX...")
    prs = create_presentation()

    # Targets
    target_repo = "07_REPORTS/docs/presentations/Web_Platform_Thang_10_2026_Monthly_Report.pptx"
    target_dl = "/Users/hienhv/Downloads/Web_Platform_Thang_10_2026_Monthly_Report.pptx"
    target_hubs = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/public/reports/Web_Platform_Thang_10_2026_Monthly_Report.pptx"

    os.makedirs(os.path.dirname(target_repo), exist_ok=True)
    os.makedirs(os.path.dirname(target_hubs), exist_ok=True)

    prs.save(target_repo)
    print(f"✓ Saved repository copy: {target_repo}")

    shutil.copy2(target_repo, target_dl)
    print(f"✓ Saved user Downloads copy: {target_dl}")

    shutil.copy2(target_repo, target_hubs)
    print(f"✓ Saved Hubs public web download copy: {target_hubs}")

if __name__ == "__main__":
    main()
