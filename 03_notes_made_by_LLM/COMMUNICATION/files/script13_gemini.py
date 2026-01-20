# Enhanced Progressive Social Mastery Engineering Journal
# (Original content preserved; improvements added: CLI, logging, metadata, validation, type hints)
# Version 3.1: Bugfix for NameError (slategray), personalized for Arun Yadav's AI/Developer Career Path

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

# --- Personalization Profile ---
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

# --- Enhanced Color Palette ---
COLOR_PRIMARY = HexColor('#007ACC')  # Professional blue
COLOR_ACCENT = HexColor('#4EC9B0')   # Success green
COLOR_WARN = HexColor('#F44747')     # Challenge red
COLOR_ENERGY = HexColor('#FFB347')   # Motivational orange
COLOR_WISDOM = HexColor('#9370DB')   # Insight purple
COLOR_KNOWLEDGE = HexColor('#FF6B6B')  # Knowledge module red
COLOR_BG_LIGHT = HexColor('#F3F3F3')
COLOR_BG_DARKER = HexColor('#EAEAEA')
COLOR_TEXT_HEADER = HexColor('#2D2D2D')
COLOR_TEXT_BODY = HexColor('#3C3C3C')

# --- NEW: Font and Size Configuration ---
FONT_BOLD = "Helvetica-Bold"
FONT_NORMAL = "Helvetica"
FONT_SIZE_XL = 20
FONT_SIZE_L = 16
FONT_SIZE_M_BOLD = 13
FONT_SIZE_M = 12
FONT_SIZE_S_BOLD = 11
FONT_SIZE_S = 10
FONT_SIZE_XS = 9

# --- Configuration ---
FILENAME = "Arun_Yadav_Social_Mastery_Journal.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.6 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
STYLES = getSampleStyleSheet()

# --- Weekly Knowledge Modules (Original content) ---
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

# --- Progressive Daily Challenges by Week (with Developer-focused additions) ---
PROGRESSIVE_CHALLENGES = {
    1: [
        "Day 1: Make conscious eye contact with 5 strangers and smile. Log their reactions.",
        "Day 2: Eye contact + smile with 3 people, say 'Hello/Good morning' to 2 others.",
        "Day 3: Ask 1 person a simple logistical question ('Excuse me, do you know the time?').",
        "Day 4: Give 1 genuine compliment to a service worker or acquaintance.",
        "Day 5: Ask a logistical question + make one follow-up comment/observation.",
        "Day 6: Have one complete 3-turn conversation (You speak, they respond, you respond).",
        "Day 7: Initiate 2 brief conversations in low-stakes environments (e.g., coffee shop)."
    ],
    2: [
        "Day 1: Use the 'tactical pause' (3 deep breaths) before responding to any minor irritation.",
        "Day 2: Catch yourself planning a response while someone is talking. Reset and listen.",
        "Day 3: When feeling triggered, name the emotion silently before responding.",
        "Day 4: Use the STOP technique in one potentially reactive situation.",
        "Day 5: Transform one complaint into a specific, actionable request.",
        "Day 6: Practice the 6-second rule when receiving difficult code review feedback.",
        "Day 7: Navigate one challenging conversation using all response control techniques."
    ],
    3: [
        "Day 1: In one conversation, focus only on listening - no planning your response.",
        "Day 2: Ask 'What I heard is...' to confirm understanding in a technical discussion.",
        "Day 3: Ask 2 clarifying questions in a conversation before giving your input.",
        "Day 4: Identify and reflect back one emotion you heard in someone's words.",
        "Day 5: Use active listening in a conversation where you disagree with a technical approach.",
        "Day 6: Practice empathic listening - focus on understanding a user's problem, not just the feature request.",
        "Day 7: Ask for feedback on your code from a senior dev and listen without defending."
    ],
    4: [
        "Day 1: Replace one 'You' statement with an 'I' statement in a team chat (e.g., Slack/Discord).",
        "Day 2: Make one request using the format: 'I would appreciate if...' instead of complaining.",
        "Day 3: Express a technical opinion clearly without apologizing or over-explaining.",
        "Day 4: Share a learning challenge using 'I feel... when... because...' format.",
        "Day 5: Set one clear boundary regarding your focus/work time.",
        "Day 6: Ask for something you want directly and specifically (e.g., a specific type of mentorship).",
        "Day 7: Have one difficult conversation about project scope using I-statements."
    ],
    5: [
        "Day 1: Ask a colleague 'How are you really doing?' and listen for the deeper answer.",
        "Day 2: Before responding to a bug report, mentally summarize the user's frustration.",
        "Day 3: Ask one person in your network about their career goals and what they're excited about.",
        "Day 4: Share something vulnerable about your own experience or struggles with a coding problem.",
        "Day 5: When someone is upset about a project delay, focus on understanding their underlying need.",
        "Day 6: Practice seeing a current technical debate entirely from the other person's viewpoint.",
        "Day 7: Have one conversation where you spend 80% of the time understanding their technical perspective."
    ],
    6: [
        "Day 1: Address one small issue in a collaboration directly instead of letting it build up.",
        "Day 2: Use collaborative language ('How can we solve this?') in one disagreement.",
        "Day 3: Practice the COIN method for giving difficult feedback on a pull request.",
        "Day 4: Apologize for a mistake (e.g., breaking the build) without making excuses.",
        "Day 5: Find one area of agreement in a conversation with someone you disagree with.",
        "Day 6: Turn one conflict into a problem-solving session by focusing on solutions.",
        "Day 7: Reach out to an expert for advice on your NEETPrepGPT product launch strategy."
    ],
    7: [
        "Day 1: Send a specific appreciation message to someone who helped you with a technical problem.",
        "Day 2: Reach out to one person on LinkedIn you haven't connected with in months.",
        "Day 3: Ask someone senior for advice on a career or technical challenge.",
        "Day 4: Invite someone from your network for a virtual coffee chat.",
        "Day 5: Introduce two people in your network who could benefit from knowing each other.",
        "Day 6: Offer specific help to someone in your developer community without them asking.",
        "Day 7: Pitch your AI project (NEETPrepGPT) to 2 new LinkedIn connections."
    ]
}

