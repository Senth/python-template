import importlib.machinery
import importlib.util
import site
import sys
from os import path
from typing import Any

from .utils.arg_parser import get_args

_app_name = "{{cookiecutter.project_slug}}"

{%- if cookiecutter.external_config == "y" -%}
_config_dir = path.join("config", _app_name)
_config_file = path.join(_config_dir, "config.py")
_example_file = path.join(_config_dir, "config.example.py")

# Search for config file in sys path
_sys_config = path.join(sys.prefix, _config_file)
_user_config_file = path.join(site.getuserbase(), _config_file)
_config_file = ""
if path.exists(_sys_config):
    _config_file = _sys_config
elif path.exists(_user_config_file):
    _config_file = _user_config_file
# User hasn't configured the program yet
else:
    _sys_config_example = path.join(sys.prefix, _example_file)
    _user_config_example = path.join(site.getuserbase(), _example_file)
    if not path.exists(_sys_config_example) and not path.exists(_user_config_example):
        print(f"Error: no configuration found. It should be here: '{_user_config_file}'")
        print("run: locate " + _example_file)
        print("This should help you find the current config location.")
        print(
            f"Otherwise you can download the config.example.py from https://github.com/Senth/{_app_name}/tree/main/config and place it in the correct location"
        )
        sys.exit(1)

    print("This seems like it's the first time you run this program.")
    print(f"For this program to work properly you have to configure it by editing '{_user_config_file}'")
    print("In the same folder there's an example file 'config.example.py' you can copy to 'config.py'.")
    sys.exit(0)

# Import config
_loader = importlib.machinery.SourceFileLoader("config", _user_config_file)
_spec = importlib.util.spec_from_loader(_loader.name, _loader)
_user_config: Any = importlib.util.module_from_spec(_spec)
_loader.exec_module(_user_config)


def _print_missing(variable_name):
    print(f"Missing {variable_name} variable in config file: {_user_config_file}")
    print("Please add it to you config.py again to continue")
    sys.exit(1)
{%- endif -%}

class Config:
    def __init__(self, user_config):
        self._user_config = user_config

        # Default values
        self.app_name: str = _app_name
        self.debug: bool
        self.verbose: bool

{%- if cookiecutter.external_config == "y" -%}
        self._get_optional_variables()
        self._check_required_variables()
{%- endif -%}
        self._add_args_settings()

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
    def _get_optional_variables(self):
        """Get optional values from the config file"""
        # try:
        #     self.log_dir = _user_config.LOG_DIR
        # except AttributeError:
        #     pass

    def _check_required_variables(self):
        """Check that all required variables are set in the user config file"""
        # try:
        #     self.port = _user_config.PORT
        # except AttributeError:
        #     _print_missing("PORT")
{%- endif -%}

config = Config(_user_config)
