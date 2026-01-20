# create_mastery_journal.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import slategray, lightgrey, black, dodgerblue, crimson
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date, timedelta

# --- Configuration ---
FILENAME = "Communication_Mastery_Journal.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.75 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
STYLES = getSampleStyleSheet()
BODY_STYLE = STYLES['BodyText']
BODY_STYLE.fontSize = 10
BODY_STYLE.leading = 14

# --- Content Definitions ---
WEEKLY_THEMES = {
    1: ("The Audit: Radical Self-Awareness", "The first step of Emotional Intelligence is Self-Awareness. You can't fix a bug you don't know exists."),
    2: ("The Control System: Mastering Self-Regulation", "The goal is to shorten the 'Refractory Period' after an emotional trigger, creating a space between stimulus and response."),
    3: ("The Receiver: The Art of Deep Listening", "Most people don't listen; they just wait for their turn to talk. Effective listening is the foundation."),
    4: ("The Transmitter: The Mechanics of Clear Expression", "Shift from blaming language ('You always...') to ownership language ('I feel...')."),
    5: ("The Bridge: Engineering Empathy", "Empathy is not agreement; it's understanding. Actively try to see the world from another's perspective."),
    6: ("The Debugger: Handling Difficult Conversations", "Treat a difficult conversation as two people solving a problem together, not a fight to be won."),
    7: ("The Network: Building & Maintaining Connections", "Relationships require consistent, small acts of proactive effort and genuine appreciation."),
}

# --- UPDATED AND COMPLETE INSIGHTS SECTION ---
DAILY_INSIGHTS = {
    1: [
        "Pay attention to your body; it often signals an emotion before your mind names it.",
        "Triggers are neutral events. Your interpretation of them creates the emotion.",
        "Self-awareness without judgment is the key. You are a scientist observing data.",
        "Notice your own conversational habits. Do you interrupt? Do you finish sentences?",
        "What is the 'story' you tell yourself immediately after a difficult interaction?",
        "Physical sensations are the raw data of emotions. Tight chest, clenched jaw, etc.",
        "Your internal monologue is a conversation. Is it a kind one?",
    ],
    2: [
        "The 'Tactical Pause' is your superpower. A single deep breath can change everything.",
        "'Name It to Tame It.' Labeling an emotion engages your prefrontal cortex, reducing its power.",
        "You are not your emotions. You are the sky; emotions are the weather passing through.",
        "Ask yourself: 'Is this reaction productive? Will it get me closer to my goal?'",
        "Regulation isn't suppression. It's choosing a wise response over an automatic reaction.",
        "A 5-minute walk can be enough to reset your nervous system after a trigger.",
        "Practice the pause in low-stakes situations so it's ready for high-stakes ones.",
    ],
    3: [
        "Listen to understand, not just to reply. Hold your response until they have finished.",
        "Paraphrasing ('So what you're saying is...') is the single best tool to confirm understanding.",
        "The most effective listeners are comfortable with silence. Don't rush to fill the void.",
        "Listen with your eyes. What is their body language telling you that their words are not?",
        "A clarifying question ('What did you mean by...?') shows you are engaged and prevents misunderstanding.",
        "Resist the urge to solve their problem. Often, people just want to be heard and understood.",
        "Assume the person you are listening to knows something you don't. - Jordan Peterson",
    ],
    4: [
        "'You' statements sound like accusations. 'I' statements express your experience.",
        "Be specific. 'You're always late' is an attack. 'I felt disrespected when you arrived 20 mins late' is a fact.",
        "Clarity is kindness. Ambiguity creates confusion and resentment.",
        "Your feelings are valid, but they are not objective facts. Own them as 'your' feelings.",
        "Before you speak, ask: Is it true? Is it necessary? Is it kind?",
        "Expressing your needs is not confrontational; it is a prerequisite for a healthy relationship.",
        "Vulnerability is not weakness. Stating 'I feel hurt' is more powerful than 'You're a jerk'.",
    ],
    5: [
        "Empathy starts with curiosity. Genuinely ask yourself: 'Why would a reasonable person do that?'",
        "Verbally acknowledge their perspective: 'It sounds like that was incredibly frustrating for you.'",
        "You don't have to agree with their position to understand their feelings.",
        "To practice empathy, try to argue their point of view for them, as strongly as they would.",
        "People's actions are often driven by a fear or a need you cannot see. Try to guess what it is.",
        "Validate the emotion, not necessarily the behavior. 'I can see why you're angry' is not the same as 'You were right to yell'.",
        "Replace the word 'but' with 'and' when you disagree. 'I see your point, and I have a different perspective.'",
    ],
    6: [
        "Prepare for a difficult conversation. Know your goal and your key facts beforehand.",
        "Start by stating a shared goal. 'We both want this project to succeed, so we need to talk about the deadline.'",
        "Describe the impact on you, not the other person's character flaws.",
        "Attack the problem, not the person. Frame it as 'us vs. the problem'.",
        "Stay calm and keep your voice low. Your emotional state is contagious.",
        "If the conversation gets heated, it's okay to say 'I need a 10-minute break before we continue.'",
        "Focus on future solutions, not just past grievances. 'How can we prevent this from happening again?'",
    ],
    7: [
        "Specific appreciation is 10x more powerful than generic thanks. 'Thanks for staying late to fix that bug' > 'Thanks'.",
        "Ask questions that show you remember previous conversations. 'How did that presentation you were worried about go?'",
        "A 30-second text message expressing gratitude can strengthen a connection for weeks.",
        "Be the first to offer help, to congratulate, or to say hello.",
        "Celebrate other people's wins. Your enthusiasm costs you nothing and builds immense goodwill.",
        "Create a 'connection list' and reach out to one person on it each day.",
        "Be fully present. Putting your phone away when someone is talking is a powerful sign of respect.",
    ],
}

