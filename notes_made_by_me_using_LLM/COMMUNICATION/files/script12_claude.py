# Enhanced Progressive Social Mastery Engineering Journal for AI/Health-Tech Developers
# Optimized for ambitious developers transitioning to entrepreneurship
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
from typing import List, Optional, Dict
import json

# --- Enhanced Setup ---
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("SocialMasteryJournal")

# --- Modern Color Palette ---
COLOR_PRIMARY = HexColor('#0066CC')      # Tech blue
COLOR_ACCENT = HexColor('#00CC66')       # Success green
COLOR_WARN = HexColor('#FF3366')         # Alert red
COLOR_ENERGY = HexColor('#FF9900')       # Motivation orange
COLOR_WISDOM = HexColor('#9933CC')       # Insight purple
COLOR_TECH = HexColor('#6699FF')         # Tech accent
COLOR_BG_LIGHT = HexColor('#F8F9FA')
COLOR_TEXT_HEADER = HexColor('#1A1A1A')
COLOR_TEXT_BODY = HexColor('#333333')

# --- Configuration ---
FILENAME = "AI_Developer_Social_Mastery_Journal.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.6 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
STYLES = getSampleStyleSheet()

# --- User Profile Integration ---
USER_PROFILE = {
    "name": "AI/Health-Tech Developer",
    "location": "Prayagraj, UP",
    "main_project": "NEETPrepGPT & Symptom2Specialist Bot",
    "career_goal": "AI Entrepreneur & Health-Tech Innovator",
    "learning_focus": [
        "Technical Communication", "Network Building", "Product Pitching",
        "Team Leadership", "Investor Relations", "Community Building",
        "Developer Advocacy", "Technical Writing"
    ],
    "target_network": [
        "AI Researchers", "Health-Tech Founders", "Medical Professionals",
        "Potential Co-founders", "Investors", "Developer Community",
        "Open Source Contributors", "Technical Mentors"
    ]
}

