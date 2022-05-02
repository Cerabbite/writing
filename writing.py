import typer
import requests

__VERSION__ = "1.0.0-Alpha"

app = typer.Typer()

@app.command()
def WRITING(input_file: str, output_file: str):
    print(input_file, output_file)

def LIST_OF_VERSION(version):
    release = version
    release_list = release.split(".")
    try:
        thing = release_list[2].split("-")[0]
        print(1)
        thing2 = release_list[2].split("-")[1]
        print(2)
        release_list[2] = thing
        print(3)
        release_list.append(thing2)
        print(4)
    except Exception as e:
        print(e)
    print(release_list)
    release = []
    for i in release_list:
        release.append(i.split('\n')[0])
    print(release)
    return release


@app.command()
def VERSION(check: bool=False):
    print(f"Your current version is v{__VERSION__}")
    if check:
        url = 'https://raw.githubusercontent.com/Cerabbite/writing/main/LATEST_VERSION'
        page = requests.get(url)
        print(LIST_OF_VERSION(page.text))
        #print("No update available")

@app.command()
def DOWNLOAD():
    print("You  are currently unable to download the latest version via you command line go to .... to download the latest version")
    # refer to VERSION() to check if update is available

if __name__ == "__main__":
    app()
