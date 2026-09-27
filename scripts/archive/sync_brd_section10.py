import re

with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
    brd = f.read()

new_s10 = """## 10. LỘ TRÌNH TRIỂN KHAI THEO 3 GIAI ĐOẠN (PRODUCT ROADMAP 2026 - 2027)

<table style="width:100%; border-collapse:collapse; border:1.5px solid #64748b; margin:1em 0; font-size:0.85em;">
  <thead>
    <tr style="background-color:#f1f5f9;">
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Giai Đoạn</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Thời Gian</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Tên Dự Án / Module Trọng Tâm</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">URL Route / Sản Phẩm</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Dung Lượng / Tác Động</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:left; font-weight:700;">Chi Tiết Triển Khai & Nhiệm Vụ Kỹ Thuật</th>
      <th style="border:1.5px solid #64748b; padding:6px; text-align:center; font-weight:700;">Ưu Tiên</th>
    </tr>
  </thead>
  <tbody>
    <!-- PHASE 1 -->
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;" rowspan="5"><strong>Phase 1</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;" rowspan="5">Tháng 8 - 9/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 1: Master Gateway & Mega Navigation</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/tai-chinh</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">1,000,000+ PV/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Xây dựng Trang Cổng Trung Tâm, Dashboard thị trường tổng hợp, thanh điều hướng tài chính thống nhất (Global Nav) và danh mục 5 nhóm nhu cầu JTBD.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 2: Hero Widget Tính Lãi Tiết Kiệm Live</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tiet-kiem-online</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">230,110 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Tích hợp Widget tính lãi đơn gửi 1 lần & lãi kép gửi hàng tháng (1-24 tháng), cho phép kéo trượt số tiền linh hoạt và mở sổ online trực tiếp vào Bản Việt/VPBank.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 3: Bộ Đôi Công Cụ Thu Nhập & Thuế 2026</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tinh-luong</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/thue-tncn</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">1,350,140 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Phát triển Tool tính lương Gross - Net (áp dụng luật thuế mới 2026), Tool quyết toán thuế TNCN tự động, thanh trượt phân bổ thu chi 50/30/20 và CTA Ứng Lương / Túi Thần Tài.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 4: Cổng Tra Cứu CIC & Khám Sức Khỏe Tín Dụng</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tra-cuu-cic</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/xoa-no-xau</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">398,890 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Xây dựng Cổng tra cứu thông tin CIC chính thống, Widget tự đánh giá phân loại nhóm nợ 1-5, cẩm nang phục hồi điểm tín dụng và CTA Check Điểm Tín Dụng MoMo miễn phí 100%.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>
    <tr style="background-color:#eff6ff;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 5: Programmatic Bank Hub (34 Ngân Hàng & Napas)</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/ngan-hang/[slug]</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/napas</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">7,015,550 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Triển khai Programmatic template tự động cho 34 ngân hàng đối tác và Cổng chuyển tiền Napas 247. Tích hợp biểu phí, Swift code, hotline và hướng dẫn liên kết nhận quà 500k.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#b91c1c;">P0</td>
    </tr>

    <!-- PHASE 2 -->
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;" rowspan="6"><strong>Phase 2</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;" rowspan="6">Tháng 10 - 11/2026</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 6: Siêu Động Cơ Tra Cứu Giá Vàng Realtime</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/gia-vang</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">78,879,270 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Xây dựng bảng giá vàng realtime (SJC, PNJ, DOJI, 24K, 9999, Nhẫn trơn), biểu đồ biến động lịch sử 7-30 ngày, công cụ tính chênh lệch Mua - Bán và nút Mua Vàng Online.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1e40af;">P1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 7: Bộ Quy Đổi Ngoại Tệ & Tỷ Giá Live</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/ty-gia</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/ngoai-te</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">9,476,250 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Bộ công cụ quy đổi tiền tệ tức thì giữa 20+ ngoại tệ (USD, EUR, JPY...) và bảng tỷ giá so sánh chênh lệch giữa các ngân hàng thương mại, dẫn luồng mở thẻ quốc tế.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1e40af;">P1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 8: Bảng So Sánh Lãi Suất 30+ Ngân Hàng</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/lai-suat-ngan-hang</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">1,246,620 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Bảng so sánh đa chiều biểu lãi suất tiền gửi tiết kiệm theo kỳ hạn 1-36 tháng của 30+ ngân hàng, tích hợp bộ lọc ngân hàng có lãi suất cao nhất và mở sổ online.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1e40af;">P1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 9: Ma Trận So Sánh Thẻ Tín Dụng & Thẻ Quốc Tế</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/the-tin-dung</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/the-visa</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">656,330 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Ma trận so sánh quyền lợi hoàn tiền, phí thường niên của các dòng thẻ tín dụng ngân hàng đối tác và thẻ quốc tế Visa/Mastercard, tích hợp mở thẻ 100% online.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1e40af;">P1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 10: Máy Tính Trả Góp 0% & Đăng Ký Vay Nhanh</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/tra-gop</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/vay-tin-chap</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">632,170 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Máy tính trả góp 0% tổng quát cho mọi mặt hàng công nghệ/điện máy (kích hoạt Ví Trả Sau 20 triệu) và Công cụ tính lãi vay mua nhà/vay tín chấp dư nợ giảm dần.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1e40af;">P1</td>
    </tr>
    <tr style="background-color:#f8fafc;">
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 11: Trung Tâm Đầu Tư Quỹ Mở & Cổ Phiếu F0</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/chung-khoan</code> & <code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">/chung-chi-quy</code></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">4,183,460 search/tháng</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Công cụ 'Có Tiền Đầu Tư Gì?', Bộ giả lập Lãi kép tích lũy định kỳ SIP từ 10.000đ và cẩm nang kiến thức đầu tư chứng khoán cơ bản cho người mới bắt đầu.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700; color:#1e40af;">P1</td>
    </tr>

    <!-- PHASE 3 -->
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center; font-weight:700;" rowspan="3"><strong>Phase 3</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;" rowspan="3">Tháng 12/2026 - Q1/2027</td>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 12: AI Financial Pulse & News Stream</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;"><code style="background:#f1f5f9;padding:2px 4px;border-radius:4px;font-family:monospace;">momo.vn/tai-chinh</code> (Module Pulse)</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Tương tác Daily Active</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Hệ thống tự động hóa ingest tin tức tài chính, lọc nhiễu AI, tóm tắt 2 gạch đầu dòng và kết hợp alert biến động số liệu thị trường 24/7 (theo mô hình Finpath AI).</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">P2</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 13: Đóng Gói Toàn Diện Embeddable Widgets SDK</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Embed Component SDK</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Cross-sell Toàn Sàn</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Đóng gói 7 bộ công cụ tiện ích thành React Web Components nhúng linh hoạt vào mọi điểm chạm Web MoMo và hệ thống đối tác ngoài (Affiliate & Partner Web).</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">P2</td>
    </tr>
    <tr>
      <td style="border:1px solid #94a3b8; padding:6px;"><strong>Dự Án 14: Cá Nhân Hóa Thời Gian Thực & Phễu U18/F0</strong></td>
      <td style="border:1px solid #94a3b8; padding:6px;">Toàn bộ hệ thống Hub</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">Nâng CVR W2A +30%</td>
      <td style="border:1px solid #94a3b8; padding:6px;">Triển khai Real-time Personalization dựa trên self-declared intent của người dùng trên Web, tối ưu hóa hành trình kích hoạt cho phân khúc Sinh Viên (U18 - U23) và Nhà Đầu Tư F0.</td>
      <td style="border:1px solid #94a3b8; padding:6px; text-align:center;">P2</td>
    </tr>
  </tbody>
</table>
"""

s10_start = brd.find("## 10. LỘ TRÌNH")
if s10_start != -1:
    brd = brd[:s10_start] + new_s10
    with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
        f.write(brd)
    print("Successfully updated Section 10 in 05_HUBS/financial-hub-brd.md!")
else:
    print("Could not find section 10")
