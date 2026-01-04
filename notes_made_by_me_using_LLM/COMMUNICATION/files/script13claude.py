# Enhanced Progressive Social Mastery Engineering Journal
# (Original content preserved; improvements added: CLI, logging, metadata, validation, type hints)
# Version 3.0: Master-Level Design with Enhanced Daily Pages for Arun Yadav's AI/Developer Career Path

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
COLOR_BG_LIGHT = HexColor('#F8F9FA')
COLOR_TEXT_HEADER = HexColor('#1A1A1A')
COLOR_TEXT_BODY = HexColor('#2C2C2C')
COLOR_CHECKBOX = HexColor('#28A745')
COLOR_TODO = HexColor('#FD7E14')
COLOR_NOTES = HexColor('#6F42C1')

# --- Configuration ---
FILENAME = "Arun_Yadav_Social_Mastery_Journal_Enhanced.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.5 * inch
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

# --- Enhanced Daily Study Notes by Week ---
DAILY_STUDY_NOTES = {
    1: [
        "🧠 NEUROSCIENCE: Mirror neurons activate when we see facial expressions. Smiling triggers positive responses in others' brains.",
        "💡 TIP: Eye contact should be 50-70% of conversation time. Break it naturally every 3-5 seconds to avoid staring.",
        "🎯 PRACTICE: Stand in front of mirror and practice genuine vs fake smiles. Notice the difference around your eyes.",
        "📚 READ: 'The Like Switch' by Jack Schafer - FBI techniques for instant rapport building.",
        "🔬 STUDY: Mehrabian's 7-38-55 rule: 7% words, 38% tone, 55% body language in emotional communication.",
        "⚡ ENERGY: Confident posture increases testosterone by 20% and decreases cortisol by 25% within 2 minutes.",
        "🎨 ART: Master painters study light and shadow. Study how confident people use space and movement."
    ],
    2: [
        "🧠 NEUROSCIENCE: The amygdala hijack lasts exactly 6 seconds. Count to 6 before responding to emotional triggers.",
        "💡 TIP: Box breathing technique: Inhale 4, hold 4, exhale 4, hold 4. Activates parasympathetic nervous system.",
        "🎯 PRACTICE: Label emotions with precision: 'frustrated' vs 'overwhelmed' vs 'disappointed' creates different responses.",
        "📚 READ: 'Emotional Intelligence' by Daniel Goleman - Chapter 5 on self-regulation mastery.",
        "🔬 STUDY: Prefrontal cortex vs limbic system: rational brain vs emotional brain conflict resolution.",
        "⚡ ENERGY: Cold exposure (cold shower) for 30 seconds builds emotional resilience and stress tolerance.",
        "🎨 ART: Japanese concept of 'Ma' - the power of pause and empty space in creating beauty and meaning."
    ],
    3: [
        "🧠 NEUROSCIENCE: Active listening activates the same brain regions as meditation, increasing empathy and focus.",
        "💡 TIP: Use the 'echo technique' - repeat the last 1-3 words of what someone said with questioning tone.",
        "🎯 PRACTICE: Listen for emotions behind facts. 'The deadline is tomorrow' might mean 'I'm stressed and need support.'",
        "📚 READ: 'Just Listen' by Mark Goulston - FBI hostage negotiator listening techniques.",
        "🔬 STUDY: Parasympathetic listening posture: open chest, relaxed shoulders, forward lean shows engagement.",
        "⚡ ENERGY: Listening to instrumental music for 10 minutes trains sustained attention for better conversations.",
        "🎨 ART: Great composers use silence as powerfully as sound. Master the art of comfortable silence."
    ],
    4: [
        "🧠 NEUROSCIENCE: I-statements activate the logical brain; You-statements trigger the defensive brain immediately.",
        "💡 TIP: The DESC script: Describe, Express, Specify, Consequences. Structure for difficult conversations.",
        "🎯 PRACTICE: Replace 'You always...' with 'When X happens, I feel Y because Z. Could we try A instead?'",
        "📚 READ: 'Crucial Conversations' by Kerry Patterson - High-stakes communication mastery.",
        "🔬 STUDY: Assertiveness vs Aggressiveness: Assertive = confident + respectful. Aggressive = confident + disrespectful.",
        "⚡ ENERGY: Power posing before important conversations increases confidence and reduces stress hormones.",
        "🎨 ART: Calligraphy teaches precision and intention with every stroke. Apply this to every word choice."
    ],
    5: [
        "🧠 NEUROSCIENCE: Empathy involves 3 networks: mirror neuron system, mentalizing network, and emotional regulation.",
        "💡 TIP: Cognitive empathy = understanding thoughts. Emotional empathy = feeling emotions. Use both strategically.",
        "🎯 PRACTICE: The empathy formula: 'It sounds like you're feeling X because Y is important to you. Is that right?'",
        "📚 READ: 'Nonviolent Communication' by Marshall Rosenberg - Connect through human needs, not positions.",
        "🔬 STUDY: Cultural empathy gaps: High-context vs low-context cultures affect communication interpretation.",
        "⚡ ENERGY: Loving-kindness meditation increases empathy and social connection in just 7 weeks of practice.",
        "🎨 ART: Method actors don't just memorize lines - they understand the character's inner world and motivations."
    ],
    6: [
        "🧠 NEUROSCIENCE: Conflict activates threat-detection centers. Use collaborative language to switch to reward centers.",
        "💡 TIP: Aikido principle: Don't meet force with force. Redirect the energy toward a shared solution.",
        "🎯 PRACTICE: Find the 10% you agree on before addressing the 90% you don't. Start with common ground.",
        "📚 READ: 'Getting to Yes' by Roger Fisher - Separate people from problems, positions from interests.",
        "🔬 STUDY: De-escalation voice patterns: Lower pitch, slower pace, softer volume signals safety to the brain.",
        "⚡ ENERGY: Progressive muscle relaxation before difficult conversations reduces physical tension and reactivity.",
        "🎨 ART: Jazz musicians resolve dissonance into harmony. Every conflict contains the seeds of deeper connection."
    ],
    7: [
        "🧠 NEUROSCIENCE: Social bonds release oxytocin and dopamine, creating positive feedback loops for relationship building.",
        "💡 TIP: The 5-minute favor rule: Offer help that costs you 5 minutes but provides significant value to others.",
        "🎯 PRACTICE: Follow up within 24 hours of meaningful conversations. Memory and connection are strongest then.",
        "📚 READ: 'Never Eat Alone' by Keith Ferrazzi - Transform networking from transaction to genuine relationship.",
        "🔬 STUDY: Dunbar's number: 150 meaningful relationships maximum. Quality over quantity in network building.",
        "⚡ ENERGY: Gratitude journaling increases social connection and makes you more attractive as a network contact.",
        "🎨 ART: Renaissance masters had patrons and communities. Your network is your modern artistic support system."
    ]
}

