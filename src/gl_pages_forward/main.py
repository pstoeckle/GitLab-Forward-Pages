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


@option("--output", "-o", default=join(".", "public"))
@option("--config_file", "-c", default="config.yml")
@command()
def create_html_pages(config_file: str, output: str) -> None:
    """

    Args:
        config_file:
        output:

    Returns:

    """
    if isfile(config_file):
        with open(config_file) as f_read:
            configuration: Dict[str, str] = safe_load(f_read.read())
        if configuration is None or not isinstance(configuration, dict):
            _LOGGER.critical(f"Please provide a valid YAML file in {config_file}")
        template = _ENV.get_template("index.html.j2")
        if not isdir(output):
            mkdir(output)
        for file_name, url in configuration.items():
            new_file = join(output, file_name) + ".html"
            _LOGGER.info(f"Create file {new_file}")
            content = template.render(new_url=url)
            with open(new_file, "w") as f_write:
                f_write.write(content)
    else:
        _LOGGER.critical(f"{config_file} is not a file!")


if __name__ == "__main__":
    create_html_pages()
