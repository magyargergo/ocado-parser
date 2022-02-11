import os
from setuptools import setup, find_packages
from apps import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = []

setup(
    name="ocado_parser",
    version=".".join(map(str, __version__)),
    description="A simple tool to parse ocardo receipt.",
    license="MIT",
    author="Gergo Magyar",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=requirements,
    tests_require=[],
    long_description=read("README.md"),
)
