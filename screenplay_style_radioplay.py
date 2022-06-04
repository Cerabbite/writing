#Original: Copyright 2019 Manuel Senfft
#Edited: Copyright (c) 2022 Cerabbite
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.colors import lightgrey, grey
from reportlab.lib.pagesizes import A4

# settings and style

DOC_SIZE = A4
FONT = 'font/Courier Prime.ttf'
FONTITALIC = 'font/Courier Prime Italic.ttf'
FONTBOLD = 'font/Courier Prime Bold.ttf'
FONTBOLDITALIC = 'font/Courier Prime Bold Italic.ttf'
SIZE = 16
INDENT_LEFT = 28
INDENT_RIGHT = 28
PRINT_EMPTY_LINES = True

RIGHTMARGIN = 65
LEFTMARGIN = 65
TOPMARGIN = 65
BOTTOMMARGIN = 65

SCENE_NUMBER_L = True
SCENE_NUMBER_R = True

registerFont(TTFont('Courier-Prime', FONT))
registerFont(TTFont('Courier-Prime-Italic', FONTITALIC))
registerFont(TTFont('Courier-Prime-Bold', FONTBOLD))
registerFont(TTFont('Courier-Prime-Bold-Italic', FONTBOLDITALIC))


STYLE_TITLEPAGE_TITLE = ParagraphStyle(
    'Titlepage Title',
    fontName='Courier-Prime',
    fontSize=SIZE * 3,
    leading=SIZE * 4,
    spaceAfter=SIZE * 6,
    alignment=TA_CENTER
)

STYLE_TITLEPAGE_CREDIT = ParagraphStyle(
    'Titlepage Credit',
    fontName='Courier-Prime',
    fontSize=SIZE * 0.75,
    leading=SIZE * 0.75 * 1.25,
    spaceAfter=SIZE * 2,
    alignment=TA_CENTER
)

STYLE_TITLEPAGE_AUTHOR = ParagraphStyle(
    'Titlepage Author',
    fontName='Courier-Prime',
    fontSize=SIZE,
    leading=SIZE * 1.25,
    spaceAfter=SIZE,
    alignment=TA_CENTER
)

STYLE_TITLEPAGE_DATE = ParagraphStyle(
    'Titlepage Date',
    fontName='Courier-Prime-Italic',
    fontSize=SIZE,
    leading=0,
    textColor=grey
)

STYLE_TITLEPAGE_CONTACT = ParagraphStyle(
    'Titlepage Contact',
    fontName='Courier-Prime-Italic',
    fontSize=SIZE,
    alignment=TA_RIGHT,
    leading=SIZE * 1.25,
    textColor=grey
)

STYLE_SECTION_HEADING = ParagraphStyle(
    'Section Heading',
    fontName='Courier-Prime',
    fontSize=SIZE * 1.4,
    leading=SIZE * 1.4 * 1.25,
    alignment=TA_CENTER
)

STYLE_SCENE_NUMBER_L = ParagraphStyle(
    'Scene Number Left',
    fontName='Courier-Prime-Bold',
    fontSize=SIZE,
    leading=0,
    textTransform='uppercase'
)

STYLE_SCENE_HEADING = ParagraphStyle(
    'Scene Heading',
    fontName='Courier-Prime-Bold',
    fontSize=SIZE,
    leading=0,
    leftIndent=SIZE * 2.5,
    rightIndent=SIZE * 2.5,
    textTransform='uppercase'
)

STYLE_SCENE_NUMBER_R = ParagraphStyle(
    'Scene Number Right',
    fontName='Courier-Prime-Bold',
    fontSize=SIZE,
    leading=SIZE * 1.25,
    alignment=TA_RIGHT,
    textTransform='uppercase'
)

STYLE_COMMENT = ParagraphStyle(
    'Comment',
    fontName='Courier-Prime-Italic',
    fontSize=SIZE * 0.7,
    leading=SIZE * 0.7,
    leftIndent=SIZE * 6,
    rightIndent=SIZE * 6,
    textColor=grey,
    alignment=TA_CENTER
)

STYLE_ACTION = ParagraphStyle(
    'Action',
    fontName='Courier-Prime',
    fontSize=SIZE,
    leading=SIZE * 1.25,
    leftIndent=SIZE * 2.5,
    rightIndent=SIZE * 2.5,
    textColor=grey
)

STYLE_CHARACTER = ParagraphStyle(
    'Character',
    fontName='Courier-Prime',
    fontSize=SIZE,
    leading=SIZE * 1.25,
    leftIndent=SIZE * 2.5,
    rightIndent=SIZE * 2.5,
    textTransform='uppercase'
)

STYLE_PARENTHETICAL = ParagraphStyle(
    'Parenthetical',
    fontName='Courier-Prime',
    fontSize=SIZE * 0.75,
    leading=SIZE * 0.75 * 1.25,
    leftIndent=SIZE * 2.5 + SIZE * 1.8,
    rightIndent=SIZE * 2.5
)

