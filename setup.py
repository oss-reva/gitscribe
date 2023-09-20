"""setup.py for runnable packaegs."""

from gitbot.consts import NAME, VERSION

from setuptools import setup, find_packages

setup(
    name=NAME,
    version=VERSION,

    packages=find_packages(),
    scripts=["scripts/gbot"]
)
