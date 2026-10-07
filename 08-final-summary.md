# 08 — Final Summary

**Date:** 7 Oct 2026 (Week 5 of 13)

## Quality check (Phase 8)

| Check | Result |
|---|---|
| Re-ran every script from scratch (`04-nutrition.py`, `04-costing.py`, `research/02_build_competitors.py`, `05-brand/build_logos.py`, `05-brand/build_packaging.py`, `07-budget.py`) | ✅ All run cleanly; outputs identical to the committed files |
| Every competitor row has a source URL and access date | ✅ 26/26 (`02-competitors.csv`, `research/sources.md`) |
| No invented testimonials, quotes or interview data | ✅ Scan found none. Landing-page social proof and founder story are clearly marked placeholders; persona is tagged "hypothesis" |
| Claims on packaging and landing page vs GB register conditions | ✅ Only "High protein" (26.8% energy) and the authorised protein muscle-mass claim are used. **Fixed during QC:** added the mandatory "varied, balanced diet and healthy lifestyle" statement that must accompany any health claim. "High fibre", "natural", "whole food", "clean" and recovery claims are kept off |
| Numbers on page/pack match calculations | ✅ 20 g / 37 g / 23 g / 295 kcal all trace to `04-nutrition.py` |
| Landing page at 390 px and 1280 px, light and dark | ✅ No horizontal scroll; no console errors; demo form submit works |

**Known limitation:** web research came through search-engine extracts, because direct page access was blocked here. Nutrition uses typical database-style values I couldn't open directly. **All product numbers are calculated, not measured.**

---

## What was built

| Phase | Deliverables |
|---|---|
| 0 | `00-briefing.md`, `PROGRESS.md`, `inputs/judging-criteria.md` (transcribed from your photos), `research/sources.md` |
| 1 | `01-judging-map.md`: criteria → evidence → deliverable, RAG scores |
| 2 | `02-competitor-analysis.md` (DVS five steps), `02-competitors.csv` (26 products), `02-positioning-map.html`, `02-ecosystem-interview-guide.md` |
| 3 | `03-persona.md` + `03-persona-card.html`: **hypothesis "Sam"**, built to be filled from your notes |
| 4 | `04-concept-bar.md`, `04-nutrition.py`, `04-nutrition-tables.md`, `04-costing.py`, `04-costing.csv`: 3 recipes + strict whole-food comparison; claims, HFSS, VAT, margins |
| 5 | `05-brand/`: name research and recommendation (**fettle**), guidelines, 6 logo SVGs, front and back wrapper, brand board |
| 6 | `06-landing/index.html` (12 sections, waitlist + price question, book-a-chat with embed/form options), `AUTOMATION.md` with 3 emails |
| 7 | `07-mvp-pilot-plan.md`, `07-budget.py`, `07-assumption-tracker.csv` (14 ranked assumptions), `07-pitch-outline.md` (12 slides + 5-minute cut) |

## Top 5 insights

1. **The gap is real on paper.** No single UK bar found gives ~20 g protein **and** 35 g+ carbs without isolates or polyols. Lab protein bars get to 20 g protein with ~18 g carbs, mostly polyols; natural recovery bars stop at 12–15 g protein.
2. **Demand is the unknown, and there's a warning sign.** Kellogg pulled **RXBAR** (an egg-white + dates bar) from the UK; its UK company was dissolved in 2023. The cheap real-food rival, **chocolate milk + a banana**, gives ~14 g protein / 60 g carbs for £1.77.
3. **The recipe works on paper, with honest trade-offs.** 80 g, 295 kcal, 19.7 g protein, 37 g carbs, 5.2 g fibre. A strict whole-food version only reaches **10.6 g protein**, so milk powder and egg white are needed. The cost is **~23 g sugar (red traffic light)** and an **HFSS "less healthy" score**, the same as most natural bars. I cut the inherited 11 g-fibre / 98 g / 345 kcal spec: the evidence doesn't support high fibre straight after exercise, and it made the bar too big.
4. **Price at £2.75 works, but grocery retail doesn't.** That's £0.14/g protein, level with Grenade and Barebells. Pilot unit cost is ~£1.07 (egg white is half the ingredient cost); ~£0.71 at co-man scale `[ASSUMPTION]`. Margins: 60% direct, 52% gym wholesale, **31% via distributor**. **Clubs, gyms and direct sales first.** Protein/sports bars carry 20% VAT once you register.
5. **Customer evidence is the whole game now.** Problem & Market Research is still Red. "People said yes" won't survive judges. Repeat purchases in a paid pilot will.

## Readiness re-score (vs Phase 1)

| Criterion | Phase 1 | Now | Why it moved / didn't |
|---|---|---|---|
| 1. Problem & Market Research | 🔴 | 🔴 | Competitor proof is strong and sourced, but **customer evidence is unchanged**. The tools to fix it (interview guide, waitlist with price question) are now ready |
| 2. Innovation & Value Proposition | 🟠 | 🟠 | Clear, mapped differentiation and a concept bar. Moat still thin; sugar weakens the "better" story |
| 3. Feasibility & Business Model | 🟠 | 🟠↑ | Unit economics, channel margins, budget and food-safety route are now calculated. Still unverified (recipe, lab, co-man quotes) |
| 4. Team Capability | 🟠 | 🟠 | Good coachability story (spec changed on evidence). Team/adviser gap remains |
| 5. Impact & Scale | 🔴 | 🔴↑ | Concrete impact options and a scale path drafted; nothing evidenced yet |
| 6. Pitch & Communication | 🟠 | 🟠↑ | Brand, map, landing page and slide plan ready. Needs a physical bar and traction numbers |

## Decisions you need to make

1. **Name:** go with **fettle**? First do the 30-minute UK IPO + Companies House check (classes 29/30/5/32). Fallback: Afta.
2. **Budget:** spend is **£1,180 vs £1,000** before pilot sales. Approve: free kitchen + egg-white on promo (my recommendation), or cut a kitchen round?
3. **Primary persona:** confirm **Sam (regular trainer, student)** as primary and the club athlete as secondary, or tell me your interviews say otherwise.
4. **Sugar trade-off:** accept ~23 g sugar and frame it as refuelling, or prioritise a lower-sugar recipe test in kitchen round 2?
5. **Snap-in-half:** keep as a light feature (my recommendation) rather than the inherited 4-segment body-weight hero?

## Riskiest open assumptions (from `07-assumption-tracker.csv`)

1. **A1:** people feel this trade-off as a real pain.
2. **A2:** they'll pay ~£2.75.
3. **A3:** they'll buy again.
4. **A4:** we can make it taste as good as Grenade.
5. **A5/A6:** lab macros match the calculation, and the bar stays soft for 4+ weeks.

## What to do this week (Week 5)

1. **Register as a food business** with the council (free; 28 days' notice, so you're legal for a Week 9 pilot).
2. **Upload your 9 interview notes** to `inputs/` (photos are fine). I'll rebuild the persona from them and re-score criterion 1.
3. **Run the "fettle" trade mark check** (UK IPO, Companies House).
4. **Connect the waitlist form** (Brevo or Formspree, per `AUTOMATION.md`) and post the page in 3–5 club and Durham SU groups. Target 50 sign-ups by next Friday.
5. **Book a kitchen and buy ingredients** for round 1 (~£35). Start the Level 2 hygiene course.
6. **Email 6 gyms, clubs or cafés** asking for a 20-minute chat about a pilot.
