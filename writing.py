from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER, LEGAL, TABLOID, ELEVENSEVENTEEN, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, C0, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
import pathlib
import os
import typer
import requests
import platform

__VERSION__ = "1.0.0-Beta"
__LICENSE__ = "MIT License"
__LICENSETEXT__ = r"""MIT License

Copyright (c) 2022 Kevin

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

class FooterCanvas(canvas.Canvas):

    def __init__(self, filename1, filename, settings, **kwargs):
        self.settings = settings
        canvas.Canvas.__init__(self, filename, **kwargs)
        self.pages = []
        #self.page_size = page_size
        #self.title = title
        #self.author = author

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
        registerFont(TTFont('Courier-Prime', 'font/Courier Prime.ttf'))
        page_number = self._pageNumber-1
        page = f"{page_number}." #"Page %s of %s" % (self._pageNumber, page_count)
        x = 1*inch
        page_size = self.settings[3]

        if page_number >= 2:
            self.saveState()
            self.setStrokeColorRGB(0, 0, 0)
            #self.setLineWidth(0.5)
            #self.line(66, 78, page_size[0] - 66, 78)
            self.setFont('Courier-Prime', 15)
            self.drawString(page_size[0]-x, page_size[1]-0.5*inch, page)
            self.drawString(x, page_size[1]-0.5*inch, self.settings[0])
            self.restoreState()
        if page_number == 0:
            self.setFont('Courier-Prime', 12)
            #self.rotate(45)
            txt = self.settings[0]
            txt2 = "screenplay by"
            txt3 = self.settings[1].split(',')
            txt_width = stringWidth(txt, "Courier-Prime", 12)
            txt2_width = stringWidth(txt2, "Courier-Prime", 12)
            #txt3_width = stringWidth(txt3, "Courier-Prime", 12)
            height_ = 7.5
            under_ = .05
            self.drawString((page_size[0] - txt_width) / 2.0, height_*inch, txt)
            self.drawString((page_size[0] - txt2_width) / 2.0, (height_-.7)*inch, txt2)
            n = 0
            for i in txt3:
                txt3_width = stringWidth(i, "Courier-Prime", 12)
                self.drawString((page_size[0] - txt3_width) / 2.0, (height_-(1+n))*inch, i)
                n += .2
            self.setLineWidth(0.5)
            self.line((page_size[0] - txt_width) / 2.0, (height_-under_)*inch, ((page_size[0] - txt_width) / 2.0)+txt_width, (height_-under_)*inch)

class WRITING:
    def settings(file, style):
        title = "Title"
        author = "Author"
        style = style
        paper_size = None
        font = None
        top_margin = 2
        bottom_margin = 2
        left_margin = 2
        right_margin = 2
        watermark = None
        genre = None

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
    def Content(file):
        #print(file_read)
        CONTENT = []
        setting_section = False
        wait = False

        for x in file:
            cont = str(x.split("\n")[0])
            cur_cont = []

            if len(cont) == 3:
                if cont[0] == "-" and cont[1] == "-" and cont[2] == "-":
                    if setting_section:
                        setting_section = False
                        wait = True
                    else:
                        setting_section = True
            if len(cont) > 1:
                if cont[0] == "/":
                    if cont[1] == "*":
                        continue
                elif cont[0] == "#":
                    if cont[1] == "#":
                        if cont[2] == " ":
                            cur_cont.append(cont[3:])
                        else:
                            cur_cont.append(cont[2:])

                        cur_cont.append('sub-header')
                        #print("SubHeader")
                    else:
                        if cont[1] == " ":
                            cur_cont.append(cont[2:])
                        else:
                            cur_cont.append(cont[1:])
                        cur_cont.append('header')
                        #print("Header")
                elif cont[0] == ">":
                    if cont[1] == ">":
                        if cont[2] == ">":
                            if cont[3] == " ":
                                cur_cont.append(cont[4:])
                            else:
                                cur_cont.append(cont[3:])

                            cur_cont.append('shot')
                        else:
                            if cont[2] == " ":
                                cur_cont.append(cont[3:])
                            else:
                                cur_cont.append(cont[2:])

                            cur_cont.append('fade')
                            #print("Action line")
                    else:
                        if cont[1] == " ":
                            cur_cont.append(cont[2:])
                        else:
                            cur_cont.append(cont[1:])
                        cur_cont.append('action-line')
                        #print("Fade")
                elif cont[0] == "<":
                    if cont[1] == "<":
                        if cont[2] == " ":
                            cur_cont.append(cont[3:])
                        else:
                            cur_cont.append(cont[2:])
                        cur_cont.append('parenthetical')
                        #print("Parenthetical")
                    else:
                        if cont[1] == " ":
                            cur_cont.append(cont[2:])
                        else:
                            cur_cont.append(cont[1:])
                        cur_cont.append('character')
                        #print("Character")
                else:
                    #cont[0] == "" and not cont[1] == " ":
                    #print(setting_section)
                    if not setting_section and not wait:
                        cur_cont.append(cont)
                        cur_cont.append('dialogue')
                        #print("Dialogue")
                    elif not setting_section and wait:
                        wait = False

                if len(cur_cont) == 2:
                    CONTENT.append(cur_cont)

        return CONTENT

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
    if read == False:
        if file_extension == ".nov":
            print("Use the 'writing novel input-file.nov output-file.pdf' for .nov files")
            return
        elif not file_extension == ".scr":
            print(f"Unkown file extension: {file_extension}")
            return

        file_read = open(input_file, "r").readlines()

        settings = WRITING.settings(file_read, "screenplay")
        content = SCREENPLAY.Content(file_read)

        file_extension_output = pathlib.Path(output_file).suffix

        if file_extension_output.lower() == ".pdf":
            styles = getSampleStyleSheet()

            page_size = WRITING.Get_PAGESIZE(settings[3])
            settings[3] = page_size

            story = []

            doc = SimpleDocTemplate(output_file,pagesize=page_size,
                                        rightMargin=settings[8]*inch,leftMargin=settings[7]*inch,
                                        topMargin=settings[5]*inch,bottomMargin=settings[6]*inch, title=f"{settings[0]} by {settings[1]}")

            registerFont(TTFont('Courier-Prime', 'font/Courier Prime.ttf'))

            screenplay_slugline_style = ParagraphStyle('screenplay-slugline-style',
                                                        fontName="Courier-Prime",
                                                        fontSize=12,
                                                        parent=styles['Normal'],
                                                        alignment=0,
                                                        spaceBefore=23,
                                                        spaceAfter=12)

            screenplay_subheaders_style = ParagraphStyle('screenplay-subheaders-style',
                                                        fontName="Courier-Prime",
                                                        fontSize=12,
                                                        parent=styles['Normal'],
                                                        alignment=0)

            screenplay_transition_style = ParagraphStyle('screenplay-transition-style',
                                                        fontName="Courier-Prime",
                                                        fontSize=12,
                                                        parent=styles['Normal'],
                                                        alignment=2,
                                                        spaceBefore=16,
                                                        spaceAfter=14)
                                                        #,
                                                        #leftIndent=4.5*inch)

            screenplay_shot_style = ParagraphStyle('screenplay-shot-style',
                                                        fontName="Courier-Prime",
                                                        fontSize=12,
                                                        parent=styles['Normal'],
                                                        alignment=0,
                                                        spaceBefore=16,
                                                        spaceAfter=14)
                                                        #,
                                                        #leftIndent=4.5*inch)

            screenplay_actionline_style = ParagraphStyle('screenplay-actionline-style',
                                                        fontName="Courier-Prime",
                                                        fontSize=12,
                                                        parent=styles['Normal'],
                                                        alignment=0)

            screenplay_character_style = ParagraphStyle('screenplay-character-style',
                                                        fontName="Courier-Prime",
                                                        fontSize=12,
                                                        parent=styles['Normal'],
                                                        alignment=0,
                                                        spaceBefore=15,
                                                        leftIndent=2*inch)

            screenplay_parenthetical_style = ParagraphStyle('screenplay-parenthetical-style',
                                                        fontName="Courier-Prime",
                                                        fontSize=12,
                                                        parent=styles['Normal'],
                                                        alignment=0,
                                                        leftIndent=1.5*inch)

            screenplay_dialogue_style = ParagraphStyle('screenplay-dialogue-style',
                                                        fontName="Courier-Prime",
                                                        fontSize=12,
                                                        parent=styles['Normal'],
                                                        alignment=0,
                                                        spaceAfter=15,
                                                        leftIndent=1*inch,
                                                        rightIndent=1*inch)

            story.append(PageBreak())
            for x in content:
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
                    story.append(Paragraph(x[0], screenplay_dialogue_style))

            # Build the PDF
            doc.multiBuild(story, canvasmaker=lambda filename1=output_file, filename=output_file, settings=settings, **kwargs:FooterCanvas(filename1, filename, settings, **kwargs))
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

        page_size = WRITING.Get_PAGESIZE(settings[3])
        settings[3] = page_size

        if countwords:
            print("Word count is NOT accurate yet.")
            word_ammount = 0
            for i in chapts:
                variable = str(i[1].split(' '))
                word_ammount += len(variable)
                print(word_ammount)

            print(word_ammount)

        if settings[2] == "novel-centered":
            print("Everything will be centered")
        elif settings[2] == "novel-right":
            print('Everything will be aligneed right')

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

if __name__ == "__main__":
    app()
