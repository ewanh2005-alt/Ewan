# 04d — Test bars: Chocolate Peanut Butter, Vanilla, Banana Bread (one bar each)

**Date:** 8 Oct 2026 (updated) · **Numbers from:** `research/04d_recovery_calcs.py` (ingredient database in `04-nutrition.py`, prices in `04-costing.py`). These are calculated values, not lab results.
**Who it's for:** athletes refuelling after training or matches. That's the coached athletes (C1, C7, C10) and the gym-goers in `03-persona.md`.

**What changed (Ewan, 8 Oct):**
- **Back to T20 size.** The 355–395 kcal bars were too big.
- **Banana and cinnamon are in the Banana Bread bar only.**
- **Egg whites stay.** Their protein makes the 20 g target possible at this size.

---

## The three bars

| Bar | Protein | Carbs | Sugar | of which honey/banana | Fat | Sat fat | Fibre | kcal | Ingredient cost |
|---|---|---|---|---|---|---|---|---|---|
| **Chocolate Peanut Butter** | **21.0 g** | **28.0 g** | 7.9 g | 4.9 g | 8.0 g | 1.8 g | 7.1 g | 282 | £1.09 |
| **Vanilla** | **20.4 g** | **29.8 g** | 8.0 g | 4.9 g | 5.4 g | 1.1 g | 6.1 g | 262 | £1.16 |
| **Banana Bread** | **20.5 g** | **30.7 g** | 6.9 g | 4.3 g | 5.4 g | 1.1 g | 7.0 g | 267 | £0.98 |

**Spec, checked by the script:**
- protein ≥20 g
- carbs ≥25 g
- sugar ≤8 g
- fat ≤9 g
- ≤285 kcal

All three pass. The sugar not from honey or banana is natural, mainly milk sugar from the quark.

### Why egg whites (from normal eggs) and not whole eggs only
You said to use normal eggs if possible, and to keep egg whites if the macros needed them. **They do.**
- **Whole egg only:** a Chocolate Peanut Butter bar made with just a whole egg comes out at **~300 kcal and 11 g fat**. That's over your target.
- **With whites:** **282 kcal and 8 g fat.**
- **You still buy normal boxed eggs.** Separate 2 eggs per bar, and use the yolks elsewhere (scrambled eggs, an omelette). Liquid egg white in a carton is optional; it just saves separating.

### Why these numbers suit an athlete after training
- **~20–21 g protein:** one recovery dose (~0.25–0.3 g per kg) for most athletes up to ~80 kg `[EVIDENCE: 01d]`.
- **~28–31 g carbs, mostly from oats:** athletes tend to eat too few carbs `[EVIDENCE: 01d, Jenner 2019]`.
- **~4–5 g fast sugar from honey or banana:** helps most on two-a-days and tournaments `[EVIDENCE: S23, S25]`. Don't claim it boosts muscle repair `[EVIDENCE: S26]`.
- **~6–7 g fibre from oats, oat bran and chia:** everyday gut health `[EVIDENCE: 01d]`.
- **Match days and two-a-days:** add a banana or a glass of milk for more carbs.

---

## Recipes (grams for ONE bar)

| Ingredient | Choc Peanut Butter | Vanilla | Banana Bread | Kitchen measure |
|---|---|---|---|---|
| Egg whites | 65 g | 60 g | 60 g | 2 large egg whites (top up from a 3rd if short) |
| Whole egg, beaten | — | 15 g | 15 g | 1 tbsp of a beaten egg |
| Fat-free quark | 45 g | 45 g | 45 g | 3 level tbsp |
| Oat bran | 25 g | 27 g | 25 g | ~3 heaped tbsp |
| Porridge oats | 12 g | 15 g | 15 g | ~2 tbsp |
| Peanut butter (100% peanuts) | 7 g | — | — | 1 heaped tsp |
| Cocoa powder | 4 g | — | — | 2 level tsp |
| Honey | 6 g | 6 g | — | 1 tsp |
| Vanilla **extract** | — | 3 g | — | ¾ tsp |
| Ripe banana, mashed | — | — | 35 g | ~⅓ of a banana |
| Ground cinnamon | — | — | 0.5 g | a good pinch |
| Chia seeds | 2 g | 2 g | 2 g | ½ tsp |
| Salt | pinch | pinch | pinch | — |

**Weigh everything on scales**, especially the honey. The Vanilla bar is right on the 8 g sugar limit.

---

## Shopping list (Tesco: enough for 3–4 rounds of all three)

