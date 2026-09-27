import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter


from scripts._lib import load_workbook_safe, save_with_backup, standard_argparser

def main(args=None):
    wb = openpyxl.Workbook()

    # Font definitions
    font_title = Font(name='Calibri', size=14, bold=True, color='1E293B')
    font_subtitle = Font(name='Calibri', size=11, italic=True, color='64748B')
    font_header = Font(name='Calibri', size=11, bold=True, color='1E293B')
    font_section = Font(name='Calibri', size=11, bold=True, color='0F172A')
    font_bold = Font(name='Calibri', size=11, bold=True, color='000000')
    font_regular = Font(name='Calibri', size=11, color='000000')
    font_code = Font(name='Consolas', size=10, color='0F172A')

    # Fills
    fill_header = PatternFill('solid', fgColor='F1F5F9')
    fill_section = PatternFill('solid', fgColor='E2E8F0')
    fill_zebra = PatternFill('solid', fgColor='F8FAFC')
    fill_completed = PatternFill('solid', fgColor='DCFCE7')
    fill_inprogress = PatternFill('solid', fgColor='FEF08A')
    fill_planned = PatternFill('solid', fgColor='F3F4F6')

    # Alignments
    align_left = Alignment(horizontal='left', vertical='center', wrap_text=True)
    align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_right = Alignment(horizontal='right', vertical='center')

    # Borders
    border_thin = Side(style='thin', color='CBD5E1')
    border = Border(left=border_thin, right=border_thin, top=border_thin, bottom=border_thin)

    # Helper function to style table header
    def style_header(ws, row_idx, headers):
        for c_idx, h in enumerate(headers, start=1):
            cell = ws.cell(row=row_idx, column=c_idx, value=h)
            cell.font = font_header
            cell.fill = fill_header
            cell.alignment = align_center
            cell.border = border

    # ==============================================================================
    # 1. SHEET: Readme
    # ==============================================================================
    ws_readme = wb.active
    ws_readme.title = 'Readme'
    ws_readme.views.sheetView[0].showGridLines = True

    ws_readme.cell(row=1, column=1, value='DANH MỤC TÀI LIỆU VÀ HƯỚNG DẪN VẬN HÀNH ROADMAP STUDENT HUB (WEB PLATFORM)').font = font_title
    ws_readme.cell(row=2, column=1, value='Tài liệu SSOT quy hoạch lộ trình phát triển, chỉ số KPI, ma trận từ khóa và ma trận phân công RACI giữa Web Platform & Youth Segment BU (Cập nhật chuẩn hóa cùng Vehicle Hub)').font = font_subtitle

    headers_readme = ['Mã Sheet', 'Tên Trang Tính (Sheet Name)', 'Nội Dung Chi Tiết & Mục Đích Vận Hành']
    style_header(ws_readme, 4, headers_readme)

    readme_data = [
        ['01', 'Readme', 'Trang tổng quan chỉ dẫn danh mục tài liệu, metadata quy hoạch và cấu trúc workbook.'],
        ['02', 'Roadmap', 'Lộ trình phát triển sản phẩm phân rã theo Phase (Phase 1, Phase 2, Phase 3), Timeline, Specs, API & Phễu W2A.'],
        ['03', 'Market Sizing', 'Ma trận nghiên cứu từ khóa 100+ trường ĐH & Cổng Việc Làm, điểm ưu tiên SEO/GEO và phân hạng Tier.'],
        ['04', 'Content', 'Kế hoạch sản xuất 100 bài viết blog cẩm nang học vụ, tân sinh viên & GenAI Content Pipeline.'],
        ['05', 'Traffic', 'Báo cáo lưu lượng truy cập hàng tháng (MTD vs Full Month) phân rã theo nguồn Out-App & In-App.'],
        ['06', 'Resources', 'Ma trận phân định trách nhiệm chi tiết RACI giữa Web Platform Team (GPD) & Youth & Student Segment BU.'],
        ['07', 'Utilities', 'Đặc tả bộ công cụ nhúng dùng chung: AI Resume Builder, ATS Scoring, Bản đồ 5km, Tính học phí, Chia tiền trọ.'],
        ['08', 'Schema', 'Quy chuẩn kiến trúc & Mẫu JSON-LD Schema (WebSite, EducationalOrganization, JobPosting, FAQPage, ItemList).'],
        ['09', 'Sitemap', 'Danh bạ quy hoạch chi tiết các trang con & subpages URL hierarchy phân rã từ gốc /sinh-vien.'],
        ['10', 'Tracking Flow', 'Bảng đặc tả luồng tracking sự kiện Web-to-App, OneLink parameters & GA4 Custom Events.'],
        ['11', 'Tracking Classes', 'Quy chuẩn đặt tên HTML CSS tracking classes phục vụ đo lường tương tác nút bấm trên Web.']
    ]

    for r_idx, row_val in enumerate(readme_data, start=5):
        for c_idx, val in enumerate(row_val, start=1):
            cell = ws_readme.cell(row=r_idx, column=c_idx, value=val)
            cell.font = font_regular
            cell.border = border
            cell.alignment = align_center if c_idx == 1 else align_left

    ws_readme.cell(row=17, column=1, value='THÔNG TIN METADATA & PHÊ DUYỆT CHIẾN LƯỢC').font = font_section
    ws_readme.cell(row=17, column=1).fill = fill_section
    ws_readme.merge_cells('A17:C17')

    meta_info = [
        ('Dự Án / Sản Phẩm', 'MoMo Student Hub (Discovery Platform & Unified Student Gateway)'),
        ('Tên Miền / Cổng Trọng Điểm', 'momo.vn/sinh-vien | Cổng Việc Làm Master: momo.vn/sinh-vien/viec-lam'),
        ('Khung Thời Gian Vận Hành', 'Quý 3/2026 - Quý 4/2026 (Standing Year-Round Platform)'),
        ('Đơn Vị Chủ Quản Web', 'Growth Platform Division (GPD) - Web Platform Team'),
        ('Đơn Vị Đồng Hành BU', 'Youth & Student Segment BU'),
        ('Trạng Thái Triển Khai', 'Phase 1 Go-live Staging/Dev | Phase 2 In Progress | Phase 3 Planned (Q4/2026)')
    ]

    for m_idx, (k, v) in enumerate(meta_info, start=18):
        ws_readme.cell(row=m_idx, column=1, value=k).font = font_bold
        ws_readme.cell(row=m_idx, column=2, value=v).font = font_regular
        for c_k in range(1, 4):
            ws_readme.cell(row=m_idx, column=c_k).border = border

    # ==============================================================================
    # 2. SHEET: Roadmap
    # ==============================================================================
    ws_roadmap = wb.create_sheet('Roadmap')
    ws_roadmap.views.sheetView[0].showGridLines = True

    ws_roadmap.cell(row=1, column=1, value='LỘ TRÌNH PHÁT TRIỂN SẢN PHẨM STUDENT HUB (STUDENT HUB ROADMAP 2026)').font = font_title
    ws_roadmap.cell(row=2, column=1, value='Quy hoạch 3 Phase chiến lược từ Foundation (Pilot 12 trường) -> Ambassador & Realtime Event -> Career Master & pSEO Scale 100+ trường (Chuẩn hóa cấu trúc Vehicle Hub).').font = font_subtitle

    headers_roadmap = ['Phase', 'Thời Gian', 'Giai Đoạn & Nhóm Dịch Vụ', 'Tên Trang / Utility / Công Việc', 'Mô Tả Sản Phẩm & Quy Hoạch Kỹ Thuật (UX/UI & Specs)', 'Dữ Liệu, API & Phối Hợp Kỹ Thuật', 'Phễu Chuyển Đổi Kinh Doanh (Web-to-App)']
    style_header(ws_roadmap, 4, headers_roadmap)

    roadmap_rows = [
        ['Phase 1.0', 'Tháng 8/2026', 'Gateway | Core Hub', 'Student Hub Master Landing Page (/sinh-vien)', '• Dựng khung HTML/CSS Master Hub với Hero Banner Student Pass, Widget Bạn Đồng Hành MoMo, 5 Content Pillars, Top 12 Trường ĐH.\n• Tích hợp Schema @graph chuẩn hóa (WebSite, EducationalOrganization, Service).\n• ĐÃ HOÀN TẤT & GO-LIVE TRÊN PRODUCTION.', '- Design Tokens & Component Library từ MoMo Design System (MoBase Web)\n- Tracking schema chuẩn GA4/GTM\n- Asset hình ảnh thương hiệu Student Pass & Banner Back2School', 'Entry Points Onelink & Dynamic QR dẫn vào Mini App Student Pass In-App; Nút CTA "Xác thực ngay / Nhận đặc quyền".'],
        ['Phase 1.1', 'Tháng 8-9/2026', 'Information & Admission | pSEO', '12 Trang Trường Đại Học Trọng Điểm (/sinh-vien/[truong-slug])', '• Xây dựng 12 trang trường trọng điểm (UEH, FTU, TDTU, HCMUT, VLU, HUST, NEU, HANU, HAU, USSH, HUIT, UEL).\n• Tích hợp 4 JTBD: (1) Học phí tín chỉ, (2) Điểm chuẩn 3 năm, (3) Tiện ích quanh campus 5km, (4) Thẻ Sinh Viên Số Custom Card UI.\n• ĐÃ HOÀN TẤT & GO-LIVE ON STAGING/DEV.', '- File Content Structure Master Data của 12 trường ĐH\n- DB Điểm chuẩn & Học phí tín chỉ các năm\n- Google Transit API & Apify Location POI quanh campus', 'Anchor links #hoc-phi, #diem-chuan & OneLink eKYC Thẻ Sinh Viên Số custom theo từng trường ĐH.'],
        ['Phase 1.2', 'Tuần 3-4 Tháng 9/2026', 'Content & SEO Pipeline', 'Blog & Content Production (100 Articles)', '• Xuất bản 100 bài viết cẩm nang chất lượng cao: Cẩm nang tân sinh viên, quy chế học vụ, thuê trọ an toàn, quản lý chi tiêu, kỹ năng mềm AI.\n• Thiết lập cấu trúc Topic Cluster & Internal Linking dẫn sâu về các trang Trường & Tool.', '- Kế hoạch biên tập chi tiết 100 bài viết từ Content Team\n- Bộ từ khóa SEO phân cấp từ kho Search Volume\n- Widget Onelink nhúng trong bài viết blog', 'Inline Banner điều hướng sử dụng dịch vụ tài chính sinh viên & Student Pass trên App MoMo.'],
        ['Phase 2.1', 'Tháng 9/2026', 'Ambassador Engine', 'Trang Đại Sứ Sinh Viên MoMo (/sinh-vien/ambassador)', '• Trang Showcase Project Đại sứ sinh viên (5-7 nhóm đại sứ, bảng thành tích 1 năm).\n• Công cụ giao nhiệm vụ tự động và Leaderboard vinh danh đại sứ xuất sắc.\n(Search Volume: 25.000 search/tháng)', '- Database 50 Đại sứ sinh viên chính thức\n- System tích lũy điểm thưởng & Bảng xếp hạng Leaderboard In-App', 'Nút CTA "Đăng ký trở thành Đại Sứ Sinh Viên MoMo" mở phễu đăng ký In-App.'],
        ['Phase 2.2', '26-27/09/2026', 'Realtime O2O Event', 'Module Photobooth Real-time Event Offline Campus', '• Xây dựng Web Photobooth Real-time cho Offline Event Campus 26-27/09.\n• Sinh viên chụp ảnh tại Booth -> Upload Web -> Nhận ảnh có khung MoMo Student Pass -> Tích lũy footprint nhận quà trực tiếp.', '- Web Realtime Image Storage & Frame Generation Service\n- QR Scanner tại gian hàng Offline Event', 'Quét QR Code nhận voucher 50K & Kích hoạt Thẻ Sinh Viên Số ngay tại sự kiện.'],
        ['Phase 3.1', 'Tháng 10-11/2026', 'Career & AI Resume Master', 'Cổng Việc Làm Sinh Viên Master (/sinh-vien/viec-lam)', '• Cổng Việc Làm Master (/sinh-vien/viec-lam) kết hợp AI Resume Builder.\n• Lọc việc làm part-time/thực tập bán kính 5km quanh campus từ đối tác F&B/bán lẻ MoMo (Highlands, Circle K, KFC, Co.opmart...).\n• GenAI Resume Builder tạo CV PDF chuẩn ATS & chấm điểm ATS Score thời gian thực.\n• 1-Tap Apply via Student Pass (xác thực sinh viên mở gói đặc quyền voucher & Ví Trả Sau 0% HSSV - KHÔNG CÓ luồng nhận lương qua Ví).\n(Search Volume: 125.000 search/tháng)', '- Database việc làm part-time từ Merchant Partnership Team\n- MoMo GenAI ATS Resume Engine Service\n- API xác thực Thẻ Sinh Viên Số In-App', 'Nút CTA "Ứng Tuyển Qua Student Pass" -> OneLink mở App MoMo eKYC Thẻ Sinh Viên Số -> Mở Ví Trả Sau 0% HSSV.'],
        ['Phase 3.2', 'Tháng 10-12/2026', 'Programmatic pSEO Scale', 'Hệ Thống pSEO Scale-out 100+ Trang Trường ĐH/CĐ (/sinh-vien/[truong-slug])', '• Programmatic pSEO Engine tự động tạo 100+ trang trường ĐH/CĐ toàn quốc theo các Tier (Tier 1 >100K search, Tier 2 50K-100K).\n• Tự động hóa MoSpark GenAI Content Pipeline cập nhật điểm chuẩn, học phí, đánh giá UGC.', '- Programmatic Content Generation Engine\n- Master Data 100+ Trường ĐH/CĐ toàn quốc', 'OneLink eKYC Thẻ Sinh Viên Số cá nhân hóa theo từng trường.'],
        ['Phase 3.3', 'Tháng 11-12/2026', 'Sub-pages Ecosystem', 'Sub-pages Chuyên Biệt (/nha-tro, /review, /workshop)', '• Mở rộng Sub-page Nhà trọ & KTX (/nha-tro) kết hợp bản đồ an toàn quanh trường.\n• Sub-page Review UGC Chi tiết (/review) vinh danh Top Reviewers.\n• Sub-page Webinar & Workshop (/workshop) đăng ký tham gia sự kiện kỹ năng/AI sinh viên.', '- Data danh bạ nhà trọ sạch từ Apify Google Maps\n- UGC Review & Rating Engine\n- Event Management Service', 'Nút CTA "Tìm Phòng Trọ An Toàn" + "Đăng Ký Workshop Kỹ Năng".']
    ]

    for r_offset, r_data in enumerate(roadmap_rows, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_roadmap.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 2, 4] else font_regular
            cell.border = border
            cell.alignment = align_center if c_idx in [1, 2] else align_left
            if 'Phase 1' in r_data[0]:
                cell.fill = fill_completed
            elif 'Phase 2' in r_data[0]:
                cell.fill = fill_inprogress
            else:
                cell.fill = fill_planned

    # ==============================================================================
    # 3. SHEET: Market Sizing
    # ==============================================================================
    ws_ms = wb.create_sheet('Market Sizing')
    ws_ms.views.sheetView[0].showGridLines = True

    ws_ms.cell(row=1, column=1, value='MA TRẬN NGUYÊN CỨU TỪ KHÓA & MARKET SIZE CÁC TRƯỜNG ĐẠI HỌC (STUDENT HUB)').font = font_title
    ws_ms.cell(row=2, column=1, value='Trích xuất 100% dữ liệu Search Volume theo cụm từ khóa trường học & việc làm từ Content Structure Master Document.').font = font_subtitle

    headers_ms = ['Cụm Chủ Đề Từ Khóa Trường (Cluster)', 'Search/tháng (Mẫu 5 Trường)', 'Volume Score (1-10)', 'Intent Score (1-5)', 'Monetization Score (1-5)', 'Data Seed Score (1-5)', 'Điểm Ưu Tiên', 'Tier Phân Hạng', 'Nhóm Định Hướng Chiến Lược']
    style_header(ws_ms, 4, headers_ms)

    ws_ms.cell(row=1, column=12, value='TRỌNG SỐ ĐÁNH GIÁ (WEIGHTS)').font = font_section
    weights = [('Weight Volume', 0.35), ('Weight Intent', 0.25), ('Weight Monetization', 0.25), ('Weight Data Seed', 0.15)]
    for w_idx, (w_name, w_val) in enumerate(weights, start=1):
        ws_ms.cell(row=w_idx+1, column=12, value=w_name).font = font_bold
        ws_ms.cell(row=w_idx+1, column=13, value=w_val).font = font_regular
        ws_ms.cell(row=w_idx+1, column=13).number_format = '0.00%'

    ms_data = [
        ['Cụm 5 - Việc làm Part-time & AI Resume (/viec-lam)', 12500, 10, 5, 5, 2, 'Nhóm 1 - Career & Monetization'],
        ['Cụm 4A - Điểm rèn luyện & Đánh giá cá nhân', 10260, 10, 3, 2, 1, 'Nhóm 1 - Engagement Magnet'],
        ['Cụm 1 - Tuyển sinh, Điểm chuẩn & Xếp hạng', 7820, 9, 4, 2, 2, 'Nhóm 1 - Information & Admission'],
        ['Cụm 3 - Đời sống sinh viên, KTX & Campus', 4730, 8, 4, 3, 1, 'Nhóm 1 - Campus Life & Accommodation'],
        ['Cụm 2 - Học phí & Học bổng Sinh viên', 3400, 7, 5, 4, 2, 'Nhóm 1 - Flagship Financial Utility'],
        ['Cụm 6 - Văn bằng 2 & Chương trình mở rộng', 2160, 6, 3, 2, 1, 'Nhóm 2 - Academic Expansion'],
        ['Cụm 4B - Đăng ký tín chỉ & Quy chế học vụ', 190, 4, 4, 2, 1, 'Nhóm 2 - Academic Rules']
    ]

    for r_offset, r_data in enumerate(ms_data, start=5):
        ws_ms.cell(row=r_offset, column=1, value=r_data[0]).font = font_bold
        ws_ms.cell(row=r_offset, column=2, value=r_data[1]).font = font_regular
        ws_ms.cell(row=r_offset, column=2).number_format = '#,##0'
        ws_ms.cell(row=r_offset, column=3, value=r_data[2]).font = font_regular
        ws_ms.cell(row=r_offset, column=4, value=r_data[3]).font = font_regular
        ws_ms.cell(row=r_offset, column=5, value=r_data[4]).font = font_regular
        ws_ms.cell(row=r_offset, column=6, value=r_data[5]).font = font_regular
    
        # Priority Formula
        formula_score = f"=(C{r_offset}*$M$2 + D{r_offset}*$M$3 + E{r_offset}*$M$4)/10 + F{r_offset}*$M$5"
        cell_score = ws_ms.cell(row=r_offset, column=7, value=formula_score)
        cell_score.font = font_bold
        cell_score.number_format = '0.00'
    
        # Tier Formula
        formula_tier = f'=IF(G{r_offset}>=0.75, "High (P1)", IF(G{r_offset}>=0.55, "Medium (P2)", "Low (P3)"))'
        cell_tier = ws_ms.cell(row=r_offset, column=8, value=formula_tier)
        cell_tier.font = font_bold
        cell_tier.alignment = align_center
    
        ws_ms.cell(row=r_offset, column=9, value=r_data[6]).font = font_regular
    
        for col_i in range(1, 10):
            cell_curr = ws_ms.cell(row=r_offset, column=col_i)
            cell_curr.border = border
            if col_i in [2,3,4,5,6,7]:
                cell_curr.alignment = align_right if col_i in [2,7] else align_center

    # ==============================================================================
    # 4. SHEET: Content
    # ==============================================================================
    ws_content = wb.create_sheet('Content')
    ws_content.views.sheetView[0].showGridLines = True

    ws_content.cell(row=1, column=1, value='KẾ HOẠCH SẢN XUẤT NỘI DUNG BLOG & CẨM NANG HỌC VỤ (100 ARTICLES CONTENT PLAN)').font = font_title
    ws_content.cell(row=2, column=1, value='Quy hoạch 100 bài viết cẩm nang theo 5 Content Pillars, vận hành bằng MoSpark GenAI Content Pipeline.').font = font_subtitle

    headers_content = ['STT', 'Pillar / Chủ Đề Trọng Tâm', 'Tiêu Đề Bài Viết Đề Xuất (Article Title)', 'Cụm Từ Khóa SEO Chính (Target Keyword)', 'Volume Search/tháng', 'Target URL Slug', 'CTA Anchor Link / Widget', 'Trạng Thái']
    style_header(ws_content, 4, headers_content)

    sample_content = [
        [1, 'Pillar 1: Học Vụ & Quy Định', 'Cách tính điểm rèn luyện đại học chuẩn nhất 2026', 'điểm rèn luyện đại học', 10260, '/sinh-vien/cam-nang/cach-tinh-diem-ren-luyen', 'Widget Bạn Đồng Hành MoMo', 'Completed'],
        [2, 'Pillar 1: Học Vụ & Quy Định', 'Điểm chuẩn Đại học Kinh tế TP.HCM (UEH) 3 năm gần nhất', 'điểm chuẩn ueh', 7820, '/sinh-vien/ueh', 'Anchor link #diem-chuan', 'Completed'],
        [3, 'Pillar 2: Chi Tiêu & Tài Chính', 'Kinh nghiệm thuê nhà trọ sinh viên giá rẻ an toàn gần trường', 'thuê nhà trọ sinh viên', 4730, '/sinh-vien/cam-nang/kinh-nghiem-thue-tro', 'Banner Bản đồ nhà trọ 5km', 'Completed'],
        [4, 'Pillar 2: Chi Tiêu & Tài Chính', 'Học phí Đại học Ngoại thương (FTU) 2026 bao nhiêu một tín chỉ?', 'học phí ftu', 3400, '/sinh-vien/ftu', 'Utility Tính Học Phí Tín Chỉ', 'Completed'],
        [5, 'Pillar 5: Việc Làm & AI Resume', 'Top 10 việc làm part-time cho sinh viên lương cao gần campus', 'việc làm part time sinh viên', 12500, '/sinh-vien/viec-lam', 'AI Resume Builder & ATS Score', 'Planned'],
        [6, 'Pillar 5: Việc Làm & AI Resume', 'Cách viết CV thực tập sinh chuẩn ATS cho sinh viên chưa có kinh nghiệm', 'mẫu cv thực tập sinh chuẩn ats', 8900, '/sinh-vien/viec-lam', 'Tải CV PDF 1-Tap qua Student Pass', 'Planned'],
        [7, 'Pillar 3: Campus Life', 'Tổng hợp tuyến xe buýt đến Đại học Bách Khoa TP.HCM (HCMUT)', 'xe buýt đến bách khoa', 2160, '/sinh-vien/hcmut', 'Map Xe buýt & Thẻ sinh viên', 'Completed']
    ]

    for r_offset, r_data in enumerate(sample_content, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_content.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 3] else font_regular
            cell.border = border
            cell.alignment = align_center if c_idx in [1, 5, 8] else align_left
            if c_idx == 5:
                cell.number_format = '#,##0'
            if c_idx == 6:
                cell.font = font_code

    # ==============================================================================
    # 5. SHEET: Traffic
    # ==============================================================================
    ws_traffic = wb.create_sheet('Traffic')
    ws_traffic.views.sheetView[0].showGridLines = True

    ws_traffic.cell(row=1, column=1, value='BÁO CÁO HIỆU SUẤT TRUY CẬP PHÂN RÃ MTD & FULL MONTH (STUDENT HUB OUTAPP & INAPP)').font = font_title
    ws_traffic.cell(row=2, column=1, value='Chuẩn hóa theo cấu trúc báo cáo Web Platform: Phân rã lưu lượng MTD vs Full Month (T5/2026 - T9/2026 MTD).').font = font_subtitle

    headers_traffic = ['Chỉ Số / Kênh Lưu Lượng (Source Group)', 'T5/2026 (Full)', 'T6/2026 (Full)', 'T7/2026 (Full)', 'T7/2026 (MTD 28d)', 'T8/2026 (MTD 28d)', 'T8/2026 (Full)', 'T9/2026 (MTD 8d)', 'MoM MTD (%)']
    style_header(ws_traffic, 5, headers_traffic)

    traffic_rows = [
        ['TỔNG CỘNG PAGE VIEWS (ALL SOURCES)', 303, 223, 438, 64, 260, 13789, 4209],
        ['1. STUDENT PASS (In-App & DeepLink Sub-total)', 303, 223, 438, 64, 260, 13527, 4137],
        ['   - Direct Traffic', 24, 24, 16, 2, 24, 6592, 357],
        ['   - Organic Search', 268, 183, 391, 46, 229, 4471, 1526],
        ['   - Paid Traffic', 0, 1, 0, 0, 0, 1942, 2199],
        ['   - Referral Traffic', 10, 13, 22, 8, 1, 408, 45],
        ['   - Others', 1, 2, 9, 8, 6, 114, 10],
        ['2. STUDENT HUB WEB (momo.vn/sinh-vien OutApp)', 0, 0, 0, 0, 0, 262, 72],
        ['   - Organic Search (Master & School Pages)', 0, 0, 0, 0, 0, 199, 60],
        ['   - Organic Search (Cổng Việc Làm /viec-lam)', 0, 0, 0, 0, 0, 0, 12]
    ]

    for r_offset, r_data in enumerate(traffic_rows, start=6):
        is_main_head = r_data[0].startswith('TỔNG CỘNG') or r_data[0].startswith('1.') or r_data[0].startswith('2.')
        for c_idx in range(1, 9):
            val = r_data[c_idx-1]
            cell = ws_traffic.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if is_main_head else font_regular
            cell.border = border
            if c_idx == 1:
                cell.alignment = align_left
                if is_main_head:
                    cell.fill = fill_section
            else:
                cell.alignment = align_right
                cell.number_format = '#,##0'
            
        mom_formula = f'=IF(E{r_offset}>0, (F{r_offset}-E{r_offset})/E{r_offset}, "N/A")'
        cell_mom = ws_traffic.cell(row=r_offset, column=9, value=mom_formula)
        cell_mom.font = font_bold if is_main_head else font_regular
        cell_mom.border = border
        cell_mom.alignment = align_right
        cell_mom.number_format = '+0.00%;-0.00%;0.00%'

    # ==============================================================================
    # 6. SHEET: Resources (RACI)
    # ==============================================================================
    ws_res = wb.create_sheet('Resources')
    ws_res.views.sheetView[0].showGridLines = True

    ws_res.cell(row=1, column=1, value='MA TRẬN PHÂN ĐỊNH TRÁCH NHIỆM RACI: WEB PLATFORM x YOUTH & STUDENT SEGMENT BU').font = font_title
    ws_res.cell(row=2, column=1, value='Quy định rõ trách nhiệm triển khai giữa Web Platform Team (GPD) & Youth Segment BU cho toàn bộ các nhóm đầu việc.').font = font_subtitle

    headers_res = ['Hạng Mục / Đầu Việc Triển Khai', 'Web Platform Team', 'Youth & Student Segment BU', 'Mô Tả Trách Nhiệm Chi Tiết & Tiêu Chí Nghiệm Thu']
    style_header(ws_res, 5, headers_res)

    res_sections = [
        ('NHÓM I: CHIẾN LƯỢC TĂNG TRƯỞNG & VẬN HÀNH SPRINT', [
            ('1.1 Hoạch Định Kế Hoạch Tăng Trưởng Tổng Thể (Growth Plan)', 'Consulted (C)', 'Key Owner (A/R)', 'Youth Segment BU chịu trách nhiệm toàn diện về Growth Plan tổng thể, cấp ngân sách Marketing, tài trợ gói Student Pass và cam kết chỉ tiêu kinh doanh (70.000 New Verified Students, 1.5M MEU).'),
            ('1.2 Lập Kế Hoạch Sprint Web 1 Tháng & Nhịp Check-in Định Kỳ', 'Key Owner (A/R)', 'Co-Owner (A/R)', 'Web Platform chủ trì tổ chức Sprint Planning đầu tháng để chốt backlog tính năng Web; Youth Segment BU đồng chủ trì check-in ngày 15 & 30 hàng tháng để rà soát KPI.')
        ]),
        ('NHÓM II: THIẾT KẾ & XÂY DỰNG SẢN PHẨM WEB (PRODUCT UI/UX)', [
            ('2.1 Thiết Kế Giao Diện UI/UX & Phễu Chuyển Đổi (Gen Z UX)', 'Key Owner (A/R)', 'Consulted (C)', 'Web Platform chịu trách nhiệm thiết kế toàn bộ luồng trải nghiệm UI/UX phong cách Gen Z cho Master Gateway (/sinh-vien), trang 100+ trường ĐH và Cổng Việc Làm (/viec-lam).'),
            ('2.2 Lập Trình Frontend Web & AI Resume Builder Engine', 'Key Owner (A/R)', 'Consulted (C)', 'Web Platform trực tiếp lập trình giao diện Web trên Next.js/MoSpark, phát triển công cụ AI Resume Builder (ATS Scoring) và Bản đồ việc làm 5km quanh campus.'),
            ('2.3 Kiểm Thử & Nghiệm Thu Chất Lượng Sản Phẩm (Product QC)', 'Contributor (R)', 'QC Owner (A/R)', 'Youth Segment BU giữ vai trò QC Owner chịu trách nhiệm nghiệm thu sản phẩm cuối cùng (Product QC), kiểm thử luồng Onelink điều hướng sang App MoMo.')
        ]),
        ('NHÓM III: CỔNG VIỆC LÀM & ĐỐI TÁC THƯƠNG MẠI (CAREER & MERCHANT JOBS)', [
            ('3.1 Kết Nối Nguồn Tin Tuyển Dụng Merchant F&B/Bán Lẻ', 'Consulted (C)', 'Key Owner (A/R)', 'Youth Segment BU phối hợp Merchant Partnership Team đưa danh sách tuyển dụng part-time của đối tác MoMo (Highlands, Circle K, KFC...) lên hệ thống.'),
            ('3.2 Vận Hành Phễu Ứng Tuyển & Kích Hoạt Student Pass', 'Key Owner (A/R)', 'Co-Owner (A/R)', 'Web Platform vận hành phễu 1-Tap Apply qua Web; Youth Segment BU chịu trách nhiệm kích hoạt gói voucher đặc quyền & Ví Trả Sau 0% HSSV.')
        ]),
        ('NHÓM IV: NỘI DUNG, SẢN XUẤT & KIỂM DUYỆT (CONTENT PLAN & QC)', [
            ('4.1 Xây Dựng Kế Hoạch Nội Dung & Từ Khóa SEO (Content Plan)', 'Key Owner (A/R)', 'Consulted (C)', 'Web Platform chịu trách nhiệm lập kế hoạch nội dung toàn diện (Content Plan), nghiên cứu cụm từ khóa 12 Trường ĐH trọng điểm & Cổng Việc Làm.'),
            ('4.2 Sản Xuất Nội Dung Bài Viết & Cẩm Nang Qua GenAI Pipeline', 'Key Owner (A/R)', 'Consulted (C)', 'Web Platform vận hành MoSpark GenAI Pipeline tự động hóa sản xuất bài viết cẩm nang học vụ và review trường học.'),
            ('4.3 Phê Duyệt & Kiểm Duyệt Chất Lượng Nội Dung (Content QC)', 'Contributor (R)', 'QC Owner (A/R)', 'Youth Segment BU giữ vai trò Content QC Owner kiểm duyệt 100% nội dung trước khi xuất bản chính thức.')
        ])
    ]

    curr_row = 6
    for sec_title, items in res_sections:
        cell_sec = ws_res.cell(row=curr_row, column=1, value=sec_title)
        cell_sec.font = font_section
        cell_sec.fill = fill_section
        ws_res.merge_cells(start_row=curr_row, start_column=1, end_row=curr_row, end_column=4)
        for col_k in range(1, 5):
            ws_res.cell(row=curr_row, column=col_k).border = border
        curr_row += 1
    
        for item_title, r_web, r_bu, r_desc in items:
            ws_res.cell(row=curr_row, column=1, value=item_title).font = font_bold
            ws_res.cell(row=curr_row, column=2, value=r_web).font = font_bold
            ws_res.cell(row=curr_row, column=3, value=r_bu).font = font_bold
            ws_res.cell(row=curr_row, column=4, value=r_desc).font = font_regular
        
            for col_k in range(1, 5):
                c_item = ws_res.cell(row=curr_row, column=col_k)
                c_item.border = border
                if col_k in [2, 3]:
                    c_item.alignment = align_center
                elif col_k == 4:
                    c_item.alignment = align_left
            curr_row += 1

    # ==============================================================================
    # 7. SHEET: Utilities
    # ==============================================================================
    ws_util = wb.create_sheet('Utilities')
    ws_util.views.sheetView[0].showGridLines = True

    ws_util.cell(row=1, column=1, value='ĐẶC TẢ BỘ TIỆN ÍCH DÙNG CHUNG & CÔNG THỨC NGHIỆP VỤ (EMBEDDABLE UTILITIES & FORMULAS)').font = font_title
    ws_util.cell(row=2, column=1, value='Toàn bộ Widget/Công cụ tính toán được thiết kế độc lập dạng Embeddable Components, có thể nhúng linh hoạt vào bất kỳ trang hoặc bài viết nào.').font = font_subtitle

    headers_util = ['STT', 'Tên Tiện Ích / Widget (Component)', 'Định Dạng Component (UI Format)', 'Mục Đích Sử Dụng (JTBD)', 'Trường Dữ Liệu Đầu Vào (Inputs)', 'Công Thức Tính Toán & Logic Nghiệp Vụ (Formulas / Rules)', 'Kết Quả Trả Về (Outputs)', 'Hành Động Chuyển Đổi (W2A CTA)', 'Khả Năng Nhúng Đa Điểm Chạm (Embeddable Scope)']
    style_header(ws_util, 4, headers_util)

    util_data = [
        [1, 'AI Resume Builder & ATS Scoring', 'Interactive Modal / Full-page Tool', 'Tạo CV chuẩn ATS và chấm điểm phù hợp công việc trong 1 phút', 'Họ tên, Trường, Ngành, Kỹ năng, Kinh nghiệm, JD Công việc', 'GenAI Prompt Engine chuẩn hóa Action Verbs + Vector Match Score (0-100%)', 'Bản xem trước CV PDF + Điểm ATS + Gợi ý tối ưu câu từ', 'Nút "Tải CV PDF / Ứng Tuyển Nhanh 1-Tap" qua Student Pass In-App', 'Master Gateway /viec-lam, Trang trường ĐH, Bài viết blog việc làm'],
        [2, 'Bản Đồ Việc Làm Campus 5km', 'Interactive Location Map Component', 'Lọc việc làm part-time/thực tập bán kính 5km quanh trường sinh viên học', 'Định vị GPS / Chọn Trường ĐH + Bán kính (500m, 1km, 3km, 5km) + Loại hình', 'Geofencing Radius Query từ DB Merchant Jobs của MoMo', 'Danh sách & vị trí cửa hàng F&B/bán lẻ tuyển part-time trên bản đồ', 'Nút "Ứng Tuyển Ngay" mở phễu eKYC Student Pass', 'Master Gateway /viec-lam, Trang chi tiết trường ĐH'],
        [3, 'Utility Tính Học Phí Theo Tín Chỉ', 'Credit Slider Component', 'Giả lập tổng tiền học phí theo số lượng tín chỉ đăng ký học kỳ', 'Chọn Trường + Số tín chỉ (12 - 30 tín chỉ) + Khóa học', 'Sum = Số_tín_chỉ * Đơn_giá_tín_chỉ_theo_ngành + Phí_cơ_sở_vật_chất', 'Tổng tiền học phí dự kiến + Phân rã chi tiết + Thông tin học bổng', 'Nút "Nộp Học Phí Ngay" mở phễu thanh toán In-App', 'Trang chi tiết trường ĐH (#hoc-phi), Bài viết cẩm nang học phí'],
        [4, 'AI Bill Splitter (Chia Tiền Trọ)', 'Interactive Financial Calculator', 'Chia đều tiền nhà trọ, điện nước, ăn uống cho nhóm sinh viên ở chung', 'Tổng tiền nhà + Tiền điện (chỉ số cũ/mới) + Tiền nước + Số người ở', 'Tiền_mỗi_người = (Tiền_nhà + Tiền_điện_nước + Phí_khác) / Số_người', 'Bảng phân bổ số tiền chính xác từng thành viên + QR Chuyển tiền', 'Nút "Tạo Mã QR Chuyển Tiền Chia Hóa Đơn" mở Ví MoMo', 'Sub-page Nhà trọ (/nha-tro), Bài viết cẩm nang thuê trọ'],
        [5, 'Quản Gia Chi Tiêu 50/30/20', 'Budget Planner Widget', 'Gợi ý phân bổ ngân sách sinh hoạt hàng tháng cho tân sinh viên', 'Tổng thu nhập/trợ cấp hàng tháng (VNĐ)', 'Essential = 50% | Personal = 30% | Savings/Invest = 20%', '3 Hũ chi tiêu chi tiết (Thiết yếu, Cho bản thân, Tích lũy)', 'Nút "Mở Túi Thần Tài Tích Lũy 20%" + "Mở Ví Trả Sau 0%"', 'Master Gateway /sinh-vien, Bài viết quản lý tài chính']
    ]

    for r_offset, r_data in enumerate(util_data, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_util.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 2] else font_regular
            cell.border = border
            cell.alignment = align_center if c_idx in [1, 3] else align_left

    # ==============================================================================
    # 8. SHEET: Schema
    # ==============================================================================
    ws_schema = wb.create_sheet('Schema')
    ws_schema.views.sheetView[0].showGridLines = True

    ws_schema.cell(row=1, column=1, value='QUY CHUẨN KIẾN TRÚC VÀ MẪU SCHEMA SCRIPT JSON-LD CHO TỪNG TRANG STUDENT HUB').font = font_title
    ws_schema.cell(row=2, column=1, value='Tuân thủ tiêu chuẩn Google Search Central & Schema.org | Tối ưu Rich Snippets & AI Overviews (AIO).').font = font_subtitle

    headers_schema = ['STT', 'Tên Loại Trang (Page Type)', 'URL Pattern', 'Trạng Thái', 'Schema Types Bắt Buộc', 'Mục Đích Tối Ưu SEO/GEO & AIO', 'Cấu Trúc JSON-LD Snippet Mẫu']
    style_header(ws_schema, 4, headers_schema)

    schema_data = [
        [1, 'Trang Chủ Master Hub', '/sinh-vien', 'Go-live Production', 'WebSite, EducationalOrganization, Service, ItemList', 'Xác thực Entity thương hiệu MoMo Student Hub; Sitelinks Search Box; Google AI Overview.', '{\n  "@context": "https://schema.org",\n  "@graph": [\n    {\n      "@type": "WebSite",\n      "name": "MoMo Student Hub",\n      "url": "https://www.momo.vn/sinh-vien"\n    },\n    {\n      "@type": "EducationalOrganization",\n      "name": "MoMo Student Pass Ecosystem",\n      "url": "https://www.momo.vn/sinh-vien"\n    }\n  ]\n}'],
        [2, 'Trang Trường Đại Học', '/sinh-vien/[truong-slug]', 'Go-live Staging/Dev', 'CollegeOrUniversity, Course, FAQPage, FinancialProduct', 'Tối ưu từ khóa "Review + Học phí + Điểm chuẩn tên trường"; Rich Snippet FAQ & Tín chỉ.', '{\n  "@context": "https://schema.org",\n  "@type": "CollegeOrUniversity",\n  "name": "Đại học Kinh tế TP.HCM (UEH)",\n  "url": "https://www.momo.vn/sinh-vien/ueh"\n}'],
        [3, 'Cổng Việc Làm Master', '/sinh-vien/viec-lam', 'Planned (Q4/2026)', 'JobPosting, ItemList, Service, FAQPage', 'Tối ưu Google Jobs Search Engine & Rich Snippets "việc làm sinh viên part-time".', '{\n  "@context": "https://schema.org",\n  "@type": "JobPosting",\n  "title": "Nhân viên Part-time Highlands Coffee Campus UEH",\n  "employmentType": "PART_TIME",\n  "hiringOrganization": { "@type": "Organization", "name": "Highlands Coffee" }\n}']
    ]

    for r_offset, r_data in enumerate(schema_data, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_schema.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 2] else font_regular
            cell.border = border
            cell.alignment = align_center if c_idx in [1, 3, 4] else align_left
            if c_idx == 7:
                cell.font = font_code

    # ==============================================================================
    # 9. SHEET: Sitemap
    # ==============================================================================
    ws_sitemap = wb.create_sheet('Sitemap')
    ws_sitemap.views.sheetView[0].showGridLines = True

    ws_sitemap.cell(row=1, column=1, value='DANH BẠ QUY HOẠCH CHI TIẾT CÁC TRANG CON & SUBPAGES ARCHITECTURE (SITEMAP)').font = font_title
    ws_sitemap.cell(row=2, column=1, value='Cấu trúc đường dẫn URL tổng thể phân rã chuẩn Subdirectory từ gốc /sinh-vien.').font = font_subtitle

    headers_sitemap = ['STT', 'Nhóm Dịch Vụ', 'Tên Trang (Page Name)', 'URL Pattern', 'Từ Khóa SEO Mục Tiêu (Target Keywords)', 'Mô Tả Chức Năng & Trải Nghiệm UX', 'Giai Đoạn Go-live']
    style_header(ws_sitemap, 4, headers_sitemap)

    sitemap_data = [
        [1, 'Master Gateway', 'Trang Chủ Student Hub', '/sinh-vien', 'sinh viên momo, student pass momo, ưu đãi sinh viên', 'Tổng quan Thẻ Sinh Viên Số, Banner ưu đãi hot, Widget Bạn đồng hành MoMo, Top Review Trường.', 'Phase 1.0 (Completed)'],
        [2, 'Trường ĐH Pilot', 'Trang Chi Tiết Trường UEH', '/sinh-vien/ueh', 'review ueh, học phí ueh, điểm chuẩn ueh', 'Thông tin tuyển sinh, điểm chuẩn 3 năm, học phí tín chỉ, tiện ích 5km quanh campus.', 'Phase 1.1 (Completed)'],
        [3, 'Cổng Việc Làm', 'Cổng Việc Làm Master & AI Resume', '/sinh-vien/viec-lam', 'việc làm sinh viên, tìm việc part time, cv thực tập sinh', 'Cổng việc làm part-time 5km quanh campus, AI Resume Builder (ATS Score), 1-Tap Apply qua Student Pass.', 'Phase 3.1 (Planned)'],
        [4, 'Đại Sứ Sinh Viên', 'Trang Showcase Ambassador', '/sinh-vien/ambassador', 'đại sứ sinh viên momo, momo campus ambassador', 'Showcase project đại sứ sinh viên, bảng vinh danh leaderboard, form đăng ký đại sứ.', 'Phase 2.1 (In Progress)'],
        [5, 'Nhà Trọ Sinh Viên', 'Sub-page Bãi Đỗ Xe & Nhà Trọ', '/sinh-vien/nha-tro', 'thuê nhà trọ sinh viên, phòng trọ gần trường', 'Bản đồ nhà trọ & KTX an toàn quanh trường, bộ lọc khoảng cách, tool chia tiền trọ.', 'Phase 3.3 (Planned)']
    ]

    for r_offset, r_data in enumerate(sitemap_data, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_sitemap.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 3] else font_regular
            cell.border = border
            cell.alignment = align_center if c_idx in [1, 7] else align_left
            if c_idx == 4:
                cell.font = font_code

    # ==============================================================================
    # 10. SHEET: Tracking Flow
    # ==============================================================================
    ws_tf = wb.create_sheet('Tracking Flow')
    ws_tf.views.sheetView[0].showGridLines = True

    ws_tf.cell(row=1, column=1, value='WEB EVENT TRACKING SPECIFICATION - STUDENT HUB (page_name = studenthub)').font = font_title
    ws_tf.cell(row=2, column=1, value='Đặc tả thông số tracking GA4/GTM cho toàn bộ luồng chuyển đổi Web-to-App qua OneLink.').font = font_subtitle

    headers_tf = ['STT', 'Sự Kiện Tracking (Event Name)', 'Trigger Point / Thao Tác Người Dùng', 'Parameters Đi Kèm (GA4 Params)', 'Mục Đích Đo Lường & Chuyển Đổi']
    style_header(ws_tf, 4, headers_tf)

    tf_data = [
        [1, 'studenthub_page_view', 'Người dùng truy cập vào bất kỳ trang nào thuộc Student Hub', 'page_name, school_slug, user_agent, traffic_source', 'Đo lường tổng lưu lượng PageViews & MUV toàn sàn Student Hub.'],
        [2, 'studenthub_click_apply_job', 'Sinh viên bấm nút "Ứng tuyển qua Student Pass" trên Cổng việc làm', 'job_id, job_title, merchant_name, school_slug', 'Đo lường nhu cầu ứng tuyển việc làm & CTR Web-to-App Cổng việc làm.'],
        [3, 'studenthub_generate_ai_resume', 'Sinh viên hoàn tất tạo CV trên công cụ AI Resume Builder', 'template_id, ats_score, target_job_title', 'Đo lường mức độ sử dụng công cụ AI Resume Builder.'],
        [4, 'studenthub_click_verify_pass', 'Sinh viên bấm nút "Xác thực Thẻ Sinh Viên Số" trên trang trường', 'school_slug, button_position, promo_id', 'Đo lường phễu chuyển đổi Web-to-App eKYC Student Pass In-App.']
    ]

    for r_offset, r_data in enumerate(tf_data, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_tf.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 2] else font_regular
            cell.border = border
            cell.alignment = align_center if c_idx == 1 else align_left
            if c_idx == 2:
                cell.font = font_code

    # ==============================================================================
    # 11. SHEET: Tracking Classes
    # ==============================================================================
    ws_tc = wb.create_sheet('Tracking Classes')
    ws_tc.views.sheetView[0].showGridLines = True

    ws_tc.cell(row=1, column=1, value='HTML TRACKING CLASS SPECIFICATION (page_name = studenthub)').font = font_title
    ws_tc.cell(row=2, column=1, value='Quy chuẩn đặt tên class HTML CSS phục vụ GTM Auto-event Listeners.').font = font_subtitle

    headers_tc = ['STT', 'Tên Thành Phần UI (UI Element)', 'Class Tracking Chuẩn (HTML Class Name)', 'Event Type', 'Vị Trí Gắn Class trong Source Code']
    style_header(ws_tc, 4, headers_tc)

    tc_data = [
        [1, 'Nút "Ứng tuyển ngay" trên Cổng Việc Làm', 'studenthub-tracking-apply-job', 'Click', 'Gắn class vào button ứng tuyển việc làm'],
        [2, 'Nút "Tải CV PDF AI" trên AI Resume Builder', 'studenthub-tracking-download-resume', 'Click', 'Gắn class vào button xuất file CV'],
        [3, 'Nút "Xác thực ngay" trên Banner Student Pass', 'studenthub-tracking-verify-student-pass', 'Click', 'Gắn class vào CTA button Hero Banner'],
        [4, 'Nút "Tính học phí" trên Utility Học Phí', 'studenthub-tracking-calculate-tuition', 'Click', 'Gắn class vào button form tính học phí']
    ]

    for r_offset, r_data in enumerate(tc_data, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_tc.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 3] else font_regular
            cell.border = border
            cell.alignment = align_center if c_idx == 1 else align_left
            if c_idx == 3:
                cell.font = font_code

    # ==============================================================================
    # Auto-adjust column widths across all sheets
    # ==============================================================================
    for sheet in wb.worksheets:
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val_str = str(cell.value or '')
                if cell.row in [1, 2]:
                    continue
                if '\n' in val_str:
                    lines = val_str.split('\n')
                    max_len = max(max_len, max(len(l) for l in lines))
                else:
                    max_len = max(max_len, len(val_str))
            sheet.column_dimensions[col_letter].width = max(max_len + 4, 12)

    # Specific custom width overrides for clean presentation
    ws_readme.column_dimensions['A'].width = 12
    ws_readme.column_dimensions['B'].width = 30
    ws_readme.column_dimensions['C'].width = 80

    ws_roadmap.column_dimensions['A'].width = 16
    ws_roadmap.column_dimensions['B'].width = 24
    ws_roadmap.column_dimensions['C'].width = 32
    ws_roadmap.column_dimensions['D'].width = 45
    ws_roadmap.column_dimensions['E'].width = 65
    ws_roadmap.column_dimensions['F'].width = 50
    ws_roadmap.column_dimensions['G'].width = 45

    ws_ms.column_dimensions['A'].width = 45
    ws_ms.column_dimensions['B'].width = 22
    ws_ms.column_dimensions['C'].width = 16
    ws_ms.column_dimensions['D'].width = 16
    ws_ms.column_dimensions['E'].width = 20
    ws_ms.column_dimensions['F'].width = 18
    ws_ms.column_dimensions['G'].width = 16
    ws_ms.column_dimensions['H'].width = 18
    ws_ms.column_dimensions['I'].width = 35

    ws_content.column_dimensions['A'].width = 8
    ws_content.column_dimensions['B'].width = 28
    ws_content.column_dimensions['C'].width = 48
    ws_content.column_dimensions['D'].width = 32
    ws_content.column_dimensions['E'].width = 20
    ws_content.column_dimensions['F'].width = 28
    ws_content.column_dimensions['G'].width = 35
    ws_content.column_dimensions['H'].width = 16

    ws_traffic.column_dimensions['A'].width = 45
    for c in ['B','C','D','E','F','G','H','I']:
        ws_traffic.column_dimensions[c].width = 18

    ws_res.column_dimensions['A'].width = 45
    ws_res.column_dimensions['B'].width = 22
    ws_res.column_dimensions['C'].width = 24
    ws_res.column_dimensions['D'].width = 75

    ws_util.column_dimensions['A'].width = 8
    ws_util.column_dimensions['B'].width = 32
    ws_util.column_dimensions['C'].width = 28
    ws_util.column_dimensions['D'].width = 45
    ws_util.column_dimensions['E'].width = 45
    ws_util.column_dimensions['F'].width = 50
    ws_util.column_dimensions['G'].width = 45
    ws_util.column_dimensions['H'].width = 45
    ws_util.column_dimensions['I'].width = 45

    ws_schema.column_dimensions['A'].width = 8
    ws_schema.column_dimensions['B'].width = 25
    ws_schema.column_dimensions['C'].width = 25
    ws_schema.column_dimensions['D'].width = 22
    ws_schema.column_dimensions['E'].width = 45
    ws_schema.column_dimensions['F'].width = 50
    ws_schema.column_dimensions['G'].width = 50

    ws_sitemap.column_dimensions['A'].width = 8
    ws_sitemap.column_dimensions['B'].width = 22
    ws_sitemap.column_dimensions['C'].width = 32
    ws_sitemap.column_dimensions['D'].width = 28
    ws_sitemap.column_dimensions['E'].width = 42
    ws_sitemap.column_dimensions['F'].width = 55
    ws_sitemap.column_dimensions['G'].width = 22

    ws_tf.column_dimensions['A'].width = 8
    ws_tf.column_dimensions['B'].width = 32
    ws_tf.column_dimensions['C'].width = 48
    ws_tf.column_dimensions['D'].width = 48
    ws_tf.column_dimensions['E'].width = 50

    ws_tc.column_dimensions['A'].width = 8
    ws_tc.column_dimensions['B'].width = 42
    ws_tc.column_dimensions['C'].width = 45
    ws_tc.column_dimensions['D'].width = 16
    ws_tc.column_dimensions['E'].width = 45

    save_with_backup(wb, '05_HUBS/student-hub-roadmap.xlsx', dry_run=args.dry_run, make_backup=not args.no_backup)
    print('Successfully generated master student-hub-roadmap.xlsx with all 11 sheets matching vehicle-hub-roadmap.xlsx!')

if __name__ == "__main__":
    _ap = standard_argparser("Fix runner - safe with --dry-run")
    main(_ap.parse_args())

