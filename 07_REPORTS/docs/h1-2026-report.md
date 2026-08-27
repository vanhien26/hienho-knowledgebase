# BÁO CÁO CHIẾN LƯỢC H1/2026 - TỔNG HỢP DỰ ÁN & CAM KẾT KPI



## 1. Tầm Nhìn Chiến Lược Out-App 2026
Chiến lược Out-App của MoMo trong năm 2026 đánh dấu bước dịch chuyển căn bản từ các chiến dịch đẩy khuyến mãi ngắn hạn sang mô hình tăng trưởng bền vững dựa trên thẩm quyền nội dung (Content Authority) và niềm tin kỹ thuật số (Trust-led Growth). 

Thông qua nền tảng MoSpark được định vị như một Software-as-a-Product (SaaP), GPD đã và đang tái cấu trúc năng lực tự vận hành cho các Cell Teams. Điều này cho phép các đơn vị tự quản trị trang đích và nội dung mà không bị phụ thuộc vào nguồn lực lập trình viên. Dưới đây là phân tích hệ thống về tình trạng kỹ thuật và các cam kết chỉ số đo lường (KPI Commits) của toàn bộ danh mục dự án từ đầu năm đến nay:

---

## 2. Nền Tảng Kỹ Thuật và Hạ Tầng (Platform Engineering)
Nền tảng kỹ thuật đóng vai trò là "Growth OS" tập trung vào hai nhánh hoạt động song hành: Phát triển nâng cấp hạ tầng MoSpark Platform và Phối hợp cùng các Cell Teams để thiết kế, xuất bản các sản phẩm truyền thông thương hiệu.

### 2.1. MoSpark Platform
MoSpark Platform đóng vai trò là lõi kỹ thuật tích hợp, cung cấp toàn bộ công cụ tự vận hành nội dung, hạ tầng SEO/GEO, hệ thống thiết kế và định danh người dùng:
*   *GenAI Content Engine:* Tích hợp API Claude (vận hành luồng sinh bài viết tự động 2 tầng: Outline và Chi tiết bài viết); bổ sung dashboard theo dõi số lượng token tiêu thụ và quy đổi trực tiếp chi phí (USD/VND) trên giao diện quản trị để tối ưu hóa ngân sách.
*   *PLG Project Engine:* Vận hành hệ thống quản lý tập trung các chiến dịch Product-Led Growth. Hỗ trợ upload trực tiếp CSV Keyword Research để tự động chia nhóm Theme/Cluster, quản lý Volume Search, thiết lập Integrity Guard (ràng buộc cứng xóa bài viết từ gốc tại PLG Project màn hình, đồng bộ Microsite Blog Editor).
*   *Merchant Page Builder:* Hoàn thành đồng bộ và lưu trữ cơ sở dữ liệu của hơn 200.000+ Merchant MoMo chấp nhận Ví Trả Sau. Hỗ trợ tự động sinh trang địa điểm (tọa độ Lat/Long, địa chỉ, category) theo template chuẩn, tích hợp Umami Tracking riêng biệt cho từng trang đối tác.
*   *Microsite & SEO Inventory:* Triển khai Microsite Engine tích hợp Umami Performance Dashboard đo lường lưu lượng thời gian thực. SEO Inventory tích hợp API Google Search Console (GSC) để đồng bộ click, impression, vị trí trung bình và tự động tính toán tỷ lệ chia sẻ hiển thị (Share of Voice - SoV).
*   *Nền tảng Thiết kế Mobase V2 & Editor:* Chuẩn hóa thư viện component Web UI/UX và tích hợp trực tiếp vào Puck Editor kéo thả, giúp các đội ngũ tự chủ thiết kế trang đích chuẩn nhận diện thương hiệu.
*   *Module Định danh Người dùng (Identity Platform):* Ứng dụng hạ tầng tracking qua Edge Cookie và Edge Middleware nhằm stitched (hợp nhất) chính xác hành vi người dùng ẩn danh từ Web tới các giao dịch thực tế trên App (Deep-link mapping), phục vụ đo lường ROI và hiệu quả chuyển đổi thực tế trên BigQuery.
*   *Ads Manager & Utilities Tool:* Vận hành Dynamic placement banner tự động hiển thị popup theo ngữ cảnh hành vi; xây dựng nền tảng SDK cho các công cụ tiện ích/widget tra cứu (Calculator, Simulator tính lãi suất/trả góp, và tiện ích theo dõi Giá Vàng) làm phễu gián tiếp dẫn lưu lượng về các dịch vụ tài chính (Tiết kiệm, Đầu tư).
*   *Chatbot & Knowledge Base:* Hoàn thiện công cụ tùy biến Chatbot Customizer (màu sắc, theme thương hiệu); vận hành RAG Knowledge Base Pipeline (tự động cào dữ liệu dự án PLG, vector hóa và nạp vào Vector Database để chạy cơ chế RAG tư vấn tự động); tích hợp Typebot giúp Cell Teams tự chủ xây dựng kịch bản hội thoại điều hướng người dùng.


