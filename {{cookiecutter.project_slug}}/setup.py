from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

project_slug = "{{cookiecutter.project_slug}}"
module_name = project_slug.replace('-', "_")

setup(
    name=project_slug,
    use_scm_version=True,
    url=f"https://github.com/{{cookiecutter.github_username}}/{project_slug}",
    license="MIT",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.project_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
{%- if cookiecutter.library == 'n' -%}
    entry_points={"console_scripts": [f"{project_slug}={module_name}.__main__:main"]},
{%- endif -%}
{%- if cookiecutter.external_config == "y" -%}
    include_package_data=True,
    data_files=[(f"config", [f"config/{project_slug}-example.cfg"])],
{%- endif -%}
    install_requires=[
{%- if cookiecutter.library == 'n' -%}
        "tealprint",
{%- endif -%}
{%- if cookiecutter.external_config == "y" -%}
        "blulib",
{%- endif -%}
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
{%- if cookiecutter.library == 'y' -%}
        "Topic :: Software Development :: Libraries",
{%- endif -%}
{%- if cookiecutter.library == 'n' -%}
        "Environment :: Console",
{%- endif -%}
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
