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

## v9 Vanilla: 15 g protein per 50 g, fresh only (19 Oct)
Ewan's target: **15 g per 50 g**. Oats dilute the protein, so v9 cuts them right down and lets egg white and quark carry it. Numbers are in `research/04d_recovery_calcs.py`, v9 section.

**Ingredients:**
- **egg whites 300 g** (about 9 eggs, or a carton of liquid egg white: still fresh egg, not powder)
- quark 120 g
- oats 25 g, toasted and blitzed
- oat bran 10 g
- honey 8 g
- vanilla 8 g
- cinnamon 1 g
- a pinch of salt
- no milk

**Batter:** ~472 g. **Bake it down to 172 g in total** (target weight). At that weight it's **15.0 g protein**, 10 g carbs, 4.2 g sugar, 1 g fat and ~112 kcal per 50 g. That makes about 3½ bars, with ~41% water left, similar to bake 1.
- If it weighs more than 172 g, there's less protein per 50 g. At ~200 g it's ~12.9 g.

**Method:**
- Same as v8: whisk the whites to soft peaks, fold them into the quark, oats and flavourings, and use a preheated metal tray under the dish.
- **Split the mix between your 2 enamel dishes.** Thinner layers dry out more and the bottoms cook through.
- Bake at 150 °C fan: foil on for 15 minutes, then off for 20–25 minutes.
- **Weigh the bake out of the dish** (or the dish minus 168 g). If it's over target, give it 5 more minutes and weigh again.

**Trade-offs:**
- Carbs drop to ~10 g per bar (the E3 professor said carbs matter).
- It tastes more eggy than bake 1. That's why the oats are toasted and the cinnamon is in.
- It needs about 9 whites per batch, so buying cartons of egg white is cheaper and wastes no yolks.

## v10 Vanilla: 15 g protein + ~16 g carbs per 50 g, fresh only (19 Oct)
Ewan wanted more carbs than v9 while keeping 15 g protein. The limit: if 15 g of every 50 g is protein, carbs can only go up if there's **less water**. So v10 uses **puffed brown rice** (81% carbs, almost dry) and is baked a bit drier. Numbers are in `research/04d_recovery_calcs.py`, v10 section.

**Ingredients:**
- **egg whites 350 g** (a carton of liquid egg white is easiest)
- quark 80 g
- oats 30 g, toasted and blitzed
- **unsweetened puffed brown rice 30 g** (new: plain, no sugar)
- honey 8 g
- vanilla 8 g
- cinnamon 1 g
- a pinch of salt

**Batter:** ~507 g. **Bake it down to 177 g in total.**

| Stop at | Water left | Per 50 g: protein | carbs | sugar | kcal |
|---|---|---|---|---|---|
| **177 g** | 30% | **15.0 g** | **15.7 g** | 3.8 g | 135 |
| 200 g | 38% | 13.3 g | 13.9 g | 3.4 g | 120 |

**Method:**
1. Whisk the whites to soft peaks.
2. Mix the quark, toasted oats, honey, vanilla, cinnamon and salt. Fold in the whites, then **fold in the puffed rice last**.
3. Split between the 2 enamel dishes on a preheated metal tray, lower-middle shelf, 150 °C fan.
4. Foil on for 15 minutes, then off for **25–30 minutes**.
5. Weigh both bakes (dish weight minus 168 g each). If they're over 177 g together, give them 5 more minutes.

**Risk:** at 30% water it's firmer and drier than bake 1, close to the dryness problem from earlier bakes. Check the texture at ~190 g before pushing on to 177 g.

## v11 Vanilla: 15 g protein + ~18 g carbs per 50 g (19 Oct)
"A few more grams of carbs" than v10. It has more puffed rice and is baked drier. Each extra 1 g of carbs per 50 g costs about 2.5 points of water.

**Ingredients:**
- egg whites 375 g
- quark 80 g
- oats 25 g, toasted
- **puffed brown rice 50 g**
- honey 8 g
- vanilla 8 g
- cinnamon 1 g
- a pinch of salt

**Batter:** ~547 g. **Bake it down to 189 g.**

| Stop at | Water left | Per 50 g: protein | carbs | sugar | kcal |
|---|---|---|---|---|---|
| **189 g** | 25% | **15.0 g** | **18.2 g** | 3.6 g | 144 |
| 210 g | 33% | 13.5 g | 16.4 g | 3.3 g | 130 |