# --- Helper Functions ---
def draw_multiline_paragraph(c, x, y, text, max_width):
    """Draws a multi-line paragraph and returns the y-position after drawing."""
    p = Paragraph(text, BODY_STYLE)
    p_width, p_height = p.wrapOn(c, max_width, PAGE_HEIGHT)
    p.drawOn(c, x, y - p_height)
    return y - p_height

def draw_section_box(c, x, y, width, height, title, title_color=black):
    """Draws a titled box with a light grey background."""
    c.saveState()
    # Box
    c.setStrokeColor(lightgrey)
    c.setFillColor(black)
    c.rect(x, y - height, width, height, stroke=1, fill=0)
    
    # Title
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(title_color)
    c.drawString(x + 0.15 * inch, y - 0.25 * inch, title)
    c.restoreState()

# --- Page Drawing Functions ---
def draw_intro_page(c):
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 2*inch, "The Communication Mastery Journal")
    c.setFont("Helvetica", 16)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 2.5*inch, "Your 8-Week Training Partner")
    
    y_pos = PAGE_HEIGHT - 4 * inch
    text = """
    Welcome. This journal is designed to do more than just record events; it's designed to rewire your approach to communication.
    <br/><br/>
    <b>How to Use This Journal:</b>
    <br/><br/>
    <b>1. Weekly Kick-off:</b> At the start of each week, review the theme and set a clear, personal intention. This is your mission.
    <br/><br/>
    <b>2. Daily Reflection:</b> Each day, take 15-20 minutes. Don't just log events. Use the prompts to dissect a 'Win' and a 'Challenge'. The goal is deep understanding, not just data entry.
    <br/><br/>
    <b>3. Be Honest:</b> The only person you need to impress is your future self. Be radically honest about your feelings, reactions, and assumptions.
    <br/><br/>
    Mastery is not an event; it's a process. This is your workshop. Let's begin.
    """
    draw_multiline_paragraph(c, MARGIN, y_pos, text, CONTENT_WIDTH)
    c.showPage()
    
def draw_weekly_kickoff_page(c, week):
    theme_title, theme_concept = WEEKLY_THEMES.get(week, ("", ""))
    
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN, f"Week {week} - Kick-off")
    
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5 * inch, theme_title)
    
    y_pos = PAGE_HEIGHT - 2.2 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, y_pos, "Core Concept:")
    y_pos -= 0.2 * inch
    y_pos = draw_multiline_paragraph(c, MARGIN, y_pos, theme_concept, CONTENT_WIDTH)

    y_pos -= 1 * inch
    draw_section_box(c, MARGIN, y_pos, CONTENT_WIDTH, 4 * inch, "My Intention for This Week")
    
    prompt_y = y_pos - 0.6 * inch
    prompt_text = "Based on this week's theme, what is one specific, measurable goal you want to achieve? (e.g., 'I will pause and take a breath before responding in every team meeting,' or 'I will successfully use one 'I' statement with my partner.')"
    draw_multiline_paragraph(c, MARGIN + 0.15*inch, prompt_y, prompt_text, CONTENT_WIDTH - 0.3*inch)
    c.showPage()
    