# --- Enhanced TODO Lists by Week ---
DAILY_TODOS = {
    1: [
        ["☐ Review mirror neuron research", "☐ Practice genuine smile for 2 minutes", "☐ Identify 5 low-risk interaction opportunities", "☐ Prepare opening lines for conversations"],
        ["☐ Study body language basics", "☐ Choose appropriate locations for practice", "☐ Prepare backup conversation topics", "☐ Review comfort zone expansion theory"],
        ["☐ Research conversation starters", "☐ Practice clear voice projection", "☐ Identify helpful strangers to approach", "☐ Study question-asking techniques"],
        ["☐ Learn compliment-giving psychology", "☐ Practice observational skills", "☐ Identify genuine appreciation opportunities", "☐ Study positive reinforcement principles"],
        ["☐ Study follow-up conversation techniques", "☐ Practice active observation", "☐ Prepare thoughtful comments", "☐ Review social momentum building"],
        ["☐ Study turn-taking in conversations", "☐ Practice listening for cues", "☐ Prepare engaging responses", "☐ Review conversation flow patterns"],
        ["☐ Study low-stakes environments", "☐ Practice conversation initiation", "☐ Prepare graceful conversation exits", "☐ Review day's learning consolidation"]
    ],
    2: [
        ["☐ Learn tactical pause technique", "☐ Practice deep breathing", "☐ Identify personal irritation triggers", "☐ Study emotional regulation science"],
        ["☐ Practice mindful listening", "☐ Study response-planning habits", "☐ Learn attention reset techniques", "☐ Practice present-moment awareness"],
        ["☐ Learn emotion labeling vocabulary", "☐ Practice emotional awareness", "☐ Study trigger recognition", "☐ Practice silent self-talk"],
        ["☐ Master STOP technique steps", "☐ Identify reactive situations", "☐ Practice technique implementation", "☐ Study pause-power psychology"],
        ["☐ Learn complaint transformation", "☐ Practice request formulation", "☐ Study actionable communication", "☐ Practice solution-focused thinking"],
        ["☐ Study feedback reception psychology", "☐ Practice 6-second rule", "☐ Learn code review etiquette", "☐ Practice professional responses"],
        ["☐ Integrate all week's techniques", "☐ Plan challenging conversation", "☐ Practice technique combination", "☐ Review week's progress"]
    ],
    3: [
        ["☐ Study focused attention techniques", "☐ Practice listening meditation", "☐ Identify conversation planning habits", "☐ Learn full presence techniques"],
        ["☐ Learn paraphrasing techniques", "☐ Practice confirmation statements", "☐ Study technical discussion dynamics", "☐ Practice understanding validation"],
        ["☐ Study clarifying question types", "☐ Practice question formulation", "☐ Learn curious inquiry techniques", "☐ Practice input timing"],
        ["☐ Study emotion recognition", "☐ Practice emotion reflection", "☐ Learn empathic responses", "☐ Practice emotional validation"],
        ["☐ Study disagreement psychology", "☐ Practice perspective-taking", "☐ Learn technical diplomacy", "☐ Practice respectful listening"],
        ["☐ Study user empathy techniques", "☐ Practice problem-focused listening", "☐ Learn need identification", "☐ Practice solution-oriented responses"],
        ["☐ Study feedback psychology", "☐ Practice non-defensive listening", "☐ Learn senior developer dynamics", "☐ Practice growth mindset responses"]
    ],
    4: [
        ["☐ Study I-statement psychology", "☐ Practice statement transformation", "☐ Learn assertive communication", "☐ Practice team communication"],
        ["☐ Learn appreciation language", "☐ Practice request formulation", "☐ Study positive communication", "☐ Practice solution-focused requests"],
        ["☐ Study confident expression", "☐ Practice opinion articulation", "☐ Learn technical confidence", "☐ Practice direct communication"],
        ["☐ Learn feeling expression formulas", "☐ Practice vulnerability in learning", "☐ Study challenge communication", "☐ Practice need articulation"],
        ["☐ Study boundary psychology", "☐ Practice boundary language", "☐ Learn time management communication", "☐ Practice focus protection"],
        ["☐ Study direct request techniques", "☐ Practice specific asking", "☐ Learn mentorship communication", "☐ Practice clarity in requests"],
        ["☐ Plan difficult conversation", "☐ Practice I-statement integration", "☐ Study scope communication", "☐ Practice professional courage"]
    ],
    5: [
        ["☐ Study deeper conversation techniques", "☐ Practice genuine inquiry", "☐ Learn empathic questioning", "☐ Practice emotional attunement"],
        ["☐ Study user frustration psychology", "☐ Practice perspective-taking", "☐ Learn problem empathy", "☐ Practice solution empathy"],
        ["☐ Study career conversation techniques", "☐ Practice goal-focused inquiry", "☐ Learn networking empathy", "☐ Practice supportive listening"],
        ["☐ Study vulnerability psychology", "☐ Practice appropriate sharing", "☐ Learn connection through struggle", "☐ Practice authentic communication"],
        ["☐ Study need identification", "☐ Practice underlying concern recognition", "☐ Learn project empathy", "☐ Practice supportive response"],
        ["☐ Study perspective-shifting", "☐ Practice viewpoint exploration", "☐ Learn technical empathy", "☐ Practice understanding prioritization"],
        ["☐ Plan 80/20 conversation", "☐ Practice understanding focus", "☐ Learn perspective mastery", "☐ Practice empathic leadership"]
    ],
    6: [
        ["☐ Study direct communication", "☐ Practice issue identification", "☐ Learn collaborative problem-solving", "☐ Practice early intervention"],
        ["☐ Study collaborative language", "☐ Practice 'we' statements", "☐ Learn partnership communication", "☐ Practice solution-focused dialogue"],
        ["☐ Master COIN method", "☐ Practice structured feedback", "☐ Learn constructive criticism", "☐ Practice code review diplomacy"],
        ["☐ Study effective apology structure", "☐ Practice responsibility taking", "☐ Learn mistake communication", "☐ Practice professional accountability"],
        ["☐ Study agreement identification", "☐ Practice common ground finding", "☐ Learn bridge-building communication", "☐ Practice unity focus"],
        ["☐ Study problem-solving frameworks", "☐ Practice conflict transformation", "☐ Learn solution orientation", "☐ Practice collaborative resolution"],
        ["☐ Research expert outreach", "☐ Practice advice-seeking", "☐ Learn mentorship requests", "☐ Practice product pitch preparation"]
    ],
    7: [
        ["☐ Study appreciation psychology", "☐ Practice specific gratitude", "☐ Learn meaningful recognition", "☐ Practice relationship investment"],
        ["☐ Study LinkedIn engagement", "☐ Practice reconnection messages", "☐ Learn network maintenance", "☐ Practice relationship nurturing"],
        ["☐ Study advice-seeking techniques", "☐ Practice senior engagement", "☐ Learn mentorship requests", "☐ Practice growth-focused inquiry"],
        ["☐ Study virtual coffee techniques", "☐ Practice invitation formulation", "☐ Learn relationship deepening", "☐ Practice connection scheduling"],
        ["☐ Study networking introductions", "☐ Practice value-add connections", "☐ Learn mutual benefit creation", "☐ Practice network orchestration"],
        ["☐ Study community contribution", "☐ Practice value offering", "☐ Learn proactive helping", "☐ Practice service-oriented networking"],
        ["☐ Prepare NEETPrepGPT pitch", "☐ Practice project presentation", "☐ Learn startup communication", "☐ Practice value proposition clarity"]
    ]
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

def draw_checkbox(c, x, y, size=8, filled=False):
    """Draw a checkbox at the given coordinates."""
    c.saveState()
    c.setStrokeColor(COLOR_CHECKBOX)
    c.setLineWidth(1)
    c.rect(x, y, size, size)
    if filled:
        c.setFillColor(COLOR_CHECKBOX)
        c.rect(x+1, y+1, size-2, size-2, fill=1)
    c.restoreState()

def draw_intro_bio_page(c):
    """Draws the personalized introductory bio page."""
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.2*inch, "Personalized Social Mastery Journal")
    
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(COLOR_ACCENT)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, "Master-Level Design for Peak Performance")
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_TEXT_HEADER)
    y = PAGE_HEIGHT - 1.9*inch
    c.drawString(MARGIN, y, f"Name: {USER_PROFILE['name']}")
    c.drawString(MARGIN, y-0.3*inch, f"Location: {USER_PROFILE['location']}")
    c.drawString(MARGIN, y-0.6*inch, f"Main Project: {USER_PROFILE['main_project']}")
    c.drawString(MARGIN, y-0.9*inch, f"Career Goal: {USER_PROFILE['career_goal']}")
    y -= 1.0 * inch
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_WISDOM)
    c.drawCentredString(PAGE_WIDTH/2, y, "This journal is crafted for you—a growth-minded developer & founder.")
    c.drawCentredString(PAGE_WIDTH/2, y-0.3*inch, "Use it to engineer the communication skills that will multiply your technical impact.")
    
    # Add design elements
    c.setStrokeColor(COLOR_ACCENT)
    c.setLineWidth(2)
    c.line(MARGIN, y-0.6*inch, PAGE_WIDTH-MARGIN, y-0.6*inch)
    
    c.showPage()

