# BRD: Merchant Detail Page - SME Digital Presence Platform

> - **Project:** Merchant Detail Page (SME Digital Presence + O2O Ecosystem)
> - **Main URL:** momo.vn/merchant
> - **Division:** GPD (Growth Platform Division)
> - **Use Case:** Merchant Pages
> - **Owner:** GPD - Out-App Traffic
> - **Governance:** SEO & GEO Lead
> - **PIC Build:** Nhật (Build Lead) - Hoài Anh (MoSpark Architecture)
> - **Version:** 2.5 - 2026-05-29
> - **Status:** Pilot Phase - 38 Merchants Live (Batch 2 + Extended)

---

> **Problem:** MoMo có hàng nghìn merchant nhưng không có trang web giúp user xác nhận và kích hoạt O2O - traffic intent cao đang rơi vào tay bên thứ 3. Đồng thời SME nhỏ không có Digital Presence để xuất hiện trên Web và AI - hoàn toàn vô hình khi user search.
> **KPI Owned:** VTS Activations + O2O Engagement từ `momo.vn/merchant` (attributed via Appsflyer + Umami)
> **Consumer Flow:** "{Merchant} có nhận MoMo không?" → `/merchant/{slug}` → O2O CTA click → App open → Activation → Transaction
> **SME Value Prop:** Xuất hiện miễn phí trên momo.vn (Web) + AI Agent responses - Digital Assets không cần chi phí marketing

---

## 1. Executive Summary

### Situation

Hai vấn đề song song trong một kiến trúc.

**Phía Consumer:** User search "{Merchant} có nhận Ví Trả Sau không" là nhóm có purchase intent cao nhất có thể capture trên Web - họ đã chọn merchant, đã chọn phương thức thanh toán, chỉ cần một xác nhận. MoMo không có trang nào serve được intent này ở cấp độ merchant cụ thể. 85K organic traffic/quý đang chảy vào 2 legacy systems không có conversion goal: `/thanh-toan-momo-{merchant}` (18K, content outdated 5-7 năm) và `/page/{id}` (67K, thin content không cập nhật).

**Phía SME:** Merchant nhỏ - quán bún thịt nướng, tiệm cà phê, hàng chả giò - không có website, không có ngân sách digital marketing. Họ hoàn toàn vô hình trên Google Search và AI engine khi user tìm kiếm. MoMo có hạ tầng web và merchant data để tạo Digital Presence cho họ miễn phí, đổi lại merchant có động lực adopt ecosystem O2O (Soundbox + VTS + Hoàn tiền).

### Complication

Consumer traffic với intent cao nhất đang thoát ra tay bên thứ 3 - không có conversion. SME không thể tự build Digital Presence. 2 legacy systems không chỉ không convert - chúng là gánh nặng: crawl budget waste, thin content kéo giảm site quality toàn domain, keyword cannibalization với kiến trúc mới.

ZaloPay đã build `/doi-tac/{merchant}` cho F&B chains nhưng chưa khai thác BNPL và SME angle - đây là cửa sổ cơ hội MoMo đi trước.

### Resolution

`momo.vn/merchant/{slug}` là một **SME Digital Presence product**, không phải trang thông tin. Product có hai jobs song song:

**Job 1 - SME:** Mỗi merchant dù nhỏ đến đâu đều có một trang truyền thông đầy đủ trên momo.vn: UI tốt, hiển thị SERP, xuất hiện trong AI responses. Miễn phí. MoMo tạo và maintain - merchant không cần tự build hay bảo trì.

**Job 2 - Consumer:** User xác nhận ngay merchant có nhận MoMo/VTS không và kích hoạt O2O trong 3 bước - không cần đọc dài.

4 template variants phục vụ đa dạng merchant từ brand chain đến SME cơ bản. QR code tại điểm bán kết nối offline với Digital Presence. Schema markup đảm bảo xuất hiện trong AI Overview và LLM - GEO moat dài hạn. Song song 301 redirect 2 legacy systems để consolidate authority vào 1 architecture sạch.

**Value exchange:** MoMo tạo Digital Presence miễn phí cho SME → SME adopt Soundbox/VTS → Consumer có O2O trải nghiệm tốt → Transaction volume tăng.

---

## 2. Bối Cảnh Thị Trường

### 2.1 Hiện Trạng Legacy Systems

| System | URL Pattern | Organic Traffic | Vấn đề chính |
|---|---|---|---|
| Merchant Landing Pages | /thanh-toan-momo-{merchant} | 18K/quý | Content outdated 5-7 năm, không có O2O angle, không có schema |
| Thổ Địa Ăn Uống | /page/{id} | 67K/quý | Thin content quy mô lớn, thông tin sai (quán đóng cửa), crawl budget waste |

### 2.2 Vấn Đề Chất Lượng Web Từ Legacy

- Google đánh giá chất lượng ở site-level (Helpful Content System). Tỷ lệ lớn thin/outdated content kéo giảm ranking toàn bộ momo.vn.
- Crawl budget bị phân tán vào hàng nghìn trang giá trị thấp - trang mới `/merchant` bị crawl chậm hơn.
- Keyword cannibalization: 3 URLs (legacy + /merchant mới) cạnh tranh cùng merchant query.

### 2.3 Phân Tích Cạnh Tranh

| Competitor | Hiện trạng | Khoảng trống MoMo có thể tận dụng |
|---|---|---|
| ZaloPay | Build merchant directory F&B chains. Chưa có SME angle, chưa có BNPL, chưa có FAQ/HowTo schema | MoMo đi trước: SME + O2O stack + AI citation |
| Klarna (quốc tế) | merchant.klarna.com với "Pay in 4" per merchant | BNPL-first merchant directory model |
| Google Business Profile | Free local listing nhưng không integrated với payment/O2O | MoMo lợi thế: O2O loop hoàn chỉnh (Soundbox + VTS + Cashback) |

