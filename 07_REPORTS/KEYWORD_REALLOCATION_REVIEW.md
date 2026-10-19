# BÁO CÁO RÀ SOÁT PHÂN LOẠI KEYWORD & GỘP BIẾN THỂ CHÍNH TẢ TOÀN BỘ KNOWLEDGE BASE

Tài liệu kiểm toán Single Source of Truth (SSOT) phục vụ rà soát phân loại từ khóa sai Theme, chuẩn hóa biến thể chính tả (Spelling & Spacing Variants) và tái cấu trúc Silo Plan trước khi đồng bộ sang Web Platform.

---

## 1. TỔNG QUAN KẾT QUẢ KIỂM TOÁN HỆ THỐNG

| Chỉ số kiểm toán | Trước rà soát | Sau rà soát & Chuẩn hóa | Đánh giá & Tác động |
| :--- | :--- | :--- | :--- |
| **Tổng từ khóa di chuyển sai Theme** | 0 | **1,130 từ khóa** | Chuyển đúng về thương hiệu / thực thể sở hữu |
| **Volume từ khóa di chuyển sai Theme** | 0 | **87,135,950 lượt/tháng** | Phục hồi dữ liệu chính xác cho các Hubs |
| **Nhóm biến thể chính tả gộp (Vietlott)** | 0 | **46 nhóm** | Lấy max volume, lưu mảng `variants[]` |
| **Nhóm biến thể chính tả gộp (XSKT)** | 0 | **393 nhóm** | Triệt tiêu hơn 740 triệu volume trùng lặp ảo |
| **Volume Theme Vietlott** | 86,243,590 (méo mó) | **2,772,350 (chuẩn xác)** | Loại bỏ hoàn toàn `xsmb` (83.1M) khỏi Vietlott |
| **Pillar Keyword Theme Vietlott** | `xsmb` (Sai thực thể) | **`vietlott` (550,000)** | Khôi phục đúng thực thể Vietlott |
| **Silo Plan Primary KW bất thường** | 8 URLs sai brand | **0 URLs bất thường** | 100% trang đích có Primary KW đúng Theme |

---

## 2. DANH SÁCH DI CHUYỂN TỪ KHÓA THEO PHÂN KHỐI (FROM_THEME -> TO_THEME)

### A. Phân khối Xổ Số & Vé Số (283 từ khóa - 84,971,110 volume)

#### Chuyển từ Theme Vietlott sang Theme Xổ Số Kiến Thiết (XSKT) & Vé Số (71 từ khóa - 83,420,150 volume)
| Từ khóa | Volume | Từ Theme | Sang Theme | Lý do di chuyển |
| :--- | :--- | :--- | :--- | :--- |
| `xsmb` | 83,100,000 | `vietlott` | `xo-so (XSKT)` | Từ khóa thương hiệu Xổ Số Miền Bắc truyền thống |
| `xổ số điện toán` | 27,100 | `vietlott` | `xo-so (XSKT)` | Khái niệm chung xổ số điện toán |
| `xổ số hàng tuần` | 18,100 | `vietlott` | `xo-so (XSKT)` | Thuộc lịch quay số XSKT truyền thống |
| `xổ số 3d` | 5,400 | `vietlott` | `xo-so (XSKT)` | Từ khóa chung |
| `kết quả xổ số điện toán` | 2,400 | `vietlott` | `xo-so (XSKT)` | Kết quả xổ số chung |
| `do ve sô` | 590 | `vietlott` | `ve-so (Vé Số)` | Hành vi dò vé số truyền thống |
| `kết quả xổ số 3d` | 590 | `vietlott` | `xo-so (XSKT)` | Kết quả xổ số |
| `sms xổ số` | 260 | `vietlott` | `xo-so (XSKT)` | Dịch vụ SMS kết quả xổ số kiến thiết |
| `vé số điện toán` | 140 | `vietlott` | `ve-so (Vé Số)` | Thuộc danh mục vé số |
| `xstuchon` | 110 | `vietlott` | `xo-so (XSKT)` | Xổ số tự chọn thủ công |
| `vip 24h` | 90 | `vietlott` | `xo-so (XSKT)` | Từ khóa rác soi cầu XSKT |
| `1900599822` | 50 | `vietlott` | `xo-so (XSKT)` | Tổng đài soi cầu XSKT |

