#Copyright (c) 2022 Cerabbite
# For speed and exporting the project change to Rust
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER, LEGAL, TABLOID, ELEVENSEVENTEEN, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.colors import lightgrey, grey
from reportlab.pdfgen import canvas
from jouvence.parser import JouvenceParser
from jouvence.html import HtmlDocumentRenderer
import pathlib
import os
import typer
import requests
import platform
import datetime

__VERSION__ = "1.0.0-Beta"
__LICENSE__ = "MIT License"
__LICENSETEXT__ = r"""MIT License

Copyright (c) 2022 Cerabbite

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

"""
Possible: A single empty line means a new line and double empty line means new paragraph
"""

# Screenplay styling: https://www.nfi.edu/screenplay-format/
#                     https://www.youtube.com/watch?v=Zx6W3fz9tnA
#                     https://online.pointpark.edu/screenwriting/screenplay-format/
# Screenplay example: http://www.dailyscript.com/scripts/inside-out-screenplay.pdf
# Need to start writing different functions for screenplay and novel styling
# To accomplish the different margins https://groups.google.com/g/reportlab-users/c/I1oOOTIARGw
# Could possibly help with page numbers https://stackoverflow.com/questions/67702808/add-header-and-footer-to-a-page-using-reportlab

app = typer.Typer()

class WRITING:
    def settings(file, style):
        title = "Title"
        author = "Author"
        style = style
        paper_size = None
        font = None
        top_margin = 1
        bottom_margin = 1
        left_margin = 1
        right_margin = 1
        watermark = None
        genre = None
        copyright = None

        start_settings = False
        for i in file:
            i_set = str(i.split("\n")[0])
            if start_settings == True:
                setting = i_set.split(":")
                if setting[0] == "title":
                    if setting[1][0] == " ":
                        setting[1] = setting[1][1:]
                    title = setting[1]
                elif setting[0] == "author":
                    if setting[1][0] == " ":
                        setting[1] = setting[1][1:]
                    author = setting[1]
                elif setting[0] == "style":
                    style = setting[1].replace(" ", "")
                elif setting[0] == "paper-size" or setting[0] == "page-size":
                    paper_size = setting[1].replace(" ", "")
                elif setting[0] == "font":
                    font = setting[1].replace(" ", "")
                elif setting[0] == "top-margin":
                    top_margin = float(setting[1].replace(" ", ""))
                elif setting[0] == "bottom-margin":
                    bottom_margin = float(setting[1].replace(" ", ""))
                elif setting[0] == "left-margin":
                    left_margin = float(setting[1].replace(" ", ""))
                elif setting[0] == "right-margin":
                    right_margin = float(setting[1].replace(" ", ""))
                elif setting[0] == "watermark":
                    watermark = setting[1].replace(" ", "")
                elif setting[0] == "genre":
                    genre = setting[1].replace(" ", "")
                elif setting[0] == "copyright":
                    currentDateTime = datetime.datetime.now()
                    date = currentDateTime.date()
                    year = date.strftime("%Y")
                    copyright = f'Copyright (c) {year} {setting[1].replace(" ", "")}'
                    print(copyright)
            if i_set == "---" and start_settings == False:
                start_settings = True
            elif i_set == "---" and start_settings == True:
                break

        if style == "screenplay":
            if not top_margin == 2 or not bottom_margin == 2 or not left_margin == 2 or not right_margin == 2:
                print("Margin settings ignored, style set to screenplay")

            top_margin = 1
            bottom_margin = .75
            left_margin = 1.5
            right_margin = 1

        settings = [title, author, style, paper_size, font, top_margin, bottom_margin, left_margin, right_margin, watermark, genre]

        return settings

    def Get_PAGESIZE(page_size):
        if not page_size:
            return A4
        elif page_size == "A0":
            return A0
        elif page_size == "A1":
            return A1
        elif page_size == "A2":
            return A2
        elif page_size == "A3":
            return A3
        elif page_size == "A4":
            return A4
        elif page_size == "A5":
            return A5
        elif page_size == "A6":
            return A6
        elif page_size == "A7":
            return A7
        elif page_size == "A8":
            return A8
        elif page_size == "A9":
            return A9
        elif page_size == "A10":
            return A10
        elif page_size == "B0":
            return B0
        elif page_size == "B1":
            return B1
        elif page_size == "B2":
            return B2
        elif page_size == "B3":
            return B3
        elif page_size == "B4":
            return B4
        elif page_size == "B5":
            return B5
        elif page_size == "B6":
            return B6
        elif page_size == "B7":
            return B7
        elif page_size == "B8":
            return B8
        elif page_size == "B9":
            return B9
        elif page_size == "B10":
            return B10
        elif page_size == "C0":
            return C0
        elif page_size == "C0":
            return C1
        elif page_size == "C0":
            return C2
        elif page_size == "C0":
            return C3
        elif page_size == "C0":
            return C4
        elif page_size == "C0":
            return C5
        elif page_size == "C0":
            return C6
        elif page_size == "C0":
            return C7
        elif page_size == "C0":
            return C8
        elif page_size == "C0":
            return C9
        elif page_size == "C0":
            return C10
        elif page_size == "LETTER":
            return LETTER
        elif page_size == "LEGAL":
            return LEGAL
        elif page_size == "TABLOID":
            return TABLOID
        elif page_size == "ELEVENSEVENTEEN":
            return ELEVENSEVENTEEN
        else:
            print(f"Unkown page size '{page_size}'.")
            print("Paper size is set to A4.")
            return A4

class SCREENPLAY:
    def Content(input_file):
        #https://nerdymovie.blogspot.com/2014/03/parsing-fountain-files.html
        def scene_list(input_ftn_file, line_numbers = False):
            """

            INPUT:
               input_ftn_file could be "/path/my-script.fountain"

            OUTPUT:
               list of scenes occurring in script

            """
            print(input_ftn_file)
            f = open(input_ftn_file)
            lines = f.readlines()
            scene_lst = []
            for j in range(len(lines)):
                x = lines[j]
                if x[:3].upper() == "INT" or x[:3].upper() == "EXT":
                    if line_numbers == True:
                        scene_lst.append([j,x[:-1]])
                    else:
                        scene_lst.append(x[:-1])
            f.close()
            return scene_lst

        def character_list(input_ftn_file):
            """

            INPUT:
               input_ftn_file could be "/home/wdj/my-script.fountain"

            OUTPUT:
               list of characters with speaking parts occurring in script

            """
            f = open(input_ftn_file,'r')
            lines = f.readlines()
            char_list = []
            N = len(lines)
            for j in range(1,N-1):
                x = lines[j]
                if lines[j-1] == "\n" and lines[j+1] != "\n" and x.isupper():
                    char = x[:-1]
                    if "(" in char and ")" in char:
                        i1 = char.index("(")
                        i2 = char.index(")")
                        char = char[:i1]
                    if char[-1] == " ":
                        char = char[:-1]
                    if "\xc2\xa0" in char:
                        char = char.replace("\xc2\xa0","")
                    if "\xc2" in char:
                        char = char.replace("\xc2","")
                    if "\xa0" in char:
                        char = char.replace("\xa0","")
                    if not(char in char_list):
                        char_list.append(char)
            f.close()
            return char_list

        print(len(scene_list(input_file, line_numbers=True)))
        print(len(character_list(input_file)))

class NOVEL:
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
        for x,i in enumerate(list(chapters)):
            chapt = []
            start_line = i[1] + 1
            if x + 1 <= len(chapters)-1:
                end_line = chapters[int(x+1)][1] + 1
            else:
                end_line = len(file)+1
            all_nums = range(start_line+1, end_line)
            all_nums = list(all_nums)
            content = ""
            for z in all_nums:
                content += f"{file[int(z-1)]}\n"
            #print(start_line, end_line, all_nums)
            chapt.append(i[0])
            chapt.append(content)
            chapts.append(chapt)

        return chapts

@app.command()
def screenplay(input_file: str, output_file: str, read: bool=False):
    # Screenplay extension: .scr
    # Read and write FDXs
    file_extension = pathlib.Path(input_file).suffix
    #print("File Extension: ", file_extension)
    #print(input_file)
    SCREENPLAY.Content(input_file)
    if read == False:
        if file_extension == ".nov":
            print("Use the 'writing novel input-file.nov output-file.pdf' for .nov files")
            return
        elif not file_extension == ".fountain":
            print(f"Unkown file extension: {file_extension}")
            return

        file_read = open(input_file, "r").readlines()

        settings = WRITING.settings(file_read, "screenplay")
        #content = SCREENPLAY.Content(file_read)

        file_extension_output = pathlib.Path(output_file).suffix

        if file_extension_output.lower() == ".pdf":
            styles = getSampleStyleSheet()

            page_size = WRITING.Get_PAGESIZE(settings[3])
            settings[3] = page_size

            story = []


        elif file_extension_output.lower() == ".fdx":
            file = open(output_file, 'w')

            file.write(r"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<FinalDraft Version="2" DocumentType="Script" Template="No">
    <Content>""")

            file.write("\n")

            characters = []

            for x in content:
                if x[1] == "header":
                    #story.append(Paragraph(x[0].upper(), screenplay_slugline_style))
                    file.write('        <Paragraph Type="Scene Heading">\n')
                    file.write(f'            <Text Font="Courier Final Draft">{x[0].upper()}</Text>\n')
                    file.write('        </Paragraph>\n')
                elif x[1] == "sub-header":
                    #story.append(Paragraph(x[0].upper(), screenplay_subheaders_style))
                    pass
                elif x[1] == "action-line":
                    #story.append(Paragraph(x[0], screenplay_actionline_style))
                    file.write('        <Paragraph Type="Action">\n')
                    file.write(f'            <Text Font="Courier Final Draft">{x[0].upper()}</Text>\n')
                    file.write('        </Paragraph>\n')
                elif x[1] == "fade":
                    #story.append(Paragraph(x[0].upper(), screenplay_transition_style))
                    file.write('        <Paragraph Type="Transition">\n')
                    file.write(f'            <Text Font="Courier Final Draft">{x[0].upper()}</Text>\n')
                    file.write('        </Paragraph>\n')
                elif x[1] == "shot":
                    file.write('        <Paragraph Type="Shot">\n')
                    file.write(f'            <Text Font="Courier Final Draft">{x[0].upper()}</Text>\n')
                    file.write('        </Paragraph>\n')
                elif x[1] == "character":
                    #story.append(Paragraph(x[0].upper(), screenplay_character_style))
                    characters.append(x[0].upper().split("(")[0])
                    file.write('        <Paragraph Type="Character">\n')
                    file.write(f'            <Text Font="Courier Final Draft">{x[0].upper()}</Text>\n')
                    file.write('        </Paragraph>\n')
                elif x[1] == "parenthetical":
                    #story.append(Paragraph(f"({x[0]})", screenplay_parenthetical_style))
                    file.write('        <Paragraph Type="Parenthetical">\n')
                    file.write(f'            <Text Font="Courier Final Draft">({x[0].upper()})</Text>\n')
                    file.write('        </Paragraph>\n')
                elif x[1] == "dialogue":
                    #story.append(Paragraph(x[0], screenplay_dialogue_style))
                    file.write('        <Paragraph Type="Dialogue">\n')
                    file.write(f'            <Text Font="Courier Final Draft">{x[0].upper()}</Text>\n')
                    file.write('        </Paragraph>\n')

            file.write("    </Content>\n")
            if settings[9]:
                file.write(f'    <Watermarking Text="{settings[9]}"/>\n')

            file.write(f'    <SmartType>\n')
            file.write(f'        <Characters>\n')
            for i in characters:
                file.write(f'            <Character>"{i}"</Character>\n')
            file.write(f'        </Characters>\n')
            file.write(r"""        <TimesOfDay Separator=" - ">
            <TimeOfDay></TimeOfDay>
            <TimeOfDay>AFTERNOON</TimeOfDay>
            <TimeOfDay>CONTINUOUS</TimeOfDay>
            <TimeOfDay>DAWN</TimeOfDay>
            <TimeOfDay>DAY</TimeOfDay>
            <TimeOfDay>DUSK</TimeOfDay>
            <TimeOfDay>EARLIER</TimeOfDay>
            <TimeOfDay>EARLY MORNING</TimeOfDay>
            <TimeOfDay>EVENING</TimeOfDay>
            <TimeOfDay>EVENING 66</TimeOfDay>
            <TimeOfDay>LATE AFTERNOON</TimeOfDay>
            <TimeOfDay>LATE NIGHT</TimeOfDay>
            <TimeOfDay>LATER</TimeOfDay>
            <TimeOfDay>MAGIC HOUR</TimeOfDay>
            <TimeOfDay>MOMENTS EARLIER</TimeOfDay>
            <TimeOfDay>MOMENTS LATER</TimeOfDay>
            <TimeOfDay>MORNING</TimeOfDay>
            <TimeOfDay>NEXT AFTERNOON</TimeOfDay>
            <TimeOfDay>NIGHT</TimeOfDay>
            <TimeOfDay>SECONDS LATER</TimeOfDay>
            <TimeOfDay>THE NEXT DAY</TimeOfDay>
            <TimeOfDay>THE PREVIOUS DAY</TimeOfDay>
        </TimesOfDay>""")
            file.write('\n')
            file.write(r"""        <SceneIntros Separator=". ">
            <SceneIntro>EXT</SceneIntro>
            <SceneIntro>I/E</SceneIntro>
            <SceneIntro>INT</SceneIntro>
        </SceneIntros>""")
            file.write('\n')
            file.write(f'    </SmartType>\n')
            file.write('</FinalDraft>')
            file.close()
        elif file_extension_output.lower() == ".html":
            pass
        elif file_extension_output.lower() == ".trelby":
            pass
        else:
            print(f"Cannot export to '{file_extension_output}'")

    elif read == True:
        pass
    else:
         print(f"Unkown read type: {read}")

