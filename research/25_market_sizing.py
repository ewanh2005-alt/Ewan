#!/usr/bin/env python3
"""25: First-market sizing (bottom-up) and price per 10 g protein benchmarks.

Stdlib only. Run: python3 research/25_market_sizing.py
Source IDs (M1, M2, ... and older C/WR/D IDs) are in research/sources.md.
Every input is tagged [EVIDENCE: id] or [ASSUMPTION]. Nothing here is sales data.
"""

# ---------------------------------------------------------------------------
# 1. Athlete pools
# ---------------------------------------------------------------------------
# Durham BUCS teams: 125 in the 2022/23 season [EVIDENCE: M9, Team Durham round-up, Dec 2022]
DURHAM_BUCS_TEAMS = 125
# Northumbria: "over 2,400 students" in "82 BUCS teams" [EVIDENCE: M11] -> ~29 per team
NORTHUMBRIA_STUDENTS, NORTHUMBRIA_TEAMS = 2400, 82
PER_TEAM_HIGH = NORTHUMBRIA_STUDENTS / NORTHUMBRIA_TEAMS  # evidence-derived ratio
PER_TEAM_MID = 22   # [ASSUMPTION] squads + reserves, some students in 2 teams
PER_TEAM_LOW = 15   # [ASSUMPTION] match-day squad size only

# North East BUCS teams
NE_TEAMS = {
    "Durham": 125,       # [EVIDENCE: M9] 2022/23
    "Newcastle": 81,     # [EVIDENCE: M12] 2018/19 league entries (old)
    "Northumbria": 82,   # [EVIDENCE: M11] year not stated
    "Sunderland": 20,    # [EVIDENCE: M13] "over 20 sports teams" in BUCS
    "Teesside": 20,      # [ASSUMPTION] no count found [GAP]
}
NE_BUCS_TEAMS = sum(NE_TEAMS.values())

UK_BUCS_ATHLETES = 100_000  # [EVIDENCE: D4] 2021/22 season, "100,000+"

# ---------------------------------------------------------------------------
# 2. Behaviour and price assumptions (low / mid / high)
# ---------------------------------------------------------------------------
SHARE_BUY = (0.05, 0.10, 0.20)   # [ASSUMPTION] share of athletes who buy regularly
BARS_PER_WEEK = (2, 3, 5)        # [ASSUMPTION] per buyer, training days only
PRICE = (2.00, 2.25, 2.50)       # [ASSUMPTION] price under test, GBP per bar (incl. VAT)
TERM_WEEKS = 30                  # [ASSUMPTION] Durham's three terms, ~10 weeks each

SCENARIOS = ("Low", "Mid", "High")


def pools():
    """Athlete counts for each scope, low/mid/high."""
    per_team = (PER_TEAM_LOW, PER_TEAM_MID, PER_TEAM_HIGH)
    return {
        "Durham BUCS athletes": [DURHAM_BUCS_TEAMS * p for p in per_team],
        "North East BUCS athletes": [NE_BUCS_TEAMS * p for p in per_team],
        "UK BUCS athletes": [UK_BUCS_ATHLETES] * 3,
    }


def sizing_table():
    rows = []
    for scope, counts in pools().items():
        for i, name in enumerate(SCENARIOS):
            athletes = counts[i]
            buyers = athletes * SHARE_BUY[i]
            bars_year = buyers * BARS_PER_WEEK[i] * TERM_WEEKS
            revenue = bars_year * PRICE[i]
            rows.append((scope, name, athletes, SHARE_BUY[i], buyers,
                         BARS_PER_WEEK[i], bars_year, PRICE[i], revenue))
    return rows