*(Và 59 từ khóa đuôi dài XSKT khác với volume < 50)*

#### Chuyển từ Theme Xổ Số Kiến Thiết sang Theme Vietlott (127 từ khóa - 1,539,230 volume)
| Từ khóa | Volume | Từ Theme | Sang Theme | Sản phẩm Vietlott nhận diện |
| :--- | :--- | :--- | :--- | :--- |
| `xổ số vietlott` | 201,000 | `xo-so (XSKT)` | `vietlott` | Thương hiệu Vietlott |
| `xs vietlott` | 165,000 | `xo-so (XSKT)` | `vietlott` | Thương hiệu Vietlott |
| `xổ số power` | 110,000 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Power 6/55 |
| `vietlott sms` | 110,000 | `xo-so (XSKT)` | `vietlott` | Ứng dụng Vietlott SMS |
| `vietlott 6 45` | 90,500 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Mega 6/45 |
| `vietlott 6 55` | 90,500 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Power 6/55 |
| `xổ số mega` | 90,500 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Mega 6/45 |
| `xsmega` | 74,000 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Mega 6/45 |
| `kết quả vietlott` | 60,500 | `xo-so (XSKT)` | `vietlott` | Kết quả Vietlott |
| `mega645` | 49,500 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Mega 6/45 |
| `truc tiep keno` | 40,500 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Keno |
| `trực tiếp keno` | 40,500 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Keno |
| `xổ số vietlott hôm nay` | 40,500 | `xo-so (XSKT)` | `vietlott` | Thương hiệu Vietlott |
| `kết quả xổ số vietlott` | 33,100 | `xo-so (XSKT)` | `vietlott` | Kết quả Vietlott |
| `max3d` | 33,100 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Max 3D |
| `xổ số keno` | 27,100 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Keno |
| `keno trực tiếp` | 27,100 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Keno |
| `vietlott 655` | 22,200 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Power 6/55 |
| `kqxs vietlott` | 22,200 | `xo-so (XSKT)` | `vietlott` | Kết quả Vietlott |
| `ket qua vietlott` | 22,200 | `xo-so (XSKT)` | `vietlott` | Kết quả Vietlott |
| `keno vietlott` | 18,100 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Keno |
| `xổ số vietlott 6 55` | 18,100 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Power 6/55 |
| `xs vietlott hôm nay` | 18,100 | `xo-so (XSKT)` | `vietlott` | Thương hiệu Vietlott |
| `kết quả keno` | 18,100 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Keno |
| `keno minh chinh` | 14,800 | `xo-so (XSKT)` | `vietlott` | Sản phẩm Keno |

---

### B. Phân khối Ngân Hàng (710 từ khóa - 2,152,710 volume)

Khắc phục triệt để tình trạng file CSV của một ngân hàng chứa từ khóa thương hiệu của ngân hàng đối thủ (làm méo mó Pillar Keyword):

