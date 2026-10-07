#!/usr/bin/env python3
"""Cost per bar, pricing and channel margins (Phase 4).

Run:  python3 04-costing.py   (runs after 04-nutrition.py; reads its recipes)
Writes: 04-costing.csv and research/04_costing_summary.json

Every price is listed with its basis. 'pilot' = UK retail prices found by web
search on 7 Oct 2026 [EVIDENCE: see research/sources.md]. 'scale' = early
co-manufacturing bulk prices: these are [ASSUMPTION]s (roughly 35-60% of
retail, typical for trade/bulk buying) until real supplier quotes arrive.
"""

import csv
import json
import runpy
from pathlib import Path

NUT = runpy.run_path("04-nutrition.py")  # loads RECIPES, totals() without running main()
RECIPES, recipe_totals, bar_inputs = NUT["RECIPES"], NUT["recipe_totals"], NUT["bar_inputs"]

# £ per kg: (pilot retail, scale bulk, pilot basis)
PRICE = {
    # v3 kitchen ingredients (fresh, supermarket)
    "egg_fresh":     (4.74, 2.50, "Tesco 12 large free-range eggs £3.30 = 27.5p each ÷ ~58 g edible"),
    "milk_semi":     (0.68, 0.55, "Tesco semi-skimmed 4 pints (2.272 L) £1.55"),
    "banana":        (1.42, 0.90, "Tesco loose banana 17p ÷ ~120 g edible"),
    "peanuts":       (7.50, 3.50, "Tesco Jumbo Peanuts 300 g £2.25"),
    "raspberries":   (10.00, 5.00, "Tesco frozen raspberries 300 g £3.00"),
    "puffed_rice":   (8.89, 3.00, "Tesco Nature's Store puffed rice 225 g £2.00"),
    "rolled_oats":   (1.35, 0.70, "Tesco Scottish Oats 1 kg £1.35"),
    "oat_bran":      (3.13, 1.50, "Mornflake Oatbran 800 g £2.50"),
    "dates":         (6.90, 3.00, "Tesco Deglet Nour dates 500 g £3.45"),
    "smp":           (10.29, 3.50, "Tesco instant dried skimmed milk 340 g £3.50"),
    "egg_white":     (34.99, 12.00, "Myprotein egg white powder 1 kg full price £34.99 (often £24.49 on promo)"),
    "peanut_butter": (5.75, 3.50, "Meridian 100% peanut butter 1 kg £5.75"),
    "ground_almond": (13.20, 7.00, "Tesco ground almonds 500 g £6.60"),
    "pumpkin_seeds": (5.43, 3.50, "Stock & Prep pumpkin seeds 1 kg £5.43"),
    "honey":         (8.80, 4.50, "Pasieka multiflower honey 1 kg £8.80"),
    "cocoa":         (27.35, 8.00, "Sephra cocoa powder 1 kg £27.35"),
    "fd_raspberry":  (118.50, 60.00, "Greencity freeze-dried raspberries 100 g £11.85"),
    "sea_salt":      (2.00, 0.50, "[ASSUMPTION] generic sea salt"),
    "cinnamon":      (20.00, 8.00, "[ASSUMPTION] generic ground cinnamon"),
}
WASTE = {"pilot": 0.05, "scale": 0.03}            # [ASSUMPTION] process loss
PACK = {"pilot": 0.17, "scale": 0.07}             # [ASSUMPTION] pilot: bag £0.12 + printed sticker £0.05; scale: printed flow-wrap + share of case
CONVERSION = {"pilot": 0.00, "scale": 0.30}       # [ASSUMPTION] bakery/co-packer production fee per bar (quote needed)
LABOUR_IF_PAID = 12.71 / 17                        # [ASSUMPTION] NLW 2026 £12.71/h ÷ ~17 bars/h hand-made (shown, not included)

# Pricing proposal
RRP = 2.75                     # single bar, incl. VAT once registered
VAT = 0.20                     # HMRC/FTT treat sports bars as standard-rated confectionery [EVIDENCE: taxation.co.uk]
CARD_FEE = 0.0169              # [ASSUMPTION] typical card-reader fee
RETAILER_MARGIN_GYM = 0.35     # [ASSUMPTION] gym/café margin on RRP ex VAT
RETAILER_MARGIN_RETAIL = 0.40  # [ASSUMPTION] specialist/grocery margin
DISTRIBUTOR_MARGIN = 0.25      # [ASSUMPTION]


def ingredient_cost(grams, scale):
    rows, total = [], 0.0
    for ing, g in grams.items():
        price = PRICE[ing][0 if scale == "pilot" else 1]
        cost = g / 1000 * price
        total += cost
        rows.append((ing, g, price, cost))
    return rows, total


