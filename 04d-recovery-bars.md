# 04d — Recovery bars for the hard-training athlete (single-bar recipes)

**Date:** 8 Oct 2026 · **Numbers from:** `research/04d_recovery_calcs.py` (ingredient database in `04-nutrition.py`, prices in `04-costing.py`). These are calculated values, not lab results.
**Who it's for:** the athlete who trains a lot (twice a day, matches, tournaments) and needs to refuel and repair afterwards. This is the "coached athlete" sub-group in `03-persona.md`: C1 (pro footballer), C7 (rugby), C10 (trains twice a day), plus the S&C coach (E1) and the professor's "high carbs" (E2).
**What's changed from T20:**
- **Whole eggs only, no separated egg whites.** Quark makes up the protein.
- **More carbs** (about 38–41 g instead of about 26–29 g).
- **A little fast sugar** from honey or banana.
- **Updated 8 Oct:** banana is now used for carbs and sweetness in two bars. R3 is renamed **Banana Bread** with more banana, and **R4 Chocolate Banana** is new: a nut-free chocolate bar sweetened only by banana, with no honey.

---

## The four bars (one bar each)

| Bar | Protein | Carbs | Sugar | of which honey/banana | Fat | Sat fat | Fibre | kcal | Ingredient cost |
|---|---|---|---|---|---|---|---|---|---|
| **R1 Chocolate Peanut Butter** | **25.8 g** | **37.9 g** | 9.6 g | 5.7 g | 13.8 g | 3.5 g | 7.6 g | 394 | £1.01 |
| **R2 Vanilla & Honey** | **23.9 g** | **40.2 g** | 9.8 g | 5.7 g | 10.3 g | 2.4 g | 7.1 g | 364 | £1.10 |
| **R3 Banana Bread** | **23.3 g** | **41.0 g** | 9.5 g | 6.1 g | 10.0 g | 2.4 g | 8.2 g | 364 | £0.85 |
| **R4 Chocolate Banana** | **24.3 g** | **41.4 g** | 9.5 g | 6.1 g | 11.1 g | 3.0 g | 9.1 g | 380 | £0.97 |

The script checks each bar against this recovery spec: **protein ≥20 g, carbs ≥35 g, sugar ≤10 g, fat ≤15 g**. All four pass. The sugar not from honey or banana is natural, mainly milk sugar from the quark.

### Why this is the best recipe for this athlete
- **Protein about 23–26 g:** that's one full recovery dose of ~0.3 g per kg of body weight for a 75–85 kg athlete `[EVIDENCE: 01d, ACSM 2016 / ISSN 2017]`.
- **Carbs about 38–41 g:** athletes in team sports tend to eat **too few carbs, not too little protein** `[EVIDENCE: 01d, Jenner 2019]`. The carbs come mostly from oats, with a little fast sugar on top.
- **A little fast sugar (about 5–6 g from honey or banana):** it helps most when the next session is within about 6–8 hours (two-a-days, tournaments) `[EVIDENCE: S23, S25]`. It **doesn't** add extra muscle repair when protein is already ~20 g+ `[EVIDENCE: S26]`, so don't claim that. Banana also adds moisture, natural sweetness and a flavour people already rebuy ("banana bread", `02c`).
- **Fibre about 7–9 g, from oats, oat bran and banana:** good for everyday gut health `[EVIDENCE: 01d]`. Sell it as an after-training bar, never a pre-training one.
- **Whole eggs work.** Quark carries the protein, so you **don't need egg whites** to reach 20 g+. The trade-off:
  - about 5 g more fat (from the yolk) and ~50 kcal more than an egg-white version
  - fat is still moderate (10–14 g), and saturated fat is low (2.4–3.5 g)
- **It's a big bar**, about 140–160 g baked and ~365–395 kcal: a "refuel after a match" bar, not a snack. For a lighter gym day, eat half.
  - Honest note: the professor's guide (~10 g protein per 100 kcal) favours leaner bars. These are ~6.5 g per 100 kcal because they carry more carbs. **For this athlete, carbs win.**

### Recipes (grams for ONE bar)

| Ingredient | R1 Choc PB | R2 Vanilla | R3 Banana Bread | R4 Choc Banana | Kitchen measure |
|---|---|---|---|---|---|
| **Whole egg** (large) | 1 (~58 g) | 1 (~58 g) | 1 (~58 g) | 1 (~58 g) | 1 egg, cracked |
| Fat-free quark | 75 g | 75 g | 70 g | 70 g | ~5 level tbsp |
| Porridge oats | 30 g | 35 g | 30 g | 30 g | ~4–5 tbsp |
| Oat bran | 20 g | 20 g | 20 g | 20 g | ~2½ heaped tbsp |
| Peanut butter (100% peanuts) | 7 g | — | — | — | 1 heaped tsp |
| Cocoa powder | 5 g | — | — | 5 g | 2½ level tsp |
| Ripe banana, mashed | — | — | 50 g | 50 g | ~½ a medium banana (peeled) |
| Honey | 7 g | 7 g | — | — | ~1 tsp |
| Vanilla **extract** | — | 4 g | — | — | ~1 tsp |
| Ground cinnamon | — | a pinch (0.5 g) | 1 g | — | ½ tsp for R3 |
| Chia seeds | — | 2 g | 2 g | 2 g | ½ tsp |
| Salt | pinch | pinch | pinch | pinch | — |

---

## Shopping list (Tesco: enough for 2–3 test rounds of all four)

