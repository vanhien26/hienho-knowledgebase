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

### 1.2. Media Team - Content Creator
- **Đại diện:** Đội ngũ Content, SEO, Agency (Media Team).
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
   - Media Team viết bài bằng AI, nhưng **Cell Team (PM) là người duy nhất có quyền khóa (lock) và phê duyệt Business Context**. AI không bao giờ được phép chạy ra khỏi ranh giới Context do PM cung cấp.

---

## 3. Ma Trận Phân Quyền Theo Module (Permission Matrix)

Dưới đây là bảng phân quyền truy cập chi tiết (View / Edit / Approve / Admin) đối với các Module cốt lõi trên MoSpark:

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Module / Tính năng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Internal (Web Platform)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Media Team</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Cell Team (PM/PO)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Tạo Use Case / Project mới</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No Access</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tạo & Yêu cầu duyệt</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M1: Landing Page Builder</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin (All)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Edit Content (All)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">View/Edit/Publish (Own Project)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M2: GenAI Context (12 fields)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">View Only</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Edit & Approve (Own Project)</strong></td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M2: Sản xuất GenAI Blog/News</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin (All)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Create/Edit/Publish (All)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">View & Review Outline</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M3: Ads Manager (Campaigns)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin (All)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No Access</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Create/Run (Own Placement)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M3: Cấu hình Ads Registry</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Admin (Global)</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No Access</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">No Access</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M4: SEO/GEO Quality Gate</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Cấu hình Rule</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">View Rules & Điểm</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">View Điểm</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>M5: SEO Inventory / Keyword</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Create/Edit (All)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">View (Own Project)</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>mospark_chatbot: Web Chatbot</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Admin (All)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Edit Bot Data</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">View Analytics (Own Project)</td>
    </tr>
  </tbody>
</table>

---

## 4. Luồng Phối Hợp Giữa Các Vai Trò (Workflow Handshake)

Sự phân quyền này tạo ra một vòng lặp phối hợp nhịp nhàng, ví dụ trong luồng xuất bản **GenAI Content**:

1. **Khởi tạo:** PM (Cell Team) tạo Use Case, nhập và xác nhận `Business Context` (Đảm bảo đúng policy sản phẩm, pháp lý).
2. **Nghiên cứu:** Media Team vào chọn từ khóa từ SEO Inventory, không bị giới hạn bởi quyền của dự án.
3. **Drafting:** Media Team chạy luồng GenAI (LLM tự động đọc Business Context mà PM đã chốt để viết bài).
4. **Approve:** Tùy thuộc vào quy trình của từng BU, PM có thể vào check outline hoặc bài viết.
5. **Publish:** Bài viết đi qua M4 (Quality Gate). Nếu pass, Media Team ấn Publish.
6. **Analytics:** PM (Cell Team) quay lại hệ thống để xem dữ liệu Traffic và Web-to-App Conversion từ bài viết đó (Chỉ xem được số của BU mình).

Với mô hình này, MoSpark vừa giữ được tính tự chủ (Cell Team không phải chờ Dev, Media Team không phải mượn tài khoản) vừa đảm bảo sự kiểm soát chặt chẽ từ trung ương (Web Platform).

---

## 5. Hiện trạng H1/2026: Tích hợp HRM & ldp.mservice.io (Automated RBAC)

**Bối cảnh:** Để mở rộng quy mô GTM cho tất cả Division mà không gây nút thắt quản trị, MoSpark đã hoàn thành việc đồng bộ API với hệ thống quản trị nhân sự (HRM) của công ty và triển khai cổng đăng nhập.

**Cơ chế Đăng nhập & Phân quyền Tự động (Completed H1):**
Trước khi sử dụng các module trên MoSpark, User truy cập vào cổng `ldp.mservice.io` để tạo tài khoản và đăng nhập bằng Gmail doanh nghiệp. Hệ thống tự động đồng bộ API HRM để đối soát dữ liệu và phân quyền tức thì cho User dựa trên các trường thông tin:
- `Email` & `Tên nhân viên` dùng để xác thực định danh gốc.
- `Phòng ban (Department/Division)` → Tự động ánh xạ và phân lập dự án (Tenant/Use Case) tương ứng, đảm bảo cách ly dữ liệu.
- `Cấp bậc (Level/Role)` → Tự động ánh xạ và phân cấp quyền hạn (Super Admin, Content Editor, Cell Team Owner).
- `Onboarding Time` → Tự động cấp quyền kịp thời cho nhân sự mới khi gia nhập dự án.

Điều này giúp MoSpark dễ dàng scale-up và quản lý user tập trung trong một nền tảng Growth OS.
