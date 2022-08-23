"""This module provides the Wikiground CLI"""
# wikiground-cli/cli.py

from typing import Optional

import typer

from wikiground_cli import __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        # raise typer.Exit() # why does not it cleanly exit the application ?

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback(True),
        # is_eager=True
    )
) -> None:
    return