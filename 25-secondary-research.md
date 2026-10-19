# 25: Secondary market research (19 Oct 2026)

**Method.** About 30 minutes of web search. Page fetches are blocked here, so **every figure was read from a search-result extract, not the full page**. Sources are M1–M42 in `research/sources.md`, plus older IDs (C, WR, D, R). Numbers come from `research/25_market_sizing.py`. Brief: `26-secondary-research-prompt.md`. Tags: `[EVIDENCE: id]` = a source says it · `[ASSUMPTION]` = Ewan's or my estimate · `[GAP]` = not found. Spot-check any number before it goes on a slide.

---

## 5 numbers for the pitch

| # | Number | Source and date | Caveat |
|---|---|---|---|
| 1 | **£225m**: UK protein bars, drinks and powders, **+24.2% year on year**. Protein bars are the fastest-growing part of snack bars (+£37.6m in two years). | Circana via Asian Trader, Sept 2025 [EVIDENCE: M1] | A second extract of the same page gave £230m (bars + shakes, +7.5%, 52 w/e Nov 2024). Quote it as "about £225–230m". |
| 2 | **78%** of UK adults are concerned about ultra-processed food (the second-biggest food concern after prices). | FSA Consumer Insights Tracker, Mar 2025 [EVIDENCE: M33] | Steady at 76–78% since July 2023. Concern is lowest among 16–34s (72%). |
| 3 | **All 7** major UK protein bars checked use polyols (maltitol, sorbitol, erythritol, xylitol). **5 of the 7** confirmed carrying "excessive consumption may produce laxative effects". | Retailer ingredient listings, checked Oct 2026 [EVIDENCE: M24–M28, C8, C31] | Recipes vary by flavour. Misfits and PhD warnings not confirmed. |
| 4 | Big-brand bars cost **£1.45 per 10 g protein** (Barebells, Grenade, Fulfil at £2.85–£2.90). Graft at £2.00 = **£1.33**; at £2.50 = £1.67. | Tesco, Boots, Sainsbury's listings, 2026 [EVIDENCE: M16–M18]; script | Shelf prices only. Promotions often take the big brands to £1.90–£2.00. |
| 5 | **12.1 million** UK gym members (17.6% of the population), a market worth **£7.29bn**. | Leisure DB State of the UK Fitness Industry 2026 [EVIDENCE: M14] | Gives a sense of scale beyond universities. The 18–24 share is a [GAP]. |

---

## 1. UK market size and growth

### 1a. Market values (UK only; sources disagree, so ranges are given)
| Scope | Value | Growth | Year / data | Publisher | Tag |
|---|---|---|---|---|---|
| Protein bars + drinks + powders (grocery) | £225m | +24.2% YoY | Circana, to ~mid-2025 | Asian Trader, Sept 2025 | [EVIDENCE: M1] |
| Protein bars + shakes (grocery) | £230m | +7.5% YoY | Circana, 52 w/e Nov 2024 | Asian Trader (same URL, different extract) | [EVIDENCE: M1] |
| Sports nutrition (all channels) | £1.1bn | +19% YoY | year not stated | Asian Trader | [EVIDENCE: M1] |
| Sports nutrition consumer spend | £1.06bn (2023), £1.40bn (2024, estimate) | ~+32% | 2023–24 | Salience (agency blog, secondary) | [EVIDENCE: M8] (low reliability) |
| Snack bars + breakfast biscuits | >£700m (2024), forecast £845m by 2029 | ~3.8% a year (implied) | 2024 → 2029 | Mintel UK Snack Bars 2025 | [EVIDENCE: M3] |
| Cereal bars | £461m (2025, estimate) | +6.0% vs 2024; CAGR 2.3% 2020–25 | 2025 | GlobalData | [EVIDENCE: M2] |
| Protein bars (bar only, £) | [GAP] | | | Paywalled (Mintel, Circana) | Generic USD estimates (~$1.4bn) from 6Wresearch / Mordor-type reports are **not trusted** [EVIDENCE: M40, low] |

