"""Market-gap analysis: which UK grab-and-go protein snacks pass four tests?
1) >=10 g protein per serving  2) protein from whole food (egg, dairy, nuts), not isolates/powders
3) no sweeteners or polyols    4) <=5 g sugar per 50 g
Data: 02-competitors.csv (bars with protein + sugar known) + rows from 02d (WR40-WR52) + RXBAR label.
Run: python3 research/16_gap_analysis.py  -> research/16_gap_output.json + 16-gap-chart.svg"""
import csv, json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# sweetener/polyol flags for CSV rows (from key_ingredients / 02-competitor-analysis; None = not confirmed)
SWEET = {"forza": False, "styrkr": False, "torq": False, "grenade": True, "barebells": True, "fulfil": True,
         "mp_layered": True, "mp_flapjack": None, "phd": True, "misfits": None, "clif": False, "huel": True,
         "vf_crunch": False, "trek": False, "eroica": False, "perfect_bar": False, "warrior_raw": True}
SKIP = {"rego", "yazoo", "banana", "milk_banana", "nakd", "ella", "graze", "bounce", "nakd_protein",
        "battle", "mp_refuel", "amacx", "high5_recovery", "voom_recover", "rxbar"}  # drinks/fruit, no sugar figure, or replaced below

rows = []
for r in csv.DictReader(open(ROOT / "02-competitors.csv")):
    if r["id"] in SKIP or not r["sugars_g"] or not r["protein_g"]:
        continue
    rows.append(dict(name=f'{r["brand"]} {r["product"]}'.split(" (")[0], g=float(r["weight_g"]),
                     protein=float(r["protein_g"]), sugar=float(r["sugars_g"]),
                     whole_food=r["processing"] == "whole_food", sweet=SWEET.get(r["id"]),
                     uk=not r["id"] == "perfect_bar", src="02-competitors.csv"))

# extra rows (EVIDENCE: 02d WR40-WR52, prices/nutrition seen 12 Oct 2026; RXBAR from Kellogg CA/US label 13 Oct 2026)
rows += [
    dict(name="Bio&Me Daily Boost", g=40, protein=9.2, sugar=6.3, whole_food=False, sweet=False, uk=True, src="WR40"),
    dict(name="Trek High Protein", g=55, protein=15, sugar=4.7, whole_food=False, sweet=True, uk=True, src="WR49"),
    dict(name="KIND Protein", g=50, protein=12, sugar=8.6, whole_food=False, sweet=False, uk=True, src="WR46"),
    dict(name="Nakd Protein", g=45, protein=7.2, sugar=13, whole_food=True, sweet=False, uk=True, src="WR47"),
    dict(name="Perkier Protein", g=35, protein=5.6, sugar=6.3, whole_food=False, sweet=False, uk=True, src="WR48"),
    dict(name="H&B Precision Engineered", g=60, protein=21, sugar=1.3, whole_food=False, sweet=None, uk=True, src="WR50"),
    dict(name="Graze Oat Boosts", g=50, protein=3.2, sugar=4.5, whole_food=False, sweet=False, uk=True, src="WR42"),
    dict(name="RXBAR (US label)", g=52, protein=12, sugar=14, whole_food=True, sweet=False, uk=False, src="H1 / Kellogg label"),
]
# de-duplicate by name (02d values win)
seen = {}
for r in rows:
    seen[r["name"]] = r
rows = list(seen.values())

GRAFT = dict(name="Graft v6 (calculated)", g=50, protein=14.6, sugar=3.8, whole_food=True, sweet=False, uk=True, src="04d v6")

def tests(r):
    s50 = r["sugar"] * 50 / r["g"]
    return {"protein10": r["protein"] >= 10, "real_food": r["whole_food"],
            "no_sweet": r["sweet"] is False, "low_sugar": s50 <= 5}

out = []
for r in rows + [GRAFT]:
    t = tests(r)
    out.append({**r, "protein_50g": round(r["protein"] * 50 / r["g"], 1), "sugar_50g": round(r["sugar"] * 50 / r["g"], 1),
                **t, "all_four": all(t.values())})

comp = [o for o in out if o["name"] != GRAFT["name"]]
summary = {
    "products_scored": len(comp),
    "pass_protein10": sum(o["protein10"] for o in comp),
    "pass_real_food": sum(o["real_food"] for o in comp),
    "pass_no_sweet": sum(o["no_sweet"] for o in comp),
    "pass_low_sugar": sum(o["low_sugar"] for o in comp),
    "pass_protein_and_low_sugar": sum(o["protein10"] and o["low_sugar"] for o in comp),
    "pass_real_food_and_protein": sum(o["real_food"] and o["protein10"] for o in comp),
    "pass_all_four": [o["name"] for o in comp if o["all_four"]],
    "graft_all_four": out[-1]["all_four"],
}
json.dump({"summary": summary, "products": out}, open(ROOT / "research" / "16_gap_output.json", "w"), indent=1)

