# Advanced Communication Engineering Journal Generator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import slategray, lightgrey, black, HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date, timedelta

# --- Enhanced Color Palette ---
COLOR_PRIMARY = HexColor('#007ACC')  # Professional blue
COLOR_ACCENT = HexColor('#4EC9B0')   # Success green
COLOR_WARN = HexColor('#F44747')     # Challenge red
COLOR_ENERGY = HexColor('#FFB347')   # Motivational orange
COLOR_WISDOM = HexColor('#9370DB')   # Insight purple
COLOR_BG_LIGHT = HexColor('#F3F3F3')
COLOR_TEXT_HEADER = HexColor('#2D2D2D')
COLOR_TEXT_BODY = HexColor('#3C3C3C')

# --- Configuration ---
FILENAME = "Social_Mastery_Engineering_Journal.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.6 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
STYLES = getSampleStyleSheet()

# --- Daily Motivation Quotes by Week ---
WEEKLY_MOTIVATION = {
    1: ["Self-awareness is the first step to mastery.", "Every expert was once a beginner.", "Today I collect data about my social patterns."],
    2: ["Between stimulus and response lies choice.", "I am rewiring my automatic reactions.", "Pause. Breathe. Choose. Respond."],
    3: ["Listen with the intent to understand, not reply.", "Deep listening is a superpower.", "I hear not just words, but emotions and needs."],
    4: ["Words have power. I choose them wisely.", "Clarity in communication creates connection.", "My message lands exactly where I intend."],
    5: ["To understand others, I must first understand myself.", "Empathy is intelligence in action.", "I see the world through many lenses."],
    6: ["Conflict is connection seeking to happen.", "Difficult conversations build stronger bonds.", "I transform tension into understanding."],
    7: ["Relationships require intentional cultivation.", "I invest in connections before I need them.", "Every interaction is an opportunity to add value."]
}

# --- Social Challenge Cards by Week ---
WEEKLY_CHALLENGES = {
    1: ["Start 3 conversations with strangers", "Make eye contact for 5+ seconds", "Ask 'How are you?' and actually listen"],
    2: ["Practice the 3-breath pause in heated moments", "Catch yourself mid-reaction and reset", "Turn a complaint into a request"],
    3: ["Use active listening in every conversation", "Ask 3 follow-up questions per discussion", "Reflect back what you heard before responding"],
    4: ["Use 'I' statements when expressing concerns", "Practice saying no without over-explaining", "Give a specific compliment to someone"],
    5: ["Ask someone about their dreams/goals", "Share a vulnerable story about yourself", "Practice seeing a conflict from the other side"],
    6: ["Have one difficult conversation you've been avoiding", "Use the COIN method in a real situation", "Apologize for something without making excuses"],
    7: ["Reach out to 3 people you haven't talked to recently", "Express appreciation with specific examples", "Ask someone for advice on something important"]
}

# --- Helper Functions ---
def setup_styles():
    """Enhanced paragraph styles."""
    styles = getSampleStyleSheet()
    body_style = styles['BodyText']
    body_style.fontName = 'Helvetica'
    body_style.fontSize = 9
    body_style.leading = 14
    body_style.textColor = COLOR_TEXT_BODY
    return styles

def draw_header(c, week, day, date_str):
    """Enhanced header with progress tracking."""
    c.saveState()
    # Main title
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN + 0.1*inch, f"Week {week}: Social Engineering Lab")
    
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

def draw_motivation_box(c, y_pos, week):
    """Daily motivation and energy booster."""
    c.saveState()
    # Background
    c.setFillColor(COLOR_ENERGY)
    c.setStrokeColor(COLOR_ENERGY)
    c.roundRect(MARGIN, y_pos - 0.8*inch, CONTENT_WIDTH, 0.8*inch, 0.1*inch, fill=1, stroke=1)
    
    # Title
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.25*inch, "⚡ DAILY ENERGY INJECTION")
    
    # Quote
    c.setFont("Helvetica-Oblique", 10)
    quotes = WEEKLY_MOTIVATION.get(week, ["Today is a new opportunity to grow."])
    quote = quotes[(hash(str(date.today())) % len(quotes))]  # Random daily quote
    c.drawString(MARGIN + 0.2*inch, y_pos - 0.5*inch, f'"{quote}"')
    
    c.restoreState()
    return y_pos - 1*inch

