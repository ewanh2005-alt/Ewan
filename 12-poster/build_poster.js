// Builds 12-poster/gym-poster-a4.pdf (A4) with a QR code to Ewan's Google Form survey.
// Run with NODE_PATH pointing at a folder that has `qrcode` and `playwright`.
const path = require("path");
const fs = require("fs");
const QRCode = require("qrcode");
const { chromium } = require("playwright");

const SURVEY = "https://docs.google.com/forms/d/e/1FAIpQLSeilE_9BxwhT6vIkU1nCfyYJWHIz9uEGCxyQN73SMp-4-bJqw/viewform";

(async () => {
  const logo = "data:image/png;base64," + fs.readFileSync(path.join(__dirname, "..", "05-brand", "graft-logo-dark.png")).toString("base64");
  const qr = await QRCode.toString(SURVEY, { type: "svg", margin: 1, errorCorrectionLevel: "M", color: { dark: "#1C1B19", light: "#FFFFFF" } });
  const html = `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Gym poster</title>
<style>
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0}
body{width:210mm;height:297mm;font-family:Arial,Helvetica,sans-serif;color:#1C1B19;background:#fff}
.page{height:297mm;padding:14mm 16mm;display:flex;flex-direction:column;align-items:center;text-align:center}
.logo{width:82mm;height:auto;margin-bottom:4mm}
.slogan{font-size:16pt;font-weight:700;color:#2F5D50;margin-bottom:7mm}
.tag{font-size:11pt;font-weight:700;letter-spacing:2px;color:#5E5A52;margin-bottom:5mm}
h1{font-size:31pt;line-height:1.05;font-weight:900;margin-bottom:8mm}
.lead{font-size:20pt;line-height:1.35;margin-bottom:3mm}
.lead b{color:#2F5D50}
.q{font-size:22pt;font-weight:700;margin:7mm 0 5mm}
.qr{width:72mm;height:72mm;padding:3mm;border:3px solid #1C1B19;border-radius:6mm}
.qr svg{width:100%;height:100%}
.scan{font-size:16pt;font-weight:700;margin-top:4mm}
.offer{margin-top:6mm;background:#2F5D50;color:#fff;font-size:20pt;font-weight:700;padding:5mm 10mm;border-radius:20mm}
.foot{margin-top:auto;padding-top:6mm;font-size:12pt;line-height:1.5;color:#3A3835}
.small{font-size:10pt;color:#5E5A52}
</style></head><body><div class="page">
<img class="logo" src="${logo}" alt="Graft">
<div class="slogan">Real food for grafters.</div>
<div class="tag">DURHAM VENTURE SCHOOL · STUDENT PROJECT</div>
<h1>Help build a real-food protein snack</h1>
<p class="lead">Real egg, quark &amp; oats.</p>
<p class="lead"><b>~15 g protein.</b> No whey. No sweeteners.</p>
<p class="q">What do you eat after training?<br>Tell me in 2 minutes</p>
<div class="qr">${qr}</div>
<p class="scan">Scan with your phone camera</p>
<div class="offer">Sign up to try the first batch, free</div>
<div class="foot"><b>Ewan</b>, local founder · Durham Venture School<br>
<span class="small">Your answers are only used for this project. Leaving your email is optional and you can ask to be removed anytime.</span></div>
</div></body></html>`;
  const htmlPath = path.join(__dirname, "gym-poster-a4.html");
  fs.writeFileSync(htmlPath, html);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto("file://" + htmlPath);
  await page.pdf({ path: path.join(__dirname, "gym-poster-a4.pdf"), format: "A4", printBackground: true });
  await page.setViewportSize({ width: 794, height: 1123 });
  await page.screenshot({ path: path.join(__dirname, "gym-poster-a4-preview.png") });
  await browser.close();
  console.log("wrote poster");
})();
