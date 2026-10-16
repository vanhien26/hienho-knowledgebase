# -*- coding: utf-8 -*-
"""
KEYWORD INTELLIGENCE ENGINE (CORE LIBRARY)
Giải quyết 2 lỗ hổng cốt lõi:
1. Multi-signal Weighted Intent Scoring & Dynamic Semantic Outlier Filtering (Không dùng Regex cứng đơn giản).
2. SERP Intent Fingerprinting & Anti-Cannibalization Shield (Triệt tiêu xung đột từ khóa cùng Intent).
"""

import re
import math
from collections import defaultdict, Counter

# Từ điển chuẩn hóa thực thể đồng nghĩa & viết tắt (Synonyms & Entities Dictionary)
SYNONYM_MAP = {
    'tiền gửi': 'tiết kiệm',
    'gửi tiết kiệm': 'tiết kiệm',
    'lãi xuất': 'lãi suất',
    'vcb': 'vietcombank',
    'viet com bank': 'vietcombank',
    'tcb': 'techcombank',
    'tech com bank': 'techcombank',
    'ctg': 'vietinbank',
    'viet in bank': 'vietinbank',
    'bid': 'bidv',
    'scb': 'sacombank',
    'vpb': 'vpbank',
    'mbb': 'mbbank',
    'mb bank': 'mbbank',
    'ô tô': 'oto',
    'xe hơi': 'oto',
    'xe oto': 'oto',
    'xe máy': 'xe_may',
    'tphcm': 'tp_hcm',
    'tp hcm': 'tp_hcm',
    'hồ chí minh': 'tp_hcm',
    'sài gòn': 'tp_hcm',
    'hn': 'ha_noi',
    'hà nội': 'ha_noi',
    'đn': 'da_nang',
    'đà nẵng': 'da_nang',
    'gplx': 'bang_lai_xe',
    'bằng lái xe': 'bang_lai_xe',
    'bằng lái': 'bang_lai_xe',
    'giấy phép lái xe': 'bang_lai_xe',
    'bhyt': 'bao_hiem_y_te',
    'bảo hiểm y tế': 'bao_hiem_y_te',
    'bhtn': 'bao_hiem_that_nghiep',
    'bhxh': 'bao_hiem_xa_hoi',
    'tndsv': 'tnds',
    'trách nhiệm dân sự': 'tnds',
}

STOPWORDS = {
    'và', 'là', 'của', 'ở', 'tại', 'cho', 'với', 'trong', 'các', 'những',
    'được', 'có', 'ra', 'khi', 'về', 'này', 'đó', 'từ', 'theo', 'như',
    'để', 'lại', 'thì', 'người', 'cái', 'làm', 'hay', 'bao', 'nhiêu',
    'gì', 'sao', 'nao', 'nào', 'mấy', 'một', 'hai', 'ba', 'bốn', 'năm'
}

TELEX_FIXES = {
    'ddaaus': 'đấu',
    'ddieenj': 'điện',
    'ddoof': 'đồ',
    'ddoongf': 'đồng',
    'ngan hang': 'ngân hàng',
    'tiet kiem': 'tiết kiệm',
    'lai suat': 'lãi suất',
    'bien so': 'biển số',
    'bao hiem': 'bảo hiểm',
    'o to': 'ô tô',
    'xe may': 'xe máy',
}

# Tập từ điển nhiễu chéo ngành (Cross-domain Alien Collisions)
CROSS_DOMAIN_OUTLIERS = {
    'financial': [
        'giao hàng', 'gửi hàng', 'ghtk', 'ghn', 'shopee express', 'chuyển phát nhanh',
        'bưu điện', 'xe tải', 'game lậu', 'hack', 'mod', 'tín dụng đen', 'xã hội đen',
        'bốc bát họ', 'lừa đảo chiếm đoạt'
    ],
    'vehicle': [
        'gta', 'mod skin', 'mô hình', 'đồ chơi', 'diogo jota', 'fifa', 'pes',
        'tiết kiệm', 'lãi suất ngân hàng', 'chứng chỉ quỹ'
    ],
    'insurtech': [
        'lừa đảo chiếm đoạt', 'bảo hiểm giang hồ', 'game', 'hack'
    ],
    'lottery': [
        'soi cầu lừa đảo', 'mua số trúng 100%', 'bán số đề'
    ],
    'hospital': [
        'chữa bệnh bằng bùa', 'thầy lang lừa đảo'
    ]
}

