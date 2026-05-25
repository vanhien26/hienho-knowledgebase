---
title: Merchant Migration Tracker - SME Batch (Final List)
source: "[MEGA26] Potential list - Final list.csv"
last_updated: 2026-05-25
---

# Merchant Migration Tracker - SME Batch (Final List)

> **Nguồn:** `[MEGA26] Potential list - Final list.csv`
> **Tổng:** 35 unique merchants (36 rows - 1 duplicate)
> **Migration Flow:** MID + /page/{id} làm reference → tạo thủ công MoSpark → 308 Redirect
> **Last updated:** 2026-05-25

---

## ✅ AMBIGUITY ĐÃ GIẢI QUYẾT

| Vấn đề | Kết luận |
|--------|---------|
| Xôi bà cụ vs Xôi Trường | **CÙNG merchant.** Tên đầy đủ: "Xôi Trường Bà Ca" (Bắc Ninh). Slug: `xoi-ba-cu` |
| Mì xào giòn A Tỷ vs Bột chiên A Tỷ | **CÙNG merchant.** MID: MOMOMMPG20231114 (Đồng Nai). Quán bán cả 2 món. Tên CSV dùng: "Mì xào giòn A Tỷ" |
| Hải Sản Ngô Thơ - tỉnh nào? | **Hải Phòng** (theo CSV). Câu chuyện đề cập Bắc Ninh là sai/nhầm |
| Miến gà cô Nhẫn - tỉnh nào? | **HCM** - Gò Vấp (địa chỉ: 2 Phan Văn Trị, Phường 10, Gò Vấp) |

---

## ❌ ĐÃ LOẠI KHỎI SCOPE (Không có trong Final List CSV)

| Merchant | Tỉnh | Volume/tháng | Ghi chú |
|---------|------|:---:|---------|
| Hương Giang Bakery | Bắc Ninh | 320 | Không có trong CSV Final - Confirmed dropped |
| Bò Lá Lốt Mỡ Chài Chị Hằng | Bình Dương | 0 | Không có trong CSV Final - Confirmed dropped |
| Bún Cá Tư Lùn | An Giang | 0 | Không có trong CSV Final - Confirmed dropped |

---

## ⚠️ LƯU Ý QUAN TRỌNG

- **STT 3 bị thiếu** trong CSV (nhảy từ STT 2 → STT 4) - có thể merchant đã bị xóa. Cần confirm với team.
- **Hủ tiếu Mỹ Tho Thanh Xuân** có 2 MID: MOMOKGBT20230427 (STT 32) và không MID (STT 11). Cùng địa chỉ 62 Tôn Thất Thiệp, Q1. Có thể 1 merchant, 2 tài khoản MoMo. Cần verify với BD/Merchant team.
- **4 merchants có format "Tên chủ / Tên quán"**: Dùng tên quán cho content, tên chủ có thể mention trong phần Giới thiệu.
- **Câu chuyện Merchant (Story)** đã có sẵn trong CSV - đây là nguồn chính cho phần Long Content khi viết bài.

---

## MERCHANT TABLE - ĐẦY ĐỦ

**Legend:**
- 🟢 LIVE | 🔴 REDIRECT (có /page/ cũ) | ⚪ CLEAN | ❓ VERIFY
- **Story** = ✓ nếu có câu chuyện trong CSV (dùng làm source cho Long Content)
- **Template:** D = SME Basic (default)

