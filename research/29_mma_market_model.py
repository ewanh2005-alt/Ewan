"""29: UK MMA post-training snack: TAM / SAM / SOM model + 5-test competitor scoring.

Stdlib only. Run:  python3 research/29_mma_market_model.py
Every input carries a tag: EVIDENCE (source ID in research/sources.md) or ASSUMPTION.
All money is GBP retail incl. 20% VAT (R8). Not profit.
"""

# ---------------------------------------------------------------- inputs
# (value_low, value_mid, value_high, tag)
I = {
    # --- people bases
    "england_martial_arts": (293_000, 293_000, 293_000,
        "EVIDENCE U12: Sport England Active Lives via Statista, martial arts, England, Nov 2022-23"),
    "england_to_uk": (1.00, 1.20, 1.20,
        "ASSUMPTION: England ~84% of UK population (ONS order of magnitude); low case = England only"),
    "boxing_extra": (0, 36_000, 250_000,
        "low 0; mid EVIDENCE U14 England Boxing 36,000+ members 2024/25; high ASSUMPTION 250k incl. boxing fitness (Active Lives figure masked = GAP)"),
    "bjj_extra": (0, 40_000, 40_000,
        "EVIDENCE U15 (weak): UKBJJA ~40,000 members 2025 via secondary site; overlap with martial arts count unknown"),
    "ma_schools": (8_000, 9_500, 12_000,
        "EVIDENCE U17 (weak): ~9,500 UK martial arts schools (range 8k-12k); no MMA-only count exists"),
    "share_schools_mma": (0.10, 0.15, 0.20, "ASSUMPTION: share of schools that teach MMA classes"),
    "members_per_mma_gym": (60, 100, 150, "ASSUMPTION: active members per MMA gym (Ewan to check own gym)"),
    "uk_gym_members": (12_100_000,) * 3 + ("EVIDENCE M14: Leisure DB 2026, 12.1m UK gym members",),
    "uk_protein_grocery_gbp": (225e6,) * 3 + ("EVIDENCE M1: Circana via Asian Trader 2025, bars+drinks+powders",),
    # --- behaviour
    "snacks_per_week_tam": (1, 2, 3, "ASSUMPTION: post-training snacks bought per participant per week"),
    "buyer_share_sam": (0.40, 0.50, 0.60, "ASSUMPTION: share of MMA trainees who buy a post-training snack regularly"),
    "bars_per_week_sam": (2, 3, 4, "ASSUMPTION: bars per buyer per week (double days push this up)"),
    "weeks": (48, 48, 48, "ASSUMPTION: training weeks per year"),
    "price": (2.00, 2.25, 2.50, "ASSUMPTION: price under test (Ewan, 28 brief)"),
    # --- SOM: what Ewan can reach in ~3 years
    "gyms_reached": (3, 10, 25, "ASSUMPTION: gyms stocking Graft (own gym + North East)"),
    "gym_adoption": (0.10, 0.20, 0.30, "ASSUMPTION: share of members who buy at least weekly"),
    "gym_bars_per_week": (1, 2, 3, "ASSUMPTION"),
    "gym_weeks": (40, 40, 40, "ASSUMPTION: weeks a gym fridge is stocked"),
    "yt_subs": (25_000,) * 3 + ("EVIDENCE: Ewan, ~25k subscribers (founder figure)",),
    "yt_uk_share": (0.30, 0.40, 0.50, "ASSUMPTION: UK share of subscribers (GAP: check YouTube Studio)"),
    "yt_trains_share": (0.20, 0.30, 0.40, "ASSUMPTION: share who train combat sports (test with Community poll)"),
    "yt_conversion": (0.01, 0.02, 0.04, "ASSUMPTION: share of UK trainers who become repeat D2C buyers"),
    "yt_bars_per_year": (24, 48, 96, "ASSUMPTION: bars per D2C buyer per year"),
}
CASES = ("low", "mid", "high")


def v(key, c):
    return I[key][CASES.index(c)]


def fmt(x):
    return f"£{x:,.0f}"


print("=" * 78)
print("INPUTS (every one tagged)")
print("=" * 78)
for k, val in I.items():
    print(f"{k:24s} {str(val[0]):>11s} {str(val[1]):>11s} {str(val[2]):>11s}  {val[3]}")