# Ma trận trọng số Intent nhiều tín hiệu (Multi-signal Weighted Intent Matrix)
INTENT_WEIGHT_SIGNALS = {
    'Transactional': {
        'keywords': [
            'mở sổ', 'đăng ký', 'đổi biển', 'nộp phạt', 'mua', 'nạp', 'thanh toán',
            'làm thẻ', 'vay ngay', 'tất toán', 'gia hạn', 'đặt vé', 'mở thẻ', 'kích hoạt'
        ],
        'weight': 3.5,
        'action_level': 'high'
    },
    'Tool/Calculator': {
        'keywords': [
            'tính', 'công cụ tính', 'tra cứu', 'kiểm tra', 'check', 'bao nhiêu tiền',
            'lãi bao nhiêu', 'cách tính', 'định giá', 'so sánh giá', 'bảng tính', 'máy tính'
        ],
        'weight': 3.0,
        'action_level': 'high'
    },
    'Commercial': {
        'keywords': [
            'nên', 'tốt nhất', 'so sánh', 'nào tốt', 'lãi suất', 'bảng giá',
            'giá bao nhiêu', 'chi phí', 'ưu đãi', 'đánh giá', 'review', 'kỳ hạn',
            'lãi cao nhất', 'ngân hàng nào', 'loại nào', 'báo giá'
        ],
        'weight': 2.2,
        'action_level': 'medium'
    },
    'Informational': {
        'keywords': [
            'an toàn', 'rủi ro', 'lừa đảo', 'bảo mật', 'có nên', 'kinh nghiệm',
            'hướng dẫn', 'thủ tục', 'quy định', 'hồ sơ', 'điều kiện', 'là gì',
            'ở đâu', 'khái niệm', 'thông tin', 'quy trình', 'ý nghĩa'
        ],
        'weight': 1.8,
        'action_level': 'low'
    },
    'Navigational': {
        'keywords': [
            'login', 'đăng nhập', 'app', 'chi nhánh', 'tổng đài', 'hotline',
            'website', 'vneid', 'dvc', 'cổng dịch vụ công', 'trang chủ'
        ],
        'weight': 2.5,
        'action_level': 'medium'
    }
}

class MultiSignalIntentClassifier:
    """
    Phân loại Search Intent bằng thuật toán tính điểm trọng số đa tín hiệu (Multi-Signal Scoring).
    Giải quyết triệt để xung đột khi từ khóa chứa nhiều từ báo hiệu khác nhau.
    """
    @staticmethod
    def classify(keyword: str) -> dict:
        kw = keyword.lower().strip()
        scores = defaultdict(float)
        matched_signals = defaultdict(list)
        
        # 1. Quét đối sánh đa tín hiệu
        for intent, config in INTENT_WEIGHT_SIGNALS.items():
            base_weight = config['weight']
            for signal in config['keywords']:
                if re.search(r'\b' + re.escape(signal) + r'\b', kw):
                    # Trọng số gia tăng nếu từ chỉ intent nằm ở đầu câu (vị trí chủ đạo của hành vi người dùng)
                    pos_bonus = 1.3 if kw.startswith(signal) else 1.0
                    score_gain = base_weight * pos_bonus
                    scores[intent] += score_gain
                    matched_signals[intent].append(signal)

        # 2. Xử lý xung đột intent đặc thù:
        # Trường hợp "cách tính...": "tính" (Tool) kết hợp "cách" (Info). Người dùng muốn tính cụ thể -> Ưu tiên Tool
        if 'tính' in kw and ('cách' in kw or 'hướng dẫn' in kw):
            scores['Tool/Calculator'] += 1.5

        # Trường hợp "lãi bao nhiêu": Tính lãi cụ thể -> Ưu tiên Tool/Calculator hơn Commercial thuần túy
        if 'lãi bao nhiêu' in kw or 'bao nhiêu tiền' in kw:
            scores['Tool/Calculator'] += 2.0

        # Nếu không có tín hiệu nào khớp rõ ràng -> Mặc định Informational
        if not scores:
            return {
                'intent': 'Informational',
                'confidence': 0.60,
                'scores': {'Informational': 1.0},
                'matched_signals': []
            }

        # Tìm intent có điểm cao nhất
        sorted_intents = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_intent, top_score = sorted_intents[0]
        
        total_score = sum(scores.values())
        confidence = round(top_score / total_score, 2) if total_score > 0 else 0.5
        
        return {
            'intent': top_intent,
            'confidence': confidence,
            'scores': dict(scores),
            'matched_signals': matched_signals[top_intent]
        }


