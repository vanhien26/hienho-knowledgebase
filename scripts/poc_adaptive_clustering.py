#!/usr/bin/env python3
"""
PoC - Thuật toán gán Cluster mới (Adaptive Clustering v2)
=========================================================

Vấn đề đang xử lý
-----------------
`sync_inventory_to_hubs.py::build_adaptive_clusters` (dòng 847-908) gán keyword
theo luật trigger và khi KHÔNG khớp trigger nào thì đổ hết vào `rules[-1]`
(rule cuối của sector). Cluster nhận luôn tên của rule cuối nên:

  - 25.3% tổng keyword (74.016/292.880) nằm trong 1 bucket mang tên không
    liên quan nội dung (Financial -> "Tra cứu & Chi nhánh", vehicle-hub ->
    "Định giá & Mua bán xe").
  - 85/494 cluster là "vỏ" <= 3 keyword.
  - 12 tên template chiếm 61% toàn bộ cluster nên tên luôn chung chung.

Thuật toán mới: 3 tầng + cổng chất lượng tên
---------------------------------------------
  TIER 1 - INTENT   : rule trigger, chọn rule khớp trigger DÀI NHẤT (specificity)
  TIER 2 - ENTITY   : token thương hiệu thật (ngân hàng, rạp, hãng bay...) mined
                      từ chính pool keyword của theme
  TIER 3 - RESIDUAL : seed-and-absorb theo keyword volume cao nhất, tên lấy từ
                      head-term thật của cụm (không dùng tên template)
  GATE            : tên cluster phải có >= 1 token hữu nghĩa trùng với top keyword
  CLEANUP         : cluster "vỏ" (< MIN_CLUSTER_KEYWORDS) bị gộp vào cụm gần nhất
  CAP             : 5 cluster/theme thường, 10 cho mega-theme (>= 5000 keyword)

Chạy thử nghiệm:
    ./.venv/bin/python scripts/poc_adaptive_clustering.py
    ./.venv/bin/python scripts/poc_adaptive_clustering.py --themes ngan-hang,co-tuc
"""

import argparse
import importlib.util
import json
import os
import re
import sys
from collections import Counter, defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts", "lib"))

# ----------------------------------------------------------------------
# Hằng số thuật toán
# ----------------------------------------------------------------------
MIN_CLUSTER_KEYWORDS = 5          # dưới ngưỡng này coi là cluster vỏ
MAX_CLUSTERS_NORMAL = 5           # cap cluster cho theme thường
MAX_CLUSTERS_MEGA = 10            # cap cluster cho mega-theme
MEGA_THEME_KW = 5000              # ngưỡng coi là mega-theme
MEGA_BRAND_MIN_SHARE = 0.005     # brand tối thiểu 0.5% keyword của mega-theme để tách page
CONCEPT_SHARE_MAX = 0.20          # token xuất hiện > 20% keyword là concept, không phải brand
MIN_ENTITY_KEYWORDS = 3           # brand cần tối thiểu số keyword để tách
DEFAULT_THEMES = ["ngan-hang", "co-tuc", "bac", "rap", "gia-vang"]

