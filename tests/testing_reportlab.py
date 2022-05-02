from reportlab.pdfgen.canvas import Canvas

def RULER(pdf):
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')

pdf = Canvas("test.pdf")
pdf.setTitle("Title")

#pdf.drawString(0, 0, text="Title", mode=None, charSpace=0, direction=None, wordSpace=None)
RULER(pdf)

pdf.save()
