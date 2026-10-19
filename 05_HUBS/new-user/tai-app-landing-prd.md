# PRD: Trang Tải Ứng Dụng MoMo Chính Thức (/tai-app)

> - **Dự án:** New User Hub & Web-to-App Acquisition - Web Platform
> - **Đơn vị phụ trách:** Web Platform Team x Growth Platform Division (GPD)
> - **Đường dẫn chuẩn (URL Schema):** `momo.vn/tai-app`
> - **Trạng thái:** P0 Priority Sprint (Tháng 10/2026)
> - **Mục tiêu:** Thuần túy là Trung tâm Tiện ích Tải Ứng dụng (Utility Software Download Center), tách biệt hoàn toàn với trang Tiếp thị Khuyến mãi / Thẻ quà

---

## I. TỔNG QUAN & BỐI CẢNH CHIẾN LƯỢC

### 1.1 Điểm Nghẽn Kỹ Thuật Trang `/download` Hiện Hữu & Phân Tách Quyền Sở Hữu (Ownership Decoupling)
- **Thực trạng trang `/download`:** Hiện tại `momo.vn/download` là mã script chuyển hướng (Client-side Redirect) cổ điển từ phiên bản v3.1 (`utm_campaign=momov3.1`), chạy hàm JavaScript thô `whatos()` và `autodetectOS()`. Khi mở trên máy tính (Desktop), logic rẽ nhánh tự động ép người dùng chuyển hướng sang trang web Google Play Store, hoàn toàn không có giao diện hiển thị, không có mã QR và không có thẻ SEO.
- **Ràng buộc với ITC:** Trang `/download` đang được ITC sử dụng trong các phiên bản App cũ để điều hướng người dùng cập nhật ứng dụng (Update App) khi có phiên bản mới hoặc bảo trì. Can thiệp trực tiếp vào `/download` sẽ gây rủi ro đứt gãy luồng vận hành của ITC.
- **Chiến lược phân tách (Decoupling):** Giữ nguyên `/download` cho mục tiêu kỹ thuật In-App Update của ITC; xây dựng mới hoàn toàn `momo.vn/tai-app` trên nền tảng MoSpark do Web Platform sở hữu 100%, phục vụ mục tiêu SEO tự nhiên và chuyển đổi Web-to-App.

### 1.2 Khoảng Trống Thị Trường (Market White Space)
- **Thực trạng đối thủ:** Khảo sát trực tiếp bằng mã phản hồi HTTP (`curl -I`) cho thấy 100% đối thủ ví điện tử và ngân hàng số tại Việt Nam (ZaloPay, Viettel Money, VNPay, MBBank) **không có trang Tải Ứng Dụng độc lập chuẩn mực** (các đường link đều trả về 404 hoặc redirect 301 về trang chủ). Các đối thủ chỉ gắn icon Store ở chân trang hoặc viết bài blog hướng dẫn cài đặt.
- **Cơ hội chiến lược:** Xây dựng `momo.vn/tai-app` chuẩn mực giúp MoMo chiếm trọn 100% thị phần tìm kiếm tự nhiên (Organic Search Dominance) cho nhóm từ khóa có ý định tải ứng dụng cao (*tải app momo, cài đặt ví momo, tải momo cho iphone/android, momo apk*).

### 1.3 Chuẩn Hóa Điểm Rơi Mặc Định Của OneLink (OneLink Desktop Fallback)
- Thiết lập `momo.vn/tai-app` làm URL đích mặc định trên môi trường máy tính (`af_web_dp`) cho toàn bộ hệ thống AppsFlyer OneLink của MoMo. Khi người dùng mở link quảng cáo/chia sẻ trên máy tính, thay vì bị văng về trang chủ gây loãng thông tin, người dùng sẽ thấy ngay mã Dynamic QR Code để quét tải app trong 5 giây.

---

## II. SƠ ĐỒ LUỒNG NGƯỜI DÙNG & BẢNG PHÂN TÍCH BƯỚC

