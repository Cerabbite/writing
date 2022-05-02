import typer

__VERSION__ = "1.0.0-Alpha"

app = typer.Typer()

@app.command()
def hello():
    print("Hello")

@app.command()
def VERSION():
    print("Your current version is v1.0.0-Alpha")

if __name__ == "__main__":
    app()