**Method:** as v10 (2 dishes, preheated tray, foil 15 minutes, then off for ~30–35 minutes, weigh it down to target). **Texture:** at 25% water it's firm, like a soft flapjack, not fluffy.

## v12 Vanilla: 15 g protein + ~21 g carbs per 50 g (19 Oct)
- **Ingredients:**
  - egg whites 425 g (carton)
  - quark 80 g
  - oats 30 g, toasted
  - **puffed brown rice 70 g**
  - honey 8 g
  - vanilla 8 g
  - cinnamon 1 g
  - a pinch of salt
- **Batter:** ~622 g. **Bake it down to 214 g.** That gives **15.0 g protein, 20.7 g carbs**, 3.4 g sugar, 1.1 g fat and ~155 kcal per 50 g. About 20% water is left.
  - At 240 g: 13.4 g protein, 18.4 g carbs.
- **Method:**
  - Split between 2 dishes on a preheated tray.
  - 150 °C fan: foil on for 15 minutes, then off for ~35 minutes.
  - If it's still over target, **drop to 120 °C** and dry it in 10-minute steps, weighing each time.
- **Texture:** a firm, flapjack-style bar, not fluffy. Upside: drier bars keep better out of the fridge, which matches E3's "stay in a bag all day" point. This still needs testing.

## v13 Bag Bar (vanilla): no fridge, keeps in a bag all day (19 Oct)
**Why:** E3 (the sport nutrition professor) said a snack that can stay in a bag all day is the way to go. Ewan wants no refrigeration, while keeping ≥15 g protein and ≥20 g carbs per 50 g.

**What changes:**
- **No quark**, so no fresh dairy. That also removes the **milk allergen**: allergens are now just **egg and oats (gluten)**.
- **Twice-baked** down to ~16% water, so it's firm and chewy, like a flapjack or soft granola bar.

**Ingredients:**
- **egg whites 475 g** (one 500 ml carton of liquid egg white, or ~14 eggs)
- oats 40 g, toasted and blitzed
- puffed brown rice 70 g
- honey 8 g
- vanilla 8 g
- cinnamon 1 g
- a pinch of salt

**Batter:** ~602 g. **Bake and dry it down to 204 g in total.** At that weight, per 50 g: **15.0 g protein, 22.5 g carbs**, 2.9 g sugar, 1.4 g fat, 1.5 g fibre, ~165 kcal. That's about 4 bars.

**Method:**
1. **Prepare:** toast the oats in a dry pan for 4–5 minutes, then blitz. Heat the oven to 150 °C fan with a metal tray inside.
2. **Mix:** whisk the whites to soft peaks. Mix the oats, honey, vanilla, cinnamon and salt, then fold in the whites. Fold in the puffed rice last.
3. **Bake 1:** split between the 2 greased dishes, stand them on the hot tray, and bake for 15 minutes with foil, then ~20 minutes without, until set.
4. **Cut:** cut into bars while warm. Lay them on a baking-paper-lined tray with gaps between them.
5. **Bake 2 (dry):** **120 °C fan for 20–40 minutes**, turning the bars halfway. Weigh every 10 minutes and stop at **204 g in total**.
6. **Cool completely:** at least 1 hour on a rack. Wrapping them warm traps steam, and that causes mould.
7. **Wrap:** each bar in baking paper, then into a zip bag.

**Safety, to be honest about:**
- Whether it's safe out of the fridge depends on **water activity (aw)**, not just % water. Cakes and flapjacks with egg are routinely kept at room temperature once fully baked, so ambient storage for a day is `[ASSUMPTION]` plausible, not proven.
- **To prove it:**
  1. **Home check (not proof of safety):** keep 1 bar in a bag at room temperature for 1, 2 and 3 days. Note the smell, texture, any mould, and whether it's gone soft.
  2. **Real proof:** a food lab water-activity test (target aw below ~0.85 for safety, lower for a longer life) `[GAP]`. This is part of the "speak to food manufacturers or feasibility experts" step E3 suggested.
- Until then: make them fresh, carry them for the day, and tell testers to eat them the same day.

**Pitch impact:** if this works, "deliver chilled" changes to "**keeps in your bag all day**". That removes the biggest practical objection. Don't change the deck until the home check is done.
