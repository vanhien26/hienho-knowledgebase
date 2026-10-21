#!/usr/bin/env python3
"""
Patch UI components in react-web-momo to handle blueprint === null and remove deprecated CTA/tracking fields:
1. components/content-plan/GeoEntityGapCard.tsx
2. components/geo/DirectAnswerHero.tsx
3. components/content-plan/GeoEntityOverview.tsx
"""

from pathlib import Path

BASE_DIR = Path('/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo')

GEO_ENTITY_GAP_CARD = r'''import React, { useState } from 'react';
import {
  Bot,
  Copy,
  Check,
  Code2,
  ShieldCheck,
  FileQuestion,
  Coins,
  Sparkles,
  ChevronDown,
  ChevronUp,
} from 'lucide-react';
import { getGeoEntityBlueprint } from '@/lib/content-plan/geo-entity-registry';

interface Props {
  themeId: string;
  themeName: string;
  sector?: string;
}

export function GeoEntityGapCard({ themeId, themeName, sector }: Props) {
  const [copiedJson, setCopiedJson] = useState(false);
  const [copiedAnswer, setCopiedAnswer] = useState(false);
  const [copiedBlueprint, setCopiedBlueprint] = useState(false);
  const [showJsonDetail, setShowJsonDetail] = useState(false);

  const blueprint = getGeoEntityBlueprint(themeId, themeName, sector);

  if (!blueprint) {
    return (
      <div className="rounded-2xl border border-dashed border-gray-300 bg-gray-50/50 p-6 text-center">
        <div className="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-100 text-gray-400 mb-2">
          <Bot size={20} />
        </div>
        <h4 className="text-sm font-bold text-gray-700">Chưa có blueprint</h4>
        <p className="text-xs text-gray-500 mt-1 max-w-md mx-auto">
          Theme &ldquo;{themeName}&rdquo; chưa được gán GEO Entity Blueprint chuẩn hóa. Nội dung YMYL tài chính yêu cầu dữ liệu chính xác từ văn bản pháp quy, không dùng nội dung mẫu chung.
        </p>
      </div>
    );
  }

  const handleCopyJson = () => {
    navigator.clipboard.writeText(JSON.stringify(blueprint.sample_jsonld, null, 2));
    setCopiedJson(true);
    setTimeout(() => setCopiedJson(false), 2000);
  };

  const handleCopyAnswer = () => {
    navigator.clipboard.writeText(blueprint.direct_answer_text);
    setCopiedAnswer(true);
    setTimeout(() => setCopiedAnswer(false), 2000);
  };

  const handleCopyBlueprint = () => {
    const text = `# BẢN THIẾT KẾ NỘI DUNG CHUẨN E-E-A-T & GEO: ${blueprint.theme.toUpperCase()}

## 1. Structured Data Schema: ${blueprint.schema_type}
${JSON.stringify(blueprint.sample_jsonld, null, 2)}

## 2. Đoạn trích Direct Answer (AI Answer Box):
"${blueprint.direct_answer_text}"

## 3. Lỗ hổng thực thể cần lấp đầy:
- ${blueprint.pillars.expertise.title}: ${blueprint.pillars.expertise.summary}
- ${blueprint.pillars.trust.title}: ${blueprint.pillars.trust.summary}
- ${blueprint.pillars.high_intent.title}: ${blueprint.pillars.high_intent.summary}

## 4. Căn cứ & Nguồn quy chuẩn:
${blueprint.sources.map((s) => `- ${s}`).join('\n')}
`;
    navigator.clipboard.writeText(text);
    setCopiedBlueprint(true);
    setTimeout(() => setCopiedBlueprint(false), 2000);
  };

  return (
    <div className="rounded-2xl border border-pink-200 bg-linear-to-b from-white via-pink-50/20 to-white p-5 sm:p-6 shadow-xs flex flex-col gap-5">
      {/* ── Top Bar: Tên tính năng & Schema Type ── */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-pink-100">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-xl bg-pink-100 text-[#D82D8B] flex items-center justify-center shrink-0">
            <Bot size={18} />
          </div>
          <div>
            <h3 className="text-base font-black text-[#1C171A] tracking-tight">
              Tối Ưu Hóa AI Search & Lỗ Hổng Thực Thể (GEO & Entity Gaps)
            </h3>
            <p className="text-xs text-gray-500 mt-0.5">
              Chuẩn hóa dữ liệu cho Google AI Overviews, Perplexity & Bing Copilot
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2 flex-wrap">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-pink-50 text-[#D82D8B] border border-pink-200 font-bold text-xs">
            <Code2 size={13} />
            <span>Schema: {blueprint.schema_type}</span>
          </span>
          <button
            type="button"
            onClick={handleCopyBlueprint}
            className="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-gray-900 hover:bg-black text-white font-bold text-xs transition-colors cursor-pointer"
          >
            {copiedBlueprint ? <Check size={13} /> : <Sparkles size={13} />}
            <span>{copiedBlueprint ? 'Đã sao chép Blueprint!' : 'Sao chép Blueprint E-E-A-T'}</span>
          </button>
        </div>
      </div>

      {/* ── 1. Đoạn Trích Trả Lời Trực Tiếp (AI Answer Box) ── */}
      <div className="flex flex-col gap-2">
        <div className="flex items-center justify-between">
          <label className="text-xs font-bold text-gray-700 uppercase tracking-wider flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-[#D82D8B]"></span>
            Đoạn Trích Trả Lời Trực Tiếp (AI Answer Box / Zero-Click Hook)
          </label>
          <div className="flex items-center gap-2">
            <span className="text-[11px] text-gray-400 font-semibold">
              {blueprint.word_count} từ • Chuẩn Inverted Pyramid
            </span>
            <button
              type="button"
              onClick={handleCopyAnswer}
              className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md text-xs font-bold text-gray-600 hover:text-[#D82D8B] hover:bg-pink-50 transition-colors cursor-pointer"
            >
              {copiedAnswer ? <Check size={12} className="text-emerald-600" /> : <Copy size={12} />}
              <span>{copiedAnswer ? 'Đã chép' : 'Chép đoạn trích'}</span>
            </button>
          </div>
        </div>

        <div className="p-4 rounded-xl border border-pink-200 bg-white shadow-2xs relative">
          <p className="text-sm font-medium text-[#1C171A] leading-relaxed italic">
            &ldquo;{blueprint.direct_answer_text}&rdquo;
          </p>
        </div>
      </div>

      {/* ── 2. Lỗ Hổng Thực Thể (Entity Gaps) ── */}
      <div className="flex flex-col gap-2.5">
        <label className="text-xs font-bold text-gray-700 uppercase tracking-wider flex items-center gap-1.5">
          <span className="w-2 h-2 rounded-full bg-amber-500"></span>
          3 Lỗ Hổng Thực Thể Đối Thủ Bỏ Sót (Information Gain)
        </label>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
          {/* Pillar 1: Expertise */}
          <div className="rounded-xl border border-blue-200 bg-blue-50/30 p-3.5 flex flex-col gap-2">
            <div className="flex items-center gap-2 text-blue-700">
              <FileQuestion size={16} className="shrink-0" />
              <h4 className="text-xs font-bold uppercase tracking-wide">
                1. {blueprint.pillars.expertise.title}
              </h4>
            </div>
            <p className="text-xs text-gray-700 leading-relaxed">
              {blueprint.pillars.expertise.detail}
            </p>
            <div className="mt-auto pt-2 border-t border-blue-100/80 text-[11px] font-semibold text-blue-900">
              Đề xuất: {blueprint.pillars.expertise.actionable_angle}
            </div>
          </div>

          {/* Pillar 2: Trust */}
          <div className="rounded-xl border border-emerald-200 bg-emerald-50/30 p-3.5 flex flex-col gap-2">
            <div className="flex items-center gap-2 text-emerald-700">
              <ShieldCheck size={16} className="shrink-0" />
              <h4 className="text-xs font-bold uppercase tracking-wide">
                2. {blueprint.pillars.trust.title}
              </h4>
            </div>
            <p className="text-xs text-gray-700 leading-relaxed">
              {blueprint.pillars.trust.detail}
            </p>
            <div className="mt-auto pt-2 border-t border-emerald-100/80 text-[11px] font-semibold text-emerald-900">
              Đề xuất: {blueprint.pillars.trust.actionable_angle}
            </div>
          </div>

          {/* Pillar 3: High-Intent */}
          <div className="rounded-xl border border-amber-200 bg-amber-50/30 p-3.5 flex flex-col gap-2">
            <div className="flex items-center gap-2 text-amber-700">
              <Coins size={16} className="shrink-0" />
              <h4 className="text-xs font-bold uppercase tracking-wide">
                3. {blueprint.pillars.high_intent.title}
              </h4>
            </div>
            <p className="text-xs text-gray-700 leading-relaxed">
              {blueprint.pillars.high_intent.detail}
            </p>
            <div className="mt-auto pt-2 border-t border-amber-100/80 text-[11px] font-semibold text-amber-900">
              Đề xuất: {blueprint.pillars.high_intent.actionable_angle}
            </div>
          </div>
        </div>
      </div>

      {/* ── 3. Schema JSON-LD ── */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 pt-2">
        <button
          type="button"
          onClick={() => setShowJsonDetail(!showJsonDetail)}
          className="inline-flex items-center gap-1.5 text-xs font-bold text-gray-600 hover:text-[#D82D8B] transition-colors cursor-pointer"
        >
          <Code2 size={14} />
          <span>{showJsonDetail ? 'Thu gọn mã JSON-LD' : 'Xem mã Schema JSON-LD'}</span>
          {showJsonDetail ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
        </button>
      </div>

      {/* ── Block JSON-LD (Mở rộng) ── */}
      {showJsonDetail && (
        <div className="rounded-xl border border-gray-200 bg-gray-900 text-gray-100 p-4 font-mono text-xs overflow-x-auto relative flex flex-col gap-2">
          <div className="flex items-center justify-between pb-2 border-b border-gray-800">
            <span className="text-gray-400 font-bold">Mã Schema JSON-LD (Nhúng vào thẻ &lt;head&gt;)</span>
            <button
              type="button"
              onClick={handleCopyJson}
              className="inline-flex items-center gap-1 px-2 py-1 rounded bg-gray-800 hover:bg-gray-700 text-gray-200 text-[11px] font-sans font-bold cursor-pointer"
            >
              {copiedJson ? <Check size={12} className="text-emerald-400" /> : <Copy size={12} />}
              <span>{copiedJson ? 'Đã sao chép' : 'Sao chép JSON'}</span>
            </button>
          </div>
          <pre className="text-emerald-400">
            {JSON.stringify(blueprint.sample_jsonld, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
'''

