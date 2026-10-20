#!/usr/bin/env node

/**
 * GA4 Data Fetcher for MoMo Web Platform
 * Uses Google Analytics Data API v1beta via native JWT authentication.
 * 
 * Usage:
 *   node scripts/fetch_ga4.js
 *   node scripts/fetch_ga4.js --start 2026-10-01 --end yesterday
 *   node scripts/fetch_ga4.js --prefix /cinema
 */

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

// Configuration SSOT
const PROPERTY_ID = "270743103";
const KEY_PATHS = [
  path.join(__dirname, "..", "07_REPORTS", "data", "credentials", "ga4-credentials.json"),
  path.join(__dirname, "..", "07_REPORTS", "data", "ga4-credentials.json"),
  "C:\\Users\\hien.ho\\Downloads\\momo-web-platform-seo-20fb7568b499.json"
];

function resolveKeyFile() {
  for (const p of KEY_PATHS) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error(`Credentials file not found in paths: ${KEY_PATHS.join(", ")}`);
}

function base64UrlEncode(str) {
  return Buffer.from(str).toString("base64url");
}

async function getAccessToken(key) {
  const now = Math.floor(Date.now() / 1000);
  const header = { alg: "RS256", typ: "JWT" };
  const claim = {
    iss: key.client_email,
    scope: "https://www.googleapis.com/auth/analytics.readonly",
    aud: "https://oauth2.googleapis.com/token",
    exp: now + 3600,
    iat: now
  };

  const tokenPayload = `${base64UrlEncode(JSON.stringify(header))}.${base64UrlEncode(JSON.stringify(claim))}`;
  const sign = crypto.createSign("RSA-SHA256");
  sign.update(tokenPayload);
  const signature = sign.sign(key.private_key, "base64url");
  const jwt = `${tokenPayload}.${signature}`;

  const res = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=${jwt}`
  });
  const data = await res.json();
  if (!data.access_token) {
    throw new Error(`Failed to get OAuth token: ${JSON.stringify(data)}`);
  }
  return data.access_token;
}

async function runReport(accessToken, requestBody) {
  const url = `https://analyticsdata.googleapis.com/v1beta/properties/${PROPERTY_ID}:runReport`;
  const res = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(requestBody)
  });
  const data = await res.json();
  if (data.error) {
    throw new Error(`GA4 API Error: ${JSON.stringify(data.error)}`);
  }
  return data;
}

// CLI args parsing
const args = process.argv.slice(2);
function getArg(flag, defaultValue) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : defaultValue;
}

const startDate = getArg("--start", "2026-10-01");
const endDate = getArg("--end", "yesterday");
const prefix = getArg("--prefix", null);
const topCount = parseInt(getArg("--top", "10"), 10);

async function main() {
  const keyFile = resolveKeyFile();
  const key = JSON.parse(fs.readFileSync(keyFile, "utf8"));
  const accessToken = await getAccessToken(key);

  console.log(`\n======================================================`);
  console.log(`  MOMO WEB PLATFORM - GA4 REPORTING (PROPERTY ${PROPERTY_ID})`);
  console.log(`  Thời gian: ${startDate} -> ${endDate}`);
  if (prefix) console.log(`  Bộ lọc URL: ${prefix}`);
  console.log(`======================================================\n`);

  // 1. Overview Metrics
  const overviewFilter = prefix ? {
    filter: {
      fieldName: "pagePath",
      stringFilter: { matchType: "BEGINS_WITH", value: prefix }
    }
  } : undefined;

  const overviewData = await runReport(accessToken, {
    dateRanges: [{ startDate, endDate }],
    metrics: [
      { name: "screenPageViews" },
      { name: "sessions" },
      { name: "activeUsers" },
      { name: "bounceRate" },
      { name: "averageSessionDuration" }
    ],
    dimensionFilter: overviewFilter
  });

  if (overviewData.rows && overviewData.rows.length > 0) {
    const vals = overviewData.rows[0].metricValues;
    const views = Number(vals[0].value);
    const sessions = Number(vals[1].value);
    const users = Number(vals[2].value);
    const bounceRate = (Number(vals[3].value) * 100).toFixed(2);
    const avgDuration = Number(vals[4].value).toFixed(1);

    console.log(`[TỔNG QUAN HIỆU SUẤT]`);
    console.log(`- Pageviews        : ${views.toLocaleString("vi-VN")}`);
    console.log(`- Sessions         : ${sessions.toLocaleString("vi-VN")}`);
    console.log(`- Active Users     : ${users.toLocaleString("vi-VN")}`);
    console.log(`- Bounce Rate      : ${bounceRate}%`);
    console.log(`- Avg Duration (s) : ${avgDuration}s`);
    console.log("");
  }

  // 2. Top Pages
  const pagesData = await runReport(accessToken, {
    dateRanges: [{ startDate, endDate }],
    dimensions: [{ name: "pagePath" }],
    metrics: [
      { name: "screenPageViews" },
      { name: "sessions" },
      { name: "activeUsers" }
    ],
    dimensionFilter: overviewFilter,
    orderBys: [{ metric: { metricName: "screenPageViews" }, desc: true }],
    limit: topCount
  });

  if (pagesData.rows && pagesData.rows.length > 0) {
    console.log(`[TOP ${topCount} TRANG CÓ LƯỢT XEM CAO NHẤT]`);
    const formatted = pagesData.rows.map((r, i) => ({
      STT: i + 1,
      URL: r.dimensionValues[0].value,
      Pageviews: Number(r.metricValues[0].value).toLocaleString("vi-VN"),
      Sessions: Number(r.metricValues[1].value).toLocaleString("vi-VN"),
      Users: Number(r.metricValues[2].value).toLocaleString("vi-VN")
    }));
    console.table(formatted);
  }
}

main().catch(err => {
  console.error("[ERROR]", err.message);
  process.exit(1);
});
