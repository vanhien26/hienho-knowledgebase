import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the extra empty columns in the group headers (leftovers from removing VTTI)
content = content.replace('| **I. CHIẾN LƯỢC, CHỈ SỐ & KẾ HOẠCH VẬN HÀNH** | | | |', '| **I. CHIẾN LƯỢC, CHỈ SỐ & KẾ HOẠCH VẬN HÀNH** | | |')
content = content.replace('| **II. GIAO DIỆN WEB & PHỄU CHUYỂN ĐỔI (W2A)** | | | |', '| **II. GIAO DIỆN WEB & PHỄU CHUYỂN ĐỔI (W2A)** | | |')
content = content.replace('| **III. QUẢN TRỊ DỮ LIỆU ĐỊA ĐIỂM & BẢN ĐỒ TIỆN ÍCH** | | | |', '| **III. QUẢN TRỊ DỮ LIỆU ĐỊA ĐIỂM & BẢN ĐỒ TIỆN ÍCH** | | |')
content = content.replace('| **IV. BỘ CÔNG CỤ DỰ TOÁN CHI PHÍ & CHUYỂN TIẾP LEAD BẢO HIỂM** | | | |', '| **IV. BỘ CÔNG CỤ DỰ TOÁN CHI PHÍ & CHUYỂN TIẾP LEAD BẢO HIỂM** | | |')
content = content.replace('| **V. CẨM NANG HƯỚNG DẪN TRÊN WEB & BÁO CÁO GIẢI TRÌNH** | | | |', '| **V. CẨM NANG HƯỚNG DẪN TRÊN WEB & BÁO CÁO GIẢI TRÌNH** | | |')

# Add Group VI
group_6_content = """| **VI. KẾ HOẠCH GROWTH, TRUYỀN THÔNG & TỐI ƯU CẢI TIẾN** | | |
| 6.1 Xây dựng chiến lược SEO Content & Inbound Marketing | **A / R (Chủ trì Web)** | C (Góp ý từ khóa) |
| 6.2 Hoạch định ngân sách Truyền thông, SEM & Paid Ads | C (Hỗ trợ Landing Page) | **A / R (Cấp ngân sách & Chạy Ads)** |
| 6.3 Triển khai In-App Marketing (Push, CRM, Banner) | I (Theo dõi) | **A / R (Chủ trì In-App)** |
| 6.4 Thiết lập Tracking Analytics, Đo lường & A/B Testing | **A / R (Chủ trì Web)** | C (Hỗ trợ công cụ) |
| 6.5 Đánh giá Conversion Rate (CR) và Tối ưu Cải tiến | **A / R (Tối ưu phễu Web)** | **A / R (Tối ưu phễu In-App)** |
"""

# Inject after Group V
content = content.replace(
    '| 5.2 Báo Cáo Tiến Độ Sản Phẩm Web & Hiệu Quả W2A (IVP) | **A / R (Chủ trì tổng hợp)** | **A / R (Đồng chủ trì Báo cáo)** |\n',
    '| 5.2 Báo Cáo Tiến Độ Sản Phẩm Web & Hiệu Quả W2A (IVP) | **A / R (Chủ trì tổng hợp)** | **A / R (Đồng chủ trì Báo cáo)** |\n' + group_6_content
)

# Add Change log v8.5
changelog_entry = """| **v8.5** | 2026-08-28 | Web Product Lead | **Bổ sung Nhóm Kế Hoạch Growth & Truyền Thông vào RACI:** Bổ sung Nhóm VI vào ma trận RACI nhằm đảm bảo sản phẩm sau khi Go-live có kế hoạch truyền thông (GTM) rõ ràng. Web Platform chủ trì SEO/Inbound & Tracking Web; InsurTech Cell chủ trì ngân sách Paid Ads & In-App Marketing. Hai bên đồng sở hữu khâu Đánh giá CR và Cải tiến liên tục. |
"""
content = content.replace('| **v8.4**', changelog_entry + '| **v8.4**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Growth Plan RACI successfully.")