DIRECT_ANSWER_HERO = r'''import React from 'react';
import { Bot, ShieldCheck, CheckCircle2 } from 'lucide-react';
import { getGeoEntityBlueprint } from '@/lib/content-plan/geo-entity-registry';

interface Props {
  themeId: string;
  themeName: string;
  sector?: string;
  className?: string;
}

/**
 * Component chuẩn GEO & AI Search tối ưu cho các trang Web Hubs:
 * 1. Tự động inject thẻ <script type="application/ld+json"> chứa Schema chuẩn.
 * 2. Render Hero Direct Answer Box (40-60 từ) chuẩn Inverted Pyramid cho Google AI Overviews.
 * 3. Render khối dữ liệu thực thể giải quyết 3 điểm mù (Information Gain) cho trang.
 */
export function DirectAnswerHero({ themeId, themeName, sector, className = '' }: Props) {
  const blueprint = getGeoEntityBlueprint(themeId, themeName, sector);

  if (!blueprint) {
    return null;
  }

  return (
    <section className={`w-full max-w-[1240px] mx-auto px-4 sm:px-6 my-6 ${className}`}>
      {/* ── JSON-LD Structured Data Schema cho AI Search Engine ── */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(blueprint.sample_jsonld) }}
      />

      <div className="rounded-2xl border border-pink-200/80 bg-linear-to-b from-white via-pink-50/15 to-white p-5 sm:p-7 shadow-xs">
        {/* Header tag */}
        <div className="flex items-center gap-2 mb-3">
          <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-pink-100 text-[#D82D8B] font-bold text-xs tracking-wide">
            <Bot size={13} />
            <span>AI Answer Box • Định Nghĩa Nhanh</span>
          </span>
          <span className="text-xs text-gray-400 font-medium">
            Chuẩn E-E-A-T & Google AI Overviews
          </span>
        </div>

        {/* Hero Direct Answer Text */}
        <blockquote className="border-l-3 border-[#D82D8B] pl-4 sm:pl-5 py-1 mb-6">
          <p className="text-base sm:text-lg font-medium text-[#1C171A] leading-relaxed">
            {blueprint.direct_answer_text}
          </p>
        </blockquote>

        {/* 3 Trụ Cột Thực Thể Khác Biệt (Information Gain) */}
        <div className="pt-5 border-t border-gray-100">
          <div className="text-xs font-bold text-gray-500 uppercase tracking-wider mb-3">
            Thông tin kiểm chứng độc quyền từ Nền tảng Web MoMo
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
            <div className="rounded-xl border border-gray-100 bg-white p-3.5 shadow-2xs">
              <div className="flex items-center gap-1.5 text-xs font-bold text-gray-900 mb-1">
                <CheckCircle2 size={14} className="text-[#D82D8B] shrink-0" />
                <span>{blueprint.pillars.expertise.title}</span>
              </div>
              <p className="text-xs text-gray-600 leading-relaxed">
                {blueprint.pillars.expertise.summary}
              </p>
            </div>

            <div className="rounded-xl border border-gray-100 bg-white p-3.5 shadow-2xs">
              <div className="flex items-center gap-1.5 text-xs font-bold text-gray-900 mb-1">
                <ShieldCheck size={14} className="text-emerald-600 shrink-0" />
                <span>{blueprint.pillars.trust.title}</span>
              </div>
              <p className="text-xs text-gray-600 leading-relaxed">
                {blueprint.pillars.trust.summary}
              </p>
            </div>

            <div className="rounded-xl border border-gray-100 bg-white p-3.5 shadow-2xs">
              <div className="flex items-center gap-1.5 text-xs font-bold text-gray-900 mb-1">
                <CheckCircle2 size={14} className="text-amber-600 shrink-0" />
                <span>{blueprint.pillars.high_intent.title}</span>
              </div>
              <p className="text-xs text-gray-600 leading-relaxed">
                {blueprint.pillars.high_intent.summary}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
'''

