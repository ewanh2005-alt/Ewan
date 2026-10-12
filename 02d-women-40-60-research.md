# 02d: UK women aged ~40–60 vs athletes as the target market (secondary research, v2)

**Date:** 12 Oct 2026 · **Type:** desk research only. **No interviews with this group yet.** · **Replaces:** v1 of this file (still in git history).

**Tags**
- `[EVIDENCE: WRn]` = numbered source in §11 (also in `research/sources.md`, section "Women 40–60, v2").
- `[ASSUMPTION]` and `[GAP]` as usual.
- **(>5 yrs)** = data from before Oct 2021.
- **MARKETING CLAIM** = brand or media-owner material.
- **weak** = forum, review or anecdote.

**Numbers:** `research/13_women_segment_numbers.py` (segment sizing, nutrition fit, price per 10 g protein, Meta test reach).

**How it was done**
- Four parallel desk-research passes, all on 12 Oct 2026.
- Search-result extracts only: full-text pages and ONS/Nomis tables could not be opened from this environment. Some figures therefore come from secondary summaries, and are flagged where they need checking against the original.
- **Health claims:** none are made in this report about the product. Where nutrition science is discussed, it describes the population, not the bar.

---

## Executive summary (one page)

### Key numbers
| | Figure | Tag |
|---|---|---|
| UK women aged 45–60 | **~7.2 m** | `[EVIDENCE: WR2, ONS mid-2019]` **(>5 yrs)** |
| …"active" (all-women rate 62.2%) | **~4.5 m** | `[ASSUMPTION-based, script]` |
| …gym members (45–54 rate 29%) | **~2.1 m** | `[ASSUMPTION-based, script; WR12]` |
| North East / County Durham gym-member women 45–60 | **~84,000 / ~15,000** | `[ASSUMPTION-based, script]` |
| Expert protein target for women after menopause | **1.0–1.2 g/kg/day** (~70–84 g for a 70 kg woman) | `[EVIDENCE: WR19, ESCEO 2014]` |
| UK adults meeting the 30 g fibre target | **~4%** | `[EVIDENCE: WR30, NDNS 2019–23]` |
| UK adults trying to avoid ultra-processed food | **71%** | `[EVIDENCE: WR53, Mintel 2025]` |
| Women 55–64 eating protein bars weekly | **10%** (vs 54% of 25–34s) | `[EVIDENCE: WR57, Grocer/Him 2019]` **(>5 yrs)** |
| Closest competitor | **Bio&Me Daily Boost**: 40 g, 9.2 g protein, no sweeteners, ~£1.08–1.40, aimed at women 35–45 | `[EVIDENCE: WR40]` |

### Top 5 insights
1. **There's a real nutrition need, but it's long-term, not urgent.** Protein needs rise and muscle and bone are lost faster around menopause `[EVIDENCE: WR19, WR25, WR26]`. But women feel this as a slow worry, not a daily problem. Their urgent pains are sleep, brain fog and hot flushes `[EVIDENCE: WR70]`, and a snack doesn't fix those. **Verdict: a strong "vitamin", not a "migraine".**
2. **They reject today's protein bars rather than wanting a better one.**
   - Only 14% of women (and 10% of 55–64s) ate protein bars weekly `[EVIDENCE: WR57]` **(>5 yrs)**.
   - Taste matters more to women than men `[EVIDENCE: WR57]`.
   - Three in five people think too many artificial sweeteners can cause long-term health problems `[EVIDENCE: WR61]`.
   - Your "real food, no sweeteners" angle speaks to exactly that, but nobody has shown they'll pay for it `[GAP]`.
3. **Your v6 bar fits their numbers better than it fits athletes'.** About 15 g protein in 135 kcal with ~4 g sugar is a "light, high-protein" profile. For a midlife woman one bar is ~17–21% of her daily protein target `[script]`. The weak spot is **fibre**: 2 g against Bio&Me's 8 g.
4. **The market is warming up fast.**
   - Women's health sales at Holland & Barrett are growing `[EVIDENCE: WR73]`, and Ocado opened a 300-product menopause aisle `[EVIDENCE: WR58]`.
   - Women are 51% of people trying to eat more protein (global) `[EVIDENCE: WR60]`.
   - About 80% of private weight-loss-jab users are women `[EVIDENCE: WR74]`, and expert guidance tells them to eat more protein `[EVIDENCE: WR35]`.
5. **They're reachable, but not where athletes are.**
   - Facebook is the main platform for older users `[EVIDENCE: WR79]`.
   - Mumsnet claims 1 in 3 women aged 35–54 visit each month (MARKETING CLAIM) `[EVIDENCE: WR80]`.
   - Holland & Barrett and supermarkets are their shops `[EVIDENCE: WR76]`.
   - Meal-kit use falls with age: 20% of 45–54s vs 46% of 25–34s `[EVIDENCE: WR77]`.

### Recommendation (provisional until your own interviews)
**Keep athletes as the main market. Run women 40–60 as a formal second-segment test over the next three weeks:**
- 6–8 interviews
- a blind taste test with ~15–20 women
- a £40 Meta split test

Switch only if the women's numbers clearly beat the athletes' on the scorecard in §8, and on **money** (pre-orders), not compliments.

### Biggest gaps
- UK female population by five-year band for the UK, North East and Durham (Nomis TS009 and ONS mid-2024 tables)
- Active Lives activity rates for women aged 35–54 and 55–74
- What these women spend on snacks, and what they'd pay for a fresh bar
- Any first-hand data from this group
- Protein, fibre and free-sugar intake for women by age (NDNS 2019–23 tables)

---

## 1. Segment size and profile

### 1.1 Population
| Measure | Figure | Year | Tag |
|---|---|---|---|
| UK population | 69,281,400 | mid-2024 | `[EVIDENCE: WR1]` |
| UK females aged 45–60 | 7,244,488 | mid-2019 | `[EVIDENCE: WR2]` **(>5 yrs)** |
| UK females by 5-year band (40–44 … 55–59), mid-2024 | — | — | `[GAP: ONS mid-2024 age-by-sex tables / Nomis]` |
| Second population peak (1960s baby boom) | around **age 59** | 2024-based projections | `[EVIDENCE: WR3]` |
| North East population | 2,760,678 | mid-2024 | `[EVIDENCE: WR4]` |
| North East: most populous single years | 55–59 | Census 2021 | `[EVIDENCE: WR4]` (geography ambiguous) |
| County Durham total / female | 538,011 / 275,579 | mid-2024 | `[EVIDENCE: WR4]` |
| County Durham females aged 45–54 | **32,963** | mid-2024 | `[EVIDENCE: WR5]` (Urbistat citing ONS, so verify) |
| County Durham residents aged 35–49 | fell ~15% since 2011 | Census 2021 | `[EVIDENCE: WR6]` |

**Where the "13 million" figure comes from**

| Source | What it says | Tag |
|---|---|---|
| NHS England, citing Wellbeing of Women | ~13 m peri- or menopausal women; "a third of the UK female population" | `[EVIDENCE: WR7]` |
| Menopause Support UK | Same figure, c.2016, no method given | `[EVIDENCE: WR7]` |
| NICE NG23 scope | ">11 million women over 45" (2011 Census) | `[EVIDENCE: WR7]` |

- **No primary source** has been found for the 13 m figure.
- It looks like a count of women aged 45+, not a measured number of women in peri- or post-menopause `[ASSUMPTION: inference]`.
- **In the pitch, say:** "an estimated 13 million, widely cited". Don't present it as an ONS statistic.

**Segment-size funnel** (from the script; order-of-magnitude only)

| Step | Estimate |
|---|---|
| UK women 45–60 | ~7.24 m |
| …"active" (150+ min/week, all-women rate) | ~4.5 m |
| …gym members (45–54 rate) | ~2.1 m |
| …strength training twice a week (55–64 rate) | ~1.4 m |
| North East women 45–60 / gym members | ~289,000 / ~84,000 |
| County Durham women 45–60 / gym members | ~53,000 / ~15,000 |