def draw_header(c, week, day, date_str):
    """Enhanced header with progress tracking."""
    c.saveState()
    # Main title with larger font
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Week {week}: Progressive Social Lab")
    
    # Progress bar
    progress = ((week - 1) * 7 + (day -1)) / 49.0
    bar_width = 3 * inch
    c.setStrokeColor(lightgrey)
    c.setLineWidth(6)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.15*inch, MARGIN + bar_width, PAGE_HEIGHT - MARGIN - 0.15*inch)
    c.setStrokeColor(COLOR_ACCENT)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.15*inch, MARGIN + (bar_width * progress), PAGE_HEIGHT - MARGIN - 0.15*inch)
    
    # Progress percentage
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(COLOR_ACCENT)
    c.drawString(MARGIN + bar_width + 0.2*inch, PAGE_HEIGHT - MARGIN - 0.18*inch, f"{int(progress*100)}%")
    
    # Date and day with larger font
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Day {(week-1)*7 + day} of 49")
    c.setFont("Helvetica", 11)
    c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 0.15*inch, date_str)
    
    # Separator line
    c.setStrokeColor(COLOR_PRIMARY)
    c.setLineWidth(2)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.35*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 0.35*inch)
    c.restoreState()

def draw_knowledge_module_page(c, week):
    """Weekly knowledge module page with learning resources."""
    module = _safe_get_module(week)
    
    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(COLOR_KNOWLEDGE)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.3*inch, f"WEEK {week} KNOWLEDGE MODULE")
    
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.7*inch, module["title"])
    
    # Decorative line
    c.setStrokeColor(COLOR_KNOWLEDGE)
    c.setLineWidth(3)
    c.line(PAGE_WIDTH/2 - 2*inch, PAGE_HEIGHT - 1.85*inch, PAGE_WIDTH/2 + 2*inch, PAGE_HEIGHT - 1.85*inch)
    
    y = PAGE_HEIGHT - 2.2*inch
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_ENERGY)
    c.drawString(MARGIN, y, "⏰ TIME INVESTMENT: 45-75 minutes before starting Week " + str(week))
    y -= 0.5*inch
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, y, "📚 RECOMMENDED LEARNING RESOURCES:")
    y -= 0.35*inch
    
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    for i, resource in enumerate(module["learning_resources"], 1):
        wrapped = textwrap.wrap(resource, width=85)
        for line_num, line in enumerate(wrapped):
            if line_num == 0:
                c.drawString(MARGIN + 0.25*inch, y, f"{i}. {line}")
            else:
                c.drawString(MARGIN + 0.5*inch, y, line)
            y -= 0.25*inch
        # Add checkbox for completion tracking
        draw_checkbox(c, PAGE_WIDTH - MARGIN - 0.3*inch, y + 0.1*inch)
        y -= 0.05*inch
    
    y -= 0.2*inch
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, y, "🎯 KEY CONCEPTS TO MASTER:")
    y -= 0.35*inch
    
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    for concept in module["key_concepts"]:
        wrapped = textwrap.wrap(concept, width=85)
        for i, line in enumerate(wrapped):
            prefix = "• " if i == 0 else "  "
            c.drawString(MARGIN + 0.25*inch, y, prefix + line)
            y -= 0.23*inch
        # Add checkbox for concept mastery
        draw_checkbox(c, PAGE_WIDTH - MARGIN - 0.3*inch, y + 0.1*inch)
        y -= 0.05*inch
    
    y -= 0.3*inch
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_ACCENT)
    c.drawString(MARGIN, y, "✅ LEARNING COMPLETION CHECKLIST:")
    y -= 0.35*inch
    
    checklist_items = [
        "☐ Watched/read at least 3 recommended resources",
        "☐ Can explain the key concepts in my own words", 
        "☐ Identified how these concepts apply to my personal goals",
        "☐ Created practice scenarios for this week",
        "☐ Ready to practice these skills in real conversations"
    ]
    
    c.setFont("Helvetica", 11)
    for item in checklist_items:
        draw_checkbox(c, MARGIN + 0.25*inch, y-3)
        c.drawString(MARGIN + 0.5*inch, y, item[2:])  # Remove ☐ since we're drawing actual checkboxes
        y -= 0.28*inch
    
    y -= 0.3*inch
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y, "🎯 MY PERSONAL APPLICATION GOAL:")
    y -= 0.35*inch
    
    goal_template = GOAL_TEMPLATES.get(week, "Set a personal goal for this week.")
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    
    wrapped = textwrap.wrap(goal_template, width=100)
    for line in wrapped:
        c.drawString(MARGIN, y, line)
        y -= 0.25*inch
    
    y -= 0.3*inch
    
    # Enhanced writing lines
    c.setStrokeColor(COLOR_PRIMARY)
    c.setLineWidth(0.8)
    for i in range(5):
        c.line(MARGIN, y - (i * 0.25*inch), PAGE_WIDTH - MARGIN, y - (i * 0.25*inch))
    
    y -= 1.4*inch
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(MARGIN, y, "📊 THIS WEEK'S SUCCESS METRIC:")
    y -= 0.35*inch
    
    metric = WEEKLY_METRICS.get(week, "No metric defined.")
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    
    wrapped_metric = textwrap.wrap(metric, width=100)
    for line in wrapped_metric:
        c.drawString(MARGIN, y, line)
        y -= 0.23*inch
    
    c.showPage()

