# Master Prompt Run Log

## Phase 0: Capability statement (20 Oct 2026)

| Capability | Status |
|---|---|
| Web search | ✅ Works (US-indexed search engine) |
| Opening pages / PDFs (publishers, doi.org, PubMed, Crossref, gov.uk, legislation.gov.uk) | ❌ **Blocked** by this cloud environment's network policy ("connect_rejected") |
| Durham Library databases (Mintel, Passport, Statista, SPORTDiscus, Web of Science) | ❌ Not available here |
| Highest achievable status | **SEARCH-CONFIRMED (not opened)**. No row can be marked VERIFIED until pages are opened |
| DVS week | ≈ Week 7 (inferred: "Week 5 on 6 Oct") — confirm |

**To unlock VERIFIED:** open the cloud environment menu in the session title bar → Edit → Network access, then choose a broader level or add hosts (doi.org, pubmed.ncbi.nlm.nih.gov, api.crossref.org, legislation.gov.uk, gov.uk, food.gov.uk, sportengland.org, publishers). Docs: https://code.claude.com/docs/en/cloud-environments#network-access. Or run batches somewhere with library access.

## Phase 1: Library progress

| Batch | Topic | Rows | A–B % | Status |
|---|---|---|---|---|
| 1 | UK protein and sports nutrition market | 28 | 0% | SEARCH-CONFIRMED |
| 5 | Combat-sport participation | 14 | 29% | SEARCH-CONFIRMED |
| 7 | Weight cutting | 8 | 100% | SEARCH-CONFIRMED |
| 12 | Competitors | 12 | 0% | SEARCH-CONFIRMED |
| 15 | Food safety / water activity | 10 | 50% | SEARCH-CONFIRMED |
| 17 | GB regulation | 10 | 60% | SEARCH-CONFIRMED |
| 3 | UPF and sweeteners | 9 | 56% | SEARCH-CONFIRMED |
| 9 | Post-exercise nutrition | 10 | 90% | SEARCH-CONFIRMED |
| 10 | GI and polyols | 7 | 71% | SEARCH-CONFIRMED |
| **Total** | | **108** | **39%** (A 15, B 27, C 43, D 22, E 1) | |
| Next (priority order) | 13 sponsorship/gyms · 14 precedents · 16 manufacturing · 18 pricing · 4 students and price · 6 MMA industry · then 2, 8, 11, 19, 20 | | | |

## Phase 2: Analysis
Sections A–O are already drafted in `../mma-venture-report.md` (20 Oct 2026). Update it after each batch.

## Changes to the report from these batches

| Report item | Was | Now | Source |
|---|---|---|---|
| BJJ size | ~40k members, 300+ clubs (weak) | **1,000+ clubs, ~100,000+ participants, ~50% members** (NGB estimate, 2025 AGM) | B5-006 |
| MMA count | GAP | Still GAP; **route found:** EMMAA / Safe MMA amateur registration | B5-011, B5-012 |
| Weight-cut prevalence | Hillier 2019 only | Triangulated: Hillier 2019 + Connor and Egan 2019 + Matthews and Nicholas 2017 + Zhong 2024 SR | B7-001 to B7-004 |
| Who advises fighters | Coaches (Hillier) | Coaches; sports scientists have little influence (Zhong 2024) | B7-004 |
| Performance angle | Implicit | **Drop it.** Moderate cuts don't impair performance (2022 MA), and regain doesn't predict winning (Kirk 2020) | B7-007, B7-008 |
| Competitor gut argument | "Polyols, laxative warning" | Plus: 13–18 g polyols per Grenade/Fulfil bar vs ~20 g/day EU laxative threshold; Misfits matches v13 macros but uses maltitol | B12-001 to B12-005, B17-008 |
| RXBAR | US success only | **UK launch via D2C + 200+ gyms (2018), exited UK within ~2 years**: key counter-precedent | B12-009 to B12-011 |
| JNCK Bakery | "Closed after Tesco delisting" | Liquidated Sept 2025 after a Tesco listing; **delisting not confirmed** | B12-008 |
| Shelf-life plan | aw test | Add **texture tracking** (egg-white hardening) and packaging barrier; target aw ≤0.65 | B15-007, B15-010 |
| Free samples | GAP | FSA: free supply can still be a food business; a regular pilot needs registration | B17-005 |
| Grenade decline cause | "Fell ~16% after a UPF documentary" | Channel 4 *Joe Wicks: Licensed to Kill* (6 Oct 2025); **causation contested**. Say "protein bars came under scrutiny; leader's volumes fell 15.9%" | B3-007, B3-008 |
| UPF stat | "78% (June 2026)" | **~78% (FSA tracker, March 2025)**; 76–78% across Apr 2024–Mar 2025 | B3-001, B3-002 |
| Sweeteners | "No sweeteners" | WHO 2023 advises against non-sugar sweeteners for weight control; **polyols excluded**, so keep the two statements separate | B3-006 |
| Gut argument | "Polyols upset fighters' stomachs" | **Overstated.** Maltitol diarrhoea threshold ~60–92 g; one bar is 13–18 g. Say "no sugar alcohols" plus the laxative-warning fact; test H2 | B10-003 |
| Carb guidance | "6–10 g/kg heavy training" | Confirmed overall "3–10 (up to 12) g/kg/day by load"; check the 6–10 band in the ACSM table | B9-003 |
| Product design | 15 g P / 22.5 g C | **Between sessions, carbs matter most**; protein doesn't speed glycogen refill. Consider a 2-bar session pack or a higher-carb between-session variant | B9-001, B9-007, B9-008 |
