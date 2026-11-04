import os
import sys
import html
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, 
    PageBreak, Flowable, KeepTogether, Preformatted, HRFlowable
)
from reportlab.pdfgen import canvas

from questions_basic import BASIC_QUESTIONS
from questions_medium import MEDIUM_QUESTIONS
from questions_advanced import ADVANCED_QUESTIONS

PAGE_WIDTH, PAGE_HEIGHT = A4  # 595.27 x 841.89 points
MARGIN = 36  # 0.5 inch margins
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN

class QuestionTracker(Flowable):
    """Logs question number and answer to the canvas for per-page footer answer printing."""
    def __init__(self, q_num, ans):
        super().__init__()
        self.q_num = q_num
        self.ans = ans
        self.width = 0
        self.height = 0

    def draw(self):
        cur_p = self.canv._pageNumber
        if not hasattr(self.canv, 'page_answers_map'):
            self.canv.page_answers_map = {}
        if cur_p not in self.canv.page_answers_map:
            self.canv.page_answers_map[cur_p] = []
        self.canv.page_answers_map[cur_p].append((self.q_num, self.ans))

class NumberedExamCanvas(canvas.Canvas):
    """Two-pass canvas that adds running headers, total pages, and per-page unobtrusive answer keys."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.page_answers_map = {}

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(total_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, total_pages):
        p_num = self._pageNumber
        self.saveState()

        # Cover page (Page 1) does not need headers or footers
        if p_num > 1:
            # Running Header
            self.setFont("Helvetica-Bold", 7.5)
            self.setFillColor(colors.HexColor("#1e293b"))
            self.drawString(MARGIN, PAGE_HEIGHT - 24, "Python Comprehensive MCQ & Code Snippet Master Bank")
            
            self.setFont("Helvetica", 7)
            self.setFillColor(colors.HexColor("#64748b"))
            self.drawString(MARGIN + 245, PAGE_HEIGHT - 24, "-  CDAC PGCP-AI Curriculum (Day 1 -> Day 11)")
            
            self.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 24, f"Page {p_num} of {total_pages}")
            
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(MARGIN, PAGE_HEIGHT - 28, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 28)

            # Running Footer - Answers for questions on THIS specific page
            ans_list = self.page_answers_map.get(p_num, [])
            if ans_list:
                ans_str = "   |   ".join([f"Q{q}: {a}" for q, a in ans_list])
                self.setStrokeColor(colors.HexColor("#e2e8f0"))
                self.setLineWidth(0.4)
                self.line(MARGIN, 24, PAGE_WIDTH - MARGIN, 24)
                
                # Small, unobtrusive muted font at bottom so eyes don't wander accidentally
                self.setFont("Helvetica-Bold", 5.5)
                self.setFillColor(colors.HexColor("#94a3b8"))
                self.drawString(MARGIN, 14, f"[ Page {p_num} Self-Check Key: ]")
                self.setFont("Helvetica", 5.5)
                self.setFillColor(colors.HexColor("#475569"))
                self.drawString(MARGIN + 85, 14, ans_str)
            else:
                # Footer for pages without questions (e.g. Master Answer Key or Explanations)
                self.setStrokeColor(colors.HexColor("#e2e8f0"))
                self.setLineWidth(0.4)
                self.line(MARGIN, 24, PAGE_WIDTH - MARGIN, 24)
                self.setFont("Helvetica", 6)
                self.setFillColor(colors.HexColor("#94a3b8"))
                self.drawCentredString(PAGE_WIDTH / 2.0, 14, "CDAC PGCP-AI Python Preparation Master Bank - End-of-Section Reference")

        self.restoreState()

def build_pdf():
    pdf_filename = r"d:\Engineering\CDAC_ALL_MODULES\Python\Python_300_MCQ_Master_Test_Bank.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=36,
        bottomMargin=36
    )

    base_styles = getSampleStyleSheet()

    # Custom typography styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=base_styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0f172a'),
        alignment=1, # Center
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=base_styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#3b82f6'),
        alignment=1,
        spaceAfter=15
    )

    desc_style = ParagraphStyle(
        'CoverDesc',
        parent=base_styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=13,
        textColor=colors.HexColor('#334155'),
        alignment=0,
        spaceAfter=8
    )

    section_banner_style = ParagraphStyle(
        'SectionBanner',
        parent=base_styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )

    section_sub_style = ParagraphStyle(
        'SectionSub',
        parent=base_styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12
    )

    q_num_style = ParagraphStyle(
        'QNum',
        parent=base_styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#0f172a')
    )

    q_topic_style = ParagraphStyle(
        'QTopic',
        parent=base_styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor('#2563eb')
    )

    opt_style = ParagraphStyle(
        'OptionText',
        parent=base_styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#1f2937')
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=base_styles['Normal'],
        fontName='Courier',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor('#0f172a')
    )

    exp_title_style = ParagraphStyle(
        'ExpTitle',
        parent=base_styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#0f172a')
    )

    exp_text_style = ParagraphStyle(
        'ExpText',
        parent=base_styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.5,
        textColor=colors.HexColor('#334155')
    )

    story = []

    # ==========================================
    # 1. COVER PAGE
    # ==========================================
    story.append(Spacer(1, 30))
    story.append(Paragraph("🐍 Python Comprehensive MCQ Test Bank", title_style))
    story.append(Paragraph("CDAC PGCP-AI - Master Certification & Assessment Preparation", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563eb'), spaceBefore=4, spaceAfter=20))

    # Overview Card Table
    card_data = [
        [
            Paragraph("<b>Target Audience:</b> CDAC PGCP-AI & Advanced Python Developers", desc_style),
            Paragraph("<b>Total Questions:</b> 300 Comprehensive MCQs & Code Snippets", desc_style)
        ],
        [
            Paragraph("<b>Syllabus Scope:</b> Complete Curriculum (Day 1 through Day 11)", desc_style),
            Paragraph("<b>Structure:</b> 100 Basic - 100 Medium - 100 Advanced", desc_style)
        ],
        [
            Paragraph("<b>Format:</b> Multiple Choice, Output Prediction, Edge Cases", desc_style),
            Paragraph("<b>Self-Testing Design:</b> Answers printed at bottom in small font", desc_style)
        ]
    ]
    card_table = Table(card_data, colWidths=[CONTENT_WIDTH * 0.5, CONTENT_WIDTH * 0.5])
    card_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(card_table)
    story.append(Spacer(1, 18))

    # Syllabus Breakdown Box
    syll_heading = Paragraph("<b>Curriculum Syllabus & Module Breakdown (Day 01 -> Day 11):</b>", ParagraphStyle(
        'SyllH', parent=base_styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=colors.HexColor('#1e293b'), spaceAfter=8
    ))
    story.append(syll_heading)

    syll_data = [
        [Paragraph("<b>Days</b>", desc_style), Paragraph("<b>Core Modules & Topics Covered</b>", desc_style), Paragraph("<b>Target Focus</b>", desc_style)],
        [Paragraph("Day 1 - 2", desc_style), Paragraph("Python Architecture, Bytecode/PVM, Syntax, Data Types, Operators (Floor Division, Modulo, Bitwise), Conditionals, Loops, Strings, Slicing, Methods & Formatting.", desc_style), Paragraph("Foundations & Core Syntax", desc_style)],
        [Paragraph("Day 3 - 4", desc_style), Paragraph("Lists & Tuples, Mutability vs Immutability, Comprehensions, Dictionaries, Hashability, Sets, Views, Shallow vs Deep Copy.", desc_style), Paragraph("Sequences & Data Structures", desc_style)],
        [Paragraph("Day 5", desc_style), Paragraph("Functions, *args/**kwargs, Positional/Keyword-Only, LEGB Scopes, Closures, Decorators, Lambdas, Built-ins (map/filter/reduce), Regular Expressions.", desc_style), Paragraph("Functional & Text Processing", desc_style)],
        [Paragraph("Day 6", desc_style), Paragraph("OOP Foundations, Encapsulation, Mangling, Properties, Inheritance, Diamond Problem, MRO (C3 Linearization), super(), Dunders, ABCs, Descriptors.", desc_style), Paragraph("Object-Oriented Design", desc_style)],
        [Paragraph("Day 7", desc_style), Paragraph("File I/O Streams, Seek/Tell Offsets, Context Managers, CSV DictReader, JSON Serialization, Pickle Security, SQLite Relational Database & Transactions.", desc_style), Paragraph("Data Persistence & Relational DB", desc_style)],
        [Paragraph("Day 8", desc_style), Paragraph("Iterator Protocol (__iter__/__next__), StopIteration, Generators (yield, yield from), .send() Coroutines, Memory Efficiency, Exception Hierarchy.", desc_style), Paragraph("Advanced Iteration & Generators", desc_style)],
        [Paragraph("Day 9 - 10", desc_style), Paragraph("Flask Web Basics, WSGI, Routing, Jinja2, REST API Architecture, HTTP Verbs, Idempotency, Status Codes (200, 201, 204, 404, 405), Web Scraping (BeautifulSoup).", desc_style), Paragraph("Web Services & Scraping", desc_style)],
        [Paragraph("Day 10 - 11", desc_style), Paragraph("NumPy ndarray, Slicing, Shapes, Broadcasting, Boolean Indexing. Pandas Series & DataFrames, .loc/.iloc, Groupby Aggregations, Missing Data, Matplotlib OO Charts.", desc_style), Paragraph("Data Analysis & Visualization", desc_style)]
    ]
    syll_table = Table(syll_data, colWidths=[CONTENT_WIDTH * 0.16, CONTENT_WIDTH * 0.60, CONTENT_WIDTH * 0.24])
    syll_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f1f5f9')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('PADDING', (0, 0), (-1, -1), 4.5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(syll_table)
    story.append(Spacer(1, 16))

    # Instructions Box
    instr_text = (
        "<b>Exam & Self-Assessment Instructions:</b><br/>"
        "- <b>Active Recall Mode:</b> The correct answers for each question are deliberately placed in a small, faint footer key at the very bottom of each page. Solve every question on paper first before checking.<br/>"
        "- <b>Difficulty Progression:</b> Questions 1-100 establish core fundamentals; Questions 101-200 evaluate code tracing and tricky Python mechanics; Questions 201-300 challenge advanced concepts, internals, and edge cases.<br/>"
        "- <b>End-of-Book Resources:</b> A unified 300-Question Master Answer Matrix and comprehensive Explanations are provided in the appendix."
    )
    instr_p = Paragraph(instr_text, desc_style)
    instr_table = Table([[instr_p]], colWidths=[CONTENT_WIDTH])
    instr_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#eff6ff')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#93c5fd')),
        ('PADDING', (0, 0), (-1, -1), 7),
    ]))
    story.append(instr_table)

    story.append(PageBreak())

    # ==========================================
    # HELPER: Render Question Block
    # ==========================================
    def render_question(q):
        elements = []
        qid = q['id']
        q_ans = q['answer']
        topic = q.get('topic', 'General Python')
        q_text = html.escape(q['question'])
        code = q.get('code')
        options = q['options']

        # Tracker flowable logs to canvas
        elements.append(QuestionTracker(qid, q_ans))

        # Header: Topic in small blue caps, Question Number and Text
        header_p = Paragraph(f"<font color='#2563eb'><b>[ {topic} ]</b></font><br/><b>Q{qid}.</b> {q_text}", q_num_style)
        elements.append(header_p)

        # Code snippet if present
        if code:
            elements.append(Spacer(1, 3))
            escaped_code = html.escape(code)
            code_p = Preformatted(escaped_code, code_style)
            code_table = Table([[code_p]], colWidths=[CONTENT_WIDTH - 12])
            code_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
                ('PADDING', (0, 0), (-1, -1), 4.5),
                ('LEFTPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            elements.append(code_table)

        # Options
        elements.append(Spacer(1, 3))
        opt_paragraphs = []
        for opt in options:
            esc_opt = html.escape(opt)
            opt_paragraphs.append([Paragraph(esc_opt, opt_style)])

        opt_table = Table(opt_paragraphs, colWidths=[CONTENT_WIDTH - 12])
        opt_table.setStyle(TableStyle([
            ('PADDING', (0, 0), (-1, -1), 1.2),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 1.2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1.2),
        ]))
        elements.append(opt_table)
        elements.append(Spacer(1, 7))

        # Wrap question in KeepTogether to prevent splitting mid-question across pages
        return KeepTogether(elements)

    # ==========================================
    # 2. SECTION 1: BASIC LEVEL (Q1 - Q100)
    # ==========================================
    sec1_banner = Table([
        [
            Paragraph("<b>SECTION 1: BASIC LEVEL (Questions 1 - 100)</b>", section_banner_style),
        ],
        [
            Paragraph("<i>Core Foundations: Python History, Syntax, Operators, Conditionals, Loops, Strings, Lists, Tuples, Dictionaries, Sets, Functions & Basic OOP</i>", section_sub_style)
        ]
    ], colWidths=[CONTENT_WIDTH])
    sec1_banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#ecfdf5')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#10b981')),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sec1_banner)
    story.append(Spacer(1, 10))

    for q in BASIC_QUESTIONS:
        story.append(render_question(q))

    story.append(PageBreak())

    # ==========================================
    # 3. SECTION 2: MEDIUM LEVEL (Q101 - Q200)
    # ==========================================
    sec2_banner = Table([
        [
            Paragraph("<b>SECTION 2: MEDIUM LEVEL (Questions 101 - 200)</b>", section_banner_style),
        ],
        [
            Paragraph("<i>Intermediate Mechanics: Tricky Slicing, Short-Circuit Logic, Comprehensions, Scopes, Closures, Decorators, Properties, File Streams, SQLite & REST APIs</i>", section_sub_style)
        ]
    ], colWidths=[CONTENT_WIDTH])
    sec2_banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#eff6ff')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#3b82f6')),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sec2_banner)
    story.append(Spacer(1, 10))

    for q in MEDIUM_QUESTIONS:
        story.append(render_question(q))

    story.append(PageBreak())

    # ==========================================
    # 4. SECTION 3: ADVANCED LEVEL (Q201 - Q300)
    # ==========================================
    sec3_banner = Table([
        [
            Paragraph("<b>SECTION 3: ADVANCED LEVEL (Questions 201 - 300)</b>", section_banner_style),
        ],
        [
            Paragraph("<i>Expert Concepts: Python Internals, Memory Optimization (__slots__), MRO (C3 Linearization), super(), Metaclasses, Generators (.send/yield from), NumPy Strides & Pandas Performance</i>", section_sub_style)
        ]
    ], colWidths=[CONTENT_WIDTH])
    sec3_banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f5f3ff')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#8b5cf6')),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(sec3_banner)
    story.append(Spacer(1, 10))

    for q in ADVANCED_QUESTIONS:
        story.append(render_question(q))

    story.append(PageBreak())

    # ==========================================
    # 5. APPENDIX: MASTER ANSWER MATRIX (Q1 - Q300)
    # ==========================================
    app_banner = Table([
        [
            Paragraph("<b>APPENDIX A: COMPLETE MASTER ANSWER KEY (Q1 - Q300)</b>", section_banner_style),
        ],
        [
            Paragraph("<i>Compact verification matrix across all 300 questions for quick evaluation and score tabulation.</i>", section_sub_style)
        ]
    ], colWidths=[CONTENT_WIDTH])
    app_banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#64748b')),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(app_banner)
    story.append(Spacer(1, 10))

    all_questions = BASIC_QUESTIONS + MEDIUM_QUESTIONS + ADVANCED_QUESTIONS

    # Build 10-column compact answer table (30 rows x 10 cols)
    cols = 10
    rows = 30
    grid_data = []
    
    # Table header
    header_row = [Paragraph(f"<b>Col {c+1}</b>", opt_style) for c in range(cols)]
    
    for r in range(rows):
        row_items = []
        for c in range(cols):
            idx = r + c * rows
            if idx < len(all_questions):
                q = all_questions[idx]
                row_items.append(Paragraph(f"<b>Q{q['id']}:</b> <font color='#2563eb'><b>{q['answer']}</b></font>", opt_style))
            else:
                row_items.append(Paragraph("", opt_style))
        grid_data.append(row_items)

    col_w = CONTENT_WIDTH / float(cols)
    matrix_table = Table(grid_data, colWidths=[col_w] * cols)
    matrix_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#ffffff')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#f1f5f9')),
        ('PADDING', (0, 0), (-1, -1), 3),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(matrix_table)
    story.append(Spacer(1, 15))

    # ==========================================
    # 6. APPENDIX B: DETAILED EXPLANATIONS REFERENCE
    # ==========================================
    story.append(PageBreak())
    exp_banner = Table([
        [
            Paragraph("<b>APPENDIX B: DETAILED EXPLANATIONS & KEY TAKEAWAYS</b>", section_banner_style),
        ],
        [
            Paragraph("<i>Comprehensive rationales, mechanics, and references for all 300 questions grouped sequentially.</i>", section_sub_style)
        ]
    ], colWidths=[CONTENT_WIDTH])
    exp_banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#0284c7')),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(exp_banner)
    story.append(Spacer(1, 10))

    # Explanations rendered in clean two-column format or structured cards
    for q in all_questions:
        qid = q['id']
        ans = q['answer']
        topic = q.get('topic', '')
        exp = html.escape(q.get('explanation', ''))
        
        exp_p = Paragraph(f"<b>Q{qid}. [{ans}]</b> <font color='#64748b'>({topic})</font> - {exp}", exp_text_style)
        story.append(exp_p)
        story.append(Spacer(1, 3.5))

    print("Building PDF document...")
    doc.build(story, canvasmaker=NumberedExamCanvas)
    print(f"PDF successfully generated at: {pdf_filename}")

if __name__ == "__main__":
    build_pdf()
