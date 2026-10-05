# BÁO CÁO TỔNG QUAN THÁNG 09/2026 - VEHICLE HUB

- **Target chiến lược:** Xây dựng Cổng tiện ích giao thông toàn diện (`momo.vn/tien-ich-giao-thong`), đóng vai trò đầu phễu thu hút lưu lượng Intent Search về xe cơ giới, phạt nguội và bảo hiểm.
- **Thực tế Tháng 9 (MTD 27d):** Đạt **61.907 PVs**, ghi nhận sự hồi phục mạnh mẽ từ cuối tháng và tập trung chuyển dịch sang đa dạng hóa hạ tầng tiện ích giao thông.

---

## I. KEY HIGHLIGHTS & BUSINESS IMPACT

- **Khai thác 3 dạng sản phẩm cốt lõi cho Vehicle Hub:**
  - **Mô-đun Widget đa dạng kích thước (Embeddable Widget Components):** Thiết kế linh hoạt các size UI (Large, Medium, Small) để nhúng trực tiếp Bảng giá xăng dầu thời gian thực vào các bài viết cẩm nang và trang liên quan.
  - **Bản đồ tra cứu địa điểm tương tác (Interactive Location Maps):** Tích hợp bản đồ hiển thị chi tiết các điểm dịch vụ giao thông (Bản đồ Cây xăng, Trạm sạc EV VinFast/V-Green, Tìm Garage sửa xe).
  - **Bộ công cụ tính toán dịch vụ (Interactive Calculators):** Xây dựng công cụ Tính tiền xăng dầu thông minh, quy đổi số tiền/lít xăng ra quãng đường di chuyển ước tính cho xe máy và ô tô.
- **Khôi phục và tối ưu đà tăng trưởng Phạt Nguội:** Sau sự cố kỹ thuật ngắt kết nối API tạm thời từ ngày 01/09 đến 20/09 làm ảnh hưởng ngắn hạn đến traffic, luồng API Phạt Nguội đã chính thức được khôi phục từ 21/09, kéo nhịp truy cập tra cứu phạt nguội hồi phục nhanh chóng về mức trung bình toàn sàn.
- **Tập trung hóa Master Hub Giao Thông:** Hoàn thiện và vận hành ổn định Master Hub `momo.vn/tien-ich-giao-thong` quy tụ chuỗi tiện ích cốt lõi bao gồm Giá xăng, Trạm sạc EV, Cây xăng và Thu phí không dừng ePass (bắt đầu ghi nhận lượt truy cập tự nhiên đầu tiên).
- **Hoàn thành Staging Tiện ích Mới:** Đưa thành công chuyên trang Tìm Garage (`/tien-ich-giao-thong/tim-garage`) lên môi trường Staging, sẵn sàng Go-live chính thức trước ngày 30/09.
- **Tự chủ Nội dung PLG qua GenAI Pipeline:** Tự chủ 100% quy trình sản xuất bài viết cẩm nang giao thông, phạt nguội, đăng kiểm và hạ tầng trạm sạc thông qua hệ thống GenAI Content Pipeline.
- **Kích hoạt Ngân sách Paid Ads 550 triệu cho Bảo Hiểm Ô Tô:** Phối hợp cùng InsurTech BU triển khai chuyên mục Blog Bảo Hiểm Ô Tô (duy trì mức ~3.200 - 3.800 PVs/tháng organic) và chuẩn bị chạy phễu acquire New User thuộc gói ngân sách Paid Ads 550 triệu VNĐ từ nay đến hết năm 2026.
- **Tái cấu trúc luồng phễu Phạt Nguội W2A:** Nhúng giao diện trả kết quả tra cứu Phạt nguội dạng khối Inline, nhúng trực tiếp CTA nộp phạt In-App và đăng ký gói thông báo tự động để tối ưu hiệu suất chuyển đổi Web-to-App.

---

## II. CROSS-TEAM COLLABORATION & SUPPORT NEEDED

- **InsurTech BU & Media Team:** Phối hợp tối ưu hóa hiệu quả phân bổ ngân sách Paid Ads 550 triệu VNĐ cho mảng Bảo Hiểm Ô Tô nhằm đảm bảo chỉ tiêu chuyển đổi tệp chủ xe U30-45.
- **VTTI BU & Data Analytics Team:** Đồng bộ 3 Google Sheets dữ liệu chuẩn hóa (Garage, Cây xăng, Trạm sạc) kết nối hạ tầng Apify giữa Web Platform và App.
- **Content Team & Legal/QC:** Duy trì quy trình kiểm duyệt Fact-check 100% tính chính xác của các bài viết luật giao thông và hoàn thiện bảng mapping mã lỗi vi phạm.

---

## III. PRIORITIES FOR THE NEXT 30 DAYS

- **Go-live trang Tìm Garage & Trạm Sạc VinFast:** Chính thức xuất bản chuyên trang Tìm Garage (`/tien-ich-giao-thong/tim-garage`) và Trạm Sạc VinFast tích hợp Location API trên Production trước ngày 30/09.
- **Tối ưu 3 dạng sản phẩm trên Master Hub:** Hoàn thiện đóng gói các Widget Component (bảng giá xăng), Location Detail Maps (bản đồ trạm sạc/cây xăng) và Calculator (tính tiền xăng/quãng đường đi được) để nhúng rộng rãi trên toàn bộ hệ thống bài viết SEO.
- **Duy trì ổn định luồng API Phạt Nguội:** Giám sát hạ tầng kỹ thuật đảm bảo Uptime cho luồng API tra cứu Phạt nguội, duy trì nhịp hồi phục traffic.
- **Tích hợp API Thời gian thực:** Hoàn thiện kết nối API Giá Xăng (Petrolimex/PVOil) cập nhật biến động giá xăng dầu real-time.
- **Đóng gói Component Captcha cho Bảo Hiểm:** Phối hợp với InsurTech Tech Team xử lý xong Captcha Module để đóng gói component mua Bảo hiểm Ô tô/Xe máy trực tiếp trên Web.
- **Tối ưu phễu W2A trên trang Phạt Nguội:** Nhúng các Widget đăng ký gói nhận thông báo phạt nguội định kỳ và Cross-sell bảo hiểm vào trang kết quả tra cứu để đẩy mạnh tỷ lệ mở App MoMo.
