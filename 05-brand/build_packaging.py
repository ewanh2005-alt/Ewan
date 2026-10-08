#!/usr/bin/env python3
"""Builds the flat wrapper mockups for the hero flavour from the Phase 4 output,
so pack numbers can never drift from the calculations.
Run from repo root (after 04-nutrition.py):  python3 05-brand/build_packaging.py"""
import json
import re
from pathlib import Path

N = json.loads(Path("research/04_nutrition_output.json").read_text())["A_cocoa_peanut"]
OAT, INK, STONE, EMBER, COCOA = "#F4EFE6", "#1C1B19", "#5E5A52", "#B93D0B", "#5A3A29"
FONT = "Archivo, Inter, 'Helvetica Neue', Arial, sans-serif"
W, H = 760, 320

# reuse the wordmark strokes from the logo file
wm = Path("05-brand/logo-wordmark-light.svg").read_text()
WORD = re.search(r"<g .*?</g>", wm, re.S).group(0)

pb, ph = N["per_bar"], N["per_100g"]
RI = dict(kcal=2000, f=70, sf=20, c=260, s=90, p=50, salt=6)


def r(k, v):  # same rounding as 04-nutrition.py
    if k in ("kj", "kcal"):
        return f"{v:.0f}"
    if k == "salt":
        return f"{v:.2f}"
    return f"{v:.0f}" if v >= 10 else f"{v:.1f}"


