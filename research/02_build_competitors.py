#!/usr/bin/env python3
"""Builds 02-competitors.csv (with derived price/protein metrics) and
02-positioning-map.html from research/02_competitors_raw.csv plus our concept
bar from research/04_nutrition_output.json.

Run from the repo root:  python3 research/02_build_competitors.py
"""

import csv
import json
from pathlib import Path

RAW = Path("research/02_competitors_raw.csv")
OURS = Path("research/04_nutrition_output.json")


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


rows = list(csv.DictReader(RAW.open()))
for r in rows:
    p, c, w, price, kcal = (num(r[k]) for k in ("protein_g", "carbs_g", "weight_g", "price_gbp", "kcal"))
    r["price_per_g_protein"] = f"{price / p:.3f}" if price and p else ""
    r["price_per_100g"] = f"{price / w * 100:.2f}" if price and w else ""
    r["carb_to_protein"] = f"{c / p:.1f}" if c and p else ""
    r["protein_pct_energy"] = f"{4 * p / kcal * 100:.0f}" if p and kcal else ""

fields = list(rows[0].keys())
with open("02-competitors.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

# ---------------------------------------------------------------- chart data
ours = json.loads(OURS.read_text())["A_cocoa_peanut"]
pts = []
for r in rows:
    p, c, sg = num(r["protein_g"]), num(r["carbs_g"]), num(r["sugars_g"])
    if p is None or sg is None:
        continue
    pts.append(dict(id=r["id"], name=f"{r['brand']} {r['product']}", p=p, c=c, s=sg, poly=num(r["polyols_g"]),
                    proc=r["processing"], fmt="other" if r["group"] == "substitute" else "bar",
                    w=num(r["weight_g"]), kcal=num(r["kcal"]), fb=num(r["fibre_g"]),
                    price=num(r["price_gbp"]), ppg=num(r["price_per_g_protein"])))
pts.append(dict(id="ours", name="fettle Cocoa & Peanut (kitchen bake, calculated)", p=round(ours["per_bar"]["p"], 1),
                c=round(ours["per_bar"]["c"], 1), s=round(ours["per_bar"]["s"], 1), poly=0, proc="ours", fmt="bar",
                w=round(ours["per_bar"]["weight"]), kcal=round(ours["per_bar"]["kcal"]),
                fb=round(ours["per_bar"]["fb"], 1), price=2.75, ppg=round(2.75 / ours["per_bar"]["p"], 3)))

html = Path("research/02_map_template.html").read_text().replace("/*DATA*/[]", json.dumps(pts))
Path("02-positioning-map.html").write_text(html)
print(f"{len(rows)} rows → 02-competitors.csv; {len(pts)} points → 02-positioning-map.html")
for r in sorted(rows, key=lambda r: num(r["price_per_g_protein"]) or 99):
    if r["price_per_g_protein"]:
        print(f"  {r['brand']:<18} {r['product'][:34]:<34} £/g protein {r['price_per_g_protein']}")
