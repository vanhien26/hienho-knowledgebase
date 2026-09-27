import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter


from scripts._lib import load_workbook_safe, save_with_backup, standard_argparser

def main(args=None):
    wb = openpyxl.Workbook()

    # Common Styles
    font_title = Font(name='Calibri', size=14, bold=True, color='1E293B')
    font_subtitle = Font(name='Calibri', size=11, italic=True, color='64748B')
    font_header = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
    font_section = Font(name='Calibri', size=11, bold=True, color='0F172A')
    font_bold = Font(name='Calibri', size=11, bold=True, color='000000')
    font_regular = Font(name='Calibri', size=11, color='000000')

    fill_header = PatternFill('solid', fgColor='1E293B')
    fill_section = PatternFill('solid', fgColor='F1F5F9')
    fill_zebra = PatternFill('solid', fgColor='F8FAFC')
    fill_completed = PatternFill('solid', fgColor='DCFCE7')
    fill_inprogress = PatternFill('solid', fgColor='FEF08A')
    fill_planned = PatternFill('solid', fgColor='F3F4F6')

    align_left = Alignment(horizontal='left', vertical='center', wrap_text=True)
    align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_right = Alignment(horizontal='right', vertical='center')

    border_thin = Side(style='thin', color='CBD5E1')
    border = Border(left=border_thin, right=border_thin, top=border_thin, bottom=border_thin)

    # ==============================================================================
    # 1. SHEET: Readme
    # ==============================================================================
    ws_readme = wb.active
    ws_readme.title = 'Readme'
    ws_readme.views.sheetView[0].showGridLines = True

    readme_rows = [
        ['DANH MỤC TÀI LIỆU VÀ HƯỚNG DẪN VẬN HÀNH ROADMAP STUDENT HUB (WEB PLATFORM)', None, None],
        ['Tài liệu SSOT quy hoạch lộ trình phát triển, chỉ số KPI và ma trận phân công RACI giữa Web Platform & Youth Segment BU.', None, None],
        [],
        ['Mã Sheet', 'Tên Trang TÍnh (Sheet Name)', 'Nội Dung Chi Tiết & Mục Đích Vận Hành'],
        ['01', 'Readme', 'Trang tổng quan chỉ dẫn danh mục tài liệu, metadata quy hoạch và cấu trúc workbook.'],
        ['02', 'Roadmap', 'Lộ trình phát triển 3 Phase chiến lược (Foundation, Ambassador, Career & Ecosystem) năm 2026.'],
        ['03', 'Opportunity & Priority', 'Ma trận nghiên cứu từ khóa 100+ trường ĐH, điểm ưu tiên SEO/GEO và phân hạng Tier.'],
        ['04', 'Performance Tracking', 'Báo cáo lưu lượng truy cập hàng tháng (MTD vs Full Month) phân rã theo nguồn Out-App & In-App.'],
        ['05', 'KPIs & Target Metrics', 'Khung chỉ số cam kết alignment (Web Traffic Target, Web-to-App CTR, New Verified Students, MEU).'],
        ['06', 'RACI & Resource Allocation', 'Ma trận phân định trách nhiệm chi tiết giữa Web Platform Team & Youth & Student Segment BU.'],
        [],
        ['THÔNG TIN METADATA & PHÊ DUYỆT CHIẾN LƯỢC', None, None],
        ['Dự Án / Sản Phẩm', 'MoMo Student Hub (Web Discovery Gateway & Student Pass Ecosystem)', None],
        ['Tên Miền / Cổng Trọng Điểm', 'momo.vn/sinh-vien | Cổng Việc Làm Master: momo.vn/sinh-vien/viec-lam', None],
        ['Khung Thời Gian Vận Hành', 'Quý 3/2026 - Quý 4/2026 (Standing Year-Round Platform)', None],
        ['Đơn Vị Chủ Quản Web', 'Growth Platform Division (GPD) - Web Platform Team', None],
        ['Đơn Vị Đồng Hành BU', 'Youth & Student Segment BU', None]
    ]

    for r_idx, row in enumerate(readme_rows, start=1):
        for c_idx, val in enumerate(row, start=1):
            if val is not None:
                cell = ws_readme.cell(row=r_idx, column=c_idx, value=val)
                cell.border = border
                if r_idx == 1:
                    cell.font = font_title
                    cell.border = Border()
                elif r_idx == 2:
                    cell.font = font_subtitle
                    cell.border = Border()
                elif r_idx == 4:
                    cell.font = font_header
                    cell.fill = fill_header
                    cell.alignment = align_center
                elif r_idx in [5,6,7,8,9,10]:
                    cell.font = font_regular
                    cell.alignment = align_center if c_idx == 1 else align_left
                elif r_idx == 12:
                    cell.font = font_section
                    cell.fill = fill_section
                elif r_idx > 12:
                    cell.font = font_bold if c_idx == 1 else font_regular
                    cell.alignment = align_left

    ws_readme.merge_cells('A1:C1')
    ws_readme.merge_cells('A2:C2')
    ws_readme.merge_cells('A12:C12')

    # ==============================================================================
    # 2. SHEET: Roadmap
    # ==============================================================================
    ws_roadmap = wb.create_sheet('Roadmap')
    ws_roadmap.views.sheetView[0].showGridLines = True

    ws_roadmap.cell(row=1, column=1, value='LỘ TRÌNH PHÁT TRIỂN SẢN PHẨM STUDENT HUB (STUDENT HUB ROADMAP 2026)').font = font_title
    ws_roadmap.cell(row=2, column=1, value='Quy hoạch 3 Phase chiến lược từ Foundation (Pilot 12 trường) -> Ambassador & Realtime Event -> Career Master & pSEO Scale 100+ trường.').font = font_subtitle

    roadmap_headers = ['Phase', 'Thời Gian', 'Trọng Tâm Phát Triển', 'Tính Năng Web & Sản Phẩm Cốt Lõi', 'Mô Tả Chi Tiết Triển Khai & Quy Trình Phối Hợp', 'Chuyển Đổi Kinh Doanh & Phễu Web-to-App', 'Trạng Thái']
    for c_idx, h in enumerate(roadmap_headers, start=1):
        cell = ws_roadmap.cell(row=4, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border

    roadmap_data = [
        ['Phase 1: Foundation & Pilot Launch', 'Tháng 8 - 9/2026', 'Gateway & 12 Trường ĐH Trọng Điểm', 'Master Hub Gateway (/sinh-vien) + 12 Trang Trường ĐH (UEH, FTU, TDTU, HCMUT, VLU, HUST, NEU, HANU, HAU, USSH, HUIT, UEL)', 'Build Cổng dẫn đường Master Gateway; Xây 12 trang trường trọng điểm đáp ứng 4 JTBD (Học phí, Điểm chuẩn, Tiện ích 5km, Student Pass); Hiển thị Custom School Card UI sau khi eKYC Thẻ Sinh Viên Số; Sản xuất 100 bài content blog chuẩn hóa GenAI Prompt.', 'Anchor links #hoc-phi, #diem-chuan & OneLink eKYC Thẻ Sinh Viên Số custom theo từng trường', 'Completed'],
        ['Phase 2: Ambassador & Campus Engagement', 'Tháng 9/2026', 'Ambassador Engine & Offline Campus Event', 'Web Ambassador Showcase (/sinh-vien/ambassador) + Real-time Web Photobooth Module', 'Mở trang Showcase Project Đại sứ sinh viên (5-7 nhóm đại sứ, bảng thành tích 1 năm); Xây module Web Real-time Photobooth cho Offline Event Campus 26-27/09 (chụp ảnh -> upload -> ghi nhận footprint -> nhận quà booth).', 'Kéo sinh viên về Booth MoMo & đăng ký Ambassador In-App', 'In Progress'],
        ['Phase 3: Career, Programmatic Scale & Ecosystem', 'Quý 4/2026', 'Cổng Việc Làm Master & Programmatic pSEO 100+ Trường', 'Cổng Việc Làm Sinh Viên Master (/sinh-vien/viec-lam) + AI Resume Builder + Sub-pages (/nha-tro, /review, /workshop)', 'Build Cổng Việc Làm Master /sinh-vien/viec-lam kết hợp AI Resume Builder (ATS Score), Bản đồ việc làm 5km quanh campus từ đối tác F&B/bán lẻ MoMo; Programmatic pSEO Engine tự động mở rộng 100+ trang trường ĐH/CĐ toàn quốc.', 'Phễu OneLink kích hoạt xác thực Thẻ Sinh Viên Số, mở gói đặc quyền voucher & Ví Trả Sau 0% HSSV (Web-to-App CTR 10-15%, 70K New Verified Students)', 'Planned']
    ]

    for r_offset, r_data in enumerate(roadmap_data, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_roadmap.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_regular
            cell.border = border
            cell.alignment = align_left if c_idx in [3, 4, 5, 6] else align_center
            if val == 'Completed':
                cell.fill = fill_completed
                cell.font = font_bold
            elif val == 'In Progress':
                cell.fill = fill_inprogress
                cell.font = font_bold
            elif val == 'Planned':
                cell.fill = fill_planned
                cell.font = font_bold

    # ==============================================================================
    # 3. SHEET: Opportunity & Priority
    # ==============================================================================
    ws_opp = wb.create_sheet('Opportunity & Priority')
    ws_opp.views.sheetView[0].showGridLines = True

    ws_opp.cell(row=1, column=1, value='MA TRẬN NGUYÊN CỨU TỪ KHÓA & MARKET SIZE CÁC TRƯỜNG ĐẠI HỌC (STUDENT HUB)').font = font_title
    ws_opp.cell(row=2, column=1, value='Trích xuất dữ liệu Search Volume theo cụm từ khóa trường học & việc làm từ Content Structure Master Document.').font = font_subtitle

    opp_headers = ['Cụm Chủ Đề Từ Khóa Trường (Cluster)', 'Search/tháng (Mẫu 5 Trường)', 'Volume Score (1-10)', 'Intent Score (1-5)', 'Monetization Score (1-5)', 'Data Seed Score (1-5)', 'Điểm Ưu Tiên', 'Tier Phân Hạng', 'Nhóm Định Hướng Chiến Lược']
    for c_idx, h in enumerate(opp_headers, start=1):
        cell = ws_opp.cell(row=4, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border

    ws_opp.cell(row=1, column=12, value='TRỌNG SỐ ĐÁNH GIÁ (WEIGHTS)').font = font_section
    weights = [('Weight Volume', 0.35), ('Weight Intent', 0.25), ('Weight Monetization', 0.25), ('Weight Data Seed', 0.15)]
    for w_idx, (w_name, w_val) in enumerate(weights, start=1):
        ws_opp.cell(row=w_idx+1, column=12, value=w_name).font = font_bold
        ws_opp.cell(row=w_idx+1, column=13, value=w_val).font = font_regular
        ws_opp.cell(row=w_idx+1, column=13).number_format = '0.00%'

    opp_data = [
        ['Cụm 4A - Điểm rèn luyện & Đánh giá cá nhân', 10260, 10, 3, 2, 1, 'Nhóm 1 - Engagement Magnet'],
        ['Cụm 1 - Tuyển sinh, Điểm chuẩn & Xếp hạng', 7820, 9, 4, 2, 2, 'Nhóm 1 - Information & Admission'],
        ['Cụm 3 - Đời sống sinh viên, KTX & Campus', 4730, 8, 4, 3, 1, 'Nhóm 1 - Campus Life & Accommodation'],
        ['Cụm 2 - Học phí & Học bổng Sinh viên', 3400, 7, 5, 4, 2, 'Nhóm 1 - Flagship Financial Utility'],
        ['Cụm 5 - Việc làm Part-time & AI Resume (/viec-lam)', 12500, 10, 5, 5, 2, 'Nhóm 1 - Career & Monetization'],
        ['Cụm 6 - Văn bằng 2 & Chương trình mở rộng', 2160, 6, 3, 2, 1, 'Nhóm 2 - Academic Expansion'],
        ['Cụm 4B - Đăng ký tín chỉ & Quy chế học vụ', 190, 4, 4, 2, 1, 'Nhóm 2 - Academic Rules']
    ]

    for r_offset, r_data in enumerate(opp_data, start=5):
        ws_opp.cell(row=r_offset, column=1, value=r_data[0]).font = font_bold
        ws_opp.cell(row=r_offset, column=2, value=r_data[1]).font = font_regular
        ws_opp.cell(row=r_offset, column=2).number_format = '#,##0'
        ws_opp.cell(row=r_offset, column=3, value=r_data[2]).font = font_regular
        ws_opp.cell(row=r_offset, column=4, value=r_data[3]).font = font_regular
        ws_opp.cell(row=r_offset, column=5, value=r_data[4]).font = font_regular
        ws_opp.cell(row=r_offset, column=6, value=r_data[5]).font = font_regular
    
        # Priority Formula: =(C5*$M$2 + D5*$M$3 + E5*$M$4)/10 + F5*$M$5
        formula_score = f"=(C{r_offset}*$M$2 + D{r_offset}*$M$3 + E{r_offset}*$M$4)/10 + F{r_offset}*$M$5"
        cell_score = ws_opp.cell(row=r_offset, column=7, value=formula_score)
        cell_score.font = font_bold
        cell_score.number_format = '0.00'
    
        # Tier Formula: =IF(G5>=0.75, "High (P1)", IF(G5>=0.55, "Medium (P2)", "Low (P3)"))
        formula_tier = f'=IF(G{r_offset}>=0.75, "High (P1)", IF(G{r_offset}>=0.55, "Medium (P2)", "Low (P3)"))'
        cell_tier = ws_opp.cell(row=r_offset, column=8, value=formula_tier)
        cell_tier.font = font_bold
        cell_tier.alignment = align_center
    
        ws_opp.cell(row=r_offset, column=9, value=r_data[6]).font = font_regular
    
        for col_i in range(1, 10):
            cell_curr = ws_opp.cell(row=r_offset, column=col_i)
            cell_curr.border = border
            if col_i in [2,3,4,5,6,7]:
                cell_curr.alignment = align_right if col_i in [2,7] else align_center

    # ==============================================================================
    # 4. SHEET: Performance Tracking
    # ==============================================================================
    ws_perf = wb.create_sheet('Performance Tracking')
    ws_perf.views.sheetView[0].showGridLines = True

    ws_perf.cell(row=1, column=1, value='BÁO CÁO HIỆU SUẤT TRUY CẬP PHÂN RÃ MTD & FULL MONTH (STUDENT HUB OUTAPP & INAPP)').font = font_title
    ws_perf.cell(row=2, column=1, value='Chuẩn hóa theo cấu trúc báo cáo Web Platform: Phân rã lưu lượng MTD vs Full Month (T5/2026 - T9/2026 MTD).').font = font_subtitle

    perf_headers = ['Chỉ Số / Kênh Lưu Lượng (Source Group)', 'T5/2026 (Full)', 'T6/2026 (Full)', 'T7/2026 (Full)', 'T7/2026 (MTD 28d)', 'T8/2026 (MTD 28d)', 'T8/2026 (Full)', 'T9/2026 (MTD 8d)', 'MoM MTD (%)']
    for c_idx, h in enumerate(perf_headers, start=5):
        cell = ws_perf.cell(row=5, column=c_idx-4, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border

    perf_rows = [
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

    for r_offset, r_data in enumerate(perf_rows, start=6):
        is_main_head = r_data[0].startswith('TỔNG CỘNG') or r_data[0].startswith('1.') or r_data[0].startswith('2.')
        for c_idx in range(1, 9):
            val = r_data[c_idx-1]
            cell = ws_perf.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if is_main_head else font_regular
            cell.border = border
            if c_idx == 1:
                cell.alignment = align_left
                if is_main_head:
                    cell.fill = fill_section
            else:
                cell.alignment = align_right
                cell.number_format = '#,##0'
            
        # Native MoM Formula: =IF(E6>0, (F6-E6)/E6, "N/A")
        mom_formula = f'=IF(E{r_offset}>0, (F{r_offset}-E{r_offset})/E{r_offset}, "N/A")'
        cell_mom = ws_perf.cell(row=r_offset, column=9, value=mom_formula)
        cell_mom.font = font_bold if is_main_head else font_regular
        cell_mom.border = border
        cell_mom.alignment = align_right
        cell_mom.number_format = '+0.00%;-0.00%;0.00%'

    # ==============================================================================
    # 5. SHEET: KPIs & Target Metrics
    # ==============================================================================
    ws_kpi = wb.create_sheet('KPIs & Target Metrics')
    ws_kpi.views.sheetView[0].showGridLines = True

    ws_kpi.cell(row=1, column=1, value='CHỈ SỐ MỤC TIÊU ĐÃ PHÊ DUYỆT - STUDENT HUB (WEB x APP ALIGNMENT)').font = font_title
    ws_kpi.cell(row=2, column=1, value='Bộ chỉ số đo lường hiệu quả chuyển đổi từ Web Hub sang hệ sinh thái Student Pass In-App (Thống nhất cùng BU Youth & Student Segment).').font = font_subtitle

    kpi_headers = ['Tầng Đo Lường', 'Chỉ Số Mục Tiêu Chính', 'Mục Tiêu Cam Kết (KPI Target)', 'Căn Cứ & Nguồn Số Liệu', 'Ý Nghĩa & Vai Trò Thực Tế']
    for c_idx, h in enumerate(kpi_headers, start=1):
        cell = ws_kpi.cell(row=4, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border

    kpi_data = [
        ['Kênh Website', 'Web Traffic Target (PageView)', '500.000 PageView / Q4 (~167.000 PageView/tháng)', 'Umami Analytics đo lường từ nguồn Organic Search (pSEO/GEO), chuyên mục Webinar và chuỗi Seeding Ambassador', 'Đo lường quy mô lưu lượng truy cập tự nhiên và số cơ hội hiển thị tiện ích sinh viên.'],
        ['Kênh Website', 'Web-to-App CTR', '10.00% - 15.00%', 'Baseline CTR tiêu chuẩn toàn nền tảng Web Platform đối với tệp người dùng trẻ Gen Z', 'Tỷ lệ nhấp nút hành động CTA OneLink từ Web Hub điều hướng người dùng sang App MoMo.'],
        ['Ứng Dụng MoMo', 'New Verified Students', '70.000 Sinh viên xác thực mới (Q3 - Q4)', 'Hệ thống xác thực Student Pass In-App kết hợp phễu điều hướng từ Web Hub', 'Số lượng sinh viên mới hoàn tất xác thực định danh Thẻ Sinh Viên Số / Email .edu.vn In-App.'],
        ['Ứng Dụng MoMo', 'Student Pass MEU', '1.500.000 Student Pass MEU', 'Số liệu người dùng active tích lũy từ hệ sinh thái Student Pass trên App MoMo', 'Tổng số người dùng sinh viên định danh hoạt động hàng tháng (Monthly Engaged Users).']
    ]

    for r_offset, r_data in enumerate(kpi_data, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws_kpi.cell(row=r_offset, column=c_idx, value=val)
            cell.font = font_bold if c_idx in [1, 2] else font_regular
            cell.border = border
            cell.alignment = align_center if c_idx in [1, 3] else align_left

    # ==============================================================================
    # 6. SHEET: RACI & Resource Allocation
    # ==============================================================================
    ws_raci = wb.create_sheet('RACI & Resource Allocation')
    ws_raci.views.sheetView[0].showGridLines = True

    ws_raci.cell(row=1, column=1, value='MA TRẬN PHÂN ĐỊNH TRÁCH NHIỆM RACI: WEB PLATFORM x YOUTH & STUDENT SEGMENT BU').font = font_title
    ws_raci.cell(row=2, column=1, value='Quy định rõ trách nhiệm triển khai giữa Web Platform Team (GPD) & Youth Segment BU cho toàn bộ các nhóm đầu việc.').font = font_subtitle

    raci_headers = ['Hạng Mục / Đầu Việc Triển Khai', 'Web Platform Team', 'Youth & Student Segment BU', 'Mô Tả Trách Nhiệm Chi Tiết & Tiêu Chí Nghiệm Thu']
    for c_idx, h in enumerate(raci_headers, start=1):
        cell = ws_raci.cell(row=5, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = align_center
        cell.border = border

    raci_sections = [
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
    for sec_title, items in raci_sections:
        cell_sec = ws_raci.cell(row=curr_row, column=1, value=sec_title)
        cell_sec.font = font_section
        cell_sec.fill = fill_section
        ws_raci.merge_cells(start_row=curr_row, start_column=1, end_row=curr_row, end_column=4)
        for col_k in range(1, 5):
            ws_raci.cell(row=curr_row, column=col_k).border = border
        curr_row += 1
    
        for item_title, r_web, r_bu, r_desc in items:
            ws_raci.cell(row=curr_row, column=1, value=item_title).font = font_bold
            ws_raci.cell(row=curr_row, column=2, value=r_web).font = font_bold
            ws_raci.cell(row=curr_row, column=3, value=r_bu).font = font_bold
            ws_raci.cell(row=curr_row, column=4, value=r_desc).font = font_regular
        
            for col_k in range(1, 5):
                c_item = ws_raci.cell(row=curr_row, column=col_k)
                c_item.border = border
                if col_k in [2, 3]:
                    c_item.alignment = align_center
                elif col_k == 4:
                    c_item.alignment = align_left
            curr_row += 1

    # ==============================================================================
    # Auto-adjust column widths across all sheets
    # ==============================================================================
    for sheet in wb.worksheets:
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val_str = str(cell.value or '')
                if cell.row in [1, 2]: # skip title rows for length calc
                    continue
                if '\n' in val_str:
                    lines = val_str.split('\n')
                    max_len = max(max_len, max(len(l) for l in lines))
                else:
                    max_len = max(max_len, len(val_str))
            sheet.column_dimensions[col_letter].width = max(max_len + 4, 12)

    # Specific custom width overrides for optimal rendering
    ws_readme.column_dimensions['A'].width = 12
    ws_readme.column_dimensions['B'].width = 30
    ws_readme.column_dimensions['C'].width = 75

    ws_roadmap.column_dimensions['A'].width = 28
    ws_roadmap.column_dimensions['B'].width = 18
    ws_roadmap.column_dimensions['C'].width = 32
    ws_roadmap.column_dimensions['D'].width = 42
    ws_roadmap.column_dimensions['E'].width = 60
    ws_roadmap.column_dimensions['F'].width = 50
    ws_roadmap.column_dimensions['G'].width = 16

    ws_opp.column_dimensions['A'].width = 42
    ws_opp.column_dimensions['B'].width = 22
    ws_opp.column_dimensions['C'].width = 16
    ws_opp.column_dimensions['D'].width = 16
    ws_opp.column_dimensions['E'].width = 20
    ws_opp.column_dimensions['F'].width = 18
    ws_opp.column_dimensions['G'].width = 16
    ws_opp.column_dimensions['H'].width = 18
    ws_opp.column_dimensions['I'].width = 35

    ws_perf.column_dimensions['A'].width = 45
    for c in ['B','C','D','E','F','G','H','I']:
        ws_perf.column_dimensions[c].width = 18

    ws_kpi.column_dimensions['A'].width = 18
    ws_kpi.column_dimensions['B'].width = 32
    ws_kpi.column_dimensions['C'].width = 40
    ws_kpi.column_dimensions['D'].width = 50
    ws_kpi.column_dimensions['E'].width = 55

    ws_raci.column_dimensions['A'].width = 45
    ws_raci.column_dimensions['B'].width = 22
    ws_raci.column_dimensions['C'].width = 24
    ws_raci.column_dimensions['D'].width = 75

    save_with_backup(wb, '05_HUBS/student-hub-roadmap.xlsx', dry_run=args.dry_run, make_backup=not args.no_backup)
    print('Successfully rebuilt full student-hub-roadmap.xlsx with all 6 sheets standard!')

if __name__ == "__main__":
    _ap = standard_argparser("Fix runner - safe with --dry-run")
    main(_ap.parse_args())