class SemanticDomainFilter:
    """
    Bộ lọc ranh giới ngữ nghĩa tự động (Dynamic Domain Boundary Filtering).
    Loại bỏ từ khóa ngoài ngành (Out-of-scope) mà không cần hardcode danh sách cho từng use case.
    """
    @staticmethod
    def is_outlier(keyword: str, sector: str, usecase_slug: str, domain_anchors: set = None) -> tuple:
        kw = keyword.lower().strip()
        sec_key = sector.lower()
        
        # 1. Kiểm tra đối chiếu với danh mục Alien Outliers của từng ngành
        alien_patterns = CROSS_DOMAIN_OUTLIERS.get(sec_key, [])
        for alien in alien_patterns:
            if alien in kw:
                return True, f"Cross-domain alien keyword: matches '{alien}' in sector '{sector}'"

        # 2. Kiểm tra nếu có domain_anchors truyền vào
        if domain_anchors and len(domain_anchors) > 0:
            kw_tokens = set([t for t in kw.split() if t not in STOPWORDS and len(t) > 1])
            # Nếu không có bất kỳ token nào giao thoa với anchor thực thể cốt lõi của use case
            overlap = kw_tokens.intersection(domain_anchors)
            if len(kw_tokens) >= 3 and len(overlap) == 0:
                return True, f"Zero domain overlap with anchors: {list(domain_anchors)[:4]}"

        # 3. Lọc các mẫu spam/lỗi ký tự đặc biệt
        if re.search(r'[<>{}@#$%^&*()_+=\[\]~`|\\]', kw):
            return True, "Contains illegal special characters/code injection"

        if len(kw) < 2 or len(kw) > 120:
            return True, "Invalid keyword length (<2 or >120 chars)"

        return False, "valid"


