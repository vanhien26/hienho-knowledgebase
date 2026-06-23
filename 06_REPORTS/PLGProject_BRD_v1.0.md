# TÀI LIỆU YÊU CẦU NGHIỆP VỤ (BRD)
## PLG Project - MoMo Knowledge Base
### *Chuẩn hóa tri thức sản phẩm/dịch vụ MoMo theo SPA Framework — hạ tầng nền tảng cho mọi Web Product tận dụng tối đa AI-Powered PLG*

**Phiên bản:** 1.0  
**Ngày:** 15/05/2026  
**Sponsored by:** Hoàng Vũ Bảo (Head of Web Platform)  
**Module Owner:** Trọng (Technical Owner) · Hiến HV (Product Lead) · Duy (Chatbot)

---

## TÓM TẮT ĐIỀU HÀNH

**Là gì:** PLG Project là hạ tầng tri thức tập trung của MoMo - một knowledge base tối ưu RAG, được vector-index hóa, hệ thống hóa thông tin sản phẩm/dịch vụ để cung cấp trải nghiệm người dùng do AI điều khiển và thúc đẩy sản xuất nội dung quy mô lớn.

**Tại sao:** Trong kỷ nguyên AI, tri thức có cấu trúc = lợi thế cạnh tranh. Các Use-Cases của MoMo đang mất khả năng tiếp cận và hiển thị vào tay đối thủ đang chiếm lĩnh Search trước và được AI Chatbots ưu tiên trích dẫn. MoMo Knowledge Base giúp Web Platform xây dựng nền tảng tri thức chuẩn hóa để phục hồi và chiếm lĩnh vị thế đó — trên Google Search, TikTok, Facebook, AI Chatbots lẫn App MoMo.

**Làm thế nào:** Tiếp cận đa giai đoạn - xây dựng hạ tầng cốt lõi (Q2), tích hợp với quy trình SPA (Q3), mở rộng quy mô cho các BU (Q4+).

**Thành công:** Đến cuối 2026: 5+ PLG Projects đang hoạt động với 1,000+ Topic Clusters chất lượng được sản xuất đa dạng loại hình Content, được đánh giá và đo lường mức độ đóng góp vào tăng trưởng các mục tiêu của Web Platform.

---

## 1. BỐI CẢNH NGHIỆP VỤ

### 1.1 Căn Chỉnh Chiến Lược

**GPD Mandate:**
- O1: 6M Monthly Views → yêu cầu nội dung quy mô lớn
- O2: AI-powered Platform → PLG Project = hạ tầng AI
- PLG Model: Out-App Traffic → Web → App → MAU

**Chuyển Đổi Web Platform:**
- TỪ: Đội ngũ hỗ trợ kỹ thuật xây dựng website theo yêu cầu
- ĐẾN: Nhà cung cấp dịch vụ sản phẩm bán giải pháp tăng trưởng (SPA Framework)

**Vấn Đề:**
- Các BU có tri thức sản phẩm rải rác (docs, wikis, kiến thức ngầm)
- Không có cách hệ thống để làm cho tri thức có thể khám phá bởi AI
- Không thể mở rộng quy mô sản xuất nội dung mà không có hạ tầng tri thức
- Trải nghiệm chatbot/tìm kiếm phụ thuộc vào tri thức có cấu trúc

**Cơ Hội:**
- 179.3M lượt tìm kiếm/tháng trên 55 thị trường sản phẩm MoMo
- Các nền tảng tìm kiếm đa dạng (Google Search, TikTok, Facebook, AI Chatbots, App MoMo) đang thúc đẩy 20-30% lưu lượng khám phá
- Tri thức = kênh thu hút với chi phí biên bằng 0
- Lợi thế đi đầu: đối thủ thiếu hạ tầng tri thức

### 1.2 Bối Cảnh Thị Trường

**Chuyển Đổi Hành Vi Người Dùng (2025-2026):**
- Hành vi tìm kiếm đa nền tảng: Google Search, TikTok, Facebook, AI Chatbots (ChatGPT/Gemini/Claude), App MoMo → Người dùng khám phá thông tin trên mọi kênh
- SEO truyền thống → GEO (Generative Engine Optimization)
- Người dùng mong đợi câu trả lời tức thì, đàm thoại (chatbots)
- Tìm kiếm đa phương thức (giọng nói, hình ảnh, văn bản)

**Bối Cảnh Cạnh Tranh:**
- Ngân hàng (VPBank, TPBank): Xây dựng knowledge base cho giáo dục tài chính
- Ví điện tử (ZaloPay, ShopeePay): Chatbot FAQ, nhưng không hỗ trợ RAG
- Lợi thế MoMo: 179.3M cơ hội tìm kiếm + nền tảng AI-first

**Bối Cảnh Nội Bộ:**
- VTTI (Phạt Nguội, DVC, Billpay): 5.4M+ lượt tìm kiếm, cần hạ tầng tri thức
- SPS + FS (Ví Trả Sau): Tri thức về các Merchant chấp nhận thanh toán nguồn tiền MoMo (Ví Trả Sau, MoMo)
- Help Center: Hub thông tin hướng dẫn/hỏi đáp về các tính năng/tiện ích/dịch vụ của MoMo
- Nhiều Cell Team hỏi "Làm thế nào để phát triển các tiện ích, nội dung cho các Use-Cases của họ trên nền tảng Web MoMo để tiếp cận người dùng Out-App?" → PLG Project là câu trả lời

