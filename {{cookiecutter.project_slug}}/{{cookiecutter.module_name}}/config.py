from tealprint import TealLevel

from .utils.config_file_args import ConfigFileArgs

_app_name = "{{cookiecutter.project_slug}}"


class Config:
    def __init__(self):
        # Default values
        self.app_name: str = _app_name
        self.level = TealLevel.info

    def set_from_cli(self, args):
        """Set additional configuration from script arguments

        Args:
            args (list): All the parsed arguments
        """
        if args.debug:
            self.level = TealLevel.debug
        elif args.verbose:
            self.level = TealLevel.verbose

{%- if cookiecutter.external_config == "y" -%}
    def set_from_config_file(self, args: ConfigFileArgs) -> None:
        # TODO set config arguments
        # if args.port:
        #     self.port = args.port
{%- endif -%}

config = Config()