### 2.2. Cell Team
Hạ tầng MoSpark đóng vai trò là bệ phóng giúp Media Team và Web Platform phối hợp chặt chẽ cùng các Cell Teams để thiết kế, xuất bản nhanh chóng các Mini Web, Landing Page chuyên đề và các chiến dịch truyền thông thương hiệu lớn trên Website. Các hoạt động xây dựng hạ tầng chiến dịch và nền tảng truyền thông tiêu biểu bao gồm:
*   *Dự án Trust (Cell Team Risk):* Phát triển hạ tầng tiếp nhận báo cáo lừa đảo cộng đồng ẩn danh, kết hợp xuất bản các bản tin Cảnh báo An toàn Bảo mật hàng quý nhằm củng cố niềm tin và giảm thiểu rủi ro cho người dùng.
*   *Mega Campaign (Cell Team Marketing):* Thiết lập hệ thống Landing Pages tối ưu hóa khả năng chịu tải và hiển thị cho các chiến dịch khuyến mãi quy mô lớn trong năm, hỗ trợ công cụ minigame gắn kết người dùng Out-App.
*   *Lắc Xì (Cell Team Gamification):* Xây dựng các trang microsite sự kiện Tết truyền thống Lắc Xì, đóng vai trò làm trang hướng dẫn, công bố giải thưởng và điều hướng người dùng ngoài App vào tham gia game chính thức In-App.
*   *Tăng trưởng New User (Cell Team User Growth - Huy Lê phụ trách):* Khai thác cấu phần Landing Page Builder của MoSpark để nhanh chóng xuất bản và tối ưu hóa các trang chiến dịch thu hút khách hàng mới, tích hợp tracking W2A phục vụ mục tiêu tăng trưởng lượt tải App và đăng ký tài khoản mới từ organic web traffic.

Khác biệt cốt lõi của các Mini Web truyền thông này so với các dự án Product-Led Growth (PLG) là **không gán các cam kết tăng trưởng số cứng** (như số lượt tải app, số lượng giao dịch hay user active mới). Thay vào đó, chúng tập trung vào tính toàn vẹn dữ liệu, giao diện tối giản thân thiện, thời gian phản hồi siêu tốc nhằm truyền tải thông tin chính thống và xây dựng niềm tin số lâu dài (Trust-led Growth).


---

## 3. Danh Mục Các Dự Án Tăng Trưởng (Growth Projects Portfolio)
Các dự án tăng trưởng số (PLG Projects) được triển khai trên kênh Web tập trung giải quyết các Job-to-be-Done (JTBD) cốt lõi của người dùng, làm phễu chuyển đổi dẫn dòng lưu lượng ngoài app (Web Platform) vào giao dịch và đăng ký dịch vụ trong App. Danh mục dự án được phân chia thành hai loại hình quản trị và chịu trách nhiệm:

