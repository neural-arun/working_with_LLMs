# create_journal.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import slategray, lightgrey, black
from datetime import date, timedelta

# --- Configuration Constants ---
FILENAME = "Bootcamp_Journal.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.75 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
TOP_MARGIN_TOP_HALF = PAGE_HEIGHT - MARGIN
BOTTOM_MARGIN_TOP_HALF = PAGE_HEIGHT / 2 + MARGIN / 2
TOP_MARGIN_BOTTOM_HALF = PAGE_HEIGHT / 2 - MARGIN / 2
BOTTOM_MARGIN_BOTTOM_HALF = MARGIN

# --- Helper function to draw the template for a day ---
def draw_day_template(c, week, day, date_str, top_y):
    """Draws the header and basic layout for a single day's entry."""
    c.saveState()
    
    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(MARGIN, top_y, f"Week {week} - Day {day}")
    c.setFont("Helvetica", 12)
    c.drawRightString(PAGE_WIDTH - MARGIN, top_y, date_str)
    
    # Divider line
    line_y = top_y - 0.25 * inch
    c.setStrokeColor(lightgrey)
    c.setLineWidth(1)
    c.line(MARGIN, line_y, PAGE_WIDTH - MARGIN, line_y)
    
    c.restoreState()
    return line_y - 0.1 * inch # Return the starting y-pos for content

