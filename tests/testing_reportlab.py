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

"""
c = canvas.Canvas("test.pdf")
textobject = c.beginText(2*cm, 29.7 * cm - 2 * cm)
for line in my_text.splitlines(False):
    textobject.textLine(line.rstrip())
c.drawText(textobject)
c.save()

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
    paragraph_style = styles['Normal']
    paragraph_style.alignment = 0
    paragraph = Paragraph(content.replace("\n", "<br />"), paragraph_style)
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
paragraph_style = styles['Normal']
paragraph_style.alignment = 0
paragraph = Paragraph(my_text.replace("\n", "<br />"), my_style)
story.append(paragraph)

doc.build(story) #[Paragraph(my_text.replace("\n", "<br />"), getSampleStyleSheet()['Normal']),])


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