# --- Enhanced Knowledge Modules with Tech Focus ---
KNOWLEDGE_MODULES = {
    1: {
        "title": "Technical Communication & Emotional Intelligence",
        "learning_resources": [
            "Book: 'The Pragmatic Programmer' - Communication Chapter",
            "YouTube: 'How to Explain Technical Concepts' by Kevin Markham",
            "Article: 'Emotional Intelligence for Engineers' (Harvard Business Review)",
            "Podcast: 'Developer Tea' episodes on communication skills",
            "Practice: Explain your AI project in 30 seconds, 2 minutes, and 10 minutes"
        ],
        "key_concepts": [
            "Translating technical complexity for different audiences",
            "Managing frustration during debugging and problem-solving",
            "Reading room dynamics during technical presentations",
            "Balancing confidence with intellectual humility",
            "Identifying emotional triggers in high-pressure situations"
        ],
        "tech_application": "Use when presenting NEETPrepGPT to non-technical stakeholders, explaining AI concepts to medical professionals, or handling feedback on your code."
    },
    2: {
        "title": "Startup Pitch Mastery & Response Control",
        "learning_resources": [
            "YouTube: 'How to Pitch Your Startup' by Y Combinator",
            "Book: 'Venture Deals' by Brad Feld - Presentation sections",
            "Article: 'The Neuroscience of Startup Pitching'",
            "Video: Watch 10 successful health-tech startup pitches",
            "Practice: Record yourself pitching, identify nervous habits"
        ],
        "key_concepts": [
            "Controlling nerves during investor presentations",
            "Handling tough questions without defensiveness",
            "Managing excitement vs. appearing measured and credible",
            "Responding to technical challenges from domain experts",
            "Maintaining composure during rejection or criticism"
        ],
        "tech_application": "Essential for fundraising, demo days, technical interviews, and presenting at conferences."
    },
    3: {
        "title": "Technical Leadership & Active Listening",
        "learning_resources": [
            "Book: 'The Manager's Path' by Camille Fournier",
            "YouTube: 'Technical Leadership' by Charity Majors",
            "Article: 'Code Reviews and Empathy' by April Wensel",
            "Podcast: 'Software Engineering Daily' leadership episodes",
            "Practice: Lead a code review session focusing on understanding before judging"
        ],
        "key_concepts": [
            "Listening to understand technical requirements, not just to respond",
            "Drawing out ideas from introverted team members",
            "Understanding user needs beyond stated requirements",
            "Active listening during pair programming sessions",
            "Hearing the emotional subtext in technical feedback"
        ],
        "tech_application": "Critical for gathering accurate requirements, leading technical teams, and understanding user pain points for your health-tech products."
    },
    4: {
        "title": "Developer Advocacy & Clear Communication",
        "learning_resources": [
            "Book: 'Developer Relations: How to Build and Grow a Successful Developer Program'",
            "YouTube: 'Technical Writing' by Google Developers",
            "Article: 'Writing Great Documentation' by Divio",
            "Twitter: Follow top developer advocates, analyze their communication",
            "Practice: Write a technical blog post explaining a complex AI concept simply"
        ],
        "key_concepts": [
            "Making technical content accessible without dumbing it down",
            "Using precise language to prevent misunderstandings",
            "Structuring complex information logically",
            "Assertive communication in technical discussions",
            "Setting clear expectations and boundaries with stakeholders"
        ],
        "tech_application": "Essential for technical documentation, API guides, user onboarding, and building developer communities around your products."
    },
    5: {
        "title": "User Empathy & Product Development",
        "learning_resources": [
            "Book: 'The Mom Test' by Rob Fitzpatrick",
            "YouTube: 'User Empathy in Product Design' by IDEO",
            "Article: 'Empathy Maps for Software Development'",
            "Course: 'Design Thinking for Software Engineers' (Stanford)",
            "Practice: Interview 5 medical students about their study challenges"
        ],
        "key_concepts": [
            "Understanding user pain points beyond surface complaints",
            "Empathizing with non-technical users of technical products",
            "Seeing your product through the eyes of different user personas",
            "Cultural empathy when building for diverse markets",
            "Balancing technical possibilities with user needs"
        ],
        "tech_application": "Crucial for building NEETPrepGPT features that actually help students, not just showcase AI capabilities."
    },
    6: {
        "title": "Technical Conflict Resolution & Team Dynamics",
        "learning_resources": [
            "Book: 'Team Topologies' by Matthew Skelton",
            "YouTube: 'Resolving Technical Disagreements' by ThoughtWorks",
            "Article: 'Psychological Safety in Engineering Teams' (Google re:Work)",
            "Podcast: 'Engineering Culture' series by various tech companies",
            "Practice: Facilitate a technical architecture discussion with conflicting viewpoints"
        ],
        "key_concepts": [
            "Separating technical merit from personal ego",
            "Finding win-win solutions in architecture decisions",
            "De-escalating heated technical debates",
            "Addressing performance issues with empathy",
            "Building consensus across technical and business stakeholders"
        ],
        "tech_application": "Necessary for managing technical debt discussions, handling code review conflicts, and aligning technical decisions with business goals."
    },
    7: {
        "title": "Network Building & Community Leadership",
        "learning_resources": [
            "Book: 'Never Eat Alone' by Keith Ferrazzi - Tech networking chapters",
            "YouTube: 'Building in Public' by Indie Hackers",
            "Article: 'Growing Your Technical Network' by Dev.to",
            "Twitter: Study how successful AI founders build their following",
            "Practice: Host a local AI/health-tech meetup or online workshop"
        ],
        "key_concepts": [
            "Building relationships before you need them",
            "Adding value to the community before asking for help",
            "Maintaining relationships across time zones and schedules",
            "Leveraging online platforms for authentic relationship building",
            "Creating win-win collaborations and partnerships"
        ],
        "tech_application": "Essential for finding co-founders, attracting users, building partnerships with medical institutions, and establishing thought leadership."
    }
}