STYLE_DIALOGUE = ParagraphStyle(
    'Dialogue',
    fontName='Courier-Prime',
    fontSize=SIZE,
    leading=SIZE * 1.25,
    leftIndent=SIZE * 2.5 + SIZE * 1.8,
    rightIndent=SIZE * 2.5
)

STYLE_CHARACTER_MARK = ParagraphStyle(
    'Character_Mark',
    fontName='Courier-Prime',
    fontSize=SIZE,
    leading=SIZE * 1.25,
    leftIndent=SIZE * 2.5,
    rightIndent=SIZE * 2.5,
    textTransform='uppercase',
    backColor=lightgrey
)

STYLE_PARENTHETICAL_MARK = ParagraphStyle(
    'Parenthetical Mark',
    fontName='Courier-Prime-Italic',
    fontSize=SIZE * 0.75,
    leading=SIZE * 0.75 * 1.25,
    leftIndent=SIZE * 2.5 + SIZE * 1.8,
    rightIndent=SIZE * 2.5,
    backColor=lightgrey
)


STYLE_DIALOGUE_MARK = ParagraphStyle(
    'Dialogue Mark',
    fontName='Courier-Prime',
    fontSize=SIZE,
    leading=SIZE * 1.25,
    leftIndent=SIZE * 2.5 + SIZE * 1.8,
    rightIndent=SIZE * 2.5,
    backColor=lightgrey
)

STYLE_TRANSITION = ParagraphStyle(
    'Transition',
    fontName='Courier-Prime',
    fontSize=SIZE,
    leading=SIZE * 1.25,
    leftIndent=SIZE * 2.5,
    rightIndent=SIZE * 2.5,
    textTransform='uppercase',
    textColor=grey,
    alignment=TA_CENTER
)

STYLE_EMPTY_LINE = ParagraphStyle(
    'Empty Line',
    fontName='Courier-Prime',
    fontSize=SIZE,
    leading=SIZE,
    leftIndent=SIZE * 2.5,
    rightIndent=SIZE * 2.5
)

STYLE_INDEX_SECTION = ParagraphStyle(
    'Index Section',
    fontName='Courier-Prime',
    fontSize=SIZE * 1.5,
    leading=SIZE * 2,
    leftIndent=SIZE * 2.5,
    rightIndent=SIZE * 2.5,
    spaceAfter=SIZE * 1.5
)

STYLE_INDEX_SCENE = ParagraphStyle(
    'Index Scene',
    fontName='Courier-Prime',
    fontSize=SIZE * 1.5,
    leading=SIZE * 2,
    leftIndent=SIZE * 4,
    rightIndent=SIZE * 4,
    spaceAfter=SIZE * 1.5
)

STYLE_INDEX_LOCATION = ParagraphStyle(
    'Index Location',
    fontName='Courier-Prime',
    fontSize=SIZE * 3,
    leading=SIZE * 3.5,
    leftIndent=SIZE * 4,
    rightIndent=SIZE * 4,
    spaceAfter=SIZE * 3
)

STYLE_SOUNDLIST_LOCATION_HEAD = ParagraphStyle(
    'Soundlist Location Head',
    fontName='Courier-Prime',
    fontSize=SIZE * 4,
    leading=SIZE * 4,
    alignment=TA_CENTER
)

STYLE_SOUNDLIST_LOCATION = ParagraphStyle(
    'Soundlist Location',
    fontName='Courier-Prime'
    fontSize=SIZE * 1.5,
    leading=SIZE * 2
)

STYLE_SOUNDLIST_SCENE = ParagraphStyle(
    'Soundlist Scene',
    fontName='Courier-Prime',
    fontSize=SIZE * 2,
    leading=SIZE * 6
)

STYLE_SOUNDLIST_SOUND = ParagraphStyle(
    'Soundlist Sound',
    fontName='Courier-Prime',
    fontSize=SIZE * 2.5,
    leading=SIZE * 3
)

STYLE_SYNOPSIS = ParagraphStyle(
    'Synopsis',
    fontName='Courier-Prime-Italic',
    fontSize=SIZE * 0.7,
    leading=SIZE * 0.7,
    leftIndent=SIZE * 6,
    rightIndent=SIZE * 6,
    textColor=grey,
    alignment=TA_CENTER
)


# DEFAULT PARAGRAPH STYLE:
#
# 'fontName':'Times-Roman',
# 'fontSize':10,
# 'leading':12,
# 'leftIndent':0,
# 'rightIndent':0,
# 'firstLineIndent':0,
# 'alignment':TA_LEFT,
# 'spaceBefore':0,
# 'spaceAfter':0,
# 'bulletFontName':'Times-Roman',
# 'bulletFontSize':10,
# 'bulletIndent':0,
# 'textColor': black,
# 'backColor':None,
# 'wordWrap':None,
# 'borderWidth': 0,
# 'borderPadding': 0,
# 'borderColor': None,
# 'borderRadius': None,
# 'allowWidows': 1,
# 'allowOrphans': 0,
# 'textTransform':None,
# 'endDots':None,
# 'splitLongWords':1,
# 'underlineProportion': _baseUnderlineProportion,
# 'bulletAnchor': 'start',
