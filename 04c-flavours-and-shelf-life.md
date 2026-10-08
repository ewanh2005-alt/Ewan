# 04c — T20 flavours (peanut butter, vanilla) and shelf life

**Date:** 8 Oct 2026 · **Numbers from:** `research/04c_flavour_calcs.py` (uses the `04-nutrition.py` ingredient database). These are calculated values, not lab results.
**Tags:** `[EVIDENCE: source]` · `[ASSUMPTION]` · `[GAP]`

---

## Part 1: Flavours

### What flavour is T20 now?
**Cocoa.** It's a dark, not-very-sweet cocoa bar with a hint of honey, a bit like a brownie with less sugar. Cocoa is the only flavouring, and it also covers the "eggy" taste of the egg whites.

### Four single-bar versions to test (per bar, same method as `04b`)

**Updated 8 Oct: "a little sugar" for recovery.** Honey goes up from 3 g to 6 g (5 g in PB & Vanilla), and the sugar cap goes from 6 g to **8 g per bar**. See "Why a little sugar" below.

| Bar | Protein | Carbs | Sugar | of which from honey | Fat | Fibre | kcal |
|---|---|---|---|---|---|---|---|
| **T20 Cocoa** | 20.9 g | 28.9 g | 7.6 g | 4.9 g | 6.1 g | 6.9 g | 268 |
| **T20 Cocoa & Peanut Butter** | 21.0 g | 27.0 g | 7.9 g | 4.9 g | 8.3 g | 7.0 g | 281 |
| **T20 Peanut Butter & Vanilla** | 21.2 g | 28.4 g | 7.5 g | 4.1 g | 8.8 g | 6.5 g | 291 |
| **T20 Vanilla** | 20.6 g | 30.4 g | 8.0 g | 4.9 g | 5.5 g | 6.5 g | 266 |

All four stay at **≥20 g protein and ≤8 g sugar**. The script checks the sugar cap. The rest of the sugar is natural, mostly milk sugar (lactose) from the quark plus a little from oats.

**Low-sugar version:** use 3 g honey instead. That gives ~5–6 g sugar per bar and keeps the "low sugar" claim (≤5 g per 100 g) for the Cocoa bar.

### Recipes (grams for ONE bar)

| Ingredient | Cocoa | Cocoa & PB | PB & Vanilla | Vanilla |
|---|---|---|---|---|
| Egg whites | 60 | 65 | 65 | 60 |
| Whole egg, beaten | 15 (1 tbsp) | — | — | 15 (1 tbsp) |
| Fat-free quark | 45 | 45 | 45 | 45 |
| Oat bran | 25 | 25 | 27 | 28 |
| Porridge oats | 15 | 10 | 12 | 15 |
| Peanut butter (100% peanuts) | — | 8 (heaped tsp) | 10 (2 tsp) | — |
| Cocoa powder | 4 | 4 | — | — |
| Chia seeds | 2 | 2 | 2 | 2 |
| Honey | 6 (1 tsp) | 6 (1 tsp) | 5 | 6 (1 tsp) |
| Vanilla extract | — | — | 2 (½ tsp) | 3 (¾ tsp) |
| Cinnamon | — | — | — | a pinch (0.5 g) |
| Salt | pinch | pinch | pinch | pinch |

**Method:** the same as `04b-t20-single-bar.md`. Two changes:
- **Peanut butter:** whisk it into the quark first, so it doesn't stay in lumps. Then add the egg whites.
- **Vanilla:** add the vanilla extract with the wet ingredients.

### What changes with each flavour, honestly
- **Peanut butter adds fat.** 8–10 g of peanut butter adds ~4–5 g fat, so these bars sit at **8–9 g fat** instead of ~6 g. To make room, I took out the whole egg and some oats. Fat is still moderate, but don't call these "low fat".
  - Powdered peanut butter (peanut flour with the fat removed) would keep fat at ~6 g. But it's a processed ingredient, which weakens the "kitchen ingredients only" story `[ASSUMPTION]`.
- **Peanut butter adds an allergen** (peanuts). Keep the Cocoa and Vanilla bars nut-free. Make the nut-free bars first, or clean everything between batches. Peanut cross-contact is the most serious allergen risk you'll handle.
- **Vanilla is the hardest flavour.** Without cocoa there's nothing to cover the egg-white taste, so expect "eggy" feedback first. If that happens:
  - add another pinch of cinnamon, or
  - swap 10 g egg white for 10 g quark.
- **Use pure vanilla extract, not "vanilla flavouring".** Flavourings can contain sugar or glucose syrup and read badly on an ingredient list. The extract is a small amount, so its sugar is tiny (~0.4 g).
- **Weigh the honey.** 1 g of honey is ~0.8 g sugar, so a heavy pour can push Vanilla (8.0 g) over the cap. Squeeze it straight onto the scales.
- **What the interviews say about peanut butter:** nothing directly, so peanut butter as a flavour preference is an `[ASSUMPTION]`. The research we have:
  - Perfect Bar sells its peanut butter bar as "the Original" `[EVIDENCE: C39]`.
  - Peanut butter was in your original ingredient list.
  - Test it in the taste test rather than assume.

