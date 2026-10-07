#!/usr/bin/env python3
"""Generates the FETTLE logo SVGs (wordmark, mark, lockup; light + dark).
The wordmark is drawn as monoline strokes (no font dependency), so it renders
identically everywhere. Run from repo root: python3 05-brand/build_logos.py"""
from pathlib import Path

INK, OAT, EMBER, EMBER_DARK = "#1C1B19", "#F4EFE6", "#B93D0B", "#F0804A"
SW = 12  # stroke width

# Letter paths on a 0..100 baseline grid (x-height 44, ascender ~10)
LETTERS = {
    "f": ("M14 100 V30 A18 18 0 0 1 32 12 H40 M2 46 H32", 40),
    "e": ("M4 70 H54 A26 26 0 1 0 47.9 86.7", 58),
    "t": ("M14 20 V84 A16 16 0 0 0 30 100 H36 M2 46 H32", 38),
    "l": ("M6 10 V100", 12),
}
GAP = 10


def wordmark_paths(x0=0):
    out, x = [], x0
    for ch in "fettle":
        d, w = LETTERS[ch]
        out.append(f'<path transform="translate({x} 0)" d="{d}"/>')
        x += w + GAP
    return "\n    ".join(out), x - GAP


def mark(x, y, s, left, right):
    # The mark: one bar, scored into two halves (half after a light session, whole after a hard one)
    w, h, g, r = 34 * s, 22 * s, 6 * s, 7 * s
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{left}"/>'
            f'<rect x="{x + w + g}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{right}"/>')


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">\n'
            f'  <title>{title}</title>\n  {body}\n</svg>\n')


def main():
    out = Path("05-brand")
    paths, width = wordmark_paths(8)
    for mode, ink, accent in (("light", INK, EMBER), ("dark", OAT, EMBER_DARK)):
        g = f'<g fill="none" stroke="{ink}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">\n    {paths}\n  </g>'
        (out / f"logo-wordmark-{mode}.svg").write_text(svg(width + 16, 112, g, "fettle"))
        (out / f"logo-mark-{mode}.svg").write_text(svg(96, 44, mark(8, 11, 1, accent, ink), "fettle mark"))
        lock_paths, lw = wordmark_paths(124)
        lg = (mark(8, 59, 1.15, accent, ink) +
              f'\n  <g fill="none" stroke="{ink}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">\n    {lock_paths}\n  </g>')
        (out / f"logo-lockup-{mode}.svg").write_text(svg(lw + 16, 112, lg, "fettle"))
    print("wrote", sorted(p.name for p in out.glob("logo-*.svg")))


if __name__ == "__main__":
    main()
