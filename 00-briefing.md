# 00 — Briefing

**Date:** 7 Oct 2026 · **Phase:** 0 (set-up) · **Status:** ⛔ blocked on inputs. See §4.

---

## 1. What you've given me

| Expected input | What I found | Status |
|---|---|---|
| `inputs/judging-criteria.*` | Not in the repo. You shared **two photos** in chat: the DVS *Judging Criteria* sheet and the *Pitching your idea* sheet. I transcribed both word for word into `inputs/judging-criteria.md`. | ✅ Usable. **No weightings** on the sheet |
| `inputs/competitor-analysis.*` | Not in `inputs/`. The repo root has three earlier documents (6 Oct 2026): `stage-1-competitor-research.md`, `stage-2-differentiation.md`, `findings-report.md`. They hold a substantial competitor analysis, but I can't tell whether they are **your notes** or earlier AI-generated drafts. | ⚠️ Need you to confirm (Q1) |
| `inputs/customer-persona.*` | **Nothing.** No persona draft and no interview notes anywhere in the repo. The earlier documents say **9 interviews done** and **1 survey response**, but the notes were never shared. | ❌ **Missing. Blocks Phase 3**, and weakens Phases 1, 4, 5 and 7 |

I read all three existing documents in full. They are summarised in §2 so you can see what I'd be building on.

## 2. What the existing documents already establish

Their tags (**[V]** verified / **[C]** company claim / **[A]** assumption) will be converted to `[EVIDENCE]` / `[ASSUMPTION]` / `[GAP]`.

| Area | Position in existing docs | Tag today |
|---|---|---|
| Primary competitor | **Veloforte Forza** (whole-food, egg white, 12 g P / 38 g C / 7.4 g fibre). Styrkr BAR+ is "category proof" but isolate- and syrup-based (15 g P, 28 g sugar, 0.7 g fibre) | Retailer listings, 6 Oct |
| White space | No UK bar with ~20 g protein **and** ≥40 g carbs from whole-food protein with high fibre | Medium (search-based) |
| Real competition | Chocolate milk, banana, or nothing | Assumption |
| Protein route | **Decided:** "Tier 3" = oats/nuts/dates + **skimmed milk powder + dried egg white**. Not vegan. No 70 g size limit | Founder decision |
| Draft spec | ~98 g bar, ~20 g P, ~42 g C, ~11 g fibre (~2 g oat beta-glucan), ~345 kcal | Recipe maths, unchecked |
| Hero feature | **Dose-to-bodyweight snap bar**: 4 segments of ~5 g protein, plus a weight chart and a refuel QR | Untested with customers |
| Go-to-market | Club "Squad Box" for university and grassroots squads; batch-lab-tested label as trust layer | Assumption |
| Budget | £1,000 per term (~£1k total) | Founder input |
| Programme | Week 5 of 13 on 6 Oct; 5-minute pitch every Friday | Founder input |
| Claims work | Carb-recovery claim (Reg. 2015/7) wording; "high protein" and "high fibre" thresholds checked; never say "speeds recovery", "reduces soreness" etc. | Partly confirmed |

**Reusable:** most of Phase 2 (profiles, ecosystem questions, Step 3–5 analysis) and the start of Phase 4. I'll re-verify, add the missing competitors (Nākd, RXBAR, Graze, Misfits, Fulfil detail, Myprotein bars, etc.), and produce the CSV, positioning map and code-calculated nutrition that don't exist yet.

## 3. Contradictions (please rule on each before I build on either side)