def crimp(x):
    pts = " ".join(f"{x + (6 if i % 2 else 0)},{i * 10}" for i in range(H // 10 + 1))
    return f'<polyline points="{pts}" fill="none" stroke="{STONE}" stroke-opacity=".35" stroke-width="1.5"/>'


def front():
    p, c, sug, wt = round(pb["p"]), round(pb["c"]), round(pb["s"]), round(pb["weight"])
    oats = "".join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="2.4" fill="{OAT}" fill-opacity=".55" transform="rotate({a} {x} {y})"/>'
                   for x, y, a in [(520, 120, 20), (548, 150, -30), (585, 112, 60), (610, 160, 10), (660, 128, -15), (690, 168, 40), (640, 105, 75), (575, 175, -50)])
    macro = lambda x, num, unit, label: (
        f'<text x="{x}" y="200" font-family="{FONT}" font-weight="800" font-size="40" fill="{INK}">{num}<tspan font-size="20" font-weight="700">{unit}</tspan></text>'
        f'<text x="{x}" y="222" font-family="{FONT}" font-size="13" fill="{STONE}" letter-spacing=".5">{label}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="fettle Cocoa and Peanut wrapper, front">
  <title>fettle Cocoa &amp; Peanut Butter: front of pack (concept)</title>
  <rect width="{W}" height="{H}" fill="{OAT}"/>
  {crimp(8)}{crimp(W - 14)}
  <g transform="translate(40 30) scale(.42)">{WORD}</g>
  <text x="{W - 40}" y="52" text-anchor="end" font-family="{FONT}" font-size="12" font-weight="700" letter-spacing="1.5" fill="{EMBER}">FOR AFTER TRAINING · BAKED FRESH</text>
  <text x="40" y="128" font-family="{FONT}" font-weight="800" font-size="34" fill="{COCOA}">Cocoa &amp; Peanut Butter</text>
  {macro(40, sug, " g", "SUGAR")}{macro(160, p, " g", "PROTEIN")}{macro(280, c, " g", "CARBS")}
  <g>
    <rect x="490" y="92" width="110" height="100" rx="16" fill="{COCOA}"/>
    <rect x="610" y="92" width="110" height="100" rx="16" fill="{COCOA}"/>
    {oats}
  </g>
  <text x="605" y="214" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{STONE}">Eggs · oats · quark · oat bran · seeds · cocoa</text>
  <rect x="0" y="252" width="{W}" height="68" fill="{COCOA}"/>
  <text x="40" y="292" font-family="{FONT}" font-size="15" font-weight="600" fill="{OAT}">Kitchen ingredients · No powders · No sweeteners</text>
  <rect x="{W - 330}" y="272" width="124" height="28" rx="14" fill="{OAT}"/>
  <text x="{W - 268}" y="291" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="800" letter-spacing=".8" fill="{COCOA}">HIGH PROTEIN</text>
  <rect x="{W - 198}" y="272" width="100" height="28" rx="14" fill="{OAT}"/>
  <text x="{W - 148}" y="291" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="800" letter-spacing=".8" fill="{COCOA}">LOW SUGAR</text>
  <text x="{W - 40}" y="291" text-anchor="end" font-family="{FONT}" font-size="13" font-weight="700" fill="{OAT}">{wt} g ℮</text>
</svg>
'''


def back():
    ing = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", N["ingredients"])
    rows = [("Energy", f'{r("kj", ph["kj"])} kJ<br/>{r("kcal", ph["kcal"])} kcal', f'{r("kj", pb["kj"])} kJ<br/>{r("kcal", pb["kcal"])} kcal', f'{pb["kcal"] / RI["kcal"] * 100:.0f}%'),
            ("Fat", f'{r("f", ph["f"])} g', f'{r("f", pb["f"])} g', f'{pb["f"] / RI["f"] * 100:.0f}%'),
            ("of which saturates", f'{r("sf", ph["sf"])} g', f'{r("sf", pb["sf"])} g', f'{pb["sf"] / RI["sf"] * 100:.0f}%'),
            ("Carbohydrate", f'{r("c", ph["c"])} g', f'{r("c", pb["c"])} g', f'{pb["c"] / RI["c"] * 100:.0f}%'),
            ("of which sugars", f'{r("s", ph["s"])} g', f'{r("s", pb["s"])} g', f'{pb["s"] / RI["s"] * 100:.0f}%'),
            ("Fibre", f'{r("fb", ph["fb"])} g', f'{r("fb", pb["fb"])} g', ""),
            ("Protein", f'{r("p", ph["p"])} g', f'{r("p", pb["p"])} g', f'{pb["p"] / RI["p"] * 100:.0f}%'),
            ("Salt", f'{r("salt", ph["salt"])} g', f'{r("salt", pb["salt"])} g', f'{pb["salt"] / RI["salt"] * 100:.0f}%')]
    trs = "".join(f'<tr><td{" class=\"sub\"" if n.startswith("of") else ""}>{n}</td><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for n, a, b, c in rows)
    css = (f"*{{margin:0;box-sizing:border-box}} div{{font-family:{FONT};color:{INK};font-size:10.5px;line-height:1.35}}"
           f" h4{{font-size:11px;letter-spacing:.6px;text-transform:uppercase;margin:0 0 3px;color:{INK}}} p{{margin:0 0 7px}}"
           f" table{{border-collapse:collapse;width:100%;font-size:10px}} th,td{{border-bottom:1px solid {INK};padding:2px 4px;text-align:right;vertical-align:top}}"
           f" th:first-child,td:first-child{{text-align:left}} th{{border-bottom:2px solid {INK}}} td.sub{{padding-left:12px}}"
           f" .ph{{background:#fff3c4;padding:0 3px;border-radius:2px}} .small{{font-size:9px;color:{STONE}}}")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="fettle Cocoa and Peanut wrapper, back">
  <title>fettle Cocoa &amp; Peanut Butter: back of pack (concept; numbers from 04-nutrition.py)</title>
  <rect width="{W}" height="{H}" fill="{OAT}"/>
  {crimp(8)}{crimp(W - 14)}
  <foreignObject x="34" y="20" width="350" height="290">
    <div xmlns="http://www.w3.org/1999/xhtml"><style>{css}</style>
      <h4>Cocoa &amp; Peanut Butter bar</h4>
      <p><b>Ingredients:</b> {ing}</p>
      <p><b>Allergy advice:</b> for allergens, including cereals containing gluten, see ingredients in <b>bold</b>. Made in a kitchen that also handles <b>peanuts</b> and other allergens. <span class="ph">[confirm after allergen risk assessment]</span></p>
      <h4>How to eat it</h4>
      <p>For after training, when a proper meal is still a way off. Not designed for eating before or during exercise.</p>
      <p><b>High protein. Low sugar.</b> Protein contributes to a growth in muscle mass. Enjoy as part of a varied, balanced diet and a healthy lifestyle.</p>
      <p class="small"><b>Keep refrigerated (0–5 °C).</b> Use by: <span class="ph">[date]</span>. Suitable for home freezing: freeze on day of purchase, defrost in the fridge · Lot: <span class="ph">[lot]</span><br/><span class="ph">[Business name, UK address]</span> · Made in <span class="ph">[Durham]</span>, UK · <span class="ph">[recycling info]</span></p>
    </div>
  </foreignObject>
  <foreignObject x="400" y="20" width="326" height="290">
    <div xmlns="http://www.w3.org/1999/xhtml"><style>{css}</style>
      <h4>Nutrition</h4>
      <table><thead><tr><th>Typical values</th><th>Per 100 g</th><th>Per bar ({round(pb["weight"])} g)</th><th>%RI*</th></tr></thead><tbody>{trs}</tbody></table>
      <p class="small" style="margin-top:4px">*Reference intake of an average adult (8400 kJ / 2000 kcal). Values calculated; to be confirmed by lab analysis before sale.</p>
    </div>
  </foreignObject>
</svg>
'''


Path("05-brand/packaging-front.svg").write_text(front())
Path("05-brand/packaging-back.svg").write_text(back())
print("wrote packaging-front.svg, packaging-back.svg")