def draw_section(c, y_pos, title, content_prompts, height, color=COLOR_PRIMARY, include_lines=True):
    """Enhanced section with better formatting and larger fonts."""
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(2)
    c.roundRect(MARGIN, y_pos - height, CONTENT_WIDTH, height, 0.08*inch)

    # Header background
    c.setFillColor(color)
    c.roundRect(MARGIN, y_pos - 0.45*inch, CONTENT_WIDTH, 0.45*inch, 0.08*inch, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.32*inch, title)

    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    current_y = y_pos - 0.7*inch
    line_spacing = 0.28*inch
    
    for prompt in content_prompts:
        if prompt.strip():
            if prompt.startswith('☐'):
                # Draw checkbox for checklist items
                draw_checkbox(c, MARGIN + 0.2*inch, current_y - 3)
                c.drawString(MARGIN + 0.45*inch, current_y, prompt[2:])
            else:
                wrapped = textwrap.wrap(prompt, width=95)
                for i, wline in enumerate(wrapped):
                    c.drawString(MARGIN + 0.2*inch, current_y, wline)
                    current_y -= 0.2*inch
            
            if include_lines and not prompt.endswith(':') and not prompt.startswith('☐'):
                line_y = current_y - 0.08*inch
                c.setStrokeColor(COLOR_BG_LIGHT)
                c.setLineWidth(1)
                for i in range(3):
                    c.line(MARGIN + 0.25*inch, line_y - (i * 0.18*inch), PAGE_WIDTH - MARGIN - 0.25*inch, line_y - (i * 0.18*inch))
                current_y -= 0.6*inch
            else:
                current_y -= line_spacing
        else:
            current_y -= line_spacing * 0.7

    c.restoreState()
    return y_pos - height - 0.25*inch

def draw_progressive_challenge_box(c, y_pos, week, day):
    """Progressive daily challenge with specific metrics and enhanced design."""
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
    # Enhanced background with gradient effect
    c.setFillColor(COLOR_BG_LIGHT)
    c.setStrokeColor(COLOR_ACCENT)
    c.setLineWidth(3)
    c.roundRect(MARGIN, y_pos - 2*inch, CONTENT_WIDTH, 2*inch, 0.12*inch, fill=1, stroke=1)
    
    # Challenge header
    c.setFillColor(COLOR_ACCENT)
    c.roundRect(MARGIN, y_pos - 0.5*inch, CONTENT_WIDTH, 0.5*inch, 0.12*inch, fill=1, stroke=0)
    
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont("Helvetica-Bold", 14)
    c.drawString(MARGIN + 0.25*inch, y_pos - 0.35*inch, f"🎯 DAY {day} PROGRESSIVE CHALLENGE")
    
    # Challenge description
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_TEXT_BODY)
    wrapped_ch = textwrap.wrap(challenge, width=100)
    desc_y = y_pos - 0.8*inch
    for line in wrapped_ch:
        c.drawString(MARGIN + 0.25*inch, desc_y, line)
        desc_y -= 0.23*inch
    
    # Success metrics section
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(MARGIN + 0.25*inch, y_pos - 1.3*inch, "📊 SUCCESS METRICS:")
    
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    draw_checkbox(c, MARGIN + 0.3*inch, y_pos - 1.55*inch)
    c.drawString(MARGIN + 0.55*inch, y_pos - 1.52*inch, "Challenge completed successfully")
    
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.75*inch, "Comfort level: ___/10  |  Energy level: ___/10")
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.95*inch, "Time taken: _____ minutes  |  Follow-up planned: ☐ Yes ☐ No")
    
    c.restoreState()
    return y_pos - 2.2*inch

def draw_daily_study_notes_section(c, y_pos, week, day):
    """Enhanced daily study notes with scientific backing."""
    notes = DAILY_STUDY_NOTES.get(week, ["No study notes available for this week."])
    if 1 <= day <= len(notes):
        note = notes[day-1]
    else:
        note = "Study note not available for this day."
    
    c.saveState()
    c.setFillColor(COLOR_NOTES)
    c.setStrokeColor(COLOR_NOTES)
    c.setLineWidth(2)
    c.roundRect(MARGIN, y_pos - 1.2*inch, CONTENT_WIDTH, 1.2*inch, 0.08*inch, fill=0, stroke=1)
    
    # Header
    c.setFillColor(COLOR_NOTES)
    c.roundRect(MARGIN, y_pos - 0.35*inch, CONTENT_WIDTH, 0.35*inch, 0.08*inch, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.28*inch, f"📚 TODAY'S STUDY NOTE - Master Level Insight")
    
    # Note content
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    wrapped_note = textwrap.wrap(note, width=100)
    note_y = y_pos - 0.6*inch
    for line in wrapped_note:
        c.drawString(MARGIN + 0.2*inch, note_y, line)
        note_y -= 0.2*inch
    
    # Action checkbox
    c.setFont("Helvetica", 10)
    draw_checkbox(c, MARGIN + 0.2*inch, y_pos - 1.1*inch)
    c.drawString(MARGIN + 0.45*inch, y_pos - 1.07*inch, "I have studied and understood today's insight")
    
    c.restoreState()
    return y_pos - 1.4*inch