- **Which figure to trust:** Circana via Asian Trader (M1) is the best UK-specific figure, because it is till data. The wide spread in growth (+7.5% vs +24.2%) probably reflects different periods and scopes (drinks and powders are growing faster than bars).
- **Brand-level counterweight:** Grenade, a brand rather than independent data, says shakes grew +21.2% against bars at +5.59% [EVIDENCE: M7, brand claim]. **So bars alone are growing roughly mid-single digits, not 24%** [ASSUMPTION drawn from M1 + M7].

### 1b. "High protein" as a claim
- UK food and drink products with a "high protein" claim: **8% (2019) → 5% (2023) → 7% (2024)** (Mintel via FoodNavigator, Mar 2025) [EVIDENCE: M4]. That is recovering, not exploding. Growth comes partly from meat, yoghurt and cereals, not only bars.
- Kantar protein boom: already logged as WR59 (not repeated).

### 1c. A shift to clean label / real food? (data, not opinion)
| Signal | Data | Tag |
|---|---|---|
| Grocer Top Products 2025 (via FoodNavigator, Jan 2026): **Grenade units −15.9%; Fulfil and PhD "significant losses"**; Optimum Nutrition +11.7%; Huel +31.1%; KBF (Warrior) +3.1% | Shoppers are moving between brands, not leaving the category. KBF's founder says the Joe Wicks UPF documentary "sped up a distinction" between products (an opinion). | [EVIDENCE: M5] |
| Grenade turnover £93.2m → £80.5m (2024 accounts, Companies House via City AM) | A brand leader is shrinking. | [EVIDENCE: M6] |
| 60% of UK shoppers say they cut back on UPF in the past year | Survey, Aug 2025 (already WR63) | [EVIDENCE: WR63] |
| Mintel 2025 says "natural ingredients" and UPF concern shape the bar market, and UPF concern "may limit growth" | Analyst commentary, no £ split | [EVIDENCE: M3] |
| £ sales or launch share of "no sweetener" / "real food" bars in the UK | **Not found** | [GAP] (searched: "clean label snack bars UK sales", "no sweeteners bars Circana", Grocer) |

- **Important caveat:** the 2025 winners (Huel, Optimum Nutrition) **still use maltitol or other polyols** [EVIDENCE: C38, M27]. So the data shows shoppers moving away from some brands, **not** a proven move to sweetener-free bars.

**So what for the pitch:** the category is large (£225m+) and still growing, but its leader is losing volume while shoppers say they distrust UPF. That is an opening for a credibly different bar, not proof of demand for one.
**Confidence: medium.** UK till data is cited second-hand, and there is no bar-only or clean-label £ split.

---

## 2. First-market sizing (bottom-up)