# Token mang tính "dịch vụ/nghị vụ", tuy xuất hiện nhiều nhưng KHÔNG phải thương hiệu
GENERIC_TOKENS = {
    "tra", "cuu", "chi", "nhanh", "phong", "giao", "dich", "tong", "dai", "hotline",
    "dia", "chi", "swift", "phi", "bieu", "thu", "tuc", "ho", "so", "dieu", "kien",
    "huong", "dan", "cach", "gia", "lai", "suat", "tiet", "kiem", "gui", "tien",
    "han", "rut", "vay", "von", "tin", "chap", "the", "chap", "tra", "gop", "han",
    "muc", "mo", "khai", "so", "tai", "khoan", "phat", "hanh", "don", "ty", "gia",
    "ngoai", "te", "chuyen", "doi", "euro", "usd", "vnd", "dxy", "kim", "loai",
    "quy", "nhan", "trơn", "tay", "mua", "ban", "thanh", "toan", "chuyen", "ke",
    "nhanh", "cau", "hien", "dien", "banh", "thay", "nhot", "chi", "phi", "nuoi",
    "xe", "tiêu", "hao", "dang", "kiem", "sang", "ten", "gara", "garage", "cuu",
    "ho", "sua", "rua", "vac", "keo", "phanh", "viem", "pham", "nghi", "dinh",
    "cham", "diem", "bang", "giay", "phep", "camera", "truc", "tuyen", "sinh",
    "nam", "hoc", "hoc", "phu", "bosch", "cong", "viec", "ky", "nang", "sinh",
    "vien", "cong", "thong", "tin", "cuu", "lien", "he", "ve", "chuyen", "di",
    "chuyen", "doi", "diem", "den", "dia", "pham", "mo", "khoa", "lich", "chi",
    "cuoc", "gia", "ban", "cau", "hoc", "den", "nam", "so", "sinh", "vien",
    "cong", "viec", "tuyen", "dung", "khoang", "thu", "le", "am", "lich",
    "tarot", "tranh", "anh", "tu", "vi", "kich", "du", "lien", "tuong",
    "xem", "ket", "qua", "soi", "cau", "thong", "ke", "tuyen", "dau", "duoi",
    "giai", "thuong", "don", "ve", "so", "giai", "thuong", "cau", "keu", "viec",
    "bao", "hiem", "mua", "online", "truc", "tuyen", "cham", "mat", "benh",
    "vien", "gia", "kham", "suc", "khoe", "chi", "so", "index", "bmi", "tdee",
    "calo", "can", "nang", "the", "gioi", "du", "bao", "gia", "vang", "bac",
    "kim", "loai", "quy", "ty", "gia", "co", "phieu", "chung", "khoan", "co",
    "tuc", "lai", "suat", "dau", "tu", "chuyen", "khoan", "giao", "dich",
    "cong", "cuu", "diem", "tin", "dung", "no", "tra", "gop", "the", "tai",
    "san", "co", "tuc", "chung", "chi", "quy", "tien", "gui", "ky", "han",
    "khoa", "vay", "tin", "chay", "the", "chap", "vay", "mua", "nha", "xe",
    "oto", "giao", "dich", "vung", "keu", "vay", "tinh", "dung", "cong",
    "phat", "nguoi", "giao", "thong", "cam", "ung", "dung", "tra", "gop",
    "the", "tai", "khoan", "chuyen", "khoan", "ngan", "hang", "ngan", "hang",
    "dia", "chi", "pho", "giao", "dich", "mua", "ban", "gia", "xe", "lam",
    "banh", "dinh", "nghia", "vay", "tinh", "chap", "phu", "thu", "dich",
    "vay", "muon", "tra", "gop", "hang", "thang", "nam", "chi", "su", "dung",
    "phu", "thu", "hop", "dong", "chi", "tiet", "su", "dung", "cua", "ban",
    "mo", "the", "mo", "the", "tin", "dung", "the", "tinh", "dung", "so",
    "tai", "khoan", "ngan", "hang", "the", "phat", "hanh", "lien", "he",
    "ngan", "hang", "so", "tai", "chi", "nhanh", "giao", "dich", "thanh",
    "toan", "chuyen", "khoan", "ngoai", "te", "chuyen", "doi", "ty", "gia",
    "chuyen", "doi", "ngoai", "te", "mua", "ban", "the", "va", "gi", "la",
    "gi", "nhu", "nao", "bao", "nhieu", "co", "nen", "khong", "khi", "sao",
    "hôm", "nay", "nam", "thang", "ngay", "tuan", "nam", "giam", "tang",
    "moi", "nhat", "tai", "day", "tinh", "phu", "thu", "chi", "dich",
}

STOPWORD_HINTS = {
    "la", "gi", "nhu", "nao", "bao", "nhieu", "co", "nen", "khong", "khi",
    "sao", "hôm", "nay", "nam", "thang", "ngay", "tuan", "moi", "nhat",
    "tai", "day", "va", "cua", "cho", "cac", "toi", "voi", "tu", "theo",
    "tinh", "phu", "thu", "chi", "dich", "vu", "hay", "bi", "duoc", "nhan",
}


