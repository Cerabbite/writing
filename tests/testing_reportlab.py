from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch, cm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont


class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        registerFont(TTFont('Courier-Prime', 'E:/GitHub/writing/font/Courier Prime.ttf'))
        page_number = self._pageNumber-1
        page = f"{page_number}." #"Page %s of %s" % (self._pageNumber, page_count)
        x = 1*inch
        if page_number >= 2:
            self.saveState()
            self.setStrokeColorRGB(0, 0, 0)
            self.setLineWidth(0.5)
            self.line(66, 78, LETTER[0] - 66, 78)
            self.setFont('Courier-Prime', 12)
            self.drawString(LETTER[0]-x, LETTER[1]-0.5*inch, page)
            self.restoreState()
        if page_number == 0:
            self.setFont('Courier-Prime', 12)
            #self.rotate(45)
            txt = "Test Script"
            txt2 = "screenplay by"
            txt3 = "Test Author"
            txt_width = stringWidth(txt, "Courier-Prime", 12)
            txt2_width = stringWidth(txt2, "Courier-Prime", 12)
            txt3_width = stringWidth(txt3, "Courier-Prime", 12)
            height_ = 7
            under_ = .05
            self.drawString((LETTER[0] - txt_width) / 2.0, height_*inch, txt)
            self.drawString((LETTER[0] - txt2_width) / 2.0, (height_-.7)*inch, txt2)
            self.drawString((LETTER[0] - txt3_width) / 2.0, (height_-1)*inch, txt3)
            self.setLineWidth(0.5)
            self.line((LETTER[0] - txt_width) / 2.0, (height_-under_)*inch, ((LETTER[0] - txt_width) / 2.0)+txt_width, (height_-under_)*inch)


if __name__ == '__main__':
    registerFont(TTFont('Courier-Prime', 'E:/GitHub/writing/font/Courier Prime.ttf'))

    # Content
    styles = getSampleStyleSheet()
    elements = []
    #elements.append(Paragraph("Title", style_underline))
    #elements.append(Paragraph("Page", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 1", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 2", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 3", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 4", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 5", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 6", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 7", styles["Normal"]))
    elements.append(PageBreak())
    elements.append(Paragraph("You are in page 8", styles["Normal"]))

    # Build
    doc = SimpleDocTemplate("my_file.pdf", pagesize=LETTER)
    doc.multiBuild(elements, canvasmaker=FooterCanvas)


"""
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm, mm, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
import os


#my_text = "Hello\nThis is a multiline text\nHere we do not have to handle the positioning of each line manually"
my_text = open("../test.md", 'r').read()

def Margins_Ruler():
    pass
"""

"""
c = canvas.Canvas("test.pdf")
textobject = c.beginText(2*cm, 29.7 * cm - 2 * cm)
for line in my_text.splitlines(False):
    textobject.textLine(line.rstrip())
c.drawText(textobject)
c.save()

"""
"""
# Make 2 styles (for now)
#   1. novel_style -> Will be selected when style:novel is
#   2. screenplay_style -> Will be selected when style:screenplay is

# Alignment:
#   0 = Left
#   1 = Middle
#   2 = Right

def Chapter_Title(title, story, style):
    title_style = styles['Heading1']
    title_style.alignment = 1
    title = Paragraph(title, title_style)
    story.append(title)
    return story

def Chapter_Content(content, story, style):
    paragraph = Paragraph(content.replace("\n", "<br />"), style)
    story.append(paragraph)
    return story

story = []
doc = SimpleDocTemplate("test.pdf",pagesize=A4,
                        rightMargin=2*cm,leftMargin=2*cm,
                        topMargin=2*cm,bottomMargin=2*cm, title="Test")

registerFont(TTFont("Baskerville","C:/Windows/Fonts/BASKVILL.TTF"))

styles = getSampleStyleSheet()
novelpar_style = ParagraphStyle('novel-paragraph',
                           fontName="Baskerville",
                           fontSize=12,
                           parent=styles['Normal'],
                           alignment=0,
                           spaceAfter=14)

screenplay_style = ParagraphStyle('novel-paragraph',
                           fontName="Courier",
                           fontSize=12,
                           parent=styles['Normal'],
                           alignment=1,
                           spaceAfter=14)

fonts = os.listdir(r'C:\Windows\fonts')

story = Chapter_Content(my_text, story, novelpar_style)

doc.build(story) #[Paragraph(my_text.replace("\n", "<br />"), getSampleStyleSheet()['Normal']),])
"""


"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
import random
import math

def RULER(pdf):
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10, 50, 'y50')
    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 150, 'y150')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 250, 'y250')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 350, 'y350')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 450, 'y450')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 550, 'y550')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 650, 'y650')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 750, 'y750')
    pdf.drawString(10, 800, 'y800')
    pdf.drawString(10, 850, 'y850')

pdf = Canvas("Test.pdf", pagesize=A4)
pdf.setFont("Courier", 12)
pdf.
"""
