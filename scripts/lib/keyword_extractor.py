# -*- coding: utf-8 -*-
"""
KEYWORD & ENTITY EXTRACTOR (CORE LIBRARY)
Trích xuất Keyphrase & Thực thể (Entity) từ content đối thủ phục vụ Content Gap & Information Gain.

Hybrid engine (graceful degradation - tự động dùng thư viện nào có sẵn):
1. YAKE  - Statistical keyphrase extraction (không cần model, nhanh).
2. RAKE  - Graph-based phrase extraction (cụm từ dài, chuẩn ý nghĩa).
3. KeyBERT - Semantic embedding extraction (hiểu ngữ nghĩa, cần sentence-transformers/torch).

Ứng dụng cho Web Platform:
- Bóc tách bộ từ khóa/thực thể mà đối thủ dẫn đầu SERP đang triển khai.
- Xác định "Table Stakes" (bắt buộc phải có) và "Differentiators" (điểm khác biệt).
- Phát hiện Information Gain (góc dữ liệu độc quyền mà LLM/AI Engine không scrape được).
"""

import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict


def _nfc(text: str) -> str:
    """Chuẩn hóa Unicode NFC để tránh tách dấu khỏi ký tự gốc (NFD) gây mojibake."""
    if not text:
        return text
    return unicodedata.normalize("NFC", text)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from keyword_intelligence import STOPWORDS as BASE_STOPWORDS, SYNONYM_MAP as BASE_SYNONYM_MAP
except Exception:
    BASE_STOPWORDS = set()
    BASE_SYNONYM_MAP = {}


# ---------------------------------------------------------------------------
# 1. TỪ ĐIỂN STOPWORDS TIẾNG VIỆT & THỰC THỂ
# ---------------------------------------------------------------------------

VN_STOPWORDS = set(BASE_STOPWORDS) | {
    "a", "à", "á", "ạ", "ạch", "ai", "anh", "ấy", "b", "bao giờ", "bằng",
    "bị", "bởi", "bớt", "cả", "cách", "các", "cái", "cần", "càng", "cấp",
    "chỉ", "chiếc", "cho", "chớ", "chưa", "chuyện", "có", "có thể", "còn",
    "cùng", "cũng", "cứ", "của", "dà", "dạ", "dẫu", "dưới", "đã", "đang",
    "đâu", "đây", "đấy", "để", "đến", "đều", "đi", "đó", "đôi", "đồng",
    "được", "e", "em", "gì", "giữa", "gồm", "hay", "hãy", "hết", "hoặc",
    "hơn", "khi", "không", "lại", "là", "làm", "lần", "lên", "lúc", "mà",
    "mang", "mỗi", "một", "mới", "mình", "muốn", "nếu", "ngay", "nên",
    "người", "nhau", "nhiều", "như", "nhưng", "những", "này", "nào", "nếu",
    "nơi", "nữa", "nước", "ở", "phải", "qua", "ra", "rằng", "rất", "rồi",
    "sau", "sẽ", "số", "sự", "tại", "tất", "tập", "theo", "thì", "thế",
    "thể", "thôi", "thường", "trên", "trong", "trước", "từ", "tới", "tuy",
    "và", "vẫn", "vào", "vậy", "về", "vì", "việc", "với", "vừa", "ý",
    "các", "mấy", "nhỉ", "nhé", "v.v", "vv", "v.v.", "etc", "al",
}

# Từ khóa phổ biến của website (điều hướng, boilerplate) - loại khỏi kết quả
NAV_NOISE = {
    "menu", "trang chủ", "liên hệ", "đăng nhập", "đăng ký", "tìm kiếm",
    "bình luận", "chia sẻ", "xem thêm", "bài viết khác", "tin liên quan",
    "cookie", "chính sách", "điều khoản", "quảng cáo", "hotline", "email",
}

