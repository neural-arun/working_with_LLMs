# communication_bootcamp_generator.py
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, lightgrey
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from datetime import date, timedelta

# --- Engineering Color Palette & Configuration ---
# (Consistent with your original design, which is excellent)
COLOR_PRIMARY = HexColor('#007ACC')
COLOR_ACCENT = HexColor('#4EC9B0')
COLOR_WARN = HexColor('#F44747')
COLOR_TEXT_HEADER = HexColor('#2D2D2D')
COLOR_TEXT_BODY = HexColor('#3C3C3C')
FILENAME = "Communication_Mastery_Bootcamp.pdf"

# --- NEW: Motivational Quotes ---
# Easily expandable list of quotes for daily inspiration
QUOTES = [
    "The art of communication is the language of leadership. - James Humes",
    "The single biggest problem in communication is the illusion that it has taken place. - George Bernard Shaw",
    "Effective communication is 20% what you know and 80% how you feel about what you know. - Jim Rohn",
    "To effectively communicate, we must realize that we are all different in the way we perceive the world. - Tony Robbins",
    "You can have brilliant ideas, but if you can't get them across, your ideas won't get you anywhere. - Lee Iacocca",
    "Precision of communication is important, more important than ever, in our era of hair-trigger balances. - James Thurber",
    "The most important thing in communication is hearing what isn't said. - Peter Drucker",
    "Seek first to understand, then to be understood. - Stephen Covey"
]

