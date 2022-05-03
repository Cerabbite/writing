from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont

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

pdf = Canvas("test.pdf")
pdf.setTitle("Title")

RULER(pdf)

for font in pdf.getAvailableFonts():
    #print(font)
    pass

registerFont(
    TTFont('Comic-Mono', 'ComicMono.ttf')
)

pdf.setFont('Comic-Mono', 36)
pdf.drawCentredString(300, 770, text="Sample Title")
pdf.setFillColorRGB(0,0,255)
pdf.setFont('Courier-Bold', 24)
pdf.drawCentredString(300, 720, text="Sample sub-title")

pdf.line(0, 710, 600, 710)

pdf.save()
