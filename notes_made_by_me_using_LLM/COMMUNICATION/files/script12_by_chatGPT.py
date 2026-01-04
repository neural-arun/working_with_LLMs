# Enhanced Progressive Social Mastery Engineering Journal (v2)
# Improved per user's personalization request: intro bio page, tech-career integration,
# QR-code logging (optional), LinkedIn action prompts, achievement badges, micro-learning,
# weekly tech+social reflections, and other requested UX/content additions.

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, lightgrey
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date, timedelta, datetime
import os
import argparse
import logging
import textwrap
from typing import List, Optional
import tempfile

# Optional QR support: attempt to import qrcode and PIL; otherwise draw placeholders
try:
    import qrcode
    from PIL import Image
    QR_AVAILABLE = True
except Exception:
    QR_AVAILABLE = False

# --- USER PROFILE (added as requested) ---
USER_PROFILE = {
    "name": "Arun Yadav",
    "location": "Prayagraj, UP",
    "main_project": "NEETPrepGPT (AI-powered medical education)",
    "career_goal": "AI Engineer/Founder",
    "learning_focus": [
        "Python Mastery", "FastAPI", "Git workflow", "OpenAI API", "Product Launch",
        "Professional Networking", "Social Skill Engineering"
    ]
}

# --- Setup logging ---
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("SocialMasteryJournal")

# --- Colors ---
COLOR_PRIMARY = HexColor('#007ACC')
COLOR_ACCENT = HexColor('#4EC9B0')
COLOR_WARN = HexColor('#F44747')
COLOR_ENERGY = HexColor('#FFB347')
COLOR_WISDOM = HexColor('#9370DB')
COLOR_KNOWLEDGE = HexColor('#FF6B6B')
COLOR_BG_LIGHT = HexColor('#F3F3F3')
COLOR_TEXT_HEADER = HexColor('#2D2D2D')
COLOR_TEXT_BODY = HexColor('#3C3C3C')

FILENAME = "Progressive_Social_Mastery_Journal_enhanced.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.6 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
STYLES = getSampleStyleSheet()

# (Knowledge modules, challenges, metrics remain the same as prior version.)
# For brevity in this file we reuse the previous structures if present.

# --- Minimal placeholder modules (you can keep full modules from the original file) ---
KNOWLEDGE_MODULES = {
    1: {"title": "Emotional Intelligence & Self-Awareness",
        "learning_resources": ["Video: Emotional Intelligence overview", "Article: Self-awareness exercises"],
        "key_concepts": ["Self-awareness", "Self-management", "Social awareness", "Relationship management"]},
    2: {"title": "Response Control & Emotional Regulation",
        "learning_resources": ["Practice: Tactical pause", "Article: The Science of Self-Control"],
        "key_concepts": ["6-second rule", "Breathing techniques"]},
    3: {"title": "Active Listening & Deep Communication", "learning_resources": ["TED: Really listen"], "key_concepts": ["Levels of listening"]},
    4: {"title": "Clear Communication & Assertiveness", "learning_resources": ["Nonviolent Communication"], "key_concepts": ["I-statements"]},
    5: {"title": "Empathy & Perspective-Taking", "learning_resources": ["Exercises on perspective-taking"], "key_concepts": ["Cognitive vs affective empathy"]},
    6: {"title": "Conflict Resolution & Difficult Conversations", "learning_resources": ["Frameworks for negotiation"], "key_concepts": ["Positions vs interests"]},
    7: {"title": "Relationship Building & Network Cultivation", "learning_resources": ["Never Eat Alone"], "key_concepts": ["Reciprocity"]}
}

PROGRESSIVE_CHALLENGES = {
    1: ["Day 1: Make conscious eye contact with 5 strangers and smile. Log reactions.",
        "Day 2: Eye contact + smile with 3 people, say 'Hello' to 2 others.",
        "Day 3: Ask 1 person a simple logistical question.",
        "Day 4: Give 1 genuine compliment.",
        "Day 5: Ask a follow-up question.",
        "Day 6: Have a 3-turn conversation.",
        "Day 7: Initiate 2 brief conversations."],
    2: ["Use tactical pause..."]
}

WEEKLY_METRICS = {1: "Binary Success Metric: Yes/No + comfort level (1-10)", 2: "Response time metric"}
GOAL_TEMPLATES = {1: "My specific goal this week: Reduce social anxiety in [context]."}

