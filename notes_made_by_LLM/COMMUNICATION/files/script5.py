# create_engineering_journal_v3.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import slategray, lightgrey, black, HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date, timedelta

# --- Engineering Color Palette ---
COLOR_PRIMARY = HexColor('#007ACC')
COLOR_ACCENT = HexColor('#4EC9B0')
COLOR_WARN = HexColor('#F44747')
COLOR_TEXT_HEADER = HexColor('#2D2D2D')
COLOR_TEXT_BODY = HexColor('#3C3C3C')

# --- Configuration ---
FILENAME = "Communication_Engineer_Journal_Final.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.7 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

# --- Helper Functions ---
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
    c.line(MARGIN, PAGE_HEIGHT - MARGIN - 0.15*inch, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - MARGIN - 0.15*inch)
    c.restoreState()

def draw_section(c, y_pos, title, prompts, height, color=COLOR_PRIMARY, x_offset=0, width_mult=1.0):
    """Draws a bordered and titled section with prompts. Returns the new y_pos."""
    c.saveState()
    x = MARGIN + x_offset
    width = CONTENT_WIDTH * width_mult
    
    c.setStrokeColor(color)
    c.setLineWidth(1.5)
    c.rect(x, y_pos - height, width, height)

    c.setFillColor(color)
    c.rect(x, y_pos - 0.4*inch, width, 0.4*inch, fill=1, stroke=0)
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x + 0.15*inch, y_pos - 0.27*inch, title)

    c.setFont("Helvetica", 9)
    c.setFillColor(COLOR_TEXT_BODY)
    current_y = y_pos - 0.6*inch
    for prompt in prompts:
        c.drawString(x + 0.15*inch, current_y, prompt)
        current_y -= 0.25*inch # Spacing for prompts inside the box
    c.restoreState()
    return y_pos - height - 0.25*inch # Return new Y pos with spacing AFTER the box

def draw_checklist(c, y_pos, title, items, x_offset=0):
    """Draws a title and a list of items with checkboxes. Returns the new y_pos."""
    c.saveState()
    x = MARGIN + x_offset
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(COLOR_TEXT_HEADER)
    c.drawString(x + 0.1*inch, y_pos, title)
    
    current_y = y_pos - 0.25*inch
    c.setFont("Helvetica", 9)
    c.setFillColor(COLOR_TEXT_BODY)
    for item in items:
        c.rect(x + 0.1*inch, current_y - 0.02*inch, 0.1*inch, 0.1*inch)
        c.drawString(x + 0.3*inch, current_y, item)
        current_y -= 0.2*inch
    c.restoreState()
    # Calculate height and return new y
    height = (y_pos - current_y) + 0.25*inch
    return y_pos - height

# --- WEEKLY SPECIALIZED PAGE DRAWING FUNCTIONS (REBUILT FOR CORRECT LAYOUT) ---

def draw_week_1_daily_page(c):
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Daily System Status Report")
    y -= 0.4*inch

    # Right Column is drawn first to set the main height of the page
    prompts = [
        "EVENT: Describe one interaction that generated a significant emotional signal.", "",
        "RAW DATA - SENSATION: Where in your body did you feel it? (e.g., chest tightness)", "",
        "RAW DATA - EMOTION API: If you had to give this feeling a name, what would it be?", "",
        "TRIGGER LOG: What specific event, word, or action immediately preceded the signal?", "",
        "INITIAL HYPOTHESIS: Why do you think this trigger produced this signal? (No judgment)"
    ]
    draw_section(c, y, "EVENT LOG: Analyzing a High-Signal Interaction", prompts, 7.5*inch, COLOR_PRIMARY, x_offset=CONTENT_WIDTH*0.4, width_mult=0.6)

    # Left Column
    checklist_y = y - 0.1*inch
    checklist_y = draw_checklist(c, checklist_y, "PHYSICAL STATE SCAN:", ["Fatigued", "Energized", "Tense", "Relaxed"])
    checklist_y -= 0.4*inch
    checklist_y = draw_checklist(c, checklist_y, "EMOTIONAL STATE SCAN:", ["Anxious/Stressed", "Calm/Content", "Irritable/Angry", "Optimistic/Happy"])
    checklist_y -= 0.4*inch
    draw_checklist(c, checklist_y, "FOCUS LEVEL:", ["Distracted", "Hyper-focused", "Neutral"])
    c.showPage()
    