### 2a–2c. Inputs
| Input | Value | Tag |
|---|---|---|
| Team Durham sports clubs | 58 | [EVIDENCE: M9] |
| Durham BUCS teams | 125 (2022/23 season) | [EVIDENCE: M9] (2022, may have changed) |
| Durham college sport | 650+ teams across 17 colleges | [EVIDENCE: M9] |
| Durham students engaged in sport or activity | "over 75%" (university's own claim, undated) | [EVIDENCE: M9] (self-reported) |
| Durham performance programmes / capped internationals | 17 programmes; ~50 internationals a year | [EVIDENCE: M9] |
| Durham total students | ~21,150 (2024/25, HESA via aggregator) | [EVIDENCE: M10] |
| Total number of Durham students in BUCS teams | **Not published** | [GAP] |
| Northumbria | 2,400+ students in 82 BUCS teams (→ ~29 per team) | [EVIDENCE: M11] |
| Newcastle | 81 BUCS league teams (2018/19, old) | [EVIDENCE: M12] |
| Sunderland | 30+ clubs, 20+ BUCS teams | [EVIDENCE: M13] |
| Teesside | No count found; 20 teams assumed | [GAP] / [ASSUMPTION] |
| UK BUCS athletes | 100,000+ (2021/22) | [EVIDENCE: D4] |
| UK HE students | 2,904,425 (2023/24) | [EVIDENCE: M15] |
| UK gym members | 11.3m / 16.6% (2025); 12.1m / 17.6%, £7.29bn, 7,463 gyms (2026) | [EVIDENCE: M14] |
| Gym members aged 18–24 | Not found. The Gym Group says ~40% of its members are Gen Z (18–27; company figure) | [GAP]; [EVIDENCE: M36] |

### 2b. North East BUCS: **~328 teams** across 5 universities (Durham 125, Northumbria 82, Newcastle 81, Sunderland 20+, Teesside assumed 20). At 15–29 athletes per team, that is **~4,900–9,600 BUCS athletes** [EVIDENCE: M9, M11–M13 + ASSUMPTION].

### 2d. Sizing table (output of `research/25_market_sizing.py`)
Formula: athletes × share who buy × bars/week × 30 term weeks × price. Share (5/10/20%), bars a week (2/3/5), price (£2.00/2.25/2.50) and term weeks are all **[ASSUMPTION]**.

```
Scope                     Case    Athletes  Share  Buyers Bars/wk    Bars/yr  Price   Revenue/yr
Durham BUCS athletes      Low        1,875     5%      94       2      5,625   2.00      £11,250
Durham BUCS athletes      Mid        2,750    10%     275       3     24,750   2.25      £55,688
Durham BUCS athletes      High       3,659    20%     732       5    109,756   2.50     £274,390
North East BUCS athletes  Low        4,920     5%     246       2     14,760   2.00      £29,520
North East BUCS athletes  Mid        7,216    10%     722       3     64,944   2.25     £146,124
North East BUCS athletes  High       9,600    20%   1,920       5    288,000   2.50     £720,000
UK BUCS athletes          Low      100,000     5%   5,000       2    300,000   2.00     £600,000
UK BUCS athletes          Mid      100,000    10%  10,000       3    900,000   2.25   £2,025,000
UK BUCS athletes          High     100,000    20%  20,000       5  3,000,000   2.50   £7,500,000
Worked example (Durham mid): 2,750 athletes x 10% x 3 bars x 30 wks x £2.25 = £55,688
```
- These are retail values including 20% VAT (R8), not profit.
- The Durham mid case means **~275 regular buyers, ~800 bars a week**. That is a realistic test for a home or small-kitchen pilot. It is also small, so the business case rests on the UK and gym scale (12.1m gym members), not on Durham alone.

**So what for the pitch:** Durham is a test bed worth ~£11k–£274k a year at retail. The North East is ~£30k–£720k, and UK BUCS ~£0.6m–£7.5m. The 12.1m gym members show scale beyond that.
**Confidence: low–medium.** Team counts are evidenced but old. The buyer share and frequency are pure assumptions until Ewan's pilot measures them.

---

## 3. Evidence that current protein bars are hard to digest

### 3a. The law
- Foods with **more than 10% added polyols** must carry **"excessive consumption may produce laxative effects"** under Annex III of Regulation (EU) 1169/2011, as restated in Commission Regulation (EU) 2021/1175 (EUR-Lex). Cargill's labelling guide says the same [EVIDENCE: M22].
- 2021/1175 also notes that polyols in solid foods are unlikely to cause laxative symptoms **below ~20 g a day from all sources** [EVIDENCE: M22].
- **GB retained text:** the legislation.gov.uk version of 1169/2011 was found (Annex I defines polyols), but the **Annex III wording in the GB version was not seen** [EVIDENCE: M23; GAP]. Retailer listings for GB products do carry the warning, which suggests it still applies [ASSUMPTION]. Check legislation.gov.uk/eur/2011/1169/annex/III directly.

### 3b. Which bars use polyols (confirmed vs not confirmed)
| Bar | Polyols in ingredients | Polyols per bar | Laxative warning | Confirmed from |
|---|---|---|---|---|
| Barebells | Maltitol (some flavours also xylitol) | n/a | **Yes**, brand page and Morrisons | M24 ✔ |
| Grenade Carb Killa | Maltitol (+ xylitol in Caramel Chaos) | ~10.6–15 g per 60 g | **Yes**, ">10 g/100 g polyols" | M26, C2 ✔ |
| Fulfil | Maltitol, maltitol syrup; xylitol, erythritol in some | 13.5 g per 55 g (24.5 g/100 g, Dark Choc Salted Caramel) | **Yes** (Choc Brownie listing) | M25 ✔ |
| Myprotein Layered / Crispy Layered | Maltitol | n/a | **Yes** | M28 ✔ |
| Optimum Nutrition Whipped | Maltitol, sorbitol, erythritol | ~12 g (Men's Fitness review) | **Yes** (Boots, Ocado) | M27 ✔ |
| PhD Smart Bar | Polyols ~20 g (from an earlier review) | ~20 g | Not confirmed | C8 (partial) |
| Misfits | Maltitol (Tesco ingredients) | n/a | Not confirmed | C31 (partial) |

- One Grenade listing advises a "**2 bars per day max**" [EVIDENCE: M26]. That is relevant to the S&C coach's comment that athletes struggled to get through boxes of bars (F4).

### 3c. Studies on gut discomfort
| Study | Finding | Relevance | Tag |
|---|---|---|---|
| Respondek et al. 2014, *Eur J Clin Nutr* (dairy desserts with maltitol 17.5–35 g + scFOS, adults) | More flatulence, rumbling, bloating and discomfort than control, but **mild and transient** | Bars carry 10–20 g polyols each; two bars approach these doses [ASSUMPTION] | [EVIDENCE: M29] |
| de Oliveira, Burini & Jeukendrup 2014, *Sports Medicine* (review) | **30–50% of athletes** report GI complaints during exercise; nutrition is one cause | Athletes are a gut-sensitive group. This is **not** evidence about bars specifically | [EVIDENCE: M30] |
| Scoping review: GI symptoms in athletes beyond endurance sports (LJMU, 2025/26) | 11.5–80% report at least one GI symptom | Includes team and combat sports | [EVIDENCE: M31] |
| Mondelēz / INQUIS trials on GI tolerance of maltitol and polydextrose (NCT06479330 and a second trial) | Ongoing, no results published | Industry itself is testing tolerance | [EVIDENCE: M32] |
| Survey of UK protein-bar eaters on gut discomfort | **Not found** | | [GAP] (WR66 has press and forum anecdotes only) |

**So what for the pitch:** every big UK protein bar Ewan competes with uses polyols, and most must legally warn about laxative effects. "No sweeteners, no sugar alcohols, no warning" is a factual, checkable difference. **Don't claim Graft is "easier to digest"**: that is a health-type claim with no test behind it.
**Confidence: high** for the polyols and warnings (from ingredient lists). **Low** for the symptom link (the studies use mild doses, and none tests protein bars in athletes).

---

## 4. Price benchmarks

### 4a–4b. Output of `research/25_market_sizing.py`
```
Product                          g  Prot g  £/bar  £/100g  £/10g P  Retailer / date
Bio&Me Protein Bar              40     9.2   1.08    2.71     1.18  Tesco 3-pack £3.25 (undated)
Graze Protein Bites (1 bite)    30     5.1   0.62    2.08     1.22  Launch RSP £2.49 / 4 (old)
Myprotein Layered Bar           60    20.0   2.50    4.17     1.25  H&B RRP (7 Oct 2026)
Graft bag bar @ £2.00           50    15.0   2.00    4.00     1.33  price under test
Grenade Carb Killa              60    20.0   2.85    4.75     1.43  Boots (seen Oct 2026)
Barebells Protein Bar           55    20.0   2.90    5.27     1.45  Tesco std price (promo page Jul-Aug 2026)
Fulfil Vitamin & Protein        55    19.5   2.90    5.27     1.49  Tesco/Sainsbury's (undated listing)
Graft bag bar @ £2.50           50    15.0   2.50    5.00     1.67  price under test
Trek Protein Flapjack           50     9.8   1.85    3.70     1.89  Tesco single (undated)
Nakd Protein                    45     7.2   1.50    3.33     2.08  H&B single (undated)
Average £/10 g protein, Barebells + Grenade + Fulfil: £1.45
```
- **Promotions:** Barebells was £1.90 with Clubcard (Jul–Aug 2026) [EVIDENCE: M16]. Grenade and Fulfil were seen at ~£2.00 at Asda and Ocado [EVIDENCE: M17, M18]. Shoppers anchor on promotional prices [ASSUMPTION].
- Graze protein per bite (17 g/100 g, Cocoa Vanilla) is from The Grocer; another source says 4 g a bite [EVIDENCE: M21, conflicting].
- **Not found:** Misfits current price, Amazon single-bar prices [GAP].

### 4c. Campus and gym vending
- PureGym started stocking **Warrior bars in its vending machines from 1 July 2025** (400+ gyms) [EVIDENCE: M35]. No vending price found [GAP].
- One Trustpilot review calls PureGym vending "extortionately priced" (one anecdote, about a drink) [EVIDENCE: M35, weak].
- Team Durham / Maiden Castle vending or café prices: **not found** [GAP]. Ewan can photograph the machines himself.

**So what for the pitch:** at £2.00, Graft costs slightly less per 10 g protein than the big three (£1.33 vs £1.45). At £2.50 it costs more (£1.67) and sits at a premium to their promotional prices, so £2.00–£2.25 is the defensible launch range.
**Confidence: medium.** Prices are real listings, but several are undated and flavours vary.

---

## 5. Trends and attitudes

### 5a. UK UPF surveys
| Finding | Source | Tag |
|---|---|---|
| UPF concern 76–78% (Apr 2024–Mar 2025); 78% in March 2025; **16–34s 72%**, 55+ 82% | FSA Consumer Insights Tracker (E, W, NI; ages 16+) | [EVIDENCE: M33] |
| 60% cut back on UPF; 75% of those for health reasons | GlobalData, Aug 2025 | [EVIDENCE: WR63] |
| Most UK adults know the term UPF but can't sort foods correctly | Robinson et al. 2024 | [EVIDENCE: WR62] |
| YouGov Apr 2025 poll on UPF health claims (n=4,589) | Labels not readable in the extract | [GAP] |

### 5b. Protein attitudes
Already covered by WR57 (Grocer 2019), WR59 (Kantar 2025) and WR60 (Euromonitor 2025). No new UK 2025–26 figure on the share of people actively seeking protein was found [GAP].

### 5c. Peer-reviewed papers
| Paper | Key finding | Fit | Tag |
|---|---|---|---|
| **Pacenta, Starkoff, Lenz & Shearer (2024), *Nutrients*:** scoping review of food insecurity in college athletes (18 studies) | Food insecurity in **9.9–65%** of college athletes. Causes include **limited money, time management, meal plans and housing amenities** | US data, but it shows that **food availability and time are structural barriers** for student athletes | [EVIDENCE: M34] |
| **Fortis, Cronin, Johnson, Shepherd, Hackney & Strauss (2025), *Nutrients* 17(23):3773**, doi 10.3390/nu17233773 (LJMU, UK) | n=72 female endurance athletes, 4-day food diaries: **carbohydrate fell short on training days**, worse with higher volume. **Protein was prioritised.** Interviews named time constraints as a barrier | UK, but the athletes average 42 years old, not students. Supports "carbs matter" (F5) | [EVIDENCE: M37] |
| Irish collegiate student athletes, nutrition knowledge (n=138), PMC article | Sports nutrition knowledge **"poor" (47%)** | Close to the UK student setting; year not seen | [EVIDENCE: M38] |
| UK university-athlete study of post-training eating | **Not found** | | [GAP] (searched "UK university student athletes dietary intake BUCS") |

**So what for the pitch:** UPF concern is mainstream (78%). The research shows athletes under-eat carbohydrate on training days and struggle with time and food access. That supports a carbohydrate-plus-protein bar that is easy to carry, but the evidence is not specific to UK students.
**Confidence: medium** (UPF data, official), **low–medium** (athlete papers are not UK-student specific).

---

## 6. Out-of-the-fridge shelf-life norms (**not proof of safety**)

| Measure | Value | Tag |
|---|---|---|
| Protein bars: water activity / moisture | aw **≤0.65**, moisture typically **10–15%**. "Intermediate-moisture" foods = aw 0.6–0.9 | [EVIDENCE: M39] (Loveday et al., Massey, 2009/10) |
| Batter cake | aw ~0.81; fresh bread ~0.93 | [EVIDENCE: M41] (secondary table) |
| Flapjack, brownie, sponge (specific aw) | **Not found** | [GAP] |
| Most bacteria | Need aw ≥0.90 (FSS 2025) | [EVIDENCE: N15, R12] |
| *Listeria* | ~0.92 | [EVIDENCE: M42] |
| *C. botulinum* | ~0.93 | [EVIDENCE: M42] (FDA guide) |
| *S. aureus* (growth / toxin) | **0.86** aerobic (0.87–0.91 in some sources) / 0.93 | [EVIDENCE: M42] |
| Xerophilic moulds, osmophilic yeasts | **~0.60–0.62** (some sources give 0.75 for yeasts) | [EVIDENCE: M42] |

**What this suggests for a ~16% moisture egg-white bar:** commercial protein bars run at 10–15% moisture and aw ≤0.65. A ~16% bar is just above that moisture range. **Water activity depends on what binds the water** (sugars, salt, glycerol), not on moisture % alone. Graft has very little sugar and no glycerol, so at 16% moisture its aw **could be higher than a commercial bar's** [ASSUMPTION]. If it is below ~0.85, pathogenic bacteria shouldn't grow. If it sits between 0.85 and 0.60, **mould over days** is the main risk. **This is not proof of safety.** Ewan needs a **lab water-activity test** (Campden BRI or similar, N14/N15), then a shelf-life or challenge test (R13), before selling an ambient bar.
**Confidence: medium** for the thresholds, **low** for any conclusion about Graft.

---

## Counter-evidence and risks
| Risk | Evidence | Tag |
|---|---|---|
| **Bar growth is modest.** The +24% headline includes drinks and powders. Grenade itself says bars grew only +5.6% | M1, M7 | [EVIDENCE] |
| **Sweetened bars are still winning.** Huel (+31%) and Optimum Nutrition (+12%) grew in 2025, and both use polyols. The shift is between brands, not proven towards "real food" | M5, C38, M27 | [EVIDENCE] |
| **High-protein claims are not booming:** 7% of UK products in 2024, below 8% in 2019 | M4 | [EVIDENCE] |
| **Young people worry least about UPF** (72% of 16–34s vs 82% of 55+). The UPF message is weaker with students | M33 | [EVIDENCE] |
| **Price:** competitors' promotional prices (£1.90–£2.00, 20 g protein) beat Graft at £2.50 (15 g). Graft gives less protein per bar | M16–M18 | [EVIDENCE] |
| **Polyol symptoms are usually mild** in trials. Judges may see "digestion" as a small problem | M29 | [EVIDENCE] |
| **Shelf-life:** a low-sugar, 16% moisture egg bar may have aw above commercial bars, so mould and texture risk is unknown | M39, M42 | [ASSUMPTION] |
| **The Durham market is small:** ~£56k a year at retail in the mid case. Scale depends on other universities and gyms | Script | [ASSUMPTION] |
| **Most papers are US-based** or not about students | M34, M37 | [EVIDENCE] |

## Gaps and what Ewan should do himself
1. **Durham library databases:** Mintel ("UK Snack Bars 2025", "Sports Nutrition"), Euromonitor Passport, Statista. Get a bar-only £ value and the share of clean-label launches (GNPD).
2. **Confirm the GB legal text:** legislation.gov.uk/eur/2011/1169/annex/III (laxative wording).
3. **Team Durham:** ask the S&C coach or the Sport office how many students are in BUCS squads and performance programmes, and how many bars they buy now (replaces the per-team assumption).
4. **Review mining (30 min):** Amazon UK, Tesco and Trustpilot reviews of Barebells, Grenade and Fulfil. Count mentions of "bloat", "stomach", "gas", "too sweet", "dense". Code them like `09_reddit_coding.csv`. Add Reddit (r/UKPersonalFinance, r/GYM, r/bjj) and TikTok comments.
5. **Prices on campus:** photograph vending and café prices at Maiden Castle and local gyms (4c gap).
6. **Lab water-activity test** on the bag bar (Campden BRI or a local university lab, `24-food-contacts.md`) before any ambient claim.
7. **Pilot data beats all of this:** sell to one squad for 4 weeks and record repeat purchase rate and bars per week. That replaces the [ASSUMPTION] rows in the sizing table.

Sources: `research/sources.md` → "Secondary market research (19 Oct 2026)", M1–M42.
