#!/usr/bin/env python3
"""Summarise landing-page sign-ups exported as CSV (standard library only).

Usage:
    python3 analyse_signups.py signups.csv
    python3 analyse_signups.py signups.csv --visits youtube=420 poster=60 meta=900

--visits gives page visits per utm_source (from your hosting or Meta stats) so
the script can print visit -> sign-up conversion. Without it, only sign-up
counts per source are shown.

Column names are matched loosely, so a Google Forms export with question text
as headers works as long as each header contains one of the keywords in
COLUMN_KEYWORDS below.
"""
import argparse
import csv
import re
import statistics
import sys
from collections import Counter

COLUMN_KEYWORDS = {
    "email": ["email"],
    "role": ["role", "fits you best", "compete"],
    "current_snack": ["current_snack", "eat after training"],
    "struggle": ["struggle"],
    "preorder": ["preorder", "pre-order"],
    "price_too_cheap": ["too_cheap", "doubt the quality"],
    "price_bargain": ["bargain"],
    "price_expensive": ["price_expensive", "getting expensive"],
    "price_too_expensive": ["too_expensive", "too expensive"],
    "utm_source": ["utm_source"],
    "utm_medium": ["utm_medium"],
    "utm_campaign": ["utm_campaign"],
    "landing_variant": ["landing_variant", "variant"],
}

# Simple keyword themes for free-text answers. Extend after reading the raw answers.
SNACK_THEMES = {
    "protein bar": ["bar", "grenade", "barebells", "fulfil", "phd"],
    "shake": ["shake", "whey", "protein powder"],
    "milk / yoghurt": ["milk", "yoghurt", "yogurt", "skyr", "quark", "yazoo", "arla"],
    "fruit": ["banana", "fruit", "apple"],
    "meal": ["meal", "chicken", "rice", "pasta", "sandwich", "wrap"],
    "nothing": ["nothing", "don't", "dont", "skip", "none"],
    "fast food / shop": ["meal deal", "greggs", "mcdonald", "takeaway", "crisps"],
}
STRUGGLE_THEMES = {
    "time / prep": ["time", "prep", "cook", "busy"],
    "weight cut / making weight": ["weight", "cut", "cutting", "scales"],
    "hunger": ["hungry", "hunger", "appetite"],
    "energy / tired": ["energy", "tired", "fatigue", "flat"],
    "cost": ["cost", "money", "expensive", "price"],
    "stomach / digestion": ["stomach", "bloat", "gut", "digest", "sick"],
    "carbs": ["carb"],
    "sugar / sweeteners": ["sugar", "sweetener"],
}


def find_columns(headers):
    mapping = {}
    for key, words in COLUMN_KEYWORDS.items():
        for h in headers:
            hl = h.lower()
            if any(w in hl for w in words) and h not in mapping.values():
                mapping[key] = h
                break
    return mapping


def pct(n, d):
    return f"{100.0 * n / d:5.1f}%" if d else "  n/a"


def to_price(value):
    if value is None:
        return None
    m = re.search(r"\d+(?:\.\d+)?", str(value).replace(",", "."))
    if not m:
        return None
    v = float(m.group())
    return v if 0 < v <= 20 else None


def theme_counts(answers, themes):
    counts = Counter()
    for a in answers:
        al = a.lower()
        hit = False
        for theme, words in themes.items():
            if any(w in al for w in words):
                counts[theme] += 1
                hit = True
        if not hit:
            counts["other / unclear"] += 1
    return counts


def crossing(grid, rising, falling):
    """First price where the rising curve meets or passes the falling curve."""
    for p, r, f in zip(grid, rising, falling):
        if r >= f:
            return p
    return None


