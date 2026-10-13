"""Prepare Graft logo files from Ewan's bubble logo (originals/graft-bubble-original.png).
Crops the "GRAFT." wordmark only (drops the baked-in tagline), removes the white background,
and makes a light version for dark backgrounds plus a square icon.
Run: python3 05-brand/prep_logo.py"""
from pathlib import Path
from PIL import Image
import numpy as np

HERE = Path(__file__).parent
SRC = HERE / "originals" / "graft-bubble-original.png"
INK = (43, 43, 43)  # charcoal from the original

img = np.array(Image.open(SRC).convert("RGB")).astype(float)
lum = img.mean(axis=2)
dark = lum < 128
rows = np.where(dark.any(axis=1))[0]
# wordmark = first run of dark rows (tagline starts after a blank gap)
end = rows[0]
while end + 1 < len(dark) and dark[end + 1].any():
    end += 1
cols = np.where(dark[rows[0]:end + 1].any(axis=0))[0]
pad = 12
y0, y1 = rows[0] - pad, end + pad
x0, x1 = cols[0] - pad, cols[-1] + pad
crop_lum = lum[y0:y1, x0:x1]

# Background = bright pixels connected to the edge (flood fill). Enclosed bright pixels = the shine highlights.
from PIL import ImageDraw, ImageFilter
bright = (crop_lum > 200).astype("uint8") * 255
mask = Image.fromarray(bright).copy()
ImageDraw.floodfill(mask, (0, 0), 128)
m = np.array(mask)
background = m == 128
enclosed = m == 255                       # bright but not reachable from the edge
# Split enclosed regions: thick ones are letter counters (holes, e.g. inside A) -> transparent; small thin ones are shine strokes
highlight = np.zeros_like(enclosed)
work = Image.fromarray(enclosed.astype("uint8") * 255).copy()
ys, xs = np.nonzero(enclosed)
seen = np.zeros_like(enclosed)
for y, x in zip(ys, xs):
    if seen[y, x]:
        continue
    ImageDraw.floodfill(work, (int(x), int(y)), 77)
    region = np.array(work) == 77
    seen |= region
    # shine strokes are thin (~6 px); counters survive an erosion
    thick = np.array(Image.fromarray(region.astype("uint8") * 255).filter(ImageFilter.MinFilter(13))).any()
    if not thick:
        highlight |= region
    else:
        background |= region
    work = Image.fromarray(np.where(region, 0, np.array(work)).astype("uint8")).copy()
alpha_ink = np.clip((255 - crop_lum) / (255 - 43), 0, 1)   # anti-aliased ink edges
alpha_ink[highlight] = 1

h, w = crop_lum.shape
dark_rgba = np.zeros((h, w, 4), dtype="uint8")
dark_rgba[..., :3] = INK
dark_rgba[..., 3] = (alpha_ink * 255).astype("uint8")
dark_rgba[highlight] = (255, 255, 255, 255)
dark_rgba[background] = (0, 0, 0, 0)
Image.fromarray(dark_rgba).save(HERE / "graft-logo-dark.png")

# Light version for dark backgrounds: white ink; highlights become transparent cut-outs (keeps the shine)
light_rgba = dark_rgba.copy()
light_rgba[..., :3] = 255
light_rgba[highlight, 3] = 0
Image.fromarray(light_rgba).save(HERE / "graft-logo-light.png")

# Square icon: wordmark centred on charcoal, white ink
side = int(w * 1.25)
icon = Image.new("RGBA", (side, side), INK + (255,))
lw = Image.fromarray(light_rgba)
icon.alpha_composite(lw, ((side - w) // 2, (side - h) // 2))
icon.convert("RGB").resize((512, 512), Image.LANCZOS).save(HERE / "graft-icon.png")
icon.convert("RGB").resize((64, 64), Image.LANCZOS).save(HERE / "graft-favicon.png")
print("wordmark", w, "x", h, "| highlights px:", int(highlight.sum()))
