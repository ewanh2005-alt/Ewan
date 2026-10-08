"""Count themes in the Reddit comments Ewan collected (8 Oct 2026). Run: python3 research/09_reddit_counts.py"""
import csv
from collections import Counter
from pathlib import Path

rows = list(csv.DictReader(open(Path(__file__).parent / "09_reddit_coding.csv")))
bars = [r for r in rows if r["thread"] == "T1_last_bar"]
print(f"Comments coded: {len(rows)} (protein-bar thread {len(bars)}, post-training {sum(r['thread']=='T2_post_training' for r in rows)}, fibre {sum(r['thread']=='T3_fibre' for r in rows)})")
print("Protein-bar thread, repurchase:", dict(Counter(r["repurchase"] for r in bars)))
print("Protein-bar thread, country:", dict(Counter(r["country"] for r in bars)))
brands = Counter(r["product"].split()[0] for r in bars)
print("Brands:", dict(brands.most_common()))
themes = Counter(t for r in rows for t in r["themes"].split(";") if t)
print("Themes (all threads):")
for t, n in themes.most_common():
    print(f"  {t}: {n}")
print("Bars bought for training/recovery:", sum("train" in r["occasion"] or "recover" in r["occasion"] for r in bars))
