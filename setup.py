# -*- coding: utf-8 -*-

import os
import sys
from codecs import open
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)

    def run_tests(self):
        import pytest

        errno = pytest.main([])
        sys.exit(errno)


current_path = os.path.abspath(os.path.dirname(__file__))
os.chdir(os.path.abspath(current_path))


version = {}
with open(
    os.path.join(current_path, "cheddar", "version.py"), encoding="utf-8"
) as f:
    exec(f.read(), version)

setup(
    name="cheddarpayments",
    version=version["VERSION"],
    description="Cheddar Python Bindings",
    long_description=open("./README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Palo Sopko",
    author_email="pavol.sopko@backbone.sk",
    url="https://www.backbone.sk/en/",
    license="MIT",
    keywords="cheddar, api, payments, money, cardpay, comfortpay, tatrapay, trustpay, sporopay, eplatby, gpwebpay, iterminal",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=["requests >= 2.21.0", "six >= 1.3.0"],
    tests_require=["pytest >= 4.6.2, < 4.7"],
    cmdclass={"test": PyTest},
    project_urls={
        "Bug Tracker": "https://github.com/backbonesk/cheddar-python/issues",
        "Source Code": "https://github.com/backbonesk/cheddar-python",
    },
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
