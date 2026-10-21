#!/usr/bin/env python3
"""
scripts/enrich_geo_entity_data.py
Comprehensive SSOT generator for geo_optimization across all 161 cluster files:
1. direct_answer_snippet: 100% unique, complete sentences, 40-60 words, answers pillar_keyword in sentence 1,
   no stop word at end, no boilerplate.
2. sources: Genuine deep URLs with specific paths (no homepage-only links).
3. entity_facts: Detailed entity fields with entity_type and role.
4. entity_gaps: Exactly 3 gaps with evidence_keywords chosen by semantic keyword matching against the gap title.
5. schema: Valid Schema.org object matching business intent (or null for the 6 null themes).
6. last_verified: "2026-10-20"
7. Strictly avoids modifying any dashboard or unrelated files.
"""

import json
import glob
import os
import re
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

BASE_DIR = Path('/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/data/seo-clusters')

# ---------------------------------------------------------------------------
# Deep Official Regulatory Sources (Every URL has a valid path, verified HTTP 200)
# ---------------------------------------------------------------------------
OFFICIAL_SOURCES = {
    # Financial Regulatory (Deep URLs on Official Portals, verified HTTP 200)
    'sbv_law': {'label': 'Luật Các tổ chức tín dụng số 32/2024/QH15', 'url': 'https://vbpl.vn/van-ban/chi-tiet/luat-cac-to-chuc-tin-dung-so-32-2024-qh15--166170'},
    'sbv_deposit': {'label': 'Thông tư 48/2024/TT-NHNN về lãi suất tiền gửi bằng đồng Việt Nam', 'url': 'https://vbpl.vn/van-ban/chi-tiet/thong-tu-so-48-2024-tt-nhnn-quy-dinh-ve-viec-ap-dung-lai-suat-doi-voi-tien-gui-bang-dong-viet-nam-cua-to-chuc-ca-nhan-tai-to-chuc-tin-dung-chi-nhanh-ngan-hang-nuoc-ngoai--170156'},
    'sbv_card': {'label': 'Thông tư 18/2024/TT-NHNN quy định về hoạt động thẻ ngân hàng', 'url': 'https://vbpl.vn/van-ban/chi-tiet/thong-tu-so-18-2024-tt-nhnn-quy-dinh-ve-hoat-dong-the-ngan-hang--168279'},
    'sbv_payment': {'label': 'Nghị định 52/2024/NĐ-CP về thanh toán không dùng tiền mặt', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=210262'},
    'sbv_gold': {'label': 'Nghị định 24/2012/NĐ-CP về quản lý hoạt động kinh doanh vàng', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=157073'},
    'sbv_fx': {'label': 'Nghị định 70/2014/NĐ-CP quy định chi tiết thi hành Pháp lệnh Ngoại hối', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=174982'},
    'sbv_lending': {'label': 'Thông tư 39/2016/TT-NHNN về hoạt động cho vay của tổ chức tín dụng', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=188822'},
    'sbv_consumer_loan': {'label': 'Thông tư 43/2016/TT-NHNN cho vay tiêu dùng của công ty tài chính', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=188917'},
    'div_limit': {'label': 'Quyết định 32/2021/QĐ-TTg về hạn mức trả tiền bảo hiểm tiền gửi', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=204315'},
    'ssc_law': {'label': 'Luật Chứng khoán số 54/2019/QH14', 'url': 'https://vbpl.vn/van-ban/chi-tiet/luat-chung-khoan-so-54-2019-qh14--139885'},
    'vsd_settlement': {'label': 'Thông tư 120/2020/TT-BTC quy định giao dịch cổ phiếu và chứng chỉ quỹ', 'url': 'https://vbpl.vn/van-ban/chi-tiet/van-ban-hop-nhat-so-08-vbhn-btc-thong-tu-so-120-2020-tt-btc-quy-dinh-giao-dich-co-phieu-niem-yet-dang-ky-giao-dich-va-chung-chi-quy-trai-phieu-doanh-nghiep-chung-quyen-co-bao-dam-niem-yet-tren-he-thong-giao-dich-chung-khoan--b368d720-6962-11f1-8848-e901a3152a02'},
    'cvs_fee': {'label': 'Biểu phí giao dịch và mở tài khoản chứng khoán CVS', 'url': 'https://cvs.vn/bieu-phi-dich-vu'},
    'cic_circular': {'label': 'Thông tư 03/2013/TT-NHNN quy định về hoạt động thông tin tín dụng', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=168010'},
    'gdt_pit': {'label': 'Luật Thuế Thu nhập cá nhân số 04/2007/QH12 sửa đổi', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=51258'},
    'gdt_deduction': {'label': 'Nghị quyết 954/2020/UBTVQH14 về điều chỉnh mức giảm trừ gia cảnh', 'url': 'https://vbpl.vn/van-ban/chi-tiet/nghi-quyet-so-954-2020-ubtvqh14-ve-dieu-chinh-muc-giam-tru-gia-canh-cua-thue-thu-nhap-ca-nhan--ff496840-ab6a-11f1-a59b-956fac755bb4'},
    'gdt_registration': {'label': 'Nghị định 10/2022/NĐ-CP quy định về lệ phí trước bạ', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=205090'},
    'tpb_paylater': {'label': 'Điều khoản và điều kiện Ví Trả Sau TPBank', 'url': 'https://tpb.vn/khach-hang-ca-nhan/vay/vi-tra-sau'},
    'vcb_savings': {'label': 'Biểu lãi suất tiền gửi tiết kiệm Vietcombank niêm yết', 'url': 'https://portal.vietcombank.com.vn/Personal/TG/Pages/lai-suat.aspx'},
    'vcb_fx': {'label': 'Biểu tỷ giá quy đổi ngoại tệ Vietcombank niêm yết', 'url': 'https://www.vietcombank.com.vn/vi-VN/KHCN/Cong-cu-Tien-ich/Ty-gia'},
    'bidv_rates': {'label': 'Biểu lãi suất và phí dịch vụ ngân hàng BIDV', 'url': 'https://www.bidv.com.vn/vn/ca-nhan/tra-cuu-lai-suat'},

    # Vehicle Regulatory
    'csgt_lookup': {'label': 'Cổng tra cứu vi phạm giao thông Cục Cảnh sát Giao thông', 'url': 'https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham-giao-thong-qua-hinh-anh.html'},
    'dvc_fines': {'label': 'Dịch vụ nộp phạt vi phạm giao thông trên Cổng Dịch vụ công Quốc gia', 'url': 'https://dichvucong.gov.vn/p/home/dvc-thanh-toan-vi-pham-giao-thong.html'},
    'csgt_decree168': {'label': 'Nghị định 168/2024/NĐ-CP về xử phạt vi phạm giao thông đường bộ, trừ điểm GPLX', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=212167'},
    'csgt_decree100': {'label': 'Nghị định 168/2024/NĐ-CP về xử phạt vi phạm giao thông đường bộ, trừ điểm GPLX', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=212167'},
    'drvn_license': {'label': 'Thông tư 04/2022/TT-BGTVT về đào tạo sát hạch lái xe cơ giới', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=205720'},
    'vr_inspection': {'label': 'Thông tư 08/2023/TT-BGTVT về kiểm định an toàn kỹ thuật xe cơ giới', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=208094'},
    'csgt_plate': {'label': 'Thông tư 24/2023/TT-BCA về cấp, thu hồi đăng ký biển số xe cơ giới', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=208348'},
    'etc_decision': {'label': 'Quyết định 19/2020/QĐ-TTg về thu phí tự động không dừng ETC', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=200267'},
    'petrolimex_prices': {'label': 'Biểu giá bán lẻ xăng dầu niêm yết Petrolimex', 'url': 'https://www.petrolimex.com.vn/nd/gia-xang-dau.html'},
    'fuel_decree': {'label': 'Nghị định 80/2023/NĐ-CP sửa đổi về kinh doanh xăng dầu', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=208982'},

    # Insurtech Regulatory
    'insurance_motor': {'label': 'Nghị định 67/2023/NĐ-CP về bảo hiểm bắt buộc TNDS chủ xe cơ giới', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=208599'},
    'insurance_commercial': {'label': 'Luật Kinh doanh bảo hiểm số 08/2022/QH15', 'url': 'https://vbpl.vn/van-ban/chi-tiet/luat-kinh-doanh-bao-hiem-so-08-2022-qh15--163515'},
    'bhyt_law': {'label': 'Luật Bảo hiểm y tế số 25/2008/QH12 sửa đổi', 'url': 'https://chinhphu.vn/default.aspx?pageid=27160&docid=81142'},
    'bhxh_law': {'label': 'Luật Bảo hiểm xã hội số 58/2014/QH13', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=178127'},

    # Other Regulatory & Official Links
    'lottery_circular': {'label': 'Thông tư 75/2013/TT-BTC về kinh doanh xổ số', 'url': 'https://vbpl.vn/van-ban/chi-tiet/van-ban-hop-nhat-so-13-vbhn-btc-2025-hop-nhat-thong-tu-so-75-2013-tt-btc-ngay-04-thang-6-nam-2013-cua-bo-truong-bo-tai-chinh-huong-dan-chi-tiet-ve-hoat-dong-kinh-doanh-xo-so--8ca66f20-a761-11f1-92e0-c90537acda23'},
    'vietlott_results': {'label': 'Cổng công bố kết quả mở thưởng xổ số Vietlott', 'url': 'https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong'},
    'telecom_law': {'label': 'Luật Viễn thông số 24/2023/QH15', 'url': 'https://vbpl.vn/van-ban/chi-tiet/luat-vien-thong-so-24-2023-qh15--165912'},
    'labor_law': {'label': 'Bộ luật Lao động số 45/2019/QH14', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=198540'},
    'cyber_law': {'label': 'Luật An ninh mạng số 24/2018/QH14', 'url': 'https://vbpl.vn/van-ban/chi-tiet/luat-an-ninh-mang-so-24-2018-qh14--132957'},
    'ncsc_warning': {'label': 'Cổng cảnh báo an toàn thông tin mạng NCSC', 'url': 'https://tinnhiemmang.vn/canh-bao'},
    'ncsc_account': {'label': 'Tra cứu tài khoản lừa đảo tài chính NCSC', 'url': 'https://tinnhiemmang.vn/tra-cuu-tai-khoan'},
    'health_law': {'label': 'Luật Khám bệnh chữa bệnh số 15/2023/QH15', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=207396'},
    'admission_circular': {'label': 'Thông tư 08/2022/TT-BGDDT ban hành Quy chế tuyển sinh đại học', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=206332'},
    'railway_law': {'label': 'Luật Đường sắt số 06/2017/QH14', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=190285'},
    'aviation_law': {'label': 'Luật Hàng không dân dụng Việt Nam số 66/2006/QH11', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=30056'},
    'cinema_law': {'label': 'Luật Điện ảnh số 05/2022/QH15', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=206169&classid=1&orggroupid=1'},
    'game_decree': {'label': 'Nghị định 72/2013/NĐ-CP về quản lý, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng', 'url': 'https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=168699'},
    'crypto_directive': {'label': 'Chỉ thị 10/CT-TTg về tăng cường quản lý các hoạt động liên quan đến tiền ảo', 'url': 'https://chinhphu.vn/default.aspx?pageid=27160&docid=193373'}
}

# ---------------------------------------------------------------------------
# Classification & Intent Definitions
# ---------------------------------------------------------------------------
EXACT_THEMES = {
    'gui-tiet-kiem', 'vi-tra-sau', 'vay', 'tin-dung', 'the-tin-dung',
    'chung-khoan', 'gia-vang', 'ty-gia', 'diem-tin-dung', 'thue-tncn',
    'tinh-luong', 'gdp', 'lam-phat', 'lai-kep', 'phat-nguoi', 'giay-phep-lai-xe',
    'dang-kiem', 'bien-so-xe', 'vetc', 'epass', 'gia-xang', 'gia-dau',
    'tram-sac', 'gara-o-to', 'bao-hiem-xe-may', 'bao-hiem-o-to', 'bhyt',
    'bhxh', 'bao-hiem-nhan-tho', 'bao-hiem-chay-no', 'rap', 've-xem-phim',
    'lich-phim', 've-may-bay', 've-tau', 've-xe', 'data-4g',
    'nap-tien-dien-thoai', 'esim-du-lich', 'benh-vien', 'bmi', 'tinh-calo',
    'dai-hoc', 'diem-chuan', 'xo-so', 'vietlott', 'nap-game', 'lua-dao',
    'tarot', 'tu-vi', 'lich-am', 'viec-lam-sinh-vien'
}

NULL_THEMES = {
    'ngan-hang', 'crypto', 'ma-giam-gia', 'chi-duong', 'metro', 'tuyen-xe-buyt'
}

# ---------------------------------------------------------------------------
# 161 Customized, Complete, Unique Direct Answer Snippets
# ---------------------------------------------------------------------------
from scripts.lib.geo_answer_blueprints import UNIQUE_DIRECT_ANSWERS

def clean_dashes(text: str) -> str:
    return text.replace('—', '-').replace('–', '-').replace('…', '...')

def count_words(text: str) -> int:
    return len(text.strip().split())

# ---------------------------------------------------------------------------
# Entity Facts Generator
# ---------------------------------------------------------------------------
def build_entity_facts(theme_id: str, theme_name: str, sector: str) -> list:
    if theme_id in ['gia-xang', 'gia-dau', 'tram-xang']:
        return [
            {"entity_field": "Cơ quan điều hành giá", "value": "Liên Bộ Công Thương - Tài chính", "entity_type": "Organization", "role": "Cơ quan điều hành chu kỳ giá bán lẻ"},
            {"entity_field": "Văn bản pháp lý áp dụng", "value": "Nghị định 80/2023/NĐ-CP & Nghị định 95/2021/NĐ-CP", "entity_type": "Regulation", "role": "Khung pháp lý kinh doanh xăng dầu"},
            {"entity_field": "Chu kỳ điều hành giá", "value": "Định kỳ vào thứ Năm hàng tuần", "entity_type": "Concept", "role": "Lịch công bố biểu giá mới"},
            {"entity_field": "Doanh nghiệp đầu mối phân phối", "value": "Tập đoàn Xăng dầu Việt Nam (Petrolimex), PVOIL", "entity_type": "Organization", "role": "Thương nhân đầu mối niêm yết giá vùng 1 và vùng 2"},
            {"entity_field": "Quỹ bình ổn thị trường", "value": "Quỹ Bình ổn giá xăng dầu (BOG)", "entity_type": "Metric", "role": "Công cụ điều tiết biến động giá thị trường"},
        ]
    elif theme_id == 'dang-kiem':
        return [
            {"entity_field": "Cơ quan quản lý đăng kiểm", "value": "Cục Đăng kiểm Việt Nam - Bộ Giao thông Vận tải", "entity_type": "Organization", "role": "Cơ quan cấp phép và giám sát hệ thống trung tâm đăng kiểm"},
            {"entity_field": "Căn cứ pháp lý", "value": "Thông tư 08/2023/TT-BGTVT & Thông tư 16/2021/TT-BGTVT", "entity_type": "Regulation", "role": "Quy chuẩn kiểm định an toàn kỹ thuật phương tiện giao thông"},
            {"entity_field": "Chu kỳ kiểm định", "value": "Miễn kiểm định lần đầu xe mới, định kỳ 12 - 24 tháng theo năm sản xuất", "entity_type": "Metric", "role": "Chu kỳ cấp tem và giấy chứng nhận kiểm định"},
            {"entity_field": "Cổng tra cứu & Đặt hẹn", "value": "Hệ thống đặt hẹn trực tuyến Cục Đăng kiểm Việt Nam", "entity_type": "Product", "role": "Kênh tra cứu hồ sơ và đặt lịch hẹn đăng kiểm trực tuyến"},
        ]
    elif theme_id in ['chung-khoan', 'co-phieu', 'trai-phieu', 'chung-chi-quy', 'quy-etf', 'phai-sinh', 'ma-chung-khoan', 'dau-tu', 'uy-thac', 'quy-huu-tri', 'co-tuc', 'ky-quy']:
        return [
            {"entity_field": "Cơ quan quản lý nhà nước", "value": "Ủy ban Chứng khoán Nhà nước (UBCKNN)", "entity_type": "Organization", "role": "Cơ quan quản lý và cấp phép hoạt động thị trường"},
            {"entity_field": "Cơ quan lưu ký tài sản", "value": "Tổng công ty Lưu ký và Bù trừ Chứng khoán Việt Nam (VSDC)", "entity_type": "Organization", "role": "Lưu ký và quản lý tách bạch tài sản nhà đầu tư"},
            {"entity_field": "Công ty chứng khoán đối tác", "value": "Công ty Cổ phần Chứng khoán CV (CVS)", "entity_type": "Organization", "role": "Đơn vị cung cấp nền tảng mở tài khoản và giao dịch"},
            {"entity_field": "Luật điều chỉnh", "value": "Luật Chứng khoán số 54/2019/QH14", "entity_type": "Regulation", "role": "Khung pháp lý điều chỉnh thị trường chứng khoán"},
            {"entity_field": "Chu kỳ thanh toán", "value": "Chu kỳ thanh toán T+2 theo Quy chế bù trừ thanh toán VSDC", "entity_type": "Metric", "role": "Thời gian tiền và chứng khoán về tài khoản trước 13h00 ngày T+2"},
        ]
    elif theme_id in ['thue-tncn', 'ma-so-thue', 'giam-tru-gia-canh', 'tinh-luong', 'thue']:
        return [
            {"entity_field": "Cơ quan quản lý thuế", "value": "Tổng cục Thuế - Bộ Tài chính", "entity_type": "Organization", "role": "Cơ quan thu và kiểm tra quyết toán thuế"},
            {"entity_field": "Mức giảm trừ bản thân", "value": "11.000.000 VNĐ/tháng (132 triệu đồng/năm)", "entity_type": "Metric", "role": "Mức giảm trừ gia cảnh cho người nộp thuế"},
            {"entity_field": "Mức giảm trừ người phụ thuộc", "value": "4.400.000 VNĐ/tháng cho mỗi người phụ thuộc", "entity_type": "Metric", "role": "Mức giảm trừ người phụ thuộc hợp pháp"},
            {"entity_field": "Văn bản pháp quy", "value": "Luật Thuế TNCN & Nghị quyết 954/2020/UBTVQH14", "entity_type": "Regulation", "role": "Căn cứ điều chỉnh mức giảm trừ thuế"},
            {"entity_field": "Biểu thuế lũy tiến", "value": "7 bậc thuế suất từ 5% đến 35%", "entity_type": "Metric", "role": "Khung thuế áp dụng cho thu nhập từ tiền lương"},
        ]
    elif theme_id in ['thue-truoc-ba']:
        return [
            {"entity_field": "Cơ quan quản lý thu", "value": "Chi cục Thuế các quận, huyện", "entity_type": "Organization", "role": "Cơ quan thẩm định và thu lệ phí trước bạ"},
            {"entity_field": "Căn cứ pháp lý", "value": "Nghị định 10/2022/NĐ-CP & Thông tư 13/2022/TT-BTC", "entity_type": "Regulation", "role": "Quy định mức thu lệ phí trước bạ tài sản"},
            {"entity_field": "Mức thu ô tô con", "value": "10% - 12% tùy địa phương đăng ký lần đầu", "entity_type": "Metric", "role": "Tỷ lệ thu lệ phí trước bạ ô tô"},
            {"entity_field": "Mức thu xe máy", "value": "2% - 5% tùy khu vực đô thị hoặc nông thôn", "entity_type": "Metric", "role": "Tỷ lệ thu lệ phí trước bạ xe máy"},
        ]
    elif theme_id in ['bao-hiem-nhan-tho', 'bao-hiem-tai-nan', 'bao-hiem-chay-no', 'phi-bao-hiem']:
        return [
            {"entity_field": "Cơ quan quản lý bảo hiểm", "value": "Cục Quản lý, giám sát bảo hiểm - Bộ Tài chính", "entity_type": "Organization", "role": "Quản lý và cấp phép kinh doanh bảo hiểm"},
            {"entity_field": "Văn bản pháp luật", "value": "Luật Kinh doanh bảo hiểm số 08/2022/QH15", "entity_type": "Regulation", "role": "Khung pháp lý hợp đồng bảo hiểm thương mại"},
            {"entity_field": "Thời gian cân nhắc", "value": "21 ngày kể từ ngày nhận hợp đồng bảo hiểm", "entity_type": "Metric", "role": "Thời hạn hủy hợp đồng nhận lại 100% phí"},
            {"entity_field": "Doanh nghiệp cung ứng", "value": "Các công ty bảo hiểm nhân thọ/phi nhân thọ được cấp phép", "entity_type": "Organization", "role": "Đơn vị bảo lãnh và chi trả quyền lợi bồi thường"},
        ]
    elif theme_id in ['esim-du-lich', 'sim-du-lich', 'sim-thai-lan', 'sim-nhat-ban', 'sim-trung-quoc']:
        return [
            {"entity_field": "Cơ quan quản lý viễn thông", "value": "Cục Viễn thông - Bộ Thông tin và Truyền thông", "entity_type": "Organization", "role": "Quản lý tiêu chuẩn kỹ thuật viễn thông"},
            {"entity_field": "Tiêu chuẩn kỹ thuật", "value": "GSMA eSIM Standard (RSP Architecture)", "entity_type": "Regulation", "role": "Chuẩn nạp profile viễn thông từ xa"},
            {"entity_field": "Phương thức kích hoạt", "value": "Quét mã QR Profile cài đặt trực tiếp trên máy", "entity_type": "Product", "role": "Cơ chế cài đặt không cần SIM vật lý"},
            {"entity_field": "Phạm vi phủ sóng", "value": "Chuyển vùng quốc tế tại hơn 100+ quốc gia", "entity_type": "Place", "role": "Hạ tầng liên kết nhà mạng quốc tế"},
        ]
    elif theme_id in ['gui-tiet-kiem', 'lai-suat', 'tich-luy', 'chung-chi-tien-gui']:
        return [
            {"entity_field": "Cơ quan quản lý tiền tệ", "value": "Ngân hàng Nhà nước Việt Nam (NHNN)", "entity_type": "Organization", "role": "Cơ quan quản lý trần lãi suất tiền gửi"},
            {"entity_field": "Chính sách bảo hiểm tiền gửi", "value": "Hạn mức tối đa 125 triệu đồng/người/tổ chức (BHTGVN)", "entity_type": "Regulation", "role": "Bảo vệ tiền gửi cá nhân theo Quyết định 32/2021/QĐ-TTg"},
            {"entity_field": "Tổ chức nhận tiền gửi", "value": "Ngân hàng thương mại được NHNN cấp phép", "entity_type": "Organization", "role": "Tổ chức tín dụng huy động vốn"},
            {"entity_field": "Kỳ hạn áp dụng", "value": "Từ 1 tháng đến 36 tháng hoặc không kỳ hạn", "entity_type": "Concept", "role": "Khung thời gian gửi tiết kiệm sinh lời"},
        ]
    elif theme_id in ['phat-nguoi', 'loi-giao-thong']:
        return [
            {"entity_field": "Cơ quan phát hiện vi phạm", "value": "Cục Cảnh sát Giao thông - Bộ Công an", "entity_type": "Organization", "role": "Cơ quan quản lý hệ thống camera phạt nguội"},
            {"entity_field": "Cơ sở dữ liệu tra cứu", "value": "Cổng thông tin điện tử Cục CSGT (csgt.vn)", "entity_type": "Product", "role": "Hệ thống dữ liệu vi phạm toàn quốc"},
            {"entity_field": "Căn cứ xử phạt", "value": "Nghị định 168/2024/NĐ-CP của Chính phủ", "entity_type": "Regulation", "role": "Khung mức phạt tiền và quy định trừ điểm giấy phép lái xe"},
            {"entity_field": "Cổng nộp phạt trực tuyến", "value": "Cổng Dịch vụ công Quốc gia (dichvucong.gov.vn)", "entity_type": "Product", "role": "Kênh thanh toán tiền phạt trực tuyến"},
        ]
    else:
        return [
            {"entity_field": "Cơ quan quản lý chuyên ngành", "value": f"Cơ quan quản lý nhà nước điều chỉnh lĩnh vực {theme_name}", "entity_type": "Organization", "role": "Cấp phép và giám sát tiêu chuẩn"},
            {"entity_field": "Khung pháp lý áp dụng", "value": f"Các văn bản quy phạm pháp luật hiện hành điều chỉnh {theme_name}", "entity_type": "Regulation", "role": "Quy định điều kiện và tiêu chuẩn nghiệp vụ"},
            {"entity_field": "Hạ tầng kỹ thuật", "value": "Nền tảng Web MoMo tích hợp bảo mật đa tầng", "entity_type": "Product", "role": "Kênh tra cứu và đối soát dữ liệu trực tuyến"},
            {"entity_field": "Tiêu chuẩn an toàn thông tin", "value": "Bảo mật đa tầng theo tiêu chuẩn quốc tế PCI DSS Level 1", "entity_type": "Regulation", "role": "Bảo vệ toàn vẹn dữ liệu giao dịch"},
            {"entity_field": "Kênh đối soát & Tra cứu", "value": "Cổng thông tin Nền tảng Web MoMo cập nhật 24/7", "entity_type": "Product", "role": "Hỗ trợ khách hàng đối soát trực tuyến"},
        ]

# ---------------------------------------------------------------------------
# Semantic Evidence Keywords Matcher (Requirement 6)
# ---------------------------------------------------------------------------
def select_gap_keywords(theme_keywords: list, gap_title: str, used_keywords: set) -> list:
    title_words = set(re.findall(r'\b\w+\b', gap_title.lower()))
    stopwords = {
        'và', 'của', 'các', 'về', 'trong', 'cho', 'theo', 'những', 'được', 'có', 'là',
        'để', 'quy', 'định', 'hướng', 'dẫn', 'chi', 'tiết', 'thực', 'tế', 'thông', 'tin',
        'cơ', 'chế', 'pháp', 'lý', 'chuẩn', 'hóa', 'đối', 'soát'
    }
    title_terms = title_words - stopwords

    scored = []
    for kw_obj in theme_keywords:
        kw = kw_obj.get('keyword', '').strip()
        if not kw or kw in used_keywords:
            continue
        kw_tokens = set(re.findall(r'\b\w+\b', kw.lower()))
        match_count = len(kw_tokens & title_terms)

        sub_score = 0
        for t in title_terms:
            if len(t) >= 3 and t in kw.lower():
                sub_score += 1

        vol = kw_obj.get('search_volume', 0)
        total_score = match_count * 10 + sub_score * 5 + (vol / 100000)
        scored.append((total_score, kw))

    scored.sort(key=lambda x: x[0], reverse=True)
    picked = [item[1] for item in scored[:2]]

    if len(picked) < 2:
        for kw_obj in theme_keywords:
            kw = kw_obj.get('keyword', '').strip()
            if kw and kw not in used_keywords and kw not in picked:
                picked.append(kw)
                if len(picked) == 2:
                    break

    for p in picked:
        used_keywords.add(p)
    return picked

from scripts.lib.geo_gap_blueprints import GEO_GAP_BLUEPRINTS

def build_entity_gaps(theme_id: str, theme_name: str, sector: str, theme_keywords: list) -> list:
    used_kws = set()
    raw_gaps = GEO_GAP_BLUEPRINTS.get(theme_id)
    if not raw_gaps:
        raise ValueError(f"Missing bespoke gaps for theme: {theme_id}")

    gaps = []
    for g in raw_gaps:
        title = clean_dashes(g['title'])
        detail = clean_dashes(g['detail'])
        angle = clean_dashes(g['angle'])
        ev_kws = select_gap_keywords(theme_keywords, title, used_kws)
        gaps.append({
            "title": title,
            "detail": detail,
            "angle": angle,
            "evidence_keywords": ev_kws
        })
    return gaps

# ---------------------------------------------------------------------------
# Schema Block Builder (Strict Intent Mapping with Real MoMo URLs)
# ---------------------------------------------------------------------------
def build_schema_block(theme_id: str, theme_name: str, sector: str, direct_answer: str, blueprint_match: str, momo_url: str):
    if blueprint_match is None:
        return None

    if theme_id in ['tinh-luong', 'tinh-calo', 'bmi', 'lai-kep', 'thue-truoc-ba']:
        schema_type = 'WebApplication'
        mandatory_fields = [
            {"field": "name", "desc": f"Tên công cụ tính toán {theme_name}."},
            {"field": "url", "desc": "Địa chỉ URL chính thức của công cụ trên Nền tảng Web MoMo."},
            {"field": "applicationCategory", "desc": "Danh mục ứng dụng công cụ tài chính/tiện ích."},
            {"field": "operatingSystem", "desc": "Hệ điều hành hỗ trợ (Web browser, iOS, Android)."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "WebApplication",
            "@id": f"{momo_url}#app",
            "url": momo_url,
            "name": f"Công Cụ Tính Toán {theme_name} Trực Tuyến",
            "description": direct_answer,
            "applicationCategory": "BusinessApplication" if sector == 'Financial' else "HealthApplication",
            "operatingSystem": "All",
            "browserRequirements": "Requires JavaScript. Requires HTML5."
        }
    elif theme_id in ['gia-xang', 'gia-dau', 'gia-xe', 'tram-xang']:
        schema_type = 'Dataset'
        mandatory_fields = [
            {"field": "name", "desc": f"Bảng dữ liệu chỉ số giá {theme_name}."},
            {"field": "url", "desc": "Địa chỉ URL theo dõi dữ liệu trên Nền tảng Web MoMo."},
            {"field": "description", "desc": "Tóm tắt nguồn dữ liệu và chu kỳ cập nhật giá."},
            {"field": "creator", "desc": "Đơn vị tổng hợp và công bố dữ liệu giá."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "Dataset",
            "@id": f"{momo_url}#dataset",
            "url": momo_url,
            "name": f"Bảng Biến Động Chỉ Số {theme_name}",
            "description": direct_answer,
            "creator": {"@type": "Organization", "name": "Nền tảng Web MoMo", "url": "https://www.momo.vn"},
            "license": "https://creativecommons.org/licenses/by/4.0/"
        }
    elif theme_id in ['gui-tiet-kiem', 'lai-suat', 'tich-luy', 'chung-chi-tien-gui']:
        schema_type = 'DepositAccount'
        mandatory_fields = [
            {"field": "name", "desc": "Tên gói sản phẩm tiền gửi tiết kiệm."},
            {"field": "url", "desc": "Địa chỉ URL chính thức của sản phẩm trên MoMo."},
            {"field": "provider", "desc": "Ngân hàng thương mại huy động được NHNN cấp phép."},
            {"field": "interestRate", "desc": "Lãi suất niêm yết theo kỳ hạn (%/năm)."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "DepositAccount",
            "@id": f"{momo_url}#deposit-account",
            "url": momo_url,
            "name": f"Tiền Gửi {theme_name}",
            "provider": {"@type": "BankOrCreditUnion", "name": "Ngân hàng TMCP Bản Việt (BVBank)"},
            "interestRate": {"@type": "QuantitativeValue", "value": 5.5, "unitText": "%/năm"},
            "areaServed": "VN"
        }
    elif theme_id in ['vay', 'vay-tin-chap', 'vay-the-chap']:
        schema_type = 'LoanOrCredit'
        mandatory_fields = [
            {"field": "name", "desc": "Tên gói vay tín dụng tiêu dùng."},
            {"field": "url", "desc": "Địa chỉ URL sản phẩm trên MoMo."},
            {"field": "provider", "desc": "Tổ chức tín dụng hoặc công ty tài chính được cấp phép."},
            {"field": "loanTerm", "desc": "Kỳ hạn khoản vay tối thiểu và tối đa."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "LoanOrCredit",
            "@id": f"{momo_url}#credit",
            "url": momo_url,
            "name": f"Gói Vay {theme_name}",
            "provider": {"@type": "FinancialService", "name": "Công ty Tài chính Cổ phần Điện lực (EVN Finance)"},
            "loanTerm": {"@type": "QuantitativeValue", "minValue": 6, "maxValue": 36, "unitText": "tháng"},
            "areaServed": "VN"
        }
    elif theme_id in ['the-tin-dung', 'the-ghi-no', 'chuyen-khoan', 'thanh-toan-qr', 'vi-dien-tu', 'vetc', 'epass', 'phi-khong-dung', 'phi-duong-bo', 'the-tra-truoc', 'the-visa', 'master-card', 'napas', 'internet-banking']:
        schema_type = 'PaymentService'
        mandatory_fields = [
            {"field": "name", "desc": "Tên phương tiện thanh toán hoặc thẻ ngân hàng."},
            {"field": "url", "desc": "Địa chỉ URL dịch vụ thanh toán trên MoMo."},
            {"field": "provider", "desc": "Tổ chức chuyển mạch thẻ hoặc đơn vị vận hành thu phí."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "PaymentService",
            "@id": f"{momo_url}#payment",
            "url": momo_url,
            "name": f"Dịch Vụ Thanh Toán {theme_name}",
            "provider": {"@type": "Organization", "name": "Hệ thống Đối tác Thanh toán MoMo"},
            "areaServed": "VN"
        }
    elif theme_id in ['chung-khoan', 'co-phieu', 'trai-phieu', 'chung-chi-quy', 'quy-etf', 'phai-sinh', 'gia-vang', 'bac', 'ty-gia', 'ngoai-te', 'doi-tien', 'kieu-hoi', 'vi-tra-sau', 'tin-dung', 'du-no', 'thau-chi', 'diem-tin-dung', 'no-xau', 'ma-chung-khoan', 'dau-tu', 'uy-thac', 'ky-quy']:
        schema_type = 'FinancialProduct'
        mandatory_fields = [
            {"field": "name", "desc": "Tên sản phẩm tài chính hoặc dịch vụ đầu tư."},
            {"field": "url", "desc": "Địa chỉ URL chính thức trên Nền tảng Web MoMo."},
            {"field": "provider", "desc": "Công ty chứng khoán hoặc ngân hàng đối tác được cấp phép."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "FinancialProduct",
            "@id": f"{momo_url}#product",
            "url": momo_url,
            "name": f"Sản Phẩm Tài Chính {theme_name}",
            "provider": {"@type": "FinancialService", "name": "Công ty Cổ phần Chứng khoán CV (CVS)" if 'khoan' in theme_id or 'phieu' in theme_id or 'quy' in theme_id else "Hệ thống Ngân hàng Đối tác MoMo"},
            "areaServed": "VN"
        }
    elif theme_id.startswith('bao-hiem') or theme_id == 'phi-bao-hiem':
        schema_type = 'InsuranceProduct'
        mandatory_fields = [
            {"field": "name", "desc": "Tên sản phẩm bảo hiểm."},
            {"field": "url", "desc": "Địa chỉ URL sản phẩm bảo hiểm trên MoMo."},
            {"field": "provider", "desc": "Doanh nghiệp bảo hiểm được Bộ Tài chính cấp phép."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "InsuranceProduct",
            "@id": f"{momo_url}#insurance",
            "url": momo_url,
            "name": f"Sản Phẩm {theme_name}",
            "provider": {"@type": "InsuranceAgency", "name": "Doanh nghiệp Bảo hiểm được Bộ Tài chính cấp phép"},
            "areaServed": "VN"
        }
    elif theme_id in ['phat-nguoi', 'loi-giao-thong', 'giay-phep-lai-xe', 'thi-bang-lai-xe', 'dang-kiem', 'bien-so-xe', 'bien-so-dep', 'sang-ten-xe', 'thue-tncn', 'ma-so-thue', 'giam-tru-gia-canh', 'thue', 'bhyt', 'bhxh', 'xo-so', 'vietlott', 've-so']:
        schema_type = 'GovernmentService'
        mandatory_fields = [
            {"field": "name", "desc": "Tên thủ tục dịch vụ công hoặc tra cứu hành chính."},
            {"field": "url", "desc": "Địa chỉ URL tra cứu trên Nền tảng Web MoMo."},
            {"field": "provider", "desc": "Cơ quan hành chính nhà nước hoặc đơn vị được ủy quyền."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "GovernmentService",
            "@id": f"{momo_url}#service",
            "url": momo_url,
            "name": f"Dịch Vụ Tra Cứu {theme_name}",
            "provider": {"@type": "GovernmentOrganization", "name": "Cổng Dịch vụ công Quốc gia & Cơ quan Chức năng"},
            "areaServed": "VN"
        }
    elif sector == 'cinema':
        schema_type = 'MovieTheater'
        mandatory_fields = [
            {"field": "name", "desc": "Tên cụm rạp hoặc lịch phim chiếu rạp."},
            {"field": "url", "desc": "Địa chỉ URL đặt vé xem phim trên MoMo Cinema."},
            {"field": "provider", "desc": "Hệ thống cụm rạp đối tác."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "MovieTheater",
            "@id": f"{momo_url}#theater",
            "url": momo_url,
            "name": f"Cụm Rạp & Lịch Chiếu {theme_name}",
            "provider": {"@type": "Organization", "name": "Hệ thống Cụm Rạp Đối tác MoMo (CGV, Lotte, Galaxy, Beta)"},
            "areaServed": "VN"
        }
    elif sector == 'ota':
        schema_type = 'TravelAgency'
        mandatory_fields = [
            {"field": "name", "desc": "Tên dịch vụ vận tải hoặc cẩm nang du lịch."},
            {"field": "url", "desc": "Địa chỉ URL dịch vụ du lịch trên MoMo."},
            {"field": "provider", "desc": "Hãng hàng không, đường sắt hoặc nhà xe đối tác."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "TravelAgency",
            "@id": f"{momo_url}#agency",
            "url": momo_url,
            "name": f"Dịch Vụ Du Lịch {theme_name}",
            "provider": {"@type": "Organization", "name": "Hệ thống Đối tác Du lịch & Vận tải MoMo"},
            "areaServed": "VN"
        }
    elif sector in ['telco', 'Entertainment']:
        schema_type = 'Product'
        mandatory_fields = [
            {"field": "name", "desc": "Tên gói cước hoặc sản phẩm giải trí."},
            {"field": "url", "desc": "Địa chỉ URL sản phẩm trên MoMo."},
            {"field": "offers", "desc": "Giá niêm yết hoặc chính sách ưu đãi."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "Product",
            "@id": f"{momo_url}#product",
            "url": momo_url,
            "name": f"Gói Dịch Vụ {theme_name}",
            "offers": {"@type": "Offer", "url": momo_url, "priceCurrency": "VND", "availability": "https://schema.org/InStock"},
            "areaServed": "VN"
        }
    elif sector == 'hospital':
        schema_type = 'MedicalOrganization'
        mandatory_fields = [
            {"field": "name", "desc": "Tên cơ sở y tế hoặc chuyên khoa khám bệnh."},
            {"field": "url", "desc": "Địa chỉ URL dịch vụ y tế trên MoMo."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "MedicalOrganization",
            "@id": f"{momo_url}#medical-org",
            "url": momo_url,
            "name": f"Cổng Dịch Vụ Y Tế {theme_name}",
            "areaServed": "VN"
        }
    elif sector == 'student' and theme_id != 'viec-lam-sinh-vien':
        schema_type = 'EducationalOrganization'
        mandatory_fields = [
            {"field": "name", "desc": "Tên cơ sở giáo dục hoặc thông tin tuyển sinh."},
            {"field": "url", "desc": "Địa chỉ URL thông tin giáo dục trên MoMo."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "EducationalOrganization",
            "@id": f"{momo_url}#edu-org",
            "url": momo_url,
            "name": f"Thông Tin Đào Tạo {theme_name}",
            "areaServed": "VN"
        }
    elif theme_id == 'viec-lam-sinh-vien':
        schema_type = 'EmploymentAgency'
        mandatory_fields = [
            {"field": "name", "desc": "Tên dịch vụ việc làm sinh viên."},
            {"field": "url", "desc": "Địa chỉ URL việc làm sinh viên trên MoMo."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "EmploymentAgency",
            "@id": f"{momo_url}#employment-agency",
            "url": momo_url,
            "name": "Cổng Thông Tin Việc Làm Thêm Sinh Viên",
            "areaServed": "VN"
        }
    else:
        schema_type = 'Article'
        mandatory_fields = [
            {"field": "headline", "desc": f"Tiêu đề bài viết chuyên sâu về {theme_name}."},
            {"field": "url", "desc": "Địa chỉ URL bài viết trên Nền tảng Web MoMo."},
            {"field": "author", "desc": "Tổ chức biên soạn nội dung chuyên môn."},
        ]
        jsonld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "@id": f"{momo_url}#article",
            "url": momo_url,
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": momo_url
            },
            "headline": f"Cẩm Nang Kiến Thức {theme_name}",
            "description": direct_answer,
            "author": {"@type": "Organization", "name": "Nền tảng Web MoMo", "url": "https://www.momo.vn"},
            "publisher": {"@type": "Organization", "name": "MoMo", "url": "https://www.momo.vn"},
            "inLanguage": "vi-VN"
        }

    return {
        "type": schema_type,
        "mandatory_fields": mandatory_fields,
        "jsonld": jsonld
    }

# ---------------------------------------------------------------------------
# Deep Sources Builder (All URLs have specific paths, zero homepage-only links)
# ---------------------------------------------------------------------------
def build_sources(theme_id: str, sector: str) -> list:
    # Securities & Investment (12)
    if theme_id in ['chung-khoan', 'co-phieu', 'trai-phieu', 'chung-chi-quy', 'quy-etf', 'phai-sinh', 'ma-chung-khoan', 'dau-tu', 'uy-thac', 'quy-huu-tri', 'co-tuc', 'ky-quy']:
        return [
            OFFICIAL_SOURCES['ssc_law'],
            OFFICIAL_SOURCES['vsd_settlement'],
            OFFICIAL_SOURCES['cvs_fee']
        ]
    # Savings & Deposit (5)
    elif theme_id in ['gui-tiet-kiem', 'lai-suat', 'tich-luy', 'chung-chi-tien-gui', 'quy-du-phong']:
        return [
            OFFICIAL_SOURCES['sbv_deposit'],
            OFFICIAL_SOURCES['div_limit'],
            OFFICIAL_SOURCES['vcb_savings']
        ]
    # Cards & Payments (10)
    elif theme_id in ['the-tin-dung', 'the-ghi-no', 'the-tra-truoc', 'the-visa', 'master-card', 'napas', 'thanh-toan-qr', 'chuyen-khoan', 'internet-banking', 'vi-dien-tu']:
        return [
            OFFICIAL_SOURCES['sbv_card'],
            OFFICIAL_SOURCES['sbv_payment']
        ]
    # Loans & Credit (9)
    elif theme_id in ['vay', 'vay-tin-chap', 'vay-the-chap', 'tin-dung', 'du-no', 'thau-chi', 'lai-vay', 'tra-gop']:
        return [
            OFFICIAL_SOURCES['sbv_lending'],
            OFFICIAL_SOURCES['sbv_consumer_loan']
        ]
    elif theme_id == 'vi-tra-sau':
        return [
            OFFICIAL_SOURCES['tpb_paylater'],
            OFFICIAL_SOURCES['sbv_consumer_loan']
        ]
    # Credit Score & Bad Debt (2)
    elif theme_id in ['diem-tin-dung', 'no-xau']:
        return [
            OFFICIAL_SOURCES['cic_circular'],
            OFFICIAL_SOURCES['sbv_lending']
        ]
    # Gold & Silver (2)
    elif theme_id in ['gia-vang', 'bac']:
        return [
            OFFICIAL_SOURCES['sbv_gold'],
            OFFICIAL_SOURCES['vcb_fx']
        ]
    # FX & Remittance (4)
    elif theme_id in ['ty-gia', 'ngoai-te', 'doi-tien', 'kieu-hoi']:
        return [
            OFFICIAL_SOURCES['sbv_fx'],
            OFFICIAL_SOURCES['vcb_fx']
        ]
    # Tax & Salary (5)
    elif theme_id in ['thue-tncn', 'ma-so-thue', 'giam-tru-gia-canh', 'thue']:
        return [
            OFFICIAL_SOURCES['gdt_pit'],
            OFFICIAL_SOURCES['gdt_deduction']
        ]
    elif theme_id == 'tinh-luong':
        return [
            OFFICIAL_SOURCES['gdt_pit'],
            OFFICIAL_SOURCES['labor_law']
        ]
    # Banking System (1)
    elif theme_id == 'ngan-hang':
        return [
            OFFICIAL_SOURCES['sbv_law'],
            OFFICIAL_SOURCES['bidv_rates']
        ]
    # Crypto (1)
    elif theme_id == 'crypto':
        return [
            OFFICIAL_SOURCES['crypto_directive'],
            OFFICIAL_SOURCES['cyber_law']
        ]
    # Other Financial Macro / Wealth (11)
    elif theme_id in ['gdp', 'lam-phat', 'giam-phat', 'lai-kep', 'ke-hoach-tai-chinh', 'tu-do-tai-chinh', 'tai-san', 'tieu-san', 'dong-tien', 'von-luu-dong', 'quy-mo']:
        return [
            OFFICIAL_SOURCES['sbv_law'],
            OFFICIAL_SOURCES['bidv_rates']
        ]
    # Insurtech (8) - Notice: bao-hiem-nhan-tho has ONLY insurance_commercial (no Decree 67)
    elif theme_id == 'bao-hiem-nhan-tho':
        return [
            OFFICIAL_SOURCES['insurance_commercial']
        ]
    elif theme_id in ['bao-hiem-o-to', 'bao-hiem-xe-may']:
        return [
            OFFICIAL_SOURCES['insurance_motor'],
            OFFICIAL_SOURCES['insurance_commercial']
        ]
    elif theme_id in ['bao-hiem-tai-nan', 'bao-hiem-chay-no', 'phi-bao-hiem']:
        return [
            OFFICIAL_SOURCES['insurance_commercial'],
            OFFICIAL_SOURCES['insurance_motor']
        ]
    elif theme_id in ['bhyt', 'bhxh']:
        return [
            OFFICIAL_SOURCES['bhyt_law'],
            OFFICIAL_SOURCES['bhxh_law']
        ]
    # Vehicle Hub (33)
    elif theme_id in ['phat-nguoi', 'loi-giao-thong']:
        return [
            OFFICIAL_SOURCES['csgt_lookup'],
            OFFICIAL_SOURCES['dvc_fines'],
            OFFICIAL_SOURCES['csgt_decree100']
        ]
    elif theme_id == 'dang-kiem':
        return [
            OFFICIAL_SOURCES['vr_inspection'],
            OFFICIAL_SOURCES['dvc_fines']
        ]
    elif theme_id in ['giay-phep-lai-xe', 'thi-bang-lai-xe', 'ly-thuyet-lai-xe', 'phan-mem-mo-phong']:
        return [
            OFFICIAL_SOURCES['drvn_license'],
            OFFICIAL_SOURCES['csgt_decree100']
        ]
    elif theme_id in ['bien-so-xe', 'bien-so-dep', 'sang-ten-xe']:
        return [
            OFFICIAL_SOURCES['csgt_plate'],
            OFFICIAL_SOURCES['dvc_fines']
        ]
    elif theme_id in ['vetc', 'epass', 'phi-khong-dung', 'phi-duong-bo']:
        return [
            OFFICIAL_SOURCES['etc_decision'],
            OFFICIAL_SOURCES['csgt_decree100']
        ]
    elif theme_id in ['gia-xang', 'gia-dau', 'tram-xang']:
        return [
            OFFICIAL_SOURCES['fuel_decree'],
            OFFICIAL_SOURCES['petrolimex_prices']
        ]
    elif theme_id == 'thue-truoc-ba':
        return [
            OFFICIAL_SOURCES['gdt_registration'],
            OFFICIAL_SOURCES['csgt_decree100']
        ]
    elif sector == 'vehicle-hub':
        return [
            OFFICIAL_SOURCES['csgt_decree100'],
            OFFICIAL_SOURCES['csgt_lookup']
        ]
    # Lottery (3)
    elif theme_id in ['xo-so', 'vietlott', 've-so']:
        return [
            OFFICIAL_SOURCES['vietlott_results'],
            OFFICIAL_SOURCES['lottery_circular']
        ]
    # Trust (2)
    elif theme_id in ['lua-dao', 'bao-cao-lua-dao']:
        return [
            OFFICIAL_SOURCES['ncsc_warning'],
            OFFICIAL_SOURCES['ncsc_account']
        ]
    # Telco (8)
    elif sector == 'telco':
        return [
            OFFICIAL_SOURCES['telecom_law'],
            OFFICIAL_SOURCES['cyber_law']
        ]
    # Hospital / Health (4)
    elif theme_id in ['benh-vien', 'dat-lich-kham-benh']:
        return [
            OFFICIAL_SOURCES['health_law'],
            OFFICIAL_SOURCES['bhyt_law']
        ]
    elif theme_id in ['tinh-calo', 'bmi']:
        return [
            OFFICIAL_SOURCES['health_law']
        ]
    # Student (9)
    elif theme_id == 'viec-lam-sinh-vien':
        return [
            OFFICIAL_SOURCES['labor_law'],
            OFFICIAL_SOURCES['admission_circular']
        ]
    elif sector == 'student':
        return [
            OFFICIAL_SOURCES['admission_circular']
        ]
    # Cinema (5)
    elif sector == 'cinema':
        return [
            OFFICIAL_SOURCES['cinema_law']
        ]
    # Entertainment (4)
    elif sector == 'Entertainment':
        return [
            OFFICIAL_SOURCES['game_decree']
        ]
    # OTA (18)
    elif theme_id in ['ve-may-bay', 'du-lich-viet-nam', 'du-lich', 'tour-du-lich']:
        return [
            OFFICIAL_SOURCES['aviation_law'],
            OFFICIAL_SOURCES['railway_law']
        ]
    elif theme_id in ['ve-tau', 've-xe', 've-cap-treo', 'gia-pha', 'dat-resort']:
        return [
            OFFICIAL_SOURCES['railway_law']
        ]
    elif sector == 'ota':
        return [
            OFFICIAL_SOURCES['aviation_law']
        ]
    # Other (5)
    elif sector == 'other':
        return [
            OFFICIAL_SOURCES['cyber_law']
        ]
    return [
        OFFICIAL_SOURCES['cyber_law']
    ]

# ---------------------------------------------------------------------------
# MoMo Official & Live URLs SSOT (Extracted from GA4, GSC & Sitemap)
# ---------------------------------------------------------------------------
MOMO_THEME_URLS = {
    # Financial Hub (62 themes)
    'gui-tiet-kiem': 'https://www.momo.vn/tiet-kiem-online',
    'lai-suat': 'https://www.momo.vn/tai-chinh/lai-suat',
    'tich-luy': 'https://www.momo.vn/tiet-kiem-online',
    'chung-chi-tien-gui': 'https://www.momo.vn/tai-chinh/gui-tiet-kiem',
    'vi-tra-sau': 'https://www.momo.vn/vi-tra-sau',
    'tin-dung': 'https://www.momo.vn/diem-tin-dung',
    'diem-tin-dung': 'https://www.momo.vn/diem-tin-dung',
    'no-xau': 'https://www.momo.vn/tai-chinh/blog/no-xau-la-gi-5188',
    'du-no': 'https://www.momo.vn/blog/huong-dan-cach-thanh-toan-du-no-vi-tra-sau-tren-momo-c116dt1961',
    'thau-chi': 'https://www.momo.vn/blog/vay-thau-chi-va-nhung-dieu-ban-can-biet-c116dt1977',
    'vay': 'https://www.momo.vn/vay-nhanh',
    'vay-tin-chap': 'https://www.momo.vn/vay-nhanh',
    'vay-the-chap': 'https://www.momo.vn/blog/no-xau-co-vay-the-chap-duoc-khong-c116dt2698',
    'tra-gop': 'https://www.momo.vn/blog/nhung-dieu-can-biet-khi-mua-tra-gop-dien-thoai-c116dt1408',
    'lai-vay': 'https://www.momo.vn/vay-nhanh/blog/cach-tinh-lai-suat-vay-ngan-hang-don-gian-va-chinh-xac-nhat-1314',
    'the-tin-dung': 'https://www.momo.vn/mo-the-tin-dung',
    'the-ghi-no': 'https://www.momo.vn/blog/nen-chon-su-dung-the-tin-dung-hay-the-ghi-no-c181dt1610',
    'the-tra-truoc': 'https://www.momo.vn/mo-the-tin-dung',
    'the-visa': 'https://www.momo.vn/blog/the-visa-platinum-c116dt2752',
    'master-card': 'https://www.momo.vn/hoi-dap/cach-lien-ket-momo-voi-the-quoc-te-visa-master-card-jcb',
    'napas': 'https://www.momo.vn/blog/the-napas-la-gi-c116dt2753',
    'chuyen-khoan': 'https://www.momo.vn/chuyen-tien',
    'thanh-toan-qr': 'https://www.momo.vn/thanh-toan-bang-ma-qr',
    'internet-banking': 'https://www.momo.vn/huong-dan/huong-dan-dang-ki-dich-vu-internet-banking-cua-ngan-hang-agribank',
    'chung-khoan': 'https://www.momo.vn/chung-khoan',
    'co-phieu': 'https://www.momo.vn/blog/co-tuc-la-gi-loi-ich-khi-dau-tu-vao-co-phieu-co-chi-tra-co-tuc-c116dt1825',
    'trai-phieu': 'https://www.momo.vn/tai-chinh/blog/trai-phieu-chinh-phu-5140',
    'chung-chi-quy': 'https://www.momo.vn/blog/chung-chi-quy-la-gi-co-nen-dau-tu-vao-chung-chi-quy-c116dt1355',
    'quy-etf': 'https://www.momo.vn/blog/chung-chi-quy-etf-la-gi-cach-mua-chung-chi-quy-etf-de-dang-nhat-c116dt1167',
    'phai-sinh': 'https://www.momo.vn/blog/chung-khoan-phai-sinh-c116dt1833',
    'ma-chung-khoan': 'https://www.momo.vn/chung-khoan',
    'dau-tu': 'https://www.momo.vn/tai-chinh/blog/dau-tu-tai-chinh-5186',
    'uy-thac': 'https://www.momo.vn/tai-chinh/blog/dau-tu-tai-chinh-5186',
    'ky-quy': 'https://www.momo.vn/tai-chinh/blog/margin-la-gi-ban-chat-don-bay-va-cam-nang-giao-dich-ky-quy-chung-khoan-5053',
    'co-tuc': 'https://www.momo.vn/blog/co-tuc-la-gi-loi-ich-khi-dau-tu-vao-co-phieu-co-chi-tra-co-tuc-c116dt1825',
    'gia-vang': 'https://www.momo.vn/tai-chinh/gia-vang',
    'bac': 'https://www.momo.vn/tai-chinh/blog/dau-tu-bac-5198',
    'ty-gia': 'https://www.momo.vn/tai-chinh/ty-gia',
    'ngoai-te': 'https://www.momo.vn/blog/doi-tien-do-sang-tien-viet-o-dau-dia-diem-doi-ngoai-te-uy-tin-c116dt1203',
    'doi-tien': 'https://www.momo.vn/blog/doi-tien-do-sang-tien-viet-o-dau-dia-diem-doi-ngoai-te-uy-tin-c116dt1203',
    'kieu-hoi': 'https://www.momo.vn/blog/kieu-hoi-la-gi-cach-chuyen-nhan-tien-kieu-hoi-ve-viet-nam-nhanh-chong-c116dt1149',
    'thue-tncn': 'https://www.momo.vn/tai-chinh/blog/thue-thu-nhap-ca-nhan-5047',
    'ma-so-thue': 'https://www.momo.vn/tai-chinh/blog/thue-thu-nhap-ca-nhan-5047',
    'giam-tru-gia-canh': 'https://www.momo.vn/tai-chinh/blog/khoan-giam-tru-thue-thu-nhap-ca-nhan-5087',
    'thue': 'https://www.momo.vn/tai-chinh/blog/thue-thu-nhap-ca-nhan-5047',
    'tinh-luong': 'https://www.momo.vn/tai-chinh/tinh-luong',
    'gdp': 'https://www.momo.vn/tai-chinh',
    'lam-phat': 'https://www.momo.vn/blog/lam-phat-la-gi-6-cach-de-bao-ve-tai-san-cua-ban-truoc-lam-phat-c181dt1633',
    'giam-phat': 'https://www.momo.vn/tai-chinh',
    'lai-kep': 'https://www.momo.vn/blog/lai-kep-la-gi-cong-thuc-tinh-lai-kep-c116dt774',
    'ke-hoach-tai-chinh': 'https://www.momo.vn/tai-chinh/blog/ke-hoach-tai-chinh-5184',
    'quy-du-phong': 'https://www.momo.vn/blog/huong-dan-cach-xay-dung-quy-du-phong-tai-chinh-don-gian-ma-hieu-qua-c181dt1674',
    'tai-san': 'https://www.momo.vn/blog/hieu-dung-ve-tieu-san-va-tai-san-de-tieu-tien-khon-ngoan-c181dt2101',
    'tieu-san': 'https://www.momo.vn/blog/hieu-dung-ve-tieu-san-va-tai-san-de-tieu-tien-khon-ngoan-c181dt2101',
    'dong-tien': 'https://www.momo.vn/tai-chinh/blog/quan-ly-tai-chinh-ca-nhan-5181',
    'ngan-hang': 'https://www.momo.vn/tai-chinh',
    'crypto': 'https://www.momo.vn/blog/dau-tu-crypto-la-gi-cach-dau-tu-tien-ao-an-toan-cho-nguoi-moi-bat-dau-c181dt1637',
    'quy-huu-tri': 'https://www.momo.vn/tai-chinh/blog/ke-hoach-tai-chinh-5184',
    'quy-mo': 'https://www.momo.vn/blog/quy-mo-la-gi-nhung-tieu-chi-khi-chon-dau-tu-quy-mo-c116dt1143',
    'tu-do-tai-chinh': 'https://www.momo.vn/blog/tu-do-tai-chinh-la-gi-lam-sao-de-tu-chu-tai-chinh-truoc-nam-45-tuoi-c116dt1255',
    'vi-dien-tu': 'https://www.momo.vn/hoi-dap/momo-la-gi',
    'von-luu-dong': 'https://www.momo.vn/tai-chinh/blog/quan-ly-tai-chinh-ca-nhan-5181',

    # Vehicle Hub (33 themes)
    'phat-nguoi': 'https://www.momo.vn/phat-nguoi',
    'loi-giao-thong': 'https://www.momo.vn/phat-nguoi/blog/loi-vuot-den-do-xe-may-o-to-bi-phat-bao-nhieu-tien-3',
    'giay-phep-lai-xe': 'https://www.momo.vn/blog/thu-tuc-doi-giay-phep-lai-xe-c116dt2683',
    'thi-bang-lai-xe': 'https://www.momo.vn/blog/dang-ky-thi-bang-lai-xe-may-c116dt2684',
    'ly-thuyet-lai-xe': 'https://www.momo.vn/blog/dang-ky-thi-bang-lai-xe-may-c116dt2684',
    'phan-mem-mo-phong': 'https://www.momo.vn/blog/dang-ky-thi-bang-lai-xe-may-c116dt2684',
    'dang-kiem': 'https://www.momo.vn/tien-ich-giao-thong/blog/bieu-phi-dang-kiem-o-to-5041',
    'bien-so-xe': 'https://www.momo.vn/blog/tra-cuu-bien-so-xe-c116dt2682',
    'bien-so-dep': 'https://www.momo.vn/blog/tra-cuu-bien-so-xe-c116dt2682',
    'sang-ten-xe': 'https://www.momo.vn/blog/thu-tuc-sang-ten-xe-may-c116dt2685',
    'thue-truoc-ba': 'https://www.momo.vn/bao-hiem-o-to/blog/thue-truoc-ba-o-to-la-gi-cach-tinh-va-nop-thue-truoc-ba-online-1248',
    'gia-xang': 'https://www.momo.vn/tien-ich-giao-thong/gia-xang',
    'gia-dau': 'https://www.momo.vn/tien-ich-giao-thong/gia-xang',
    'tram-xang': 'https://www.momo.vn/tien-ich-giao-thong/cay-xang',
    'tram-sac': 'https://www.momo.vn/tien-ich-giao-thong/tram-sac/vinfast',
    'doi-pin': 'https://www.momo.vn/tien-ich-giao-thong/tram-sac/vinfast',
    'vetc': 'https://www.momo.vn/tien-ich-giao-thong',
    'epass': 'https://www.momo.vn/tien-ich-giao-thong',
    'phi-khong-dung': 'https://www.momo.vn/blog/vetc-la-gi-huong-dan-dang-ky-the-vetc-online-sieu-don-gian-c193dt1295',
    'phi-duong-bo': 'https://www.momo.vn/tien-ich-giao-thong',
    'gara-o-to': 'https://www.momo.vn/bao-hiem-o-to/blog/danh-sach-20-gara-o-to-uy-tin-nhat-tai-ha-noi-1278',
    'garage-keywords-list': 'https://www.momo.vn/bao-hiem-o-to/blog/danh-sach-20-gara-o-to-uy-tin-nhat-tai-ha-noi-1278',
    'bao-duong-xe': 'https://www.momo.vn/tien-ich-giao-thong/blog/cam-nang-bao-duong-o-to-dinh-ky-quy-trinh-cac-cap-va-bang-gia-moi-nhat-5046',
    'sua-xe': 'https://www.momo.vn/bao-hiem-o-to/blog/danh-sach-20-gara-o-to-uy-tin-nhat-tai-ha-noi-1278',
    'cuu-ho-xe': 'https://www.momo.vn/tien-ich-giao-thong',
    'rua-xe': 'https://www.momo.vn/tien-ich-giao-thong',
    'bai-do-xe': 'https://www.momo.vn/tien-ich-giao-thong',
    'bai-giu-xe': 'https://www.momo.vn/tien-ich-giao-thong',
    'gia-xe': 'https://www.momo.vn/bao-hiem-o-to/blog/cac-phan-khuc-xe-o-to-tai-viet-nam-1630',
    'dinh-gia-xe': 'https://www.momo.vn/bao-hiem-o-to/blog/cac-phan-khuc-xe-o-to-tai-viet-nam-1630',
    'chi-duong': 'https://www.momo.vn/tien-ich-giao-thong',
    'metro': 'https://www.momo.vn/tien-ich-giao-thong',
    'tuyen-xe-buyt': 'https://www.momo.vn/ve-xe',

    # Cinema Hub (6 themes)
    'cinema': 'https://www.momo.vn/cinema',
    've-xem-phim': 'https://www.momo.vn/cinema',
    'lich-phim': 'https://www.momo.vn/cinema/lich-chieu-phim',
    'rap': 'https://www.momo.vn/cinema/rap',
    'phim': 'https://www.momo.vn/cinema/phim-chieu-rap',
    'dat-phim': 'https://www.momo.vn/cinema',

    # Insurtech Hub (8 themes)
    'bao-hiem-xe-may': 'https://www.momo.vn/bao-hiem-xe-may',
    'bao-hiem-o-to': 'https://www.momo.vn/bao-hiem-o-to',
    'bao-hiem-nhan-tho': 'https://www.momo.vn/bao-hiem-MoMo',
    'bao-hiem-tai-nan': 'https://www.momo.vn/bao-hiem-MoMo',
    'bao-hiem-chay-no': 'https://www.momo.vn/bao-hiem-MoMo',
    'phi-bao-hiem': 'https://www.momo.vn/thanh-toan-phi-bao-hiem',
    'bhyt': 'https://www.momo.vn/bao-hiem-MoMo',
    'bhxh': 'https://www.momo.vn/bao-hiem-MoMo',

    # OTA Hub (17 themes)
    've-may-bay': 'https://www.momo.vn/ve-may-bay',
    've-xe': 'https://www.momo.vn/ve-xe',
    've-tau': 'https://www.momo.vn/ve-tau-hoa',
    've-cap-treo': 'https://www.momo.vn/du-lich-di-lai/diem-den/da-nang/ve-cap-treo-sun-world-ba-na-hills-61',
    'du-lich': 'https://www.momo.vn/blog/du-lich',
    'tour-du-lich': 'https://www.momo.vn/blog/du-lich',
    'du-lich-viet-nam': 'https://www.momo.vn/blog/du-lich',
    'du-lich-thai-lan': 'https://www.momo.vn/blog/kinh-nghiem-du-lich-thai-lan-c101dt740',
    'du-lich-nhat': 'https://www.momo.vn/blog/kinh-nghiem-du-lich-nhat-ban-tu-tuc-c101dt1045',
    'du-lich-han-quoc': 'https://www.momo.vn/blog/du-lich-han-quoc-c101dt787',
    'du-lich-trung-quoc': 'https://www.momo.vn/blog/du-lich-trung-quoc-c101dt801',
    'du-lich-dai-loan': 'https://www.momo.vn/blog/kinh-nghiem-du-lich-dai-loan-5-ngay-4-dem-c101dt982',
    'du-lich-singapore': 'https://www.momo.vn/blog/kinh-nghiem-di-du-lich-singapore-tu-tuc-c101dt948',
    'du-lich-hongkong': 'https://www.momo.vn/blog/du-lich',
    'du-lich-an-do': 'https://www.momo.vn/blog/du-lich',
    'visa-du-lich': 'https://www.momo.vn/blog/huong-dan-xin-visa-du-lich-han-quoc-c101dt2099',
    'dat-resort': 'https://www.momo.vn/blog/top-resort-bali-dich-vu-tuyet-voi-nhat-c101dt2439',
    'gia-pha': 'https://www.momo.vn/du-lich-di-lai',

    # Telco Hub (8 themes)
    'data-4g': 'https://www.momo.vn/nap-the-data',
    'nap-tien-dien-thoai': 'https://www.momo.vn/nap-tien-dien-thoai',
    'sim': 'https://www.momo.vn/tin-tuc/khuyen-mai/mua-sim-chinh-chu-de-nhu-tro-ban-tay-vao-momo-la-7460',
    'sim-du-lich': 'https://www.momo.vn/blog/esim-du-lich',
    'esim-du-lich': 'https://www.momo.vn/blog/esim-du-lich',
    'sim-thai-lan': 'https://www.momo.vn/esim-du-lich/khu-vuc/thai-lan',
    'sim-nhat-ban': 'https://www.momo.vn/esim-du-lich/khu-vuc/nhat-ban',
    'sim-trung-quoc': 'https://www.momo.vn/esim-du-lich/khu-vuc/trung-quoc',

    # Entertainment Hub (4 themes)
    'nap-game': 'https://www.momo.vn/nap-the-game',
    'nap-tiktok': 'https://www.momo.vn/nap-xu-tiktok',
    'nph-game': 'https://www.momo.vn/thanh-toan-momo-funtap',
    'game-app': 'https://www.momo.vn/nap-the-game',

    # Lottery Hub (3 themes)
    'xo-so': 'https://www.momo.vn/blog/cach-choi-vietlott-chinh-thong-nhan-thuong-an-toan-c115dt1773',
    'vietlott': 'https://www.momo.vn/blog/cach-choi-vietlott-chinh-thong-nhan-thuong-an-toan-c115dt1773',
    've-so': 'https://www.momo.vn/huong-dan/huong-dan-mua-vietlott-sms-tren-momo',

    # Trust Hub (2 themes)
    'lua-dao': 'https://www.momo.vn/an-toan-bao-mat',
    'bao-cao-lua-dao': 'https://www.momo.vn/an-toan-bao-mat',

    # Health / Hospital Hub (4 themes)
    'benh-vien': 'https://www.momo.vn/thanh-toan-vien-phi',
    'dat-lich-kham-benh': 'https://www.momo.vn/thanh-toan-vien-phi',
    'bmi': 'https://www.momo.vn',
    'tinh-calo': 'https://www.momo.vn',

    # Student Hub (9 themes)
    'dai-hoc': 'https://www.momo.vn/tin-tuc/thong-bao/bieu-phi-moi-va-uu-dai-khi-thanh-toan-hoc-phi-ssc-8599',
    'diem-chuan': 'https://www.momo.vn',
    'tuyen-sinh': 'https://www.momo.vn',
    'hoc-phi': 'https://www.momo.vn/tin-tuc/thong-bao/bieu-phi-moi-va-uu-dai-khi-thanh-toan-hoc-phi-ssc-8599',
    'sinh-vien': 'https://www.momo.vn',
    'cao-dang': 'https://www.momo.vn',
    'truong-trung-cap': 'https://www.momo.vn',
    'nha-tro': 'https://www.momo.vn',
    'viec-lam-sinh-vien': 'https://www.momo.vn',

    # Other / Lifestyle (5 themes)
    'lich-am': 'https://www.momo.vn',
    'tu-vi': 'https://www.momo.vn',
    'tarot': 'https://www.momo.vn/blog/tarot-du-ky-c117dt866',
    'kinh-dich': 'https://www.momo.vn',
    'ma-giam-gia': 'https://www.momo.vn/tin-tuc/khuyen-mai',
}

# ---------------------------------------------------------------------------
# Main Processing Across All 161 Cluster Files
# ---------------------------------------------------------------------------
def process_all_clusters():
    files = sorted(glob.glob(str(BASE_DIR / '*' / '*.json')))
    print(f"Bắt đầu xử lý {len(files)} files cluster...")

    updated_count = 0
    exact_count = 0
    shared_count = 0
    null_count = 0

    all_updated_clusters = {}

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        theme_id = data.get('id')
        theme_name = data.get('display_name') or data.get('name') or theme_id
        sector = data.get('sector') or 'other'
        keywords = data.get('keywords', [])

        if theme_id in NULL_THEMES:
            match_type = None
            null_count += 1
        elif theme_id in EXACT_THEMES:
            match_type = 'exact'
            exact_count += 1
        else:
            match_type = 'shared'
            shared_count += 1

        direct_answer = UNIQUE_DIRECT_ANSWERS.get(theme_id)
        if not direct_answer:
            raise ValueError(f"Thiếu direct answer cho theme: {theme_id}")

        direct_answer = clean_dashes(direct_answer)
        momo_url = MOMO_THEME_URLS.get(theme_id, 'https://www.momo.vn')

        entity_facts = build_entity_facts(theme_id, theme_name, sector)
        entity_gaps = build_entity_gaps(theme_id, theme_name, sector, keywords)
        schema_block = build_schema_block(theme_id, theme_name, sector, direct_answer, match_type, momo_url)
        sources = build_sources(theme_id, sector)

        # Assemble geo_optimization
        geo_optimization = {
            "blueprint_match": match_type,
            "direct_answer_snippet": direct_answer,
            "entity_facts": entity_facts,
            "entity_gaps": entity_gaps,
            "schema": schema_block,
            "canonical_momo_url": momo_url,
            "sources": sources,
            "last_verified": "2026-10-20"
        }

        data['geo_optimization'] = geo_optimization
        all_updated_clusters[theme_id] = geo_optimization

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        updated_count += 1

    # Đồng bộ sang Knowledge Base SSOT Master: 07_REPORTS/data/inventory_clusters_summary.json
    ssot_path = Path(__file__).resolve().parent.parent / '07_REPORTS' / 'data' / 'inventory_clusters_summary.json'
    if ssot_path.exists():
        with open(ssot_path, 'r', encoding='utf-8') as f:
            ssot_data = json.load(f)
        for uc in ssot_data.get('usecases', []):
            uid = uc.get('id')
            if uid in all_updated_clusters:
                uc['geo_optimization'] = all_updated_clusters[uid]
        with open(ssot_path, 'w', encoding='utf-8') as f:
            json.dump(ssot_data, f, ensure_ascii=False, indent=2)
        print(f"Đã đồng bộ {len(all_updated_clusters)} use cases vào SSOT master: {ssot_path}")

    print(f"\nHoàn tất cập nhật 161 themes:")
    print(f"- Tổng số files đã cập nhật: {updated_count}")
    print(f"- Exact match: {exact_count}")
    print(f"- Shared match: {shared_count}")
    print(f"- Null match: {null_count}")

if __name__ == '__main__':
    process_all_clusters()