# --- Concrete Success Metrics for Each Week (Original content) ---
WEEKLY_METRICS = {
    1: "Binary Success Metric: Did you complete each day's specific challenge? Track: Yes/No + comfort level (1-10) + one thing learned",
    2: "Response Time Metric: How long between trigger and thoughtful response? Track: Seconds + technique used + outcome quality (1-10)",
    3: "Listening Quality Metric: In each conversation, did the other person say 'Yes, that's exactly right' to your paraphrase? Track: Yes/No + their satisfaction level",
    4: "Message Clarity Metric: Did your message land as intended? Track: Their response matched your intent (Yes/No) + follow-up questions needed",
    5: "Empathy Accuracy Metric: When you guessed someone's feeling/need, were you right? Track: Accurate guess (Yes/No) + their confirmation",
    6: "Resolution Success Metric: Did the conflict discussion end with agreed-upon next steps? Track: Mutual agreement reached (Yes/No) + relationship strengthened",
    7: "Connection Depth Metric: Did your interaction lead to concrete next steps? Track: Follow-up planned (Yes/No) + relationship investment level (1-10)"
}

# --- Personal Goal Templates (Original content) ---
GOAL_TEMPLATES = {
    1: "My specific goal this week: Reduce social anxiety in [specific context, e.g., team meetings] by practicing low-stakes interactions to build confidence.",
    2: "My specific goal this week: Gain control over my [specific trigger, e.g., critical feedback] reactions, especially in [context like code reviews/family].",
    3: "My specific goal this week: Become a better listener in [specific relationship/context, e.g., with my mentor] to deepen understanding and connection.",
    4: "My specific goal this week: Learn to express my technical opinions clearly in [specific situations, e.g., planning sessions] without being aggressive or passive.",
    5: "My specific goal this week: Build deeper empathy with [specific people, e.g., end-users of my project] to strengthen product quality.",
    6: "My specific goal this week: Address [specific conflict/tension, e.g., a disagreement on architecture] using structured approaches rather than avoidance.",
    7: "My specific goal this week: Strengthen my [professional/personal] network by reconnecting with [specific types of people, e.g., other AI developers]."
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

def draw_intro_bio_page(c):
    """Draws the personalized introductory bio page."""
    c.setFont(FONT_BOLD, FONT_SIZE_XL)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.2*inch, "Personalized Social Mastery Journal")
    
    c.setFont(FONT_NORMAL, FONT_SIZE_M_BOLD)
    c.setFillColor(COLOR_TEXT_HEADER)
    y = PAGE_HEIGHT - 1.8*inch
    c.drawString(MARGIN, y, f"Name: {USER_PROFILE['name']}")
    c.drawString(MARGIN, y-0.3*inch, f"Location: {USER_PROFILE['location']}")
    c.drawString(MARGIN, y-0.6*inch, f"Main Project: {USER_PROFILE['main_project']}")
    c.drawString(MARGIN, y-0.9*inch, f"Career Goal: {USER_PROFILE['career_goal']}")
    y -= 1.3 * inch
    c.drawString(MARGIN, y, "Learning Focus:")
    y -= 0.1 * inch
    
    c.setFont(FONT_NORMAL, FONT_SIZE_S_BOLD)
    c.setFillColor(COLOR_TEXT_BODY)
    for i, topic in enumerate(USER_PROFILE["learning_focus"], 1):
        y -= 0.25*inch
        c.drawString(MARGIN + 0.3*inch, y, f"• {topic}")

    y -= 1.0 * inch
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_WISDOM)
    c.drawCentredString(PAGE_WIDTH/2, y, "This journal is crafted for you—a growth-minded developer & founder.")
    c.drawCentredString(PAGE_WIDTH/2, y-0.25*inch, "Use it to engineer the communication skills that will multiply your technical impact.")
    c.showPage()

