# create_engineering_journal.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import slategray, lightgrey, black, HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date, timedelta # <--- THIS LINE WAS MISSING. IT IS NOW FIXED.

# --- Engineering Color Palette ---
COLOR_PRIMARY = HexColor('#007ACC')  # A professional blue
COLOR_ACCENT = HexColor('#4EC9B0')   # Teal for success/positive
COLOR_WARN = HexColor('#F44747')     # Red for challenges/errors
COLOR_BG_LIGHT = HexColor('#F3F3F3')  # Light background for sections
COLOR_TEXT_HEADER = HexColor('#2D2D2D')
COLOR_TEXT_BODY = HexColor('#3C3C3C')

# --- Configuration ---
FILENAME = "Communication_Engineer_Journal.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.7 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
STYLES = getSampleStyleSheet()

# --- Helper Functions ---
def setup_styles():
    """Sets up custom Paragraph styles."""
    styles = getSampleStyleSheet()
    body_style = styles['BodyText']
    body_style.fontName = 'Helvetica'
    body_style.fontSize = 9
    body_style.leading = 14
    body_style.textColor = COLOR_TEXT_BODY
    return styles

def draw_header(c, week, day, date_str):
    """Draws the main page header."""
    c.saveState()
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN, PAGE_HEIGHT - MARGIN, f"Week {week} Diagnostic")
    c.setFont("Helvetica", 11)
    c.setFillColor(COLOR_TEXT_BODY)
    c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN, f"Day {day} | {date_str}")
    c.setStrokeColor(lightgrey)
    c.setLineWidth(1)
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.1*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 0.1*inch)
    c.restoreState()

def draw_section(c, y_pos, title, content_prompts, height, color=COLOR_PRIMARY):
    """Draws a bordered and titled section with prompts."""
    c.saveState()
    # Draw border
    c.setStrokeColor(color)
    c.setLineWidth(1.5)
    c.rect(MARGIN, y_pos - height, CONTENT_WIDTH, height)

    # Draw title bar
    c.setFillColor(color)
    c.rect(MARGIN, y_pos - 0.4*inch, CONTENT_WIDTH, 0.4*inch, fill=1, stroke=0)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN + 0.15*inch, y_pos - 0.27*inch, title)

    # Draw content prompts
    c.setFont("Helvetica", 9)
    c.setFillColor(COLOR_TEXT_BODY)
    current_y = y_pos - 0.6*inch
    for prompt in content_prompts:
        c.drawString(MARGIN + 0.15*inch, current_y, prompt)
        current_y -= 0.25*inch
    c.restoreState()
    return y_pos - height - 0.2*inch

def draw_checklist(c, y_pos, title, items):
    """Draws a title and a list of items with checkboxes."""
    c.saveState()
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(MARGIN + 0.1*inch, y_pos, title)
    
    current_y = y_pos - 0.25*inch
    c.setFont("Helvetica", 9)
    c.setFillColor(COLOR_TEXT_BODY)
    for item in items:
        # Draw checkbox
        c.rect(MARGIN + 0.1*inch, current_y - 0.02*inch, 0.1*inch, 0.1*inch)
        c.drawString(MARGIN + 0.3*inch, current_y, item)
        current_y -= 0.2*inch
    c.restoreState()
    return current_y

# --- WEEKLY SPECIALIZED PAGE DRAWING FUNCTIONS ---