# --- Utility: QR drawing (optional) ---
def _draw_qr_on_pdf(c, x, y, data: str, size: int = 120):
    """Try to render a QR code on the canvas. If qrcode isn't available, draw a placeholder box with instructions."""
    if QR_AVAILABLE:
        try:
            qr = qrcode.QRCode(box_size=3, border=2)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            img.save(tmp.name)
            c.drawImage(tmp.name, x, y - size, width=size, height=size, preserveAspectRatio=True, mask='auto')
            tmp.close()
            os.unlink(tmp.name)
            return True
        except Exception as e:
            logger.debug("QR generation failed: %s", e)
    # Fallback: draw placeholder box
    c.setStrokeColor(lightgrey)
    c.setLineWidth(1)
    c.rect(x, y - size, size, size)
    c.setFont("Helvetica", 8)
    c.drawCentredString(x + size/2, y - size/2, "QR not available")
    c.setFont("Helvetica", 7)
    c.drawCentredString(x + size/2, y - size/2 - 10, "Install 'qrcode' to enable")
    return False

# --- New: Intro bio page function (per user spec) ---
def draw_intro_bio_page(c):
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.2*inch, "Personalized Social Mastery Journal")

    c.setFont("Helvetica", 13)
    c.setFillColor(COLOR_TEXT_HEADER)
    y = PAGE_HEIGHT - 1.8*inch
    c.drawString(MARGIN, y, f"Name: {USER_PROFILE['name']}")
    c.drawString(MARGIN, y-0.25*inch, f"Location: {USER_PROFILE['location']}")
    c.drawString(MARGIN, y-0.5*inch, f"Main Project: {USER_PROFILE['main_project']}")
    c.drawString(MARGIN, y-0.75*inch, f"Career Goal: {USER_PROFILE['career_goal']}")
    c.drawString(MARGIN, y-1.0*inch, "Learning Focus:")
    for i, topic in enumerate(USER_PROFILE["learning_focus"], 1):
        c.drawString(MARGIN + 0.3*inch, y-1.0*inch-(i*0.18*inch), f"{i}. {topic}")

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y-2.2*inch, "This journal is crafted for you—a growth-minded developer & founder.")

    # Quick action prompts (one-liners)
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawString(MARGIN, y-2.6*inch, "Quick Actions:")
    c.drawString(MARGIN + 0.2*inch, y-2.85*inch, "• Pitch NEETPrepGPT to 3 LinkedIn contacts this week")
    c.drawString(MARGIN + 0.2*inch, y-3.05*inch, "• Ask 1 senior dev for feedback on your code")
    c.drawString(MARGIN + 0.2*inch, y-3.25*inch, "• Share one social-win on LinkedIn/GitHub")

    # QR for daily quick-log
    qr_label_y = y-4.0*inch
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN, qr_label_y, "Quick log (scan with phone):")
    qr_data = "https://example.com/quick-log?user=Arun"  # placeholder; user can replace with their logging URL
    _draw_qr_on_pdf(c, PAGE_WIDTH - MARGIN - 1.4*inch, qr_label_y + 0.8*inch, qr_data, size=120)

    c.showPage()

# --- Integrate Tech+Social prompts used in weekly review ---
TECH_SOCIAL_PROMPTS = [
    "This week, how did improved social skills help you with:",
    "• Technical collaboration (code review, study group, feedback)?",
    "• Networking (LinkedIn, Twitter, expert outreach)?",
    "• Learning (explaining concepts, asking questions, sharing resources)?",
    "",
    "Action Step: What's one developer or AI founder you will connect with next week?",
]

# --- Achievement badges page (visuals + placeholders) ---
def draw_achievement_badges_page(c):
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_ENERGY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, "Social & Career Achievement Badges")

    badges = [
        "💡 First LinkedIn tech connection",
        "🚀 First open-source collaborator onboarded",
        "🏆 First AI project demo delivered",
        "🔗 First successful professional introduction",
        "🎓 First technical mentorship call completed"
    ]
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    y = PAGE_HEIGHT - 2.2*inch
    for badge in badges:
        c.drawString(MARGIN, y, badge)
        y -= 0.35*inch

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y-0.2*inch, "Add your custom badges as you progress!")
    c.showPage()

# --- Reusable small-draw helpers (header, challenge, sections) ---
def draw_header(c, week, day, date_str):
    c.saveState()
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Week {week}: Progressive Social Lab")
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Day {day} | {date_str}")
    c.setStrokeColor(lightgrey)
    c.setLineWidth(1)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.25*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 0.25*inch)
    c.restoreState()

def draw_progressive_challenge_box(c, y_pos, week, day):
    week_challenges = PROGRESSIVE_CHALLENGES.get(week)
    challenge = "No challenge available for this week." if not week_challenges else week_challenges[min(day-1, len(week_challenges)-1)]
    c.saveState()
    c.setFillColor(COLOR_ACCENT)
    c.roundRect(MARGIN, y_pos - 1.5*inch, CONTENT_WIDTH, 1.5*inch, 0.1*inch, fill=1, stroke=1)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.3*inch, f"🎯 DAY {day} PROGRESSIVE CHALLENGE")
    c.setFont("Helvetica-Bold", 10)
    wrapped_ch = textwrap.wrap(challenge, width=110)
    desc_y = y_pos - 0.6*inch
    for line in wrapped_ch:
        c.drawString(MARGIN + 0.2*inch, desc_y, line)
        desc_y -= 0.2*inch
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.9*inch, "SUCCESS METRICS:")
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.1*inch, "☐ Challenge completed   ☐ Comfort: ___/10")
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.3*inch, "☐ Key learning: ________________________")
    c.restoreState()
    return y_pos - 1.7*inch