### 2.4 SME Digital Gap - Core Insight

SME nhỏ chiếm phần lớn merchant base của MoMo nhưng:
- Không có website
- Không có ngân sách digital marketing
- Hoàn toàn vô hình trên Google Search và AI engine
- Không có điểm tiếp xúc digital với khách hàng ngoài mạng xã hội cá nhân

MoMo có đủ điều kiện giải quyết gap này: domain authority momo.vn, merchant data, platform MoSpark, GenAI content pipeline, và O2O product stack để làm value prop thuyết phục với SME.

---

## 3. Định Hướng Dự Án

### 3.1 Dự Án Này Phục Vụ Điều Gì?

**Dual-sided product - 3 điểm kết nối:**

**Cho SME:** Mỗi `momo.vn/merchant/{slug}` là Digital Presence page hoàn toàn miễn phí. SME không cần tự build, không cần bảo trì. Được xuất hiện trên Google Search và AI Agent responses khi user tìm kiếm tên merchant hoặc danh mục.

**Cho Consumer:** Xác nhận merchant nhận MoMo/VTS và kích hoạt O2O ngay từ trang. Product job: xác nhận + activate trong 3 bước.

**Cho MoMo - O2O Ecosystem Connector:** Merchant Microsite là điểm kết nối tam giác End User / MoMo / Merchant thông qua 4 sản phẩm O2O:
- **VTS (Ví Trả Sau):** Consumer kích hoạt BNPL ngay khi biết merchant hỗ trợ
- **Soundbox:** SME thu tiền QR → QR link về Microsite → đóng vòng lặp Offline → Online
- **Hoàn tiền (Cashback):** Consumer thấy cashback offer → incentive thanh toán MoMo tại merchant
- **Xu (Reward):** Tích điểm khi thanh toán - long term loyalty loop. Chi tiết TBD Q3+.

**Timeline:**
- **Q2/2026 - Mega Campaign:** Phục vụ chiến dịch "Trả Sau Hoàn Sâu" - hứng search demand từ OOH, kết nối user với SME đang trong campaign.
- **Long Term:** Nền tảng truyền thông thường xuyên cho SME yếu thế về comm. Dịch chuyển hành vi O2O bền vững theo 2 chiều:
  - **Online → Offline:** User discover merchant qua Search/AI → visit điểm bán → transaction với MoMo
  - **Offline → Online:** QR tại Soundbox/điểm bán → user vào Microsite → kích hoạt O2O product

### 3.2 Dự Án Này KHÔNG Phải

- Không xây lại Thổ Địa Ăn Uống (hệ thống review local)
- Không phải CMS cho merchant tự quản lý
- Không phải store locator (merchant-level, không phải branch-level)
- Không phải trang marketing/campaign - đây là evergreen content + platform
- Không phải Google Business Profile replica - MoMo value-add là O2O stack, không phải local listing đơn thuần

---

## 4. JTBD Analysis

### Job #1 (SME): Được Xuất Hiện Trên Digital Assets Miễn Phí

> "Tôi là chủ quán nhỏ. Tôi muốn khách hàng tìm thấy tôi trên mạng và biết tôi nhận MoMo."

| Dimension | Nội dung |
|---|---|
| Functional | Có trang web đầy đủ trên momo.vn mà không cần tự build hay trả hosting |
| Emotional | Cảm giác được công nhận - quán nhỏ nhưng có Digital Presence như brand lớn |
| Social | Khách hàng có thể share link, check-in, giới thiệu người khác qua link chuẩn |
| Trigger | Merchant thấy đối thủ cùng khu vực có trang MoMo, hoặc sales MoMo tư vấn khi lắp Soundbox |

**Giải pháp:** `momo.vn/merchant/{slug}` - MoMo tạo và maintain, merchant được xuất hiện trên Search + AI Agent.

---

### Job #2 (Consumer): Xác Nhận Merchant Có Nhận MoMo/VTS Không

> "{Merchant} có thanh toán qua MoMo không? Có nhận Ví Trả Sau không?"

| Dimension | Nội dung |
|---|---|
| Functional | Xác nhận ngay merchant mình chọn có nhận MoMo/VTS không |
| Emotional | Tránh bị từ chối tại quầy thanh toán trước mặt người khác |
| Social | Confirm trước khi đề xuất cho nhóm bạn/đồng nghiệp |
| Trigger | Đang ở trước merchant hoặc chuẩn bị đi - cần quyết định nhanh |

**Giải pháp:** `/merchant/{slug}` với payment methods rõ ràng, FAQ direct, CTA kích hoạt ngay.

---

### Job #3 (Consumer): Kích Hoạt VTS Khi Biết Merchant Hỗ Trợ

> "Tôi muốn dùng VTS tại Highlands nhưng chưa kích hoạt - làm thế nào?"

| Dimension | Nội dung |
|---|---|
| Functional | Biết merchant hỗ trợ VTS, hiểu điều kiện, kích hoạt ngay từ trang |
| Emotional | Mua sắm thông minh - mua trước trả sau 0% lãi |
| Trigger | Tại merchant, hết tiền ví, hoặc muốn dùng VTS để tích điểm |

**Giải pháp:** VTS Promotion Module + CTA "Mở Ví Trả Sau" với thông tin hạn mức, phí, kỳ hạn.

---

### Job #4 (Consumer): Tìm Cách Thanh Toán MoMo Tại Merchant Cụ Thể

> "Cách thanh toán MoMo tại FPT Shop như thế nào?"