def draw_daily_todos_section(c, y_pos, week, day):
    """Enhanced daily TODO section with checkboxes."""
    todos = DAILY_TODOS.get(week, [])
    if week in DAILY_TODOS and 1 <= day <= len(todos):
        day_todos = todos[day-1]
    else:
        day_todos = ["☐ No todos available for this day"]
    
    c.saveState()
    c.setFillColor(COLOR_TODO)
    c.setStrokeColor(COLOR_TODO)
    c.setLineWidth(2)
    c.roundRect(MARGIN, y_pos - 1.8*inch, CONTENT_WIDTH, 1.8*inch, 0.08*inch, fill=0, stroke=1)
    
    # Header
    c.setFillColor(COLOR_TODO)
    c.roundRect(MARGIN, y_pos - 0.35*inch, CONTENT_WIDTH, 0.35*inch, 0.08*inch, fill=1, stroke=0)
    c.setFillColor(HexColor('#FFFFFF'))
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.28*inch, f"✅ TODAY'S PREPARATION TODOs")
    
    # TODO items
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    todo_y = y_pos - 0.6*inch
    
    for todo in day_todos:
        if todo.startswith('☐'):
            draw_checkbox(c, MARGIN + 0.25*inch, todo_y - 3)
            wrapped_todo = textwrap.wrap(todo[2:], width=90)
            for i, line in enumerate(wrapped_todo):
                c.drawString(MARGIN + 0.5*inch, todo_y, line)
                todo_y -= 0.2*inch
            todo_y -= 0.05*inch
        else:
            wrapped_todo = textwrap.wrap(todo, width=95)
            for line in wrapped_todo:
                c.drawString(MARGIN + 0.25*inch, todo_y, line)
                todo_y -= 0.2*inch
    
    c.restoreState()
    return y_pos - 2*inch

def draw_daily_page(c, date_str, week, day):
    """Enhanced daily page with developer-focused reflection and more content."""
    y = PAGE_HEIGHT - MARGIN - 0.45*inch
    
    # Main challenge box
    y = draw_progressive_challenge_box(c, y, week, day)
    
    # Study notes section
    y = draw_daily_study_notes_section(c, y, week, day)
    
    # TODO section
    y = draw_daily_todos_section(c, y, week, day)
    
    # Pre-Challenge Preparation
    prompts_prep = [
        "🧠 MINDSET CHECK: Rate your current confidence level (1-10): ____",
        "⚡ ENERGY LEVEL: How energized do you feel right now (1-10): ____",
        "🎯 SPECIFIC GOAL: What exactly do I want to achieve today?",
        "",
        "🔥 MOTIVATION BOOSTER: Why is mastering this skill important for my AI career?",
        ""
    ]
    y = draw_section(c, y, "🚀 PRE-CHALLENGE PREPARATION", prompts_prep, 2*inch, COLOR_ENERGY)
    
    c.showPage()  # Start new page for execution tracking
    
    # New page header
    draw_header(c, week, day, date_str + " (continued)")
    y = PAGE_HEIGHT - MARGIN - 0.6*inch
    
    # Execution tracking
    prompts_execution = [
        "⏰ EXECUTION TIME: Started at: _____ | Ended at: _____ | Duration: _____ mins",
        "📍 LOCATION: Where did this interaction take place?",
        "",
        "👥 PEOPLE INVOLVED: Who did you interact with? (describe briefly)",
        "",
        "💬 CONVERSATION DETAILS: What exactly happened? (be specific)",
        "",
        "",
        "☐ Challenge completed as planned",
        "☐ Had to modify approach (explain below)",
        "☐ Will retry tomorrow with adjustments",
        "COMFORT LEVEL: Before ___/10 | During ___/10 | After ___/10",
        "",
        "🎯 SUCCESS METRICS ACHIEVED:",
        "☐ Primary objective met",
        "☐ Conversation felt natural", 
        "☐ Other person responded positively",
        "☐ I felt confident throughout"
    ]
    y = draw_section(c, y, "📊 DETAILED EXECUTION TRACKING", prompts_execution, 4*inch, COLOR_PRIMARY)
    
    # Learning and insights
    prompts_learning = [
        "💡 BREAKTHROUGH MOMENT: What surprised you most?",
        "",
        "",
        "🔧 TECHNICAL CONNECTION: How did today's social skill help with:",
        "• Debugging a problem: ________________________________",
        "• Learning something new: _____________________________", 
        "• Collaborating with others: ___________________________",
        "",
        "🚀 NEETPREPGPT APPLICATION: How will this skill help your project?",
        "",
        "",
        "📈 IMPROVEMENT AREAS: What will you focus on tomorrow?",
        "",
        ""
    ]
    y = draw_section(c, y, "🧠 LEARNING & INSIGHTS", prompts_learning, 3*inch, COLOR_WISDOM)
    
    c.showPage()  # Start third page for reflection
    
    # Third page header  
    draw_header(c, week, day, date_str + " (reflection)")
    y = PAGE_HEIGHT - MARGIN - 0.6*inch
    
    # Reflection and planning
    prompts_reflection = [
        "🏆 TODAY'S WINS (celebrate small victories):",
        "1. ________________________________________________",
        "2. ________________________________________________", 
        "3. ________________________________________________",
        "",
        "⚠️ CHALLENGES FACED:",
        "What was difficult? ____________________________________",
        "Why was it difficult? __________________________________",
        "How can I prepare better next time? ____________________",
        "",
        "🎨 CREATIVE INSIGHTS: What did you notice about human behavior?",
        "",
        "",
        "💪 CONFIDENCE BUILDING: How did today make you stronger?",
        "",
        ""
    ]
    y = draw_section(c, y, "🤔 DEEP REFLECTION & ANALYSIS", prompts_reflection, 3.5*inch, COLOR_WISDOM)
    
    # Tomorrow's preparation
    prompts_tomorrow = [
        "🔮 TOMORROW'S FOCUS: Based on today, what should I emphasize?",
        "",
        "",
        "📋 SPECIFIC PREPARATION NEEDED:",
        "☐ Review certain conversation techniques",
        "☐ Practice specific phrases or responses", 
        "☐ Identify better practice opportunities",
        "☐ Work on confidence-building exercises",
        "",
        "🌟 ACCOUNTABILITY: Who will I tell about today's progress?",
        "☐ Posted update on LinkedIn",
        "☐ Shared with mentor/friend",
        "☐ Updated personal development log",
        "",
        "⭐ ENERGY RATING for tomorrow (1-10): ____"
    ]
    y = draw_section(c, y, "⏭️ TOMORROW'S STRATEGIC PLANNING", prompts_tomorrow, 2.8*inch, COLOR_ACCENT)
    
    c.showPage()

