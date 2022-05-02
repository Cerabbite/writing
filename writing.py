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


@app.command()
def VERSION(check: bool=False):
    print(f"Your current version is v{__VERSION__}")
    if check:
        url = 'https://raw.githubusercontent.com/Cerabbite/writing/main/LATEST_VERSION'
        page = requests.get(url)
        latest_version = LIST_OF_VERSION(page.text)
        current_version = LIST_OF_VERSION(__VERSION__)
        print(latest_version)
        print(current_version)
        if latest_version[0] > current_version[0]:
            print(f"New version available {page.text}")
        elif latest_version[1] > current_version[1]:
            print(f"New version available {page.text}")
        elif latest_version[2] > current_version[2]:
            print(f"New version available {page.text}")
        elif len(latest_version) < len(current_version):
            print(f"New version available {page.text}")
        elif len(latest_version) == 4 and len(current_version) == 4:
            if latest_version[3] == 'Beta' and latest_version[3] == 'Alpha':
                print(f"New version available {page.text}")
        #print("No update available")

@app.command()
def DOWNLOAD():
    print("You  are currently unable to download the latest version via you command line go to .... to download the latest version")
    # refer to VERSION() to check if update is available

if __name__ == "__main__":
    app()
