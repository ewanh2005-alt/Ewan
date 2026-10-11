# 04e — Texture-first plan (v5): no dryness, height, even bake

**Date:** 11 Oct 2026 · **Numbers from:** `research/04d_recovery_calcs.py` (v5 section → `research/04d_v5_output.json`). These are calculated values; the weight model assumes about 40% water stays in after baking.
**Brief (Ewan):**
- **Size and nutrition:** about 50 g bar, 20 g protein, high carbs, low sugar, fibre a bit high.
- **Texture:** **zero dryness**; texture is the priority.
- **Shape:** height and shape, both sides cooked evenly.
- **Ingredients:** the same ones as before.
- **Feedback so far:**
  - Vanilla: dry, bad texture.
  - Chocolate: too peanutty.
  - Banana Bread: dry.
  - All three: awful texture.

---

## 1. The honest maths: why one 50 g bar can't do everything
Checked in code at 30%, 38% and 45% moisture:

| What's in a 50 g bar (moist, not dry) | Protein | Carbs | Fibre |
|---|---|---|---|
| Egg white + quark only (a baked cheesecake, no oats) | 21–27 g | ~4 g | 0 g |
| Mostly egg white and quark, some oats | 12–15 g | 11–14 g | ~1.5 g |
| Balanced (oats for carbs) | 9–12 g | 13–17 g | ~2 g |

- 20 g protein in 50 g means **40% protein**.
- A bar that isn't dry has to keep about 35–45% water.
- That leaves almost no room for oats, so **no carbs and no fibre**.
- Only protein powder gets 20 g protein, plus carbs, into 50 g, and that isn't one of your ingredients.

**The way to get it all: 2 × 50 g bars per pack.**
- **Each bar:** about 10 g protein.
- **Each pack:** about **20 g protein, 25–27 g carbs, about 7 g sugar, about 5 g fibre**.
- **What you keep:**
  - the 50 g bar size
  - 20 g protein per serving
  - high carbs, low sugar, fibre
  - real food only

## 2. Why the texture failed, and the fix for each

| Problem | Cause | Fix (technique, same ingredients) |
|---|---|---|
| Dry | Dry oats and oat bran pull water out of the egg while baking; long, hot, open bake; thin layer | **Soak** the oats, oat bran and chia in milk **overnight** (like overnight oats), so they're already full of water. **Water bath** at a lower heat. **Foil** over the top. **Pull at 75 °C** in the centre, not later |
| Flat, no height | Liquid batter just spreads; no air | **Whisk the egg whites to soft peaks** and **fold them in**. That's how a soufflé or angel cake rises, with nothing added. Use a **20 cm square tin with sides** |
| Uneven: burnt edges, pale middle | Direct heat from the tray and top; thin edges | **Water bath** (tin sitting in hot water): gentle, even heat on the bottom and sides. **Foil** for the first 25 min, so the top doesn't dry before the middle sets |
| Gritty, crumbly | Whole oats and oat bran | **Blitz the oats** into a rough flour before soaking (blender or hand blender), for a softer, cake-like crumb |
| Bland | Little salt or sweetness | More **vanilla**, a proper pinch of **salt**, honey kept modest |
| Too peanutty | Peanut butter overpowers cocoa | **Chocolate-led:** cocoa 20 g, peanut butter cut to **5 g** per batch (just a background note), plus a splash of vanilla |
| Collapses after baking | Sudden temperature change | Turn the oven off and **leave the door ajar for 10 min** before taking it out |
| Hard to cut cleanly | Cut warm | **Chill overnight, covered**, then cut with a **hot, wet knife** |

## 3. Test plan: fix the texture first, then do all three
1. **Round 1 (one flavour): Banana Bread v5.**
   - Banana already tasted best, so it isolates the texture fix.
   - Score: dryness 1–5 (5 = not dry at all), height in cm, evenness of top and bottom, taste 1–9.
2. **If it passes** (dryness ≥4, height ≥2 cm, taste ≥7): bake Vanilla and Chocolate v5.
3. **If not,** change **one thing at a time**:

| Result | Next change |
|---|---|
| Still dry | Bake 5 min less, or add 30 g quark |
| Wet or eggy in the middle | Bake 5 min longer |
| No height | Whisk the whites stiffer; fold more gently |
| Sank | Leave the oven door ajar longer; don't open the oven before 30 min |

