# MoSpark - Phân Quyền & Vai Trò (RBAC)

> **Owner:** Văn Hiến (Web Product Lead) | **Version:** v1.0

Để MoSpark thực sự vận hành như một Growth OS cho phép PM/PO tự chủ (self-service) mà không phá vỡ tính nhất quán của hệ thống, nền tảng sử dụng mô hình Phân quyền dựa trên vai trò (RBAC) kết hợp Phân lập dữ liệu theo Use Case (Data Isolation).

Hệ thống được chia thành 3 nhóm người dùng chính:

---

## 1. Định Nghĩa 3 Nhóm Role Cốt Lõi

### 1.1. Internal (Web Platform) - Super Admin
- **Đại diện:** Web Product Lead (Hiến), Web Platform Manager (Bảo), Tech Lead.
- **Quyền hạn:** **Chỉnh sửa và làm tất cả**. Có toàn quyền cấu hình platform, thay đổi luật Quality Gate, xem và can thiệp vào mọi dự án (Mini Web, LP, Ads, Content) của tất cả các Cell Team.
- **Trách nhiệm chính:** Đảm bảo hệ thống chạy đúng policy, giải quyết các xung đột tài nguyên (VD: 2 Division cùng tranh một vị trí Ads), và định hướng chuẩn SEO/GEO chung.

### 1.2. Inbound - Content Creator
- **Đại diện:** Đội ngũ Content, SEO, Agency (Mai và team).
- **Quyền hạn:** Có quyền truy cập ngang (Cross-project access) vào **tất cả các nội dung** thuộc Blog / News / GenAI Content / Copywriting của Mini Web. Tuy nhiên, họ bị giới hạn các quyền liên quan đến cấu hình hệ thống hoặc chi tiêu (Ads).
- **Trách nhiệm chính:** Sản xuất nội dung chuẩn SEO/E-E-A-T, quản lý Master Keyword Registry, tối ưu điểm SEO/GEO Score.

### 1.3. Cell Team - Use Case Owner (Tenant)
- **Đại diện:** Product Manager (PM), Product Owner (PO), Growth Manager của từng BU cụ thể (VD: Vay Nhanh, Cinema, Bảo Hiểm).
- **Quyền hạn:** Quản trị chính dự án (Mini Web, Landing Page, Blog vệ tinh) của **riêng họ**. Họ không thể nhìn thấy hoặc chỉnh sửa dự án của Cell Team khác. 
- **Trách nhiệm chính:** Cung cấp và chịu trách nhiệm pháp lý cho `Business Context` (12 fields), tạo Landing Page chiến dịch, và tự setup chiến dịch Ads Manager chuyển đổi W2A.

---

## 2. Nguyên Tắc Phân Quyền Bắt Buộc (Governance Rules)

1. **Tenant Data Isolation (Cách ly theo Use Case):**
   - PM Cell Team A không thể can thiệp vào Use Case của Cell Team B. Điều này triệt tiêu rủi ro ghi đè Landing Page hoặc Cannibalize từ khóa.
2. **Quality Gate là tuyệt đối (Hard-Rule):**
   - Phân quyền không bypass được Quality Gate. Ngay cả tài khoản Super Admin (Internal) nếu publish một bài viết có SEO Score < 60 điểm hoặc dính lỗi Core Web Vitals nghiêm trọng, hệ thống vẫn sẽ disable nút Publish.
3. **Single Source of Truth cho Business Context:**
   - Inbound Team viết bài bằng AI, nhưng **Cell Team (PM) là người duy nhất có quyền khóa (lock) và phê duyệt Business Context**. AI không bao giờ được phép chạy ra khỏi ranh giới Context do PM cung cấp.

---

## 3. Ma Trận Phân Quyền Theo Module (Permission Matrix)

Dưới đây là bảng phân quyền truy cập chi tiết (View / Edit / Approve / Admin) đối với các Module cốt lõi trên MoSpark:

| Module / Tính năng | Internal (Web Platform) | Inbound | Cell Team (PM/PO) |
|---|---|---|---|
| **Tạo Use Case / Project mới** | Admin | No Access | Tạo & Yêu cầu duyệt |
| **M1: Landing Page Builder** | Admin (All) | Edit Content (All) | View/Edit/Publish (Own Project) |
| **M2: GenAI Context (12 fields)** | Admin | View Only | **Edit & Approve (Own Project)** |
| **M2: Sản xuất GenAI Blog/News** | Admin (All) | **Create/Edit/Publish (All)** | View & Review Outline |
| **M3: Ads Manager (Campaigns)**| Admin (All) | No Access | Create/Run (Own Placement) |
| **M3: Cấu hình Ads Registry** | **Admin (Global)** | No Access | No Access |
| **M4: SEO/GEO Quality Gate** | **Cấu hình Rule** | View Rules & Điểm | View Điểm |
| **M5: SEO Inventory / Keyword** | Admin | Create/Edit (All) | View (Own Project) |
| **mospark_chatbot: Web Chatbot** | Admin (All) | Edit Bot Data | View Analytics (Own Project) |

---

## 4. Luồng Phối Hợp Giữa Các Vai Trò (Workflow Handshake)

Sự phân quyền này tạo ra một vòng lặp phối hợp nhịp nhàng, ví dụ trong luồng xuất bản **GenAI Content**:

1. **Khởi tạo:** PM (Cell Team) tạo Use Case, nhập và xác nhận `Business Context` (Đảm bảo đúng policy sản phẩm, pháp lý).
2. **Nghiên cứu:** Inbound Team vào chọn từ khóa từ SEO Inventory, không bị giới hạn bởi quyền của dự án.
3. **Drafting:** Inbound Team chạy luồng GenAI (LLM tự động đọc Business Context mà PM đã chốt để viết bài).
4. **Approve:** Tùy thuộc vào quy trình của từng BU, PM có thể vào check outline hoặc bài viết.
5. **Publish:** Bài viết đi qua M4 (Quality Gate). Nếu pass, Inbound Team ấn Publish.
6. **Analytics:** PM (Cell Team) quay lại hệ thống để xem dữ liệu Traffic và Web-to-App Conversion từ bài viết đó (Chỉ xem được số của BU mình).

Với mô hình này, MoSpark vừa giữ được tính tự chủ (Cell Team không phải chờ Dev, Inbound không phải mượn tài khoản) vừa đảm bảo sự kiểm soát chặt chẽ từ trung ương (Web Platform).

---

## 5. Roadmap: Tích hợp HRM & LnD (Automated RBAC)

**Bối cảnh:** Dựa trên định hướng của nền tảng LnD (Product Led Growth) chia sẻ khóa học từ Head of BU/VP, MoSpark đang lên kế hoạch đồng bộ API với hệ thống quản trị nhân sự (HRM).

**Cơ chế Phân quyền Tương lai:**
Khi mở rộng quy mô GTM cho tất cả Division, việc phân quyền thủ công sẽ tạo ra nút thắt. Việc đồng bộ API HRM sẽ giúp tự động hóa RBAC dựa vào:
- `Email` & `Tên nhân viên`
- `Phòng ban` (Department/Division) → Tự động map vào đúng Project / Use Case.
- `Cấp bậc` (Level) → Tự động phân quyền (Reviewer, Editor, Viewer).
- `Onboarding Time` → Nắm bắt và cấp quyền kịp thời cho nhân sự mới.

Điều này giúp MoSpark dễ dàng scale-up và quản lý user tập trung trong một nền tảng Growth OS.
