"""Rough segment sizing for UK women ~45-60 (secondary research, 12 Oct 2026).
Every input is tagged. These are ORDER-OF-MAGNITUDE estimates, not a market size.
Run: python3 research/13_women_segment_numbers.py"""

WOMEN_45_60_UK = 7_244_488      # EVIDENCE: ONS FOI, mid-2019 estimate, females aged 45-60, UK (W2)
ACTIVE_SHARE_WOMEN = 0.61       # EVIDENCE: Sport England Active Lives Nov 22-23, all adult women "active" (W3); not age-specific
GYM_MEMBER_45_54 = 0.29         # EVIDENCE: Total Fitness/YouGov-style poll 2025, women 45-54 gym members (W8; operator-commissioned)
NORTH_EAST_SHARE = 0.039        # ASSUMPTION: North East ~2.7m of ~69m UK population (~3.9%)
DURHAM_SHARE_OF_NE = 0.20       # ASSUMPTION: County Durham ~0.52m of ~2.7m North East (~20%)

active = WOMEN_45_60_UK * ACTIVE_SHARE_WOMEN
gym = WOMEN_45_60_UK * GYM_MEMBER_45_54
ne_active = active * NORTH_EAST_SHARE
durham_active = ne_active * DURHAM_SHARE_OF_NE

rows = [
    ("UK women aged 45-60", WOMEN_45_60_UK),
    ("...of whom 'active' (150+ min/week, all-women rate applied)", active),
    ("...of whom gym/health-club members (45-54 rate applied)", gym),
    ("North East, active women 45-60 (estimate)", ne_active),
    ("County Durham, active women 45-60 (estimate)", durham_active),
]
print("| Step | Estimate |\n|---|---|")
for name, v in rows:
    print(f"| {name} | ~{v/1e6:.2f} m |" if v >= 1e6 else f"| {name} | ~{v:,.0f} |")