---

## 2. PRODUCT VISION & POSITIONING

### 2.1 Vision Statement

> "Build MoMo's single source of truth for product/service knowledge — structured, AI-ready, and distributed across every search surface (Google Search, TikTok, Facebook, AI Chatbots, App MoMo) — to fuel Product-Led Growth at scale."

### 2.2 Product Positioning

**NOT:**
- ❌ Just a chatbot platform
- ❌ Another CMS or documentation tool
- ❌ An SEO content factory

**BUT:**
- ✅ Enterprise knowledge infrastructure for Web Platform
- ✅ RAG-optimized, AI-native knowledge base
- ✅ Multi-channel distribution engine (web, chatbot, search, API)
- ✅ The knowledge foundation that powers every PLG project via SPA Framework

### 2.3 Value Proposition

**For BUs:**
> "Turn your product knowledge into a growth engine. We structure, enrich, and distribute it across every search surface — Google Search, TikTok, Facebook, AI Chatbots, App MoMo — driving MAU at near-zero marginal cost."

**For Users:**
> "Get instant, accurate answers about MoMo products and services — wherever you search: Google, TikTok, Facebook, AI Chatbots (ChatGPT/Gemini/Claude), or directly inside the MoMo App."

**For Web Platform:**
> "Activate the SPA Framework at scale. Without MoMo Knowledge Base, we build one-off websites. With it, we build reusable, AI-accessible knowledge that compounds over time."

---

## 3. MỤC TIÊU NGHIỆP VỤ

### 3.1 Mục Tiêu Chiến Lược (2026)

**O1: Kích Hoạt SPA Framework Quy Mô Lớn**
- Nghiên cứu, lựa chọn và đồng hành cùng 3-5 Strategic Projects của các Division hướng đến mục tiêu tăng trưởng, bao gồm: VTTI (Tra cứu Phạt Nguội, DVC, E-Sim), Payment/Financial Services (SPS, Loa Soundbox, Ví Trả Sau), Customer Service (Help Center), GPD (Landing Page, Merchant Page), MDS (Cinema, Promotion Hub, Donation)
- Tối ưu thời gian và chi phí sản xuất nội dung (text, KV, video...) xuống 5-10 lần
- Làm cho nội dung có thể tiếp cận người dùng trên các nền tảng Out-App (Search Engine, Social...)

**O2: Xây Dựng Lợi Thế Tri Thức MoMo**
- Hệ thống hóa tri thức cho 10+ danh mục sản phẩm
- Trở thành nguồn thông tin #1 về sản phẩm MoMo trên mọi nền tảng tìm kiếm (Google Search, TikTok, Facebook, AI Chatbots, App MoMo)
- Độ sâu tri thức = lợi thế cạnh tranh (khó sao chép)

**O3: Thúc Đẩy Tăng Trưởng MAU Có Thể Đo Lường**
- Gán thuộc tính: X% MAU mới đến từ các kênh tri thức
- Tự phục vụ: Giảm ticket CS Y% qua chatbot/help center
- Tương tác: Tăng thời gian trên site qua khám phá tri thức

### 3.2 Chỉ Số Thành Công (KPIs)

**Số Lượng Tri Thức:**
| Chỉ số | Q2 2026 | Q3 2026 | Q4 2026 |
|--------|---------|---------|---------|
| # Knowledge base BU | 2 (VTTI Phạt Nguội, VTTI DVC pilot) | 5 | 10 |
| # Bài viết được ingest | 200 | 500 | 1000+ |
| # Sản phẩm/dịch vụ được bao phủ | 5 | 15 | 30 |

**Chất Lượng Tri Thức:**
| Chỉ số | Mục tiêu | Đo lường |
|--------|--------|----------|
| Độ chính xác nội dung | >95% | Tỷ lệ validation BU |
| Độ tươi mới tri thức | <30 ngày | Trung bình ngày kể từ cập nhật cuối |
| Độ hoàn chỉnh bao phủ | >80% | % catalog sản phẩm có tri thức |

**Tiêu Thụ Tri Thức:**
| Chỉ số | Q2 2026 | Q3 2026 | Q4 2026 |
|--------|---------|---------|---------|
| Truy vấn chatbot/tháng | 5K | 20K | 50K |
| Tỷ lệ tự phục vụ | 60% | 70% | 80% |
| RAG API calls (từ GenAI, Help Center) | 10K | 50K | 100K |

**Tác Động Nghiệp Vụ:**
| Chỉ số | Q2 2026 | Q3 2026 | Q4 2026 |
|--------|---------|---------|---------|
| Monthly Views từ nội dung tri thức | 100K | 500K | 1M |
| MAU gán thuộc tính cho kênh tri thức | TBD | TBD | 5K+ |
| Giảm ticket CS | 5% | 10% | 20% |

---

## 4. YÊU CẦU CHỨC NĂNG

### 4.1 Khả Năng Cốt Lõi

#### **R1: Knowledge Ingestion (Tiếp Nhận Tri Thức)**