def draw_section(c, y_pos, title, content_prompts, height, color=COLOR_PRIMARY, include_lines=True):
    """Enhanced section with better formatting."""
    c.saveState()
    # Draw border with rounded corners
    c.setStrokeColor(color)
    c.setLineWidth(1.5)
    c.roundRect(MARGIN, y_pos - height, CONTENT_WIDTH, height, 0.05*inch)

    # Draw title bar with gradient effect
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
            c.drawString(MARGIN + 0.15*inch, current_y, prompt)
            if include_lines and not prompt.endswith(':'):
                # Draw lines for writing
                line_y = current_y - 0.05*inch
                c.setStrokeColor(lightgrey)
                c.setLineWidth(0.5)
                for i in range(2):
                    c.line(MARGIN + 0.2*inch, line_y - (i * 0.15*inch), PAGE_WIDTH - MARGIN - 0.2*inch, line_y - (i * 0.15*inch))
        current_y -= line_spacing
    
    c.restoreState()
    return y_pos - height - 0.2*inch

def draw_enhanced_checklist(c, y_pos, title, items, color=COLOR_PRIMARY):
    """Enhanced checklist with better visual design."""
    c.saveState()
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(color)
    c.drawString(MARGIN + 0.1*inch, y_pos, title)
    
    current_y = y_pos - 0.3*inch
    c.setFont("Helvetica", 9)
    c.setFillColor(COLOR_TEXT_BODY)
    
    for item in items:
        # Draw enhanced checkbox
        c.setStrokeColor(color)
        c.setLineWidth(1.5)
        c.roundRect(MARGIN + 0.1*inch, current_y - 0.05*inch, 0.12*inch, 0.12*inch, 0.02*inch)
        c.drawString(MARGIN + 0.3*inch, current_y, item)
        current_y -= 0.25*inch
    
    c.restoreState()
    return current_y

def draw_daily_social_challenge(c, y_pos, week):
    """Daily social challenge section."""
    challenges = WEEKLY_CHALLENGES.get(week, ["Practice active listening"])
    challenge = challenges[(hash(str(date.today())) % len(challenges))]
    
    prompts = [
        f"TODAY'S CHALLENGE: {challenge}",
        "",
        "EXECUTION PLAN: How will you complete this challenge today?",
        "",
        "RESULT: What happened when you tried it?",
        "",
        "LEARNING: What did you discover about yourself or others?"
    ]
    
    return draw_section(c, y_pos, "🎯 DAILY SOCIAL CHALLENGE", prompts, 2.2*inch, COLOR_ACCENT)

def draw_reflection_notes(c, y_pos):
    """Daily reflection and notes section."""
    prompts = [
        "HIGHLIGHT: What was the best social moment of your day?",
        "",
        "LESSON: What did you learn about communication today?",
        "",
        "TOMORROW'S FOCUS: One specific thing you'll pay attention to tomorrow:",
        ""
    ]
    
    return draw_section(c, y_pos, "📝 DAILY REFLECTION NOTES", prompts, 2.0*inch, COLOR_WISDOM)

# --- ENHANCED WEEKLY PAGE FUNCTIONS ---

