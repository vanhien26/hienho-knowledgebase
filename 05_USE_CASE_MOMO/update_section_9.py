import re

file_path = "/Users/hienhv/Documents/Obsidian_Vault/hovanhien_knowledgebase_momo/05_USE_CASE_MOMO/doi-tac-brd.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

section_9_pattern = r"(## 9\. Dependencies & Constraints\n\n\| Dependency \|.*?)\n---\n\n## 10\."
match = re.search(section_9_pattern, content, re.DOTALL)

if not match:
    print("Could not find section 9")
    exit(1)

old_section = match.group(1)

new_section = """## 9. Dependencies & Constraints

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
"""

new_content = content.replace(old_section, new_section)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated Section 9 successfully.")