class SERPCannibalizationShield:
    """
    Cơ chế phát hiện SERP Intent Overlap & Triệt tiêu Keyword Cannibalization.
    Tạo Fingerprint chuẩn hóa và gom các từ khóa có cùng kết quả SERP về 1 canonical entry.
    """
    @staticmethod
    def normalize_entities(text: str) -> str:
        text = text.lower().strip()
        for syn, target in SYNONYM_MAP.items():
            text = re.sub(r'\b' + re.escape(syn) + r'\b', target, text)
        return text

    @classmethod
    def generate_intent_fingerprint(cls, keyword: str, intent: str) -> str:
        """
        Tạo mã định danh dấu vân tay (Fingerprint) dựa trên Intent + Tập thực thể đã chuẩn hóa.
        Hai từ khóa có cùng Fingerprint chắc chắn phục vụ cùng 1 trang đích duy nhất.
        """
        norm_text = cls.normalize_entities(keyword)
        # Tách token, loại trừ stopwords, loại bỏ trùng lặp và sắp xếp theo bảng chữ cái
        tokens = sorted(list(set([t for t in norm_text.split() if t not in STOPWORDS and len(t) > 1])))
        token_hash = "_".join(tokens)
        return f"{intent}::{token_hash}"

    @classmethod
    def calculate_token_similarity(cls, kw1: str, kw2: str) -> float:
        """Tính Jaccard Similarity giữa hai tập token thực thể đã chuẩn hóa"""
        n1 = set([t for t in cls.normalize_entities(kw1).split() if t not in STOPWORDS and len(t) > 1])
        n2 = set([t for t in cls.normalize_entities(kw2).split() if t not in STOPWORDS and len(t) > 1])
        if not n1 or not n2:
            return 0.0
        intersection = len(n1.intersection(n2))
        union = len(n1.union(n2))
        return intersection / union if union > 0 else 0.0

    @classmethod
    def cluster_and_shield(cls, keyword_items: list, similarity_threshold: float = 0.70) -> tuple:
        """
        Gom cụm và triệt tiêu Cannibalization:
        - Nhóm các từ có cùng fingerprint hoặc độ tương đồng semantic token >= threshold.
        - Giữ từ khóa có volume lớn nhất làm Primary Keyword.
        - Gom các từ còn lại thành Secondary Synonyms.
        """
        # Sắp xếp danh sách giảm dần theo Volume để từ khóa có volume lớn nhất luôn làm Canonical Leader
        sorted_items = sorted(keyword_items, key=lambda x: x['volume'], reverse=True)
        
        canonical_clusters = []
        merge_log = []
        processed_fingerprints = {}
        token_to_leaders = defaultdict(set)

        for item in sorted_items:
            kw = item['keyword']
            intent = item['intent']
            norm_kw = cls.normalize_entities(kw)
            tokens = set([t for t in norm_kw.split() if t not in STOPWORDS and len(t) > 1])
            fp = f"{intent}::{'_'.join(sorted(tokens))}"

            # Trường hợp 1: Trùng Fingerprint hoàn toàn -> Chắc chắn cannibalized
            if fp in processed_fingerprints:
                leader_idx = processed_fingerprints[fp]
                leader = canonical_clusters[leader_idx]
                leader['secondary_keywords'].append(kw)
                leader['total_cluster_volume'] += item['volume']
                merge_log.append({
                    'merged_keyword': kw,
                    'canonical_primary': leader['keyword'],
                    'reason': f"Exact Intent Fingerprint: {fp}",
                    'volume_added': item['volume']
                })
                continue

            # Trường hợp 2: Kiểm tra Inverted Index - chỉ xét các Leader có chung ít nhất 1 token
            candidates = set()
            for t in tokens:
                if (intent, t) in token_to_leaders:
                    candidates.update(token_to_leaders[(intent, t)])

            merged = False
            for leader_idx in candidates:
                leader = canonical_clusters[leader_idx]
                l_tokens = leader['_tokens']
                union_len = len(tokens.union(l_tokens))
                sim = len(tokens.intersection(l_tokens)) / union_len if union_len > 0 else 0.0
                if sim >= similarity_threshold:
                    leader['secondary_keywords'].append(kw)
                    leader['total_cluster_volume'] += item['volume']
                    processed_fingerprints[fp] = leader_idx
                    merged = True
                    merge_log.append({
                        'merged_keyword': kw,
                        'canonical_primary': leader['keyword'],
                        'reason': f"High Semantic Token Similarity ({round(sim, 2)} >= {similarity_threshold})",
                        'volume_added': item['volume']
                    })
                    break

            if not merged:
                # Trở thành một Canonical Cluster Leader mới
                idx = len(canonical_clusters)
                new_cluster = {
                    'keyword': kw,
                    '_tokens': tokens,
                    'volume': item['volume'],
                    'cpc': item.get('cpc', 0.0),
                    'competition': item.get('competition', 'Low'),
                    'intent': intent,
                    'opportunity_score': item.get('opportunity_score', 0.0),
                    'quadrant': item.get('quadrant', 'Supporting'),
                    'total_cluster_volume': item['volume'],
                    'secondary_keywords': []
                }
                canonical_clusters.append(new_cluster)
                processed_fingerprints[fp] = idx
                for t in tokens:
                    token_to_leaders[(intent, t)].add(idx)

        # Xóa trường tạm _tokens trước khi return
        for c in canonical_clusters:
            c.pop('_tokens', None)

        return canonical_clusters, merge_log


class StructuredSchemaGenerator:
    """
    Tự động sinh JSON-LD Structured Data Schema chuẩn Google Search Central:
    - FAQPage Schema cho các cụm câu hỏi và công cụ tra cứu.
    - BreadcrumbList Schema cho cấu trúc phân tầng Hub -> Sector -> Use Case.
    """
    @staticmethod
    def generate_faq_jsonld(usecase_name: str, qa_pairs: list) -> dict:
        entities = []
        for q, a in qa_pairs:
            entities.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })
        return {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "name": f"Hỏi đáp thường gặp về {usecase_name}",
            "mainEntity": entities
        }

    @staticmethod
    def generate_breadcrumb_jsonld(sector: str, usecase_name: str, usecase_slug: str, base_url: str = "https://momo.vn") -> dict:
        sector_slug = sector.lower().replace('_', '-').replace(' ', '-')
        return {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Trang chủ",
                    "item": base_url
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": sector.title(),
                    "item": f"{base_url}/{sector_slug}"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": usecase_name,
                    "item": f"{base_url}/{usecase_slug.strip('/')}"
                }
            ]
        }


