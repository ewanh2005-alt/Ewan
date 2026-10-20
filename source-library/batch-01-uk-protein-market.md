# Batch 1: UK Protein and Sports Nutrition Market Size and Growth

**Run:** 20 Oct 2026 · **Prompt:** `source-hunt-mega-prompt.md` · **Data:** [`batch-01-uk-protein-market.csv`](batch-01-uk-protein-market.csv) (28 rows)

## Read this first: verification status

**None of these 28 sources meets the prompt's `VERIFIED` standard yet.** This environment's network policy blocked direct page access: every publisher, doi.org, PubMed, Crossref and legislation.gov.uk returned "connection rejected". Only the search engine got through. So:

- Each source is **`SEARCH-CONFIRMED (not opened)`**. The search index shows the page exists, at that URL, with that title, and returned the quoted text.
- Quotes without brackets are **verbatim extracts returned by search**. Quotes in `[square brackets]` are the search tool's **paraphrase**. Treat those as unverified wording and replace them with the exact sentence once you open the page.
- **To upgrade a row to `VERIFIED`:** open the URL (or the Durham Library copy), confirm title, date and figure, paste the exact sentence, and change the status. It takes about 2 minutes per row.

**Shortfall: 28 of 50.** Reasons: (1) no page access; (2) Durham Library databases (Mintel, Passport, Statista, The Grocer archive) are not reachable from here, and they hold most of the credible UK market data; (3) the topic is narrow, and free web coverage is dominated by low-quality "market research" pages, which were excluded. I stopped rather than pad.

**Grade mix: A–B 0% · C 79% (22) · D 21% (6) · E 0%.** The prompt's ≥40% A–B target can't be met for market sizing, because no peer-reviewed or official UK statistics measure protein-bar sales. Official data (ONS, DEFRA Family Food) don't break out this category. Market sizing rests on industry panels (Circana, Kantar, NIQ, Mintel) by nature.

---

## 2. Reasoning summary

**What the batch establishes**
- **The UK protein category is large and growing.** Grocery protein bars + drinks + powders were worth **£225m, +24.2% YoY** (Circana via Asian Trader, 2025; B1-001). In an earlier period they were worth **£230m, +7.5%** (MAT to Nov 2024; B1-002). Kantar showed **+47% in Jan 2025, with >2m households buying** (B1-003). NIQ showed **+9.6% for protein foods** in the 26 weeks to Jan 2026 (B1-025). Grade C.
- **Big money keeps buying in:** Mondelēz–Grenade (2021; B1-009–011), Ferrero–Fulfil (2022; B1-012–013), Danone–Huel (~€1bn, 2026; B1-014–015). Listed and filed results show growth: Applied Nutrition **+24.2%** (B1-021), Myprotein back to growth (**+8.1%** in Q4 2025; B1-018–020), Huel UK **+17%** (B1-016). Grade C/D.
- **The incumbent leader is slipping:** Grenade unit sales **−15.9%** in 2025, while Optimum (+11.7%) and Huel (+31.1%) grew (B1-008). Grade C, **[SINGLE-SOURCE]**.
- **Relevant to the gap:** ~90% of 88 UK high-protein snacks exceed NHS free-sugar guidance (B1-027, D). 65% of UK consumers say they try to avoid artificial sweeteners (B1-005, C). Barebells claims **~3,500 UK gyms** stock it (B1-022, D), so gyms are a real but contested channel.

**Triangulation**
- *Category growth* is **triangulated**: industry panels (Circana, Kantar, NIQ) + company filings (THG, Applied Nutrition, Huel) + M&A activity.
- *Grenade decline* is **single-source**. Find The Grocer Top Products 2025 table.
- *Sports nutrition total (~£1.1bn)* is only weakly triangulated: Circana via trade press (B1-002) and Verified Market Research via an agency blog (B1-007).

**Contradictions**
- Protein category growth: **+7.5% vs +24.2%**. These are different periods and possibly different definitions (bars + shakes vs bars + drinks + powders), not a real conflict. Use the later Circana figure, **with its date**.
- UK sports nutrition: **£1.06bn (2023) to £1.40bn (2024)** across sources. Content-farm estimates of US$1.38–2.68bn were excluded. **Trust Circana (~£1.1bn)**: it has a named panel and period.

**What the evidence does *not* show (steelman against)**
- Nothing here is **combat-sport-specific** or about **real-food or ambient** demand. Growth is mainstream grocery protein, where Ewan can't compete.
- **Consolidation cuts both ways.** Mondelēz, Ferrero and Danone could launch a "clean" variant fast, with distribution Ewan will never match.
- Mintel reports **low consumer confidence**, and trade press flags **protein saturation** (B1-004, B1-025, B1-026). "High protein" alone no longer differentiates.
- **No UK bars-only value and no channel split (gym vs grocery vs online)** was found.

**So what for the pitch:** "UK protein is a ~£225m grocery category growing fast and attracting billion-euro deals, but its leader is losing volume and most protein snacks are high in sugar. That is the opening for a low-sugar, real-food niche."

---

## 3. Search log and exclusions