| # | This prompt says | Existing documents say | Why it matters | My suggestion |
|---|---|---|---|---|
| C1 | **Week 2–4**, customer-discovery stage | **Week 5 of 13** on 6 Oct, 9 interviews done | Phase 7's plan is set for Weeks 4–13 | Plan **Weeks 6–13** (8 weeks), not 10 |
| C2 | Audience: **active UK 18–34s**, athletes **and everyday gym-goers** | Club athletes: **endurance + team sport**, university and grassroots squads. Gym-goers barely mentioned | Changes the persona, channel (gym vs club), flavour and brand voice | Can't choose without the interview notes. Tell me who your 9 interviewees were |
| C3 | **All-natural, whole-food** ingredients, with whole food vs high protein as an **open** question | Already **decided**: milk powder + dried egg white | Changes how Phase 4 is framed and what "whole food" can say on pack | Treat Tier 3 as the working choice, but still show you the strict whole-food option, as asked |
| C4 | Calorie/portion is an **open tension** ("past 300 kcal") | Draft spec is **~98 g / ~345 kcal**, and "no 70 g limit" is decided | A 98 g, 345 kcal bar is big for a gym-goer snack, less so for a rugby forward | Re-test in Phase 4. Likely offer the snap-segment portion as the answer |
| C5 | No hero feature named; differentiation = protein + carbs + real food + minimal brand | Hero = **dose-to-bodyweight snap bar** + Squad Box | The brand, packaging and landing page all hang off the hero | Keep the snap bar **as a candidate**, untested. Confirm you still want it |
| C6 | — | Stage 2 calls fibre "a quality feature, **not the hero**, 5–6 g". The later findings report makes **~11 g fibre a headline** | Internal contradiction. Also matters for gut comfort straight after exercise | Assume the later version (~11 g) supersedes, then re-test against the evidence in Phase 4 |
| C7 | — | Budget is "**£1k per term**" in the findings report, but "**~£2k**" in Stage 2's risk list | Pilot plan and costings | Use **£1,000 total** unless you say otherwise |
| C8 | Final pitch is in **Week 13** | Also a **5-minute pitch every Friday** | Phase 7 outline should probably have a 5-minute version | I'll build the Week 13 outline with a 5-minute cut |
| C9 | Phase 4 says "if Phase 4's tension analysis calls for it" | — | Typo: I read it as the tension analysis in section 4 of your prompt | No action needed |

**Not a contradiction, just a note:** your brief asks for a "clean, minimal **brand**" and also says don't use the word "clean" in claims. I read that as: minimal **visual** style is fine; the **word** "clean" stays off pack and page.

## 4. What I need from you (blocking)

1. **Q1. Competitor notes.** Are `stage-1-competitor-research.md`, `stage-2-differentiation.md` and `findings-report.md` your competitor notes (i.e. should I treat them as `inputs/competitor-analysis`)? If you have other notes (a spreadsheet, Word doc, photos), add them to `inputs/`.
2. **Q2. Persona and interview notes (blocking).** Add whatever you have to `inputs/customer-persona.*`. Rough is fine: bullet notes per interview, a photo of a notebook, survey export. For each interviewee, ideally note: age band, sport/training type, how often they train, what they eat after training, and anything they said about price, taste or gut. **I will not invent any of this.** Without it, Phase 3 is just a list of `[GAP]`s.
3. **Q3. Rule on C1–C8 above.** One-word answers are fine (e.g. "C2: gym-goers primary").

## 5. Plan once unblocked

| Phase | What I'll do | Depends on |
|---|---|---|
| 1 | Judging map from the transcribed criteria (no weightings, so I'll treat them as equal and say so), mapped to the "Pitching your idea" questions | Can start now; scoring improves with Q2 |
| 2 | Re-verify existing competitors; add missing ones; build CSV with price per g protein; positioning map; ecosystem interview guide | Q1 |
| 3 | Persona from your evidence only | **Q2** |
| 4 | Spec, 2–3 recipes, `04-nutrition.py` (CoFID/USDA values), GB claims check, costing in code | C3, C4, C6 |
| 5 | Names (not "CRISP"), trade mark/company/domain checks I can do read-only, identity, SVG logos, packaging | Phase 4 numbers |
| 6 | Landing page with waitlist, interest and booking flow (placeholders only, no real services) | Phases 4–5 |
| 7 | Pilot plan for the weeks left, assumption tracker, pitch outline | C1, C7, C8 |
| 8 | Re-run scripts, source and claims audit, final summary | All |

**Limits to expect:**
- Earlier work found brand websites and the UK IPO site blocked from this environment. If that's still true, trade mark and Companies House checks will be marked "couldn't verify", with the exact searches for you to run.
- I won't sign up to anything, buy domains, or connect real keys.

## 6. What I'll do if you only answer some questions

If you answer **Q1 + Q3** but don't have notes yet, I'll go ahead with Phases 1, 2 and 4. Phase 3 will become a persona *skeleton* full of `[GAP]`s plus the interview questions to fill it. Branding and the landing page will be voiced for the provisional audience and marked as such.
