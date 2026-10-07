# 07 — MVP / Pilot Plan (Weeks 5–13)

**Date:** 7 Oct 2026 (Week 5) · **Updated 8 Oct** for the v3 kitchen bake (fresh eggs + milk, ≤6 g sugar) · **Budget:** £1,000 total · **Budget numbers from:** `07-budget.py`
**Goal by Week 13:** turn the Red judging scores (Problem & Market Research; Impact) into evidence. Specifically: **30+ structured conversations, 150+ waitlist sign-ups with price data, and a small paid pilot with repeat purchases.**

> The prompt assumed Weeks 4–13 (10 weeks). You're in Week 5, so this is a **9-week plan** starting this week.

---

## 1. The MVP ladder

| Step | What | Cheapest test of | Weeks |
|---|---|---|---|
| 0. **Smoke test** | Landing page + waitlist (no product) posted in club WhatsApps, Durham SU groups, gym noticeboards | Do people want it enough to give an email and a price? | 5–13 |
| 1. **Kitchen bake** | 3 flavours from the recipe cards in `04-concept-bar.md` §3, one tin each, 4 rounds. **Weigh before and after baking** | Does it taste good, hold together, and stay ≤6 g sugar? | 6–8 |
| 2. **Blind taste test** | n ≈ 20–30 trainers; our bars vs Grenade and Forza, unbranded | Do people like it as much as what they already buy? | 7–8 |
| 3. **Small paid pilot** | ~250 fresh bars over 3 weeks (bake **twice a week**, ~35–40 bars each; 3-day use-by) at **one club** and **one gym/café counter with a fridge** | Will people pay, and come back? | 9–11 |
| 4. **Scale-up conversation** | (a) a local bakery/café kitchen to bake fresh under contract; (b) a co-manufacturer for the shelf-stable v2 route | Can it be made beyond your kitchen? | 10–12 |

## 2. Week-by-week

