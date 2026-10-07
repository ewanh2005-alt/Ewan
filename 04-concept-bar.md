# 04 — The Concept Bar

**Date:** 7 Oct 2026 · **Numbers from:** `04-nutrition.py` → `04-nutrition-tables.md`; `04-costing.py` → `04-costing.csv`. Re-run both scripts after any recipe change; don't edit numbers by hand.
**Status:** paper recipe. Every number is `[ASSUMPTION]` until (1) a kitchen trial, (2) supplier spec sheets and (3) one lab analysis.

---

## 1. Target spec (per bar)

| | **Target** | Our hero calc (Cocoa & Peanut) | Why this number |
|---|---|---|---|
| Weight | **80 g** | 80 g | Fits ~20 g protein + ~37 g carbs. Smaller than the inherited 98 g draft; 6–25 g heavier than Styrkr/Grenade |
| Energy | **≤300 kcal** | 295 kcal | A snack that bridges to a meal, not a meal. Inherited 345 kcal was too much for a gym-goer `[ASSUMPTION]` |
| Protein | **~20 g** | 19.7 g | 0.25 g/kg per serving (ISSN) or 20–40 g; 0.25–0.31 g/kg covers a ~65–80 kg adult `[EVIDENCE: S3, S4]` |
| Carbohydrate | **35–40 g** | 37.1 g | Kick-starts refuelling. Full glycogen refuel needs ≥1.2 g/kg/h (≈85 g/h at 70 kg), and protein helps most when carbs are below ~0.8 g/kg/h `[EVIDENCE: S2]`, which is exactly the bar's range |
| of which sugars | ideally ≤20 g | **23.3 g** | ⚠️ Misses. See §3e |
| Fibre | **5–6 g** | 5.2 g | Enough for "high fibre" (≥6 g/100 g); low enough for after training. See §3b |
| Fat | ≤8 g | 6.4 g | Fat slows digestion and adds calories |
| Saturates | ≤2 g | 1.4 g | |
| Salt | ≤0.8 g | 0.56 g | Some sodium is useful after sweating; mostly from egg white and milk powder |

**Format:** one 80 g bar, scored into **2 × 40 g halves** (each ~10 g protein). Half after a light session; whole bar after a hard one. This is a simpler, testable version of the inherited 4-segment "dose" idea `[ASSUMPTION: test in pilot]`.

## 2. The three flavours (+ one comparison)

| | A. **Cocoa & Peanut** (hero) | B. **Raspberry & Almond** | C. **Honey Oat & Sea Salt** (nut-free recipe) | S. Strict whole-food (comparison) |
|---|---|---|---|---|
| kcal | 295 | 294 | 288 | 323 |
| Protein | 19.7 g | 19.5 g | 19.7 g | **10.6 g** |
| Carbs (sugars) | 37.1 (23.3) | 36.9 (23.8) | 38.0 (23.4) | 37.8 (17.5) |
| Fibre | 5.2 g | 5.1 g | 4.7 g | 7.4 g |
| Fat (sat) | 6.4 (1.4) | 6.5 (0.7) | 5.3 (1.0) | 12.7 (2.5) |
| Salt | 0.56 g | 0.57 g | 0.75 g | 0.01 g |
| High protein | ✅ 26.8% energy | ✅ | ✅ | ❌ 13.1% (only "source of") |
| High fibre | ✅ 6.5 g/100 g | ✅ 6.3 | ❌ 5.9 (source only) | ✅ |
| Pilot cost/bar | £1.07 | £1.33 | £1.02 | — |
| Scale cost/bar | £0.71 | £0.85 | £0.70 | — |

Full gram-level recipes, 1 kg batch quantities, ingredient lists and back-of-pack tables are in **`04-nutrition-tables.md`**.

### Per-bar formulation (g)