| STT | MID | Tên Merchant | Tỉnh/TP | Địa chỉ | /page/ cũ | Slug đề xuất | Status | Story | Ghi chú |
|:---:|-----|-------------|---------|---------|----------|-------------|:------:|:-----:|---------|
| 1 | MOMOSNCN20260404 | Bánh Mì Hữu Liêm | Cần Thơ | 163 đường 30/4, Ninh Kiều | - | `banh-mi-huu-liem-{id}` | ⚪ | ✓ | Từ 1985 |
| 2 | MOMOGSOY20260206 | Quán Cơm Chú Lùn | Cần Thơ | 79 Đ. Phan Đăng Lưu, Ninh Kiều | - | `quan-com-chu-lun-{id}` | ⚪ | ✓ | Chú U70 vẫn bán |
| **3** | - | **MISSING** | - | - | - | - | ❓ | - | **STT 3 bị xóa khỏi CSV** |
| 4 | MOMOOG3N20240222 | Bánh Mì Khánh Nạp | Hải Phòng | 172 P. Hàng Kênh, Lê Chân | - | `banh-mi-khanh-nap-{id}` | ⚪ | ✓ | Nghệ sĩ Chí Trung review |
| 5 | MOMOH19P20260411 / MOMOUIMT20260415 | Bánh Ướt Cây Me | Cần Thơ | Chi 1: 31 Đồng Khởi; Chi 2: 138D Nguyễn Văn Cừ | - | `banh-uot-cay-me-{id}` | ⚪ | ✓ | 45+ năm, 2 cơ sở, 2 MID |
| 6 | MOMOUEWQ20260409 / MOMOLTAR20260508 | Cơm Tấm Ống Khói Diệu | An Giang | 200/4 Đặng Dung, Mỹ Long, Long Xuyên | - | `com-tam-ong-khoi-dieu-{id}` | ⚪ | ✓ | **P0 - 4.400/tháng.** Từ 2000, câu chuyện mẹ-con xúc động. 📝 Draft: `merchant-pages/com-tam-ong-khoi-dieu.md` |
| 7 | MOMOOZR420250704 | Trà Đá Mạnh Nháy | Bắc Ninh | (Không có trong CSV) | - | `tra-da-manh-nhay-{id}` | ⚪ | ✓ | Mẹ của tuyển thủ Levi Liên Minh Huyền Thoại |
| 8 | MOMO35G620260409 | Xôi Bà Cụ | Bắc Ninh | (Không có trong CSV) | - | `xoi-ba-cu-{id}` | ⚪ | ✓ | Tên đầy đủ: Xôi Trường Bà Ca. 47 năm, 3 thế hệ |
| 9 | MOMOWNXX20250121 | Hải Sản Ngô Thơ | Hải Phòng | (Không có trong CSV) | - | `hai-san-ngo-tho-{id}` | ⚪ | ✓ | 15+ năm, live TikTok 20K người xem |
| 10 | MOMOGKL020250927 | Cô Hường Bún Chả | Hải Phòng | 3 Phạm Minh Đức, Hải Phòng | - | `co-huong-bun-cha-{id}` | ⚪ | ✓ | SĐT: 0764667384 |
| 11 | *(xem STT 32)* | Hủ Tiếu Mỹ Tho Thanh Xuân | HCM | 62 Tôn Thất Thiệp, Q1 | - | `hu-tieu-my-tho-thanh-xuan-{id}` | ⚪ | ✓ | **DUPLICATE với STT 32.** 80 năm từ 1946. Michelin Street Food. Masan Chin-Su. 📝 Draft: `merchant-pages/hu-tieu-my-tho-thanh-xuan.md` - BLOCK: verify MID trước |
| 12 | MOMOJEE620220516 | Bún Thịt Nướng Chị Tuyền | HCM | 4 Cách Mạng Tháng 8, Q1 | /page/9819516 | `bun-thit-nuong-chi-tuyen-44` | 🟢 LIVE | ✓ | **ĐÃ LIVE.** Từ 1978. Đăng ký thương hiệu độc quyền |
| 13 | MOMOAKH820241017 | Tiệm Mì Chú Cao | HCM | 289 Hai Thượng Lãn Ông, Q5 | - | `tiem-mi-chu-cao-{id}` | ⚪ | ✓ | 40+ năm từ 1967. Người Hoa |
| 14 | MOMOUS7120241207 | Hủ Tiếu Nam Vang 69 | HCM | 68B Nguyễn Văn Trỗi, P8, Phú Nhuận | - | `hu-tieu-nam-vang-69-{id}` | ⚪ | ✓ | 4 thế hệ, 80 năm. TikTok 300K likes |
| 15 | MOMOLY7R20260422 | Cháo Sườn Cô Là | Hà Nội | 2A P. Lý Quốc Sư, Hoàn Kiếm | - | `chao-suon-co-la-{id}` | ⚪ | ✓ | Từ 1996. Con trai học bổng Canada |
| 16 | MOMOZDRF20260416 | Miến Gà Cô Nhẫn | HCM | 2 Phan Văn Trị, P10, Gò Vấp | - | `mien-ga-co-nhan-{id}` | ⚪ | ✓ | Từ 1966. 65+ năm. Giá 35K/tô giữ nguyên |
| 17 | MOMOHNVV20250325 | Giò Chả Bà Bính | Hà Nội | 108 Trần Đại Nghĩa, Đồng Tâm, Bạch Mai | - | `gio-cha-ba-binh-{id}` | ⚪ | ✓ | 100+ năm, đời thứ 3. Festival Thu HN 2024 |
| 18 | MOMOPFHC20241030 | Nộm Bò Khô Long Vi Dung | Hà Nội | Phố Hoàn Kiếm (địa chỉ cụ thể TBD) | - | `nom-bo-kho-long-vi-dung-{id}` | ⚪ | ✓ | Chủ: Đoàn Thị Xuân. Từ 1945. 5 thế hệ. Xuất hiện trong văn Tô Hoài |
| 19 | MOMOTBNY20260414 | Hàng Chè Bà Thơm | Hà Nội | 146 Quán Thánh, Hà Nội | - | `hang-che-ba-thom-{id}` | ⚪ | ✓ | Chủ: Lê Hoàng Trung. Từ 1975. 3 thế hệ |
| 20 | MOMOZYKE20260419 | Cháo Bò O Liên | Đà Nẵng | 73 Nguyễn Hoàng, Hải Châu, Đà Nẵng | - | `chao-bo-o-lien-{id}` | ⚪ | ✓ | Gốc Huế, di tản 1968. 44+ năm bán cháo |
| 21 | MOMOGOVS20260425 | Bún Mắm Dì Liên | Đà Nẵng | 52 Trần Bình Trọng, Phước Ninh, Hải Châu | - | `bun-mam-di-lien-{id}` | ⚪ | ✓ | Từ 1993. Nuôi 3 con học Đại học từ gánh bún |
| 22 | MOMOXP3L20260420 | Bò Nhúng Mắm Ruốc 8 Còn | Bình Dương | 720 Nguyễn Tri Phương, Chánh Nghĩa, TDM | /page/9949928 | `bo-nhung-mam-ruoc-8-con-{id}` | 🔴 REDIRECT | ✓ | 30 năm, 3 thế hệ. Đang mở chi nhánh Đà Lạt (17/4) |
| 23 | MOMOF4HM20240416 | Cơm Tấm Dì Đức | Bình Dương | 9 Nguyễn Trãi, Phú Cường, Thủ Dầu Một | - | `com-tam-di-duc-{id}` | ⚪ | ✓ | Từ 1991. Nơi đầu tiên bán Sườn Mỡ tại VN |
| 24 | MOMON8PP20250918 | Bánh Bèo Bánh Bột Lộc Cô Hai Thương | Bình Dương | 23 Đ. Số 6, Khu Tây A, Đông Hòa | - | `banh-beo-banh-bot-loc-co-hai-thuong-{id}` | ⚪ | ✓ | Từ 1970, 50+ năm. Website: cohaithuong1970.com |
| 25 | MOMOI2VS20241128 | Cafe Bọt Long Lý | Nghệ An | Khu chợ Vinh (địa chỉ cụ thể TBD) | - | `cafe-bot-long-ly-{id}` | ⚪ | ✓ | 30+ năm từ 1992. Lính về hưu mở quán. 100 ly/ngày |
| 26 | MOMOSFZU20260114 | Chả Rươi Hằng Béo | Hà Nội | 244 Phố Lò Đúc, Hà Nội | /page/9843228 | `cha-ruoi-hang-beo-{id}` | 🔴 REDIRECT | ✓ | Chủ: Lê Lệ Hằng. CNN/Great Big Story 2020 |
| 27 | MOMOSOPJ20240918 | Miến Lươn Chân Cầm | Hà Nội | 1 Phố Chân Cầm, Hoàn Kiếm | - | `mien-luon-chan-cam-{id}` | ⚪ | ✓ | Chủ: Vũ Thị Lan. **Michelin Bib Gourmand 2025.** 37+ năm |
| 28 | MOMOC9DC20260415 | Mỳ Cường Thư | Thanh Hóa | 58 Nguyễn Bỉnh Khiêm, Hạc Thành | - | `my-cuong-thu-{id}` | ⚪ | ✓ | SĐT: 0916550145. 46 năm, mỳ Vằn Thắn gốc Hoa |
| 29 | MOMORXQA20221104 | Bún Cá Hờn | Đà Nẵng | Nguyễn Chí Thanh, Hải Châu, Đà Nẵng | - | `bun-ca-hon-{id}` | ⚪ | ✓ | **Michelin Bib Gourmand.** 52 năm, trước 1975 |
| 30 | MOMOYA8F20260417 | Lươn Xuân Leo | Nghệ An | (Không có trong CSV) | - | `luon-xuan-leo-{id}` | ⚪ | ✓ | SĐT: 0837290688 (Chị Thủy). 26 năm từ 1998 |
| 31 | MOMOFUZG20260301 | Hủ Tiếu Nam Vang Ông Hai Bầu | Đồng Nai | Biên Hòa (địa chỉ cụ thể TBD) | - | `hu-tieu-nam-vang-ong-hai-bau-{id}` | ⚪ | ✓ | 36 năm. Con dâu tiếp quản, học truyền thông |
| 32 | MOMOKGBT20230427 | Hủ Tiếu Mỹ Tho Thanh Xuân | HCM | 62 Tôn Thất Thiệp, Q1 | - | *(merge với STT 11)* | ⚪ | ✓ | **DUPLICATE STT 11.** Verify 2 MID cùng merchant |
| 33 | MOMOLTQG20260505 | Chả Giò Phượng | Đồng Nai | 39 Lê Thánh Tôn, Thanh Bình, Trấn Biên | - | `cha-gio-phuong-{id}` | ⚪ | ✓ | 30 năm từ 600đ → 6.000đ/cuốn |
| 34 | MOMOIPNI20260417 | Nem Chua Phương Chi Lê | Thanh Hóa | 21 Phố Quan Sơn, TT. Nhồi, Đông Quang | - | `nem-chua-phuong-chi-le-{id}` | ⚪ | ✓ | Từ 2016. Về quê vì mẹ bệnh, học lại công thức |
| 35 | MOMOMMPG20231114 | Mì Xào Giòn A Tỷ | Đồng Nai | 257 đường 30/4, Quyết Thắng, Biên Hòa (gốc) | - | `mi-xao-gion-a-ty-{id}` | ⚪ | ✓ | = Bột chiên A Tỷ. 3 cơ sở. Gốc Hoa. Từ 1991 |
| 36 | MOMO4WSL20240820 | Bún Thịt Nướng Cô Bế | Bình Dương | 132 Gia Long, Lái Thiêu | - | `bun-thit-nuong-co-be-{id}` | ⚪ | ✓ | 30 năm từ 1995. Con làm ngân hàng |
| 37 | MOMOAWPF20260519 | Tiệm Chè Hữu Hòa | Cần Thơ | 62 Phan Đình Phùng, Ninh Kiều | - | `tiem-che-huu-hoa-{id}` | ⚪ | ✓ | SĐT: 0357057272 (Hưng). 70+ năm từ 1956. Gốc Quảng Đông |

