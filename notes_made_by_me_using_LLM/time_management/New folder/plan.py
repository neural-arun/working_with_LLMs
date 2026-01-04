#!/usr/bin/env python3
"""
Generate a 60-day dense time-management logbook as a single Markdown file,
optimized so each day fits on exactly one A4 page.

Start date: 2025-09-16
Pages: 60 (one day per A4 page)
Output: 60_day_logbook.md
"""

from datetime import datetime, timedelta
import calendar

# -------- CONFIG ----------
START_DATE = datetime(2025, 9, 16)
NUM_DAYS = 60
OUTPUT_MD = "60_day_logbook.md"
# ---------------------------

HOURS = [
    "00:00–01:00", "01:00–02:00", "02:00–03:00", "03:00–04:00",
    "04:00–05:00", "05:00–06:00", "06:00–07:00", "07:00–08:00",
    "08:00–09:00", "09:00–10:00", "10:00–11:00", "11:00–12:00",
    "12:00–13:00", "13:00–14:00", "14:00–15:00", "15:00–16:00",
    "16:00–17:00", "17:00–18:00", "18:00–19:00", "19:00–20:00",
    "20:00–21:00", "21:00–22:00", "22:00–23:00", "23:00–24:00",
]

DAILY_CHECKLIST = [
    "Wake by 05:30 / morning routine (hydration, quick stretch)",
    "First focused study block — 90+ minutes (Pomodoro)",
    "Coding / project work — 60 minutes",
    "Active revision (flashcards / MCQs) — 30–45 minutes",
    "Physical exercise — 20–40 minutes",
    "No social media during deep work",
    "Plan tomorrow (3 top priorities)",
    "Read / learn something new — 30 minutes",
    "Sleep by 23:00 target",
]

def weekday_name(date_obj):
    return calendar.day_name[date_obj.weekday()]

# Much tighter CSS to force single-page layout per day
HEADER = """<!-- Tight A4 CSS to fit one day per page -->
<style>
@page { size: A4; margin: 10mm; }

/* Ensure each day block occupies one printable page */
.day-page {
  box-sizing: border-box;
  display: block;
  page-break-after: always;
  /* content box height = A4 height (297mm) minus top+bottom margins (2*10mm) */
  height: calc(297mm - 20mm);
  overflow: hidden;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 10px;
  line-height: 1.05;
}

/* Compact header */
.day-title {
  font-size: 12px;
  font-weight:700;
  margin: 0 0 4px 0;
}

/* Dense table */
.log-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9.25px;
}
.log-table th, .log-table td {
  border: 1px solid #333;
  padding: 2px 4px;
  vertical-align: middle;
}
.log-table th {
  background: #f4f4f4;
  font-weight:700;
  font-size: 9.5px;
}
.log-table td { height: 10px; }

/* Tight review and boxes */
.section-title { font-weight:700; margin-top:6px; margin-bottom:4px; font-size:10px; }
.box {
  border: 1px dashed #333;
  padding: 6px;
  min-height: 28px;
  font-size: 9.25px;
  overflow: hidden;
}

/* Signature row compressed */
.signature-line {
  margin-top: 8px;
  display:flex;
  justify-content:space-between;
  font-size: 9px;
}
.signature-line .left { width: 45%; border-top: 1px solid #333; text-align:left; padding-top:4px; }
.signature-line .right { width: 45%; border-top: 1px solid #333; text-align:right; padding-top:4px; }

/* Checklist - small and compact */
.checklist { margin-top: 6px; font-size: 9px; }
.checklist ul { margin: 2px 0 0 16px; padding:0; }

/* Reduce list spacing */
.day-page ul { margin: 0 0 0 14px; padding: 0; }
.day-page li { margin: 2px 0; }

/* Force no page breaks inside the day content */
.day-page, .day-page * { break-inside: avoid; -webkit-column-break-inside: avoid; }

/* Slightly reduce spacing in table header */
.log-table thead th { padding-top:2px; padding-bottom:2px; }
</style>

"""

DAY_TEMPLATE = """
<div class="day-page">
  <div class="day-title">{weekday}, {date_str}  &nbsp;&nbsp;  Day {day_index} / {total_days}</div>

  <table class="log-table">
    <thead>
      <tr>
        <th style="width:16%;">Time</th>
        <th style="width:42%;">Expected</th>
        <th style="width:42%;">Actual</th>
      </tr>
    </thead>
    <tbody>
{rows}
    </tbody>
  </table>

  <div class="section-title">End of Day Review</div>
  <ul>
    <li>Top wins / achievements:</li>
    <li>Biggest distractions / time leaks:</li>
    <li>Energy / focus (1–10):</li>
    <li>Quick notes / learnings:</li>
  </ul>

  <div class="section-title">Improvement Box (What will I change tomorrow?)</div>
  <div class="box"></div>

  <div class="signature-line">
    <div class="left">Signature</div>
    <div class="right">Date</div>
  </div>

  <div class="checklist">
    <div style="font-weight:700; margin-bottom:4px; font-size:9.5px;">Daily MUST-DO Checklist (non-negotiable)</div>
    <ul>
{checklist_items}
    </ul>
  </div>
</div>

<div style="height:0; visibility:hidden;"></div>
"""

def make_hour_rows():
    lines = []
    for h in HOURS:
        lines.append(
            f'      <tr>\n        <td style="padding:2px 4px;">{h}</td>\n        <td></td>\n        <td></td>\n      </tr>'
        )
    return "\n".join(lines)

def make_checklist_html():
    lines = []
    for item in DAILY_CHECKLIST:
        # compact checklist item
        lines.append(f'      <li>[ ] {item}</li>')
    return "\n".join(lines)

def main():
    rows_html = make_hour_rows()
    checklist_html = make_checklist_html()

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("<!-- 60-Day Time Management Logbook — one day per A4 page (tight layout) -->\n")
        f.write(HEADER)
        for i in range(NUM_DAYS):
            day_date = START_DATE + timedelta(days=i)
            weekday = weekday_name(day_date)
            page_md = DAY_TEMPLATE.format(
                weekday=weekday,
                date_str=day_date.strftime("%d %B %Y"),
                day_index=i+1,
                total_days=NUM_DAYS,
                rows=rows_html,
                checklist_items=checklist_html
            )
            f.write(page_md)
    print(f"Wrote {OUTPUT_MD} with {NUM_DAYS} pages starting {START_DATE.strftime('%Y-%m-%d')}.")

if __name__ == "__main__":
    main()