| # | Item | Look for | Approx. price |
|---|---|---|---|
| 1 | Eggs | Tesco Large Free Range Eggs, 12 | £3.30 |
| 2 | Quark | Tesco Fat Free Quark 250 g. **Buy 2 tubs**: each round of 4 bars uses ~290 g | £1.30 each |
| 3 | Porridge oats | Tesco Scottish Porridge Oats 1 kg (any plain rolled oats) | ~£1.35 |
| 4 | Oat bran | Tesco Oat Bran 675 g (plain oat bran, **not** bran-flakes cereal) | £2.65 |
| 5 | Peanut butter | Label says **100% peanuts** (or peanuts + salt), no palm oil or sugar | ~£2–3.50 `[check app]` |
| 6 | Cocoa powder | Tesco Cocoa Powder 250 g (unsweetened, **not** hot chocolate) | ~£2.99 |
| 7 | Honey | Tesco Squeezy Clear Honey 340 g | £1.19 |
| 8 | Vanilla extract | Says **"extract"**, not "flavouring" | ~£2–4 `[check app]` |
| 9 | Ground cinnamon | Any | ~£1 `[check app]` |
| 10 | Chia seeds | Tesco Chia Seeds 100 g | £1.20 |
| 11 | Bananas | 3–4 loose, **ripe** (brown spots = sweeter, better banana bread) | ~17p each |
| — | Salt | At home | — |
| | **Total** | | **≈ £22** (most of it lasts many bakes) |

Prices are from Tesco listings found 7–8 Oct 2026 (`research/sources.md`) or marked "check app". **Equipment:** digital scales (1 g), a **1 lb / 450 g loaf tin** (about 16 × 10 cm) or a similar small dish, baking paper, a bowl and fork. A probe thermometer (~£10) is recommended.

---

## How to cook ONE bar (≈ 50 minutes, most of it waiting)

**Same steps for all four bars. The differences are in steps 4 and 5.**

1. **Heat the oven** to **160 °C fan / 180 °C conventional / gas 4**.
2. **Line the loaf tin** with baking paper. **Weigh the empty lined tin** and write it down.
3. **Crack 1 egg** into a bowl. Whisk with a fork for 20 seconds.
4. **Add the wet ingredients and flavour.** Whisk until smooth.
   - **R1 Choc PB:** quark + **peanut butter** + honey. Whisk the peanut butter into the quark well so there are no lumps.
   - **R2 Vanilla:** quark + honey + **vanilla extract**.
   - **R3 Banana Bread and R4 Choc Banana:** **mash the banana** on a plate with a fork until almost smooth, then whisk it in with the quark. No honey; the banana sweetens it.
5. **Add the dry ingredients:**
   - all bars: oats, oat bran and a pinch of salt
   - **R1:** cocoa
   - **R2 and R3:** chia and cinnamon
   - **R4:** cocoa and chia

   Stir until there are no dry patches. It should be a thick, scoopable batter, like a stiff porridge. The banana bars are a little wetter, which is normal.
6. **Rest 10 minutes.** The oats, oat bran and chia soak up liquid, which helps the bar hold together.
7. **Spoon into the tin** and press it flat and even, about 2.5–3 cm deep. **Weigh the full tin** (batter ≈ 200–235 g).
8. **Bake 30–35 minutes** (banana bars: allow up to 40 min), until the top is firm and springs back, the edges pull away from the paper, and a skewer in the middle comes out clean. With a probe, the **centre must reach 75 °C**.
9. **Weigh straight out of the oven** and write it down (you should lose ~50–70 g as steam).
10. **Cool** 10 minutes in the tin, lift out on the paper and cool fully on a rack. **Chill 1 hour**: it firms up as it cools.
11. **Taste and score:**
    - taste 1–9
    - texture 1–5 (1 = wet or eggy, 5 = firm and bar-like)
    - sweetness: too little / right / too much
12. **Store** covered in the fridge. **Eat within 3 days**, or wrap and freeze (thaw overnight in the fridge).

**Send me the three weights** (empty tin, full tin, baked). Then I can correct the moisture and per-100 g figures.

### If it's not right

| Problem | Fix next time |
|---|---|
| Wet in the middle | Bake 5–10 min longer, or press thinner in a wider dish |
| Too eggy | Add another pinch of cinnamon; for R1, 1 g more cocoa |
| Dry or crumbly | Bake 5 min less; add 1 tbsp milk to the batter |
| Not sweet enough | R1/R2: 2 g more honey (adds ~1.6 g sugar, still ≤10 g). R3/R4: use a riper banana rather than more banana, as they're already at 9.5 g sugar |
| Falls apart | Rest 15 min before baking; add ½ tsp chia (R1 too) |
| Too big | Halve it. Each half is ~12 g protein, ~19 g carbs |

### Order to bake (allergen safety)
**Bake R2, R3 and R4 first (nut-free), then R1** (peanut). Wash the bowl, fork and tin between bars.

**Allergens:**
- all four: **egg, milk** (quark) and **oats** (gluten)
- R1 also contains **peanuts**

Don't give test bars to anyone with these allergies. Register as a food business (free; 28 days' notice) before giving bars to people regularly.

---

## How to use it with athletes
- **Eat within ~1 hour** of training or a match, with water.
- **Two-a-days or tournaments:** have the bar **plus a banana or a glass of milk** (+20–25 g fast carbs). A full glycogen refill needs ~1 g of carbs per kg of body weight `[EVIDENCE: S23]`, more than any bar holds.
- **Pitch line:** *"Refuel like you'd cook it: ~25 g protein and ~40 g carbs from eggs, quark and oats, with a little honey, and nothing else."*
- **Claims:**
  - Don't say "low sugar"; these bars are at ~6–7 g sugar per 100 g.
  - Don't use the official carbohydrate-recovery claim (it needs ≥4 g per kg per day and mandatory wording).
  - Don't say the sugar "boosts muscle repair".
  - You can say "high protein" (>20% of energy from protein: ~25–26% here) once the label is checked.