def draw_week_1_daily_page(c, date_str, week, day):
    """Week 1: Advanced Self-Awareness System."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    y = draw_motivation_box(c, y, week)
    
    # Daily checklist
    daily_items = [
        "Morning intention set for social awareness",
        "Tracked emotional responses in interactions",
        "Noticed body language patterns (mine & others)",
        "Practiced mindful presence in conversations"
    ]
    y = draw_enhanced_checklist(c, y, "🔄 DAILY SOCIAL AWARENESS CHECKLIST:", daily_items, COLOR_PRIMARY)
    y -= 0.3*inch
    
    # Social challenge
    y = draw_daily_social_challenge(c, y, week)
    
    # Core diagnostic
    prompts_event = [
        "SOCIAL INTERACTION: Describe one significant social interaction today:",
        "",
        "ENERGY SCAN: What was your energy level? (1-10) Before: ___ After: ___",
        "",
        "BODY SIGNALS: Where did you feel tension, excitement, or discomfort?",
        "",
        "THOUGHT PATTERN: What story did your mind tell you about this interaction?",
        "",
        "EMOTIONAL DATA: Name 2-3 emotions you experienced during this interaction:",
        ""
    ]
    y = draw_section(c, y, "🔍 SOCIAL INTERACTION DIAGNOSTIC", prompts_event, 3*inch, COLOR_PRIMARY)
    
    # Reflection
    draw_reflection_notes(c, y)
    c.showPage()

def draw_week_2_daily_page(c, date_str, week, day):
    """Week 2: Response Control Engineering."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    y = draw_motivation_box(c, y, week)
    
    # Daily checklist
    daily_items = [
        "Used the 'tactical pause' at least once",
        "Caught myself in an automatic reaction",
        "Chose a thoughtful response over a reactive one",
        "Practiced breathing before difficult conversations"
    ]
    y = draw_enhanced_checklist(c, y, "⚙️ RESPONSE CONTROL CHECKLIST:", daily_items, COLOR_PRIMARY)
    y -= 0.3*inch
    
    # Social challenge
    y = draw_daily_social_challenge(c, y, week)
    
    # Trigger analysis
    prompts_trigger = [
        "TRIGGER EVENT: What specific situation triggered a strong reaction?",
        "",
        "AUTOMATIC RESPONSE: What was your immediate, unfiltered reaction?",
        "",
        "PAUSE DEPLOYMENT: Did you use a tactical pause? What technique?",
        "",
        "CHOSEN RESPONSE: What did you actually do after the pause (or wish you had)?",
        "",
        "OUTCOME ANALYSIS: How did your response affect the situation?",
        ""
    ]
    y = draw_section(c, y, "🎛️ TRIGGER-RESPONSE ENGINEERING", prompts_trigger, 3*inch, COLOR_PRIMARY)
    
    draw_reflection_notes(c, y)
    c.showPage()

def draw_week_3_daily_page(c, date_str, week, day):
    """Week 3: Deep Listening System Upgrade."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    y = draw_motivation_box(c, y, week)
    
    # Daily checklist
    daily_items = [
        "Asked clarifying questions in conversations",
        "Reflected back what I heard before responding",
        "Noticed when I was planning my response vs. listening",
        "Identified emotions behind someone's words"
    ]
    y = draw_enhanced_checklist(c, y, "👂 DEEP LISTENING CHECKLIST:", daily_items, COLOR_PRIMARY)
    y -= 0.3*inch
    
    # Social challenge
    y = draw_daily_social_challenge(c, y, week)
    
    # Listening analysis
    prompts_listen = [
        "CONVERSATION PARTNER: Who did you have a meaningful conversation with?",
        "",
        "LISTENING BARRIERS: What internal distractions did you notice?",
        "☐ Planning response ☐ Judging ☐ Distracted ☐ Assuming ☐ Time pressure",
        "",
        "ACTIVE TECHNIQUES USED:",
        "☐ Paraphrasing ☐ Clarifying questions ☐ Emotion labeling ☐ Body language mirroring",
        "",
        "DISCOVERY: What did you learn about this person that you didn't know before?",
        "",
        "LISTENING QUALITY: Rate your listening performance (1-10): ___"
    ]
    y = draw_section(c, y, "🎧 LISTENING PERFORMANCE ANALYSIS", prompts_listen, 3.2*inch, COLOR_PRIMARY)
    
    draw_reflection_notes(c, y)
    c.showPage()

def draw_week_4_daily_page(c, date_str, week, day):
    """Week 4: Message Transmission Optimization."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    y = draw_motivation_box(c, y, week)
    
    # Daily checklist
    daily_items = [
        "Used 'I' statements when expressing concerns",
        "Practiced clear, specific communication",
        "Asked if my message was understood as intended",
        "Avoided blame language in difficult conversations"
    ]
    y = draw_enhanced_checklist(c, y, "📡 MESSAGE CLARITY CHECKLIST:", daily_items, COLOR_PRIMARY)
    y -= 0.3*inch
    
    # Social challenge
    y = draw_daily_social_challenge(c, y, week)
    
    # Message construction
    prompts_message = [
        "CHALLENGING MESSAGE: What difficult thing did you need to communicate?",
        "",
        "DRAFT 1 (Raw/Blaming): What did you initially want to say?",
        "",
        "I STATEMENT REBUILD:",
        "I feel: _____________ when: _____________",
        "because: _____________ What I need: _____________",
        "",
        "FINAL MESSAGE: How did you actually communicate it?",
        "",
        "RECEPTION: How did the other person respond to your message?"
    ]
    y = draw_section(c, y, "📝 MESSAGE ENGINEERING WORKSHOP", prompts_message, 3.2*inch, COLOR_PRIMARY)
    
    draw_reflection_notes(c, y)
    c.showPage()

