# Enhanced Progressive Social Mastery Engineering Journal
# (Original content preserved; improvements added: CLI, logging, metadata, validation, type hints)
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import slategray, lightgrey, black, HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date, timedelta, datetime
import os
import argparse
import logging
import textwrap
from typing import List, Optional

# --- Setup logging ---
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("SocialMasteryJournal")

# --- Enhanced Color Palette ---
COLOR_PRIMARY = HexColor('#007ACC')  # Professional blue
COLOR_ACCENT = HexColor('#4EC9B0')   # Success green
COLOR_WARN = HexColor('#F44747')     # Challenge red
COLOR_ENERGY = HexColor('#FFB347')   # Motivational orange
COLOR_WISDOM = HexColor('#9370DB')   # Insight purple
COLOR_KNOWLEDGE = HexColor('#FF6B6B')  # Knowledge module red
COLOR_BG_LIGHT = HexColor('#F3F3F3')
COLOR_TEXT_HEADER = HexColor('#2D2D2D')
COLOR_TEXT_BODY = HexColor('#3C3C3C')

# --- Configuration ---
FILENAME = "Progressive_Social_Mastery_Journal.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.6 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
STYLES = getSampleStyleSheet()

# --- Weekly Knowledge Modules ---
KNOWLEDGE_MODULES = {
    1: {
        "title": "Emotional Intelligence & Self-Awareness",
        "learning_resources": [
            "YouTube: 'Daniel Goleman: Emotional Intelligence' (TED Talk)",
            "Book: 'Emotional Intelligence 2.0' by Travis Bradberry",
            "Article: 'The Four Domains of Emotional Intelligence' (Harvard Business Review)",
            "Practice: 'Body Scan Meditation' for emotional awareness"
        ],
        "key_concepts": [
            "The 4 domains: Self-awareness, Self-management, Social awareness, Relationship management",
            "Recognizing emotional triggers and physical sensations",
            "The difference between emotions and reactions",
            "Mindful awareness vs. autopilot responses"
        ]
    },
    2: {
        "title": "Response Control & Emotional Regulation",
        "learning_resources": [
            "YouTube: 'Viktor Frankl: Between Stimulus and Response'",
            "Book: 'The Power of Now' by Eckhart Tolle (Chapter on reactive patterns)",
            "Article: 'The Science of Self-Control' (Psychology Today)",
            "Technique: 'STOP Method' (Stop, Take a breath, Observe, Proceed)"
        ],
        "key_concepts": [
            "The neurological 6-second rule for emotional hijacking",
            "Breathing techniques for immediate regulation",
            "Creating space between trigger and response",
            "Reframing thoughts to change emotional responses"
        ]
    },
    3: {
        "title": "Active Listening & Deep Communication",
        "learning_resources": [
            "YouTube: 'How to Really Listen' by Julian Treasure (TED Talk)",
            "Book: 'Just Listen' by Mark Goulston",
            "Article: 'The Levels of Listening' by Otto Scharmer",
            "Practice: 'Reflective Listening Exercises'"
        ],
        "key_concepts": [
            "The difference between hearing and listening",
            "Levels of listening: Internal, focused, empathic, generative",
            "Paraphrasing vs. summarizing techniques",
            "Nonverbal listening cues and body language"
        ]
    },
    4: {
        "title": "Clear Communication & Assertiveness",
        "learning_resources": [
            "YouTube: 'Nonviolent Communication' by Marshall Rosenberg",
            "Book: 'Crucial Conversations' by Kerry Patterson",
            "Article: 'I-Statements vs You-Statements' (Psychology Today)",
            "Framework: 'COIN Method' for difficult conversations"
        ],
        "key_concepts": [
            "The anatomy of I-statements: Observation, Feeling, Need, Request",
            "Separating facts from interpretations",
            "Assertive vs. aggressive vs. passive communication",
            "The art of making clear, specific requests"
        ]
    },
    5: {
        "title": "Empathy & Perspective-Taking",
        "learning_resources": [
            "YouTube: 'The Power of Empathy' by Brené Brown",
            "Book: 'Nonviolent Communication' by Marshall Rosenberg",
            "Article: 'Cognitive Empathy vs. Affective Empathy' (Greater Good Science Center)",
            "Exercise: 'Perspective-Taking Scenarios'"
        ],
        "key_concepts": [
            "Types of empathy: Cognitive, affective, compassionate",
            "The difference between empathy and sympathy",
            "Understanding needs beneath behaviors",
            "Cultural and individual differences in communication styles"
        ]
    },
    6: {
        "title": "Conflict Resolution & Difficult Conversations",
        "learning_resources": [
            "YouTube: 'Getting to Yes: Negotiating Agreement' by Roger Fisher",
            "Book: 'Difficult Conversations' by Douglas Stone",
            "Article: 'The Anatomy of Peace' concepts",
            "Framework: 'Nonviolent Communication in Conflict'"
        ],
        "key_concepts": [
            "Separating positions from interests",
            "De-escalation techniques and language patterns",
            "Finding win-win solutions",
            "Managing your own triggers during conflict"
        ]
    },
    7: {
        "title": "Relationship Building & Network Cultivation",
        "learning_resources": [
            "YouTube: 'How to Win Friends and Influence People' key concepts",
            "Book: 'Never Eat Alone' by Keith Ferrazzi",
            "Article: 'The Science of Strong Relationships' (Harvard Business Review)",
            "Practice: 'Gratitude and Appreciation Expressions'"
        ],
        "key_concepts": [
            "The principle of reciprocity in relationships",
            "Building trust through consistency and vulnerability",
            "The art of following up and staying connected",
            "Adding value before asking for favors"
        ]
    }
}