---

## REDIRECT CHECKLIST (3 merchants)

| Merchant | /page/ cũ | URL mới | Status |
|---------|----------|---------|--------|
| Bún Thịt Nướng Chị Tuyền | /page/9819516 | /merchant/bun-thit-nuong-chi-tuyen-44 | ✅ Done |
| Chả Rươi Hằng Béo | /page/9843228 | /merchant/cha-ruoi-hang-beo-{id} | ⏳ Chờ page live |
| Bò Nhúng Mắm Ruốc 8 Còn | /page/9949928 | /merchant/bo-nhung-mam-ruoc-8-con-{id} | ⏳ Chờ page live |

---

## CONTENT PRIORITY QUEUE

| Priority | STT | Merchant | Tỉnh | Volume/tháng | Điểm nổi bật để khai thác |
|---------|:---:|---------|------|:---:|---------|
| **P0** | 6 | Cơm Tấm Ống Khói Diệu | An Giang | 4.400 | Câu chuyện mẹ con, 2000-2025, ống khói = brand name |
| **P0** | 11/32 | Hủ Tiếu Mỹ Tho Thanh Xuân | HCM | 1.300 | 80 năm, Michelin, Chin-Su Masan, verify 2 MID |
| **P1** | 5 | Bánh Ướt Cây Me | Cần Thơ | 480 | 45 năm, cây me bị đốn nhưng tên còn đó |
| **P1** | 35 | Mì Xào Giòn A Tỷ | Đồng Nai | 480 | 30 năm, người Hoa, 3 cơ sở |
| **P1** | 31 | Hủ Tiếu Nam Vang Ông Hai Bầu | Đồng Nai | 390 | 36 năm, con dâu tiếp quản |
| **P1** | 2 | Quán Cơm Chú Lùn | Cần Thơ | 320 | Chú U70 vẫn bán, viral |
| **P2** | 14 | Hủ Tiếu Nam Vang 69 | HCM | 110 | 4 thế hệ, 80 năm, TikTok 300K |
| **P2** | 33 | Chả Giò Phượng | Đồng Nai | 90 | 30 năm, 600đ → 6.000đ |
| **P2** | 9 | Hải Sản Ngô Thơ | Hải Phòng | 70 | TikTok live 20K người xem |
| **P3** | 26 | Chả Rươi Hằng Béo | Hà Nội | 30 | CNN 2020, **launch trước khi set redirect** |
| **P3** | 1 | Bánh Mì Hữu Liêm | Cần Thơ | 20 | Từ 1985 |
| **P3** | 13 | Tiệm Mì Chú Cao | HCM | 10 | 40+ năm, người Hoa |
| **P4** | Còn lại | Các merchants volume = 0 | Nhiều tỉnh | 0 | OOH đang chạy → demand sẽ phát sinh |

