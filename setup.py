from setuptools import setup, find_packages
from gbot.consts import NAME, VERSION

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.rst", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name=NAME,
    version=VERSION,
    description="A Discord bot that provides information about GitHub repositories and issues.",
    long_description=long_description,
    author="SNG Viraj Reddy",
    author_email="vir200319@gmail.com",
    url="https://github.com/oss-reva/gbot.py",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    install_requires=requirements,
    scripts=[
        "scripts/gbot"
    ]
)