# --- Progressive Daily Challenges by Week ---
PROGRESSIVE_CHALLENGES = {
    1: [
        # Week 1: Building Social Awareness (Progressive Difficulty)
        "Day 1: Make conscious eye contact with 5 strangers and smile. Log their reactions.",
        "Day 2: Eye contact + smile with 3 people, say 'Hello/Good morning' to 2 others.",
        "Day 3: Ask 1 person a simple logistical question ('Excuse me, do you know the time?').",
        "Day 4: Give 1 genuine compliment to a service worker or acquaintance.",
        "Day 5: Ask a logistical question + make one follow-up comment/observation.",
        "Day 6: Have one complete 3-turn conversation (You speak, they respond, you respond).",
        "Day 7: Initiate 2 brief conversations with strangers in low-stakes environments."
    ],
    2: [
        # Week 2: Response Control (Progressive Difficulty)
        "Day 1: Use the 'tactical pause' (3 deep breaths) before responding to any minor irritation.",
        "Day 2: Catch yourself planning a response while someone is talking. Reset and listen.",
        "Day 3: When feeling triggered, name the emotion silently before responding.",
        "Day 4: Use the STOP technique in one potentially reactive situation.",
        "Day 5: Transform one complaint into a specific, actionable request.",
        "Day 6: Practice the 6-second rule when feeling strong emotion before responding.",
        "Day 7: Navigate one challenging conversation using all response control techniques."
    ],
    3: [
        # Week 3: Deep Listening (Progressive Difficulty)
        "Day 1: In one conversation, focus only on listening - no planning your response.",
        "Day 2: Ask 'What I heard is...' and confirm understanding in one conversation.",
        "Day 3: Ask 2 clarifying questions in a single conversation before giving your input.",
        "Day 4: Identify and reflect back one emotion you heard in someone's words.",
        "Day 5: Use active listening in a conversation where you disagree with the person.",
        "Day 6: Practice empathic listening - focus on understanding their feelings and needs.",
        "Day 7: Conduct one 'deep listening' conversation lasting at least 15 minutes."
    ],
    4: [
        # Week 4: Clear Communication (Progressive Difficulty)
        "Day 1: Replace one 'You' statement with an 'I' statement in conversation.",
        "Day 2: Make one request using the format: 'I would appreciate if...' instead of complaining.",
        "Day 3: Express a preference clearly without apologizing or over-explaining.",
        "Day 4: Share one vulnerable feeling using 'I feel... when... because...' format.",
        "Day 5: Set one clear boundary using assertive (not aggressive) language.",
        "Day 6: Ask for something you want directly and specifically.",
        "Day 7: Have one complete difficult conversation using I-statements and clear requests."
    ],
    5: [
        # Week 5: Empathy & Perspective-Taking (Progressive Difficulty)
        "Day 1: Ask someone 'How are you really doing?' and listen for the deeper answer.",
        "Day 2: Before responding in a disagreement, mentally summarize their perspective.",
        "Day 3: Ask one person about their dreams, goals, or what they're excited about.",
        "Day 4: Share something vulnerable about your own experience or struggles.",
        "Day 5: When someone is upset, focus on understanding their underlying need.",
        "Day 6: Practice seeing a current conflict entirely from the other person's viewpoint.",
        "Day 7: Have one conversation where you spend 80% of the time understanding them."
    ],
    6: [
        # Week 6: Conflict Resolution (Progressive Difficulty)
        "Day 1: Address one small issue directly instead of letting it build up.",
        "Day 2: Use collaborative language ('How can we...') in one disagreement.",
        "Day 3: Practice the COIN method for giving difficult feedback to someone.",
        "Day 4: Apologize for something specific without making excuses or deflecting.",
        "Day 5: Find one area of agreement in a conversation with someone you disagree with.",
        "Day 6: Turn one conflict into a problem-solving session by focusing on solutions.",
        "Day 7: Have the difficult conversation you've been avoiding using all conflict resolution tools."
    ],
    7: [
        # Week 7: Relationship Building (Progressive Difficulty)
        "Day 1: Send a specific appreciation message to someone who helped you recently.",
        "Day 2: Reach out to one person you haven't connected with in months.",
        "Day 3: Ask someone for advice on something you're genuinely curious about.",
        "Day 4: Invite someone to do an activity together (coffee, lunch, walk).",
        "Day 5: Introduce two people who should know each other.",
        "Day 6: Offer specific help to someone without them asking.",
        "Day 7: Plan follow-up actions to deepen 2-3 relationships from your week's connections."
    ]
}

