file_path = '/Users/hienhv/HienHv/Klaus/Hienho_MoMo-Base/05_HUBS/vehicle-hub-brd.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_text = """  * Danh mục 5 mặt hàng nhiên liệu: Xăng RON 95-III, RON 95-V, Xăng Sinh Học E5 RON 92-II, Dầu Diesel 0.05S-II, Dầu Hỏa."""

new_text = """  * Danh mục chuẩn hóa gồm 7 mặt hàng nhiên liệu chính thức niêm yết theo kỳ điều hành của Bộ Công Thương / Petrolimex / PVOil:
    1. **Xăng RON 95-V (Euro 5):** Xăng cao cấp nhất thị trường, tiêu chuẩn khí thải Mức 5 (hàm lượng lưu huỳnh <10 ppm), chuyên dụng cho xe sang, ô tô đời mới từ 2022 trở đi để bảo vệ động cơ và chống đóng cặn kim phun.
    2. **Xăng RON 95-III (Euro 3):** Loại xăng phổ biến nhất toàn quốc (chiếm >70% thị phần RON 95), dành cho ô tô phổ thông và toàn bộ các dòng xe máy tay ga (Vision, SH, Air Blade, Lead...).
    3. **Xăng Sinh Học E5 RON 92-II (Euro 2):** Xăng pha 5% cồn sinh học Ethanol E100, giá thành tiết kiệm, phù hợp cho xe máy số (Wave, Sirius) và tài xế xe công nghệ/taxi.
    4. **Dầu Diesel DO 0,001S-V (Euro 5):** Dầu diesel cao cấp đạt chuẩn Euro 5 (lưu huỳnh <10 ppm), bắt buộc dùng cho các dòng ô tô máy dầu thế hệ mới (Ford Everest/Ranger, Hyundai SantaFe, Kia Carnival, Isuzu D-Max...) để tránh nghẹt bộ lọc hạt khí xả (DPF) và hư kim phun điện tử.
    5. **Dầu Diesel DO 0,05S-II (Euro 2):** Dầu diesel thông dụng (lưu huỳnh <500 ppm), dùng cho xe tải thương mại, xe khách, máy nông cơ và công trình.
    6. **Dầu Hỏa (Kerosene):** Dầu dân dụng phục vụ nhu cầu đun nấu, nhiệt luyện và công nghiệp nhẹ.
    7. **Dầu Mazut 180CST 3.5S (FO):** Nhiên liệu đốt lò công nghiệp và động cơ tàu biển (niêm yết đơn vị tính VNĐ/kg).
  * *Lộ trình tương lai:* Sẵn sàng module hiển thị xăng **E10** (pha 10% Ethanol) theo đề án lộ trình chuyển đổi năng lượng xanh của Chính phủ."""

if old_text in content:
    content = content.replace(old_text, new_text)
    print("Found and replaced fuel types successfully.")
else:
    print("Old text not found!")
    exit(1)

# Update Change Log to v8.9
changelog_entry = """| **v8.9** | 2026-09-03 | Web Product Lead | **Cập Nhật Toàn Bộ Danh Mục Nhiên Liệu Mới Nhất:** Chuẩn hóa danh mục 7 mặt hàng xăng dầu theo biểu giá điều hành chính thức của Petrolimex/PVOil. Bổ sung dầu cao cấp DO 0,001S-V (Euro 5) bắt buộc cho ô tô máy dầu đời mới, phân định rõ chuẩn Euro 5 và Euro 2/3 (RON 95-V vs RON 95-III), dầu Mazut và sẵn sàng cho xăng sinh học E10. |
"""
content = content.replace('| **v8.8**', changelog_entry + '| **v8.8**', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated BRD Change Log v8.9 successfully.")
