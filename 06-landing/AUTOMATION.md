# 06 — Wiring up the forms and automated emails

**Nothing is connected yet.** Both forms point at placeholder URLs (`YOUR_WAITLIST_FORM_ID`, `YOUR_PARTNER_FORM_ID`). While those placeholders are in place, the page shows "Demo mode" and sends nothing. Below are two free-tier ways to wire it up, then the copy for all three emails.

Before going live you need:
1. A sending email address on your own domain (e.g. hello@yourdomain), or at least a dedicated Gmail.
2. A privacy notice filled in (`#privacy` section placeholder).
3. To check whether you must pay the ICO data protection fee (usually £52/yr for small organisations; check ico.org.uk). `[ASSUMPTION: verify the current fee]`

---

## Recommended route: Brevo (free tier) + Cal.com (free)

Why: Brevo gives a mailing list, double opt-in and automated emails on its free plan; Cal.com handles booking, confirmation and reminder emails with no code. Free-tier limits change, so check them when you sign up.

### 1. Waitlist → Brevo
1. Create a free Brevo account. Create a **list** called "Waitlist".
2. Contacts → Settings: add attributes `SPORT`, `FREQUENCY`, `FLAVOURS`, `PRICE`, `CURRENT_HABIT`.
3. Forms → **Subscription form** → turn on **double opt-in** (best practice under UK GDPR/PECR; proves consent). Map the fields.
4. Brevo gives you a form action URL. In `index.html`, replace `https://formspree.io/f/YOUR_WAITLIST_FORM_ID` with it, and rename the inputs to Brevo's expected names (`EMAIL`, `SPORT`, …). *Simpler alternative:* embed Brevo's own form HTML in place of ours and copy our styling onto it.
5. Automations → "Welcome message" → trigger: *contact added to list Waitlist* → send **Email 1** below.

### 2. Partner chats → Cal.com
1. Create a free Cal.com account. Event type: **"Pilot chat: 20 min"** (video or phone), with your available hours and a 15-min buffer.
2. Booking questions: name, email, organisation, "You are a…" (same options as the form), message.
3. Workflows: **on booking** send **Email 2**; **24 h before** send **Email 3** (Cal.com sends its own confirmation; replace its text with ours).
4. Embed → Inline → copy the snippet and paste it inside `<div id="scheduler">` in `index.html`, replacing the placeholder text.
5. Keep **Option B** (the request form) for people who prefer not to pick a slot. Point it at Formspree (below) or Brevo.

### Option: Formspree (free) for both forms, with no mailing list
1. Create two forms on Formspree; each gives a URL like `https://formspree.io/f/abcd1234`.
2. Paste them into the two `action="…"` attributes. Our JavaScript already posts with `Accept: application/json` and handles success and error.
3. Turn on the **autoresponse** for each form and paste in Email 1 or Email 2. (Check the current free plan: autoresponses may need a paid tier.)
4. Spam: the hidden `_gotcha` field is Formspree's honeypot; it's already in both forms.

### Option: Google Forms + Apps Script (free, more fiddly)
Use only if you want everything in Google Sheets. Build the form in Google Forms; in the linked Sheet, Extensions → Apps Script; add an `onFormSubmit` trigger that calls `MailApp.sendEmail(email, subject, body)` with the copy below. Gmail's daily sending limits apply. Link to the Google Form instead of using our HTML form.

### Analytics
The page has a commented-out **Plausible** snippet in `<head>` (cookieless, so no cookie banner needed; paid after the trial). Free alternative: Cloudflare Web Analytics (also cookieless). Track: page views, `waitlist-submit`, `partner-submit`, booking completions (from Cal.com). **Don't** add Google Analytics without a consent banner.

### What to measure (feeds `07-mvp-pilot-plan.md`)
- Visitors → waitlist sign-up rate (target ≥10% of visitors from targeted club/WhatsApp posts) `[ASSUMPTION]`
- Double opt-in confirmation rate
- Price question distribution (share choosing ≥£2.50)
- Partner chats booked

---

## Email copy

### Email 1: Waitlist confirmation
**Subject:** You're on the fettle list
**Preview text:** First batch, taste tests, and a say in the flavours.

> Hi there,
>
> Thanks for joining the fettle waitlist. *(If double opt-in: "Please confirm your email with the button below. Then you're in.")*
>
> fettle is a fresh-baked bar for after training: about 2 g sugar, 17 g protein and 23 g carbs, made from eggs, oats, quark, oat bran, seeds and milk. No powders, no sweeteners. We're baking the first small batches in Durham this term.
>
> **What happens next**
> - We'll email you when taste tests and the first batch are ready (no more than twice a month).
> - Waitlist members get first access, and a vote on which flavours we make.
>
> **One quick question:** what do you usually eat in the two hours after training? Just hit reply. I read every answer.
>
> Thanks,
> Ewan
> Founder, fettle
>
> *Contains peanuts, milk, egg and oats. You're getting this because you signed up at [domain]. [Unsubscribe] · [Privacy notice] · [Business name, address]*

### Email 2: Meeting booking confirmation
**Subject:** Confirmed: fettle pilot chat, {{date}} at {{time}}
**Preview text:** 20 minutes on a taste test or pilot for {{organisation}}.

> Hi {{first_name}},
>
> Thanks for booking a chat. You're confirmed for **{{date}} at {{time}}** ({{video link / phone number}}).
>
> **What I'd like to cover (20 min):**
> 1. What your members or athletes eat after training now
> 2. Whether a small, free taste test or a short paid pilot would fit your schedule this term
> 3. What you'd need from us (allergen info, pricing, display, invoices)
>
> If anything's useful to share beforehand, e.g. roughly how many members train in a typical week, just reply.
>
> Need to change the time? [Reschedule] · [Cancel]
>
> Thanks,
> Ewan
> fettle · [phone placeholder]

### Email 3: Reminder (24 hours before)
**Subject:** Tomorrow: fettle chat at {{time}}
**Preview text:** Quick reminder, plus the link.

> Hi {{first_name}},
>
> A quick reminder that we're speaking **tomorrow, {{date}} at {{time}}**.
> Join here: {{video link}} *(or I'll call you on {{phone}})*
>
> If you've got a spare 2 minutes beforehand, I'd love to know: **what's the most common thing your members eat straight after training?**
>
> Can't make it? [Reschedule] (no problem at all).
>
> See you tomorrow,
> Ewan

---

## Compliance checklist before going live
- [ ] Privacy notice written and linked (who you are, what you collect, why, how long, rights, ICO complaint route)
- [ ] Consent box unticked by default (it is) and stored with each sign-up (Brevo stores the timestamp)
- [ ] Unsubscribe link in every marketing email (Brevo adds this automatically)
- [ ] Only claims from `04-concept-bar.md` §3d on the page and in emails
- [ ] Replace every `[placeholder]` and `example.co.uk`
- [ ] Test each form end to end with your own email before sharing the link
