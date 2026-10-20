#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO PIPELINE DATA INTEGRITY & AUDIT SUITE
Kiểm thử toàn diện 5 tầng dữ liệu giữa Hienho_MoMo-Base và hubs-momo (react-web-momo):
1. Local SSOT Integrity (inventory_clusters_summary.json)
2. Hubs Modular Chunks (188 files, index.json, quick-wins.json)
3. Internal Linking Topology (Valid targets, parent hubs, cross-bridges)
4. GEO Direct Answers & Knowledge Graph Quality
5. Content Plans & Central Hub Directory (INDEX.md)
"""

import os
import sys
import json
import glob

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HUBS_REPO = "/Users/hienhv/HienHv/Klaus/Web-Idea/react-web-momo"
SSOT_JSON = os.path.join(BASE_DIR, "07_REPORTS", "data", "inventory_clusters_summary.json")
MODULAR_DIR = os.path.join(HUBS_REPO, "data", "seo-clusters")
CONTENT_PLANS_DIR = os.path.join(BASE_DIR, "06_USE_CASE_MOMO", "content-plans")

class PipelineValidator:
    def __init__(self):
        self.passes = 0
        self.fails = 0
        self.warnings = 0
        self.report = []

    def log(self, status: str, check_name: str, message: str):
        if status == "PASS":
            self.passes += 1
            icon = "[PASS]"
        elif status == "FAIL":
            self.fails += 1
            icon = "[FAIL]"
        else:
            self.warnings += 1
            icon = "[WARN]"
        self.report.append(f"{icon} {check_name}: {message}")
        print(f"{icon} {check_name}: {message}")

    def run_all_checks(self):
        print("=== BẮT ĐẦU KIỂM THỬ TOÀN VẸN HỆ THỐNG SEO PIPELINE ===\n")

        # Tầng 1: Kiểm thử SSOT Master Data
        if not os.path.exists(SSOT_JSON):
            self.log("FAIL", "SSOT Existence", f"Không tìm thấy file SSOT tại {SSOT_JSON}")
            return
        
        with open(SSOT_JSON, 'r', encoding='utf-8') as f:
            ssot_data = json.load(f)

        usecases = ssot_data.get('usecases', [])
        stats = ssot_data.get('stats', {})
        total_uc = len(usecases)

        if total_uc >= 160:
            self.log("PASS", "SSOT Use Case Count", f"Phát hiện đầy đủ {total_uc} use cases trong SSOT.")
        else:
            self.log("FAIL", "SSOT Use Case Count", f"Số lượng use cases quá ít: {total_uc} (kỳ vọng >= 160).")

        if stats.get('total_keywords', 0) > 200000:
            self.log("PASS", "SSOT Keyword Volume", f"Tổng từ khóa đạt {stats['total_keywords']:,} từ khóa sạch.")
        else:
            self.log("FAIL", "SSOT Keyword Volume", f"Số từ khóa không đạt chuẩn: {stats.get('total_keywords', 0)}")

        # Tầng 2: Kiểm thử Modular Chunks bên hubs-momo
        if not os.path.exists(MODULAR_DIR):
            self.log("FAIL", "Hubs Modular Dir", f"Thư mục {MODULAR_DIR} không tồn tại.")
        else:
            index_path = os.path.join(MODULAR_DIR, "index.json")
            if os.path.exists(index_path):
                with open(index_path, 'r', encoding='utf-8') as f:
                    idx_data = json.load(f)
                idx_count = len(idx_data.get('usecases', []))
                idx_size_kb = os.path.getsize(index_path) / 1024
                if idx_count == total_uc:
                    self.log("PASS", "Hubs Index Count", f"index.json khớp chính xác {idx_count} use cases (Dung lượng: {idx_size_kb:.1f} KB).")
                else:
                    self.log("FAIL", "Hubs Index Count", f"index.json lệch số lượng: {idx_count} vs SSOT {total_uc}.")
            else:
                self.log("FAIL", "Hubs Index File", "Thiếu file index.json trong modular directory.")

            # Kiểm thử file quick-wins.json
            qw_path = os.path.join(MODULAR_DIR, "quick-wins.json")
            if os.path.exists(qw_path):
                with open(qw_path, 'r', encoding='utf-8') as f:
                    qw_data = json.load(f)
                qw_list = qw_data.get('quick_wins', [])
                if len(qw_list) > 0:
                    self.log("PASS", "Hubs Quick Wins", f"quick-wins.json chứa {len(qw_list)} từ khóa cơ hội cao.")
                else:
                    self.log("WARN", "Hubs Quick Wins", "quick-wins.json rỗng.")
            else:
                self.log("FAIL", "Hubs Quick Wins", "Thiếu file quick-wins.json.")

            # Kiểm tra tính toàn vẹn của 188 chunks
            chunk_files = glob.glob(os.path.join(MODULAR_DIR, "**", "*.json"), recursive=True)
            chunk_files = [c for c in chunk_files if not c.endswith("index.json") and not c.endswith("quick-wins.json")]
            
            missing_fields = 0
            empty_chunks = 0
            valid_chunks = 0

            for cf in chunk_files:
                try:
                    with open(cf, 'r', encoding='utf-8') as f:
                        cdata = json.load(f)
                    req_fields = ['id', 'name', 'sector', 'pillar_keyword', 'top_opportunities', 'internal_links', 'geo_optimization']
                    if all(rf in cdata for rf in req_fields):
                        valid_chunks += 1
                    else:
                        missing_fields += 1
                except Exception:
                    empty_chunks += 1

            if missing_fields == 0 and empty_chunks == 0 and valid_chunks >= 160:
                self.log("PASS", "Hubs Modular Chunks Integrity", f"100% chunks ({valid_chunks} files) có đầy đủ metadata, internal links và GEO schema.")
            else:
                self.log("FAIL", "Hubs Modular Chunks Integrity", f"Có {missing_fields} files thiếu trường, {empty_chunks} files lỗi.")

        # Tầng 3: Kiểm thử Mạng lưới liên kết nội bộ (Internal Linking Silo)
        broken_peers = 0
        all_ids = set(u['id'] for u in usecases)
        for uc in usecases:
            silo = uc.get('internal_links', {})
            peers = silo.get('peer_in_silo', [])
            for p in peers:
                if p['target_id'] not in all_ids:
                    broken_peers += 1
        if broken_peers == 0:
            self.log("PASS", "Internal Linking Topology", "Toàn bộ peer links đều trỏ đến target use case hợp lệ tồn tại trong hệ thống.")
        else:
            self.log("WARN", "Internal Linking Topology", f"Phát hiện {broken_peers} liên kết trỏ tới target_id không tồn tại.")

        # Tầng 4: Kiểm thử GEO & Direct Answers Quality
        invalid_geo = 0
        for uc in usecases:
            geo = uc.get('geo_optimization', {})
            snip = geo.get('direct_answer_snippet', '')
            facts = geo.get('entity_facts', [])
            if len(snip.split()) < 20 or len(facts) < 4:
                invalid_geo += 1
        if invalid_geo == 0:
            self.log("PASS", "GEO Quality & Factsheet", f"100% {total_uc} use cases có Direct Answer Snippet chuẩn SEO/GEO và Factsheet tối thiểu 4 thuộc tính.")
        else:
            self.log("WARN", "GEO Quality & Factsheet", f"Có {invalid_geo} use cases thiếu snippet hoặc factsheet.")

        # Tầng 5: Kiểm thử Thư mục Content Plans & INDEX.md
        index_md = os.path.join(CONTENT_PLANS_DIR, "INDEX.md")
        if os.path.exists(index_md):
            self.log("PASS", "Content Plans Index", f"Đã có tệp mục lục tập trung tại {index_md}")
        else:
            self.log("WARN", "Content Plans Index", "Chưa tìm thấy tệp mục lục INDEX.md tại 06_USE_CASE_MOMO/content-plans/")

        # Tầng 6: Kiểm thử MoMo Domain SERP & Sitemap Shield SSOT
        live_urls_json = os.path.join(BASE_DIR, "07_REPORTS", "data", "momo_live_urls.json")
        if os.path.exists(live_urls_json):
            with open(live_urls_json, 'r', encoding='utf-8') as f:
                urls_data = json.load(f)
            url_count = len(urls_data.get('urls', []))
            if url_count >= 1400:
                self.log("PASS", "MoMo Live URLs SSOT", f"Kho dữ liệu momo_live_urls.json chứa {url_count:,} URLs thực tế từ sitemap.")
            else:
                self.log("WARN", "MoMo Live URLs SSOT", f"Số lượng URLs momo thấp hơn dự kiến: {url_count}")
        else:
            self.log("FAIL", "MoMo Live URLs SSOT", "Không tìm thấy file momo_live_urls.json tại 07_REPORTS/data/")

        # Kiểm thử logic phân giải rủi ro tự ăn thịt từ khóa
        try:
            sys.path.append(os.path.join(BASE_DIR, "scripts", "lib"))
            from keyword_intelligence import MoMoDomainSERPShield
            r_exist = MoMoDomainSERPShield.evaluate_cannibalization_risk('tiết kiệm online', check_live_serp=False)
            r_new = MoMoDomainSERPShield.evaluate_cannibalization_risk('kinh nghiệm nuôi cá rồng', check_live_serp=False)
            if r_exist.get('action') in ['UPDATE_OR_REDIRECT', 'PROTECT_AND_LINK', 'INTERNAL_LINK_REALIGNMENT'] and r_new.get('action') == 'ALLOCATE_NEW':
                self.log("PASS", "Domain Cannibalization Shield", "Phân loại chuẩn xác: Chặn tạo mới với URL đã có ('tiết kiệm online') và Cấp phép với từ khóa sạch ('nuôi cá rồng').")
            else:
                self.log("FAIL", "Domain Cannibalization Shield", f"Logic nhận diện lỗi: {r_exist.get('action')} / {r_new.get('action')}")
        except Exception as e:
            self.log("FAIL", "Domain Cannibalization Shield", f"Lỗi khởi chạy module: {e}")

        # Tổng kết
        print("\n" + "="*55)
        print(f"KẾT QUẢ KIỂM THỬ: {self.passes} PASS | {self.warnings} WARN | {self.fails} FAIL")
        print("="*55)
        return self.fails == 0

if __name__ == '__main__':
    v = PipelineValidator()
    success = v.run_all_checks()
    sys.exit(0 if success else 1)