### Why a little sugar (and what the evidence really says)
**Decision (Ewan, 8 Oct):** add a little fast sugar (honey) for refuelling after training.

| Claim | Verdict | Evidence |
|---|---|---|
| Fast sugars straight after training refill muscle glycogen (stored carbs) faster | ✅ **True, mainly when the next session is within ~6–8 h** (two-a-days, tournaments). With a longer gap, total carbs over the day matter more | 2003 review `[EVIDENCE: S23]`; 2015 review `[EVIDENCE: S24]` |
| Two-a-days, long sessions and endurance athletes benefit most | ✅ **True.** Carbs clearly help a second session the same day | *Nutrients* 2022 systematic review, 49 studies `[EVIDENCE: S25]` |
| Sugar + protein increases muscle repair and lowers breakdown | ⚠️ **Overstated.** With ~20–25 g protein, adding even 50 g carbs raised insulin 5-fold but did **not** increase muscle building or reduce breakdown. T20 already has ~21 g protein | Staples et al. 2011 `[EVIDENCE: S26]`; van Loon & Gibala review `[EVIDENCE: S26]` |
| Typical gym session empties glycogen | ⚠️ **Partly.** A hard multi-set session uses ~25–40% | UNM review `[EVIDENCE: S27]` |

**Health warning on those sources:** the links you found are from 1st Phorm, 33Fuel, Jefit and Fiteg. Most of them sell sports nutrition, so they are **marketing, not evidence**. The first two claims hold up in the research; the "sugar boosts muscle repair" one doesn't.

**What this means for fettle:**
- ~5 g sugar from honey is a **small top-up**, not a full glycogen refill. A refill after a hard session or match needs ~1 g carbs per kg of body weight (~75 g for a 75 kg athlete). The bar gives ~29 g carbs in total.
- **Honest framing:** "~29 g carbs, including a little fast-acting honey, with ~21 g protein for recovery." Don't say the sugar "boosts muscle repair".
- **Match days and two-a-days:** still recommend "T20 + a banana or a glass of milk".
- **Claim impact:** at ~7.6 g sugar per bar (~7 g per 100 g), you **lose the "low sugar" claim** (≤5 g/100 g). You're still well below the real-food bars (10–28 g; see `02-competitor-analysis.md`). On pack, give the number rather than a claim: "under 8 g sugar, from honey, oats and milk".
- **Carb recovery claim:** the authorised claim needs ≥4 g carbs per kg body weight per day and mandatory wording `[EVIDENCE: R1]`. **Don't use it.**
- **Check the T20 in your taste test:** bake 3 g honey vs 6 g honey and see whether people notice.

### Extra Tesco items (on top of the `04b` list)

| Item | What to look for | Approx. price |
|---|---|---|
| Peanut butter | Label says **100% peanuts** (or peanuts + salt). Avoid ones with palm oil or added sugar | ~£2–3.50 `[ASSUMPTION: check app]` |
| Vanilla extract | **"Extract"**, not "flavouring" (e.g. Taylor & Colledge, Nielsen-Massey) | ~£2–4 `[ASSUMPTION: check app]` |
| Ground cinnamon | Any | ~£1 `[ASSUMPTION]` |

### Suggested test plan
1. Bake one of each over two evenings.
2. Score each one: taste 1–9, texture 1–5, and how eggy it is (1–5).
3. Get 5 people to blind-rank them, with no labels. Ask C8 and C9 (taste "super important") and C3 (sceptical about taste).
4. Keep the best 2–3 for the pilot.

---

## Part 2: Shelf life, and could this work like Simmer Eats?

### The short answer
**Yes. As it stands, T20 is a fresh, chilled product, much closer to a Simmer Eats meal than to a Grenade bar.** It can't sit in a cupboard for months without being reformulated, and that would mean powders, which is the thing that makes it different. A short shelf life fits the "real food, baked this week" story, but it shapes the whole business model.

### Why it doesn't last long
- T20 is a baked egg and dairy product, and it's still **~40% water** after baking. That's calculated from the bake-loss model in `04-nutrition.py` `[ASSUMPTION until you send tin weights]`.
- Raw egg has a water activity of about **0.96** `[EVIDENCE: S20]`. Water activity measures how much water is free for microbes to use; most harmful bacteria can't grow below **0.85**. Mould needs it below **~0.70**, and for full stability it needs to be below **0.6** `[EVIDENCE: S20, S21]`.
- A moist baked bar like ours is almost certainly well above 0.85, so it needs **chilling and a use-by date**, like a quiche or a chilled ready meal `[ASSUMPTION: not measured; a lab can measure water activity]`.
- Lab bars (Grenade, Warrior) last 9–12 months because they're dry `[ASSUMPTION: typical, not measured]` and use powders, polyols and humectants (ingredients that hold on to water).

### How the comparisons handle it