class ContentBriefGenerator:
    """
    Tự động tạo Content Brief chi tiết cho từng bài viết:
    - Dự toán dung lượng bài viết (Word Count Target)
    - Dàn ý H2/H3 Entity Checklist bắt buộc
    - Hướng dẫn liên kết nội bộ và CTA Web-to-App
    """
    @staticmethod
    def estimate_word_count(format_type: str, intent: str, cluster_volume: int) -> dict:
        if 'Pillar' in format_type or cluster_volume >= 20000:
            return {'min_words': 2500, 'target_words': 3500, 'tier': 'Master Hub Pillar'}
        elif intent in ('Tool/Calculator', 'Transactional'):
            return {'min_words': 1500, 'target_words': 2200, 'tier': 'High Conversion Guide'}
        elif intent == 'Commercial':
            return {'min_words': 1800, 'target_words': 2500, 'tier': 'Comparison & Review'}
        else:
            return {'min_words': 1200, 'target_words': 1600, 'tier': 'Educational Spoke'}

    @classmethod
    def generate_outline_checklist(cls, page_plan: dict, usecase_name: str) -> list:
        kw = page_plan['primary_kw']
        intent = page_plan['intent']
        sec_kws = page_plan.get('secondary_kws', [])
        
        outline = [
            f"## H2 1: Tổng quan & Khái niệm cốt lõi về {kw}",
            f"## H2 2: Chi tiết các tiêu chí & Bảng tổng hợp số liệu mới nhất"
        ]
        
        if intent == 'Tool/Calculator':
            outline.extend([
                f"## H2 3: Hướng dẫn sử dụng công cụ tính toán / tra cứu trực tuyến trên Web",
                f"### H3 3.1: Các bước điền tham số và cách đọc kết quả",
                f"## H2 4: Công thức tính và ví dụ thực tế minh họa từng bước"
            ])
        elif intent == 'Commercial':
            outline.extend([
                f"## H2 3: So sánh chi tiết các lựa chọn hàng đầu trên thị trường hiện nay",
                f"### H3 3.1: Ưu và nhược điểm của từng đơn vị cung cấp",
                f"## H2 4: Lời khuyên nên chọn giải pháp nào tối ưu nhất theo nhu cầu"
            ])
        elif intent == 'Transactional':
            outline.extend([
                f"## H2 3: Hồ sơ và điều kiện cần chuẩn bị trước khi thực hiện",
                f"## H2 4: Quy trình 3 bước thực hiện giao dịch nhanh chóng trên điện thoại"
            ])
        else:
            outline.extend([
                f"## H2 3: 5 lưu ý quan trọng để đảm bảo an toàn và tối đa hóa quyền lợi",
                f"## H2 4: Những sai lầm thường gặp và cách phòng tránh"
            ])

        # Đề mục FAQ chuẩn Schema
        outline.append(f"## H2 5: Câu hỏi thường gặp (FAQs) giải đáp thắc mắc về {kw}")
        for idx, s in enumerate(sec_kws[:3], 1):
            outline.append(f"### H3 5.{idx}: {s.capitalize()}?")
            
        outline.append("## H2 6: Giải pháp tối ưu quyền lợi và thao tác nhanh qua Ứng dụng MoMo")
        return outline