```mermaid
graph TD
    A["Người dùng tìm kiếm Google / Bấm OneLink Fallback từ Desktop / Bấm chuyển từ /download"] --> B["Website momo.vn/tai-app (Nhận diện thiết bị tự động)"]
    B --> C1{"Môi trường truy cập"}
    C1 -->|"Desktop / Laptop"| D1["Hiển thị Dynamic QR Code OneLink + 2 Store Badges + Link Direct APK"]
    C1 -->|"Mobile iOS"| D2["Hiển thị Nút CTA chính 'Tải trên App Store' + Sticky Bottom Button"]
    C1 -->|"Mobile Android"| D3["Hiển thị Nút CTA chính 'Tải trên Google Play' + Nút phụ 'Tải file APK'"]
    D1 --> E1["Quét mã QR bằng Camera điện thoại"]
    D2 --> E2["1 Chạm mở Apple App Store"]
    D3 --> E3["1 Chạm mở Google Play Store hoặc tải trực tiếp file APK"]
    E1 --> F["Tải & Cài đặt App MoMo Chính Thức (M-Service)"]
    E2 --> F
    E3 --> F
```

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Bước</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Giai Đoạn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Trải Nghiệm Người Dùng (UX)</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Hạ Tầng / Cơ Chế Kỹ Thuật</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nền Tảng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tiếp nhận truy cập</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Truy cập từ Google Search, OneLink Fallback hoặc banner từ trang `/download`. Tốc độ tải tức thì (LCP &lt; 1.5s).</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">MoSpark Next.js Server-Side Rendering + Edge CDN Caching</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Nhận diện thiết bị (Device Detection)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Không cần thao tác chọn thủ công; hệ thống tự nhận diện iOS, Android hoặc Desktop để hiển thị đúng CTA.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">User-Agent Parsing &amp; Client Viewport Detector</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Kích hoạt luồng tải (Action Trigger)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Desktop: Quét mã QR to bản giữa màn hình.<br>Mobile: Bấm 1 chạm vào nút Store chính hoặc nút tải APK.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">AppsFlyer OneLink Smart Script + Dynamic QR Generator</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Web Platform x AppsFlyer</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">4</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cài đặt an toàn</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Mở trực tiếp trang MoMo chính thức trên App Store / Google Play hoặc tải bộ cài APK có chữ ký số M-Service.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Official Stores / MoMo CDN Direct APK (Signed)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">App Stores &amp; Infra</td>
    </tr>
  </tbody>
</table>

---

## III. MA TRẬN JOBS TO BE DONE (JTBD)

- **Nguyên tắc thiết kế cốt lõi:** **Zero Marketing Noise** - Loại bỏ 100% nội dung giới thiệu thẻ quà, sự kiện khuyến mại hoặc bài viết tin tức. Toàn bộ trang tập trung vào mục tiêu duy nhất: Tải ứng dụng an toàn, đúng thiết bị, nhanh nhất.

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Nhóm JTBD</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Mô Tả Nhu Cầu Của Người Dùng</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giải Pháp Đáp Ứng Trên Trang /tai-app</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Functional Job</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tìm kiếm và tải ứng dụng MoMo chính thức phù hợp với hệ điều hành điện thoại.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Tự nhận diện iOS / Android; cung cấp mã Dynamic QR cho Desktop và link tải APK cho máy chuyên biệt.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Trust &amp; Security Job</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảo đảm không tải nhầm ứng dụng giả mạo, mã độc lừa đảo tiền bạc hoặc đánh cắp mã OTP.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khẳng định pháp nhân phát hành M-Service JSC, chứng nhận bảo mật quốc tế PCI DSS Level 1 và cấp phép NHNN.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Technical Information Job</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Biết rõ ứng dụng có tương thích với phiên bản máy hiện tại không trước khi bấm tải.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bảng thông số kỹ thuật minh bạch: Yêu cầu hệ điều hành tối thiểu, dung lượng bộ nhớ và phiên bản phát hành.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Troubleshooting Job</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Cần hướng dẫn nhanh khi gặp sự cố không tải được từ Store hoặc cần cài file APK.</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Khối hướng dẫn kỹ thuật dạng Accordion: Hướng dẫn cài APK, xử lý bộ nhớ đầy và giải thích quyền hệ thống.</td>
    </tr>
  </tbody>
</table>

---

## IV. CẤU TRÚC GIAO DIỆN UI/UX & NỘI DUNG KỸ THUẬT

### 4.1 Khung Điều Hướng Tối Giản (Zero Navigation Header)
- Bỏ 100% Mega Menu và các đường dẫn phân tán.
- Chỉ hiển thị: Logo MoMo (bên trái) và nhãn xác thực `Kênh Tải Ứng Dụng Chính Thức của M-Service` (bên phải).