**Queries (all run 20 Oct 2026, web search; databases not reachable)**
1. `UK sports nutrition market value 2025 Circana The Grocer`
2. `The Grocer protein bars sales 2025 Grenade Barebells Fulfil`
3. `Mintel sports nutrition UK 2025 protein products usage`
4. `Grenade Ltd annual accounts turnover 2024 Companies House protein bar sales decline`
5. `Kantar protein products UK households 2025 high protein launches`
6. `ESSNA UK sports nutrition market report value`
7. `Circana UK sports nutrition £1.1bn growth protein 2025 grocery`
8. `The Grocer Top Products 2025 sports nutrition protein bars unit sales Grenade 15.9%`
9. `Huel revenue 2025 annual results UK sales growth`
10. `Mondelez acquires Grenade 2021 price protein bar UK market share`
11. `Barebells UK sales growth 2025 Vitamin Well protein bar retail sales value`
12. `THG Myprotein nutrition revenue 2025 results UK`
13. `Applied Nutrition plc full year results 2025 revenue growth UK grocery`
14. `Danone acquire Huel March 2026 €1bn`
15. `UK protein snacking saturation 2026 The Grocer high protein claims too many launches`
16. `Fulfil Nutrition sales UK 2024 2025 Vitamin Well Ferrero protein bar Ireland`

Earlier in the same session: `Circana protein bars UK grocery sales 2025 Asian Trader`.
Page fetches attempted (all blocked): asiantrader.biz ×2, mintel.com, store.mintel.com, cbinsights.com, grocerygazette.co.uk, plus doi.org, PubMed, Crossref, gov.uk and legislation.gov.uk.

**Screened ≈ 95 · included 28 · excluded ≈ 67**

| Reason | Count | Examples |
|---|---|---|
| Content farm / no stated method | 12 | MarketDataForecast, ReportCubes, Ken Research, GII/Coherent, Mordor Intelligence, IndexBox, Technavio, odoo "market outlook" blog, SEO page on nutrition testing costs, IMARC, SNS Insider, DRI |
| Wrong entity | 6 | Companies House "Grenade (UK) Ltd" (SIC 82990, not the bar firm); French/Latvian "Grenade" companies |
| Out of date, no landmark reason | 5 | Statista UK sports nutrition 2010–15; NutraIngredients 2014/2016 Euromonitor €743m; ESSNA 2011 European figure; Mars/Mintel undated 24% stat |
| Estimates with opaque method | 3 | ECDB GMV estimates (Grenade, Huel); Sacra Huel revenue estimate |
| Duplicate / syndicated | ~25 | Repeat Huel–Danone stories (City AM, ESM, Checkout, BusinessDay, HeyGoTrade); repeat THG stories; repeat Fulfil–Ferrero stories |
| Off-topic for this batch | ~16 | Brand launch news without market data; product listings; patents |

**Still to find (via Durham Library, next session)**
- Mintel *UK Attitudes towards Sports Nutrition 2026* and *Snack Bars UK*: full figures.
- Euromonitor *Sports Nutrition in the UK* (Sept 2025): value and brand shares.
- The Grocer *Top Products 2025*: Sports nutrition table (primary source for B1-008).
- Grenade Ltd statutory accounts on Companies House (correct entity; founder brief cites £93.2m → £80.5m).
- THG FY25 RNS: full-year Nutrition revenue.
- Any channel split (gym / convenience / online) for protein bars.

---

## 4. Top 5 sources in this batch

1. **Asian Trader (2025) 'Protein' feature citing Circana.** *Asian Trader*, p.32. https://digitaledition.asiantrader.biz/flip-book/288011/2133365/page/32 (accessed 20 Oct 2026).
   *£225m, +24.2% YoY for grocery protein bars, drinks and powders; bars are the fastest-growing snack-bar segment. This is the headline category-momentum number for the pitch.*
2. **CB Insights (2026) *Grenade*, citing The Grocer Top Products 2025.** https://www.cbinsights.com/investor/grenade (accessed 20 Oct 2026).
   *Market leader Grenade's unit sales fell 15.9% in 2025 while rivals grew. Evidence the incumbent is vulnerable; find the primary Grocer table before quoting.*
3. **Protein Production Technology (2026) 'High-protein snacks under scrutiny as UK study finds most exceed NHS sugar guidelines'.** https://proteinproductiontechnology.com/post/high-protein-snacks-under-scrutiny-as-uk-study-finds-most-exceed-nhs-sugar-guidelines (accessed 20 Oct 2026).
   *~90% of 88 UK high-protein snacks exceed NHS free-sugar guidance. Independent (though PR-driven) support for the low-sugar gap.*
4. **Just Food (2026) 'Danone buys meal-replacement firm Huel'.** https://www.just-food.com/news/danone-buys-meal-replacement-firm-huel/ (accessed 20 Oct 2026).
   *A ~€1bn (reported) acquisition in March 2026. Shows global food groups are still paying premiums for UK protein and nutrition brands: a strong "why now" and scale signal.*
5. **Retail Times (2024) 'Barebells launches into nearly 1,000 Tesco stores nationwide with an exclusive new bar'.** https://retailtimes.co.uk/barebells-launches-into-nearly-1000-tesco-stores-nationwide-with-an-exclusive-new-bar/ (accessed 20 Oct 2026).
   *Brand says it is in ~3,500 UK gyms. Proves gyms are an established protein-bar channel, and shows who Ewan's gym-counter competition is.*
