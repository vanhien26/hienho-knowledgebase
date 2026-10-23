#!/usr/bin/env node

/**
 * GTM & GA4 OAuth Authorizer and MCP Server Configurator
 * 
 * Script này cấp quyền truy cập Google Tag Manager (GTM API v2) và Google Analytics 4,
 * tự động lưu token và đồng bộ cấu hình GTM MCP Server vào ~/.gemini/config/mcp_config.json.
 */

const fs = require("fs");
const path = require("path");
const http = require("http");
const { exec } = require("child_process");

const BASE_DIR = path.resolve(__dirname, "..");
const CREDS_FILE = path.join(BASE_DIR, "07_REPORTS", "data", "credentials", "ga4-credentials.json");
const TOKEN_FILE = path.join(BASE_DIR, "07_REPORTS", "data", "credentials", "gtm-token.json");
const GA4_TOKEN_FILE = path.join(BASE_DIR, "07_REPORTS", "data", "credentials", "ga4-token.json");
const GLOBAL_MCP_CONFIG = path.join(process.env.HOME, ".gemini", "config", "mcp_config.json");

if (!fs.existsSync(CREDS_FILE)) {
  console.error("Không tìm thấy file credentials tại:", CREDS_FILE);
  process.exit(1);
}

const credsRaw = JSON.parse(fs.readFileSync(CREDS_FILE, "utf8"));
const creds = credsRaw.installed || credsRaw.web;
const clientId = creds.client_id;
const clientSecret = creds.client_secret;

const PORT = 8089;
const redirectUri = `http://localhost:${PORT}`;

const scopes = [
  "https://www.googleapis.com/auth/analytics.readonly",
  "https://www.googleapis.com/auth/tagmanager.readonly",
  "https://www.googleapis.com/auth/tagmanager.edit.containers",
  "https://www.googleapis.com/auth/tagmanager.edit.containerversions",
  "https://www.googleapis.com/auth/tagmanager.publish"
].join(" ");

const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?` + new URLSearchParams({
  client_id: clientId,
  redirect_uri: redirectUri,
  response_type: "code",
  scope: scopes,
  access_type: "offline",
  prompt: "consent"
}).toString();

console.log(`\n======================================================`);
console.log(`  XÁC THỰC GOOGLE TAG MANAGER (GTM MCP SERVER)`);
console.log(`======================================================`);
console.log(`Đang mở trình duyệt để cấp quyền GTM và GA4...\n`);
console.log(`Nếu trình duyệt không tự mở, hãy truy cập link sau:`);
console.log(authUrl);
console.log(`\nĐang lắng nghe mã xác thực trên cổng ${PORT}...`);

const openCmd = process.platform === "darwin" ? `open "${authUrl}"` : process.platform === "win32" ? `start "${authUrl}"` : `xdg-open "${authUrl}"`;
exec(openCmd, () => {});

const server = http.createServer(async (req, res) => {
  try {
    const reqUrl = new URL(req.url, `http://localhost:${PORT}`);
    const code = reqUrl.searchParams.get("code");
    const error = reqUrl.searchParams.get("error");

    if (error) {
      res.writeHead(400, { "Content-Type": "text/html; charset=utf-8" });
      res.end(`<h2>Xác thực thất bại: ${error}</h2>`);
      server.close();
      console.error("Lỗi xác thực OAuth:", error);
      process.exit(1);
    }

    if (code) {
      res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      res.end(`<html><body style="font-family: -apple-system, sans-serif; text-align: center; padding: 60px;"><h2>Xác thực GTM & GA4 thành công!</h2><p>Hệ thống đã nhận token và cập nhật MCP Server. Bạn có thể đóng tab này.</p></body></html>`);
      server.close();

      const tokenRes = await fetch("https://oauth2.googleapis.com/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({
          client_id: clientId,
          client_secret: clientSecret,
          code: code,
          grant_type: "authorization_code",
          redirect_uri: redirectUri
        }).toString()
      });

      const tokenData = await tokenRes.json();
      if (!tokenData.access_token || !tokenData.refresh_token) {
        console.error("Không lấy được refresh_token từ Google:", tokenData);
        process.exit(1);
      }

      // Lưu gtm-token.json và đồng bộ ga4-token.json
      const tokenPayload = {
        client_id: clientId,
        refresh_token: tokenData.refresh_token,
        updated_at: new Date().toISOString()
      };
      fs.writeFileSync(TOKEN_FILE, JSON.stringify(tokenPayload, null, 2), "utf8");
      fs.writeFileSync(GA4_TOKEN_FILE, JSON.stringify(tokenPayload, null, 2), "utf8");
      console.log(`\n✓ Đã lưu token mới vào: ${TOKEN_FILE}`);

      // Cập nhật cấu hình MCP Server toàn cục (~/.gemini/config/mcp_config.json)
      let mcpConfig = { mcpServers: {} };
      if (fs.existsSync(GLOBAL_MCP_CONFIG)) {
        try {
          mcpConfig = JSON.parse(fs.readFileSync(GLOBAL_MCP_CONFIG, "utf8"));
          if (!mcpConfig.mcpServers) mcpConfig.mcpServers = {};
        } catch (e) {}
      }

      mcpConfig.mcpServers.gtm = {
        command: "npx",
        args: ["-y", "samarth-gtm-mcp"],
        env: {
          GOOGLE_OAUTH_CLIENT_ID: clientId,
          GOOGLE_OAUTH_CLIENT_SECRET: clientSecret,
          GOOGLE_REFRESH_TOKEN: tokenData.refresh_token,
          GTM_MCP_ENABLE_WRITES: "true",
          GTM_MCP_ENABLE_PUBLISH: "false"
        }
      };

      fs.writeFileSync(GLOBAL_MCP_CONFIG, JSON.stringify(mcpConfig, null, 2), "utf8");
      console.log(`✓ Đã đăng ký thành công GTM MCP Server vào: ${GLOBAL_MCP_CONFIG}`);
      console.log(`\nCấu hình MCP hoàn tất!`);
      process.exit(0);
    }
  } catch (err) {
    console.error("Lỗi trong quá trình xử lý:", err);
    process.exit(1);
  }
});

server.listen(PORT);
server.on("error", (e) => {
  console.error(`Không thể mở cổng ${PORT}:`, e.message);
  process.exit(1);
});