### 4.2 Hero Conversion Block (Trung Tâm Tải Ứng Dụng)
- **Tiêu đề chính (H1):** `Tải Ứng Dụng MoMo Cho Mọi Thiết Bị`
- **Mô tả ngắn:** `Phiên bản chính thức mới nhất cho điện thoại iOS và Android. Cài đặt nhanh chóng, an toàn và bảo mật.`
- **Trải nghiệm Desktop (Split Screen):**
  - Cột trái: Tên phiên bản hiện hành, dung lượng ứng dụng, yêu cầu hệ điều hành và chứng nhận an toàn.
  - Cột phải: Khung mã Dynamic QR Code kích thước lớn kèm chỉ dẫn *"Mở camera trên điện thoại để quét mã QR và tải ứng dụng ngay lập tức"*. Bên dưới là huy hiệu chính thức của App Store, Google Play và liên kết `Tải trực tiếp file APK cho Android`.
- **Trải nghiệm Mobile (100% Above the Fold):**
  - Tự động hiển thị 1 nút hành động chính (Primary CTA Button) tương ứng với hệ điều hành: `Tải ngay trên App Store` (với iOS) hoặc `Tải ngay trên Google Play` (với Android, kèm nút phụ tải file APK).
  - Ghim nút bấm tải cố định ở đáy màn hình (Sticky Bottom CTA) khi cuộn trang.

### 4.3 Bảng Thông Số Kỹ Thuật Phiên Bản (Technical Specs)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Thông Số Kỹ Thuật</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phiên Bản Cho iOS</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Phiên Bản Cho Android</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Phiên bản hiện tại</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v4.2.x (Đồng bộ theo bản phát hành mới nhất)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">v4.2.x (Đồng bộ theo bản phát hành mới nhất)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Yêu cầu hệ điều hành tối thiểu</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">iOS 13.0 trở lên (Tương thích iPhone, iPad)</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Android 7.0 trở lên</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Dung lượng cài đặt xấp xỉ</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~180 MB</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">~95 MB (hoặc bản APK rút gọn)</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Nhà phát triển chính thức</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M-SERVICE JSC</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">M-SERVICE JSC</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;"><strong>Định dạng phân phối</strong></td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Apple App Store Bundle</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Google Play Bundle / Direct APK</td>
    </tr>
  </tbody>
</table>

### 4.4 Ma Trận Cửa Ngõ Phân Phối (Official Distribution Matrix)
1. **Apple App Store:** Nút chuyển tiếp trực tiếp vào ứng dụng MoMo chính thức trên App Store.
2. **Google Play Store:** Nút chuyển tiếp vào Google Play Store.
3. **Bộ cài đặt APK trực tiếp (Direct APK):** Lưu trữ trên CDN chính thức của MoMo, có chữ ký số xác thực của M-Service, phục vụ người dùng sử dụng thiết bị Android không có sẵn Google Mobile Services (như máy Huawei, máy xách tay).

### 4.5 Khối Hướng Dẫn Kỹ Thuật & Khắc Phục Sự Cố (Troubleshooting Accordion)
Tích hợp 3 câu hỏi kỹ thuật chuẩn cấu trúc dữ liệu JSON-LD Schema `FAQPage`:
- *Cách cài đặt file APK MoMo trên điện thoại Android?* (Hướng dẫn bật cho phép cài đặt nguồn tin cậy trong Cài đặt).
- *Điện thoại báo không đủ dung lượng khi tải MoMo thì xử lý thế nào?* (Hướng dẫn xóa bộ nhớ tạm để giải phóng tối thiểu 300MB).
- *MoMo yêu cầu những quyền hệ thống nào khi cài đặt lần đầu?* (Giải thích quyền Camera để quét QR/eKYC và quyền Thông báo để nhận biến động số dư).

---

## V. CẤU HÌNH KỸ THUẬT & PHÂN LUỒNG HỆ THỐNG

### 5.1 Cấu Hình AppsFlyer OneLink Master Fallback
- Thiết lập quy tắc chuyển hướng mặc định trên toàn hệ thống OneLink:
  ```
  af_web_dp = https://momo.vn/tai-app?utm_source=onelink_desktop_fallback
  ```
