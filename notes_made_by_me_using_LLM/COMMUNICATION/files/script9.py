# Enhanced Progressive Social Mastery Engineering Journal - v2 (PLATYPUS Refactor)
# ---------------------------------------------------------------------------------
# This version refactors the original script to use the ReportLab PLATYPUS framework.
# Key Improvements:
#   - Robust Layout: Automatic text wrapping using Paragraphs. No more manual line breaks.
#   - Maintainability: Layout is managed by flowable elements, not hardcoded coordinates.
#   - Cleaner Code: An object-oriented approach (JournalGenerator class) encapsulates logic.
#   - Reusability: Components (like styled boxes) are easier to create and reuse.
# ---------------------------------------------------------------------------------

import sys
from datetime import date, timedelta
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import slategray, lightgrey, black, HexColor, white
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

# --- Enhanced Color Palette (Constants) ---
COLOR_PRIMARY = HexColor('#007ACC')
COLOR_ACCENT = HexColor('#4EC9B0')
COLOR_WARN = HexColor('#F44747')
COLOR_ENERGY = HexColor('#FFB347')
COLOR_WISDOM = HexColor('#9370DB')
COLOR_KNOWLEDGE = HexColor('#FF6B6B')
COLOR_BG_LIGHT = HexColor('#F3F3F3')
COLOR_TEXT_HEADER = HexColor('#2D2D2D')
COLOR_TEXT_BODY = HexColor('#3C3C3C')

