from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER, LEGAL, TABLOID
from reportlab.lib.pagesizes import A1, A2, A3, A4, A5, A6
import typer
import requests

__VERSION__ = "1.0.0-Alpha"

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
        #https://raw.githubusercontent.com/Cerabbite/writing/main/LATEST_VERSION
        return __VERSION__

    file = open(input_file)
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

if __name__ == "__main__":
    app()
