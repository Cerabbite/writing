import typer

__VERSION__ = "1.0.0-Alpha"

app = typer.Typer()

@app.command()
def hello():
    print("Hello")

@app.command()
def VERSION(check: bool=False):
    print(f"Your current version is v{__VERSION__}")
    if check:
        print("No update available")

if __name__ == "__main__":
    app()
