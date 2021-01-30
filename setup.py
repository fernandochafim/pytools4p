#!/usr/bin/env python3
""" PYTHON TOOLS FOR PROJECTS is a personal package for Data Science Projects with Python.
It provides:
- TODO
- TODO
- TODO
- TODO
- TODO
Besides its obvious scientific uses, it can also be used as an efficient
multi-dimensional container of generic data. Arbitrary data-types can be
defined.
All pytools4p wheels are distributed on PyPI are BSD licensed.
"""
DOCLINES = (__doc__ or '').split("\n")

import sys
import setuptools

# Python supported version checks. Keep right after stdlib imports to ensure we
# get a sensible error for older Python versions
if sys.version_info[:2] < (3, 7):
    raise RuntimeError("Python version >= 3.7 required.")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytools4p",
    version="0.0.1",
    author="Fernando Chafim",
    author_email="fernandochafim@gmail.com",
    description="A personal package with tools for my Data Science Projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fernandochafim/pytools4p",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)