| Dimension | Nội dung |
|---|---|
| Functional | Hướng dẫn step-by-step tại merchant cụ thể |
| Emotional | Không muốn mất thời gian, bị nhân viên chờ, trông ngớ ngẩn |
| Trigger | Lần đầu dùng MoMo tại merchant hoặc merchant thay đổi quy trình |

**Giải pháp:** HowTo section 3-4 bước + HowTo Schema cho AI citation.

---

## 5. Kiến Trúc Web

### 5.1 URL Architecture - 3 Cấp + Sub-pages

| Cấp | URL Pattern | Số lượng | Vai trò |
|---|---|---|---|
| Hub | `momo.vn/merchant` | 1 | Discovery + Navigation |
| Category | `momo.vn/merchant/{ten-category}` | 15 | Consideration + Listing |
| Merchant Detail | `momo.vn/merchant/{ten-merchant}-{dia-diem}-{id}` | 100-200 (pilot) → 500-1.000+ | Decision + O2O Conversion |
| Sub-pages (Phase 2) | `momo.vn/merchant/{slug}/{sub-page}` | Per merchant | Deep content (menu, chi nhánh, ưu đãi) |

**Slug pattern:** `{ten-merchant}-{id}` - tên merchant kebab-case không dấu, không tỉnh thành, kết thúc bằng ID backend tự assign. Ví dụ thực tế: `momo.vn/merchant/bun-thit-nuong-chi-tuyen-44`.

**Sub-pages scope (Phase 2 - TBD với Nhật):**
- `/merchant/{slug}/menu` - Thực đơn/sản phẩm
- `/merchant/{slug}/chi-nhanh` - Danh sách chi nhánh (chain merchants)
- `/merchant/{slug}/uu-dai` - Ưu đãi đang chạy

Sub-pages chỉ được tạo khi merchant có đủ data - không tạo sub-page placeholder rỗng.

### 5.2 Category List (15 danh mục)

| # | Category Name | URL Path | O2O Hook |
|---|---|---|---|
| 1 | Nhà hàng | /merchant/nha-hang | Ăn trả sau + Hoàn tiền |
| 2 | Quán ăn | /merchant/quan-an | Ăn uống trả sau |
| 3 | Cà phê | /merchant/ca-phe | Uống cà phê trả sau |
| 4 | Trà sữa | /merchant/tra-sua | Trà sữa trả sau |
| 5 | Bách hóa | /merchant/bach-hoa | Mua đồ trả sau |
| 6 | Cửa hàng tiện lợi | /merchant/cua-hang-tien-loi | Tiện lợi trả sau |
| 7 | Siêu thị | /merchant/sieu-thi | Mua sắm trả sau |
| 8 | Giáo dục | /merchant/giao-duc | Học phí trả góp VTS |
| 9 | Tài chính - Bảo hiểm | /merchant/tai-chinh-bao-hiem | Đóng phí trả sau |
| 10 | Giải trí | /merchant/giai-tri | Mua vé trả sau |
| 11 | Du lịch - Đi lại | /merchant/du-lich-di-lai | Đặt vé/phòng trả sau |
| 12 | Mua sắm | /merchant/mua-sam | Mua trước trả sau |
| 13 | Làm đẹp - Sức khỏe | /merchant/lam-dep-suc-khoe | Chăm sóc trả sau |

### 5.3 Template System - 2 Variants

**Mọi merchant đều có KV** - không phân biệt brand chain hay SME. Biến quyết định template duy nhất: **Review** (có sync được hay không).

| Template | KV | Review | Target Merchant |
|---|---|---|---|
| A - With Review | AI-generated (mọi merchant) | Có Review (sync) | Merchant có review data (brand chain hoặc SME trending) |
| B - Without Review | AI-generated (mọi merchant) | Non-review | Merchant chưa có review sync |

**AI KV Generation Workflow:**
1. **Input:** Ảnh thô của merchant (chụp vội từ BD team khi lắp Soundbox, hoặc ảnh SME cung cấp)
2. **AI Process:** Image-to-Image retouch - chuẩn hóa ánh sáng, composition, nâng chất lượng ảnh
3. **Output:** KV fill vào MoSpark template - đạt chuẩn brand guideline tự động
4. **Review gate:** Review trước publish (cùng pipeline với Content review)

**Review Sync:** Data source cần xác nhận - MoMo transaction rating / Google Places API / internal review system. **TBD với PO team trước khi apply Template A.**

### 5.4 Merchant Detail Page Structure

**Nguyên tắc Standalone Microsite:** Mỗi `momo.vn/merchant/{slug}` là một Microsite độc lập - không cross-link sang merchant khác, không hiển thị merchant liên quan. Mỗi trang tự hoàn chỉnh về nội dung và O2O value prop. SEO strength đến từ domain authority momo.vn + schema riêng của từng trang, không phụ thuộc vào internal linking giữa các merchant.

Mỗi `momo.vn/merchant/{slug}` gồm 2 phần tách biệt:

- **Merchant Content (Long Content):** Nội dung giới thiệu merchant, FAQ, HowTo. Do GenAI Content Engine sản xuất và phải qua editorial review trước publish. Không auto-publish.
- **Platform Modules:** Payment Methods, O2O Promotions. Inject tự động từ MoSpark template, fix cứng để đảm bảo tính pháp lý.

