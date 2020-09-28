#!/usr/bin/env python3.8

# Copyright: Ismael Narváez Berenjeno
import pathlib

from setuptools import setup

description = "Validates input/output data used in a JSON API."

# Get the long description from the README file
long_description = (
    pathlib.Path(__file__).parent.resolve() / "README.md"
).read_text(encoding="utf-8")

setup(
    name="json-api-validation",
    version="0.0.1",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
    ],
    author="Ismael Narváez",
    url="https://github.com/isnarvaez/json-api-validation",
    license="MIT",
    packages=["json_api_validation"],
    python_requires=">=3.6",
    install_requires=["pydantic>=1.6.1", "jsonpointer>=2.0"],
)
