#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='nanoqc',
    version='0.0.1',
    packages=find_packages(),
    scripts=['nanoqc/nanoQC.py'],
    author='Marc-Olivier Duceppe',
    author_email="andrew.low@canada.ca",
    url='https://github.com/lowandrew/nanoQC',
    install_requires=['numpy',
                      'matplotlib',
                      'pandas',
                      'seaborn',
                      'sklearn',
                      'pytest']
)