| Ingredient | A | B | C | Role |
|---|---|---|---|---|
| Dates (Deglet Nour, pitted) | 20 | 19 | 18 | Binder, carbs, sweetness |
| Rolled oats | 14 | 14 | 16.4 | Carbs, fibre, texture |
| Skimmed milk powder | 12 | 13 | 12 | Protein (whey + casein), carbs |
| Dried egg white (pasteurised, food grade) | 12 | 12 | 12 | Protein (9.6 g) |
| Oat bran | 8 | 8 | 8 | Fibre (beta-glucan), protein |
| Peanut butter / ground almonds / pumpkin seeds | 8 | 8 | 7 | Fat, binding, flavour |
| Honey | 4 | 4 | 6 | Binding, flavour |
| Cocoa / freeze-dried raspberry / cinnamon + salt | 2 | 2 | 0.4 + 0.2 | Flavour |
| **Total** | **80** | **80** | **80** | |

**1 kg batch = 12.5 bars** (≈11–12 after trimming).

### Method (no-bake, cold-formed; kitchen pilot)
1. Blitz dates (+ honey, nut butter) to a paste in a food processor.
2. Separately mix oats, oat bran, milk powder, egg-white powder, cocoa/flavour, salt.
3. Combine and pulse until it holds when squeezed. If too dry, add water **1 tsp at a time** (every addition shortens shelf life; record it).
4. Press firmly into a lined 20 × 20 cm tin (or segmented mould) to a set depth; weigh one bar to check 80 g ± 4 g.
5. Chill 2 h, cut, wrap immediately and label.

**Optional bake** at ~160 °C for 10–12 min firms the bar and lowers moisture, but browns milk powder and changes taste. Test both in round 1.

### Binding and shelf life `[ASSUMPTION: all to test]`
- **Water activity** drives shelf life. Date/honey bars typically sit around aw 0.55–0.65. Lab test aw on pilot bars (~£20–40 per test via a food lab `[ASSUMPTION]`).
- **Hardening:** high-protein bars go hard over weeks as moisture moves into protein powders. Milk powder hardens more than egg white. Trial a 2-week and a 4-week keep at room temperature.
- **Rancidity:** nut butters and oat bran fats can go stale; use stabilised oat bran and keep packs sealed.
- **Pilot shelf-life claim:** be conservative (e.g. "best before 14 days") until tested.

## 3. The honest tensions

### 3a. Whole food vs high protein
| Route | Protein (80 g bar) | What we can honestly say |
|---|---|---|
| **Strict whole food** (oats, dates, nuts, seeds) | **10.6 g** (calculated) | "Made only from whole foods". But only "source of protein", and no better than Forza (12 g) |
| **Whole food + milk powder + dried egg white** (recommended) | **19.7 g** | "Made from real food ingredients. No protein isolates, no sweeteners, no palm oil." **Not** "100% whole food": milk powder and egg-white powder are dried, single-ingredient foods, but they are processed |
| Add pea protein / whey isolate | 20 g+ easily | Loses the point of difference vs Grenade and Myprotein |

**Recommendation:** route 2. It's the only one that clears 20% energy from protein *and* keeps a defensible ingredient story. RXBAR used the same egg-white approach.
**What would change it:** if interviews show buyers don't care about isolates, use whey protein concentrate instead: cheaper, less hardening, easier to make.

### 3b. Fibre vs fast recovery
- **What the evidence says:**
  - The ACSM advises **low fibre before** exercise to avoid gut trouble.
  - Mancin, Burke & Rollo (2025) argue athletes should reach **~30 g/day**, ramping over ~6 weeks if they eat under 20 g, for gut-microbiome benefits.
  - The same paper notes there are **no RCTs** on athlete fibre intake, and none specifically on fibre in the post-exercise window `[EVIDENCE: S1]`.
- **Fibre also slows gastric emptying.** That isn't an issue for a snack eaten once the session is over, but it argues against a very high dose.
- **Recommendation: 5–6 g per bar, from oats and oat bran only.** That's ~20% of a 30 g/day target, gives a "high fibre" claim, and avoids chicory/inulin, which are high-FODMAP and linked to gut symptoms (inherited research). The inherited 11 g target is **dropped**: more gut risk, and it pushed the bar to 98 g.
- **What would change it:** if pilot gut-comfort scores are fine at 5 g, test 7–8 g in round 2.

