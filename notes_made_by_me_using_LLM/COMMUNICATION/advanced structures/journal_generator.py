# journal_generator.py

import os
import argparse
import logging
import yaml
from datetime import date, timedelta, datetime
from typing import Optional, Dict, Any, List

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, lightgrey
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# --- Setup logging ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("SocialMasteryJournal")

# --- Constants ---
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.75 * inch
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
COLORS = {
    'primary': HexColor('#007ACC'), 'accent': HexColor('#4EC9B0'),
    'warn': HexColor('#F44747'), 'energy': HexColor('#FFB347'),
    'wisdom': HexColor('#9370DB'), 'knowledge': HexColor('#FF6B6B'),
    'bg_light': HexColor('#F8F9FA'), 'text_header': HexColor('#1A1A1A'),
    'text_body': HexColor('#2C2C2C'), 'checkbox': HexColor('#28A745'),
    'todo': HexColor('#FD7E14'), 'notes': HexColor('#6F42C1'),
    'white': HexColor('#FFFFFF'), 'light_grey': lightgrey,
}

class JournalGenerator:
    """
    Generates a personalized Social Mastery Journal PDF from a YAML content file.
    This class uses an object-oriented structure and robust text rendering with
    reportlab.platypus.Paragraph to prevent text overlaps.
    """
    def __init__(self, content: Dict[str, Any], start_date: date, filename: str):
        self.content = content
        self.start_date = start_date
        self.filename = filename
        self.user_profile = self.content['user_profile']
        self.c = canvas.Canvas(self.filename, pagesize=A4)
        self._setup_metadata()
        self._setup_styles()

    def _setup_metadata(self):
        """Sets the PDF metadata."""
        self.c.setTitle(f"Social Mastery Journal for {self.user_profile['name']}")
        self.c.setAuthor(self.user_profile['name'])
        self.c.setSubject(f"7-week program for {self.user_profile['career_goal']}")
        self.c.setCreator("Journal Generator v4.0")

    def _setup_styles(self):
        """Creates a central stylesheet for consistent typography."""
        styles = getSampleStyleSheet()
        self.styles = {
            'h1': ParagraphStyle('h1', parent=styles['h1'], fontName='Helvetica-Bold', fontSize=24, spaceAfter=14, alignment=TA_CENTER, textColor=COLORS['primary']),
            'h2': ParagraphStyle('h2', parent=styles['h2'], fontName='Helvetica-Bold', fontSize=18, spaceAfter=10, alignment=TA_CENTER, textColor=COLORS['text_header']),
            'h3': ParagraphStyle('h3', parent=styles['h3'], fontName='Helvetica-Bold', fontSize=14, spaceAfter=8, textColor=COLORS['text_header']),
            'body': ParagraphStyle('body', parent=styles['BodyText'], fontName='Helvetica', fontSize=11, leading=15, textColor=COLORS['text_body']),
            'body_bold': ParagraphStyle('body_bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=COLORS['text_body']),
            'centered': ParagraphStyle('centered', parent=styles['BodyText'], fontName='Helvetica', fontSize=12, alignment=TA_CENTER, textColor=COLORS['text_body']),
            'list': ParagraphStyle('list', parent=styles['BodyText'], fontName='Helvetica', fontSize=11, leading=16, leftIndent=18),
        }

    def _draw_paragraph(self, text: str, y: float, style: ParagraphStyle, x: float = MARGIN, width: float = CONTENT_WIDTH) -> float:
        """Draws a Paragraph and returns the height it consumed."""
        if not text: return 0
        p = Paragraph(text, style)
        p_width, p_height = p.wrapOn(self.c, width, PAGE_HEIGHT)
        if y - p_height < MARGIN:
            self.c.showPage()
            y = PAGE_HEIGHT - MARGIN
        p.drawOn(self.c, x, y - p_height)
        return p_height

    def _draw_checkbox(self, x, y, size=10):
        """Draws a checkbox."""
        self.c.saveState()
        self.c.setStrokeColor(COLORS['checkbox'])
        self.c.setLineWidth(1)
        self.c.rect(x, y, size, size)
        self.c.restoreState()

    def _draw_header(self, week: int, day: int, date_str: str):
        """Draws the daily page header."""
        y = PAGE_HEIGHT - 0.5 * inch
        self.c.setFont("Helvetica-Bold", 20)
        self.c.setFillColor(COLORS['text_header'])
        self.c.drawString(MARGIN, y, f"Week {week}: Progressive Social Lab")

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(COLORS['text_body'])
        self.c.drawRightString(PAGE_WIDTH - MARGIN, y, f"Day {(week-1)*7 + day} of 49")
        self.c.setFont("Helvetica", 11)
        self.c.drawRightString(PAGE_WIDTH - MARGIN, y - 0.2 * inch, date_str)

        line_y = y - 0.4 * inch
        self.c.setStrokeColor(COLORS['primary'])
        self.c.setLineWidth(2)
        self.c.line(MARGIN, line_y, PAGE_WIDTH - MARGIN, line_y)

    def draw_intro_bio_page(self):
        """Draws the personalized introductory bio page."""
        y = PAGE_HEIGHT - 1.5 * inch
        y -= self._draw_paragraph("Personalized Social Mastery Journal", y, self.styles['h1'])
        y -= self._draw_paragraph("Master-Level Design for Peak Performance", y, self.styles['h2'], style_kwargs={'textColor': COLORS['accent']})
        
        y -= 1 * inch
        bio_text = f"""
        <b>Name:</b> {self.user_profile['name']}<br/>
        <b>Location:</b> {self.user_profile['location']}<br/>
        <b>Main Project:</b> {self.user_profile['main_project']}<br/>
        <b>Career Goal:</b> {self.user_profile['career_goal']}
        """
        y -= self._draw_paragraph(bio_text, y, self.styles['h3'])

        y -= 0.5 * inch
        mission_text = "This journal is crafted for you—a growth-minded developer & founder. Use it to engineer the communication skills that will multiply your technical impact."
        self._draw_paragraph(mission_text, y, self.styles['centered'], style_kwargs={'textColor': COLORS['wisdom']})

        self.c.showPage()

    def draw_knowledge_module_page(self, week: int):
        """Draws the weekly knowledge module page."""
        module = self.content['knowledge_modules'].get(week, {})
        if not module:
            logger.warning(f"No knowledge module found for week {week}")
            return

        y = PAGE_HEIGHT - 1.3 * inch
        y -= self._draw_paragraph(f"WEEK {week} KNOWLEDGE MODULE", y, self.styles['h1'], style_kwargs={'textColor': COLORS['knowledge'], 'fontSize': 26})
        y -= self._draw_paragraph(module.get('title', 'Untitled'), y, self.styles['h2'])
        y -= 0.5 * inch

        # Learning Resources
        y -= self._draw_paragraph("📚 RECOMMENDED LEARNING RESOURCES:", y, self.styles['h3'])
        for resource in module.get('learning_resources', []):
            self._draw_checkbox(MARGIN, y - 12)
            y -= self._draw_paragraph(resource, y, self.styles['list'])
            y -= 0.1 * inch

        y -= 0.3 * inch

        # Key Concepts
        y -= self._draw_paragraph("🎯 KEY CONCEPTS TO MASTER:", y, self.styles['h3'])
        for concept in module.get('key_concepts', []):
            y -= self._draw_paragraph(f"• {concept}", y, self.styles['list'], x=MARGIN, width=CONTENT_WIDTH - 20)
            self._draw_checkbox(PAGE_WIDTH - MARGIN - 15, y + 12) # Checkbox on the right
            y -= 0.1 * inch
        
        self.c.showPage()
        
    def draw_daily_page(self, week: int, day: int, date_str: str):
        """Draws a full 3-page daily entry."""
        # --- Page 1: Plan & Challenge ---
        self._draw_header(week, day, date_str)
        y = PAGE_HEIGHT - MARGIN - 0.6*inch

        # Progressive Challenge Box
        challenge = self.content['progressive_challenges'].get(week, [])[day-1]
        y -= self._draw_paragraph(f"🎯 <b>DAY {day} PROGRESSIVE CHALLENGE:</b><br/>{challenge}", y, self.styles['body_bold'])
        y -= 0.5 * inch

        # Study Note
        note = self.content['daily_study_notes'].get(week, [])[day-1]
        y -= self._draw_paragraph(f"📚 <b>TODAY'S STUDY NOTE:</b><br/>{note}", y, self.styles['body'])
        y -= 0.5 * inch

        # TODOs
        todos = self.content['daily_todos'].get(week, [])[day-1]
        y -= self._draw_paragraph("✅ <b>TODAY'S PREPARATION TODOs:</b>", y, self.styles['body_bold'])
        for todo in todos:
            self._draw_checkbox(MARGIN + 5, y - 12)
            y -= self._draw_paragraph(todo[2:], y, self.styles['list'])
        
        self.c.showPage()
        
        # --- Page 2: Execution & Learning ---
        self._draw_header(week, day, f"{date_str} (Execution)")
        y = PAGE_HEIGHT - MARGIN - 0.6*inch
        # Simplified for brevity - add prompts as paragraphs
        y -= self._draw_paragraph("📊 <b>DETAILED EXECUTION TRACKING</b>", y, self.styles['h3'])
        y -= self._draw_paragraph("Record the details of your practice session here.", y, self.styles['body'])
        y -= 2 * inch
        y -= self._draw_paragraph("🧠 <b>LEARNING & INSIGHTS</b>", y, self.styles['h3'])
        y -= self._draw_paragraph("What did you learn? How does this apply to NEETPrepGPT?", y, self.styles['body'])

        self.c.showPage()

        # --- Page 3: Reflection & Planning ---
        self._draw_header(week, day, f"{date_str} (Reflection)")
        y = PAGE_HEIGHT - MARGIN - 0.6*inch
        y -= self._draw_paragraph("🤔 <b>DEEP REFLECTION & ANALYSIS</b>", y, self.styles['h3'])
        y -= self._draw_paragraph("What were your wins and challenges?", y, self.styles['body'])
        y -= 2 * inch
        y -= self._draw_paragraph("⏭️ <b>TOMORROW'S STRATEGIC PLANNING</b>", y, self.styles['h3'])
        y -= self._draw_paragraph("How will you prepare for tomorrow's challenge?", y, self.styles['body'])

        self.c.showPage()

    def generate(self):
        """Main method to generate the entire PDF journal."""
        logger.info(f"Starting journal generation for {self.user_profile['name']}...")
        
        self.draw_intro_bio_page()

        day_offset = 0
        for week in range(1, 8):
            logger.info(f"Generating Week {week}...")
            self.draw_knowledge_module_page(week)
            
            for day in range(1, 8):
                current_date = self.start_date + timedelta(days=day_offset)
                date_str = current_date.strftime('%A, %B %d, %Y')
                self.draw_daily_page(week, day, date_str)
                day_offset += 1
            
            # self.draw_weekly_review_page(week) # This would be another detailed method

        self.c.save()
        logger.info(f"✅ Journal generation successful! File saved as: {self.filename}")

    # Helper to add styles dynamically - useful for one-off color changes
    def _get_style(self, base_style, **kwargs):
        new_style = ParagraphStyle(name='temp_style', parent=base_style)
        for key, value in kwargs.items():
            setattr(new_style, key, value)
        return new_style

    def _draw_paragraph(self, text: str, y: float, base_style: ParagraphStyle, x: float = MARGIN, width: float = CONTENT_WIDTH, style_kwargs: dict = None) -> float:
        """Draws a Paragraph with optional style overrides and returns its height."""
        if not text: return 0
        
        style = self._get_style(base_style, **style_kwargs) if style_kwargs else base_style
        
        p = Paragraph(text, style)
        p_width, p_height = p.wrapOn(self.c, width, PAGE_HEIGHT)
        if y - p_height < MARGIN:
            self.c.showPage()
            y = PAGE_HEIGHT - MARGIN
        p.drawOn(self.c, x, y - p_height)
        return p_height + base_style.spaceAfter


def main():
    """CLI entry point for the journal generator."""
    parser = argparse.ArgumentParser(description="Generate a Social Mastery Journal PDF from a YAML file.")
    parser.add_argument("--start-date", type=str, help="Start date in YYYY-MM-DD format. Defaults to today.")
    parser.add_argument("--output", type=str, default="Social_Mastery_Journal.pdf", help="Output PDF filename.")
    parser.add_argument("--content", type=str, default="journal_content.yaml", help="Path to the YAML content file.")
    args = parser.parse_args()

    # --- Date Parsing ---
    start_date = date.today()
    if args.start_date:
        try:
            start_date = datetime.strptime(args.start_date, "%Y-%m-%d").date()
        except ValueError:
            logger.error("Invalid date format. Use YYYY-MM-DD. Using today's date.")
    
    # --- Content Loading ---
    try:
        with open(args.content, 'r', encoding='utf-8') as f:
            content_data = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Error: Content file not found at '{args.content}'.")
        return
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        return

    # --- PDF Generation ---
    try:
        generator = JournalGenerator(content_data, start_date, args.output)
        generator.generate()
    except Exception as e:
        logger.error(f"A critical error occurred during PDF generation: {e}", exc_info=True)


if __name__ == "__main__":
    main()