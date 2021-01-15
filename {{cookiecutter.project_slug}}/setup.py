from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

module_name = "{{cookiecutter.module_name}}"
project_slug = "{{cookiecutter.project_slug}}"

setup(
    name=project_slug,
    version="{{cookiecutter.version}}",
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}",
    license="MIT",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.project_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[module_name],
    entry_points={"console_scripts": [f"{project_slug}={module_name}.__main__:main"]},
    include_package_data=True,
    data_files=[(f"config/{project_slug}", ["config/config.example.py"])],
    install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Licence :: OSI Approved :: MIT Licence",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)
