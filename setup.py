#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ini',
    description = 'parcer ini files',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'ConfigParser'
    ],
    entry_points='''
        [console_scripts]
        ini=ini.main:cli
    ''',
)