# --- Journal Content (Data remains the same) ---
# KNOWLEDGE_MODULES, PROGRESSIVE_CHALLENGES, WEEKLY_METRICS, GOAL_TEMPLATES
# are unchanged and assumed to be defined as in the original script.
# (Copy and paste the data dictionaries from your original script here)
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
PROGRESSIVE_CHALLENGES = {
    1: [
        # Week 1: Building Social Awareness (Progressive Difficulty)
        "Day 1: Make conscious eye contact with 5 strangers and smile. Log their reactions.",
        "Day 2: Eye contact + smile with 3 people, say 'Hello/Good morning' to 2 others.",
        "Day 3: Ask 1 person a simple logistical question ('Excuse me, do you know the time?').",
        "Day 4: Give 1 genuine compliment to a service worker or acquaintance.",
        "Day 5: Ask a logistical question + make one follow-up comment/observation.",
        "Day 6: Have one complete 3-turn conversation (You speak, they respond, you respond).",
        "Day 7: Initiate 2 brief conversations with strangers in low-stakes environments."
    ],
    2: [
        # Week 2: Response Control (Progressive Difficulty)
        "Day 1: Use the 'tactical pause' (3 deep breaths) before responding to any minor irritation.",
        "Day 2: Catch yourself planning a response while someone is talking. Reset and listen.",
        "Day 3: When feeling triggered, name the emotion silently before responding.",
        "Day 4: Use the STOP technique in one potentially reactive situation.",
        "Day 5: Transform one complaint into a specific, actionable request.",
        "Day 6: Practice the 6-second rule when feeling strong emotion before responding.",
        "Day 7: Navigate one challenging conversation using all response control techniques."
    ],
    3: [
        # Week 3: Deep Listening (Progressive Difficulty)
        "Day 1: In one conversation, focus only on listening - no planning your response.",
        "Day 2: Ask 'What I heard is...' and confirm understanding in one conversation.",
        "Day 3: Ask 2 clarifying questions in a single conversation before giving your input.",
        "Day 4: Identify and reflect back one emotion you heard in someone's words.",
        "Day 5: Use active listening in a conversation where you disagree with the person.",
        "Day 6: Practice empathic listening - focus on understanding their feelings and needs.",
        "Day 7: Conduct one 'deep listening' conversation lasting at least 15 minutes."
    ],
    4: [
        # Week 4: Clear Communication (Progressive Difficulty)
        "Day 1: Replace one 'You' statement with an 'I' statement in conversation.",
        "Day 2: Make one request using the format: 'I would appreciate if...' instead of complaining.",
        "Day 3: Express a preference clearly without apologizing or over-explaining.",
        "Day 4: Share one vulnerable feeling using 'I feel... when... because...' format.",
        "Day 5: Set one clear boundary using assertive (not aggressive) language.",
        "Day 6: Ask for something you want directly and specifically.",
        "Day 7: Have one complete difficult conversation using I-statements and clear requests."
    ],
    5: [
        # Week 5: Empathy & Perspective-Taking (Progressive Difficulty)
        "Day 1: Ask someone 'How are you really doing?' and listen for the deeper answer.",
        "Day 2: Before responding in a disagreement, mentally summarize their perspective.",
        "Day 3: Ask one person about their dreams, goals, or what they're excited about.",
        "Day 4: Share something vulnerable about your own experience or struggles.",
        "Day 5: When someone is upset, focus on understanding their underlying need.",
        "Day 6: Practice seeing a current conflict entirely from the other person's viewpoint.",
        "Day 7: Have one conversation where you spend 80% of the time understanding them."
    ],
    6: [
        # Week 6: Conflict Resolution (Progressive Difficulty)
        "Day 1: Address one small issue directly instead of letting it build up.",
        "Day 2: Use collaborative language ('How can we...') in one disagreement.",
        "Day 3: Practice the COIN method for giving difficult feedback to someone.",
        "Day 4: Apologize for something specific without making excuses or deflecting.",
        "Day 5: Find one area of agreement in a conversation with someone you disagree with.",
        "Day 6: Turn one conflict into a problem-solving session by focusing on solutions.",
        "Day 7: Have the difficult conversation you've been avoiding using all conflict resolution tools."
    ],
    7: [
        # Week 7: Relationship Building (Progressive Difficulty)
        "Day 1: Send a specific appreciation message to someone who helped you recently.",
        "Day 2: Reach out to one person you haven't connected with in months.",
        "Day 3: Ask someone for advice on something you're genuinely curious about.",
        "Day 4: Invite someone to do an activity together (coffee, lunch, walk).",
        "Day 5: Introduce two people who should know each other.",
        "Day 6: Offer specific help to someone without them asking.",
        "Day 7: Plan follow-up actions to deepen 2-3 relationships from your week's connections."
    ]
}
WEEKLY_METRICS = {
    1: "Binary Success Metric: Did you complete each day's specific challenge? Track: Yes/No + comfort level (1-10) + one thing learned",
    2: "Response Time Metric: How long between trigger and thoughtful response? Track: Seconds + technique used + outcome quality (1-10)",
    3: "Listening Quality Metric: In each conversation, did the other person say 'Yes, that's exactly right' to your paraphrase? Track: Yes/No + their satisfaction level",
    4: "Message Clarity Metric: Did your message land as intended? Track: Their response matched your intent (Yes/No) + follow-up questions needed",
    5: "Empathy Accuracy Metric: When you guessed someone's feeling/need, were you right? Track: Accurate guess (Yes/No) + their confirmation",
    6: "Resolution Success Metric: Did the conflict discussion end with agreed-upon next steps? Track: Mutual agreement reached (Yes/No) + relationship strengthened",
    7: "Connection Depth Metric: Did your interaction lead to concrete next steps? Track: Follow-up planned (Yes/No) + relationship investment level (1-10)"
}
GOAL_TEMPLATES = {
    1: "My specific goal this week: Reduce social anxiety in [specific context] by practicing low-stakes social interactions to build confidence.",
    2: "My specific goal this week: Gain control over my [specific trigger] reactions, especially in [context like meetings/family/dating].",
    3: "My specific goal this week: Become a better listener in [specific relationship/context] to deepen understanding and connection.",
    4: "My specific goal this week: Learn to express my needs clearly in [specific situations] without being aggressive or passive.",
    5: "My specific goal this week: Build deeper empathy with [specific people/types of people] to strengthen those relationships.",
    6: "My specific goal this week: Address [specific conflict/tension] using structured approaches rather than avoidance.",
    7: "My specific goal this week: Strengthen my [professional/personal] network by reconnecting with [specific types of people]."
}