def load_sync_module():
    """Nạp module sync_inventory_to_hubs để dùng ĐÚNG rule và pipeline upstream."""
    path = os.path.join(BASE_DIR, "scripts", "sync_inventory_to_hubs.py")
    spec = importlib.util.spec_from_file_location("sync_inv", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ----------------------------------------------------------------------
# Tiện ích token
# ----------------------------------------------------------------------
TOKEN_RE = re.compile(r"[a-zA-Zà-ỹĐđ0-9]+")


def tokenize(text):
    return [t.lower() for t in TOKEN_RE.findall(text or "")]


def significant_tokens(text):
    return [t for t in tokenize(text) if t not in STOPWORD_HINTS and len(t) > 1]


def title_case(name):
    """Viết hoa chữ đầu mỗi từ, giữ nguyên phần còn lại."""
    def cap(w):
        return w[0].upper() + w[1:] if w else w
    parts = name.split(" ")
    out = []
    for p in parts:
        if p and p[0].islower() and p.isalpha():
            out.append(cap(p))
        else:
            out.append(p)
    return " ".join(out)


def clean_seed_name(keyword, max_words=4):
    """Tên cluster từ keyword thật: bỏ ký tự rác, cắt tối đa max_words từ."""
    k = re.sub(r"[^a-zA-Zà-ỹĐđ0-9\s]", " ", keyword or "")
    k = re.sub(r"\s+", " ", k).strip()
    words = k.split(" ")
    if len(words) > max_words:
        k = " ".join(words[:max_words])
    return title_case(k)


def _fold(text):
    """Bỏ dấu + bỏ khoảng trắng để so khớp 2 biến thể cùng nghĩa."""
    s = "".join(ch for ch in (text or "").lower() if not _has_diacritic(ch))
    return re.sub(r"[^a-z0-9]+", "", s)


def best_display_variant(seed_keyword, members, pool=None):
    """
    Keyword nguồn có thể viết không dấu ("vangphutai"). Nếu trong cụm (hoặc trong
    toàn bộ pool của theme) có biến thể CÙNG nghĩa nhưng có dấu ("vàng phú tài")
    thì lấy bản có dấu để tên hiển thị đúng.
    """
    if not seed_keyword or _has_diacritic(seed_keyword):
        return seed_keyword
    seed_fold = _fold(seed_keyword)
    if not seed_fold:
        return seed_keyword
    for it in list(members or []) + list(pool or []):
        kw = it.get('keyword', '')
        if _has_diacritic(kw) and _fold(kw) == seed_fold:
            return kw
    return seed_keyword


def catchall_base_name(theme_name, pillar_keyword):
    """Tên gốc cho cluster tổng hợp: bỏ tiền tố rác, ưu tiên cụm danh từ cốt lõi."""
    base = (theme_name or '').strip()
    for prefix in ('Hệ Thống ', 'He Thong '):
        if base.startswith(prefix):
            base = base[len(prefix):]
            break
    if not base:
        base = (pillar_keyword or 'Chủ đề').strip()
    return title_case(base)



# ----------------------------------------------------------------------
# TIER 2 - Entity (thương hiệu thật mined từ pool keyword của theme)
# ----------------------------------------------------------------------
VI_CHARS = set("àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộờớởỡợùúủũụưừứửữựỳýỷỹỵđ")


def _is_vietnamese(text):
    """Keyword tiếng Việt = có ít nhất 1 ký tự có dấu."""
    return any(ch in VI_CHARS for ch in (text or '').lower())


def _has_diacritic(token):
    return any(ch in token for ch in VI_CHARS)


def _display_entity(token):
    """Hiển thị thương hiệu: acronym ngắn -> VIET HOA (hpg -> HPG), còn lại -> Title Case."""
    if len(token) <= 4 and token.isalpha() and not _has_diacritic(token):
        return token.upper()
    return title_case(token)


def mine_entities(items, theme_tokens, curated=None, concept_tokens=None, strict=True):
    """
    Entity = token thương hiệu. 3 tín hiệu phải cùng đạt (ngoại trừ lexicon curate):
      1. Lexicon curate khớp chuỗi -> chắc chắn là entity.
      2. Token KHÔNG dấu (vietcombank, cgv, hpg, pnj) - dấu hiệu mạnh của brand viết tắt.
      3. Token có dấu chỉ chấp nhận khi nằm trong lexicon curate.
    Bổ sung: khá nhiều keyword, chiếm <= CONCEPT_SHARE_MAX tổng số keyword,
    không thuộc concept token (pillar + top keyword + trigger của rule).
    """
    curated = curated or {}
    concept_tokens = concept_tokens or set()
    token_kw = defaultdict(list)
    for it in items:
        for t in set(tokenize(it['keyword'])):
            token_kw[t].append(it)

    n = max(len(items), 1)
    candidates = {}
    for tok, kws in token_kw.items():
        if len(kws) < MIN_ENTITY_KEYWORDS:
            continue
        if tok in STOPWORD_HINTS or tok in GENERIC_TOKENS:
            continue
        if tok in theme_tokens or tok in concept_tokens:
            continue
        if tok.isdigit() or len(tok) < 2:
            continue
        share = len(kws) / n
        if share > CONCEPT_SHARE_MAX:
            continue
        # Không dấu = ứng viên brand mạnh; có dấu = từ tiếng Việt thường, loại
        if strict and _has_diacritic(tok):
            continue
        # Token phải xuất hiện trong ngữ cảnh tiếng Việt (loại token Đức/Pháp/Anh
        # lọt vào từ CSV so sánh ngân hàng quốc tế)
        vi_ctx = sum(1 for it in kws if _is_vietnamese(it['keyword']))
        if vi_ctx / len(kws) < 0.6:
            continue
        candidates[tok] = len(kws)

    # Ưu tiên lexicon curate, loại token bị token dài hơn bao trùm
    out = {}
    for tok, cnt in sorted(candidates.items(), key=lambda x: -len(x[0])):
        if any(tok != other and tok in other for other in candidates):
            continue
        out[tok] = cnt
    for tok in curated:
        out.setdefault(tok, 0)
    return out


def collect_concept_tokens(items, rules, theme_tokens, top_n=8):
    """Concept = token của pillar + top keyword theo volume + token nằm trong trigger rule."""
    concepts = set(theme_tokens)
    for rule in rules:
        for tr in rule[1]:
            concepts.update(significant_tokens(tr))
    for it in sorted(items, key=lambda x: x.get('volume', 0), reverse=True)[:top_n]:
        concepts.update(significant_tokens(it['keyword']))
    return concepts



# ----------------------------------------------------------------------
# TIER 1 - Intent (rule trigger, ưu tiên trigger dài nhất)
# ----------------------------------------------------------------------
def assign_intent_tier(items, rules):
    assigned = []
    residual = []
    for it in items:
        kw = it['keyword'].lower()
        best = None
        best_len = -1
        for rule in rules:
            topic_name, triggers = rule[0], rule[1]
            for tr in triggers:
                if tr and tr.lower() in kw and len(tr) > best_len:
                    best = topic_name
                    best_len = len(tr)
        if best:
            assigned.append((best, it))
        else:
            residual.append(it)
    return assigned, residual


# ----------------------------------------------------------------------
# TIER 3 - Residual seed-and-absorb
# ----------------------------------------------------------------------
def cluster_residual(items, max_clusters, pool=None):
    """Seed = keyword volume cao nhất, hút các keyword còn lại có chung token hữu nghĩa."""
    pool = sorted(items, key=lambda x: (x['volume'], x['opportunity_score']), reverse=True)
    clusters = []
    used = set()

    while pool and len(clusters) < max_clusters:
        seed = pool[0]
        seed_tokens = set(significant_tokens(seed['keyword']))
        members = [seed]
        used.add(seed['keyword'])
        rest = []
        for it in pool[1:]:
            if it['keyword'] in used:
                continue
            it_tokens = set(significant_tokens(it['keyword']))
            if not it_tokens or not seed_tokens:
                rest.append(it)
                continue
            overlap = len(seed_tokens & it_tokens)
            if overlap >= 1 and (overlap / min(len(it_tokens), len(seed_tokens))) >= 0.34:
                members.append(it)
                used.add(it['keyword'])
            else:
                rest.append(it)
        clusters.append({
            'name': clean_seed_name(best_display_variant(seed['keyword'], members, pool)),
            'members': members,
            'tier': 'residual',
        })
        pool = rest

    # Vượt cap -> gộp phần dư vào cluster cuối
    if pool and clusters:
        clusters[-1]['members'].extend(pool)
    return clusters


# ----------------------------------------------------------------------
# Cổng chất lượng tên + cleanup shell
# ----------------------------------------------------------------------
def name_has_overlap(name, items):
    """Tên phải có >= 1 token hữu nghĩa trùng với keyword trong cụm."""
    name_tokens = set(significant_tokens(name))
    if not name_tokens:
        return False
    for it in items:
        if name_tokens & set(significant_tokens(it['keyword'])):
            return True
    return False


def refine_cluster_name(cluster, pillar_keyword, theme_tokens, rules):
    """
    Cluster residual có tên trùng pillar (vd seed = "cổ tức" trong theme "cổ tức")
    thì bổ sung token đặc trưng nhất của cụm để tên có nghĩa, vd "Cổ tức & Chia".
    """
    name = cluster['cluster_name']
    name_tokens = set(significant_tokens(name))
    pillar_tokens = set(significant_tokens(pillar_keyword or "")) | set(theme_tokens)
    if not name_tokens or not name_tokens.issubset(pillar_tokens):
        return name

    # Ưu tiên token xuất hiện trong nhiều keyword của cụm
    counter = Counter()
    for it in cluster.get('members', []):
        for t in set(significant_tokens(it['keyword'])):
            if t not in pillar_tokens and t not in name_tokens:
                counter[t] += 1
    if not counter:
        return name
    best_token, best_cnt = counter.most_common(1)[0]
    if best_cnt < 2:
        return name
    return '%s & %s' % (name, title_case(best_token))


def merge_shells(clusters, min_kw=MIN_CLUSTER_KEYWORDS):
    """Gộp cluster vỏ (< min_kw) vào cụm có overlap token cao nhất."""
    clusters = [c for c in clusters]
    kept, shells = [], []
    for c in clusters:
        (shells if len(c['members']) < min_kw else kept).append(c)

    for sh in shells:
        sh_tokens = set(significant_tokens(sh['cluster_name']))
        best, best_score = None, 0.0
        for k in kept:
            k_tokens = set(significant_tokens(k['cluster_name']))
            score = len(sh_tokens & k_tokens)
            if score > best_score:
                best, best_score = k, score
        if best is not None:
            best['members'].extend(sh['members'])
            best['merged_from'] = best.get('merged_from', []) + [sh['cluster_name']]
    return kept


# ----------------------------------------------------------------------
# Thuật toán chính
# ----------------------------------------------------------------------
def build_new_clusters(canonical_clusters, rules, theme_name, pillar_keyword, sector):
    """
    Trả về danh sách cluster mới theo schema production:
    cluster_name, count, total_volume, top_keywords (+ tier, entity, slug, no_page)
    """
    total_kw = len(canonical_clusters)
    theme_tokens = set(significant_tokens(theme_name)) | set(significant_tokens(pillar_keyword or ""))
    is_mega = total_kw >= MEGA_THEME_KW
    max_clusters = MAX_CLUSTERS_MEGA if is_mega else MAX_CLUSTERS_NORMAL

    def to_cluster(name, members, tier, entity=None):
        members = sorted(members, key=lambda x: (x.get('opportunity_score', 0), x.get('volume', 0)), reverse=True)
        vol = sum(m.get('volume', 0) for m in members)
        top = members[:15]
        return {
            'cluster_name': name,
            'count': len(members),
            'total_volume': vol,
            'tier': tier,
            'entity': entity,
            'slug': slugify(name),
            'no_page': len(members) < MIN_CLUSTER_KEYWORDS,
            'members': members,
            'top_keywords': [
                {
                    'keyword': k['keyword'],
                    'volume': k.get('volume', 0),
                    'cluster_volume': k.get('total_cluster_volume', k.get('volume', 0)),
                    'cpc': k.get('cpc', 0.0),
                    'competition': k.get('competition', 'Low'),
                    'kd': k.get('kd', 0),
                    'trending': k.get('trending', False),
                    'intent': k.get('intent', 'Informational'),
                    'score': k.get('opportunity_score', 0),
                    'quadrant': k.get('quadrant', 'Supporting'),
                    'secondary_synonyms': (k.get('secondary_keywords') or [])[:3],
                } for k in top
            ],
        }

    clusters = []

    curated = CURATED_ENTITIES.get(sector, {})
    concept_tokens = collect_concept_tokens(canonical_clusters, rules, theme_tokens)
    entities = mine_entities(canonical_clusters, theme_tokens, curated, concept_tokens, strict=True)
    curated_tokens = set(curated.keys())

    # Rule của theme đã tự bao phủ chiều brand thì không cần tách entity lần nữa
    # (vd cinema/rap có rule "Cụm rạp & Đặt vé" đã chứa cgv/lotte/galaxy)
    rule_mentions_entity = any(
        any(ent in [t.lower() for t in tokenize(tr)] or ent in tr.lower()
            for ent in curated_tokens for tr in rule[1])
        for rule in rules
    ) if curated_tokens else False

    entity_hits = defaultdict(list)
    # Gộp alias cùng 1 thương hiệu (vietinbank + viettinbank -> VietinBank)
    groups = defaultdict(list)
    for ent in entities:
        disp = curated.get(ent) or _display_entity(ent)
        groups[disp].append(ent)

    for disp, tokens in groups.items():
        is_curated = any(t in curated_tokens for t in tokens)
        if not is_mega:
            if not is_curated or rule_mentions_entity:
                continue
        for it in canonical_clusters:
            toks = tokenize(it['keyword'])
            if any(t in toks for t in tokens):
                entity_hits[disp].append(it)


    # Lọc brand quá nhỏ (theme thường) hoặc trùng thương hiệu
    min_entity_kw = MIN_ENTITY_KEYWORDS if is_mega else max(MIN_ENTITY_KEYWORDS, int(total_kw * 0.03))
    entity_hits = {e: v for e, v in entity_hits.items() if len(v) >= min_entity_kw}


    if is_mega and entity_hits:
        # MEGA THEME: ưu tiên entity (mỗi thương hiệu là 1 cluster riêng)
        used = set()
        for disp, members in sorted(entity_hits.items(), key=lambda x: -len(x[1])):
            if len(members) < MIN_ENTITY_KEYWORDS:
                continue
            members = [m for m in members if m['keyword'] not in used]
            if not members:
                continue
            used.update(m['keyword'] for m in members)
            clusters.append(to_cluster(disp, members, 'entity', disp))

        rest = [it for it in canonical_clusters if it['keyword'] not in used]
        assigned, residual = assign_intent_tier(rest, rules)
        by_topic = defaultdict(list)
        for topic, it in assigned:
            by_topic[topic].append(it)
        for topic, members in by_topic.items():
            clusters.append(to_cluster(topic, members, 'intent'))
        clusters.extend(
            to_cluster(c['name'], c['members'], c['tier'])
            for c in cluster_residual(residual, max_clusters, canonical_clusters)
        )
    else:
        # THEME THƯỜNG: intent trước, entity curate cho phần dư, residual cuối
        assigned, residual = assign_intent_tier(canonical_clusters, rules)
        by_topic = defaultdict(list)
        for topic, it in assigned:
            by_topic[topic].append(it)
        for topic, members in by_topic.items():
            clusters.append(to_cluster(topic, members, 'intent'))

        used = set()
        for disp, members in sorted(entity_hits.items(), key=lambda x: -len(x[1])):
            if len(members) < MIN_ENTITY_KEYWORDS:
                continue
            members = [m for m in members if m['keyword'] not in used]
            if not members:
                continue
            used.update(m['keyword'] for m in members)
            clusters.append(to_cluster(disp, members, 'entity', disp))

        leftover = [it for it in residual if it['keyword'] not in used]
        clusters.extend(
            to_cluster(c['name'], c['members'], c['tier'])
            for c in cluster_residual(leftover, max_clusters, canonical_clusters)
        )

    # Cổng chất lượng tên: tên không có overlap -> đổi tên theo seed keyword thật
    for c in clusters:
        c['cluster_name'] = refine_cluster_name(c, pillar_keyword, theme_tokens, rules)
        if not name_has_overlap(c['cluster_name'], c['top_keywords']):
            c['cluster_name'] = clean_seed_name(c['top_keywords'][0]['keyword']) if c['top_keywords'] else c['cluster_name']
            c['renamed_by_gate'] = True

    # Dọn cluster vỏ
    clusters = merge_shells(clusters)

    # Giữ tối đa max_clusters theo chính sách chừa slot cho từng tầng
    clusters, dropped = select_clusters(clusters, max_clusters, is_mega, theme_name, total_kw)

    # Cluster tổng hợp cho thương hiệu bị loại (giữ đủ độ phủ keyword)
    if dropped:
        catch_members = [m for c in dropped for m in c.get('members', [])]
        if len(catch_members) >= MIN_CLUSTER_KEYWORDS:
            catch = to_cluster('%s khác' % catchall_base_name(theme_name, pillar_keyword), catch_members, 'catchall')
            catch['merged_from'] = [c['cluster_name'] for c in dropped]
            clusters.append(catch)
    return clusters


def select_clusters(clusters, max_n, is_mega, theme_name, total_kw=0):
    """
    Chính sách chừa slot:
      mega-theme  : 3 intent + N brand (brand >= 0.5% keyword của theme) + 1 residual
                    -> số cluster có thể VƯỢT max_n: đây là tín hiệu cần nhiều page brand
      theme thường: 4 intent + 1 entity + 1 residual
    Trả về (clusters đã chọn, clusters bị loại).
    """
    by_tier = defaultdict(list)
    for c in clusters:
        by_tier[c['tier']].append(c)
    for t in by_tier:
        by_tier[t].sort(key=lambda c: -c['total_volume'])

    if is_mega:
        brand_floor = max(MIN_ENTITY_KEYWORDS, int(total_kw * MEGA_BRAND_MIN_SHARE))
        entity_pool = [c for c in by_tier.get('entity', []) if c['count'] >= brand_floor]
        quota = {'intent': 3, 'entity': len(entity_pool), 'residual': 1, 'catchall': 0}
    else:
        quota = {'intent': 4, 'entity': 1, 'residual': 1, 'catchall': 0}

    chosen, dropped = [], []
    for tier in ('intent', 'entity', 'residual', 'catchall'):
        pool = by_tier.get(tier, [])
        take = quota.get(tier, 0)
        chosen.extend(pool[:take])
        dropped.extend(pool[take:])

    if not is_mega and len(chosen) > max_n:
        rank = {'intent': 0, 'entity': 1, 'residual': 2, 'catchall': 3}
        chosen.sort(key=lambda c: (rank.get(c['tier'], 3), -c['total_volume']))
        keep, extra = chosen[:max_n], chosen[max_n:]
        dropped.extend(extra)
        chosen = keep
    chosen.sort(key=lambda c: -c['total_volume'])
    return chosen, dropped



def slugify(name):
    s = re.sub(r"đ", "d", (name or "").lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


# Entity curate theo sector (bổ sung cho lexicon sẵn có)
CURATED_ENTITIES = {
    'Financial': {
        'vietcombank': 'Vietcombank', 'vietcom': 'Vietcombank', 'vcom': 'Vietcombank', 'vcb': 'Vietcombank',
        'techcombank': 'Techcombank', 'techcom': 'Techcombank', 'tcb': 'Techcombank',
        'mbbank': 'MBB', 'mb bank': 'MBB', 'acb': 'ACB', 'bidv': 'BIDV', 'agribank': 'Agribank',
        'vpbank': 'VPBank', 'scb': 'SCB', 'vib': 'VIB', 'shb': 'SHB', 'msb': 'MSB',
        'ocb': 'OCB', 'tpbank': 'TPBank', 'hdbank': 'HDBank',
        'vietinbank': 'VietinBank', 'viettinbank': 'VietinBank', 'vtb': 'VietinBank',
        'eximbank': 'Eximbank', 'seabank': 'Seabank', 'sacombank': 'Sacombank',
        'vndirect': 'VNDirect', 'futu': 'Futu', 'tiger': 'Tiger', 'econstock': 'econstock',
    },
    'cinema': {
        'cgv': 'CGV', 'lotte': 'Lotte', 'galaxy': 'Galaxy', 'bhd': 'BHD', 'beta': 'Beta',
        'cinestar': 'Cinestar', 'quốc gia': 'Quốc Gia', 'dcine': 'Dcine', 'megags': 'MegaGS',
    },
    'vehicle-hub': {
        'honda': 'Honda', 'yamaha': 'Yamaha', 'toyota': 'Toyota', 'suzuki': 'Suzuki',
        'vespa': 'Vespa', 'bản tay ga': 'Bản tay ga',
    },
    'insurtech': {
        'bảo việt': 'Bảo Việt', 'baoviet': 'Bảo Việt', 'manulife': 'Manulife',
        'prudential': 'Prudential', 'aia': 'AIA', 'pvi': 'PVI', 'bảo minh': 'Bảo Minh',
    },
    'telco': {
        'viettel': 'Viettel', 'vinaphone': 'Vinaphone', 'mobifone': 'Mobifone',
        'vietnamobile': 'VinaMobile', 'gvn': 'g.vn', 'vinacomm': 'Vinacomm',
    },
    'ota': {
        'traveloka': 'Traveloka', 'klook': 'Klook', 'booking': 'Booking', 'agoda': 'Agoda',
    },
    'other': {
        'momo': 'MoMo', 'zalopay': 'ZaloPay', 'vnpay': 'VNPay',
    },
}


# ----------------------------------------------------------------------
# Chạy PoC
# ----------------------------------------------------------------------
def collect_csv_paths(mod, sector, slug):
    """Tái tạo logic gom CSV theo slug (không chạy lại toàn bộ inventory)."""
    s_dir = os.path.join(mod.INVENTORY_DIR, sector)
    groups = defaultdict(list)
    for fpath in sorted(__import__('glob').glob(os.path.join(s_dir, '*.csv'))):
        raw_slug = os.path.splitext(os.path.basename(fpath))[0]
        clean_slug = re.sub(r'[\s_]*\(\d+\)$', '', raw_slug).strip()
        canonical = mod.MERGE_MAP.get(clean_slug, mod.MERGE_MAP.get(clean_slug.lower(), clean_slug))
        groups[canonical].append(fpath)
    return groups.get(slug, [])


def run_theme(mod, slug, sector):
    paths = collect_csv_paths(mod, sector, slug)
    if not paths:
        return None

    captured = {}
    original = mod.build_adaptive_clusters

    def spy(canonical_clusters, **kwargs):
        captured['canonical_clusters'] = canonical_clusters
        return original(canonical_clusters, **kwargs)

    mod.build_adaptive_clusters = spy
    try:
        old_theme = mod.process_csv_paths(paths, sector, slug)
    finally:
        mod.build_adaptive_clusters = original

    if not old_theme:
        return None

    canonical = captured.get('canonical_clusters') or []
    rules = mod.USECASE_SPECIFIC_RULES.get(slug) or mod.SECTOR_SPECIFIC_RULES.get(sector, [])
    pillar = (old_theme.get('pillar_keyword') or {}).get('keyword', '')

    new_clusters = build_new_clusters(
        canonical, rules, old_theme.get('name', slug), pillar, sector
    )
    return {
        'slug': slug,
        'sector': sector,
        'name': old_theme.get('name'),
        'pillar': pillar,
        'clean_keywords_count': old_theme.get('clean_keywords_count'),
        'canonical_topics_count': len(canonical),
        'rules_source': 'usecase' if mod.USECASE_SPECIFIC_RULES.get(slug) else 'sector',
        'rule_count': len(rules),
        'old_clusters': old_theme.get('sub_clusters') or [],
        'new_clusters': new_clusters,
    }


def cluster_stats(clusters, total_kw):
    if not clusters:
        return {'count': 0, 'max_share': 0, 'shells': 0, 'name_overlap_rate': 0, 'names': []}
    biggest = max(c['count'] for c in clusters)
    shells = sum(1 for c in clusters if c['count'] < MIN_CLUSTER_KEYWORDS)
    ok = 0
    for c in clusters:
        items = [{'keyword': k['keyword']} for k in c.get('top_keywords', [])]
        if name_has_overlap(c['cluster_name'], items):
            ok += 1
    return {
        'count': len(clusters),
        'max_share': biggest / total_kw if total_kw else 0,
        'shells': shells,
        'name_overlap_rate': ok / len(clusters),
        'names': [c['cluster_name'] for c in clusters],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--themes', default=','.join(DEFAULT_THEMES))
    ap.add_argument('--out-json', default=os.path.join(BASE_DIR, '07_REPORTS', 'data', 'poc_cluster_naming.json'))
    ap.add_argument('--out-md', default=os.path.join(BASE_DIR, '07_REPORTS', 'data', 'poc_cluster_naming_report.md'))
    args = ap.parse_args()

    mod = load_sync_module()
    wanted = [t.strip() for t in args.themes.split(',') if t.strip()]

    # map slug -> sector
    slug_sector = {}
    for sector in sorted(os.listdir(mod.INVENTORY_DIR)):
        sdir = os.path.join(mod.INVENTORY_DIR, sector)
        if not os.path.isdir(sdir):
            continue
        for f in __import__('glob').glob(os.path.join(sdir, '*.csv')):
            raw = os.path.splitext(os.path.basename(f))[0]
            clean = re.sub(r'[\s_]*\(\d+\)$', '', raw).strip()
            canon = mod.MERGE_MAP.get(clean, mod.MERGE_MAP.get(clean.lower(), clean))
            slug_sector.setdefault(canon, sector)

    results = []
    for slug in wanted:
        sector = slug_sector.get(slug)
        if not sector:
            print('!! Khong tim thay sector cho slug:', slug)
            continue
        print('Dang xu ly theme %-18s sector=%s ...' % (slug, sector), flush=True)
        res = run_theme(mod, slug, sector)
        if res:
            results.append(res)

    # Xuất báo cáo
    lines = []
    lines.append('# PoC Adaptive Clustering v2 - Bao cao doi soat Before vs After\n')
    lines.append('| Theme | Sector | KW | Clusters truoc | Clusters sau | Cluster lon nhat (truoc) | Cluster lon nhat (sau) | Shell truoc | Shell sau |')
    lines.append('|---|---|---|---|---|---|---|---|---|')
    payload = []
    for r in results:
        total = r['clean_keywords_count']
        old = cluster_stats(r['old_clusters'], total)
        new = cluster_stats(r['new_clusters'], total)
        old_max = max(r['old_clusters'], key=lambda c: c['count']) if r['old_clusters'] else None
        new_max = max(r['new_clusters'], key=lambda c: c['count']) if r['new_clusters'] else None
        lines.append('| %s | %s | %s | %d | %d | %s (%d kw / %.0f%%) | %s (%d kw / %.0f%%) | %d | %d |' % (
            r['slug'], r['sector'], format(total, ','), old['count'], new['count'],
            (old_max['cluster_name'] if old_max else '-'),
            (old_max['count'] if old_max else 0), (old_max['count'] / total * 100 if old_max else 0),
            (new_max['cluster_name'] if new_max else '-'),
            (new_max['count'] if new_max else 0), (new_max['count'] / total * 100 if new_max else 0),
            old['shells'], new['shells']))
        payload.append({
            'slug': r['slug'], 'sector': r['sector'], 'name': r['name'], 'pillar': r['pillar'],
            'clean_keywords_count': r['clean_keywords_count'],
            'canonical_topics_count': r['canonical_topics_count'],
            'rules_source': r['rules_source'], 'rule_count': r['rule_count'],
            'old': r['old_clusters'], 'new': r['new_clusters'],
            'old_stats': old, 'new_stats': new,
        })

    for p in payload:
        lines.append('\n---\n')
        lines.append('## Theme `%s` (%s) - pillar: %s' % (p['slug'], p['sector'], p['pillar']))
        lines.append('')
        lines.append('Keyword: %s | Canonical topics: %s | Rule nguon: %s (%d rule)' % (
            format(p['clean_keywords_count'], ','), format(p['canonical_topics_count'], ','),
            p['rules_source'], p['rule_count']))
        lines.append('')
        lines.append('| BEFORE - ten | kw | vol | | AFTER - ten | tier | kw | vol | Top keyword |')
        lines.append('|---|---|---|---|---|---|---|---|---|')
        rows = max(len(p['old']), len(p['new']))
        for i in range(rows):
            o = p['old'][i] if i < len(p['old']) else None
            n = p['new'][i] if i < len(p['new']) else None
            o_name = o['cluster_name'] if o else '-'
            o_kw = format(o['count'], ',') if o else '-'
            o_vol = format(o['total_volume'], ',') if o else '-'
            n_name = n['cluster_name'] if n else '-'
            n_tier = n.get('tier', '-') if n else '-'
            n_kw = format(n['count'], ',') if n else '-'
            n_vol = format(n['total_volume'], ',') if n else '-'
            n_top = n['top_keywords'][0]['keyword'] if n and n.get('top_keywords') else '-'
            lines.append('| %s | %s | %s | | %s | %s | %s | %s | %s |' % (
                o_name, o_kw, o_vol, n_name, n_tier, n_kw, n_vol, n_top))
        lines.append('')
        lines.append('Ten co overlap voi top keyword - truoc: %.0f%% | sau: %.0f%%' % (
            p['old_stats']['name_overlap_rate'] * 100, p['new_stats']['name_overlap_rate'] * 100))

    md = '\n'.join(lines) + '\n'
    with open(args.out_md, 'w', encoding='utf-8') as f:
        f.write(md)
    with open(args.out_json, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print('\n' + md)
    print('Da xuat: %s' % args.out_md)
    print('Da xuat: %s' % args.out_json)


if __name__ == '__main__':
    main()
