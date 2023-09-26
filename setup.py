"""setup.py for runnable packaegs."""

from setuptools import setup, find_packages
from gbot.consts import NAME, VERSION

requirements = open("requirements.txt").read().splitlines()

setup(
    name=NAME,
    version=VERSION,

    install_requires=requirements,

    packages=find_packages(),
    scripts=[
        "scripts/gbot"
    ]
)
