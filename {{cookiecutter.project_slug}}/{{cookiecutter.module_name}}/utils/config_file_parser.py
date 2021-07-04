import configparser
from pathlib import Path
from shutil import copy
from site import getuserbase
from typing import Any

from ..config import config
from .config_file_args import ConfigFileArgs


class ConfigFileParser:
    def __init__(self) -> None:
        self.path = Path.home().joinpath(f".{config.app_name}.cfg")

    def get_args(self) -> ConfigFileArgs:
        args = ConfigFileArgs()

        if not self.path.exists():
            return args

        config = configparser.ConfigParser()
        config.read(self.path)

        # TODO add configuration variables
        # if "general" in config:
        #     general = config["general"]
        #     ConfigFileParser._set_str(args, general, "port")

        return args

    @staticmethod
    def _set_str(args: Any, section: configparser.SectionProxy, *varnames: str) -> None:
        for varname in varnames:
            default = getattr(args, varname)
            value = section.get(varname, fallback=default)
            setattr(args, varname, value)

    @staticmethod
    def _set_str_list(args: Any, section: configparser.SectionProxy, *varnames: str) -> None:
        for varname in varnames:
            values = getattr(args, varname)
            value = section.get(varname, fallback="")
            if value != "":
                values = value.split("\n")
            setattr(args, varname, values)

    def create_if_not_exists(self) -> None:
        if self.path.exists():
            return

        # Copy file from config location to home
        example_name = f"{config.app_name}-example.cfg"
        example_path = Path(getuserbase()).joinpath("config", example_name)

        if not example_path.exists():
            return

        copy(example_path, self.path)
