from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER, LEGAL, TABLOID
from reportlab.lib.pagesizes import A1, A2, A3, A4, A5, A6
import os

"""
Functions to add:
    - Auto table of content generator
    - Command to get all installed fonts on your system with their paths
    - Add images
    - Hav standard indentation for novel and screenplay

Possible solution to current problem: https://www.codegrepper.com/code-examples/whatever/reportlab+table+wrap+text
https://stackoverflow.com/questions/4899885/how-to-set-any-font-in-reportlab-canvas-in-python
https://stackoverflow.com/questions/3755851/python-reportlab-pdf-centering-text-on-page
"""

__VERSION__ = "1.0.0-Alpha"

filename = "test.md" #input(">>")

def Settings(file):
    pass

def Find_Chapters(file):
    chapters = []
    for x, i in enumerate(file):
        chapter = []
        if len(i) <= 0:
            continue
        if i[0] == "#":
            #print(i)
            if i[1] == " ":
                chapter.append(i[2:])
            else:
                chapter.append(i[1:])

            chapter.append(x)
            chapters.append(chapter)
    return chapters

def Get_Content(file, chapters):
    chapts = []
    for x,i in enumerate(chapters):
        chapt = []
        start_line = i[1] + 1
        if x + 1 <= len(chapters)-1:
            end_line = chapters[int(x+1)][1] + 1
        else:
            end_line = len(file)
        all_nums = range(start_line+1, end_line)
        all_nums = list(all_nums)
        content = ""
        for z in all_nums:
            content += f"{file[int(z-1)]}\n"
        print(start_line, end_line, all_nums)
        chapt.append(i[0])
        chapt.append(content)
        chapts.append(chapt)

    return chapts



def Create_PDF(settings, chapters):
    font = "Baskerville"
    font_size = 12
    font_location = f'C:\Windows\fonts\{font}.tff'

    pdf = Canvas("test-novel.pdf", pagesize=LETTER)
    pdf.setFont("Courier", font*5)
    pdf.drawString(1 * inch, LETTER, "Document Title")
    pdf.setFont("Courier", font*3)
    pdf.drawString(1 * inch, 10 * inch, "Document Title")
    #pdf.drawString(1 * inch, 9.5 * inch, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis vel eros donec ac odio tempor orci dapibus ultrices. Non nisi est sit amet facilisis magna etiam tempor orci. Turpis egestas pretium aenean pharetra magna ac placerat. Orci nulla pellentesque dignissim enim sit amet venenatis. Arcu felis bibendum ut tristique et egestas quis ipsum suspendisse. Mattis molestie a iaculis at erat pellentesque adipiscing commodo. Feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi. Nec nam aliquam sem et tortor consequat. Nec ultrices dui sapien eget mi proin. Morbi non arcu risus quis varius quam.<br />\nMassa eget egestas purus viverra. Urna molestie at elementum eu facilisis sed odio. Volutpat maecenas volutpat blandit aliquam etiam. Neque convallis a cras semper auctor neque. Aliquet lectus proin nibh nisl condimentum. Nec sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae. Nisl rhoncus mattis rhoncus urna neque. Diam vel quam elementum pulvinar etiam non quam. In hac habitasse platea dictumst quisque sagittis purus. Dolor morbi non arcu risus. Faucibus vitae aliquet nec ullamcorper sit amet risus nullam.")
    pdf.save()

def Commands(command):
    pass

def VERSION():
    # Check if new version is available
    return __VERSION__

file = open(filename)
file_read = file.readlines()
f_read = []
for i in file_read:
    f_read.append(i.split("\n")[0])

chapters = Find_Chapters(f_read)
chapters_and_content = Get_Content(f_read, chapters)
Create_PDF(None, chapters_and_content)
#print(chapters)
#print(chapters_and_content)
file.close()
