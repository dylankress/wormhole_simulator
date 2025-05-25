"""Console script for wormhole_simulator."""
import wormhole_simulator

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for wormhole_simulator."""
    console.print("Replace this message by putting your code into "
               "wormhole_simulator.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
