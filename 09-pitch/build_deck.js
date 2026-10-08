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
  name: "Recovery Bar Pitch",
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
  pres.title = "Real-food recovery bar: pitch";
  pres.author = "Ewan";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;

  pres.defineSlideMaster({
    title: "Dark title",
    background: { color: C.text1 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.45, w: 12.1, h: 1.3, fontSize: 36, bold: true, color: C.background1, valign: "top", align: "left", margin: 0 }, text: "" } },
      { text: { text: "Durham Venture School · Week 5 · working name & branding TBC", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.accent3, margin: 0 } } },
    ],
    slideNumber: { x: 12.4, y: 7.0, w: 0.4, h: 0.3, fontSize: 10, color: C.accent3 },
  });
  pres.defineSlideMaster({
    title: "Content",
    background: { color: C.background1 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 12.1, h: 0.85, fontSize: 32, bold: true, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
      { text: { text: "Durham Venture School · Week 5 · working name & branding TBC", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.accent3, margin: 0 } } },
    ],
    slideNumber: { x: 12.4, y: 7.0, w: 0.4, h: 0.3, fontSize: 10, color: C.accent3 },
  });

  const circleIcon = async (slide, Comp, x, y, d, name, fill = C.accent1) => {
    slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fill }, line: { type: "none" }, objectName: name + " circle" });
    slide.addImage({ data: await icon(Comp), x: x + d * 0.25, y: y + d * 0.25, w: d * 0.5, h: d * 0.5, objectName: name + " icon", altText: name });
  };

  // ---------------- Slide 1: pivot + story ----------------
  pres.addSection({ title: "Concept" });
  let s = pres.addSlide({ masterName: "Dark title", sectionTitle: "Concept" });
  s.addText([
    { text: "The pivot: a ", options: {} },
    { text: "real-food", options: { color: C.accent1 } },
    { text: " recovery bar for athletes who train hard", options: {} },
  ], { placeholder: "title" });
  s.addText("~20 g protein  ·  ~30 g carbs  ·  made from eggs, quark & oats  ·  no powders, sweeteners or sugar alcohols", {
    x: 0.6, y: 1.8, w: 12.1, h: 0.45, fontSize: 18, color: C.background1, margin: 0, isTextBox: true, objectName: "Subtitle",
  });
  s.addText("Where it came from: my own training", { x: 0.6, y: 2.65, w: 12.1, h: 0.4, fontSize: 16, bold: true, color: C.accent1, margin: 0, isTextBox: true, objectName: "Story heading" });
  const moments = [
    [fa.FaHandRock, "Two MMA classes back to back", "Ate a full meal afterwards and was still after more. A meal alone wasn't enough to refuel."],
    [fa.FaFutbol, "MMA, then straight to football", "In a rush between sessions, with no time to cook and needing something quick and proper."],
    [fa.FaWeight, "Same-day weigh-in", "Depleted after making weight, with a short window to refuel before competing."],
  ];
  for (let i = 0; i < 3; i++) {
    const x = 0.6 + i * 4.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 3.2, w: 3.8, h: 2.9, rectRadius: 0.12, fill: { color: C.text2 }, line: { type: "none" }, objectName: `Moment ${i + 1} card` });
    await circleIcon(s, moments[i][0], x + 0.3, 3.45, 0.75, `Moment ${i + 1}`);
    s.addText(moments[i][1], { x: x + 0.3, y: 4.35, w: 3.2, h: 0.6, fontSize: 17, bold: true, color: C.background1, margin: 0, valign: "top", isTextBox: true, objectName: `Moment ${i + 1} title` });
    s.addText(moments[i][2], { x: x + 0.3, y: 4.95, w: 3.2, h: 1.05, fontSize: 14, color: C.background1, margin: 0, valign: "top", isTextBox: true, objectName: `Moment ${i + 1} text` });
  }
  s.addText("Branding is in the works: working name only, nothing set yet.", { x: 0.6, y: 6.35, w: 12.1, h: 0.4, fontSize: 14, italic: true, color: C.accent3, margin: 0, isTextBox: true, objectName: "Branding note" });
  s.addNotes("~60s. I've pivoted. The idea is now a recovery bar made from real food, for athletes who train hard. It came from my own training. After two MMA classes back to back I'd eat a full meal and still be after more. Going from MMA straight to football, I'm in a rush and need something quick but proper. On a same-day weigh-in I'm depleted after making weight and have a short window to refuel before I compete. Every time, the choice is a lab-made protein bar full of powders and sweeteners, or nothing. So the bar is ~20 g protein and ~30 g carbs from eggs, quark and oats. Branding's in progress: working name only, nothing's set. (Note for weigh-in days: fibre before competing can upset the gut, so a lower-fibre version may suit that use. Worth testing.)");

  // ---------------- Slide 2: why it's needed ----------------
  pres.addSection({ title: "Problem" });
  s = pres.addSlide({ masterName: "Content", sectionTitle: "Problem" });
  s.addText("Why it's needed: told to eat real food, no time to make it", { placeholder: "title" });
  const stats = [
    ["80%", "of Canadian university athletes say their schedule limits their ability to cook and prepare meals", "Morassutti 2024, U Sports survey"],
    ["Carbs", "are what athletes miss: team-sport athletes meet protein targets but fall short on carbohydrate and energy", "Jenner et al. 2019, 21 studies"],
    ["#1", "Whole-food products were the most preferred choice among 405 athletes", "Carey et al. 2023"],
    ["Tastier", "Athletes rate everyday food tastier, cheaper and safer. Sports foods win only on convenience", "Forsyth & Mantzioris 2023"],
  ];
  for (let i = 0; i < 4; i++) {
    const x = 0.6 + i * 3.075;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.5, w: 2.85, h: 3.2, rectRadius: 0.12, fill: { color: C.background2 }, line: { type: "none" }, objectName: `Stat ${i + 1} card` });
    s.addText(stats[i][0], { x: x + 0.25, y: 1.7, w: 2.4, h: 1.0, fontSize: 48, bold: true, color: C.accent1, fontFace: THEME.headFontFace, margin: 0, isTextBox: true, objectName: `Stat ${i + 1} number` });
    s.addText(stats[i][1], { x: x + 0.25, y: 2.75, w: 2.4, h: 1.4, fontSize: 14, color: C.text1, margin: 0, valign: "top", isTextBox: true, objectName: `Stat ${i + 1} text` });
    s.addText(stats[i][2], { x: x + 0.25, y: 4.2, w: 2.4, h: 0.35, fontSize: 10, italic: true, color: C.accent3, margin: 0, isTextBox: true, objectName: `Stat ${i + 1} source` });
  }
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 5.0, w: 12.1, h: 1.25, rectRadius: 0.12, fill: { color: C.accent4 }, line: { type: "none" }, objectName: "Gap box" });
  await circleIcon(s, fa.FaExclamation, 0.85, 5.25, 0.75, "Gap");
  s.addText([
    { text: "The convenient options don't fit. ", options: { bold: true } },
    { text: "Low-sugar bars rely on protein powders, sweeteners and sugar alcohols; \"real-food\" bars carry 10–28 g sugar and little protein. Only ~4% of UK adults get enough fibre." },
  ], { x: 1.8, y: 5.1, w: 10.7, h: 1.05, fontSize: 15, color: C.text1, margin: 0, valign: "middle", isTextBox: true, objectName: "Gap text" });
  s.addNotes("~60s. This isn't just me. A survey of Canadian university athletes found 80% say their schedule limits their ability to cook. A review of 21 studies found team-sport athletes hit their protein but fall short on carbs, which is exactly what you need to refuel. Given the choice, athletes prefer whole-food products (405 athletes), and they rate everyday food as tastier, cheaper and safer. Sports foods only win on convenience. So athletes are stuck between real food they can't always make and convenient bars built on powders, sweeteners and sugar alcohols, or 'natural' bars full of sugar. Sources: Morassutti 2024 (York University); Jenner 2019; Carey 2023; Forsyth & Mantzioris 2023; NDNS fibre data.");

  // ---------------- Slide 3: customers ----------------
  pres.addSection({ title: "Customers" });
  s = pres.addSlide({ masterName: "Content", sectionTitle: "Customers" });
  s.addText("What athletes told me, and who it's for", { placeholder: "title" });
  // left column: who + persona
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 1.45, w: 4.3, h: 2.55, rectRadius: 0.12, fill: { color: C.background2 }, line: { type: "none" }, objectName: "Spoken to card" });
  await circleIcon(s, fa.FaComments, 0.85, 1.65, 0.6, "Spoken to");
  s.addText("Who I've spoken to", { x: 1.6, y: 1.65, w: 3.1, h: 0.6, fontSize: 17, bold: true, color: C.text1, margin: 0, valign: "middle", isTextBox: true, objectName: "Spoken to title" });
  s.addText([
    { text: "10 athletes & gym-goers: pro footballer, rugby player, bodybuilder, gym/football/padel", options: { bullet: true, breakLine: true } },
    { text: "Team Durham S&C coach + nutrition professor", options: { bullet: true, breakLine: true } },
    { text: "Lined up: [add who's booked]", options: { bullet: true, bold: true, color: C.accent1 } },
  ], { x: 0.85, y: 2.35, w: 3.9, h: 1.55, fontSize: 14, color: C.text1, margin: 0, valign: "top", paraSpaceAfter: 4, isTextBox: true, objectName: "Spoken to list" });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 4.2, w: 4.3, h: 2.6, rectRadius: 0.12, fill: { color: C.text1 }, line: { type: "none" }, objectName: "Persona card" });
  await circleIcon(s, fa.FaUserCircle, 0.85, 4.4, 0.6, "Persona");
  s.addText("Early persona: Jack", { x: 1.6, y: 4.4, w: 3.1, h: 0.6, fontSize: 17, bold: true, color: C.background1, margin: 0, valign: "middle", isTextBox: true, objectName: "Persona title" });
  s.addText([
    { text: "Trains most days: gym (8/10) + a sport (4/10)", options: { bullet: true, breakLine: true } },
    { text: "Trying to eat well (8/10); trusts his coach", options: { bullet: true, breakLine: true } },
    { text: "Often can't cook after training; worries about taste & price", options: { bullet: true } },
  ], { x: 0.85, y: 5.1, w: 3.9, h: 1.6, fontSize: 14, color: C.background1, margin: 0, valign: "top", paraSpaceAfter: 4, isTextBox: true, objectName: "Persona list" });

  // right column: four insight rows
  const rows = [
    [fa.FaQuoteLeft, "What they said", "7/10 liked the idea. They want high protein (4/10) and real food (4/10). Coach: whole foods, good taste, high protein:carb ratio, some fibre."],
    [fa.FaTimes, "Problems with what's out there", "Too expensive (3/10), taste is a gamble (3/10), \"bad ingredients\". Boxes of Grenade bars given to students went uneaten."],
    [fa.FaExchangeAlt, "Why they'd switch", "Real food their coach approves of, with protein and carbs in one, made to taste good."],
    [fa.FaBolt, "Why it's a migraine, not a headache", "After training they need protein and carbs. Meal prep isn't always possible, and quick options fall short: fruit lacks protein, lab bars are artificial, \"natural\" bars are sugary. It happens after almost every session."],
  ];
  for (let i = 0; i < 4; i++) {
    const y = 1.45 + i * 1.18;
    await circleIcon(s, rows[i][0], 5.3, y + 0.1, 0.6, rows[i][1]);
    s.addText(rows[i][1], { x: 6.1, y, w: 6.6, h: 0.38, fontSize: 16, bold: true, color: C.accent1, margin: 0, isTextBox: true, objectName: `Row ${i + 1} title` });
    s.addText(rows[i][2], { x: 6.1, y: y + 0.38, w: 6.6, h: 0.72, fontSize: 14, color: C.text1, margin: 0, valign: "top", isTextBox: true, objectName: `Row ${i + 1} text` });
  }
  s.addText("Still to prove: 0/10 have committed yet, and some gym-goers just wait for a meal, so the focus is athletes who train hard.", {
    x: 5.3, y: 6.35, w: 7.4, h: 0.55, fontSize: 13, italic: true, color: C.accent3, margin: 0, valign: "top", isTextBox: true, objectName: "Still to prove",
  });
  s.addNotes("~70s. I've spoken to 10 athletes and gym-goers, including a pro footballer, a rugby player and an aspiring bodybuilder, plus the Team Durham S&C coach and a nutrition professor. I've got more interviews lined up [say who]. 7 of 10 liked the idea. They want high protein and real food. The problems with what's out there: price, taste, and ingredients they don't trust. The S&C coach watched students fail to finish boxes of Grenade bars. Why it's a migraine: after training they need protein and carbs. Chicken-and-rice meal prep works when they manage it, but it means cooking ahead and carrying a tub. The quick options fall short: fruit has no protein, lab bars are full of powders and sweeteners, 'natural' bars are mostly sugar. So they compromise or go without, after almost every session, which for someone training 5-6 days a week is 5-6 times a week. Early persona: Jack trains most days, is trying to eat well and trusts his coach. Honestly: nobody has committed yet, and some gym-goers just wait for a meal, so I'm focusing on athletes who train hard. Interview notes are paraphrased, not quotes.");

  // ---------------- Slide 4: competition ----------------
  pres.addSection({ title: "Market" });
  s = pres.addSlide({ masterName: "Content", sectionTitle: "Market" });
  s.addText("Competition: nobody gets 20 g protein from real food", { placeholder: "title" });
  const hdr = ["Bar (per bar)", "Protein", "Carbs", "Sugar", "What it's made with"].map((t) => ({ text: t, options: { bold: true, color: C.background1, fill: { color: C.text1 } } }));
  const comp = [
    ["Myprotein THE Re-Fuel (80 g)", "22 g", "32 g", "n/p", "Maltitol (1st ingredient), whey, glycerol"],
    ["Amacx Recovery (55 g, XMiles)", "20 g", "22 g", "n/p", "Soy/whey/milk protein mix, glucose-fructose syrup"],
    ["HIGH5 Recovery Protein (50 g)", "19 g", "19 g", "n/p", "Glucose syrup, invert sugar, sugar, milk & soy protein"],
    ["Styrkr BAR+ Recovery (74 g)", "15 g", "47 g", "28 g", "Glucose syrup, soy protein isolate, sugar"],
    ["Huel Bar (55 g)", "15 g", "17 g", "2 g", "Maltitol, rice & pea protein, corn fibre"],
    ["Veloforte Forza (70 g, \"real food\")", "12 g", "38 g", "28 g", "Apricot, almond, egg white, cane sugar"],
  ];
  const body = comp.map((r) => r.map((t) => ({ text: t, options: { color: C.text1 } })));
  const ours = ["Our bar (calculated)", "~20–21 g", "~28–31 g", "~7–8 g", "Eggs, quark, oats, honey or banana. Nothing else"].map((t) => ({ text: t, options: { bold: true, color: C.background1, fill: { color: C.accent1 } } }));
  s.addTable([hdr, ...body, ours], {
    x: 0.6, y: 1.4, w: 8.4, colW: [2.75, 0.95, 0.95, 0.85, 2.9], fontSize: 12, rowH: 0.52, valign: "middle",
    border: { type: "solid", pt: 0.75, color: HEX.accent6 }, fill: { color: C.background1 }, margin: 0.06, objectName: "Competitor table",
  });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 9.3, y: 1.4, w: 3.4, h: 4.15, rectRadius: 0.12, fill: { color: C.background2 }, line: { type: "none" }, objectName: "Gap card" });
  await circleIcon(s, fa.FaCheck, 9.55, 1.6, 0.6, "What we have", C.accent2);
  s.addText("What they don't have, and we do", { x: 9.55, y: 2.3, w: 3.0, h: 0.7, fontSize: 16, bold: true, color: C.text1, margin: 0, valign: "top", isTextBox: true, objectName: "Gap card title" });
  s.addText([
    { text: "~20 g protein from real food", options: { bullet: true, breakLine: true } },
    { text: "Real carbs from oats", options: { bullet: true, breakLine: true } },
    { text: "No powders, sweeteners or sugar alcohols", options: { bullet: true, breakLine: true } },
    { text: "Baked fresh", options: { bullet: true } },
  ], { x: 9.55, y: 3.05, w: 3.0, h: 2.35, fontSize: 14, color: C.text1, margin: 0, valign: "top", paraSpaceAfter: 6, isTextBox: true, objectName: "Gap card list" });
  s.addText("Checked 32+ UK bars: the high-protein ones use powders and sweeteners; the real-food ones are high in sugar, low in protein.", {
    x: 0.6, y: 5.75, w: 12.1, h: 0.55, fontSize: 14, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: "Market summary",
  });
  s.addText("Per bar, from brand/retailer pages, Oct 2026. n/p = not published where checked. Our figures are calculated from ingredients, not lab-tested.", {
    x: 0.6, y: 6.35, w: 12.1, h: 0.35, fontSize: 10, italic: true, color: C.accent3, margin: 0, isTextBox: true, objectName: "Table source",
  });
  s.addNotes("~60s. These are the recovery bars athletes see: Myprotein's Re-Fuel, Amacx, HIGH5, Styrkr, Huel. The ones with 20 g protein get it from protein powder, and most rely on syrups or sugar alcohols. Re-Fuel's first ingredient is maltitol. The 'real food' bars like Veloforte have lots of sugar and only 12 g protein. Across 32+ UK bars I checked, none gets around 20 g protein from real food alone. Ours does: ~20 g protein and ~30 g carbs from eggs, quark and oats, with a little honey or banana. Our numbers are calculated from the ingredients and will be lab-checked.");

  // ---------------- Slide 5: model ----------------
  pres.addSection({ title: "Model" });
  s = pres.addSlide({ masterName: "Content", sectionTitle: "Model" });
  s.addText("How it works: baked fresh, like Simmer Eats", { placeholder: "title" });
  const flav = ["Chocolate Peanut Butter", "Vanilla", "Banana Bread"];
  s.addText("Three flavours in testing", { x: 0.6, y: 1.4, w: 5, h: 0.4, fontSize: 16, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: "Flavours heading" });
  for (let i = 0; i < 3; i++) {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6 + i * 2.55, y: 1.9, w: 2.35, h: 0.6, rectRadius: 0.3, fill: { color: C.accent4 }, line: { type: "none" }, objectName: `Flavour ${i + 1}` });
    s.addText(flav[i], { x: 0.6 + i * 2.55, y: 1.9, w: 2.35, h: 0.6, fontSize: 14, bold: true, color: C.accent5, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `Flavour ${i + 1} label` });
  }
  s.addText("Each ~20 g protein · ~30 g carbs · ≤8 g sugar · ~260–280 kcal (calculated)", { x: 0.6, y: 2.6, w: 7.6, h: 0.4, fontSize: 14, color: C.accent3, margin: 0, isTextBox: true, objectName: "Flavour macros" });

  const steps = [
    [fa.FaClipboardList, "Order", "Weekly orders and squad orders via coaches"],
    [fa.FaFire, "Bake", "Baked to order, no long-life additives"],
    [fa.FaTruck, "Deliver chilled", "Hand-delivered in Durham to start"],
    [fa.FaSnowflake, "Eat or freeze", "Fridge 3 days, or freeze for later"],
  ];
  for (let i = 0; i < 4; i++) {
    const x = 0.6 + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 3.3, w: 2.8, h: 2.0, rectRadius: 0.12, fill: { color: C.background2 }, line: { type: "none" }, objectName: `Step ${i + 1} card` });
    await circleIcon(s, steps[i][0], x + 0.25, 3.5, 0.6, `Step ${i + 1}`);
    s.addText(`${i + 1}. ${steps[i][1]}`, { x: x + 0.95, y: 3.5, w: 1.75, h: 0.6, fontSize: 16, bold: true, color: C.text1, margin: 0, valign: "middle", isTextBox: true, objectName: `Step ${i + 1} title` });
    s.addText(steps[i][2], { x: x + 0.25, y: 4.25, w: 2.35, h: 0.95, fontSize: 14, color: C.text1, margin: 0, valign: "top", isTextBox: true, objectName: `Step ${i + 1} text` });
    if (i < 3) s.addShape(pres.shapes.RIGHT_ARROW, { x: x + 2.83, y: 4.15, w: 0.24, h: 0.3, fill: { color: C.accent1 }, line: { type: "none" }, objectName: `Arrow ${i + 1}` });
  }
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 5.55, w: 12.1, h: 1.2, rectRadius: 0.12, fill: { color: C.text1 }, line: { type: "none" }, objectName: "Close box" });
  s.addText([
    { text: "\"Baked this week, not 12 months ago.\" ", options: { bold: true, color: C.accent1 } },
    { text: "The short shelf life is the proof it's real food, the same model as Simmer Eats' fresh meals. Next: taste tests vs Barebells, a squad trial with Team Durham, and more interviews.", options: { color: C.background1 } },
  ], { x: 0.9, y: 5.65, w: 11.5, h: 1.0, fontSize: 15, margin: 0, valign: "middle", isTextBox: true, objectName: "Close text" });
  s.addNotes("~60s. Three flavours in testing: Chocolate Peanut Butter, Vanilla and Banana Bread. Each is around 20 g protein and 30 g carbs. Because it's real food, it's fresh and chilled, not shelf-stable, so I'm using the Simmer Eats model. Simmer cooks fresh meals that last up to 5 days in the fridge and can be frozen on arrival. People order weekly (and squads order through their coach), I bake to order, deliver chilled around Durham to start, and they eat it within 3 days or freeze it. 'Baked this week, not 12 months ago.' Next steps: blind taste tests against Barebells, a squad trial with Team Durham, registering as a food business, and more interviews. Thank you.");

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
