"""Single-bar T20 flavour variants (Cocoa, Cocoa & Peanut Butter, Peanut Butter & Vanilla, Vanilla).
Uses the ingredient database in 04-nutrition.py. One bar = all of the batter, so baking only
changes the weight, not the nutrients. Calculated values, not lab-tested.
Run: python3 research/04c_flavour_calcs.py"""
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ING = runpy.run_path(str(ROOT / "04-nutrition.py"), run_name="lib")["ING"]
# Pure vanilla extract (not "vanilla flavouring"): USDA FDC 'Vanilla extract' ~12.7 g sugars/100 g
ING.setdefault("vanilla_extract", dict(p=0.1, c=12.7, s=12.7, fb=0.0, f=0.1, sf=0.0, salt=0.02))

BARS = {
    "T20 Cocoa (current)": dict(egg_white_fresh=60, egg_fresh=15, quark=45, oat_bran=25, rolled_oats=15,
                                cocoa=4, chia=2, honey=3, sea_salt=0.15),
    "T20 Cocoa & Peanut Butter": dict(egg_white_fresh=65, quark=45, oat_bran=25, rolled_oats=10,
                                      peanut_butter=8, cocoa=4, chia=2, honey=3, sea_salt=0.2),
    "T20 Peanut Butter & Vanilla": dict(egg_white_fresh=65, quark=45, oat_bran=27, rolled_oats=12,
                                        peanut_butter=10, chia=2, honey=3, vanilla_extract=2, sea_salt=0.2),
    "T20 Vanilla": dict(egg_white_fresh=60, egg_fresh=15, quark=45, oat_bran=28, rolled_oats=15,
                        chia=2, honey=3, vanilla_extract=3, cinnamon=0.5, sea_salt=0.15),
}
SUGAR_CAP = 6.0


def calc(g):
    t = {k: sum(ING[i][k] * v / 100 for i, v in g.items()) for k in ("p", "c", "s", "fb", "f", "sf", "salt")}
    t["kcal"] = 4 * t["p"] + 4 * t["c"] + 9 * t["f"] + 2 * t["fb"]
    t["protein_pct_energy"] = 4 * t["p"] / t["kcal"] * 100
    t["batter_g"] = sum(g.values())
    return {k: round(v, 1) for k, v in t.items()}


rows = {name: calc(g) for name, g in BARS.items()}
print("| Bar | Protein | Carbs | Sugar | Fat | Fibre | kcal | % energy protein | Batter |")
print("|---|---|---|---|---|---|---|---|---|")
for name, r in rows.items():
    flag = "" if r["s"] <= SUGAR_CAP else " ⚠"
    print(f"| {name} | {r['p']} g | {r['c']} g | {r['s']} g{flag} | {r['f']} g | {r['fb']} g | {r['kcal']:.0f} | "
          f"{r['protein_pct_energy']:.0f}% | {r['batter_g']:.0f} g |")
    assert r["s"] <= SUGAR_CAP, name
(ROOT / "research" / "04c_flavour_output.json").write_text(json.dumps({"bars": BARS, "per_bar": rows}, indent=2))