def draw_header(c, week, day, date_str):
    """Enhanced header with progress tracking."""
    c.saveState()
    # Main title
    c.setFont(FONT_BOLD, FONT_SIZE_XL)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Week {week}: Progressive Social Lab")
    
    # Progress bar
    progress = ((week - 1) * 7 + (day -1)) / 49.0
    bar_width = 2.5 * inch
    c.setStrokeColor(lightgrey)
    c.setLineWidth(4)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.1*inch, MARGIN + bar_width, PAGE_HEIGHT - MARGIN - 0.1*inch)
    c.setStrokeColor(COLOR_ACCENT)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.1*inch, MARGIN + (bar_width * progress), PAGE_HEIGHT - MARGIN - 0.1*inch)
    
    # Date and day
    c.setFont(FONT_NORMAL, FONT_SIZE_S_BOLD)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Day {(week-1)*7 + day} of 49 | {date_str}")
    
    # Separator line
    c.setStrokeColor(lightgrey)
    c.setLineWidth(1)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.25*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 0.25*inch)
    c.restoreState()

def draw_knowledge_module_page(c, week):
    """Weekly knowledge module page with learning resources."""
    module = _safe_get_module(week)
    
    c.setFont(FONT_BOLD, 22)
    c.setFillColor(COLOR_KNOWLEDGE)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, f"WEEK {week} KNOWLEDGE MODULE")
    
    c.setFont(FONT_BOLD, FONT_SIZE_L)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.8*inch, module["title"])
    
    y = PAGE_HEIGHT - 2.3*inch
    
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_ENERGY)
    c.drawString(MARGIN, y, "⏰ TIME INVESTMENT: 30-60 minutes before starting Week " + str(week))
    y -= 0.4*inch
    
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, y, "📚 RECOMMENDED LEARNING RESOURCES:")
    y -= 0.3*inch
    
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    c.setFillColor(COLOR_TEXT_BODY)
    for i, resource in enumerate(module["learning_resources"], 1):
        wrapped = textwrap.wrap(resource, width=90)
        for line_num, line in enumerate(wrapped):
            if line_num == 0:
                c.drawString(MARGIN + 0.2*inch, y, f"{i}. {line}")
            else:
                c.drawString(MARGIN + 0.45*inch, y, line)
            y -= 0.22*inch
    
    y -= 0.1*inch
    
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, y, "🎯 KEY CONCEPTS TO MASTER:")
    y -= 0.3*inch
    
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    c.setFillColor(COLOR_TEXT_BODY)
    for concept in module["key_concepts"]:
        wrapped = textwrap.wrap(concept, width=90)
        for i, line in enumerate(wrapped):
            prefix = "• " if i == 0 else "  "
            c.drawString(MARGIN + 0.2*inch, y, prefix + line)
            y -= 0.2*inch
    
    y -= 0.2*inch
    
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_ACCENT)
    c.drawString(MARGIN, y, "✅ LEARNING COMPLETION CHECKLIST:")
    y -= 0.3*inch
    
    checklist_items = [
        "☐ Watched/read at least 2 recommended resources",
        "☐ Can explain the key concepts in my own words", 
        "☐ Identified how these concepts apply to my personal goals",
        "☐ Ready to practice these skills in real conversations"
    ]
    
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    for item in checklist_items:
        c.drawString(MARGIN + 0.2*inch, y, item)
        y -= 0.25*inch
    
    y -= 0.2*inch
    
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y, "🎯 MY PERSONAL APPLICATION GOAL:")
    y -= 0.3*inch
    
    goal_template = GOAL_TEMPLATES.get(week, "Set a personal goal for this week.")
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    c.setFillColor(COLOR_TEXT_BODY)
    
    wrapped = textwrap.wrap(goal_template, width=110)
    for line in wrapped:
        c.drawString(MARGIN, y, line)
        y -= 0.22*inch
    
    y -= 0.3*inch
    
    c.setStrokeColor(lightgrey)
    c.setLineWidth(0.5)
    for i in range(4):
        c.line(MARGIN, y - (i * 0.2*inch), PAGE_WIDTH - MARGIN, y - (i * 0.2*inch))
    
    y -= 1*inch
    
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(MARGIN, y, "📊 THIS WEEK'S SUCCESS METRIC:")
    y -= 0.3*inch
    
    metric = WEEKLY_METRICS.get(week, "No metric defined.")
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    c.setFillColor(COLOR_TEXT_BODY)
    
    wrapped_metric = textwrap.wrap(metric, width=110)
    for line in wrapped_metric:
        c.drawString(MARGIN, y, line)
        y -= 0.2*inch
    
    c.showPage()

