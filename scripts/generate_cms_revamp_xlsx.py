import csv
import os
import openpyxl
import xlsxwriter
from collections import defaultdict

def generate_revamped_workbook():
    csv_path = '/Users/hienhv/Downloads/Project - Trang tính1.csv'
    overview_path = '/Users/hienhv/Downloads/[Web MoMo] Overview Web 2026.xlsx'
    out_dir = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/sheets'
    os.makedirs(out_dir, exist_ok=True)
    out_xlsx = os.path.join(out_dir, 'cms_projects_audit_and_restructuring_report.xlsx')

    cms_projects = list(csv.DictReader(open(csv_path, encoding='utf-8')))

    # Read Overview Web 2026 Mini Web sheet
    wb_ref = openpyxl.load_workbook(overview_path, data_only=True)
    ws_mini = wb_ref['Mini Web']
    ref_products = []
    for r in range(2, ws_mini.max_row + 1):
        div = ws_mini.cell(r, 1).value
        use_case = ws_mini.cell(r, 2).value
        prod = ws_mini.cell(r, 3).value
        srv = ws_mini.cell(r, 4).value
        url = ws_mini.cell(r, 5).value
        p_type = ws_mini.cell(r, 6).value
        note = ws_mini.cell(r, 7).value
        if div and prod:
            ref_products.append({
                'division': str(div).strip(),
                'use_case': str(use_case).strip() if use_case else '',
                'product': str(prod).strip(),
                'service': str(srv).strip() if srv else '',
                'url': str(url).strip() if url else '',
                'page_type': str(p_type).strip() if p_type else 'Advanced MiniWeb',
                'note': str(note).strip() if note else ''
            })

    # Deduplicate standard products list
    unique_std_projects = []
    seen = set()
    for p in ref_products:
        key = (p['division'], p['use_case'], p['product'], p['service'], p['url'])
        if key not in seen:
            seen.add(key)
            unique_std_projects.append(p)

    # Classification logic for 420 CMS entries
    ngo_keywords = ['Quỹ', 'DNXH', 'Foundation', 'Sức mạnh', 'Thiện Nhân', 'SCDI', 'Operation', 'Trung Tâm', 'Hoa Chia Sẻ', 'msd', 'Teach', 'WildAct', 'Bếp', 'Saigon', 'VinaCapital', 'Trăng Khuyết', 'Hy Vọng']
    
    legacy_camp_ids = {
        '90', '134', '152', '258', '19', '301', '344', '340', '376', '414',
        '576', '415', '462', '60', '530', '202', '225', '311', '324', '328',
        '337', '342', '350', '361', '371', '387', '399', '406', '533', '648',
        '681', '740', '688'
    }

    mapped_420 = []
    for p in cms_projects:
        p_id = p['Id']
        p_name = p['Project']
        p_parent = p['Project Cha'].strip()
        p_link = p['Link']

        item_nature = 'TRUE_PROJECT'
        nature_desc = 'Dự án Sản phẩm Cốt lõi (Product Project)'
        std_name = ''
        std_div = ''
        target_zone = 'Productivity & Self-serve'
        action_req = 'Chuẩn hóa tên theo quy chuẩn [Division] - [Product].'

        if p_id in ['540', '541']:
            item_nature = 'TEST_DATA'
            nature_desc = 'Dữ liệu Thử nghiệm (Test Data)'
            action_req = 'Xóa khỏi Production CMS.'
            std_name = 'N/A'
            std_div = 'N/A'
        elif p_parent == 'Phim chiếu':
            item_nature = 'DYNAMIC_TAG_GENRE'
            nature_desc = 'Thuộc tính Thể loại Phim (Genre Tag)'
            action_req = 'Chuyển sang Tag / Dynamic Facet của MDS - Cinema.'
            std_name = 'MDS - Cinema (Tag: Thể loại)'
            std_div = 'MDS'
            target_zone = 'Performance Zone'
        elif p_parent == 'Điểm đến':
            item_nature = 'DYNAMIC_ENTITY_GEO'
            nature_desc = 'Thực thể Địa lý Điểm đến (Geo Destination Entity)'
            action_req = 'Chuyển sang Destination Entity Database của MDS - OTA.'
            std_name = 'MDS - OTA (Entity: Điểm đến)'
            std_div = 'MDS'
            target_zone = 'Performance Zone'
        elif p_parent == 'Rạp chiếu':
            item_nature = 'PARTNER_ENTITY_CINEMA'
            nature_desc = 'Thực thể Cụm Rạp Đối tác (Cinema Merchant Entity)'
            action_req = 'Chuyển sang Cinema Partner Profile của MDS - Cinema.'
            std_name = 'MDS - Cinema (Entity: Cụm rạp)'
            std_div = 'MDS'
            target_zone = 'Performance Zone'
        elif p_parent == 'Donation' and any(k in p_name for k in ngo_keywords):
            item_nature = 'PARTNER_ENTITY_NGO'
            nature_desc = 'Hồ sơ Tổ chức Thiện nguyện Đối tác (NGO Partner Profile)'
            action_req = 'Chuyển sang NGO Directory Profile của MDS - Donation.'
            std_name = 'MDS - Donation (Entity: Tổ chức NGO)'
            std_div = 'MDS'
            target_zone = 'Productivity & Self-serve'
        elif p_parent == 'Campaign MoMo' or p_id in legacy_camp_ids or p_name in ['Campaign MoMo', 'Popup Ads'] or p_parent == 'Popup Ads':
            item_nature = 'CAMPAIGN_EVENT'
            nature_desc = 'Chiến dịch / Sự kiện Marketing Mùa (Campaign / Event)'
            action_req = 'Lưu trữ (Archive) & Cấu hình 301 Redirect về Hub tương ứng.'
            std_name = 'BMC - Gamification (Campaign)'
            std_div = 'BMC'
            target_zone = 'Productivity & Self-serve'
        elif '[PROMOTION]' in p_name or 'Landing Page' in p_name or '[Exclude]' in p_name or p_parent == 'Deal':
            item_nature = 'LANDING_PAGE_PROMO'
            nature_desc = 'Trang Đích / Webview Khuyến mãi Đơn lẻ (Ad-hoc Landing Page)'
            action_req = 'Chuyển thành Template Webview T&C tự phục vụ hoặc hợp nhất về Hub.'
            std_name = 'GPD - Promotion / Webview'
            std_div = 'GPD'
            target_zone = 'Productivity & Self-serve'
        elif p_parent in ['Quốc gia', 'Diễn viên', 'Blog Phim', 'Phim hay', 'Netflix', 'Ví Trả Sau', 'Airtime', 'Topup', 'Delivery', 'Logistics', 'Application Store', 'Apple', 'Tiktok', 'Agent Network', 'Học phí', 'Dịch vụ công', 'SME Offline', 'Sàn Đầu Tư', 'Tài chính cá nhân', 'Heo đất MoMo - Quyên góp', 'Donation Campaign', 'Life At MoMo', 'eSim du lịch', 'Ví Nhân Ái - Blog']:
            item_nature = 'SUB_CATEGORY_OR_TOPIC'
            nature_desc = 'Chuyên mục Con / Chủ đề Nội dung (Sub-category / Topic)'
            action_req = 'Quản trị bằng Category Tree hoặc Tag của Master Hub.'
            std_name = f"Category / Tag thuộc {p_parent}"
            std_div = 'N/A'
            target_zone = 'Productivity & Self-serve'
        else:
            # Match True Projects to standard naming
            if p_name in ['Cinema']:
                std_name = 'MDS - Cinema'
                std_div = 'MDS'
                target_zone = 'Performance Zone'
            elif p_name in ['Vé máy bay']:
                std_name = 'MDS - Flight'
                std_div = 'MDS'
                target_zone = 'Performance Zone'
            elif p_name in ['Vé xe khách', 'Phương Trang', 'Vé xe Tết']:
                std_name = 'MDS - Bus'
                std_div = 'MDS'
                target_zone = 'Performance Zone'
            elif p_name in ['Khách sạn theo giờ']:
                std_name = 'MDS - Hourly Hotel'
                std_div = 'MDS'
                target_zone = 'Performance Zone'
            elif p_name in ['OTA', 'Đặt khách sạn', 'Vé tàu hỏa', 'Thuê xe', 'Vé khu vui chơi', 'Vé trải nghiệm']:
                std_name = 'MDS - OTA'
                std_div = 'MDS'
                target_zone = 'Performance Zone'
            elif p_name in ['Donation', 'Ví Nhân Ái - Blog', 'Trái tim MoMo - Quyên Góp', 'Heo đất MoMo - Quyên góp']:
                std_name = 'MDS - Donation'
                std_div = 'MDS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Thổ Địa MoMo']:
                std_name = 'MDS - Tho Dia'
                std_div = 'MDS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Sống tốt']:
                std_name = 'MDS - Community'
                std_div = 'MDS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Vay Nhanh', 'Vay nhanh nhà bán hàng', 'Vay Nhanh - Simular', 'Trả góp Flik']:
                std_name = 'FS - Loan'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Bảo hiểm ô tô', 'Bảo hiểm vật chất ô tô', 'Bảo hiểm trách nhiệm dân sự ô tô']:
                std_name = 'FS - Car Insurance'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Bảo hiểm xe máy']:
                std_name = 'FS - Bike Insurance'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Bảo Hiểm Y Tế']:
                std_name = 'FS - BHYT'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Bảo hiểm sức khỏe']:
                std_name = 'FS - Critical Illness'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Bảo hiểm', 'Bảo hiểm Du lịch', 'Bảo hiểm Du lịch Quốc tế', 'Thanh toán phí bảo hiểm']:
                std_name = 'FS - InsurTech'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Túi Thần Tài']:
                std_name = 'FS - TTT'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Ví Trả Sau']:
                std_name = 'FS - PayLater'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Thanh toán khoản vay', 'Thanh toán thẻ tín dụng', 'Mở thẻ tín dụng', 'Thẻ Tín Dụng', 'Tài chính siêu tốc']:
                std_name = 'FS - CreditTech'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Tiết Kiệm Online']:
                std_name = 'FS - Online Saving'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Trả Góp Apple']:
                std_name = 'FS - Device Financing'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Sàn Đầu Tư', 'Chứng khoán']:
                std_name = 'FS - Brokerage'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Chứng Chỉ Quỹ']:
                std_name = 'FS - Mutual Funds'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Tiệm Vàng Online']:
                std_name = 'FS - Gold'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Tài chính - Bảo hiểm', 'Tài chính']:
                std_name = 'FS - Overall'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Điểm tín dụng']:
                std_name = 'FS - Credit Score'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Mở tài khoản ngân hàng', 'Source of Fund', 'Bank']:
                std_name = 'FS - Source of Funds'
                std_div = 'FS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Phạt nguội']:
                std_name = 'PS - Phạt Nguội'
                std_div = 'PS'
                target_zone = 'Transformation Zone'
            elif p_name in ['Tiện ích giao thông', 'Busmap', 'Vận tải', 'Phí không dừng', 'Cứu hộ giao thông', 'Đăng kiểm ô tô', 'Phí VETC']:
                std_name = 'UTI - Vehicle'
                std_div = 'UTI'
                target_zone = 'Transformation Zone'
            elif p_name in ['Billpay', 'Điện', 'Nước', 'Truyền hình', 'Chung cư', 'Internet', 'Điện thoại cố định', 'Học phí', 'Phí xét tuyển', 'Môi trường', 'Bệnh viện', 'Dịch vụ công', 'Metro', 'Xăng dầu', 'Di động trả sau', 'Y Tế', 'Nha khoa', 'Phật Giáo', 'Tiêm chủng', 'Giáo dục', 'VTTIDeal', 'Đánh giá năng lực']:
                std_name = 'UTI - Billpay'
                std_div = 'UTI'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Telco', 'Viettel', 'Mobifone', 'Vinaphone', 'Data 4G/5G', 'Airtime', 'Topup', 'eSim du lịch', 'Sim chính chủ']:
                std_name = 'UTI - Telco'
                std_div = 'UTI'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Chuyển Nhận Tiền', 'P2P', 'W2B', 'W2W', 'Điểm nạp rút (W2C)', 'Thanh toán quốc tế', 'VietQR']:
                std_name = 'SP - Transfer'
                std_div = 'SP'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Quỹ Nhóm']:
                std_name = 'SP - Quy'
                std_div = 'SP'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Nạp thẻ Game', 'VNG', 'Napthengay.vn', 'VGP', 'Tiktok Coin']:
                std_name = 'DLS - Digital Entertainment'
                std_div = 'DLS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Application Store', 'Apple', 'Google Play', 'Spotify', 'App Store']:
                std_name = 'DLS - App Store'
                std_div = 'DLS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['OTT', 'FPT Play', 'Galaxy Play', 'VTVgo']:
                std_name = 'DLS - OTT'
                std_div = 'DLS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Offline Payment', 'Retails', 'FnB', 'SME Offline', 'Spa', 'Quản lý chi tiêu', 'SME Merchant', 'Cộng Tác Viên MoMo', 'IPOS', 'Soundbox', 'QR đa năng']:
                std_name = 'DLS - Offline Payment'
                std_div = 'DLS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Caishen', 'Lazada', 'Tiki', 'Tiktok Shop']:
                std_name = 'DLS - Cashien'
                std_div = 'DLS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Dịch vụ liên kết', 'Ads Payment', 'Facebook', 'Mini App']:
                std_name = 'DLS - Token / Services'
                std_div = 'DLS'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Vé số', 'Vietlott SMS']:
                std_name = 'UTI - Lottery'
                std_div = 'UTI'
                target_zone = 'Incubator Zone'
            elif p_name in ['Student Pass']:
                std_name = 'GPD - Sinh Viên'
                std_div = 'GPD'
                target_zone = 'Incubator Zone'
            elif p_name in ['Business Page']:
                std_name = 'GPD - Merchant'
                std_div = 'GPD'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Growth User', 'New User', 'Retention', 'Giới thiệu MoMo', 'Family Hub', 'Cross-Sell']:
                std_name = 'GPD - Growth Campaign / Onboarding'
                std_div = 'GPD'
                target_zone = 'Incubator Zone'
            elif p_name in ['An toàn bảo mật (TRUST)', 'Thủ đoạn lừa đảo', 'Bảo mật giao dịch', 'NFC', 'Bảo mật MoMo', 'KYC', 'Risk']:
                std_name = 'GPD - Trust / BMC - Brand'
                std_div = 'GPD'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['Life At MoMo', 'Event', 'Our Life']:
                std_name = 'BMC - Brand & Culture'
                std_div = 'BMC'
                target_zone = 'Productivity & Self-serve'
            elif p_name in ['MoMo XU', 'Promotion']:
                std_name = 'GPD - Promotion'
                std_div = 'GPD'
                target_zone = 'Productivity & Self-serve'
            else:
                std_name = f'Standardized - {p_name}'
                std_div = 'PS'

        mapped_420.append({
            'Id': p_id,
            'Project': p_name,
            'Project Cha': p_parent,
            'Nature': item_nature,
            'Nature Desc': nature_desc,
            'Std Div': std_div,
            'Std Name': std_name,
            'Target Zone': target_zone,
            'Action': action_req,
            'Link': p_link
        })

    # Write Excel workbook using xlsxwriter
    wb = xlsxwriter.Workbook(out_xlsx)

    # Styles
    f_title = wb.add_format({'bold': True, 'font_size': 14, 'font_color': '#FFFFFF', 'bg_color': '#A50064', 'align': 'left', 'valign': 'vcenter', 'font_name': 'Arial'})
    f_subtitle = wb.add_format({'italic': True, 'font_size': 9, 'font_color': '#475569', 'font_name': 'Arial'})
    f_sec_header = wb.add_format({'bold': True, 'font_size': 10, 'font_color': '#FFFFFF', 'bg_color': '#1E293B', 'align': 'left', 'valign': 'vcenter', 'font_name': 'Arial'})
    f_tbl_header = wb.add_format({'bold': True, 'font_size': 9, 'font_color': '#1E293B', 'bg_color': '#E2E8F0', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_left = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'left', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_center = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_right = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'right', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial', 'num_format': '#,##0'})
    f_cell_pct = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'right', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial', 'num_format': '0.0%'})

    f_tag_proj = wb.add_format({'font_size': 9, 'font_color': '#15803D', 'bg_color': '#DCFCE7', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_tag_nonproj = wb.add_format({'font_size': 9, 'font_color': '#B45309', 'bg_color': '#FEF3C7', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_tag_del = wb.add_format({'font_size': 9, 'font_color': '#B91C1C', 'bg_color': '#FEE2E2', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})

    # ----------------------------------------------------
    # SHEET 1: Executive_Summary
    # ----------------------------------------------------
    ws1 = wb.add_worksheet('Executive_Summary')
    ws1.set_column('A:A', 4)
    ws1.set_column('B:B', 38)
    ws1.set_column('C:C', 18)
    ws1.set_column('D:D', 18)
    ws1.set_column('E:E', 45)

    ws1.merge_range('B2:E2', 'BÁO CÁO PHÂN TÁCH BẢN CHẤT DỰ ÁN & CHUẨN HÓA TAXONOMY WEB MOMO 2026', f_title)
    ws1.write('B3', 'Tham chiếu: [Web MoMo] Overview Web 2026.xlsx (SSOT) | Phạm vi: 420 entries trong CMS', f_subtitle)
    ws1.write('B4', 'Mục tiêu: Phân tách rõ True Projects vs Non-Projects & Áp dụng quy chuẩn đặt tên [Division] - [Product]', f_subtitle)

    # Table 1: Nature of 420 items
    ws1.merge_range('B6:E6', 'I. PHÂN BỔ BẢN CHẤT 420 MỤC ĐANG LƯU TRỮ TRONG CMS PROJECT', f_sec_header)
    for col_idx, h in enumerate(['Nhóm Bản Chất (Classification)', 'Số Lượng Entries', 'Tỷ Trọng (%)', 'Giải Pháp Chuẩn Hóa & Vận Hành']):
        ws1.write(6, 1 + col_idx, h, f_tbl_header)

    nature_counts = defaultdict(int)
    for p in mapped_420:
        nature_counts[p['Nature']] += 1

    nature_rows = [
        ('Dự án Sản phẩm Cốt lõi (True Projects)', nature_counts['TRUE_PROJECT'], nature_counts['TRUE_PROJECT']/420, 'Giữ lại trong CMS Project; đổi tên theo chuẩn [Division] - [Product].'),
        ('Thuộc tính Thể loại Phim (Genre Tags)', nature_counts['DYNAMIC_TAG_GENRE'], nature_counts['DYNAMIC_TAG_GENRE']/420, 'Không phải Project. Chuyển thành Dynamic Tags/Facets thuộc MDS - Cinema.'),
        ('Thực thể Địa lý Điểm đến (Geo Destinations)', nature_counts['DYNAMIC_ENTITY_GEO'], nature_counts['DYNAMIC_ENTITY_GEO']/420, 'Không phải Project. Chuyển sang Database Table Điểm đến của MDS - OTA.'),
        ('Thực thể Cụm Rạp Đối tác (Cinema Partners)', nature_counts['PARTNER_ENTITY_CINEMA'], nature_counts['PARTNER_ENTITY_CINEMA']/420, 'Không phải Project. Chuyển sang Hồ sơ Đối tác Cụm Rạp của MDS - Cinema.'),
        ('Hồ sơ Tổ chức Thiện nguyện (NGO Profiles)', nature_counts['PARTNER_ENTITY_NGO'], nature_counts['PARTNER_ENTITY_NGO']/420, 'Không phải Project. Chuyển sang NGO Directory Table của MDS - Donation.'),
        ('Chiến dịch / Sự kiện Mùa (Campaigns & Events)', nature_counts['CAMPAIGN_EVENT'], nature_counts['CAMPAIGN_EVENT']/420, 'Không phải Standing Project. Lưu trữ (Archive) & 301 Redirect về Hub.'),
        ('Trang Đích / Webview Khuyến mãi (Ad-hoc Pages)', nature_counts['LANDING_PAGE_PROMO'], nature_counts['LANDING_PAGE_PROMO']/420, 'Không phải Project. Chuyển thành Template Webview T&C tự phục vụ.'),
        ('Chuyên mục Con / Chủ đề Nội dung (Sub-categories)', nature_counts['SUB_CATEGORY_OR_TOPIC'], nature_counts['SUB_CATEGORY_OR_TOPIC']/420, 'Không phải Project. Quản trị dưới dạng Category Tree của Master Hub.'),
        ('Dữ liệu Thử nghiệm (Test Data)', nature_counts['TEST_DATA'], nature_counts['TEST_DATA']/420, 'Xóa bỏ hoàn toàn khỏi hệ thống Production CMS.')
    ]

    for row_idx, row in enumerate(nature_rows):
        r_num = 7 + row_idx
        ws1.write(r_num, 1, row[0], f_cell_left)
        ws1.write(r_num, 2, row[1], f_cell_right)
        ws1.write(r_num, 3, row[2], f_cell_pct)
        ws1.write(r_num, 4, row[3], f_cell_left)

    # Table 2: Divisions breakdown
    start_div = 7 + len(nature_rows) + 2
    ws1.merge_range(f'B{start_div}:E{start_div}', 'II. QUY CHUẨN ĐẶT TÊN DỰ ÁN THEO 5 KHỐI DIVISION (OVERVIEW WEB 2026)', f_sec_header)
    for col_idx, h in enumerate(['Khối Nghiệp Vụ (Division)', 'Tên Viết Tắt Chuẩn', 'Lĩnh Vực & Danh Mục Phụ Trách', 'Ví Dụ Đặt Tên Chuẩn Hóa']):
        ws1.write(start_div, 1 + col_idx, h, f_tbl_header)

    div_rules = [
        ('Merchant & Digital Services', 'MDS', 'Cinema, Du lịch (Vé máy bay, Vé xe, Khách sạn, OTA), Ví Nhân Ái, Thổ Địa, Community', 'MDS - Cinema, MDS - Flight, MDS - Bus, MDS - Donation, MDS - OTA'),
        ('Financial Services (Financial Hub)', 'FS', 'Tín dụng CIC, Vay Nhanh, Tiết kiệm, Sàn đầu tư, Chứng khoán, Vàng, Bảo hiểm toàn diện, Ví Trả Sau', 'FS - Loan, FS - Car Insurance, FS - Credit Score, FS - Online Saving, FS - Gold'),
        ('Payment, Utilities & Digital Life', 'PS / UTI / DLS', 'Hóa đơn Billpay, Tiện ích Giao thông / Phạt nguội, Telco 4G, Chuyển tiền, Nạp Game, OTT, Soundbox', 'UTI - Billpay, PS - Phạt Nguội, UTI - Telco, SP - Transfer, DLS - Digital Entertainment'),
        ('Growth Platform Division', 'GPD', 'Cổng Sinh Viên (Student Hub), Merchant Hub, New User Onboarding, Quản lý chi tiêu, Xác thực TRUST', 'GPD - Sinh Viên, GPD - Merchant, GPD - New User, GPD - Trust, GPD - QLCT'),
        ('Brand & Marketing Communications', 'BMC', 'Thương hiệu MoMo, An toàn bảo mật Brand, Cổng Gamification (Lắc Xì, Mega Campaign), Blog/News', 'BMC - Brand, BMC - Gamification, BMC - Trust, BMC - Blog')
    ]

    for row_idx, row in enumerate(div_rules):
        r_num = start_div + 1 + row_idx
        ws1.write(r_num, 1, row[0], f_cell_left)
        ws1.write(r_num, 2, row[1], f_cell_center)
        ws1.write(r_num, 3, row[2], f_cell_left)
        ws1.write(r_num, 4, row[3], f_cell_left)

    # ----------------------------------------------------
    # SHEET 2: Revamped_Standard_Projects
    # ----------------------------------------------------
    ws2 = wb.add_worksheet('Revamped_Standard_Projects')
    ws2.set_column('A:A', 6)
    ws2.set_column('B:B', 12)
    ws2.set_column('C:C', 22)
    ws2.set_column('D:D', 32)
    ws2.set_column('E:E', 32)
    ws2.set_column('F:F', 45)
    ws2.set_column('G:G', 22)
    ws2.set_column('H:H', 22)
    ws2.set_column('I:I', 20)

    ws2.merge_range('A1:I1', 'DANH SÁCH DỰ ÁN WEB MOMO CHUẨN HÓA NĂM 2026 (STANDARDIZED PRODUCT PROJECTS)', f_title)

    headers_std = [
        'STT', 'Division', 'Use Case', 'Tên Dự Án Chuẩn (Product Name)',
        'Tên Dịch Vụ (Service Name)', 'Đường Dẫn URL Chuẩn (Standard URL)',
        'Loại Trang (Page Type)', 'Phân Vùng 4-Zone', 'Ghi Chú Kỹ Thuật'
    ]
    for col_idx, h in enumerate(headers_std):
        ws2.write(1, col_idx, h, f_tbl_header)

    for row_idx, p in enumerate(unique_std_projects):
        r_num = 2 + row_idx
        ws2.write(r_num, 0, row_idx + 1, f_cell_center)
        ws2.write(r_num, 1, p['division'], f_cell_center)
        ws2.write(r_num, 2, p['use_case'], f_cell_left)
        ws2.write(r_num, 3, p['product'], f_cell_left)
        ws2.write(r_num, 4, p['service'], f_cell_left)
        ws2.write(r_num, 5, p['url'], f_cell_left)
        ws2.write(r_num, 6, p['page_type'], f_cell_center)

        # 4-Zone mapping
        zone = 'Productivity & Self-serve'
        if p['division'] == 'MDS' and p['use_case'] in ['Cinema', 'Flight', 'Bus', 'OTA', 'Hourly Hour']:
            zone = 'Performance Zone'
        elif p['division'] == 'FS':
            zone = 'Transformation Zone'
        elif p['product'] in ['PS - Phạt Nguội', 'UTI - Vehicle']:
            zone = 'Transformation Zone'
        elif p['product'] in ['GPD - Sinh Viên', 'UTI - Lottery', 'GPD - New User']:
            zone = 'Incubator Zone'

        ws2.write(r_num, 7, zone, f_cell_left)
        ws2.write(r_num, 8, p['note'] if p['note'] else 'Standard Web Product', f_cell_left)

    ws2.autofilter(1, 0, 1 + len(unique_std_projects), len(headers_std) - 1)
    ws2.freeze_panes(2, 4)

    # ----------------------------------------------------
    # SHEET 3: Non_Project_Classification
    # ----------------------------------------------------
    ws3 = wb.add_worksheet('Non_Project_Classification')
    ws3.set_column('A:A', 8)
    ws3.set_column('B:B', 32)
    ws3.set_column('C:C', 24)
    ws3.set_column('D:D', 35)
    ws3.set_column('E:E', 45)
    ws3.set_column('F:F', 35)

    ws3.merge_range('A1:F1', 'DANH SÁCH 239 MỤC TRONG CMS KHÔNG PHẢI LÀ PROJECT VÀ PHƯƠNG ÁN XỬ LÝ', f_title)

    headers_non = [
        'ID CMS', 'Tên Mục Hiện Tại', 'Dự Án Cha Trong CMS',
        'Bản Chất Thực Tế (Nature)', 'Giải Pháp Kỹ Thuật / Vận Hành (Action Plan)',
        'Định Tuyến Về Master Hub Nào'
    ]
    for col_idx, h in enumerate(headers_non):
        ws3.write(1, col_idx, h, f_tbl_header)

    non_proj_items = [p for p in mapped_420 if p['Nature'] != 'TRUE_PROJECT']

    for row_idx, p in enumerate(non_proj_items):
        r_num = 2 + row_idx
        ws3.write(r_num, 0, int(p['Id']), f_cell_center)
        ws3.write(r_num, 1, p['Project'], f_cell_left)
        ws3.write(r_num, 2, p['Project Cha'], f_cell_left)
        ws3.write(r_num, 3, p['Nature Desc'], f_cell_left)
        ws3.write(r_num, 4, p['Action'], f_cell_left)
        ws3.write(r_num, 5, p['Std Name'], f_cell_left)

    ws3.autofilter(1, 0, 1 + len(non_proj_items), len(headers_non) - 1)
    ws3.freeze_panes(2, 2)

    # ----------------------------------------------------
    # SHEET 4: All_420_CMS_Audit_Mapped
    # ----------------------------------------------------
    ws4 = wb.add_worksheet('All_420_CMS_Audit_Mapped')
    ws4.set_column('A:A', 8)
    ws4.set_column('B:B', 32)
    ws4.set_column('C:C', 24)
    ws4.set_column('D:D', 18)
    ws4.set_column('E:E', 35)
    ws4.set_column('F:F', 12)
    ws4.set_column('G:G', 35)
    ws4.set_column('H:H', 22)
    ws4.set_column('I:I', 45)
    ws4.set_column('J:J', 45)

    headers_all = [
        'ID CMS', 'Tên Trên CMS', 'Dự Án Cha CMS', 'Có Phải Project?',
        'Bản Chất Thực Tế', 'Division', 'Tên Dự Án / Hub Chuẩn Hóa Đề Xuất',
        'Phân Vùng 4-Zone', 'Hành Động Xử Lý Chi Tiết', 'Link CMS Admin'
    ]
    for col_idx, h in enumerate(headers_all):
        ws4.write(0, col_idx, h, f_tbl_header)

    for row_idx, p in enumerate(mapped_420):
        r_num = 1 + row_idx
        ws4.write(r_num, 0, int(p['Id']), f_cell_center)
        ws4.write(r_num, 1, p['Project'], f_cell_left)
        ws4.write(r_num, 2, p['Project Cha'], f_cell_left)

        is_proj = 'TRUE PROJECT' if p['Nature'] == 'TRUE_PROJECT' else 'NON-PROJECT'
        fmt_proj = f_tag_proj if is_proj == 'TRUE PROJECT' else f_tag_nonproj
        if p['Nature'] == 'TEST_DATA':
            fmt_proj = f_tag_del

        ws4.write(r_num, 3, is_proj, fmt_proj)
        ws4.write(r_num, 4, p['Nature Desc'], f_cell_left)
        ws4.write(r_num, 5, p['Std Div'], f_cell_center)
        ws4.write(r_num, 6, p['Std Name'], f_cell_left)
        ws4.write(r_num, 7, p['Target Zone'], f_cell_left)
        ws4.write(r_num, 8, p['Action'], f_cell_left)
        ws4.write(r_num, 9, p['Link'], f_cell_left)

    ws4.autofilter(0, 0, len(mapped_420), len(headers_all) - 1)
    ws4.freeze_panes(1, 2)

    # ----------------------------------------------------
    # SHEET 5: Roadmap_and_Governance
    # ----------------------------------------------------
    ws5 = wb.add_worksheet('Roadmap_and_Governance')
    ws5.set_column('A:A', 6)
    ws5.set_column('B:B', 14)
    ws5.set_column('C:C', 20)
    ws5.set_column('D:D', 35)
    ws5.set_column('E:E', 45)
    ws5.set_column('F:F', 24)

    ws5.merge_range('B2:F2', 'LỘ TRÌNH THỰC THI TÁI CẤU TRÚC CMS & QUY CHẾ VẬN HÀNH', f_title)

    ws5.merge_range('B4:F4', 'I. KẾ HOẠCH HÀNH ĐỘNG 4 BƯỚC THIẾT LẬP LẠI HỆ THỐNG CMS', f_sec_header)
    for col_idx, h in enumerate(['Bước', 'Thời Gian', 'Hạng Mục Triển Khai', 'Chi Tiết Kỹ Thuật & Nghiệp Vụ', 'Đội Ngũ Phụ Trách']):
        ws5.write(4, 1 + col_idx, h, f_tbl_header)

    plan_steps = [
        ('Bước 1', '01/09 - 05/09/2026', 'Tách Lọc Dữ Liệu Non-Project', 'Trích xuất 52 thể loại phim & 54 điểm đến sang bảng Dynamic Facets/Entity DB; chuyển 18 NGO sang Directory Profile; dọn 2 test nodes.', 'Web Dev Team (R/A),\nContent Team (C)'),
        ('Bước 2', '06/09 - 12/09/2026', 'Đổi Tên & Áp Dụng Chuẩn [Division] - [Product]', 'Đổi tên toàn bộ True Projects trên CMS theo cú pháp chuẩn của Overview Web 2026 (FS - Loan, MDS - Cinema, UTI - Billpay...).', 'Web Dev Team (R),\nInbound Team (A)'),
        ('Bước 3', '13/09 - 20/09/2026', 'Lưu Trữ (Archive) 36 Campaign Lịch Sử', 'Đưa 36 chiến dịch cũ vào trạng thái Archive trong CMS và thiết lập rule 301 Redirect trên Edge/CDN về Master Hub.', 'SEO Vendor (R/A),\nWeb Dev Team (R)'),
        ('Bước 4', '21/09 - 30/09/2026', 'Thiết Lập Bộ Lọc Guardrails Chặn Tạo Sai', 'Lập trình bộ quy tắc trên CMS: Chặn tạo project nếu không thuộc danh mục Division duyệt; bắt buộc gắn URL chuẩn SEO.', 'Web Dev Team (R/A),\nInbound Team (A)')
    ]

    for row_idx, row in enumerate(plan_steps):
        r_num = 5 + row_idx
        ws5.write(r_num, 1, row[0], f_cell_left)
        ws5.write(r_num, 2, row[1], f_cell_center)
        ws5.write(r_num, 3, row[2], f_cell_left)
        ws5.write(r_num, 4, row[3], f_cell_left)
        ws5.write(r_num, 5, row[4], f_cell_left)

    wb.close()
    print(f"Successfully generated revamped Excel workbook at: {out_xlsx}")

if __name__ == '__main__':
    generate_revamped_workbook()
