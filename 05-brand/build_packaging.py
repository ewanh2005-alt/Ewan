#!/usr/bin/env python3
"""Builds flat wrapper mockups (front + back) for the three test bars from research/04d_recovery_output.json,
so pack numbers can never drift from the calculations.
Run from repo root (after research/04d_recovery_calcs.py):  python3 05-brand/build_packaging.py
Writes 05-brand/packaging-{front,back}-{slug}.svg, plus packaging-front.svg / packaging-back.svg (= hero flavour)."""
import json
import re
from pathlib import Path

D = json.loads(Path("research/04d_recovery_output.json").read_text())["label"]
OAT, INK, STONE = "#F4EFE6", "#1C1B19", "#5E5A52"
FONT = "Archivo, Inter, 'Helvetica Neue', Arial, sans-serif"
W, H = 760, 320
RI = dict(kcal=2000, f=70, sf=20, c=260, s=90, p=50, salt=6)

FLAVOURS = {  # name in 04d -> slug, colour, front decoration, front ingredient line
    "Chocolate Peanut Butter": dict(slug="choc-pb", colour="#5A3A29", deco="oats",
                                    line="Eggs · quark · oats · peanut butter · cocoa"),
    "Vanilla": dict(slug="vanilla", colour="#8A5A0B", deco="speck",
                    line="Eggs · quark · oats · honey · vanilla"),
    "Banana Bread": dict(slug="banana-bread", colour="#B93D0B", deco="banana",
                         line="Eggs · quark · oats · banana · cinnamon"),
}
HERO = "Chocolate Peanut Butter"

wm = Path("05-brand/logo-wordmark-light.svg").read_text()
WORD = re.search(r"<g .*?</g>", wm, re.S).group(0)


def r(k, v):
    if k in ("kj", "kcal"):
        return f"{v:.0f}"
    if k == "salt":
        return f"{v:.2f}"
    return f"{v:.0f}" if v >= 10 else f"{v:.1f}"


def crimp(x):
    pts = " ".join(f"{x + (6 if i % 2 else 0)},{i * 10}" for i in range(H // 10 + 1))
    return f'<polyline points="{pts}" fill="none" stroke="{STONE}" stroke-opacity=".35" stroke-width="1.5"/>'


def deco(kind):
    if kind == "oats":
        return "".join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="2.4" fill="{OAT}" fill-opacity=".6" transform="rotate({a} {x} {y})"/>'
                       for x, y, a in [(520, 120, 20), (548, 150, -30), (585, 112, 60), (640, 105, 75), (660, 128, -15), (690, 168, 40), (575, 175, -50), (700, 120, 10)])
    if kind == "speck":
        return "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="{INK}" fill-opacity=".55"/>'
                       for x, y in [(515, 115), (530, 160), (560, 130), (585, 175), (575, 108), (640, 118), (665, 150), (690, 112), (700, 170), (650, 178), (545, 140), (680, 135)])
    # banana slices
    return "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#F6E7A8"/><circle cx="{x}" cy="{y}" r="3" fill="#E2C76A"/>'
                   for x, y in [(530, 125), (575, 165), (650, 120), (695, 160)])


def front(name, f, L):
    pb = L["per_bar"]
    col = f["colour"]
    p, c, s = round(pb["p"]), round(pb["c"]), round(pb["s"])
    macro = lambda x, num, label: (
        f'<text x="{x}" y="200" font-family="{FONT}" font-weight="800" font-size="40" fill="{INK}">{num}<tspan font-size="20" font-weight="700"> g</tspan></text>'
        f'<text x="{x}" y="222" font-family="{FONT}" font-size="13" fill="{STONE}" letter-spacing=".5">{label}</text>')
    title = name.replace("&", "&amp;")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="fettle {title} wrapper, front (concept)">
  <title>fettle {title}: front of pack (concept; working name; numbers from research/04d_recovery_calcs.py)</title>
  <rect width="{W}" height="{H}" fill="{OAT}"/>
  {crimp(8)}{crimp(W - 14)}
  <g transform="translate(40 30) scale(.42)">{WORD}</g>
  <text x="{W - 40}" y="52" text-anchor="end" font-family="{FONT}" font-size="12" font-weight="700" letter-spacing="1.5" fill="{col}">REAL-FOOD RECOVERY BAR · BAKED FRESH</text>
  <text x="40" y="128" font-family="{FONT}" font-weight="800" font-size="34" fill="{col}">{title}</text>
  {macro(40, p, "PROTEIN")}{macro(160, c, "CARBS")}{macro(280, s, "SUGAR")}
  <g>
    <rect x="490" y="92" width="110" height="100" rx="16" fill="{col}"/>
    <rect x="610" y="92" width="110" height="100" rx="16" fill="{col}"/>
    {deco(f["deco"])}
  </g>
  <text x="605" y="214" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{STONE}">{f["line"]}</text>
  <rect x="0" y="252" width="{W}" height="68" fill="{col}"/>
  <text x="40" y="282" font-family="{FONT}" font-size="15" font-weight="600" fill="{OAT}">No protein powder · No sweeteners</text>
  <text x="40" y="302" font-family="{FONT}" font-size="12" font-weight="700" letter-spacing="1" fill="{OAT}" fill-opacity=".85">KEEP REFRIGERATED</text>
  <rect x="{W - 300}" y="272" width="124" height="28" rx="14" fill="{OAT}"/>
  <text x="{W - 238}" y="291" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="800" letter-spacing=".8" fill="{col}">HIGH PROTEIN</text>
  <text x="{W - 40}" y="291" text-anchor="end" font-family="{FONT}" font-size="13" font-weight="700" fill="{OAT}">approx. {L["baked_g_estimate"]} g</text>