class InternalLinkingTopologyEngine:
    """
    Xây dựng mạng lưới liên kết nội bộ phân tầng (Internal Linking & Silo Matrix):
    - Parent Hub: Liên kết ngược về Hub trụ cột của phân khối.
    - Peer In-Silo: 3-5 Use Cases cùng ngành có độ tương đồng ngữ nghĩa cao nhất.
    - Cross-Silo Bridges: Liên kết chéo ngành có tính chất bổ trợ chuyển đổi tự nhiên (Vehicle <-> Insurtech, Financial <-> Vehicle).
    """
    SECTOR_HUB_MAP = {
        'Financial': {'name': 'Tài Chính & Ngân Hàng', 'url': '/tai-chinh', 'anchor': 'Cổng dịch vụ Tài chính MoMo'},
        'vehicle-hub': {'name': 'Giao Thông & Tiện Ích Xe', 'url': '/xe', 'anchor': 'Trung tâm tiện ích Giao thông & Hồ sơ xe'},
        'insurtech': {'name': 'Bảo Hiểm Số', 'url': '/bao-hiem', 'anchor': 'Sàn giao dịch Bảo hiểm trực tuyến MoMo'},
        'ota': {'name': 'Du Lịch & Đi Lại', 'url': '/du-lich', 'anchor': 'Cổng đặt vé máy bay & Khách sạn MoMo Travel'},
        'Lottery': {'name': 'Xổ Số & Trúng Thưởng', 'url': '/xo-so', 'anchor': 'Tra cứu kết quả & Vé số Vietlott MoMo'},
        'hospital': {'name': 'Y Tế & Viện Phí', 'url': '/y-te', 'anchor': 'Thanh toán viện phí & Dịch vụ Y tế MoMo'},
        'telco': {'name': 'Viễn Thông & 4G/5G', 'url': '/vien-thong', 'anchor': 'Cổng Nạp điện thoại & Data 4G/5G'},
        'MDS': {'name': 'Dịch Vụ Đời Sống', 'url': '/dich-vu-doi-song', 'anchor': 'Thanh toán hóa đơn & Dịch vụ sinh hoạt'},
        'PS': {'name': 'Giải Trí & Mua Sắm', 'url': '/giai-tri', 'anchor': 'Đặt vé xem phim & Giải trí MoMo'},
        'trust': {'name': 'Xác Thực & Uy Tín', 'url': '/xac-thuc', 'anchor': 'Cổng bảo mật & Xác thực an toàn MoMo'},
        'other': {'name': 'Tiện Ích Nền Tảng', 'url': '/tien-ich', 'anchor': 'Hệ sinh thái tiện ích Web MoMo'},
    }

    CROSS_SECTOR_RULES = [
        ('vehicle-hub', 'insurtech', ['bảo hiểm', 'tnds', 'tai nạn', 'vật chất', 'xe máy', 'ô tô']),
        ('Financial', 'vehicle-hub', ['vay', 'mua xe', 'trả góp', 'định giá', 'thế chấp']),
        ('ota', 'insurtech', ['bảo hiểm', 'du lịch', 'chuyến bay', 'trễ chuyến']),
        ('hospital', 'insurtech', ['bảo hiểm', 'y tế', 'sức khỏe', 'viện phí']),
        ('telco', 'Financial', ['nạp tiền', 'thanh toán', 'ví trả sau', 'chiết khấu']),
        ('MDS', 'Financial', ['hóa đơn', 'ví trả sau', 'trả chậm', 'tiết kiệm']),
    ]

    @classmethod
    def extract_keywords_tokens(cls, usecase: dict) -> set:
        raw_text = f"{usecase.get('id', '')} {usecase.get('name', '')}"
        tokens = set(re.findall(r'\b\w{2,}\b', raw_text.lower()))
        for kw_item in usecase.get('top_opportunities', [])[:10]:
            kw_str = kw_item.get('keyword', '')
            tokens.update([t for t in kw_str.lower().split() if len(t) > 2 and t not in STOPWORDS])
        return tokens

    @classmethod
    def build_silo_matrix(cls, current_usecase: dict, all_usecases: list) -> dict:
        cur_id = current_usecase['id']
        cur_sec = current_usecase['sector']
        cur_tokens = cls.extract_keywords_tokens(current_usecase)
        parent_hub = cls.SECTOR_HUB_MAP.get(cur_sec, cls.SECTOR_HUB_MAP['other'])

        # 1. Tìm Peer In-Silo (Cùng phân khối)
        peer_candidates = []
        for u in all_usecases:
            if u['id'] == cur_id or u['sector'] != cur_sec:
                continue
            u_tokens = cls.extract_keywords_tokens(u)
            overlap = len(cur_tokens.intersection(u_tokens))
            sim = overlap / len(cur_tokens.union(u_tokens)) if cur_tokens.union(u_tokens) else 0.0
            
            # Gợi ý anchor text tối ưu từ pillar keyword hoặc top opportunity
            p_kw = u.get('pillar_keyword', {}).get('keyword') or u.get('name', '')
            peer_candidates.append({
                'target_id': u['id'],
                'target_name': u['name'],
                'target_url': f"/{u['id']}/",
                'suggested_anchor': p_kw,
                'similarity_score': round(sim, 3),
                'volume': u.get('total_volume', 0)
            })

        # Sắp xếp ưu tiên: similarity cao nhất, sau đó đến volume
        peer_candidates.sort(key=lambda x: (x['similarity_score'], x['volume']), reverse=True)
        peer_links = peer_candidates[:4]

        # 2. Tìm Cross-Silo Bridges (Cầu nối liên kết xuyên ngành)
        cross_bridges = []
        for u in all_usecases:
            if u['sector'] == cur_sec:
                continue
            target_sec = u['sector']
            
            # Kiểm tra xem có luật tương hỗ giữa 2 ngành không
            is_compatible = False
            for s1, s2, triggers in cls.CROSS_SECTOR_RULES:
                if (cur_sec == s1 and target_sec == s2) or (cur_sec == s2 and target_sec == s1):
                    # Kiểm tra xem có token trigger nào xuất hiện
                    u_tokens = cls.extract_keywords_tokens(u)
                    if any(tr in ' '.join(cur_tokens) or tr in ' '.join(u_tokens) for tr in triggers):
                        is_compatible = True
                        break
            
            if is_compatible:
                u_tokens = cls.extract_keywords_tokens(u)
                overlap = len(cur_tokens.intersection(u_tokens))
                p_kw = u.get('pillar_keyword', {}).get('keyword') or u.get('name', '')
                cross_bridges.append({
                    'target_id': u['id'],
                    'target_sector': target_sec,
                    'target_name': u['name'],
                    'target_url': f"/{u['id']}/",
                    'suggested_anchor': p_kw,
                    'overlap_tokens': overlap,
                    'volume': u.get('total_volume', 0)
                })

        cross_bridges.sort(key=lambda x: (x['overlap_tokens'], x['volume']), reverse=True)
        selected_bridges = cross_bridges[:2]

        return {
            'parent_hub': {
                'title': parent_hub['name'],
                'url': parent_hub['url'],
                'anchor': parent_hub['anchor']
            },
            'peer_in_silo': peer_links,
            'cross_silo_bridges': selected_bridges
        }