**R1.1 Import Đa Nguồn**
- Upload thủ công (docs, PDFs, markdown)
- API ingestion (từ GenAI Content Module)
- Bulk import (CSV, JSON)
- Web scraping (nội dung web hiện có)

**R1.2 Xử Lý Nội Dung**
- Trích xuất văn bản từ nhiều định dạng
- Auto-chunking để tối ưu vector indexing
- Trích xuất metadata (sản phẩm, category, tags, tác giả, ngày)
- Version control (theo dõi thay đổi, khả năng rollback)

**R1.3 Kiểm Soát Chất Lượng**
- Quy trình validation (draft → review → approved)
- Gán reviewer BU
- Theo dõi phê duyệt
- Phát hiện trùng lặp

**Ưu tiên:** P0 (Must-have cho Q2)

---

#### **R2: Lưu Trữ & Đánh Chỉ Mục Tri Thức**

**R2.1 Vector Database**
- Semantic embeddings cho toàn bộ nội dung
- Vector similarity search (truy vấn RAG)
- Hỗ trợ nhiều embedding models (OpenAI, Gemini)
- Truy xuất hiệu quả (<100ms p95 latency)

**R2.2 Cơ Sở Dữ Liệu Có Cấu Trúc**
- PostgreSQL cho metadata, relationships
- Schema: Products, Categories, Articles, Tags, Authors
- Khả năng full-text search
- Truy vấn quan hệ (tìm tất cả bài viết về Sản phẩm X)

**R2.3 Quản Lý Taxonomy**
- Cấu trúc category phân cấp (Products → Services → Topics)
- Hệ thống tag (metadata linh hoạt)
- Mối quan hệ sản phẩm (dependencies, các mục liên quan)
- Ánh xạ user persona

**Ưu tiên:** P0 (Hạ tầng cốt lõi)

---

#### **R3: Phân Phối Tri Thức (RAG API)**

**R3.1 Giao Diện Truy Vấn**
- RESTful API để truy xuất tri thức
- Semantic search endpoint (vector-based)
- Exact search endpoint (keyword-based)
- Hybrid search (kết hợp vector + keyword)

**R3.2 RAG Pipeline**
- Truy xuất context từ vector DB
- Xếp hạng mức độ liên quan
- Lắp ráp context cho LLM
- Tạo response (qua GenAI models)

**R3.3 Tiêu Thụ Đa Kênh**
- Tích hợp chatbot (Typebot + AI Assistant V2)
- GenAI Content Module (context cho tạo bài viết)
- Help Center (bài viết có cấu trúc)
- Semantic Search UI (tương lai)

**Ưu tiên:** P0 (Kích hoạt tất cả giao diện tiêu thụ)

---

#### **R4: UI Quản Lý Tri Thức**

**R4.1 Admin Dashboard**
- Xem tất cả knowledge base (theo BU, sản phẩm, category)
- Tìm kiếm & lọc bài viết
- Analytics dashboard (sử dụng, gaps, chất lượng)

**R4.2 Content Editor**
- Markdown editor cho tạo nội dung thủ công
- Giao diện metadata tagging
- Xem lịch sử version
- Preview trước khi publish

**R4.3 Quản Lý Workflow**
- Review queue (bài viết pending approval)
- Gán cho BU reviewers
- Phê duyệt/từ chối với comments
- Hệ thống thông báo

**Ưu tiên:** P1 (Quan trọng cho Q2, có thể bắt đầu cơ bản)

---

#### **R5: Phân Tích & Insights**

**R5.1 Usage Analytics**
- Chủ đề được truy vấn nhiều nhất (chatbot, RAG API)
- Knowledge gaps (truy vấn không có câu trả lời tốt)
- Hiệu suất nội dung (bài viết nào hữu ích nhất)
- Phân tích theo kênh (web vs chatbot vs API)

**R5.2 Chỉ Số Chất Lượng**
- Tỷ lệ validation (% approved vs rejected)
- Điểm freshness (tuổi trung bình của nội dung)
- Coverage map (% sản phẩm có tri thức)

**R5.3 Chỉ Số Nghiệp Vụ**
- Gán thuộc tính: MAU từ kênh tri thức
- Tỷ lệ tự phục vụ: % truy vấn chatbot được giải quyết
- CS deflection: tickets tránh được qua tự phục vụ

**Ưu tiên:** P1 (Quan trọng cho chứng minh ROI cho BUs)

---

### 4.2 Yêu Cầu Tích Hợp

#### **I1: Tích Hợp SPA Framework**

**Stage S (reSearch):**
- INPUT: Keyword research, phân tích đối thủ
- OUTPUT: Knowledge Gap Map, Taxonomy Blueprint

**Stage P (Pilot):**
- INPUT: 10-15 bài viết pilot từ GenAI Content
- PROCESS: Validation workflow → Ingestion → Vector indexing
- OUTPUT: Knowledge base ban đầu, sẵn sàng RAG

**Stage A (Action):**
- INPUT: 50-200 bài viết/tháng từ GenAI Content
- PROCESS: Auto-ingestion pipeline, bulk vector indexing
- OUTPUT: Knowledge base quy mô lớn, phân phối đa kênh

**Ưu tiên:** P0 (Workflow cốt lõi)

---

#### **I2: Tích Hợp GenAI Content Module**

**Luồng Hai Chiều:**

