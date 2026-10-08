"""Single-bar test recipes (final set, 8 Oct): Chocolate Peanut Butter, Vanilla, Banana Bread.
T20-sized: ~20 g protein, ~28-31 g carbs, <=8 g sugar, ~5-8 g fat, ~260-280 kcal. Uses the ingredient database in 04-nutrition.py. Calculated, not lab-tested.
Run: python3 research/04d_recovery_calcs.py"""
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ING = runpy.run_path(str(ROOT / "04-nutrition.py"), run_name="lib")["ING"]
# Pure vanilla extract (not "vanilla flavouring"): USDA FDC 'Vanilla extract' ~12.7 g sugars/100 g
PRICE = runpy.run_path(str(ROOT / "04-costing.py"), run_name="lib")["PRICE"]  # £/kg retail, first value
EXTRA_PRICE = {"vanilla_extract": 60.0}  # [ASSUMPTION] ~£3 per 50 ml supermarket vanilla extract
ING.setdefault("vanilla_extract", dict(label="vanilla extract", p=0.1, c=12.7, s=12.7, fb=0.0, f=0.1, sf=0.0, salt=0.02, allergen=None))

# Spec (Ewan, 8 Oct): back to T20 size. >=20 g protein, >=25 g carbs, <=8 g sugar, <=9 g fat, <=285 kcal
SPEC = dict(p_min=20, c_min=25, s_max=8, f_max=9, kcal_max=285)
# Egg whites are separated from normal boxed eggs. A whole-egg-only version was tested in code and came out at
# ~275-300 kcal with 8-11 g fat, over spec, so whites stay (Ewan's rule: keep whites if needed for the macros).
BARS = {
    "Chocolate Peanut Butter": dict(egg_white_fresh=65, quark=45, oat_bran=25, rolled_oats=12, peanut_butter=7,
                                    cocoa=4, chia=2, honey=6, sea_salt=0.2),
    "Vanilla": dict(egg_white_fresh=60, egg_fresh=15, quark=45, oat_bran=27, rolled_oats=15, chia=2, honey=6,
                    vanilla_extract=3, sea_salt=0.15),
    "Banana Bread": dict(egg_white_fresh=60, egg_fresh=15, quark=45, oat_bran=25, rolled_oats=15, banana=35, chia=2,
                         cinnamon=0.5, sea_salt=0.15),
    # whole-egg comparison (not a test recipe): shows why whites are kept
    "(comparison) Choc PB, whole egg only": dict(egg_fresh=58, quark=80, rolled_oats=15, oat_bran=15,
                                                  peanut_butter=5, honey=5, cocoa=4, sea_salt=0.2),
}
FAST_SUGAR_SOURCES = ("honey", "banana")


def calc(g):
    t = {k: sum(ING[i][k] * v / 100 for i, v in g.items()) for k in ("p", "c", "s", "fb", "f", "sf", "salt")}
    t["kcal"] = 4 * t["p"] + 4 * t["c"] + 9 * t["f"] + 2 * t["fb"]
    t["fast_sugar"] = sum(ING[i]["s"] * g.get(i, 0) / 100 for i in FAST_SUGAR_SOURCES)
    t["protein_per_100kcal"] = t["p"] / t["kcal"] * 100
    t["batter_g"] = sum(g.values())
    t["cost_gbp"] = sum((PRICE[i][0] if i in PRICE else EXTRA_PRICE[i]) * v / 1000 for i, v in g.items())
    return {k: round(v, 2 if k == "cost_gbp" else 1) for k, v in t.items()}


rows = {name: calc(g) for name, g in BARS.items()}
print("| Bar | Protein | Carbs | Sugar | of which honey/banana | Fat | Sat fat | Fibre | Salt | kcal | Batter | Ingredient cost |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")
for name, r in rows.items():
    print(f"| {name} | {r['p']} g | {r['c']} g | {r['s']} g | {r['fast_sugar']} g | {r['f']} g | {r['sf']} g | "
          f"{r['fb']} g | {r['salt']} g | {r['kcal']:.0f} | {r['batter_g']:.0f} g | £{r['cost_gbp']:.2f} |")
    if name.startswith("(comparison)"):
        continue
    assert r["p"] >= SPEC["p_min"] and r["c"] >= SPEC["c_min"], name
    assert r["s"] <= SPEC["s_max"] and r["f"] <= SPEC["f_max"] and r["kcal"] <= SPEC["kcal_max"], name

# ---- label data for packaging (05-brand/build_packaging.py) ----
# Baked weight is ESTIMATED with the T20 bake-loss model in 04-nutrition.py (36% of batter lost as steam)
# until Ewan's tin weights arrive. Per-100 g values depend on it; per-bar values do not.
BAKE_LOSS = 0.36
QUID = {"peanut_butter", "cocoa", "vanilla_extract", "banana", "honey"}  # characterising ingredients
LABEL_EXTRA = {"vanilla_extract": "vanilla extract", "sea_salt": "salt"}
label = {}
for name, g in BARS.items():
    if name.startswith("(comparison)"):
        continue
    r = rows[name]
    batter = sum(g.values())
    baked = batter * (1 - BAKE_LOSS)
    parts = []
    for i, v in sorted(g.items(), key=lambda kv: -kv[1]):
        lab = LABEL_EXTRA.get(i, ING[i]["label"])
        parts.append(f"{lab} ({v / batter * 100:.0f}%)" if i in QUID else lab)
    ingredients = ", ".join(parts)
    ingredients = ingredients[0].upper() + ingredients[1:] + "."
    allergens = sorted({ING[i]["allergen"] for i in g if ING.get(i, {}).get("allergen")})
    per_bar = dict(r, kj=17 * r["p"] + 17 * r["c"] + 37 * r["f"] + 8 * r["fb"], weight=round(baked))
    per_100 = {k: per_bar[k] / baked * 100 for k in ("p", "c", "s", "fb", "f", "sf", "salt", "kcal", "kj")}
    label[name] = dict(ingredients=ingredients, allergens=allergens, baked_g_estimate=round(baked),
                       per_bar=per_bar, per_100g={k: round(v, 2) for k, v in per_100.items()},
                       protein_pct_energy=round(4 * r["p"] / r["kcal"] * 100, 1))
    assert label[name]["protein_pct_energy"] >= 20, name  # 'high protein' claim threshold

(ROOT / "research" / "04d_recovery_output.json").write_text(
    json.dumps({"spec": SPEC, "bake_loss_estimate": BAKE_LOSS, "bars": BARS, "per_bar": rows, "label": label}, indent=2))
