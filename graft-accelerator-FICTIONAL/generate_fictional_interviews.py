"""FICTIONAL SAMPLE DATA GENERATOR, for the (fictional) Graft Accelerator teaching programme.
Every person, answer and quote produced here is INVENTED by a script. None of it is real customer research.
Do not use any of it as evidence in a real pitch (e.g. Durham Venture School), persona, or slide.

Run: python3 graft-accelerator-FICTIONAL/generate_fictional_interviews.py
Outputs (all prefixed FICTIONAL_): interviews CSV, transcripts MD, survey CSV (Google-Forms-style)."""
import csv, random
from pathlib import Path

random.seed(2026)  # reproducible
HERE = Path(__file__).parent
BANNER = "FICTIONAL SAMPLE DATA: invented for the Graft Accelerator teaching programme. Not real people. Not evidence."

FIRST = ["Alfie", "Priya", "Callum", "Jade", "Tom", "Niamh", "Oscar", "Leah", "Sam", "Imogen", "Ryan", "Amira", "Josh",
         "Hannah", "Kieran", "Sophie", "Dan", "Maya", "Ben", "Ellie", "Luca", "Grace", "Harvey", "Zara", "Joe", "Chloe",
         "Adam", "Freya", "Liam", "Ruby", "Matt", "Isla", "Nathan", "Erin", "Charlie", "Megan", "Jack", "Aisha", "Will",
         "Holly", "Ethan", "Lucy", "Owen", "Katie", "Rob", "Nadia", "Finn", "Beth", "Max", "Tara"]

GROUPS = [("squad athlete", 20), ("MMA / combat", 10), ("gym-goer", 15), ("coach", 5)]
SPORTS = {"squad athlete": ["rugby", "football", "rowing", "hockey", "netball", "athletics"],
          "MMA / combat": ["MMA", "boxing", "BJJ", "Muay Thai"],
          "gym-goer": ["weights", "weights + running", "weights + padel", "classes + weights"],
          "coach": ["S&C coach", "rugby coach", "MMA coach", "football coach", "PT"]}
POST_FOOD = ["a proper meal at home", "a protein shake", "a protein bar", "a banana", "nothing until dinner",
             "a meal deal", "chicken and rice from a tub", "toast and peanut butter"]
BRANDS = ["Barebells", "Grenade", "Fulfil", "Trek", "Myprotein", "none", "none", "Nakd"]
ANNOY = ["the aftertaste from sweeteners", "they upset my stomach", "they're expensive", "they feel processed",
         "they're full of sugar", "they all taste the same", "nothing really", "the chalky texture"]
COACH_ADVICE = ["eat whole food where you can", "get protein in within a couple of hours", "nothing specific",
                "more carbs on double days", "avoid too many bars", "eat a proper meal after training"]
BARRIERS = ["has to taste good", "price", "keeping it in the fridge", "would need to try it first", "convenience",
            "not sure it'd fill me up", "allergens (egg/dairy)"]
REACT = {5: ["That's exactly what I'd want.", "Honestly I'd buy that every week."],
         4: ["Sounds good, depends on taste.", "I like that it's real food."],
         3: ["Maybe. I'd need to try it.", "Not sure about the fridge bit."],
         2: ["I'd probably just eat a meal.", "Bit pricey for what it is."],
         1: ["Not for me, I just wait for dinner.", "I don't really snack after training."]}

def person(i, group):
    sess = {"squad athlete": random.choice([5, 6, 7, 8, 9]), "MMA / combat": random.choice([3, 4, 5, 6]),
            "gym-goer": random.choice([3, 4, 5]), "coach": None}[group]
    reaction = random.choices([5, 4, 3, 2, 1], weights={"squad athlete": [3, 4, 2, 1, 0.5], "MMA / combat": [3, 3, 2, 1, 0.5],
                                                        "gym-goer": [1.5, 3, 3, 2, 1], "coach": [2, 3, 1, 0.5, 0.2]}[group])[0]
    price = random.choices(["£1.50", "£2.00", "£2.50", "£3.00", "wouldn't buy"],
                           weights=[2, 4, 3, 1, 1] if reaction >= 3 else [3, 2, 0.5, 0.2, 4])[0]
    return dict(
        id=f"F{i:02d}", name=f"{FIRST[i-1]} (fictional)", group=group, sport=random.choice(SPORTS[group]),
        sessions_per_week=sess, coached="yes" if group in ("squad athlete", "MMA / combat") else random.choice(["yes", "no"]),
        last_post_training_food=random.choice(POST_FOOD), missed_meal_freq_per_week=random.choice([0, 1, 2, 2, 3, 4]),
        bars_last_month=random.choice([0, 0, 2, 4, 6, 10, 12]), bar_brands=random.choice(BRANDS),
        bar_annoyances=random.choice(ANNOY), coach_advice=random.choice(COACH_ADVICE), first_reaction_1to5=reaction,
        barriers=random.choice(BARRIERS), price_gbp=price,
        taste_test_yes="yes" if reaction >= 3 and random.random() < 0.8 else "no",
        quote=random.choice(REACT[reaction]))