def draw_week_5_daily_page(c, date_str, week, day):
    """Week 5: Empathy Bridge Construction."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    y = draw_motivation_box(c, y, week)
    
    # Daily checklist
    daily_items = [
        "Asked someone about their perspective on a situation",
        "Shared something vulnerable about myself",
        "Practiced seeing a disagreement from the other side",
        "Showed genuine curiosity about someone's experience"
    ]
    y = draw_enhanced_checklist(c, y, "🌉 EMPATHY BRIDGE CHECKLIST:", daily_items, COLOR_PRIMARY)
    y -= 0.3*inch
    
    # Social challenge
    y = draw_daily_social_challenge(c, y, week)
    
    # Perspective simulation
    prompts_empathy = [
        "PERSON OF FOCUS: Who did you try to understand better today?",
        "",
        "THEIR SITUATION: What challenge or experience are they facing?",
        "",
        "THEIR POSSIBLE FEELINGS: What emotions might they be experiencing?",
        "",
        "THEIR POSSIBLE NEEDS: What might they need most right now?",
        "",
        "MY EMPATHY ACTION: How did I show understanding or support?",
        "",
        "INSIGHT GAINED: What new understanding did I develop about them?"
    ]
    y = draw_section(c, y, "🔍 EMPATHY SIMULATION LAB", prompts_empathy, 3*inch, COLOR_PRIMARY)
    
    draw_reflection_notes(c, y)
    c.showPage()

def draw_week_6_daily_page(c, date_str, week, day):
    """Week 6: Conflict Resolution Engineering."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    y = draw_motivation_box(c, y, week)
    
    # Daily checklist
    daily_items = [
        "Addressed a small issue before it became bigger",
        "Used collaborative language in disagreements",
        "Focused on solutions rather than blame",
        "Practiced staying calm during tense moments"
    ]
    y = draw_enhanced_checklist(c, y, "⚔️ CONFLICT RESOLUTION CHECKLIST:", daily_items, COLOR_PRIMARY)
    y -= 0.3*inch
    
    # Social challenge
    y = draw_daily_social_challenge(c, y, week)
    
    # Conflict analysis
    prompts_conflict = [
        "CONFLICT SITUATION: What disagreement or tension occurred?",
        "",
        "COIN FRAMEWORK APPLICATION:",
        "Context: When/where did this happen?",
        "",
        "Observation: What specifically did you see/hear?",
        "",
        "Impact: How did this affect you/others?",
        "",
        "Next Steps: What collaborative solution did you suggest?",
        "",
        "RESULT: How did applying this framework change the outcome?"
    ]
    y = draw_section(c, y, "🛠️ CONFLICT DEBUGGING SESSION", prompts_conflict, 3.2*inch, COLOR_PRIMARY)
    
    draw_reflection_notes(c, y)
    c.showPage()

def draw_week_7_daily_page(c, date_str, week, day):
    """Week 7: Relationship Network Optimization."""
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    y = draw_motivation_box(c, y, week)
    
    # Daily checklist
    daily_items = [
        "Reached out to someone I haven't talked to recently",
        "Expressed specific appreciation to someone",
        "Made plans to deepen a relationship",
        "Offered help or support without being asked"
    ]
    y = draw_enhanced_checklist(c, y, "🌐 NETWORK CULTIVATION CHECKLIST:", daily_items, COLOR_PRIMARY)
    y -= 0.3*inch
    
    # Social challenge
    y = draw_daily_social_challenge(c, y, week)
    
    # Network building
    prompts_network = [
        "CONNECTION MADE: Who did you intentionally connect with today?",
        "",
        "APPRECIATION GIVEN: What specific thing did you thank someone for?",
        "",
        "VALUE ADDED: How did you help or support someone today?",
        "",
        "RELATIONSHIP GOAL: What relationship do you want to strengthen this week?",
        "",
        "ACTION PLAN: What specific step will you take to deepen this connection?",
        "",
        "FOLLOW-UP: What conversation or interaction will you initiate tomorrow?"
    ]
    y = draw_section(c, y, "🔗 RELATIONSHIP ENGINEERING LAB", prompts_network, 3*inch, COLOR_PRIMARY)
    
    draw_reflection_notes(c, y)
    c.showPage()