# --- Tech-Focused Progressive Challenges ---
PROGRESSIVE_CHALLENGES = {
    1: [
        "Day 1: Introduce yourself to 3 people in a tech forum/Discord with your current project. Track responses.",
        "Day 2: Comment meaningfully on 5 technical posts, leading to 2 brief conversations.",
        "Day 3: Ask one technical question in a public forum and engage with all responders.",
        "Day 4: Share one learning insight about your AI project on LinkedIn/Twitter.",
        "Day 5: Direct message 1 AI researcher with a thoughtful question about their work.",
        "Day 6: Join a virtual tech meetup and introduce yourself to 3 attendees.",
        "Day 7: Start a technical discussion thread and actively engage with all participants."
    ],
    2: [
        "Day 1: Practice the 'tactical pause' during your next technical code review or debugging session.",
        "Day 2: When receiving technical feedback, ask clarifying questions before defending your approach.",
        "Day 3: Respond to one critical GitHub issue without immediate defensiveness.",
        "Day 4: During a technical discussion, acknowledge one valid point from someone you disagree with.",
        "Day 5: Transform one technical complaint into a specific feature request or bug report.",
        "Day 6: Practice the 6-second rule when encountering a frustrating bug or system failure.",
        "Day 7: Lead a technical discussion where you maintain composure despite disagreement."
    ],
    3: [
        "Day 1: In your next technical meeting, focus only on listening without planning your response.",
        "Day 2: Ask 'What I understood is...' and confirm requirements in one project discussion.",
        "Day 3: Ask 2 clarifying questions about user needs before proposing any technical solution.",
        "Day 4: In a code review, identify and acknowledge the reviewer's underlying concern.",
        "Day 5: Practice empathic listening with a non-technical stakeholder explaining their needs.",
        "Day 6: Listen to a user complaint and identify 3 different underlying problems.",
        "Day 7: Conduct one 30-minute user interview focusing purely on understanding their workflow."
    ],
    4: [
        "Day 1: Explain one technical concept using 'I believe this approach works because...' instead of 'This is obviously...'",
        "Day 2: Make one technical request using 'Would it be possible to...' instead of 'Just change...'",
        "Day 3: Present one technical solution clearly stating assumptions and limitations.",
        "Day 4: Share one technical challenge using 'I'm struggling with... because...' format.",
        "Day 5: Set one clear boundary about scope or timeline using assertive but respectful language.",
        "Day 6: Ask for technical help by clearly stating what you've tried and what you need.",
        "Day 7: Give technical feedback using specific, actionable language without personal judgments."
    ],
    5: [
        "Day 1: Ask a team member 'What's the most challenging part of your current project?'",
        "Day 2: Before disagreeing with a technical decision, state their perspective back to them first.",
        "Day 3: Ask a user about their biggest frustrations with existing solutions in their field.",
        "Day 4: Share something you're genuinely uncertain about in your technical work.",
        "Day 5: When someone reports a bug, focus on understanding their workflow, not just the symptoms.",
        "Day 6: Spend a full conversation understanding why someone chose a different technical approach.",
        "Day 7: Interview someone outside tech about how they currently solve the problem your product addresses."
    ],
    6: [
        "Day 1: Address one small technical disagreement directly instead of letting it fester.",
        "Day 2: Use collaborative language ('How might we...') in one architecture discussion.",
        "Day 3: Give constructive code review feedback focusing on code quality, not personal style.",
        "Day 4: Apologize specifically for one technical mistake without excuses or blame-shifting.",
        "Day 5: Find one area of technical agreement in a discussion with someone you disagree with.",
        "Day 6: Turn one technical conflict into a problem-solving session with measurable outcomes.",
        "Day 7: Have the technical conversation you've been avoiding using structured conflict resolution."
    ],
    7: [
        "Day 1: Send specific appreciation to someone who helped you with a technical challenge.",
        "Day 2: Reach out to one developer you admire but haven't contacted in months.",
        "Day 3: Ask an industry expert for advice on a specific technical or career challenge.",
        "Day 4: Invite someone to collaborate on a small technical project or code review.",
        "Day 5: Introduce two developers who should know each other for mutual benefit.",
        "Day 6: Offer specific technical help to someone in your network without them asking.",
        "Day 7: Plan 3 concrete actions to deepen your relationship with key technical contacts."
    ]
}

# --- Success Metrics Tailored for Developers ---
WEEKLY_METRICS = {
    1: "Network Expansion: Track new meaningful connections made. Measure: New LinkedIn/GitHub connections + quality of conversations (1-10) + follow-up actions taken",
    2: "Technical Composure: Measure response control in technical situations. Track: Pause-before-response rate + feedback quality received + conflict de-escalation success",
    3: "Understanding Accuracy: Measure how well you understand others' technical needs. Track: Confirmation accuracy rate + user requirement clarity + solution alignment score",
    4: "Communication Precision: Track clarity of your technical communication. Track: Questions-per-explanation ratio + stakeholder comprehension rate + actionable feedback quality",
    5: "User Insight Quality: Measure depth of empathic understanding. Track: New user insights discovered + problem validation accuracy + feature request quality",
    6: "Resolution Effectiveness: Track successful technical conflict resolution. Track: Conflicts resolved vs escalated + team satisfaction + technical debt discussions led",
    7: "Relationship Investment ROI: Measure network building success. Track: Meaningful follow-ups completed + collaboration opportunities created + mutual value exchanges initiated"
}

# --- Tech-Specific Goal Templates ---
GOAL_TEMPLATES = {
    1: "My specific goal this week: Build my technical network by connecting with [specific type of developer/researcher] to support my [NEETPrepGPT/health-tech] goals.",
    2: "My specific goal this week: Maintain composure during [technical presentations/code reviews/user feedback] to be seen as a confident technical leader.",
    3: "My specific goal this week: Become a better listener in [user interviews/technical requirements gathering/team meetings] to build better products.",
    4: "My specific goal this week: Communicate technical concepts clearly to [investors/users/medical professionals] without losing precision or credibility.",
    5: "My specific goal this week: Develop deeper empathy for [medical students/healthcare workers/end users] to build more useful AI solutions.",
    6: "My specific goal this week: Resolve [specific technical disagreement/architectural debate/team conflict] using structured communication approaches.",
    7: "My specific goal this week: Strengthen my [developer/health-tech/AI research] network to support my transition from developer to entrepreneur."
}

