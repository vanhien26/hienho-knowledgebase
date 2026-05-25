# 🏛️ Decision Log - MoMo Web Growth

Tài liệu này ghi lại các quyết định chiến lược (Fork Points) quan trọng trong quá trình phát triển dự án. Giúp đội ngũ hiểu được bối cảnh (Context) và lý do (Rationale) đằng sau mỗi quyết định.

---

## 📅 Log Quyết định

| Ngày | Dự án | Quyết định | Lý do (Rationale) | Người quyết định |
| 2026-05-21 | **Phạt Nguội** | Bỏ Smart Banner/Popup; thay bằng **Inline Lookup Widget** nhúng trong nội dung bài blog | Không phù hợp với trải nghiệm đọc blog và ngữ cảnh người dùng | Văn Hiến |
| 2026-05-19 | **Telecom** | Sử dụng **Intent-Based Audience Filtering** (Phân loại bằng Search Intent) | Bỏ qua giới hạn kỹ thuật không thể segment New/Current trên Web ẩn danh; gom nhóm keyword để gián tiếp xác định tệp khách hàng và phân phối trải nghiệm content/CTA tương thích. | Văn Hiến + Trang Phạm + Anh Bảo |
| 2026-05-14 | **Auto Insurance** | Không dùng geo-based URL clusters | Tránh pha loãng Topical Authority; tập trung vào JTBD cross-reference hiệu quả hơn cho mảng Bảo hiểm. | Văn Hiến |
| 2026-05-10 | **Technical SEO** | Sử dụng `Disallow: /*?` | Chặn crawl các URL tham số gây trùng lặp nội dung và lãng phí Crawl Budget. | Văn Hiến |
| 2026-04-20 | **MoSpark Platform** | Chuyển sang Claude API cho GenAI | Khả năng viết tiếng Việt tự nhiên hơn và tuân thủ tốt hơn các prompt phức tạp về YMYL. | Văn Hiến + Anh Bảo |
| 2026-04-15 | **Phạt Nguội** | Chọn mô hình Wise (pSEO) làm pilot | Phạt nguội có search volume cực lớn và tính chất dữ liệu phù hợp để tự động hóa hàng ngàn trang landing page. | Văn Hiến + Anh Công |
| 2026-04-10 | **Org Structure** | Anh Bảo làm Project Lead Out-App | Tăng cường sự kết nối giữa định hướng SEO/GEO và khả năng thực thi kỹ thuật của Web Platform. | Anh Công |

---

## 💡 Hướng dẫn sử dụng
1. Ghi lại mọi quyết định có ảnh hưởng đến cấu trúc hệ thống, ngân sách hoặc định hướng chiến lược.
2. Format: [Ngày] | [Dự án] | [Quyết định] | [Lý do] | [Owner].
3. Link đến các file BRD hoặc Meeting Log liên quan nếu cần.
