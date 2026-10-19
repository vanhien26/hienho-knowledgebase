# -*- coding: utf-8 -*-
"""
VIETNAMESE NLP GATEWAY (SSOT)
Backend tách từ tiếng Việt dùng chung cho toàn Web Platform pipeline.

Thứ tự ưu tiên (graceful degradation):
1. underthesea  - backend chính, word segmentation chuẩn, ~4.000 keyword/s
2. pyvi         - backend dự phòng (legacy, không còn maintain)
3. naive split  - fallback cuối, tách theo khoảng trắng (không đổi hành vi cũ)

Cách dùng:
    from lib.vi_nlp import segment, segment_text, backend, has_segmenter
    segment("giá vé rạp chiếu phim")       -> ['giá vé', 'rạp', 'chiếu phim']
    segment_text("giá vé rạp chiếu phim")  -> 'giá_vé rạp chiếu_phim'
"""

_UNDERTHESEA_TOKENIZE = None
_PYVI_TOKENIZE = None
_BACKEND = None


def _resolve_backend() -> str:
    """Xác định backend khả dụng, cache lại cho các lần gọi sau."""
    global _UNDERTHESEA_TOKENIZE, _PYVI_TOKENIZE, _BACKEND
    if _BACKEND is not None:
        return _BACKEND
    try:
        from underthesea import word_tokenize as _wt
        _UNDERTHESEA_TOKENIZE = _wt
        _BACKEND = "underthesea"
        return _BACKEND
    except Exception:
        pass
    try:
        from pyvi import ViTokenizer
        _PYVI_TOKENIZE = ViTokenizer.tokenize
        _BACKEND = "pyvi"
        return _BACKEND
    except Exception:
        pass
    _BACKEND = "naive"
    return _BACKEND


def backend() -> str:
    """Tên backend đang dùng: 'underthesea' | 'pyvi' | 'naive'."""
    return _resolve_backend()


def has_segmenter() -> bool:
    """True nếu có backend tách từ thật (underthesea/pyvi)."""
    return _resolve_backend() != "naive"


def segment(text: str) -> list:
    """Tách từ tiếng Việt -> list token. Từ ghép trả về dạng có khoảng trắng bên trong."""
    if not text:
        return []
    b = _resolve_backend()
    try:
        if b == "underthesea":
            return [t.strip() for t in _UNDERTHESEA_TOKENIZE(text) if t and t.strip()]
        if b == "pyvi":
            return _PYVI_TOKENIZE(text).split()
    except Exception:
        pass
    return text.split()


def segment_text(text: str) -> str:
    """Tách từ, nối các tiếng trong từ ghép bằng '_' (tương thích định dạng pyvi cũ)."""
    if not text:
        return text
    return " ".join(tok.replace(" ", "_") for tok in segment(text))