# --- Achievement System ---
ACHIEVEMENT_BADGES = {
    "networking": [
        "🔗 First meaningful LinkedIn connection made",
        "💬 First technical discussion thread started", 
        "🎤 First virtual meetup participation",
        "📝 First technical blog post shared",
        "🤝 First collaboration proposal sent"
    ],
    "leadership": [
        "👥 First technical meeting led",
        "📋 First code review session facilitated",
        "🎯 First project requirements gathered",
        "🏆 First team conflict successfully resolved",
        "🚀 First product demo delivered"
    ],
    "growth": [
        "📈 First week completed with 100% challenge completion",
        "💡 First major breakthrough insight recorded",
        "🎭 First presentation given without excessive nerves",
        "📊 First user interview conducted professionally",
        "🔧 First technical concept explained successfully to non-tech audience"
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
            "key_concepts": ["No key concepts available."],
            "tech_application": "No application guidance available."
        }
    return module

def draw_user_bio_page(c):
    """Personalized bio page for AI/Health-Tech developers."""
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.2*inch, "AI Developer Social Mastery Journal")
    
    c.setFont("Helvetica", 13)
    c.setFillColor(COLOR_TEXT_HEADER)
    y = PAGE_HEIGHT - 1.8*inch
    c.drawString(MARGIN, y, f"Profile: {USER_PROFILE['name']}")
    c.drawString(MARGIN, y-0.25*inch, f"Location: {USER_PROFILE['location']}")
    c.drawString(MARGIN, y-0.5*inch, f"Current Projects: {USER_PROFILE['main_project']}")
    c.drawString(MARGIN, y-0.75*inch, f"Career Goal: {USER_PROFILE['career_goal']}")
    
    c.drawString(MARGIN, y-1.1*inch, "Technical Communication Focus:")
    for i, topic in enumerate(USER_PROFILE["learning_focus"], 1):
        c.drawString(MARGIN + 0.3*inch, y-1.1*inch-(i*0.18*inch), f"{i}. {topic}")
    
    target_y = y-1.1*inch-(len(USER_PROFILE["learning_focus"])*0.18*inch)-0.3*inch
    c.drawString(MARGIN, target_y, "Target Network:")
    for i, target in enumerate(USER_PROFILE["target_network"], 1):
        c.drawString(MARGIN + 0.3*inch, target_y-(i*0.18*inch), f"• {target}")
    
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_WISDOM)
    final_y = target_y-(len(USER_PROFILE["target_network"])*0.18*inch)-0.3*inch
    c.drawString(MARGIN, final_y, "This journal bridges technical expertise with communication mastery.")
    c.drawString(MARGIN, final_y-0.2*inch, "Transform from skilled developer to influential tech leader.")
    c.showPage()

def draw_enhanced_knowledge_module_page(c, week):
    """Enhanced knowledge module with tech applications."""
    module = _safe_get_module(week)
    
    # Title section
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(COLOR_TECH)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, f"WEEK {week} KNOWLEDGE MODULE")
    
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.8*inch, module["title"])
    
    y = PAGE_HEIGHT - 2.3*inch
    
    # Learning resources with tech focus
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, y, "🎓 TECHNICAL LEARNING RESOURCES:")
    y -= 0.3*inch
    
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    for i, resource in enumerate(module["learning_resources"], 1):
        wrapped = textwrap.wrap(resource, width=90)
        for line_num, line in enumerate(wrapped):
            if line_num == 0:
                c.drawString(MARGIN + 0.2*inch, y, f"{i}. {line}")
            else:
                c.drawString(MARGIN + 0.45*inch, y, line)
            y -= 0.22*inch
    
    y -= 0.2*inch
    
    # Key concepts
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, y, "⚡ KEY TECHNICAL COMMUNICATION CONCEPTS:")
    y -= 0.3*inch
    
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    for concept in module["key_concepts"]:
        wrapped = textwrap.wrap(concept, width=90)
        for i, line in enumerate(wrapped):
            prefix = "• " if i == 0 else "  "
            c.drawString(MARGIN + 0.2*inch, y, prefix + line)
            y -= 0.2*inch
    
    y -= 0.2*inch
    
    # Tech application section
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_ENERGY)
    c.drawString(MARGIN, y, "🚀 DIRECT APPLICATION TO YOUR PROJECTS:")
    y -= 0.3*inch
    
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    tech_app = module.get("tech_application", "Apply these concepts to your technical work.")
    wrapped_app = textwrap.wrap(tech_app, width=110)
    for line in wrapped_app:
        c.drawString(MARGIN + 0.2*inch, y, line)
        y -= 0.22*inch
    
    y -= 0.3*inch
    
    # Personal goal with tech context
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y, "🎯 MY PERSONALIZED GOAL:")
    y -= 0.3*inch
    
    goal_template = GOAL_TEMPLATES.get(week, "Set a personal goal for this week.")
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    wrapped_goal = textwrap.wrap(goal_template, width=110)
    for line in wrapped_goal:
        c.drawString(MARGIN, y, line)
        y -= 0.22*inch
    
    # Goal customization space
    y -= 0.2*inch
    c.setStrokeColor(lightgrey)
    c.setLineWidth(0.5)
    for i in range(4):
        c.line(MARGIN, y - (i * 0.2*inch), PAGE_WIDTH - MARGIN, y - (i * 0.2*inch))
    
    y -= 1*inch
    
    # Success metrics
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_ACCENT)
    c.drawString(MARGIN, y, "📊 THIS WEEK'S SUCCESS METRICS:")
    y -= 0.3*inch
    
    metric = WEEKLY_METRICS.get(week, "No metric defined.")
    c.setFont("Helvetica", 10)
    c.setFillColor(COLOR_TEXT_BODY)
    wrapped_metric = textwrap.wrap(metric, width=110)
    for line in wrapped_metric:
        c.drawString(MARGIN, y, line)
        y -= 0.2*inch
    
    c.showPage()