def draw_week_1_daily_page(c, date_str):
    """Diagnostic: System Status Report."""
    y = PAGE_HEIGHT - MARGIN - 0.3*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Daily System Status Report")
    y -= 0.4*inch

    # Left Column: Checklists
    checklist_y = y
    checklist_y = draw_checklist(c, checklist_y, "PHYSICAL STATE SCAN:", ["Fatigued", "Energized", "Tense", "Relaxed"])
    checklist_y -= 0.3*inch
    checklist_y = draw_checklist(c, checklist_y, "EMOTIONAL STATE SCAN:", ["Anxious/Stressed", "Calm/Content", "Irritable/Angry", "Optimistic/Happy"])
    checklist_y -= 0.3*inch
    checklist_y = draw_checklist(c, checklist_y, "FOCUS LEVEL:", ["Distracted", "Hyper-focused", "Neutral"])
    
    # Right Column: Event Log
    prompts = [
        "EVENT: Describe one interaction that generated a significant emotional signal.",
        "",
        "RAW DATA - SENSATION: Where in your body did you feel it? (e.g., chest tightness, flushed face)",
        "",
        "RAW DATA - EMOTION API: If you had to give this feeling a name, what would it be?",
        "",
        "TRIGGER LOG: What specific event, word, or action immediately preceded the signal?",
        "",
        "INITIAL HYPOTHESIS: Why do you think this trigger produced this signal? (No judgment, just analysis)"
    ]
    draw_section(c, y, "EVENT LOG: Analyzing a High-Signal Interaction", prompts, 7*inch, COLOR_PRIMARY)
    c.showPage()
    
def draw_week_2_daily_page(c, date_str):
    """Control System: Trigger-Response Analysis."""
    y = PAGE_HEIGHT - MARGIN - 0.3*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Trigger-Response Debugger")
    y -= 0.4*inch

    prompts_trigger = [
        "TRIGGER (Input): A specific event that occurred.",
        "", "",
        "AUTOMATIC THOUGHT (Processing): The immediate story I told myself about the event.",
        "", "",
        "EMOTIONAL-PHYSICAL RESPONSE (Output): The feeling & sensation that resulted."
    ]
    y = draw_section(c, y, "STEP 1: Deconstruct the Automatic Reaction Chain", prompts_trigger, 2.8*inch, COLOR_PRIMARY)

    prompts_deploy = [
        "Did I deploy the 'Tactical Pause' before reacting?",
        "☐ Yes  ☐ No",
        "",
        "If YES: What did I do during the pause? (e.g., Deep breath, left the room)",
        "",
        "If NO: At what point did I realize a pause would have been useful?",
        "",
        "RESULTING ACTION: What was my actual response after the initial reaction/pause?",
        "",
        "PERFORMANCE REVIEW: How did deploying (or not deploying) the pause affect the outcome?"
    ]
    draw_section(c, y, "STEP 2: Control System Deployment Analysis", prompts_deploy, 4.2*inch, COLOR_ACCENT)
    c.showPage()

def draw_week_3_daily_page(c, date_str):
    """Receiver Upgrade: Signal Decoding."""
    y = PAGE_HEIGHT - MARGIN - 0.3*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Deep Listening Signal Analyzer")
    y -= 0.4*inch

    prompts_log = [
        "CONVERSATION CONTEXT: Who was it with? What was the topic?",
        ""
    ]
    y = draw_section(c, y, "Log a Conversation for Analysis", prompts_log, 0.9*inch, COLOR_PRIMARY)
    
    # Left Column: Signal Breakdown
    y_left = y
    c.setFont("Helvetica-Bold", 10); c.drawString(MARGIN, y_left, "SIGNAL BREAKDOWN")
    y_left -= 0.2*inch; c.setStrokeColor(lightgrey); c.line(MARGIN, y_left, PAGE_WIDTH/2 - 0.1*inch, y_left)
    y_left -= 0.2*inch; c.setFont("Helvetica-Bold", 9); c.drawString(MARGIN, y_left, "Verbal Data (The Words):")
    y_left -= 1.5*inch; c.setFont("Helvetica-Bold", 9); c.drawString(MARGIN, y_left, "Vocal Data (The Tone):")
    y_left -= 1.5*inch; c.setFont("Helvetica-Bold", 9); c.drawString(MARGIN, y_left, "Non-Verbal Data (The Body):")

    # Right Column: My Performance
    y_right = y
    c.setFont("Helvetica-Bold", 10); c.drawString(PAGE_WIDTH/2 + 0.1*inch, y_right, "MY RECEIVER PERFORMANCE")
    y_right -= 0.2*inch; c.setStrokeColor(lightgrey); c.line(PAGE_WIDTH/2 + 0.1*inch, y_right, PAGE_WIDTH-MARGIN, y_right)
    
    y_checklist = y_right - 0.2*inch
    checklist_items = [
        "Planning my response while they spoke",
        "Jumping to conclusions/assumptions",
        "Listening only for facts, ignoring feelings",
        "Getting distracted by my own thoughts"
    ]
    y_checklist = draw_checklist(c, y_checklist, "LISTENING BARRIERS DETECTED:", checklist_items)

    y_deploy = y_checklist - 0.2*inch
    c.setFont("Helvetica-Bold", 9); c.drawString(PAGE_WIDTH/2 + 0.1*inch, y_deploy, "TECHNIQUES DEPLOYED:")
    y_deploy -= 0.2*inch; c.drawString(PAGE_WIDTH/2 + 0.2*inch, y_deploy, "Paraphrase Attempt:")
    y_deploy -= 0.8*inch; c.drawString(PAGE_WIDTH/2 + 0.2*inch, y_deploy, "Clarifying Question Asked:")

    c.showPage()
    
