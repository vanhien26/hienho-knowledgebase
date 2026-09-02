import csv
import os
import openpyxl
import xlsxwriter
from collections import defaultdict

def create_standardized_project_name_excel():
    csv_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/data/cms_projects.csv'
    overview_path = '/Users/hienhv/Downloads/[Web MoMo] Overview Web 2026.xlsx'
    out_dir = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/sheets'
    os.makedirs(out_dir, exist_ok=True)
    out_xlsx = os.path.join(out_dir, 'project_name.xlsx')

    cms_projects = list(csv.DictReader(open(csv_path, encoding='utf-8')))

    # Read Overview Web 2026 for URL / PageType mapping
    wb_ref = openpyxl.load_workbook(overview_path, data_only=True)
    ws_mini = wb_ref['Mini Web']
    ref_map = {}
    for r in range(2, ws_mini.max_row + 1):
        div = ws_mini.cell(r, 1).value
        uc = ws_mini.cell(r, 2).value
        srv = ws_mini.cell(r, 4).value
        url = ws_mini.cell(r, 5).value
        pt = ws_mini.cell(r, 6).value
        note = ws_mini.cell(r, 7).value
        if srv:
            ref_map[str(srv).strip().lower()] = {
                'division': str(div).strip() if div else '',
                'use_case': str(uc).strip() if uc else '',
                'url': str(url).strip() if url else '',
                'page_type': str(pt).strip() if pt else 'Advanced MiniWeb',
                'note': str(note).strip() if note else ''
            }

    ngo_keywords = ['Quỹ', 'DNXH', 'Foundation', 'Sức mạnh', 'Thiện Nhân', 'SCDI', 'Operation', 'Trung Tâm', 'Hoa Chia Sẻ', 'msd', 'Teach', 'WildAct', 'Bếp', 'Saigon', 'VinaCapital', 'Trăng Khuyết', 'Hy Vọng']
    legacy_camp_ids = {
        '90', '134', '152', '258', '19', '301', '344', '340', '376', '414',
        '576', '415', '462', '60', '530', '202', '225', '311', '324', '328',
        '337', '342', '350', '361', '371', '387', '399', '406', '533', '648',
        '681', '740', '688'
    }

    all_processed = []

    for p in cms_projects:
        p_id = p['Id']
        raw_name = p['Project']
        raw_parent = p['Project Cha'].strip()
        link = p['Link']

        # Default values
        std_name = raw_name
        std_parent = raw_parent if raw_parent else 'Master Hub (Gốc)'
        status = 'Chuẩn'
        reason = 'Chuẩn - Dự án Sản phẩm Cốt lõi (True Project)'
        cluster = '10. Utilities & Khác'
        cluster_order = 10
        div = 'PS'
        use_case = 'Utilities'
        url = f"https://www.momo.vn/{p_id}"
        page_type = 'Advanced MiniWeb'
        zone = 'Productivity & Self-serve'
        action = 'Giữ lại & Chuẩn hóa cấu trúc.'

        # 1. Cinema Cluster
        if raw_name == 'Cinema' or raw_parent in ['Cinema', 'Phim chiếu', 'Blog Phim', 'Quốc gia', 'Rạp chiếu', 'Diễn viên', 'Phim hay', 'Netflix']:
            cluster = '01. Cinema'
            cluster_order = 1
            div = 'MDS'
            use_case = 'Cinema'
            zone = 'Performance Zone'
            url = 'https://www.momo.vn/cinema'
            if raw_name == 'Cinema':
                std_parent = 'Master Hub (Gốc)'
                status = 'Chuẩn'
                reason = 'Chuẩn - Master Hub Điện Ảnh'
                page_type = 'Master Hub Platform'
            elif raw_parent == 'Phim chiếu':
                std_parent = 'Phim chiếu'
                status = 'Thừa'
                reason = 'Thừa - Thể loại phim (Dynamic Genre Tag)'
                action = 'Chuyển sang Tag / Dynamic Facet của Cinema Hub.'
                page_type = 'Dynamic Facet'
            elif raw_parent == 'Rạp chiếu':
                std_parent = 'Rạp chiếu'
                status = 'Thừa'
                reason = 'Thừa - Cụm rạp đối tác (Cinema Partner Entity)'
                action = 'Chuyển sang Cinema Partner Profile của Cinema Hub.'
                page_type = 'Partner Entity'
            elif raw_parent in ['Blog Phim', 'Quốc gia', 'Diễn viên', 'Phim hay', 'Netflix']:
                std_parent = raw_parent
                status = 'Thừa'
                reason = f'Thừa - Chuyên mục con / Topic thuộc {raw_parent}'
                action = 'Quản trị dưới dạng Category Tree của Cinema Hub.'
                page_type = 'Category / Topic'
            else:
                std_parent = 'Cinema'
                status = 'Chuẩn'
                reason = 'Chuẩn - Danh mục con của Cinema'

        # 2. Financial Services Cluster
        elif raw_name in ['Tài chính - Bảo hiểm', 'Tài chính', 'Bảo hiểm', 'Bảo hiểm xe máy', 'Bảo hiểm xe máy Landing Page', 'Vay Nhanh Landing Page'] or raw_parent in ['Tài chính - Bảo hiểm', 'Tài chính', 'Sàn Đầu Tư', 'Ví Trả Sau', 'Vay Nhanh Landing Page', 'Bảo hiểm', 'Bảo hiểm ô tô']:
            cluster = '02. Financial Services & InsurTech'
            cluster_order = 2
            div = 'FS'
            zone = 'Transformation Zone'
            url = 'https://www.momo.vn/tai-chinh'

            # Clean name typo
            if 'Simular' in raw_name:
                std_name = raw_name.replace('Simular', 'Simulator')

            # Clean parent
            if raw_name in ['Bảo hiểm xe máy', 'Bảo hiểm xe máy Landing Page']:
                std_parent = 'Bảo hiểm'
                if 'Landing Page' in raw_name:
                    status = 'Thừa'
                    reason = 'Thừa - Trang đích / Webview khuyến mãi (Ad-hoc Landing Page)'
                    action = 'Gộp vào chuyên mục Bảo hiểm xe máy thuộc Bảo hiểm.'
                    page_type = 'Ad-hoc Landing Page'
                else:
                    status = 'Chuẩn'
                    reason = 'Chuẩn - Dự án Bảo hiểm xe máy'
                    url = 'https://www.momo.vn/bao-hiem-xe-may'
            elif raw_name in ['Vay Nhanh Landing Page', 'Vay Nhanh', 'Vay nhanh nhà bán hàng', 'Vay Nhanh - Simular']:
                std_parent = 'Vay Nhanh'
                if raw_name == 'Vay Nhanh Landing Page':
                    status = 'Thừa'
                    reason = 'Thừa - Trang đích / Gốc tách rời (Ad-hoc Landing Page)'
                    action = 'Gộp vào chuyên mục Vay Nhanh thuộc Financial Hub.'
                    page_type = 'Ad-hoc Landing Page'
                else:
                    status = 'Chuẩn'
                    reason = 'Chuẩn - Dự án Vay Nhanh & Vay tiêu dùng'
                    url = 'https://www.momo.vn/vay-nhanh'
            elif raw_name == 'Ví Trả Sau Landing Page':
                std_parent = 'Ví Trả Sau'
                status = 'Thừa'
                reason = 'Thừa - Trang đích đơn lẻ (Ad-hoc Landing Page)'
                action = 'Gộp vào chuyên mục Ví Trả Sau thuộc Financial Hub.'
                page_type = 'Ad-hoc Landing Page'
            elif raw_parent in ['Ví Trả Sau', 'Sàn Đầu Tư']:
                std_parent = raw_parent
                status = 'Thừa'
                reason = f'Thừa - Chuyên mục con / Topic thuộc {raw_parent}'
                action = 'Quản trị dưới dạng Category Tree của Financial Hub.'
                page_type = 'Category / Topic'
            else:
                std_parent = 'Tài chính - Bảo hiểm'
                status = 'Chuẩn'
                reason = 'Chuẩn - Dự án Dịch vụ Tài chính'

            # Specific use cases
            if 'Vay' in raw_name or 'Flik' in raw_name:
                use_case = 'Loan'
            elif 'Bảo hiểm' in raw_name:
                use_case = 'InsurTech'
            elif 'Tín dụng' in raw_name or 'CIC' in raw_name:
                use_case = 'Credit Score'
            elif 'Vàng' in raw_name:
                use_case = 'Gold'
            elif 'Tiết kiệm' in raw_name:
                use_case = 'Online Saving'
            elif 'Túi Thần Tài' in raw_name:
                use_case = 'TTT'
            elif 'Ví Trả Sau' in raw_name:
                use_case = 'PayLater'
            elif 'Đầu tư' in raw_name or 'Chứng khoán' in raw_name:
                use_case = 'Brokerage'
            elif 'Chứng Chỉ Quỹ' in raw_name:
                use_case = 'Mutual Funds'
            elif 'Apple' in raw_name:
                use_case = 'Device Financing'
            else:
                use_case = 'Financial Hub'

        # 3. Vehicle & Giao thông Cluster
        elif raw_name in ['Tiện ích giao thông'] or raw_parent in ['Tiện ích giao thông']:
            cluster = '03. Vehicle & Giao Thông'
            cluster_order = 3
            div = 'PS'
            zone = 'Transformation Zone'
            std_parent = 'Tiện ích giao thông'
            if raw_name == 'Tiện ích giao thông':
                std_parent = 'Master Hub (Gốc)'
                use_case = 'Vehicle Hub'
                url = 'https://www.momo.vn/tien-ich-giao-thong'
                page_type = 'Master Hub Platform'
            elif raw_name == 'Phạt nguội':
                use_case = 'Phạt Nguội'
                url = 'https://www.momo.vn/phat-nguoi'
            else:
                use_case = 'Vehicle Utilities'
            status = 'Chuẩn'
            reason = 'Chuẩn - Tiện ích Cổng Giao thông'

        # 4. Travel & OTA Cluster
        elif raw_name in ['OTA'] or raw_parent in ['OTA', 'Vé máy bay', 'Vé xe khách', 'OTA Game', 'Điểm đến']:
            cluster = '04. Travel & OTA'
            cluster_order = 4
            div = 'MDS'
            zone = 'Performance Zone'
            url = 'https://www.momo.vn/du-lich-di-lai'
            if raw_name == 'OTA':
                std_parent = 'Master Hub (Gốc)'
                status = 'Chuẩn'
                reason = 'Chuẩn - Master Hub Du lịch & Đi lại'
                use_case = 'OTA'
                page_type = 'Master Hub Platform'
            elif raw_parent == 'Điểm đến':
                std_parent = 'Điểm đến'
                status = 'Thừa'
                reason = 'Thừa - Điểm đến du lịch (Geo Destination Entity)'
                action = 'Chuyển sang Destination Entity Database của OTA Hub.'
                use_case = 'OTA'
                page_type = 'Geo Entity'
            elif raw_parent in ['Vé máy bay', 'Vé xe khách', 'OTA Game']:
                std_parent = raw_parent
                status = 'Thừa'
                reason = f'Thừa - Chuyên mục con / Đối tác thuộc {raw_parent}'
                action = 'Quản trị dưới dạng Category Tree của OTA Hub.'
                page_type = 'Category / Topic'
                use_case = 'Flight' if raw_parent == 'Vé máy bay' else 'Bus'
            else:
                std_parent = 'OTA'
                status = 'Chuẩn'
                reason = 'Chuẩn - Danh mục con của OTA'
                use_case = 'OTA'

        # 5. Student Hub
        elif raw_name == 'Student Pass':
            cluster = '05. Student Hub'
            cluster_order = 5
            div = 'GPD'
            use_case = 'Sinh Viên'
            zone = 'Incubator Zone'
            std_parent = 'Master Hub (Gốc)'
            url = 'https://www.momo.vn/sinh-vien'
            status = 'Chuẩn'
            reason = 'Chuẩn - Cổng Thông tin Sinh Viên'
            page_type = 'Master Hub Platform'

        # 6. Utilities & Billpay Cluster
        elif raw_name in ['Billpay', 'Telco', 'Vé số'] or raw_parent in ['Billpay', 'Học phí', 'Dịch vụ công', 'Telco', 'Airtime', 'Topup', 'Vé số']:
            cluster = '06. Utilities, Billpay & Telco'
            cluster_order = 6
            div = 'PS'
            zone = 'Productivity & Self-serve'
            if raw_parent in ['Học phí', 'Dịch vụ công', 'Airtime', 'Topup']:
                std_parent = raw_parent
                status = 'Thừa'
                reason = f'Thừa - Chuyên mục con / Topic thuộc {raw_parent}'
                action = 'Quản trị dưới dạng Category Tree của Billpay / Telco.'
                page_type = 'Category / Topic'
            else:
                std_parent = raw_parent if raw_parent else 'Master Hub (Gốc)'
                status = 'Chuẩn'
                reason = 'Chuẩn - Dịch vụ Hóa đơn & Viễn thông'
            
            if 'Billpay' in raw_name or raw_parent == 'Billpay':
                use_case = 'Billpay'
                url = 'https://www.momo.vn/thanh-toan-hoa-don'
            elif 'Telco' in raw_name or raw_parent == 'Telco':
                use_case = 'Telco'
                url = 'https://www.momo.vn/nap-tien-dien-thoai'
            elif 'Vé số' in raw_name or raw_parent == 'Vé số':
                use_case = 'Lottery'
                zone = 'Incubator Zone'
                url = 'https://www.momo.vn/ve-so'

        # 7. Payment Core Cluster
        elif raw_name in ['Chuyển Nhận Tiền'] or raw_parent in ['Chuyển Nhận Tiền']:
            cluster = '07. Payment Core'
            cluster_order = 7
            div = 'PS'
            use_case = 'Transfer / P2P'
            zone = 'Productivity & Self-serve'
            std_parent = 'Chuyển Nhận Tiền' if raw_name != 'Chuyển Nhận Tiền' else 'Master Hub (Gốc)'
            status = 'Chuẩn'
            reason = 'Chuẩn - Cốt lõi Chuyển Nhận Tiền'
            url = 'https://www.momo.vn/chuyen-nhan-tien'

        # 8. Donation Cluster
        elif raw_name in ['Donation'] or raw_parent in ['Donation', 'Heo đất MoMo - Quyên góp', 'Ví Nhân Ái - Blog', 'Donation Campaign']:
            cluster = '08. Donation & Ví Nhân Ái'
            cluster_order = 8
            div = 'MDS'
            use_case = 'Donation'
            zone = 'Productivity & Self-serve'
            url = 'https://www.momo.vn/vi-nhan-ai'
            if raw_name == 'Donation':
                std_parent = 'Master Hub (Gốc)'
                status = 'Chuẩn'
                reason = 'Chuẩn - Master Hub Ví Nhân Ái'
                page_type = 'Master Hub Platform'
            elif raw_parent == 'Donation' and any(k in raw_name for k in ngo_keywords):
                std_parent = 'Donation'
                status = 'Thừa'
                reason = 'Thừa - Tổ chức thiện nguyện (NGO Partner Profile)'
                action = 'Chuyển sang NGO Directory Table của Donation Hub.'
                page_type = 'Partner Entity'
            elif raw_parent in ['Ví Nhân Ái - Blog', 'Heo đất MoMo - Quyên góp', 'Donation Campaign']:
                std_parent = raw_parent
                status = 'Thừa'
                reason = f'Thừa - Chuyên mục con / Topic thuộc {raw_parent}'
                action = 'Quản trị dưới dạng Category Tree của Donation Hub.'
                page_type = 'Category / Topic'
            else:
                std_parent = 'Donation'
                status = 'Chuẩn'
                reason = 'Chuẩn - Danh mục con của Donation'

        # 9. Merchant & Partner Hub
        elif raw_name in ['Caishen', 'SME Merchant', 'Dịch vụ liên kết', 'Ads Payment', 'Offline Payment', 'Soundbox', 'Marketing Solution', 'Business Page'] or raw_parent in ['Caishen', 'SME Merchant', 'Dịch vụ liên kết', 'Application Store', 'Apple', 'Tiktok', 'Online Payment', 'Delivery', 'Logistics', 'OTT', 'Ads Payment', 'Offline Payment', 'SME Offline']:
            cluster = '09. Merchant & Partner Hub'
            cluster_order = 9
            div = 'PS'
            use_case = 'Merchant & Partners'
            zone = 'Productivity & Self-serve'
            if raw_parent in ['Application Store', 'Apple', 'Tiktok', 'Delivery', 'Logistics', 'OTT', 'SME Offline']:
                std_parent = raw_parent
                status = 'Thừa'
                reason = f'Thừa - Chuyên mục con / Đối tác thuộc {raw_parent}'
                action = 'Quản trị dưới dạng Category Tree của Merchant & Partner Hub.'
                page_type = 'Category / Topic'
            else:
                std_parent = raw_parent if raw_parent else 'Master Hub (Gốc)'
                status = 'Chuẩn'
                reason = 'Chuẩn - Giải pháp Doanh nghiệp & Đối tác'

        # 10. Campaigns & Events
        elif raw_name in ['Campaign MoMo', 'Lắc xì 2026', 'Popup Ads'] or raw_parent in ['Campaign MoMo', 'Tài chính cá nhân', 'Popup Ads'] or raw_parent == 'Deal' or '[PROMOTION]' in raw_name or p_id in legacy_camp_ids:
            cluster = '11. Campaigns & Sự Kiện Mùa'
            cluster_order = 11
            div = 'BMC'
            use_case = 'Gamification & Promo'
            zone = 'Productivity & Self-serve'
            if raw_name == 'Campaign MoMo':
                std_parent = 'Master Hub (Gốc)'
                status = 'Chuẩn'
                reason = 'Chuẩn - Cổng Quản lý Chiến dịch (Master Container)'
                page_type = 'Master Hub Platform'
            elif raw_parent == 'Deal' or '[PROMOTION]' in raw_name:
                std_parent = 'Promotion'
                std_name = raw_name.replace('[PROMOTION] - ', '')
                status = 'Thừa'
                reason = 'Thừa - Trang đích / Webview khuyến mãi (Ad-hoc Landing Page)'
                action = 'Sửa danh mục cha về Promotion (295) & Chuyển sang Webview T&C tự phục vụ.'
                page_type = 'Ad-hoc Landing Page'
            elif raw_name == 'Lắc xì 2026':
                std_parent = 'Campaign MoMo'
                status = 'Thừa'
                reason = 'Thừa - Chiến dịch tạo nhầm thành gốc Cấp 1 (Campaign Event)'
                action = 'Gán danh mục cha về Campaign MoMo (89).'
                page_type = 'Campaign Event'
            else:
                std_parent = 'Campaign MoMo'
                status = 'Thừa'
                reason = 'Thừa - Chiến dịch / Sự kiện cũ (Campaign / Event)'
                action = 'Lưu trữ (Archive) & Cấu hình 301 Redirect về Hub tương ứng.'
                page_type = 'Campaign Event'

        # 11. Growth User & Trust
        elif raw_name in ['Growth User', 'An toàn bảo mật (TRUST)', 'Life At MoMo', 'MOMO', 'Promotion', 'MoMo XU', 'Mini App', 'Sim chính chủ', 'eSim du lịch'] or raw_parent in ['Growth User', 'An toàn bảo mật (TRUST)', 'Life At MoMo', 'MOMO', 'Promotion', 'eSim du lịch']:
            cluster = '10. Brand, Growth & Trust'
            cluster_order = 10
            div = 'GPD'
            if 'Life At MoMo' in raw_name or raw_parent == 'Life At MoMo':
                div = 'BMC'
                use_case = 'Brand Culture'
            elif 'TRUST' in raw_name or raw_parent == 'An toàn bảo mật (TRUST)':
                div = 'GPD'
                use_case = 'Trust & Security'
            else:
                use_case = 'Growth & Onboarding'
                zone = 'Incubator Zone'

            if raw_parent in ['An toàn bảo mật (TRUST)', 'Life At MoMo', 'Growth User']:
                std_parent = raw_parent
                status = 'Thừa'
                reason = f'Thừa - Chuyên mục con / Topic thuộc {raw_parent}'
                action = 'Quản trị dưới dạng Category Tree thuộc Brand & Growth Hub.'
                page_type = 'Category / Topic'
            else:
                std_parent = raw_parent if raw_parent else 'Master Hub (Gốc)'
                status = 'Chuẩn'
                reason = 'Chuẩn - Dự án Nền tảng & Tăng trưởng'

        # 12. Test Data
        elif p_id in ['540', '541'] or 'Test' in raw_name or raw_name == 'Web Platform':
            cluster = '12. Dữ Liệu Thử Nghiệm'
            cluster_order = 12
            div = 'GPD'
            use_case = 'Test'
            zone = 'Productivity & Self-serve'
            if p_id in ['540', '541']:
                status = 'Thừa'
                reason = 'Thừa - Dữ liệu thử nghiệm trên Production (Test Data)'
                action = 'Xóa bỏ hoàn toàn khỏi Production CMS.'
                page_type = 'Test Node'
            else:
                std_parent = 'Master Hub (Gốc)'
                status = 'Chuẩn'
                reason = 'Chuẩn - Cổng Kỹ thuật Web Platform'

        # Fetch refined URL / PageType if in ref_map
        lookup_key = std_name.lower().strip()
        if lookup_key in ref_map:
            ref_info = ref_map[lookup_key]
            if ref_info['url']:
                url = ref_info['url']
            if ref_info['division']:
                div = ref_info['division']
            if ref_info['use_case']:
                use_case = ref_info['use_case']
            if ref_info['page_type']:
                page_type = ref_info['page_type']

        all_processed.append({
            'id': int(p_id),
            'std_name': std_name,
            'raw_name': raw_name,
            'std_parent': std_parent,
            'raw_parent': raw_parent,
            'status': status,
            'reason': reason,
            'use_case': use_case,
            'division': div,
            'url': url,
            'page_type': page_type,
            'zone': zone,
            'action': action,
            'link': link,
            'cluster': cluster,
            'cluster_order': cluster_order
        })

    # Sort items logically:
    # 1. Cluster order
    # 2. Status: Chuẩn (0) before Thừa (1)
    # 3. Standard Parent
    # 4. Standard Name
    all_processed.sort(key=lambda x: (
        x['cluster_order'],
        0 if x['status'] == 'Chuẩn' else 1,
        x['std_parent'],
        x['std_name'],
        x['id']
    ))

    # Write Excel workbook with ONLY 1 SHEET
    wb = xlsxwriter.Workbook(out_xlsx)
    ws = wb.add_worksheet('Project_Name')

    # Styles
    f_title = wb.add_format({'bold': True, 'font_size': 13, 'font_color': '#FFFFFF', 'bg_color': '#A50064', 'align': 'left', 'valign': 'vcenter', 'font_name': 'Arial'})
    f_subtitle = wb.add_format({'italic': True, 'font_size': 9, 'font_color': '#475569', 'font_name': 'Arial'})
    f_tbl_header = wb.add_format({'bold': True, 'font_size': 9, 'font_color': '#1E293B', 'bg_color': '#E2E8F0', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_left = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'left', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_center = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_bold = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'bold': True, 'align': 'left', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_url = wb.add_format({'font_size': 9, 'font_color': '#0284C7', 'align': 'left', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})

    # Status styles
    f_status_chuan = wb.add_format({'font_size': 9, 'font_color': '#15803D', 'bg_color': '#DCFCE7', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_status_thua = wb.add_format({'font_size': 9, 'font_color': '#B45309', 'bg_color': '#FEF3C7', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})

    # Zone styles
    f_zone_perf = wb.add_format({'font_size': 9, 'font_color': '#166534', 'bg_color': '#DCFCE7', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_zone_trans = wb.add_format({'font_size': 9, 'font_color': '#1E40AF', 'bg_color': '#DBEAFE', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_zone_incub = wb.add_format({'font_size': 9, 'font_color': '#854D0E', 'bg_color': '#FEF9C3', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_zone_prod = wb.add_format({'font_size': 9, 'font_color': '#475569', 'bg_color': '#F1F5F9', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})

    # Column widths
    ws.set_column('A:A', 6)   # STT
    ws.set_column('B:B', 8)   # ID CMS
    ws.set_column('C:C', 30)  # Project Name (Chuẩn)
    ws.set_column('D:D', 26)  # Project Cha (Chuẩn)
    ws.set_column('E:E', 16)  # Phân Loại (Chuẩn / Thừa)
    ws.set_column('F:F', 38)  # Lý Do Thừa / Bản Chất
    ws.set_column('G:G', 20)  # Use Case
    ws.set_column('H:H', 10)  # Division
    ws.set_column('I:I', 30)  # Cụm Nghiệp Vụ
    ws.set_column('J:J', 28)  # Project Name (Gốc CMS)
    ws.set_column('K:K', 24)  # Project Cha (Gốc CMS)
    ws.set_column('L:L', 38)  # URL
    ws.set_column('M:M', 20)  # Loại Trang
    ws.set_column('N:N', 22)  # Phân Vùng 4-Zone
    ws.set_column('O:O', 45)  # Hành Động Xử Lý Chi Tiết
    ws.set_column('P:P', 45)  # Link CMS Admin

    # Title & Metadata
    ws.merge_range('A1:P1', 'BẢNG CHUẨN HÓA VÀ PHÂN LOẠI TOÀN BỘ 420 DỰ ÁN CMS WEB MOMO NĂM 2026', f_title)
    ws.write('A2', 'Tài liệu chuẩn hóa tên dự án (không kẹp Division), phân tách rõ ràng mục Chuẩn vs Thừa | Nguồn SSOT: [Web MoMo] Overview Web 2026.xlsx', f_subtitle)

    # Headers
    headers = [
        'STT', 'ID CMS', 'Project Name (Tên Chuẩn Hóa)', 'Project Cha (Parent Chuẩn)',
        'Phân Loại', 'Ghi Chú / Lý Do Thừa (Bản Chất)', 'Use Case', 'Division',
        'Cụm Nghiệp Vụ (Cluster)', 'Project Name (Gốc CMS)', 'Project Cha (Gốc CMS)',
        'URL', 'Loại Trang (Page Type)', 'Phân Vùng 4-Zone', 'Hành Động Xử Lý Chi Tiết', 'Link CMS Admin'
    ]
    for col_idx, h in enumerate(headers):
        ws.write(3, col_idx, h, f_tbl_header)

    for row_idx, item in enumerate(all_processed):
        r_num = 4 + row_idx
        ws.write(r_num, 0, row_idx + 1, f_cell_center)
        ws.write(r_num, 1, item['id'], f_cell_center)
        ws.write(r_num, 2, item['std_name'], f_cell_bold)
        ws.write(r_num, 3, item['std_parent'], f_cell_left)

        # Status formatting
        stat_fmt = f_status_chuan if item['status'] == 'Chuẩn' else f_status_thua
        ws.write(r_num, 4, item['status'], stat_fmt)
        ws.write(r_num, 5, item['reason'], f_cell_left)

        ws.write(r_num, 6, item['use_case'], f_cell_left)
        ws.write(r_num, 7, item['division'], f_cell_center)
        ws.write(r_num, 8, item['cluster'], f_cell_left)
        ws.write(r_num, 9, item['raw_name'], f_cell_left)
        ws.write(r_num, 10, item['raw_parent'], f_cell_left)
        ws.write(r_num, 11, item['url'], f_cell_url)
        ws.write(r_num, 12, item['page_type'], f_cell_center)

        # Zone formatting
        z_str = item['zone']
        if z_str == 'Performance Zone':
            z_fmt = f_zone_perf
        elif z_str == 'Transformation Zone':
            z_fmt = f_zone_trans
        elif z_str == 'Incubator Zone':
            z_fmt = f_zone_incub
        else:
            z_fmt = f_zone_prod
        ws.write(r_num, 13, z_str, z_fmt)

        ws.write(r_num, 14, item['action'], f_cell_left)
        ws.write(r_num, 15, item['link'], f_cell_left)

    ws.autofilter(3, 0, 3 + len(all_processed), len(headers) - 1)
    ws.freeze_panes(4, 3)

    wb.close()
    print(f"Successfully generated clean standardized Excel workbook at: {out_xlsx} (Total rows: {len(all_processed)})")

if __name__ == '__main__':
    create_standardized_project_name_excel()
