"""Combat-sports segment scoring (22 Oct 2026). Which combat-sports groups should Ewan target first?
Scores are 1-5. Size uses the evidence-backed UK figures in 37-combat-sports-market.md; everything else is a
judgement from the cited evidence and is marked as such. Run: python3 research/37_combat_segments.py"""

# weights: need and reach matter most for a first market (beachhead); size matters least at this stage
W = dict(need=0.30, reach=0.30, wtp=0.15, gap=0.15, size=0.10)

# size_uk: (low, high) people; src: source IDs; tag: how solid the size figure is
SEGMENTS = {
    "Competing amateur MMA fighters": dict(size_uk=(5_000, 7_000), src="U18 proxy (UK+IE rankings)", tag="ASSUMPTION",
        need=5, reach=5, wtp=3, gap=5, size=2,
        why="Cut weight (~97%, X1), double sessions, under-eat carbs (X3); Ewan's gym + 25k channel; 8 fighters asked for this"),
    "MMA gym members who train but don't compete": dict(size_uk=(48_000, 360_000), src="U17 + ASSUMPTION", tag="ASSUMPTION",
        need=3, reach=5, wtp=3, gap=4, size=4,
        why="Train hard, many stay lean; same gyms and channel; some say current bars are 'fine'"),
    "BJJ competitors and regular trainers": dict(size_uk=(40_000, 40_000), src="CS4 (UKBJJA ~40k, weak)", tag="EVIDENCE (weak)",
        need=4, reach=4, wtp=3, gap=4, size=3,
        why="Weight classes at competitions; grappling on a full stomach; many MMA gyms run BJJ"),
    "Muay Thai and kickboxing": dict(size_uk=(100_000, 100_000), src="CS1 (unsourced site claim, 2023)", tag="EVIDENCE (weak)",
        need=4, reach=4, wtp=3, gap=4, size=4,
        why="Weight classes; ~400 MMA gyms reportedly also teach Muay Thai (weak)"),
    "Competitive amateur boxers (England Boxing)": dict(size_uk=(36_000, 36_000), src="U14 (all members, incl. juniors)", tag="EVIDENCE",
        need=4, reach=3, wtp=2, gap=4, size=3,
        why="Weigh-ins every bout; Durham ranked #2 UK city for boxing clubs per capita (CS6, weak); many members are juniors with low spend"),
    "White-collar boxers in an 8-week camp": dict(size_uk=(20_000, 40_000), src="CS5 (promoter estimates)", tag="EVIDENCE (promoter)",
        need=4, reach=3, wtp=5, gap=4, size=3,
        why="First-time adults training hard for 8 weeks to a weight; have money; want guidance; event-based so easy to reach per camp"),
    "University combat clubs (BUCS)": dict(size_uk=(240, 2_000), src="CS7 (240 BUCS boxers / 72 unis; judo 45+ unis)", tag="EVIDENCE + ASSUMPTION",
        need=4, reach=4, wtp=2, gap=4, size=1,
        why="Durham has clubs on the doorstep; student budgets; small numbers"),
    "Women in combat sports": dict(size_uk=(2_920, 30_000), src="CS2 (England Boxing women 2,920 in 2024, +23.5% in 2 yrs) + ASSUMPTION", tag="EVIDENCE + ASSUMPTION",
        need=4, reach=4, wtp=4, gap=5, size=2,
        why="Fast growth; feel served by male-coded brands (WA1-WA4); weight classes; Ewan's gym has access"),
    "Boxing-fitness / recreational martial arts": dict(size_uk=(293_000, 293_000), src="U12 (martial arts, England)", tag="EVIDENCE",
        need=2, reach=2, wtp=3, gap=2, size=5,
        why="Large but lower need; general fitness bars already serve them"),
}

def score(s):
    return round(sum(W[k] * s[k] for k in W), 2)

rows = sorted(((score(s), name, s) for name, s in SEGMENTS.items()), reverse=True)
print(f"{'Rank':<5}{'Segment':<46}{'Score':>6}  need reach wtp gap size  UK size (people)        source / tag")
for i, (sc, name, s) in enumerate(rows, 1):
    lo, hi = s["size_uk"]
    size = f"{lo:,}" if lo == hi else f"{lo:,}-{hi:,}"
    print(f"{i:<5}{name:<46}{sc:>6}  {s['need']:>4} {s['reach']:>5} {s['wtp']:>3} {s['gap']:>3} {s['size']:>4}  {size:<22}  {s['src']} [{s['tag']}]")

top = [name for _, name, _ in rows[:3]]
assert "Competing amateur MMA fighters" in top, "beachhead check"
print("\nBeachhead (top 3):", "; ".join(top))
print("Weights:", W, "(need + reach = 60%: a first market must hurt and be reachable)")
