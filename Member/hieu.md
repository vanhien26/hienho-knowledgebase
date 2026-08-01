# **Team Leader Software Engineer — Strategic & OKRs H2 2026**

**Hiếu — Team Leader Software Engineer (Tech Lead) | Trục 1 - Web Platform Team**

---

## **I. BỐI CẢNH & VAI TRÒ**

Web Platform Division đặt ra 4 mục tiêu chiến lược cho H2/2026: (1) Chiếm lĩnh Use-Case chiến lược để dẫn dắt traffic có độ tin cậy cao, (2) Xây dựng nền tảng AI-Powered phục vụ toàn bộ MoMo, (3) Chuẩn hóa Full Funnel Tracking đo lường chuyển đổi Web-to-App, (4) Vận hành hạ tầng công nghệ ổn định và tuân thủ chuẩn ITC.

Với vai trò Team Leader Software Engineer (Tech Lead), Hiếu chịu trách nhiệm hiện thực hóa 4 mục tiêu trên ở lớp kỹ thuật: thiết kế và trực tiếp phát triển các module frontend/backend cho Use Case chiến lược, chuẩn hóa nền tảng và tài liệu kỹ thuật dùng chung cho Cell Teams, đảm bảo hệ thống tracking đo lường chính xác, và vận hành hạ tầng ổn định, bảo mật theo tiêu chuẩn ITC. Đây không phải vai trò quản lý nhân sự trực tiếp mà tập trung vào chất lượng kỹ thuật, tốc độ triển khai và tính ổn định của hệ sinh thái Web.

---

## **II. VISION CÁ NHÂN**

*Trở thành lực lượng kỹ thuật nòng cốt giúp Web Platform triển khai nhanh, đúng chuẩn SEO/GEO và vận hành ổn định — biến mỗi Use Case chiến lược và mỗi Cell Team request thành sản phẩm chất lượng cao, đo lường được và không gián đoạn dịch vụ.*

---

## **III. OKRS H2/2026**

### **Objective 1: Thực thi kỹ thuật các công cụ tiện ích (Utilities) hướng đến xây dựng Financial Authority và hỗ trợ nền tảng cho các Use Cases của Cell Teams**

***Focus:*** *Thiết lập hạ tầng kỹ thuật cho bộ Widget Store (tra cứu/giả lập tài chính) nhằm tạo phễu organic uy tín dẫn về dịch vụ Tiết kiệm/Đầu tư; đồng thời chuyển giao giải pháp nền tảng (Onelink, tracking, dynamic placements) để các Cell Teams triển khai độc lập.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Hiếu (Tech Lead) |
| :---: | :--- | :--- | :--- |
| **KR 1.1** | **Financial Authority Utilities** | Phát triển, đóng gói và vận hành thực tế bộ công cụ tiện ích tài chính: **Calculator (tính lãi tích lũy), Simulator (giả lập trả góp/lãi suất vay), Gold Price Tracker (theo dõi giá vàng) và bộ công cụ Lương hưu/BHXH** làm phễu organic dẫn về các dịch vụ tài chính (Tiết kiệm, Đầu tư). | Chủ trì thiết kế data model, kiến trúc backend và quy chuẩn đóng gói Widget Store. Chịu trách nhiệm cao nhất về tính chính xác của thuật toán/công thức tính toán tài chính. |
| **KR 1.2** | **Cell Team Platform Support** | 100% dự án/chiến dịch của Cell Teams (Vehicle Hub, Cinema, eSIM, BHYT, BHXM...) được cung cấp giải pháp công nghệ nền tảng (Onelink chuẩn hóa, dynamic slot ads, tracking layer) và hướng dẫn tích hợp để Cell Teams tự vận hành. | Thiết kế và chuyển giao giải pháp công nghệ nền tảng; hỗ trợ kỹ thuật và kiểm duyệt kiến trúc trước khi go-live nhằm đảm bảo ổn định và tối ưu SEO/GEO. |
| **KR 1.3** | **Quality Gate & Automated Testing** | Đạt tỷ lệ bao phủ mã nguồn (Code Coverage) **$\ge$ 80%** cho các logic tài chính cốt lõi; 100% công thức tính toán tài chính của các Utility Tool được tự động kiểm thử và đối chiếu khớp dữ liệu tham chiếu trước khi release. | Xây dựng Framework kiểm thử tự động (Unit Test / Integration Test) cho các module logic tài chính để triệt tiêu lỗi tính toán sai lệch trên các trang YMYL. |

### **Objective 2: Chuẩn hóa nền tảng kỹ thuật phục vụ Cell Teams tự vận hành**

