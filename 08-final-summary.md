# 08 — Final Summary

**Updated:** 8 Oct 2026 (Week 5) · **Change since 7 Oct:** product redesigned to Ewan's brief: **supermarket ingredients, fresh milk and boxed eggs, max 6 g sugar, clearly different from competitors** (v3 kitchen bake).

## Quality check (re-run 8 Oct)

| Check | Result |
|---|---|
| Re-ran every script (`04-nutrition.py`, `04-costing.py`, `research/02_build_competitors.py`, `05-brand/build_logos.py`, `05-brand/build_packaging.py`, `07-budget.py`) | ✅ All run cleanly; committed outputs match |
| Every competitor row has a source URL and date | ✅ 26/26; new sources logged (C31, R10, P16–P21) |
| No invented testimonials, quotes or interview data | ✅ Placeholders only; persona still tagged "hypothesis" |
| Claims on pack and page vs GB conditions | ✅ "Low sugar" (3.0–3.8 g/100 g), "source of protein", authorised protein claim + balanced-diet statement. **Removed:** "high protein" (doesn't qualify now) and "no added sugar" (banana adds sweetness) |
| Numbers on page/pack match calculations | ✅ 3 g sugar / 14 g protein / 28 g carbs / 90 g trace to `04-nutrition.py` |
| Landing page at 390 and 1280 px | ✅ No horizontal scroll, no console errors |

**Known limitations:** research came via search-engine extracts (direct page access was blocked). Nutrition uses typical database values and an **assumed 24% bake loss**. Your first bake replaces that with a real number.

## What was built
All of Phases 0–8 (see `PROGRESS.md`). On 8 Oct, the product, packaging, landing page, positioning map, costing, budget, pilot plan, assumption tracker and pitch outline were updated for the v3 kitchen bake.

## Top 5 insights

1. **The difference is now low sugar without lab ingredients.** Every UK bar we found with ≤6 g sugar uses polyols, sweeteners or protein isolates (Grenade, Barebells, PhD, Misfits). Every whole-food or "natural" bar has 9.5–38 g sugar. The v3 bake has **~3 g sugar from 7 supermarket ingredients**: alone in that corner of the map (`02-positioning-map.html`).
2. **Baking with eggs is what makes it possible.** "Natural" bars need dates or syrup to stick together; ours is set by eggs and milk in the oven. That's a real, explainable point of difference, and a good pitch line: *sugar like a protein bar, ingredients like home baking.*
3. **The honest trade-offs are protein and shelf life.** Supermarket whole foods top out at **~12–14 g protein per 90 g bar** (lab bars: ~20 g), so **no "high protein" claim**. And a fresh egg and milk bake must be **chilled with a short use-by**. The pilot tests whether buyers mind; if they do, the v2 route (same foods, dried) gets ~23 g protein and is shelf-stable, at ~9 g sugar.
4. **The economics got better.** Pilot cost is **£0.65/bar** (vs £1.07 with powders). Margin is 76% selling direct and 60% to gyms/cafés. The pilot budget is **£960, within the £1,000**. It's no longer an HFSS product (score −3 vs +9 before), so it could be promoted by retailers later.
5. **Customer evidence is still the whole game.** Problem & Market Research stays Red until the interviews, waitlist and pilot produce numbers.

## Readiness (vs Phase 1)

| Criterion | Phase 1 | Now | Why |
|---|---|---|---|
| 1. Problem & Market Research | 🔴 | 🔴 | Competitor evidence is strong; customer evidence is unchanged |
| 2. Innovation & Value Proposition | 🟠 | 🟠↑ | Clearer, provable difference (low sugar + kitchen ingredients). Lower protein is a weakness |
| 3. Feasibility & Business Model | 🟠 | 🟠↑ | You can make it this week; cheap; within budget. Chilled distribution limits scale |
| 4. Team Capability | 🟠 | 🟠 | Strong coachability story (23 g → 3 g sugar after testing against competitors and claims law) |
| 5. Impact & Scale | 🔴 | 🔴↑ | Low-sugar, non-HFSS, real-food positioning gives a concrete impact story; still unevidenced |
| 6. Pitch & Communication | 🟠 | 🟠↑ | You'll have a real bar to hand out within a week |

## Decisions you need to make
1. **Name:** confirm **fettle** after the UK IPO check (fallback: Afta).
2. **Protein vs simplicity:** accept ~14 g protein for the pilot (my recommendation), and let pilot data decide whether to add the dried-ingredient v2 route.
3. **Fresh vs shelf-stable:** pilot fresh and chilled (my recommendation), sold where there's a fridge: club fridge, gym café.
4. **Primary persona:** confirm Sam (regular trainer, student), or adjust once you have your interview notes.

## Riskiest open assumptions (from `07-assumption-tracker.csv`)
1. **A1:** people want low sugar **and** real food together.
2. **A2:** ~14 g protein is enough.
3. **A3/A4:** they'll pay £2.75 and buy again.
4. **A5:** a chilled, short-life product works for partners.
5. **A6:** it tastes good sweetened only by banana.

## What to do this week
1. **Bake recipe A** (`04-concept-bar.md` §3). Weigh the tin empty, full and after baking, then tell me the numbers and I'll re-run the nutrition.
2. **Register as a food business** with the council (28 days' notice, so you're legal for a Week 9 pilot).
3. **Upload your 9 interview notes** to `inputs/`.
4. **Check "fettle"** on the UK IPO and Companies House.
5. **Connect the waitlist** (`06-landing/AUTOMATION.md`) and post it in 3–5 club and SU groups.
6. **Email 6 gyms, clubs or cafés with a fridge** about a 3-week pilot.
