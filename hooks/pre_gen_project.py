import re
import sys

# Project slug
PROJECT_SLUG_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"

project_slug = "{{cookiecutter.project_slug}}"

if not re.match(PROJECT_SLUG_REGEX, project_slug):
    print(
        f"ERROR: The project slug ({project_slug}) is not a valid Python module name. Please use - instead of spaces and _"
    )

    # Exit to cancel project
    sys.exit(1)


# Module name
MODULE_REGEX = r"^[a-zA-Z][a-zA-Z0-9]+$"

module_name = "{{cookiecutter.module_name}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        f"ERROR: The project slug ({module_name}) is not a valid Python module name. Please do not use - or _"
    )

    # Exit to cancel project
    sys.exit(1)