**How the funnel was built**
- Each step applies one age group's or one area's rate to the whole segment `[ASSUMPTION]`.
- The North East figure assumes the region has the UK's age mix. It's actually older (median age 42), so this understates it.
- **For comparison:** Durham's student-athlete pool is in the low thousands, and over 100,000 student athletes compete for UK universities `[EVIDENCE: D4]`. **Locally, the women's pool is several times bigger.**

### 1.2 Activity and exercise
| Measure | Figure | Year | Tag |
|---|---|---|---|
| Women "active" (150+ min/week), England 16+ | **62.2%** vs men 67.3% | Nov 2024-25 | `[EVIDENCE: WR8]` (secondary summary) |
| Women inactive | 26.3% | Nov 2023-24 | `[EVIDENCE: WR9]` |
| % active, women aged 35–54 and 55–74 | — | — | `[GAP: Active Lives data tables]` |
| Adults 55+ meeting the strength guideline (Sport England definition) | 38% → **41%** | 2019-20 → 2024-25 | `[EVIDENCE: WR10]` |
| Women 16+ meeting the strength guideline | **29%** vs men 36% | HSE 2021 | `[EVIDENCE: WR13]` |
| Women meeting the strength guideline, by age (Scotland) | 25–54: 33–34%; **55–64: 19%** | 2023 | `[EVIDENCE: WR11]` |
| Women 45–54 who are gym members | **29%** vs men 38% (women's peak 67% at 25–34) | 2025 | `[EVIDENCE: WR12]` (operator-commissioned poll) |
| UK gym penetration (all adults) | 16.6–16.9% | 2024–25 | `[EVIDENCE: WR14]` |
| Women's fitness participation | +1.7% (vs +0.7% for sport) | 2024–25 | `[EVIDENCE: WR85]` (advocacy) |
| Women 41–60 not meeting 150 min/week | ~one third | 2021 | `[EVIDENCE: WR15]` |
| Inactive midlife women who want to do more | 80%+ | 2021 | `[EVIDENCE: WR15]` |

**Read-across**
- **Most women in this age group are not gym-goers.** About 3 in 10 aged 45–54 are members, and only about 1 in 5 aged 55–64 do strength training.
- **The target is narrower than "midlife women":** the active, strength-training minority, roughly 1.4–2.1 m nationally.
- **No UK trend data** shows strength training among women 40+ growing `[GAP]`. The evidence is indirect: the 55+ strength figures and growth in fitness participation.

**Disagreement:** Sport England says gym growth is "much of it coming from older people" `[EVIDENCE: WR10]`. YouGov (via Jetts) says strength-training women skew young: 25% are aged 25–34 `[EVIDENCE: WR12]`. Both may be true: growth from a low base among older women.

### 1.3 Lifestyle and life stage
| Measure | Figure | Year | Tag |
|---|---|---|---|
| Employment rate, women 16–64 | 72.3–72.4% | 2025 | `[EVIDENCE: WR83]` |
| Inactivity among women 50–64 | ~29% | 2026 | `[EVIDENCE: WR83]` |
| Sandwich carers (children + adults) | 1.4 m; **61% female, 51% aged 45–64** | 2021–23 | `[EVIDENCE: WR82]` |
| North East disposable income per head | **£19,977**, the lowest UK region (UK £24,836) | 2023 | `[EVIDENCE: WR84]` |
| Women aged 40–60 with dependent children at home | — | — | `[GAP]` |
| Menopause symptoms affecting work | CIPD: 67% mostly negative impact (n 2,000+, women 40–60, 2023); Fawcett: 44% ability to work affected, 10% left a job (2022) | 2022–23 | `[EVIDENCE: WR69, WR70]` |
| HRT patients, England | ~2.8 m (+6.4%); items +370% in 10 years | 2024/25 | `[EVIDENCE: WR71]` |

**Disagreement on "10% left a job":** LSE CASE and BBC *More or Less* point out that Fawcett only sampled women with symptoms, and "left a job" may include changing jobs `[EVIDENCE: WR70]`. Don't quote the figure without that caveat.

**Profile (from the evidence)**
- Mostly working, often caring for others, short of time.
- Income is lower in the North East than nationally.
- Engaging with menopause care more than ever, judging by HRT growth.
- Snacking is mostly emotional or a treat (see §3).

---

## 2. Nutrition needs (science, not marketing)

### 2.1 Protein
| Body | Recommendation | Strength | Tag |
|---|---|---|---|
| UK RNI (COMA 1991) | 0.75 g/kg/day (~45 g for a 60 kg woman) | Guideline | `[EVIDENCE: WR16]` **(>5 yrs)** |
| PROT-AGE (2013) | ≥1.0–1.2 g/kg/day for over-65s; ≥1.2 if active | Expert consensus | `[EVIDENCE: WR17]` **(>5 yrs)** |
| ESPEN (2014) | ≥1.0–1.2 g/kg/day healthy older adults, plus resistance exercise | Expert consensus | `[EVIDENCE: WR18]` **(>5 yrs)** |
| **ESCEO (2014): postmenopausal women 50+** | **1.0–1.2 g/kg/day, with ≥20–25 g protein per main meal**, plus exercise 3–5×/week | Expert consensus | `[EVIDENCE: WR19]` **(>5 yrs)** |
| British Menopause Society / BDA / IMS 2025 / EMAS 2026 | Protein is important for muscle and bone, but **no numeric target found** | Guideline (qualitative) | `[GAP]` |

**Per meal**
- In older **men**, muscle building levelled off at about 0.4 g/kg per meal (~28 g for 70 kg) `[EVIDENCE: WR20]`.
- No equivalent study in women was found `[GAP]`.
- So **"25–30 g per meal" is a conversion based on body weight, not a figure measured in women.**

**Training matters more than extra protein**
- Across 49 trials, extra protein boosted strength-training gains, with no further benefit above ~1.6 g/kg/day `[EVIDENCE: WR21, strong]`.
- In postmenopausal women, whey helped muscle **only when combined with resistance training** `[EVIDENCE: WR22]`.
- Exercise alone improves lean mass `[EVIDENCE: WR23, 27 RCTs]`.
- In a small 10-week trial, 1.2 g/kg did no better than 0.8 g/kg `[EVIDENCE: WR24]`.
- A 2024 review calls the protein evidence for postmenopausal women "limited and not of high quality" `[EVIDENCE: WR38]`.

**Actual intake**
- UK adults on average **meet the RNI** (older NDNS data).
- In over-65s: **52% are below 1.0 g/kg and 82% below 1.2 g/kg** `[EVIDENCE: WR31]`.
- Equivalent figures for women aged 40–60 `[GAP]`.

**Disagreement:** UK policy (0.75 g/kg) vs expert groups (1.0–1.2 g/kg). The UK judged the evidence too weak to raise its figure `[EVIDENCE: WR16]`. **Honest framing:** many midlife women meet the official minimum but fall short of what expert groups recommend for keeping muscle.

### 2.2 Body changes around menopause
| Change | Evidence | Tag |
|---|---|---|
| Bone loss fastest from ~1 year before to 2 years after the final period | ~2.5%/yr at the spine, ~1.8%/yr at the femoral neck (SWAN cohort) | `[EVIDENCE: WR25, strong]` **(>5 yrs)** |
| Fat gain roughly doubles and lean mass starts falling at the transition, while scale weight barely changes | SWAN DXA, ~1,246 women | `[EVIDENCE: WR26, strong]` **(>5 yrs)** |
| Menopause status predicts lean-mass loss; physical activity protects | ERMA, 234 women aged 47–55 | `[EVIDENCE: WR27]` **(>5 yrs)** |
| Sleep disorders | 51.6% of postmenopausal women (meta-analysis of 41 studies) | `[EVIDENCE: WR37]` |
| Appetite and cravings rise at menopause | Mainly animal or mechanistic evidence; claimed on consumer sites | `[GAP: no human systematic review]` |
| Yearly rate of muscle or strength loss specific to menopause ("1–2% a year") | Not traceable to a primary study | `[GAP]` |

### 2.3 Fibre, sugar and ultra-processed food
| Measure | Figure | Year | Tag |
|---|---|---|---|
| Fibre target | 30 g/day | SACN 2015 | `[EVIDENCE: WR28]` |
| Adults meeting it | **~4%**; adults 19–64 average ~16 g/day | NDNS 2019–23 | `[EVIDENCE: WR30]` (16 g via a secondary citation) |
| Free sugars target | ≤5% of energy (~30 g/day) | SACN 2015 | `[EVIDENCE: WR28]` |
| Adults' actual free sugars | **10% of energy**; only 19% meet the 5% target | NDNS 2019–23 | `[EVIDENCE: WR29]` |
| Fibre and free sugars for women 40–60 specifically | — | — | `[GAP: NDNS 2019–23 ch. 5 tables]` |
| Ultra-processed food share of UK adult energy | **56.8%** (2008–14); 54% (2008–19) | NDNS | `[EVIDENCE: WR32, S30]` |
| Ultra-processed food and health | Linked to 32 outcomes; type 2 diabetes evidence rated "moderate" certainty; much of the rest low or very low | BMJ 2024 umbrella review | `[EVIDENCE: WR33]` |
| Ultra-processed food share for women vs men | ~52.8% vs 55.9% | — | `[UNVERIFIED: source paper not confirmed]` |

### 2.4 Weight-loss injections (GLP-1 drugs)
| Measure | Figure | Year | Tag |
|---|---|---|---|
| GB adults using a GLP-1 drug in the past year | **2.9%** (~1.6 m); higher among women and ages 45–55 | 2025 | `[EVIDENCE: WR34, strong]` |
| Private-prescription users who are women | ~80% | 2024–25 | `[EVIDENCE: WR74]` |
| British households using GLP-1 drugs | 4.1% | 2025 | `[EVIDENCE: WR74]` |
| Lean mass as a share of weight lost on these drugs | ~20–40% (one meta-analysis ~25%) | 2021–24 | `[EVIDENCE: WR36]` |
| Expert advice to users | Protein **1.2–1.6 g/kg/day** plus strength training | US advisory 2025 | `[EVIDENCE: WR35]` |
| UK numeric protein target for users (NICE / BDA / BOMSS) | — | — | `[GAP]` |

The two prevalence figures measure different things (individuals vs households), so they don't conflict.

**Why this matters:** a growing, mostly female, midlife group is being told to eat more protein on reduced appetite. **A small, light, high-protein, real-food snack fits that brief.** It is also a sensitive area: no claims linking the product to the drugs or to weight loss.

### 2.5 What you can legally say (GB)
| Claim | Rule | Your v6 bar | Tag |
|---|---|---|---|
| "High protein" | ≥20% of energy from protein | **~43%: OK** | `[EVIDENCE: WR39]`, script |
| "Source of fibre" | ≥3 g/100 g (high fibre ≥6 g) | ~4.2 g/100 g: **possible** after lab testing; "high fibre" no | `[EVIDENCE: WR39]`, script |
| "Protein contributes to the maintenance of muscle mass / normal bones" | Authorised; the food must be at least a "source of protein" | OK (with evidence on file) | `[EVIDENCE: WR39]` |
| Anything about menopause, hormones, hot flushes, "meno belly", weight loss | **No authorised claim**; EFSA rejected soy isoflavone menopause claims | **Do not use** | `[EVIDENCE: WR39]` |
| Low sugar | ≤5 g/100 g | ~7.6 g/100 g: **no** | `[EVIDENCE: 04-nutrition rules]`, script |

**Words you can use:** "made for women who lift" or "for midlife strength" is positioning, not a health claim `[ASSUMPTION: get CAP/Trading Standards advice before printing]`.

---

## 3. Behaviour and motivations

### 3.1 When and why they snack
- **58%** of UK consumers often snack between meals `[EVIDENCE: WR54, YouGov 2022]`.
- In 2015, **65% of over-55s** snacked daily vs 86% of 25–34s, and many 45–54s skipped lunch (64%) `[EVIDENCE: WR55]` **(>5 yrs)**.
- **Reasons:**
  - boredom (41%) `[EVIDENCE: WR54]`
  - treating yourself, the #2 reason `[EVIDENCE: WR53]`
  - evenings in front of the TV (59%) `[EVIDENCE: WR54]`
  - stress: twice as many women as men snack because of it `[EVIDENCE: WR55]` **(>5 yrs)**
- Over half of snack eaters say they snack partly to **boost nutrient intake** `[EVIDENCE: WR53]`.
- Over-55s rate health as a more important snacking need `[EVIDENCE: WR56]`.
- Snacking frequency and timing for women aged 40–60 specifically `[GAP]`.

### 3.2 What drives choice
| Driver | Evidence | Tag |
|---|---|---|
| Taste | 66% of women vs 52% of men say taste matters most when choosing protein products | `[EVIDENCE: WR57]` **(>5 yrs)** |
| Low or no sugar | Top thing over-55s look for (36%) | `[EVIDENCE: WR56]` (supplier research, 2021) **(>5 yrs)** |
| Fewer ingredients | 77% of snack eaters find this more attractive | `[EVIDENCE: WR53]` |
| Avoiding ultra-processed food | 71% try to avoid (Mintel 2025); 60.1% cut back in the past year (GlobalData 2025); 76–78% worried (FSA tracker) | `[EVIDENCE: WR53, WR63, WR64]` |
| Higher protein | 21% of UK households actively seek it, with the fastest growth among **Gen X (44–59)** and Boomers | `[EVIDENCE: WR59]` (Kantar via a dairy brand, so verify) |
| Help with menopause food choices | 68% unsure which diet changes help; 71% say menopause-friendly products are hard to find | `[EVIDENCE: WR58]` (Ocado survey, n 2,000+, 2025) |
| Price | UK shoppers are less willing to pay premiums than other Europeans | `[EVIDENCE: WR76 / GNT via WR61]` |

**Disagreements on ultra-processed food**
- **Who avoids it most:** concern is highest among richer, better-educated people `[EVIDENCE: WR62]`. One poll found over-50s more "very concerned" (35% vs 22% of under-30s), but GlobalData found the biggest cut-backs among Gen Z `[EVIDENCE: WR63, WR64]`. **Concern and action don't line up neatly by age.**
- **Data split by sex:** no data showing how women avoid ultra-processed food differently from men `[GAP]`.

### 3.3 Attitudes to protein and strength
| Attitude | Evidence | Tag |
|---|---|---|
| Protein bars seen as male or gym products | Weekly bar eating: men about a third vs women 14% | `[EVIDENCE: WR57]` **(>5 yrs)** |
| Worry about "bulking up" | 28% of women avoided or hesitated over protein powder (base unclear) | `[EVIDENCE: WR65]` (brand-commissioned) |
| More open to lifting | 67% of women more likely to pick up weights than a few years ago | `[EVIDENCE: WR65]` (brand-commissioned) |
| Brands' view | Many protein products are aimed at men and gym-goers (Coconut Collab, 2024) | `[EVIDENCE: WR52]` |
| Rising demand | Women are 51% of people seeking more protein (global) | `[EVIDENCE: WR60]` |

### 3.4 Where they get advice
| Source | Evidence | Tag |
|---|---|---|
| Holland & Barrett | ~600 in-store women's health coaches; menopause nurse helpline bookings +144% | `[EVIDENCE: WR73]` |
| Ocado | Menopause aisle with GenM (Nov 2025) | `[EVIDENCE: WR58]` |
| Supermarket advice | 81% would feel more confident buying with expert-backed advice | `[EVIDENCE: WR58]` |
| Influencers | Dr Louise Newson tops a UK women's-health influencer ranking (podcast 8.2 m downloads, MARKETING CLAIM) | `[EVIDENCE: WR80 list]` |
| Mumsnet | Huge reach (see §6), but no protein-bar threads found; one 2016 menopause-food thread mentions soy and cutting sugar, not bars | `[EVIDENCE: WR68]` (weak) |

---

## 4. Pain points, and is it a "migraine" or a "vitamin"?

### 4.1 Pain points with current options
| Pain point | Evidence | Strength | Tag |
|---|---|---|---|
| Sweeteners and aftertaste | 3 in 5 think too many artificial sweeteners can cause long-term health problems; reviews say Barebells has a "slightly bitter aftertaste" | Survey + reviews | `[EVIDENCE: WR61, WR67]` |
| Gut upset from polyols and chicory fibre | Gut-health expert names maltitol and chicory root fibre; one bar tested at 20 g polyols; forum users report diarrhoea | Trade + **weak** | `[EVIDENCE: WR66]` |
| "Not real food" / ultra-processed | 71% try to avoid ultra-processed food; nutritionists advise whole-food protein over bars | Survey + trade | `[EVIDENCE: WR53, WR66]` |
| Too macho, gym-coded | Women eat bars weekly at less than half the rate of men; brands say the category is aimed at men | Survey **(>5 yrs)** + trade | `[EVIDENCE: WR57, WR52]` |
| "Healthy" bars are sugary | Nākd Protein 13 g sugar, KIND Protein 8.6 g, Trek flapjack 14 g | Product data | `[EVIDENCE: WR46, WR47, WR49]` |
| Price | Bars typically £2–3 | Product data | `[EVIDENCE: WR43–WR45]` |
| Confusion about what to eat | 68% unsure which diet changes help with menopause | Survey | `[EVIDENCE: WR58]` |

**No published quotes from women 40–60 about protein bars were found.** None are invented here. Real quotes must come from your interviews.

### 4.2 Migraine vs vitamin

| For "migraine" (urgent) | For "vitamin" (nice to have) |
|---|---|
| Symptoms are severe and common: 77% find at least one very difficult; sleep 84%; brain fog 73% `[EVIDENCE: WR70]` | Those pains aren't food-snack problems. A bar doesn't fix sleep or hot flushes, and you can't claim it does |
| They're actively searching and not finding: 68% unsure, 71% can't find products `[EVIDENCE: WR58]`; H&B helpline +144% `[EVIDENCE: WR73]` | Snacking is mainly a treat or emotional `[EVIDENCE: WR53, WR54]`, so a health snack competes with chocolate |
| Weight-loss-jab users (mostly women) are told to eat more protein `[EVIDENCE: WR34, WR35, WR74]` | Most UK adults already meet the official protein minimum `[EVIDENCE: WR31]`; the "gap" is against expert targets only |
| Muscle and bone loss is fastest at this life stage `[EVIDENCE: WR25, WR26]` | Only 10% of 55–64s ate protein bars weekly `[EVIDENCE: WR57]`; many simply avoid the category |
| | Quark pots give 15–25 g protein for 85p–£1.25 `[EVIDENCE: WR52]`; cheap real-food options exist |

**Verdict:** **"Vitamin"**, with one possible "migraine" pocket:
- **Who:** women who strength-train, or who are on weight-loss jabs, and are actively trying to hit a protein number without ultra-processed bars `[ASSUMPTION: test in interviews]`.
- **Athletes for comparison:** their problem is a "migraine". It happens after every session, they're told to eat real food, and nothing convenient fits `[EVIDENCE: 01d, 02c]`.

---

## 5. Competitor table (UK, prices seen 12 Oct 2026)

| Product | g | Protein | Carbs | Sugar | Fibre | kcal | Protein source | Sweetener / polyols | Price (retailer) | £ per 10 g protein | Positioning (MARKETING CLAIM) | Tag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **fettle v6 (yours)** | 50 | ~14.6 | ~14 | ~3.8 | ~2.1 | ~135 | Egg, quark | None | £2.00–2.50 (test) | £1.37–1.71 | Real food, fresh | script |
| **Bio&Me Daily Boost** | 40 | 9.2 | 14 | 5.2–6.3 | 7.6–8 | 145 | Soya | None | £3.25/3 (Tesco), ~£1.08; single ~£1.40 | £1.17 | "Less male-oriented"; aimed at women 35–45; gut health | `[WR40]` |
| **Mena bar** | ~50 | GAP | GAP | GAP | GAP | GAP | Soya, oats | GAP | £22.50/10, ~£2.25 (direct only) | GAP | "UK's first menopause friendly food range" | `[WR41]` |
| Trek High Protein | 55 | 15–16 | GAP | ~4.7 | "high" | ~200 | Soya | **Stevia** | £2.50 (Ocado) | £1.67 | "15g plant protein" | `[WR49]` |
| Fulfil | 55 | 18.9 | 19.3 (17.8 polyols) | 1.1 | 2.5 | 186 | Milk | **Maltitol, sucralose** | £2.90 (Tesco) | £1.53 | Vitamins + protein | `[WR43]` |
| Barebells | 55 | 20 | 15 | 1.5 | GAP | 200 | Milk proteins | **Maltitol, sucralose** | £2.90 (Tesco) | £1.45 | "No added sugar" | `[WR44]` |
| Grenade | 60 | 20 | 20 (+~15 polyols) | 1.3 | 2.5 | 226 | Casein, whey, collagen | **Maltitol, sucralose** | £2.70 (Tesco) | £1.35 | High protein | `[WR45]` |
| H&B Precision Engineered | 60 | 21 | 19 | 1.3 | GAP | 187 | Whey, soy, collagen | GAP | £1.80 (H&B) | £0.86 | Informed Sport | `[WR50]` |
| KIND Protein | 50 | 12 | 15 | 8.6 | 3.3 | 268 | Nuts, soy | None (syrups) | £2.40 (Sainsbury's) | £2.00 | "#1 ingredient nuts" | `[WR46]` |
| Nākd Protein | 45 | 7.2 | 15 | 13 | 7.2 | 191 | Peanut | None | £3.30/3 (Tesco), ~£1.10 | £1.53 | 100% natural | `[WR47]` |
| Perkier Protein | 35 | 5.6–6.1 | 9.5 | 6.3–6.8 | 7.8–8.1 | 140–149 | Soy, peanut | None | £1.79/3 (Morrisons) | £1.07 | "40% less sugar" | `[WR48]` |
| Trek Protein Flapjack | 50 | 9 | GAP | 14 | GAP | 227 | Soya | None | £1.65 (Tesco) | £1.83 | Plant protein | `[WR49]` |
| Graze Oat Boosts | 50 | 3.2 | 17 | 4.5 | 8.6 | 193 | Oats, soya | None | £1.20 (Tesco) | — | "60% less sugar" | `[WR42]` |
| MenoWell (US) | GAP | 7 | GAP | 1–3 | high | 150–160 | Pea | GAP | Not sold in UK | — | "Menopause… bars for women" | `[WR51]` |
| **Substitute:** Graham's Protein 25 quark | 200 | 25 | 15 | 11 | — | 166 | Quark | None (sugar) | £0.85 (Tesco) | **£0.34** | "25g protein per pot" | `[WR52]` |
| **Substitute:** Lindahls Kvarg | 150 | 15 | — | 5.6 | — | 86 | Quark | **Aspartame, ace-K** | £1.25 (Tesco) | £0.83 | Low sugar | `[WR52]` |
| **Substitute:** Arla Protein yogurt | 200 | 20 | 12.8 | 12 | — | 142 | Milk | Sweetener | £1.45 (Tesco) | £0.73 | 20 g protein | `[WR52]` |
| **Substitute:** Coconut Collab Protein Yog | 170 serving | 10 | — | ~2 | ~1.7 | ~230 | Almond, soy | None | £2.75 / 350 g | — | Launched "to support menopause" | `[WR52]` |

All nutrition and positioning figures are what brands state on packs or retailer pages (MARKETING CLAIMS), not independent tests. £ per 10 g protein comes from the script.

### Where the gap is
**No UK bar combines all four:**
1. ≥12 g protein from dairy or egg
2. no sweeteners or polyols
3. ≤5 g sugar
4. under 150 kcal

That's your space.

**But:**
- **Bio&Me** already owns "women + clean label + bar" in Tesco, Waitrose and Holland & Barrett, at half your price.
- **Quark pots** give the same real-food protein for a third of the cost per gram (just not as a bar).
- **Your weaknesses for this segment:**
  - price: 25–60% more per gram of protein than Bio&Me or quark
  - fibre: 2 g vs 8 g
  - must be kept in the fridge
  - not in shops

---

## 6. Channels, price and marketing

### 6.1 Where they buy
| Channel | Evidence | Tag |
|---|---|---|
| Supermarkets | 54% of UK snack-bar sales; protein bars and shakes £230 m in grocery (+7.5%) | `[EVIDENCE: WR76]` |
| Holland & Barrett | Women's health growth; competitor bars stocked | `[EVIDENCE: WR73, WR40]` |
| Ocado | Menopause aisle, 300+ products | `[EVIDENCE: WR58]` |
| Online / direct to consumer | Fastest-growing snack-bar channel (~8.4% CAGR) | `[EVIDENCE: WR76]` (market-research firm) |
| Meal kits and subscriptions | Use falls with age: 45–54 **20%**, 55+ **8%** (vs 46% at 25–34; all sexes) | `[EVIDENCE: WR77, 2023]` |
| | Mindful Chef says its core audience is women 40–60 (MARKETING CLAIM) | `[EVIDENCE: WR78]` |
| Channel split for women 40–60 by retailer or Amazon | — | `[GAP]` |

### 6.2 Price
| Evidence | Tag |
|---|---|
| Typical protein bar £2–3 | `[EVIDENCE: WR43–WR45]` |
| Women-targeted clean bars ~£1.10–1.40 | `[EVIDENCE: WR40, WR47]` |
| Menopause bar (Mena) ~£2.25 | `[EVIDENCE: WR41]` |
| 76% "willing to pay more" for higher protein | `[EVIDENCE: WR59]` (secondhand; stated intent, not behaviour) |
| UK shoppers' resistance to premiums | `[EVIDENCE: WR61]` |
| North East income is lowest in the UK | `[EVIDENCE: WR84]` |

**Willingness to pay for a fresh, chilled weekly box (this segment):** `[GAP]`.

**Pricing reasoning:** £2.00–2.50 is the right range to **test** `[ASSUMPTION]`.
- **Above £2.25:** you're more expensive than everything women-targeted.
- **Below £2.00:** the scale model doesn't work (`10-scale-plan.md`).

### 6.3 Marketing channels
| Channel | Evidence | Tag |
|---|---|---|
| Social media overall | 89% of adult internet users use at least one platform | `[EVIDENCE: WR79, Ofcom 2025]` |
| Facebook | Most common "main" platform (48%), driven by older users | `[EVIDENCE: WR79, Ofcom 2024]` |
| Instagram | Women 45–54 = 7.6% of UK users (~2.9 m) | `[EVIDENCE: WR81]` (ad-audience estimate) |
| Mumsnet | "1 in 3 women aged 35–54 visit monthly"; 8 m+ users; minimum ad spend £5k (MARKETING CLAIMS) | `[EVIDENCE: WR80]` |
| Meta ad costs (UK) | CPM ~£18.89; CPC ~£1.17 | `[EVIDENCE: WR75]` (third-party benchmark, 2025) |
| Platform use for women 45–54 specifically (Ofcom) | — | `[GAP]` |
| Meta cost for audiences of women 45–54 | — | `[GAP]` |

**Free routes for a student founder**
- local Facebook groups (Durham mums, running clubs, menopause support groups; post only where the group rules allow)
- gym and Pilates studio noticeboards (your poster)
- parkrun
- women's strength classes at local gyms

---

## 7. Fit with your product, and recommendations

### 7.1 Product fit
| Need (women 40–60) | v6 bar | Fit |
|---|---|---|
| Protein toward 1.0–1.2 g/kg | ~15 g = 17–21% of the daily target | ✅ Good |
| Low calories, low sugar | 135 kcal, ~4 g sugar | ✅ Better than KIND, Nākd, Trek |
| No sweeteners or ultra-processed ingredients | Egg, quark, oats | ✅ Core difference |
| Fibre (gap of ~14 g/day) | ~2 g | ⚠️ Weak vs Bio&Me (8 g) |
| Carbs | ~14 g | ➖ Neutral. Women may not need "recovery carbs"; athletes do |
| Taste (#1 for women) | v1–v4 failed; v6 untested | ❌ Unknown, the biggest risk |
| Convenience | Fridge, 3-day life | ⚠️ Worse than shelf-stable bars |
| Price | £2.00–2.50 | ⚠️ Above Bio&Me and quark |

### 7.2 If you test this segment, what changes
- **Product:**
  - Same base bar.
  - Test **one "lighter" variant**: fewer oats, a little more quark, plus **ground flaxseed or chia** to lift fibre towards ~4–5 g. Run it in `04d_recovery_calcs.py` before baking `[ASSUMPTION]`.
  - Keep a **single bar** (not a 2-pack).
- **Message:**
  - "Real-food protein. No sweeteners. No powders you can't pronounce." "~15 g protein, 135 kcal."
  - **No** "menopause" health claims and no weight-loss claims.
  - "For women who lift" is positioning, which is fine.
- **Price:** test £2.00 vs £2.50, and a weekly box of 6 rather than 12 `[ASSUMPTION]`.
- **Channels:** Facebook groups, local women's strength and Pilates classes, parkrun. Holland & Barrett is a later, scale-stage conversation (you've already emailed them).
- **What stays the same:** the brand, kitchen, recipe base and Simmer-style delivery. **Testing costs you almost nothing extra**, which is why it's worth doing.

---

## 8. Scorecard: athletes vs women 40–60 (1 = weak, 5 = strong)

| Criterion | Athletes | Women 40–60 | Why |
|---|---|---|---|
| **Pain urgency (migraine)** | **5** | 2 | Athletes refuel after every session; women's need is long-term (§4.2) |
| **Segment size (local)** | 2 | **4** | ~15,000 gym-member women 45–60 in County Durham vs a few thousand student athletes (§1.1) `[ASSUMPTION-based]` |
| **Willingness to pay** | 3 | 3 | Neither tested; athletes are students (low income); women earn more but NE income is low and Bio&Me is £1.08 (§6.2) `[GAP]` |
| **Competition** | 3 | 2 | Athletes: lab bars (beatable on "real food"); women: Bio&Me already targets them, cheaply, in shops (§5) |
| **Product fit (v6)** | 4 | 4 | Athletes want carbs (✓); women want low kcal and no sweeteners (✓) but more fibre (✗) (§7.1) |
| **Reachability / route to sale** | **5** | 3 | Squads = one coach, one drop (`10-scale-plan.md`); women = many individual buyers, Facebook / Mumsnet (§6.3) |
| **Your credibility (founder–market fit)** | **5** | 2 | You train MMA and lift; you aren't a midlife woman. You'd need a credible partner or adviser |
| **Evidence you have now** | 3 | 1 | 10+ athlete interviews vs zero with women 40–60 |
| **Total (out of 40)** | **30** | **21** | |

**What would change the call:** the women's segment wins only if your tests show:
- interviews with **clear, repeated frustration** with current snacks
- taste-test "would buy again" **≥50%**
- the Meta test showing **lower cost per sign-up** than the athlete ad
- **at least 2–3 paid pre-orders**

---

## 9. Primary research plan (next 3 weeks)

### 9.1 Interviews: 6–8 women aged 40–60 who exercise at least twice a week, 20 min each
**Rules (Mom Test style)**
- Ask about **past behaviour**, not opinions about your idea.
- Don't mention the bar until the final two questions.
- Record (with permission) or take notes, and write them up within 24 hours.

1. Tell me about a typical week of exercise. What do you do, and when?
2. Walk me through what you ate yesterday between meals. When, what, and why that?
3. When you last ate something straight after exercise, what was it? Where did it come from?
4. Have you ever bought a protein bar, shake or protein yogurt? Tell me about the last time. What made you buy it? Did you buy it again?
5. What's put you off protein products, if anything? Can you remember a specific product?
6. How much do you think about protein, sugar or "processed" food when you shop? Can you give me an example from your last shop?
7. Has anything changed in how you eat or train over the last few years? What prompted it?
8. Where do you get food or fitness advice? Who or what do you trust?
9. What do you usually spend on snacks in a week, roughly? Where do you buy them?
10. Have you ever used a food subscription or delivery box (Simmer, Mindful Chef, Gousto)? Why did you start, and why did you stop?
11. *(Show the bar card: ingredients and nutrition.)* What's your first reaction? What would stop you buying it?
12. If this were available next week at £2.25, delivered weekly, would you order a trial box? *(Ask for the pre-order. That's the real answer.)*

**Avoid** "Would you buy…?" and "Do you like…?" until Q11–12. Never lead with menopause; let them raise it.

### 9.2 Survey (Google Form, poster QR code and Facebook groups): 10 questions, under 3 minutes
1. Age band: 18–29 / 30–39 / 40–49 / 50–60 / 60+
2. Gender
3. How often do you exercise? (never → 5+ times a week)
4. Main type: gym weights / classes / running / walking / Pilates or yoga / team sport / other
5. In the last month, how often did you eat a protein bar? (never / 1–3 times / weekly / several times a week)
6. What matters most when you choose a snack? Rank: taste, protein, low sugar, natural ingredients, price, convenience
7. Which bothers you about protein bars? Tick all: sweeteners / aftertaste / gut upset / too sugary / too processed / price / "not for me" / nothing
8. Would you keep a snack in the fridge if it meant no preservatives? (yes / maybe / no)
9. What's the most you'd pay for one fresh, real-food protein bar? (£1.50 / £2.00 / £2.50 / £3.00)
10. Want to try a free sample or join the waitlist? (email, optional, with GDPR consent wording)

Questions 1–2 let you **split results by segment**, so the same form serves athletes and women.

### 9.3 Blind taste test
| Item | Design |
|---|---|
| Who | **15–20 women aged 40–60** who exercise (plus your planned 20 athletes, same protocol) |
| What | 3 coded samples (e.g. 417, 238, 951): **fettle v6** (best flavour), **Bio&Me Daily Boost** (closest competitor) and **Trek High Protein** (closest macros) |
| Order | Rotate which sample goes first; water between samples |
| Scores | 9-point liking scale for overall, taste, texture, sweetness. Texture "just right" scale (too dry ↔ too moist). "Would you buy this?" (5-point). Price you'd pay. Favourite of the three |
| Pass mark | fettle overall liking **≥7/9**, **≥50%** "would probably or definitely buy", and not last on texture |
| Safety | Allergen sheet (egg, milk, oats/gluten, peanut in chocolate, soya in competitors); ask about allergies first; consent. Friends and family only until your food business registration and Level 2 hygiene are done (see `10-scale-plan.md`) |
| Analysis | Mean and spread per sample; % top-2 purchase intent; split by segment. With n≈20, report it as a **directional** result, not proof |

### 9.4 Meta split test (£40)
| Item | Design |
|---|---|
| Goal | Which segment signs up to the waitlist more cheaply? |
| Set-up | One campaign, **2 ad sets, £20 each, 5–7 days**, same image of the bar, County Durham + Newcastle radius |
| Ad set A (athletes) | Men and women 18–30, interests: gym, MMA, rugby, football, CrossFit. Copy: "Real-food recovery bar. 15 g protein from egg and quark. No whey. No sweeteners." |
| Ad set B (women 40–60) | Women 40–60, interests: strength training, Pilates, parkrun, healthy eating. Copy: "Real-food protein snack. ~15 g protein, 135 kcal, no sweeteners or powders." No menopause or weight-loss claims |
| Landing | Same waitlist page, with a hidden field or separate link per ad set (e.g. `?src=A` / `?src=B`) |
| Measure | Click-through rate, cost per click, **cost per waitlist sign-up** |
| Expected reach | ~2,100 impressions, **~34 clicks (~17 per ad set)**, perhaps ~5 sign-ups `[script; CPM/CPC from WR75; sign-up rate ASSUMPTION]` |
| Honest limit | **Far too small for a statistically reliable answer.** Use it as a directional signal alongside the interviews. If one ad set gets 3× the sign-ups, that's worth noting |
| What you need to set up | A Meta Business account and ad account (your own card); a working form connected to the landing page. **I haven't set any of this up.** It's an external account and payment, so it's your call |

---

## 10. Gaps and how to fill them
| Gap | How to fill it | Time |
|---|---|---|
| UK, North East and Durham females by 5-year band (mid-2024, Census 2021) | Nomis Census 2021 table TS009; ONS mid-2024 "related data" tables | 15 min |
| Active Lives % active for women aged 35–54 and 55–74 | Sport England Active Lives online tool / data tables | 15 min |
| Fibre, free sugars and protein for women by age | NDNS 2019–23 report, chapter 5 tables (gov.uk) | 30 min |
| What women 40–60 spend on snacks; willingness to pay | Your survey Q9 + interview Q9 + pre-order ask | 2–3 weeks |
| Real pain points and quotes | 6–8 interviews (§9.1); never paraphrase as a quote | 2–3 weeks |
| Snack and protein-bar buyers by sex and age | Kantar / Euromonitor (paywalled); ask Durham University library or Business School for Mintel access | 1 hour |
| Meta cost for women 45–54 | Run the £40 test; it will tell you | 1 week |
| Mena nutrition panel | Email Mena or buy one bar | 1 week |
| Menopause-specific protein target (BMS / IMS 2025) | BMS / Women's Health Concern "Nutrition in menopause" fact sheet; IMS 2025 *Climacteric* sarcopenia section | 30 min |
| Primary source for the "13 million" figure | Ask Wellbeing of Women for their method, or just call it "estimated / widely cited" | Optional |
| Whether "for women who lift" style wording is acceptable | Primary Authority / Trading Standards or CAP Copy Advice (free) before printing anything | 1 week |

---

## 11. Sources (numbered; all accessed 12 Oct 2026 via search extracts)
**Population and life stage**
- WR1 ONS, Population estimates UK mid-2024: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/bulletins/annualmidyearpopulationestimates/mid2024
- WR2 ONS FOI, women aged 45–60 UK (mid-2019): https://www.ons.gov.uk/aboutus/transparencyandgovernance/freedomofinformationfoi/numberofwomenagedbetween45and60bothintheukandinengland
- WR3 ONS, National population projections 2024-based: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections/bulletins/nationalpopulationprojections/2024based
- WR4 citypopulation.de (citing ONS) North East / County Durham: https://citypopulation.de/en/uk/admin/E06000047u__county_durham · NECA Evidence Hub: https://evidencehub.northeast-ca.gov.uk/report/population-by-age-2021-census
- WR5 Urbistat, County Durham by age (citing ONS 2024): https://ugeo.urbistat.com/AdminStat/en/uk/demografia/eta/county-durham/45/4
- WR6 ONS, How the population changed in County Durham (Census 2021): https://www.ons.gov.uk/visualisations/censuspopulationchange/E06000047
- WR7 "13 million" origin: NHS England https://www.engage.england.nhs.uk/safety-and-innovation/menopause-in-the-workplace/ · Menopause Support https://menopausesupport.co.uk/menopause-the-facts/ · NICE NG23 final scope https://nice.org.uk/guidance/ng23/documents/menopause-final-scope2

**Activity and exercise**
- WR8 Sport in Herts, Active Lives Adult headlines 2024-25: https://sportinherts.org.uk/newsfuse/uploads/documents/2026-May/2663-Actives-Lives-Adult-Headlines-24-25.pdf
- WR9 Sport England, Active Lives Adult Nov 2023-24 / 2024-25 reports: https://sportengland-production-files.s3.eu-west-2.amazonaws.com/s3fs-public/2025-04/ActiveLivesAdult-Nov23-24_V9-23-04-25-10-03-03-02.pdf · https://sportengland-production-files.s3.eu-west-2.amazonaws.com/s3fs-public/2026-04/Active%20Lives%20Adult%20Survey%20November%202024-25%20Report.pdf
- WR10 Sport England, Older adults: https://www.sportengland.org/research-and-data/research/older-adults
- WR11 BMC Public Health 2026 (Scottish Health Survey 2023 analysis): https://link.springer.com/article/10.1186/s12889-026-26207-9
- WR12 Health Club Management, Total Fitness white paper 2025: https://www.healthclubmanagement.co.uk/health-club-management-news/Total-Fitness-white-paper-reveals-that-gyms-are-still-failing-women/362724 · Jetts/YouGov: https://www.healthclubmanagement.co.uk/health-club-management-news/Jetts-UK-empowers-women-to-lift-with-new-programme/361507
- WR13 Health Survey for England 2021, physical activity: https://nhsd-proxy.openprescribing.net/data-and-information/publications/statistical/health-survey-for-england/2021-part-2/physical-activity
- WR14 Leisure DB 2025: https://www.healthclubmanagement.co.uk/health-club-management-news/Industry-metrics-are-at-an-all-time-high-says-LeisureDB-David-Minton/356016 · ukactive Market Report 2025: https://www.ukactive.com/wp-content/uploads/2025/04/UK-Health-and-Fitness-Market-Report-2025.pdf
- WR15 Women in Sport, midlife and menopause (2021): https://womeninsport.org/resource/inspiring-women-to-be-active-during-midlife-and-menopause/

**Nutrition science**
- WR16 BNF nutrition requirements: https://www.nutrition.org.uk/media/nmmewdug/nutrition-requirements.pdf · COMA 1991 DRVs: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/743786/Dietary_Reference_Values_for_Food_Energy_and_Nutrients_for_the_United_Kingdom__1991_.pdf · Frontiers in Nutrition 2024: https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2024.1394916/pdf
- WR17 Bauer et al. 2013, PROT-AGE (JAMDA): https://researchexperts.utmb.edu/en/publications/evidence-based-recommendations-for-optimal-dietary-protein-intake/
- WR18 Deutz et al. 2014, ESPEN (Clin Nutr): https://pmc.ncbi.nlm.nih.gov/articles/PMC4208946/
- WR19 Rizzoli et al. 2014, ESCEO (Maturitas): https://www.esceo.org/sites/esceo/files/pdf/The%20role%20of%20dietary%20protein%20and%20vitamin%20D%20in%20maintainning%20musculoskeletal%20health_Maturitas%202014_Rizzoli%20et%20al.pdf
- WR20 Moore et al. 2015 (J Gerontol A): https://experts.mcmaster.ca/scholarly-works/1615370
- WR21 Morton et al. 2018 (BJSM): https://pubmed.ncbi.nlm.nih.gov/28698222/
- WR22 Kuo et al. 2022 (Nutrients): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9572824/
- WR23 Tan et al. 2023 (BMC Women's Health): https://pmc.ncbi.nlm.nih.gov/articles/PMC10647115/
- WR24 RCT 1.2 vs 0.8 g/kg in postmenopausal women (2017): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5622767/
- WR25 SWAN bone density rates: https://pmc.ncbi.nlm.nih.gov/articles/PMC7069840
- WR26 Greendale et al. 2019 (JCI Insight): https://insight.jci.org/articles/view/124865/pdf
- WR27 Juppi et al. 2020 (J Clin Med): https://jyx.jyu.fi/handle/123456789/69265
- WR28 SACN, Carbohydrates and Health (2015): https://assets.publishing.service.gov.uk/media/5a7f7cc3ed915d74e622ac2a/SACN_Carbohydrates_and_Health.pdf
- WR29 NDNS 2019 to 2023 report (2025): https://www.gov.uk/government/statistics/national-diet-and-nutrition-survey-2019-to-2023/national-diet-and-nutrition-survey-2019-to-2023-report
- WR30 BAPEN NDNS summary: https://www.bapen.org.uk/other-news/national-diet-and-nutrition-survey-report-key-findings/ · Food Foundation: https://foodfoundation.org.uk/news/uk-still-failing-meet-basic-dietary-guidelines · Trends in Food Science 2025: https://doi.org/10.1093/trfood/vxaf021
- WR31 Protein intake in over-65s, NDNS (Age & Ageing 2024): https://academic.oup.com/ageing/article/53/Supplement_1/afad246.078/7585064
- WR32 Rauber et al. 2018 (Nutrients), UPF in UK diet: https://www.mdpi.com/2072-6643/10/5/587
- WR33 Lane et al. 2024 (BMJ), UPF umbrella review: https://bmj.com/content/384/bmj-2023-077310
- WR34 Jackson et al. 2026 (BMC Medicine), GLP-1 use in GB: https://www.yorksj.ac.uk/news/2026/weight-loss-injections/ · https://www.news-medical.net/news/20260713/Nearly-one-in-10-Britons-use-or-want-weight-loss-medication.aspx
- WR35 Mozaffarian et al. 2025 (AJCN), nutrition priorities for GLP-1 therapy: https://ajcn.nutrition.org/article/S0002-9165(25)00240-0/fulltext
- WR36 STEP 1 DXA substudy: https://pmc.ncbi.nlm.nih.gov/articles/PMC8089287 · Neeland et al. 2024: https://pubmed.ncbi.nlm.nih.gov/40181228/
- WR37 Salari et al. 2023, sleep disorders in menopause (meta-analysis): https://pure.northampton.ac.uk/files/49477120/Salara_et_al_2023_Global_prevalence_of_sleep_disorders_during_menopause_a_meta_analysis.pdf
- WR38 Physiologia 2024 narrative review, protein in postmenopausal women: https://doaj.org/article/f746498e4cbb417d8d78396620474790

**Claims**
- WR39 European Commission nutrition claims (retained in GB): https://food.ec.europa.eu/food-safety/labelling-and-nutrition/nutrition-and-health-claims/nutrition-claims_en · EFSA protein opinion 2010: https://efsa.europa.eu/en/efsajournal/pub/1811 · EFSA soy isoflavones 2012: https://efsa.europa.eu/en/efsajournal/pub/2847 · CAP Code s.15: https://www.asa.org.uk/type/non_broadcast/code_section/15.html

**Competitors (all MARKETING CLAIMS / retailer listings)**
- WR40 Bio&Me: https://www.tesco.com/groceries/en-GB/products/322544285 · https://www.foodanddrinktechnology.com/news/62113/biome-targets-underserved-female-snacker-market-with/ · https://www.theplantbasemag.com/news/bio-me-launches-new-protein-and-fibre-bars-targeting-female-consumers
- WR41 Mena: https://www.mena-pause.co.uk/products/mena-bars-subscription-10 · https://www.foodnavigator.com/Article/2024/07/23/Menopause-friendly-foods/
- WR42 Graze Oat Boosts, Tesco: https://www.tesco.com/groceries/en-GB/products/312984803
- WR43 Fulfil, Tesco: https://www.tesco.com/groceries/en-GB/products/330772853
- WR44 Barebells, Tesco: https://www.tesco.com/groceries/en-GB/products/317399405
- WR45 Grenade, H&B IE + Trolley: https://www.hollandandbarrett.ie/shop/product/60043240 · https://www.trolley.co.uk/product/grenade-carb-killa-chocolate-chip-salted-caramel/MML834
- WR46 KIND Protein, Ocado + Trolley: https://www.ocado.com/products/kind-double-dark-chocolate-nut-protein-554679011 · https://www.trolley.co.uk/product/kind-protein-double-dark-chocolate-nut-snack-bar/RWY178
- WR47 Nākd Protein, H&B + Trolley: https://www.hollandandbarrett.com/shop/product/nakd-cocoa-hazelnut-protein-bar-45g-6100001958 · https://www.trolley.co.uk/product/nakd-protein-bars-cocoa-hazelnut/XLE519
- WR48 Perkier, Ocado + Morrisons: https://www.ocado.com/products/perkier-cacao-orange-protein-bars/620681011 · https://groceries.morrisons.com/products/perkier-crunchy-peanut-protein-bars-541314011
- WR49 Trek Protein Flapjack + High Protein: https://www.tesco.com/groceries/en-GB/products/317645938 · https://www.ocado.com/products/trek-high-protein-low-sugar-choc-caramel-protein-bar-659155011
- WR50 H&B Precision Engineered: https://www.hollandandbarrett.com/shop/product/protein-bar-belgian-brownie-60g-6100004694
- WR51 MenoWell (US): https://www.supplysidefbj.com/food-development/a-functional-food-brand-that-s-breaking-out-in-the-menopause-category
- WR52 Quark / yogurt substitutes: Graham's https://www.tesco.com/groceries/en-GB/products/309486549 · Arla https://www.tesco.com/shop/en-GB/products/286702481 · Lindahls https://www.tesco.com/shop/en-GB/products/306953849 · Coconut Collab (The Grocer) https://www.thegrocer.co.uk/new-product-development/the-coconut-collab-launches-protein-yog-to-support-menopause/693275.article

**Behaviour and attitudes**
- WR53 Mintel UK Consumer Snacking 2025: https://store.mintel.com/report/uk-consumer-snacking-market-report · https://reports.mintel.com/sinatra/oxygen/brochure/id=1155129
- WR54 YouGov snacking: https://yougov.com/en-gb/articles/32288-can-britain-resist-snack · FoodNavigator 2022: https://www.foodnavigator.com/Article/2022/06/09/the-european-snackers-who-is-snacking-on-what-where
- WR55 The Grocer Snack Report 2015 (Harris): https://www.thegrocer.co.uk/snack-report-2015/revealed-40-of-young-binge-on-crisps-and-75-skip-meals/512721.article
- WR56 Glanbia snack trends for Europe 2021: https://www.glanbianutritionals.com/sites/default/files/guides/2021-08/glanbia-nutritionals-snack-trends-for-europe-0721-04.pdf · Pladis (The Grocer): https://www.thegrocer.co.uk/analysis-and-features/pladis-indulgence-trumps-health-when-it-comes-to-snacks/550579.article
- WR57 The Grocer / Him 2019, 10 charts on protein: https://www.thegrocer.co.uk/consumer-trends/gender-bias-health-concerns-and-sports-shy-consumers-10-charts-explaining-uk-attitudes-to-protein/598311.article
- WR58 Ocado Retail menopause survey and aisle (Nov 2025): https://ocadoretail.com/media-centre/press-releases/ocado-retail-launches-uks-largest-range-of-menopause-friendly-products-thanks-to-the-mtick/
- WR59 Kantar 2025 via Graham's Family Dairy: https://www.farmersguide.co.uk/business/food-drink/grahams-family-dairy-explains-protein-boom/
- WR60 Euromonitor Sept 2025: https://www.euromonitor.com/newsroom/press-releases/september-2025/women-now-outnumber-men-globally-in-seeking-higher-protein-intake
- WR61 Mintel Sugar & Sweeteners 2024: https://store.mintel.com/report/uk-attitudes-towards-sugar-sweeteners-market-report · GNT survey: https://www.confectioneryproduction.com/news/16535/brits-seek-salty-snacks-free-additives/
- WR62 Robinson et al. 2024 (Foods): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11311829/
- WR63 GlobalData Aug 2025: https://www.globaldata.com/media/retail/ultra-processed-foods-dwindling-british-baskets-six-ten-shoppers-cut-back-says-globaldata/
- WR64 FSA tracker via FoodNavigator 2025: https://www.foodnavigator.com/Article/2025/07/10/ultra-processed-foods-dominate-consumer-concerns · Attest: https://www.askattest.com/blog/research/ultra-processed-foods-tackling-consumer-confusion
- WR65 SCI-MX / Censuswide (brand-commissioned): https://www.yorkshirepost.co.uk/must-read/protein-powders-supplements-men-and-women-can-boost-their-training-and-muscle-strength-with-protein-power-4606424
- WR66 Gut issues: Yahoo UK https://uk.news.yahoo.com/gut-health-expert-warns-high-124743719.html · NutraIngredients 2024 https://www.nutraingredients.com/Article/2024/05/21/are-protein-bars-and-powders-damaging-to-gut-health/ · Diabetes UK forum (weak) https://forum.diabetes.org.uk/boards/threads/maltilol.104254/latest
- WR67 Aftertaste reviews: https://mensfitness.co.uk/review/barebells-bar-review/ · https://www.tastingtable.com/1929398/worst-flavor-barebells-protein-bar
- WR68 Mumsnet menopause food thread (2016, weak): https://www.mumsnet.com/talk/menopause/2744300-Foods-that-I-should-be-eating-to-help-with-the-menopause

**Menopause, work and market**
- WR69 CIPD 2023: https://www.cipd.org/uk/knowledge/reports/menopause-workplace-experiences/
- WR70 Fawcett Society 2022: https://wearethecity.com/wp-content/uploads/2022/05/menopauseandtheworkplace1.pdf · LSE critique: https://sticerd.lse.ac.uk/_NEW/NEWS/abstract.asp?index=1434
- WR71 NHSBSA HRT 2024/25: https://www.nhsbsa.nhs.uk/node/14524 · https://pharmaceutical-journal.com/article/news/hrt-prescribing-increases-by-370-in-past-decade
- WR72 Grand View Research, UK menopause market: https://grandviewresearch.com/horizon/outlook/menopause-market/uk
- WR73 Holland & Barrett: https://www.warc.com/article/holland-barrett-damn-right-im-hormonal-how-hb-championed-a-new-narrative-in-womens-health-218b1156257b4b68aee5f4f1d48ec045 · https://corporate.hollandandbarrett.com/news/13-10-2025/
- WR74 GLP-1 users by sex / households: https://www.expressandstar.com/uk-news/women-and-the-middle-classes-dominate-take-up-of-weight-loss-jabs-5634985 · https://www.grocerygazette.co.uk/2026/02/02/jab-effect-weight-loss-grocery/

**Channels and marketing**
- WR75 SuperAds, UK Meta CPM / CPC 2025: https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/united-kingdom · https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/united-kingdom
- WR76 Mordor Intelligence, UK snack bars: https://mordorintelligence.com/industry-reports/united-kingdom-snack-bar-market · Circana via KamCity: https://www.kamcity.com/?p=244789
- WR77 money.co.uk meal-kit survey 2023 (via Public Sector Catering): https://www.publicsectorcatering.co.uk/news/more-half-gen-z-subscribe-recipe-delivery-services
- WR78 Mindful Chef "Eat for Joy" (LBB Online): https://lbbonline.com/news/Mindful-Chef-Eat-For-Joy-McCann
- WR79 Ofcom Adults' Media Use and Attitudes 2024 / 2025: https://www.ofcom.org.uk/__data/assets/pdf_file/0020/283025/adults-media-use-and-attitudes-report-2024.pdf · https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/media-literacy-research/adults/adults-media-use-and-attitudes-2025/adults-media-use-and-attitudes-report-2025.pdf
- WR80 Mumsnet advertising (MARKETING CLAIMS): https://advertising.mumsnet.com/ · Favikon, Dr Louise Newson: https://www.favikon.com/blog/who-is-dr-louise-newson
- WR81 NapoleonCat, UK Instagram users 2025: https://stats.napoleoncat.com/social-media-users-in-united_kingdom/2025/
- WR82 ONS, Sandwich carers: https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/articles/morethanoneinfoursandwichcarersreportsymptomsofmentalillhealth/latest
- WR83 DWP, Labour market status 50+ (Sept 2026): https://www.gov.uk/government/statistics/economic-labour-market-status-of-individuals-aged-50-and-over-trends-over-time-september-2026/economic-labour-market-status-of-individuals-aged-50-and-over-trends-over-time-september-2026 · ONS LF25: https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/timeseries/lf25/lms
- WR84 ONS, Regional GDHI: https://www.ons.gov.uk/economy/regionalaccounts/grossdisposablehouseholdincome/bulletins/regionalgrossdisposablehouseholdincomegdhi/latest
- WR85 ukactive written evidence (Parliament): https://committees.parliament.uk/writtenevidence/166594/html/

**Internal:** S30 (UPF NDNS), D4 (student athletes), 01d/02c (athlete interviews, Reddit) are in `research/sources.md`.
