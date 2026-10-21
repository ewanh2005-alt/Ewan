# Landing page: setup, hosting and tracking

**Status:** draft for Ewan's approval. Nothing is live, and no form, pixel or ad account is connected.
**Files:** `index.html` (the page, ~16 KB, no frameworks) · `analyse_signups.py` (sign-up summary, standard-library Python).

## 1. Before publishing (checklist)

- [ ] Replace `[CONTACT EMAIL]` in the privacy notice with an address you check.
- [ ] Connect a form (step 2). Until you do, the page runs in **demo mode** and sends nothing.
- [ ] Leave `ANALYTICS_ENABLED = false` unless you have decided to run Meta ads (step 5).
- [ ] Read the page once more against the claims rules: **no nutrition numbers, no "low sugar", no "high protein", no "recovery/fuel/repair/boost"** until the product is lab-tested and the wording is checked.
- [ ] Ask your DVS mentor whether Durham's student-research ethics or data rules apply to collecting sign-ups.

## 2. Connect a form

**Option A: your existing Google Form (free)**
1. Add questions to the form that match the page: Email, First name, Which fits you best?, What do you usually eat after training now?, Biggest food struggle in camp?, Pre-order 5-pack at £10?, the 4 price questions, and short-answer fields for utm_source, utm_medium, utm_campaign, utm_content, landing_variant and consent.
2. In Google Forms, open ⋮ → **Get pre-filled link**, type a dummy answer in every field, then **Get link**. The link contains `entry.123456789=...` for each question.
3. Paste each `entry.` number into `GOOGLE_ENTRY_IDS` in `index.html`, matched to the field.
4. Set `FORM_ENDPOINT` to the form's `.../viewform` URL. The page converts it to `.../formResponse`.
5. **Test it:** submit once from the live page and check the response appears in the form's Responses tab. (Google gives the page no confirmation, so this check matters.)
6. Make the email and choice questions **not required** in Google Forms, so a partly filled answer still saves.

**Option B: Formspree or Tally (free tiers).** Create a form, copy its endpoint URL into `FORM_ENDPOINT`. Field names are sent as they appear in the page. Never paste API keys into the page; these endpoints don't need one.

## 3. Free hosting

**GitHub Pages**
1. In this repository on GitHub, go to **Settings → Pages**.
2. Source: **Deploy from a branch**; choose the branch and the `/ (root)` folder, then Save.
3. The page will be at `https://<username>.github.io/<repo>/landing-page/`.
4. Note: a public repository makes the code public (not the sign-ups, which live in the form).

**Netlify (drag and drop)**
1. Sign in at app.netlify.com → **Add new site → Deploy manually**.
2. Drag the `landing-page` folder onto the page. You get a URL like `https://<name>.netlify.app`, which you can rename in Site settings.

## 4. UTM links, one per channel

Replace `BASE` with your hosted URL. Keep sources lower-case so the script groups them correctly.

| Channel | Link |
|---|---|
| YouTube video description | `BASE?utm_source=youtube&utm_medium=video&utm_campaign=first_batch` |
| YouTube Community post | `BASE?utm_source=youtube&utm_medium=community&utm_campaign=first_batch` |
| Gym poster QR code | `BASE?utm_source=poster&utm_medium=qr&utm_campaign=first_batch` |
| Instagram bio / story | `BASE?utm_source=instagram&utm_medium=social&utm_campaign=first_batch` |
| Fighter WhatsApp groups | `BASE?utm_source=whatsapp&utm_medium=message&utm_campaign=first_batch` |
| Meta ad, concept 1 (founder video) | `BASE?utm_source=meta&utm_medium=paid&utm_campaign=first_batch&utm_content=founder_video` |
| Meta ad, concept 2 (question) | `BASE?utm_source=meta&utm_medium=paid&utm_campaign=first_batch&utm_content=question` |
| Meta ad, concept 3 (gap) | `BASE?utm_source=meta&utm_medium=paid&utm_campaign=first_batch&utm_content=gap` |

For a headline A/B test, publish a second copy of the page with `LANDING_VARIANT = "B"` and a different `<h1>`, and split traffic between the two URLs.

## 5. Meta Pixel (only if Ewan approves ad spend)

1. Create a pixel in Meta Events Manager and paste its ID into `META_PIXEL_ID`.
2. Set `ANALYTICS_ENABLED = true`. A cookie banner then appears, and the pixel loads **only after "Accept"**.
3. The page sends a `Lead` event on a successful sign-up.

## 6. Analyse sign-ups

Export responses as CSV (Google Forms: Responses → Sheets → File → Download → CSV), then:

```bash
python3 analyse_signups.py signups.csv --visits youtube=420 poster=60 meta=900
```

`--visits` takes page visits per source from Netlify/GitHub stats or Meta Ads Manager (landing-page views), so the script can print visit → sign-up conversion. It also prints the compete/train/watch split, pre-order intent (all and trainers only), themes in current snacks and camp struggles, and a Van Westendorp price summary. Read the raw free-text answers too: keyword themes are a rough first pass.
