import typer

app = typer.Typer()

@app.command()
def hello():
    print("Hello")

def VERSION():
    print("Your current version is v1.0.0-Alpha")

if __name__ == "__main__":
    app()
