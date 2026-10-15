# Student Perspective on Solar Car Parking System

Pie-chart visualisation of a student survey on solar PV car parking at VIT Vellore, built with Python, matplotlib and seaborn.

## Dataset

- **File:** `Untitled form (Responses).xlsx` (Google Forms export)
- **Survey:** *Student Perception of Solar PV Panel Car Parking System at VIT*
- **Responses:** 26 students, collected on 13 October 2026
- **Columns:** a `Timestamp` column plus one column for each of the 10 questions

| # | Question | Answer type |
|---|----------|-------------|
| 1 | Are you aware of solar-powered car parking systems? | Single choice |
| 2 | Have you noticed any solar panels installed on the VIT campus? | Single choice |
| 3 | How useful do you think a solar PV car parking system would be at VIT? | Scale 1–5 |
| 4 | What benefits do you expect from a solar PV car parking system? | Multiple choice |
| 5 | What do you think is the biggest challenge in using solar energy on campus? | Single choice |
| 6 | Do you think solar energy can help reduce the environmental impact of VIT's electricity consumption? | Single choice |
| 7 | What do you think is the most important factor for making solar energy more useful on campus? | Single choice |
| 8 | How would you rate the current parking facilities on campus in terms of shading and vehicle protection? | Scale 1–5 |
| 9 | Do you think solar panels over parking areas offer more benefits than solar panels on building rooftops? | Single choice |
| 10 | If solar-powered parking spaces are available, how should they be allocated? | Single choice |

## Visualisation

The script makes one pie chart for each question and saves 10 PNG images at 200 dpi.

- Every chart has the title **"Student Perspective on Solar Car Parking System"**, with the full question below it.
- Slices are grouped by the answer options defined in the Google Form.
- The legend gives the count and percentage for each answer. Slices under 6% show no label on the pie, but they still appear in the legend.
- Charts use seaborn's `Set2` colour palette.

## Python code

**File:** `solar_parking_pie_charts.py`

**Purpose:** reads the survey export, groups each question's responses by answer option, and saves one pie chart per question.

How it works:

1. Loads the Excel file with pandas and skips the `Timestamp` column.
2. Counts the answers for each question:
   - **Single-choice questions:** counts each answer option.
   - **1–5 scale questions (Q3, Q8):** labels the end points, for example "1 - Not useful at all" and "5 - Extremely useful", and keeps the scores in order from 1 to 5.
   - **Multiple-choice question (Q4):** splits each response into its separate options and counts each option. The percentages are shares of all options chosen, not of students.
3. Draws each pie with matplotlib, styled with seaborn.
4. Saves the images to `pie_charts/Q01_pie_chart.png` … `pie_charts/Q10_pie_chart.png`.

### Requirements

```bash
pip install pandas matplotlib seaborn openpyxl
```

### Usage

```bash
python solar_parking_pie_charts.py "Untitled form (Responses).xlsx"
```

The 10 charts are saved in the `pie_charts/` folder.

## Repository structure

```
├── Untitled form (Responses).xlsx   # survey dataset
├── solar_parking_pie_charts.py      # visualisation script
├── pie_charts/                      # generated charts (Q01–Q10)
└── README.md
```
