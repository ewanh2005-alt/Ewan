#!/usr/bin/env python3
"""Pilot budget for Weeks 5-13 against a £1,000 total (Phase 7).
Run after 04-costing.py:  python3 07-budget.py"""
import json
from pathlib import Path

C = json.loads(Path("research/04_costing_summary.json").read_text())
N = json.loads(Path("research/04_nutrition_output.json").read_text())
BUDGET = 1000.0

bars_per_kg = N["A_cocoa_peanut"]["bars_per_kg"]
avg_ing_per_bar = sum(C[k]["pilot"]["ingredients"] for k in ("A_cocoa_peanut", "B_raspberry_almond", "C_honey_oat_salt")) / 3
proto_batches = 3 * 4                      # 3 flavours x 4 kitchen rounds, 1 kg each
pilot_bars = 250                           # 2 partners x ~125 bars
hero_unit = C["A_cocoa_peanut"]["pilot"]["unit_cost"]

items = [
    ("Prototype ingredients (12 × 1 kg batches)", proto_batches * bars_per_kg * avg_ing_per_bar, "calc from 04-costing"),
    ("Pilot bars incl. packaging (250 × hero unit cost)", pilot_bars * hero_unit, "calc from 04-costing"),
    ("Lab nutrition analysis, 1 sample", 150, "[ASSUMPTION] get 2 quotes"),
    ("Water activity / shelf-life test", 40, "[ASSUMPTION]"),
    ("Commercial kitchen hire (4 sessions × £15/h × 3 h)", 4 * 15 * 3, "[ASSUMPTION] community/church kitchen rates vary"),
    ("Food hygiene Level 2 (online)", 15, "[EVIDENCE: £10-25, P12]"),
    ("Public + product liability insurance (pilot)", 120, "[ASSUMPTION] PL from ~£57/yr (P13); product liability adds"),
    ("Segmented moulds, scales, thermometer", 60, "[ASSUMPTION]"),
    ("Label printing (allergen-compliant stickers)", 30, "[ASSUMPTION]"),
    ("Taste-test materials + competitor bars for blind test", 40, "[ASSUMPTION] ~10 competitor bars"),
    ("Survey / interview incentive (prize draw)", 30, "[ASSUMPTION]"),
]
subtotal = sum(v for _, v, _ in items)
contingency = 0.10 * subtotal
total = subtotal + contingency
revenue = 200 * 2.50  # [ASSUMPTION] 200 of 250 pilot bars sold at an average £2.50 (incl. Squad Box discount)

rows = ["| Item | £ | Basis |", "|---|---|---|"]
rows += [f"| {n} | {v:.0f} | {b} |" for n, v, b in items]
rows += [f"| Contingency (10%) | {contingency:.0f} | |", f"| **Total spend** | **{total:.0f}** | Budget £{BUDGET:.0f} → {'within' if total <= BUDGET else 'OVER'} by £{abs(BUDGET - total):.0f} |",
         f"| Pilot sales (offset) | −{revenue:.0f} | [ASSUMPTION] 200 bars × £2.50 |", f"| **Net cost** | **{total - revenue:.0f}** | |"]
Path("research/07_budget_table.md").write_text("\n".join(rows) + "\n")
print("\n".join(rows))