class JournalGenerator:
    """
    An object-oriented class to handle the creation and layout of the journal.
    This encapsulates all the drawing logic and makes the main script cleaner.
    """
    def __init__(self, filename):
        self.c = canvas.Canvas(filename, pagesize=A4)
        self.width, self.height = A4
        self.margin = 0.7 * inch
        self.content_width = self.width - 2 * self.margin
        self.styles = getSampleStyleSheet()
        self.styles['BodyText'].fontName = 'Helvetica'
        self.styles['BodyText'].fontSize = 9
        self.styles['BodyText'].leading = 14
        self.styles['BodyText'].textColor = COLOR_TEXT_BODY

    def draw_header(self, week, day, date_str):
        self.c.saveState()
        self.c.setFont("Helvetica-Bold", 16)
        self.c.setFillColor(COLOR_TEXT_HEADER)
        self.c.drawString(self.margin, self.height - self.margin, f"Week {week}: {self.get_week_theme(week)}")
        
        self.c.setFont("Helvetica", 11)
        self.c.setFillColor(COLOR_TEXT_BODY)
        self.c.drawRightString(self.width - self.margin, self.height - self.margin, f"Day {day} | {date_str}")
        
        y_pos = self.height - self.margin - 0.1 * inch
        self.c.setStrokeColor(lightgrey)
        self.c.setLineWidth(1)
        self.c.line(self.margin, y_pos, self.width - self.margin, y_pos)
        self.c.restoreState()

    def draw_section(self, y_pos, title, content_prompts, height, color=COLOR_PRIMARY, x_offset=0, custom_width=None):
        width = custom_width if custom_width is not None else self.content_width
        x = self.margin + x_offset
        
        self.c.saveState()
        self.c.setStrokeColor(color)
        self.c.setLineWidth(1.5)
        self.c.rect(x, y_pos - height, width, height)

        if title:
            self.c.setFillColor(color)
            self.c.rect(x, y_pos - 0.4*inch, width, 0.4*inch, fill=1, stroke=0)
            self.c.setFillColor(black)
            self.c.setFont("Helvetica-Bold", 11)
            self.c.drawString(x + 0.15*inch, y_pos - 0.27*inch, title)

        current_y = y_pos - 0.6*inch
        for prompt in content_prompts:
            p = Paragraph(prompt, self.styles['BodyText'])
            p.wrapOn(self.c, width - 0.3*inch, self.height)
            p.drawOn(self.c, x + 0.15*inch, current_y)
            current_y -= p.height + 0.1*inch
            
        self.c.restoreState()
        return y_pos - height - 0.2*inch

    def draw_checklist(self, y_pos, title, items, x_offset=0):
        self.c.saveState()
        x = self.margin + x_offset
        self.c.setFont("Helvetica-Bold", 10)
        self.c.setFillColor(COLOR_TEXT_HEADER)
        self.c.drawString(x + 0.1*inch, y_pos, title)
        
        current_y = y_pos - 0.25*inch
        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(COLOR_TEXT_BODY)
        for item in items:
            self.c.rect(x + 0.1*inch, current_y - 0.02*inch, 0.1*inch, 0.1*inch)
            self.c.drawString(x + 0.3*inch, current_y, item)
            current_y -= 0.2*inch
        self.c.restoreState()
        return current_y
    
    def draw_daily_ops_checklist(self):
        """NEW: A consistent checklist for the start of every day."""
        y = self.height - self.margin - 0.4 * inch
        items = [
            "Initiated one small talk conversation (e.g., with a barista, colleague).",
            "Made eye contact while speaking and listening.",
            "Listened without interrupting in a key conversation.",
            "Asked one open-ended question today.",
        ]
        self.draw_checklist(y, "DAILY OPERATIONS CHECKLIST:", items)

    def draw_footer(self):
        """NEW: A footer with a random motivational quote and a notes section."""
        y = self.margin + 2.5 * inch
        # Draw notes section
        self.draw_section(y, "Field Notes & Observations", [], 2.5 * inch, COLOR_TEXT_BODY)
        # Draw quote
        self.c.saveState()
        self.c.setFont("Helvetica-Oblique", 9)
        self.c.setFillColor(COLOR_TEXT_BODY)
        quote = random.choice(QUOTES)
        self.c.drawCentredString(self.width / 2, self.margin - 0.3 * inch, quote)
        self.c.restoreState()
    
    @staticmethod
    def get_week_theme(week):
        themes = {
            1: "Self-Awareness: The Internal Diagnostic",
            2: "Emotional Regulation: The Control System",
            3: "Active Listening: Upgrading the Receiver",
            4: "Clear Expression: Calibrating the Transmitter",
            5: "Empathy: Building the Protocol Bridge",
            6: "Conflict Resolution: The Debugger",
            7: "Building Rapport: Network Maintenance",
            8: "Influence & Storytelling: Advanced Scenarios" # NEW WEEK
        }
        return themes.get(week, "Final Review")

    # --- Page Layout Definitions ---
    # Each week's layout is now a method of the class.
    
    def draw_week_1_page(self):
        y = self.height - self.margin - 2.2*inch
        prompts = [
            "<b>EVENT:</b> Describe one interaction that generated a significant emotional signal.",
            "<b>RAW DATA (SENSATION):</b> Where in your body did you feel it? (e.g., chest tightness, flushed face)",
            "<b>RAW DATA (EMOTION API):</b> If you had to give this feeling a name, what would it be?",
            "<b>TRIGGER LOG:</b> What specific event, word, or action immediately preceded the signal?",
            "<b>INITIAL HYPOTHESIS:</b> Why do you think this trigger produced this signal? (No judgment, just analysis)"
        ]
        self.draw_section(y, "High-Signal Interaction Log", prompts, 5*inch, COLOR_PRIMARY)

    def draw_week_2_page(self):
        y = self.height - self.margin - 2.2*inch
        prompts1 = [
            "<b>TRIGGER (Input):</b> A specific event that occurred.",
            "<b>AUTOMATIC THOUGHT (Processing):</b> The immediate story I told myself about the event.",
            "<b>EMOTIONAL-PHYSICAL RESPONSE (Output):</b> The feeling & sensation that resulted."
        ]
        y = self.draw_section(y, "Step 1: Deconstruct the Automatic Reaction Chain", prompts1, 2.5*inch, COLOR_PRIMARY)
        
        prompts2 = [
            "Did I deploy the 'Tactical Pause' before reacting? ☐ Yes ☐ No",
            "If YES: What did I do during the pause? (e.g., Deep breath, left the room)",
            "If NO: At what point did I realize a pause would have been useful?",
            "<b>RESULTING ACTION:</b> What was my actual response after the initial reaction/pause?",
            "<b>PERFORMANCE REVIEW:</b> How did deploying (or not deploying) the pause affect the outcome?"
        ]
        self.draw_section(y, "Step 2: Control System Deployment Analysis", prompts2, 3.5*inch, COLOR_ACCENT)

    def draw_week_3_page(self):
        y = self.height - self.margin - 2.2*inch
        y = self.draw_section(y, "Log a Conversation for Analysis", ["<b>CONTEXT:</b> Who was it with? What was the topic?"], 0.9*inch, COLOR_PRIMARY)
        
        col_width = self.content_width / 2 - 0.1*inch
        prompts_left = ["<b>VERBAL DATA (The Words):</b> What were the key phrases they used?", "<b>VOCAL DATA (The Tone):</b> What was their tone, pace, and volume?", "<b>NON-VERBAL DATA (The Body):</b> What was their posture, eye contact, and gestures?"]
        self.draw_section(y, "Signal Breakdown", prompts_left, 4.5*inch, COLOR_TEXT_BODY, custom_width=col_width)
        
        prompts_right = ["Did I plan my response while they spoke? ☐", "Did I jump to conclusions? ☐", "Did I get distracted by my own thoughts? ☐", "<b>PARAPHRASE ATTEMPT:</b> (e.g., 'So what you're saying is...')", "<b>CLARIFYING QUESTION:</b> (e.g., 'Can you tell me more about...')"]
        self.draw_section(y, "My Receiver Performance", prompts_right, 4.5*inch, COLOR_ACCENT, x_offset=col_width + 0.2*inch, custom_width=col_width)

    def draw_week_4_page(self):
        y = self.height - self.margin - 2.2*inch
        y = self.draw_section(y, "Step 1: Capture the Raw 'You-Statement'", ["(e.g., 'You always interrupt me.')"], 1.0*inch, COLOR_WARN)
        
        formula_prompts = {
            "I feel... [Emotion]": 1.0,
            "when... [Specific, Objective Behavior]": 1.3,
            "because... [The Impact on Me]": 1.3,
            "What I would appreciate is... [A Positive Request]": 1.3
        }
        for title, height in formula_prompts.items():
            y = self.draw_section(y, title, [], height, COLOR_PRIMARY)

    def draw_week_5_page(self):
        y = self.height - self.margin - 2.2*inch
        y = self.draw_section(y, "Simulation Context", ["Describe a situation with a strong disagreement or misunderstanding."], 1.2*inch, COLOR_PRIMARY)

        col_width = self.content_width / 2 - 0.1*inch
        prompts = ["<b>My Goal:</b>", "<b>My Core Assumption:</b>", "<b>My Primary Emotion/Fear:</b>"]
        self.draw_section(y, "My Operating System", prompts, 4*inch, COLOR_TEXT_BODY, custom_width=col_width)
        
        prompts_sim = ["<b>Their Likely Goal:</b>", "<b>Their Likely Assumption:</b>", "<b>Their Likely Emotion/Fear:</b>"]
        self.draw_section(y, "Their OS (Simulated)", prompts_sim, 4*inch, COLOR_ACCENT, x_offset=col_width + 0.2*inch, custom_width=col_width)

    def draw_week_6_page(self):
        y = self.height - self.margin - 2.2*inch
        y = self.draw_section(y, "Problem Statement", ["Define the problem as a neutral, shared goal."], 1.0*inch, COLOR_PRIMARY)
        
        coin_prompts = {
            "C - Context: When and where did the specific event happen?": 1.5,
            "O - Observation: What did you see or hear? (Factual, objective)": 1.5,
            "I - Impact: How did this affect you, the team, or the project?": 1.5,
            "N - Next Steps: What is a collaborative suggestion for moving forward?": 1.5
        }
        for title, height in coin_prompts.items():
            y = self.draw_section(y, title, [], height, COLOR_TEXT_BODY)

    def draw_week_7_page(self):
        y = self.height - self.margin - 2.2*inch
        prompts_appreciation = [
            "Who did you appreciate today?", 
            "What SPECIFIC action did you thank them for?",
            "How did you communicate it? (Verbal, text, public praise)"
        ]
        y = self.draw_section(y, "Proactive Appreciation Log", prompts_appreciation, 2.5*inch, COLOR_ACCENT)
        
        prompts_questions = [
            "Who did you seek to understand better today?",
            "What 'better question' did you ask? (e.g., 'What's the most challenging part of this for you?')",
            "What did you learn from their response?"
        ]
        self.draw_section(y, "Better Questions Log", prompts_questions, 2.5*inch, COLOR_PRIMARY)

    def draw_week_8_page(self):
        """NEW: The capstone week for advanced skills."""
        y = self.height - self.margin - 2.2*inch
        prompts1 = [
            "What is a core message or idea you need to convey this week? (e.g., a project proposal, a difficult decision)",
            "<b>The Hook:</b> How can you start to grab their attention?",
            "<b>The Core Narrative:</b> What is the simple story or journey?",
            "<b>The 'Why':</b> Why should they care? What's in it for them?",
            "<b>The Call to Action:</b> What do you want them to do next?"
        ]
        y = self.draw_section(y, "The Storytelling Blueprint", prompts1, 4.0*inch, COLOR_PRIMARY)
        
        prompts2 = [
            "Describe a difficult conversation you need to have or recently had.",
            "What is the IDEAL outcome?",
            "What is the worst-case scenario you fear?",
            "How can you start the conversation from a place of shared interest?"
        ]
        self.draw_section(y, "Difficult Conversation Planner", prompts2, 2.5*inch, COLOR_WARN)

    def generate(self):
        """Main loop to build the PDF document."""
        draw_map = {
            1: self.draw_week_1_page, 2: self.draw_week_2_page, 3: self.draw_week_3_page,
            4: self.draw_week_4_page, 5: self.draw_week_5_page, 6: self.draw_week_6_page,
            7: self.draw_week_7_page, 8: self.draw_week_8_page
        }
        
        # --- Title Page ---
        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawCentredString(self.width/2, self.height/2 + 2*inch, "Communication Mastery Bootcamp")
        self.c.setFont("Helvetica", 14)
        self.c.drawCentredString(self.width/2, self.height/2 + 1.5*inch, "An 8-Week Engineering Approach to Social Dynamics")
        self.c.showPage()
        
        start_date = date.today()
        day_offset = 0
        for week in range(1, 9): # Expanded to 8 weeks
            for day in range(1, 8):
                current_date = start_date + timedelta(days=day_offset)
                date_str = current_date.strftime('%A, %B %d, %Y')
                
                # --- Draw Page Elements ---
                self.draw_header(week, day, date_str)
                self.draw_daily_ops_checklist() # On every page
                
                # Call the correct function for the week's content
                draw_function = draw_map.get(week)
                if draw_function:
                    draw_function()
                
                self.draw_footer() # On every page
                self.c.showPage()
                day_offset += 1
                
        self.save()

    def save(self):
        self.c.save()
        print(f"✅ Successfully created {FILENAME}")


if __name__ == "__main__":
    journal = JournalGenerator(FILENAME)
    journal.generate()