### 3.1. Các Dự Án Web Platform Đồng Chịu Trách Nhiệm Chính

#### 3.1.1. Tra cứu Phạt Nguội
*   **Trạng thái:** Đang hoạt động (Phase 1 Live / Phase 2 Scaling)
*   **Định hướng chiến lược & Cập nhật mới:**
    *   *Định vị Chiến lược:* Dự án Phạt Nguội được xác định là case study mẫu điển hình cho mô hình Product-Led Growth (PLG) trên Web Platform. Phạt Nguội đóng vai trò "phễu gom người dùng" (Governance & Acquisition) để dắt dòng lưu lượng ngoài app (Non-MoMo Users) vào hệ sinh thái MoMo, không định hình làm nguồn doanh thu Web trực tiếp.
    *   *Nội dung đã triển khai (Phase 1):*
        *   Tích hợp thành công API dữ liệu thời gian thực official từ Trung tâm Đăng Kiểm Việt Nam (TTDK) và Cục Cảnh sát Giao thông (CSGT).
        *   Tích hợp bản đồ camera giao thông tương tác (Interactive Camera Map) giúp người dùng xác định các điểm nóng giám sát giao thông trực quan.
        *   Triển khai gói Subscription cảnh báo phạt nguội tự động định kỳ (gói Năm 29.000đ hoặc dùng thử 7 ngày) giúp giữ chân người dùng.
        *   Xây dựng luồng liên kết chéo động (Contextual Violation Guide Flow): Khi người dùng có lỗi vi phạm, hệ thống tự động bóc tách mã lỗi và hiển thị trực tiếp bài blog hướng dẫn chi tiết của lỗi đó (mức phạt Nghị định 168, cách xử lý) ngay tại màn hình kết quả Web.
        *   Triển khai chiến dịch Off-page trị giá 75 triệu đồng cùng SEO Mentor và trao đổi liên kết (backlink exchange) trực tiếp từ các trang đăng kiểm đối tác.
    *   *Lộ trình tiếp theo (Phase 2):* Triển khai pSEO quy mô lớn cho 63 tỉnh thành (Location Scale Up) bằng layout trang địa phương tối ưu hóa đường truyền vi phạm, và tăng tốc sản xuất nội dung blog hỗ trợ (Batch 2).
*   **Cam kết KPI cốt lõi (KPI Commit):** *Top 3 Google Search Ranking* cho các từ khóa chính (như *"tra cứu phạt nguội"*, *"phạt nguội"*), chỉ số *Monthly Engagement Users (MEU)* (lượt tương tác qua widget tra cứu/lưu xe), tỷ lệ chuyển đổi *Web-to-App (W2A)* thông qua link thông báo tự động, và tỷ lệ người dùng mới dịch vụ (*% New to Services*).

#### 3.1.2. eSIM Du Lịch
*   **Trạng thái:** Đang hoạt động (Phase di chuyển)
*   **Định hướng chiến lược:** Di chuyển microsite sang MoSpark để đón đầu 50.8K search volume/tháng từ khách quốc tế.
*   **Cam kết KPI cốt lõi (KPI Commit):** *eSIM Transactions & Revenue* (Số lượng giao dịch mua eSIM thành công và doanh thu tương ứng).

#### 3.1.3. Tiện ích Giao thông (Vehicle Hub)
*   **Trạng thái:** Đang tiến hành
*   **Định hướng chiến lược:** Dự án đồng sở hữu cùng VTTI (ePass) nhằm quản lý phương tiện toàn diện qua biển số xe.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Monthly Active Vehicles (MAV)* (Số lượng xe có phát sinh ít nhất một meaningful action trên hệ thống) và *Service Attach Rate per Vehicle* (Số lượng dịch vụ đính kèm trên mỗi đầu xe).