def draw_week_2_daily_page(c):
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Trigger-Response Debugger")
    y -= 0.4*inch

    prompts_trigger = [
        "TRIGGER (Input): A specific event that occurred.", "", "",
        "AUTOMATIC THOUGHT (Processing): The immediate story I told myself.", "", "",
        "EMOTIONAL-PHYSICAL RESPONSE (Output): The feeling & sensation that resulted."
    ]
    y = draw_section(c, y, "STEP 1: Deconstruct the Automatic Reaction Chain", prompts_trigger, 3.2*inch, COLOR_PRIMARY)

    prompts_deploy = [
        "Did I deploy the 'Tactical Pause' before reacting?  ☐ Yes  ☐ No", "",
        "If YES: What did I do during the pause? (e.g., Deep breath, left the room)", "",
        "If NO: At what point did I realize a pause would have been useful?", "",
        "RESULTING ACTION: What was my actual response after the initial reaction/pause?", "",
        "PERFORMANCE REVIEW: How did deploying (or not deploying) the pause affect the outcome?"
    ]
    draw_section(c, y, "STEP 2: Control System Deployment Analysis", prompts_deploy, 4.3*inch, COLOR_ACCENT)
    c.showPage()

def draw_week_3_daily_page(c):
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Deep Listening Signal Analyzer")
    y -= 0.4*inch

    y = draw_section(c, y, "Log a Conversation for Analysis", ["CONVERSATION CONTEXT: Who was it with? What was the topic?"], 1.0*inch, COLOR_PRIMARY)
    
    # Define starting y for both columns
    column_y_start = y
    
    # Left Column: Signal Breakdown
    c.setFont("Helvetica-Bold", 10); c.drawString(MARGIN, column_y_start, "SIGNAL BREAKDOWN")
    y_left = column_y_start - 0.2*inch; c.setStrokeColor(lightgrey); c.line(MARGIN, y_left, MARGIN + CONTENT_WIDTH*0.48, y_left)
    y_left -= 0.3*inch; c.setFont("Helvetica-Bold", 9); c.drawString(MARGIN, y_left, "Verbal Data (The Words):")
    y_left -= 2.0*inch; c.setFont("Helvetica-Bold", 9); c.drawString(MARGIN, y_left, "Vocal Data (The Tone):")
    y_left -= 2.0*inch; c.setFont("Helvetica-Bold", 9); c.drawString(MARGIN, y_left, "Non-Verbal Data (The Body):")

    # Right Column: My Performance
    x_right = MARGIN + CONTENT_WIDTH*0.52
    c.setFont("Helvetica-Bold", 10); c.drawString(x_right, column_y_start, "MY RECEIVER PERFORMANCE")
    y_right = column_y_start - 0.2*inch; c.setStrokeColor(lightgrey); c.line(x_right, y_right, PAGE_WIDTH - MARGIN, y_right)
    
    checklist_items = ["Planning my response", "Jumping to conclusions", "Ignoring feelings", "Distracted"]
    y_checklist = draw_checklist(c, y_right - 0.1*inch, "LISTENING BARRIERS DETECTED:", checklist_items, x_offset=CONTENT_WIDTH*0.52)

    c.setFont("Helvetica-Bold", 9); c.drawString(x_right, y_checklist, "TECHNIQUES DEPLOYED:")
    y_deploy = y_checklist - 0.3*inch
    c.drawString(x_right, y_deploy, "Paraphrase Attempt:")
    y_deploy -= 1.5*inch
    c.drawString(x_right, y_deploy, "Clarifying Question Asked:")
    c.showPage()
    
def draw_week_4_daily_page(c):
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: 'I-Statement' Message Builder")
    y -= 0.4*inch

    prompts_blame = ["First, write down the blaming thought or 'You-Statement' you wanted to say.", "(e.g., 'You never help out around here.')"]
    y = draw_section(c, y, "STEP 1: Capture the Raw, Uncalibrated Message", prompts_blame, 1.4*inch, COLOR_WARN)

    c.setFont("Helvetica-Bold", 10); c.drawString(MARGIN, y, "STEP 2: Calibrate Using the 'I-Statement' Formula")
    y -= 0.3*inch

    y = draw_section(c, y, "I feel... [Emotion]", [], 1.1*inch, COLOR_PRIMARY)
    y = draw_section(c, y, "when... [Specific, Objective Behavior]", [], 1.6*inch, COLOR_PRIMARY)
    y = draw_section(c, y, "because... [The Impact on You]", [], 1.6*inch, COLOR_PRIMARY)
    draw_section(c, y, "FINAL CALIBRATED MESSAGE", ["Assemble the parts into the final message ready for transmission."], 1.2*inch, COLOR_ACCENT)
    c.showPage()

