# 02 — Competitor Analysis

**Date:** 7 Oct 2026 · **Method:** DVS five-step competitor research · **Data:** `02-competitors.csv` (26 rows, built by `research/02_build_competitors.py`) · **Chart:** `02-positioning-map.html`
**Tags:** `[EVIDENCE: source]` · `[ASSUMPTION]` · `[GAP]` · Competitor marketing = **claim**, not fact.

> **How the data was gathered.** Direct page access to retailer and brand sites is blocked in this environment, so every figure comes from **web-search extracts of the cited retailer pages** (Tesco, Boots, Ocado, Holland & Barrett, Morrisons, cycle retailers), checked 7 Oct 2026. Each row in the CSV has a URL and a confidence rating. **Before any number goes on a slide, check it on the real pack or page** (photographing the 6 key packs takes 30 minutes and doubles as "proof you know your competitors").

---

## Summary: the six things that matter

| # | Finding | Tag |
|---|---|---|
| 1 | **The gap (updated 8 Oct): low sugar without lab ingredients.** Every UK bar found with ≤6 g sugar uses polyols, sweeteners or protein isolates; every whole-food or "natural" bar has 9.5–38 g sugar. Our v3 kitchen bake calculates at ~3 g sugar, ~14 g protein, ~28 g carbs (90 g) | `[EVIDENCE: 02-competitors.csv]` + `[ASSUMPTION: concept maths, unverified]` |
| 2 | **But a gap is not demand.** Kellogg **withdrew RXBAR** (egg white + dates, the best-known whole-food protein bar) from the UK about two years after launch; RX BAR UK Ltd was dissolved 18 May 2023. No reason was published | `[EVIDENCE: Food Business News; Companies House 11297949]` |
| 3 | **The price ceiling is about £2.50–2.95 a bar.** Lab protein bars sit at £0.12–0.15 per g protein; recovery bars at £0.18–0.23 | `[EVIDENCE: retailer prices, CSV]` |
| 4 | **Chocolate milk + a banana is the real benchmark.** About 14 g protein + 60 g carbs for **£1.77**, sold everywhere | `[EVIDENCE: Tesco prices]` + `[ASSUMPTION: banana nutrition]` |
| 5 | **The 20 g protein bars are built for "low sugar", not refuelling.** Grenade (16 g polyols), PhD (20 g polyols) and Barebells/Fulfil reach 20 g protein with 15–22 g carbs. Polyols are excluded from the GB carbohydrate recovery claim | `[EVIDENCE: Boots, H&B listings; Reg. 2015/7]` |
| 6 | **"Natural" recovery bars trade protein for sugar.** Veloforte Forza: 12 g protein, 27.6 g sugar. Styrkr BAR+: 15 g protein, 28.4 g sugar, glucose syrup first, 0.67 g fibre | `[EVIDENCE: retailer listings]` |

**Update 8 Oct:** the v1 concept had ~23 g sugar (red traffic light), so it couldn't beat Forza or Styrkr on sugar. Ewan set a **6 g sugar cap** and asked for supermarket ingredients (fresh milk, boxed eggs). The v3 kitchen bake has ~3 g sugar. **Honest weaknesses now:** ~14 g protein (lab bars have ~20 g), and it's a fresh, chilled product. See `04-concept-bar.md`.

---

## Step 1 — Public information

### 1a. The three groups (full numbers in `02-competitors.csv`)

**Protein bars** (all sold in UK grocery or pharmacy unless noted)

| Product | Wt | Protein | Carbs | Fibre | £/bar | £/g protein | How they get to 20 g |
|---|---|---|---|---|---|---|---|
| Grenade Carb Killa | 60 g | 20 | 18 (16 polyols) | 3.0 | 2.85 | 0.143 | Milk protein blend, polyols. Pack warns of laxative effect |
| Barebells | 55 g | 20 | 17 | 3.5 | 2.90 | 0.145 | Milk protein; "no added sugar" (claim) |
| Fulfil | 55 g | 19.5 | 15.9 | 3.8 | 2.90 | 0.149 | Protein blend, 9 added vitamins |
| PhD Smart Bar | 64 g | 21 | 22 (20 polyols) | — | 2.50 | 0.119 | Milk protein, collagen, soy isolate, maltitol |
| Myprotein Layered | 60 g | 20 | 20 | 6.4 | 2.50 | 0.125 | Protein blend |
| Myprotein Protein Flapjack | 80 g | 20 | 32 | 7.8 | 2.49 | 0.125 | Soy isolate (20%), whey isolate, golden syrup, palm-oil margarine, FOS |
| Misfits | 45 g | 16 | `[GAP]` | 8 | 2.20 | 0.138 | Plant protein blend |
| Huel bar | 55 g | 14 | 19 | 7 | 2.50 | 0.179 | Plant protein + vitamins |
| Clif Builders | 68 g | 20 | 31 | 3 | 1.90 | 0.095 | Soy isolate. **UK supply patchy**: Sigma has delisted it; Premcrest out of stock |
| Veloforte Protein Crunch | 66 g | 20 | 17 | 12 | ~3.08 | 0.154 | Soy crisps + 5 g collagen + chicory syrup |

