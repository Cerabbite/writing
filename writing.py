import typer
import requests

__VERSION__ = "1.0.0-Alpha"

app = typer.Typer()

@app.command()
def WRITING(input_file: str, output_file: str):
    print(input_file, output_file)

@app.command()
def VERSION(check: bool=False):
    print(f"Your current version is v{__VERSION__}")
    if check:
        url = 'https://raw.githubusercontent.com/Cerabbite/writing/main/LATEST_VERSION'
        page = requests.get(url)
        latest_release = page.text
        latest_release_list = latest_release.split(".")
        print9
        print(page.text)
        #print("No update available")

@app.command()
def DOWNLOAD():
    print("You  are currently unable to download the latest version via you command line go to .... to download the latest version")
    # refer to VERSION() to check if update is available

if __name__ == "__main__":
    app()