# Lexicon thực thể: ngân hàng, tổ chức, thương hiệu lớn tại VN (danh sách curate)
ENTITY_LEXICON = {
    "momo", "vietcombank", "techcombank", "bidv", "vietinbank", "agribank",
    "acb", "sacombank", "vpbank", "mbbank", "tpbank", "vib", "shb", "hdbank",
    "ocb", "msb", "seabank", "eximbank", "lienvietpostbank", "namabank",
    "bacabank", "pvcombank", "scb", "abbank", "kienlongbank", "oceanbank",
    "cimb", "cake", "timo", "vnpay", "zalopay", "moca", "shopeepay",
    "cổng dịch vụ công", "vneid", "cục cảnh sát giao thông", "c02", "etag",
    "vetchi", "viettel", "vinaphone", "mobifone", "vietnamobile", "vinfast",
    "honda", "yamaha", "toyota", "cgv", "lotte", "galaxy", "beta",
    # Bảo hiểm
    "bảo việt", "baoviet", "manulife", "prudential", "dai-ichi", "daiichi",
    "fwd", "generali", "pvi", "bảo minh", "baominh", "liberty", "aia",
    "chubb", "bhyt", "vssid", "bảo hiểm xã hội việt nam",
}

# Regex nhận diện thực thể số liệu (Information Gain - dữ liệu định lượng)
NUMERIC_PATTERNS = [
    r"\d+(?:[.,]\d+)?\s*%",
    r"\d+(?:[.,]\d+)?\s*(?:triệu|tỷ|nghìn|ngàn|đồng|vnđ|vnd|usd)",
    r"\d+(?:[.,]\d+)?\s*(?:tháng|năm|ngày|giờ|phút|tuần|quý)",
    r"\d{1,3}(?:[.,]\d{3})+",
]

QUESTION_MARKERS = [
    "là gì", "như thế nào", "bao nhiêu", "có nên", "so sánh", "tại sao",
    "khi nào", "ở đâu", "cách", "hướng dẫn", "thủ tục", "quy trình",
    "điều kiện", "thời hạn", "lãi suất", "phí", "mức phạt", "hạn mức",
]

UTILITY_SIGNALS = [
    "công cụ", "tính toán", "tra cứu", "máy tính", "bảng tính", "tra biển số",
    "tra phạt nguội", "định giá", "mô phỏng", "so sánh", "simulator", "calculator",
]


def _load_stopwords() -> set:
    return set(VN_STOPWORDS)


STOPWORDS = _load_stopwords()


# ---------------------------------------------------------------------------
# 2. TRÍCH XUẤT KEYPHRASE (YAKE / RAKE / KeyBERT)
# ---------------------------------------------------------------------------

try:
    import yake
    HAS_YAKE = True
except Exception:
    HAS_YAKE = False

try:
    from rake_nltk import Rake
    HAS_RAKE = True
except Exception:
    HAS_RAKE = False

try:
    from keybert import KeyBERT
    HAS_KEYBERT = True
except Exception:
    HAS_KEYBERT = False

try:
    from sentence_transformers import SentenceTransformer, util as st_util
    HAS_ST = True
except Exception:
    HAS_ST = False

try:
    from pyvi import ViTokenizer
    HAS_PYVI = True
except Exception:
    HAS_PYVI = False


def segment_text(text: str) -> str:
    """Tách từ tiếng Việt (ghép từ ghép bằng '_') để tránh cắt ngang ranh giới từ."""
    if not text:
        return text
    text = _nfc(text)
    if not HAS_PYVI:
        return text
    try:
        return ViTokenizer.tokenize(text)
    except Exception:
        return text


def _restore(phrase: str) -> str:
    """Khôi phục cụm từ đã tách từ (bỏ dấu gạch dưới nối từ ghép)."""
    return phrase.replace("_", " ").strip()


_KEYBERT_MODEL = None
_ST_MODEL = None
KEYBERT_MODEL_NAME = os.environ.get(
    "KEYBERT_MODEL", "paraphrase-multilingual-MiniLM-L12-v2"
)


def _is_meaningful(phrase: str) -> bool:
    """Loại bỏ cụm từ rác: quá ngắn, toàn stopword, boilerplate điều hướng."""
    p = _restore(phrase).lower()
    if len(p) < 3:
        return False
    if p in NAV_NOISE:
        return False
    tokens = [t for t in re.findall(r"\w+", p, flags=re.UNICODE) if t]
    if not tokens:
        return False
    content_tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    return len(content_tokens) >= 1


def _valid_ngram_set(seg_text: str, max_n: int = 3) -> set:
    """
    Sinh tập n-gram hợp lệ (đúng ranh giới từ) từ văn bản đã tách từ.
    Dùng để lọc bỏ các cụm từ cắt ngang ranh giới từ do YAKE sinh ra.
    """
    toks = seg_text.split()
    valid = set()
    for n in range(1, max_n + 1):
        for i in range(len(toks) - n + 1):
            gram = _restore(" ".join(toks[i:i + n])).lower()
            valid.add(re.sub(r"\s+", " ", gram).strip())
    return valid


