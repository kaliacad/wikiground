"""Wikiground-cli entry point script."""
# wikiground-cli/__main__.py

from wikiground_cli import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()