</svg>
'''


def back(name, f, L):
    pb, ph = L["per_bar"], L["per_100g"]
    ing = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", L["ingredients"])
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
           f" h4{{font-size:11px;letter-spacing:.6px;text-transform:uppercase;margin:0 0 3px;color:{f['colour']}}} p{{margin:0 0 6px}}"
           f" table{{border-collapse:collapse;width:100%;font-size:10px}} th,td{{border-bottom:1px solid {INK};padding:2px 4px;text-align:right;vertical-align:top}}"
           f" th:first-child,td:first-child{{text-align:left}} th{{border-bottom:2px solid {INK}}} td.sub{{padding-left:12px}}"
           f" .ph{{background:#fff3c4;padding:0 3px;border-radius:2px}} .small{{font-size:9px;color:{STONE}}}")
    title = name.replace("&", "&amp;")
    nut_line = " Made in a kitchen that also handles <b>peanuts</b>." if "peanuts" not in L["allergens"] else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="fettle {title} wrapper, back (concept)">
  <title>fettle {title}: back of pack (concept; numbers from research/04d_recovery_calcs.py)</title>
  <rect width="{W}" height="{H}" fill="{OAT}"/>
  {crimp(8)}{crimp(W - 14)}
  <foreignObject x="34" y="20" width="350" height="290">
    <div xmlns="http://www.w3.org/1999/xhtml"><style>{css}</style>
      <h4>{title} recovery bar</h4>
      <p><b>Ingredients:</b> {ing}</p>
      <p><b>Allergy advice:</b> for allergens, including cereals containing gluten, see ingredients in <b>bold</b>.{nut_line} <span class="ph">[confirm after allergen risk assessment]</span></p>
      <p><b>High protein.</b> Protein contributes to a growth in muscle mass. Enjoy as part of a varied, balanced diet and a healthy lifestyle.</p>
      <p>Made for after training. Not designed for eating before or during exercise.</p>
      <p class="small"><b>Keep refrigerated (0–5 °C).</b> Use by: <span class="ph">[date]</span>. Once opened, eat straight away. Suitable for home freezing: freeze on day of purchase, defrost overnight in the fridge · Lot: <span class="ph">[lot]</span><br/><span class="ph">[Business name, UK address]</span> · Baked in <span class="ph">[Durham]</span>, UK</p>
    </div>
  </foreignObject>
  <foreignObject x="400" y="20" width="326" height="290">
    <div xmlns="http://www.w3.org/1999/xhtml"><style>{css}</style>
      <h4>Nutrition</h4>
      <table><thead><tr><th>Typical values</th><th>Per 100 g</th><th>Per bar (approx. {L["baked_g_estimate"]} g)</th><th>%RI*</th></tr></thead><tbody>{trs}</tbody></table>
      <p class="small" style="margin-top:4px">*Reference intake of an average adult (8400 kJ / 2000 kcal). Concept pack: values calculated from the recipe; bar weight and per-100 g values estimated until test bakes are weighed. To be confirmed by lab analysis before sale.</p>
    </div>
  </foreignObject>
</svg>
'''


for name, f in FLAVOURS.items():
    L = D[name]
    Path(f"05-brand/packaging-front-{f['slug']}.svg").write_text(front(name, f, L))
    Path(f"05-brand/packaging-back-{f['slug']}.svg").write_text(back(name, f, L))
    if name == HERO:
        Path("05-brand/packaging-front.svg").write_text(front(name, f, L))
        Path("05-brand/packaging-back.svg").write_text(back(name, f, L))
print("wrote packaging fronts and backs for:", ", ".join(FLAVOURS))