def main():
    out_rows, summary = [], {}
    for key, r in RECIPES.items():
        if key.startswith(("S_", "V1_")):
            continue  # comparison variants only
        t = recipe_totals(r)
        summary[key] = {"name": r["name"], "protein_g": round(t["p"], 1)}
        for scale in ("pilot", "scale"):
            rows, ing_total = ingredient_cost(bar_inputs(r), scale)
            for ing, g, price, cost in rows:
                basis = PRICE[ing][2] if scale == "pilot" else "[ASSUMPTION] bulk/trade price, quote needed"
                out_rows.append([r["name"], scale, ing, f"{g:.1f}", f"{price:.2f}", f"{cost:.3f}", basis])
            waste = ing_total * WASTE[scale]
            unit = ing_total + waste + PACK[scale] + CONVERSION[scale]
            out_rows += [
                [r["name"], scale, "process waste", "", "", f"{waste:.3f}", f"[ASSUMPTION] {WASTE[scale]:.0%} loss"],
                [r["name"], scale, "packaging", "", "", f"{PACK[scale]:.3f}", "[ASSUMPTION] see script"],
                [r["name"], scale, "production fee (bakery/co-packer)", "", "", f"{CONVERSION[scale]:.3f}", "[ASSUMPTION] quote needed"],
                [r["name"], scale, "TOTAL COST PER BAR", "", "", f"{unit:.3f}", "excl. labour, delivery, testing"],
            ]
            summary[key][scale] = {"ingredients": round(ing_total, 3), "unit_cost": round(unit, 3)}

    # channel economics on the hero recipe
    hero = summary["A_cocoa_peanut"]
    ex_vat = RRP / (1 + VAT)
    ch = {
        "DTC pilot (not VAT-registered, cash/card at events)": dict(price_to_brand=RRP * (1 - CARD_FEE), cost=hero["pilot"]["unit_cost"]),
        "DTC at scale (VAT-registered, multipack 4 for £10)": dict(price_to_brand=10 / 4 / (1 + VAT) * (1 - CARD_FEE), cost=hero["scale"]["unit_cost"] + 0.35),
        "Gym/café wholesale at scale": dict(price_to_brand=ex_vat * (1 - RETAILER_MARGIN_GYM), cost=hero["scale"]["unit_cost"]),
        "Retail via distributor at scale": dict(price_to_brand=ex_vat * (1 - RETAILER_MARGIN_RETAIL) * (1 - DISTRIBUTOR_MARGIN), cost=hero["scale"]["unit_cost"]),
    }
    for v in ch.values():
        v["gross_margin_gbp"] = round(v["price_to_brand"] - v["cost"], 2)
        v["gross_margin_pct"] = round((v["price_to_brand"] - v["cost"]) / v["price_to_brand"] * 100, 0)
        v["price_to_brand"] = round(v["price_to_brand"], 2)
        v["cost"] = round(v["cost"], 2)
    summary["channels_hero"] = ch
    summary["pricing"] = dict(rrp=RRP, rrp_ex_vat=round(ex_vat, 2),
                              price_per_g_protein=round(RRP / hero["protein_g"], 3),
                              labour_per_bar_if_paid=round(LABOUR_IF_PAID, 2),
                              note="DTC-at-scale cost adds £0.35/bar for postage share [ASSUMPTION]")

    with open("04-costing.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["recipe", "scale", "item", "grams_per_bar", "price_per_kg_gbp", "cost_per_bar_gbp", "basis_or_tag"])
        w.writerows(out_rows)
        w.writerow([])
        w.writerow(["CHANNEL (hero: Cocoa & Peanut)", "", "price_to_brand_gbp", "cost_gbp", "gross_margin_gbp", "gross_margin_pct", f"RRP £{RRP:.2f}"])
        for name, v in ch.items():
            w.writerow([name, "", v["price_to_brand"], v["cost"], v["gross_margin_gbp"], v["gross_margin_pct"], ""])
    Path("research/04_costing_summary.json").write_text(json.dumps(summary, indent=2))

    for k, v in summary.items():
        if k.startswith(("A_", "B_", "C_", "SH_")):
            print(f"{v['name']:<24} pilot ingredients £{v['pilot']['ingredients']:.2f} → unit £{v['pilot']['unit_cost']:.2f} | "
                  f"scale ingredients £{v['scale']['ingredients']:.2f} → unit £{v['scale']['unit_cost']:.2f}")
    for name, v in ch.items():
        print(f"{name:<55} to brand £{v['price_to_brand']:.2f}  cost £{v['cost']:.2f}  margin £{v['gross_margin_gbp']:.2f} ({v['gross_margin_pct']:.0f}%)")
    print(summary["pricing"])


if __name__ == "__main__":
    main()