# ---------- SVG chart: protein vs sugar per 50 g ----------
W, H, L, R, T, B = 900, 560, 70, 30, 60, 70
xmax, ymax = 25, 20
X = lambda v: L + v / xmax * (W - L - R)
Y = lambda v: H - B - v / ymax * (H - T - B)
REAL, POWDER, INK, MUTED, GRID = "#1baf7a", "#eb6834", "#1d1d1b", "#52514e", "#e4e3de"
s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Arial, Helvetica, sans-serif">',
     f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>',
     f'<text x="{L}" y="28" font-size="20" font-weight="bold" fill="{INK}">The gap: nobody combines high protein, low sugar AND real food</text>',
     f'<text x="{L}" y="48" font-size="13" fill="{MUTED}">UK grab-and-go protein snacks, per 50 g. Every bar in the shaded zone (≥10 g protein, ≤5 g sugar) gets its protein from powders; most add sweeteners.</text>']
# gap zone
s.append(f'<rect x="{X(0)}" y="{Y(ymax)}" width="{X(5)-X(0)}" height="{Y(10)-Y(ymax)}" fill="{REAL}" fill-opacity="0.10" stroke="{REAL}" stroke-dasharray="4 4"/>')
for v in range(0, xmax + 1, 5):
    s.append(f'<line x1="{X(v)}" x2="{X(v)}" y1="{Y(0)}" y2="{Y(ymax)}" stroke="{GRID}"/><text x="{X(v)}" y="{Y(0)+18}" font-size="12" fill="{MUTED}" text-anchor="middle">{v}</text>')
for v in range(0, ymax + 1, 5):
    s.append(f'<line x1="{X(0)}" x2="{X(xmax)}" y1="{Y(v)}" y2="{Y(v)}" stroke="{GRID}"/><text x="{X(0)-8}" y="{Y(v)+4}" font-size="12" fill="{MUTED}" text-anchor="end">{v}</text>')
s.append(f'<text x="{(X(0)+X(xmax))/2}" y="{H-25}" font-size="13" fill="{MUTED}" text-anchor="middle">Sugar per 50 g (g)</text>')
s.append(f'<text transform="translate(20,{(Y(0)+Y(ymax))/2}) rotate(-90)" font-size="13" fill="{MUTED}" text-anchor="middle">Protein per 50 g (g)</text>')
LABELS = {"Barebells": "Barebells", "Trek High": "Trek High Protein", "Bio&Me": "Bio&Me",
          "Nakd Protein": "Nākd Protein", "Veloforte Forza": "Veloforte Forza", "RXBAR": "RXBAR (US)", "KIND": "KIND Protein"}
for o in comp:
    x, y = X(min(o["sugar_50g"], xmax)), Y(min(o["protein_50g"], ymax))
    c = REAL if o["whole_food"] else POWDER
    fill = "#fcfcfb" if o["sweet"] else c
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{fill}" stroke="{c}" stroke-width="2.5"><title>{escape(o["name"])}: {o["protein_50g"]} g protein, {o["sugar_50g"]} g sugar per 50 g</title></circle>')
    lab = next((v for k, v in LABELS.items() if o["name"].startswith(k)), None)
    if lab:
        s.append(f'<text x="{x+9:.1f}" y="{y+4:.1f}" font-size="11" fill="{MUTED}">{escape(lab)}</text>')
g = out[-1]
gx, gy = X(g["sugar_50g"]), Y(g["protein_50g"])
s.append(f'<path d="M{gx},{gy-11} L{gx+3.2},{gy-3.5} L{gx+11},{gy-3.5} L{gx+4.8},{gy+1.5} L{gx+7},{gy+9.5} L{gx},{gy+4.5} L{gx-7},{gy+9.5} L{gx-4.8},{gy+1.5} L{gx-11},{gy-3.5} L{gx-3.2},{gy-3.5} Z" fill="{INK}" stroke="#fcfcfb" stroke-width="2"/>')
s.append(f'<text x="{gx+14}" y="{gy+5}" font-size="13" font-weight="bold" fill="{INK}">Graft (calculated)</text>')
# legend
lx, ly = X(13), Y(19.2)
s += [f'<circle cx="{lx}" cy="{ly}" r="6" fill="{REAL}" stroke="{REAL}" stroke-width="2.5"/><text x="{lx+12}" y="{ly+4}" font-size="12" fill="{INK}">Protein from real food (egg, dairy, nuts)</text>',
      f'<circle cx="{lx}" cy="{ly+22}" r="6" fill="{POWDER}" stroke="{POWDER}" stroke-width="2.5"/><text x="{lx+12}" y="{ly+26}" font-size="12" fill="{INK}">Protein from powders / isolates</text>',
      f'<circle cx="{lx}" cy="{ly+44}" r="6" fill="#fcfcfb" stroke="{MUTED}" stroke-width="2.5"/><text x="{lx+12}" y="{ly+48}" font-size="12" fill="{INK}">Hollow = contains sweeteners or sugar alcohols</text>']
s.append(f'<text x="{L}" y="{H-6}" font-size="10" fill="{MUTED}">Sources: brand/retailer pages Oct 2026 (02-competitors.csv; 02d WR40–WR52); RXBAR US/CA label. Sugar capped at 25 g on chart. Graft figures calculated, not lab-tested.</text>')
s.append("</svg>")
(ROOT / "16-gap-chart.svg").write_text("\n".join(s))

print(json.dumps(summary, indent=1))
for o in out:
    flags = "".join("✓" if o[k] else "✗" for k in ("protein10", "real_food", "no_sweet", "low_sugar"))
    print(f'{flags}  {o["name"]:<40} P50 {o["protein_50g"]:>5}  S50 {o["sugar_50g"]:>5}  sweet={o["sweet"]}')
