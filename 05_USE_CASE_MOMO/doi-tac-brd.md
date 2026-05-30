# BRD: Merchant Detail Page - SME Digital Presence Platform

> - **Project:** Merchant Detail Page (SME Digital Presence + O2O Ecosystem)
> - **Main URL:** momo.vn/merchant
> - **Division:** GPD (Growth Platform Division)
> - **Use Case:** Merchant Pages
> - **Owner:** GPD - Out-App Traffic
> - **Governance:** Web Product Lead
> - **PIC Build:** Nhật (Build Lead) - Hoài Anh (MoSpark Architecture)
> - **Version:** 2.0 - May 2026
> - **Status:** Pilot Phase - Foundation Build (100-200 Merchants)

---

> **Problem:** MoMo có hàng nghìn merchant nhưng không có trang web giúp user xác nhận và kích hoạt O2O - traffic intent cao đang rơi vào tay bên thứ 3. Đồng thời SME nhỏ không có Digital Presence để xuất hiện trên Web và AI - hoàn toàn vô hình khi user search.
> **KPI Owned:** VTS Activations + O2O Engagement từ `momo.vn/merchant` (attributed via Appsflyer + Umami)
> **Consumer Flow:** "{Merchant} có nhận MoMo không?" → `/merchant/{slug}` → O2O CTA click → App open → Activation → Transaction
> **SME Value Prop:** Xuất hiện miễn phí trên momo.vn (Web) + AI Agent responses - Digital Assets không cần chi phí marketing

---

## 1. Executive Summary

### Situation

Hai vấn đề song song trong một kiến trúc.

**Phía Consumer:** User search "{Merchant} có nhận Ví Trả Sau không" là nhóm có purchase intent cao nhất có thể capture trên Web - họ đã chọn merchant, đã chọn phương thức thanh toán, chỉ cần một xác nhận. MoMo không có trang nào serve được intent này ở cấp độ merchant cụ thể. 85K organic traffic/quý đang chảy vào 2 legacy systems không có conversion goal: `/thanh-toan-momo-{merchant}` (18K, content outdated 5-7 năm) và `https://www.momo.vn/page/{id}` (67K, thin content không cập nhật).

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

### Job #2 (Consumer - Core Mega JTBD): "Hoàn tiền 50% ở đâu?"

> "Tôi thấy quảng cáo Trả Sau Hoàn Sâu 50%. Quán {Merchant} này có được áp dụng hoàn tiền 50% khi quét Ví Trả Sau không? Xung quanh tôi có quán nào khác đang hoàn tiền không?"

*Vì dự án này là nền tảng trực tiếp cho chiến dịch Mega 2026 (VTS x SME), JTBD quan trọng cốt lõi nhất của người dùng không chỉ dừng lại ở việc hỏi "Có thanh toán được không?", mà là săn tìm **"Hoàn tiền 50% ở đâu?"**.*

| Dimension | Nội dung |
|---|---|
| Functional | Xác định nhanh chóng quán ăn có áp dụng ưu đãi Hoàn 50% của Ví Trả Sau. |
| Emotional | Cảm giác "Săn được deal hời", ăn uống tiết kiệm thông minh. Tránh bực bội vì thanh toán xong mới biết quán không có hoàn tiền. |
| Social | Share link quán rủ bạn bè/đồng nghiệp đi ăn chung vì đang có deal hoàn 50% rất hời. |
| Trigger | Bị kích thích bởi Billboard OOH/Digital Ads (Mega Campaign), hoặc đang đói và chủ động tìm deal. |

**Giải pháp:** Giao diện `/merchant/{slug}` phải đẩy mạnh Badge/KV "Hoàn tiền 50% với VTS" lên vị trí nổi bật nhất. Mọi nội dung text và hình ảnh sinh ra từ GenAI Banana Pro đều phải hook vào keyword "Hoàn 50%".

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

### 5.3 Template System - Role Permission & JTBD