def draw_week_5_daily_page(c):
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Perspective Simulation Worksheet")
    y -= 0.4*inch

    prompts_context = ["Describe a situation of disagreement or misunderstanding."]
    y = draw_section(c, y, "Simulation Context", prompts_context, 1.2*inch, COLOR_PRIMARY)
    
    column_width_mult = 0.48
    column_height = 5.5*inch
    
    # Left Column: My OS
    prompts_left = ["My Goal in this situation:", "", "My Core Belief/Assumption:", "", "My Primary Emotion/Fear:"]
    draw_section(c, y, "My Operating System", prompts_left, column_height, COLOR_TEXT_BODY, width_mult=column_width_mult)

    # Right Column: Their OS (Simulated)
    prompts_right = ["Their Likely Goal:", "", "Their Likely Belief/Assumption:", "", "Their Likely Emotion/Fear:"]
    draw_section(c, y, "Their Operating System (Simulated)", prompts_right, column_height, COLOR_TEXT_BODY, x_offset=CONTENT_WIDTH*(1-column_width_mult), width_mult=column_width_mult)
    y -= (column_height + 0.25*inch)

    prompts_insight = ["What is one key insight gained from running this simulation? How does it change your approach?"]
    draw_section(c, y, "Simulation Insight", prompts_insight, 1.1*inch, COLOR_ACCENT)
    c.showPage()
    
def draw_week_6_daily_page(c):
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: The COIN Conflict Debugger")
    y -= 0.4*inch
    
    prompts_problem = ["Define the problem you need to discuss as a neutral, shared goal.", "(e.g., 'Finalize the project plan without further delays.')"]
    y = draw_section(c, y, "Problem Statement", prompts_problem, 1.4*inch, COLOR_PRIMARY)
    
    c.setFont("Helvetica-Bold", 10); c.drawString(MARGIN, y, "Execute the COIN Framework")
    y -= 0.3*inch
    
    y = draw_section(c, y, "C - Context: When and where did the specific event happen?", [], 1.5*inch, COLOR_TEXT_BODY)
    y = draw_section(c, y, "O - Observation: What did you see or hear? (Factual, objective)", [], 1.5*inch, COLOR_TEXT_BODY)
    y = draw_section(c, y, "I - Impact: How did this observation affect you/the project? (Use 'I' Statements)", [], 1.5*inch, COLOR_TEXT_BODY)
    draw_section(c, y, "N - Next Steps: What is a collaborative suggestion for moving forward?", [], 1.5*inch, COLOR_TEXT_BODY)
    c.showPage()
    
def draw_week_7_daily_page(c):
    y = PAGE_HEIGHT - MARGIN - 0.4*inch
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN, y, "Tool: Daily Connection Quality Check")
    y -= 0.4*inch

    y = draw_checklist(c, y, "PROACTIVE APPRECIATION PROTOCOL", ["Sent a text/email with a SPECIFIC thank you.", "Publicly acknowledged someone's good work.", "Verbally thanked someone, explaining their positive IMPACT."])
    y -= 0.1*inch
    y = draw_section(c, y, "Appreciation Log", ["Log the details of the appreciation sent:"], 2.0*inch, COLOR_ACCENT)

    y = draw_checklist(c, y, "DEEPER QUESTIONS PROTOCOL", ["Asked a follow-up question based on a past conversation.", "Asked for their opinion/advice on something important.", "Asked about their life/interests outside of our usual context."])
    y -= 0.1*inch
    draw_section(c, y, "Better Questions Log", ["Log the 'better question' you asked and the response:"], 3.0*inch, COLOR_PRIMARY)
    c.showPage()

WEEKLY_DRAW_FUNCTIONS = {
    1: draw_week_1_daily_page, 2: draw_week_2_daily_page, 3: draw_week_3_daily_page,
    4: draw_week_4_daily_page, 5: draw_week_5_daily_page, 6: draw_week_6_daily_page,
    7: draw_week_7_daily_page,
}

def create_engineering_journal():
    c = canvas.Canvas(FILENAME, pagesize=A4)
    start_date = date.today()
    
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
            draw_function = WEEKLY_DRAW_FUNCTIONS.get(week)
            if draw_function:
                draw_function(c) # Removed date_str as it's in the header
            
            day_offset += 1
            
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2, "Week 8: Performance Review & Roadmap")
    c.showPage()

    c.save()
    print(f"✅ Successfully created {FILENAME}")

if __name__ == "__main__":
    create_engineering_journal()