from setuptools import setup, find_packages
import pathlib

current_dir = pathlib.Path(__file__).parent

read_me = (current_dir / "README.md").read_text()

setup(
    name="py-dad-joke",
    version="1.0.0",
    long_description=,
    long_description_content_type="text/markdown",
    install_requires=[
        "fire",
        "requests"
    ],
    packages=find_packages(),
    description="CLI to call the dad joke API and returns a random joke",
    entry_points={"console_scripts": ["joke"]}
)