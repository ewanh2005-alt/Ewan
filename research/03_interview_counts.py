#!/usr/bin/env python3
"""Counts themes in Ewan's 10 customer interviews (research/03_interview_coding.csv).
Run from repo root: python3 research/03_interview_counts.py -> research/03_interview_counts.md"""
import csv
from collections import Counter
from pathlib import Path

rows = list(csv.DictReader(open("research/03_interview_coding.csv")))
n = len(rows)
themes = [k for k in rows[0] if k not in ("id", "segment", "gender", "notes")]
seg = Counter(r["segment"] for r in rows)
gen = Counter(r["gender"] for r in rows)
out = [f"# Interview theme counts (n = {n} potential customers; generated, do not edit)\n",
       "| Theme | Count | Who |", "|---|---|---|"]
for t in sorted(themes, key=lambda t: -sum(int(r[t]) for r in rows)):
    who = [r["id"] for r in rows if r[t] == "1"]
    out.append(f"| {t} | {len(who)}/{n} | {', '.join(who) or '—'} |")
out.append("\n| Segment | Count |\n|---|---|")
out += [f"| {k} | {v}/{n} |" for k, v in seg.most_common()]
out.append("\n| Gender | Count |\n|---|---|")
out += [f"| {k} | {v}/{n} |" for k, v in gen.most_common()]
# theme rates by segment
out.append("\n| Theme | performance_athlete | gym_regular | casual |\n|---|---|---|---|")
for t in themes:
    cells = []
    for s in ("performance_athlete", "gym_regular", "casual"):
        grp = [r for r in rows if r["segment"] == s]
        cells.append(f"{sum(int(r[t]) for r in grp)}/{len(grp)}")
    out.append(f"| {t} | " + " | ".join(cells) + " |")
Path("research/03_interview_counts.md").write_text("\n".join(out) + "\n")
print("\n".join(out))