def draw_multiline_text(c, x, y, text, max_width, leading):
    """Draws multi-line text in a given area."""
    lines = []
    # Simple line wrapping
    words = text.split()
    if not words:
        return y
    
    current_line = words[0]
    for word in words[1:]:
        if c.stringWidth(current_line + " " + word, "Helvetica", 10) < max_width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def create_journal_pdf():
    """Generates the entire 8-week bootcamp journal PDF."""
    c = canvas.Canvas(FILENAME, pagesize=A4)
    start_date = date.today()

    # --- Title Page ---
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT / 2 + 1.5 * inch, "My Communication & EQ Bootcamp")
    c.setFont("Helvetica", 16)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT / 2, "An 8-Week Guided Journal")
    c.setFont("Helvetica-Oblique", 12)
    c.drawCentredString(PAGE_WIDTH / 2, MARGIN, f"Generated on: {start_date.strftime('%B %d, %Y')}")
    c.showPage()
    
    # --- Weeks 1-7: Daily Logs ---
    day_counter = 0
    for week in range(1, 8):
        for day in range(1, 8):
            day_counter += 1
            current_date = start_date + timedelta(days=day_counter - 1)
            date_str = current_date.strftime('%A, %B %d, %Y')
            
            # Determine if drawing on top or bottom half
            is_top_half = (day_counter % 2 != 0)
            top_y = TOP_MARGIN_TOP_HALF if is_top_half else TOP_MARGIN_BOTTOM_HALF
            
            # Draw the daily header
            content_y = draw_day_template(c, week, day, date_str, top_y)
            
            c.setFont("Helvetica", 10)
            text_x = MARGIN + 0.1 * inch
            line_spacing = 0.2 * inch
            
            # --- Custom Content for each week ---
            if week == 1:
                c.setFont("Helvetica-Bold", 10)
                content_y -= line_spacing
                c.drawString(text_x, content_y, "Emotion Journal:")
                
                c.setFont("Helvetica", 10)
                content_y -= line_spacing
                c.drawString(text_x + 0.2*inch, content_y, "a. What did I physically feel?")
                content_y -= 1 * inch
                c.drawString(text_x + 0.2*inch, content_y, "b. What was the emotion I'd name for this feeling?")
                content_y -= 1 * inch
                c.drawString(text_x + 0.2*inch, content_y, "c. What was the trigger?")
                
                content_y = top_y - 0.9*inch # Reset for second column
                c.setFont("Helvetica-Bold", 10)
                c.drawString(MARGIN + CONTENT_WIDTH/2, content_y, "Communication Log:")
                c.setFont("Helvetica-Oblique", 9)
                c.drawString(MARGIN + CONTENT_WIDTH/2, content_y - 0.2*inch, "(Note a conversation that went poorly. Just record data.)")

            elif week == 2:
                c.setFont("Helvetica-Bold", 10)
                content_y -= line_spacing
                c.drawString(text_x, content_y, "Emotion Journal Update:")

                c.setFont("Helvetica", 10)
                content_y -= line_spacing
                c.drawString(text_x + 0.2*inch, content_y, "Did I pause before reacting? What happened when I did?")
                
                content_y -= 1.5 * inch
                c.setFont("Helvetica-Bold", 10)
                c.drawString(text_x, content_y, "'Name It to Tame It' Practice:")
                c.setFont("Helvetica", 10)
                content_y -= line_spacing
                c.drawString(text_x + 0.2*inch, content_y, "Mentally label the emotion you felt (e.g., 'This is anger.').")
                
            elif week == 3:
                c.setFont("Helvetica-Bold", 10)
                content_y -= line_spacing
                c.drawString(text_x, content_y, "Deep Listening Practice: Paraphrasing")
                c.setFont("Helvetica-Oblique", 9)
                content_y -= 0.2*inch
                c.drawString(text_x, content_y, "Log a moment where you tried to paraphrase. (e.g., 'So, if I'm understanding you...')")
                
                content_y -= 2 * inch
                c.setFont("Helvetica-Bold", 10)
                c.drawString(text_x, content_y, "Asking Clarifying Questions")
                c.setFont("Helvetica-Oblique", 9)
                content_y -= 0.2*inch
                c.drawString(text_x, content_y, "Before offering an opinion, what one question did you ask to go deeper?")

            elif week == 4:
                c.setFont("Helvetica-Bold", 10)
                content_y -= line_spacing
                c.drawString(text_x, content_y, "Practicing 'I' Statements")
                
                c.setFont("Helvetica", 9)
                text = "Use the formula: 'I feel [Emotion] when [Specific Behavior] because [Reason/Impact on You].' First, rewrite a blaming thought here. Then, try it in a real conversation."
                content_y -= line_spacing
                content_y = draw_multiline_text(c, text_x, content_y, text, CONTENT_WIDTH - 0.2*inch, 14)

            elif week == 5:
                c.setFont("Helvetica-Bold", 10)
                content_y -= line_spacing
                c.drawString(text_x, content_y, "Perspective-Taking Exercise")
                
                c.setFont("Helvetica", 9)
                text = "Think of someone you disagree with. Write out a situation from their point of view. What are their motivations, fears, and goals?"
                content_y -= line_spacing
                content_y = draw_multiline_text(c, text_x, content_y, text, CONTENT_WIDTH - 0.2*inch, 14)
                
                content_y -= 0.5 * inch
                c.setFont("Helvetica-Bold", 10)
                c.drawString(text_x, content_y, "Verbal Acknowledgment Log")
                c.setFont("Helvetica-Oblique", 9)
                content_y -= 0.2*inch
                c.drawString(text_x, content_y, "Note a time you said: 'From your perspective, it must seem like...'")

            elif week == 6:
                c.setFont("Helvetica-Bold", 10)
                content_y -= line_spacing
                c.drawString(text_x, content_y, "Handling Difficult Conversations: The COIN Framework")
                
                c.setFont("Helvetica", 10)
                content_y -= line_spacing * 1.5
                c.drawString(text_x, content_y, "Context:")
                content_y -= 1 * inch
                c.drawString(text_x, content_y, "Observation (Objective facts):")
                content_y -= 1 * inch
                c.drawString(text_x, content_y, "Impact (Use an 'I' statement):")
                content_y -= 1 * inch
                c.drawString(text_x, content_y, "Next Steps (Propose a way forward):")
                
            elif week == 7:
                c.setFont("Helvetica-Bold", 10)
                content_y -= line_spacing
                c.drawString(text_x, content_y, "Practice Asking Better Questions")
                c.setFont("Helvetica-Oblique", 9)
                content_y -= 0.2*inch
                c.drawString(text_x, content_y, "Instead of 'How are you?', what specific question did you ask today?")
                
                content_y -= 2 * inch
                c.setFont("Helvetica-Bold", 10)
                c.drawString(text_x, content_y, "The Appreciation Log")
                c.setFont("Helvetica-Oblique", 9)
                content_y -= 0.2*inch
                c.drawString(text_x, content_y, "Note one specific, genuine appreciation you expressed today.")

            # Move to a new page after every two days
            if day_counter % 2 == 0:
                c.showPage()
                
    # If total days is odd, need to push the last half page
    if day_counter % 2 != 0:
        c.showPage()
        
    # --- Week 8: Final Review ---
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 1.5*inch, "Week 8: The Full Stack - Integration & Roadmap")
    
    # Review Your Journal
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, PAGE_HEIGHT - 2.5*inch, "1. Review Your Journal")
    c.setFont("Helvetica", 10)
    text = "Read your entries from Week 1. What patterns do you notice? What has changed? Acknowledge your progress and write your key takeaways below."
    draw_multiline_text(c, MARGIN, PAGE_HEIGHT - 2.8*inch, text, CONTENT_WIDTH, 14)
    c.showPage()

    # Identify Biggest Challenge
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, PAGE_HEIGHT - 1.5*inch, "2. Identify Your Biggest Challenge")
    c.setFont("Helvetica", 10)
    text = "Looking back over the last seven weeks, what is still the hardest part for you? Is it pausing before reacting? Listening without formulating a response? Giving feedback? Be specific."
    draw_multiline_text(c, MARGIN, PAGE_HEIGHT - 1.8*inch, text, CONTENT_WIDTH, 14)
    c.showPage()

    # Create a Mini-Plan
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN, PAGE_HEIGHT - 1.5*inch, "3. Create a Mini-Plan for the Next Month")
    c.setFont("Helvetica", 10)
    text = "Based on your biggest challenge, set one specific, small, and achievable goal for the next month. What is the goal? What one daily or weekly action will you take to work on it? How will you measure success?"
    draw_multiline_text(c, MARGIN, PAGE_HEIGHT - 1.8*inch, text, CONTENT_WIDTH, 14)

    c.save()
    print(f"✅ Successfully created {FILENAME}")

if __name__ == "__main__":
    create_journal_pdf()