def draw_section(c, y_pos, title, content_prompts, height, color=COLOR_PRIMARY, include_lines=True):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(1.5)
    c.roundRect(MARGIN, y_pos - height, CONTENT_WIDTH, height, 0.05*inch)
    c.setFillColor(color)
    c.roundRect(MARGIN, y_pos - 0.4*inch, CONTENT_WIDTH, 0.4*inch, 0.05*inch, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN + 0.15*inch, y_pos - 0.27*inch, title)
    c.setFont("Helvetica", 9)
    c.setFillColor(COLOR_TEXT_BODY)
    current_y = y_pos - 0.6*inch
    for prompt in content_prompts:
        if prompt.strip():
            wrapped = textwrap.wrap(prompt, width=100)
            for i, wline in enumerate(wrapped):
                c.drawString(MARGIN + 0.15*inch, current_y, wline)
                current_y -= 0.18*inch
            if include_lines:
                line_y = current_y - 0.05*inch
                c.setStrokeColor(lightgrey)
                c.setLineWidth(0.5)
                for i in range(2):
                    c.line(MARGIN + 0.2*inch, line_y - (i * 0.15*inch), PAGE_WIDTH - MARGIN - 0.2*inch, line_y - (i * 0.15*inch))
                current_y -= 0.35*inch
        else:
            current_y -= 0.18*inch
    c.restoreState()
    return y_pos - height - 0.2*inch

# --- Daily page builder (augmented with tech prompts and QR logging note) ---
def draw_daily_page(c, date_str, week, day):
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    y = draw_progressive_challenge_box(c, y, week, day)
    prompts_execution = [
        "PRE-CHALLENGE MINDSET: How are you feeling before attempting this challenge?",
        "EXECUTION DETAILS: Describe exactly what happened when you tried the challenge:",
        "COMFORT LEVEL: Rate your comfort (1=terrifying, 10=completely natural): ___/10",
        "SUCCESS METRICS: Did you achieve the specific goal? ☐ Yes ☐ Partial ☐ No",
        "WHAT WORKED: What specific technique or approach was most helpful?",
        "WHAT TO ADJUST: What will you do differently in similar situations?",
        "Did you share a learning or social breakthrough today on LinkedIn/GitHub? If yes, paste link:"
    ]
    y = draw_section(c, y, "📊 EXECUTION & METRICS TRACKING", prompts_execution, 3*inch, COLOR_PRIMARY)
    prompts_reflection = [
        "BREAKTHROUGH MOMENT: What surprised you most about today's social interaction?",
        "SKILL DEVELOPMENT: Which communication skill improved most today?",
        "TOMORROW'S PREPARATION: How will you build on today's progress tomorrow?",
        "How did today's communication growth impact your coding, networking, learning, or project launches?"
    ]
    draw_section(c, y, "🧠 DAILY GROWTH REFLECTION", prompts_reflection, 1.8*inch, COLOR_WISDOM)
    c.showPage()

# --- Weekly review: now includes TECH_SOCIAL_PROMPTS + action challenges ---
def draw_weekly_review_page(c, week):
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, f"Week {week} Performance Review")
    y = PAGE_HEIGHT - 2*inch
    metrics_prompts = [
        "CHALLENGE COMPLETION RATE: ___/7 days completed successfully",
        "AVERAGE COMFORT LEVEL: Day 1: ___  Day 7: ___ (Improvement: ___)",
        "SUCCESS METRIC ACHIEVEMENT: How well did you hit your weekly metric?",
        WEEKLY_METRICS.get(week, "No metric provided for this week."),
    ]
    y = draw_section(c, y, "📊 QUANTITATIVE RESULTS", metrics_prompts, 2.3*inch, COLOR_ACCENT, False)
    insights_prompts = [
        "BIGGEST BREAKTHROUGH: What was your most significant 'aha' moment?",
        "PATTERN RECOGNITION: What patterns did you notice in your social behavior?",
        "KNOWLEDGE APPLICATION: How did the pre-week learning help your practice?",
        "RELATIONSHIP IMPACT: Which relationship improved most this week?"
    ]
    y = draw_section(c, y, "💡 QUALITATIVE INSIGHTS", insights_prompts, 2.2*inch, COLOR_WISDOM, False)
    # Tech + social integration
    y = draw_section(c, y, "🤝 TECH & CAREER INTEGRATION", TECH_SOCIAL_PROMPTS, 1.8*inch, COLOR_PRIMARY)
    # Action challenges for the week
    action_prompts = [
        "WEEKLY ACTION CHALLENGES:",
        "• Pitch NEETPrepGPT to 3 new LinkedIn connections (copy your pitch below):",
        "• Ask for feedback on your code from one senior dev (who?):",
        "• Reach out to an expert for advice on product launch (who?):",
        "• Post one short insight on GitHub/LinkedIn and paste the link here:"
    ]
    draw_section(c, y, "🚀 WEEKLY ACTION CHALLENGES", action_prompts, 1.8*inch, COLOR_ENERGY)
    c.showPage()