| # | Thành phần | Loại | Chi tiết |
|---|---|---|---|
| 1 | KV (Key Visual) | AI-generated | Ảnh thô merchant → Image-to-Image AI retouch → fill MoSpark template. Mọi merchant đều có. |
| 2 | NAP (Merchant Data) | Platform Data | Tên Merchant, Category, SĐT, Địa chỉ, Hours |
| 3 | Payment Methods | Platform Module | MoMo/VTS/QR - fix từ merchant data |
| 4 | O2O Promotion Stack | Platform Module (Fix cứng) | VTS Card + Hoàn tiền + Soundbox CTA (tùy merchant có sản phẩm tương ứng) |
| 5 | Review Block | Platform Module (conditional) | Aggregate rating + số review - chỉ hiển thị nếu Template A (có Review sync) |
| 6 | Long Content | GenAI Content | Bài viết 150-300 từ giới thiệu chuyên sâu về merchant |
| 7 | FAQ & HowTo | GenAI + editor review | Câu hỏi thường gặp + hướng dẫn thanh toán step-by-step |

**Nguyên tắc tách biệt quan trọng:**
- Long Content phục vụ merchant story - không lồng ghép O2O thái quá
- O2O chỉ xuất hiện tại 2 nơi: Payment Methods list và O2O Promotion Stack module
- Editor không được chỉnh sửa VTS/Hoàn tiền data - inject từ 1 nguồn duy nhất

### 5.5 O2O Solution Stack

| Sản phẩm | Vai trò trên Merchant Page | Điều kiện hiển thị | CTA |
|---|---|---|---|
| VTS (Ví Trả Sau) | Mua trước trả sau tại merchant | Merchant có trong VTS merchant list (PO VTS verify) | "Kích hoạt Ví Trả Sau" → Onelink |
| Hoàn tiền (Cashback) | Ưu đãi cashback khi thanh toán MoMo | Merchant đang chạy cashback campaign | "Xem ưu đãi hoàn tiền" → App |
| Soundbox | Giải pháp thu tiền QR cho SME | Merchant là SME dùng/cân nhắc Soundbox | "Đăng ký Soundbox" → App/form |
| Xu (Reward) | Tích điểm thưởng khi thanh toán tại merchant | TBD - Product vision Q3+ | TBD |

**VTS Module Data (Fixed - YMYL):**

| Data point | Giá trị |
|---|---|
| Lãi suất | 0% (không tính lãi) |
| Hạn mức | Đến 20 triệu |
| Phí | 33.000đ/tháng (không xài không mất phí) |
| Kỳ hạn | 2/3/6/9/12 tháng |
| Điều kiện | Xác thực CCCD + Liên kết ngân hàng |

**YMYL Notice:** Template inject từ 1 nguồn duy nhất do PO VTS approve. Editor không được chỉnh sửa tùy ý per merchant page.

### 5.6 Schema & GEO Requirements

| Cấp trang | Schema bắt buộc | GEO Target |
|---|---|---|
| Hub `/merchant` | ItemList - FAQPage - Organization - BreadcrumbList | "MoMo có những đối tác nào" |
| Category `/merchant/{cat}` | ItemList - FAQPage - HowTo - BreadcrumbList | "Cách thanh toán MoMo tại {category}" |
| Merchant `/merchant/{slug}` | LocalBusiness - FAQPage - HowTo - Offer - BreadcrumbList | "{Merchant} có nhận VTS không" |
| Sub-pages (Phase 2) | BreadcrumbList + type-specific (Menu/Event) | Tùy sub-page |

### 5.7 Search Intent Mapping

| Keyword Pattern | Intent | Landing Page | CTA |
|---|---|---|---|
| "{Merchant} có nhận MoMo không" | Navigation/BoFu | /merchant/{slug} | Thanh toán ngay |
| "{Category} nhận MoMo" | MoFu | /merchant/{category} | Xem đối tác |
| "Ưu đãi MoMo {danh mục}" | Commercial | /merchant/{category} | Xem ưu đãi |
| "Ví Trả Sau {Merchant}" | BoFu | /merchant/{slug}#vi-tra-sau | Kích hoạt VTS |
| "{Merchant} review" | Informational | /merchant/{slug} | Review block (nếu có) |

---

## 6. Comm Activities

3 channel song song - không phụ thuộc nhau, cộng hưởng nhau.

### 6.1 SEO - Organic Search

- **Cơ chế:** LocalBusiness + FAQPage + HowTo schema + Long Content + Internal Linking
- **Target keyword:** "{Merchant} có nhận MoMo không", "{Merchant} VTS", "{Category} nhận MoMo"
- **Gate bắt buộc:** Foundation Checklist pass trước publish. CWV gate (LCP < 2.5s, INP < 200ms, CLS < 0.1).
- **Expected:** Top 5 cho 80% branded merchant queries trong 90 ngày post-launch.

### 6.2 QR Code Tại Điểm Bán (O2O Offline-to-Digital)

- **Cơ chế:** QR code dán tại quầy/Soundbox → link về `/merchant/{slug}`
- **UTM structure:** `?utm_source=qr&utm_medium=offline&utm_campaign=soundbox&utm_content={merchant_id}`
- **Mục tiêu:** Khách tại điểm bán scan QR → vào trang merchant → thấy O2O offers → kích hoạt
- **Attribution:** Umami track on-site event + Appsflyer track app open sau QR scan
- **Rollout priority:** Soundbox merchants trước - QR đã có trên máy, chỉ cần update link về /merchant/{slug}

### 6.3 LLM / AI Agent Search (GEO)

- **Cơ chế:** Structured data + Entity signal + FAQ content cho Google AI Overview, ChatGPT, Perplexity
- **Target queries:** "Quán [tên] có nhận MoMo không?", "[Merchant] review", "Cách thanh toán MoMo tại [merchant]"
- **Gate bắt buộc:** FAQPage + HowTo schema required. LocalBusiness schema với đầy đủ NAP + openingHours.
- **Measurement:** Manual check AI responses + GSC AI Referral tracking

---

## 7. Content Production Scale