print("\n" + "=" * 78)
print("TAM / SAM / SOM (UK, retail £ per year)")
print("=" * 78)
res = {}
for c in CASES:
    combat = v("england_martial_arts", c) * v("england_to_uk", c) + v("boxing_extra", c) + v("bjj_extra", c)
    tam = combat * v("snacks_per_week_tam", c) * v("weeks", c) * v("price", c)
    tam_td = v("uk_protein_grocery_gbp", c) * combat / v("uk_gym_members", c)
    mma = v("ma_schools", c) * v("share_schools_mma", c) * v("members_per_mma_gym", c)
    sam = mma * v("buyer_share_sam", c) * v("bars_per_week_sam", c) * v("weeks", c) * v("price", c)
    sam_td = v("uk_protein_grocery_gbp", c) * mma / v("uk_gym_members", c)
    gym_bars = v("gyms_reached", c) * v("members_per_mma_gym", c) * v("gym_adoption", c) * v("gym_bars_per_week", c) * v("gym_weeks", c)
    yt_buyers = v("yt_subs", c) * v("yt_uk_share", c) * v("yt_trains_share", c) * v("yt_conversion", c)
    yt_bars = yt_buyers * v("yt_bars_per_year", c)
    som = (gym_bars + yt_bars) * v("price", c)
    res[c] = dict(combat=combat, tam=tam, tam_td=tam_td, mma=mma, sam=sam, sam_td=sam_td,
                  gym_bars=gym_bars, yt_buyers=yt_buyers, yt_bars=yt_bars, som=som)

rows = [("UK combat-sport participants", "combat", False),
        ("TAM bottom-up (all post-training snacks as bars)", "tam", True),
        ("TAM top-down (combat share of £225m protein grocery)", "tam_td", True),
        ("People training at UK MMA gyms", "mma", False),
        ("SAM bottom-up (MMA trainees who buy snacks)", "sam", True),
        ("SAM top-down (MMA share of £225m protein grocery)", "sam_td", True),
        ("SOM: gym bars a year", "gym_bars", False),
        ("SOM: YouTube D2C repeat buyers", "yt_buyers", False),
        ("SOM: YouTube D2C bars a year", "yt_bars", False),
        ("SOM (3-yr reachable revenue)", "som", True)]
print(f"{'Measure':52s} {'Low':>13s} {'Mid':>13s} {'High':>13s}")
for label, key, money in rows:
    vals = [res[c][key] for c in CASES]
    print(f"{label:52s} " + " ".join(f"{(fmt(x) if money else f'{x:,.0f}'):>13s}" for x in vals))

m = res["mid"]
print("\nWorked arithmetic (mid case):")
print(f"  Combat participants = 293,000 x 1.20 + 36,000 + 40,000 = {m['combat']:,.0f}")
print(f"  TAM = {m['combat']:,.0f} x 2 snacks/wk x 48 wks x £2.25 = {fmt(m['tam'])}")
print(f"  TAM top-down = £225m x {m['combat']:,.0f} / 12.1m gym members = {fmt(m['tam_td'])}")
print(f"  MMA trainees = 9,500 schools x 15% x 100 members = {m['mma']:,.0f}")
print(f"  SAM = {m['mma']:,.0f} x 50% x 3 bars/wk x 48 wks x £2.25 = {fmt(m['sam'])}")
print(f"  SAM top-down = £225m x {m['mma']:,.0f} / 12.1m = {fmt(m['sam_td'])}")
print(f"  SOM gyms = 10 gyms x 100 x 20% x 2 bars x 40 wks = {m['gym_bars']:,.0f} bars")
print(f"  SOM YouTube = 25,000 x 40% UK x 30% train x 2% = {m['yt_buyers']:,.0f} buyers x 48 bars = {m['yt_bars']:,.0f} bars")
print(f"  SOM = ({m['gym_bars']:,.0f} + {m['yt_bars']:,.0f}) x £2.25 = {fmt(m['som'])}")
print("  Note: top-down < bottom-up because the top-down only counts today's grocery protein spend"
      " at the average gym-goer rate; the bottom-up assumes every post-training snack becomes a bar.")