def draw_week_4_daily_page(c, date_str):
    """Transmitter Calibration: Message Construction."""
    y = PAGE_HEIGHT - MARGIN - 0.3*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: 'I-Statement' Message Builder")
    y -= 0.4*inch

    prompts_blame = ["First, write down the blaming thought or 'You-Statement' you wanted to say.", "(e.g., 'You never help out around here.')"]
    y = draw_section(c, y, "STEP 1: Capture the Raw, Uncalibrated Message", prompts_blame, 1.2*inch, COLOR_WARN)

    c.setFont("Helvetica-Bold", 10); c.drawString(MARGIN, y, "STEP 2: Calibrate Using the 'I-Statement' Formula")
    y -= 0.3*inch

    # Formulaic boxes
    formula_prompts = {
        "I feel... [Emotion]": 1.0,
        "when... [Specific, Objective Behavior]": 1.5,
        "because... [The Impact on You]": 1.5,
        "What I would appreciate is... [A Positive Request]": 1.5
    }
    for title, height in formula_prompts.items():
        draw_section(c, y, title, [], height, COLOR_PRIMARY)
        y -= (height + 0.1*inch)
        
    prompts_final = ["Assemble the parts into the final, calibrated message ready for transmission."]
    draw_section(c, y, "FINAL CALIBRATED MESSAGE", prompts_final, 1*inch, COLOR_ACCENT)
    c.showPage()

def draw_week_5_daily_page(c, date_str):
    """Empathy Bridge: Perspective Simulation."""
    y = PAGE_HEIGHT - MARGIN - 0.3*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Perspective Simulation Worksheet")
    y -= 0.4*inch

    prompts_context = ["Describe a situation where you and another person have a strong disagreement or misunderstanding."]
    y = draw_section(c, y, "Simulation Context", prompts_context, 1.2*inch, COLOR_PRIMARY)
    
    # Left Column: My OS
    c.setFont("Helvetica-Bold", 10); c.drawString(MARGIN, y, "My Operating System")
    y_left = y - 0.2*inch
    prompts_left = [
        "My Goal in this situation:", "", "",
        "My Core Belief/Assumption:", "", "",
        "My Primary Emotion/Fear:", "", ""
    ]
    draw_section(c, y, "", prompts_left, 5.2*inch, COLOR_TEXT_BODY)

    # Right Column: Their OS (Simulated)
    c.setFont("Helvetica-Bold", 10); c.drawString(PAGE_WIDTH/2 + 0.1*inch, y, "Their Operating System (Simulated)")
    y_right = y - 0.2*inch
    prompts_right = [
        "Their Likely Goal:", "", "",
        "Their Likely Belief/Assumption:", "", "",
        "Their Likely Emotion/Fear:", "", ""
    ]
    # This is a bit tricky, need to manually create the box on the right
    c.saveState()
    c.translate(PAGE_WIDTH/2, 0)
    draw_section(c, y, "", prompts_right, 5.2*inch, COLOR_TEXT_BODY)
    c.restoreState()

    y -= (5.2*inch + 0.2*inch)
    prompts_insight = ["What is one key insight gained from running this simulation? How does it change your approach?"]
    draw_section(c, y, "Simulation Insight", prompts_insight, 1.0*inch, COLOR_ACCENT)
    c.showPage()
    
