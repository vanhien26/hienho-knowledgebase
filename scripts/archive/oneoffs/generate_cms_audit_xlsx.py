import csv
import os
from collections import defaultdict
import xlsxwriter

def build_cms_audit_excel():
    csv_path = '/Users/hienhv/Downloads/Project - Trang tính1.csv'
    out_dir = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/07_REPORTS/sheets'
    os.makedirs(out_dir, exist_ok=True)
    out_xlsx = os.path.join(out_dir, 'cms_projects_audit_and_restructuring_report.xlsx')

    projects = list(csv.DictReader(open(csv_path, encoding='utf-8')))
    print(f"Loaded {len(projects)} projects.")

    # Build hierarchy & depth map
    name_map = defaultdict(list)
    for r in projects:
        name_map[r['Project']].append(r)

    def get_depth(item, visited=None):
        if visited is None:
            visited = set()
        p = item['Project Cha'].strip()
        if not p or p in visited:
            return 1
        visited.add(item['Project'])
        p_items = name_map.get(p, [])
        if not p_items:
            return 1
        return 1 + get_depth(p_items[0], visited)

    # Classify each project
    legacy_campaign_ids = {
        '90', '134', '152', '258', '19', '301', '344', '340', '376', '414',
        '576', '415', '462', '60', '530', '202', '225', '311', '324', '328',
        '337', '342', '350', '361', '371', '387', '399', '406', '533', '648',
        '681'
    }

    enriched_projects = []
    for r in projects:
        p_id = r['Id']
        p_name = r['Project']
        p_parent = r['Project Cha'].strip()
        p_link = r['Link']
        depth = get_depth(r)

        # Audit status & action logic
        audit_status = 'Hợp Lệ'
        issue_detail = 'Cấu trúc bình thường, hoạt động ổn định.'
        target_zone = 'Productivity & Self-serve'
        proposed_hub = 'Utilities & Billpay'
        action_req = 'Duy trì và tối ưu luồng chuyển đổi W2A.'

        # Determine Hub & Zone
        if p_name in ['Cinema'] or p_parent in ['Cinema', 'Phim chiếu', 'Blog Phim', 'Quốc gia', 'Rạp chiếu', 'Diễn viên', 'Phim hay', 'Netflix']:
            target_zone = 'Performance Zone'
            proposed_hub = '1. Cinema Hub'
            if p_parent == 'Phim chiếu':
                audit_status = 'Phân Loại Động Cần Tinh Gọn'
                issue_detail = 'Thể loại phim chi tiết làm phình to bảng dự án CMS; nên quản trị bằng Dynamic Tagging/Facet.'
                action_req = 'Chuyển sang Dynamic Facet / Tagging thuộc Cinema Hub.'
        elif p_name in ['OTA'] or p_parent in ['OTA', 'Vé máy bay', 'Vé xe khách', 'OTA Game', 'Điểm đến']:
            target_zone = 'Performance Zone'
            proposed_hub = '4. Travel & OTA Hub'
            if p_parent == 'Điểm đến':
                audit_status = 'Phân Loại Động Cần Tinh Gọn'
                issue_detail = 'Điểm đến tỉnh thành làm phình to bảng dự án CMS; nên quản lý qua bảng Destination Entity kết nối API.'
                action_req = 'Chuyển sang Destination Entity Database thuộc Travel Hub.'
        elif p_name in ['Tài chính - Bảo hiểm', 'Tài chính', 'Bảo hiểm', 'Bảo hiểm xe máy', 'Bảo hiểm xe máy Landing Page', 'Vay Nhanh Landing Page'] or p_parent in ['Tài chính - Bảo hiểm', 'Tài chính', 'Sàn Đầu Tư', 'Ví Trả Sau', 'Vay Nhanh Landing Page', 'Bảo hiểm', 'Bảo hiểm ô tô']:
            target_zone = 'Transformation Zone'
            proposed_hub = '2. Financial Hub'
            if p_id in ['216', '736']:
                audit_status = 'Phân Mảnh / Trùng Lặp'
                issue_detail = 'Tách riêng thành gốc độc lập, không nằm trong cây Bảo hiểm chung.'
                action_req = 'Hợp nhất về Trung tâm Bảo hiểm (Financial Hub).'
            elif p_id in ['735', '452', '128', '359']:
                if p_id == '128':
                    audit_status = 'Sai Quy Chuẩn / Typo'
                    issue_detail = 'Lỗi chính tả "Simular" thay vì "Simulator"; tách gốc độc lập.'
                    action_req = 'Sửa lỗi chính tả Simulator & Hợp nhất về Vay tiêu dùng (Financial Hub).'
                else:
                    audit_status = 'Phân Mảnh / Trùng Lặp'
                    issue_detail = 'Dự án Vay Nhanh tách riêng thành gốc độc lập thay vì gom về Financial Hub.'
                    action_req = 'Hợp nhất về Vay tiêu dùng (Financial Hub).'
            elif p_id == '734':
                audit_status = 'Phân Mảnh / Trùng Lặp'
                issue_detail = 'Trùng lặp với dự án Ví Trả Sau (ID 16).'
                action_req = 'Gộp vào chuyên mục Ví Trả Sau thuộc Financial Hub.'
            elif p_parent in ['Bảo hiểm', 'Bảo hiểm ô tô']:
                audit_status = 'Phân Mảnh / Trùng Lặp'
                issue_detail = 'Cụm Bảo hiểm đang nằm ở gốc độc lập (ID 13) thay vì tích hợp trong Financial Hub.'
                action_req = 'Di chuyển toàn bộ cây Bảo hiểm vào Financial Hub.'
        elif p_name in ['Tiện ích giao thông'] or p_parent in ['Tiện ích giao thông']:
            target_zone = 'Transformation Zone'
            proposed_hub = '3. Vehicle Hub'
            action_req = 'Đồng bộ dữ liệu qua Apify & Tối ưu phễu W2A Phạt nguội/Bảo hiểm.'
        elif p_name in ['Student Pass'] or 'Student' in p_name:
            target_zone = 'Incubator Zone'
            proposed_hub = '5. Student Hub'
            audit_status = 'Phân Mảnh / Trùng Lặp'
            issue_detail = 'Chỉ có 1 node đơn lẻ Student Pass, chưa có cấu trúc 3 trang con (Sinh viên, Trường học, BXH).'
            action_req = 'Nâng cấp và mở rộng cấu trúc Student Hub theo PRD chiến lược.'
        elif p_name in ['Vé số'] or p_parent in ['Vé số']:
            target_zone = 'Incubator Zone'
            proposed_hub = '6. Utilities & Billpay'
            action_req = 'Tích hợp module Tra cứu kết quả xổ số & Mua vé Vietlott qua Native QR.'
        elif p_name in ['Growth User'] or p_parent in ['Growth User']:
            target_zone = 'Incubator Zone'
            proposed_hub = '10. Brand, Life & Trust'
            action_req = 'Tối ưu Personalization Welcome Flow cho New User.'
        elif p_name in ['Billpay'] or p_parent in ['Billpay', 'Học phí', 'Dịch vụ công']:
            target_zone = 'Productivity & Self-serve'
            proposed_hub = '6. Utilities & Billpay'
            if p_name == 'Giáo dục' and p_id == '323':
                audit_status = 'Phân Mảnh / Trùng Lặp'
                issue_detail = 'Trùng tên với dự án Giáo dục (ID 287) thuộc Ví Nhân Ái.'
                action_req = 'Đổi tên thành "Học phí & Giáo dục Billpay" để tránh trùng lặp.'
        elif p_name in ['Chuyển Nhận Tiền', 'Offline Payment', 'Source of Fund'] or p_parent in ['Chuyển Nhận Tiền', 'Offline Payment', 'SME Offline', 'Source of Fund', 'Bank', 'Agent Network']:
            target_zone = 'Productivity & Self-serve'
            proposed_hub = '7. Payment & Core Services'
        elif p_name in ['Donation'] or p_parent in ['Donation', 'Heo đất MoMo - Quyên góp', 'Ví Nhân Ái - Blog', 'Donation Campaign']:
            target_zone = 'Productivity & Self-serve'
            proposed_hub = '8. Ví Nhân Ái / Donation'
            if p_name == 'Giáo dục' and p_id == '287':
                audit_status = 'Phân Mảnh / Trùng Lặp'
                issue_detail = 'Trùng tên với dự án Giáo dục (ID 323) thuộc Billpay.'
                action_req = 'Đổi tên thành "Thiện nguyện Giáo dục" để tránh trùng lặp.'
        elif p_name in ['Caishen', 'SME Merchant', 'Dịch vụ liên kết', 'Ads Payment', 'Soundbox', 'Marketing Solution', 'Business Page'] or p_parent in ['Caishen', 'SME Merchant', 'Dịch vụ liên kết', 'Application Store', 'Apple', 'Tiktok', 'Online Payment', 'Delivery', 'Logistics', 'OTT', 'Ads Payment']:
            target_zone = 'Productivity & Self-serve'
            proposed_hub = '9. Merchant & Partner Hub'
        elif p_name in ['Telco', 'Sim chính chủ', 'eSim du lịch', 'Nạp thẻ Game'] or p_parent in ['Telco', 'Airtime', 'eSim du lịch', 'Nạp thẻ Game']:
            target_zone = 'Productivity & Self-serve'
            proposed_hub = '6. Utilities & Billpay'
            if p_id in ['413', '402', '724']:
                audit_status = 'Phân Mảnh / Trùng Lặp'
                issue_detail = 'SIM chính chủ và eSIM du lịch bị tách thành các gốc riêng ngoài cụm Telco.'
                action_req = 'Hợp nhất về cụm Telco & Viễn thông thuộc Utilities Hub.'
        elif p_name in ['Campaign MoMo', 'Lắc xì 2026'] or p_parent in ['Campaign MoMo', 'Tài chính cá nhân']:
            target_zone = 'Productivity & Self-serve'
            proposed_hub = '10. Brand, Life & Trust'
            if p_id in legacy_campaign_ids:
                audit_status = 'Chiến Dịch Cũ Cần Archive'
                issue_detail = 'Chiến dịch từ 2021-2025 đã kết thúc, tích lũy crawl waste.'
                action_req = 'Chuyển sang trạng thái Archive & Thiết lập 301 Redirect.'
            elif p_id == '688':
                audit_status = 'Phân Mảnh / Trùng Lặp'
                issue_detail = 'Lắc xì 2026 bị tạo thành gốc Cấp 1 thay vì nằm dưới Campaign MoMo.'
                action_req = 'Gán danh mục cha về Campaign MoMo (ID 89).'
        elif p_name in ['An toàn bảo mật (TRUST)', 'Life At MoMo', 'Web Platform', 'MOMO', 'Popup Ads', 'Promotion', 'MoMo XU', 'Mini App'] or p_parent in ['An toàn bảo mật (TRUST)', 'Life At MoMo', 'Web Platform', 'MOMO', 'Popup Ads', 'Promotion']:
            target_zone = 'Productivity & Self-serve'
            proposed_hub = '10. Brand, Life & Trust'
            if p_id in ['540', '541']:
                audit_status = 'Dữ Liệu Thử Nghiệm'
                issue_detail = 'Dự án Test tạo trực tiếp trên production CMS.'
                action_req = 'Xóa khỏi CMS production.'

        # Check for Orphaned nodes (Parent = Deal)
        if p_parent == 'Deal':
            audit_status = 'Lỗi Mồ Côi'
            issue_detail = 'Tham chiếu cha "Deal" không tồn tại trong CMS, làm gãy breadcrumbs và sitemap.'
            target_zone = 'Productivity & Self-serve'
            proposed_hub = '9. Merchant & Partner Hub'
            action_req = 'Sửa danh mục cha trỏ về Promotion (ID 295) & Xóa tiền tố [PROMOTION].'

        enriched_projects.append({
            'Id': p_id,
            'Project': p_name,
            'Project Cha': p_parent,
            'Link': p_link,
            'Depth': f"Level {depth}",
            'Audit Status': audit_status,
            'Issue Detail': issue_detail,
            'Target Zone': target_zone,
            'Proposed Hub': proposed_hub,
            'Action Req': action_req
        })

    # Create Workbook
    wb = xlsxwriter.Workbook(out_xlsx)

    # Styles
    f_title = wb.add_format({'bold': True, 'font_size': 15, 'font_color': '#FFFFFF', 'bg_color': '#A50064', 'align': 'left', 'valign': 'vcenter', 'font_name': 'Arial'})
    f_subtitle = wb.add_format({'italic': True, 'font_size': 10, 'font_color': '#475569', 'font_name': 'Arial'})
    f_sec_header = wb.add_format({'bold': True, 'font_size': 11, 'font_color': '#FFFFFF', 'bg_color': '#1E293B', 'align': 'left', 'valign': 'vcenter', 'font_name': 'Arial'})
    f_tbl_header = wb.add_format({'bold': True, 'font_size': 10, 'font_color': '#1E293B', 'bg_color': '#E2E8F0', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_left = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'left', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_center = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_cell_right = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'right', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial', 'num_format': '#,##0'})
    f_cell_pct = wb.add_format({'font_size': 9, 'font_color': '#0F172A', 'align': 'right', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial', 'num_format': '0.0%'})
    
    # Status styles
    f_status_err = wb.add_format({'font_size': 9, 'font_color': '#991B1B', 'bg_color': '#FEE2E2', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_status_warn = wb.add_format({'font_size': 9, 'font_color': '#92400E', 'bg_color': '#FEF3C7', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_status_ok = wb.add_format({'font_size': 9, 'font_color': '#166534', 'bg_color': '#DCFCE7', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})
    f_status_info = wb.add_format({'font_size': 9, 'font_color': '#1E40AF', 'bg_color': '#DBEAFE', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'font_name': 'Arial'})

    # ----------------------------------------------------
    # SHEET 1: Executive_Summary
    # ----------------------------------------------------
    ws1 = wb.add_worksheet('Executive_Summary')
    ws1.set_column('A:A', 6)
    ws1.set_column('B:B', 38)
    ws1.set_column('C:C', 18)
    ws1.set_column('D:D', 16)
    ws1.set_column('E:E', 45)

    ws1.merge_range('B2:E2', 'BÁO CÁO KIỂM TOÁN HIỆN TRẠNG 420 DỰ ÁN CMS VÀ ĐỀ XUẤT TÁI CẤU TRÚC WEB PLATFORM', f_title)
    ws1.write('B3', 'Đơn vị thực hiện: Web Platform Team (Growth Platform Division) | Thời gian: Tháng 08/2026', f_subtitle)
    ws1.write('B4', 'Phạm vi: Toàn bộ 420 dự án danh mục CMS momo.vn | Mục tiêu: Chuẩn hóa 4 Zone & 10 Master Hubs', f_subtitle)

    # Section 1: Structural Metrics
    ws1.merge_range('B6:E6', 'I. BẢNG CHỈ SỐ ĐỊNH LƯỢNG HỆ THỐNG CMS HIỆN TẠI', f_sec_header)
    headers_s1 = ['Chỉ Số Cấu Trúc (Structural Metrics)', 'Số Lượng', 'Tỷ Trọng (%)', 'Ghi Chú Kỹ Thuật']
    for col_idx, h in enumerate(headers_s1):
        ws1.write(6, 1 + col_idx, h, f_tbl_header)

    metrics_data = [
        ('Tổng số dự án ghi nhận (Total Projects)', 420, 1.0, 'Dải ID trải từ 1 đến 841'),
        ('Dự án Gốc Cấp 1 (Root Projects / Level 1)', 37, 37/420, 'Gồm cả 11 gốc cô lập không có dự án con'),
        ('Dự án Cấp 2 (Level 2 Sub-projects)', 185, 185/420, 'Nhóm danh mục phân nhánh trực tiếp từ Gốc'),
        ('Dự án Cấp 3 (Level 3 Sub-projects)', 179, 179/420, 'Nhóm thể loại phim, điểm đến, blog chuyên đề'),
        ('Dự án Cấp 4 (Level 4 Sub-projects)', 14, 14/420, 'Độ sâu tối đa của cây danh mục hiện tại'),
        ('Dự án mồ côi (Orphaned Projects)', 5, 5/420, 'Tham chiếu cha không tồn tại (Parent: "Deal")'),
        ('Dự án chiến dịch cũ cần lưu trữ (Archive Candidates)', 34, 34/420, 'Các chiến dịch Mega, Lắc xì, Game từ 2021 đến 2025'),
        ('Dự án phân loại động cần tinh gọn (Dynamic Facets)', 106, 106/420, '52 thể loại phim & 54 điểm đến du lịch')
    ]

    for row_idx, row in enumerate(metrics_data):
        r_num = 7 + row_idx
        ws1.write(r_num, 1, row[0], f_cell_left)
        ws1.write(r_num, 2, row[1], f_cell_right)
        ws1.write(r_num, 3, row[2], f_cell_pct)
        ws1.write(r_num, 4, row[3], f_cell_left)

    # Section 2: Top Clusters
    start_r = 17
    ws1.merge_range(f'B{start_r}:E{start_r}', 'II. MA TRẬN 15 CỤM DỰ ÁN LỚN NHẤT TRÊN CMS', f_sec_header)
    headers_c = ['Cụm Dự Án / Master Domain', 'ID Gốc', 'Tổng Số Nodes', 'Đánh Giá Trọng Số & Hiện Trạng']
    for col_idx, h in enumerate(headers_c):
        ws1.write(start_r, 1 + col_idx, h, f_tbl_header)

    clusters_data = [
        ('Cinema (Phim ảnh & Rạp chiếu)', '10', 83, 'Chứa 52 thể loại phim chiếu rạp, 9 cụm rạp, 8 quốc gia. Cần tinh gọn facet.'),
        ('OTA (Du lịch & Đi lại)', '12', 72, 'Chứa 54 điểm đến tỉnh thành/quốc gia. Cần chuyển sang Destination Database.'),
        ('Donation (Ví Nhân Ái & Quyên góp)', '63', 43, '28 tổ chức thiện nguyện, 8 chuyên mục blog, 4 chiến dịch quyên góp.'),
        ('Campaign MoMo (Chiến dịch Tổng)', '89', 36, 'Hơn 30 chiến dịch cũ từ 2021-2025; Lắc xì 2026 bị tách thành gốc riêng.'),
        ('Tài chính - Bảo hiểm (Financial Hub)', '57', 27, 'Bị phân mảnh với các gốc Bảo hiểm (13, 216, 736) và Vay Nhanh (735).'),
        ('Dịch vụ liên kết (Affiliates & Partners)', '280', 27, 'Bao gồm App Store, Online Payment (Delivery/Logistics) và OTT.'),
        ('Billpay (Hóa đơn & Tiện ích công)', '68', 22, '19 nhóm dịch vụ thanh toán hóa đơn thiết yếu (Điện, Nước, Internet...).'),
        ('Nạp thẻ Game', '18', 11, 'Nhóm tiện ích thẻ nạp, cổng nạp nhà phát hành (VNG, VGP, Napthengay).'),
        ('Chuyển Nhận Tiền (Payment Core)', '191', 9, 'Cốt lõi thanh toán: P2P, W2B, W2W, W2C, VietQR, Quỹ nhóm.'),
        ('Tiện ích giao thông (Vehicle Hub)', '389', 8, 'Phạt nguội, Vận tải, Cứu hộ, Đăng kiểm, Phí ETC/VETC. Đang mở rộng.'),
        ('Offline Payment & SME', '66', 7, 'Retails, Thổ Địa, FnB, SME Offline, Spa, Quản lý chi tiêu.'),
        ('An toàn bảo mật (TRUST)', '326', 7, 'Thủ đoạn lừa đảo, Bảo mật giao dịch, NFC, KYC, Risk.'),
        ('Telco (Viễn thông)', '403', 7, 'Viettel, Mobifone, Vinaphone, Data 4G/5G, Airtime (Topup).'),
        ('Bảo hiểm (InsurTech Cluster)', '13', 6, 'Bảo hiểm sức khỏe, Bảo hiểm ô tô (Vật chất, TNDS), Bảo hiểm Y tế.'),
        ('Growth User (Tăng trưởng & Onboarding)', '686', 6, 'Retention, Giới thiệu MoMo, Family Hub, New User, Cross-Sell.')
    ]

    for row_idx, row in enumerate(clusters_data):
        r_num = start_r + 1 + row_idx
        ws1.write(r_num, 1, row[0], f_cell_left)
        ws1.write(r_num, 2, row[1], f_cell_center)
        ws1.write(r_num, 3, row[2], f_cell_right)
        ws1.write(r_num, 4, row[3], f_cell_left)

    # Section 3: 4-Zone Framework
    start_z = start_r + len(clusters_data) + 3
    ws1.merge_range(f'B{start_z}:E{start_z}', 'III. QUY HOẠCH TÁI CẤU TRÚC THEO KHUNG 4 ZONE (4-ZONE PORTFOLIO)', f_sec_header)
    headers_z = ['Phân Vùng (Zone)', 'Tiêu Chí & Mục Tiêu Tăng Trưởng', 'Master Hubs & Danh Mục Ánh Xạ', 'Hành Động Chuẩn Hóa CMS']
    for col_idx, h in enumerate(headers_z):
        ws1.write(start_z, 1 + col_idx, h, f_tbl_header)

    zones_data = [
        ('Performance Zone', 'Traffic >= 1.000.000 PV/tháng.\nTăng trưởng: +20% đến +30%.', 'Cinema Hub, Travel & OTA Hub', 'Gộp 52 thể loại phim và 54 tỉnh thành thành Dynamic Facets. Chuẩn hóa trang cụm rạp đối tác.'),
        ('Transformation Zone', 'Traffic: 500k - 1.000.000 PV/tháng.\nMục tiêu bứt phá: x2 đến x5.', 'Financial Hub (CIC, Vay Nhanh, Vàng, Tiết kiệm, Bảo hiểm),\nVehicle Hub (Phạt nguội, Giá xăng, Cây xăng, Trạm sạc EV)', 'Hợp nhất toàn bộ gốc Bảo hiểm rời rạc (13, 216, 736) và Vay Nhanh (735) vào Financial Hub. Đồng bộ dữ liệu Vehicle qua Apify.'),
        ('Incubator Zone', 'Dự án mới / Đột phá.\nCam kết tối thiểu: 500.000 PV/tháng.', 'Student Hub, Cổng Tra cứu Xổ Số & Vietlott,\nNew User Personalization Flow', 'Quy hoạch cấu trúc Student Hub hoàn chỉnh; tích hợp module Xổ số Native QR; tối ưu Onboarding New User.'),
        ('Productivity Zone & Self-serve', 'Hạ tầng & Tiện ích nghiệp vụ BU.\nMục tiêu: Tự động hóa 100%, không tốn Dev.', 'Utilities & Billpay, Payment Core, Donation / Ví Nhân Ái,\nMerchant & Partner Hub, Brand/Life/Trust, In-App Webviews', 'Chuyển giao quyền tự xuất bản cho BU qua Admin Tool theo Template TLDR chuẩn hóa kèm Guardrails. Lưu trữ 34 campaign cũ.')
    ]

    for row_idx, row in enumerate(zones_data):
        r_num = start_z + 1 + row_idx
        ws1.write(r_num, 1, row[0], f_cell_left)
        ws1.write(r_num, 2, row[1], f_cell_left)
        ws1.write(r_num, 3, row[2], f_cell_left)
        ws1.write(r_num, 4, row[3], f_cell_left)

    # ----------------------------------------------------
    # SHEET 2: Current_420_Projects_Audit
    # ----------------------------------------------------
    ws2 = wb.add_worksheet('All_420_Projects_Audit')
    ws2.set_column('A:A', 8)
    ws2.set_column('B:B', 32)
    ws2.set_column('C:C', 24)
    ws2.set_column('D:D', 45)
    ws2.set_column('E:E', 12)
    ws2.set_column('F:F', 24)
    ws2.set_column('G:G', 45)
    ws2.set_column('H:H', 22)
    ws2.set_column('I:I', 24)
    ws2.set_column('J:J', 45)

    headers_p = [
        'ID Dự Án', 'Tên Dự Án CMS', 'Dự Án Cha Hiện Tại', 'Đường Dẫn CMS Admin',
        'Phân Cấp', 'Trạng Thái Kiểm Toán', 'Chi Tiết Vấn Đề / Rủi Ro',
        'Phân Vùng 4-Zone', 'Master Hub Đề Xuất', 'Hành Động Khắc Phục'
    ]

    for col_idx, h in enumerate(headers_p):
        ws2.write(0, col_idx, h, f_tbl_header)

    for row_idx, r in enumerate(enriched_projects):
        r_num = 1 + row_idx
        ws2.write(r_num, 0, int(r['Id']), f_cell_center)
        ws2.write(r_num, 1, r['Project'], f_cell_left)
        ws2.write(r_num, 2, r['Project Cha'], f_cell_left)
        ws2.write(r_num, 3, r['Link'], f_cell_left)
        ws2.write(r_num, 4, r['Depth'], f_cell_center)

        status_fmt = f_cell_center
        if r['Audit Status'] == 'Lỗi Mồ Côi':
            status_fmt = f_status_err
        elif r['Audit Status'] in ['Phân Mảnh / Trùng Lặp', 'Sai Quy Chuẩn / Typo']:
            status_fmt = f_status_warn
        elif r['Audit Status'] == 'Chiến Dịch Cũ Cần Archive':
            status_fmt = f_status_warn
        elif r['Audit Status'] == 'Dữ Liệu Thử Nghiệm':
            status_fmt = f_status_err
        elif r['Audit Status'] == 'Phân Loại Động Cần Tinh Gọn':
            status_fmt = f_status_info
        else:
            status_fmt = f_status_ok

        ws2.write(r_num, 5, r['Audit Status'], status_fmt)
        ws2.write(r_num, 6, r['Issue Detail'], f_cell_left)
        ws2.write(r_num, 7, r['Target Zone'], f_cell_left)
        ws2.write(r_num, 8, r['Proposed Hub'], f_cell_left)
        ws2.write(r_num, 9, r['Action Req'], f_cell_left)

    ws2.autofilter(0, 0, len(enriched_projects), len(headers_p) - 1)
    ws2.freeze_panes(1, 2)

    # ----------------------------------------------------
    # SHEET 3: Defects_Detail
    # ----------------------------------------------------
    ws3 = wb.add_worksheet('Defects_Detail')
    ws3.set_column('A:A', 6)
    ws3.set_column('B:B', 10)
    ws3.set_column('C:C', 32)
    ws3.set_column('D:D', 24)
    ws3.set_column('E:E', 45)
    ws3.set_column('F:F', 45)

    ws3.merge_range('B2:F2', 'DANH SÁCH CHI TIẾT DỰ ÁN LỖI, PHÂN MẢNH & RỦI RO QUẢN TRỊ', f_title)

    # Table 1: Orphaned
    curr_r = 4
    ws3.merge_range(f'B{curr_r}:F{curr_r}', '1. DANH SÁCH 5 DỰ ÁN MỒ CÔI (ORPHANED NODES TRỎ VÀO "DEAL")', f_sec_header)
    curr_r += 1
    for col_idx, h in enumerate(['ID', 'Tên Dự Án Lỗi', 'Project Cha Cấu Hình', 'Chi Tiết Lỗi & Rủi Ro', 'Hành Động Khắc Phục']):
        ws3.write(curr_r - 1, 1 + col_idx, h, f_tbl_header)

    orphans = [p for p in enriched_projects if p['Audit Status'] == 'Lỗi Mồ Côi']
    for p in orphans:
        ws3.write(curr_r, 1, int(p['Id']), f_cell_center)
        ws3.write(curr_r, 2, p['Project'], f_cell_left)
        ws3.write(curr_r, 3, p['Project Cha'], f_status_err)
        ws3.write(curr_r, 4, p['Issue Detail'], f_cell_left)
        ws3.write(curr_r, 5, p['Action Req'], f_cell_left)
        curr_r += 1

    # Table 2: Fragmented & Duplicates
    curr_r += 2
    ws3.merge_range(f'B{curr_r}:F{curr_r}', '2. DANH SÁCH DỰ ÁN PHÂN MẢNH, TRÙNG LẶP & CHỒNG CHÉO DANH MỤC', f_sec_header)
    curr_r += 1
    for col_idx, h in enumerate(['ID', 'Tên Dự Án', 'Project Cha Hiện Tại', 'Hiện Trạng Phân Mảnh', 'Hành Động Hợp Nhất']):
        ws3.write(curr_r - 1, 1 + col_idx, h, f_tbl_header)

    fragmented = [p for p in enriched_projects if p['Audit Status'] == 'Phân Mảnh / Trùng Lặp']
    for p in fragmented:
        ws3.write(curr_r, 1, int(p['Id']), f_cell_center)
        ws3.write(curr_r, 2, p['Project'], f_cell_left)
        ws3.write(curr_r, 3, p['Project Cha'], f_cell_left)
        ws3.write(curr_r, 4, p['Issue Detail'], f_cell_left)
        ws3.write(curr_r, 5, p['Action Req'], f_cell_left)
        curr_r += 1

    # Table 3: Legacy Campaigns
    curr_r += 2
    ws3.merge_range(f'B{curr_r}:F{curr_r}', '3. DANH SÁCH 34 DỰ ÁN CHIẾN DỊCH CŨ CẦN LƯU TRỮ (ARCHIVE & 301 REDIRECT)', f_sec_header)
    curr_r += 1
    for col_idx, h in enumerate(['ID', 'Tên Chiến Dịch Cũ', 'Project Cha', 'Giai Đoạn Sự Kiện', 'Hành Động Lưu Trữ']):
        ws3.write(curr_r - 1, 1 + col_idx, h, f_tbl_header)

    legacy_camps = [p for p in enriched_projects if p['Audit Status'] == 'Chiến Dịch Cũ Cần Archive']
    for p in legacy_camps:
        ws3.write(curr_r, 1, int(p['Id']), f_cell_center)
        ws3.write(curr_r, 2, p['Project'], f_cell_left)
        ws3.write(curr_r, 3, p['Project Cha'], f_cell_left)
        ws3.write(curr_r, 4, p['Issue Detail'], f_cell_left)
        ws3.write(curr_r, 5, p['Action Req'], f_cell_left)
        curr_r += 1

    # Table 4: Test & Typo
    curr_r += 2
    ws3.merge_range(f'B{curr_r}:F{curr_r}', '4. DANH SÁCH DỰ ÁN LỖI CHÍNH TẢ, TIỀN TỐ RÁC & DỮ LIỆU THỬ NGHIỆM', f_sec_header)
    curr_r += 1
    for col_idx, h in enumerate(['ID', 'Tên Dự Án Lỗi', 'Project Cha', 'Chi Tiết Lỗi', 'Hành Động Khắc Phục']):
        ws3.write(curr_r - 1, 1 + col_idx, h, f_tbl_header)

    test_typos = [p for p in enriched_projects if p['Audit Status'] in ['Dữ Liệu Thử Nghiệm', 'Sai Quy Chuẩn / Typo'] and p['Audit Status'] != 'Lỗi Mồ Côi']
    for p in test_typos:
        ws3.write(curr_r, 1, int(p['Id']), f_cell_center)
        ws3.write(curr_r, 2, p['Project'], f_cell_left)
        ws3.write(curr_r, 3, p['Project Cha'], f_cell_left)
        ws3.write(curr_r, 4, p['Issue Detail'], f_cell_left)
        ws3.write(curr_r, 5, p['Action Req'], f_cell_left)
        curr_r += 1

    # ----------------------------------------------------
    # SHEET 4: Proposed_10_Master_Hubs
    # ----------------------------------------------------
    ws4 = wb.add_worksheet('Proposed_10_Master_Hubs')
    ws4.set_column('A:A', 6)
    ws4.set_column('B:B', 24)
    ws4.set_column('C:C', 22)
    ws4.set_column('D:D', 32)
    ws4.set_column('E:E', 38)
    ws4.set_column('F:F', 30)
    ws4.set_column('G:G', 45)

    ws4.merge_range('B2:G2', 'KIẾN TRÚC DANH MỤC 10 MASTER HUBS CHUẨN HÓA CHO CMS MOMO.VN', f_title)

    headers_hub = [
        'Master Hub Cấp 1', 'Phân Vùng 4-Zone', 'Danh Mục Sub-Hub Cấp 2',
        'Tiện Ích & Content Types Cấp 3', 'Business KPIs & Targets', 'Cơ Chế Kỹ Thuật & Vận Hành'
    ]
    for col_idx, h in enumerate(headers_hub):
        ws4.write(3, 1 + col_idx, h, f_tbl_header)

    master_hubs_data = [
        ('1. Cinema Hub', 'Performance Zone', 'Cụm rạp đối tác (CGV, BHD, Lotte, Galaxy, Beta, Cinestar)', 'Trang chi tiết cụm rạp, khoảng cách màn hình, loại ghế, khuyến mãi rạp', 'Baseline 800k -> 1.3M-2.0M PV/tháng, CTR >= 4.5%', 'MoSpark Component, Gamification Missions, Dynamic Tagging 52 thể loại'),
        ('1. Cinema Hub', 'Performance Zone', 'Phim chiếu & Review', 'Review phim bom tấn, Top phim hay, Blog điện ảnh, Đánh giá diễn viên', 'Chiếm lĩnh 50% thị phần thông tin phim ảnh trên Web', 'GenAI Content Pipeline, Tiệm Sưu Tầm IP Merchandise (Rolex/Hermès Model)'),
        ('2. Financial Hub', 'Transformation Zone (Ưu tiên #1)', 'Điểm tín dụng & Kiểm tra CIC', 'Tool tra cứu nợ xấu CIC miễn phí, hướng dẫn xóa nợ xấu, cẩm nang tín dụng', '1.000.000 MPV, 500k MEU, CTR 50.00%', 'Interactive CIC Simulator Widget, E-E-A-T / YMYL Guardrails, Block Retro'),
        ('2. Financial Hub', 'Transformation Zone (Ưu tiên #1)', 'Vay Nhanh & Vay tiêu dùng', 'Vay nhanh cá nhân, Vay hộ kinh doanh, Bảng tính lãi vay tiêu dùng', 'Tăng x2 - x5 chuyển đổi mở khoản vay qua Web-to-App', 'Simulate Calculator Widget, Onelink Deep Link vào Mini App Vay'),
        ('2. Financial Hub', 'Transformation Zone (Ưu tiên #1)', 'Tiết kiệm, Đầu tư & Vàng Online', 'Bảng so sánh lãi suất ngân hàng, Giá vàng 24/7, Tỷ giá ngoại tệ, Chứng chỉ quỹ', 'Top 1-3 Google Search từ khóa Tra cứu tài chính', 'Real-time Financial Price Tracker API, Native QR Payment'),
        ('2. Financial Hub', 'Transformation Zone (Ưu tiên #1)', 'Trung tâm Bảo hiểm Toàn diện', 'Bảo hiểm ô tô (TNDS, Vật chất, Thủy kích), Bảo hiểm xe máy, Bảo hiểm sức khỏe/Y tế', 'Tăng tỷ lệ Cross-sell Bảo hiểm từ các cổng tiện ích', 'Hợp nhất toàn bộ gốc Bảo hiểm rời rạc (13, 216, 736); Captcha Module'),
        ('3. Vehicle Hub', 'Transformation Zone', 'Tra cứu Phạt nguội & Nộp phạt', 'Màn hình kết quả Inline, Cross-sell Bảo hiểm & Gói thông báo tự động', 'Tăng trưởng Login App, Nộp phạt In-App & Đăng ký gói', 'Mapping tự động mã lỗi CSGT với bài viết hướng dẫn luật GenAI'),
        ('3. Vehicle Hub', 'Transformation Zone', 'Cổng Tiện ích Giao thông', 'Bản đồ Cây xăng (PVOil, Comeco), Bản đồ Trạm sạc EV, Garage sửa xe, Thu phí ePass/VETC', 'Top 1 thị trường tiện ích giao thông số', '3 Google Sheets chuẩn hóa qua Apify, Dynamic Filtering theo hãng xe'),
        ('4. Travel & OTA Hub', 'Performance Zone', 'Vé máy bay, Tàu hỏa, Xe khách', 'Đặt vé máy bay nội địa/quốc tế, Vé xe Tết Phương Trang, Vé tàu hỏa', 'Giữ vững vị thế Top OTA Payment Hub', 'OTA Booking Widget, Dynamic Destination Entity Database'),
        ('4. Travel & OTA Hub', 'Performance Zone', 'Khách sạn & Trải nghiệm', 'Đặt phòng khách sạn theo giờ, Vé khu vui chơi, Cẩm nang du lịch 54 tỉnh thành', 'Tăng trưởng giao dịch OTA In-App', 'Database Destination Engine, Quick Wins Landing Pages'),
        ('5. Student Hub', 'Incubator Zone', 'Cổng Thông Tin Sinh Viên', 'Trang tổng quan Sinh viên, Trường học (50+ Đại học), Bảng xếp hạng trường', 'Đạt mốc 500.000 PV/tháng để giữ trạng thái Chiến lược', 'Mini-web cho từng trường đại học, Student Pass Gamification'),
        ('6. Utilities & Billpay', 'Productivity Zone & Self-serve', 'Thanh toán Hóa đơn Thiết yếu', 'Điện, Nước, Internet, Chung cư, Học phí, Dịch vụ công, Metro, Viễn thông Topup 4G/5G', 'Bảo vệ phễu Web-to-App cho dịch vụ cốt lõi', 'Mô hình Self-service cho BU, Template TLDR chuẩn hóa, Chặn URL rác'),
        ('6. Utilities & Billpay', 'Productivity Zone & Self-serve', 'Cổng Tra cứu Xổ Số & Vietlott', 'Tra cứu KQXS 3 miền, Mua vé Vietlott SMS online', 'Chiếm lĩnh volume tìm kiếm xổ số khổng lồ', 'Native Web QR Payment, Onelink sync vé số vào App MoMo'),
        ('7. Payment & Core Services', 'Productivity Zone & Self-serve', 'Chuyển Nhận Tiền & Thanh Toán', 'Chuyển tiền P2P, W2B, W2W, W2C điểm nạp rút, VietQR, Quỹ nhóm, Thổ Địa MoMo', 'Hỗ trợ nhận diện thương hiệu thanh toán số', 'Đơn giản hóa giao diện hướng dẫn thanh toán'),
        ('8. Ví Nhân Ái / Donation', 'Productivity Zone & Self-serve', 'Cổng Thiện Nguyện Cộng Đồng', 'Trái tim MoMo, Heo đất MoMo, Danh bạ 28 tổ chức thiện nguyện, Blog Ví Nhân Ái', 'Lan tỏa giá trị thương hiệu và trách nhiệm xã hội', 'Directory Listing tự động cho các tổ chức đối tác NGO'),
        ('9. Merchant & Partner Hub', 'Productivity Zone & Self-serve', 'Giải pháp Bán hàng & Đối tác', 'Soundbox, IPOS, CTV MoMo, SME Merchant, Dịch vụ liên kết (App Store, Delivery, OTT)', 'Hỗ trợ B2B Merchant & Affiliate Partners', 'Template trang đối tác chuẩn hóa, Phân quyền quản trị Cell Team'),
        ('10. Brand, Life & Trust', 'Productivity Zone & Self-serve', 'Thương Hiệu, Tuyển Dụng & An Toàn', 'Cảnh báo lừa đảo, Bảo mật MoMo, KYC, Life At MoMo, Onboarding New User', 'Bảo vệ uy tín thương hiệu & Tăng trưởng New Installs', 'Personalization Survey Engine, Welcome Voucher Funnel')
    ]

    for row_idx, row in enumerate(master_hubs_data):
        r_num = 4 + row_idx
        ws4.write(r_num, 1, row[0], f_cell_left)
        ws4.write(r_num, 2, row[1], f_cell_left)
        ws4.write(r_num, 3, row[2], f_cell_left)
        ws4.write(r_num, 4, row[3], f_cell_left)
        ws4.write(r_num, 5, row[4], f_cell_left)
        ws4.write(r_num, 6, row[5], f_cell_left)

    ws4.autofilter(3, 1, 3 + len(master_hubs_data), 6)

    # ----------------------------------------------------
    # SHEET 5: Action_Plan_Roadmap
    # ----------------------------------------------------
    ws5 = wb.add_worksheet('Action_Plan_Roadmap')
    ws5.set_column('A:A', 6)
    ws5.set_column('B:B', 14)
    ws5.set_column('C:C', 18)
    ws5.set_column('D:D', 32)
    ws5.set_column('E:E', 45)
    ws5.set_column('F:F', 24)

    ws5.merge_range('B2:F2', 'LỘ TRÌNH THỰC THI TÁI CẤU TRÚC CMS & MA TRẬN TRÁCH NHIỆM RACI', f_title)

    # Roadmap
    ws5.merge_range('B4:F4', 'I. KẾ HOẠCH HÀNH ĐỘNG 4 GIAI ĐOẠN (IMPLEMENTATION ROADMAP)', f_sec_header)
    for col_idx, h in enumerate(['Giai Đoạn', 'Thời Gian', 'Tên Giai Đoạn', 'Chi Tiết Triển Khai & Mục Tiêu', 'Đội Ngũ Phụ Trách']):
        ws5.write(4, 1 + col_idx, h, f_tbl_header)

    roadmap_data = [
        ('Giai đoạn 1', '01/09 - 07/09/2026', 'Dọn Dẹp Dữ Liệu Rác & Sửa Lỗi Cấp Bách', 'Sửa 5 dự án mồ côi về gốc Promotion (295); xóa 2 dự án Test (540, 541); sửa lỗi chính tả Simulator (128); gán Lắc xì 2026 (688) về đúng mục Campaign.', 'Web Dev Team (R/A),\nInbound Team (C)'),
        ('Giai đoạn 2', '08/09 - 15/09/2026', 'Hợp Nhất Danh Mục Phân Mảnh', 'Hợp nhất toàn bộ các gốc Bảo hiểm rời rạc (13, 216, 736) và Vay Nhanh (735) về cấu trúc chuẩn của Financial Hub; gộp landing pages trùng lặp.', 'Inbound Team (A),\nWeb Dev Team (R)'),
        ('Giai đoạn 3', '16/09 - 25/09/2026', 'Lưu Trữ Chiến Dịch Cũ & Tinh Gọn Facet', 'Đưa 34 dự án chiến dịch cũ (2021-2025) vào Archive đính kèm 301 Redirect; chuyển 52 thể loại phim và 54 điểm đến du lịch sang Dynamic Facets / Database Table.', 'SEO Vendor (R/A),\nWeb Dev Team (R)'),
        ('Giai đoạn 4', '26/09 - 30/09/2026', 'Đóng Gói Guardrails & Vận Hành Tự Phục Vụ', 'Kích hoạt bộ lọc Guardrails tự động kiểm duyệt URL/YMYL; phân quyền biên tập cho BU với đầu mối phê duyệt tập trung từ Inbound Team (BMC).', 'Web Dev Team (R/A),\nInbound Team (A)')
    ]

    for row_idx, row in enumerate(roadmap_data):
        r_num = 5 + row_idx
        ws5.write(r_num, 1, row[0], f_cell_left)
        ws5.write(r_num, 2, row[1], f_cell_center)
        ws5.write(r_num, 3, row[2], f_cell_left)
        ws5.write(r_num, 4, row[3], f_cell_left)
        ws5.write(r_num, 5, row[4], f_cell_left)

    # RACI Matrix
    start_raci = 11
    ws5.merge_range(f'B{start_raci}:F{start_raci}', 'II. MA TRẬN TRÁCH NHIỆM THỰC THI LIÊN ĐỘI NGŨ (RACI MATRIX)', f_sec_header)
    
    ws5.set_column('G:G', 22)
    ws5.set_column('H:H', 22)
    headers_raci = ['Hạng Mục Công Việc', 'Web Dev Team', 'Inbound Team (BMC)', 'SEO Vendor', 'Business Units (BUs)', 'Executive Leadership']
    for col_idx, h in enumerate(headers_raci):
        ws5.write(start_raci, 1 + col_idx, h, f_tbl_header)

    raci_data = [
        ('Sửa lỗi kỹ thuật CMS, dự án mồ côi & test nodes', 'R / A', 'C', 'I', 'I', 'I'),
        ('Hợp nhất cây danh mục Bảo hiểm, Vay Nhanh, FinHub', 'R', 'A', 'C', 'C', 'I'),
        ('Rà soát 301 Redirect & Lưu trữ Campaign cũ', 'R', 'C', 'R / A', 'I', 'I'),
        ('Thiết lập Bộ lọc Guardrails & Chặn xuất bản URL lỗi', 'R / A', 'C', 'C', 'I', 'I'),
        ('Vận hành Tự phục vụ & Phê duyệt nội dung hàng ngày', 'I', 'A', 'I', 'R', 'I'),
        ('Phê duyệt Chính sách & Giám sát Chiến lược', 'I', 'I', 'I', 'I', 'A / Approver')
    ]

    for row_idx, row in enumerate(raci_data):
        r_num = start_raci + 1 + row_idx
        ws5.write(r_num, 1, row[0], f_cell_left)
        for c_idx in range(5):
            val = row[1 + c_idx]
            fmt = f_cell_center
            if 'A' in val:
                fmt = f_status_err
            elif 'R' in val:
                fmt = f_status_ok
            ws5.write(r_num, 2 + c_idx, val, fmt)

    ws5.write(start_raci + len(raci_data) + 2, 1, 'Ghi chú: R (Responsible - Thực thi), A (Accountable - Chịu trách nhiệm chính), C (Consulted - Tham vấn), I (Informed - Nhận thông tin).', f_subtitle)

    wb.close()
    print(f"Successfully generated Excel workbook at: {out_xlsx}")

if __name__ == '__main__':
    build_cms_audit_excel()
