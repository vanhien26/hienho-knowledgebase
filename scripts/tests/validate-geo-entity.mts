import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Import THEME_ARCHETYPE from geo-entity-registry
let THEME_ARCHETYPE: Record<string, string> = {};
try {
  const regPath = path.resolve(__dirname, '../../Web-Idea/react-web-momo/lib/content-plan/geo-entity-registry.ts');
  const mod = await import(regPath);
  THEME_ARCHETYPE = mod.THEME_ARCHETYPE || {};
} catch {
  try {
    const localRegPath = path.resolve(__dirname, '../lib/content-plan/geo-entity-registry.ts');
    const mod = await import(localRegPath);
    THEME_ARCHETYPE = mod.THEME_ARCHETYPE || {};
  } catch (err) {
    console.warn('Could not load THEME_ARCHETYPE:', err);
  }
}

// Base directories
let clustersBaseDir = path.resolve(__dirname, '../../Web-Idea/react-web-momo/data/seo-clusters');
if (!fs.existsSync(clustersBaseDir)) {
  clustersBaseDir = path.resolve(__dirname, '../data/seo-clusters');
}

const sectors = fs.readdirSync(clustersBaseDir).filter(s => {
  const p = path.join(clustersBaseDir, s);
  return fs.statSync(p).isDirectory() && !s.startsWith('.');
});

// Stopwords set (hư từ tiếng Việt không được đứng cuối câu)
const STOP_WORDS = new Set([
  'và', 'của', 'giúp', 'tại', 'cho', 'với', 'theo', 'là', 'để', 'ở', 'do',
  'từ', 'vì', 'nên', 'mà', 'hay', 'hoặc', 'cũng', 'các', 'những', 'được',
  'bởi', 'về', 'trong', 'lên', 'xuống', 'ra', 'vào', 'thì', 'rằng', 'bằng',
  'minh', 'nhiều', 'như', 'nhưng', 'khi', 'qua', 'đến', 'gồm', 'thuộc',
  'một', 'có', 'lại', 'hãy', 'còn'
]);

// Classification definitions for intent verification
const NULL_THEMES = new Set(['ngan-hang', 'crypto', 'ma-giam-gia', 'chi-duong', 'metro', 'tuyen-xe-buyt']);
const CALCULATOR_THEMES = new Set(['tinh-luong', 'tinh-calo', 'bmi', 'lai-kep']);
const FUEL_THEMES = new Set(['gia-xang', 'gia-dau', 'tram-xang', 'gia-xe']);
const SAVINGS_THEMES = new Set(['gui-tiet-kiem', 'lai-suat', 'tich-luy', 'chung-chi-tien-gui']);
const LOAN_THEMES = new Set(['vay', 'vay-tin-chap', 'vay-the-chap']);
const PAYMENT_THEMES = new Set([
  'the-tin-dung', 'the-ghi-no', 'chuyen-khoan', 'thanh-toan-qr', 'vi-dien-tu',
  'vetc', 'epass', 'phi-khong-dung', 'phi-duong-bo', 'the-tra-truoc', 'the-visa',
  'master-card', 'napas', 'internet-banking'
]);
const FIN_PRODUCT_THEMES = new Set([
  'chung-khoan', 'co-phieu', 'trai-phieu', 'chung-chi-quy', 'quy-etf', 'phai-sinh',
  'gia-vang', 'bac', 'ty-gia', 'ngoai-te', 'doi-tien', 'kieu-hoi', 'vi-tra-sau',
  'tin-dung', 'du-no', 'thau-chi', 'diem-tin-dung', 'no-xau', 'ma-chung-khoan',
  'dau-tu', 'uy-thac', 'ky-quy'
]);
const GOV_THEMES = new Set([
  'phat-nguoi', 'loi-giao-thong', 'giay-phep-lai-xe', 'thi-bang-lai-xe', 'dang-kiem',
  'bien-so-xe', 'bien-so-dep', 'sang-ten-xe', 'thue-tncn', 'ma-so-thue',
  'giam-tru-gia-canh', 'thue', 'bhyt', 'bhxh', 'xo-so', 'vietlott', 've-so'
]);

