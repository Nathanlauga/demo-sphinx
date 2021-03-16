#! /usr/bin/env python
import os
from setuptools import setup, find_packages

DISTNAME = 'my_little_poney'

os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup(
    name=DISTNAME,
    packages=find_packages(),
    include_package_data=True
)