def draw_tech_achievement_badges_page(c):
    """Achievement badges page with tech focus."""
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_ENERGY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, "Technical Communication Achievement Badges")
    
    y = PAGE_HEIGHT - 2.2*inch
    
    for category, badges in ACHIEVEMENT_BADGES.items():
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(COLOR_TEXT_HEADER)
        c.drawString(MARGIN, y, f"{category.upper()} ACHIEVEMENTS:")
        y -= 0.3*inch
        
        c.setFont("Helvetica", 11)
        c.setFillColor(COLOR_TEXT_BODY)
        for badge in badges:
            c.drawString(MARGIN + 0.2*inch, y, f"□ {badge}")
            y -= 0.3*inch
        
        y -= 0.2*inch
    
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(COLOR_WISDOM)
    c.drawString(MARGIN, y, "Track your progress as you build technical leadership skills!")
    c.showPage()

# Use the same helper functions from the original with modifications for tech focus
def draw_header(c, week, day, date_str):
    """Enhanced header with tech progress tracking."""
    c.saveState()
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Week {week}: Technical Communication Lab")
    
    # Progress bar
    progress = (week - 1) / 7.0
    bar_width = 2 * inch
    c.setStrokeColor(COLOR_PRIMARY)
    c.setLineWidth(3)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.1*inch, MARGIN + bar_width, PAGE_HEIGHT - MARGIN - 0.1*inch)
    c.setStrokeColor(COLOR_ACCENT)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.1*inch, MARGIN + (bar_width * progress), PAGE_HEIGHT - MARGIN - 0.1*inch)
    
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Day {day} | {date_str}")
    
    c.setStrokeColor(lightgrey)
    c.setLineWidth(1)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.25*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 0.25*inch)
    c.restoreState()

def draw_section(c, y_pos, title, content_prompts, height, color=COLOR_PRIMARY, include_lines=True):
    """Enhanced section with better formatting."""
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

def draw_tech_challenge_box(c, y_pos, week, day):
    """Tech-focused daily challenge box."""
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
    c.setFillColor(COLOR_ACCENT)
    c.setStrokeColor(COLOR_ACCENT)
    c.roundRect(MARGIN, y_pos - 1.5*inch, CONTENT_WIDTH, 1.5*inch, 0.1*inch, fill=1, stroke=1)
    
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.3*inch, f"⚡ DAY {day} TECHNICAL COMMUNICATION CHALLENGE")
    
    c.setFont("Helvetica-Bold", 10)
    wrapped_ch = textwrap.wrap(challenge, width=110)
    desc_y = y_pos - 0.6*inch
    for line in wrapped_ch:
        c.drawString(MARGIN + 0.2*inch, desc_y, line)
        desc_y -= 0.2*inch
    
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.9*inch, "TECH SUCCESS METRICS:")
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.1*inch, "□ Challenge completed (Yes/No)   □ Technical confidence level: ___/10")
    c.drawString(MARGIN + 0.3*inch, y_pos - 1.3*inch, "□ Key technical insight: ________________________________")
    
    c.restoreState()
    return y_pos - 1.7*inch