# --- Concrete Success Metrics for Each Week ---
WEEKLY_METRICS = {
    1: "Binary Success Metric: Did you complete each day's specific challenge? Track: Yes/No + comfort level (1-10) + one thing learned",
    2: "Response Time Metric: How long between trigger and thoughtful response? Track: Seconds + technique used + outcome quality (1-10)",
    3: "Listening Quality Metric: In each conversation, did the other person say 'Yes, that's exactly right' to your paraphrase? Track: Yes/No + their satisfaction level",
    4: "Message Clarity Metric: Did your message land as intended? Track: Their response matched your intent (Yes/No) + follow-up questions needed",
    5: "Empathy Accuracy Metric: When you guessed someone's feeling/need, were you right? Track: Accurate guess (Yes/No) + their confirmation",
    6: "Resolution Success Metric: Did the conflict discussion end with agreed-upon next steps? Track: Mutual agreement reached (Yes/No) + relationship strengthened",
    7: "Connection Depth Metric: Did your interaction lead to concrete next steps? Track: Follow-up planned (Yes/No) + relationship investment level (1-10)"
}

# --- Personal Goal Templates ---
GOAL_TEMPLATES = {
    1: "My specific goal this week: Reduce social anxiety in [specific context] by practicing low-stakes social interactions to build confidence.",
    2: "My specific goal this week: Gain control over my [specific trigger] reactions, especially in [context like meetings/family/dating].",
    3: "My specific goal this week: Become a better listener in [specific relationship/context] to deepen understanding and connection.",
    4: "My specific goal this week: Learn to express my needs clearly in [specific situations] without being aggressive or passive.",
    5: "My specific goal this week: Build deeper empathy with [specific people/types of people] to strengthen those relationships.",
    6: "My specific goal this week: Address [specific conflict/tension] using structured approaches rather than avoidance.",
    7: "My specific goal this week: Strengthen my [professional/personal] network by reconnecting with [specific types of people]."
}

