"""
Student Perspective on Solar Car Parking System
Pie charts of the Google Form responses, one per question.
Usage: python solar_parking_pie_charts.py "student perspective  google form (Responses).xlsx"
"""
import sys
import textwrap
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILE = sys.argv[1] if len(sys.argv) > 1 else "students perspective dataset.xlsx"
TITLE = "Student Perspective on Solar Car Parking System"

df = pd.read_excel(FILE)
df.columns = [c.strip() for c in df.columns]
questions = [c for c in df.columns if c.lower() != "timestamp"]

# Categories exactly as defined in the Google Form (used for ordering)
SCALE_USEFUL = {1: "1 - Not useful at all", 2: "2", 3: "3", 4: "4", 5: "5 - Extremely useful"}
SCALE_RATING = {1: "1 - Very poor", 2: "2", 3: "3", 4: "4", 5: "5 - Excellent"}

short_titles = [
    "Q1. Awareness of solar car parking systems",
    "Q2. Noticed solar panels on VIT campus",
    "Q3. Usefulness of solar PV parking at VIT (1-5)",
    "Q4. Expected benefits (multiple choice)",
    "Q5. Biggest challenge for campus solar",
    "Q6. Can solar reduce VIT's environmental impact?",
    "Q7. Most important factor for useful solar",
    "Q8. Current parking shade & protection (1-5)",
    "Q9. Parking-lot solar vs rooftop solar",
    "Q10. Allocation of solar parking spaces",
]


def categorise(i, col):
    s = df[col].dropna()
    if i == 2:                                   # Q3: 1-5 usefulness scale
        return s.astype(int).map(SCALE_USEFUL).value_counts().reindex(SCALE_USEFUL.values()).dropna().astype(int)
    if i == 7:                                   # Q8: 1-5 rating scale
        return s.astype(int).map(SCALE_RATING).value_counts().reindex(SCALE_RATING.values()).dropna().astype(int)
    if i == 3:                                   # Q4: multi-select -> split each response
        opts = s.str.split(r",\s*(?=[A-Z])").explode().str.strip()
        return opts.value_counts()
    return s.astype(str).str.strip().value_counts()


sns.set_theme(style="white", context="notebook")
fig, axes = plt.subplots(5, 2, figsize=(16, 40))
axes = axes.flatten()

for i, (col, ax) in enumerate(zip(questions, axes)):
    counts = categorise(i, col)
    colors = sns.color_palette("Set2", len(counts))
    wedges, _, autotexts = ax.pie(
        counts.values,
        colors=colors,
        startangle=90,
        counterclock=False,
        autopct=lambda p: f"{p:.1f}%" if p >= 6 else "",
        pctdistance=0.72,
        wedgeprops=dict(edgecolor="white", linewidth=2),
        textprops=dict(fontsize=11, fontweight="bold", color="#222"),
    )
    total = counts.sum()
    labels = [f"{textwrap.fill(str(k), 60)}  ({v}, {v / total:.1%})" for k, v in counts.items()]
    ax.legend(wedges, labels, loc="upper center", bbox_to_anchor=(0.5, 0.02),
              fontsize=11, frameon=False, ncol=1)
    note = "  (counts = selections)" if i == 3 else f"  (n = {int(counts.sum())})"
    ax.set_title(short_titles[i] + note, fontsize=13, fontweight="bold", pad=10)
    ax.axis("equal")

fig.suptitle(TITLE, fontsize=24, fontweight="bold", y=1.0)
fig.text(0.5, 0.989, f"Survey of {len(df)} VIT students", ha="center", fontsize=13, color="#555")
plt.tight_layout(rect=[0, 0, 1, 0.985])
plt.savefig("student_perspective_solar_car_parking_pie_charts.png", dpi=200, bbox_inches="tight")
print("Saved: student_perspective_solar_car_parking_pie_charts.png")