**Pilot Foundation: 100-200 merchants** - chốt template và đo CR baseline trước khi scale.

**Batch 1 - Top Brand Chains (32 đối tác):**
- Siêu thị & CHTL: Bách Hóa Xanh, Coopmart, Emart, 7-11, GS25, Family Mart, Mega Market, Circle K, Go, Lotte Mart, Ministop, Aeon
- F&B: Pizza 4P, Katinat, Highlands, Phúc Long, Jollibee, Kichi Kichi, Manwah, Dookki, Gogi, Starbucks, Lotteria, Sasin
- Sức khỏe & Làm đẹp: Pharmacity, Long Châu
- Bán lẻ chuyên biệt: Lazada, Fahasa, Con Cưng, CellphoneS
- Dịch vụ: Grab, TikTok

**Batch 2 - SME Soundbox - Mega 2026 OOH Comm (24 đối tác - URGENT):**

24 merchant SME đang được truyền thông OOH trên 11 tỉnh trong chiến dịch "Trả Sau Hoàn Sâu" (Mega 2026). OOH đang chạy nhưng chưa có trang MoMo nào hứng search demand - mỗi ngày chậm là demand rơi vào tay bên thứ 3.

| # | Merchant | Tỉnh/TP | Danh mục | Organic Volume/tháng | Trending |
|---|---|---|---|---|---|
| 1 | Bún thịt nướng Chị Tuyền | HCM | F&B - Bún thịt nướng | 8.100 | - |
| 2 | Cơm tấm Ống Khói Diệu | An Giang | F&B - Cơm tấm | 4.400 | - |
| 3 | Hủ tiếu Mỹ Tho Thanh Xuân | HCM | F&B - Hủ tiếu | 1.300 | - |
| 4 | Bánh ướt Cây Me | Cần Thơ | F&B - Bánh ướt | 480 | - |
| 5 | Bột chiên A Tỷ | Đồng Nai | F&B - Bột chiên | 480 | - |
| 6 | Hủ tiếu Nam Vang Ông Hai Bầu | Đồng Nai | F&B - Hủ tiếu | 390 | Trending |
| 7 | Quán Cơm Chú Lùn | Cần Thơ | F&B - Cơm | 320 | Trending |
| 8 | Hương Giang Bakery | Bắc Ninh | F&B - Bánh | 320 | - |
| 9 | Hủ tiếu Nam Vang 69 | HCM | F&B - Hủ tiếu | 110 | - |
| 10 | Chả giò Phượng | Đồng Nai | F&B - Chả giò | 90 | - |
| 11 | Hải sản Ngô Thơ | Hải Phòng | F&B - Hải sản | 70 | Trending |
| 12 | Chả rươi Hằng Béo | Hà Nội | F&B - Chả rươi | 30 | - |
| 13 | Bánh mì Hữu Liêm | Cần Thơ | F&B - Bánh mì | 20 | Trending |
| 14 | Tiệm mì Chú Cao | HCM | F&B - Mì | 10 | - |
| 15 | Bún cá Tư Lùn | An Giang | F&B - Bún cá | 0 | - |
| 16 | Trà đá Mạnh Nháy | Bắc Ninh | F&B - Trà đá | 0 | - |
| 17 | Xôi Trường | Bắc Ninh | F&B - Xôi | 0 | - |
| 18 | Bánh mì Khánh Nạp | Hải Phòng | F&B - Bánh mì | 0 | - |
| 19 | Cô Hường Bún Chả | Hải Phòng | F&B - Bún chả | 0 | - |
| 20 | Bò nhúng Mắm ruốc 8 Còn | Bình Dương | F&B - Bò nhúng | 0 | - |
| 21 | Bò lá lốt mỡ chài chị Hằng | Bình Dương | F&B - Bò lá lốt | 0 | - |
| 22 | Bún thịt nướng cô Bế | Bình Dương | F&B - Bún thịt nướng | 0 | - |
| 23 | Miến lươn chân cầm | Hà Nội | F&B - Miến lươn | 0 | - |
| 24 | Mỳ Cường Thư | Thanh Hóa | F&B - Mì | 0 | - |
| | **Tổng Batch 2** | **11 tỉnh/TP** | F&B | **16.120** | |

14/24 merchants có branded search volume thực. 10 còn lại volume = 0 trong keyword tool nhưng OOH đang chạy - demand sẽ phát sinh. Launch song song OOH để capture ngay, không để rơi vào tay bên thứ 3.

**Scale-up post-pilot:**
- 500+ đối tác (phủ 80% lượng giao dịch SME)
- 1.000+ đối tác qua pSEO

---

## 8. Success Metrics

**North Star Metric:** O2O Activations từ /merchant (VTS activation + Soundbox adoption, attributed via Appsflyer).

| Metric | Target (90 ngày post-launch) | Source |
|---|---|---|
| Organic Traffic | Duy trì 85K/quý (không giảm net vs 2 legacy systems) | GSC |
| VTS Module CTR | 3% baseline từ Pilot | Umami |
| Soundbox inquiry từ /merchant | Baseline TBD | Umami |
| Top queries "{Merchant} + MoMo" | 80% rank Top 5 | GSC |
| QR scan → Page view (O2O offline signal) | Baseline từ UTM tracking | Umami |

**Conversion Funnel:**
```
/merchant/{slug} page view
  -> O2O CTA click (VTS / Hoàn tiền / Soundbox)
    -> App open (Onelink)
      -> Activation (VTS kích hoạt / Soundbox đăng ký)
        -> Transaction
```

---

## 9. Dependencies & Constraints

