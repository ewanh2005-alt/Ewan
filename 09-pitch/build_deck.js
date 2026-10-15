// Builds 09-pitch/pitch-deck.pptx (5 slides, editable). Run from the scratchpad deck dir with its node_modules:
//   NODE_PATH=<dir>/node_modules node 09-pitch/build_deck.js
const path = require("path");
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");
const { applyTheme } = require(process.env.APPLY_THEME);

const OUT = path.join(__dirname, "pitch-deck.pptx");
const THEME = {
  name: "Pitch",
  headFontFace: "Arial",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1C1B19", lt1: "FFFFFF", dk2: "3A3835", lt2: "F3F4F6",
    accent1: "C2410C", accent2: "15803D", accent3: "6B7280", accent4: "FDE7DC",
    accent5: "7C2D12", accent6: "E5E7EB", hlink: "C2410C", folHlink: "7C2D12",
  },
};
const HEX = THEME.colors;

async function icon(Comp, color = "FFFFFF") {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color: "#" + color, size: 256 }));
  const buf = await sharp(Buffer.from(svg)).resize(256, 256).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5 in
  pres.title = "Real-food protein snack: pitch";
  pres.author = "Ewan";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;

  pres.defineSlideMaster({
    title: "Dark title",
    background: { color: C.text1 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.45, w: 12.1, h: 1.3, fontSize: 36, bold: true, color: C.background1, valign: "top", align: "left", margin: 0 }, text: "" } },
      { text: { text: "Durham Venture School · Ewan Hetherington", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.accent3, margin: 0 } } },
    ],
    slideNumber: { x: 12.4, y: 7.0, w: 0.4, h: 0.3, fontSize: 10, color: C.accent3 },
  });
  pres.defineSlideMaster({
    title: "Content",
    background: { color: C.background1 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 12.1, h: 0.85, fontSize: 32, bold: true, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
      { text: { text: "Durham Venture School · Ewan Hetherington", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.accent3, margin: 0 } } },
    ],
    slideNumber: { x: 12.4, y: 7.0, w: 0.4, h: 0.3, fontSize: 10, color: C.accent3 },
  });

  const ONE = "A fresh, baked protein snack made from real food for athletes who train hard and can't always cook.";
  const big = (s, text, opts) => s.addText(text, { margin: 0, isTextBox: true, color: C.text1, ...opts });

  // ---------------- Slide 1: the idea ----------------
  let s = pres.addSlide({ masterName: "Dark title" });
  s.addText([
    { text: "A ", options: {} },
    { text: "real-food", options: { color: C.accent1 } },
    { text: " protein snack for people who train hard", options: {} },
  ], { placeholder: "title" });
  big(s, "Fresh.  Baked to order.  No powders or sweeteners.", { x: 0.6, y: 2.4, w: 12.1, h: 0.6, fontSize: 24, color: C.background1, objectName: "Subtitle" });
  big(s, "Born from my own training: MMA, football, gym.", { x: 0.6, y: 3.5, w: 12.1, h: 0.5, fontSize: 20, color: C.accent3, objectName: "Story" });
  big(s, "Ewan Hetherington · Durham Business Management graduate", { x: 0.6, y: 6.2, w: 12.1, h: 0.4, fontSize: 14, italic: true, color: C.accent3, objectName: "Founder" });
  s.addNotes(`~50s. SAY FIRST: '${ONE} Baked to order.' I'm Ewan, a Durham Business Management graduate; I train MMA, play football and lift. After two MMA classes back to back I'd eat a full meal and still be hungry. Going from MMA straight to football I had no time to cook. On a same-day weigh-in I had a short window to eat before competing. Every time, the choice was a lab-made protein bar full of powders and sweeteners, or nothing.`);

  // ---------------- Slide 2: the problem ----------------
  s = pres.addSlide({ masterName: "Content" });
  s.addText("The problem: told to eat real food, no time to make it", { placeholder: "title" });
  const stats = [
    ["80%", "of student athletes say their schedule limits cooking"],
    ["#1", "whole food is athletes' top choice"],
    ["71%", "of UK adults try to avoid ultra-processed food"],
  ];
  stats.forEach(([n, t], i) => {
    const x = 0.6 + i * 4.1;
    big(s, n, { x, y: 1.9, w: 3.8, h: 1.3, fontSize: 72, bold: true, color: C.accent1, fontFace: THEME.headFontFace, objectName: `Stat ${i + 1}` });
    big(s, t, { x, y: 3.25, w: 3.6, h: 1.0, fontSize: 20, valign: "top", objectName: `Stat ${i + 1} text` });
  });
  big(s, "Quick options today: lab bars or sugary bars.", { x: 0.6, y: 5.3, w: 12.1, h: 0.6, fontSize: 24, bold: true, objectName: "Punchline" });
  big(s, "Morassutti 2024 · Carey 2023 · Mintel 2025", { x: 0.6, y: 6.4, w: 12.1, h: 0.3, fontSize: 10, italic: true, color: C.accent3, objectName: "Sources" });
  s.addNotes("~55s. 80% of university athletes say their schedule limits their ability to cook (Morassutti 2024). Team-sport athletes hit protein but fall short on carbs (Jenner 2019). Whole-food products were the number one preference among 405 athletes (Carey 2023), and athletes rate everyday food tastier, cheaper and safer; sports foods only win on convenience (Forsyth 2023). Why this needs to happen: the quick options are lab bars full of powders, sweeteners and sugar alcohols, or 'natural' bars full of sugar. Over half of what UK adults eat is ultra-processed and 71% are trying to avoid it (Mintel 2025). After Joe Wicks' ultra-processed food documentary last year, Grenade's sales fell 16%.");

  // ---------------- Slide 3: who it's for ----------------
  s = pres.addSlide({ masterName: "Content" });
  s.addText("Who it's for", { placeholder: "title" });
  const cols = [
    ["Customer: Jack", "Trains daily.\nTrying to eat well.\nListens to his coach."],
    ["Early interest", "Athletes who fit this profile\nsaid they were interested."],
    ["Then interviewed", "They shared their views:\nwant real food, high protein;\nworried about taste & price."],
  ];
  cols.forEach(([h, t], i) => {
    const x = 0.6 + i * 4.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.6, w: 3.8, h: 3.6, rectRadius: 0.12, fill: { color: i === 1 ? C.accent4 : C.background2 }, line: { type: "none" }, objectName: `Card ${i + 1}` });
    big(s, h, { x: x + 0.3, y: 1.85, w: 3.2, h: 0.6, fontSize: 24, bold: true, color: i === 1 ? C.accent5 : C.text1, objectName: `Card ${i + 1} title` });
    big(s, t, { x: x + 0.3, y: 2.6, w: 3.2, h: 2.4, fontSize: 22, valign: "top", objectName: `Card ${i + 1} text` });
  });
  big(s, "10 athlete interviews + an S&C coach + a nutrition professor. First test group: coached and combat-sport athletes.", { x: 0.6, y: 5.6, w: 12.1, h: 0.5, fontSize: 18, color: C.accent3, objectName: "Evidence" });
  s.addNotes("~55s. I've spoken to 10 athletes and gym-goers, including a pro footballer and a rugby player, plus the Team Durham S&C coach and a nutrition professor. My typical customer is Jack: trains once a day, plays a sport, is trying to eat well and listens to his coach. 8 of 10 train in the gym and are trying to eat better; their deal-breakers are taste and price. Athletes who fit this profile told me they were interested, and I then interviewed them: they want real food and high protein, and they worry about taste and price. The S&C coach told me boxes of Grenade bars given to students went uneaten. I'll test first with coached and combat-sport athletes, because one coach can reach a whole squad. No agreements yet; that's the next step. It's a migraine, not a vitamin: it happens after almost every session. Honestly, nobody has committed yet; the squad trial tests that.");

  // ---------------- Slide 4: the gap (competitors) ----------------
  s = pres.addSlide({ masterName: "Content" });
  s.addText("The gap: nobody does all of it", { placeholder: "title" });
  const Y = "✓", N = "✗";
  const head = ["", "High protein", "Real-food protein", "No sweeteners", "Low sugar", "Grab-and-go"];
  const comp = [
    ["Barebells · Grenade · Fulfil", Y, N, N, Y, Y],
    ["Nākd · Veloforte", "Some", Y, Y, N, Y],
    ["Bio&Me", N, N, Y, N, Y],
    ["Protein quark pots", Y, Y, "Some", Y, N],
    ["Our snack (aim)", Y, Y, Y, Y, Y],
  ];
  const cell = (t, r, c) => ({ text: t, options: {
    bold: r === 0 || c === 0 || r === comp.length,
    color: r === 0 ? C.background1 : (t === Y ? C.accent2 : t === N ? C.accent1 : C.text1),
    fill: { color: r === 0 ? C.text1 : (r === comp.length ? C.accent4 : C.background1) },
    align: c === 0 ? "left" : "center", fontSize: c === 0 || r === 0 ? 16 : (t === "Some" ? 16 : 24) } });
  s.addTable([head.map((t, c) => cell(t, 0, c)), ...comp.map((row, r) => row.map((t, c) => cell(t, r + 1, c)))], {
    x: 0.6, y: 1.4, w: 12.1, colW: [3.6, 1.7, 1.7, 1.7, 1.7, 1.7], rowH: 0.62, valign: "middle",
    border: { type: "solid", pt: 0.75, color: HEX.accent6 }, margin: 0.08, objectName: "Competitor table",
  });
  big(s, "25 UK snacks checked: none pass all four tests.  Why? Shops need months of shelf life; real food lasts days.", { x: 0.6, y: 5.45, w: 12.1, h: 0.8, fontSize: 18, bold: true, objectName: "Gap line" });
  big(s, "Brand and retailer pages, Oct 2026. Protein ≥10 g; low sugar ≤5 g per 50 g.", { x: 0.6, y: 6.35, w: 12.1, h: 0.3, fontSize: 10, italic: true, color: C.accent3, objectName: "Sources" });
  s.addNotes("~55s. Here's the competition and where the gap comes from. Protein bars like Barebells, Grenade and Fulfil have the protein and low sugar, but it comes from milk protein powders, with sweeteners and sugar alcohols like maltitol. 'Natural' bars like Nākd and Veloforte are real food with no sweeteners, but they carry 13 to 20 g of sugar per 50 g, and Nākd's protein is only 7 g. Bio&Me targets clean eating but has only 9 g of soya protein. Protein quark pots are real protein and fairly low in sugar, though some use sweeteners, but they're a pot with a spoon, not a grab-and-go snack after training. I checked 25 UK snacks on four tests and none passed all four. [pause] Why does the gap exist? Shops need bars that last months; real food lasts days, so brands use powders and sweeteners. I design around shelf life: bake to order and sell direct. And it can work: in the US, RXBAR built a real-food bar from a kitchen and sold for $600m, and Perfect Bar proved people buy protein bars from the fridge. Our snack's ticks are the aim; the recipe is still in testing.");

  // ---------------- Slide 5: how it works + next ----------------
  s = pres.addSlide({ masterName: "Content" });
  s.addText("How it works and what's next", { placeholder: "title" });
  big(s, "Order weekly  →  bake to order  →  deliver chilled", { x: 0.6, y: 1.7, w: 12.1, h: 0.7, fontSize: 28, bold: true, objectName: "Flow" });
  big(s, "Recipe still in testing. Aim: high protein, low sugar, no powders or sweeteners.", { x: 0.6, y: 2.5, w: 12.1, h: 0.5, fontSize: 20, color: C.accent3, objectName: "Spec" });
  const nx = [["Next", "Poster + landing page (Monday)  →  taste test  →  squad trial"], ["Need", "Kitchen access + coach introductions"]];
  nx.forEach(([h, t], i) => {
    const y = 3.5 + i * 1.0;
    big(s, h, { x: 0.6, y, w: 1.8, h: 0.7, fontSize: 26, bold: true, color: C.accent1, objectName: `${h} label` });
    big(s, t, { x: 2.5, y, w: 10.2, h: 0.7, fontSize: 24, objectName: `${h} text` });
  });
  big(s, "Real food for people who train hard.", { x: 0.6, y: 5.7, w: 12.1, h: 0.6, fontSize: 24, bold: true, italic: true, objectName: "Close" });
  s.addNotes(`~50s. Same ingredients, three formats in testing: soft-baked bar, bites or a slice; the taste test decides. The recipe is still being finalised, so I'm not quoting exact numbers yet. People and squads order weekly; I bake to order, deliver chilled around Durham, eaten within a few days or frozen. Next: on Monday my gym poster and a simple landing page go live; both send people to a two-minute survey and a waitlist, so I'm counting real sign-ups, not compliments. Then a blind taste test against Barebells, aiming for 7 out of 9, then a free squad trial. What I need: kitchen access and coach introductions. SAY LAST: '${ONE} Baked to order.' Thank you.`);

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