- Chấm dứt hoàn toàn tình trạng mở OneLink trên máy tính bị rơi về trang chủ `momo.vn` hoặc bị ép nhảy vào Google Play web như hiện tại.

### 5.2 Điểm Chạm Chuyển Tiếp Từ Trang `/download`
- Giữ nguyên toàn bộ mã nguồn và logic chuyển tiếp của trang `/download` để phục vụ ITC.
- Chèn thêm một Banner điều hướng trang nhã ở vị trí đầu trang `/download`:
  `"Bạn là người dùng mới hoặc cần cài đặt lại ứng dụng? Đến Trang Tải Ứng Dụng Chính Thức -> momo.vn/tai-app"`
- Cấu hình thẻ chuẩn hóa SEO trên `/tai-app`:
  ```html
  <link rel="canonical" href="https://momo.vn/tai-app" />
  ```

### 5.3 Bảng Mã Đo Lường Sự Kiện (Umami & Analytics Tracking)
Tuân thủ chuẩn SSOT `04_MOSPARK_PLATFORM/umami_utility_tracking.md`:

| Tên sự kiện (Event Name) | Loại sự kiện | Tham số ghi nhận (Custom Parameters) | Mục đích đo lường |
| :--- | :--- | :--- | :--- |
| `tai_app_page_view` | Pageview | `device: desktop \| ios \| android`, `referrer` | Đo lường lưu lượng truy cập phân rã theo thiết bị. |
| `click_store_download` | Click | `store: appstore \| googleplay \| direct_apk` | Đo lường tỷ lệ nhấp nút tải về Store / APK. |
| `desktop_qr_scan_intent` | Interaction | `trigger: impression \| view_duration` | Đo lường số lượt hiển thị mã Dynamic QR trên máy tính. |
| `troubleshoot_toggle` | Click | `item: install_apk \| memory_error \| permissions` | Đo lường mức độ quan tâm đến hướng dẫn kỹ thuật. |

---

## VI. LỘ TRÌNH TRIỂN KHAI & CHỈ SỐ MỤC TIÊU (ROADMAP & KPIS)

### 6.1 Lộ Trình Triển Khai (Roadmap)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.9em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Giai đoạn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:center; font-weight:700;">Thời gian</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Tên Giai Đoạn</th>
      <th style="border:1.5px solid #64748b; padding:8px 12px; text-align:left; font-weight:700;">Chi Tiết Triển Khai &amp; Mục Tiêu Kỹ Thuật</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sprint 1</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Tuần 3 Tháng 10/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">UI/UX Design &amp; OneLink Setup</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Hoàn thiện thiết kế Wireframe (Split Screen Desktop + Sticky Bottom Mobile). Cấu hình Template OneLink Dynamic QR và thiết lập <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">af_web_dp</code> về <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tai-app</code>.</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sprint 2</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Tuần 4 Tháng 10/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Development &amp; MoSpark Release</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Phát triển trang trên MoSpark (Next.js + MoBase Design Token). Tích hợp link CDN file APK có chữ ký số. Gắn đầy đủ Umami Event Tracking.</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Sprint 3</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:center;">Đầu Tháng 11/2026</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Traffic Cutover &amp; SEO Submission</td>
      <td style="border:1px solid #94a3b8; padding:8px 12px; text-align:left;">Bổ sung Banner điều hướng từ <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/download</code> sang <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tai-app</code>. Submit sitemap và FAQ JSON-LD Schema lên Google Search Console để xác lập Top 1 thứ hạng tìm kiếm.</td>
    </tr>
  </tbody>
</table>

### 6.2 Chỉ Số Đo Lường Hiệu Suất (KPI Targets)
- **Tốc độ tải trang Core Web Vitals:** LCP < 1.5 giây, CLS = 0.
- **Tỷ lệ chuyển đổi Click-to-Store (CVR):** Đạt >= **45.0%** trên tổng lượt truy cập trang.
- **Tỷ lệ quét mã Dynamic QR trên Desktop:** Đạt >= **20.0%** trên tổng lượt truy cập từ thiết bị máy tính.
- **Thứ hạng SEO từ khóa kỹ thuật:** Lọt Top 1 - 3 Google Search cho cụm từ khóa: *tải app momo, cài đặt momo, momo apk, download momo*.