def extract_yake(text: str, top_n: int = 25, ngram: int = 3) -> list:
    """Trích xuất keyphrase thống kê bằng YAKE. Trả list[(phrase, score)] (score nhỏ = quan trọng hơn)."""
    if not HAS_YAKE or not text:
        return []
    text = _nfc(text)
    try:
        # YAKE chạy trên text gốc, sau đó lọc theo tập n-gram hợp lệ (ranh giới từ tiếng Việt)
        valid_grams = _valid_ngram_set(segment_text(text), max_n=ngram) if HAS_PYVI else None
        kw = yake.KeywordExtractor(
            lan="vi", n=ngram, dedupLim=0.7, windowsSize=2,
            top=max(top_n * 2, top_n), stopwords=STOPWORDS,
        )
        results = []
        for phrase, score in kw.extract_keywords(text):
            norm = re.sub(r"\s+", " ", _restore(phrase).lower()).strip()
            if valid_grams is not None and norm not in valid_grams:
                continue
            if _is_meaningful(phrase):
                results.append((norm, float(score)))
        return results[:top_n]
    except Exception as e:
        print(f"[WARN] YAKE lỗi: {e}")
        return []


def extract_rake(text: str, top_n: int = 25, max_phrase_len: int = 5) -> list:
    """Trích xuất cụm từ bằng RAKE (graph-based). Trả list[(phrase, score)] (score lớn = quan trọng hơn)."""
    if not HAS_RAKE or not text:
        return []
    try:
        text = segment_text(text)
        rake = Rake(
            stopwords=STOPWORDS,
            min_length=1,
            max_length=max_phrase_len,
            include_repeated_phrases=False,
            word_tokenizer=lambda t: t.split(),
        )
        rake.extract_keywords_from_text(text)
        results = []
        for score, phrase in rake.get_ranked_phrases_with_scores():
            if _is_meaningful(phrase):
                results.append((_restore(phrase).lower(), float(score)))
        # Khử trùng lặp giữ điểm cao nhất
        seen = {}
        for phrase, score in results:
            if phrase not in seen or score > seen[phrase]:
                seen[phrase] = score
        ranked = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        return ranked[:top_n]
    except Exception as e:
        print(f"[WARN] RAKE lỗi: {e}")
        return []


def _get_keybert_model():
    global _KEYBERT_MODEL
    if _KEYBERT_MODEL is None:
        _KEYBERT_MODEL = KeyBERT(model=KEYBERT_MODEL_NAME)
    return _KEYBERT_MODEL


def extract_keybert(text: str, top_n: int = 25, ngram=(1, 2)) -> list:
    """Trích xuất keyphrase ngữ nghĩa bằng KeyBERT. Trả list[(phrase, score)] (score lớn = quan trọng hơn)."""
    if not HAS_KEYBERT or not text or len(text.strip()) < 20:
        return []
    text = _nfc(text)
    try:
        model = _get_keybert_model()
        results = model.extract_keywords(
            text,
            keyphrase_ngram_range=ngram,
            stop_words=list(STOPWORDS),
            top_n=max(top_n * 2, top_n),
            diversity=0.5,
        )
        out = []
        for phrase, score in results:
            if _is_meaningful(phrase):
                out.append((_restore(phrase).lower(), float(score)))
        return out[:top_n]
    except Exception as e:
        print(f"[WARN] KeyBERT lỗi: {e}")
        return []


def _get_st_model():
    global _ST_MODEL
    if _ST_MODEL is None:
        _ST_MODEL = SentenceTransformer(KEYBERT_MODEL_NAME)
    return _ST_MODEL


