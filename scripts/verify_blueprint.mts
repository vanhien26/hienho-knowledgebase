import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { getGeoEntityBlueprint, THEME_ARCHETYPE } from '../../Web-Idea/react-web-momo/lib/content-plan/geo-entity-registry.ts';

const summaryPath = path.resolve('../Web-Idea/react-web-momo/data/seo-clusters-summary.json');
const summaryData = JSON.parse(fs.readFileSync(summaryPath, 'utf-8'));
const usecases = summaryData.usecases;

console.log(`\n========================================================================================`);
console.log(`BÁO CÁO KIỂM TRA GEO ENTITY BLUEPRINT CHO TOÀN BỘ 161 THEMES (SSOT)`);
console.log(`========================================================================================\n`);

let mappedCount = 0;
let nullCount = 0;
const nullThemes: Array<{ id: string; name: string; sector: string }> = [];

console.log(`STT | ${'Theme ID'.padEnd(25)} | ${'Sector'.padEnd(14)} | ${'Archetype'.padEnd(28)} | ${'Schema Type'.padEnd(22)} | Words | Status`);
console.log(`----+---------------------------+----------------+------------------------------+------------------------+-------+--------`);

usecases.forEach((u: any, idx: number) => {
  const blueprint = getGeoEntityBlueprint(u.id, u.display_name || u.name, u.sector);
  const archetypeKey = THEME_ARCHETYPE[u.id];

  if (blueprint) {
    mappedCount++;
    const words = blueprint.word_count;
    console.log(
      `${String(idx + 1).padStart(3)} | ` +
      `${u.id.padEnd(25)} | ` +
      `${(u.sector || '').padEnd(14)} | ` +
      `${(archetypeKey || '').padEnd(28)} | ` +
      `${blueprint.schema_type.padEnd(22)} | ` +
      `${String(words).padStart(5)} | ` +
      `OK`
    );
  } else {
    nullCount++;
    nullThemes.push({ id: u.id, name: u.display_name || u.name, sector: u.sector });
    console.log(
      `${String(idx + 1).padStart(3)} | ` +
      `${u.id.padEnd(25)} | ` +
      `${(u.sector || '').padEnd(14)} | ` +
      `${'null'.padEnd(28)} | ` +
      `${'null'.padEnd(22)} | ` +
      `${'0'.padStart(5)} | ` +
      `NULL`
    );
  }
});

console.log(`\n----------------------------------------------------------------------------------------`);
console.log(`TỔNG KẾT:`);
console.log(`- Tổng số themes kiểm tra: ${usecases.length}`);
console.log(`- Số themes có Blueprint hợp lệ: ${mappedCount}`);
console.log(`- Số themes trả về null: ${nullCount}`);
console.log(`\nDANH SÁCH ${nullCount} THEMES TRẢ VỀ NULL (CHƯA CÓ ARCHETYPE / NGOÀI PHẠM VI):`);
nullThemes.forEach((t, i) => {
  console.log(`  ${i + 1}. ${t.id.padEnd(22)} (${t.name}) - Sector: ${t.sector}`);
});
console.log(`----------------------------------------------------------------------------------------\n`);