**Whole-food / natural bars**

| Product | Wt | Protein | Carbs | Fibre | £/bar | Note |
|---|---|---|---|---|---|---|
| Nākd Cocoa Delight | 35 g | 2.9 | 19 | 3.3 | `[GAP]` | Fruit and nut snack, not sports |
| Nākd Protein Peanut Butter | 45 g | 7 | 15 | 6.8 | `[GAP]` | Protein source not captured `[GAP]` |
| Trek Protein Flapjack | 50 g | 9.8 | 23 | 2.2 | 1.65 | Soy isolate crispies, rice syrup |
| Bounce Protein Ball | 40 g | 9.3 | 15.5 | — | 1.75 | Protein source not captured |
| Deliciously Ella Oat Bar | 50 g | 2.8 | `[GAP]` | — | 1.29 | Oat snack, not sports |
| Graze Protein Oat Bites | 30 g | ~4 | `[GAP]` | — | 0.62 | Snack bite |
| Battle Oats | 80 g | 12 | 38 | 6.6 | `[GAP]` (2017: £1.42) | "Protein isolate"; outdoor retail |
| 33Fuel Eroica (2 bars) | 100 g | 20 | 43 | — | 4.40 | Almond + egg white; 38 g sugar. Inherited data, low confidence |
| **RXBAR** | — | — | — | — | — | **Withdrawn from UK**; company dissolved 2023 |

**Recovery products and real-food substitutes**

| Product | Serving | Protein | Carbs | Fibre | £ | £/g protein |
|---|---|---|---|---|---|---|
| Veloforte Forza | 70 g bar | 12 | 38.3 | 7.4 | ~2.75 `[ASSUMPTION: price not confirmed]` | 0.229 |
| Styrkr BAR+ | 74 g bar | 15 | 46.6 | 0.67 | 2.75 (£32.95/12) | 0.183 |
| TORQ Recovery Bar | 65 g bar | 13.4 | 40.2 | 2.1 | 2.50 SRP | 0.187 |
| SiS REGO Rapid Recovery | 50 g sachet (shake) | 20 | 22 | — | 2.50 | 0.125 |
| Yazoo chocolate milk | 400 ml | 12.8 | 35.2 | — | 1.60 | 0.125 |
| Banana | 1 medium | ~1.4 | ~24 | ~1.3 | 0.17 | — |
| **Yazoo + banana** | — | **14.2** | **59.6** | 1.3 | **1.77** | 0.125 |

### 1b. Company profiles (the three that matter most)

| Field | Veloforte (closest product) | Styrkr (category proof) | Myprotein / THG (closest macros) |
|---|---|---|---|
| Product & features | Forza: whole-food, egg white, 12 g P. Also Protein Crunch (20 g P with collagen) | BAR+: puffed rice + soy isolate, 3:1 carb:protein | Protein Flapjack: 20 g P / 32 g C from isolates |
| Customer segments | Cyclists and endurance athletes `[ASSUMPTION]` | Endurance "everyday athletes" (claim) | Gym-goers, online fitness `[ASSUMPTION]` |
| Price | ~£2.75 `[ASSUMPTION]` | £2.75 | £2.49 (third-party listing) |
| Channels & partners | Sigma, Decathlon, H&B, D2C `[EVIDENCE: listings]` | Cycle retail (Tweeks, Halfords), UK distributor Upgrade `[EVIDENCE: inherited, BikeBiz]` | D2C, H&B, grocery |
| Technical approach | Handmade in UK, real-food recipes (claim) | Dual-source carbs (claim) | Mass manufacture, isolates |
| Funding & growth | Founded 2016 (Tracxn, inherited). Funding not found `[GAP: Companies House filings]` | Founded 2018 per founder. Launched CEL50 chew Jul 2026 `[EVIDENCE: endurance.biz, inherited]`. Funding not found `[GAP]` | Part of THG `[ASSUMPTION]` |
| Stage | Scale-up, national + export | Scale-up, national + export | Mature |

**Trade mark / Companies House checks** for competitors weren't possible (sites blocked) `[GAP]`. These matter less than checking our own name (Phase 5).

---

## Step 2 — Ecosystem conversations

The questions are in **`02-ecosystem-interview-guide.md`**: customers, coaches/PTs, sports nutritionists, co-manufacturers, gym owners/retailers and investors. Each covers the five DVS questions.

---

## Step 3 — Analyse the evidence