def draw_section(c, y_pos, title, content_prompts, height, color=COLOR_PRIMARY, include_lines=True):
    """Enhanced section with better formatting."""
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(1.5)
    c.roundRect(MARGIN, y_pos - height, CONTENT_WIDTH, height, 0.05*inch)

    c.setFillColor(color)
    c.roundRect(MARGIN, y_pos - 0.4*inch, CONTENT_WIDTH, 0.4*inch, 0.05*inch, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont(FONT_BOLD, FONT_SIZE_S_BOLD)
    c.drawString(MARGIN + 0.15*inch, y_pos - 0.27*inch, title)

    c.setFont(FONT_NORMAL, FONT_SIZE_XS)
    c.setFillColor(COLOR_TEXT_BODY)
    current_y = y_pos - 0.6*inch
    line_spacing = 0.25*inch
    
    for prompt in content_prompts:
        if prompt.strip():
            wrapped = textwrap.wrap(prompt, width=100)
            for i, wline in enumerate(wrapped):
                c.drawString(MARGIN + 0.15*inch, current_y, wline)
                current_y -= 0.18*inch
            if include_lines and not prompt.endswith(':'):
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
    """(ENHANCED) Progressive daily challenge with specific metrics and better design."""
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

    height = 1.6*inch
    c.saveState()
    # Background
    c.setFillColor(COLOR_BG_LIGHT)
    c.setStrokeColor(COLOR_ACCENT)
    c.setLineWidth(1.5)
    c.roundRect(MARGIN, y_pos - height, CONTENT_WIDTH, height, 0.1*inch, fill=1, stroke=1)
    
    # Title
    c.setFillColor(COLOR_TEXT_HEADER)
    c.setFont(FONT_BOLD, FONT_SIZE_M_BOLD)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.35*inch, f"🎯 TODAY'S MISSION: DAY {day} CHALLENGE")
    
    # Challenge Text
    c.setFont(FONT_BOLD, FONT_SIZE_S_BOLD)
    c.setFillColor(COLOR_TEXT_BODY)
    wrapped_ch = textwrap.wrap(challenge, width=100)
    desc_y = y_pos - 0.65*inch
    for line in wrapped_ch:
        c.drawString(MARGIN + 0.2*inch, desc_y, line)
        desc_y -= 0.22*inch
    
    # Metrics Area
    c.setFont(FONT_BOLD, FONT_SIZE_XS)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(MARGIN + 0.2*inch, y_pos - 1.2*inch, "SUCCESS METRICS:")
    
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.4*inch, "☐ Mission Completed (Y/N)   |   ☐ Comfort Level: ___/10   |   ☐ Outcome Quality: ___/10")
    
    c.restoreState()
    return y_pos - height - 0.15*inch