### 3c. Calories and portion
- 80 g / 295 kcal is a big snack for a 60 kg runner after an easy session, about right for a 90 kg rugby player after a hard one.
- Scoring into halves gives both a sensible portion without two SKUs.
- **Don't market it as a meal replacement.**

### 3d. Claims check (GB)
Full conditions are in the sources (R1–R3). ✅ = qualifies on our calculation, **subject to lab verification**.

| Claim | Condition | A | B | C | Use? |
|---|---|---|---|---|---|
| "High protein" | ≥20% energy from protein | ✅ | ✅ | ✅ | **Yes**, after lab test |
| "Source of fibre" | ≥3 g/100 g | ✅ | ✅ | ✅ | Yes |
| "High fibre" | ≥6 g/100 g | ✅ (6.5) | ✅ (6.3) | ❌ (5.9) | A and B only, and the margin is small. **Hold until lab-tested** |
| "Protein contributes to a growth in / maintenance of muscle mass" | At least a source of protein | ✅ | ✅ | ✅ | **Yes**, exact authorised wording only (Reg. 432/2012) |
| "Carbohydrates contribute to the recovery of normal muscle function (contraction) after highly intensive and/or long-lasting physical exercise leading to muscle fatigue and the depletion of glycogen stores in skeletal muscle" | Metabolisable carbs (no polyols). Pack **must** say the effect comes from **4 g of carbs per kg body weight, from all sources, in doses, within the first 4 h and no later than 6 h** after such exercise. Adults only | ✅ | ✅ | ✅ | **Optional.** Legal, but long and needs the mandatory wording. Use on back of pack and website only |
| "Recovery bar" as a product name | Could be read as an implied health claim; must be backed by an authorised claim | ⚠️ | ⚠️ | ⚠️ | **Trading Standards check.** Safer: "for after training" |
| "No added sugar" | No added sugars or foods used for sweetening | ❌ (honey, dates) | ❌ | ❌ | **Never** |
| "Natural" / "all natural" | FSA criteria: ingredients from nature, not chemically altered | ⚠️ | ⚠️ | ⚠️ | Avoid as a headline. Dried milk and egg are arguable |
| "Whole food" | No legal definition; must not mislead | ⚠️ | ⚠️ | ⚠️ | Use "**real food ingredients**", not "100% whole food" |
| "No isolates / no sweeteners / no palm oil" | Must be true and not imply competitors are unsafe | ✅ | ✅ | ✅ | Yes, factual |
| "Clean", "superfood", "speeds recovery", "reduces soreness", "repairs muscle", "anti-inflammatory" | Not authorised / not defensible | ❌ | ❌ | ❌ | **Never** |

**Mandatory with any health claim:** a statement on the importance of a varied and balanced diet and a healthy lifestyle (Reg. 1924/2006 Art. 10(2)). Added to the back of pack and the landing page.

**Needs a Trading Standards / regulatory check before use:** (1) "recovery" in the product name or tagline; (2) "real food" and "no isolates" comparative wording; (3) the 2-half portion guidance, if it's linked to body weight. Durham County Council Trading Standards (or Newcastle, wherever you register) offers advice; ask about **Primary Authority**.

### 3e. Sugar (an extra tension I found)
- ~23 g sugar per bar = **29 g/100 g: a RED front-of-pack traffic light.** It comes from dates (~13 g), milk lactose (~6 g) and honey (~3 g).
- Post-exercise, sugars are useful carbohydrate, and Forza (27.6 g) and Styrkr (28.4 g) are higher. **But we can't claim to be "lower sugar" than them.**
- **UK HFSS:** all three recipes score **8–10 on the 2004/05 nutrient profiling model** (≥4 = "less healthy"), even with a generous fibre score, because sugar and energy score high. If bars fall in a regulated category, **large retailers may not be able to promote them on multibuys or at checkouts**, and paid TV/online ads are restricted (small businesses under 250 staff are exempt from the ad rules `[ASSUMPTION: verify]`). Lab protein bars avoid this by using polyols. This is a **retail-scale** issue, not a pilot issue. `[GAP: confirm whether cereal/protein bars are an in-scope HFSS category]`
- **Options:** (a) accept it and frame sugars as "carbs for refuelling" (honest for the use case); (b) replace 5 g dates with oats (≈−3 g sugar) and test whether it still binds; (c) swap honey for a little more nut butter. Test (b) in kitchen round 2.