---

## MERCHANTS NỔI BẬT (EEAT cao - ưu tiên content quality)

Các merchant dưới đây có Trust Signal mạnh - content cần khai thác rõ:

| Merchant | Trust Signal | Cách khai thác |
|---------|-------------|----------------|
| Miến Lươn Chân Cầm | **Michelin Bib Gourmand 2025** | Đề cập giải thưởng Michelin, 37 năm tự học công thức |
| Bún Cá Hờn | **Michelin Bib Gourmand** | Quán trong hẻm nhỏ, 52 năm từ trước 1975 |
| Hủ Tiếu Mỹ Tho Thanh Xuân | **Chin-Su Masan, 80 năm** | Thương hiệu lên bao bì Chin-Su - tín hiệu xác thực mạnh |
| Nộm Bò Khô Long Vi Dung | **Xuất hiện trong văn Tô Hoài, 5 thế hệ từ 1945** | Di sản văn hóa Hà Nội |
| Giò Chả Bà Bính | **Festival Thu HN 2024, 100+ năm** | Chứng nhận sự kiện nhà nước |
| Chả Rươi Hằng Béo | **CNN Great Big Story 2020** | Media quốc tế coverage |

---

## PHÂN BỔ THEO TỈNH THÀNH

| Tỉnh/TP | Số merchant | Merchants |
|---------|:---:|---------|
| HCM | 7 | Chị Tuyền, Thanh Xuân (2 MID), Mì Chú Cao, Hủ tiếu 69, Miến gà Cô Nhẫn |
| Hà Nội | 6 | Cô Là, Bà Bính, Long Vi Dung, Bà Thơm, Hằng Béo, Chân Cầm |
| Cần Thơ | 5 | Hữu Liêm, Cơm Chú Lùn, Cây Me, Hữu Hòa |
| Đồng Nai | 4 | A Tỷ, Ông Hai Bầu, Chả giò Phượng, *Bột chiên A Tỷ (cùng = 3)* |
| Bình Dương | 4 | 8 Còn, Dì Đức, Cô Hai Thương, Cô Bế |
| Đà Nẵng | 3 | O Liên, Dì Liên, Bún cá Hờn |
| Hải Phòng | 3 | Khánh Nạp, Ngô Thơ, Cô Hường |
| Bắc Ninh | 2 | Mạnh Nháy, Xôi Bà Cụ |
| Thanh Hóa | 2 | Cường Thư, Phương Chi Lê |
| An Giang | 1 | Ống Khói Diệu |
| Nghệ An | 2 | Long Lý, Lươn Xuân Leo |

