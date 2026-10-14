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
  name: "Graft Pitch",
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
  pres.title = "Graft: pitch";
  pres.author = "Ewan";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;

  pres.defineSlideMaster({
    title: "Dark title",
    background: { color: C.text1 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.45, w: 12.1, h: 1.3, fontSize: 36, bold: true, color: C.background1, valign: "top", align: "left", margin: 0 }, text: "" } },
      { text: { text: "Graft · Real food for grafters · Durham Venture School", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.accent3, margin: 0 } } },
    ],
    slideNumber: { x: 12.4, y: 7.0, w: 0.4, h: 0.3, fontSize: 10, color: C.accent3 },
  });
  pres.defineSlideMaster({
    title: "Content",
    background: { color: C.background1 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 12.1, h: 0.85, fontSize: 32, bold: true, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
      { text: { text: "Graft · Real food for grafters · Durham Venture School", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.accent3, margin: 0 } } },
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
    { text: "Graft: ", options: {} },
    { text: "real food", options: { color: C.accent1 } },
    { text: " for people who train hard", options: {} },
  ], { placeholder: "title" });
  s.addText("Graft is a fresh, baked protein snack made from real food (egg, quark and oats) for athletes who train hard and can't always cook. Baked to order and delivered to squads.", {
    x: 0.6, y: 1.55, w: 12.1, h: 0.9, fontSize: 18, color: C.background1, margin: 0, isTextBox: true, objectName: "Subtitle",
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
  s.addImage({ path: path.join(__dirname, "..", "05-brand", "graft-logo-light.png"), x: 0.6, y: 6.2, w: 1.75, h: 0.49, objectName: "Graft logo", altText: "Graft logo" });
  s.addText("Ewan Hetherington · Durham Business Management graduate · MMA, football, gym · Real food for grafters.", { x: 2.6, y: 6.25, w: 10.1, h: 0.4, fontSize: 14, italic: true, color: C.accent3, margin: 0, valign: "middle", isTextBox: true, objectName: "Branding note" });
  s.addNotes("~60s. SAY FIRST: 'Graft is a fresh, baked protein snack made from real food (egg, quark and oats) for athletes who train hard and can't always cook. Baked to order and delivered to squads.' I'm Ewan: Durham Business Management graduate; I train MMA, play football and lift. It came from my own training. After two MMA classes back to back I'd eat a full meal and still be after more. Going from MMA straight to football, I'm in a rush and need something quick but proper. On a same-day weigh-in I'm depleted after making weight and have a short window to refuel before I compete. Every time, the choice is a lab-made protein bar full of powders and sweeteners, or nothing. So I made Graft: about 15 g protein per 50 g from egg, quark and oats, no powders or sweeteners. The format (soft-baked bar, bites or slice) is decided by taste test. Graft is British slang for hard work: it is for people who put the work in. Real food for grafters. (Note for weigh-in days: fibre before competing can upset the gut, so a lower-fibre version may suit that use. Worth testing.)");

  // ---------------- Slide 2: why it's needed ----------------
  pres.addSection({ title: "Problem" });
  s = pres.addSlide({ masterName: "Content", sectionTitle: "Problem" });
  s.addText("The problem: told to eat real food, no time to make it", { placeholder: "title" });
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
  s.addText("Who it's for: Jack, and the squads who'll try it first", { placeholder: "title" });
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
    { text: "Trains once a day: gym (8/10) + a sport (4/10)", options: { bullet: true, breakLine: true } },
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
  s.addText("Early adopters: coached Durham squads + my MMA club. One coach = ~25 athletes = one drop. (0/10 committed yet; the squad trial tests this.)", {
    x: 5.3, y: 6.3, w: 7.4, h: 0.6, fontSize: 14, bold: true, color: C.accent1, margin: 0, valign: "top", isTextBox: true, objectName: "Still to prove",
  });
  s.addNotes("~70s. I've spoken to 10 athletes and gym-goers, including a pro footballer, a rugby player and an aspiring bodybuilder, plus the Team Durham S&C coach and a nutrition professor. I've got more interviews lined up [say who]. 7 of 10 liked the idea. They want high protein and real food. The problems with what's out there: price, taste, and ingredients they don't trust. The S&C coach watched students fail to finish boxes of Grenade bars. Why it's a migraine: after training they need protein and carbs. Chicken-and-rice meal prep works when they manage it, but it means cooking ahead and carrying a tub. The quick options fall short: fruit has no protein, lab bars are full of powders and sweeteners, 'natural' bars are mostly sugar. So they compromise or go without, after almost every session, which for someone training 5-6 days a week is 5-6 times a week. My persona is Jack: trains once a day, plays a sport, is trying to eat well and trusts his coach. My early adopters are the sharpest slice of Jack: coached athletes, starting with Team Durham squads and my MMA club. Why them: they train hardest, their coach tells them to eat whole food, and one coach means about 25 athletes and one delivery, which suits a fresh bar. Honestly: nobody has committed yet; that's what the squad trial is for. Interview notes are paraphrased, not quotes.");

  // ---------------- Slide 4: competition ----------------
  pres.addSection({ title: "Market" });
  s = pres.addSlide({ masterName: "Content", sectionTitle: "Market" });
  s.addText("The gap: nobody does all three", { placeholder: "title" });
  s.addImage({ path: path.join(__dirname, "..", "16-gap-chart.png"), x: 0.6, y: 1.35, w: 8.6, h: 5.35, objectName: "Gap chart", altText: "Scatter of 25 UK protein snacks: protein vs sugar per 50 g. Every high-protein, low-sugar bar uses powders; real-food bars are high in sugar; Graft is the only real-food point in the gap." });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 9.45, y: 1.35, w: 3.25, h: 5.35, rectRadius: 0.12, fill: { color: C.background2 }, line: { type: "none" }, objectName: "Gap card" });
  s.addText("25 snacks, 4 tests", { x: 9.7, y: 1.55, w: 2.8, h: 0.4, fontSize: 16, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: "Tests title" });
  s.addText([
    { text: "≥10 g protein: 20", options: { bullet: true, breakLine: true } },
    { text: "Low sugar: 11", options: { bullet: true, breakLine: true } },
    { text: "Real-food protein: 4", options: { bullet: true, breakLine: true } },
    { text: "All four: 0", options: { bullet: true, bold: true, color: C.accent1 } },
  ], { x: 9.7, y: 2.0, w: 2.8, h: 1.5, fontSize: 13, color: C.text1, margin: 0, valign: "top", paraSpaceAfter: 3, isTextBox: true, objectName: "Tests list" });
  s.addText("Why the gap exists", { x: 9.7, y: 3.65, w: 2.8, h: 0.4, fontSize: 16, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: "Why title" });
  s.addText([
    { text: "Shops need months of shelf life; real food lasts days", options: { bullet: true, breakLine: true } },
    { text: "Powders and sweeteners keep bars soft and cheap", options: { bullet: true, breakLine: true } },
    { text: "Graft bakes to order and sells direct to squads", options: { bullet: true, bold: true } },
  ], { x: 9.7, y: 4.1, w: 2.8, h: 2.4, fontSize: 13, color: C.text1, margin: 0, valign: "top", paraSpaceAfter: 4, isTextBox: true, objectName: "Why list" });
  s.addNotes("~60s. I scored 25 UK protein snacks on four tests: at least 10 g protein, protein from real food rather than powders, no sweeteners, and low sugar. 20 have the protein, 11 are low in sugar, only 4 use real-food protein, and none pass all four. The high-protein, low-sugar bars all use powders, mostly with sweeteners. The real-food bars carry 13 to 20 g of sugar. Why? Shops need months of shelf life, and real food lasts days. Graft designs around that: bake to order, sell direct to squads. Graft's numbers are calculated, not yet lab-tested. OLD NOTES (competitor detail): These are the bars athletes see: Myprotein's Re-Fuel, Amacx, HIGH5, Styrkr, Huel. The ones with 20 g protein get it from protein powder, and most rely on syrups or sugar alcohols. Re-Fuel's first ingredient is maltitol. The 'real food' bars like Veloforte have lots of sugar and only 12 g protein. Across 32+ UK bars I checked, none gets its protein from real food with low sugar. Graft does: two 50 g bars give about 29 g protein and 28 g carbs from egg, quark and oats, with a little honey or banana and no sweeteners. Our numbers are calculated from the ingredients and will be lab-checked.");

  // ---------------- Slide 5: model ----------------
  pres.addSection({ title: "Model" });
  s = pres.addSlide({ masterName: "Content", sectionTitle: "Model" });
  s.addText("Graft: how it works and what's next", { placeholder: "title" });
  s.addImage({ path: path.join(__dirname, "..", "05-brand", "graft-logo-dark.png"), x: 11.15, y: 0.5, w: 1.55, h: 0.43, objectName: "Graft logo", altText: "Graft logo" });
  const flav = ["Soft-baked bar", "Bites", "Slice"];
  s.addText("Formats in testing", { x: 0.6, y: 1.4, w: 5, h: 0.4, fontSize: 16, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: "Flavours heading" });
  for (let i = 0; i < 3; i++) {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6 + i * 2.55, y: 1.9, w: 2.35, h: 0.6, rectRadius: 0.3, fill: { color: C.accent4 }, line: { type: "none" }, objectName: `Flavour ${i + 1}` });
    s.addText(flav[i], { x: 0.6 + i * 2.55, y: 1.9, w: 2.35, h: 0.6, fontSize: 14, bold: true, color: C.accent5, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `Flavour ${i + 1} label` });
  }
  s.addText("~15 g protein per 50 g · egg, quark & oats · no powders or sweeteners · ~4 g sugar (calculated, not lab-tested)", { x: 0.6, y: 2.6, w: 12.1, h: 0.4, fontSize: 14, color: C.accent3, margin: 0, isTextBox: true, objectName: "Flavour macros" });

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
    { text: "Next: ", options: { bold: true, color: C.accent1 } },
    { text: "blind taste test (≥7/9) → free squad trial.  ", options: { color: C.background1 } },
    { text: "Need: ", options: { bold: true, color: C.accent1 } },
    { text: "kitchen access + coach intros.", options: { color: C.background1, breakLine: true } },
    { text: "Graft: fresh, baked, real-food protein for people who train hard. Real food for grafters.", options: { bold: true, color: C.background1 } },
  ], { x: 0.9, y: 5.65, w: 11.5, h: 1.0, fontSize: 15, margin: 0, valign: "middle", isTextBox: true, objectName: "Close text" });
  s.addNotes("~60s. I'm testing three formats with the same ingredients: a soft-baked bar, bites and a slice; the taste test decides. About 15 g protein per 50 g, calculated. Because it's real food, it's fresh and chilled, not shelf-stable, so I'm using the Simmer Eats model. Simmer cooks fresh meals that last up to 5 days in the fridge and can be frozen on arrival. People order weekly (and squads order through their coach), I bake to order, deliver chilled around Durham to start, and they eat it within 3 days or freeze it. 'Baked this week, not 12 months ago.' Next: a blind taste test against Barebells, aiming for 7 out of 9, then a free squad trial. What I need: kitchen access and coach introductions. SAY LAST: 'Graft is a fresh, baked protein snack made from real food (egg, quark and oats) for athletes who train hard and can't always cook. Baked to order and delivered to squads. Real food for grafters.' Thank you.");

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