#### 3.1.4. Cinema (Vé xem phim)
*   **Trạng thái:** Hoạt động (Hoàn thành Phase 1)
*   **Định hướng chiến lược:** Nhúng widget lịch chiếu và đặt vé.
*   **Kết quả H1/2026 (Actual):**
    *   *Organic Traffic:* Đạt **2,010,041 clicks** (GSC), chiếm 37.77% tổng clicks của `momo.vn`.
    *   *W2A Users:* Đạt **38,079** người dùng mở app qua CTA Web (giảm -30.3%).
    *   *W2A Conversion Rate (W2A Users / Booking Clicks):* Đạt **4.37%** (tính trên **870,467 Booking Clicks** thực tế ghi nhận trên Dashboard [Q1: 81,517; Q2: 788,950]).
    *   *Transactions:* Đạt **48,830** giao dịch mua vé thành công (giảm -27.0%).
    *   *Tickets Sold:* Đạt **107,146** vé xem phim bán ra (giảm -27.9%).
*   **Cam kết KPI cốt lõi (KPI Commit):** *Transactions (Số vé xem phim bán ra)* từ `/cinema/*`.

#### 3.1.5. Bảo hiểm Ô tô
*   **Trạng thái:** Đang hoạt động
*   **Phân vai trách nhiệm:** **Media Team tham gia cùng Midas và hỗ trợ tối ưu hóa** (Web Platform đồng chịu trách nhiệm chính).
*   **Định hướng chiến lược & Cập nhật mới:**
    *   *Revamp Miniweb BHOTO:* Cải tiến cấu trúc trang và nội dung bám sát các từ khóa chính ("bảo hiểm thân vỏ ô tô", "giá bảo hiểm thân vỏ ô tô"). Tích hợp trực tiếp hiển thị ưu đãi giảm phí khi đăng ký qua MoMo và bổ sung nhiều hình thức thanh toán.
    *   *Mở rộng User Intent:* Xây dựng hệ thống 1.537 sub-pages chuyên sâu theo từng hãng xe/dòng xe cụ thể (như bảo hiểm thân vỏ VF8...) và thương hiệu nhà bảo hiểm đối tác (Bảo Việt, PVI...) kết hợp tính năng so sánh phí bảo hiểm nhanh.
    *   *Tối ưu hóa Nội dung:* Điều chỉnh thứ tự ưu tiên của 72 bài viết hiện tại để củng cố thứ hạng trên Google Search và kết quả Google AI Overview (AIO).
*   **Cam kết KPI cốt lõi (KPI Commit):** *Car Insurance Bundle Conversion Rate* (Tỷ lệ chuyển đổi mua bảo hiểm ô tô thông qua chương trình tặng 1 năm dịch vụ tra cứu phạt nguội).

#### 3.1.6. Merchant Detail Page
*   **Trạng thái:** Đang thử nghiệm (Pilot Live)
*   **Phân vai trách nhiệm:** **Web Platform phụ trách chính** (PIC Build: Nhật & Hoài Anh; GPD - Web Platform làm Owner).
*   **Định hướng chiến lược:** Xây dựng sự hiện diện O2O tích hợp Ví Trả Sau, Soundbox để đón đầu organic search intent ngoài app ("{quán} có nhận ví trả sau không") và tạo digital presence cho các hộ kinh doanh SME.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Local Organic Search Impressions* và *Google Maps click-through rate (CTR)*.


### 3.2. Các Dự Án Do Media Team Triển Khai (Web Platform Phối Hợp, Theo Dõi & Kiểm Soát)

