# -*- coding: utf-8 -*-
"""Tạo component GA4EventsView.tsx và tích hợp vào FunnelMatrixView.tsx trên react-web-momo."""

ga4_events_view_code = """'use client';

import React, { useState, useMemo } from 'react';
import {
  Activity,
  AlertCircle,
  AlertTriangle,
  ArrowRight,
  ArrowUpRight,
  CheckCircle2,
  ChevronDown,
  ChevronRight,
  Database,
  ExternalLink,
  Filter,
  Flame,
  Globe,
  Layers,
  MousePointerClick,
  Search,
  ShieldAlert,
  ShieldCheck,
  TrendingUp,
  Zap,
} from 'lucide-react';
import { cn } from '@/lib/utils';
import ga4EventsData from '@/data/analytics/ga4-events-inventory.json';

interface GA4EventItem {
  event_name: string;
  category: string;
  description: string;
  audit_note: string;
  is_conversion: boolean;
  event_count: number;
  total_users: number;
  sessions: number;
  events_per_user: number;
  share_pct: number;
}

interface CategorySummary {
  category: string;
  total_volume: number;
  unique_events: number;
  share_pct: number;
}

interface CinemaStep {
  step: number;
  step_name: string;
  action: string;
  event_count: number;
  users: number;
  step_cr: number;
}

interface FinancialSimItem {
  product: string;
  tool_name: string;
  views: number;
  cta_clicks: number;
  cta_users: number;
  cr: number;
  evaluation: string;
}

interface MicroFunnelItem {
  hub: string;
  flow: string;
  completed_orders: number;
  notes: string;
}

interface AuditItem {
  severity: 'HIGH' | 'MEDIUM' | 'LOW';
  issue: string;
  affected_volume: string;
  impact: string;
  recommendation: string;
}

const fmt = (n: number) => new Intl.NumberFormat('vi-VN').format(Math.round(n || 0));
const pct = (n: number, d = 1) => `${((n || 0) * 100).toFixed(d)}%`;

export function GA4EventsView() {
  const [selectedCategory, setSelectedCategory] = useState<string>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [sortCol, setSortCol] = useState<keyof GA4EventItem>('event_count');
  const [sortAsc, setSortAsc] = useState<boolean>(false);
  const [showOnlyConversions, setShowOnlyConversions] = useState<boolean>(false);

  const rawData = ga4EventsData as unknown as {
    summary: {
      total_event_count: number;
      total_conversions: number;
      unique_events_tracked: number;
      conversion_events_count: number;
      categories_count: number;
    };
    period: { start: string; end: string };
    categories_summary: CategorySummary[];
    cinema_funnel: CinemaStep[];
    financial_simulations: FinancialSimItem[];
    vertical_micro_funnels: MicroFunnelItem[];
    data_quality_audit: AuditItem[];
    events: GA4EventItem[];
  };

  const summary = rawData.summary;
  const categories = rawData.categories_summary;
  const cinemaFunnel = rawData.cinema_funnel;
  const simulations = rawData.financial_simulations;
  const microFunnels = rawData.vertical_micro_funnels;
  const audits = rawData.data_quality_audit;
  const allEvents = rawData.events;

  // Filter & Sort
  const filteredEvents = useMemo(() => {
    let list = [...allEvents];

    if (selectedCategory !== 'ALL') {
      list = list.filter((e) => e.category === selectedCategory);
    }

    if (showOnlyConversions) {
      list = list.filter((e) => e.is_conversion);
    }

    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase().trim();
      list = list.filter(
        (e) =>
          e.event_name.toLowerCase().includes(q) ||
          e.category.toLowerCase().includes(q) ||
          e.description.toLowerCase().includes(q) ||
          e.audit_note.toLowerCase().includes(q)
      );
    }

    list.sort((a, b) => {
      let va = a[sortCol];
      let vb = b[sortCol];
      if (typeof va === 'string') {
        return sortAsc ? (va as string).localeCompare(vb as string) : (vb as string).localeCompare(va as string);
      }
      return sortAsc ? Number(va) - Number(vb) : Number(vb) - Number(va);
    });

    return list;
  }, [allEvents, selectedCategory, showOnlyConversions, searchQuery, sortCol, sortAsc]);

  const handleSort = (col: keyof GA4EventItem) => {
    if (sortCol === col) {
      setSortAsc(!sortAsc);
    } else {
      setSortCol(col);
      setSortAsc(false);
    }
  };

  return (
    <div className="flex flex-col gap-6 text-gray-900">
      {/* ── KPI HEADER CARDS ── */}
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        <div className="rounded-2xl border border-gray-200 bg-white p-4 shadow-xs">
          <div className="text-[11px] font-semibold uppercase tracking-wider text-gray-500">
            Tổng Lượt Sự Kiện (30D)
          </div>
          <div className="mt-1 text-2xl font-black text-gray-900 tabular-nums">
            {fmt(summary.total_event_count)}
          </div>
          <div className="mt-1 text-xs text-gray-500">
            Phân rã qua <strong>{summary.unique_events_tracked}</strong> loại sự kiện
          </div>
        </div>

        <div className="rounded-2xl border border-pink-200 bg-pink-50/40 p-4 shadow-xs">
          <div className="text-[11px] font-semibold uppercase tracking-wider text-[#A50064]">
            Lượt Chuyển Đổi (Conversions)
          </div>
          <div className="mt-1 text-2xl font-black text-[#A50064] tabular-nums">
            {fmt(summary.total_conversions)}
          </div>
          <div className="mt-1 text-xs text-pink-900/80">
            Chiếm <strong>{pct(summary.total_conversions / summary.total_event_count)}</strong> tổng sự kiện Web
          </div>
        </div>

        <div className="rounded-2xl border border-emerald-200 bg-emerald-50/40 p-4 shadow-xs">
          <div className="text-[11px] font-semibold uppercase tracking-wider text-emerald-700">
            Danh Mục Sự Kiện
          </div>
          <div className="mt-1 text-2xl font-black text-emerald-800 tabular-nums">
            {summary.categories_count} Phân Khối
          </div>
          <div className="mt-1 text-xs text-emerald-900/80">
            Lifecycle, CTA, Funnel, Ngành dọc
          </div>
        </div>

        <div className="rounded-2xl border border-amber-200 bg-amber-50/40 p-4 shadow-xs">
          <div className="text-[11px] font-semibold uppercase tracking-wider text-amber-800">
            Điểm Mù Dữ Liệu Cần Gắn
          </div>
          <div className="mt-1 text-2xl font-black text-amber-900 tabular-nums">
            2,560,075
          </div>
          <div className="mt-1 text-xs text-amber-900/80">
            Lượt click_to_app bị <code>(not set)</code> URL
          </div>
        </div>
      </div>

      {/* ── HIGHLIGHT 1: PHỄU ĐIỆN ẢNH VÀ CÔNG CỤ TÀI CHÍNH ── */}
      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        {/* Card 1: Phễu Điện Ảnh */}
        <div className="flex flex-col gap-3 rounded-2xl border border-gray-200 bg-white p-5 shadow-xs">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-[#A50064]" />
              <h3 className="text-sm font-bold text-gray-900">
                Phễu Chuyển Đổi Điện Ảnh 4 Bước (Cinema Funnel)
              </h3>
            </div>
            <span className="rounded-full bg-pink-100 px-2.5 py-0.5 text-[11px] font-bold text-[#A50064]">
              CR Toàn Phễu: 20.7%
            </span>
          </div>
          <p className="text-xs text-gray-500">
            Đo lường hành trình đặt vé trực tiếp trên Web Cinema từ lúc xem suất chiếu đến khi lấy vé thành công.
          </p>

          <div className="flex flex-col gap-2 pt-1">
            {cinemaFunnel.map((st, idx) => (
              <div
                key={st.step_name}
                className="flex items-center justify-between rounded-xl border border-gray-100 bg-gray-50/70 p-2.5 text-xs"
              >
                <div className="flex items-center gap-2.5">
                  <span className="flex h-5 w-5 items-center justify-center rounded-full bg-white font-mono text-[10px] font-bold text-gray-600 shadow-2xs border border-gray-200">
                    {st.step}
                  </span>
                  <div>
                    <div className="font-bold text-gray-900">{st.step_name}</div>
                    <div className="text-[11px] text-gray-500">{st.action}</div>
                  </div>
                </div>

                <div className="text-right">
                  <div className="font-bold text-gray-900 tabular-nums">
                    {fmt(st.users)} users
                  </div>
                  <div className="text-[10px] font-semibold text-gray-500 tabular-nums">
                    {fmt(st.event_count)} lượt {idx > 0 && `(CR: ${pct(st.step_cr)})`}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Card 2: Interactive Simulation & Micro-Funnels */}
        <div className="flex flex-col gap-4">
          {/* Simulation Tools */}
          <div className="flex flex-col gap-3 rounded-2xl border border-gray-200 bg-white p-5 shadow-xs">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <div className="h-2 w-2 rounded-full bg-emerald-500" />
                <h3 className="text-sm font-bold text-gray-900">
                  Hiệu Suất Công Cụ Tính & Mô Phỏng Tài Chính
                </h3>
              </div>
              <span className="rounded-full bg-emerald-100 px-2.5 py-0.5 text-[11px] font-bold text-emerald-800">
                High Intent Hub
              </span>
            </div>

            <div className="grid grid-cols-1 gap-2 pt-1">
              {simulations.map((sim) => (
                <div
                  key={sim.tool_name}
                  className="flex items-center justify-between rounded-xl border border-gray-100 bg-gray-50/70 p-2.5 text-xs"
                >
                  <div>
                    <div className="font-bold text-gray-900">{sim.product}</div>
                    <div className="font-mono text-[11px] text-gray-500">{sim.tool_name}</div>
                    <div className="mt-0.5 text-[10px] text-gray-500">{sim.evaluation}</div>
                  </div>

                  <div className="text-right">
                    <div className="text-sm font-black text-emerald-700 tabular-nums">
                      {pct(sim.cr)}
                    </div>
                    <div className="text-[11px] font-bold text-gray-900 tabular-nums">
                      {fmt(sim.cta_clicks)} clicks
                    </div>
                    <div className="text-[10px] text-gray-500 tabular-nums">
                      từ {fmt(sim.views)} lượt dùng
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Micro-Funnels Ngành Dọc */}
          <div className="rounded-2xl border border-gray-200 bg-white p-4 shadow-xs">
            <div className="text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
              Giao Dịch Hoàn Tất Trực Tiếp Trên Web (Micro-Funnels)
            </div>
            <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
              {microFunnels.map((mf) => (
                <div key={mf.hub} className="rounded-xl border border-gray-100 bg-gray-50/50 p-2.5 text-xs">
                  <div className="font-bold text-gray-900 truncate">{mf.hub}</div>
                  <div className="mt-1 text-base font-black text-gray-900 tabular-nums">
                    {fmt(mf.completed_orders)}
                  </div>
                  <div className="text-[10px] text-gray-500 leading-tight mt-0.5">
                    {mf.notes}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* ── HIGHLIGHT 2: DATA QUALITY AUDIT ALERTS ── */}
      <div className="rounded-2xl border border-amber-200 bg-amber-50/40 p-4">
        <div className="flex items-center gap-2 mb-3">
          <ShieldAlert className="h-4 w-4 text-amber-700" />
          <h4 className="text-xs font-bold uppercase tracking-wider text-amber-900">
            Cảnh Báo Chất Lượng Dữ Liệu & Điểm Mù Cần Chuẩn Hóa Tracking
          </h4>
        </div>
        <div className="grid grid-cols-1 gap-2.5 md:grid-cols-3 text-xs">
          {audits.map((item, idx) => (
            <div key={idx} className="rounded-xl border border-amber-200/80 bg-white p-3 shadow-2xs">
              <div className="flex items-center justify-between mb-1">
                <span className="font-bold text-gray-900">{item.issue}</span>
                <span className={cn(
                  'px-1.5 py-0.5 rounded text-[10px] font-bold uppercase',
                  item.severity === 'HIGH' ? 'bg-red-100 text-red-700' : 'bg-amber-100 text-amber-800'
                )}>
                  {item.severity}
                </span>
              </div>
              <div className="text-[11px] font-semibold text-red-600 mb-1">
                Ảnh hưởng: {item.affected_volume}
              </div>
              <p className="text-[11px] text-gray-600 mb-2 leading-relaxed">
                {item.impact}
              </p>
              <div className="rounded-md bg-gray-50 p-1.5 font-mono text-[10px] text-gray-700 border border-gray-100">
                Khuyến nghị: {item.recommendation}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* ── BẢNG CHI TIẾT 123 SỰ KIỆN GA4 ── */}
      <div className="flex flex-col gap-3">
        {/* Filters Bar */}
        <div className="flex flex-wrap items-center justify-between gap-3">
          {/* Category Filter Pills */}
          <div className="flex flex-wrap items-center gap-1.5">
            <button
              type="button"
              onClick={() => setSelectedCategory('ALL')}
              className={cn(
                'rounded-xl px-3 py-1.5 text-xs font-bold transition-all cursor-pointer',
                selectedCategory === 'ALL'
                  ? 'bg-gray-900 text-white shadow-2xs'
                  : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
              )}
            >
              Tất Cả ({allEvents.length})
            </button>
            {categories.map((c) => (
              <button
                key={c.category}
                type="button"
                onClick={() => setSelectedCategory(c.category)}
                className={cn(
                  'rounded-xl px-3 py-1.5 text-xs font-bold transition-all cursor-pointer',
                  selectedCategory === c.category
                    ? 'bg-gray-900 text-white shadow-2xs'
                    : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
                )}
              >
                {c.category} ({c.unique_events})
              </button>
            ))}
          </div>

          {/* Toggle Conversions & Search */}
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={() => setShowOnlyConversions(!showOnlyConversions)}
              className={cn(
                'rounded-xl px-3 py-1.5 text-xs font-bold transition-all border cursor-pointer',
                showOnlyConversions
                  ? 'bg-pink-50 border-[#A50064] text-[#A50064]'
                  : 'bg-white border-gray-200 text-gray-600 hover:bg-gray-50'
              )}
            >
              Chỉ Chuyển Đổi ({summary.conversion_events_count})
            </button>

            <div className="relative min-w-[220px]">
              <Search className="absolute left-3 top-1/2 h-3.5 w-3.5 -translate-y-1/2 text-gray-400" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Tìm tên sự kiện, ghi chú..."
                className="w-full rounded-xl border border-gray-200 bg-white py-1.5 pl-8 pr-3 text-xs text-gray-800 placeholder-gray-400 shadow-2xs focus:border-[#A50064] focus:outline-hidden"
              />
            </div>
          </div>
        </div>

        {/* Events Table */}
        <div className="overflow-x-auto rounded-2xl border border-gray-200 bg-white shadow-xs">
          <table className="w-full text-left text-xs text-gray-600">
            <thead className="border-b border-gray-200 bg-gray-50/80 text-[11px] font-bold uppercase tracking-wider text-gray-500">
              <tr>
                <th
                  onClick={() => handleSort('event_name')}
                  className="px-5 py-3.5 cursor-pointer hover:text-gray-900"
                >
                  Tên Sự Kiện GA4 {sortCol === 'event_name' && (sortAsc ? '↑' : '↓')}
                </th>
                <th
                  onClick={() => handleSort('category')}
                  className="px-3 py-3.5 cursor-pointer hover:text-gray-900"
                >
                  Phân Loại
                </th>
                <th
                  onClick={() => handleSort('event_count')}
                  className="px-3 py-3.5 text-right cursor-pointer hover:text-gray-900"
                >
                  Lượt Events (% Tổng) {sortCol === 'event_count' && (sortAsc ? '↑' : '↓')}
                </th>
                <th
                  onClick={() => handleSort('total_users')}
                  className="px-3 py-3.5 text-right cursor-pointer hover:text-gray-900"
                >
                  Người Dùng (Users) {sortCol === 'total_users' && (sortAsc ? '↑' : '↓')}
                </th>
                <th
                  onClick={() => handleSort('sessions')}
                  className="px-3 py-3.5 text-right cursor-pointer hover:text-gray-900"
                >
                  Phiên (Sessions) {sortCol === 'sessions' && (sortAsc ? '↑' : '↓')}
                </th>
                <th
                  onClick={() => handleSort('events_per_user')}
                  className="px-3 py-3.5 text-right cursor-pointer hover:text-gray-900"
                >
                  TB/User {sortCol === 'events_per_user' && (sortAsc ? '↑' : '↓')}
                </th>
                <th className="px-3 py-3.5 text-center">
                  Trạng Thái
                </th>
                <th className="px-4 py-3.5">
                  Ý Nghĩa & Ghi Chú Đánh Giá
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {filteredEvents.map((ev) => (
                <tr key={ev.event_name} className="hover:bg-gray-50/60 transition-colors">
                  <td className="px-5 py-3 font-mono font-bold text-gray-900">
                    {ev.event_name}
                  </td>

                  <td className="px-3 py-3">
                    <span className="inline-flex items-center rounded-md bg-gray-100 px-2 py-0.5 text-[11px] font-semibold text-gray-700">
                      {ev.category}
                    </span>
                  </td>

                  <td className="px-3 py-3 text-right tabular-nums">
                    <div className="font-bold text-gray-900">{fmt(ev.event_count)}</div>
                    <div className="text-[10px] text-gray-400">{pct(ev.share_pct, 2)}</div>
                  </td>

                  <td className="px-3 py-3 text-right font-medium tabular-nums text-gray-700">
                    {fmt(ev.total_users)}
                  </td>

                  <td className="px-3 py-3 text-right tabular-nums text-gray-600">
                    {fmt(ev.sessions)}
                  </td>

                  <td className="px-3 py-3 text-right font-mono text-[11px] tabular-nums text-gray-600">
                    {ev.events_per_user.toFixed(2)}
                  </td>

                  <td className="px-3 py-3 text-center">
                    {ev.is_conversion ? (
                      <span className="inline-flex items-center rounded-full bg-pink-100 px-2 py-0.5 text-[10px] font-bold text-[#A50064]">
                        Conversion
                      </span>
                    ) : (
                      <span className="text-[10px] text-gray-400">Standard</span>
                    )}
                  </td>

                  <td className="px-4 py-3 text-xs">
                    <div className="font-medium text-gray-800">{ev.description}</div>
                    <div className="text-[11px] text-gray-500">{ev.audit_note}</div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default GA4EventsView;
"""