people, i = [], 1
for g, n in GROUPS:
    for _ in range(n):
        people.append(person(i, g)); i += 1

# 1) interviews CSV
fields = list(people[0].keys()) + ["data_status"]
with open(HERE / "FICTIONAL_interviews.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
    for p in people:
        w.writerow({**p, "data_status": "FICTIONAL"})

# 2) transcripts
md = [f"# FICTIONAL interview transcripts (50)\n\n> **{BANNER}**\n"]
for p in people:
    md.append(f"## {p['id']} · {p['name']} · {p['group']} · {p['sport']}\n*FICTIONAL*\n")
    if p["group"] == "coach":
        md += [f"- **What do you tell athletes to eat after training?** \"Mostly to {p['coach_advice']}.\"",
               f"- **What do they actually eat?** \"A lot of them grab {p['last_post_training_food']}, or {p['bar_brands'] if p['bar_brands']!='none' else 'nothing'}.\"",
               f"- **Ever supplied bars to a squad?** \"We've had boxes of bars; the main complaint was {p['bar_annoyances']}.\"",
               f"- **Would you trial a fresh real-food snack?** \"{p['quote']} I'd want to see that it {p['barriers'].replace('has to ','')}.\"",
               f"- **Reaction (1–5):** {p['first_reaction_1to5']} · **Taste test:** {p['taste_test_yes']}\n"]
    else:
        md += [f"- **Last training day and what you ate after?** \"{p['sport'].capitalize()}, then {p['last_post_training_food']}.\"",
               f"- **How often do you miss a proper meal after training?** \"About {p['missed_meal_freq_per_week']} times a week.\"",
               f"- **Protein bars last month?** \"{p['bars_last_month']}, usually {p['bar_brands']}.\"",
               f"- **What annoys you about them?** \"{p['bar_annoyances'].capitalize()}.\"",
               f"- **Coach advice?** \"{p['coach_advice'].capitalize()}.\"",
               f"- **First reaction to the card?** \"{p['quote']}\" ({p['first_reaction_1to5']}/5)",
               f"- **What would stop you?** \"{p['barriers'].capitalize()}.\"",
               f"- **Price?** {p['price_gbp']} · **Taste test:** {p['taste_test_yes']}\n"]
(HERE / "FICTIONAL_interview_transcripts.md").write_text("\n".join(md))

# 3) Google-Forms-style survey CSV (same 50 fictional people, non-coaches answer survey)
qs = ["Timestamp", "How often do you train?", "Are you coached (club, squad or PT)?",
      "How often can't you eat a proper meal within 2 hours of training?", "In the last month, how many protein bars did you eat?",
      "What puts you off protein bars?", "How appealing is a fresh, real-food protein snack?", "What would you pay for one?",
      "Email (optional)", "Anything else about what you eat after training?"]
def band(n): return "1–2" if n <= 2 else "3–4" if n <= 4 else "5–6" if n <= 6 else "7+"
def missed(n): return "never" if n == 0 else "sometimes" if n <= 2 else "often"
def bars(n): return "0" if n == 0 else "1–3" if n <= 3 else "4–10" if n <= 10 else "10+"
with open(HERE / "FICTIONAL_survey_export.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(qs)
    for p in people:
        if p["group"] == "coach":
            continue
        w.writerow(["FICTIONAL", band(p["sessions_per_week"]), p["coached"].capitalize(), missed(p["missed_meal_freq_per_week"]),
                    bars(p["bars_last_month"]), p["bar_annoyances"], p["first_reaction_1to5"], p["price_gbp"],
                    "fictional@example.com" if p["taste_test_yes"] == "yes" else "", p["quote"]])
print(f"Wrote {len(people)} fictional interviews + {sum(p['group']!='coach' for p in people)} fictional survey rows. {BANNER}")
