# 17: Research sprint: 50 real responses in 5 days

**Date:** 13 Oct 2026 · **Goal:** 50 real people from the persona and early-adopter groups. Aim for **40 survey responses and 10 short interviews**.
**Analysis:** `research/17_analyse_responses.py` turns a Google Forms CSV export, plus your interview notes, into counts, charts and quotes.

> **Why these must be real:** the judges score "meaningful customer discovery". Invented interviews would be fabricated evidence, against the programme's rules and your own project rules. If a judge asks a follow-up question about a named interviewee, the pitch collapses. Fifty real, short responses beat fifty fake long ones.

---

## Who to ask (target mix)
| Group | Target | Where |
|---|---|---|
| Coached Durham squad athletes | 20 | S&C coach's squad group chats; Team Durham club captains |
| MMA / combat-sports club members | 10 | Your club's WhatsApp group; after class |
| Regular gym-goers (the persona) | 15 | Gym poster QR code; gym Instagram story; friends |
| Coaches / S&C staff | 3–5 | Email or in person (use the coach interview questions below) |

---

## Day by day
| Day | Do | Output |
|---|---|---|
| 1 | Update the Google Form with the 10 questions below. Ask the S&C coach and the MMA coach to forward the message below | Form live |
| 2 | Post in 3 group chats; put up the gym poster (QR code → form). DM 15 friends who train | ~20 responses |
| 3 | 5 quick interviews (10 min each, in person or by phone) after training. Use the script below | 5 notes |
| 4 | Chase up: "Last call, 2 minutes, really helps." Ask each person to forward it to one teammate | ~40 responses |
| 5 | 5 more interviews. Export the form to CSV and send it to me for analysis | 50 total |

**Incentive (optional, cheap):** "Everyone who fills it in can try the first batch free." This also builds your taste-test list.

---

## Message to send (group chats, coaches)
> Hi all, I'm Ewan, a Durham graduate working on a real-food protein snack for people who train (egg, quark and oats, no powders or sweeteners). Could you spare 2 minutes for this survey? It really helps my Durham Venture School project, and everyone who fills it in can try the first batch free 👉 [form link]. Thanks!

---

## Survey (Google Form, 10 questions, about 2 minutes)
1. **How often do you train?** 1–2 / 3–4 / 5–6 / 7+ sessions a week
2. **What do you mainly do?** (tick all) Gym weights / team sport / combat sports / running or cycling / classes / other
3. **Are you coached** (club, squad or PT)? Yes / No
4. **After training, what do you usually eat within 2 hours?** (tick all) Proper meal / protein shake / protein bar / fruit / nothing until later / other
5. **How often can't you eat a proper meal within 2 hours of training?** Never / sometimes / often / almost always
6. **In the last month, how many protein bars did you eat?** 0 / 1–3 / 4–10 / 10+
7. **What puts you off protein bars?** (tick all) Taste or aftertaste / sweeteners / stomach issues / too processed / price / too sugary / nothing / other
8. **How appealing is a fresh, real-food protein snack** (egg, quark, oats, ~15 g protein, no sweeteners; kept in the fridge)? 1–5
9. **What would you pay for one?** £1.50 / £2.00 / £2.50 / £3.00 / wouldn't buy
10. **Want to taste-test the first batch? Leave your email** (optional), with a consent line: "We'll only use this to contact you about Graft taste tests. You can ask us to delete it any time."

Add **one optional open question**: "Anything else about what you eat after training?" This is where your quotes come from.

---

## 10-minute interview script (athletes and gym-goers)
Ask about real past behaviour, not opinions about your idea. Don't mention the product until question 7.
1. Talk me through your last training day: what did you do, and what did you eat after?
2. When did you last *not* manage a proper meal after training? What happened, and what did you eat instead?
3. How often does that happen in a normal week?
4. Have you bought a protein bar or shake in the last month? Which one, and why that one?
5. What annoys you about them, if anything?
6. Has a coach told you what to eat? What did they say?
7. *(Show the card: egg, quark, oats; ~15 g protein; no sweeteners; fridge.)* What's your honest first reaction?
8. What would stop you buying it?
9. What would you pay?
10. Can I contact you for a free taste test? *(Their commitment, or not, is the most important data.)*

**Write up within 24 hours** using `research/17_interview_template.csv` (one row per person). Write **their words** in the quote column, and mark paraphrases as paraphrases.

## Coach questions (3–5 coaches)
1. What do you tell your athletes to eat after training?
2. What do they actually eat?
3. Have you ever supplied snacks or bars to a squad? What happened?
4. Would you trial a fresh real-food snack with your squad? What would you need to see first?

---

## What to send me
- The Google Forms CSV export.
- The filled-in interview template.

I'll run the analysis script and give you:
- counts and %
- a price chart
- a pain-point ranking
- the top quotes
- an updated persona and slide

**Before any data comes in, this file and the script contain zero responses.**