#### 3.2.1. Ví Trả Sau (BNPL)
*   **Trạng thái:** Đang hoạt động
*   **Phân vai trách nhiệm:** **Media Team phụ trách chính (incharge chính)** phối hợp cùng Web Platform & Content BMC.
*   **Định hướng chiến lược & Cập nhật mới:**
    *   *Mục tiêu Chiến dịch:* Đạt Top-of-Mind (TOM) 50% vào tháng 6/2026.
    *   *Mục tiêu SEO:* Bảo vệ và tăng SOV (Share of Voice) trên 3 thị trường: thị trường Trả Sau (tăng từ 60% lên 75% SOV, bao phủ 550 từ khóa tiềm năng), thị trường Trả Góp (tăng từ 10% lên 70% SOV, bao phủ 269 từ khóa), và thị trường Tín Dụng (tăng từ 40% lên 60% SOV, bao phủ 3.600 từ khóa).
    *   *Cải tiến Miniweb VTS:* Cải thiện Scroll Depth và CTR (baseline cũ chỉ có 7,25% user click vào CTA) hướng tới sub-KPI tăng tỷ lệ chuyển đổi (CR) từ 7% lên 20% trong năm 2026 bằng cách tái cấu trúc UI/UX, làm nổi bật social proof và bổ sung kịch bản theo phân khúc người dùng (Sinh viên, Nhân viên văn phòng, Lao động tự do).
    *   *Công cụ Trả Góp (Installment Simulator):* Xây dựng Microsite hiển thị công cụ tính phí trả góp và số tiền cần góp theo số dư từ 2 triệu đến 20 triệu đồng; tận dụng cross-sell với chương trình Trả Góp Apple.
    *   *Trust Hub (Xử lý tin tiêu cực):* Xây dựng cụm bài viết đánh chặn và đẩy lùi các nội dung xấu liên quan đến việc "rút tiền ví trả sau" trên Google Search để bảo vệ người dùng.
    *   *Quy mô Nội dung:* Lên kế hoạch sản xuất từ 50 đến 100 bài blog chất lượng cao.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Activated VTS Users from Web* (Đo lường lượng người dùng lần đầu kích hoạt thành công Ví Trả Sau trên App MoMo có nguồn gốc từ organic web, đối soát trong vòng 7 ngày kể từ lần truy cập đầu tiên).

#### 3.2.2. Vay Nhanh
*   **Trạng thái:** Đang tiến hành
*   **Phân vai trách nhiệm:** **Media Team phụ trách chính (incharge chính)** phối hợp cùng Web Platform.
*   **Định hướng chiến lược & Cập nhật mới:**
    *   *Mục tiêu Chiến dịch:* Xây dựng ToM (Top of Mind) và sự cân nhắc sớm cho nhóm 80% người dùng chưa phát sinh nhu cầu vay ngay lập tức. Đạt bao phủ 50% SOV thị trường (không gồm nhu cầu vay trên 100 triệu và từ khóa thương hiệu đối thủ) và xếp hạng tối thiểu 20% từ khóa trong Top 5 Google Search.
    *   *Cải tiến Miniweb & Trải nghiệm:* Khắc phục lỗi hiển thị lặp đi lặp lại 4 review (trong khi có 8 slot) bằng cách điều chỉnh review thành 1 dòng. Đẩy phần nội dung dài (long content) lên trước phần blog để công cụ tìm kiếm Google crawl sớm hơn. Tối ưu hóa nút CTA để đạt mục tiêu tăng 15% click Web-to-App so với H1/2025.
    *   *Tối ưu hóa Kỹ thuật (Technical SEO):* Bổ sung các thẻ structured data quan trọng (LoanOrCredit schema, FAQPage schema, BreadcrumbList schema, Organization schema với thông tin giấy phép NHNN). Sửa lỗi hiển thị thẻ Copyright từ năm 2019 thành năm 2026 (hoặc 2016) để củng cố tín hiệu tin cậy (trust signal).
    *   *Nội dung chuẩn YMYL (E-E-A-T):* Audit toàn bộ 30 bài blog hiện có, bổ sung khung tác giả (chuyên gia tài chính uy tín), bổ sung trích dẫn các nguồn thông tư/luật của Ngân hàng Nhà nước và đính kèm disclaimer tài chính chuẩn ở cuối mỗi bài viết.
    *   *SEO Offpage:* Triển khai disavow các spam link tấn công và đa dạng hóa neo liên kết (anchor text) từ đối tác thay vì chỉ dùng brand name thuần túy.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Clicks to App (W2A) & Loan Registrations* (Số lượng click chuyển đổi sang app và số lượt hoàn tất đăng ký vay thành công qua widget Loan Calculator).