# --- Helper Functions ---
def _safe_get_module(week: int) -> dict:
    """Return the knowledge module for `week` or a safe default."""
    module = KNOWLEDGE_MODULES.get(week)
    if not module:
        logger.warning("Requested knowledge module for week %s not found. Using fallback.", week)
        module = {
            "title": "Unknown Module",
            "learning_resources": ["No resources available."],
            "key_concepts": ["No key concepts available."]
        }
    return module

def draw_header(c, week, day, date_str):
    """Enhanced header with progress tracking."""
    c.saveState()
    # Main title
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Week {week}: Progressive Social Lab")
    
    # Progress bar
    progress = (week - 1) / 7.0
    bar_width = 2 * inch
    c.setStrokeColor(COLOR_PRIMARY)
    c.setLineWidth(3)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.1*inch, MARGIN + bar_width, PAGE_HEIGHT - MARGIN - 0.1*inch)
    c.setStrokeColor(COLOR_ACCENT)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.1*inch, MARGIN + (bar_width * progress), PAGE_HEIGHT - MARGIN - 0.1*inch)
    
    # Date and day
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Day {day} | {date_str}")
    
    # Separator line
    c.setStrokeColor(lightgrey)
    c.setLineWidth(1)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.25*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 0.25*inch)
    c.restoreState()

def draw_knowledge_module_page(c, week):
    """Weekly knowledge module page with learning resources."""
    module = _safe_get_module(week)
    
    # Title
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(COLOR_KNOWLEDGE)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, f"WEEK {week} KNOWLEDGE MODULE")
    
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.8*inch, module["title"])
    
    y = PAGE_HEIGHT - 2.3*inch
    
    # Learning Time Investment
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_ENERGY)
    c.drawString(MARGIN, y, "⏰ TIME INVESTMENT: 30-60 minutes before starting Week " + str(week))
    y -= 0.4*inch
    
    # Learning Resources
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, y, "📚 RECOMMENDED LEARNING RESOURCES:")
    y -= 0.3*inch
    
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    for i, resource in enumerate(module["learning_resources"], 1):
        # wrap resource text if too long
        wrapped = textwrap.wrap(resource, width=90)
        for line_num, line in enumerate(wrapped):
            if line_num == 0:
                c.drawString(MARGIN + 0.2*inch, y, f"{i}. {line}")
            else:
                c.drawString(MARGIN + 0.45*inch, y, line)
            y -= 0.22*inch
    
    y -= 0.1*inch
    
    # Key Concepts
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, y, "🎯 KEY CONCEPTS TO MASTER:")
    y -= 0.3*inch
    
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    for concept in module["key_concepts"]:
        # Word wrap for long concepts
        wrapped = textwrap.wrap(concept, width=90)
        for i, line in enumerate(wrapped):
            prefix = "• " if i == 0 else "  "
            c.drawString(MARGIN + 0.2*inch, y, prefix + line)
            y -= 0.2*inch
    
    y -= 0.2*inch
    
    # Learning Completion Checklist
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_ACCENT)
    c.drawString(MARGIN, y, "✅ LEARNING COMPLETION CHECKLIST:")
    y -= 0.3*inch
    
    checklist_items = [
        "☐ Watched/read at least 2 recommended resources",
        "☐ Can explain the key concepts in my own words", 
        "☐ Identified how these concepts apply to my personal goals",
        "☐ Ready to practice these skills in real conversations"
    ]
    
    c.setFont("Helvetica", 10)
    for item in checklist_items:
        c.drawString(MARGIN + 0.2*inch, y, item)
        y -= 0.25*inch
    
    y -= 0.2*inch
    
    # Personal Application
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y, "🎯 MY PERSONAL APPLICATION GOAL:")
    y -= 0.3*inch
    
    # Goal template
    goal_template = GOAL_TEMPLATES.get(week, "Set a personal goal for this week.")
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    
    # Word wrap the goal template
    wrapped = textwrap.wrap(goal_template, width=110)
    for line in wrapped:
        c.drawString(MARGIN, y, line)
        y -= 0.22*inch
    
    y -= 0.3*inch
    
    # Space for personal goal
    c.setStrokeColor(lightgrey)
    c.setLineWidth(0.5)
    for i in range(4):
        c.line(MARGIN, y - (i * 0.2*inch), PAGE_WIDTH - MARGIN, y - (i * 0.2*inch))
    
    y -= 1*inch
    
    # Success metric
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(MARGIN, y, "📊 THIS WEEK'S SUCCESS METRIC:")
    y -= 0.3*inch
    
    metric = WEEKLY_METRICS.get(week, "No metric defined.")
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    
    # Word wrap the metric
    wrapped_metric = textwrap.wrap(metric, width=110)
    for line in wrapped_metric:
        c.drawString(MARGIN, y, line)
        y -= 0.2*inch
    
    c.showPage()

