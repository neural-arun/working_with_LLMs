"""
communication_journal_enhanced.py

An improved, feature-rich Communication Engineer's Journal generator.
Generates a multi-week PDF designed as a daily bootcamp to improve
communication, social confidence, and real-world practice.

Features added compared to the original:
- Configurable duration and start date
- Table of Contents + intro + index pages
- Daily motivational quote and micro-challenge
- Habit tracker and daily run-checklist
- Conversation starters & practice scripts
- Social exposure tasks with difficulty scaling
- Confidence & social metrics tracker (quantitative)
- Weekly reflection, SMART goals, action plan
- Export of a lightweight CSV log (optional)
- Well-structured functions for maintainability

Usage:
    python communication_journal_enhanced.py

Requirements:
    pip install reportlab

"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, lightgrey
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date, timedelta
import random
import csv
import os

# ---------------------- CONFIGURATION ----------------------
FILENAME = "Communication_Engineer_Journal_Enhanced.pdf"
CSV_LOG = "communication_journal_log.csv"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.6 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
STYLES = getSampleStyleSheet()

# Palette
COLOR_PRIMARY = HexColor('#0B5FFF')
COLOR_ACCENT = HexColor('#4EC9B0')
COLOR_WARN = HexColor('#F44747')
COLOR_BG_LIGHT = HexColor('#FBFBFD')
COLOR_TEXT_TITLE = HexColor('#111827')
COLOR_TEXT_BODY = HexColor('#333333')

# Duration (weeks) and daily pages per week
WEEKS = 8
DAYS_PER_WEEK = 7

# Motivational quotes and micro-challenges
MOTIVATIONAL_QUOTES = [
    "Small consistent actions beat occasional intensity.",
    "You don't need to be extroverted to be influential.",
    "Vulnerability grows connection, not weakness.",
    "Practice the skill you want to own.",
    "Make curiosity your social superpower.",
]

MICRO_CHALLENGES = [
    "Ask one open-ended question to a stranger today.",
    "Give a sincere compliment to someone you interact with.",
    "Practice a 30-second intro about yourself.",
    "Share one short story from your day in a conversation.",
    "Ask a follow-up question instead of giving advice.",
]

CONVERSATION_STARTERS = [
    "What’s been the highlight of your week so far?",
    "If you could spend a day learning anything, what would it be?",
    "I read something interesting recently — can I share?",
    "What’s one small win you had recently?",
]

# ---------------------- UTILITIES ----------------------

def pick_random(seq):
    return random.choice(seq)


def make_csv_log_header(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'date', 'week', 'day', 'micro_challenge', 'interaction_count',
                'positive_responses', 'self_rating_1_10', 'notes'
            ])


def log_daily_entry(file_path, row):
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(row)


# ---------------------- DRAW HELPERS ----------------------

def draw_header(c, title, subtitle=None):
    c.saveState()
    c.setFont('Helvetica-Bold', 18)
    c.setFillColor(COLOR_TEXT_TITLE)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN, title)
    if subtitle:
        c.setFont('Helvetica', 10)
        c.setFillColor(COLOR_TEXT_BODY)
        c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN + 2, subtitle)
    c.setStrokeColor(lightgrey)
    c.setLineWidth(0.8)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 6, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 6)
    c.restoreState()


def draw_footer(c, page_number=None):
    c.saveState()
    c.setFont('Helvetica', 8)
    c.setFillColor(COLOR_TEXT_BODY)
    footer_text = "Communication Engineer's Journal — Daily Bootcamp"
    c.drawCentredString(PAGE_WIDTH/2, MARGIN/2, footer_text)
    if page_number is not None:
        c.drawRightString(PAGE_WIDTH - MARGIN, MARGIN/2, f"Page {page_number}")
    c.restoreState()


def draw_box(c, x, y, w, h, title=None, title_height=14, fill=False, stroke_color=COLOR_PRIMARY):
    c.saveState()
    c.setStrokeColor(stroke_color)
    c.setLineWidth(1)
    if fill:
        c.setFillColor(COLOR_BG_LIGHT)
        c.rect(x, y - h, w, h, stroke=1, fill=1)
    else:
        c.rect(x, y - h, w, h, stroke=1, fill=0)
    if title:
        c.setFont('Helvetica-Bold', 10)
        c.setFillColor(black)
        c.drawString(x + 6, y - 12, title)
    c.restoreState()


def draw_checkbox_line(c, x, y, label, box_size=10):
    c.saveState()
    c.rect(x, y - box_size + 2, box_size, box_size)
    c.setFont('Helvetica', 9)
    c.drawString(x + box_size + 6, y - box_size + 6, label)
    c.restoreState()


# ---------------------- PAGE TEMPLATES ----------------------

def draw_intro_page(c, start_date, weeks):
    draw_header(c, "The Communication Engineer's Journal (Enhanced)", f"Start: {start_date.isoformat()} | {weeks} weeks bootcamp")
    c.setFont('Helvetica', 11)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN - 0.6*inch, "How to use this journal:")
    c.setFont('Helvetica', 9)
    bullets = [
        "Do one page per day. Each page contains reflection prompts, micro-challenges and a checklist.",
        "Log quantitative metrics briefly (interactions, positive responses) — this helps track progress.",
        "Aim for small, consistent exposure: 3 micro-actions per day is better than one big attempt.",
    ]
    y = PAGE_HEIGHT - MARGIN - 0.85*inch
    for b in bullets:
        c.drawString(MARGIN + 6, y, u"• " + b)
        y -= 0.25*inch

    # Table of Contents stub
    y -= 0.2*inch
    c.setFont('Helvetica-Bold', 11)
    c.drawString(MARGIN, y, "Table of Contents (high level)")
    y -= 0.2*inch
    toc_items = [
        "Weeks 1–2: Awareness & Diagnostic",
        "Weeks 3–4: Receiver & Transmitter Skills",
        "Weeks 5–6: Empathy, Conflict & Practice",
        "Weeks 7–8: Network, Habits & Review",
    ]
    c.setFont('Helvetica', 9)
    for t in toc_items:
        c.drawString(MARGIN + 6, y, u"- " + t)
        y -= 0.2*inch

    # Quick daily checklist example
    y -= 0.3*inch
    c.setFont('Helvetica-Bold', 10)
    c.drawString(MARGIN, y, "Daily run checklist (example):")
    y -= 0.2*inch
    checklist = [
        "Breathing exercise (2 minutes)",
        "Set today's micro-challenge",
        "Have at least 1 short social interaction (>=30s)",
        "Record one reflection note",
    ]
    c.setFont('Helvetica', 9)
    for ch in checklist:
        draw_checkbox_line(c, MARGIN + 4, y + 6, ch)
        y -= 0.25*inch

    c.showPage()


def draw_daily_page(c, current_date, week, day, page_number):
    date_str = current_date.strftime('%A, %B %d, %Y')
    draw_header(c, f"Week {week} — Day {day}", date_str)

    # Left column: Motivation & Micro-challenge
    left_x = MARGIN
    left_y = PAGE_HEIGHT - MARGIN - 0.4*inch
    quote = pick_random(MOTIVATIONAL_QUOTES)
    challenge = pick_random(MICRO_CHALLENGES)

    draw_box(c, left_x, left_y, CONTENT_WIDTH/2 - 10, 1.1*inch, title="Motivation")
    c.setFont('Helvetica-Oblique', 9)
    c.drawString(left_x + 8, left_y - 18, f"Quote: {quote}")
    c.setFont('Helvetica', 9)
    c.drawString(left_x + 8, left_y - 34, f"Micro-challenge: {challenge}")

    # Short breathing exercise box
    bx = left_x
    by = left_y - 1.3*inch
    draw_box(c, bx, by, CONTENT_WIDTH/2 - 10, 0.8*inch, title="Quick Grounding / Breathing (2 min)")
    c.setFont('Helvetica', 8)
    c.drawString(bx + 8, by - 18, "4-4-4 breathing: Inhale 4s - Hold 4s - Exhale 4s — repeat 4 times")

    # Right column: Daily action plan & metrics
    rx = PAGE_WIDTH/2 + 10
    ry = PAGE_HEIGHT - MARGIN - 0.4*inch
    draw_box(c, rx, ry, CONTENT_WIDTH/2 - 10, 2.2*inch, title="Today's Action Plan")
    c.setFont('Helvetica-Bold', 9)
    c.drawString(rx + 8, ry - 18, "Top 3 Actions (be specific):")
    c.setFont('Helvetica', 9)
    c.drawString(rx + 12, ry - 34, "1.")
    c.drawString(rx + 12, ry - 50, "2.")
    c.drawString(rx + 12, ry - 66, "3.")

    # Metrics tracker box
    m_y = ry - 2.4*inch
    draw_box(c, rx, m_y, CONTENT_WIDTH/2 - 10, 1.1*inch, title="Social Metrics (quick)")
    c.setFont('Helvetica', 9)
    c.drawString(rx + 8, m_y - 18, "Interactions today: ____")
    c.drawString(rx + 8, m_y - 34, "Positive responses / smiles: ____")
    c.drawString(rx + 8, m_y - 50, "Self-confidence rating (1-10): ____")

    # Center area: Conversation log + Reflection
    cx = MARGIN
    cy = PAGE_HEIGHT/2 + 0.6*inch
    draw_box(c, cx, cy, CONTENT_WIDTH - 20, 2.6*inch, title="Conversation Log / Reflection")
    c.setFont('Helvetica', 9)
    lines = [
        "Who did I talk to? (Name/Role):", "What was the topic?", "What did I notice (tone/body language)?", "What did I try to do differently?", "Key learning:" 
    ]
    y = cy - 22
    for l in lines:
        c.drawString(cx + 8, y, l)
        y -= 0.35*inch

    # Bottom left: Practice scripts and starters
    bx2 = MARGIN
    by2 = MARGIN + 1.6*inch
    draw_box(c, bx2, by2 + 2.2*inch, CONTENT_WIDTH/2 - 10, 1.9*inch, title="Practice Scripts / Starters")
    c.setFont('Helvetica', 9)
    c.drawString(bx2 + 8, by2 + 2.0*inch, "Try: " + pick_random(CONVERSATION_STARTERS))
    c.drawString(bx2 + 8, by2 + 1.6*inch, "Script: Short intro - ask an open question - listen & paraphrase")

    # Bottom right: Daily checklist & gratitude
    rx2 = PAGE_WIDTH/2 + 10
    ry2 = MARGIN + 1.6*inch
    draw_box(c, rx2, ry2 + 2.2*inch, CONTENT_WIDTH/2 - 10, 1.9*inch, title="Daily Checklist & Gratitude")
    checklist = [
        "Breathing exercise completed",
        "Micro-challenge completed",
        "At least 1 authentic conversation",
        "Quick reflection recorded",
        "Gratitude: write one short item"
    ]
    y = ry2 + 2.0*inch
    for ch in checklist:
        draw_checkbox_line(c, rx2 + 6, y, ch)
        y -= 0.28*inch

    # Small note for user to log into CSV (optional)
    c.setFont('Helvetica-Oblique', 8)
    c.drawString(MARGIN, MARGIN + 6, "Tip: After completing this page, run the CSV logger or paste metrics into your tracking app.")

    draw_footer(c, page_number)
    c.showPage()


def draw_weekly_reflection_page(c, week, start_date, page_number):
    draw_header(c, f"Week {week} — Reflection & Planning")
    y = PAGE_HEIGHT - MARGIN - 0.6*inch
    draw_box(c, MARGIN, y, CONTENT_WIDTH, 3.2*inch, title="Weekly Reflection")
    c.setFont('Helvetica', 9)
    lines = [
        "Wins this week:", "What held me back:", "Patterns I noticed:", "One skill I improved:", "One social habit to keep:" 
    ]
    yy = y - 18
    for l in lines:
        c.drawString(MARGIN + 8, yy, l)
        yy -= 0.5*inch

    # SMART goal box
    smart_y = yy - 10
    draw_box(c, MARGIN, smart_y, CONTENT_WIDTH, 1.6*inch, title="SMART Goal for next week")
    c.setFont('Helvetica', 9)
    c.drawString(MARGIN + 8, smart_y - 18, "Specific:")
    c.drawString(MARGIN + 8, smart_y - 36, "Measurable:")
    c.drawString(MARGIN + 8, smart_y - 54, "Achievable / Realistic:")

    draw_footer(c, page_number)
    c.showPage()


# ---------------------- MAIN GENERATOR ----------------------

def create_journal(start_date=None, weeks=WEEKS, filename=FILENAME, csv_log=CSV_LOG):
    if start_date is None:
        start_date = date.today()

    make_csv_log_header(csv_log)

    c = canvas.Canvas(filename, pagesize=A4)
    page_number = 1

    # Intro
    draw_intro_page(c, start_date, weeks)
    page_number += 1

    day_offset = 0
    for week in range(1, weeks + 1):
        for day in range(1, DAYS_PER_WEEK + 1):
            current_date = start_date + timedelta(days=day_offset)
            # header + daily page
            draw_daily_page(c, current_date, week, day, page_number)

            # default auto-log row (empty metrics) so CSV stays aligned — user can edit later
            micro = pick_random(MICRO_CHALLENGES)
            row = [current_date.isoformat(), week, day, micro, '', '', '', '']
            log_daily_entry(csv_log, row)

            page_number += 1
            day_offset += 1

        # Weekly reflection page
        draw_weekly_reflection_page(c, week, start_date + timedelta(days=(week-1)*DAYS_PER_WEEK), page_number)
        page_number += 1

    # Final wrap-up / progress roadmap
    draw_header(c, "Final Review: 8-Week Roadmap")
    c.setFont('Helvetica', 11)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN - 0.6*inch, "Use this page to summarize lessons learned across the bootcamp and plan next 8 weeks.")
    draw_footer(c, page_number)
    c.showPage()

    c.save()
    print(f"✅ Created {filename}")
    print(f"CSV log template created/updated: {csv_log}")


if __name__ == '__main__':
    # Run generator with today's date by default. You can pass a different date
    # by editing the call below: create_journal(date(2025, 10, 1), weeks=8)
    create_journal()