def draw_week_6_daily_page(c, date_str):
    """Conflict Debugger."""
    y = PAGE_HEIGHT - MARGIN - 0.3*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: The COIN Conflict Debugger")
    y -= 0.4*inch
    
    prompts_problem = ["Define the problem you need to discuss as a neutral, shared goal.", "(e.g., 'Finalize the project plan without further delays.')"]
    y = draw_section(c, y, "Problem Statement", prompts_problem, 1.2*inch, COLOR_PRIMARY)
    
    c.setFont("Helvetica-Bold", 10); c.drawString(MARGIN, y, "Execute the COIN Framework")
    y -= 0.3*inch

    coin_prompts = {
        "C - Context: When and where did the specific event happen? (Set the scene)": 1.5,
        "O - Observation: What did you see or hear? (Factual, objective, like a camera would record it)": 1.5,
        "I - Impact: How did this observation affect you, the team, or the project? (Use 'I' Statements)": 1.5,
        "N - Next Steps: What is a collaborative suggestion for moving forward? (Frame as a question)": 1.5
    }
    for title, height in coin_prompts.items():
        draw_section(c, y, title, [], height, COLOR_TEXT_BODY)
        y -= (height + 0.1*inch)
    c.showPage()
    
def draw_week_7_daily_page(c, date_str):
    """Network Maintenance Protocol."""
    y = PAGE_HEIGHT - MARGIN - 0.3*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Daily Connection Quality Check")
    y -= 0.4*inch

    y = draw_checklist(c, y, "PROACTIVE APPRECIATION PROTOCOL (Select one or more)", [
        "Sent a text/email with a SPECIFIC thank you.",
        "Publicly acknowledged someone's good work in a meeting.",
        "Verbally thanked someone, explaining the positive IMPACT of their help."
    ])
    y -= 0.2*inch
    prompts_appreciation = ["Log the details of the appreciation sent:"]
    y = draw_section(c, y, "Appreciation Log", prompts_appreciation, 1.5*inch, COLOR_ACCENT)

    y = draw_checklist(c, y, "DEEPER QUESTIONS PROTOCOL (Select one or more)", [
        "Asked a follow-up question based on a past conversation.",
        "Asked for their opinion/advice on something important.",
        "Asked about their life/interests outside of work/our usual context."
    ])
    y -= 0.2*inch
    prompts_questions = ["Log the 'better question' you asked and the response:"]
    draw_section(c, y, "Better Questions Log", prompts_questions, 2.5*inch, COLOR_PRIMARY)
    c.showPage()

# This is a map to call the correct function for each week
WEEKLY_DRAW_FUNCTIONS = {
    1: draw_week_1_daily_page,
    2: draw_week_2_daily_page,
    3: draw_week_3_daily_page,
    4: draw_week_4_daily_page,
    5: draw_week_5_daily_page,
    6: draw_week_6_daily_page,
    7: draw_week_7_daily_page,
}

def create_engineering_journal():
    """Main function to generate the PDF."""
    c = canvas.Canvas(FILENAME, pagesize=A4)
    start_date = date.today()
    
    # Simple intro page
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 + 2*inch, "The Communication Engineer's Journal")
    c.setFont("Helvetica", 14)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 + 1.5*inch, "An 8-Week Diagnostic & Calibration Toolkit")
    c.showPage()
    
    day_offset = 0
    for week in range(1, 8):
        for day in range(1, 8):
            current_date = start_date + timedelta(days=day_offset)
            date_str = current_date.strftime('%A, %B %d, %Y')
            
            draw_header(c, week, day, date_str)
            
            # Call the specific drawing function for the current week
            draw_function = WEEKLY_DRAW_FUNCTIONS.get(week)
            if draw_function:
                draw_function(c, date_str)
            
            day_offset += 1
            
    # Add final review pages (can be designed similarly)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2, "Week 8: Performance Review & Roadmap")
    c.showPage()

    c.save()
    print(f"✅ Successfully created {FILENAME}")

if __name__ == "__main__":
    create_engineering_journal()