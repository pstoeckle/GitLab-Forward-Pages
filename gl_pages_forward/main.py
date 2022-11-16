"""
Main.
"""
from logging import INFO, basicConfig, getLogger
from os import mkdir
from pathlib import Path
from typing import Mapping, Optional

from click import echo
from click.exceptions import Exit
from jinja2 import Environment, PackageLoader
from ruamel.yaml import safe_load

from gl_pages_forward import __version__
from minify_html import minify as minify_html_minify
from typer import Option, Typer

basicConfig(level=INFO)
app = Typer()
_LOGGER = getLogger(__name__)
_ENV = Environment(
    loader=PackageLoader("gl_pages_forward", "rsc"), trim_blocks=True, autoescape=True
)
_INDEX_TEMPLATE = _ENV.get_template("index.html.j2")
_OVERVIEW_TEMPLATE = _ENV.get_template("overview.html.j2")


def _version_callback(value: bool) -> None:
    """

    Args:
        value:

    Returns:

    """
    if value:
        echo(f"gl-pages-forward {__version__}")
        raise Exit()


@app.command()
def create_html_pages(
    _: Optional[bool] = Option(None, "--version", "-v", callback=_version_callback),
    config_file: Path = Option(
        "config.yml",
        "--config-file",
        "-c",
        dir_okay=False,
        exists=True,
        resolve_path=True,
    ),
    output: Path = Option(
        Path(".", "public"),
        "--output",
        "-o",
        file_okay=False,
        writable=True,
        resolve_path=True,
    ),
    base_url: str = Option("", "--base-url", "-u"),
    minify: bool = Option(
        False,
        "--minify",
        "-m",
        is_flag=True,
        help="If this flag is set, the tool will minify the HTML.",
    ),
) -> None:
    """
    Creates 'index.html's that forward to a specific URL.
    """
    with config_file.open() as f_read:
        configuration: Mapping[str, str] = safe_load(f_read.read())
    if configuration is None or not isinstance(configuration, dict):
        _LOGGER.critical(f"Please provide a valid YAML file in {config_file}")

    if not output.is_dir():
        mkdir(output)
    for file_name, url in configuration.items():
        if file_name == "index":
            new_file = output.joinpath("index.html")
        else:
            new_folder = output.joinpath(file_name)
            mkdir(new_folder)
            new_file = new_folder.joinpath("index.html")
        _LOGGER.info(f"Create file {new_file}")
        content = _INDEX_TEMPLATE.render(new_url=url)
        if minify:
            content = minify_html_minify(content, minify_js=True, minify_css=False)
        with open(new_file, "w") as f_write:
            f_write.write(content)
    if base_url != "":
        with output.joinpath("overview.html").open("w") as f_write:
            f_write.write(
                _OVERVIEW_TEMPLATE.render(url=base_url, websites=configuration.items())
            )


if __name__ == "__main__":
    app()
