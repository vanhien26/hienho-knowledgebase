# scripts/archive - FROZEN & ARCHIVED

Toàn bộ 132 script một lần (one-off) phục vụ các đợt cập nhật Roadmap/BRD từ tháng 6 đến tháng 9/2026 đã được đóng gói an toàn vào tệp nén:

```
scripts/archive.tar.gz
```

### Hướng dẫn giải nén khi cần tra cứu:
```bash
tar -xzf scripts/archive.tar.gz -C scripts/
```

### Quy ước vận hành:
- Không sử dụng các script cũ trong archive cho nghiệp vụ mới.
- Các công cụ hoạt động chính thức:
  - `scripts/cli.py` (Unified CLI Engine)
  - `scripts/sync_tracking_report.py` (Đồng bộ số liệu Tracking)
  - `scripts/lib/` (Thư viện tiện ích Excel & Markdown)
  - `scripts/tools/` (Engine sinh báo cáo HTML & PPTX)