**3 trục quyết định template:** KV (Key Visual) - Review (sync) - AI Tools (enable/disable)

| Template | KV | Review | AI Tools | Role assign | Target Merchant |
|---|---|---|---|---|---|
| **A - Premium** | Có (brand asset) | Có (sync) | Không | Platform Admin only | Brand chain lớn: Highlands, BHX, Grab |
| **B - Brand** | Có (brand asset) | Không | Không | Platform Admin + Senior PM | Chain merchants có visual identity, chưa có review sync |
| **C - SME Review** | Không (category default) | Có (Google Places API) | Không | Mọi PM | SME trending, có review data từ Google |
| **D - SME Basic (AI-Powered)** | GenAI logo/image | Không | **Có** | Mọi PM / Auto-assign | SME cơ bản, ít thông tin - AI tạo toàn bộ assets |

**Lý do restrict Role assign cho Template A/B:** Template A/B gắn với brand chain có data pháp lý phức tạp (VTS terms, promotion data, verified merchant status). Platform Admin phải verify merchant trước khi assign template này. PM thường không đủ context để assign đúng.

**JTBD Consumer - UI/UX sắp xếp theo từng Template:**

| Template | Consumer JTBD chính | Prioritize trên UI | Xuống sau |
|---|---|---|---|
| A - Premium | "Xác nhận brand quen nhận MoMo + tìm ưu đãi tốt nhất" | Review block + VTS promo + KV prominent | Story/Long content |
| B - Brand | "Tìm thông tin chain + confirm thanh toán được" | KV + Payment methods + Branch locator (nếu có) | Review, Story |
| C - SME Review | "Tìm SME trending - kiểm tra review + nhận MoMo không" | Review aggregate + Payment confirm | O2O stack |
| D - SME Basic | "Xác nhận quán quen nhận MoMo" | Payment methods ngay đầu trang + Story (AI) + O2O | Review (không có) |

**Review Sources (theo Template):**

| Source | Template áp dụng | Approach | Ghi chú |
|---|---|---|---|
| Google Places API | C, A (fallback) | Batch fetch monthly, cache, hiển thị "Đánh giá từ Google" + Google branding | Paid API - $17/1000 requests. Phải attribution đúng theo ToS |
| MoMo transaction rating | A, C (Phase 2) | Internal review data nếu merchant có rating từ giao dịch MoMo | Cần xác nhận availability với data team |
| Không có review | B, D | Không hiển thị Review Block | Không tạo placeholder empty |

> **Scraping Google Maps: KHÔNG làm.** Vi phạm Google ToS, rủi ro pháp lý, không ổn định. Approach đúng là Google Places API (có trả phí, có attribution, ổn định).

**Template mở rộng Phase 2 (TBD):**
- **E - Service/Professional:** Bác sĩ, tiệm sửa xe, salon - JTBD là book lịch/liên hệ, không phải payment-first. Contact CTA nổi bật thay vì VTS.
- **F - Retail/Shop:** Cửa hàng bán lẻ - showcase sản phẩm, VTS prominent (mua trước trả sau), price range visible.

### 5.4 Merchant Detail Page Structure

**Nguyên tắc Standalone Microsite:** Mỗi `momo.vn/merchant/{slug}` là một Microsite độc lập - không cross-link sang merchant khác, không hiển thị merchant liên quan. Mỗi trang tự hoàn chỉnh về nội dung và O2O value prop. SEO strength đến từ domain authority momo.vn + schema riêng của từng trang, không phụ thuộc vào internal linking giữa các merchant.

Mỗi `momo.vn/merchant/{slug}` gồm 2 phần tách biệt:

- **Merchant Content (Long Content):** Nội dung giới thiệu merchant, FAQ, HowTo. Do GenAI Content Engine sản xuất và phải qua editorial review trước publish. Không auto-publish.
- **Platform Modules:** Payment Methods, O2O Promotions. Inject tự động từ MoSpark template, fix cứng để đảm bảo tính pháp lý.