# ---------------------------------------------------------------- competitors
# name, serving g, protein g, carbs g, sugar g, sat fat g/100 g (None = GAP),
# sweetener/polyol (True/False/None), protein whole-food or natural (True/False/None),
# price £ per unit (None = GAP), price note, source IDs
# "natural protein" = egg/egg white, milk/milk powder, whey or milk protein CONCENTRATE, nuts.
# Isolates, soy crisps and collagen count as not natural for test 5 (per 28 brief option b).
C = [
    ("Grenade Carb Killa", 60, 20, 18, 0.9, 5.6 / 60 * 100, True, False, 2.85, "Boots single", "C1 C2 M26"),
    ("Barebells Protein Bar", 55, 20, 17, 1.4, 3.1 / 55 * 100, True, False, 2.90, "Tesco single", "C3 M24"),
    ("Fulfil Vitamin & Protein", 55, 19.5, 15.9, 1.1, 8.0, True, False, 2.90, "Tesco single", "C4 M25 U30"),
    ("Myprotein Layered Bar", 60, 20, 20.4, 1.9, 5.5, True, False, 2.50, "H&B RRP", "C5 M28 U31"),
    ("PhD Smart Bar", 64, 21, 22, 2.0, None, True, False, 2.50, "H&B single", "C7 C8"),
    ("Huel Complete Nutrition Bar", 55, 15, 17, 1.7, 3.1 / 55 * 100, True, False, 2.50, "H&B", "C38"),
    ("Misfits Plant Protein Bar", 50, 14, 19, 0.6, 2.9 / 50 * 100, True, False, 2.20, "Tesco single", "C31 U32"),
    ("Warrior RAW Protein Flapjack", 75, 20.1, None, 3.1, None, True, False, 1.00, "£11.99/12", "C34 U34"),
    ("Myprotein Oat Bakes", 75, 18, 34, 3.8, None, True, False, None, "GAP", "U34"),
    ("Myprotein THE Re-Fuel Bar", 80, 22, 32, None, None, True, False, 1.54, "£18.49/12", "C33"),
    ("Trek Protein Flapjack", 50, 9.8, 23, 12, None, False, False, 1.85, "Tesco single", "C15 M19"),
    ("Nakd Protein", 45, 7.2, 15, 13, None, False, None, 1.50, "H&B single", "C14 M19"),
    ("Bounce Protein Ball", 40, 9.3, 15.5, None, None, None, None, 1.75, "Ocado single", "C16"),
    ("Veloforte Forza", 70, 12.1, 38.3, 27.6, 1.2, False, True, 2.75, "inherited est.", "C24 U33"),
    ("TORQ Recovery Bar", 65, 13.4, 40.2, 22.7, 0.7 / 65 * 100, False, True, 2.50, "SRP", "C26"),
    ("Styrkr BAR+ Recovery", 74, 15, 46.6, 28.4, None, False, False, 2.75, "£32.95/12", "C22 C23"),
    ("33Fuel Eroica (2-bar pack)", 100, 20, 43, 38, None, False, True, 4.40, "inherited", "C30"),
    ("Huel Ready-to-Drink 500 ml", 500, 20, 34, 4.3, None, True, False, 3.00, "Tesco", "U36"),
    ("Arla Protein pudding 200 g", 200, 20, None, None, None, True, True, 1.75, "Tesco", "U35"),
    ("Yazoo chocolate milk 400 ml", 400, 12.8, 35.2, None, None, False, True, 1.60, "Tesco", "C28"),
    ("Main Event (UFC) bar [US only]", None, 20, None, 3.0, None, False, False, None, "US D2C", "U2 U3"),
]
GRAFT = [
    ("Graft v13 bag bar (CALCULATED)", 50, 15.0, 22.5, 2.9, 0.6, False, True, 2.00, "test price", "PROGRESS 19 Oct; sat fat ASSUMPTION"),
    ("Graft real bake 1 (MEASURED, 18 Oct)", 50, 9.6, 13.2, 3.7, None, False, True, 2.00, "test price", "04f"),
]


def score(r):
    name, g, p, carb, sug, sat, sweet, natural = r[:8]
    t1 = None if p is None else p >= 10
    t2 = None if carb is None else carb >= 20
    t3 = None if sug is None else sug <= 5
    t4 = None if sat is None else sat <= 1.5
    if sweet is True or natural is False:
        t5 = False
    elif sweet is False and natural is True:
        t5 = True
    else:
        t5 = None
    return [t1, t2, t3, t4, t5]


def mark(t):
    return {True: "Y", False: "n", None: "?"}[t]


print("\n" + "=" * 78)
print("5-TEST COMPETITOR SCORING (Y pass / n fail / ? data gap)")
print("T1 protein>=10 g/serving  T2 carbs>=20 g/serving  T3 sugar<=5 g/serving")
print("T4 sat fat<=1.5 g/100 g   T5 no artificial sweeteners/polyols AND whole-food/natural protein")
print("=" * 78)
print(f"{'Product':38s} T1 T2 T3 T4 T5  pass  £/unit £/10gP  sources")
all5 = 0
fails_known = 0
best = []
for r in C + GRAFT:
    t = score(r)
    n = sum(1 for x in t if x)
    price = r[8]
    p10 = f"{price / r[2] * 10:5.2f}" if price and r[2] else "  n/a"
    pr = f"{price:5.2f}" if price else "  n/a"
    print(f"{r[0]:38s}  {'  '.join(mark(x) for x in t)}  {n}/5  {pr}  {p10}  {r[10]}")
    if r in C:
        if all(x is True for x in t):
            all5 += 1
        if any(x is False for x in t):
            fails_known += 1
        best.append((n, r[0]))
print(f"\nCompetitors scored: {len(C)}")
print(f"Competitors passing all 5 tests: {all5}")
print(f"Competitors failing at least one test on known data: {fails_known} of {len(C)}")
best.sort(reverse=True)
print("Nearest misses: " + "; ".join(f"{name} ({n}/5)" for n, name in best[:4]))
print("Graft v13 passes all 5 ONLY on calculated values; the one measured bake fails T1 (9.6 g) and T2.")