#### 3.2.3. Tra cứu Điểm Tín Dụng (CIC)
*   **Trạng thái:** Pending
*   **Định hướng chiến lược:** Xây dựng widget tra cứu và mô phỏng điểm tín dụng (CIC Simulator) làm PLG hook trên web.
*   **Cam kết KPI cốt lõi (KPI Commit):** *CIC Check Volume & Ví Trả Sau Cross-sell Conversion Rate* (Lượng tra cứu điểm tín dụng ẩn danh và tỷ lệ chuyển đổi bán chéo thành công sang Ví Trả Sau).

#### 3.2.4. Bảo hiểm Y tế (BHYT)
*   **Trạng thái:** Đang hoạt động
*   **Phân vai trách nhiệm:** **Media Team tham gia cùng Midas và hỗ trợ tối ưu hóa**.
*   **Định hướng chiến lược & Cập nhật mới:**
    *   *Mục tiêu Giai đoạn 1 (Tối ưu Ý định Tìm kiếm):* Bổ sung các trang tiện ích con có lượt tìm kiếm tự nhiên cao bao gồm: Trang tra cứu số thẻ BHYT bằng CCCD (search volume ~18,100), Trang tra cứu mã số BHYT (~12,100), và Trang thời hạn đóng/mua BHYT (~25,000).
    *   *Mục tiêu Giai đoạn 2 (Danh bạ Bệnh viện):* Xây dựng danh bạ tích hợp thông tin của hơn 500 bệnh viện tuyến tỉnh và cấp chuyên sâu trên cả nước để kéo traffic tự nhiên.
    *   *Quy mô Nội dung & Lưu lượng:* Đăng tải từ 60 đến 150 bài blog/năm để cover 20% đến 40% dung lượng thị trường. Đặt mục tiêu Traffic Web (Views) đạt 120.662 lượt (Base Case) và kỳ vọng tối đa đạt 452.294 lượt (Best Case).
    *   *Ngân sách SEO Offpage:* Dự chi ngân sách đi backlink từ 300 triệu đến 500 triệu đồng/năm, đồng bộ thời điểm chạy các chiến dịch SEM.
*   **Cam kết KPI cốt lõi (KPI Commit):** *BHYT Online Purchase & Renewal Transactions* (Số lượng giao dịch mua mới và gia hạn BHYT thành công qua Web).

#### 3.2.5. Bảo hiểm xe máy (BHXM)
*   **Trạng thái:** Đang tiến hành
*   **Phân vai trách nhiệm:** **Media Team tham gia cùng Midas và hỗ trợ tối ưu hóa**.
*   **Định hướng chiến lược & Cập nhật mới:**
    *   *Khôi phục Lưu lượng:* Tập trung khắc phục đà sụt giảm organic traffic (hiện tại đạt khoảng 4.000 views vào tháng 5 so với mốc lịch sử).
    *   *Kế hoạch Đi link (Backlink Plan):*
        *   *Option 1 (Ngân sách 330 triệu đồng/năm):* Đưa 4/10 từ khóa mục tiêu vào Top 1-3 và 5/10 từ khóa vào Top 3-5 Google Search.
        *   *Option 2 (Ngân sách 450 triệu đồng/năm):* Đưa 5/10 từ khóa vào Top 1-3 và 7/10 từ khóa vào Top 3-5 Google Search.
        *   *Hạng mục triển khai:* Phân phối 15-20 bài viết Guest Post, 20-35 bài PR trên các báo tỉnh và mua 2 textlink trỏ về landing page chính `https://www.momo.vn/bao-hiem-xe-may`.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Motorcycle Insurance Purchase Volume* (Số đơn bảo hiểm xe máy xuất bản thành công qua web).