| Product | Storage | Life | How |
|---|---|---|---|
| **Simmer Eats** (UK chilled ready meals) | Fridge, ≤5 °C | **Up to 5 days**; freeze on arrival if you won't eat them in time | Cooked fresh, DPD delivery in insulated packaging that keeps them chilled until 10 pm on delivery day `[EVIDENCE: C40, C41]` |
| **Perfect Bar** (US "fresh" protein bar) | Fridge (recommended) | Brand says **about a week out of the fridge** and still safe | Low-moisture nut butter + honey + powders. Chilled for texture, not safety `[EVIDENCE: C39 brand claim]` |
| **Lab bars** (Grenade, Warrior RAW) | Cupboard | ~9–12 months | Dry; isolates, polyols, humectants |
| **fettle T20** | **Fridge** | **3 days for home testing**; a realistic commercial target with evidence is maybe 5–7 days `[ASSUMPTION]` | Baked egg/dairy, ~40% water, no preservatives |
| **fettle T20, frozen** | Freezer | **Probably 2–3 months** for good quality `[weak evidence: S22, recipe and home-cooking sites]` | Bake, cool, wrap one by one, freeze. Customer thaws overnight in the fridge |

**Perfect Bar isn't the model to copy for shelf life.** It sits in a fridge but is basically a dry nut-butter bar. Ours is closer to a protein-packed baked good.

### Three routes

| Route | How it works | Fits fettle? | Main problem |
|---|---|---|---|
| **A. Fresh, baked to order (the Simmer model)** | Orders close Sunday → bake Monday → deliver Tue/Wed → use-by ~5 days | ✅ Best fit for the pilot | Delivery cost per order. Simmer charges ~£7. On a £2 bar you'd need **boxes of 10–12** or a hand-delivered squad order `[ASSUMPTION]` |
| **B. Fresh + frozen** | Same bake, but bars are frozen for a stock buffer. Ship or hand over frozen; the customer keeps them in the freezer and thaws one the night before | ✅ Good add-on | Texture after thawing is untested. The egg may go rubbery `[GAP: test it]` |
| **C. Long-life (cupboard)** | Reformulate to dry: egg-white powder, milk powder, less water (the `SH_cocoa_peanut` route in `04-nutrition.py`) | ❌ Not now | You lose fresh eggs and milk, and you end up much closer to the competitors. Needs a co-manufacturer with 10k–25k minimum orders `[EVIDENCE: P15]` |

### Recommendation
1. **Pilot (now to Week 13):** Route A, kept local.
   - Bake to order weekly and hand-deliver in Durham, starting with squad orders through the S&C coach. A squad order is predictable demand, which a short shelf life needs.
   - Keep everything chilled at ≤5 °C, with a cool bag and ice packs for drop-offs.
   - Use a **3-day use-by** until you have evidence for longer.
2. **Test freezing in Week 6.**
   - Freeze 3 bars.
   - Thaw one at 1 week, one at 2 weeks and one at 4 weeks.
   - Score each against a fresh bar.
   - If it holds up, offer "freezer packs". That's the answer to "what if I don't eat them in 3 days?".
3. **Later (after the pitch):** online national delivery like Simmer, as a weekly box with insulated packaging and next-day courier. This is only worth it once you have repeat customers and a lab-backed shelf life.
4. **In the pitch, turn the weakness into the point:** *"Baked this week, not 12 months ago."* The short shelf life is proof there's nothing artificial keeping it alive. Judges will ask about it, so have the frozen-route and squad-order answers ready.

### What a real shelf life needs (before selling beyond friends)
- **Register as a food business** (28 days' notice) and write a simple HACCP plan, the hazard-and-controls plan your council will ask for. The baking step must reach a **centre temperature of 75 °C**.
- **Evidence for the use-by date.** The UK industry guidance for chilled ready-to-eat food is the Chilled Food Association guidance, which the FSA endorses `[EVIDENCE: R11]`. Food Standards Scotland says there's no single standard method; you have to evidence and verify whatever date you choose `[EVIDENCE: R12]`. In practice that means:
  - a microbiology test on bars at day 0 and at the end of their shelf life, and possibly a challenge test, from a UK lab such as Eurofins `[EVIDENCE: R13]`
  - cost: `[GAP]`, so ask for quotes. Your council's environmental health officer (EHO) can advise first, sometimes free.
- **Labels:** "Keep refrigerated at 0–5 °C. Use by [date]. Once opened, eat immediately." For frozen: "Freeze on day of purchase. Defrost overnight in the fridge and eat within 24 hours."
- **Home sensory test you can do now:** bake 4 bars, keep them in the fridge, and taste one on day 1, 2, 3 and 5. Note smell, texture and any moisture or mould. That's **not** safety evidence, but it tells you where quality drops off.

### Gaps
- Measured water activity and moisture of a real T20 bar `[GAP]`
- Texture after freezing and thawing `[GAP]`
- Lab test costs `[GAP]`
- Courier and insulated-packaging cost per box `[GAP]`
- Whether athletes will plan ahead and order weekly `[GAP: ask at interviews]`