---

## SUMMARY

| Chỉ số | Số |
|--------|:---:|
| Tổng rows trong CSV | 37 (STT 3 missing) |
| Unique merchants | **35** (sau dedup Hủ tiếu Thanh Xuân 2 MID) |
| Đã LIVE | 1 (Chị Tuyền) |
| Cần 308 Redirect | 2 (Hằng Béo, 8 Còn - chờ page live) |
| Clean launch | 32 |
| Có Michelin | 2 (Chân Cầm, Bún cá Hờn) |
| Có story sẵn từ CSV | 34/35 |
| Confirmed dropped vs BRD | 3 (Hương Giang Bakery, Bò lá lốt, Bún cá Tư Lùn) |
| Đã có draft nội dung | 2 (Cơm Tấm Ống Khói Diệu - P0, Hủ Tiếu Mỹ Tho Thanh Xuân - P0) |

---

## Change Log

- **2026-05-25 (v2.1):** Tạo draft nội dung cho 2 P0 merchants. STT 6 (Cơm Tấm Ống Khói Diệu) → `merchant-pages/com-tam-ong-khoi-dieu.md`. STT 11/32 (Hủ Tiếu Mỹ Tho Thanh Xuân) → `merchant-pages/hu-tieu-my-tho-thanh-xuan.md` (BLOCK: pending MID verify).
- **2026-05-25 (v2.0):** Rewrite toàn bộ từ CSV chính thức `[MEGA26] Potential list - Final list.csv`. Bổ sung MID, địa chỉ đầy đủ, story marker, giải quyết 4 ambiguity cases, xác nhận 3 merchants dropped, phân bổ tỉnh thành, highlight EEAT trust signals.
- **2026-05-25 (v1.0):** Khởi tạo từ phân tích danh sách thủ công.
