"""
make_logbook_engineered.py
Generates engineered_productivity_logbook.pdf — A4 portrait pages, 1 day per page.

Changes from previous version:
- Removed "Quote of the day"
- Time formatted as ranges (00:00-01:00 ... 23:00-24:00) with 24 rows
- Replaced Gratitude with "Biggest problems faced in the day"
- Habit tracker uses one checkbox per habit
- Added "Arun Yadav" on top of the page
- Footer is a single-line short motivation quote
- Added a signature line at the bottom-right of each page.
- Added a unique "Weekly Review" page for every Sunday.
- Added "Expected" and "Actual" labels to the Time Log columns.
- Aligned the footer quote to the right to prevent overlap.
- Added a vertical divider between the "Expected" and "Actual" columns.
- NEW: Every Sunday now generates TWO pages: the standard daily log AND the weekly review page.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date, timedelta
import os
import random

# Optional: register a clean sans-serif if available on your system
try:
    pdfmetrics.registerFont(TTFont("Inter", "Inter-Regular.ttf"))
    FONT = "Inter"
except Exception:
    FONT = "Helvetica"

PAGE_SIZE = A4
W, H = PAGE_SIZE

OUTPUT = "engineered_productivity_logbook.pdf"
NUM_DAYS = 100
START_DATE = date.today()

# Styling values
MARGIN = 12 * mm
LINE_COLOR = colors.HexColor("#000000")
HEADER_COLOR = colors.HexColor("#000000")
LIGHT_GREY = colors.HexColor("#000000")

usable_w = W - 2 * MARGIN
usable_h = H - 2 * MARGIN

FOOTER_QUOTES = [
    "The secret of getting ahead is getting started.",
    "Do it now. Sometimes 'later' becomes 'never'.",
    "Discipline is the bridge between goals and accomplishment.",
    "A year from now you may wish you had started today.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Consistency is what transforms average into excellence."
]

def dot_grid(c, x, y, w, h, spacing=6*mm, dot_radius=0.25):
    """Draw faint dotted grid for handwriting guidance."""
    c.saveState()
    c.setFillColor(colors.HexColor("#e6e9ec"))
    nx = max(2, int(w / spacing) + 1)
    ny = max(2, int(h / spacing) + 1)
    x0 = x + (spacing / 2)
    y0 = y + (spacing / 2)
    for i in range(nx):
        for j in range(ny):
            cx = x0 + i * spacing
            cy = y0 + j * spacing
            if cx < x + w - 1 and cy < y + h - 1:
                c.circle(cx, cy, dot_radius, stroke=0, fill=1)
    c.restoreState()

def small_checkbox(c, x, y, size=6):
    c.rect(x, y, size, size, stroke=1, fill=0)

def draw_section_title(c, x, y, title):
    c.setFont(FONT, 8)
    c.setFillColor(HEADER_COLOR)
    c.drawString(x, y, title)

def draw_box(c, x, y, w, h):
    c.setLineWidth(1)
    c.setStrokeColor(LINE_COLOR)
    c.rect(x, y, w, h, stroke=1, fill=0)
    c.setStrokeColor(colors.black)

def draw_header(c, day_index, the_date):
    left = MARGIN
    right = W - MARGIN
    top = H - MARGIN
    
    # Header area
    header_h = 28 * mm
    header_x = left
    header_y = top - header_h
    draw_box(c, header_x, header_y, usable_w, header_h)

    # Date + day (left)
    c.setFont(FONT, 14)
    c.setFillColor(HEADER_COLOR)
    date_str = the_date.strftime("%A, %d %b %Y")
    c.drawString(header_x + 8, header_y + header_h - 18, date_str)

    # Your name (top-right)
    c.setFont(FONT, 10)
    c.setFillColor(HEADER_COLOR)
    c.drawRightString(right - 8, header_y + header_h - 14, "Arun Yadav")

    # Small day progress (right, under name)
    c.setFont(FONT, 8)
    progress_text = f"Day {day_index + 1} / {NUM_DAYS}"
    c.drawRightString(right - 8, header_y + header_h - 28, progress_text)

def draw_footer_and_signature(c):
    left = MARGIN
    right = W - MARGIN
    bottom = MARGIN

    # Signature line (bottom-right)
    c.setFont(FONT, 9)
    c.setFillColor(HEADER_COLOR)
    sig_y = bottom + 18
    c.drawString(right - 100, sig_y, "Signature:")
    c.line(right - 70, sig_y - 1, right - 10, sig_y - 1)

    # Footer one-line short motivation quote (bottom-right)
    footer_y = bottom + 6
    c.setFont(FONT, 8)
    c.setFillColor(HEADER_COLOR)
    quote = random.choice(FOOTER_QUOTES)
    c.drawRightString(right - 8, footer_y, quote)
    c.setFillColor(colors.black)

def draw_daily_page(c, day_index, the_date):
    left = MARGIN
    right = W - MARGIN
    top = H - MARGIN
    bottom = MARGIN

    # faint outer frame
    c.setStrokeColor(LINE_COLOR)
    c.setLineWidth(1.0)
    c.rect(left - 6, bottom - 6, (right - left) + 12, (top - bottom) + 12, stroke=1, fill=0)
    c.setStrokeColor(colors.black)
    
    draw_header(c, day_index, the_date)
    
    header_h = 28 * mm
    header_y = top - header_h

    # Energy / Focus score (right top inside header)
    ef_box_w = 46 * mm
    ef_box_h = 12 * mm
    ef_x = right - ef_box_w - 8
    ef_y = header_y + 8
    c.setLineWidth(1)
    c.setStrokeColor(LINE_COLOR)
    c.rect(ef_x, ef_y, ef_box_w, ef_box_h, stroke=1, fill=0)
    c.setFillColor(HEADER_COLOR)
    c.setFont(FONT, 9)
    c.drawString(ef_x + 6, ef_y + ef_box_h - 10, "Energy / Focus (0-10): ______")
    c.setStrokeColor(colors.black)

    # Top 3 Priorities
    pri_h = 28 * mm
    pri_w = (usable_w - 16) / 3
    pri_x = left
    pri_y = header_y - pri_h - 8
    for i in range(3):
        x = pri_x + i * (pri_w + 8)
        draw_box(c, x, pri_y, pri_w, pri_h)
        c.setFont(FONT, 9)
        c.setFillColor(HEADER_COLOR)
        c.drawString(x + 6, pri_y + pri_h - 12, f"Top Priority #{i+1}")
        dot_grid(c, x + 6, pri_y + 6, pri_w - 12, pri_h - 20, spacing=7*mm, dot_radius=0.2)

    # Left column: Time Log (tall)
    time_w = usable_w * 0.38
    time_h = pri_y - bottom - 12
    time_x = left
    time_y = bottom + 12
    draw_box(c, time_x, time_y, time_w, time_h)
    draw_section_title(c, time_x + 6, time_y + time_h - 10, "Time Log")

    # Time log grid: 
    time_label_width = 44
    mid_x = time_x + time_label_width
    
    c.setFont(FONT, 7)
    c.setFillColor(HEADER_COLOR)
    col_width = (time_w - time_label_width) / 2
    c.drawCentredString(mid_x + col_width / 2, time_y + time_h - 16, "Expected")
    c.drawCentredString(mid_x + col_width * 1.5, time_y + time_h - 16, "Actual")

    rows = 24
    row_h = (time_h - 18) / rows
    c.setFont(FONT, 7)
    c.setStrokeColor(LINE_COLOR)
    for r in range(rows):
        y = time_y + time_h - 18 - (r+1) * row_h + 2
        c.setLineWidth(0.5)
        c.line(time_x + 6, y, time_x + time_w - 6, y)
        # hour range label
        start_hour = r
        end_hour = r + 1
        start_label = f"{start_hour:02d}:00"
        end_label = f"{end_hour:02d}:00"
        hour_label = f"{start_label}-{end_label}"
        c.setFillColor(HEADER_COLOR)
        c.drawString(time_x + 8, y + 3, hour_label)
    
    # Vertical dividers
    c.line(mid_x, time_y + time_h - 18, mid_x, time_y + 2)
    divider_2_x = mid_x + col_width
    c.line(divider_2_x, time_y + time_h - 18, divider_2_x, time_y + 2)
    c.setStrokeColor(colors.black)

    # Right column: Reflection + Habits + Notes
    right_x = time_x + time_w + 12
    right_w = usable_w - time_w - 12

    # Wins box
    wins_h = 22 * mm
    wins_x = right_x
    wins_y = top - header_h - pri_h - wins_h - 22
    draw_box(c, wins_x, wins_y, right_w, wins_h)
    draw_section_title(c, wins_x + 6, wins_y + wins_h - 12, "Wins")

    # Key Learnings & Distractions
    kl_h = 28 * mm
    kl_w = (right_w - 8) / 2
    kl_x = right_x
    kl_y = wins_y - kl_h - 8
    draw_box(c, kl_x, kl_y, kl_w, kl_h)
    draw_section_title(c, kl_x + 6, kl_y + kl_h - 12, "Key Learnings")
    dis_x = kl_x + kl_w + 8
    draw_box(c, dis_x, kl_y, kl_w, kl_h)
    draw_section_title(c, dis_x + 6, kl_y + kl_h - 12, "Distractions")

    # Plan for Tomorrow
    plan_h = 22 * mm
    plan_x = right_x
    plan_y = kl_y - plan_h - 8
    draw_box(c, plan_x, plan_y, right_w, plan_h)
    draw_section_title(c, plan_x + 6, plan_y + plan_h - 12, "Plan for Tomorrow")

    # Biggest Problems faced in the day (replaces Gratitude)
    prob_h = 22 * mm
    prob_x = right_x
    prob_y = plan_y - prob_h - 8
    draw_box(c, prob_x, prob_y, right_w, prob_h)
    draw_section_title(c, prob_x + 6, prob_y + prob_h - 12, "Biggest problems faced in the day")
    # 3 lines with checkboxes
    c.setFont(FONT, 9)
    for i in range(3):
        yline = prob_y + prob_h - 28 - i * 12
        small_checkbox(c, prob_x + 10, yline, size=8)
        c.line(prob_x + 26, yline + 4, prob_x + right_w - 12, yline + 4)

    # Habit tracker (one checkbox per habit)
    habit_h = 26 * mm
    habit_x = right_x
    habit_y = prob_y - habit_h - 8
    draw_box(c, habit_x, habit_y, right_w, habit_h)
    draw_section_title(c, habit_x + 6, habit_y + habit_h - 12, "Habit Tracker (check if done)")
    habits = ["Go For Run", "Commit on Github", "4 Focus blocks", "No Distraction"]
    c.setFont(FONT, 9)
    cx = habit_x + 8
    cy = habit_y + habit_h - 28
    box_size = 10
    for i, h in enumerate(habits):
        c.drawString(cx, cy, h)
        small_checkbox(c, cx + 120, cy - 2, size=box_size)
        cy -= 14

    # Notes / Brain Dump (largest area bottom-right)
    notes_h = habit_y - bottom - 24
    notes_x = right_x
    notes_y = bottom + 12
    draw_box(c, notes_x, notes_y, right_w, notes_h)
    draw_section_title(c, notes_x + 6, notes_y + notes_h - 12, "Notes / Brain Dump")
    dot_grid(c, notes_x + 8, notes_y + 8, right_w - 16, notes_h - 24, spacing=6*mm, dot_radius=0.25)

    draw_footer_and_signature(c)

def draw_sunday_review_page(c, day_index, the_date):
    left = MARGIN
    right = W - MARGIN
    top = H - MARGIN
    bottom = MARGIN

    # faint outer frame
    c.setStrokeColor(LINE_COLOR)
    c.setLineWidth(1.0)
    c.rect(left - 6, bottom - 6, (right - left) + 12, (top - bottom) + 12, stroke=1, fill=0)
    c.setStrokeColor(colors.black)
    
    draw_header(c, day_index, the_date)

    header_h = 28 * mm
    content_start_y = top - header_h - 8

    # Overall Week Rating (in header)
    c.setFont(FONT, 10)
    c.setFillColor(HEADER_COLOR)
    c.drawString(left + 8, top - header_h + 10, "Overall Week Rating (1-10): ______")

    # Box 1: Biggest Wins This Week
    box1_h = 70 * mm
    box1_y = content_start_y - box1_h
    draw_box(c, left, box1_y, usable_w, box1_h)
    draw_section_title(c, left + 6, box1_y + box1_h - 12, "Biggest Wins This Week")
    dot_grid(c, left + 8, box1_y + 8, usable_w - 16, box1_h - 24, spacing=6*mm, dot_radius=0.25)

    # Box 2: Challenges & Lessons Learned
    box2_h = 70 * mm
    box2_y = box1_y - box2_h - 8
    draw_box(c, left, box2_y, usable_w, box2_h)
    draw_section_title(c, left + 6, box2_y + box2_h - 12, "Challenges & Lessons Learned")
    dot_grid(c, left + 8, box2_y + 8, usable_w - 16, box2_h - 24, spacing=6*mm, dot_radius=0.25)
    
    # Two columns for Habit Review and Next Week's Goals
    col_w = (usable_w - 8) / 2
    col_h = box2_y - bottom - 20
    
    # Left Column: Habit Consistency Review
    habits_x = left
    habits_y = bottom + 12
    draw_box(c, habits_x, habits_y, col_w, col_h)
    draw_section_title(c, habits_x + 6, habits_y + col_h - 12, "Habit Consistency Review")
    habits = ["Go For Run", "Commit on Github", "4 Focus blocks", "No Distraction"]
    c.setFont(FONT, 10)
    cy = habits_y + col_h - 28
    for h in habits:
        c.drawString(habits_x + 10, cy, f"{h}: ____ / 7")
        cy -= 18

    # Right Column: Top 3 Goals for Next Week
    goals_x = left + col_w + 8
    goals_y = bottom + 12
    draw_box(c, goals_x, goals_y, col_w, col_h)
    draw_section_title(c, goals_x + 6, goals_y + col_h - 12, "Top 3 Goals for Next Week")
    c.setFont(FONT, 12)
    for i in range(3):
        yline = goals_y + col_h - 32 - i * 30
        c.drawString(goals_x + 10, yline, f"{i+1}.")
        c.line(goals_x + 20, yline - 2, goals_x + col_w - 12, yline - 2)

    draw_footer_and_signature(c)

def main():
    c = canvas.Canvas(OUTPUT, pagesize=PAGE_SIZE)
    c.setAuthor("Arun Yadav")
    c.setTitle("Engineered Productivity Logbook")
    current = START_DATE
    page_count = 0
    
    for i in range(NUM_DAYS):
        # 1. Always draw the standard daily page for every day, including Sunday.
        draw_daily_page(c, i, current)
        c.showPage()
        page_count += 1
        
        # 2. If it's a Sunday (weekday 6), ALSO draw the review page.
        if current.weekday() == 6:
            draw_sunday_review_page(c, i, current)
            c.showPage()
            page_count += 1
            
        current = current + timedelta(days=1)
        
    c.save()
    print(f"Saved {OUTPUT} ({page_count} pages for {NUM_DAYS} days, start date {START_DATE.isoformat()})")

if __name__ == "__main__":
    main()
    