**GenAI → PLG Project (Producer):**
- GenAI tạo bài viết → API push đến PLG Project
- Auto-metadata tagging (sản phẩm, category, intent)
- Bulk ingestion endpoint

**PLG Project → GenAI (Consumer):**
- GenAI truy vấn PLG Project cho context (RAG)
- Truy xuất tri thức hiện có trước khi tạo nội dung mới
- Đảm bảo nhất quán qua các bài viết

**Ưu tiên:** P0 (Quan trọng cho sản xuất nội dung quy mô lớn)

---

#### **I3: Tích Hợp Chatbot**

**Typebot (Scripted):**
- Luồng được định nghĩa trước truy vấn PLG Project cho FAQ tĩnh
- Truy vấn exact match (keyword-based)

**AI Assistant V2 (Free-form):**
- Truy vấn người dùng → RAG pipeline → truy xuất tri thức liên quan
- LLM tạo câu trả lời với context PLG Project
- Citation links trở lại bài viết nguồn

**Ưu tiên:** P0 (Giao diện chính hướng người dùng)

---

#### **I4: Tích Hợp Help Center**

**Content Sync:**
- PLG Project = nguồn tin cậy
- Help Center hiển thị bài viết từ PLG Project
- Thay đổi trong PLG Project → auto-update trong Help Center

**Navigation:**
- Help Center taxonomy được điều khiển bởi PLG Project categories
- Search được cung cấp bởi PLG Project API

**Ưu tiên:** P1 (Nice-to-have Q2, must-have Q3)

---

#### **I5: Tích Hợp Full Funnel Tracking**

**Event Tracking:**
- Lượt xem bài viết tri thức (web, chatbot, help center)
- Query-to-answer latency
- Hành trình người dùng: Search → Knowledge → W2A → MAU

**Attribution:**
- Theo dõi MAU có nguồn gốc từ kênh tri thức
- Tính toán ROI tri thức (giá trị MAU / đầu tư tri thức)

**Ưu tiên:** P1 (Quan trọng cho chứng minh tác động nghiệp vụ)

---

## 5. YÊU CẦU PHI CHỨC NĂNG

### 5.1 Hiệu Suất

| Yêu cầu | Mục tiêu | Đo lường |
|---------|----------|----------|
| RAG query latency | <500ms p95 | API monitoring |
| Vector search | <100ms p95 | DB query time |
| Bulk ingestion | 100 bài viết/phút | Throughput pipeline |
| API availability | 99.5% uptime | Monthly uptime % |

### 5.2 Khả Năng Mở Rộng

- Hỗ trợ 10,000+ bài viết đến cuối 2026
- Xử lý 100K+ truy vấn RAG/ngày
- Nhiều dự án BU đồng thời (5+ knowledge base)

### 5.3 Bảo Mật & Quyền Riêng Tư

- RBAC: BU reviewers chỉ có thể xem/chỉnh sửa tri thức của họ
- Audit log: Tất cả thay đổi được theo dõi (ai, cái gì, khi nào)
- Mã hóa dữ liệu: At rest và in transit
- Xử lý PII: Đánh dấu nội dung nhạy cảm, hạn chế truy cập

### 5.4 Độ Tin Cậy

- Backup tự động (hàng ngày)
- Kế hoạch khắc phục thảm họa (RTO <4 giờ, RPO <1 giờ)
- Degradation nhẹ nhàng (nếu vector DB down, fallback sang keyword search)

### 5.5 Khả Năng Sử Dụng

- Admin UI: Trực quan cho BU reviewers không kỹ thuật
- API documentation: Rõ ràng, với ví dụ
- Error messages: Có thể hành động, thân thiện người dùng

---

## 6. USER STORIES & USE CASES

### 6.1 Personas Người Dùng Chính

**Persona 1: BU Product Owner (ví dụ: Hằng Mỵ - VTTI)**
- Nhu cầu: Xác thực độ chính xác tri thức sản phẩm, đảm bảo tuân thủ
- Pain: Không có cách hệ thống để tổ chức/cập nhật thông tin sản phẩm
- Mục tiêu: Tri thức sản phẩm thúc đẩy MAU, giảm tải CS

**Persona 2: Web Platform Content Producer (ví dụ: Hiến, Trọng)**
- Nhu cầu: Truy cập tri thức sản phẩm đã được xác thực để tạo nội dung
- Pain: Nghiên cứu lại cùng chủ đề nhiều lần, thông tin không nhất quán
- Mục tiêu: Sản xuất nội dung chính xác quy mô lớn, nhanh

**Persona 3: End User (khách hàng MoMo)**
- Nhu cầu: Câu trả lời nhanh, chính xác cho câu hỏi sản phẩm
- Pain: Không thể tìm thông tin, hoặc thông tin lỗi thời/không chính xác
- Mục tiêu: Tự phục vụ, không cần liên hệ CS

**Persona 4: PLG Project Admin (Duy, team content tương lai)**
- Nhu cầu: Quản lý quy trình tri thức, giám sát chất lượng/sử dụng
- Pain: Quy trình thủ công, khó mở rộng
- Mục tiêu: Hoạt động tri thức hiệu quả, tác động có thể đo lường

---

### 6.2 User Stories Chính

**Epic 1: Knowledge Ingestion**

