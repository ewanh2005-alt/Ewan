#!/usr/bin/env python3
"""Concept bar nutrition calculator (Phase 4).

Run:  python3 04-nutrition.py
Writes: 04-nutrition-tables.md and research/04_nutrition_output.json

INGREDIENT VALUES — read this before trusting any number
---------------------------------------------------------
Values are per 100 g, using UK labelling conventions (carbohydrate = available
carbohydrate; fibre = AOAC method). They are TYPICAL values of the kind found
in UK CoFID (McCance & Widdowson's Composition of Foods Integrated Dataset 2021)
and USDA FoodData Central (SR Legacy), cross-checked against typical UK
retail pack labels. Neither database could be opened from this environment,
so every value is tagged [ASSUMPTION] until checked against:
  1. the supplier's specification sheet for the exact product bought, then
  2. one lab analysis of the finished bar (budgeted in Phase 7).
A GB label may be based on the manufacturer's analysis, a calculation from
known average values, or generally established data. Calculation is legal,
but must use the real ingredients' data.
"""

import json
from pathlib import Path

# ---------------------------------------------------------------- ingredients
# p=protein c=available carbohydrate s=sugars fb=fibre f=fat sf=saturates
# salt in g/100 g. allergen = one of the 14 UK allergens (None if none).
ING = {
    "rolled_oats":   dict(label="**oats**", p=11.0, c=60.0, s=1.1, fb=9.0, f=8.0, sf=1.5, salt=0.01, allergen="cereals containing gluten (oats)",
                          ref="CoFID 'Oats, porridge oats/rolled, raw' / typical UK pack"),
    "oat_bran":      dict(label="**oat** bran", p=17.0, c=49.0, s=1.5, fb=15.0, f=7.5, sf=1.4, salt=0.01, allergen="cereals containing gluten (oats)",
                          ref="USDA FDC 'Oat bran, raw' / Mornflake Oatbran pack (typical)"),
    "dates":         dict(label="dates", p=2.5, c=67.0, s=63.0, fb=8.0, f=0.4, sf=0.0, salt=0.0, allergen=None,
                          ref="USDA FDC 'Dates, deglet noor' (available carbs = total - fibre)"),
    "smp":           dict(label="skimmed **milk** powder", p=36.0, c=52.0, s=52.0, fb=0.0, f=0.8, sf=0.5, salt=1.38, allergen="milk",
                          ref="CoFID 'Milk, dried, skimmed' (sodium ~0.55 g/100 g)"),
    "egg_white":     dict(label="dried **egg** white", p=80.0, c=4.5, s=4.5, fb=0.0, f=0.3, sf=0.0, salt=3.2, allergen="egg",
                          ref="USDA FDC 'Egg, white, dried' (sodium ~1.28 g/100 g)"),
    "peanut_butter": dict(label="**peanut** butter", p=25.0, c=13.0, s=5.0, fb=7.0, f=50.0, sf=9.0, salt=0.02, allergen="peanuts",
                          ref="Typical UK 100% peanut butter label (e.g. Meridian)"),
    "ground_almond": dict(label="ground **almonds**", p=21.0, c=6.9, s=4.2, fb=7.4, f=55.8, sf=4.4, salt=0.01, allergen="nuts (almond)",
                          ref="CoFID 'Almonds, ground' / typical UK pack"),
    "egg_fresh":     dict(label="free-range **eggs**", p=12.6, c=0.2, s=0.2, fb=0.0, f=9.0, sf=2.5, salt=0.35, w=75, allergen="egg",
                          ref="CoFID 'Eggs, chicken, whole, raw' (large egg ~58 g without shell)"),
    "milk_semi":     dict(label="semi-skimmed **milk**", p=3.5, c=4.7, s=4.7, fb=0.0, f=1.7, sf=1.1, salt=0.11, w=89, allergen="milk",
                          ref="CoFID 'Milk, semi-skimmed, pasteurised'"),
    "banana":        dict(label="banana", p=1.1, c=20.2, s=12.2, fb=2.6, f=0.3, sf=0.1, salt=0.0, w=75, allergen=None,
                          ref="USDA FDC 'Bananas, raw' (available carbs = total - fibre)"),
    "peanuts":       dict(label="**peanuts**", p=25.8, c=7.6, s=4.0, fb=8.5, f=49.0, sf=8.7, salt=0.01, w=2, allergen="peanuts",
                          ref="CoFID 'Peanuts, plain' / typical unsalted pack"),
    "raspberries":   dict(label="raspberries", p=1.2, c=5.4, s=4.4, fb=6.5, f=0.7, sf=0.0, salt=0.0, w=86, allergen=None,
                          ref="USDA FDC 'Raspberries, raw' (frozen, unsweetened)"),
    "puffed_rice":   dict(label="puffed brown rice", p=7.0, c=81.0, s=0.7, fb=3.0, f=2.0, sf=0.4, salt=0.01, allergen=None,
                          ref="Rude Health / Nature's Store unsweetened puffed brown rice labels"),
    "pumpkin_seeds": dict(label="pumpkin seeds", p=30.0, c=6.0, s=1.4, fb=6.0, f=46.0, sf=8.7, salt=0.02, allergen=None,
                          ref="Typical UK pumpkin seed pack label"),
    "honey":         dict(label="honey", p=0.4, c=82.0, s=82.0, fb=0.0, f=0.0, sf=0.0, salt=0.01, allergen=None,
                          ref="CoFID 'Honey'"),
    "cocoa":         dict(label="cocoa powder", p=20.0, c=12.0, s=0.5, fb=28.0, f=21.0, sf=12.7, salt=0.1, allergen=None,
                          ref="Typical UK unsweetened cocoa powder label"),
    "fd_raspberry":  dict(label="freeze-dried raspberries", p=7.0, c=37.0, s=30.0, fb=25.0, f=3.0, sf=0.2, salt=0.01, allergen=None,
                          ref="Typical freeze-dried raspberry label (wide variation; check spec)"),
    "sea_salt":      dict(label="sea salt", p=0.0, c=0.0, s=0.0, fb=0.0, f=0.0, sf=0.0, salt=100.0, allergen=None,
                          ref="—"),
    "cinnamon":      dict(label="cinnamon", p=4.0, c=27.0, s=2.2, fb=53.0, f=1.2, sf=0.3, salt=0.03, allergen=None,
                          ref="USDA FDC 'Spices, cinnamon, ground'"),
}