#### 3.2.6. Dịch Vụ Công MoMo
*   **Trạng thái:** Đang tiến hành
*   **Định hướng chiến lược:** Tích hợp cổng thanh toán trực tiếp ePass/ETC và công cụ tương tác Smart DVC Checklist Generator.
*   **Cam kết KPI cốt lõi (KPI Commit):** *MEU Utility on Web* (Lượt tương tác qua Checklist TTHC trên Web) và *MAU % New to services on App* (Tỷ lệ giao dịch ePass mới phát sinh thành công).

#### 3.2.7. Viễn Thông (Telco)
*   **Trạng thái:** Đang hoạt động
*   **Định hướng chiến lược:** Phân loại và định tuyến traffic ẩn danh theo Search Intent.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Web-to-Transaction (Telco)* (Số giao dịch viễn thông được ghi nhận qua organic web).

#### 3.2.8. Trust - Báo Cáo Lừa Đảo
*   **Trạng thái:** Đang hoạt động
*   **Định hướng chiến lược:** Mở rộng cổng tiếp nhận báo cáo lừa đảo cộng đồng ẩn danh.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Số lượng báo cáo lừa đảo ẩn danh tiếp nhận thành công trên Web*.

#### 3.2.9. Vé xe khách (OTA - BUS)
*   **Trạng thái:** Đang tiến hành
*   **Định hướng chiến lược:** pSEO các trang Routes và Bus Operators.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Transactions (Số vé xe khách bán thành công)* được ghi nhận qua Appsflyer.

#### 3.2.10. Soundbox
*   **Trạng thái:** Đang tiến hành
*   **Định hướng chiến lược:** Landing page đặt hàng thiết bị Soundbox cho SME offline.
*   **Cam kết KPI cốt lõi (KPI Commit):** *Web Order Volume* (Số lượng Soundbox đặt hàng thành công qua Web).

#### 3.2.11. Destination Promotion Hub (MoMo Travel)
*   **Trạng thái:** Đang tiến hành
*   **Phân vai trách nhiệm:** **Media Team phụ trách triển khai chính** dưới sự phối hợp, theo dõi và kiểm soát hạ tầng của Web Platform (Cell Team OTA MoMo Travel và Cell Team Telco/Fintech cùng tham gia).
*   **Định hướng chiến lược & Cập nhật mới:**
    *   *Mục tiêu Chiến dịch:* Xây dựng cổng thông tin tích hợp Web & In-App (Cổng Destination Hub - Cổng thông tin du lịch quốc tế Outbound) giúp người dùng lên kế hoạch hành trình du lịch tự túc nước ngoài (Thái Lan, Singapore, Nhật Bản, Đài Loan...) trọn gói trong 3 phút.
    *   *Chiến lược Cross-sell:* Hợp nhất bán chéo chuỗi dịch vụ Outbound: Vé máy bay quốc tế, Đặt phòng khách sạn (Agoda), eSIM du lịch (Gohub) và hướng dẫn cổng thanh toán QR quốc tế (PromptPay Thái Lan, NETS Singapore...) với tỷ giá quy đổi ưu đãi.
    *   *Cập nhật Onpage:* Xây dựng Landing Page chuyên biệt theo điểm đến (Destination-specific template) tối ưu hóa qua CMS, tích hợp Widget tính toán tỷ giá ngoại tệ real-time để thu hút traffic tự nhiên.
*   **Cam kết KPI cốt lõi (KPI Commit):** Đạt trên 250.000 Pageviews/tháng cho Hub Web, tỷ lệ chuyển đổi Web-to-App (W2A CR) > 12%, tỷ lệ bán chéo sản phẩm (Cross-sell Rate) > 15% khách mua vé máy bay quốc tế sẽ mua kèm eSIM hoặc Khách sạn.