| # | Item | Look for | Approx. price |
|---|---|---|---|
| 1 | Eggs | Tesco Large Free Range Eggs, 12 (2 eggs per bar) | £3.30 |
| 2 | Quark | Tesco Fat Free Quark 250 g (each round of 3 bars uses ~135 g) | £1.30 |
| 3 | Oat bran | Tesco Oat Bran 675 g (plain oat bran, **not** bran-flakes cereal) | £2.65 |
| 4 | Porridge oats | Tesco Scottish Porridge Oats 1 kg | ~£1.35 |
| 5 | Peanut butter | Label says **100% peanuts** (or peanuts + salt) | ~£2–3.50 `[check app]` |
| 6 | Cocoa powder | Tesco Cocoa Powder 250 g (unsweetened, **not** hot chocolate) | ~£2.99 |
| 7 | Honey | Tesco Squeezy Clear Honey 340 g | £1.19 |
| 8 | Vanilla extract | Says **"extract"**, not "flavouring" | ~£2–4 `[check app]` |
| 9 | Chia seeds | Tesco Chia Seeds 100 g | £1.20 |
| 10 | Bananas | 1–2 ripe (brown spots) | ~17p each |
| 11 | Ground cinnamon | Any small jar (Banana Bread only) | ~£1 `[check app]` |
| — | Salt | At home | — |
| | **Total** | | **≈ £20** (most of it lasts many bakes) |

*Optional:* liquid egg white (e.g. Two Chicks 500 g, ~£3.48) saves separating eggs. Tesco stock isn't confirmed.

**Equipment:**
- digital scales (1 g)
- a **small** tin or ovenproof dish, about 12 × 8 cm (a mini loaf tin works), so the batter sits ~2.5 cm deep
- baking paper, a bowl, a fork, a cup
- a probe thermometer is recommended

---

## How to cook ONE bar (≈ 45 minutes, most of it waiting)

1. **Heat the oven** to **160 °C fan / 180 °C conventional / gas 4**.
2. **Line the tin** with baking paper. **Weigh the empty tin** and write it down.
3. **Separate 2 eggs.** Put the whites in a bowl (weigh: you want 60–65 g).
   - **Vanilla and Banana Bread:** beat a third egg (or one of the yolks + a little white) in a cup and add **1 tablespoon (15 g)** to the bowl.
   - **Chocolate Peanut Butter:** no whole egg.
4. **Add the wet ingredients and flavour, then whisk** for ~30 seconds until smooth:
   - **Chocolate Peanut Butter:** quark + peanut butter + honey. **Whisk the peanut butter into the quark first** so there are no lumps.
   - **Vanilla:** quark + honey + vanilla extract.
   - **Banana Bread:** mash the banana with a fork until almost smooth, then whisk it in with the quark. No honey.
5. **Add the dry ingredients:**
   - all bars: oat bran, oats, chia and a pinch of salt
   - **Chocolate Peanut Butter:** also cocoa
   - **Banana Bread:** also cinnamon

   Stir until there are no dry patches. It will be a thick, wet batter.
6. **Rest 10 minutes.** The oat bran and chia soak up liquid, so the bar holds together.
7. **Pour into the tin** and level it. **Weigh the full tin.**
8. **Bake 25–30 minutes** (Banana Bread: up to 35), until the top is firm and springs back, the edges pull away and a skewer comes out clean. With a probe, the **centre must reach 75 °C**.
9. **Weigh straight out of the oven** and write it down.
10. **Cool** 10 minutes in the tin, lift out, cool fully on a rack, then **chill 1 hour**. It firms up as it cools.
11. **Score it:**
    - taste 1–9
    - texture 1–5 (1 = wet or eggy, 5 = firm and bar-like)
    - sweetness: too little / right / too much
12. **Store** covered in the fridge and **eat within 3 days**.

**Send me the three weights** (empty tin, full tin, baked) for each bar, and I'll correct the figures.

### If it's not right

| Problem | Fix next time |
|---|---|
| Too wet or custard-like | Bake 5–10 min longer, or swap 10 g quark for 10 g extra oat bran |
| Too eggy | Choc PB: 1 g more cocoa. Vanilla: ½ tsp more vanilla. Or swap 10 g egg white for 10 g quark |
| Dry or crumbly | Bake 5 min less; add 1 tsp milk |
| Not sweet enough | Choc PB: 1 g more honey is OK (sugar ~8.7 g). Banana Bread: riper banana. Vanilla is already at the limit |
| Falls apart | Rest 15 min before baking; add another ½ tsp chia |

### Baking order and allergens
- **Bake Vanilla and Banana Bread first, then Chocolate Peanut Butter.** Wash everything between bars.
- **All three contain egg, milk (quark) and oats (gluten).** Chocolate Peanut Butter also contains **peanuts**.
- Don't give test bars to anyone with these allergies. Register as a food business (free; 28 days' notice) before giving bars out regularly.

### What you can say
- "~20 g protein from eggs, quark and oats. No protein powder, no sweeteners."
- **"High protein":** ~30% of energy comes from protein, above the 20% the claim needs. Check the final label.
- **Don't say "low sugar":** the Chocolate PB and Vanilla bars are at ~7 g sugar per 100 g, over the 5 g limit for that claim (Banana Bread ~5.4 g, also just over).

*Superseded:* the bigger R1–R4 recovery bars (355–395 kcal), 8 Oct.
