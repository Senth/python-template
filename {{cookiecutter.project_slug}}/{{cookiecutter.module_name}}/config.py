
from .utils.arg_parser import get_args
from .utils.config_file_args import ConfigFileArgs

_app_name = "{{cookiecutter.project_slug}}"


class Config:
    def __init__(self):
        # Default values
        self.app_name: str = _app_name
        self.debug: bool = False
        self.verbose: bool = False

    def _add_args_settings(self, args):
        """Set additional configuration from script arguments

        Args:
            args (list): All the parsed arguments
        """
        args = get_args()
        self.verbose = args.verbose
        self.debug = args.debug

        if args.debug:
            self.verbose = True

{%- if cookiecutter.external_config == "y" -%}
    def set_from_config_file(self, args: ConfigFileArgs) -> None:
        # TODO set config arguments
        # if args.port:
        #     self.port = args.port
{%- endif -%}

config = Config()
