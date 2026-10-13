# ⚠️ FICTIONAL SAMPLE DATA: Graft Accelerator teaching programme

> **Everything in this folder is invented by a script** (`generate_fictional_interviews.py`, fixed random seed).
> No real people were interviewed. Every name ends "(fictional)". Every quote and number is made up.
> **Do not use any of it as evidence** in the Durham Venture School pitch, the persona, the deck, `research/sources.md`, or anywhere it could be read as real customer research.

**What it's for:** a worked example for a fictional "Graft Accelerator" programme. It shows learners what 50 interviews and a survey look like once collected, and how they're analysed.

## Files
| File | What |
|---|---|
| `FICTIONAL_interviews.csv` | 50 fictional interviewees: 20 squad athletes, 10 MMA/combat, 15 gym-goers, 5 coaches (same columns as `research/17_interview_template.csv`) |
| `FICTIONAL_interview_transcripts.md` | Short Q&A transcript for each of the 50 |
| `FICTIONAL_survey_export.csv` | Google-Forms-style export (45 non-coach rows) |
| `FICTIONAL_results.json`, `FICTIONAL_price_chart.svg` | Output of the real analysis script run on the fictional data |

## Worked analysis (FICTIONAL numbers, for teaching only)
From `research/17_analyse_responses.py`:
- **Missing a meal after training:** 91% "sometimes" or "often".
- **Appeal:** 3.4/5 on average; 51% rate it 4–5.
- **Taste-test sign-ups:** 62% left an email.
- **Price:** £2.00 was the most picked option (27%); 24% "wouldn't buy".
- **Top put-offs:** price (20%), chalky texture (18%), sweetener aftertaste (18%).
- **By group (interviews), mean reaction:** squad 3.8, MMA 3.8, coaches 3.2, gym-goers 2.7.
  - *Teaching point:* the sharpest-need group (coached athletes) reacts better than general gym-goers, which is the kind of pattern you'd look for in real data.

## How learners should use it
1. Practise reading the CSV and running the analysis script.
2. Practise turning results into a persona and a slide.
3. Then collect **real** data with `17-research-sprint.md` and replace all of this.

To regenerate: `python3 graft-accelerator-FICTIONAL/generate_fictional_interviews.py`
