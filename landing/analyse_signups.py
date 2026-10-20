#!/usr/bin/env python3
"""Summarise landing-page sign-ups from an exported CSV (standard library only).

Usage:
    python3 analyse_signups.py signups.csv
    python3 analyse_signups.py signups.csv --visits youtube=600 poster=120 instagram=300

Expected columns (as exported by the page in test mode; rename Google Forms
headers to match): timestamp, name, email, status, post_training, post_other,
struggle, vw_too_cheap, vw_cheap, vw_expensive, vw_too_expensive, utm_source,
utm_medium, utm_campaign, utm_content, consent.

Visits per source come from your analytics tool (or YouTube/QR click counts);
without them, sign-ups by source are shown but not conversion rates.
"""
import argparse
import csv
import statistics
import sys
from collections import Counter

PRICE_COLS = ["vw_too_cheap", "vw_cheap", "vw_expensive", "vw_too_expensive"]


def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [{(k or "").strip().lower(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]
    # Drop duplicate emails, keeping the first sign-up.
    seen, unique = set(), []
    for r in rows:
        email = r.get("email", "").lower()
        if email and email in seen:
            continue
        seen.add(email)
        unique.append(r)
    return rows, unique


def parse_visits(pairs):
    visits = {}
    for p in pairs or []:
        if "=" not in p:
            sys.exit(f"--visits expects source=number, got {p!r}")
        k, v = p.split("=", 1)
        visits[k.strip().lower()] = int(v)
    return visits


def pct(n, d):
    return f"{100 * n / d:.0f}%" if d else "n/a"


def show_counter(title, counter, total):
    print(f"\n{title} (n = {total})")
    if not counter:
        print("  (no answers)")
    for k, v in counter.most_common():
        print(f"  {k or '(blank)':<22} {v:>4}  {pct(v, total):>5}")


def to_float(x):
    try:
        return float(x.replace("£", ""))
    except (ValueError, AttributeError):
        return None


def van_westendorp(rows):
    """Return (n, medians, approximate range of acceptable prices).

    Lower bound: where 'too cheap' (falling) crosses 'expensive' (rising).
    Upper bound: where 'cheap' (falling) crosses 'too expensive' (rising).
    """
    answers = []
    for r in rows:
        vals = [to_float(r.get(c, "")) for c in PRICE_COLS]
        if None not in vals and vals == sorted(vals):
            answers.append(vals)
    n = len(answers)
    if n == 0:
        return 0, None, None
    medians = [statistics.median(a[i] for a in answers) for i in range(4)]
    grid = sorted({v for a in answers for v in a})

    def share_at_or_below(i, p):
        return sum(1 for a in answers if a[i] >= p) / n  # "falling" curves

    def share_at_or_above(i, p):
        return sum(1 for a in answers if a[i] <= p) / n  # "rising" curves

    def cross(falling_i, rising_i):
        for p in grid:
            if share_at_or_above(rising_i, p) >= share_at_or_below(falling_i, p):
                return p
        return None

    return n, medians, (cross(0, 2), cross(1, 3))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--visits", nargs="*", help="visits per source, e.g. youtube=600 poster=120")
    args = ap.parse_args()

    raw, rows = read_rows(args.csv)
    visits = parse_visits(args.visits)
    n = len(rows)
    print(f"Sign-ups: {n} unique ({len(raw) - n} duplicate emails removed)")
    if n == 0:
        return

    consented = sum(1 for r in rows if r.get("consent", "").lower() in ("yes", "true", "1", "on"))
    print(f"With consent ticked: {consented}/{n}")

    # Conversion by source
    by_source = Counter(r.get("utm_source", "").lower() or "(none)" for r in rows)
    print("\nSign-ups and conversion by source")
    print(f"  {'source':<14} {'sign-ups':>8} {'visits':>7} {'conv.':>6}")
    for src in sorted(set(by_source) | set(visits)):
        s, v = by_source.get(src, 0), visits.get(src)
        conv = pct(s, v) if v else "n/a"
        print(f"  {src:<14} {s:>8} {v if v is not None else '-':>7} {conv:>6}")

    # Compete / train / watch, overall and by source
    status = Counter(r.get("status", "").lower() for r in rows)
    show_counter("Compete / train / watch", status, n)
    print("\n  By source:")
    for src in sorted(by_source):
        sub = Counter(r.get("status", "").lower() for r in rows if (r.get("utm_source", "").lower() or "(none)") == src)
        parts = ", ".join(f"{k or 'blank'} {v}" for k, v in sub.most_common())
        print(f"  {src:<14} {parts}")

    # Fighters and trainers only for the problem questions
    active = [r for r in rows if r.get("status", "").lower() in ("compete", "train")]
    na = len(active)

    snacks = Counter()
    for r in active:
        for item in filter(None, (x.strip() for x in r.get("post_training", "").replace(",", ";").split(";"))):
            snacks[item] += 1
    show_counter("What they ate after last training (compete + train; multi-select, counts of people)", snacks, na)
    others = [r.get("post_other") for r in active if r.get("post_other")]
    if others:
        print("  'Other' answers: " + "; ".join(others[:20]))

    struggles = Counter(r.get("struggle", "") for r in active)
    show_counter("Biggest food struggle (compete + train)", struggles, na)
    problem = na - struggles.get("none", 0) - struggles.get("", 0)
    print(f"\n  Report a struggle other than 'none': {problem}/{na} ({pct(problem, na)})"
          "  <- validation threshold: >= 40%")

    # Price
    pn, medians, rng = van_westendorp(active)
    print(f"\nPrice (Van Westendorp, compete + train, complete and ordered answers: {pn}/{na})")
    if pn:
        labels = ["too cheap", "bargain", "getting expensive", "too expensive"]
        for lab, m in zip(labels, medians):
            print(f"  median '{lab}': £{m:.2f}")
        lo, hi = rng
        lo_s = f"£{lo:.2f}" if lo is not None else "n/a"
        hi_s = f"£{hi:.2f}" if hi is not None else "n/a"
        print(f"  approx. acceptable range: {lo_s} to {hi_s}")
        if pn < 30:
            print("  Caution: fewer than 30 answers; treat the range as indicative only.")


if __name__ == "__main__":
    main()
