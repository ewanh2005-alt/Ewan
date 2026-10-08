# 02c — Reddit insights: what people actually buy, and why

**Date:** 8 Oct 2026 · **Data:** comments Ewan collected from three Reddit threads (r/proteinsnack). Ads and empty or deleted comments were removed and usernames anonymised (R01–R16). Coding: `research/09_reddit_coding.csv`. Counts: `research/09_reddit_counts.py`.
**Tags:** `[EVIDENCE: Reddit Rxx]` · `[ASSUMPTION]` · `[GAP]`

> **Health warning:** this is **online secondary evidence, not interviews**, and it is kept separate from the persona counts.
> - It's a **small, self-selected group**: people in a protein-snack forum, who already like processed bars.
> - It's **mostly American**: 5 of 13 named a US shop or price, and none said UK.
> - Response rates were low:
>   - Ewan's post-training post: 1.1K views, **1 reply**
>   - fibre post: 1.9K views, **2 readable replies**
>
> Use it for direction and quotes, never as market size or proof of demand.

## What was collected

| Thread | Question | Replies coded |
|---|---|---|
| T1 | "What was the last protein bar you bought, and would you buy it again?" | 13 |
| T2 | Ewan's post: "What do you eat after training when a meal isn't convenient? Would a recovery bar fit?" | 1 (the survey link responses are separate, `[GAP]`: not shared yet) |
| T3 | "Do you buy fibre bars or snacks, or is fibre something you rarely check?" | 2 |

**Brands named in T1:**
- Barebells 4
- Quest 2 (plus a third who says they "love Quest Overloads")
- Atlas, Built Puff, Grenade, YMMY, Met-Rx, Muscle Nation, Elevation (Aldi) 1 each

## Themes

### 1. Taste drives repeat purchase, and the winning flavours are desserts
- **6/13 bought again or would.** Every reason given was taste: "best tasting bar I've tried… bought a 12-pack the day after" `[EVIDENCE: R05]`; "would buy again and did" `[R01]`.
- **9/13 named a dessert flavour:** birthday cake, brownie batter, caramel cookies, Oreo, cookies & cream, pistachio cheesecake, cookie dough, banana bread `[EVIDENCE: R02–R13]`.
- **Texture decides the rejects:** Built Puff "like gum", so they won't buy it again `[R07]`. Liked textures were "soft" `[R09]`, "great texture" `[R04]`, and "not a granola base" as a nice change `[R13]`.
- **Same as the interviews:** taste was the top worry there too (3/10 + the S&C coach).

### 2. Nobody bought a bar for training recovery
- **0/13** said they ate their last bar around training. The reasons given were:
  - an afternoon snack `[R09]`
  - to "hit protein for the day" `[R06]`
  - **instead of a chocolate bar** `[R06]`
  - managing blood sugar as a diabetic `[R13]`
- **The only reply to Ewan's post-training question was a clear "no":** *"I can easily wait 2–4 hours. The 'post-workout window' is so overblown."* They eat a normal meal 2–3 h after training `[EVIDENCE: R14]`.
- **The research partly agrees.** A meta-analysis found **total daily protein matters more than timing** for muscle gain `[EVIDENCE: S28, Schoenfeld et al. 2013]`. That paper is debated, because most of the studies didn't match total protein between groups. Timing matters more for **carbs when the next session is within ~6–8 h** `[EVIDENCE: S23]`.

### 3. People feel bars are a compromise; they'd rather eat whole food
- *"Ideally I'd eat more 'whole' foods than protein bars… I see them almost as a necessary evil"* `[EVIDENCE: R06]`.
- **Same as the interviews:** C1, C2, C4, C7 and the S&C coach all lean towards whole foods.

### 4. Fibre: from food, not "fibre snacks"
- One person tracks **30+ g fibre a day from whole foods** and avoids fibre snacks because they *"upset my stomach"* `[EVIDENCE: R15]`. That fits the research: isolated fibres like chicory root can cause gut trouble, and food fibre is preferred `[EVIDENCE: 01d]`.
- **Their breakfast is overnight oats + chia + Greek yoghurt + berries** `[R15]`. That's essentially **what fettle's bar is made of.**
- Another deliberately buys products **high in both protein and fibre** `[EVIDENCE: R16]`.

### 5. Price and offers matter; a premium bar is a "treat"
- **Prices paid (USA):** $1.50 on buy-one-get-one-free `[R04]`, $2.48 `[R06]`, $3.50 `[R09]`, $4.99 for 4 `[R10]`.
- **Offers drive repeat buying:** one person didn't rebuy *only* because the buy-one-get-one-free offer ended `[R04]`.
- **Premium bars become occasional treats:** *"the price makes it a splurging treat"* `[R13]`.
- **UK prices weren't covered here** `[GAP]`.

### 6. Not everyone wants carbs
- A diabetic buyer wants **≤22–23 g carbs and ≥10 g protein** `[EVIDENCE: R13]`.
- The R-series recovery bars (~38–40 g carbs, `04d`) are **not for that buyer**, and that's fine: they're built for athletes refuelling.

## What this changes for fettle

| Finding | What to do |
|---|---|
| **Taste and dessert flavours win repeat buys** | Name flavours like treats people already love. **R3 renamed "Banana Bread" (done 8 Oct)** (Barebells Banana Bread was rebought, R06). Keep **Chocolate Peanut Butter**. Test "Vanilla" vs "Vanilla Cookie Dough" naming. **Use Barebells as the taste benchmark** in the blind test: it's the most-praised bar here and sold in Tesco (`02-competitors.csv`) |
| **Nobody buys bars for recovery; "the window is overblown"** | **Don't sell on urgency** ("eat within 30 minutes or lose your gains"). Sell on: **"a proper recovery meal when you can't get one"**, which is Ewan's own framing and C7/C10's problem. Keep "match days and two-a-days" for the carb message, where timing does matter. **Test whether gym-goers (Jack) feel a need at all** `[ASSUMPTION at risk]` |
| **Bars feel like a "necessary evil"** | This is the **opening**: "the bar you don't have to feel bad about: eggs, quark, oats and nothing else." It backs up the differentiation in `01b` |
| **Fibre from food, not fibre snacks** | Say "fibre from oats and chia". Pitch line to test: **"Overnight oats you can carry."** |
| **Price: offers and multi-packs; premium = treat** | At £2–2.75 fettle is premium. Plan **bundles** (squad boxes, 10-packs) and a first-order offer. Get **UK** price evidence `[GAP]` |
| **Some people want low carbs** | Keep the target clear: **athletes refuelling**, not general snackers or low-carb dieters |

## Effect on the persona and the assumptions
- **Persona (`03-persona.md`):** no change to the interview-based counts. This **adds weight** to the "coached athlete" sub-group: their need (training twice a day, no time to cook) is real, while a casual gym-goer can often just wait for a meal `[R14]`.
- **Assumption tracker:**
  - A1 (people want this bar) is still only partly supported.
  - **New A16:** *"Athletes see a bar as a solution when a meal isn't possible after training"*. Reddit is against it (1/1), the interviews lean for it (C7, C10). Test it.
- **For the next round of interviews:** ask *"What did you eat after your last session, and how long after?"* and *"What's the last bar you bought, and did you buy it again?"*. That's the same question as T1, so you can compare UK athletes with Reddit.

## Gaps
- Responses to the Google Form survey linked in T2 `[GAP]`: share them and I'll code them the same way.
- UK-specific Reddit replies, e.g. post in r/UKfitness or a Durham University sports page `[GAP]`.
- Ages and training levels of the people who replied `[GAP]`.