### 3f. Allergens (14 UK allergens)
| Flavour | Contains | Cross-contact risk in a shared kitchen |
|---|---|---|
| A. Cocoa & Peanut | **Peanuts, milk, egg, cereals containing gluten (oats)** | Almonds (from B) |
| B. Raspberry & Almond | **Nuts (almond), milk, egg, oats** | Peanuts (from A) |
| C. Honey Oat & Sea Salt | **Milk, egg, oats** | **Peanuts and almonds**, unless made on a separate day with a full clean and validated, or in a nut-free kitchen |

- Not suitable for vegans, or people with egg or milk allergy.
- Oats: unless you buy certified gluten-free oats, declare oats (cereal containing gluten) and **don't** claim gluten-free.
- Precautionary "may contain" labels should follow a real risk assessment, not be added by default (FSA guidance).
- **Pilot rule:** make C first after a deep clean, or only offer C as "made in a kitchen that handles peanuts and nuts".

## 4. Costing and price

From `04-costing.csv` (pilot = retail ingredient prices found on 7 Oct; scale = `[ASSUMPTION]` bulk prices):

| | A. Cocoa & Peanut | B. Raspberry & Almond | C. Honey Oat |
|---|---|---|---|
| Ingredients, pilot | £0.86 | £1.11 | £0.81 |
| **Unit cost, pilot** (+5% waste + £0.17 pack) | **£1.07** | £1.33 | £1.02 |
| Ingredients, early co-man | £0.33 | £0.46 | £0.32 |
| **Unit cost, co-man** (+3% waste, £0.07 pack, £0.30 conversion) | **£0.71** | £0.85 | £0.70 |

- **Egg-white powder is about half the pilot ingredient cost** (12 g × £34.99/kg = £0.42). Buy on Myprotein promo (£24.49/kg) and the hero unit cost falls to about £0.94.
- Labour if paid at the 2026 National Living Wage would add **~£0.75/bar** at hand-made speed (not included above).
- Freeze-dried raspberry makes B the most expensive.

**Proposed RRP: £2.75 single · £10 for 4 · Squad Box of 12 for £27 (£2.25 each).**
At £2.75 that's **£0.14/g protein**: in line with Grenade (£0.143), Barebells (£0.145) and Fulfil (£0.149), and well below Forza (£0.229) and Styrkr (£0.183).

**Channel economics (hero):**

| Channel | Brand receives | Cost | Gross margin |
|---|---|---|---|
| Direct at pilot events (not VAT-registered) | £2.70 | £1.07 | **£1.63 (60%)** |
| Direct online at scale (4 for £10, VAT, postage share) | £2.05 | £1.06 | £0.99 (48%) |
| Gym/café wholesale at scale (35% retailer margin) | £1.49 | £0.71 | £0.78 (52%) |
| Retail via distributor (40% + 25%) | £1.03 | £0.71 | **£0.32 (31%)** |

**Business-model conclusion:** grocery retail is a poor first channel. Lead with **direct sales, clubs (Squad Box) and gyms/cafés**.

**VAT:** sports and protein bars are treated as standard-rated confectionery, so 20% VAT applies once registered (threshold £90k turnover `[ASSUMPTION: check current threshold]`). That's why the scale rows use ex-VAT prices.

## 5. When and how it's eaten

| | |
|---|---|
| **Occasion** | Within ~1–2 h after training, when a proper meal is more than an hour away (walk home, lecture, travel) |
| **How much** | Half after a light or short session; whole bar after a hard or long one |
| **Packs** | Single (pilot, events, gym fridge-free counter) · 4-pack (direct) · **Squad Box of 12** for clubs and teams |
| **Not for** | Before or during exercise (fibre, fat, egg). Not a meal replacement |
