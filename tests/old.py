@app.command()
def WRITING_OLD(input_file: str, output_file: str):
    def Settings(file):
        title = "Title"
        author = "Author"
        style = ""
        paper_size = None
        font = None
        top_margin = 2
        bottom_margin = 2
        left_margin = 2
        right_margin = 2

        start_settings = False
        for i in file:
            if start_settings == True:
                setting = i.split(":")
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
            if i == "---" and start_settings == False:
                start_settings = True
            elif i == "---" and start_settings == True:
                break

        if style == "screenplay":
            if not top_margin == 2 or not bottom_margin == 2 or not left_margin == 2 or not right_margin == 2:
                print("Margin settings ignored, style set to screenplay")

            top_margin = 1
            bottom_margin = .75
            left_margin = 1.5
            right_margin = 1

        settings = [title, author, style, paper_size, font, top_margin, bottom_margin, left_margin, right_margin]

        return settings

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

        def Page_Break(story):
            story.append(PageBreak())
            return story

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

        page_size = Get_PAGESIZE(settings[3])
        settings[3] = page_size

        story = []

        if settings[2] == "screenplay":
            doc = SimpleDocTemplate(output_file,pagesize=page_size,
                                    rightMargin=settings[8]*inch,leftMargin=settings[7]*inch,
                                    topMargin=settings[5]*inch,bottomMargin=settings[6]*inch, title=f"{settings[0]} by {settings[1]}")
        else:
            doc = SimpleDocTemplate(output_file,pagesize=page_size,
                                    rightMargin=settings[8]*cm,leftMargin=settings[7]*cm,
                                    topMargin=settings[5]*cm,bottomMargin=settings[6]*cm, title=f"{settings[0]} by {settings[1]}")

        registerFont(TTFont("Baskerville","C:/Windows/Fonts/BASKVILL.TTF"))
        registerFont(TTFont('Courier-Prime', 'font/Courier Prime.ttf'))

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
                                                    alignment=0,
                                                    spaceBefore=16,
                                                    spaceAfter=14)#,
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

        # Add screen play title and page number style insead of the header/footer class.
        #   Change top margin to .5 inch and put the number x inches from the left and add white space for the slugline/transition
        #   Option to have transition both on the left and right side and for the right side just align the text to the right. With a default to the right side
        """
        screenplay_title_style = ParagraphStyle("screenplay-title-style",
                                                fontName="Courier-Prime",
                                                fontSize=12,
                                                parent=styles['title'],
                                                alignment=1,)

        #screenplay_title_author_style = ParagraphStyle("screenplay-title-style",
                                                fontName="Courier-Prime",
                                                fontSize=12,
                                                parent=styles['title'],
                                                alignment=1)
        """

        """
        screenplay_dialogue_last_line_style = ParagraphStyle('screenplay-dialogue-style',
                                                    fontName="Courier",
                                                    fontSize=12,
                                                    parent=styles['Normal'],
                                                    alignment=0,
                                                    spaceAfter=15
                                                    leftIndent=1*inch)
        """

        fonts = os.listdir(r'C:\Windows\fonts')

        #print(chapters)
        #settings = ["screenplay"]

        """
        if settings[2].lower() == "novel":
            for x in chapters:
                story = Chapter_Content(x[0], story, novelchap_style)
                story = Chapter_Content(x[1], story, novelpar_style)
                story = Page_Break(story)
        elif settings[2].lower() == "screenplay":
            for x in chapters:
                story = Chapter_Content(x[0], story, screenplay_style)
                story = Chapter_Content(x[1], story, screenplay_style)
                story = Page_Break(story)
        else:
            print(f"Unkown style: '{settings[2]}'")
        """

        # Add different screenplay_x_style with different spacings before and after for different scenarios and write an algorithm to decide when to use which screenplay_x_style
        #story.append(Paragraph("Test Title", screenplay_title_style))
        story.append(PageBreak())
        story.append(Paragraph("BLACK.", screenplay_transition_style))
        story.append(Paragraph("JOY (V.O.)", screenplay_character_style))
        #story.append(Paragraph("(sample parentheticals)", screenplay_parenthetical_style))
        story.append(Paragraph("Do you ever look at someone and wonder, 'What is going on inside their head?' Well, I know. I know Riley's head.", screenplay_dialogue_style))
        story.append(Paragraph("WHITE. FADE IN...", screenplay_transition_style))
        story.append(Paragraph("INT. HOSPITAL - DAY", screenplay_slugline_style))
        story.append(Paragraph("A new born baby swaddled in a blanket, held by her parents.", screenplay_actionline_style))
        story.append(Paragraph("Push in... and ZOOM IN TO HER HEAD.", screenplay_actionline_style))
        story.append(Paragraph("INT. HEADQUARTERS", screenplay_slugline_style))
        story.append(Paragraph("Out of the blackness steps a glowing figure. This is JOY. The room is black except for a bright CONSCIOUSNESS SCREEN.", screenplay_actionline_style))
        story.append(Paragraph("JOY", screenplay_character_style))
        story.append(Paragraph("Hmm?", screenplay_dialogue_style))
        story.append(Paragraph("In front of Joy is a single large BUTTON. She pushes it.", screenplay_actionline_style))
        story.append(Paragraph("INT. HOSPITAL - CONTINUOUS", screenplay_slugline_style))
        story.append(Paragraph("The baby gurgles and wiggles happily.", screenplay_actionline_style))
        story.append(Paragraph("JOY (V.O.)", screenplay_character_style))
        story.append(Paragraph("And there she was...", screenplay_dialogue_style))
        story.append(Paragraph("INT. HEADQUARTERS - CONTINUOUS", screenplay_slugline_style))
        story.append(Paragraph("ON THE CONSCIOUSNESS SCREEN:", screenplay_actionline_style))
        story.append(Paragraph("MOM", screenplay_character_style))
        story.append(Paragraph("Hello, Riley.", screenplay_dialogue_style))
        story.append(Paragraph("DAD", screenplay_character_style))
        story.append(Paragraph("Oh look at you. Aren't you a little bundle of joy?", screenplay_dialogue_style))
        story.append(Paragraph("A GOLDEN GLOWING SPHERE rolls from behind the screen. It's a MEMORY of what we just saw: Mom and Dad cooing at Riley.", screenplay_actionline_style))
        story.append(Paragraph("JOY", screenplay_character_style))
        story.append(Paragraph("Whoa.", screenplay_dialogue_style))
        story.append(Paragraph("Joy rolls the memory on its track, illuminating the room. She turns back to the button and pushes it again.", screenplay_actionline_style))
        story.append(Paragraph("INT. HOSPITAL - CONTINUOUS", screenplay_slugline_style))
        story.append(Paragraph("Baby Riley gurgles happily.", screenplay_actionline_style))
        story.append(Paragraph("JOY (V.O.)", screenplay_character_style))
        story.append(Paragraph("It waas amazing. Just Riley and me, forever...", screenplay_dialogue_style))
        story.append(Paragraph("INT. HEADQUARTERS - CONTINUOUS", screenplay_slugline_style))
        story.append(Paragraph("Babu Riley CRIES.", screenplay_actionline_style))
        story.append(Paragraph("JOY (V.O.)", screenplay_character_style))
        story.append(Paragraph("...for 33 seconds.", screenplay_dialogue_style))
        story.append(Paragraph("Joy looks to her side. There's a new, droopy, blue character touching the button.", screenplay_actionline_style))
        story.append(Paragraph("SADNESS", screenplay_character_style))
        story.append(Paragraph("I'm Sadness", screenplay_dialogue_style))
        story.append(Paragraph("JOY (V.O.)", screenplay_character_style))
        story.append(Paragraph("Oh, hello. I’m Joy.", screenplay_dialogue_style))
        story.append(Paragraph("Joy tries to muscle past Sadness to press the button.", screenplay_actionline_style))
        story.append(Paragraph("JOY (CONT'D)", screenplay_character_style))
        story.append(Paragraph("Can I just... if you could... I just want to fix that. Thanks.", screenplay_dialogue_style))


        # was multiBuild
        doc.multiBuild(story, canvasmaker=lambda filename1=output_file, filename=output_file, settings=settings, **kwargs:FooterCanvas(filename1, filename, settings, **kwargs))
        #doc.build(story) #canvasmaker=lambda filename1=output_file, filename=output_file, settings=settings, **kwargs:FooterCanvas(filename1, filename, settings, **kwargs))

    def novel(settings, f_read, input_file, output_file):
        def Find_Chapters(file):
            pass

        def Get_Content(file, chapters):
            pass

    def screenplay(settings, f_read, input_file, output_file):
        # Max of 55 lines per page
        def Get_SceneHeading(f_read):
            pass
        def Get_FADE(f_read):
            pass

    file = open(input_file)
    file_read = file.readlines()
    f_read = []
    for i in file_read:
        f_read.append(i.split("\n")[0])

    #print(f_read)
    # Maybe if settings[3] == "screenplay" then do have another function that just finds all the content instead of trying to find chapters
    # Because now you need to have a chapter with screenplay even though it doesnt do anything
    settings = Settings(f_read)
    chapters = Find_Chapters(f_read)
    #print(chapters)
    chapters_and_content = Get_Content(f_read, chapters)
    Create_PDF(settings, chapters_and_content, output_file)
    #print(chapters)
    #print(chapters_and_content)
    file.close()