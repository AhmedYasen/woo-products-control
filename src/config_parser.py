"""
parsing the config toml file as dict
"""
from pathlib import Path
import tomli


def config_parser(toml_path: Path):
    """
    :toml_path: path to config file.toml
    """
    return tomli.load(toml_path.open('rb'))
