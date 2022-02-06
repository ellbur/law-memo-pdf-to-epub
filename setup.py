#!/usr/bin/env python3

from setuptools import setup

setup(
    name       = 'law-memo-pdf-to-epub',
    version    = '1.0',
    py_modules = [],
    scripts    = ['law-memo-pdf-to-epub'],
    install_requires = ['pdfminer.six', 'ebooklib']
)