def draw_weekly_review_page(c, week):
    """Enhanced weekly review with tech/career integration and more comprehensive analysis."""
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.0*inch, f"Week {week} Performance Review")
    
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(COLOR_ENERGY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.4*inch, "Growth Mindset: 'Every challenge makes me a stronger leader and developer.'")

    # Decorative line
    c.setStrokeColor(COLOR_PRIMARY)
    c.setLineWidth(3)
    c.line(MARGIN, PAGE_HEIGHT - 1.6*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 1.6*inch)

    y = PAGE_HEIGHT - 1.9*inch
    
    # Weekly completion overview
    completion_prompts = [
        "📊 WEEKLY COMPLETION OVERVIEW:",
        "Days completed successfully: ___/7",
        "Average comfort level improvement: Start: ___/10 → End: ___/10",
        "Total practice time this week: _____ hours _____ minutes",
        "Most consistent day of practice: _________________________",
        "Most challenging day: ___________________________________",
        "",
        "🎯 CHALLENGE-SPECIFIC RESULTS:",
        "☐ All daily challenges attempted",
        "☐ At least 5/7 challenges completed successfully", 
        "☐ Comfort level improved by at least 2 points",
        "☐ Applied skills in real-world situations"
    ]
    y = draw_section(c, y, "📈 QUANTITATIVE WEEKLY ANALYSIS", completion_prompts, 2.3*inch, COLOR_PRIMARY, False)

    # Tech and career integration
    tech_social_prompts = [
        "💻 TECHNICAL COLLABORATION IMPROVEMENTS:",
        "• Code reviews: How did better communication help? __________",
        "• Team meetings: What changed in your participation? ________",
        "• Problem-solving: Did you ask better questions? ____________",
        "",
        "🚀 NEETPREPGPT PROJECT ADVANCEMENT:",
        "• User research: Did you gather better feedback? ____________",
        "• Networking: New connections made this week: ______________",
        "• Pitch practice: Did you explain your project better? _______",
        "",
        "📚 LEARNING ACCELERATION:",
        "• Mentor interactions: Quality improvement? ________________",
        "• Online community engagement: Better questions/responses? ___",
        "• Study groups: Leadership or participation changes? ________"
    ]
    y = draw_section(c, y, "🤝 TECH & CAREER INTEGRATION ANALYSIS", tech_social_prompts, 2.8*inch, COLOR_ACCENT, False)
    
    c.showPage()  # Continue on next page
    
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 0.8*inch, f"Week {week} Review (continued)")
    
    y = PAGE_WIDTH - 1.2*inch

    # Pattern recognition and insights  
    insights_prompts = [
        "🔍 PATTERN RECOGNITION:",
        "What behavioral patterns did you notice in yourself?",
        "________________________________________________",
        "What patterns did you observe in others' responses?", 
        "________________________________________________",
        "Which techniques worked best for your personality?",
        "________________________________________________",
        "",
        "💡 BREAKTHROUGH INSIGHTS:",
        "Most significant 'aha' moment: _______________________",
        "How this insight changes your approach: ______________",
        "Application to future situations: ____________________",
        "",
        "🧠 KNOWLEDGE MODULE APPLICATION:",
        "How did pre-week learning help your practice?",
        "________________________________________________",
        "Which concepts need more study? ____________________",
        "Real-world examples you discovered: _________________"
    ]
    y = draw_section(c, y, "🧩 PATTERN RECOGNITION & INSIGHTS", insights_prompts, 3.2*inch, COLOR_WISDOM, False)
    
    # Success metrics specific to the week
    metrics_prompts = [
        "📊 WEEK-SPECIFIC SUCCESS METRICS:",
        WEEKLY_METRICS.get(week, "No metric provided for this week."),
        "",
        "📈 METRIC ACHIEVEMENT RATING:",
        "How well did you achieve this week's specific metric?",
        "☐ Exceeded expectations (9-10/10)",
        "☐ Met expectations (7-8/10)", 
        "☐ Partially met expectations (5-6/10)",
        "☐ Below expectations (1-4/10)",
        "",
        "📋 EVIDENCE OF SUCCESS:",
        "Specific examples that prove you're improving:",
        "1. ____________________________________________",
        "2. ____________________________________________",
        "3. ____________________________________________"
    ]
    y = draw_section(c, y, "🎯 SUCCESS METRICS EVALUATION", metrics_prompts, 2.5*inch, COLOR_PRIMARY, False)
    
    # Next week preparation or final mastery assessment
    if week < 7:
        prep_prompts = [
            f"🎯 WEEK {week+1} STRATEGIC PREPARATION:",
            f"Based on this week's learning, how will you customize Week {week+1}?",
            "________________________________________________",
            f"Specific goals for Week {week+1}: __________________",
            "Areas that need extra focus: _______________________",
            "",
            f"📅 WEEK {week+1} LEARNING SCHEDULE:",
            f"When will you complete Week {week+1}'s knowledge module?",
            "Day: _______ Time: _______ Duration: _____ minutes",
            "",
            "🤝 ACCOUNTABILITY PLAN:",
            "Who will help keep you accountable next week?",
            "How will you track your daily progress?",
            "What rewards will you give yourself for completion?"
        ]
        draw_section(c, y, f"🚀 WEEK {week+1} PREPARATION STRATEGY", prep_prompts, 2.3*inch, COLOR_ENERGY, False)
    else:
        mastery_prompts = [
            "🏆 FINAL MASTERY ASSESSMENT:",
            "Compare your abilities now vs. Week 1:",
            "Self-awareness: Week 1: ___/10 → Now: ___/10",
            "Response control: Week 1: ___/10 → Now: ___/10",
            "Active listening: Week 1: ___/10 → Now: ___/10",
            "Clear communication: Week 1: ___/10 → Now: ___/10",
            "Empathy: Week 1: ___/10 → Now: ___/10",
            "Conflict resolution: Week 1: ___/10 → Now: ___/10",
            "Relationship building: Week 1: ___/10 → Now: ___/10",
            "",
            "🎯 ONGOING MASTERY PLAN:",
            "Daily practice routine: _____________________________",
            "Weekly skill maintenance: ___________________________",
            "Monthly skill advancement: __________________________",
            "Quarterly assessment: ______________________________"
        ]
        draw_section(c, y, "🏆 FINAL TRANSFORMATION ASSESSMENT", mastery_prompts, 2.5*inch, COLOR_ENERGY, False)
    
    c.showPage()