def print_sizing():
    print("=" * 110)
    print("FIRST-MARKET SIZING (bottom-up): athletes x share buying x bars/week x term weeks x price")
    print(f"Term weeks = {TERM_WEEKS} [ASSUMPTION]; North East BUCS teams = {NE_BUCS_TEAMS} "
          f"({', '.join(f'{k} {v}' for k, v in NE_TEAMS.items())})")
    print(f"Athletes per team: low {PER_TEAM_LOW} [A], mid {PER_TEAM_MID} [A], "
          f"high {PER_TEAM_HIGH:.1f} [E: Northumbria 2,400 / 82 teams]")
    print("-" * 110)
    print(f"{'Scope':<26}{'Case':<6}{'Athletes':>10}{'Share':>7}{'Buyers':>8}"
          f"{'Bars/wk':>8}{'Bars/yr':>11}{'Price':>7}{'Revenue/yr':>13}")
    for scope, name, ath, share, buyers, bpw, bars, price, rev in sizing_table():
        print(f"{scope:<26}{name:<6}{ath:>10,.0f}{share:>7.0%}{buyers:>8,.0f}"
              f"{bpw:>8}{bars:>11,.0f}{price:>7.2f}{'£' + format(rev, ',.0f'):>13}")
    print("-" * 110)
    # Arithmetic shown for the Durham mid case
    d = pools()["Durham BUCS athletes"][1]
    print(f"Worked example (Durham mid): {d:,.0f} athletes x {SHARE_BUY[1]:.0%} x {BARS_PER_WEEK[1]} bars"
          f" x {TERM_WEEKS} wks x £{PRICE[1]:.2f} = £{d*SHARE_BUY[1]*BARS_PER_WEEK[1]*TERM_WEEKS*PRICE[1]:,.0f}")
    print("All revenue is retail value incl. VAT (20% on sports-nutrition bars, R8), not profit.")


# ---------------------------------------------------------------------------
# 3. Price per 10 g protein (single-bar shelf prices)
# ---------------------------------------------------------------------------
# (product, grams, protein g per bar, price GBP, retailer/date, source IDs)
PRICES = [
    ("Barebells Protein Bar", 55, 20.0, 2.90, "Tesco std price (promo page Jul-Aug 2026)", "M16; C3"),
    ("Grenade Carb Killa", 60, 20.0, 2.85, "Boots (seen Oct 2026)", "M17; C1"),
    ("Fulfil Vitamin & Protein", 55, 19.5, 2.90, "Tesco/Sainsbury's (undated listing)", "M18; C4"),
    ("Myprotein Layered Bar", 60, 20.0, 2.50, "H&B RRP (7 Oct 2026)", "C5"),
    ("Nakd Protein", 45, 7.2, 1.50, "H&B single (undated)", "M19; WR47"),
    ("Trek Protein Flapjack", 50, 9.8, 1.85, "Tesco single (undated)", "M19; C15"),
    ("Bio&Me Protein Bar", 40, 9.2, 3.25 / 3, "Tesco 3-pack £3.25 (undated)", "M20; WR40"),
    ("Graze Protein Bites (1 bite)", 30, 5.1, 2.49 / 4, "Launch RSP £2.49 / 4 (old)", "C18; M21"),
    ("Graft bag bar @ £2.00", 50, 15.0, 2.00, "price under test", "[ASSUMPTION]"),
    ("Graft bag bar @ £2.50", 50, 15.0, 2.50, "price under test", "[ASSUMPTION]"),
]


def print_prices():
    print()
    print("=" * 110)
    print("PRICE BENCHMARKS: £ per bar and £ per 10 g protein (single-bar prices; promos ignored)")
    print("-" * 110)
    print(f"{'Product':<30}{'g':>4}{'Prot g':>8}{'£/bar':>7}{'£/100g':>8}{'£/10g P':>9}  {'Retailer / date':<44}{'Src'}")
    rows = sorted(PRICES, key=lambda r: r[3] / r[2])
    for name, g, prot, price, where, src in rows:
        print(f"{name:<30}{g:>4}{prot:>8.1f}{price:>7.2f}{price / g * 100:>8.2f}"
              f"{price / prot * 10:>9.2f}  {where:<44}{src}")
    big = [r for r in PRICES if r[0].split()[0] in ("Barebells", "Grenade", "Fulfil")]
    avg = sum(r[3] / r[2] * 10 for r in big) / len(big)
    print("-" * 110)
    print(f"Average £/10 g protein, Barebells + Grenade + Fulfil: £{avg:.2f}")
    print(f"Graft at £2.00 = £{2.00 / 15 * 10:.2f}/10 g; at £2.50 = £{2.50 / 15 * 10:.2f}/10 g")
    print("Note: protein figures come from labels in earlier searches (sources.md); flavours differ.")


if __name__ == "__main__":
    print_sizing()
    print_prices()