target_view = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/components/content-plan/GA4EventsView.tsx"
with open(target_view, "w", encoding="utf-8") as f:
    f.write(ga4_events_view_code)

print("Đã ghi thành công GA4EventsView.tsx")

# Tích hợp vào FunnelMatrixView.tsx
fmv_path = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/components/content-plan/FunnelMatrixView.tsx"
with open(fmv_path, "r", encoding="utf-8") as f:
    fmv_code = f.read()

# 1. Thêm import GA4EventsView nếu chưa có
if "import GA4EventsView from './GA4EventsView';" not in fmv_code:
    fmv_code = fmv_code.replace(
        "import { cn } from '@/lib/utils';",
        "import { cn } from '@/lib/utils';\nimport GA4EventsView from './GA4EventsView';"
    )

# 2. Cập nhật activeTab type
fmv_code = fmv_code.replace(
    "const [activeTab, setActiveTab] = useState<'projects' | 'channels' | 'matrix' | 'pages' | 'quickwins' | 'cannibal'>('projects');",
    "const [activeTab, setActiveTab] = useState<'projects' | 'channels' | 'matrix' | 'pages' | 'quickwins' | 'cannibal' | 'events'>('projects');"
)

# 3. Thêm nút Tab 6 trong thanh tabs
tab_button = """          {/* Tab 6: Kho Sự Kiện GA4 */}
          <button
            type="button"
            onClick={() => setActiveTab('events')}
            className={cn(
              'inline-flex items-center gap-1.5 rounded-xl px-4 py-2 text-xs font-bold transition-all cursor-pointer',
              activeTab === 'events'
                ? 'bg-[#1C171A] text-white shadow-sm'
                : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
            )}
          >
            <Activity className="h-3.5 w-3.5 text-pink-500" />
            6. Sự Kiện GA4 (123)
          </button>
        </div>"""

if "onClick={() => setActiveTab('events')}" not in fmv_code:
    fmv_code = fmv_code.replace(
        "          {/* Tab 5: Quick Wins SEO */}",
        tab_button + "\n\n          {/* Tab 5: Quick Wins SEO */}"
    )

# 4. Thêm render block cho activeTab === 'events'
render_block = """      {/* ── GÓC NHÌN 6: KHO SỰ KIỆN GA4 INVENTORY & PHỄU CHUYỂN ĐỔI ── */}
      {activeTab === 'events' && (
        <GA4EventsView />
      )}

      {/* ── GÓC NHÌN 5: QUICK WINS SEO (STRIKE ZONE) ── */}"""

if "{activeTab === 'events' && (" not in fmv_code:
    fmv_code = fmv_code.replace(
        "      {/* ── GÓC NHÌN 5: QUICK WINS SEO (STRIKE ZONE) ── */}",
        render_block
    )

with open(fmv_path, "w", encoding="utf-8") as f:
    f.write(fmv_code)

print("Đã tích hợp thành công tab 'events' vào FunnelMatrixView.tsx")
