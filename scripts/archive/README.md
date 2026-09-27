# scripts/archive - FROZEN (không dùng cho code mới)

Thư mục này chứa 99 script một lần (one-off) đã chạy xong cho roadmap Excel.
Quy ước từ 17/09/2026:

- Không import từ archive, không sửa file trong này để tái sử dụng.
- Cần logic tương tự: viết script mới ở root hoặc `scripts/` dùng `scripts/_lib.py` (có backup và `--dry-run`).
- File trùng đã gộp: bản duy nhất của `generate_pptx.py` và `generate_report_html.py` nằm ở `scripts/`, bản trong `07_REPORTS/scripts/` chỉ là shim.
- `analyze_h1.py` bản gốc đã chuyển vào `scripts/archive/oneoffs/`.
