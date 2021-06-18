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
    entry_points={"console_scripts": [f"{project_slug}={module_name}.__main__:main"]},
{%- if cookiecutter.external_config == "y" -%}
    include_package_data=True,
    data_files=[(f"config/{project_slug}", ["config/config.example.py"])],
{%- endif -%}
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Licence :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.8",
)
