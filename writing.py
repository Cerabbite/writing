from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER, LEGAL, TABLOID
from reportlab.lib.pagesizes import A1, A2, A3, A4, A5, A6
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
import os
import typer
import requests
import platform

__VERSION__ = "1.0.0-Alpha"
__LICENSE__ = "MIT License"

"""
A single empty line means a new line and double empty line means new paragraph
"""

app = typer.Typer()

@app.command()
def WRITING(input_file: str, output_file: str):
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

    def Create_PDF(settings, chapters, output_file):
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
        doc = SimpleDocTemplate(output_file,pagesize=A4,
                                rightMargin=2*cm,leftMargin=2*cm,
                                topMargin=2*cm,bottomMargin=2*cm, title="Test")

        registerFont(TTFont("Baskerville","C:/Windows/Fonts/BASKVILL.TTF"))

        styles = getSampleStyleSheet()

        novelchap_style = ParagraphStyle('novel-chapter',
                                   fontName="Baskerville",
                                   fontSize=24,
                                   parent=styles['Heading2'],
                                   alignment=0,
                                   spaceAfter=14)

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

        print(chapters)
        #story = Chapter_Content(my_text, story, novelpar_style)

        #doc.build(story)


    def Commands(command):
        pass

    file = open(input_file)
    file_read = file.readlines()
    f_read = []
    for i in file_read:
        f_read.append(i.split("\n")[0])

    chapters = Find_Chapters(f_read)
    chapters_and_content = Get_Content(f_read, chapters)
    Create_PDF(None, chapters_and_content, output_file)
    print(chapters)
    print(chapters_and_content)
    file.close()

def LIST_OF_VERSION(version):
    release = version
    release_list = release.split(".")
    try:
        thing = release_list[2].split("-")[0]
        #print(1)
        thing2 = release_list[2].split("-")[1]
        #print(2)
        release_list[2] = thing
        #print(3)
        release_list.append(thing2)
        #print(4)
    except Exception as e:
        #print(e)
        pass
    #print(release_list)
    release = []
    for i in release_list:
        release.append(i.split('\n')[0])
    #print(release)
    return release

def NEW_VERSION(version):
    print(f"New version available v{version}")
    print(f"Do you want to download v{version}?")
    inp = input("[Y/N] ")
    if inp.lower() == "y":
        UPDATE()
        # Download the new version
        pass

@app.command()
def VERSION(check: bool=False):
    print(f"Your current version is v{__VERSION__}")
    if check:
        url = 'https://raw.githubusercontent.com/Cerabbite/writing/main/LATEST_VERSION'
        page = requests.get(url)
        v = page.text.split("\n")[0]
        latest_version = LIST_OF_VERSION(v)
        current_version = LIST_OF_VERSION(__VERSION__)
        #print(len(latest_version))
        #print(len(current_version))
        if latest_version[0] > current_version[0]:
            NEW_VERSION(v)
        elif latest_version[1] > current_version[1]:
            NEW_VERSION(v)
        elif latest_version[2] > current_version[2]:
            NEW_VERSION(v)
        elif len(latest_version) < len(current_version) and latest_version[0] == current_version[0] and latest_version[1] == current_version[1] and latest_version[2] == current_version[2]:
            NEW_VERSION(v)
        elif len(latest_version) == 4 and len(current_version) == 4:
            #print(latest_version[0], current_version[0], latest_version[1], current_version[1], latest_version[2], current_version[2])
            if latest_version[3] == 'Beta' and current_version[3] == 'Alpha':
                NEW_VERSION(v)
        else:
            print("No update available")

@app.command()
def UPDATE():
    print("You are currently unable to download the latest version via you command line go to 'https://github.com/Cerabbite/writing/releases' to download the latest version.")
    # refer to VERSION() to check if update is available

@app.command()
def INFO():
    print(platform.system())
    print(__VERSION__)
    print()
    with open("LICENSE_TEXT.txt") as txt:
        txt_read = txt.read()
        print(txt_read)

if __name__ == "__main__":
    app()
