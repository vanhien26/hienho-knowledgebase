import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update the RACI Table Header
content = content.replace(
    '| Nhóm & Hạng Mục Công Việc Chi Tiết | Web Platform (Web & W2A) | InsurTech Cell (KPI & Bảo Hiểm) | VTTI (API & Giao Thông) |',
    '| Nhóm & Hạng Mục Công Việc Chi Tiết | Web Platform (Web & W2A) | InsurTech Cell (Đầu mối FS & KPI) |'
)
content = content.replace(
    '| :--- | :---: | :---: | :---: |',
    '| :--- | :---: | :---: |'
)

# Update Rows (Combine InsurTech and VTTI columns into one InsurTech column)
# Row 1.1
content = content.replace('| **A / R (Chủ trì Web)** | **A / R (Đồng sở hữu)** | **A / R (Đồng sở hữu)** |', '| **A / R (Chủ trì)** | **A / R (Đồng sở hữu)** |')
# Row 1.2
content = content.replace('| **A / R (Chủ trì)** | **A / R (Đồng chủ trì)** | R (Tham gia API) |', '| **A / R (Chủ trì)** | **A / R (Đồng chủ trì & Đầu mối API)** |')
# Row 2.1
content = content.replace('| **A / R (Chủ trì)** | C (Góp ý phễu BH) | C (Cung cấp API) |', '| **A / R (Chủ trì)** | C (Góp ý phễu BH & Điều phối API) |')
# Row 2.2
content = content.replace('| **A / R (Chủ trì)** | C (Góp ý phễu) | C (Cung cấp API) |', '| **A / R (Chủ trì)** | C (Góp ý phễu & Điều phối API) |')
# Row 2.3
content = content.replace('| **A / R (Chủ trì Web)** | C (Cross-sell BH) | C (Luật giao thông) |', '| **A / R (Chủ trì)** | C (Cross-sell BH & Duyệt logic) |')
# Row 2.4
content = content.replace('| **A / R (Chủ trì)** | C (Góp ý luồng BH) | C (Cung cấp Schema API) |', '| **A / R (Chủ trì)** | C (Góp ý luồng BH & Schema API) |')
# Row 2.5
content = content.replace('| **A / R (Chủ trì Web)** | I (Theo dõi) | C (Cung cấp Data API) |', '| **A / R (Chủ trì)** | C (Điều phối Data API) |')
# Row 3.1
content = content.replace('| A (Nghiệm thu Web) | I (Theo dõi) | **A / R (Chủ trì API & Data)** |', '| A (Nghiệm thu Web) | **A / R (Cung cấp API & Data qua VTTI)** |')
# Row 3.2
content = content.replace('| A (Nghiệm thu Web) | I (Theo dõi) | **A / R (Chủ trì API & Data)** |', '| A (Nghiệm thu Web) | **A / R (Cung cấp API & Data qua VTTI)** |')
# Row 3.3
content = content.replace('| A (Nghiệm thu Web) | I (Theo dõi) | **A / R (Chủ trì API & Data)** |', '| A (Nghiệm thu Web) | **A / R (Cung cấp API & Data qua VTTI)** |')
# Row 3.4
content = content.replace('| **A / R (Chủ trì)** | I (Theo dõi) | C (Hỗ trợ API) |', '| **A / R (Chủ trì)** | C (Hỗ trợ API) |')
# Row 4.1
content = content.replace('| **A / R (Xây Web & CTA)** | I (Theo dõi) | **A / R (Cung cấp API ePass)** |', '| **A / R (Chủ trì Web)** | **A / R (Đầu mối API ePass từ VTTI)** |')
# Row 4.2
content = content.replace('| **A / R (Chủ trì Web Tool)** | C (Góp ý công thức BH) | I (Theo dõi) |', '| **A / R (Chủ trì Web)** | C (Góp ý công thức BH) |')
# Row 4.3
content = content.replace('| **A / R (Chủ trì Web)** | C (Góp ý nghiệp vụ) | C (Góp ý luật GT) |', '| **A / R (Chủ trì Web)** | C (Góp ý nghiệp vụ) |')
# Row 4.4
content = content.replace('| **A / R (Bắt Lead Web)** | **A / R (Nhận Auto-fill)** | C (Hỗ trợ Data xe) |', '| **A / R (Bắt Lead Web)** | **A / R (Nhận Auto-fill & Xử lý data)** |')
# Row 5.1
content = content.replace('| **A / R (Chủ trì Web)** | C (Duyệt luật BH) | C (Duyệt luật GT) |', '| **A / R (Chủ trì Web)** | C (Duyệt nội dung & Luật) |')
# Row 5.2
content = content.replace('| **A / R (Chủ trì tổng hợp)** | **A / R (Đồng chủ trì Báo cáo)** | R (Báo cáo API) |', '| **A / R (Chủ trì tổng hợp)** | **A / R (Đồng chủ trì Báo cáo)** |')

# Update surrounding text
content = content.replace('3 đơn vị nòng cốt: Web Platform, InsurTech Cell và VTTI', '2 đơn vị nòng cốt: Web Platform và InsurTech Cell')
content = content.replace('3 đơn vị nòng cốt: Web Platform, InsurTech Cell (Bảo hiểm) và VTTI (Giao thông/ePass)', '2 đơn vị nòng cốt: Web Platform và InsurTech Cell')

# Change log addition
changelog_entry = """| **v8.4** | 2026-08-28 | Web Product Lead | **Lược bỏ VTTI khỏi RACI Matrix:** Chuyển đổi RACI về cơ chế hợp tác song phương (Bilateral) giữa 2 đơn vị nòng cốt: **Web Platform** và **InsurTech Cell**. FS/InsurTech sẽ đóng vai trò là đầu mối (Proxy) duy nhất để làm việc, điều phối API và Data từ VTTI, giúp Web Platform không cần giao tiếp chéo nhiều bên gây chậm trễ tiến độ. |
"""
content = content.replace('| **v8.3**', changelog_entry + '| **v8.3**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("RACI matrix updated successfully with VTTI removed.")
