"""Python setup.py for better_compiler_output package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("better_compiler_output", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="better_compiler_output",
    version=read("better_compiler_output", "VERSION"),
    description="Awesome better_compiler_output created by JRodez",
    url="https://github.com/JRodez/Better-Compiler-Output/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="JRodez",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["bco = better_compiler_output.__main__:main"]
    },
)