def draw_daily_reflection_page(c, week, day, date_str):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN, f"Week {week} - Day {day}")
    c.setFont("Helvetica", 12)
    c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN, date_str)

    # Master's Insight
    y_pos = PAGE_HEIGHT - 1.25 * inch
    insights = DAILY_INSIGHTS.get(week, ["No insight available."])
    insight_text = insights[day - 1]
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(slategray)
    c.drawString(MARGIN, y_pos, "🎓 Master's Insight of the Day:")
    c.setFont("Helvetica-Oblique", 10)
    y_pos -= 0.2 * inch
    y_pos = draw_multiline_paragraph(c, MARGIN, y_pos, insight_text, CONTENT_WIDTH)
    
    # Divider
    c.setStrokeColor(lightgrey)
    c.line(MARGIN, y_pos - 0.1*inch, PAGE_WIDTH - MARGIN, y_pos - 0.1*inch)
    y_pos -= 0.3 * inch

    # Communication Win
    box_height = 3.2 * inch
    draw_section_box(c, MARGIN, y_pos, CONTENT_WIDTH, box_height, "✅ Communication Win", dodgerblue)
    prompt_text = "<b>Situation:</b> Describe a positive interaction. <br/><b>Analysis:</b> Why did it go well? What specific skill (e.g., listening, pausing, 'I' statement) did you use effectively?"
    draw_multiline_paragraph(c, MARGIN + 0.15*inch, y_pos - 0.4*inch, prompt_text, CONTENT_WIDTH - 0.3*inch)
    y_pos -= (box_height + 0.25*inch)
    
    # Communication Challenge
    box_height = 4.5 * inch
    draw_section_box(c, MARGIN, y_pos, CONTENT_WIDTH, box_height, "🧠 Communication Challenge", crimson)
    prompt_text = """
    <b>Situation:</b> Describe an interaction that was difficult or went poorly. (Objective facts only)
    <br/><br/>
    <b>My Initial Reaction:</b> What did you feel physically and emotionally? What was the automatic thought?
    <br/><br/>
    <b>My Deeper Analysis:</b> What underlying belief or trigger caused this reaction? What was I trying to achieve or protect?
    <br/><br/>
    <b>Alternative Response:</b> How could I apply this week's core concept for a better outcome next time?
    """
    draw_multiline_paragraph(c, MARGIN + 0.15*inch, y_pos - 0.4*inch, prompt_text, CONTENT_WIDTH - 0.3*inch)
    
    c.showPage()
    
def draw_final_review_pages(c):
    # Page 1: Retrospective
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5 * inch, "Week 8: The Full Stack Review")
    
    y_pos = PAGE_HEIGHT - 2.5 * inch
    draw_section_box(c, MARGIN, y_pos, CONTENT_WIDTH, 7*inch, "Progress Retrospective")
    prompt = """
    Read your first entry from Week 1. Then answer the following:
    <br/><br/>
    <b>1. My Biggest Transformation:</b> What is the single most significant change you've observed in your awareness or behavior?
    <br/><br/><br/>
    <b>2. From Unconscious to Conscious:</b> What pattern of behavior were you completely unaware of 8 weeks ago that you can now see clearly?
    <br/><br/><br/>
    <b>3. Proudest Moment:</b> Describe one specific conversation from the past 8 weeks where you handled it far better than you would have previously.
    """
    draw_multiline_paragraph(c, MARGIN + 0.15*inch, y_pos - 0.4*inch, prompt, CONTENT_WIDTH - 0.3*inch)
    c.showPage()
    
    # Page 2: The Path Forward
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 1.5 * inch, "The Path Forward: My 90-Day Plan")
    y_pos = PAGE_HEIGHT - 2.5 * inch
    draw_section_box(c, MARGIN, y_pos, CONTENT_WIDTH, 7*inch, "Strategic Development Plan")
    prompt = """
    Mastery is a continuous journey. Use this page to create a clear plan for the next 90 days.
    <br/><br/>
    <b>1. My Core Focus Skill:</b> Based on your review, what is the #1 skill you will dedicate yourself to mastering? (e.g., Proactive Empathy, Calmness in Conflict, etc.)
    <br/><br/><br/>
    <b>2. Key Habit:</b> What single daily or weekly habit will you implement to practice this skill? (Be specific: 'I will spend 5 mins before my daily stand-up thinking about one teammate's perspective.')
    <br/><br/><br/>
    <b>3. Accountability:</b> How will you hold yourself accountable? (e.g., A weekly review in this journal, telling a trusted friend, setting a phone reminder.)
    """
    draw_multiline_paragraph(c, MARGIN + 0.15*inch, y_pos - 0.4*inch, prompt, CONTENT_WIDTH - 0.3*inch)
    c.showPage()


def create_mastery_journal():
    c = canvas.Canvas(FILENAME, pagesize=A4)
    start_date = date.today()
    
    draw_intro_page(c)
    
    day_offset = 0
    for week in range(1, 8):
        draw_weekly_kickoff_page(c, week)
        for day in range(1, 8):
            current_date = start_date + timedelta(days=day_offset)
            date_str = current_date.strftime('%A, %B %d, %Y')
            draw_daily_reflection_page(c, week, day, date_str)
            day_offset += 1
            
    draw_final_review_pages(c)
    
    c.save()
    print(f"✅ Successfully created {FILENAME}")

if __name__ == "__main__":
    create_mastery_journal()