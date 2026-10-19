# 04f: v7 recipes, fresh ingredients only (no dried egg white)

**Date:** 18 Oct 2026 · **Why:** the dried egg white for v6 wasn't bought. **Numbers:** `research/04d_recovery_calcs.py` (v7 section) → `research/04d_v7_output.json`. These are calculated, not lab-tested; 35% water is assumed to stay in after baking.
**Trade-off:** about **11 g protein** per 50 g bar instead of ~15 g. It's all real food.

## Per 50 g bar (calculated)
| | Protein | Carbs | Sugar | Fibre | kcal |
|---|---|---|---|---|---|
| Vanilla | 11.1 g | 15.2 g | 4.2 g | 1.9 g | ~125 |
| Chocolate | 10.9 g | 14.3 g | 4.5 g | 2.5 g | ~128 |
| Banana Bread | 10.4 g | 16.3 g | 4.0 g | 2.5 g | ~127 |

**Each tray** makes ~4 bars of 50 g (~400 g batter). Use a **small loaf tin or tray, about 16 × 10 cm**, so the mix is 2–2.5 cm deep. A 20 cm pie dish spreads it too thin.

## Recipes (one tray each)
**Vanilla**
- egg whites 130 g (4 whites)
- quark 150 g
- semi-skimmed milk 20 ml
- porridge oats 60 g
- oat bran 12 g
- honey 8 g (1 level tsp)
- vanilla extract 8 g (1½ tsp)
- a pinch of salt

**Chocolate**
- egg whites 130 g
- quark 150 g
- milk 25 ml
- oats 55 g
- oat bran 12 g
- cocoa 11 g (2 tbsp)
- peanut butter 3 g (½ tsp)
- honey 11 g (1½ tsp)
- vanilla 3 g (½ tsp)
- a pinch of salt

**Banana Bread**
- egg whites 130 g
- quark 130 g
- ripe banana 70 g (~¾ of a medium one), mashed
- oats 60 g
- oat bran 10 g
- cinnamon 1 g (½ tsp)
- a pinch of salt
- no honey or milk

## Method (no water bath)
**The night before**
1. Blitz the oats to a rough flour.
2. Mix with the oat bran, salt, and the milk (or the mashed banana). Cover and chill overnight.

**On the day**

3. Heat the oven to **150 °C fan** (170 °C / gas 3). Line the loaf tin with baking paper, leaving extra hanging over the sides.
4. Separate the eggs, putting the whites in a clean, dry bowl. Keep the yolks covered in the fridge for an omelette.
5. Whisk the quark smooth with the honey and vanilla.
   - **Chocolate:** stir the peanut butter into the quark, then sift in the cocoa.
   - **Banana Bread:** add the cinnamon.
6. Stir in the soaked oat mix.
7. Whisk the whites to **soft peaks**: the tips flop over when you lift the whisk. That's 3–4 minutes with an electric whisk.
8. Stir in a spoonful of whites to loosen the mix, then **gently fold in the rest** in figure-of-eights until there are no streaks.
9. Spoon into the tin and level it. **Weigh the full tin.**
10. **Cover loosely with foil and bake 20 minutes.** Remove the foil and bake **10–15 minutes more**.
11. **It's done when** the top springs back and a skewer comes out with moist crumbs. The centre should read 75 °C on a probe thermometer.
12. **Turn the oven off, door ajar, for 10 minutes.**
13. Take it out, **weigh the tin again**, cool for 30 minutes, then cover and chill overnight.
14. Lift it out by the paper and **cut 4 bars with a hot, wet knife.** Weigh one bar.

**Storage:** fridge, eat within 3 days, or freeze.
**Allergens:** egg, milk, oats (gluten). Chocolate: also **peanut**, so make it last and clean down afterwards.

## Test order and what to record
1. **Banana Bread first**, since it tasted best before.
2. **Score it:**
   - dryness 1–5 (5 = not dry)
   - height in cm
   - taste out of 9
   - photo of the inside
   - tin weight before and after
3. **If it's dry:** bake 5 minutes less, or add 30 g quark.
4. **If it's wet in the middle:** bake 5 minutes more.
5. **If it's flat:** whisk the whites stiffer and fold more gently.

## Real bake 1: Vanilla (18 Oct 2026, Ewan) `[EVIDENCE: Ewan's weights]`
- Same-day method: hot-milk oat soak for about 10 minutes, whites frothed by hand, greased enamel dish (no paper), foil-tent bake.
- **Weights:**
  - dish empty: 168 g
  - with batter: 528 g, so **360 g of batter**
  - final bake: **198 g** (Ewan's corrected figure, bake alone; earlier readings of 508 g and 298 g were superseded)
  - lost **162 g (45%)**
- **Moisture:** final moisture is ~43%. The model assumed 35%, so it's a little moister than planned.
- **Real macros** (recipe scaled to 360 g; `research/04d_recovery_calcs.py`, "REAL" section):
  - per 100 g: **19.4 g protein**, 26.6 g carbs, 7.4 g sugar, 3.1 g fat, 3.4 g fibre, ~219 kcal
  - **4 bars of ~50 g each: 9.6 g protein**, 13.2 g carbs, 3.7 g sugar, 1.5 g fat, 1.7 g fibre, ~108 kcal
- **Lesson:** fresh-only gives ~10 g protein per 50 g bar. ~15 g per 50 g needs dried egg white (v6).

### Feedback on bake 1 (Ewan, 19 Oct)
- Tasted too much like yoghurt.
- The bottom wasn't cooked.
- Fluffy (good).
- Protein felt low.
- Baked **22 minutes only** (the plan was 30–35). The 198 g final weight may be off because the base was wet.

## v8 Vanilla (next bake): fixes for taste and the raw bottom
Numbers are in `research/04d_recovery_calcs.py`, v8 section, using the measured ~43% moisture. Per 50 g bar: ~9.9 g protein, 13.3 g carbs, 3.4 g sugar, 1.6 g fat, ~111 kcal.

**Changes from v7:**
- **Less yoghurt taste:** quark 150 → **100 g**, egg whites 130 → **180 g** (about 5–6 whites).
- **Toast the oats:** 60 g in a dry pan for 4–5 minutes until they smell nutty, then blitz. This gives a baked, biscuity flavour instead of a dairy one.
- Add a pinch of **cinnamon** (optional). Keep the honey, vanilla, oat bran, milk and salt the same.

**Fixing the raw bottom:**
- Put a **metal baking tray in the oven while it heats**, and stand the dish on it. This sends heat straight into the base.
- Bake on the **lower-middle shelf**.
- **Foil for 15 minutes only**, then uncovered for **15–20 minutes**: **30–35 minutes in total**.
- **Check the base:** push a knife into the centre all the way to the bottom. It should come out with no wet batter.

**About nuts (checked in code):** they **don't raise protein per 50 g bar**. Nuts add fat and weight, so 20 g of peanuts takes a bar from ~9.7 g to ~9.4 g protein and adds ~8 kcal. Add 10 g chopped only if you want them for taste or crunch. Two things do raise protein per bar: a **drier bake** (~11 g at 35% moisture, ~12 g at 30%) or **dried egg white**.