def draw_achievement_badges_page(c):
    """Draws the enhanced achievement badges page with more categories."""
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(COLOR_ENERGY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.2*inch, "Social & Career Achievement Badges")
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_ACCENT)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, "Track Your Transformation Journey")
    
    # Decorative line
    c.setStrokeColor(COLOR_ENERGY)
    c.setLineWidth(3)
    c.line(MARGIN, PAGE_HEIGHT - 1.7*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 1.7*inch)
    
    y = PAGE_HEIGHT - 2*inch
    
    # Technical Career Badges
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(COLOR_PRIMARY)
    c.drawString(MARGIN, y, "💻 TECHNICAL CAREER BADGES:")
    y -= 0.3*inch
    
    tech_badges = [
        "☐ 🤝 First successful code review collaboration",
        "☐ 💡 First LinkedIn tech connection made",
        "☐ 🚀 First open-source collaborator onboarded",
        "☐ 🎯 First AI project demo delivered (NEETPrepGPT)",
        "☐ 📞 First technical mentorship call completed",
        "☐ 🗣️ Pitched your project to a potential user/stakeholder",
        "☐ 👥 Organized a study or collaboration session",
        "☐ 🏆 Received positive feedback on communication in team setting"
    ]
    
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    for badge in tech_badges:
        draw_checkbox(c, MARGIN + 0.2*inch, y-3)
        c.drawString(MARGIN + 0.45*inch, y, badge[2:])
        y -= 0.3*inch
    
    y -= 0.2*inch
    
    # Social Mastery Badges
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y, "🌟 SOCIAL MASTERY BADGES:")
    y -= 0.3*inch
    
    social_badges = [
        "☐ 😊 First comfortable conversation with stranger",
        "☐ 👂 First successful active listening session",
        "☐ 💬 First 'difficult conversation' navigated successfully",
        "☐ 🤝 First conflict resolved through communication",
        "☐ 🎭 First time staying calm under social pressure",
        "☐ 💪 First confident presentation of technical idea",
        "☐ 🔄 First successful introduction between two people",
        "☐ 🌱 First vulnerable sharing that deepened relationship"
    ]
    
    for badge in social_badges:
        draw_checkbox(c, MARGIN + 0.2*inch, y-3)
        c.drawString(MARGIN + 0.45*inch, y, badge[2:])
        y -= 0.3*inch
    
    y -= 0.2*inch
    
    # Leadership Development Badges
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(COLOR_ACCENT)
    c.drawString(MARGIN, y, "👑 LEADERSHIP DEVELOPMENT BADGES:")
    y -= 0.3*inch
    
    leadership_badges = [
        "☐ 🎤 First time leading a technical discussion",
        "☐ 🌉 First successful bridge between conflicting viewpoints",
        "☐ 📈 First measurable improvement in team communication",
        "☐ 🎯 First time others sought your advice on communication",
        "☐ 🚀 First successful project pitch to stakeholders",
        "☐ 💼 First professional networking event attended confidently"
    ]
    
    for badge in leadership_badges:
        draw_checkbox(c, MARGIN + 0.2*inch, y-3)
        c.drawString(MARGIN + 0.45*inch, y, badge[2:])
        y -= 0.3*inch
    
    y -= 0.4*inch
    
    # Custom achievements section
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(COLOR_ENERGY)
    c.drawString(MARGIN, y, "🏆 YOUR CUSTOM ACHIEVEMENT BADGES:")
    y -= 0.3*inch
    
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawString(MARGIN, y, "Add your personal milestones and celebrate every victory:")
    
    custom_lines = [
        "☐ _________________________________________________",
        "☐ _________________________________________________", 
        "☐ _________________________________________________",
        "☐ _________________________________________________",
        "☐ _________________________________________________",
        "☐ _________________________________________________"
    ]
    
    y -= 0.4*inch
    for line in custom_lines:
        draw_checkbox(c, MARGIN + 0.2*inch, y-3)
        c.setStrokeColor(COLOR_TEXT_BODY)
        c.setLineWidth(0.5)
        c.line(MARGIN + 0.45*inch, y-5, PAGE_WIDTH - MARGIN - 0.2*inch, y-5)
        y -= 0.35*inch

    # Motivational footer
    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_WISDOM)
    c.drawCentredString(PAGE_WIDTH/2, y, "🌟 Every badge represents growth. Every growth multiplies your impact. 🌟")
    c.setFont("Helvetica", 11)
    c.drawCentredString(PAGE_WIDTH/2, y-0.3*inch, "Your technical skills + communication mastery = Unstoppable career acceleration")

    c.showPage()

