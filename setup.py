from setuptools import setup, find_packages
import pathlib

current_dir = pathlib.Path(__file__).parent

read_me = (current_dir / "README.md").read_text()

setup(
    name="pydadjoke",
    version="1.0.0",
    description="CLI to call the icanhazdadjoke API and returns a dad joke",
    long_description=read_me,
    long_description_content_type="text/markdown",
    install_requires=[
        "fire",
        "requests"
    ],
    url="https://github.com/jwood803/pydadjoke",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["pydadjoke=src.__main__:main"]}
)