class GEODirectAnswerGenerator:
    """
    Sinh nội dung tối ưu cho Tìm kiếm Tạo sinh (Generative Engine Optimization - GEO):
    Phục vụ trích dẫn trực tiếp cho Google AI Overviews, SearchGPT, Perplexity và Gemini.
    """
    @staticmethod
    def generate_direct_answer_snippet(usecase_name: str, pillar_kw: str, intent: str, sector: str) -> str:
        """Đoạn định nghĩa chuẩn xác 40-60 từ để công cụ tìm kiếm AI bốc làm Direct Answer"""
        action_verb = "tra cứu và tính toán" if intent == 'Tool/Calculator' else ("so sánh và lựa chọn giải pháp" if intent == 'Commercial' else "thực hiện giao dịch trực tuyến")
        return (
            f"{pillar_kw.capitalize()} là giải pháp tiện ích số trên Nền tảng Web MoMo, cho phép người dùng "
            f"{action_verb} {usecase_name.lower()} một cách nhanh chóng, minh bạch và chính xác theo thời gian thực. "
            f"Dịch vụ liên kết với các đối tác uy tín hàng đầu, đảm bảo chuẩn bảo mật PCI DSS quốc tế và hỗ trợ thao tác "
            f"liền mạch từ trình duyệt Web đến Ứng dụng MoMo trong 1-3 phút."
        )

    @staticmethod
    def generate_entity_factsheet(usecase_name: str, sector: str, intent: str) -> list:
        """Bảng dữ liệu thực thể (Entity Facts) chuẩn hóa cho AI Knowledge Graph"""
        return [
            {"entity_field": "Phân loại giải pháp", "value": f"Tiện ích Web {sector.title()} - MoMo Web Platform"},
            {"entity_field": "Đối tượng áp dụng", "value": "Toàn bộ người dùng cá nhân có nhu cầu tra cứu và giao dịch trực tuyến"},
            {"entity_field": "Thời gian xử lý", "value": "Xử lý tức thì (Real-time), hỗ trợ 24/7 không phụ thuộc giờ hành chính"},
            {"entity_field": "Hạ tầng kỹ thuật", "value": "Kết nối API trực tiếp từ hệ thống đối tác liên kết chính thức"},
            {"entity_field": "Tiêu chuẩn bảo mật", "value": "Bảo mật đa tầng, đạt chứng chỉ bảo mật quốc tế PCI DSS Level 1"},
            {"entity_field": "Kênh thao tác liền mạch", "value": "Trình duyệt Web (Desktop/Mobile) kết hợp chuyển tiếp Web-to-App MoMo"}
        ]