def patch_geo_entity_overview():
    p = BASE_DIR / 'components/content-plan/GeoEntityOverview.tsx'
    text = p.read_text(encoding='utf-8')
    # Add Bot to lucide-react import if missing
    if 'Bot,' not in text and 'Bot ' not in text:
        text = text.replace('import {\n  Search,', 'import {\n  Bot,\n  Search,')
    # Check if empty blueprint handling exists
    if '{selected && detail && !blueprint && (' not in text:
        marker = '{selected && detail && blueprint && ('
        null_block = '''{selected && detail && !blueprint && (
        <div className="rounded-2xl border border-dashed border-gray-300 bg-white p-8 text-center flex flex-col items-center justify-center">
          <div className="w-12 h-12 rounded-full bg-gray-100 text-gray-400 flex items-center justify-center mb-3">
            <Bot size={24} />
          </div>
          <h4 className="text-base font-bold text-gray-800">Chưa có blueprint</h4>
          <p className="text-sm text-gray-500 mt-1 max-w-md">
            Theme &ldquo;{selected.display_name || selected.name}&rdquo; chưa được gán GEO Entity Blueprint chuẩn hóa. Nội dung YMYL tài chính yêu cầu dữ liệu chính xác từ văn bản pháp quy, không dùng nội dung mẫu chung.
          </p>
        </div>
      )}

      '''
        if marker in text:
            text = text.replace(marker, null_block + marker)
    p.write_text(text, encoding='utf-8')
    print('Patched GeoEntityOverview.tsx with Bot import')

def main():
    (BASE_DIR / 'components/content-plan/GeoEntityGapCard.tsx').write_text(GEO_ENTITY_GAP_CARD, encoding='utf-8')
    print('Wrote GeoEntityGapCard.tsx')
    (BASE_DIR / 'components/geo/DirectAnswerHero.tsx').write_text(DIRECT_ANSWER_HERO, encoding='utf-8')
    print('Wrote DirectAnswerHero.tsx')
    patch_geo_entity_overview()

if __name__ == '__main__':
    main()