| # | Thành phần | Loại | Chi tiết |
|---|---|---|---|
| 1 | NAP (Merchant Data) | Platform Data | Logo/KV (nếu có), Tên Merchant, Category, SĐT, Địa chỉ, Hours |
| 2 | Payment Methods | Platform Module | MoMo/VTS/QR - fix từ merchant data |
| 3 | O2O Promotion Stack | Platform Module (Fix cứng) | VTS Card + Hoàn tiền + Soundbox CTA (tùy merchant có sản phẩm tương ứng) |
| 4 | Review Block | Platform Module (conditional) | Aggregate rating + số review - chỉ hiển thị nếu Template A hoặc C |
| 5 | Long Content | GenAI Content | Bài viết 150-300 từ giới thiệu chuyên sâu về merchant |
| 6 | FAQ & HowTo | GenAI + editor review | Câu hỏi thường gặp + hướng dẫn thanh toán step-by-step |

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

### 5.8 AI-Powered SME Marketing Tools

> **CEO's Vision:** *"SME nhỏ nhất - quán bún, tiệm chè, xe xôi - đều có thể chia sẻ trang MoMo của mình trong bữa ăn gia đình và cảm thấy tự hào."*

SME Batch 2 (38 merchants) và toàn bộ SME pipeline về sau có một vấn đề thực tế: **không có ảnh, không có logo, không có nội dung marketing**. Template D (SME Basic) không thể làm việc được nếu input data gần như rỗng.

Giải pháp: MoSpark AI Tools cung cấp 3 công cụ tích hợp vào quy trình onboarding SME, giúp merchant yếu thế có trang truyền thông đẹp - không cần biết thiết kế hay copywriting.

**Tool 1 - Logo & Hero Image GenAI:**

| Field | Chi tiết |
|---|---|
| Input | Tên merchant, Danh mục (F&B/Retail/Service), Style preference (truyền thống/hiện đại/vui tươi), USP cốt lõi (ví dụ: "bánh bèo Huế", "lâu đời"). |
| Output | 3-5 logo variants (PNG transparent) + 1-2 hero image (KV) theo chuẩn cấu trúc chuyển đổi O2O. |
| KV Template | Hình chân dung chủ quán realistic + Text "Tên Quán + USP" (VD: "Quán Cô Hai Thương 66 năm giữ phong vị bánh bèo Huế") + Banner MoMo Ví Trả Sau. |
| Apply cho | Template D. Kết quả lưu vào NAP block thay thế "category default visual" |
| Technology | **GenAI Banana Pro của Gemini** - Đảm bảo hình ảnh realistic, ánh sáng đẹp, tích hợp text tiếng Việt chính xác lên banner. |
| Gate | PM review + chọn 1 variant trước khi apply. Merchant không tự chọn (Phase 1). |

**Tool 2 - Merchant Story GenAI:**

| Field | Chi tiết |
|---|---|
| Input | Tên merchant, Năm thành lập (nếu có), Đặc trưng món/dịch vụ, 1-2 câu từ chủ quán (optional), Tỉnh/TP |
| Output | Merchant story 150-300 từ (narrative form, warm tone, không marketing-speak), FAQ 3-5 cặp hỏi đáp |
| Apply cho | Template C và D |
| Technology | Claude API (same pipeline với GenAI Content Engine) |
| Context injection | Business Context auto-fill từ merchant data (tên, category, VTS status, payment methods) |
| Gate | **PM QC/QA bắt buộc trước publish** (xem Section 5.9) |