// Danh sách các văn bản quy phạm pháp luật đã hết hiệu lực hoặc đã bị thay thế (SSOT check)
const REPLACED_DOCUMENTS = new Set([
  '100/2019', // Thay thế bởi Nghị định 168/2024/NĐ-CP (hiệu lực 01/01/2025)
  '123/2021', // Bị thay thế đối với các điều khoản xử phạt giao thông bởi Nghị định 168/2024/NĐ-CP
  '46/2016',  // Đã hết hiệu lực (thay thế bởi Nghị định 100/2019/NĐ-CP)
  '171/2013', // Đã hết hiệu lực
  '86/2014',  // Đã hết hiệu lực (thay thế bởi Nghị định 10/2020/NĐ-CP)
]);

// Helper to normalize gap title (stripping theme name and theme id)
function normalizeGapTitle(title: string, themeId: string, themeName: string): string {
  let t = title.toLowerCase();
  const tokens = new Set([
    ...themeName.toLowerCase().split(/\s+/),
    ...themeId.toLowerCase().split('-')
  ]);
  for (const token of tokens) {
    if (token.length > 2) {
      t = t.replaceAll(token, '');
    }
  }
  return t.replace(/[^\p{L}\p{N}\s]/gu, ' ').replace(/\s+/g, ' ').trim();
}

// ---------------------------------------------------------------------------
// Pre-scan Pass: Collect Sentences, Gap Titles, and Source URLs
// ---------------------------------------------------------------------------
const sentenceToTheme = new Map<string, string>();
const themesWithDuplicateSentences = new Map<string, string>();
const normGapTitleToThemes = new Map<string, Set<string>>();
const urlToThemes = new Map<string, Set<string>>();

interface ClusterRecord {
  filePath: string;
  data: any;
  themeId: string;
  themeName: string;
  sector: string;
}

const allClusters: ClusterRecord[] = [];

for (const sector of sectors.sort()) {
  const sectorDir = path.join(clustersBaseDir, sector);
  const files = fs.readdirSync(sectorDir).filter(f => f.endsWith('.json')).sort();
  for (const file of files) {
    const filePath = path.join(sectorDir, file);
    const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    const themeId = data.id || file.replace('.json', '');
    const themeName = data.display_name || data.name || themeId;
    allClusters.push({ filePath, data, themeId, themeName, sector });

    const geo = data.geo_optimization || {};
    const directAnswer = (geo.direct_answer_snippet || '').trim();

    // Check duplicate sentences
    if (directAnswer) {
      const sentences = directAnswer
        .split(/[.!?]+/)
        .map((s: string) => s.trim().toLowerCase())
        .filter((s: string) => s.length > 15);

      for (const s of sentences) {
        if (sentenceToTheme.has(s)) {
          const prevTheme = sentenceToTheme.get(s)!;
          if (prevTheme !== themeId) {
            themesWithDuplicateSentences.set(themeId, prevTheme);
          }
        } else {
          sentenceToTheme.set(s, themeId);
        }
      }
    }

    // Check gap titles
    const gaps = Array.isArray(geo.entity_gaps) ? geo.entity_gaps : [];
    for (const g of gaps) {
      const title = (g.title || '').trim();
      if (!title) continue;
      const norm = normalizeGapTitle(title, themeId, themeName);
      if (!normGapTitleToThemes.has(norm)) {
        normGapTitleToThemes.set(norm, new Set());
      }
      normGapTitleToThemes.get(norm)!.add(themeId);
    }

    // Check source URLs
    const sources = Array.isArray(geo.sources) ? geo.sources : [];
    for (const src of sources) {
      const url = (src.url || '').trim();
      if (!url) continue;
      if (!urlToThemes.has(url)) {
        urlToThemes.set(url, new Set());
      }
      urlToThemes.get(url)!.add(themeId);
    }
  }
}