| Từ khóa | Volume | Từ Theme (Bị lẫn) | Sang Theme (Chính chủ) | Thương hiệu đối thủ nhận diện |
| :--- | :--- | :--- | :--- | :--- |
| `agribank` | 368,000 | `vrb (Việt Nga)` | `agribank` | Agribank |
| `mbbank` | 301,000 | `ab-bank (An Bình)` | `mbbank` | MBBank |
| `mbbank` | 301,000 | `ocb (Phương Đông)` | `mbbank` | MBBank |
| `mbbank` | 301,000 | `scb (Sài Gòn)` | `mbbank` | MBBank |
| `mb bank` | 301,000 | `MSB (Hàng Hải)` | `mbbank` | MBBank |
| `mb bank atm` | 90,500 | `seabank (Đông Nam Á)` | `mbbank` | MBBank |
| `vietinbank ipay` | 27,100 | `vietbank` | `VietinBank` | VietinBank |
| `seabank` | 27,100 | `nam-a-bank` | `seabank` | SeABank |
| `tỷ giá vietinbank` | 22,200 | `vietbank` | `VietinBank` | VietinBank |
| `acb bank` | 22,200 | `ncb (Quốc Dân)` | `ACB` | ACB |
| `acb bank` | 22,200 | `ocb (Phương Đông)` | `ACB` | ACB |
| `bidv i bank` | 18,100 | `nam-a-bank` | `BIDV` | BIDV |
| `ngân hàng bản việt` | 14,800 | `VietinBank` | `ban-viet` | BVBank |
| `mbbank đăng nhập` | 14,800 | `ab-bank` | `mbbank` | MBBank |
| `mbbank đăng nhập` | 14,800 | `ocb` | `mbbank` | MBBank |
| `mbbank online` | 12,100 | `ocb` | `mbbank` | MBBank |
| `mbbank online` | 12,100 | `ab-bank` | `mbbank` | MBBank |
| `bank bidv` | 12,100 | `nam-a-bank` | `BIDV` | BIDV |
| `agribank plus` | 9,900 | `vrb` | `agribank` | Agribank |
| `msb bank` | 9,900 | `nam-a-bank` | `MSB` | MSB |

---

### C. Phân khối Bảo Hiểm & Giao Thông

- **Thu phí không dừng (Vehicle Hub):** 111 từ khóa thương hiệu ePass (ví dụ: `dán epass`, `thẻ epass`, `đăng ký epass`...) bị lẫn trong `vetc.csv` được chuyển về đúng Theme `epass`.
- **Bảo hiểm số (Insurtech):**
  - 12 từ khóa thuần BHXH (ví dụ: `cách tra cứu bảo hiểm xã hội`, `đóng bhxh tự nguyện`) trong `bhyt.csv` chuyển sang `bhxh`.
  - 14 từ khóa thuần BHYT (ví dụ: `thẻ bảo hiểm y tế điện tử`, `mua bhyt tự nguyện`) trong `bhxh.csv` chuyển sang `bhyt`.

---

## 3. DANH SÁCH NHÓM BIẾN THỂ CHÍNH TẢ ĐÃ GỘP (MAX VOLUME & VARIANTS[])

Áp dụng quy tắc: Gộp các từ khóa cùng nghĩa khác cách viết (dấu cách, gạch nối, dấu tiếng Việt) thành 1 từ khóa chính; **Volume lấy MAX** (không cộng dồn để tránh phình số liệu ảo); lưu mảng `variants[]` phục vụ tra cứu.

### A. Nhóm Biến thể Theme Vietlott (Top 15 nhóm tiêu biểu)

| STT | Từ khóa chính (Canonical) | Max Volume | Danh sách biến thể gộp (`variants[]`) |
| :--- | :--- | :--- | :--- |
| 1 | `viet lott` | 550,000 | `['vietlott']` |
| 2 | `xổ số vietlott` | 201,000 | `['xo so vietlott']` |
| 3 | `vietlott 6 45` | 90,500 | `['vietlott645']` |
| 4 | `vietlott 6 55` | 90,500 | `['vietlott 655']` |
| 5 | `kết quả vietlott` | 60,500 | `['ket qua vietlott']` |
| 6 | `mega 6 45` | 49,500 | `['mega 6.45', 'mega645']` |
| 7 | `xổ số vietlott hôm nay` | 40,500 | `['xo so vietlott hom nay']` |
| 8 | `truc tiep keno` | 40,500 | `['trực tiếp keno']` |
| 9 | `vietlott hôm nay` | 33,100 | `['vietlott hom nay']` |
| 10 | `max3d` | 33,100 | `['max3d+']` |
| 11 | `mega 6 55` | 22,200 | `['mega6 55']` |
| 12 | `xổ số vietlott 6 55` | 18,100 | `['xổ số vietlott 655']` |
| 13 | `kết quả keno` | 18,100 | `['ket qua keno']` |
| 14 | `keno minh chinh` | 14,800 | `['keno minh chính']` |
| 15 | `số vietlott` | 12,100 | `['so vietlott']` |

### B. Nhóm Biến thể Theme Xổ Số Kiến Thiết (Top 15 nhóm tiêu biểu)

