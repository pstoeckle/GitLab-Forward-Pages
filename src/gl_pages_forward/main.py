"""
Main.
"""
from logging import INFO, basicConfig, getLogger
from os import mkdir
from os.path import isdir, isfile, join
from typing import Dict

from click import command, option
from jinja2 import Environment, PackageLoader
from ruamel.yaml import safe_load

basicConfig(level=INFO)

_LOGGER = getLogger(__name__)
_ENV = Environment(
    loader=PackageLoader("gl_pages_forward", "rsc"), trim_blocks=True, autoescape=True
)
_INDEX_TEMPLATE = _ENV.get_template("index.html.j2")
_OVERVIEW_TEMPLATE = _ENV.get_template("overview.html.j2")


@option("--base_url", "-u", default="")
@option("--output", "-o", default=join(".", "public"))
@option("--config_file", "-c", default="config.yml")
@command()
def create_html_pages(config_file: str, output: str, base_url: str) -> None:
    """

    Args:
        config_file:
        output:
        base_url:
    Returns:

    """
    if isfile(config_file):
        with open(config_file) as f_read:
            configuration: Dict[str, str] = safe_load(f_read.read())
        if configuration is None or not isinstance(configuration, dict):
            _LOGGER.critical(f"Please provide a valid YAML file in {config_file}")

        if not isdir(output):
            mkdir(output)
        for file_name, url in configuration.items():
            if file_name == "index":
                new_file = join(output, "index.html")
            else:
                new_folder = join(output, file_name)
                mkdir(new_folder)
                new_file = join(new_folder, "index.html")
            _LOGGER.info(f"Create file {new_file}")
            content = _INDEX_TEMPLATE.render(new_url=url)
            with open(new_file, "w") as f_write:
                f_write.write(content)
        if base_url != "":
            with open(join(output, "overview.html"), "w") as f_write:
                f_write.write(
                    _OVERVIEW_TEMPLATE.render(url=base_url, websites=configuration.items())
                )
    else:
        _LOGGER.critical(f"{config_file} is not a file!")


if __name__ == "__main__":
    create_html_pages()