# --- Final assembly: generate PDF and call new intro and badges pages ---
def _estimate_total_pages() -> int:
    intro = 1
    weeks = 7
    knowledge = weeks
    daily_pages = weeks * 7
    weekly_reviews = weeks
    final_assessment = 1
    badges = 1
    return intro + knowledge + daily_pages + weekly_reviews + final_assessment + badges

def create_progressive_social_mastery_journal(start_date: Optional[date] = None, filename: Optional[str] = None):
    output_file = filename or FILENAME
    c = None
    try:
        out_dir = os.path.dirname(os.path.abspath(output_file))
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
        c = canvas.Canvas(output_file, pagesize=A4)
        c.setTitle("Progressive Social Mastery Journal - Personalized")
        c.setAuthor(USER_PROFILE['name'])
        c.setSubject("Personalized social mastery + career integration journal")
        start_date = start_date or date.today()
        logger.info("Generating journal starting from %s -> %s", start_date.isoformat(), output_file)

        # New: personalized intro bio page
        draw_intro_bio_page(c)

        # System intro (kept brief)
        c.setFont("Helvetica-Bold", 24)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, "PROGRESSIVE SOCIAL MASTERY SYSTEM")
        c.setFont("Helvetica", 12)
        c.setFillColor(COLOR_TEXT_BODY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.5*inch, "A 7-week scaffolded system tailored for developers & founders")
        c.showPage()

        day_offset = 0
        for week in range(1, 8):
            # Knowledge module page
            module = KNOWLEDGE_MODULES.get(week, {})
            c.setFont("Helvetica-Bold", 20)
            c.setFillColor(COLOR_KNOWLEDGE)
            c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, f"WEEK {week} KNOWLEDGE MODULE")
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(COLOR_TEXT_HEADER)
            c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.9*inch, module.get('title', 'Module'))
            # Micro-learning snippet + growth mindset affirmation
            c.setFont("Helvetica", 10)
            c.drawString(MARGIN, PAGE_HEIGHT - 2.6*inch, "Micro-learning: Engineers with high EQ are more likely to lead projects — reflect how this applies to your role.")
            c.setFont("Helvetica-Oblique", 9)
            c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 2.6*inch, "Affirmation: Every challenge makes me a stronger leader.")
            c.showPage()

            # Daily pages
            for day in range(1, 8):
                current_date = start_date + timedelta(days=day_offset)
                date_str = current_date.strftime('%A, %B %d, %Y')
                draw_header(c, week, day, date_str)
                draw_daily_page(c, date_str, week, day)
                day_offset += 1

            # Weekly review
            draw_weekly_review_page(c, week)

        # Achievement badges page
        draw_achievement_badges_page(c)

        # Final assessment
        c.setFont("Helvetica-Bold", 24)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, "SOCIAL MASTERY ACHIEVED")
        c.setFont("Helvetica", 12)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.6*inch, "How will these skills accelerate your NEETPrepGPT and AI career goals?")
        c.showPage()

        c.save()
        logger.info("✅ Successfully created %s", output_file)
        logger.info("Estimated pages: %s", _estimate_total_pages())
    except Exception as exc:
        logger.exception("Failed to generate journal: %s", exc)
        if c:
            try:
                c.save()
            except Exception:
                pass
        raise

# --- CLI parsing ---
def _parse_args():
    parser = argparse.ArgumentParser(description="Generate a Personalized Progressive Social Mastery Journal PDF.")
    parser.add_argument("--start-date", type=str, default=None, help="Start date for Day 1 in YYYY-MM-DD format. Defaults to today.")
    parser.add_argument("--output", type=str, default=None, help="Output PDF filename (optional).")
    return parser.parse_args()

if __name__ == "__main__":
    args = _parse_args()
    parsed_date = None
    if args.start_date:
        try:
            parsed_date = datetime.strptime(args.start_date, "%Y-%m-%d").date()
        except ValueError:
            logger.error("Invalid --start-date format. Use YYYY-MM-DD. Falling back to today.")
            parsed_date = date.today()
    create_progressive_social_mastery_journal(start_date=parsed_date, filename=args.output)
