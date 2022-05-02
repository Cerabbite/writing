from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm

document = []
document.append(Image('image.jpg', 2.2*inch, 2.2*inch))

def addTitle(doc):
    doc.append(Spacer(1, 20))
    doc.append(Paragraph('Sample Title', ParagraphStyle(name='Title',
                                                        fontFamily='Helvetica',
                                                        fontSize=36,
                                                        alignment=TA_CENTER)))
    doc.append(Spacer(1, 50))
    return document

SimpleDocTemplate('test.pdf', pagesize=letter,
                rightMargin=12, leftMargin=12,
                topMargin=12, bottomMargin=6).build(addTitle(document))