def rerank_semantic(text: str, candidates: list, top_n: int = 25) -> list:
    """
    Xếp hạng lại danh sách candidate phrase theo độ tương đồng ngữ nghĩa với văn bản
    bằng embedding đa ngữ (SentenceTransformer). Khắc phục nhược điểm fragment tiếng Việt
    của KeyBERT khi trích xuất tự do: candidate lấy từ YAKE/RAKE (đúng ranh giới từ),
    embedding chỉ đảm nhiệm vai trò chấm điểm ngữ nghĩa.

    Trả list[(phrase, cosine_score)] (score lớn = quan trọng hơn).
    """
    cands = [c for c in dict.fromkeys(candidates) if _is_meaningful(c)]
    if not HAS_ST or not text or not cands:
        return []
    text = _nfc(text)
    try:
        model = _get_st_model()
        doc_emb = model.encode([text], convert_to_tensor=True, show_progress_bar=False)
        cand_emb = model.encode(cands, convert_to_tensor=True, show_progress_bar=False)
        sims = st_util.cos_sim(doc_emb, cand_emb)[0].tolist()
        ranked = sorted(zip(cands, sims), key=lambda x: x[1], reverse=True)
        return [(p, float(s)) for p, s in ranked[:top_n]]
    except Exception as e:
        print(f"[WARN] Semantic rerank lỗi: {e}")
        return []


# ---------------------------------------------------------------------------
# 3. TRÍCH XUẤT THỰC THỂ (ENTITY)
# ---------------------------------------------------------------------------

def _canonicalize(text: str) -> str:
    t = text.lower()
    for syn, target in BASE_SYNONYM_MAP.items():
        t = re.sub(r"\b" + re.escape(syn) + r"\b", target, t)
    return t


def extract_entities(text: str, top_n: int = 20) -> dict:
    """
    Trích xuất thực thể theo 3 nhóm:
    - brand_org : ngân hàng / thương hiệu / tổ chức (lexicon + proper noun).
    - numeric   : số liệu định lượng (%, tiền, thời hạn) - tín hiệu Information Gain.
    - proper    : danh từ riêng viết hoa (địa danh, tên riêng).
    """
    if not text:
        return {"brand_org": [], "numeric": [], "proper": []}

    norm = _canonicalize(text)

    brand_counter = Counter()
    for ent in ENTITY_LEXICON:
        if re.search(r"\b" + re.escape(ent) + r"\b", norm):
            brand_counter[ent] += len(re.findall(r"\b" + re.escape(ent) + r"\b", norm))

    numeric_counter = Counter()
    for pat in NUMERIC_PATTERNS:
        for m in re.findall(pat, text, flags=re.UNICODE):
            numeric_counter[m.strip().lower()] += 1

    proper_counter = Counter()
    for m in re.findall(r"\b[A-ZĐ][\wÀ-ỹ]+(?:\s+[A-ZĐ][\wÀ-ỹ]+){0,2}\b", text, flags=re.UNICODE):
        low = m.lower()
        if low in STOPWORDS or low in NAV_NOISE:
            continue
        if any(t in STOPWORDS for t in low.split() if len(t) > 1):
            continue
        proper_counter[m.strip()] += 1

    return {
        "brand_org": [{"entity": e, "count": c} for e, c in brand_counter.most_common(top_n)],
        "numeric": [{"entity": e, "count": c} for e, c in numeric_counter.most_common(top_n)],
        "proper": [{"entity": e, "count": c} for e, c in proper_counter.most_common(top_n)],
    }


# ---------------------------------------------------------------------------
# 4. PHÂN TÍCH CONTENT GAP & INFORMATION GAIN
# ---------------------------------------------------------------------------

def _page_text(page: dict) -> str:
    """Gộp toàn bộ text khả dụng của 1 trang đối thủ (body + headings) sau khi chuẩn hóa."""
    parts = []
    for key in ("body_text", "h1", "h2", "h3"):
        val = page.get(key)
        if isinstance(val, list):
            parts.extend([str(x) for x in val])
        elif isinstance(val, str):
            parts.append(val)
    text = _nfc(" . ".join([p for p in parts if p]))
    # Chèn khoảng trắng tại ranh giới chữ-số / camelCase (chỉ dùng ký tự ASCII để không phá dấu tiếng Việt)
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    text = re.sub(r"(?<=[A-Za-z])(?=\d)", " ", text)
    text = re.sub(r"(?<=\d)(?=[A-Za-z])", " ", text)
    return re.sub(r"\s+", " ", text).strip()


# Token rác từ các trang render lỗi (JS app chưa hydrate, service worker, v.v.)
JUNK_TOKENS = {
    "error", "errors", "failed", "fail", "serviceworker", "navigator",
    "registration", "registered", "catch", "function", "undefined", "null",
    "load", "then", "const", "var", "let", "return", "window", "document",
    "false", "true", "object", "script", "loading", "bundle", "webpack",
}