def draw_daily_page(c, date_str, week, day):
    """Enhanced daily page with tech-focused challenges and metrics."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    
    # Tech challenge
    y = draw_tech_challenge_box(c, y, week, day)
    
    # Execution tracking with tech focus
    prompts_execution = [
        "PRE-CHALLENGE TECHNICAL MINDSET: How confident do you feel about this technical communication challenge?",
        "",
        "EXECUTION DETAILS: Describe exactly what happened during your technical interaction:",
        "",
        "TECHNICAL CONFIDENCE LEVEL: Rate your confidence (1=imposter syndrome, 10=thought leader): ___/10",
        "",
        "SUCCESS METRICS: Did you achieve the technical communication goal? □ Yes □ Partial □ No",
        "",
        "WHAT WORKED TECHNICALLY: What specific approach resonated with your technical audience?",
        "",
        "TECHNICAL ADJUSTMENT: What will you refine in your next technical presentation/discussion?"
    ]
    y = draw_section(c, y, "⚡ TECHNICAL EXECUTION & METRICS", prompts_execution, 3*inch, COLOR_PRIMARY)
    
    # Tech-focused reflection
    prompts_reflection = [
        "TECHNICAL BREAKTHROUGH: What surprised you about communicating technical concepts today?",
        "",
        "SKILL DEVELOPMENT: Which technical communication skill improved most today?",
        "",
        "PROJECT IMPACT: How will today's communication progress help with NEETPrepGPT/health-tech goals?",
        "",
        "NETWORK BUILDING: What new technical relationships or insights did you gain?",
        "",
        "TOMORROW'S TECHNICAL PREP: How will you build on today's technical communication progress?"
    ]
    y = draw_section(c, y, "💻 TECHNICAL GROWTH REFLECTION", prompts_reflection, 2.2*inch, COLOR_WISDOM)
    
    # Weekly integration section for tech context
    tech_integration = [
        "LINKEDIN/GITHUB SHARE: Did you document this learning publicly? □ Yes □ No",
        "",
        "NETWORK IMPACT: Who in your network could benefit from today's insight?",
        "",
        "PROJECT APPLICATION: How does today's skill directly support your AI/health-tech projects?"
    ]
    draw_section(c, y, "🔗 TECH CAREER INTEGRATION", tech_integration, 1.5*inch, COLOR_TECH)
    
    c.showPage()

def draw_enhanced_weekly_review_page(c, week):
    """Enhanced weekly review with tech career focus."""
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5*inch, f"Week {week} Technical Communication Review")
    
    y = PAGE_HEIGHT - 2*inch
    
    # Quantitative results with tech metrics
    metrics_prompts = [
        "CHALLENGE COMPLETION RATE: ___/7 technical communication challenges completed",
        "",
        "TECHNICAL CONFIDENCE PROGRESSION: Day 1: ___/10  →  Day 7: ___/10 (Growth: ___)",
        "",
        "NETWORK EXPANSION: New LinkedIn connections: ___ GitHub interactions: ___ Forum contributions: ___",
        "",
        "SUCCESS METRIC ACHIEVEMENT: How well did you hit your weekly technical communication metric?",
        WEEKLY_METRICS.get(week, "No metric provided for this week."),
        "",
        "MOST MEASURABLE TECHNICAL IMPROVEMENT: What concrete change can you document?"
    ]
    y = draw_section(c, y, "📊 TECHNICAL COMMUNICATION METRICS", metrics_prompts, 2.5*inch, COLOR_ACCENT, False)
    
    # Qualitative insights with project focus
    insights_prompts = [
        "BIGGEST TECHNICAL BREAKTHROUGH: What was your most significant communication 'aha' moment?",
        "",
        "PROJECT ALIGNMENT: How did improved communication directly benefit NEETPrepGPT development?",
        "",
        "KNOWLEDGE APPLICATION: How did this week's learning improve your technical presentations?",
        "",
        "NETWORK QUALITY: Which new technical relationship has the highest potential value?",
        "",
        "USER EMPATHY GROWTH: How has your understanding of your target users (medical students) deepened?"
    ]
    y = draw_section(c, y, "💡 TECHNICAL INSIGHTS & PROJECT IMPACT", insights_prompts, 2.2*inch, COLOR_WISDOM, False)
    
    # Next week preparation or mastery assessment
    if week < 7:
        prep_prompts = [
            f"WEEK {week+1} TECHNICAL FOCUS: How will you customize next week's challenges for your AI projects?",
            "",
            f"LEARNING SCHEDULE: When will you complete Week {week+1}'s technical communication learning?",
            "",
            "DIFFICULTY SCALING: Should next week's technical challenges be more advanced? Why?",
            "",
            "PROJECT INTEGRATION: How will you apply next week's skills to NEETPrepGPT/Symptom2Specialist?",
            "",
            "NETWORK STRATEGY: Which 3 technical professionals will you focus on connecting with next week?"
        ]
        draw_section(c, y, f"🚀 WEEK {week+1} TECHNICAL PREPARATION", prep_prompts, 2.4*inch, COLOR_ENERGY, False)
    else:
        # Final assessment with career transformation focus
        mastery_prompts = [
            "TRANSFORMATION SUMMARY: How have your technical communication abilities evolved since Week 1?",
            "",
            "SKILL MASTERY LEVELS (Rate 1-10):",
            "Technical Explanation: ___ Pitch Presentation: ___ User Empathy: ___ Team Leadership: ___",
            "Network Building: ___ Conflict Resolution: ___ Community Building: ___",
            "",
            "CAREER IMPACT: How will these skills accelerate your transition from developer to entrepreneur?",
            "",
            "PROJECT SUCCESS PREDICTION: How much more likely are you to succeed with NEETPrepGPT now?",
            "",
            "ONGOING PRACTICE PLAN: How will you maintain these technical communication skills?"
        ]
        draw_section(c, y, "🏆 TECHNICAL LEADERSHIP MASTERY ASSESSMENT", mastery_prompts, 2.6*inch, COLOR_ENERGY, False)
    
    c.showPage()

def create_progressive_social_mastery_journal(start_date: Optional[date] = None, filename: Optional[str] = None):
    """Generate the enhanced AI developer social mastery journal."""
    output_file = filename or FILENAME
    c = None
    try:
        # Ensure output directory exists
        out_dir = os.path.dirname(os.path.abspath(output_file))
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
            logger.debug("Created output directory: %s", out_dir)

        c = canvas.Canvas(output_file, pagesize=A4)

        # Enhanced PDF metadata
        c.setTitle("AI Developer Social Mastery Journal")
        c.setAuthor("AI/Health-Tech Communication System")
        c.setSubject("Technical Communication Mastery for AI Developers & Health-Tech Entrepreneurs")
        c.setCreator("Enhanced Social Mastery Generator for Tech Professionals")

        start_date = start_date or date.today()
        if isinstance(start_date, str):
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            except Exception:
                logger.warning("start_date string provided but could not parse, using today instead.")
                start_date = date.today()

        logger.info("Generating AI Developer journal starting from %s -> %s", start_date.isoformat(), output_file)

        # Enhanced intro page with tech focus
        c.setFont("Helvetica-Bold", 26)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.8*inch, "AI DEVELOPER")
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.2*inch, "SOCIAL MASTERY SYSTEM")
        
        c.setFont("Helvetica", 16)
        c.setFillColor(COLOR_TEXT_HEADER)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.7*inch, "Transform Technical Expertise into Leadership Influence")
        
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 3.1*inch, "From Coding Excellence to Communication Mastery")
        
        # System overview for developers
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(COLOR_ENERGY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 3.7*inch, "🔧 TECHNICAL COMMUNICATION SYSTEM:")
        
        features_text = [
            "✅ Progressive Technical Challenges: Build from basic networking to thought leadership",
            "✅ Developer-Focused Modules: Communication skills specifically for tech professionals", 
            "✅ Measurable Outcomes: Track network growth, presentation quality, and user empathy",
            "✅ Project Integration: Apply skills directly to NEETPrepGPT and health-tech goals",
            "✅ Career Acceleration: Transform from developer to technical leader and entrepreneur",
            "✅ Evidence-Based Approach: Grounded in communication science and startup success patterns"
        ]
        
        y_pos = PAGE_HEIGHT - 4.1*inch
        c.setFont("Helvetica", 11)
        c.setFillColor(COLOR_TEXT_BODY)
        for feature in features_text:
            c.drawCentredString(PAGE_WIDTH/2, y_pos, feature)
            y_pos -= 0.25*inch
        
        # Mission statement for tech professionals
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(COLOR_WISDOM)
        c.drawCentredString(PAGE_WIDTH/2, y_pos - 0.3*inch, "🚀 YOUR TECHNICAL LEADERSHIP TRANSFORMATION:")
        
        mission_text = [
            "This system transforms brilliant developers into influential technical leaders.",
            "You will master the art of translating complex AI concepts for any audience.",
            "Every interaction becomes a learning opportunity. Every challenge builds authority.",
            "In 7 weeks, you'll have the communication skills to launch successful health-tech products.",
            "Your technical expertise + communication mastery = unstoppable career trajectory.",
            "",
            "Commit to the process. Apply the system. Become the leader your industry needs."
        ]
        
        y_mission = y_pos - 0.7*inch
        c.setFont("Helvetica", 11)
        c.setFillColor(COLOR_TEXT_BODY)
        for line in mission_text:
            if line.strip():
                c.drawCentredString(PAGE_WIDTH/2, y_mission, line)
            y_mission -= 0.22*inch
        
        c.showPage()
        
        # Add personalized bio page
        draw_user_bio_page(c)
        
        # Generate enhanced knowledge modules and daily pages
        day_offset = 0
        for week in range(1, 8):
            # Enhanced knowledge module page
            draw_enhanced_knowledge_module_page(c, week)
            
            # Daily pages with tech focus
            for day in range(1, 8):
                current_date = start_date + timedelta(days=day_offset)
                date_str = current_date.strftime('%A, %B %d, %Y')
                
                draw_header(c, week, day, date_str)
                draw_daily_page(c, date_str, week, day)
                
                day_offset += 1
            
            # Enhanced weekly review
            draw_enhanced_weekly_review_page(c, week)
        
        # Add achievement badges page
        draw_tech_achievement_badges_page(c)
        
        # Enhanced final transformation assessment
        c.setFont("Helvetica-Bold", 24)
        c.setFillColor(COLOR_PRIMARY)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, "TECHNICAL LEADERSHIP")
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.4*inch, "MASTERY ACHIEVED")
        
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(COLOR_ACCENT)
        c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.9*inch, "AI Developer → Technical Leader → Entrepreneur")
        
        # Final assessment with career focus
        y = PAGE_HEIGHT - 3.4*inch
        final_prompts = [
            "TECHNICAL COMMUNICATION TRANSFORMATION ASSESSMENT:",
            "",
            "Week 1 Technical Confidence: ___/10  →  Week 7 Technical Confidence: ___/10",
            "",
            "Most Significant Technical Communication Breakthrough:",
            "",
            "New Technical Leadership Superpowers Acquired:",
            "1. ________________________________",
            "2. ________________________________", 
            "3. ________________________________",
            "",
            "NEETPrepGPT/Health-Tech Impact: How will these skills accelerate your projects?",
            "",
            "Network Quality Improvement: Describe your enhanced technical network:",
            "",
            "Entrepreneurial Readiness: Rate your readiness to launch and lead (1-10): ___",
            "",
            "Ongoing Technical Leadership Plan:"
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
                if len(prompt) > 80:
                    wrapped = textwrap.wrap(prompt, width=80)
                    for line in wrapped:
                        c.drawCentredString(PAGE_WIDTH/2, y, line)
                        y -= 0.22*inch
                else:
                    c.drawCentredString(PAGE_WIDTH/2, y, prompt)
                    y -= 0.25*inch
            else:
                y -= 0.15*inch
        
        # Success celebration for tech professionals
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(COLOR_ENERGY)
        c.drawCentredString(PAGE_WIDTH/2, y - 0.3*inch, "🎉 TRANSFORMATION COMPLETE! 🎉")
        c.setFont("Helvetica", 12)
        c.setFillColor(COLOR_TEXT_BODY)
        c.drawCentredString(PAGE_WIDTH/2, y - 0.6*inch, "You now possess the systematic communication skills to:")
        c.drawCentredString(PAGE_WIDTH/2, y - 0.85*inch, "• Explain complex AI concepts to any audience with confidence")
        c.drawCentredString(PAGE_WIDTH/2, y - 1.1*inch, "• Build a network of technical professionals and potential collaborators") 
        c.drawCentredString(PAGE_WIDTH/2, y - 1.35*inch, "• Lead technical teams and drive product development effectively")
        c.drawCentredString(PAGE_WIDTH/2, y - 1.6*inch, "• Pitch your health-tech solutions to investors and stakeholders")
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(COLOR_WISDOM)
        c.drawCentredString(PAGE_WIDTH/2, y - 2*inch, "Your technical expertise + communication mastery = Unstoppable career trajectory")
        
        c.save()
        logger.info("✅ Successfully created enhanced AI Developer Social Mastery Journal: %s", output_file)
        logger.info("🚀 Key enhancements implemented:")
        logger.info("   • Developer-focused knowledge modules with technical applications")
        logger.info("   • Tech-specific progressive challenges (GitHub, LinkedIn, technical presentations)")
        logger.info("   • Project integration sections linking skills to NEETPrepGPT/health-tech goals")
        logger.info("   • Achievement badge system for technical communication milestones")
        logger.info("   • Enhanced metrics tracking technical confidence and network quality")
        logger.info("   • Career transformation focus from developer to technical leader")
        
    except Exception as exc:
        logger.exception("Failed to generate enhanced journal: %s", exc)
        if c:
            try:
                c.save()
            except Exception:
                pass
        raise

def _parse_args():
    parser = argparse.ArgumentParser(description="Generate an Enhanced AI Developer Social Mastery Journal PDF.")
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
        print("\n🎯 SUCCESS: Your AI Developer Social Mastery Journal is ready!")
        print("📈 This system will transform your technical communication skills in 7 weeks")
        print("🚀 Apply these skills to accelerate NEETPrepGPT and your health-tech career goals")
    except Exception as e:
        logger.error("Generation failed: %s", e)
        print("❌ Generation failed. Check the logs above for details.")