# -------------------------------------------------------------------- recipes
# grams per bar. Order = descending weight for the ingredients list.
RECIPES = {
    # v3 KITCHEN RECIPES (8 Oct 2026): what Ewan will actually bake. Supermarket ingredients only:
    # fresh eggs, fresh milk, oats, nuts/seeds, banana, cocoa. No powders, no sweeteners, no added sugar.
    # g = grams per BATCH (one 20 x 20 cm tin). loss = share of batter weight lost as steam in the oven
    # [ASSUMPTION 24%: a firm bake; weigh the tray before and after baking to replace this]. bar = cut weight (g).
    "A_cocoa_peanut": dict(
        name="Cocoa & Peanut", role="Hero flavour (v3 kitchen bake)", batch=True, loss=0.24, bar=90,
        quid=["peanuts", "peanut_butter", "cocoa"],
        g=dict(rolled_oats=320, egg_fresh=348, banana=130, peanut_butter=80, peanuts=60, milk_semi=50, cocoa=25)),
    "B_raspberry_almond": dict(
        name="Raspberry & Almond", role="Fruity flavour (v3 kitchen bake)", batch=True, loss=0.24, bar=90,
        quid=["raspberries", "ground_almond"],
        g=dict(rolled_oats=320, egg_fresh=348, banana=110, raspberries=100, ground_almond=100, milk_semi=50)),
    "C_oat_cinnamon": dict(
        name="Toasted Oat & Cinnamon", role="Nut-free recipe (v3 kitchen bake)", batch=True, loss=0.24, bar=90,
        quid=["rolled_oats", "cinnamon"],
        g=dict(rolled_oats=330, egg_fresh=348, banana=130, pumpkin_seeds=90, milk_semi=60, cinnamon=6)),
    # ---- comparisons (not for the pilot) ----
    "SH_cocoa_peanut": dict(
        name="Shelf-stable route (v2: same foods, dried: milk powder + egg-white powder)", role="Comparison: co-man scale-up route",
        quid=["peanut_butter", "cocoa"],
        g=dict(rolled_oats=26.0, egg_white=14.0, puffed_rice=10.0, peanut_butter=9.0, oat_bran=6.0,
               smp=6.0, dates=6.0, cocoa=3.0)),
    "V1_cocoa_peanut": dict(
        name="v1 Cocoa & Peanut (7 Oct, superseded: 23 g sugar)", role="Comparison only",
        quid=["peanut_butter", "cocoa"],
        g=dict(dates=20.0, rolled_oats=14.0, smp=12.0, egg_white=12.0, oat_bran=8.0,
               peanut_butter=8.0, honey=4.0, cocoa=2.0)),
    "S_strict_wholefood": dict(
        name="Strict whole-food variant (Cocoa & Peanut, no powders, no eggs/milk)", role="Comparison only: shows the protein ceiling",
        quid=["peanut_butter", "cocoa"],
        g=dict(dates=26.0, rolled_oats=22.0, peanut_butter=12.0, oat_bran=10.0,
               pumpkin_seeds=8.0, cocoa=2.0)),
}