// ---------------------------------------------------------------------------
// Asynchronous HTTP Status & Document Content Verification for Unique URLs
// ---------------------------------------------------------------------------
const uniqueUrls = Array.from(urlToThemes.keys());
const urlStatus = new Map<string, number | string>();
const urlContent = new Map<string, string>();
const urlTitle = new Map<string, string>();

console.log(`Kiểm tra trạng thái HTTP và nội dung trang cho ${uniqueUrls.length} URL nguồn duy nhất...`);

const CHUNK_SIZE = 10;
for (let i = 0; i < uniqueUrls.length; i += CHUNK_SIZE) {
  const chunk = uniqueUrls.slice(i, i + CHUNK_SIZE);
  await Promise.all(
    chunk.map(async (url) => {
      try {
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), 12000);
        try {
          const res = await fetch(url, {
            method: 'GET',
            headers: {
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            },
            signal: controller.signal
          });
          urlStatus.set(url, res.status);
          if (res.status === 200) {
            const html = await res.text();
            urlContent.set(url, html);
            const titleMatch = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
            if (titleMatch) {
              urlTitle.set(url, titleMatch[1].replace(/\s+/g, ' ').trim());
            }
          }
        } finally {
          clearTimeout(timeout);
        }
      } catch (err: any) {
        const isTimeout = err?.name === 'TimeoutError' || err?.name === 'AbortError';
        urlStatus.set(url, isTimeout ? 'TIMEOUT' : (err?.message || 'ERROR'));
      }
    })
  );
}

// ---------------------------------------------------------------------------
// Main Validation Loop
// ---------------------------------------------------------------------------
interface ValidationRow {
  themeId: string;
  archetype: string;
  blueprint_match: string;
  schema_type: string;
  factsCount: number;
  gapsCount: number;
  sourcesCount: number;
  last_verified: string;
  flag: string;
}

const rows: ValidationRow[] = [];
let exactCount = 0;
let sharedCount = 0;
let nullCount = 0;
let flagCount = 0;

