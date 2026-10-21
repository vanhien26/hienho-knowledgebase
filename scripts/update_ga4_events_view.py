# -*- coding: utf-8 -*-
"""Cập nhật GA4EventsView.tsx với tính năng Bóc tách chuyển đổi Web-to-App (Đã hồi tố 100% từ URL)."""

import json

new_component_code = """'use client';

import React, { useState, useMemo } from 'react';
import {
  Activity,
  AlertCircle,
  AlertTriangle,
  ArrowRight,
  ArrowUpRight,
  BarChart2,
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
import ga4W2AData from '@/data/analytics/ga4-w2a-attribution.json';

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
  status?: string;
  resolution?: string;
}

interface W2AProjectItem {
  project_name: string;
  sector: string;
  w2a_clicks: number;
  users: number;
  share_pct: number;
  top_landing_pages: { path: string; clicks: number }[];
}

const fmt = (n: number) => new Intl.NumberFormat('vi-VN').format(Math.round(n || 0));
const pct = (n: number, d = 1) => `${((n || 0) * 100).toFixed(d)}%`;

export function GA4EventsView() {
  const [subView, setSubView] = useState<'events' | 'w2a_attribution'>('w2a_attribution');
  const [selectedCategory, setSelectedCategory] = useState<string>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [sortCol, setSortCol] = useState<keyof GA4EventItem>('event_count');
  const [sortAsc, setSortAsc] = useState<boolean>(false);
  const [showOnlyConversions, setShowOnlyConversions] = useState<boolean>(false);

  // W2A Sorting
  const [w2aSortCol, setW2aSortCol] = useState<keyof W2AProjectItem>('w2a_clicks');
  const [w2aSortAsc, setW2aSortAsc] = useState<boolean>(false);

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

  const w2aRaw = ga4W2AData as unknown as {
    summary: {
      total_w2a_events_attributed: number;
      total_projects_count: number;
      top_project: string;
      top_project_share: number;
      attribution_method: string;
    };
    projects_attribution: W2AProjectItem[];
  };

  const summary = rawData.summary;
  const categories = rawData.categories_summary;
  const cinemaFunnel = rawData.cinema_funnel;
  const simulations = rawData.financial_simulations;
  const microFunnels = rawData.vertical_micro_funnels;
  const audits = rawData.data_quality_audit;
  const allEvents = rawData.events;
  const w2aProjects = w2aRaw.projects_attribution || [];

  // Filter & Sort Events
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

  // Filter & Sort W2A
  const filteredW2A = useMemo(() => {
    let list = [...w2aProjects];

    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase().trim();
      list = list.filter(
        (p) =>
          p.project_name.toLowerCase().includes(q) ||
          p.sector.toLowerCase().includes(q) ||
          p.top_landing_pages.some((t) => t.path.toLowerCase().includes(q))
      );
    }

    list.sort((a, b) => {
      let va = a[w2aSortCol];
      let vb = b[w2aSortCol];
      if (typeof va === 'string') {
        return w2aSortAsc ? (va as string).localeCompare(vb as string) : (vb as string).localeCompare(va as string);
      }
      return w2aSortAsc ? Number(va) - Number(vb) : Number(vb) - Number(va);
    });

    return list;
  }, [w2aProjects, searchQuery, w2aSortCol, w2aSortAsc]);

  const handleSort = (col: keyof GA4EventItem) => {
    if (sortCol === col) setSortAsc(!sortAsc);
    else {
      setSortCol(col);
      setSortAsc(false);
    }
  };

  const handleW2ASort = (col: keyof W2AProjectItem) => {
    if (w2aSortCol === col) setW2aSortAsc(!w2aSortAsc);
    else {
      setW2aSortCol(col);
      setW2aSortAsc(false);
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
            Định Nghĩa W2A Thành Công
          </div>
          <div className="mt-1 text-2xl font-black text-emerald-800 tabular-nums">
            {fmt(w2aRaw.summary.total_w2a_events_attributed)}
          </div>
          <div className="mt-1 text-xs text-emerald-900/80">
            Hồi tố <strong>100%</strong> vào <strong>{w2aRaw.summary.total_projects_count}</strong> Dự Án qua URL
          </div>
        </div>

        <div className="rounded-2xl border border-blue-200 bg-blue-50/40 p-4 shadow-xs">
          <div className="text-[11px] font-semibold uppercase tracking-wider text-blue-800">
            Dự Án Đóng Góp W2A Lớn Nhất
          </div>
          <div className="mt-1 text-2xl font-black text-blue-900 truncate">
            {w2aRaw.summary.top_project}
          </div>
          <div className="mt-1 text-xs text-blue-900/80">
            Chiếm <strong>{pct(w2aRaw.summary.top_project_share)}</strong> tổng chuyển đổi mở App toàn sàn
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

      {/* ── HIGHLIGHT 2: DATA QUALITY AUDIT & GIẢI PHÁP HỒI TỐ ── */}
      <div className="rounded-2xl border border-emerald-200 bg-emerald-50/30 p-4">
        <div className="flex items-center gap-2 mb-3">
          <ShieldCheck className="h-4 w-4 text-emerald-700" />
          <h4 className="text-xs font-bold uppercase tracking-wider text-emerald-900">
            Tình Trạng Dữ Liệu & Kết Quả Hồi Tố Điểm Mù (Data Attribution Status)
          </h4>
        </div>
        <div className="grid grid-cols-1 gap-2.5 md:grid-cols-3 text-xs">
          {audits.map((item, idx) => (
            <div
              key={idx}
              className={cn(
                'rounded-xl border bg-white p-3 shadow-2xs',
                item.status === 'RESOLVED_RETROSPECTIVELY'
                  ? 'border-emerald-200 ring-1 ring-emerald-100'
                  : 'border-amber-200'
              )}
            >
              <div className="flex items-center justify-between mb-1">
                <span className="font-bold text-gray-900">{item.issue}</span>
                {item.status === 'RESOLVED_RETROSPECTIVELY' ? (
                  <span className="px-1.5 py-0.5 rounded text-[10px] font-bold uppercase bg-emerald-100 text-emerald-800">
                    ĐÃ HỒI TỐ
                  </span>
                ) : (
                  <span className={cn(
                    'px-1.5 py-0.5 rounded text-[10px] font-bold uppercase',
                    item.severity === 'HIGH' ? 'bg-red-100 text-red-700' : 'bg-amber-100 text-amber-800'
                  )}>
                    {item.severity}
                  </span>
                )}
              </div>
              <div className="text-[11px] font-semibold text-emerald-700 mb-1">
                Số lượng: {item.affected_volume}
              </div>
              <p className="text-[11px] text-gray-600 mb-2 leading-relaxed">
                {item.resolution || item.impact}
              </p>
              <div className="rounded-md bg-gray-50 p-1.5 font-mono text-[10px] text-gray-700 border border-gray-100">
                Phương pháp: {item.recommendation}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* ── BỘ ĐIỀU HƯỚNG GÓC NHÌN CON (SUB-VIEWS TOGGLE) ── */}
      <div className="flex flex-col gap-3">
        <div className="flex flex-wrap items-center justify-between gap-3 border-b border-gray-200 pb-3">
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={() => setSubView('w2a_attribution')}
              className={cn(
                'inline-flex items-center gap-1.5 rounded-xl px-4 py-2 text-xs font-bold transition-all cursor-pointer',
                subView === 'w2a_attribution'
                  ? 'bg-[#1C171A] text-white shadow-sm'
                  : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
              )}
            >
              <BarChart2 className="h-3.5 w-3.5 text-emerald-400" />
              1. Bóc Tách Chuyển Đổi Web-to-App ({w2aProjects.length} Dự Án)
            </button>

            <button
              type="button"
              onClick={() => setSubView('events')}
              className={cn(
                'inline-flex items-center gap-1.5 rounded-xl px-4 py-2 text-xs font-bold transition-all cursor-pointer',
                subView === 'events'
                  ? 'bg-[#1C171A] text-white shadow-sm'
                  : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
              )}
            >
              <Layers className="h-3.5 w-3.5 text-pink-500" />
              2. Toàn Bộ Kho Sự Kiện ({allEvents.length} Events)
            </button>
          </div>

          {/* Search box chung */}
          <div className="relative min-w-[240px]">
            <Search className="absolute left-3 top-1/2 h-3.5 w-3.5 -translate-y-1/2 text-gray-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder={
                subView === 'w2a_attribution'
                  ? 'Tìm theo tên dự án, URL...'
                  : 'Tìm tên sự kiện, ghi chú...'
              }
              className="w-full rounded-xl border border-gray-200 bg-white py-1.5 pl-8 pr-3 text-xs text-gray-800 placeholder-gray-400 shadow-2xs focus:border-[#A50064] focus:outline-hidden"
            />
          </div>
        </div>

        {/* ── SUB-VIEW 1: BÓC TÁCH CHUYỂN ĐỔI WEB-TO-APP 51 DỰ ÁN ── */}
        {subView === 'w2a_attribution' && (
          <div className="flex flex-col gap-3">
            {/* Quick summary pills */}
            <div className="flex flex-wrap items-center gap-2">
              <span className="text-xs font-bold text-gray-500">Top Đóng Góp:</span>
              {w2aProjects.slice(0, 5).map((p) => (
                <span
                  key={p.project_name}
                  className="inline-flex items-center gap-1.5 rounded-lg border border-gray-200 bg-white px-2.5 py-1 text-xs font-semibold text-gray-800 shadow-2xs"
                >
                  <span className="font-bold">{p.project_name}:</span>
                  <span className="text-emerald-700 font-black">{fmt(p.w2a_clicks)}</span>
                  <span className="text-[10px] text-gray-400">({pct(p.share_pct)})</span>
                </span>
              ))}
            </div>

            {/* W2A Attribution Table */}
            <div className="overflow-x-auto rounded-2xl border border-gray-200 bg-white shadow-xs">
              <table className="w-full text-left text-xs text-gray-600">
                <thead className="border-b border-gray-200 bg-gray-50/80 text-[11px] font-bold uppercase tracking-wider text-gray-500">
                  <tr>
                    <th
                      onClick={() => handleW2ASort('project_name')}
                      className="px-5 py-3.5 cursor-pointer hover:text-gray-900"
                    >
                      Dự Án BigQuery {w2aSortCol === 'project_name' && (w2aSortAsc ? '↑' : '↓')}
                    </th>
                    <th
                      onClick={() => handleW2ASort('sector')}
                      className="px-3 py-3.5 cursor-pointer hover:text-gray-900"
                    >
                      Phân Khối (Hub)
                    </th>
                    <th
                      onClick={() => handleW2ASort('w2a_clicks')}
                      className="px-3 py-3.5 text-right cursor-pointer hover:text-gray-900"
                    >
                      Lượt Clicks Mở App (W2A) {w2aSortCol === 'w2a_clicks' && (w2aSortAsc ? '↑' : '↓')}
                    </th>
                    <th
                      onClick={() => handleW2ASort('users')}
                      className="px-3 py-3.5 text-right cursor-pointer hover:text-gray-900"
                    >
                      Người Dùng (Users) {w2aSortCol === 'users' && (w2aSortAsc ? '↑' : '↓')}
                    </th>
                    <th
                      onClick={() => handleW2ASort('share_pct')}
                      className="px-3 py-3.5 text-right cursor-pointer hover:text-gray-900"
                    >
                      Tỷ Trọng Toàn Sàn {w2aSortCol === 'share_pct' && (w2aSortAsc ? '↑' : '↓')}
                    </th>
                    <th className="px-5 py-3.5">
                      Top Trang Đích Mang Lại Chuyển Đổi (Top Landing Pages)
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-100">
                  {filteredW2A.map((p) => (
                    <tr key={p.project_name} className="hover:bg-emerald-50/20 transition-colors">
                      <td className="px-5 py-3 font-bold text-gray-900">
                        {p.project_name}
                      </td>

                      <td className="px-3 py-3">
                        <span className="inline-flex items-center rounded-md bg-gray-100 px-2 py-0.5 text-[11px] font-semibold text-gray-700">
                          {p.sector}
                        </span>
                      </td>

                      <td className="px-3 py-3 text-right tabular-nums">
                        <span className="font-black text-emerald-800">{fmt(p.w2a_clicks)}</span>
                      </td>

                      <td className="px-3 py-3 text-right font-medium tabular-nums text-gray-700">
                        {fmt(p.users)}
                      </td>

                      <td className="px-3 py-3 text-right font-bold tabular-nums text-[#A50064]">
                        {pct(p.share_pct)}
                      </td>

                      <td className="px-5 py-3 text-xs">
                        <div className="flex flex-col gap-1 max-w-lg">
                          {p.top_landing_pages.map((tlp, idx) => (
                            <div key={idx} className="flex items-center justify-between gap-2 text-[11px]">
                              <span className="font-mono text-gray-600 truncate max-w-sm">
                                {tlp.path}
                              </span>
                              <span className="font-bold text-gray-900 tabular-nums shrink-0">
                                {fmt(tlp.clicks)} clicks
                              </span>
                            </div>
                          ))}
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* ── SUB-VIEW 2: TOÀN BỘ KHO 123 SỰ KIỆN GA4 ── */}
        {subView === 'events' && (
          <div className="flex flex-col gap-3">
            {/* Category Filter Pills & Conversion Toggle */}
            <div className="flex flex-wrap items-center justify-between gap-3">
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
        )}
      </div>
    </div>
  );
}

export default GA4EventsView;
"""

target_view = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo/components/content-plan/GA4EventsView.tsx"
with open(target_view, "w", encoding="utf-8") as f:
    f.write(new_component_code)

print("Đã cập nhật thành công GA4EventsView.tsx với tính năng Bóc Tách Chuyển Đổi Web-to-App.")