def van_westendorp(rows):
    """Return (n, medians, OPP, IDP, PMC, PME) from complete, consistent answers."""
    keys = ["price_too_cheap", "price_bargain", "price_expensive", "price_too_expensive"]
    sets = []
    for r in rows:
        vals = [to_price(r.get(k)) for k in keys]
        if None not in vals and vals == sorted(vals):
            sets.append(vals)
    n = len(sets)
    if n == 0:
        return 0, None, None, None, None, None
    medians = [statistics.median(s[i] for s in sets) for i in range(4)]
    grid = [round(0.05 * i, 2) for i in range(1, 201)]  # £0.05 to £10.00
    too_cheap = [sum(s[0] >= p for s in sets) / n for p in grid]
    cheap = [sum(s[1] >= p for s in sets) / n for p in grid]
    expensive = [sum(s[2] <= p for s in sets) / n for p in grid]
    too_exp = [sum(s[3] <= p for s in sets) / n for p in grid]
    opp = crossing(grid, too_exp, too_cheap)
    idp = crossing(grid, expensive, cheap)
    pmc = crossing(grid, [1 - c for c in cheap], too_cheap)
    pme = crossing(grid, too_exp, [1 - e for e in expensive])
    return n, medians, opp, idp, pmc, pme


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv_file")
    ap.add_argument("--visits", nargs="*", default=[], help="source=visits pairs, e.g. youtube=420")
    args = ap.parse_args()

    with open(args.csv_file, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        cols = find_columns(headers)
        raw = list(reader)

    if "email" not in cols:
        sys.exit("No email column found. Headers seen: " + ", ".join(headers))

    # Normalise rows to our keys and drop duplicate emails (keep the first).
    rows, seen = [], set()
    for r in raw:
        row = {k: (r.get(h) or "").strip() for k, h in cols.items()}
        email = row["email"].lower()
        if not email or email in seen:
            continue
        seen.add(email)
        rows.append(row)
    n = len(rows)
    print(f"Sign-ups (unique emails): {n}   (rows in file: {len(raw)})")
    missing = [k for k in COLUMN_KEYWORDS if k not in cols]
    if missing:
        print("Columns not found (skipped):", ", ".join(missing))
    if n == 0:
        return

    print("\n== Sign-ups by source ==")
    visits = {}
    for pair in args.visits:
        if "=" in pair:
            k, v = pair.split("=", 1)
            try:
                visits[k.strip().lower()] = int(v)
            except ValueError:
                print(f"Ignoring bad --visits value: {pair}")
    by_source = Counter((r.get("utm_source") or "direct").lower() for r in rows)
    print(f"{'source':<18}{'sign-ups':>9}{'share':>8}{'visits':>8}{'conv.':>8}")
    for src, c in by_source.most_common():
        v = visits.get(src)
        conv = pct(c, v) if v else "  n/a"
        print(f"{src:<18}{c:>9}{pct(c, n):>8}{(v or ''):>8}{conv:>8}")

    if any(r.get("utm_campaign") for r in rows):
        print("\n== Sign-ups by campaign ==")
        for camp, c in Counter(r.get("utm_campaign") or "(none)" for r in rows).most_common():
            print(f"{camp:<30}{c:>5}")

    if any(r.get("landing_variant") for r in rows):
        print("\n== Sign-ups by landing-page variant ==")
        for var, c in Counter(r.get("landing_variant") or "(none)" for r in rows).most_common():
            print(f"{var:<10}{c:>5}")

    print("\n== Compete / train / watch ==")
    roles = Counter((r.get("role") or "no answer").lower() for r in rows)
    for role, c in roles.most_common():
        print(f"{role:<12}{c:>5}{pct(c, n):>8}")
    trainers = [r for r in rows if (r.get("role") or "").lower() in ("compete", "train")]

    print("\n== Pre-order intent: 5-pack at £10 ==")
    for label, group in (("everyone", rows), ("compete + train only", trainers)):
        po = Counter((r.get("preorder") or "no answer").lower() for r in group)
        g = len(group)
        parts = "  ".join(f"{k}: {po.get(k, 0)} ({pct(po.get(k, 0), g).strip()})"
                          for k in ("yes", "maybe", "no", "no answer"))
        print(f"{label:<22} n={g:<4} {parts}")

    for title, key, themes in (("Current post-training food", "current_snack", SNACK_THEMES),
                               ("Biggest food struggle in camp", "struggle", STRUGGLE_THEMES)):
        answers = [r[key] for r in rows if r.get(key)]
        print(f"\n== {title} (answered: {len(answers)}) ==")
        for theme, c in theme_counts(answers, themes).most_common():
            print(f"{theme:<28}{c:>5}{pct(c, len(answers)):>8}")

    print("\n== Price (Van Westendorp, £ per snack) ==")
    vw_n, medians, opp, idp, pmc, pme = van_westendorp(rows)
    if vw_n == 0:
        print("No complete, consistent price answers yet.")
    else:
        labels = ["too cheap", "bargain", "getting expensive", "too expensive"]
        print(f"Complete, consistent answers: {vw_n}")
        for lab, m in zip(labels, medians):
            print(f"  median '{lab}': £{m:.2f}")
        fmt = lambda x: f"£{x:.2f}" if x is not None else "n/a"
        print(f"  acceptable range (PMC to PME): {fmt(pmc)} to {fmt(pme)}")
        print(f"  optimal price point: {fmt(opp)}   indifference price: {fmt(idp)}")
        if vw_n < 30:
            print("  Caution: fewer than 30 answers, so treat these points as indicative only.")


if __name__ == "__main__":
    main()