def draw_lined_notes_section(c, y_pos, title, prompts, num_lines_per_prompt, height, color):
    """(NEW) A generic section for prompts followed by lines for notes."""
    c.saveState()
    
    # Bounding box
    c.setStrokeColor(color)
    c.setLineWidth(1)
    c.roundRect(MARGIN, y_pos - height, CONTENT_WIDTH, height, 0.05 * inch, fill=0)

    # Header
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(color)
    c.drawString(MARGIN + 0.15*inch, y_pos - 0.3*inch, title)
    
    # Prompts and lines
    current_y = y_pos - 0.55*inch
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    c.setFillColor(COLOR_TEXT_BODY)
    
    for prompt in prompts:
        wrapped_prompt = textwrap.wrap(prompt, width=100)
        for line in wrapped_prompt:
            c.drawString(MARGIN + 0.15*inch, current_y, line)
            current_y -= 0.2*inch
        
        current_y -= 0.05*inch # space before lines
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.5)
        for i in range(num_lines_per_prompt):
            line_y = current_y - (i * 0.2*inch)
            c.line(MARGIN + 0.2*inch, line_y, PAGE_WIDTH - MARGIN - 0.2*inch, line_y)
        
        current_y -= (num_lines_per_prompt * 0.2*inch) + 0.1*inch
    
    c.restoreState()
    return y_pos - height - 0.15*inch