| Dependency | Mô tả | Blocker? | PIC |
|---|---|---|---|
| VTS merchant list (updated) | List merchants chấp nhận VTS - quyết định hiển thị VTS badge | Có | PO VTS team |
| VTS Terms Data | Lãi suất, hạn mức, phí - YMYL, sai data = legal risk | Có | PO VTS team |
| Soundbox merchant list | Merchants dùng Soundbox để ưu tiên onboard pilot | Có | BD/Soundbox team |
| Cashback campaign data | Merchants đang chạy hoàn tiền để inject Promotion Module | Không (có thể launch trước) | Campaign team |
| Review sync mechanism | Source review data: MoMo internal / Google Places / other. TBD | Có nếu dùng Template A | PO + Hiến confirm |
| PAGE_ID → Merchant mapping | Export từ Thổ Địa DB cho legacy audit + redirect | Có | Hiến request |
| MoSpark platform readiness | LP Builder sẵn sàng với 2 template variants + KV slot | Có | Hoài Anh |
| AI Image pipeline (Image-to-Image) | Tool/model retouch ảnh thô → KV chuẩn brand. Input: ảnh thô từ BD/SME. Output: fill MoSpark KV slot tự động | Có | Trọng (cùng GenAI pipeline) |
| Ảnh thô merchant | BD team thu thập khi lắp Soundbox, hoặc SME cung cấp. Không có ảnh thô = không có KV AI | Có | BD/Soundbox team |
| GenAI Content pipeline | Template + prompts cho merchant content (Long Content + FAQ + HowTo) | Không (đang chạy) | Trọng |
| Deep Link specs per merchant | Onelink URLs cho O2O CTAs | Có | DA team |
| Umami tracking setup | Track page view, O2O CTA click, QR scan, scroll depth. Phải có trước launch | Có | Thuận |
| Sub-pages data requirements | Xác nhận loại sub-pages và data source | Không - Phase 2 | Nhật + Hiến |

**Constraints:**
- Content production trên MoSpark - không custom development
- GenAI Content (Long Content + FAQ) phải qua review/edit trước publish - không auto-publish
- AI-generated KV phải qua review trước publish - không auto-apply
- VTS badge chỉ gắn sau khi verify với PO team - không dựa trên blog data
- Soundbox CTA chỉ hiển thị với SME merchants được BD team xác nhận
- Schema markup inject qua MoSpark template - không hardcode
- Không có ảnh thô = không có KV AI. Không deploy trang nếu thiếu KV (brand guideline gate)
- Sub-pages chỉ tạo khi có đủ data - không tạo placeholder rỗng
- Inbound không làm việc trực tiếp với Web Platform - mọi technical request qua SEO & GEO Lead

---

## 10. Action Plan - SME Merchant URL Migration (Batch 2 + Extended)

> **Scope:** 38 SME Soundbox merchants - Batch 2 gốc (24) + mở rộng thêm 14 trong chiến dịch Mega 2026. Batch 1 (Top Brand Chains) xử lý riêng sau khi pilot SME hoàn tất.
> **Nguyên tắc slug:** `{ten-merchant}-{id}` - tên merchant kebab-case không dấu, kết thúc bằng ID backend tự assign.
> **Redirect rule:** 308 Permanent (không dùng 301 - giữ method). 3 merchants có legacy /page/ URL vẫn cần set redirect dù page mới đã live.
> **Status cập nhật:** 2026-05-29 - Toàn bộ 38 trang đã live.

### 10.1 Launch Matrix - Toàn bộ 38 SME Merchants (Live)

