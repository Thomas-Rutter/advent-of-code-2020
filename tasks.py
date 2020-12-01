"""Invoke Task file for repo."""
import os
from pathlib import Path
import platform
from shutil import copytree, ignore_patterns, rmtree

from invoke import task


def _ensure_directory(dir):
    """Ensure that the given directory path exists.

    Args:
        dir (str): The path of the directory.
    """
    if not os.path.isdir(dir):
        os.mkdir(dir)


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


@task
def install(c):
    """Build tool.

    Args:
        c: context arg to pass to invoke.
    """
    c.run("python setup.py install")


@task
def test(c):
    """Test tool.

    Args:
        c: context arg to pass to invoke.
    """
    c.run("tox src --skip-missing-interpreters")


@task
def lint(c):
    """Lint repo.

    Args:
        c: context arg to pass to invoke.
    """
    c.run("flake8 .")
    print("No linting errors found.")


@task
def version(c):
    """Print version of tool.

    Args:
        c: context arg to pass to invoke.
    """
    print(get_version())


@task
def set_version(c, version):
    """Set the version of the tool.

    Args:
        c: context arg to pass to invoke.
        version: The version to set the tool to.
    """
    init_file = Path("./src/advent_of_code_2020/__init__.py")
    with open(init_file, "r") as read_file:
        lines = read_file.readlines()
    new_lines = []
    for line in lines:
        if line.startswith("__version__ ="):
            line = f'__version__ = "{version}"\n'
        new_lines.append(line)
    with open(init_file, "w") as write_file:
        write_file.writelines(new_lines)


@task
def docs(c):
    """Create and copy the docs to read_my_docs.

    Args:
        c: context arg to pass to invoke.
    """
    c.run("python setup.py build_sphinx")
    repo = "advent-of-code-2020"
    source = Path("./build/sphinx/html/")
    docs_dir = Path(f"R:/Read-My-Docs/docs/{repo}")
    version = get_version()
    _ensure_directory(docs_dir)
    dest = Path.joinpath(docs_dir, repo)
    if os.path.exists(dest):
        rmtree(dest)
    copytree(source, dest, ignore=ignore_patterns(".buildinfo"))
    dest = Path.joinpath(docs_dir, f"{repo}-{version}")
    copytree(source, dest, ignore=ignore_patterns(".buildinfo"))


@task
def preview_docs(c):
    """Build docs and open them.

    Args:
        c: context arg to pass to invoke.
    """
    c.run("python setup.py build_sphinx")
    index = Path("./build/sphinx/html/index.html")
    if platform.system() == "Windows":
        c.run(f"start {index}")
    elif platform.system() == "Linux":
        c.run(f"xdg-open {index}")