@app.command()
def novel(input_file: str, output_file: str, read: bool=False, countwords: bool=False):
    # Novel extension: .nov
    file_extension = pathlib.Path(input_file).suffix.lower()
    if read == False:
        if file_extension == ".scr":
            print("Use the 'writing screenplay input-file.scr output-file.pdf' for .scr files")
            return
        elif not file_extension == ".nov":
            print(f"Unkown file extension: {file_extension}")
            return

        file = open(input_file)
        file_read = file.readlines()
        f_read = []
        for i in file_read:
            f_read.append(i.split("\n")[0])

        settings = WRITING.settings(f_read, "novel")
        chapters = NOVEL.Find_Chapters(f_read)
        chapts = NOVEL.Get_Content(f_read, chapters)

        print(settings)

        if countwords or settings[2] == "manuscript":
            print("Word count is NOT accurate yet.")
            word_ammount = 0
            for i in chapts:
                variable = list(i[1].split(' '))
                word_ammount += len(variable)
                #print(word_ammount)

            print(word_ammount)


        aligment = 0

        if settings[2] == "novel-centered":
            #print("Everything will be centered")
            aligment = 1
        elif settings[2] == "novel-right":
            #print('Everything will be aligneed right')
            aligment = 2
        elif settings[2] == "manuscript":
            print("Manuscript style")

        file_extension_output = pathlib.Path(output_file).suffix

        if file_extension_output == ".pdf":
            styles = getSampleStyleSheet()

            page_size = WRITING.Get_PAGESIZE(settings[3])
            settings[3] = page_size

            story = []

            doc = SimpleDocTemplate(output_file,pagesize=page_size,
                                        rightMargin=settings[8]*inch,leftMargin=settings[7]*inch,
                                        topMargin=settings[5]*inch,bottomMargin=settings[6]*inch, title=f"{settings[0]} by {settings[1]}")

            registerFont(TTFont("Baskerville","C:/Windows/Fonts/BASKVILL.TTF"))

            novelchap_style = ParagraphStyle('novel-chapter',
                                            fontName="Baskerville",
                                            fontSize=24,
                                            parent=styles['Heading2'],
                                            alignment=aligment,
                                            spaceAfter=14)

            novelpar_style = ParagraphStyle('novel-paragraph',
                                            fontName="Baskerville",
                                            fontSize=12,
                                            parent=styles['Normal'],
                                            alignment=aligment,
                                            spaceAfter=14)

            novelcontact_style = ParagraphStyle('novel-contact',
                                            fontName="Baskerville",
                                            fontSize=12,
                                            parent=styles['Normal'],
                                            alignment=0)

            novelwordcount_style = ParagraphStyle('novel-wordcount',
                                            fontName="Baskerville",
                                            fontSize=12,
                                            parent=styles['Normal'],
                                            alignment=2)

            if settings[2] == "manuscript":
                tbl_data = [
                    [Paragraph(f"{settings[1]}", novelcontact_style), Paragraph(f"Approx. {word_ammount} words", novelwordcount_style)],
                    [Paragraph(f"street", novelcontact_style), Paragraph(f"{settings[10]}", novelwordcount_style)],
                    [Paragraph(f"Address", novelcontact_style)],
                    [Paragraph(f"Phone number", novelcontact_style)],
                    [Paragraph(f"E-mail", novelcontact_style)]
                ]

                tbl = Table(tbl_data)

                story.append(tbl)

                story.append(PageBreak())
            """for x in content:
                if x[1] == "header":
                    story.append(Paragraph(x[0].upper(), screenplay_slugline_style))
                elif x[1] == "sub-header":
                    story.append(Paragraph(x[0].upper(), screenplay_subheaders_style))
                elif x[1] == "action-line":
                    story.append(Paragraph(x[0], screenplay_actionline_style))
                elif x[1] == "fade":
                    story.append(Paragraph(x[0].upper(), screenplay_transition_style))
                elif x[1] == "shot":
                    story.append(Paragraph(x[0].upper(), screenplay_shot_style))
                elif x[1] == "character":
                    story.append(Paragraph(x[0].upper(), screenplay_character_style))
                elif x[1] == "parenthetical":
                    story.append(Paragraph(f"({x[0]})", screenplay_parenthetical_style))
                elif x[1] == "dialogue":
                    story.append(Paragraph(x[0], screenplay_dialogue_style))"""

            # Build the PDF
            doc.build(story)
            #doc.multiBuild(story, canvasmaker=lambda filename1=output_file, filename=output_file, settings=settings, **kwargs:FooterCanvas(filename1, filename, settings, **kwargs))

    elif file_extension == ".scr":
        print("")

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
    print(f"writing v{__VERSION__}")
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
        else:
            print("No update available")
    return

@app.command()
def UPDATE():
    print("You are currently unable to download the latest version via you command line go to 'https://github.com/Cerabbite/writing/releases' to download the latest version.")
    # refer to VERSION() to check if update is available

@app.command()
def INFO():
    print("writing is licensed under the MIT License")
    print("Copyright (c) 2022 Kevin")
    print("For more information visit https://github.com/Cerabbite/writing/blob/main/LICENSE")
    #print(f"Your system: {platform.system()}")
    print()
    VERSION(True)
    #print()
    #print(__LICENSETEXT__)
    #with open("LICENSE_TEXT.txt") as txt:
    #    txt_read = txt.read()
    #    print(txt_read)

@app.command()
def LICENSE():
    print(__LICENSETEXT__)

if __name__ == "__main__":
    app()
