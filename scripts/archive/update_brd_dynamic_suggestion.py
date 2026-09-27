with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    brd = f.read()

target = "### 5.2 Cơ Chế Điều Hướng Trọng Tâm Đến 3 Sản Phẩm FinHub (Driven-Traffic Engine)"
insertion = """### 5.2.1 Quy Chuẩn "MoMo Gợi Ý (AI)" Cá Nhân Hóa Theo Hành Vi Nhập (Dynamic Rule Engine)

Khối **MoMo Gợi Ý** tuyệt đối không sử dụng câu chữ tĩnh (Static Text), mà vận hành bằng **Động cơ Phân tích Ngữ cảnh Thời gian thực (Client-side Dynamic Rule Engine)**: Text gợi ý tự động thay đổi tức thì (Reactive UI / Debounce 150ms) khớp chính xác với từng mốc giá trị mà người dùng vừa nhập vào công cụ.

#### Ma Trận Phân Tầng Gợi Ý Mẫu Cho Công Cụ Tính Lương:
1. **Phân khúc Thu nhập Khởi điểm (< 11 triệu/tháng - Chưa chịu thuế TNCN):**
   - *Logic:* Lương thực nhận = Lương Gross trừ BHXH (10.5%). Thuế TNCN = 0đ do dưới mức giảm trừ gia cảnh 11 triệu.
   - *Câu gợi ý động:* "Với mức lương [10 triệu]/tháng, bạn chưa phải nộp thuế TNCN. Mẹo tối ưu: Hãy trích ngay [2 triệu] (20%) vào Túi Thần Tài để sau 1 năm tích lũy được quỹ dự phòng khẩn cấp [24 triệu] có sinh lời mỗi ngày."
   - *Icon ưu tiên:* Túi Thần Tài, Hũ Chi Tiêu.

2. **Phân khúc Thu nhập Trung bình - Khá (15 - 30 triệu/tháng - Chịu thuế bậc 1 & 2):**
   - *Logic:* Bắt đầu phát sinh thuế TNCN từ vài trăm ngàn đến 2-3 triệu/tháng. Đã có thặng dư tài chính tích lũy.
   - *Câu gợi ý động:* "Với mức lương [30 triệu]/tháng, bạn đang nộp khoảng [2.15 triệu] tiền thuế TNCN. Dòng tiền thặng dư sau sinh hoạt ước đạt [9 triệu]/tháng. Mẹo tối ưu: Chia [6 triệu] vào Tiết Kiệm Online Bản Việt/VPBank nhận lãi suất cao và [3 triệu] vào Thực Tập Sinh Đầu Tư để gia tăng tài sản dài hạn."
   - *Icon ưu tiên:* Tiết Kiệm Online, Thực Tập Sinh Đầu Tư, Thẻ Tín Dụng Hoàn Tiền.

3. **Phân khúc Thu nhập Cao (> 40 triệu/tháng - Chịu thuế bậc 3 trở lên):**
   - *Logic:* Chịu thuế suất biên cao (20% - 35%). Nhu cầu quản trị thuế, tối ưu chi phí và đầu tư đa kênh.
   - *Câu gợi ý động:* "Với mức lương [50 triệu]/tháng, bạn đang đóng [6.4 triệu] tiền thuế TNCN mỗi tháng. Mẹo tối ưu: Hãy khai báo tối đa người phụ thuộc hợp lệ để giảm trừ thuế, đồng thời phân bổ 40% dòng tiền thặng dư vào danh mục tích sản cân bằng (50% Tiết Kiệm an toàn + 50% Quỹ Mở tăng trưởng)."
   - *Icon ưu tiên:* Thực Tập Sinh Đầu Tư Quỹ Mở, Tiết Kiệm Kỳ Hạn Lớn, Báo Cáo CIC Hạng Cao.

"""

if target in brd and "Quy Chuẩn \"MoMo Gợi Ý (AI)\" Cá Nhân Hóa Theo Hành Vi Nhập" not in brd:
    brd = brd.replace(target, target + "\n\n" + insertion)
    with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
        f.write(brd)
    print("Successfully updated BRD with Dynamic Suggestion Rule Engine!")
else:
    print("Already exists or target not found.")