# ---------------------------------------------------------- reference numbers
# "Reduced sugars" comparator = representative natural recovery bars, per 100 g
# [EVIDENCE: 02-competitors.csv] Veloforte Forza 27.6 g sugar / 254 kcal per 70 g; Styrkr BAR+ 28.4 g / 285 kcal per 74 g
COMPARATOR = dict(s=(27.6 / 70 + 28.4 / 74) / 2 * 100, kcal=(254 / 70 + 285 / 74) / 2 * 100)
RI = dict(kj=8400, kcal=2000, f=70, sf=20, c=260, s=90, p=50, salt=6)  # GB/EU adult RIs
# FSA front-of-pack traffic lights for foods, per 100 g: (low <=, high >)
TRAFFIC = dict(f=(3.0, 17.5), sf=(1.5, 5.0), s=(5.0, 22.5), salt=(0.3, 1.5))


def totals(grams):
    t = dict(p=0.0, c=0.0, s=0.0, fb=0.0, f=0.0, sf=0.0, salt=0.0)
    for ing, g in grams.items():
        for k in t:
            t[k] += ING[ing][k] * g / 100.0
    # GB energy conversion factors (Reg. 1169/2011 Annex XIV as retained)
    t["kj"] = 17 * t["p"] + 17 * t["c"] + 37 * t["f"] + 8 * t["fb"]
    t["kcal"] = 4 * t["p"] + 4 * t["c"] + 9 * t["f"] + 2 * t["fb"]
    t["weight"] = sum(grams.values())
    return t


WATER_DEFAULT = dict(rolled_oats=9, oat_bran=7, dates=21, smp=3.5, egg_white=7, peanut_butter=1, ground_almond=4,
                     pumpkin_seeds=5, honey=17, cocoa=3, fd_raspberry=3, sea_salt=0, cinnamon=10, puffed_rice=5)


def recipe_totals(r):
    """Per-bar nutrition. Batch recipes: nutrients of the whole batter, divided by the number of
    bars of r['bar'] g cut from the baked weight (batter minus evaporated water)."""
    t = totals(r["g"])
    if not r.get("batch"):
        return t
    batter = t["weight"]
    water = sum(ING[i].get("w", WATER_DEFAULT.get(i, 5)) * g / 100 for i, g in r["g"].items())
    lost = batter * r["loss"]
    if lost > water:
        raise ValueError(f"{r['name']}: bake loss exceeds the water in the batter")
    baked = batter - lost
    n = baked / r["bar"]
    out = {k: v / n for k, v in t.items()}
    out.update(weight=r["bar"], bars=n, batter=batter, baked=baked, moisture_pct=(water - lost) / baked * 100)
    return out


def bar_inputs(r):
    """Ingredient grams that go into one bar (batch grams / bars)."""
    if not r.get("batch"):
        return dict(r["g"])
    n = recipe_totals(r)["bars"]
    return {i: g / n for i, g in r["g"].items()}


def per100(t):
    k = 100.0 / t["weight"]
    skip = ("weight", "bars", "batter", "baked", "moisture_pct")
    return {key: (v * k if key not in skip else v) for key, v in t.items() if key != "weight"} | {"weight": 100.0}