4. **Blind test** the best version against a Barebells bar with 5 people.

**Kit you'll need:**
- **For the bake:**
  - **an electric hand whisk** (soft peaks by hand take 5–8 min of hard whisking)
  - a **20 cm square tin with a solid base** (not loose-bottomed, because of the water bath)
  - a **roasting tray** big enough to hold the tin
- **Also:** a probe thermometer, foil, baking paper, a blender or hand blender.

## 4. v5 batch recipes (each makes ~9–10 bars of 50 g)

| | Vanilla | Chocolate | Banana Bread |
|---|---|---|---|
| Egg whites (whipped) | 270 g (9 whites or carton) | 270 g | 270 g |
| Whole egg | 1 | 1 | 1 |
| Fat-free quark | 250 g | 250 g | 250 g |
| Semi-skimmed milk (soak) | 80 ml | 80 ml | 40 ml |
| Porridge oats (blitzed) | 90 g | 85 g | 90 g |
| Oat bran | 70 g | 70 g | 65 g |
| Chia seeds | 8 g | 8 g | 8 g |
| Honey | 16 g | 20 g | — |
| Vanilla extract | 15 g | 5 g | 5 g |
| Cocoa | — | 20 g | — |
| Peanut butter | — | 5 g | — |
| Ripe banana | — | — | 130 g |
| Cinnamon | — | — | 2 g |
| Salt | ¼ tsp | ¼ tsp | ¼ tsp |
| **Per 50 g bar** | 10.0 P · 12.9 C · 3.5 S · 2.3 Fb · 118 kcal | 9.9 P · 12.3 C · 3.5 S · 2.7 Fb · 121 kcal | 9.7 P · 13.4 C · 3.3 S · 2.6 Fb · 119 kcal |
| **Per pack of 2** | **20.1 P · 25.8 C · 7.0 S · 4.6 Fb** | **19.8 P · 24.6 C · 7.0 S · 5.5 Fb** | **19.4 P · 26.8 C · 6.7 S · 5.3 Fb** |

**Method (all three):**
1. **The night before:** blitz the oats to a rough flour. Mix with the oat bran, chia, milk and salt (Banana Bread: add the mashed banana too). Cover and chill overnight.
2. **Next day:** heat the oven to **150 °C fan / 170 °C / gas 3**. Boil a kettle. Line the square tin (paper hanging over two sides).
3. **Whisk in:** add the quark, whole egg, honey and flavour to the soaked oats. Whisk smooth.
   - **Chocolate:** loosen the peanut butter in the quark first, and sift in the cocoa.
   - **Banana Bread:** add the cinnamon.
4. In a clean, grease-free bowl, **whisk the egg whites to soft peaks**. When you lift the whisk, the peaks should flop over at the tip.
5. **Fold in the whites:** stir a third into the oat mix to loosen it, then **gently fold in the rest** with a spoon in figure-of-eight strokes until there are no white streaks. Don't stir hard, or the air goes.
6. Spoon into the tin and level gently. **Weigh the full tin.**
7. **Water bath:**
   - Put the tin in the roasting tray, on the middle shelf.
   - Pour boiling water into the tray to about **2 cm up the sides of the tin**.
   - **Cover the tin loosely with foil.**
8. **Bake 40–50 min.** Take the foil off after 25 min.
   - It's done when the top is set and springs back, and the **centre reads 75 °C** (or a skewer comes out with moist crumbs).
   - Banana Bread may need 5–10 min more.
9. **Turn the oven off, prop the door open and leave for 10 min.** Then lift the tin out of the water.
10. **Weigh the tin.** Cool 30 min, then cover and **chill overnight**.
11. **Cut with a hot, wet knife** into about 10 bars of 50 g. Weigh one bar.
12. **Store:** fridge, eat within 3 days, or freeze.

**Allergens:**
- **All three:** egg, milk, oats.
- **Chocolate:** also **peanuts**. Bake it last.

## 5. What the pack says (when it passes testing)
- **Front of pack:** "2 bars · 20 g protein · real food".
- **Each bar:** about 10 g protein, about 13 g carbs, about 3.5 g sugar.
- **"High protein" claim:** fine, because about 33% of the energy comes from protein.
