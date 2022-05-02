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
