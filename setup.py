#!/usr/bin/env python
import io
import os
import re

from setuptools import find_packages, setup

setup(
    name="server",
    version=1.0,
    license="MIT",
    description="Security systems management",
    author="tzevet5",
    author_email="nrbnlulu@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "django-phonenumber-field[phonenumbers]>=6.3.0",
    ],

    keywords="bugreport",
    zip_safe=False,
    include_package_data=True,
)