for (const { data, themeId, themeName, sector } of allClusters) {
  const geo = data.geo_optimization || {};

  const blueprintMatch = geo.blueprint_match ?? null;
  const directAnswer = (geo.direct_answer_snippet || '').trim();
  const entityFacts = Array.isArray(geo.entity_facts) ? geo.entity_facts : [];
  const entityGaps = Array.isArray(geo.entity_gaps) ? geo.entity_gaps : [];
  const schema = geo.schema ?? null;
  const schemaType = schema?.type ?? null;
  const sources = Array.isArray(geo.sources) ? geo.sources : [];
  const lastVerified = geo.last_verified ?? '';

  const archetype = THEME_ARCHETYPE[themeId] ?? null;

  if (blueprintMatch === 'exact') exactCount++;
  else if (blueprintMatch === 'shared') sharedCount++;
  else if (blueprintMatch === null) nullCount++;

  const flags: string[] = [];

  // Rule 1: Theme financial mà không có source nào thuộc cơ quan quản lý hợp chuẩn -> FLAG
  if (sector === 'Financial') {
    const hasFinSource = sources.some((s: any) => {
      const url = (s.url || '').toLowerCase();
      const label = (s.label || '').toLowerCase();
      return (
        ['sbv', 'ssc', 'gdt', 'div', 'cic', 'chinhphu', 'vbpl', 'cvs', 'vietcombank', 'bidv', 'tpb'].some(k => url.includes(k)) ||
        ['ngân hàng nhà nước', 'chứng khoán', 'thuế', 'bảo hiểm tiền gửi', 'thông tin tín dụng', 'vietcombank', 'bidv', 'tpbank', 'tctd'].some(k => label.includes(k))
      );
    });
    if (!hasFinSource) {
      flags.push('FIN_SOURCE_MISSING');
    }
  }

  // Rule 2: entity_gaps.length !== 3 -> FLAG
  if (entityGaps.length !== 3) {
    flags.push(`GAPS_NOT_3(${entityGaps.length})`);
  }

  // Rule 3: Gap title (sau khi bỏ tên theme) trùng ở hơn 3 theme -> FLAG
  for (const g of entityGaps) {
    const title = (g.title || '').trim();
    if (!title) continue;
    const norm = normalizeGapTitle(title, themeId, themeName);
    const count = normGapTitleToThemes.get(norm)?.size || 0;
    if (count > 3) {
      flags.push(`GAP_TITLE_DUPLICATE(${count})`);
      break;
    }
  }

  // Rule 4: direct_answer_snippet word count < 40 hoặc > 60 -> FLAG
  const words = directAnswer.split(/\s+/).filter(Boolean);
  if (words.length < 40 || words.length > 60) {
    flags.push(`WC_OUT_OF_BOUNDS(${words.length})`);
  }

  // Rule 5: evidence_keywords dùng keyword không có trong theme.keywords -> FLAG
  const themeKws = new Set((data.keywords || []).map((k: any) => k.keyword));
  let missingKw = false;
  for (const g of entityGaps) {
    for (const ek of g.evidence_keywords || []) {
      if (!themeKws.has(ek)) {
        missingKw = true;
        break;
      }
    }
  }
  if (missingKw) {
    flags.push('EVIDENCE_KW_MISSING');
  }

  // Rule 6: schema.type không map đúng intent -> FLAG
  if (NULL_THEMES.has(themeId)) {
    if (schema !== null || schemaType !== null) {
      flags.push(`NULL_INTENT_MISMATCH(${schemaType})`);
    }
  } else if (CALCULATOR_THEMES.has(themeId)) {
    if (schemaType !== 'WebApplication') flags.push(`CALC_INTENT_MISMATCH(${schemaType})`);
  } else if (FUEL_THEMES.has(themeId)) {
    if (schemaType !== 'Dataset') flags.push(`FUEL_INTENT_MISMATCH(${schemaType})`);
  } else if (SAVINGS_THEMES.has(themeId)) {
    if (schemaType !== 'DepositAccount') flags.push(`SAVINGS_INTENT_MISMATCH(${schemaType})`);
  } else if (LOAN_THEMES.has(themeId)) {
    if (schemaType !== 'LoanOrCredit') flags.push(`LOAN_INTENT_MISMATCH(${schemaType})`);
  } else if (PAYMENT_THEMES.has(themeId)) {
    if (schemaType !== 'PaymentService') flags.push(`PAYMENT_INTENT_MISMATCH(${schemaType})`);
  } else if (FIN_PRODUCT_THEMES.has(themeId)) {
    if (schemaType !== 'FinancialProduct') flags.push(`FIN_PRODUCT_MISMATCH(${schemaType})`);
  } else if (themeId.startsWith('bao-hiem') || themeId === 'phi-bao-hiem') {
    if (schemaType !== 'InsuranceProduct') flags.push(`INSURANCE_MISMATCH(${schemaType})`);
  } else if (GOV_THEMES.has(themeId)) {
    if (schemaType !== 'GovernmentService') flags.push(`GOV_MISMATCH(${schemaType})`);
  } else if (sector === 'cinema') {
    if (schemaType !== 'MovieTheater') flags.push(`CINEMA_MISMATCH(${schemaType})`);
  } else if (sector === 'ota') {
    if (schemaType !== 'TravelAgency') flags.push(`OTA_MISMATCH(${schemaType})`);
  } else if (sector === 'telco') {
    if (schemaType !== 'Product') flags.push(`TELCO_MISMATCH(${schemaType})`);
  } else if (themeId === 'viec-lam-sinh-vien') {
    if (schemaType !== 'EmploymentAgency') flags.push(`STUDENT_JOBS_MISMATCH(${schemaType})`);
  } else if (sector === 'hospital') {
    if (schemaType !== 'MedicalOrganization') flags.push(`HOSPITAL_MISMATCH(${schemaType})`);
  } else if (sector === 'student') {
    if (schemaType !== 'EducationalOrganization') flags.push(`STUDENT_MISMATCH(${schemaType})`);
  }

  // Rule 7: đoạn trả lời kết thúc bằng hư từ hoặc chưa trọn vẹn câu -> FLAG
  if (!directAnswer.endsWith('.')) {
    flags.push('NOT_COMPLETE_SENTENCE');
  } else {
    const cleanSnippet = directAnswer.replace(/[.!?]+$/, '').trim();
    const lastWord = cleanSnippet.split(/\s+/).pop()?.toLowerCase() || '';
    if (STOP_WORDS.has(lastWord)) {
      flags.push(`END_WITH_STOPWORD(${lastWord})`);
    }
  }

  // Rule 8: đoạn trả lời trùng câu với đoạn của theme khác -> FLAG
  if (themesWithDuplicateSentences.has(themeId)) {
    flags.push(`DUPLICATE_SENTENCE(${themesWithDuplicateSentences.get(themeId)})`);
  }

  // Rule 9: Nguồn là link trang chủ (không có path và không có search param) -> FLAG
  for (const s of sources) {
    const urlStr = s.url || '';
    try {
      const u = new URL(urlStr);
      if ((!u.pathname || u.pathname === '' || u.pathname === '/') && !u.search) {
        flags.push(`HOMEPAGE_SOURCE(${u.hostname})`);
        break;
      }
    } catch {
      flags.push(`INVALID_URL(${urlStr})`);
      break;
    }
  }

  // Rule 10: URL nguồn trả về HTTP khác 200 -> FLAG
  for (const s of sources) {
    const urlStr = (s.url || '').trim();
    if (!urlStr) continue;
    const status = urlStatus.get(urlStr);
    if (status !== 200) {
      flags.push(`URL_HTTP_NOT_200(${status})`);
      break;
    }
  }

  // Rule 11: Một URL được dẫn ở hơn 30 theme -> FLAG
  for (const s of sources) {
    const urlStr = (s.url || '').trim();
    if (!urlStr) continue;
    const count = urlToThemes.get(urlStr)?.size || 0;
    if (count > 30) {
      flags.push(`URL_OVERUSED_30(${count})`);
      break;
    }
  }

  // Rule 12: Văn bản đã hết hiệu lực hoặc bị thay thế -> FLAG
  for (const s of sources) {
    const label = s.label || '';
    const urlStr = s.url || '';
    const docMatch = label.match(/\b(\d{1,4}\/\d{4})\b/);
    const docNum = docMatch ? docMatch[1] : null;

    if (docNum && REPLACED_DOCUMENTS.has(docNum)) {
      flags.push(`EXPIRED_OR_REPLACED_DOC(${docNum})`);
      break;
    }
    let repFound: string | null = null;
    for (const rep of REPLACED_DOCUMENTS) {
      if (label.includes(rep) || urlStr.includes(rep)) {
        repFound = rep;
        break;
      }
    }
    if (repFound) {
      flags.push(`EXPIRED_OR_REPLACED_DOC(${repFound})`);
      break;
    }
    const pageContent = urlContent.get(urlStr) || '';
    if (urlStr.includes('vanban.chinhphu.vn') && pageContent.includes('>Hết hiệu lực toàn bộ<')) {
      flags.push(`EXPIRED_OR_REPLACED_DOC(${docNum || 'chinhphu'})`);
      break;
    }
  }

  // Rule 13: Số hiệu văn bản ghi trong label không xuất hiện trong <title> hoặc nội dung trang -> FLAG
  for (const s of sources) {
    const label = s.label || '';
    const urlStr = s.url || '';
    const docMatch = label.match(/\b(\d{1,4}\/\d{4})\b/);
    if (docMatch) {
      const docNum = docMatch[1];
      const title = urlTitle.get(urlStr) || '';
      const pageContent = urlContent.get(urlStr) || '';
      const found = title.includes(docNum) || pageContent.includes(docNum);
      if (!found) {
        flags.push(`DOC_NUM_MISMATCH(${docNum})`);
        break;
      }
    }
  }

  const flagStr = flags.length > 0 ? flags.join(',') : 'OK';
  if (flagStr !== 'OK') flagCount++;

  rows.push({
    themeId,
    archetype: archetype ?? 'null',
    blueprint_match: blueprintMatch ?? 'null',
    schema_type: schemaType ?? 'null',
    factsCount: entityFacts.length,
    gapsCount: entityGaps.length,
    sourcesCount: sources.length,
    last_verified: lastVerified,
    flag: flagStr
  });
}