**US1.1:** Là BU Product Owner, tôi muốn upload tài liệu sản phẩm (PDF/Word) để nó trở thành tri thức có thể tìm kiếm.  
**Acceptance Criteria:**
- Upload file qua UI
- Hệ thống trích xuất văn bản, tạo draft articles
- Tôi có thể review/edit trước khi publish

**US1.2:** Là Content Producer, tôi muốn bài viết do GenAI tạo tự động chảy vào PLG Project để tôi không phải upload thủ công từng bài.  
**AC:**
- GenAI Content Module gọi API để push bài viết
- Bài viết xuất hiện trong review queue
- Tôi có thể bulk-approve nếu chất lượng tốt

---

**Epic 2: Knowledge Retrieval (RAG)**

**US2.1:** Là Chatbot, tôi muốn truy xuất top 3 bài viết tri thức liên quan nhất cho truy vấn người dùng để tôi có thể cung cấp câu trả lời chính xác.  
**AC:**
- Gửi truy vấn qua API
- Nhận kết quả xếp hạng (vector similarity scores)
- Kết quả bao gồm văn bản bài viết + metadata (nguồn, ngày, sản phẩm)

**US2.2:** Là End User, tôi muốn chatbot trả lời câu hỏi VÀ hiển thị bài viết nguồn để tôi có thể đọc thêm nếu cần.  
**AC:**
- Câu trả lời chatbot bao gồm citation (tiêu đề bài viết, link)
- Click link mở bài viết đầy đủ trong Help Center hoặc web

---

**Epic 3: Quản Lý Chất Lượng Tri Thức**

**US3.1:** Là BU Product Owner, tôi muốn review bài viết mới/cập nhật trước khi chúng live để tôi đảm bảo độ chính xác.  
**AC:**
- Bài viết trong trạng thái "pending review" xuất hiện trong queue của tôi
- Tôi có thể approve, reject (với comment), hoặc yêu cầu chỉnh sửa
- Chỉ bài viết đã approve mới có thể truy cập RAG

**US3.2:** Là PLG Project Admin, tôi muốn xem bài viết nào đã lỗi thời (>90 ngày) để tôi có thể đánh dấu chúng để review.  
**AC:**
- Dashboard hiển thị báo cáo "stale content"
- Sắp xếp theo ngày cập nhật cuối
- Tôi có thể gán cho BU reviewer để refresh

---

**Epic 4: Analytics & ROI**

**US4.1:** Là BU Product Owner, tôi muốn xem có bao nhiêu người dùng tìm thấy câu trả lời qua nội dung tri thức (vs liên hệ CS) để tôi có thể chứng minh đầu tư.  
**AC:**
- Dashboard hiển thị tỷ lệ tự phục vụ (% truy vấn được giải quyết bởi chatbot)
- Xu hướng theo thời gian (cải thiện tháng qua tháng)
- Drill-down theo sản phẩm/chủ đề

**US4.2:** Là Web Platform Lead, tôi muốn gán thuộc tính MAU cho kênh tri thức để tôi có thể báo cáo ROI cho VP.  
**AC:**
- Full Funnel Tracking tag người dùng đến qua nội dung tri thức
- Tính toán đóng góp MAU (kênh tri thức)
- So sánh với kênh khác (Paid Media, Organic Search)

---

## 7. LỘ TRÌNH THEO GIAI ĐOẠN

### Phase 1: Nền Tảng (Q2 2026 - Tuần 19-26)

**Mục tiêu:** Hạ tầng cốt lõi live, 2 knowledge base BU pilot (VTTI Phạt Nguội, VTTI DVC)

**Deliverables:**
- [ ] Vector DB + PostgreSQL setup (Lộc)
- [ ] Knowledge ingestion API (Duy)
- [ ] RAG pipeline cơ bản (Duy + Trọng)
- [ ] Admin UI - CRUD cơ bản (Duy)
- [ ] Tích hợp: GenAI Content → PLG Project (Trọng)
- [ ] Tích hợp: PLG Project → Chatbot (Duy)
- [ ] Phạt Nguội knowledge base (140 bài viết ingested)
- [ ] DVC knowledge base (TBD bài viết từ research)

**Tiêu Chí Thành Công:**
- Chatbot có thể trả lời câu hỏi Phạt Nguội qua RAG
- GenAI Content sử dụng PLG Project context cho bài viết mới
- Hằng Mỵ (VTTI) xác thực chất lượng tri thức >90%

**Timeline:** 8 tuần (giữa tháng 5 đến giữa tháng 7)

---

### Phase 2: Quy Mô Production (Q3 2026)

**Mục tiêu:** 5 BU knowledge base, 500+ bài viết, quy trình sản xuất nội dung quy mô lớn

**Deliverables:**
- [ ] Quản lý workflow (review queue, approvals) (Duy)
- [ ] Analytics dashboard v1 (usage, quality metrics) (Duy + Hiếu)
- [ ] Tích hợp Help Center (Hùng + Duy)
- [ ] 3 Strategic Projects mới (Payment/Financial Services, Help Center, GPD/MDS)
- [ ] Programmatic SEO: PLG Project → landing page tự động tạo
- [ ] AI Assistant V2 (free-form chatbot) được cung cấp bởi PLG Project

