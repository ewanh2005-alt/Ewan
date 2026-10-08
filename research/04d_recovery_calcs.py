"""Single-bar RECOVERY recipes for the hard-training athlete (post-training / post-competition).
Whole eggs only (no separated whites), quark for extra protein, oats for carbs, a little honey/banana
for fast sugar. Uses the ingredient database in 04-nutrition.py. Calculated, not lab-tested.
Run: python3 research/04d_recovery_calcs.py"""
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ING = runpy.run_path(str(ROOT / "04-nutrition.py"), run_name="lib")["ING"]
# Pure vanilla extract (not "vanilla flavouring"): USDA FDC 'Vanilla extract' ~12.7 g sugars/100 g
PRICE = runpy.run_path(str(ROOT / "04-costing.py"), run_name="lib")["PRICE"]  # £/kg retail, first value
EXTRA_PRICE = {"vanilla_extract": 60.0}  # [ASSUMPTION] ~£3 per 50 ml supermarket vanilla extract
ING.setdefault("vanilla_extract", dict(p=0.1, c=12.7, s=12.7, fb=0.0, f=0.1, sf=0.0, salt=0.02))

# Recovery spec: >=20 g protein, >=35 g carbs, <=10 g sugar, <=15 g fat
SPEC = dict(p_min=20, c_min=35, s_max=10, f_max=15)
BARS = {
    "R1 Chocolate Peanut Butter": dict(egg_fresh=58, quark=75, rolled_oats=30, oat_bran=20, peanut_butter=7,
                                       honey=7, cocoa=5, sea_salt=0.2),
    "R2 Vanilla & Honey": dict(egg_fresh=58, quark=75, rolled_oats=35, oat_bran=20, honey=7, chia=2,
                               vanilla_extract=4, cinnamon=0.5, sea_salt=0.15),
    "R3 Banana & Cinnamon": dict(egg_fresh=58, quark=70, rolled_oats=30, oat_bran=20, banana=40, chia=2,
                                 cinnamon=1, sea_salt=0.15),
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
    assert r["p"] >= SPEC["p_min"] and r["c"] >= SPEC["c_min"], name
    assert r["s"] <= SPEC["s_max"] and r["f"] <= SPEC["f_max"], name
(ROOT / "research" / "04d_recovery_output.json").write_text(json.dumps({"spec": SPEC, "bars": BARS, "per_bar": rows}, indent=2))