| # | Merchant | Tỉnh/TP | URL cũ | URL thực tế | Redirect Status |
|---|---|---|---|---|---|
| 1 | Bún thịt nướng Chị Tuyền | HCM | `/page/9819516` | `/merchant/bun-thit-nuong-chi-tuyen-44` | **308 PENDING** |
| 2 | Cơm tấm Ống Khói Diệu | An Giang | Không có | `/merchant/com-tam-ong-khoi-dieu-45` | Clean |
| 3 | Hủ tiếu Mỹ Tho Thanh Xuân | HCM | Không có | `/merchant/hu-tieu-my-tho-thanh-xuan-69` | Clean |
| 4 | Bánh ướt Cây Me | Cần Thơ | Không có | `/merchant/banh-uot-cay-me-can-tho-48` | Clean |
| 5 | A Tỷ mì xào giòn - Bột chiên | Đồng Nai | Không có | `/merchant/a-ty-mi-xao-gion-bot-chien-64` | Clean |
| 6 | Hủ tiếu Nam Vang Ông Hai Bầu | Đồng Nai | Không có | `/merchant/hu-tieu-nam-vang-ong-hai-bau-75` | Clean |
| 7 | Quán Cơm Chú Lùn | Cần Thơ | Không có | `/merchant/quan-com-chu-lun-47` | Clean |
| 8 | Hương Giang Bakery | Bắc Ninh | Không có | `/merchant/huong-giang-bakery-bac-ninh-63` | Clean |
| 9 | Hủ tiếu Nam Vang 69 | HCM | Không có | `/merchant/hu-tieu-nam-vang-69-50` | Clean |
| 10 | Chả giò Phượng | Đồng Nai | Không có | `/merchant/cha-gio-phuong-dong-nai-56` | Clean |
| 11 | Hải sản Ngô Thơ | Hải Phòng | Không có | `/merchant/hai-san-ngo-tho-55` | Clean |
| 12 | Chả rươi Hằng Béo | Hà Nội | `/page/9843228` | `/merchant/cha-ruoi-hang-beo-51` | **308 PENDING** |
| 13 | Bánh mì Hữu Liêm | Cần Thơ | Không có | `/merchant/banh-mi-huu-liem-can-tho-49` | Clean |
| 14 | Tiệm mỳ Chú Cao | HCM | Không có | `/merchant/tiem-my-chu-cao-46` | Clean |
| 15 | Bún cá Tư Lùn | An Giang | Không có | `/merchant/bun-ca-tu-lun-54` | Clean |
| 16 | Trà đá Mạnh Nháy | Bắc Ninh | Không có | `/merchant/tra-da-manh-nhay-bac-ninh-53` | Clean |
| 17 | Xôi Trường | Bắc Ninh | Không có | `/merchant/xoi-truong-bac-ninh-52` | Clean |
| 18 | Bánh mì Cây Khánh Nạp | Hải Phòng | Không có | `/merchant/banh-mi-cay-khanh-nap-70` | Clean |
| 19 | Bún chả Cô Hường | Hải Phòng | Không có | `/merchant/bun-cha-co-huong-58` | Clean |
| 20 | Lẩu Mắm ruốc 8 Còn | Bình Dương | `/page/9949928` | `/merchant/lau-mam-ruoc-8-con-80` | **308 PENDING** |
| 21 | Bò lá lốt Chị Hằng | Bình Dương | Không có | `/merchant/bo-la-lot-chi-hang-68` | Clean |
| 22 | Bún thịt nướng Cô Bế | Bình Dương | Không có | `/merchant/bun-thit-nuong-co-be-71` | Clean |
| 23 | Miến lươn chân cầm | Hà Nội | Không có | `/merchant/mien-luon-chan-cam-72` | Clean |
| 24 | Mỳ Cường Thư | Thanh Hóa | Không có | `/merchant/mi-cuong-thu-thanh-hoa-65` | Clean |
| 25 | Tiệm chè Hữu Hoa | Cần Thơ | Không có | `/merchant/tiem-che-huu-hoa-can-tho-66` | Clean |
| 26 | Miến gà Cô Nhân | - | Không có | `/merchant/mien-ga-co-nhan-59` | Clean |
| 27 | Cơm tấm Đi Đức | - | Không có | `/merchant/com-tam-di-duc-57` | Clean |
| 28 | Quán Cô Hai Thượng | - | Không có | `/merchant/quan-co-hai-thuong-62` | Clean |
| 29 | Cháo bò Ô Lien | Đà Nẵng | Không có | `/merchant/chao-bo-o-lien-da-nang-73` | Clean |
| 30 | Bún chả cá Hòn | - | Không có | `/merchant/bun-cha-ca-hon-74` | Clean |
| 31 | Bún mắm Đi Liên | Đà Nẵng | Không có | `/merchant/bun-mam-di-lien-da-nang-76` | Clean |
| 32 | Cháo sườn Cô La | Hà Nội | Không có | `/merchant/chao-suon-co-la-ha-noi-77` | Clean |
| 33 | Giò chả Bà Bình | - | Không có | `/merchant/gio-cha-ba-binh-78` | Clean |
| 34 | Nộm bò khô Long Vị Dũng | - | Không có | `/merchant/nom-bo-kho-long-vi-dung-79` | Clean |
| 35 | Hàng chè Bà Thơm | - | Không có | `/merchant/hang-che-ba-thom-60` | Clean |
| 36 | Cafe bột lồng ly | - | Không có | `/merchant/cafe-bot-long-ly-81` | Clean |
| 37 | Quán lươn Xuân Leo | - | Không có | `/merchant/quan-luon-xuan-leo-61` | Clean |
| 38 | Nem chua Phượng Chi Lê | - | Không có | `/merchant/nem-chua-phuong-chi-le-67` | Clean |

**3 legacy /page/ URLs cần 308 redirect ngay (PENDING - tuần 1 tháng 6):**
- `/page/9819516` → `/merchant/bun-thit-nuong-chi-tuyen-44`
- `/page/9843228` → `/merchant/cha-ruoi-hang-beo-51`
- `/page/9949928` → `/merchant/lau-mam-ruoc-8-con-80`

### 10.2 Lưu Ý Kỹ Thuật

- **GSC Coverage:** 38 pages đã live nhưng indexing chưa verify. Check GSC Coverage Report tuần 2 T6.
- **Redirect timing:** 3 /page/ URLs chưa redirect dù page mới đã live - đây là gap cần close ngay. Không để quá 7 ngày.
- **Canonical:** Page `/merchant/{slug}` phải có self-referencing canonical. Kiểm tra trước khi đóng ticket.
- **Sitemap:** Verify 38 URLs mới đã được add vào sitemap. 3 /page/ URLs cần xóa khỏi sitemap cùng lúc set redirect.
- **Sitemap:** Thêm `/merchant/{slug}` vào sitemap ngay khi live. Xóa URL cũ khỏi sitemap cùng lúc set redirect.

---

## Appendix A: Template Examples

### Template D - SME Basic (Quán Cơm Chú Lùn)

**URL:** `momo.vn/merchant/quan-com-chu-lun-can-tho-24`
**Template:** D (Non-KV, Non-review)
**Category:** Quán ăn

**Title:** Quán Cơm Chú Lùn Cần Thơ - Thanh toán MoMo & Ưu đãi | MoMo
**H1:** Quán Cơm Chú Lùn - Thanh toán qua MoMo, xem ưu đãi Ví Trả Sau

**Payment Methods:** Ví MoMo - Quét QR | Ví Trả Sau - Mua trước trả sau | Ngân hàng liên kết - Quét QR

