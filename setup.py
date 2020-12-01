"""Setup module for package."""
from pathlib import Path

from setuptools import find_packages, setup


def get_version():
    """Get the version from the __init__.py file.

    Returns:
        str: The version.
    """
    init_file = Path("./src/advent_of_code_2020/__init__.py")
    with open(init_file, "r") as read_file:
        lines = read_file.readlines()
    for line in lines:
        if line.startswith("__version__ ="):
            return line.split('"')[1]


NAME = "advent-of-code-2020"
VERSION = get_version()

setup(
    name=NAME,
    version=VERSION,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    command_options={
        'build_sphinx': {
            'project': ('setup.py', NAME),
            'version': ('setup.py', VERSION),
            'release': ('setup.py', VERSION),
            'source_dir': ('setup.py', 'docs')
        }
    },
    # entry_points={
    #     'console_scripts': [
    #         'name = advent_of_code_2020.core:main'
    #     ]
    # },
)