| Week | Do | Output / evidence |
|---|---|---|
| **5 (now)** | **Register as a food business with the council today** (free; 28 days' notice, so legal from ~Week 9). Start Level 2 food hygiene. Upload your 9 interview notes. Publish landing page (demo forms → connect Brevo/Formspree per `AUTOMATION.md`). Do the UK IPO check on "fettle". Book a commercial or community kitchen | Registration confirmation; page live; persona v2 |
| 6 | Kitchen round 1 (3 flavours, recipe cards; weigh before/after baking and update `loss=` in `04-nutrition.py`). 10 interviews using `02-ecosystem-interview-guide.md`. Contact 6 gyms/clubs/cafés for a pilot | Recipe notes (weights, texture, binding); interview log |
| 7 | Kitchen round 2 (fix texture; try grated apple instead of banana for even less sugar). **Blind taste test** (n ≈ 20). Send hero sample to a UK food lab for nutrition (+ water activity). Waitlist push | Taste scores; lab order placed |
| 8 | Kitchen round 3 (lock recipes). **Fridge keep test**: check texture, smell and mould on days 1, 3, 5 and 7 to set the use-by date (agree it with your EHO). Finalise **PPDS label** (name, full ingredients, allergens in bold). Buy insurance. Confirm **2 pilot partners** | Locked spec; labels; signed-off partners |
| 9 | **Pilot bakes start** (2 bakes a week, ~35–40 bars each, delivered chilled in a cool bag). Pilot opens at Partner 1 (club) and Partner 2 (gym/café). Sell at £2.75 single / Squad Box £27 per 12 | Sales log by day; QR feedback survey on label |
| 10 | Pilot week 2 (2 bakes). Mid-pilot check-in with partners. Lab results back → update label/claims if needed | Repeat-purchase data; partner feedback |
| 11 | Pilot week 3. Ask partners "would you reorder, at what price?" Request 2–3 co-man quotes | Partner commitments; co-man MOQs and prices |
| 12 | Analyse; update persona, assumption tracker and costings with real numbers. Rehearse the pitch twice with a mentor | Pitch deck v2 |
| 13 | **Final pitch** | — |

## 3. What to measure, and what counts as success

Thresholds are `[ASSUMPTION]`s set *before* the pilot, so you can't move the goalposts afterwards.

| Metric | How | Success | Kill / pivot signal |
|---|---|---|---|
| Waitlist sign-ups | Brevo/Formspree count | **≥150** by Week 12 | <50 after 3 weeks of posting |
| Visit → sign-up conversion | Analytics | ≥10% from targeted posts | <3% |
| Price acceptance | Waitlist price question | **≥50% choose ≥£2.50** | <30% → resize bar or club-subsidised model |
| Blind taste score | 9-point hedonic scale | Mean ≥6.5 and not worse than Grenade by >1 point | Mean <5.5 after round 3 |
| "Would buy again" | Taste test + pilot survey | ≥60% | <35% |
| **Repeat purchase** (the strongest evidence) | Pilot sales log, first-name or card-last-4 tally | **≥30% of buyers buy 2+ times in 3 weeks** | <15% |
| Partner sell-through | Bars sold ÷ stocked | ≥60% within 2 weeks | <30% |
| Partner reorder intent | Week 11 ask | ≥1 of 2 says yes, at wholesale price | 0 of 2 |
| Gut comfort | Pilot survey: "Any stomach discomfort?" | <10% moderate or worse | >15% → cut fibre to ~4 g |
| Is ~14 g protein enough? | Taste test + pilot survey: "Would you want more protein, even if it meant protein powder?" | <40% say yes | >60% say yes → move to the v2 shelf-stable route with milk/egg powders |
| Fridge / short shelf life a barrier? | Partner feedback + waste count | Waste <15% of bars delivered | Waste >30% → bake to order only |

## 4. Rough budget (from `07-budget.py`, updated 8 Oct for the kitchen bake)

| Item | £ | Basis |
|---|---|---|
| Prototype ingredients (12 tins) | 46 | calc from 04-costing (~£3.81/tin) |
| Pilot bars incl. packaging (250 × hero unit cost) | 162 | calc from 04-costing |
| Lab nutrition analysis, 1 sample | 150 | `[ASSUMPTION]` get 2 quotes |
| Water activity / shelf-life test | 40 | `[ASSUMPTION]` |
| Commercial kitchen hire (4 sessions × £15/h × 3 h) | 180 | `[ASSUMPTION]` community/church kitchen rates vary |
| Food hygiene Level 2 (online) | 15 | `[EVIDENCE]` £10–25 |
| Public + product liability insurance (pilot) | 120 | `[ASSUMPTION]` PL from ~£57/yr (P13); product liability adds |
| 20 cm tins ×2, scales, probe thermometer, cool bag + ice packs | 60 | `[ASSUMPTION]` chilled transport to partners |
| Label printing (allergen-compliant stickers) | 30 | `[ASSUMPTION]` |
| Taste-test materials + competitor bars for blind test | 40 | `[ASSUMPTION]` ~10 competitor bars |
| Survey / interview incentive (prize draw) | 30 | `[ASSUMPTION]` |
| Contingency (10%) | 87 | |
| **Total spend** | **960** | Budget £1000 → within by £40 |
| Pilot sales (offset) | −500 | `[ASSUMPTION]` 200 bars × £2.50 |
| **Net cost** | **460** | |

**Within the £1,000.** Fresh eggs and milk cost far less than the powders in v1 (pilot bars £0.65 each vs £1.07). Finding a free kitchen (SU, university catering, a church hall) would save another £180.

## 5. Food-safety basics for selling at pilot scale (UK)

| Requirement | What it means for you | Tag |
|---|---|---|
| **Register as a food business** | Free, with the local council (Durham County Council or wherever you make the bars), **at least 28 days before** you start, including if you give food away regularly at events. It's an offence not to | `[EVIDENCE: R6, R7]` |
| **Home kitchen?** | Legally allowed once registered, and Environmental Health may inspect. **But** a shared student kitchen is a bad idea: allergen cross-contact (peanuts, nuts, egg, milk), housemates' food, landlord terms. **Recommend a hired community or commercial kitchen** | `[EVIDENCE]` + `[ASSUMPTION]` |
| **Food hygiene training** | Level 2 Food Hygiene (online, £10–25) for anyone making bars. Not strictly mandatory, but expected by EHOs and partners | `[EVIDENCE: P12]` |
| **Food safety management** | Write a simple HACCP-based plan; the FSA's free **"Safer Food, Better Business"** pack works. Key hazards: allergen cross-contact, **undercooked egg** (bake until set; centre 75 °C), cooling and chilled storage (0–5 °C), moisture/mould | `[ASSUMPTION: standard practice]` |
| **Allergen labelling** | Bars wrapped where you sell them (e.g. your own stall) = **PPDS** (Natasha's Law): name + full ingredients with the 14 allergens emphasised. Bars wrapped in your kitchen and sold by a gym or café = **prepacked**: full mandatory labelling (name, ingredients, allergens, net quantity, best before, storage, business name and UK address, nutrition declaration). **Label every pilot bar to full prepacked standard**; the back-of-pack design in `05-brand/` already does this | `[EVIDENCE: R5]` |
| **Nutrition declaration** | Small producers supplying direct to the final consumer or local retail *may* be exempt `[ASSUMPTION: check the exemption with Trading Standards]`, but **any nutrition or health claim ("low sugar", "source of protein") makes the full nutrition table mandatory** | `[ASSUMPTION]` |
| **Claims** | Use only the claims marked "Yes" in `04-concept-bar.md` §5 ("low sugar", "source of protein", the protein claim). Ask Trading Standards about "real food" / "kitchen ingredients" wording and any "less sugar than…" comparison | — |
| **Insurance** | Public + product liability before selling; partners will ask for it | `[ASSUMPTION]` |
| **Selling on campus / in gyms** | Check Durham SU or university rules on selling food, and the partner's own requirements | `[GAP]` |
| **Chilled food** | Keep at 0–5 °C from cooling to sale; carry in a cool bag with ice packs; partner must have a fridge. Use a **use-by** date (perishable), not best-before. Label "Keep refrigerated" | `[ASSUMPTION: confirm use-by period with EHO]` |
| **Weights** | Net quantity "90 g ℮" means average weight must be ≥90 g under the average quantity system. Weigh a sample from each batch | `[ASSUMPTION]` |

## 6. Next step to a co-manufacturer (Weeks 11–13+)

1. **Fresh route (first):** ask 2–3 local bakeries or café kitchens whether they'd bake the recipe under contract, and at what price per tray. That keeps the product exactly as piloted.
   **Shelf-stable route (later):** shortlist UK bar co-manufacturers that handle egg and milk (e.g. Morga Foods, Boundary, Wholebake; verify each) for the v2 dried-ingredient version.
2. **Send a one-page spec:** recipe, target macros (≤6 g sugar), allergens, 90 g format, packaging, volumes (1k → 10k → 25k bars).
3. **Ask:** minimum run, price per bar, lead time, shelf-life testing, allergen controls, whether they can do a 1,000–5,000 bar pilot run.
4. **Reality check:** typical MOQs are **10,000–25,000 bars** `[EVIDENCE: P15]`, with printed wrapper MOQs ~25,000 `[EVIDENCE: P14]`. That's roughly £7k–18k of stock at ~£0.70/bar, beyond the DVS budget. The Week 13 "ask" should be funding or a grant for this first run, **backed by pilot repeat-purchase data**.

## 7. Impact options (to fix the Red on criterion 5)

Pick one or two you can actually evidence:
- **Grassroots club fund:** 10% of every Squad Box goes back to the club's funds `[ASSUMPTION: margin allows it, see 04-costing]`. Measurable £ to clubs.
- **Honest labelling:** every batch lab-tested and published by QR ("others claim, we publish").
- **Low sugar without ultra-processed ingredients:** ~3 g sugar with no isolates, polyols or sweeteners; not HFSS. Describe it; don't claim health outcomes.
- **Packaging:** move to a recyclable mono-material or paper-based wrapper at co-man scale.