# Map week numbers to their respective functions
WEEKLY_DRAW_FUNCTIONS = {
    1: draw_week_1_daily_page,
    2: draw_week_2_daily_page,
    3: draw_week_3_daily_page,
    4: draw_week_4_daily_page,
    5: draw_week_5_daily_page,
    6: draw_week_6_daily_page,
    7: draw_week_7_daily_page,
}

def draw_weekly_review_page(c, week):
    """Weekly review and planning page."""
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, f"Week {week} Performance Review")
    
    y = PAGE_HEIGHT - 2.5*inch
    
    # Weekly wins
    wins_prompts = [
        "BIGGEST BREAKTHROUGH: What was your most significant improvement this week?",
        "",
        "SKILL UPGRADE: Which communication skill improved the most?",
        "",
        "RELATIONSHIP IMPACT: How did your relationships change this week?"
    ]
    y = draw_section(c, y, "🏆 WEEKLY WINS", wins_prompts, 2*inch, COLOR_ACCENT)
    
    # Challenges
    challenge_prompts = [
        "BIGGEST CHALLENGE: What was the most difficult situation you faced?",
        "",
        "LEARNING OPPORTUNITY: What would you do differently?",
        "",
        "SKILL GAP: What area needs more focus next week?"
    ]
    y = draw_section(c, y, "🎯 CHALLENGES & GROWTH EDGES", challenge_prompts, 2*inch, COLOR_WARN)
    
    # Next week planning
    planning_prompts = [
        "FOCUS AREA: What communication skill will you prioritize next week?",
        "",
        "RELATIONSHIP GOAL: Which relationship will you invest in most?",
        "",
        "SUCCESS METRIC: How will you measure progress next week?"
    ]
    draw_section(c, y, "📋 NEXT WEEK PLANNING", planning_prompts, 2*inch, COLOR_WISDOM)
    
    c.showPage()

def create_enhanced_communication_journal():
    """Generate the complete social mastery journal."""
    c = canvas.Canvas(FILENAME, pagesize=A4)
    start_date = date.today()
    
    # Enhanced intro page
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2*inch, "SOCIAL MASTERY")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 2.5*inch, "ENGINEERING JOURNAL")
    
    c.setFont("Helvetica", 16)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 3*inch, "A 7-Week System for Communication Excellence")
    
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(COLOR_ACCENT)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 4*inch, "From Introvert to Influence")
    
    # Mission statement
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    mission_text = [
        "This journal is your systematic approach to becoming a world-class communicator.",
        "Through daily practice, reflection, and structured challenges, you will:",
        "• Master emotional awareness and response control",
        "• Develop deep listening and empathy skills", 
        "• Learn to express yourself clearly and persuasively",
        "• Build and maintain strong relationships",
        "• Transform conflict into connection",
        "",
        "Commit to the process. Trust the system. Become unstoppable."
    ]
    
    y_pos = PAGE_HEIGHT - 5*inch
    for line in mission_text:
        c.drawCentredString(PAGE_WIDTH/2, y_pos, line)
        y_pos -= 0.25*inch
    
    c.showPage()
    
    # Generate daily pages
    day_offset = 0
    for week in range(1, 8):
        for day in range(1, 8):  # 7 days per week
            current_date = start_date + timedelta(days=day_offset)
            date_str = current_date.strftime('%A, %B %d, %Y')
            
            draw_header(c, week, day, date_str)
            
            # Call the specific drawing function for the current week
            draw_function = WEEKLY_DRAW_FUNCTIONS.get(week)
            if draw_function:
                draw_function(c, date_str, week, day)
            
            day_offset += 1
        
        # Add weekly review page
        draw_weekly_review_page(c, week)
    
    # Final mastery assessment
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(COLOR_PRIMARY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 + inch, "COMMUNICATION MASTERY")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 + 0.5*inch, "ACHIEVED")
    
    c.setFont("Helvetica", 14)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 - 0.5*inch, "You are now equipped with the systems and skills")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 - 0.8*inch, "to build meaningful connections and influence positive change.")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 - 1.1*inch, "Continue practicing. Keep growing. Stay connected.")
    
    c.save()
    print(f"✅ Successfully created {FILENAME}")
    print(f"📊 Generated {7 * 7 + 7 + 2} pages of communication mastery content")
    print("🚀 Your social transformation journey begins now!")

if __name__ == "__main__":
    create_enhanced_communication_journal()