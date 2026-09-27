import re

file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_raci_section = """### 4.3 Phân định Nguồn lực (Resources / RACI)

Dự án áp dụng mô hình hợp tác song phương (Bilateral) với đầu mối được tinh gọn tối đa. **InsurTech Cell** đóng vai trò là Product Owner & Business Owner tổng thể; **Web Platform** đóng vai trò là đơn vị xây dựng Kênh phân phối ngoài App (Acquisition Channel).

| Nhóm Công Việc | Web Platform | InsurTech Cell |
| :--- | :--- | :--- |
| **Sản phẩm (UI/UX)** | **Chủ trì (A/R):** Xây dựng toàn bộ giao diện Web, luồng UI/UX và phễu Onelink W2A. | **Nghiệm thu (QC):** QC nghiệm thu chất lượng sản phẩm cuối trước khi Go-live. |
| **Sản xuất Nội dung** | **Chủ trì (A/R):** Lên Content Plan và trực tiếp sản xuất bài viết (Content Production). | **Nghiệm thu (QC):** QC nội dung, kiểm duyệt độ chính xác luật và nghiệp vụ. |
| **Hạ tầng Dữ liệu (API)** | **Hỗ trợ (C):** Phối hợp tích hợp và render API lên giao diện Web. | **Chủ trì (A/R):** Cung cấp API (nếu có) và Database liên quan (Giá xăng, Trạm sạc...). |
| **Đo lường (Tracking)** | **Chủ trì Web (A/R):** Thiết lập DataLayer, tracking luồng hành vi trên Web. | **Chủ trì In-App (A/R):** Theo dõi luồng in-app và tỷ lệ rớt phễu thanh toán. |
| **Growth Plan** | **Hỗ trợ (C):** Đẩy mạnh SEO để hứng Organic Search Traffic. | **Chủ trì (A/R):** Lên Growth Plan tổng thể, hoạch định chiến lược và In-app Marketing. |

---

### 4.4 Change Log"""

# Replace everything from "### 4.3 RACI Matrix..." down to "### 4.4 Change Log"
pattern = re.compile(r'### 4\.3 RACI Matrix.*?---\n\n### 4\.4 Change Log', re.DOTALL)
content = re.sub(pattern, new_raci_section, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("BRD RACI section updated.")