def claims(t, h):
    """GB nutrition-claim checks (Reg. 1924/2006 Annex, retained)."""
    pe = 4 * t["p"] / t["kcal"] * 100  # % energy from protein
    fib100kcal = t["fb"] / t["kcal"] * 100
    out = {
        "protein_pct_energy": round(pe, 1),
        "source_of_protein (>=12% energy)": pe >= 12,
        "high_protein (>=20% energy)": pe >= 20,
        "fibre_g_per_100g": round(h["fb"], 1),
        "fibre_g_per_100kcal": round(fib100kcal, 2),
        "source_of_fibre (>=3 g/100 g or >=1.5 g/100 kcal)": h["fb"] >= 3 or fib100kcal >= 1.5,
        "high_fibre (>=6 g/100 g or >=3 g/100 kcal)": h["fb"] >= 6 or fib100kcal >= 3,
        "low_sugars (<=5 g/100 g)": h["s"] <= 5.0,
        "reduced_sugars_vs_natural_recovery_bars (>=30% less sugar AND energy <= comparator)":
            h["s"] <= 0.7 * COMPARATOR["s"] and h["kcal"] <= COMPARATOR["kcal"],
        "sugar_reduction_vs_comparator_pct": round((1 - h["s"] / COMPARATOR["s"]) * 100),
        # Health claims: conditions of use (Reg. 432/2012 and 2015/7, retained)
        "protein_muscle_claim_condition (source of protein)": pe >= 12,
        "carb_recovery_claim_condition (metabolisable carbs, no polyols)": True,
        "carb_recovery_claim_note": "Allowed only with the mandatory 4 g/kg wording and for adults after glycogen-depleting exercise",
    }
    return out


def npm_score(h, fvn_points=0):
    """UK 2004/05 Nutrient Profiling Model (the HFSS test). Score >= 4 = 'less healthy' (food).
    fvn_points = fruit/veg/nut credit; conservatively 0 here (dates + nuts are ~30-35% of
    the bar; the credit needs >40%) [ASSUMPTION: check the FVN rules for dried fruit]."""
    energy = min(10, sum(h["kj"] > t for t in [335 * i for i in range(1, 11)]))
    sat = min(10, sum(h["sf"] > t for t in range(1, 11)))
    sugars = min(10, sum(h["s"] > t for t in [4.5 * i for i in range(1, 11)]))
    sodium_mg = h["salt"] / 2.5 * 1000
    sodium = min(10, sum(sodium_mg > t for t in [90 * i for i in range(1, 11)]))
    a = energy + sat + sugars + sodium
    fibre = sum(h["fb"] > t for t in (0.9, 1.9, 2.8, 3.7, 4.7))  # AOAC thresholds
    protein = sum(h["p"] > t for t in (1.6, 3.2, 4.8, 6.4, 8.0))
    if a >= 11 and fvn_points < 5:
        score = a - (fibre + fvn_points)  # protein can't be counted
    else:
        score = a - (fibre + fvn_points + protein)
    return dict(a_points=a, fibre_points=fibre, protein_points=protein, fvn_points=fvn_points,
                score=score, hfss_less_healthy=score >= 4)


def traffic(h):
    res = {}
    for k, (lo, hi) in TRAFFIC.items():
        res[k] = "LOW (green)" if h[k] <= lo else ("HIGH (red)" if h[k] > hi else "MEDIUM (amber)")
    return res


def rnd(key, v):
    """Simplified EU/GB labelling tolerance-guidance rounding."""
    if key in ("kj", "kcal"):
        return f"{v:.0f}"
    if key == "salt":
        return f"{v:.2f}" if v < 1 else f"{v:.1f}"
    if v >= 10:
        return f"{v:.0f}"
    if v < 0.5:
        return "<0.5"
    return f"{v:.1f}"


def allergens(grams):
    return sorted({ING[i]["allergen"] for i in grams if ING[i]["allergen"]})


def ingredients_line(recipe):
    g = recipe["g"]
    total = sum(g.values())
    parts = []
    for ing, grams in sorted(g.items(), key=lambda kv: -kv[1]):
        lab = ING[ing]["label"]
        if ing in recipe["quid"]:
            lab += f" ({grams / total * 100:.0f}%)"
        parts.append(lab)
    line = ", ".join(parts)
    return line[0].upper() + line[1:] + "."


def table_md(t, h):
    rows = [("Energy", "kj", "kJ"), ("", "kcal", "kcal"), ("Fat", "f", "g"), ("of which saturates", "sf", "g"),
            ("Carbohydrate", "c", "g"), ("of which sugars", "s", "g"), ("Fibre", "fb", "g"),
            ("Protein", "p", "g"), ("Salt", "salt", "g")]
    out = [f"| Typical values | Per 100 g | Per bar ({t['weight']:.0f} g) | %RI* per bar |", "|---|---|---|---|"]
    for name, k, unit in rows:
        ri = f"{t[k] / RI[k] * 100:.0f}%" if k in RI else ""
        if k == "kj":
            out.append(f"| Energy | {rnd(k, h[k])} kJ / {rnd('kcal', h['kcal'])} kcal | "
                       f"{rnd(k, t[k])} kJ / {rnd('kcal', t['kcal'])} kcal | {t['kcal'] / RI['kcal'] * 100:.0f}% |")
            continue
        if k == "kcal":
            continue
        out.append(f"| {name} | {rnd(k, h[k])} {unit} | {rnd(k, t[k])} {unit} | {ri} |")
    out.append("\n\\*Reference intake of an average adult (8400 kJ / 2000 kcal).")
    return "\n".join(out)


