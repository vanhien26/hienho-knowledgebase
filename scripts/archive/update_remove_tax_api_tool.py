import openpyxl

wb = openpyxl.load_workbook('05_HUBS/financial-hub-roadmap.xlsx')
ws_rd = wb['Roadmap']

for r in range(3, ws_rd.max_row + 1):
    feat_name = str(ws_rd.cell(row=r, column=4).value or '').strip()
    if 'Tính Lương & Thuế TNCN' in feat_name:
        ws_rd.cell(row=r, column=5).value = (
            "• Công cụ tính lương Gross - Net 2026 (Pure Client-side JS, không phụ thuộc API ngoài): Cập nhật mức đóng BHXH tối đa, BHYT, BHTN và mức giảm trừ gia cảnh 11tr/4.4tr.\n"
            "• Bộ Dự Toán Thuế TNCN Lũy Tiến 7 Bậc: Tự động tính tiền thuế phải nộp theo tháng và dự toán quyết toán thuế cả năm.\n"
            "• Hướng dẫn quy trình tra cứu Mã Số Thuế cá nhân chính thống qua Cổng Tổng Cục Thuế (gdt.gov.vn / App eTax Mobile).\n"
            "• Gợi ý 3 Hero Products: Trích 20% gửi Tiết Kiệm TKO | Trích 10% tham gia Thực Tập Sinh Đầu Tư | Kiểm tra CIC."
        )
        ws_rd.cell(row=r, column=6).value = (
            "Sau khi tính Lương Net & Thuế: 3 nút CTA trực tiếp 'Mở Sổ Tiết Kiệm Bản Việt / VPBank' | 'Tích Sản Quỹ Mở SIP Chỉ Từ 10k' | 'Kiểm Tra Điểm Tín Dụng CIC'."
        )
        ws_rd.row_dimensions[r].height = 70.0

wb.save('05_HUBS/financial-hub-roadmap.xlsx')
print("Successfully removed Tax ID API lookup dependency from Roadmap!")
