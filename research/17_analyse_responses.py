"""Analyse REAL survey + interview responses (no data is included in the repo).
Usage:
  python3 research/17_analyse_responses.py survey.csv [interviews.csv] [--out DIR]
- survey.csv: Google Forms export. Columns are matched by keywords from the question text (see KEYS).
- interviews.csv: research/17_interview_template.csv filled in.
Prints counts/percentages and writes research/17_results.json (+ a price chart SVG)."""
import csv, json, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEYS = {  # column-name keyword -> short name
    "how often do you train": "freq", "mainly do": "sport", "coached": "coached",
    "usually eat within 2 hours": "post_food", "can't you eat": "missed", "protein bars did you eat": "bars",
    "puts you off": "putoff", "appealing": "appeal", "pay for one": "price", "email": "email",
    "anything else": "open",
}

def load(path):
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8-sig")))
    if not rows:
        return [], {}
    cols = {}
    for c in rows[0].keys():
        for k, short in KEYS.items():
            if k in c.lower():
                cols[short] = c
    return rows, cols

def pct(n, d):
    return f"{n} ({n / d * 100:.0f}%)" if d else "0"

def multi(rows, col):
    c = Counter()
    for r in rows:
        for part in (r.get(col) or "").split(";" if ";" in (r.get(col) or "") else ","):
            p = part.strip()
            if p:
                c[p] += 1
    return c

def main():
    out_dir = ROOT / "research"
    if "--out" in sys.argv:
        i = sys.argv.index("--out"); out_dir = Path(sys.argv[i + 1]); del sys.argv[i:i + 2]
    if len(sys.argv) < 2:
        print(__doc__); return
    rows, cols = load(sys.argv[1])
    n = len(rows)
    res = {"n_survey": n, "columns_matched": cols}
    print(f"Survey responses: {n}")
    if n == 0:
        print("No responses yet."); return
    for short in ("freq", "coached", "missed", "bars", "price"):
        if short in cols:
            c = Counter((r[cols[short]] or "blank").strip() for r in rows)
            res[short] = dict(c)
            print(f"\n{short}:"); [print(f"  {k}: {pct(v, n)}") for k, v in c.most_common()]
    for short in ("sport", "post_food", "putoff"):
        if short in cols:
            c = multi(rows, cols[short]); res[short] = dict(c)
            print(f"\n{short} (tick all):"); [print(f"  {k}: {pct(v, n)}") for k, v in c.most_common()]
    if "appeal" in cols:
        vals = [int(r[cols["appeal"]]) for r in rows if (r[cols["appeal"]] or "").strip().isdigit()]
        if vals:
            res["appeal_mean"] = round(sum(vals) / len(vals), 2)
            res["appeal_top2_pct"] = round(sum(v >= 4 for v in vals) / len(vals) * 100)
            print(f"\nAppeal: mean {res['appeal_mean']}/5, {res['appeal_top2_pct']}% rate 4-5 (n={len(vals)})")
    if "email" in cols:
        res["emails_left"] = sum(1 for r in rows if "@" in (r[cols["email"]] or ""))
        print(f"\nTaste-test sign-ups (emails left): {pct(res['emails_left'], n)}")
    if "open" in cols:
        res["open_answers"] = [r[cols["open"]].strip() for r in rows if (r[cols["open"]] or "").strip()]
        print(f"\nOpen answers: {len(res['open_answers'])} (verbatim, see JSON)")
    if len(sys.argv) > 2:
        iv = list(csv.DictReader(open(sys.argv[2], newline="", encoding="utf-8-sig")))
        res["n_interviews"] = len(iv)
        res["interview_taste_test_yes"] = sum((r.get("taste_test_yes") or "").lower().startswith("y") for r in iv)
        res["interview_quotes"] = [{"id": r["id"], "quote": r["quote"], "verbatim": r.get("quote_is_verbatim", "")} for r in iv if r.get("quote")]
        print(f"\nInterviews: {len(iv)}; agreed to taste test: {res['interview_taste_test_yes']}")
    # price chart
    if "price" in res:
        order = ["£1.50", "£2.00", "£2.50", "£3.00", "wouldn't buy"]
        data = [(k, res["price"].get(k, 0)) for k in order if k in res["price"]] or list(res["price"].items())
        w, bh = 520, 34
        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {len(data)*bh+50}" font-family="Arial"><rect width="100%" height="100%" fill="#fcfcfb"/>',
               f'<text x="10" y="22" font-size="15" font-weight="bold" fill="#1d1d1b">What would you pay? (n={n})</text>']
        mx = max(v for _, v in data) or 1
        for i, (k, v) in enumerate(data):
            y = 40 + i * bh
            svg.append(f'<text x="10" y="{y+18}" font-size="12" fill="#52514e">{k}</text><rect x="110" y="{y+4}" width="{v/mx*340:.0f}" height="20" rx="4" fill="#1baf7a"/><text x="{116+v/mx*340:.0f}" y="{y+18}" font-size="12" fill="#1d1d1b">{v}</text>')
        svg.append("</svg>")
        (out_dir / "17_price_chart.svg").write_text("\n".join(svg))
    json.dump(res, open(out_dir / "17_results.json", "w"), indent=1, ensure_ascii=False)
    print(f"\nWrote {out_dir / '17_results.json'}")

if __name__ == "__main__":
    main()