| STT | Từ khóa chính (Canonical) | Max Volume | Danh sách biến thể gộp (`variants[]`) |
| :--- | :--- | :--- | :--- |
| 1 | `xổ so miền bắc` | 83,100,000 | `['xô sô miên băc', 'xo số mien bac', 'xổ số miền bắc', 'xo so mien bac' + 13 biến thể khác]` |
| 2 | `xổ số miền nam` | 68,000,000 | `['xo số mien nam', 'xô số miền nam', 'xo so mien nam' + 11 biến thể khác]` |
| 3 | `xổ số miền trung` | 20,400,000 | `['xo so mien trung', 'xo so miên trung', 'xo so miền trung']` |
| 4 | `xổ số miền nam hôm nay` | 11,100,000 | `['xo số miền nam hôm nay', 'xo so mien nam hom nay']` |
| 5 | `kq xsmb` | 9,140,000 | `['kqxsmb', 'kqxs mb']` |
| 6 | `xổ số hôm nay` | 7,480,000 | `['xô số hôm nay', 'xo so hom nay', 'xo số hôm nay' + 2 biến thể]` |
| 7 | `xổ số miền bắc hôm nay` | 7,480,000 | `['xo số miền bắc hôm nay', 'xổ số miên bắc hôm nay', 'xo so mien bac hom nay']` |
| 8 | `xổ số minh ngọc` | 5,000,000 | `['xổ số mình ngọc', 'xo so minhngoc', 'xôsominhngoc']` |
| 9 | `kết quả xổ số miền bắc` | 5,000,000 | `['ket qua xo so mien bac', 'kết qua xo so mien bac', 'ket qua xổ số miền bắc' + 5 biến thể]` |
| 10 | `xổ số miền trung hôm nay` | 4,090,000 | `['xo so mien trung hom nay', 'xổ số miền trung hôm nay']` |
| 11 | `xs mb hôm nay` | 3,350,000 | `['xsmb hôm nay']` |
| 12 | `kq xsmn` | 2,740,000 | `['kqxs mn']` |
| 13 | `xo so` | 2,240,000 | `['xổ số', 'xô số']` |
| 14 | `kết quả xổ số miền nam` | 2,240,000 | `['ket qua xo so mien nam', 'ket quả xổ số miền nam']` |
| 15 | `kết quả xổ số hôm nay` | 1,830,000 | `['ket qua xo so hom nay']` |

---

## 4. TÍNH TOÁN LẠI CHỈ MỤC SILO PLAN & SUB-CLUSTERS

### Sửa lỗi Primary Keyword trong Silo Plan (`data/content-plan-data.json`)
| Slug URL | Trang bài viết | Primary KW cũ (Sai) | Primary KW mới (Chuẩn hóa) | Volume mới |
| :--- | :--- | :--- | :--- | :--- |
| `/vietlott/` | Trang chủ Hub Vietlott Mega & Power | `xsmb` (Sai theme XSKT) | **`vietlott`** | 550,000 |
| `/vrb/` | Trang chủ Hub Ngân hàng Việt Nga (VRB) | `agribank` (Sai brand) | **`vrb`** | 14,800 |
| `/vrb/kien-thuc-chuyen-sau/` | Bài kiến thức chuyên sâu VRB | `agribank plus` (Sai brand) | **`ngân hàng việt nga`** | 5,400 |
| `/ab-bank/` | Trang chủ Hub Ngân hàng ABBank | `mbbank` (Sai brand) | **`ab bank`** | 18,100 |
| `/ab-bank/cong-cu-tinh-toan/` | Công cụ tính toán ABBank | `agribank giữ lại bao nhiêu` | **`lãi suất ab bank`** | 2,400 |
| `/ab-bank/an-toan-bao-mat/` | An toàn bảo mật ABBank | `mbbank online doanh nghiệp` | **`abbank online`** | 1,900 |
| `/ocb/` | Trang chủ Hub Ngân hàng OCB | `mbbank` (Sai brand) | **`ocb`** | 18,100 |
| `/scb/` | Trang chủ Hub Ngân hàng SCB | `mbbank` (Sai brand) | **`scb`** | 12,100 |