def draw_section(c, y_pos, title, content_prompts, height, color=COLOR_PRIMARY, include_lines=True):
    """Enhanced section with better formatting."""
    c.saveState()
    # Draw border with rounded corners
    c.setStrokeColor(color)
    c.setLineWidth(1.5)
    c.roundRect(MARGIN, y_pos - height, CONTENT_WIDTH, height, 0.05*inch)

    # Draw title bar
    c.setFillColor(color)
    c.roundRect(MARGIN, y_pos - 0.4*inch, CONTENT_WIDTH, 0.4*inch, 0.05*inch, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN + 0.15*inch, y_pos - 0.27*inch, title)

    # Draw content prompts with lines for writing
    c.setFont("Helvetica", 9)
    c.setFillColor(COLOR_TEXT_BODY)
    current_y = y_pos - 0.6*inch
    line_spacing = 0.25*inch
    
    for prompt in content_prompts:
        if prompt.strip():  # If there's content
            # wrap the prompt to multiple lines if long
            wrapped = textwrap.wrap(prompt, width=100)
            for i, wline in enumerate(wrapped):
                c.drawString(MARGIN + 0.15*inch, current_y, wline)
                current_y -= 0.18*inch
            if include_lines and not prompt.endswith(':'):
                # Draw lines for writing
                line_y = current_y - 0.05*inch
                c.setStrokeColor(lightgrey)
                c.setLineWidth(0.5)
                for i in range(2):
                    c.line(MARGIN + 0.2*inch, line_y - (i * 0.15*inch), PAGE_WIDTH - MARGIN - 0.2*inch, line_y - (i * 0.15*inch))
                current_y -= 0.35*inch
        else:
            current_y -= line_spacing

    c.restoreState()
    return y_pos - height - 0.2*inch

def draw_progressive_challenge_box(c, y_pos, week, day):
    """Progressive daily challenge with specific metrics."""
    # safe retrieval and bounds checking
    week_challenges = PROGRESSIVE_CHALLENGES.get(week)
    if not week_challenges:
        logger.warning("No challenges found for week %s. Using placeholder.", week)
        challenge = "No challenge available for this week."
    else:
        if 1 <= day <= len(week_challenges):
            challenge = week_challenges[day-1]
        else:
            logger.warning("Day %s is out of range for week %s. Using placeholder.", day, week)
            challenge = "No challenge available for this day."

    c.saveState()
    # Background
    c.setFillColor(COLOR_ACCENT)
    c.setStrokeColor(COLOR_ACCENT)
    c.roundRect(MARGIN, y_pos - 1.5*inch, CONTENT_WIDTH, 1.5*inch, 0.1*inch, fill=1, stroke=1)
    
    # Title
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.3*inch, f"🎯 DAY {day} PROGRESSIVE CHALLENGE")
    
    # Challenge description (wrapped)
    c.setFont("Helvetica-Bold", 10)
    wrapped_ch = textwrap.wrap(challenge, width=110)
    desc_y = y_pos - 0.6*inch
    for line in wrapped_ch:
        c.drawString(MARGIN + 0.2*inch, desc_y, line)
        desc_y -= 0.2*inch
    
    # Metrics tracking
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.9*inch, "SUCCESS METRICS:")
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.1*inch, "☐ Challenge completed (Yes/No)   ☐ Comfort level: ___/10")
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.3*inch, "☐ Key learning: ________________________________")
    
    c.restoreState()
    return y_pos - 1.7*inch