def main():
    results = {}
    md = ["# 04 — Nutrition tables (generated by `04-nutrition.py`; do not edit by hand)\n",
          "Ingredient values are typical CoFID/USDA-type values (see script header). "
          "**All figures are `[ASSUMPTION]` until supplier specs and one lab test confirm them.**\n"]
    for key, r in RECIPES.items():
        t = recipe_totals(r)
        h = per100(t)
        cl = claims(t, h)
        tl = traffic(h)
        npm = npm_score(h)
        al = allergens(r["g"])
        results[key] = dict(name=r["name"], role=r["role"], grams=r["g"], per_bar=t, per_100g=h,
                            claims=cl, traffic_lights_per_100g=tl, npm=npm, allergens=al,
                            ingredients=ingredients_line(r),
                            bar_inputs={i: round(g, 1) for i, g in bar_inputs(r).items()},
                            batch=r.get("batch", False),
                            bars_per_batch=round(t.get("bars", 1000 / t["weight"]), 1))
        md.append(f"\n## {r['name']} ({r['role']})\n")
        md.append(table_md(t, h))
        md.append(f"\n**Ingredients:** {ingredients_line(r)}\n")
        md.append(f"**Contains (14 UK allergens):** {', '.join(al) if al else 'none'}\n")
        md.append("**Claim checks:**\n")
        for ck, v in cl.items():
            md.append(f"- {ck}: {'✅' if v is True else ('❌' if v is False else v)}")
        md.append("\n**FSA traffic lights (per 100 g):** " + ", ".join(f"{k} {v}" for k, v in tl.items()) + "\n")
        md.append(f"**UK nutrient profile (HFSS) score:** {npm['score']} (A {npm['a_points']}, fibre {npm['fibre_points']}, "
                  f"protein {npm['protein_points']}{' not counted' if npm['a_points'] >= 11 else ''}) → "
                  f"{'**less healthy (HFSS)**' if npm['hfss_less_healthy'] else 'not HFSS'}\n")
        if r.get("batch"):
            md.append("**Formulation:** one 20 × 20 cm tin\n")
            md.append("| Ingredient | Per tin (g) | Goes into one bar (g) | Source of values |\n|---|---|---|---|")
            for i, g in sorted(r["g"].items(), key=lambda kv: -kv[1]):
                md.append(f"| {i} | {g:.0f} | {g / t['bars']:.1f} | {ING[i]['ref']} |")
            md.append(f"\nBatter {t['batter']:.0f} g → baked {t['baked']:.0f} g (assumes {r['loss']:.0%} lost as steam; **weigh it**) → "
                      f"**{t['bars']:.1f} bars of {r['bar']} g**. Estimated moisture after baking ≈ {t['moisture_pct']:.0f}%.\n")
        else:
            md.append("**Formulation (g):** per bar / per 1 kg batch\n")
            md.append("| Ingredient | Per bar (g) | Per 1 kg batch (g) | Source of values |\n|---|---|---|---|")
            for i, g in sorted(r["g"].items(), key=lambda kv: -kv[1]):
                md.append(f"| {i} | {g:.1f} | {g / t['weight'] * 1000:.0f} | {ING[i]['ref']} |")
            md.append(f"\nOne 1 kg batch makes **{1000 / t['weight']:.1f} bars** of {t['weight']:.0f} g (before ~5% process loss).\n")
        # console summary
        print(f"{r['name']:<58} {t['weight']:.0f} g | {t['kcal']:.0f} kcal | P {t['p']:.1f} | C {t['c']:.1f} "
              f"(S {t['s']:.1f}) | Fb {t['fb']:.1f} | F {t['f']:.1f} (Sat {t['sf']:.1f}) | Salt {t['salt']:.2f} | "
              f"P%E {cl['protein_pct_energy']} | HighP {cl['high_protein (>=20% energy)']} | "
              f"HighFb {cl['high_fibre (>=6 g/100 g or >=3 g/100 kcal)']} | NPM {npm['score']}")
    Path("04-nutrition-tables.md").write_text("\n".join(md) + "\n")
    Path("research").mkdir(exist_ok=True)
    Path("research/04_nutrition_output.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