**Tiêu Chí Thành Công:**
- 500+ bài viết qua 5 BUs
- Chatbot xử lý 20K truy vấn/tháng, 70% tỷ lệ tự phục vụ
- MAU attribution được theo dõi qua Full Funnel

**Timeline:** 12 tuần (giữa tháng 7 đến cuối tháng 9)

---

### Phase 3: Lớp Intelligence (Q4 2026)

**Mục tiêu:** PLG Project = nền tảng intelligence tri thức MoMo

**Deliverables:**
- [ ] Semantic Search UI (cổng tri thức hướng người dùng)
- [ ] Tự động phát hiện knowledge gap (AI phân tích truy vấn, xác định tri thức thiếu)
- [ ] Hỗ trợ đa ngôn ngữ (EN, VI)
- [ ] Knowledge API cho bên thứ ba (cho phép đối tác truy vấn tri thức MoMo)
- [ ] Analytics nâng cao (calculator ROI tri thức, insights hiệu suất nội dung)

**Tiêu Chí Thành Công:**
- 1000+ bài viết, 10 BU knowledge base
- 50K truy vấn chatbot/tháng, 80% tự phục vụ
- MAU có thể gán thuộc tính: 5K+/tháng từ kênh tri thức

**Timeline:** 12 tuần (tháng 10 đến cuối tháng 12)

---

## 8. MÔ HÌNH KINH DOANH & GIÁ (Nội Bộ)

### 8.1 Tiers Dịch Vụ (căn chỉnh với SPA Framework)