***Focus:*** *Tái cấu trúc CMS MoSpark để hỗ trợ phân quyền đa cấp, đóng gói bộ SPA Framework Boilerplate và tự động hóa khâu kiểm duyệt chất lượng deploy.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Hiếu (Tech Lead) |
| :---: | :--- | :--- | :--- |
| **KR 2.1** | **Kiến trúc MoSpark CMS Multi-Tenant** | Tái cấu trúc (Refactor) cơ sở dữ liệu và hệ thống quản trị MoSpark để hỗ trợ phân quyền đa cấp, cô lập dữ liệu (data isolation) giữa các BU/Cell Teams theo chuẩn bảo mật ITC. | Chủ trì thiết kế kiến trúc hệ thống lưu trữ, phân quyền dữ liệu và trực tiếp tối ưu hiệu năng CMS MoSpark. |
| **KR 2.2** | **SPA Framework Boilerplate** | Phát hành bộ Boilerplate Code và component chuẩn hóa tích hợp sẵn **SPA Framework** cùng bộ Mobase Component Kits V2, đảm bảo Cell Teams tự phát triển Web mà không cần can thiệp code từ Web Platform. | Đóng gói bộ Boilerplate tích hợp sẵn tracking layer chuẩn (Umami/GA4) và tối ưu hóa SEO onpage mặc định cho Cell Teams. |
| **KR 2.3** | **Automated Quality Gate Integration** | Tự động hóa 100% quy trình kiểm duyệt kỹ thuật (SEO/GEO, Core Web Vitals) trước khi deploy bằng cách tích hợp **Publish Quality Gate trực tiếp vào CI/CD pipeline**. | Thiết kế và tích hợp bộ công cụ rà quét (crawler/linter) tự động chấm điểm chất lượng (5 blocks) và thực thi cơ chế Hard-block trên pipeline xuất bản. |

### **Objective 3: Xây dựng Full Funnel Tracking Pipeline đo lường chuyển đổi Web-to-App**

***Focus:*** *hợp nhất dữ liệu đa nguồn về BigQuery, report real-time, và định danh User xuyên nền tảng. đồng bộ GA + Search Console + AppsFlyer về BigQuery, phối hợp DA build Full Funnel Report, giải pháp định danh User Web to App.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Hiếu (Tech Lead) |
| :---: | :--- | :--- | :--- |
| **KR 3.1** | **Data Unification (Anti-Fragmentation)** | Hoàn tất chuẩn hóa, đồng bộ 100% dữ liệu từ GA, Search Console, AppsFlyer về BigQuery, không còn phân mảnh nguồn dữ liệu đo lường Web-to-App. | Phối hợp với ITC và team News User chuẩn hóa, đồng bộ dữ liệu đa nguồn về BigQuery. |
| **KR 3.2** | **Full Funnel Report Real-time** | Vận hành ổn định report thời gian thực cho toàn bộ Full Funnel Web-to-App. | Phối hợp cùng DA build và duy trì Full Funnel Report; trực tiếp xử lý các rào cản kỹ thuật đa nền tảng để dữ liệu thông suốt, minh bạch. |
| **KR 3.3** | **Cross-Platform User Identity** | Duy trì và mở rộng độ phủ giải pháp định danh User thông suốt đa nền tảng Web-to-App, phục vụ đo lường chính xác New User/MAU. | Hiện thực và tối ưu giải pháp định danh User xuyên nền tảng Web-to-App (Identity Platform). |

### **Objective 4: Vận hành hạ tầng công nghệ ổn định, bảo mật, tuân thủ chuẩn ITC**

***Focus:*** *giám sát chủ động, rà soát bảo mật định kỳ, và làm đầu mối kỹ thuật với ITC. Nền H1: hệ thống giám sát/log chủ động, rà soát lỗ hổng bảo mật, tối ưu chi phí hạ tầng.*

| KR | Chỉ số cốt lõi | Tiêu chuẩn hoàn thành (H2/2026 Target) | Vai trò của Hiếu (Tech Lead) |
| :---: | :--- | :--- | :--- |
| **KR 4.1** | **Proactive Monitoring & Uptime** | Duy trì hệ thống giám sát/ghi log chủ động, đảm bảo hạ tầng Web Platform ổn định và phản hồi nhanh kể cả trong cao điểm traffic của các chiến dịch lớn. | Thiết kế và vận hành hệ thống giám sát, ghi log chủ động cho toàn bộ hạ tầng Web Platform. |
| **KR 4.2** | **Security & ITC Compliance** | Rà soát định kỳ kiến trúc hạ tầng, vá các lỗ hổng bảo mật phát hiện trong SLA cam kết; toàn bộ quy trình dev/deploy/lưu trữ dữ liệu tuân thủ chuẩn ITC. | Liên tục rà soát kiến trúc hạ tầng, vá lỗ hổng bảo mật, triển khai lớp bảo vệ và phân quyền tối ưu. |
| **KR 4.3** | **ITC Cost & Governance Liaison** | Đóng vai trò đầu mối kỹ thuật với ITC, tối ưu chi phí hạ tầng nền tảng trong khi vẫn đáp ứng đầy đủ tiêu chuẩn chung của ITC và MoMo. | Làm việc trực tiếp với đội ngũ ITC để tối ưu chi phí hạ tầng và đảm bảo tuân thủ tiêu chuẩn. |
