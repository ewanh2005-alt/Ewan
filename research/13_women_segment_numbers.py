"""Women ~40-60 segment: sizing, nutrition fit and test-budget maths (v2, 12 Oct 2026).
Every input is tagged EVIDENCE (with source ID in 02d-women-40-60-research.md) or ASSUMPTION.
These are ORDER-OF-MAGNITUDE estimates, not a market size.
Run: python3 research/13_women_segment_numbers.py"""

# ---------- 1. Segment size ----------
WOMEN_45_60_UK = 7_244_488   # EVIDENCE [WR2]: ONS FOI, mid-2019, UK females 45-60 (>5 yrs old; mid-2024 band counts = GAP)
ACTIVE_SHARE_WOMEN = 0.622   # EVIDENCE [WR8]: Active Lives Nov 2024-25, all women 16+ "active" (secondary summary; not age-specific)
GYM_MEMBER_45_54 = 0.29      # EVIDENCE [WR12]: Total Fitness poll 2025 (n=5,091), women 45-54 gym members (operator-commissioned)
STRENGTH_55_64 = 0.19        # EVIDENCE [WR11]: Scottish Health Survey 2023, women 55-64 meeting strength guideline (Scotland)
NE_SHARE = 2_760_678 / 69_281_400   # EVIDENCE [WR4, WR1]: North East / UK population mid-2024
DURHAM_F_45_54 = 32_963      # EVIDENCE [WR5]: Urbistat citing ONS mid-2024, County Durham females 45-54 (secondary; verify)

active = WOMEN_45_60_UK * ACTIVE_SHARE_WOMEN
gym = WOMEN_45_60_UK * GYM_MEMBER_45_54
strength = WOMEN_45_60_UK * STRENGTH_55_64
ne_women = WOMEN_45_60_UK * NE_SHARE              # ASSUMPTION: NE has the UK's age mix (it is slightly older, so this understates)
ne_gym = ne_women * GYM_MEMBER_45_54
durham_f_45_60 = DURHAM_F_45_54 * 16 / 10         # ASSUMPTION: 45-60 = 16 single years ~ 1.6 x the 10-year 45-54 band
durham_gym = durham_f_45_60 * GYM_MEMBER_45_54

# ---------- 2. Nutrition fit of the v6 bar ----------
BAR = dict(protein=14.6, carbs=14.0, sugar=3.8, fibre=2.1, kcal=135)  # EVIDENCE: research/04d_recovery_calcs.py v6 (average of 3 flavours, calculated not lab-tested)
BODY_KG = 70                 # ASSUMPTION: illustrative midlife woman (NHS/HSE average for women ~70-72 kg; not verified this session)
PROT_LOW, PROT_HIGH = 1.0, 1.2   # EVIDENCE [WR17, WR18, WR19]: PROT-AGE / ESPEN / ESCEO g/kg/day
RNI_G_PER_KG = 0.75          # EVIDENCE [WR16]: UK RNI
PER_MEAL_G_PER_KG = 0.4      # EVIDENCE [WR20]: Moore 2015, plateau in older MEN (no women-specific data)
FIBRE_TARGET = 30            # EVIDENCE [WR28]: SACN 2015
FIBRE_ACTUAL = 16            # EVIDENCE [WR30]: adults 19-64 ~16 g/day (secondary citation of NDNS 2019-23)
FREE_SUGAR_MAX_G = 30        # EVIDENCE [WR28]: SACN 5% energy ~ 30 g/day adults
FREE_SUGAR_IN_BAR = 2.0      # ASSUMPTION: honey + part of banana/milk; most bar sugar is lactose (not free sugar)

need_lo, need_hi = BODY_KG * PROT_LOW, BODY_KG * PROT_HIGH
rni = BODY_KG * RNI_G_PER_KG
per_meal = BODY_KG * PER_MEAL_G_PER_KG
prot_energy_pct = BAR["protein"] * 4 / BAR["kcal"] * 100
fibre_per_100g = BAR["fibre"] * 2