def _looks_like_junk(text: str) -> bool:
    toks = re.findall(r"\b[a-z_]+\b", text.lower())
    if not toks:
        return True
    junk = sum(1 for t in toks if t in JUNK_TOKENS)
    return (junk / len(toks)) > 0.12


def _is_content_worthy(page: dict) -> bool:
    """Loại trang rác: quá ngắn hoặc nội dung chủ yếu là text lỗi JS/render."""
    text = _page_text(page)
    wc = page.get("word_count")
    if isinstance(wc, int) and wc < 150:
        return False
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    if len(words) < 120:
        return False
    if _looks_like_junk(text):
        return False
    return True


def _detect_utility_signals(text: str) -> list:
    t = text.lower()
    return [s for s in UTILITY_SIGNALS if s in t]


def _detect_question_markers(phrase: str) -> bool:
    p = phrase.lower()
    return any(m in p for m in QUESTION_MARKERS)


def _match_momo(ranked_all: list, momo_text: str, sim_threshold: float = 0.72) -> tuple:
    """
    Đối chiếu nội dung MoMo hiện hữu với các Concept của đối thủ ở cấp ngữ nghĩa (embedding).
    Trả về (covered, missing, momo_phrases_sample).
    """
    momo_phrases = [p for p, _ in extract_yake(momo_text, top_n=60)]
    momo_phrases += [p for p, _ in extract_rake(momo_text, top_n=60)]
    momo_phrases = list(dict.fromkeys(momo_phrases))

    concept_phrases = [c["phrase"] for c in ranked_all]

    c_emb = m_emb = None
    if HAS_ST and momo_phrases:
        try:
            model = _get_st_model()
            all_emb = model.encode(
                concept_phrases + momo_phrases, convert_to_tensor=True,
                normalize_embeddings=True, show_progress_bar=False,
            )
            c_emb = all_emb[:len(concept_phrases)]
            m_emb = all_emb[len(concept_phrases):]
        except Exception:
            c_emb = m_emb = None

    covered, missing = [], []
    for i, c in enumerate(ranked_all):
        matched = None
        sim = 0.0
        if c_emb is not None and len(momo_phrases) > 0:
            sims = st_util.cos_sim(c_emb[i], m_emb)[0]
            j = int(sims.argmax())
            sim = float(sims[j])
            if sim >= sim_threshold:
                matched = momo_phrases[j]
        elif c["phrase"] in momo_phrases:
            matched = c["phrase"]
            sim = 1.0

        base = {k: c[k] for k in ("phrase", "coverage", "coverage_pct", "is_question")}
        if matched:
            covered.append({**base, "matched_momo_phrase": matched, "similarity": round(sim, 3)})
        else:
            missing.append(base)

    return covered, missing, momo_phrases[:20]


def _cluster_concepts(phrase_pages: dict, phrase_scores: dict, page_count: int,
                      sim_threshold: float = 0.80) -> list:
    """
    Gom nhóm các cụm từ đồng nghĩa/gần nghĩa thành Concept (bằng embedding đa ngữ).
    Độ phủ của Concept = số trang riêng biệt chứa ít nhất 1 biến thể.
    Khắc phục hạn chế khớp chuỗi tuyệt đối: các trang diễn đạt khác nhau nhưng cùng ý
    vẫn được ghi nhận là "Table Stakes".
    """
    phrases = list(phrase_pages.keys())
    if not phrases:
        return []

    embs = None
    if HAS_ST:
        try:
            embs = _get_st_model().encode(
                phrases, convert_to_tensor=True, normalize_embeddings=True,
                show_progress_bar=False,
            )
        except Exception:
            embs = None

    idx = {p: i for i, p in enumerate(phrases)}
    order = sorted(phrases, key=lambda p: (len(phrase_pages[p]), phrase_scores[p]), reverse=True)
    assigned = set()
    clusters = []

    for p in order:
        if p in assigned:
            continue
        members = [p]
        assigned.add(p)
        if embs is not None:
            ip = idx[p]
            for q in order:
                if q in assigned:
                    continue
                sim = float(st_util.cos_sim(embs[ip], embs[idx[q]]))
                if sim >= sim_threshold:
                    members.append(q)
                    assigned.add(q)
        page_set = set()
        for m in members:
            page_set |= phrase_pages[m]
        rep = max(members, key=lambda m: (len(phrase_pages[m]), phrase_scores[m]))
        clusters.append({
            "phrase": rep,
            "coverage": len(page_set),
            "coverage_pct": round(len(page_set) / page_count * 100, 1),
            "score": round(sum(phrase_scores[m] for m in members), 3),
            "is_question": any(_detect_question_markers(m) for m in members),
            "variants": members[:6],
        })

    clusters.sort(key=lambda x: (x["coverage"], x["score"]), reverse=True)
    return clusters