def _estimate_total_pages() -> int:
    """Estimate total pages in the generated journal."""
    bio = 1
    intro = 1
    weeks = 7
    knowledge = weeks
    daily_pages = weeks * 7 * 3  # Now 3 pages per day
    weekly_reviews = weeks * 2   # Now 2 pages per week
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

        c.setTitle(f"Enhanced Social Mastery Journal for {USER_PROFILE['name']}")
        c.setAuthor(USER_PROFILE['name'])
        c.setSubject(f"7-week program for {USER_PROFILE['career_goal']}")
        c.setCreator("Enhanced Progressive Social Mastery Generator Script v3.0")

        start_date = start_date or date.today()
        if isinstance(start_date, str):
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            except Exception:
                logger.warning("start_date string provided but could not parse, using today instead.")
                start_date = date.today()

        logger.info("Generating enhanced journal for %s, starting %s -> %s", USER_PROFILE['name'], start_date.isoformat(), output_file)
        logger.info("Estimated total pages: %s", _estimate_total_pages())

        # Personalized Bio Page
        draw_intro_bio_page(c)

        # Enhanced intro page with master-level design
        c.setFont("Helvetica-Bold", 32)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.8*inch, "PROGRESSIVE SOCIAL")
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.3*inch, "MASTERY SYSTEM")
        
        c.setFont("Helvetica-Bold", 18)
        c.setFillColor(COLOR_TEXT_HEADER)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.8*inch, "An Engineering Approach to Communication Excellence")
        
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 3.2*inch, "From Introvert to Influential Communicator")
        
        # Enhanced decorative line
        c.setStrokeColor(COLOR_PRIMARY)
        c.setLineWidth(4)
        c.line(PAGE_WIDTH/2 - 3*inch, PAGE_HEIGHT - 3.5*inch, PAGE_WIDTH/2 + 3*inch, PAGE_HEIGHT - 3.5*inch)
        
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(COLOR_ENERGY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 4*inch, "🔧 MASTER-LEVEL SYSTEM FEATURES:")
        
        features_text = [
            "✅ Progressive Difficulty: Each week builds on the last with scaffolded challenges",
            "✅ Scientific Knowledge Modules: Neuroscience-backed theory before practice", 
            "✅ Concrete Metrics: Measurable success criteria for every challenge",
            "✅ Daily Study Notes: Master-level insights from psychology and communication",
            "✅ Comprehensive TODOs: Detailed preparation checklists for peak performance",
            "✅ Multi-Page Daily Tracking: Deep reflection and progress monitoring",
            "✅ Evidence-Based: Rooted in psychology, neuroscience, and communication research",
            "✅ Career Integration: Specifically designed for AI developers and technical founders"
        ]
        
        y_pos = PAGE_HEIGHT - 4.4*inch
        c.setFont("Helvetica", 12)
        c.setFillColor(COLOR_TEXT_BODY)
        for feature in features_text:
            c.drawCentredString(PAGE_WIDTH/2, y_pos, feature)
            y_pos -= 0.25*inch
        
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(COLOR_WISDOM)
        c.drawCentredString(PAGE_WIDTH/2, y_pos - 0.4*inch, "🚀 YOUR TRANSFORMATION COMMITMENT:")
        
        mission_text = [
            "This system will transform you from socially anxious to socially confident.",
            "You will master the engineering principles of human connection.",
            "Every interaction becomes data. Every challenge builds competence.",
            "In 7 weeks, you will have the communication skills to accelerate your career.",
            "Your technical expertise + social mastery = Unlimited potential.",
            "Commit fully. Follow the system. Become unstoppable."
        ]
        
        y_mission = y_pos - 0.8*inch
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(COLOR_TEXT_BODY)
        for line in mission_text:
            c.drawCentredString(PAGE_WIDTH/2, y_mission, line)
            y_mission -= 0.25*inch
        
        c.showPage()
        
        day_offset = 0
        for week in range(1, 8):
            # Knowledge module page
            draw_knowledge_module_page(c, week)
            
            # Daily pages (now 3 pages per day)
            for day in range(1, 8):
                current_date = start_date + timedelta(days=day_offset)
                date_str = current_date.strftime('%A, %B %d, %Y')
                
                draw_header(c, week, day, date_str)
                draw_daily_page(c, date_str, week, day)
                
                day_offset += 1
            
            # Weekly review (now 2 pages)
            draw_weekly_review_page(c, week)
        
        # Final transformation assessment
        c.setFont("Helvetica-Bold", 28)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.8*inch, "SOCIAL MASTERY ACHIEVED")
        
        c.setFont("Helvetica-Bold", 18)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.4*inch, "Final Transformation Assessment")
        
        # Enhanced decorative line
        c.setStrokeColor(COLOR_PRIMARY)
        c.setLineWidth(4)
        c.line(PAGE_WIDTH/2 - 2.5*inch, PAGE_HEIGHT - 2.7*inch, PAGE_WIDTH/2 + 2.5*inch, PAGE_HEIGHT - 2.7*inch)
        
        y = PAGE_HEIGHT - 3.2*inch
        final_prompts = [
            "🏆 BEFORE vs. AFTER ASSESSMENT:",
            "Week 1 Overall Comfort Level: ___/10    Week 7 Comfort Level: ___/10",
            "Week 1 Confidence in Tech Discussions: ___/10    Week 7: ___/10",
            "Week 1 Networking Ability: ___/10    Week 7: ___/10",
            "",
            "💻 Most Significant Transformation in your developer workflow:",
            "",
            "",
            "🚀 New Social Superpowers Acquired:",
            "1. _______________________________________________",
            "2. _______________________________________________", 
            "3. _______________________________________________",
            "4. _______________________________________________",
            "",
            "🎯 NEETPREPGPT IMPACT: How will these skills accelerate your project?",
            "• User research and feedback gathering: ___________________",
            "• Team building and collaboration: ________________________",
            "• Investor/stakeholder communication: ____________________",
            "• Community building and user engagement: ________________",
            "",
            "🏢 CAREER ACCELERATION IMPACT:",
            "• Technical mentorship seeking: ___________________________",
            "• Job interview confidence: _______________________________",
            "• Leadership opportunities: _______________________________",
            "• Professional network quality: ___________________________"
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
                
                wrapped_prompt = textwrap.wrap(prompt, width=85)
                for line in wrapped_prompt:
                    if len(line.strip()) > 0:
                        if line.startswith('•'):
                            c.drawString(MARGIN + 0.3*inch, y, line)
                        else:
                            c.drawString(MARGIN, y, line)
                    y -= 0.25*inch
            else:
                y -= 0.25*inch

        y -= 0.4*inch
        
        # Ongoing practice plan
        practice_prompts = [
            "📅 ONGOING PRACTICE PLAN:",
            "Daily (5-10 mins): ___________________________________",
            "Weekly (30 mins): ____________________________________", 
            "Monthly (1 hour): ____________________________________",
            "Quarterly assessment: ________________________________",
            "",
            "🎯 6-MONTH GOALS:",
            "Social skills: _______________________________________",
            "Career advancement: __________________________________",
            "NEETPrepGPT milestones: ______________________________",
            "",
            "🔄 CONTINUOUS IMPROVEMENT CYCLE:",
            "☐ Monthly skill assessment and goal adjustment",
            "☐ Quarterly review of communication effectiveness", 
            "☐ Semi-annual update of practice techniques",
            "☐ Annual celebration of transformation journey"
        ]
        
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(COLOR_WISDOM)
        for prompt in practice_prompts:
            if prompt.strip():
                if prompt.endswith(':'):
                    c.setFont("Helvetica-Bold", 12)
                    c.setFillColor(COLOR_WISDOM)
                elif prompt.startswith('☐'):
                    c.setFont("Helvetica", 11)
                    c.setFillColor(COLOR_TEXT_BODY)
                    draw_checkbox(c, MARGIN, y-3)
                    c.drawString(MARGIN + 0.25*inch, y, prompt[2:])
                    y -= 0.25*inch
                    continue
                else:
                    c.setFont("Helvetica", 11)
                    c.setFillColor(COLOR_TEXT_BODY)
                
                wrapped_prompt = textwrap.wrap(prompt, width=85)
                for line in wrapped_prompt:
                    if len(line.strip()) > 0:
                        c.drawString(MARGIN, y, line)
                    y -= 0.25*inch
            else:
                y -= 0.2*inch

        y -= 0.6*inch
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(COLOR_ENERGY)
        c.drawCentredString(PAGE_WIDTH/2, y, "🎉 CONGRATULATIONS! 🎉")
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(COLOR_TEXT_BODY)
        c.drawCentredString(PAGE_WIDTH/2, y - 0.35*inch, "You now possess the systematic communication skills")
        c.drawCentredString(PAGE_WIDTH/2, y - 0.6*inch, "to build any relationship and influence any outcome.")
        c.drawCentredString(PAGE_WIDTH/2, y - 0.85*inch, "Your AI/health-tech career will benefit immeasurably.")
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, y - 1.15*inch, "You are now a master of both code and communication.")
        c.showPage()

        # Enhanced Achievement Badges Page
        draw_achievement_badges_page(c)
        
        c.save()
        logger.info("✅ Successfully created enhanced journal: %s", output_file)
        logger.info("🎨 Generated master-level progressive social mastery system:")
        logger.info("   • 1 Personalized Bio Page")
        logger.info("   • 1 Enhanced Master-Level Introduction")
        logger.info("   • 7 Comprehensive Knowledge Module pages")
        logger.info("   • 147 Daily Practice pages (3 pages per day with deep tracking)")
        logger.info("   • 14 Weekly Review pages (2 pages per week)")
        logger.info("   • 1 Comprehensive Final Assessment page")
        logger.info("   • 1 Enhanced Achievement Badge Page")
        logger.info("   • Total pages: %s", _estimate_total_pages())
        logger.info("🚀 Enhanced features added:")
        logger.info("   • Daily study notes with scientific insights")
        logger.info("   • Comprehensive TODO checklists")
        logger.info("   • Multiple tracking checkboxes")
        logger.info("   • Larger fonts and master-level design")
        logger.info("   • 3-page daily format for comprehensive reflection")
        logger.info("   • Enhanced career integration focus")

    except Exception as exc:
        logger.exception("Failed to generate journal: %s", exc)
        if c:
            try:
                c.save()
            except Exception:
                pass
        raise

def _parse_args():
    parser = argparse.ArgumentParser(description="Generate an Enhanced Progressive Social Mastery Journal PDF.")
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
        print("✅ Journal generation completed successfully!")
    except Exception as e:
        logger.error("Generation failed: %s", e)
        print(f"❌ Error: {e}")