# QUY CHUẨN THIẾT KẾ ĐỘNG CƠ VIẾT LẠI VĂN BẢN (PARAPHRASE RULES SSOT)

Tài liệu này định nghĩa Single Source of Truth (SSOT) cho toàn bộ quy tắc viết lại văn bản, tối ưu hóa câu từ, chống phát hiện AI (Humanize) và bảo vệ thực thể SEO trên Nền tảng Web MoMo.

Được đồng bộ trực tiếp sang Web Hubs tại: `lib/content-plan/paraphrase-engine.ts` và API endpoint `/api/paraphrase`.

---

## 1. QUY CHUẨN CHẾ ĐỘ VIẾT LẠI (MODE SPECIFICATIONS)

| Chế độ (Mode) | Mục tiêu cốt lõi | Quy tắc hành văn bắt buộc |
| :--- | :--- | :--- |
| **Tiêu chuẩn (`standard`)** | Làm câu văn mạch lạc, dễ hiểu, bảo toàn 100% ngữ nghĩa gốc. | Giữ nguyên đại từ nhân xưng; sắp xếp lại trật tự chủ ngữ - vị ngữ; tinh giản câu rườm rà. |
| **SEO (`seo`)** | Bảo toàn từ khóa hạt giống và cấu trúc thẻ đề mục cho Google Search. | BẢO TOÀN TUYỆT ĐỐI các thẻ Heading (`# H1`, `## H2`, `### H3`), từ khóa mục tiêu, bảng biểu dữ liệu Markdown và liên kết nội bộ. Không làm giảm mật độ từ khóa. |
| **Bài viết (`article`)** | Tái cấu trúc thành bài viết chuyên sâu dạng phóng sự / cẩm nang. | Giữ nguyên dàn ý bài viết; chia nhỏ các đoạn văn dài thành từng khối 2-3 câu thoáng đãng; chuyển đổi số liệu phức tạp thành danh sách gạch đầu dòng. |
| **Humanize (`humanize`)** | Phá vỡ cấu trúc máy móc của AI, vượt qua các bộ lọc phát hiện AI. | **Tăng Burstiness:** Xen kẽ câu cực ngắn (3-6 từ) và câu ghép dài (20-30 từ).<br>**Tăng Perplexity:** Dùng từ nối tự nhiên của tiếng Việt (*thực tế là*, *nói cách khác*, *mặt khác*).<br>**Loại bỏ sáo rỗng AI:** Cấm tuyệt đối các từ sáo rỗng kinh điển. |

---

## 2. QUY CHUẨN GIỌNG ĐIỆU (TONE SPECIFICATIONS)

* **Tiêu chuẩn (`standard`):** Chuẩn mực, trung tính, khách quan, tự nhiên.
* **Trôi chảy (`fluent`):** Uyển chuyển, nhịp nhàng, câu từ liền mạch, hạn chế lặp từ.
* **Trang trọng (`formal`):** Chuẩn văn phong doanh nghiệp, tài chính, pháp lý; lịch thiệp và đáng tin cậy.
* **Đơn giản (`simple`):** Bình dân, dễ hiểu với đại chúng, giải thích trực diện, tránh thuật ngữ Hán-Việt phức tạp.
* **Sáng tạo (`creative`):** Giàu hình ảnh, lôi cuốn, khơi gợi cảm xúc, phù hợp tiếp thị số và mạng xã hội.
* **Học thuật (`academic`):** Nghiêm cẩn, dẫn luận chặt chẽ, khách quan, không dùng đại từ cảm tính chủ quan.

---

## 3. THANG ĐO CƯỜNG ĐỘ (INTENSITY & TEMPERATURE FORMULA)

Công thức ánh xạ giữa Cường độ trên Slider (1 đến 5) sang `temperature` của mô hình LLM:

$$\text{Temperature} = 0.2 + (\text{Intensity} - 1) \times 0.18$$

* **Cường độ 1 (Nhẹ) - Temp `0.2`:** Chỉ sửa lỗi ngữ pháp, chính tả, dấu câu; thay đổi dưới 15% từ ngữ.
* **Cường độ 2 (Vừa) - Temp `0.38`:** Thay thế một số từ đồng nghĩa phù hợp; giữ nguyên 85-90% cấu trúc câu.
* **Cường độ 3 (Cân bằng) - Temp `0.56`:** Đảo vị trí mệnh đề, diễn đạt lại tự nhiên; thay đổi 35-50% cấu trúc câu.
* **Cường độ 4 (Mạnh) - Temp `0.74`:** Viết lại toàn diện các câu, sử dụng góc nhìn mới mẻ hơn; thay đổi 60-80% cách diễn đạt.
* **Cường độ 5 (Tối đa) - Temp `0.92`:** Tái cấu trúc triệt để văn bản, đổi mới hoàn toàn cách hành văn nhưng bảo toàn thông điệp cốt lõi.

---

## 4. TỪ ĐIỂN TỪ SÁO RỖNG CỦA AI CẦN LOẠI BỎ (ANTI-AI-SLOP LEXICON)

Toàn bộ các cụm từ sau đây bị cấm xuất hiện trong đầu ra của công cụ:

| Cụm từ AI sáo rỗng | Thay thế chuẩn mực trên Nền tảng Web MoMo |
| :--- | :--- |
| *bứt phá ngoạn mục* | phát triển mạnh / tăng trưởng rõ rệt |
| *khẳng định vị thế uy tín* | xây dựng độ tin cậy / nâng cao uy tín |
| *hành trình chuyển đổi* | quá trình thay đổi / lộ trình nâng cấp |
| *bệ phóng phát triển* | nền tảng hỗ trợ / cơ sở thúc đẩy |
| *đóng vai trò then chốt* | rất quan trọng / mang tính cốt lõi |
| *trong bối cảnh ngày nay* | hiện nay / trong giai đoạn này |
| *không ngừng nỗ lực* | luôn tập trung / duy trì cải tiến |
| *giải pháp toàn diện* | giải pháp đầy đủ / dịch vụ trọn gói |

---

## 5. CƠ CHẾ BẢO VỆ THỰC THỂ (ENTITY MASKING PROTOCOL)

1. **Trước khi xử lý:** Trích xuất mảng `protectedKeywords` từ người dùng kết hợp với danh sách thực thể lõi của MoMo (`MoMo`, `Ví trả sau`, `Túi Thần Tài`, `CIC`, `eKYC`, `NHNN`, `BVBank`, `TPBank`...).
2. **Mã hóa thành Token:** Thay thế các từ khóa thành token `[[P_ENT_0]]`, `[[P_ENT_1]]`... theo thứ tự độ dài giảm dần (tránh nuốt từ khóa con).
3. **Chỉ thị mô hình AI:** Ép LLM giữ nguyên 100% vị trí và tên gọi của token `[[P_ENT_x]]`.
4. **Giải mã (Unmasking):** Sau khi nhận kết quả, khôi phục toàn bộ token về chính xác từ khóa ban đầu.