def analyze_content_gap(competitor_pages: list, momo_text: str = None,
                        top_n: int = 25, use_keybert: bool = True) -> dict:
    """
    Phân tích Content Gap & Information Gain từ danh sách trang đối thủ.

    Input: competitor_pages - list dict, mỗi dict cần có tối thiểu:
           {rank, domain, title, url, h1[], h2[], h3[], body_text (tùy chọn)}
           momo_text - (tùy chọn) nội dung trang MoMo hiện hữu để tính Gap trực tiếp.
    Output: dict tổng hợp table_stakes, differentiators, top_keyphrases,
            entities, information_gain.
    """
    raw_pages = [p for p in (competitor_pages or []) if _page_text(p).strip()]
    pages = [p for p in raw_pages if _is_content_worthy(p)]
    excluded = len(raw_pages) - len(pages)
    n = len(pages)
    if n == 0:
        return {"error": "Không có dữ liệu trang đối thủ hợp lệ", "competitor_count": 0}

    phrase_coverage = defaultdict(set)   # phrase -> set(page index)
    phrase_rank_score = defaultdict(float)
    page_phrases = []                    # per-page top phrases
    entity_agg = Counter()
    numeric_agg = Counter()
    utility_hits = Counter()
    combined_texts = []

    for idx, page in enumerate(pages):
        text = _page_text(page)
        combined_texts.append(text)

        py = extract_yake(text, top_n=top_n)
        pr = extract_rake(text, top_n=top_n)

        merged = {}
        for phrase, score in py:
            merged[phrase] = merged.get(phrase, 0.0) + (1.0 / (1.0 + score))
        for phrase, score in pr:
            merged[phrase] = merged.get(phrase, 0.0) + score / 10.0

        # Xếp hạng ngữ nghĩa: chấm điểm các candidate (YAKE/RAKE) bằng embedding đa ngữ
        if use_keybert and HAS_ST:
            candidates = list(merged.keys())
            for phrase, sim in rerank_semantic(text, candidates, top_n=top_n * 2):
                merged[phrase] = merged.get(phrase, 0.0) + sim * 2.0

        top_page = sorted(merged.items(), key=lambda x: x[1], reverse=True)[:top_n]
        page_phrases.append({"rank": page.get("rank"), "domain": page.get("domain"),
                             "phrases": [{"phrase": p, "score": round(s, 3)} for p, s in top_page]})

        for phrase, score in top_page:
            phrase_coverage[phrase].add(idx)
            phrase_rank_score[phrase] += score

        ents = extract_entities(text, top_n=15)
        for e in ents["brand_org"]:
            entity_agg[e["entity"]] += e["count"]
        for e in ents["numeric"]:
            numeric_agg[e["entity"]] += e["count"]
        for u in _detect_utility_signals(text):
            utility_hits[u] += 1

    # Gom cụm ngữ nghĩa (Concept) & xếp hạng theo độ phủ cấp Concept
    ranked_all = _cluster_concepts(phrase_coverage, phrase_rank_score, n)

    coverage_threshold = max(2, (n + 1) // 2)
    table_stakes = [r for r in ranked_all if r["coverage"] >= coverage_threshold][:top_n]
    differentiators = [r for r in ranked_all if r["coverage"] == 1][:top_n]

    # Information Gain: câu hỏi/cụm ý nghĩa độ phủ thấp + thực thể số liệu + góc tiện ích
    ig_candidates = [r for r in ranked_all if r["coverage"] <= 1 and r.get("is_question")]
    question_gaps = [r["phrase"] for r in ig_candidates[:top_n]]

    # Content Gap: đối chiếu trang MoMo hiện hữu với Concept của đối thủ (cấp ngữ nghĩa)
    momo_gap = []
    content_gap = {"momo_analyzed": False}
    if momo_text:
        covered, missing, momo_sample = _match_momo(ranked_all, momo_text)
        total = len(ranked_all)
        content_gap = {
            "momo_analyzed": True,
            "competitor_concepts": total,
            "momo_covered": len(covered),
            "missing_in_momo": len(missing),
            "gap_pct": round(len(missing) / total * 100, 1) if total else 0.0,
            "momo_covered_concepts": covered[:top_n],
            "missing_concepts": missing[:top_n],
            "momo_phrases_sample": momo_sample,
        }
        momo_gap = [m["phrase"] for m in missing[:top_n]]

    competitor_utility = sorted(utility_hits.items(), key=lambda x: x[1], reverse=True)

    information_gain = {
        "question_gaps": question_gaps,
        "numeric_data_available": [{"entity": e, "count": c} for e, c in numeric_agg.most_common(15)],
        "competitor_utility_signals": [{"signal": s, "pages": c} for s, c in competitor_utility],
        "momo_missing_keyphrases": momo_gap,
        "recommended_unique_angles": _recommend_unique_angles(pages, question_gaps, competitor_utility),
    }

    return {
        "competitor_count": n,
        "excluded_low_quality_pages": excluded,
        "engines": {
            "yake": HAS_YAKE,
            "rake": HAS_RAKE,
            "semantic_rerank": HAS_ST and use_keybert,
            "embedding_model": KEYBERT_MODEL_NAME if (HAS_ST and use_keybert) else None,
        },
        "table_stakes": table_stakes,
        "differentiators": differentiators,
        "top_keyphrases": ranked_all[:top_n],
        "entities": {
            "brand_org": [{"entity": e, "count": c} for e, c in entity_agg.most_common(15)],
            "numeric": [{"entity": e, "count": c} for e, c in numeric_agg.most_common(15)],
        },
        "information_gain": information_gain,
        "content_gap": content_gap,
        "per_page": page_phrases,
    }


def _recommend_unique_angles(pages: list, question_gaps: list, utility_hits: Counter) -> list:
    """Gợi ý góc nội dung độc quyền MoMo (anti-LLM moat): tiện ích + dữ liệu động."""
    angles = []
    has_utility = len(utility_hits) > 0
    if not has_utility:
        angles.append("Đối thủ chưa có công cụ tra cứu/tính toán tương tác: xây Widget tiện ích trên Web (dữ liệu động, LLM không scrape được).")
    if question_gaps:
        angles.append("Bổ sung mục Giải đáp trực tiếp (Direct Answer) cho các câu hỏi đối thủ bỏ trống: " + "; ".join(question_gaps[:5]))
    angles.append("Nhúng bảng số liệu động (lãi suất/phí/biểu phí theo thời gian thực) thay vì nội dung tĩnh sao chép được.")
    angles.append("Gắn Schema FAQPage + BreadcrumbList + cơ chế Web-to-App để chiếm Rich Snippet và chuyển đổi.")
    return angles


# ---------------------------------------------------------------------------
# 5. CLI
# ---------------------------------------------------------------------------

def _clean_text(html: str) -> str:
    text = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Keyword & Entity Extractor (YAKE + RAKE + KeyBERT)")
    parser.add_argument("text", nargs="?", help="Đoạn text cần trích xuất")
    parser.add_argument("--url", help="URL cần cào và trích xuất")
    parser.add_argument("--top-n", type=int, default=15)
    parser.add_argument("--no-keybert", action="store_true", help="Tắt KeyBERT (nhanh hơn)")
    args = parser.parse_args()

    text = args.text or ""
    if args.url:
        import urllib.request
        req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            text = _clean_text(resp.read().decode("utf-8", errors="ignore"))

    if not text.strip():
        parser.error("Cần cung cấp text hoặc --url")

    print("\n=== KEYPHRASE EXTRACTION ===")
    print(f"YAKE    : {[p for p, _ in extract_yake(text, top_n=args.top_n)]}")
    print(f"RAKE    : {[p for p, _ in extract_rake(text, top_n=args.top_n)]}")
    if not args.no_keybert:
        print(f"KeyBERT : {[p for p, _ in extract_keybert(text, top_n=args.top_n)]}")
    print("\n=== ENTITIES ===")
    print(extract_entities(text, top_n=args.top_n))


if __name__ == "__main__":
    main()