def draw_daily_page(c, date_str, week, day):
    """Enhanced daily page with progressive challenges and concrete metrics."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    
    # Progressive challenge
    y = draw_progressive_challenge_box(c, y, week, day)
    
    # Execution tracking
    prompts_execution = [
        "PRE-CHALLENGE MINDSET: How are you feeling before attempting this challenge?",
        "",
        "EXECUTION DETAILS: Describe exactly what happened when you tried the challenge:",
        "",
        "COMFORT LEVEL: Rate your comfort (1=terrifying, 10=completely natural): ___/10",
        "",
        "SUCCESS METRICS: Did you achieve the specific goal? ☐ Yes ☐ Partial ☐ No",
        "",
        "WHAT WORKED: What specific technique or approach was most helpful?",
        "",
        "WHAT TO ADJUST: What will you do differently in similar situations?"
    ]
    y = draw_section(c, y, "📊 EXECUTION & METRICS TRACKING", prompts_execution, 3*inch, COLOR_PRIMARY)
    
    # Daily reflection
    prompts_reflection = [
        "BREAKTHROUGH MOMENT: What surprised you most about today's social interaction?",
        "",
        "SKILL DEVELOPMENT: Which communication skill improved most today?",
        "",
        "TOMORROW'S PREPARATION: How will you build on today's progress tomorrow?"
    ]
    draw_section(c, y, "🧠 DAILY GROWTH REFLECTION", prompts_reflection, 1.8*inch, COLOR_WISDOM)
    
    c.showPage()

def draw_weekly_review_page(c, week):
    """Enhanced weekly review with concrete metrics and next week planning."""
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, f"Week {week} Performance Review")
    
    y = PAGE_HEIGHT - 2*inch
    
    # Quantitative results
    metrics_prompts = [
        "CHALLENGE COMPLETION RATE: ___/7 days completed successfully",
        "",
        "AVERAGE COMFORT LEVEL: Day 1: ___  Day 7: ___ (Improvement: ___)",
        "",
        "SUCCESS METRIC ACHIEVEMENT: How well did you hit your weekly metric?",
        WEEKLY_METRICS.get(week, "No metric provided for this week."),
        "",
        "MOST MEASURABLE IMPROVEMENT: What concrete change can you document?"
    ]
    y = draw_section(c, y, "📊 QUANTITATIVE RESULTS", metrics_prompts, 2.3*inch, COLOR_ACCENT, False)
    
    # Qualitative insights
    insights_prompts = [
        "BIGGEST BREAKTHROUGH: What was your most significant 'aha' moment?",
        "",
        "PATTERN RECOGNITION: What patterns did you notice in your social behavior?",
        "",
        "KNOWLEDGE APPLICATION: How did the pre-week learning help your practice?",
        "",
        "RELATIONSHIP IMPACT: Which relationship improved most this week?"
    ]
    y = draw_section(c, y, "💡 QUALITATIVE INSIGHTS", insights_prompts, 2.2*inch, COLOR_WISDOM, False)
    
    # Next week preparation
    if week < 7:
        prep_prompts = [
            f"WEEK {week+1} GOAL CUSTOMIZATION: How will you personalize next week's challenges?",
            "",
            f"KNOWLEDGE MODULE PLAN: When will you complete Week {week+1}'s learning?",
            "",
            "DIFFICULTY ADJUSTMENT: Should next week be more/less challenging? Why?",
            "",
            "ACCOUNTABILITY PLAN: How will you ensure consistent practice next week?"
        ]
        draw_section(c, y, f"🎯 WEEK {week+1} PREPARATION", prep_prompts, 2.2*inch, COLOR_ENERGY, False)
    else:
        # Final week - mastery assessment
        mastery_prompts = [
            "TRANSFORMATION SUMMARY: How have you changed since Week 1?",
            "",
            "SKILL MASTERY LEVEL: Rate each skill (1-10):",
            "Self-awareness: ___ Response control: ___ Listening: ___ Clear communication: ___",
            "Empathy: ___ Conflict resolution: ___ Relationship building: ___",
            "",
            "ONGOING PRACTICE PLAN: How will you maintain and continue growing these skills?"
        ]
        draw_section(c, y, "🏆 MASTERY ASSESSMENT", mastery_prompts, 2.2*inch, COLOR_ENERGY, False)
    
    c.showPage()

def _estimate_total_pages() -> int:
    """Estimate total pages in the generated journal for informational/logging purposes."""
    # 1 intro + (for each week: 1 knowledge + 7 daily pages (each has header + daily) + 1 weekly review) + final assessment
    intro = 1
    weeks = 7
    knowledge = weeks
    daily_pages = weeks * 7
    weekly_reviews = weeks
    final_assessment = 1
    total = intro + knowledge + daily_pages + weekly_reviews + final_assessment
    return total

def create_progressive_social_mastery_journal(start_date: Optional[date] = None, filename: Optional[str] = None):
    """Generate the complete progressive social mastery journal.

    Args:
        start_date: Optional[date] - the date for Day 1. If None, uses today's date.
        filename: Optional[str] - the output filename. If None, uses FILENAME global.
    """
    output_file = filename or FILENAME
    c = None
    try:
        # Ensure output directory exists
        out_dir = os.path.dirname(os.path.abspath(output_file))
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
            logger.debug("Created output directory: %s", out_dir)

        c = canvas.Canvas(output_file, pagesize=A4)

        # PDF metadata for better file properties
        c.setTitle("Progressive Social Mastery Journal")
        c.setAuthor("Progressive Social Mastery System")
        c.setSubject("A 7-week progressive program to transform communication skills")
        c.setCreator("Progressive Social Mastery Generator Script")

        start_date = start_date or date.today()
        if isinstance(start_date, str):
            # attempt parse if someone passed a string accidentally
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            except Exception:
                logger.warning("start_date string provided but could not parse, using today instead.")
                start_date = date.today()

        logger.info("Generating journal starting from %s -> %s", start_date.isoformat(), output_file)
        logger.info("Estimated total pages: %s", _estimate_total_pages())

        # Enhanced intro page
        c.setFont("Helvetica-Bold", 28)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, "PROGRESSIVE SOCIAL")
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.4*inch, "MASTERY SYSTEM")
        
        c.setFont("Helvetica", 16)
        c.setFillColor(COLOR_TEXT_HEADER)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.9*inch, "Engineering Approach to Communication Excellence")
        
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 3.4*inch, "From Introvert to Influential Communicator")
        
        # System overview
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(COLOR_ENERGY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 4*inch, "🔧 SYSTEM FEATURES:")
        
        features_text = [
            "✅ Progressive Difficulty: Each week builds on the last with scaffolded challenges",
            "✅ Knowledge Modules: Learn the theory before practicing the skills", 
            "✅ Concrete Metrics: Measurable success criteria for every challenge",
            "✅ Personal Goals: Customize each week to your specific social contexts",
            "✅ Daily Tracking: Detailed reflection and progress monitoring",
            "✅ Evidence-Based: Rooted in psychology, neuroscience, and communication research"
        ]
        
        y_pos = PAGE_HEIGHT - 4.4*inch
        c.setFont("Helvetica", 11)
        c.setFillColor(COLOR_TEXT_BODY)
        for feature in features_text:
            c.drawCentredString(PAGE_WIDTH/2, y_pos, feature)
            y_pos -= 0.25*inch
        
        # Mission statement
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(COLOR_WISDOM)
        c.drawCentredString(PAGE_WIDTH/2, y_pos - 0.3*inch, "🚀 YOUR TRANSFORMATION COMMITMENT:")
        
        mission_text = [
            "This system will transform you from socially anxious to socially confident.",
            "You will master the engineering principles of human connection.",
            "Every interaction becomes data. Every challenge builds competence.",
            "In 7 weeks, you will have the communication skills to accelerate your career.",
            "",
            "Commit fully. Follow the system. Become unstoppable."
        ]
        
        y_mission = y_pos - 0.7*inch
        c.setFont("Helvetica", 11)
        c.setFillColor(COLOR_TEXT_BODY)
        for line in mission_text:
            c.drawCentredString(PAGE_WIDTH/2, y_mission, line)
            y_mission -= 0.22*inch
        
        c.showPage()
        
        # Generate knowledge modules and daily pages
        day_offset = 0
        for week in range(1, 8):
            # Knowledge module page at start of each week
            draw_knowledge_module_page(c, week)
            
            # Daily pages for the week
            for day in range(1, 8):  # 7 days per week
                current_date = start_date + timedelta(days=day_offset)
                date_str = current_date.strftime('%A, %B %d, %Y')
                
                draw_header(c, week, day, date_str)
                draw_daily_page(c, date_str, week, day)
                
                day_offset += 1
            
            # Weekly review page
            draw_weekly_review_page(c, week)
        
        # Final transformation assessment
        c.setFont("Helvetica-Bold", 24)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, "SOCIAL MASTERY")
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.4*inch, "ACHIEVED")
        
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 3*inch, "Transformation Complete")
        
        # Final assessment prompts
        y = PAGE_HEIGHT - 3.5*inch
        final_prompts = [
            "BEFORE vs. AFTER ASSESSMENT:",
            "",
            "Week 1 Comfort Level: ___/10    Week 7 Comfort Level: ___/10",
            "",
            "Most Significant Transformation:",
            "",
            "New Social Superpowers Acquired:",
            "1. ________________________________",
            "2. ________________________________", 
            "3. ________________________________",
            "",
            "Career Impact: How will these skills accelerate your AI/health-tech goals?",
            "",
            "Ongoing Practice Plan: How will you maintain and expand these abilities?",
            ""
        ]
        
        c.setFont("Helvetica", 12)
        c.setFillColor(COLOR_TEXT_BODY)
        for prompt in final_prompts:
            if prompt.strip():
                if prompt.endswith(':'):
                    c.setFont("Helvetica-Bold", 12)
                    c.setFillColor(COLOR_TEXT_HEADER)
                else:
                    c.setFont("Helvetica", 12)
                    c.setFillColor(COLOR_TEXT_BODY)
                c.drawCentredString(PAGE_WIDTH/2, y, prompt)
            y -= 0.25*inch
        
        # Success celebration
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(COLOR_ENERGY)
        c.drawCentredString(PAGE_WIDTH/2, y - 0.5*inch, "🎉 CONGRATULATIONS! 🎉")
        c.setFont("Helvetica", 12)
        c.setFillColor(COLOR_TEXT_BODY)
        c.drawCentredString(PAGE_WIDTH/2, y - 0.8*inch, "You now possess the systematic communication skills")
        c.drawCentredString(PAGE_WIDTH/2, y - 1.1*inch, "to build any relationship and influence any outcome.")
        c.drawCentredString(PAGE_WIDTH/2, y - 1.4*inch, "Your AI/health-tech career will benefit immeasurably.")
        
        c.save()
        logger.info("✅ Successfully created %s", output_file)
        logger.info("📊 Generated comprehensive progressive social mastery system:")
        logger.info("   • 7 Knowledge Module pages (30-60 min learning each)")
        logger.info("   • 49 Daily Practice pages (progressive difficulty)")
        logger.info("   • 7 Weekly Review pages (quantitative + qualitative)")
        logger.info("   • 2 Assessment pages (intro + final transformation)")
        logger.info("   • Total (estimated): %s pages", _estimate_total_pages())
        logger.info("💡 Key improvements enabled:")
        logger.info("   ✅ CLI options (--start-date, --output)")
        logger.info("   ✅ PDF metadata (title, author, subject)")
        logger.info("   ✅ Safe lookups and bounds checking for weeks/days")
        logger.info("   ✅ Logging for visibility and simple error handling")
    except Exception as exc:
        logger.exception("Failed to generate journal: %s", exc)
        if c:
            try:
                c.save()
            except Exception:
                pass
        raise
    finally:
        # no-op; canvas already saved or attempted to save
        pass

def _parse_args():
    parser = argparse.ArgumentParser(description="Generate a Progressive Social Mastery Journal PDF.")
    parser.add_argument("--start-date", type=str, default=None,
                        help="Start date for Day 1 in YYYY-MM-DD format. Defaults to today.")
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
    try:
        create_progressive_social_mastery_journal(start_date=parsed_date, filename=args.output)
    except Exception as e:
        logger.error("Generation failed: %s", e)