**Tool 3 - Social Share Kit (CEO's Vision):**

| Field | Chi tiết |
|---|---|
| Mục tiêu | SME chủ quán có thể share link trang của họ trên Zalo/Facebook - thumbnail đẹp, professional |
| Output | OG Image tự động generate: merchant name + logo + "Nhận thanh toán MoMo" + category icon |
| OG metadata | `og:title` = "{Tên Merchant} - Thanh toán MoMo" / `og:image` = generated OG image URL |
| UTM tracking | Shareable URL kèm `?utm_source=sme_share&utm_medium=social&utm_content={merchant_id}` |
| Trigger | Auto-generate khi page publish. Regenerate nếu merchant info update. |
| Dành cho ai | Merchant chủ quán nhận link page của mình và share - không cần setup gì |

**Quy trình AI Tools trong onboarding SME:**

```
1. PM nhập merchant data tối thiểu (tên, địa chỉ, SĐT, category)
2. Hệ thống trigger AI Tools: Logo GenAI + Story GenAI chạy song song
3. PM review kết quả AI (xem Section 5.9 QC/QA Flow)
4. PM chọn logo variant + edit story nếu cần
5. Publish → Social Share Kit auto-generate OG image
6. MoMo gửi link page cho merchant → merchant share với gia đình/khách hàng
```

### 5.9 QC/QA Flow - PM Role trong Quản trị Merchant Page

**Vấn đề:** Merchant page chứa thông tin có tính pháp lý (VTS terms, địa chỉ, SĐT, giờ mở cửa) và AI-generated content (có thể hallucinate chi tiết sai). Cần PM review trước khi page live - không auto-publish.

**3 lớp kiểm tra:**

| Lớp | Nội dung kiểm tra | Ai làm | Gate |
|---|---|---|---|
| **L1 - Data Accuracy** | Tên merchant đúng, SĐT đúng, địa chỉ đúng, category đúng, VTS status đúng theo list PO VTS | PM | Hard block nếu VTS status không khớp với PO VTS list |
| **L2 - AI Content Review** | Story không có thông tin sai (ngày mở, số chi nhánh, giải thưởng chưa verify), FAQ không có cam kết pháp lý ngoài scope MoMo, không đề cập competitor | PM | Warning - PM edit trực tiếp trước approve |
| **L3 - Legal/Policy** | VTS data chỉ từ nguồn PO VTS (không AI generate VTS terms), Soundbox CTA chỉ hiển thị nếu BD confirm, không có điều khoản tài chính ngoài template fix | PM + SEO Lead sign-off | Hard block |

**Workflow trong Editor:**

```
[Draft Page] 
    → PM mở review mode
    → L1 Data Accuracy checklist (tự check, tick từng item)
    → L2 AI Content (đọc + edit inline nếu cần)
    → L3 Legal/Policy (checklist auto-validate VTS data source)
    → PM click "Gửi duyệt"
    → SEO Lead sign-off (cho Template A, B; optional cho C, D nếu PM confident)
    → Publish
```

**Template D (SME Basic) streamlined flow:** Do SME Basic không có VTS/complex legal content, flow rút ngắn hơn: L1 + L2 đủ để publish, không cần SEO Lead sign-off mandatory.

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

**Batch 2 - SME Soundbox - Mega 2026 OOH Comm (38 đối tác - URGENT):**

38 merchant SME đang được truyền thông OOH trên 11 tỉnh trong chiến dịch "Trả Sau Hoàn Sâu" (Mega 2026). OOH đang chạy nhưng chưa có trang MoMo nào hứng search demand - mỗi ngày chậm là demand rơi vào tay bên thứ 3.

> **Đã gộp bảng dữ liệu vào Section 10.1 (SME Batch 2 Matrix) bên dưới.**

14/38 merchants có branded search volume thực. 24 còn lại volume = 0 trong keyword tool nhưng OOH đang chạy - demand sẽ phát sinh. Launch song song OOH để capture ngay, không để rơi vào tay bên thứ 3.

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

Đã được cấu trúc lại để team dễ tracking các Blockers thực sự.

### 9.1 Hard Blockers (Dependencies)

| Domain | Yêu cầu bắt buộc (Block Launch) | PIC |
|---|---|---|
| **O2O & Legal Data** | Dữ liệu VTS (Merchant list, Lãi suất, Phí) phải chuẩn 100% (YMYL rule).<br>Danh sách Soundbox merchant phải được BD confirm. | PO VTS, BD |
| **Platform Infra** | MoSpark Builder sẵn sàng với 4 Templates + Phân quyền Role (Admin/PM). | Hoài Anh |
| **Tracking & SEO** | Setup xong Umami (O2O CTR, QR Scan) & Mapping OA-ID chính xác để set 308 redirect. | Thuận, Nhật |
| **QC/QA Gate** | PM được assign bắt buộc phải check L1 Data Accuracy trước khi publish. | Nhật, PO |
| **Review API** | Tích hợp Google Places API (có billing/attribution) hoặc MoMo Internal API. | Hoài Anh |

*(Các hạng mục không block launch: Sub-pages data (Phase 2), Cashback campaign, GenAI Content Pipeline).*

### 9.2 Strict Constraints (Nguyên tắc cấm kỵ)

1. **No Custom Code:** 100% content và schema markup phải chạy qua MoSpark Builder Template. Không hardcode.
2. **No Auto-Publish:** Mọi GenAI content (Story/FAQ) bắt buộc qua editor review. VTS badge chỉ được gắn khi có confirm từ BU.
3. **No Google Maps Scraping:** Tuyệt đối không crawl data lậu vi phạm ToS. Chỉ dùng API chính thống.
4. **No Blind Redirect:** 308 redirect chỉ được kích hoạt khi OA-ID mapping đã verify thành công.
5. **Process Strict:** Template A (Premium) chỉ dành cho Platform Admin. Mọi Inbound request kỹ thuật phải qua Web Product Lead.

---

## 10. Action Plan - SME Merchant URL Migration (Batch 2)

> **Scope:** 38 SME Soundbox merchants thuộc chiến dịch Mega 2026 OOH. Batch 1 (Top Brand Chains) xử lý riêng sau khi pilot SME hoàn tất.
> **Nguyên tắc slug:** `{ten-merchant}-{id}` - tên merchant kebab-case không dấu, không tỉnh thành, kết thúc bằng ID backend tự assign. Ví dụ thực tế: `/merchant/bun-thit-nuong-chi-tuyen-44` (ID = 44).
> **Redirect rule:** 308 Permanent (không dùng 301 - giữ method). Áp dụng ngay khi /merchant/{slug} live, không để 2 URL tồn tại song song quá 7 ngày.

### 10.0 OA-ID Migration - Sync từ /page sang /merchant

**Owner:** Nhật (Build) + Hoài Anh (MoSpark Architecture)
**Trigger:** Chạy song song với Phase 1 pilot - không block launch nhưng phải complete trước khi set 308 redirect

#### Vấn đề

Hệ thống cũ `https://www.momo.vn/page/{id}` dùng Thổ Địa DB với Thổ Địa ID (PAGE_ID). Hệ thống mới `/merchant/{slug}` dùng MoMo Internal Merchant ID (OA-ID). Hai ID systems không tương đồng - cần bridge layer để attribution tracking và redirect hoạt động chính xác.

| Field | /page (Old System) | /merchant (New System) |
|---|---|---|
| Primary ID | PAGE_ID (e.g., 9819516) | OA-ID (MoMo Internal Merchant ID) |
| URL Pattern | /page/{PAGE_ID} | /merchant/{slug} |
| Data Source | Thổ Địa DB | MoMo Merchant DB |
| Umami tracking | Không có | Có (PIC: Thuận) |
| Merchant status | Stale - không cập nhật | Live - sync từ Merchant DB |

#### Migration Steps

1. Nhật xuất mapping table từ Thổ Địa DB: `PAGE_ID → OA-ID → Merchant Name → Slug đề xuất`
2. Hoài Anh verify OA-ID còn active trong MoMo Merchant DB (loại bỏ merchant đã off-board)
3. Hiến review slug format theo URL governance policy (`{ten-merchant}-{id}`, kebab-case, no diacritics)
4. Set 308 redirect TRƯỚC hoặc CÙNG LÚC `/merchant/{slug}` live - không để gap quá 7 ngày
5. Umami attribution bridge: traffic từ session cũ (/page) ghi attribution sang OA-ID mới trong analytics

#### Scope Batch 2 - Merchants cần OA-ID bridge

> Đã gộp toàn bộ vào bảng Tracking Matrix (Mục 10.1) bên dưới.


**Constraint cứng:** OA-ID bridge phải verified trước khi set 308 redirect. Nếu OA-ID chưa xác nhận active = HOLD redirect, không set blindly.

---

### 10.1 Redirect & Launch Matrix - SME Batch 2

| # | Merchant | Tỉnh/TP | Volume/tháng | URL cũ (momo.vn) | URL mới | Action | Status |
|---|---|---|---|---|---|---|---|
| 1 | Bún thịt nướng Chị Tuyền | HCM | 8.100 | `https://www.momo.vn/page/9819516` | `https://www.momo.vn/merchant/bun-thit-nuong-chi-tuyen-44` | 308 Redirect | **Live** |
| 2 | Cơm Tấm Ống Khói Điệu | An Giang | 4.400 | Không có | `https://www.momo.vn/merchant/com-tam-ong-khoi-dieu-45` | Clean launch | **Live** |
| 3 | Hủ tiếu Mỹ Tho Thanh Xuân | HCM | 1.300 | Không có | `https://www.momo.vn/merchant/hu-tieu-my-tho-thanh-xuan-69` | Clean launch | **Live** |
| 4 | Bánh ướt Cây Me | Cần Thơ | 480 | Không có | `https://www.momo.vn/merchant/banh-uot-cay-me-can-tho-48` | Clean launch | **Live** |
| 5 | Mì Xào Giòn A Tỷ | Đồng Nai | 480 | Không có | `https://www.momo.vn/merchant/a-ty-mi-xao-gion-bot-chien-64` | Clean launch | **Live** |
| 6 | Hủ tiếu Nam Vang Ông Hai Bầu | Đồng Nai | 390 | Không có | `https://www.momo.vn/merchant/hu-tieu-nam-vang-ong-hai-bau-{id}` | Clean launch | Chưa launch |
| 7 | Quán Cơm Chú Lùn | Cần Thơ | 320 | Không có | `https://www.momo.vn/merchant/quan-com-chu-lun-47` | Clean launch | **Live** |
| 8 | Hương Giang Bakery | Bắc Ninh | 320 | Không có | `https://www.momo.vn/merchant/huong-giang-bakery-bac-ninh-63` | Clean launch | **Live** |
| 9 | Hủ tiếu Nam Vang 69 | HCM | 110 | Không có | `https://www.momo.vn/merchant/hu-tieu-nam-vang-69-50` | Clean launch | **Live** |
| 10 | Chả giò Phượng | Đồng Nai | 90 | Không có | `https://www.momo.vn/merchant/cha-gio-phuong-dong-nai-56` | Clean launch | **Live** |
| 11 | Hải sản Ngô Thơ | Hải Phòng | 70 | Không có | `https://www.momo.vn/merchant/hai-san-ngo-tho-55` | Clean launch | **Live** |
| 12 | Chả rươi Hằng Béo | Hà Nội | 30 | `https://www.momo.vn/page/9843228` | `https://www.momo.vn/merchant/cha-ruoi-hang-beo-51` | 308 Redirect | **Live** |
| 13 | Bánh mì Hữu Liêm | Cần Thơ | 20 | Không có | `https://www.momo.vn/merchant/banh-mi-huu-liem-can-tho-49` | Clean launch | **Live** |
| 14 | Tiệm Mỳ Chú Cao | HCM | 10 | Không có | `https://www.momo.vn/merchant/tiem-my-chu-cao-46` | Clean launch | **Live** |
| 15 | Bún cá Tư Lùn | An Giang | 0 | Không có | `https://www.momo.vn/merchant/bun-ca-tu-lun-{id}` | Clean launch | Chưa launch |
| 16 | Trà đá Mạnh Nháy | Bắc Ninh | 0 | Không có | `https://www.momo.vn/merchant/tra-da-manh-nhay-bac-ninh-53` | Clean launch | **Live** |
| 17 | Xôi Trường | Bắc Ninh | 0 | Không có | `https://www.momo.vn/merchant/xoi-truong-bac-ninh-52` | Clean launch | **Live** |
| 18 | Bánh mì Khánh Nạp | Hải Phòng | 0 | Không có | `https://www.momo.vn/merchant/banh-mi-khanh-nap-{id}` | Clean launch | Chưa launch |
| 19 | Cô Hường Bún Chả | Hải Phòng | 0 | Không có | `https://www.momo.vn/merchant/bun-cha-co-huong-58` | Clean launch | **Live** |
| 20 | Bò nhúng Mắm ruốc 8 Còn | Bình Dương | 0 | `https://www.momo.vn/page/9949928` | `https://www.momo.vn/merchant/bo-nhung-mam-ruoc-8-con-{id}` | 308 Redirect | Chưa launch |
| 21 | Bò lá lốt mỡ chài chị Hằng | Bình Dương | 0 | Không có | `https://www.momo.vn/merchant/bo-la-lot-chi-hang-68` | Clean launch | **Live** |
| 22 | Bún thịt nướng cô Bế | Bình Dương | 0 | Không có | `https://www.momo.vn/merchant/bun-thit-nuong-co-be-{id}` | Clean launch | Chưa launch |
| 23 | Miến lươn chân cầm | Hà Nội | 0 | Không có | `https://www.momo.vn/merchant/mien-luon-chan-cam-{id}` | Clean launch | Chưa launch |
| 24 | Mỳ Cường Thư | Thanh Hóa | 0 | Không có | `https://www.momo.vn/merchant/mi-cuong-thu-thanh-hoa-65` | Clean launch | **Live** |
| 25 | Tiệm Chè Hữu Hòa | Cần Thơ | 0 | Không có | `https://www.momo.vn/merchant/tiem-che-huu-hoa-can-tho-66` | Clean launch | **Live** |
| 26 | Miến Gà Cô Nhẫn | HCM | 0 | Không có | `https://www.momo.vn/merchant/mien-ga-co-nhan-59` | Clean launch | **Live** |
| 27 | Cơm Tấm Dì Đức | Bình Dương | 0 | Không có | `https://www.momo.vn/merchant/com-tam-di-duc-57` | Clean launch | **Live** |
| 28 | Bánh Bèo Bánh Bột Lộc Cô Hai Thương | Bình Dương | 0 | Không có | `https://www.momo.vn/merchant/quan-co-hai-thuong-62` | Clean launch | **Live** |
| 29 | Cháo Bò O Liên | Đà Nẵng | 0 | Không có | `https://www.momo.vn/merchant/chao-bo-o-lien-{id}` | Clean launch | Chưa launch |
| 30 | Bún Chả Cá Hờn | Đà Nẵng | 0 | Không có | `https://www.momo.vn/merchant/bun-cha-ca-hon-{id}` | Clean launch | Chưa launch |
| 31 | Bún Mắm Dì Liên | Đà Nẵng | 0 | Không có | `https://www.momo.vn/merchant/bun-mam-di-lien-{id}` | Clean launch | Chưa launch |
| 32 | Cháo Sườn Cô Là | Hà Nội | 0 | Không có | `https://www.momo.vn/merchant/chao-suon-co-la-{id}` | Clean launch | Chưa launch |
| 33 | Giò Chả Bà Bính | Hà Nội | 0 | Không có | `https://www.momo.vn/merchant/gio-cha-ba-binh-{id}` | Clean launch | Chưa launch |
| 34 | Nộm Bò Khô Long Vi Dung | Hà Nội | 0 | Không có | `https://www.momo.vn/merchant/nom-bo-kho-long-vi-dung-{id}` | Clean launch | Chưa launch |
| 35 | Hàng Chè Bà Thơm | Hà Nội | 0 | Không có | `https://www.momo.vn/merchant/hang-che-ba-thom-60` | Clean launch | **Live** |
| 36 | Cafe Bọt Long Lý | Nghệ An | 0 | Không có | `https://www.momo.vn/merchant/cafe-bot-long-ly-{id}` | Clean launch | Chưa launch |
| 37 | Lươn Xuân Leo | Nghệ An | 0 | Không có | `https://www.momo.vn/merchant/quan-luon-xuan-leo-61` | Clean launch | **Live** |
| 38 | Nem Chua Phương Chi Lê | Thanh Hóa | 0 | Không có | `https://www.momo.vn/merchant/nem-chua-phuong-chi-le-67` | Clean launch | **Live** |

### 10.3 Lưu Ý Kỹ Thuật

- **GSC Verify:** SERP re-audit (site:momo.vn) lần 2 đã hoàn tất - phát hiện thêm 2 merchants có /page/. Tuy nhiên SERP chỉ trả về top kết quả, GSC Coverage Report vẫn cần verify để đảm bảo không bỏ sót, đặc biệt các merchants có volume > 0 nhưng không hiện trong SERP.
- **Redirect timing:** Set 308 TRƯỚC hoặc CÙNG LÚC page mới live. Không để gap giữa page mới live và redirect cũ.
- **Canonical:** Page mới `/merchant/{slug}` phải có self-referencing canonical. Page cũ sau khi redirect không cần canonical.
- **Sitemap:** Thêm `/merchant/{slug}` vào sitemap ngay khi live. Xóa URL cũ khỏi sitemap cùng lúc set redirect.

---

## Appendix A: Template Examples

### Template D - SME Basic (Quán Cơm Chú Lùn)

**URL:** `https://www.momo.vn/merchant/quan-com-chu-lun-47`
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

- **Tháng 5/2026 (v2.5):** Strategic update từ Bảo (sync 26/05/2026). (1) Section 5.3 rewrite với 3-axis template system + Role Permission: Template A = Platform Admin only, B = Admin+Senior PM, C/D = Mọi PM. JTBD consumer per template. Review Sources table. (2) Thêm Section 5.8 - AI-Powered SME Marketing Tools: Logo GenAI (3-5 variants), Merchant Story GenAI (Claude API pipeline), Social Share Kit (auto OG image, UTM tracking) - CEO vision operationalized: SME chia sẻ trang trong bữa ăn gia đình. (3) Thêm Section 5.9 - QC/QA Flow 3 layers: L1 Data Accuracy (hard block nếu VTS mismatch), L2 AI Content Review (warning + inline edit), L3 Legal/Policy (hard block, SEO Lead sign-off). Template D: L1+L2 only. (4) Section 9 Dependencies: Bổ sung Google Places API, PM QC/QA Role, cập nhật Review sync row. Thêm 3 constraints: Template A Platform Admin only, no Google Maps scraping, OA-ID bridge constraint. (5) Section 10: Thêm subsection 10.0 OA-ID Migration architecture - Nhật + Hoài Anh bridge PAGE_ID sang OA-ID trước khi set 308 redirect.
- **Tháng 5/2026 (v2.4):** Bổ sung 14 merchants mới từ CSV OOH Mega 2026 (nguồn: Master Tracker). Batch 2 tăng từ 24 lên 38 đối tác. Thêm 2 tỉnh mới: Đà Nẵng (3 merchants) và Nghệ An (2 merchants). Rename "Bột chiên A Tỷ" → "Mì Xào Giòn A Tỷ" theo tên chính thức. Thêm 14 rows vào Section 10 redirect matrix.
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