# ---------- 3. Price per 10 g protein (competitors, prices seen 12 Oct 2026) ----------
comp = [  # name, price GBP per item, protein g per item   EVIDENCE [WR40-WR52]
    ("fettle v6 @ £2.00", 2.00, 14.6), ("fettle v6 @ £2.50", 2.50, 14.6),
    ("Bio&Me Daily Boost (3-pack price)", 1.08, 9.2), ("Mena bar (box of 10)", 2.25, None),
    ("Trek High Protein", 2.50, 15), ("Fulfil", 2.90, 18.9), ("Barebells", 2.90, 20),
    ("Grenade", 2.70, 20), ("H&B Precision Engineered", 1.80, 21), ("KIND Protein", 2.40, 12),
    ("Nakd Protein (3-pack)", 1.10, 7.2), ("Perkier Protein", 0.60, 5.6),
    ("Graham's Protein 25 quark pot", 0.85, 25), ("Lindahls Kvarg pot", 1.25, 15),
]

# ---------- 4. Meta split test reach ----------
BUDGET = 40                  # ASSUMPTION: middle of Ewan's £30-50
CPM = 18.89                  # EVIDENCE [WR75]: SuperAds UK Meta CPM 2025 (third-party benchmark)
CPC = 1.17                   # EVIDENCE [WR75]: SuperAds UK Meta CPC 2025
SIGNUP_RATE = 0.15           # ASSUMPTION: landing page click -> waitlist sign-up (unknown; test will measure)
impressions = BUDGET / CPM * 1000
clicks = BUDGET / CPC
signups = clicks * SIGNUP_RATE

if __name__ == "__main__":
    def fmt(v): return f"~{v/1e6:.2f} m" if v >= 1e6 else f"~{v:,.0f}"
    print("## 1. Segment size\n| Step | Estimate |\n|---|---|")
    for n, v in [("UK women 45-60 (ONS 2019)", WOMEN_45_60_UK), ("...'active' (all-women rate)", active),
                 ("...gym members (45-54 rate)", gym), ("...doing strength 2x/week (55-64 Scottish rate)", strength),
                 ("North East women 45-60", ne_women), ("North East gym-member women 45-60", ne_gym),
                 ("County Durham women 45-60", durham_f_45_60), ("County Durham gym-member women 45-60", durham_gym)]:
        print(f"| {n} | {fmt(v)} |")
    print(f"\n## 2. Nutrition fit (70 kg woman)\n- Daily protein target 1.0-1.2 g/kg: {need_lo:.0f}-{need_hi:.0f} g (UK RNI {rni:.0f} g)")
    print(f"- One bar = {BAR['protein']/need_hi*100:.0f}-{BAR['protein']/need_lo*100:.0f}% of the expert target; per-meal plateau ~{per_meal:.0f} g -> one bar reaches {BAR['protein']/per_meal*100:.0f}%")
    print(f"- Protein = {prot_energy_pct:.0f}% of energy (high protein needs >=20%) -> claim OK")
    print(f"- Fibre {BAR['fibre']} g = {BAR['fibre']/FIBRE_TARGET*100:.0f}% of 30 g; gap is {FIBRE_TARGET-FIBRE_ACTUAL} g/day; {fibre_per_100g:.1f} g/100 g ('source of fibre' needs 3 g/100 g; 'high fibre' 6 g) -> 'source of fibre' possible once lab-tested")
    print(f"- Free sugar ~{FREE_SUGAR_IN_BAR} g = {FREE_SUGAR_IN_BAR/FREE_SUGAR_MAX_G*100:.0f}% of 30 g daily max [ASSUMPTION on free share]")
    print("\n## 3. Price per 10 g protein\n| Product | £/item | Protein g | £ per 10 g protein |\n|---|---|---|---|")
    for n, p, g in comp:
        print(f"| {n} | £{p:.2f} | {g if g else 'GAP'} | {'£%.2f' % (p/g*10) if g else 'GAP'} |")
    print(f"\n## 4. Meta test (£{BUDGET})\n- ~{impressions:,.0f} impressions, ~{clicks:.0f} clicks (~{clicks/2:.0f} per arm), ~{signups:.0f} sign-ups at {SIGNUP_RATE:.0%} [ASSUMPTION]")
    print("- Too small for statistical significance: treat as directional only")

    assert 4_000_000 < active < 5_000_000
    assert 20 <= prot_energy_pct, "high-protein claim threshold"
    assert 3 <= fibre_per_100g < 6, "source of fibre yes, high fibre no"