**Tier 1: Discovery (1-2 tuần)**
- **BU nhận được:** Knowledge Gap Analysis + Taxonomy Blueprint
- **BU đầu tư:** 1 buổi brief (60 phút)
- **Web Platform cung cấp:**
  - Keyword research → Yêu cầu tri thức
  - Cấu trúc taxonomy đề xuất
  - Scope ước tính (# bài viết, categories)
- **Giá (nội bộ):** Miễn phí (part of BU engagement)

---

**Tier 2: Pilot (2-4 tuần)**
- **BU nhận được:** Knowledge Base ban đầu (10-15 bài viết) + Chatbot pilot
- **BU đầu tư:** Review nội dung (2h/tuần)
- **Web Platform cung cấp:**
  - PLG Project setup cho BU
  - GenAI sản xuất 10-15 bài viết pilot
  - BU xác thực → bài viết được ingested
  - Chatbot có thể trả lời câu hỏi cơ bản
- **Giá (nội bộ):** Tính vào GPD OKRs (MAU attribution)

---

**Tier 3: Growth (Liên tục)**
- **BU nhận được:** Knowledge base quy mô lớn (50-200 bài viết/tháng) + Phân phối đa kênh
- **BU đầu tư:** Ngân sách SEO/SEM (cho vendor, nội dung, media)
- **Web Platform cung cấp:**
  - Quy trình tri thức production
  - Ingestion, indexing, distribution liên tục
  - Analytics & báo cáo ROI
- **Giá (nội bộ):** Phân bổ ngân sách BU (chi phí vendor), Web Platform headcount (GPD hấp thụ)

---

### 8.2 Tính Toán Giá Trị Cho BUs

**Khung ROI:**

**Đầu tư (BU):**
- Thời gian: 2h/tuần review nội dung (Tier 2+3)
- Ngân sách: Chi phí vendor SEO/SEM (chỉ Tier 3, ~$X,XXX/tháng)

**Lợi nhuận (BU):**
- MAU: X người dùng mới/tháng từ kênh tri thức
- CS Deflection: Y tickets/tháng tránh được (tiết kiệm chi phí)
- Lifetime Value: MAU × Average LTV = Tác động doanh thu

**Ví dụ (Phạt Nguội):**
- Đầu tư: 2h/tuần review + $5K/tháng vendor
- Lợi nhuận: 1,000 MAU/tháng × $20 LTV = $20K/tháng doanh thu
- ROI: 4x (payback đơn giản)

---

## 9. RỦI RO & GIẢM THIỂU

### 9.1 Rủi Ro Kỹ Thuật

| Rủi ro | Khả năng | Tác động | Giảm thiểu |
|---------|----------|----------|------------|
| Hiệu suất Vector DB giảm ở quy mô lớn (>10K bài viết) | Trung bình | Cao | Benchmark sớm (Q2), tối ưu chiến lược indexing, xem xét sharding |
| Chất lượng RAG kém (context truy xuất không liên quan) | Trung bình | Cao | Triển khai hybrid search (vector + keyword), điều chỉnh liên tục embedding models, feedback loop từ người dùng |
| Tích hợp GenAI → PLG Project dễ vỡ | Thấp | Trung bình | Thiết kế API vững chắc, retry logic, monitoring/alerting |
| PLG Project single point of failure (downtime = no chatbot) | Trung bình | Cao | Redundancy (multi-region DB), degradation nhẹ nhàng (fallback sang static FAQs) |

---

### 9.2 Rủi Ro Tổ Chức

| Rủi ro | Khả năng | Tác động | Giảm thiểu |
|---------|----------|----------|------------|
| BUs không đầu tư thời gian review nội dung (2h/tuần quá nhiều) | Cao | Cao | Bắt đầu nhỏ (Tier 1 Discovery), chứng minh giá trị trước khi yêu cầu thời gian. Tự động hóa càng nhiều càng tốt (chất lượng GenAI đủ cao để giảm gánh nặng review). |
| Quyền sở hữu tri thức không rõ ràng (ai maintain/update?) | Cao | Trung bình | Chính thức hóa trong hợp đồng Tier 2: BU sở hữu tri thức, Web Platform vận hành hạ tầng. Định nghĩa SLA cho updates (ví dụ: refresh hàng quý). |
| Tri thức trở nên lỗi thời (không ai update bài viết cũ) | Cao | Trung bình | Tự động phát hiện staleness (đánh dấu bài viết >90 ngày tuổi), gán refresh tasks cho BU reviewers, khuyến khích qua MAU attribution. |
| Xung đột tri thức cross-BU (BU khác nhau có thông tin mâu thuẫn) | Thấp | Trung bình | Namespace theo BU (mỗi BU có knowledge base riêng), HOẶC quản trị tập trung (Product team sở hữu tri thức canonical). |

---

### 9.3 Rủi Ro Kinh Doanh

| Rủi ro | Khả năng | Tác động | Giảm thiểu |
|---------|----------|----------|------------|
| ROI không thể đo lường (không chứng minh MAU đến từ tri thức) | Trung bình | Cao | Triển khai Full Funnel Tracking sớm (Phase 1), tag tất cả session tri thức, làm việc với Hoàng DA để xây dựng attribution model. |
| BUs xây dựng giải pháp tri thức riêng (bypass Web Platform) | Thấp | Trung bình | Định vị PLG Project là hạ tầng GPD-wide (VP mandate), tích hợp với công cụ hiện có (Help Center, chatbot) để switching cost cao. |
| Scope creep (BUs yêu cầu tính năng custom) | Cao | Trung bình | Tuân thủ SPA Framework tiers, công việc custom chỉ trong Tier 3 (với ngân sách). Ưu tiên tính năng có lợi cho TẤT CẢ BUs. |

---

## 10. PHỤ THUỘC & RÀNG BUỘC

### 10.1 Phụ Thuộc Nội Bộ

**Phụ Thuộc Quan Trọng:**
- **Capacity Duy:** Module owner duy nhất, đang chuyển đổi tech stack (Admin Panel → MoSpark)
  - **Rủi ro:** Giao hàng chậm nếu quá tải
  - **Giảm thiểu:** Hỗ trợ onboarding Hoài Anh, xem xét dev thứ 2 trong Q3

- **GenAI Content Module:** PLG Project phụ thuộc vào GenAI cho sản xuất nội dung quy mô lớn
  - **Trạng thái:** MVP done, đang nâng cấp (System Prompt, AI Gateway, Gemini 2.5 migration)
  - **Giảm thiểu:** Căn chỉnh roadmaps, đảm bảo nâng cấp GenAI không block PLG Project

- **Full Funnel Tracking:** Cần thiết cho MAU attribution
  - **Trạng thái:** Foundation done, pending Appsflyer→BigQuery (ITC blocker)
  - **Giảm thiểu:** Xây dựng attribution cơ bản mà không có Appsflyer trước, nâng cấp sau

**Phụ Thuộc Hỗ Trợ:**
- Lộc: Infrastructure (Vector DB, PostgreSQL, hosting)
- Hoài Anh: Tích hợp permission system, onboarding Duy
- Trọng: Tích hợp AI model (embeddings, RAG pipeline)
- Hiếu: Analytics pipeline, tích hợp BigQuery

---

### 10.2 Phụ Thuộc Bên Ngoài

**BU Stakeholders:**
- **VTTI (Hằng Mỵ, Thơ Hồ):** Xác thực tri thức sản phẩm, review nội dung
- **SPS + FS/Ví Trả Sau (Linh Trang):** Tri thức về các Merchant chấp nhận thanh toán nguồn tiền MoMo (Ví Trả Sau, MoMo)
- **Help Center (Ngọc Tạ):** Hub thông tin hướng dẫn/hỏi đáp về các tính năng/tiện ích/dịch vụ của MoMo

**Ràng buộc:** Cam kết thời gian BU (2h/tuần review) - yêu cầu buy-in

---

### 10.3 Ngân Sách & Nguồn Lực

**Headcount:**
- Duy: Full-time (Module Owner)
- Lộc: 20% allocation (Infrastructure)
- Hoài Anh: 10% allocation (Permissions, onboarding)
- Trọng: 20% allocation (Tích hợp AI)
- Hiếu: 10% allocation (Analytics)

**Chi Phí Hạ Tầng (ước tính):**
- Vector DB (Pinecone/Weaviate/Qdrant): $XXX/tháng (scales với # vectors)
- PostgreSQL (Supabase): Bao gồm trong plan hiện tại
- OpenAI/Gemini API (embeddings): $XXX/tháng (scales với # bài viết)

**Chi Phí Vendor (BU-funded trong Tier 3):**
- Content vendors: $5-10K/tháng per BU (cho sản xuất nội dung quy mô lớn)

---

## 11. TIÊU CHÍ THÀNH CÔNG & CHẤP NHẬN

### 11.1 Thành Công Phase 1 (Q2 2026)

**Must-Have (Tiêu chí go-live):**
- [ ] Chatbot có thể trả lời ≥80% FAQs Phạt Nguội qua RAG
- [ ] GenAI Content Module truy vấn thành công PLG Project cho context
- [ ] 200+ bài viết ingested (Phạt Nguội + DVC)
- [ ] Tỷ lệ validation BU >90% (phê duyệt Hằng Mỵ)
- [ ] RAG query latency <500ms p95

**Nice-to-Have:**
- [ ] Admin UI cho BU reviewers
- [ ] Analytics dashboard (chỉ số sử dụng cơ bản)

---

### 11.2 Thành Công Phase 2 (Q3 2026)

**Must-Have:**
- [ ] 5 BU knowledge base live
- [ ] 500+ bài viết tổng
- [ ] Chatbot xử lý 20K truy vấn/tháng, 70% tự phục vụ
- [ ] Help Center được cung cấp bởi PLG Project
- [ ] MAU attribution được theo dõi

**Nice-to-Have:**
- [ ] Programmatic SEO tự động tạo landing pages
- [ ] Tự động phát hiện knowledge gap

---

### 11.3 Thành Công Phase 3 (Q4 2026)

**Must-Have:**
- [ ] 10 BU knowledge base
- [ ] 1000+ bài viết
- [ ] 50K truy vấn chatbot/tháng, 80% tự phục vụ
- [ ] 5K+ MAU/tháng gán thuộc tính cho kênh tri thức
- [ ] ROI chứng minh cho BUs (payback <6 tháng)

**Nice-to-Have:**
- [ ] Semantic Search UI live
- [ ] Hỗ trợ đa ngôn ngữ (EN/VI)
- [ ] Truy cập API bên thứ ba

---

## 12. QUẢN TRỊ & QUYỀN SỞ HỮU

### 12.1 Quyền Quyết Định

| Loại Quyết Định | Owner | Consulted | Informed |
|-----------------|-------|-----------|----------|
| Tầm nhìn sản phẩm & roadmap | Bảo | VP, Hiến, Duy | GPD team |
| Kiến trúc kỹ thuật | Duy | Lộc, Hoài Anh, Trọng | Bảo |
| Validation tri thức BU | BU Product Owner | Web Platform (Hiến) | Duy |
| Ưu tiên tính năng | Bảo + Duy | Hiến, Hùng, Trọng | VP |
| Phân bổ ngân sách (infra) | VP | Bảo | Finance |

### 12.2 Mô Hình Quyền Sở Hữu Tri Thức

**Nguyên tắc:** BU sở hữu nội dung tri thức, Web Platform sở hữu hạ tầng.

**Trách Nhiệm BU:**
- Độ chính xác tri thức sản phẩm
- Validation nội dung (review/approve)
- Refresh tri thức hàng quý

**Trách Nhiệm Web Platform:**
- Hạ tầng (Vector DB, APIs, UI)
- Quy trình sản xuất nội dung (tích hợp GenAI)
- Công cụ chất lượng (phát hiện trùng lặp, cảnh báo staleness)
- Phân phối (chatbot, web, help center)

---

## 13. PHỤ LỤC

### Phụ lục A: Từ vựng

- **RAG (Retrieval-Augmented Generation):** Kỹ thuật AI nơi LLM truy xuất context liên quan từ knowledge base trước khi tạo câu trả lời
- **Vector DB:** Cơ sở dữ liệu tối ưu cho semantic similarity search (ví dụ: Pinecone, Weaviate)
- **Embedding:** Biểu diễn số của văn bản nắm bắt ý nghĩa ngữ nghĩa
- **SPA Framework:** reSearch → Pilot → Action (phương pháp tăng trưởng của Web Platform)
- **GEO:** Generative Engine Optimization (tối ưu khả năng hiển thị trên toàn bộ Search Engines: Google Search, TikTok, Facebook, AI Chatbots và App MoMo)
- **W2A:** Web-to-App (chỉ số hành trình người dùng)
- **Tỷ lệ tự phục vụ:** % truy vấn người dùng được giải quyết mà không cần hỗ trợ con người

### Phụ lục B: Tài Liệu Liên Quan

- MoSpark Product Service Model (SPA Framework doc của Hiến)
- GenAI Content Module PRD
- Help Center Module Overview
- Full Funnel Tracking Technical Spec
- VTTI Meeting Recap (15/05/2026)

### Phụ lục C: Câu Hỏi Mở (Cần Giải Quyết)

- [ ] Vector DB nào? (Pinecone vs Weaviate vs Qdrant vs pgvector)
- [ ] Embedding model nào? (OpenAI text-embedding-3 vs Google textembedding-gecko)
- [ ] Chiến lược version tri thức? (Git-like vs timestamp đơn giản)
- [ ] Multi-tenancy model? (DB riêng per BU vs single DB với namespacing)
- [ ] Content licensing? (Có thể sử dụng nội dung GenAI thương mại?)

---

**KẾT THÚC BRD v1.0**

**Bước Tiếp Theo:**
1. Review với VP để căn chỉnh chiến lược (tuần 19/05)
2. Review với Duy về tính khả thi kỹ thuật (tuần 19/05)
3. Review với Hiến về tích hợp SPA (tuần 19/05)
4. Hoàn thiện scope & timeline Phase 1 (đến cuối tháng 5)
5. Bắt đầu phát triển PRD cho Phase 1 (đầu tháng 6)
