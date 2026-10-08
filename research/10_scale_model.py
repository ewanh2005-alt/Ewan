"""Scale model: home kitchen -> Durham -> North East universities -> national weekly box.
Every input is tagged EVIDENCE (with source id from research/sources.md) or ASSUMPTION.
Run: python3 research/10_scale_model.py   (writes research/10_scale_model_table.md)"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BARS = json.loads((ROOT / "research" / "04d_recovery_output.json").read_text())["per_bar"]
ING_RETAIL = sum(BARS[k]["cost_gbp"] for k in ("Chocolate Peanut Butter", "Vanilla", "Banana Bread")) / 3  # EVIDENCE: 04-costing prices

STAGES = [
    dict(name="0. Prove it (home kitchen, Weeks 5-13)",
         bars_week=60,               # ASSUMPTION: friends, one squad trial, MMA club
         price=2.25,                 # ASSUMPTION: middle of the £2.00-2.75 test
         ing_factor=1.00,            # retail Tesco prices
         pack=0.10,                  # ASSUMPTION: greaseproof wrap + printed sticker label
         kitchen_week=0,             # registered home kitchen (EVIDENCE: home kitchens can register, R14)
         labour_hours_per_100=6,     # ASSUMPTION: Ewan's own time (unpaid at this stage)
         wage=0,
         delivery_per_bar=0.05,      # ASSUMPTION: walk/bike, cool bag + ice packs
         fixed_month=25),            # ASSUMPTION: insurance + hygiene cert spread
    dict(name="1. Durham (hired kitchen, months 1-6)",
         bars_week=400, price=2.25, ing_factor=0.85,   # ASSUMPTION: cash-and-carry / bulk eggs, oats, quark
         pack=0.15,                  # ASSUMPTION: printed compostable wrapper, small run
         kitchen_week=2 * 4 * 16,    # 2 sessions x 4 h x ~£16/h (EVIDENCE: community kitchen £13-19.20/h, P30)
         labour_hours_per_100=4, wage=12.21,  # ASSUMPTION: student helper at UK National Living Wage (21+, Apr 2025)
         delivery_per_bar=0.10,      # ASSUMPTION: squad drops + local bike/car round
         fixed_month=150),           # ASSUMPTION: insurance, lab nutrition + shelf-life tests spread, web/forms
    dict(name="2. North East universities (own unit / long-term kitchen, months 6-18)",
         bars_week=2500, price=2.25, ing_factor=0.75,  # ASSUMPTION: wholesale suppliers
         pack=0.12, kitchen_week=600,                  # ASSUMPTION: small unit rent + utilities ~£2.6k/month
         labour_hours_per_100=2.5, wage=12.21,
         delivery_per_bar=0.35,      # ASSUMPTION: weekly van round to campuses with cool boxes
         fixed_month=1500),          # ASSUMPTION: SALSA audit, insurance, ambassadors' base, software
    dict(name="3. National weekly box (co-manufacturer or bigger unit, months 18-36)",
         bars_week=10000, price=2.25, ing_factor=0.70,
         pack=0.10,
         kitchen_week=0,             # co-manufacturer charge folded into labour line below
         labour_hours_per_100=0, wage=0,
         coman_per_bar=0.45,         # ASSUMPTION: contract bakery conversion fee per bar (get quotes)
         delivery_per_bar=(7.10 + 3.00) / 12,  # EVIDENCE: next-day 2-5 kg ~£7.10 (P31) + ASSUMPTION £3 insulated box & ice; 12-bar box
         fixed_month=6000),          # ASSUMPTION: marketing, staff, certification, customer service
]

# Scenario B: price £2.50 from stage 2, and the national box charges a delivery fee
# (EVIDENCE: Simmer Eats charges ~£6.99-7.99 delivery, C40/P-notes; we assume £4.95 per 12-bar box)
SCENARIOS = {"A: £2.25, we absorb delivery": {}, "B: £2.50 from stage 2 + £4.95 box delivery fee": {
    2: dict(price=2.50), 3: dict(price=2.50, fee_per_bar=4.95 / 12)}}

rows = ["| Scenario | Stage | Bars/week | Cost per bar | Margin per bar | Weekly contribution after fixed costs | Baking hours/week |",
        "|---|---|---|---|---|---|---|"]
out = []
for scen, changes in SCENARIOS.items():
    for idx, base in enumerate(STAGES):
        s = dict(base, **changes.get(idx, {}))
        ing = ING_RETAIL * s["ing_factor"]
        labour = s["labour_hours_per_100"] * s["wage"] / 100
        kitchen = s["kitchen_week"] / s["bars_week"]
        coman = s.get("coman_per_bar", 0)
        cost = ing + s["pack"] + labour + kitchen + coman + s["delivery_per_bar"]
        margin = s["price"] + s.get("fee_per_bar", 0) - cost
        weekly = margin * s["bars_week"] - s["fixed_month"] * 12 / 52
        hours = s["labour_hours_per_100"] * s["bars_week"] / 100
        out.append(dict(scenario=scen, stage=s["name"], cost=round(cost, 2), margin=round(margin, 2), weekly=round(weekly), hours=round(hours)))
        rows.append(f"| {scen[0]} | {s['name']} | {s['bars_week']:,} | £{cost:.2f} | £{margin:.2f} | £{weekly:,.0f} | {hours:.0f} |")
table = "\n".join(rows)
print(table)
print(f"\nIngredient cost per bar at retail prices: £{ING_RETAIL:.2f} (average of the three test bars)")
(ROOT / "research" / "10_scale_model_table.md").write_text(table + "\n")
(ROOT / "research" / "10_scale_model.json").write_text(json.dumps(out, indent=2))