# --- Main Generator Class ---
class JournalGenerator:
    """
    A class to generate the Progressive Social Mastery Journal PDF using PLATYPUS.
    """
    def __init__(self, filename="Progressive_Social_Mastery_Journal_v2.pdf"):
        self.filename = filename
        self.width, self.height = A4
        self.margin = 0.6 * inch
        self.content_width = self.width - 2 * self.margin
        self.story = []
        self._register_styles()
        self.current_page_info = {}

    def _register_styles(self):
        """Central place to define all ParagraphStyles."""
        styles = getSampleStyleSheet()
        self.styles = {
            'Normal': styles['Normal'],
            'h1': styles['h1'],
            'h2': styles['h2'],
            'BodyText': styles['BodyText'],
            'Title': ParagraphStyle(name='Title', parent=styles['h1'], fontSize=28, alignment=TA_CENTER, textColor=COLOR_PRIMARY),
            'Subtitle': ParagraphStyle(name='Subtitle', parent=styles['h2'], fontSize=16, alignment=TA_CENTER, textColor=COLOR_TEXT_HEADER),
            'Header': ParagraphStyle(name='Header', fontSize=18, fontName='Helvetica-Bold', textColor=COLOR_TEXT_HEADER),
            'Date': ParagraphStyle(name='Date', fontSize=11, alignment=TA_RIGHT, textColor=COLOR_TEXT_BODY),
            'SectionTitle': ParagraphStyle(name='SectionTitle', fontSize=11, fontName='Helvetica-Bold', textColor=white),
            'Prompt': ParagraphStyle(name='Prompt', fontSize=9, textColor=COLOR_TEXT_BODY, spaceAfter=4),
            'Small': ParagraphStyle(name='Small', fontSize=10, textColor=COLOR_TEXT_BODY),
            'Bullet': ParagraphStyle(name='Bullet', parent=self.styles['Small'], leftIndent=0.2*inch, spaceAfter=6),
            'BoldSmall': ParagraphStyle(name='BoldSmall', parent=self.styles['Small'], fontName='Helvetica-Bold'),
        }

    def _header(self, canvas, doc):
        """Draws the header on each page."""
        canvas.saveState()
        week = self.current_page_info.get('week', 1)
        day = self.current_page_info.get('day', 1)
        date_str = self.current_page_info.get('date_str', '')

        # Main title
        canvas.setFont("Helvetica-Bold", 18)
        canvas.setFillColor(COLOR_TEXT_HEADER)
        canvas.drawString(self.margin, self.height - self.margin + 0.1*inch, f"Week {week}: Progressive Social Lab")

        # Date and day
        canvas.setFont("Helvetica", 11)
        canvas.setFillColor(COLOR_TEXT_BODY)
        canvas.drawRightString(self.width - self.margin, self.height - self.margin + 0.1*inch, f"Day {day} | {date_str}")
        
        # Separator line
        canvas.setStrokeColor(lightgrey)
        canvas.setLineWidth(1)
        canvas.line(self.margin, self.height - self.margin - 0.15*inch, self.width - self.margin, self.height - self.margin - 0.15*inch)
        
        canvas.restoreState()

    def _create_section(self, title, content_prompts, color=COLOR_PRIMARY):
        """Creates a styled section using a Table for robust layout."""
        title_para = Paragraph(title, self.styles['SectionTitle'])
        
        content = []
        for prompt in content_prompts:
            content.append(Paragraph(prompt, self.styles['Prompt']))
            # Add space for writing, represented by a Spacer. A real line is purely decorative.
            content.append(Spacer(1, 0.2 * inch))

        data = [
            [title_para],
            [content]
        ]
        
        table = Table(data, colWidths=[self.content_width - 12]) # Subtract padding
        
        style = TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), color),
            ('TEXTCOLOR', (0, 0), (0, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOX', (0, 0), (-1, -1), 1.5, color),
            ('TOPPADDING', (0, 0), (0, 0), 8),
            ('BOTTOMPADDING', (0, 0), (0, 0), 8),
            ('LEFTPADDING', (0, 0), (0, 0), 8),
            ('RIGHTPADDING', (0, 0), (0, 0), 8),
            ('LEFTPADDING', (0, 1), (0, 1), 10),
            ('RIGHTPADDING', (0, 1), (0, 1), 10),
            ('TOPPADDING', (0, 1), (0, 1), 10),
        ])
        
        table.setStyle(style)
        return [table, Spacer(1, 0.2 * inch)]

    def _build_intro_page(self):
        """Builds the flowables for the intro page."""
        flowables = [
            Spacer(1, 1.5 * inch),
            Paragraph("PROGRESSIVE SOCIAL", self.styles['Title']),
            Paragraph("MASTERY SYSTEM", self.styles['Title']),
            Spacer(1, 0.2 * inch),
            Paragraph("An Engineering Approach to Communication Excellence", self.styles['Subtitle']),
            Spacer(1, 0.2 * inch),
            Paragraph("From Introvert to Influential Communicator", ParagraphStyle(name='Tagline', parent=self.styles['Subtitle'], textColor=COLOR_ACCENT, fontSize=14)),
            Spacer(1, 0.4 * inch),
            Paragraph("🔧 SYSTEM FEATURES:", ParagraphStyle(name='Features', parent=self.styles['h2'], alignment=TA_CENTER, textColor=COLOR_ENERGY, fontSize=12)),
            Spacer(1, 0.2 * inch),
        ]
        
        features_text = [
            "✅ Progressive Difficulty: Each week builds on the last with scaffolded challenges",
            "✅ Knowledge Modules: Learn the theory before practicing the skills",
            "✅ Concrete Metrics: Measurable success criteria for every challenge",
            "✅ Personal Goals: Customize each week to your specific social contexts",
            "✅ Daily Tracking: Detailed reflection and progress monitoring",
            "✅ Evidence-Based: Rooted in psychology, neuroscience, and communication research"
        ]
        for feature in features_text:
            flowables.append(Paragraph(feature, ParagraphStyle(name='FeatureItem', alignment=TA_CENTER, textColor=COLOR_TEXT_BODY, fontSize=11)))
        
        flowables.append(Spacer(1, 0.4 * inch))
        flowables.append(Paragraph("🚀 YOUR TRANSFORMATION COMMITMENT:", ParagraphStyle(name='Commitment', parent=self.styles['h2'], alignment=TA_CENTER, textColor=COLOR_WISDOM, fontSize=12)))
        flowables.append(Spacer(1, 0.2 * inch))
        
        mission_text = [
            "This system will transform you from socially anxious to socially confident.",
            "You will master the engineering principles of human connection.",
            "Every interaction becomes data. Every challenge builds competence.",
            "In 7 weeks, you will have the communication skills to accelerate your career.",
            "Commit fully. Follow the system. Become unstoppable."
        ]
        for line in mission_text:
            flowables.append(Paragraph(line, ParagraphStyle(name='MissionItem', alignment=TA_CENTER, textColor=COLOR_TEXT_BODY, fontSize=11)))
            
        flowables.append(PageBreak())
        return flowables

    def _build_knowledge_page(self, week):
        """Builds the flowables for a weekly knowledge module page."""
        module = KNOWLEDGE_MODULES[week]
        flowables = [
            Spacer(1, 1 * inch),
            Paragraph(f"WEEK {week} KNOWLEDGE MODULE", ParagraphStyle(name='KMTitle', fontSize=22, alignment=TA_CENTER, textColor=COLOR_KNOWLEDGE, fontName='Helvetica-Bold')),
            Paragraph(module['title'], ParagraphStyle(name='KMSubtitle', fontSize=16, alignment=TA_CENTER, textColor=COLOR_TEXT_HEADER, fontName='Helvetica-Bold', spaceAfter=20)),
            
            Paragraph(f"⏰ TIME INVESTMENT: 30-60 minutes before starting Week {week}", ParagraphStyle(name='Time', parent=self.styles['BoldSmall'], textColor=COLOR_ENERGY, spaceAfter=15)),
            
            Paragraph("📚 RECOMMENDED LEARNING RESOURCES:", self.styles['BoldSmall']),
            Spacer(1, 0.1 * inch),
        ]
        
        for resource in module['learning_resources']:
            flowables.append(Paragraph(f"• {resource}", self.styles['Bullet']))
        
        flowables.extend([
            Spacer(1, 0.2 * inch),
            Paragraph("🎯 KEY CONCEPTS TO MASTER:", self.styles['BoldSmall']),
            Spacer(1, 0.1 * inch),
        ])
        
        for concept in module['key_concepts']:
            flowables.append(Paragraph(f"• {concept}", self.styles['Bullet']))

        flowables.extend([
            Spacer(1, 0.2 * inch),
            Paragraph("✅ LEARNING COMPLETION CHECKLIST:", ParagraphStyle(parent=self.styles['BoldSmall'], textColor=COLOR_ACCENT)),
            Spacer(1, 0.1 * inch),
        ])
        
        checklist_items = [
            "☐ Watched/read at least 2 recommended resources",
            "☐ Can explain the key concepts in my own words",
            "☐ Identified how these concepts apply to my personal goals",
            "☐ Ready to practice these skills in real conversations"
        ]
        for item in checklist_items:
            flowables.append(Paragraph(item, self.styles['Bullet']))

        flowables.append(Spacer(1, 0.2 * inch))
        
        goal_section = self._create_section(
            "MY PERSONAL APPLICATION GOAL",
            [
                GOAL_TEMPLATES[week],
                "My goal:",
                "____________________________________________________________________",
                "____________________________________________________________________",
            ],
            COLOR_WISDOM
        )
        flowables.extend(goal_section)
        
        metric_section = self._create_section(
            "THIS WEEK'S SUCCESS METRIC",
            [WEEKLY_METRICS[week]],
            COLOR_PRIMARY
        )
        flowables.extend(metric_section)
        
        flowables.append(PageBreak())
        return flowables

    def _build_daily_page(self, week, day):
        """Builds the flowables for a daily challenge page."""
        self.current_page_info.update({'week': week, 'day': day})
        
        # Challenge Box (using a Table)
        challenge_text = PROGRESSIVE_CHALLENGES[week][day-1]
        challenge_title = Paragraph(f"🎯 DAY {day} PROGRESSIVE CHALLENGE", self.styles['SectionTitle'])
        challenge_desc = Paragraph(challenge_text, ParagraphStyle(parent=self.styles['BoldSmall'], textColor=black))
        metrics_text = Paragraph(
            "<b>SUCCESS METRICS:</b><br/>☐ Challenge completed (Yes/No) &nbsp;&nbsp;&nbsp; ☐ Comfort level: ___/10<br/>☐ Key learning: ________________________________",
            self.styles['Small']
        )
        
        challenge_table = Table([
            [challenge_title],
            [challenge_desc],
            [metrics_text]
        ], colWidths=[self.content_width - 12])
        
        challenge_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), COLOR_ACCENT),
            ('BACKGROUND', (0, 1), (0, 2), HexColor('#A0E6D9')),
            ('BOX', (0, 0), (-1, -1), 1.5, COLOR_ACCENT),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        
        # Sections
        execution_prompts = [
            "<b>PRE-CHALLENGE MINDSET:</b> How are you feeling before attempting this challenge?",
            "<b>EXECUTION DETAILS:</b> Describe exactly what happened when you tried the challenge:",
            "<b>COMFORT LEVEL:</b> Rate your comfort (1=terrifying, 10=completely natural): ___/10",
            "<b>SUCCESS METRICS:</b> Did you achieve the specific goal? ☐ Yes ☐ Partial ☐ No",
            "<b>WHAT WORKED:</b> What specific technique or approach was most helpful?",
            "<b>WHAT TO ADJUST:</b> What will you do differently in similar situations?"
        ]
        
        reflection_prompts = [
            "<b>BREAKTHROUGH MOMENT:</b> What surprised you most about today's social interaction?",
            "<b>SKILL DEVELOPMENT:</b> Which communication skill improved most today?",
            "<b>TOMORROW'S PREPARATION:</b> How will you build on today's progress tomorrow?"
        ]
        
        flowables = [
            challenge_table,
            Spacer(1, 0.2 * inch),
        ]
        flowables.extend(self._create_section("📊 EXECUTION & METRICS TRACKING", execution_prompts, COLOR_PRIMARY))
        flowables.extend(self._create_section("🧠 DAILY GROWTH REFLECTION", reflection_prompts, COLOR_WISDOM))
        flowables.append(PageBreak())
        return flowables

    def _build_weekly_review_page(self, week):
        """Builds the flowables for the weekly review page."""
        self.current_page_info = {} # Reset page info for non-daily pages

        metrics_prompts = [
            "<b>CHALLENGE COMPLETION RATE:</b> ___/7 days completed successfully",
            "<b>AVERAGE COMFORT LEVEL:</b> Day 1: ___ Day 7: ___ (Improvement: ___)",
            f"<b>SUCCESS METRIC ACHIEVEMENT:</b><br/><i>({WEEKLY_METRICS[week]})</i>",
            "<b>MOST MEASURABLE IMPROVEMENT:</b> What concrete change can you document?"
        ]
        insights_prompts = [
            "<b>BIGGEST BREAKTHROUGH:</b> What was your most significant 'aha' moment?",
            "<b>PATTERN RECOGNITION:</b> What patterns did you notice in your social behavior?",
            "<b>KNOWLEDGE APPLICATION:</b> How did the pre-week learning help your practice?",
            "<b>RELATIONSHIP IMPACT:</b> Which relationship improved most this week?"
        ]
        if week < 7:
            prep_prompts = [
                f"<b>WEEK {week+1} GOAL CUSTOMIZATION:</b> How will you personalize next week's challenges?",
                f"<b>KNOWLEDGE MODULE PLAN:</b> When will you complete Week {week+1}'s learning?",
                "<b>DIFFICULTY ADJUSTMENT:</b> Should next week be more/less challenging? Why?",
                "<b>ACCOUNTABILITY PLAN:</b> How will you ensure consistent practice next week?"
            ]
            prep_section = self._create_section(f"🎯 WEEK {week+1} PREPARATION", prep_prompts, COLOR_ENERGY)
        else:
            mastery_prompts = [
                "<b>TRANSFORMATION SUMMARY:</b> How have you changed since Week 1?",
                "<b>SKILL MASTERY LEVEL (1-10):</b><br/>Self-awareness: ___ Response control: ___ Listening: ___<br/>Clear communication: ___ Empathy: ___ Conflict resolution: ___<br/>Relationship building: ___",
                "<b>ONGOING PRACTICE PLAN:</b> How will you maintain and continue growing these skills?"
            ]
            prep_section = self._create_section("🏆 MASTERY ASSESSMENT", mastery_prompts, COLOR_ENERGY)
        
        flowables = [
            Paragraph(f"Week {week} Performance Review", ParagraphStyle(name='ReviewTitle', parent=self.styles['h1'], alignment=TA_CENTER, textColor=COLOR_PRIMARY, spaceAfter=20)),
        ]
        flowables.extend(self._create_section("📊 QUANTITATIVE RESULTS", metrics_prompts, COLOR_ACCENT))
        flowables.extend(self._create_section("💡 QUALITATIVE INSIGHTS", insights_prompts, COLOR_WISDOM))
        flowables.extend(prep_section)
        flowables.append(PageBreak())
        return flowables
    
    def _build_final_page(self):
        """Builds the flowables for the final assessment page."""
        self.current_page_info = {}
        flowables = [
            Spacer(1, 1.5 * inch),
            Paragraph("SOCIAL MASTERY", self.styles['Title']),
            Paragraph("ACHIEVED", self.styles['Title']),
            Spacer(1, 0.2 * inch),
            Paragraph("Transformation Complete", ParagraphStyle(name='FinalTagline', parent=self.styles['Subtitle'], textColor=COLOR_ACCENT)),
            Spacer(1, 0.4 * inch),
        ]
        
        final_prompts = [
            "<b>BEFORE vs. AFTER ASSESSMENT:</b><br/>Week 1 Comfort Level: ___/10 &nbsp;&nbsp;&nbsp; Week 7 Comfort Level: ___/10",
            "<b>Most Significant Transformation:</b>",
            "____________________________________________________________________",
            "<b>New Social Superpowers Acquired:</b><br/>1. ___________________<br/>2. ___________________<br/>3. ___________________",
            "<b>Career Impact:</b> How will these skills accelerate your AI/health-tech goals?",
            "____________________________________________________________________",
            "<b>Ongoing Practice Plan:</b> How will you maintain and expand these abilities?",
            "____________________________________________________________________",
        ]
        
        for prompt in final_prompts:
            flowables.append(Paragraph(prompt, ParagraphStyle(parent=self.styles['Normal'], alignment=TA_CENTER, spaceAfter=12)))
        
        flowables.extend([
            Spacer(1, 0.3 * inch),
            Paragraph("🎉 CONGRATULATIONS! 🎉", ParagraphStyle(parent=self.styles['h2'], alignment=TA_CENTER, textColor=COLOR_ENERGY)),
            Spacer(1, 0.1 * inch),
            Paragraph("You now possess the systematic communication skills to build any relationship and influence any outcome.", ParagraphStyle(parent=self.styles['Normal'], alignment=TA_CENTER)),
            Paragraph("Your AI/health-tech career will benefit immeasurably.", ParagraphStyle(parent=self.styles['Normal'], alignment=TA_CENTER)),
        ])
        
        return flowables

    def build(self):
        """Generate the complete PDF document."""
        # 1. Build Intro
        self.story.extend(self._build_intro_page())
        
        # 2. Build Weekly Content
        start_date = date.today()
        day_offset = 0
        for week in range(1, 8):
            # Knowledge Module Page
            self.story.extend(self._build_knowledge_page(week))
            
            # Daily Pages
            for day in range(1, 8):
                current_date = start_date + timedelta(days=day_offset)
                self.current_page_info['date_str'] = current_date.strftime('%A, %B %d, %Y')
                self.story.extend(self._build_daily_page(week, day))
                day_offset += 1
            
            # Weekly Review Page
            self.story.extend(self._build_weekly_review_page(week))
            
        # 3. Build Final Page
        self.story.extend(self._build_final_page())

        # 4. Create the PDF
        doc = SimpleDocTemplate(
            self.filename,
            pagesize=A4,
            leftMargin=self.margin,
            rightMargin=self.margin,
            topMargin=self.margin + 0.3*inch, # Make space for header
            bottomMargin=self.margin
        )
        
        # NOTE: Using a FrameAction to update page info before drawing the header
        # is a more advanced technique. For simplicity, we manually update a dict.
        # This works well for sequential page generation.
        doc.build(self.story, onFirstPage=self._header, onLaterPages=self._header)
        
        print(f"✅ Successfully created {self.filename}")
        print("🚀 Your systematic path from introvert to social mastery is ready!")
        print("💡 Key improvements implemented:")
        print("   ✅ PLATYPUS Framework: Robust, maintainable layout with automatic text wrapping.")
        print("   ✅ Object-Oriented Design: Encapsulated logic in a clean, reusable class.")
        print("   ✅ Centralized Styling: All styles are defined once for easy updates.")
        print("   ✅ Table-Based Layouts: Sections are built with Tables for pixel-perfect alignment.")

if __name__ == "__main__":
    # Suppress verbose font warnings from ReportLab if they occur
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
        
    journal = JournalGenerator()
    journal.build()