**FAQ:**
> Q: Quán Cơm Chú Lùn có nhận thanh toán MoMo không?
> A: Có. Quán Cơm Chú Lùn nhận thanh toán MoMo qua quét mã QR tại quầy.
>
> Q: Quán Cơm Chú Lùn có nhận Ví Trả Sau không?
> A: Có. Bạn có thể dùng Ví Trả Sau tại Quán Cơm Chú Lùn - mua trước trả sau 0% lãi suất.
>
> Q: Cách thanh toán MoMo tại Quán Cơm Chú Lùn?
> A: Mở app MoMo → chọn "Mã thanh toán" → đưa mã QR cho nhân viên quét → xác nhận thanh toán.

---

### Template A - Premium (Highlands Coffee)

**URL:** `momo.vn/merchant/highlands-coffee`
**Template:** A (Có KV, Có Review sync)
**Category:** Cà phê

**Title:** Highlands Coffee - Thanh toán & Ưu đãi MoMo | MoMo
**H1:** Highlands Coffee - Thanh toán qua MoMo, xem ưu đãi & Ví Trả Sau

**Payment Methods:** Ví Trả Sau - Mua trước trả sau | Ví MoMo - Quét QR | Ngân hàng liên kết - Quét QR

**FAQ:**
> Q: Highlands Coffee có nhận thanh toán qua MoMo không?
> A: Có. Highlands Coffee chấp nhận MoMo tại tất cả cửa hàng trên toàn quốc, bao gồm Ví MoMo, Ví Trả Sau, và QR ngân hàng liên kết.
>
> Q: Highlands Coffee có nhận Ví Trả Sau không?
> A: Có. Bạn có thể dùng Ví Trả Sau tại Highlands - mua trước trả sau 0% lãi, hạn mức đến 20 triệu.
>
> Q: Cách thanh toán MoMo tại Highlands Coffee?
> A: Mở app MoMo → chọn "Mã thanh toán" → đưa mã QR cho nhân viên quét → xác nhận thanh toán.
>
> Q: Highlands Coffee có ưu đãi MoMo nào đang chạy?
> A: Mở app MoMo để xem ưu đãi mới nhất tại Highlands Coffee.
>
> Q: Thanh toán Highlands bằng MoMo có an toàn không?
> A: Có. MoMo là ví điện tử được Ngân hàng Nhà nước cấp phép, bảo mật theo chuẩn PCI DSS.

---

## Change Log

- **2026-05-29 (v2.5):** Cập nhật Template System - từ 4 variants (KV/Non-KV × Review/Non-review) còn 2 variants (With Review / Without Review). Mọi merchant đều có KV AI-generated (Image-to-Image từ ảnh thô). Thêm AI Image pipeline vào Dependencies. Cập nhật page structure: KV là thành phần bắt buộc slot 1. Thêm constraint: không có ảnh thô = không deploy trang.
- **2026-05-29 (v2.4):** Cập nhật Section 10 - Launch Matrix với actual live URLs của 38 merchants (từ 24 Batch 2 gốc, mở rộng thêm 14). Chuyển status toàn bộ sang "Live". Flag 3 legacy /page/ URLs chưa được redirect (PENDING). Cập nhật scope Version từ 2.0 sang 2.4.
- **Tháng 5/2026 (v2.3):** Re-audit SERP toàn bộ 24 SME merchants. Phát hiện thêm 2 merchants có /page/ đang index: Chả rươi Hằng Béo (/page/9843228) và Bò nhúng Mắm ruốc 8 Còn (/page/9949928). Cập nhật Action từ "Clean launch" sang "308 Redirect" cho cả 2. Tổng merchants cần 308 redirect: 3/24.
- **Tháng 5/2026 (v2.2):** Thêm Section 10 - Action Plan URL Migration cho 24 SME Batch 2. Redirect matrix đầy đủ: URL cũ, URL mới đề xuất, action type. Nguồn: SERP audit site:momo.vn lần 1 - phát hiện Bún thịt nướng Chị Tuyền (/page/9819516).
- **Tháng 5/2026 (v2.1):** Confirm Standalone Microsite - gỡ Related Merchants module, bổ sung Standalone principle vào Section 5.4. Thêm Xu (Reward) vào O2O stack (TBD Q3+). Bổ sung Timeline (Q2 Mega / Long Term SME comm), O2O Behavior Shift 2 chiều (Online→Offline / Offline→Online), tam giác End User - MoMo - Merchant. Cập nhật PIC GenAI Content: Trọng.
- **Tháng 5/2026 (v2.0):** Refactor toàn bộ theo định hướng chiến lược mới từ họp với Bảo (25/05/2026). Thêm SME Digital Presence angle, Dual-sided value prop (SME + Consumer), Template System 4 variants (KV/non-KV x Review/non-review), O2O Stack mở rộng (Hoàn tiền + VTS + Soundbox), Comm Activities 3 channels (SEO + QR + LLM/GEO), Sub-pages concept (Phase 2), Review sync (TBD). Cập nhật PIC: Nhật (Build Lead), Hoài Anh (MoSpark Architecture). Cập nhật scale pilot 100-200 merchants.
- **Tháng 5/2026 (v1.7):** Cập nhật Tracking: Umami + PIC Thuận. Bổ sung PIC column vào Dependencies.
- **Tháng 5/2026 (v1.6):** Xóa Tracking Event Schema + AB Test - thuộc PRD/Action Plan.
- **Tháng 5/2026 (v1.5):** Xóa Risk Assessment - thuộc PRD/Action Plan.
- **Tháng 5/2026 (v1.4):** Thêm Problem Statement, Tracking Event Schema, AB Test.
- **Tháng 5/2026 (v1.3):** Tích hợp Batch 2 - 24 SME Soundbox Merchants, fix URL /doi-tac → /merchant.
- **Tháng 5/2026 (v1.2):** Bổ sung Content Production Scale, chuẩn hóa cấu trúc.
- **Tháng 5/2026 (v1.0):** Khởi tạo tài liệu.