| | What it covers |
|---|---|
| **Known with confidence** | Macros and prices of the lab protein bars (Grenade, Barebells, Fulfil, PhD), all £2.50–2.90. Styrkr's ingredient list and 28 g sugar. Forza's 12 g protein. Chocolate milk £1.60 / 400 ml. Polyols excluded from the carb recovery claim. RXBAR's UK exit. Protein/sports bars are standard-rated for VAT (20%) `[EVIDENCE: FTT case via taxation.co.uk]` |
| **Assumptions to test** | That buyers care about low sugar **and** simple ingredients together (not just one). That ~14 g protein is enough for them. That a chilled, fresh bar fits how they buy. That £2.75 is acceptable for a 90 g bake. That club/university channels are unserved. That gut comfort is a real pain with lab bars |
| **Missing information** | Customer interview data (blocking). Forza's current price. Nākd and Bounce protein sources. Why RXBAR left the UK. Competitors' sales volumes, margins, funding. Co-manufacturer quotes |
| **Where we're differentiated** | Only bar found with ≤6 g sugar made from kitchen ingredients alone: no powders, polyols, sweeteners or syrups. ~90% less sugar than Forza/Styrkr. Weaknesses: less protein than lab bars (~14 g vs ~20 g); perishable (chilled, short use-by); 90 g, heavier than most bars |

---

## Step 4 — Direct engagement

**Recommendation: don't contact Veloforte or Styrkr yet.** You have no prototype, so there's little to gain and a small risk of tipping off a faster-moving competitor.

**Worth asking now (low risk):**
- **Kellogg / ex-RXBAR UK staff (via LinkedIn):** "What made RXBAR hard to sell in the UK?" This is the single most valuable competitor question. A former brand or sales manager is more likely to answer than the company.
- **Cycle-shop and gym staff:** "Which recovery bars sell through, and which sit on the shelf?"

**Ask in Weeks 9–10, once you have a bar:** Veloforte or Styrkr founders, framed as founder-to-founder: how they found a co-manufacturer, their starting MOQ, and how they got into Sigma or H&B.

**Risks of asking:** they copy the idea (low: they could already); they decline (no cost); you rely on a competitor's self-serving view (treat it as a claim).

---

## Step 5 — What matters

| Dimension | Conclusion |
|---|---|
| **Market readiness** | Protein bars are mature and crowded; "natural" recovery bars exist in cycle retail. Buyers already accept £2.50–2.90 a bar `[EVIDENCE]`. Whether they want a *bigger, carb-heavier* bar is unknown `[GAP]` |
| **Customer adoption** | Lab protein bars have mass adoption (supermarkets, Boots). Whole-food recovery bars are niche. RXBAR's exit is a warning that "simple ingredients" alone didn't win UK shoppers `[EVIDENCE]` |
| **Pricing & business model** | Buyers already pay £2.50–2.90 a bar `[EVIDENCE]`. At £2.75, the v3 kitchen bake (pilot cost £0.65) makes ~76% selling direct and ~60% via gyms/cafés. It's a fresh, chilled product, so grocery retail isn't a near-term channel. **Clubs, gyms and cafés with fridges first** (see `04-costing.csv`). On £ per gram of protein (£0.19) it's dearer than lab bars (£0.12–0.15), so don't sell it on protein value |
| **Technical strengths & weaknesses** | Strength: low sugar from a binding method (baking with eggs), cheap ingredients (~£0.65/bar), no HFSS issue. Weaknesses: short chilled shelf life; protein ceiling ~14 g without powders; texture consistency between home bakes `[ASSUMPTION: needs trials]` |
| **Partnerships & distribution** | Pro sports clubs are tied to SiS, Myprotein and Grenade (inherited research). University and grassroots clubs show no visible natural-bar supplier `[ASSUMPTION]` |
| **Competitive advantages & barriers** | Our advantage today is a specific formulation and a local network, which is easy to copy. **Barriers to us:** co-man MOQs of 10k–25k bars `[EVIDENCE: industry guide]`, wrapper MOQs ~25k `[EVIDENCE: TIPA]`, listing fees, shelf-life testing. Durable moats would have to come from community and pilot evidence |

## Is the gap real? (the positioning map)

**The map is now sugar vs protein (updated 8 Oct).** In the ≤6 g sugar / ≥10 g protein box, every other bar is a lab protein bar (isolates, polyols, sweeteners). fettle is the only kitchen-ingredient bar there. Three things stop me calling it a winning gap:
1. **Lab bars have more protein (~20 g)** and are on every shelf. We must prove buyers value *simple ingredients + low sugar* enough to accept ~14 g.
2. **Chocolate milk + a banana** costs £1.77 and everyone knows it. It's real food too, though with more sugar.
3. **RXBAR:** a well-funded simple-ingredient bar left the UK. "Simple ingredients" alone didn't win.

**What would change my mind:** 30+ conversations showing people already improvise "protein bar + banana" or buy two products after training (= real pain), plus waitlist sign-ups that accept £2.50+.