def draw_daily_page(c, date_str, week, day):
    """(COMPLETELY REDESIGNED) Daily page with more sections for a richer experience."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    
    # 1. Today's Mission Box
    y = draw_progressive_challenge_box(c, y, week, day)
    
    # 2. Morning Mindset & Intention
    height_mindset = 1.3*inch
    c.saveState()
    c.setFillColor(COLOR_BG_DARKER)
    c.roundRect(MARGIN, y - height_mindset, CONTENT_WIDTH, height_mindset, 0.05*inch, fill=1, stroke=0)
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_ENERGY)
    c.drawString(MARGIN + 0.15*inch, y - 0.3*inch, "☀️ MORNING MINDSET & INTENTION")
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    c.setFillColor(COLOR_TEXT_BODY)
    mindset_prompts = [
        "☐ Reviewed this week's Knowledge Module concepts.",
        "☐ Set a clear intention for today's social interactions.",
        "☐ Visualized successfully completing today's mission.",
        "My primary goal today, besides the challenge, is to:"
    ]
    y_mindset = y - 0.55*inch
    for prompt in mindset_prompts:
        c.drawString(MARGIN + 0.15*inch, y_mindset, prompt)
        y_mindset -= 0.2*inch
    c.setStrokeColor(slategray) # <<< THIS IS THE CORRECTED LINE
    c.line(MARGIN + 0.15*inch, y_mindset + 0.15*inch, PAGE_WIDTH - MARGIN - 0.2*inch, y_mindset + 0.15*inch)
    c.restoreState()
    y -= (height_mindset + 0.15*inch)
    
    # 3. Execution Log & Metrics
    prompts_execution = [
        "PRE-CHALLENGE MINDSET: How did you feel before attempting the mission?",
        "EXECUTION LOG: Describe exactly what happened, step-by-step. Who, what, where, when?",
        "OBSTACLES & SUCCESSES: What went better than expected? What was the hardest part?"
    ]
    y = draw_lined_notes_section(c, y, "📊 EXECUTION LOG & METRICS", prompts_execution, 2, 2.5*inch, COLOR_PRIMARY)

    # 4. Evening Reflection & Insights
    prompts_reflection = [
        "KEY INSIGHT: What was your biggest 'aha!' moment from today's practice?",
        "DEV-SPECIFIC APPLICATION: How can this skill improve your code reviews, team collaboration, or work on NEETPrepGPT?",
        "KNOWLEDGE CONNECTION: How did today's experience connect to the week's Knowledge Module?"
    ]
    y = draw_lined_notes_section(c, y, "🧠 EVENING REFLECTION & INSIGHTS", prompts_reflection, 2, 2.5*inch, COLOR_WISDOM)
    
    # 5. Daily Action Items / TODO
    height_todo = 1.1*inch
    c.saveState()
    c.setStrokeColor(COLOR_TEXT_HEADER)
    c.roundRect(MARGIN, y - height_todo, CONTENT_WIDTH, height_todo, 0.05*inch, fill=0, stroke=1)
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN + 0.15*inch, y - 0.3*inch, "✅ ACTION ITEMS & TO-DO")
    c.setFont(FONT_NORMAL, FONT_SIZE_S)
    c.setFillColor(COLOR_TEXT_BODY)
    y_todo = y - 0.55*inch
    for i in range(3):
        c.drawString(MARGIN + 0.15*inch, y_todo, f"☐ ____________________________________________________________________")
        y_todo -= 0.22*inch
    c.restoreState()
    y -= height_todo
    
    c.showPage()


def draw_weekly_review_page(c, week):
    """Enhanced weekly review with tech/career integration."""
    c.setFont(FONT_BOLD, FONT_SIZE_XL)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.0*inch, f"Week {week} Performance Review")
    
    c.setFont(FONT_BOLD, FONT_SIZE_S_BOLD)
    c.setFillColor(COLOR_ENERGY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.4*inch, "Growth Mindset: 'Every challenge makes me a stronger leader and developer.'")

    y = PAGE_HEIGHT - 1.8*inch
    
    tech_social_prompts = [
        "This week, how did improved social skills help you with:",
        "• Technical collaboration (code review, study group, feedback)?",
        "• Networking (LinkedIn, expert outreach for NEETPrepGPT)?",
        "• Learning (explaining concepts, asking better questions)?",
        "",
        "Action Step: What's one developer or AI founder you will connect with next week?"
    ]
    y = draw_section(c, y, "🤝 TECH & CAREER INTEGRATION", tech_social_prompts, 1.8*inch, COLOR_ACCENT, False)

    metrics_prompts = [
        "CHALLENGE COMPLETION RATE: ___/7 days completed successfully", "",
        "AVERAGE COMFORT LEVEL: Day 1: ___  Day 7: ___ (Improvement: ___)", "",
        "SUCCESS METRIC ACHIEVEMENT: How well did you hit this week's metric?",
        WEEKLY_METRICS.get(week, "No metric provided for this week."),
    ]
    y = draw_section(c, y, "📊 QUANTITATIVE RESULTS", metrics_prompts, 1.8*inch, COLOR_PRIMARY, False)
    
    insights_prompts = [
        "BIGGEST BREAKTHROUGH: What was your most significant 'aha' moment?", "",
        "PATTERN RECOGNITION: What patterns did you notice in your social behavior?", "",
        "KNOWLEDGE APPLICATION: How did the pre-week learning help your practice?",
    ]
    y = draw_section(c, y, "💡 QUALITATIVE INSIGHTS", insights_prompts, 1.6*inch, COLOR_WISDOM, False)
    
    if week < 7:
        prep_prompts = [
            f"WEEK {week+1} GOAL CUSTOMIZATION: How will you personalize next week's challenges?", "",
            f"KNOWLEDGE MODULE PLAN: When will you complete Week {week+1}'s learning?", "",
            "ACCOUNTABILITY PLAN: How will you ensure consistent practice next week?"
        ]
        draw_section(c, y, f"🎯 WEEK {week+1} PREPARATION", prep_prompts, 1.6*inch, COLOR_ENERGY, False)
    else:
        mastery_prompts = [
            "TRANSFORMATION SUMMARY: How have you changed since Week 1?", "",
            "SKILL MASTERY: Rate each skill (1-10): Self-awareness: ___, Response control: ___, Listening: ___, Communication: ___, Empathy: ___, Conflict resolution: ___, Relationship building: ___", "",
            "ONGOING PRACTICE PLAN: How will you maintain and continue growing these skills?"
        ]
        draw_section(c, y, "🏆 MASTERY ASSESSMENT", mastery_prompts, 1.6*inch, COLOR_ENERGY, False)
    
    c.showPage()

def draw_achievement_badges_page(c):
    """Draws the final achievement badges page."""
    c.setFont(FONT_BOLD, 18)
    c.setFillColor(COLOR_ENERGY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, "Social & Career Achievement Badges")
    
    c.setFont(FONT_NORMAL, FONT_SIZE_S_BOLD)
    c.setFillColor(COLOR_TEXT_BODY)
    
    y = PAGE_HEIGHT - 2.2*inch
    
    badges = [
        "☐ 💡 First LinkedIn tech connection made",
        "☐ 🚀 First open-source collaborator onboarded",
        "☐ 🏆 First AI project demo delivered (NEETPrepGPT)",
        "☐ 🔗 First successful professional introduction made",
        "☐ 🎓 First technical mentorship call completed",
        "☐ 💬 Positive code review feedback received",
        "☐ 📢 Pitched your project to a potential user/stakeholder",
        "☐ 🤝 Organized a study or collaboration session"
    ]
    
    for badge in badges:
        c.drawString(MARGIN, y, badge)
        y -= 0.35*inch
    
    y -= 0.5 * inch
    c.setFont(FONT_BOLD, FONT_SIZE_M)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y, "Add your custom badges as you progress!")
    c.setStrokeColor(lightgrey)
    for i in range(5):
        y -= 0.35*inch
        c.line(MARGIN, y, PAGE_WIDTH - MARGIN, y)

    c.showPage()

def _estimate_total_pages() -> int:
    """Estimate total pages in the generated journal."""
    bio = 1
    intro = 1
    weeks = 7
    knowledge = weeks
    daily_pages = weeks * 7
    weekly_reviews = weeks
    final_assessment = 1
    badges = 1
    total = bio + intro + knowledge + daily_pages + weekly_reviews + final_assessment + badges
    return total

def create_progressive_social_mastery_journal(start_date: Optional[date] = None, filename: Optional[str] = None):
    """Generate the complete progressive social mastery journal."""
    output_file = filename or FILENAME
    c = None
    try:
        out_dir = os.path.dirname(os.path.abspath(output_file))
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
            logger.debug("Created output directory: %s", out_dir)

        c = canvas.Canvas(output_file, pagesize=A4)

        c.setTitle(f"Social Mastery Journal for {USER_PROFILE['name']}")
        c.setAuthor(USER_PROFILE['name'])
        c.setSubject(f"7-week program for {USER_PROFILE['career_goal']}")
        c.setCreator("Progressive Social Mastery Generator Script")

        start_date = start_date or date.today()
        if isinstance(start_date, str):
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            except Exception:
                logger.warning("start_date string provided but could not parse, using today instead.")
                start_date = date.today()

        logger.info("Generating journal for %s, starting %s -> %s", USER_PROFILE['name'], start_date.isoformat(), output_file)
        logger.info("Estimated total pages: %s", _estimate_total_pages())

        # NEW: Personalized Bio Page
        draw_intro_bio_page(c)

        # Enhanced intro page
        c.setFont(FONT_BOLD, 28)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, "PROGRESSIVE SOCIAL")
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.4*inch, "MASTERY SYSTEM")
        
        c.setFont(FONT_NORMAL, FONT_SIZE_L)
        c.setFillColor(COLOR_TEXT_HEADER)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.9*inch, "An Engineering Approach to Communication Excellence")
        
        c.setFont(FONT_BOLD, 14)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 3.4*inch, "From Introvert to Influential Communicator")
        
        c.setFont(FONT_BOLD, FONT_SIZE_M)
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
        c.setFont(FONT_NORMAL, FONT_SIZE_S_BOLD)
        c.setFillColor(COLOR_TEXT_BODY)
        for feature in features_text:
            c.drawCentredString(PAGE_WIDTH/2, y_pos, feature)
            y_pos -= 0.25*inch
        
        c.setFont(FONT_BOLD, FONT_SIZE_M)
        c.setFillColor(COLOR_WISDOM)
        c.drawCentredString(PAGE_WIDTH/2, y_pos - 0.3*inch, "🚀 YOUR TRANSFORMATION COMMITMENT:")
        
        mission_text = [
            "This system will transform you from socially anxious to socially confident.",
            "You will master the engineering principles of human connection.",
            "Every interaction becomes data. Every challenge builds competence.",
            "In 7 weeks, you will have the communication skills to accelerate your career.",
            "Commit fully. Follow the system. Become unstoppable."
        ]
        
        y_mission = y_pos - 0.7*inch
        c.setFont(FONT_NORMAL, FONT_SIZE_S_BOLD)
        c.setFillColor(COLOR_TEXT_BODY)
        for line in mission_text:
            c.drawCentredString(PAGE_WIDTH/2, y_mission, line)
            y_mission -= 0.22*inch
        
        c.showPage()
        
        day_offset = 0
        for week in range(1, 8):
            draw_knowledge_module_page(c, week)
            
            for day in range(1, 8):
                current_date = start_date + timedelta(days=day_offset)
                date_str = current_date.strftime('%A, %B %d, %Y')
                
                draw_header(c, week, day, date_str)
                draw_daily_page(c, date_str, week, day)
                
                day_offset += 1
            
            draw_weekly_review_page(c, week)
        
        # Final transformation assessment
        c.setFont(FONT_BOLD, 24)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, "SOCIAL MASTERY ACHIEVED")
        
        c.setFont(FONT_BOLD, FONT_SIZE_L)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.6*inch, "Final Transformation Assessment")
        
        y = PAGE_HEIGHT - 3.5*inch
        final_prompts = [
            "BEFORE vs. AFTER ASSESSMENT:",
            "Week 1 Comfort Level: ___/10    Week 7 Comfort Level: ___/10",
            "",
            "Most Significant Transformation in your developer workflow:", "",
            "New Social Superpowers Acquired:",
            "1. ____________________ 2. ____________________ 3. ____________________",
            "",
            "NEETPrepGPT IMPACT: How will these new skills accelerate your project's launch, user feedback gathering, and potential team building?",
            "",
            "CAREER IMPACT: How will these skills help you achieve your goals as an AI Engineer/Founder?",
            "",
            "ONGOING PRACTICE PLAN: How will you maintain and expand these abilities?"
        ]
        
        c.setFont(FONT_NORMAL, FONT_SIZE_M)
        c.setFillColor(COLOR_TEXT_BODY)
        for prompt in final_prompts:
            if prompt.strip():
                if prompt.endswith(':'):
                    c.setFont(FONT_BOLD, FONT_SIZE_M)
                    c.setFillColor(COLOR_TEXT_HEADER)
                else:
                    c.setFont(FONT_NORMAL, FONT_SIZE_M)
                    c.setFillColor(COLOR_TEXT_BODY)
                
                wrapped_prompt = textwrap.wrap(prompt, width=70)
                for line in wrapped_prompt:
                    c.drawCentredString(PAGE_WIDTH/2, y, line)
                    y -= 0.25*inch
            else:
                y -= 0.25*inch

        y -= 0.5*inch
        c.setFont(FONT_BOLD, 14)
        c.setFillColor(COLOR_ENERGY)
        c.drawCentredString(PAGE_WIDTH/2, y, "🎉 CONGRATULATIONS! 🎉")
        c.setFont(FONT_NORMAL, FONT_SIZE_M)
        c.setFillColor(COLOR_TEXT_BODY)
        c.drawCentredString(PAGE_WIDTH/2, y - 0.3*inch, "You now possess the systematic communication skills")
        c.drawCentredString(PAGE_WIDTH/2, y - 0.6*inch, "to build any relationship and influence any outcome.")
        c.drawCentredString(PAGE_WIDTH/2, y - 0.9*inch, "Your AI/health-tech career will benefit immeasurably.")
        c.showPage()

        # NEW: Achievement Badges Page
        draw_achievement_badges_page(c)
        
        c.save()
        logger.info("✅ Successfully created %s", output_file)
        logger.info("📊 Generated comprehensive progressive social mastery system:")
        logger.info("   • 1 Personalized Bio Page")
        logger.info("   • 7 Knowledge Module pages")
        logger.info("   • 49 Daily Practice pages (with developer focus)")
        logger.info("   • 7 Weekly Review pages (with career integration)")
        logger.info("   • 2 Assessment pages (intro + final transformation)")
        logger.info("   • 1 Achievement Badge Page")
        logger.info("   • Total (estimated): %s pages", _estimate_total_pages())

    except Exception as exc:
        logger.exception("Failed to generate journal: %s", exc)
        if c:
            try:
                c.save()
            except Exception:
                pass
        raise

def _parse_args():
    parser = argparse.ArgumentParser(description="Generate a Progressive Social Mastery Journal PDF.")
    parser.add_argument("--start-date", type=str, default=None,
                        help="Start date for Day 1 in YYYY-MM-DD format. Defaults to today.")
    parser.add_argument("--output", type=str, default=None, help=f"Output PDF filename. Defaults to {FILENAME}.")
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