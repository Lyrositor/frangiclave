#!/usr/bin/env python

import io
import os

from setuptools import find_packages, setup

from ._version import __version__

REQUIRED = [
    'flask',
    'sqlalchemy',
    'toml'
]

EXTRAS = {
}

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='frangiclave',
    version=__version__,
    description='A modding tool for Cultist Simulator.',
    long_description=long_description,
    author='Lyrositor',
    python_requires='>=3.6.0',
    url='https://github.com/Lyrositor/frangiclave',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'flask',
        'sqlalchemy',
        'toml'
    ],
    extras_require={},
    include_package_data=True,
    license='CC0'
)