// ---------------------------------------------------------------------------
// Render Output Tables & Summary
// ---------------------------------------------------------------------------
console.log('\n| themeId | archetype | blueprint_match | schema.type | số entity_facts | số entity_gaps | số sources | last_verified | FLAG |');
console.log('|---|---|---|---|---|---|---|---|---|');
for (const r of rows) {
  console.log(`| ${r.themeId} | ${r.archetype} | ${r.blueprint_match} | ${r.schema_type} | ${r.factsCount} | ${r.gapsCount} | ${r.sourcesCount} | ${r.last_verified} | ${r.flag} |`);
}

console.log('\n======================================================');
console.log('TỔNG HỢP KIỂM ĐỊNH GEO ENTITY DATA (161 THEMES):');
console.log(`- Tổng số themes: ${rows.length}`);
console.log(`- Số theme 'exact': ${exactCount}`);
console.log(`- Số theme 'shared': ${sharedCount}`);
console.log(`- Số theme 'null': ${nullCount}`);
console.log(`- Số theme bị FLAG: ${flagCount}`);
console.log('======================================================\n');

// ---------------------------------------------------------------------------
// Flagged URLs Table
// ---------------------------------------------------------------------------
const flaggedUrls: { url: string; reason: string; themesCount: number }[] = [];
for (const [url, themes] of urlToThemes.entries()) {
  const status = urlStatus.get(url);
  const isOverused = themes.size > 30;
  const isNot200 = status !== 200;

  // Find all labels referring to this URL
  const labelsForUrl: string[] = [];
  for (const themeId of themes) {
    const cluster = allClusters.find(c => c.themeId === themeId);
    for (const s of cluster?.data?.geo_optimization?.sources || []) {
      if (s.url === url && s.label && !labelsForUrl.includes(s.label)) {
        labelsForUrl.push(s.label);
      }
    }
  }

  const reasons: string[] = [];
  if (isNot200) reasons.push(`HTTP ${status}`);
  if (isOverused) reasons.push(`Dẫn ở ${themes.size} themes (> 30)`);

  for (const label of labelsForUrl) {
    const docMatch = label.match(/\b(\d{1,4}\/\d{4})\b/);
    if (docMatch) {
      const docNum = docMatch[1];
      if (REPLACED_DOCUMENTS.has(docNum)) {
        reasons.push(`Văn bản đã bị thay thế: ${docNum}`);
      }
      const title = urlTitle.get(url) || '';
      const pageContent = urlContent.get(url) || '';
      if (!title.includes(docNum) && !pageContent.includes(docNum)) {
        reasons.push(`Số hiệu ${docNum} không xuất hiện trong trang`);
      }
    }
  }

  if (reasons.length > 0) {
    flaggedUrls.push({
      url,
      reason: Array.from(new Set(reasons)).join(', '),
      themesCount: themes.size
    });
  }
}

console.log('DANH SÁCH URL BỊ FLAG:');
if (flaggedUrls.length === 0) {
  console.log('Không có URL nào bị FLAG. Tất cả các URL nguồn đều trả về HTTP 200, nội dung khớp số hiệu văn bản và không bị hết hiệu lực/thay thế.');
} else {
  console.log('| URL | Lý do FLAG | Số themes sử dụng |');
  console.log('|---|---|---|');
  for (const fu of flaggedUrls) {
    console.log(`| ${fu.url} | ${fu.reason} | ${fu.themesCount} |`);
  }
}
