#!/usr/bin/env python3
# coding: utf-8
from setuptools import setup, find_packages
from monte_carlo import __author__, __version__
 
setup(
        name             = 'monte carlo',
        version          = __version__,
        description      = 'Test program of Monte Carlo',
        #license          = __license__,
        author           = __author__,
        author_email     = 'ay65535@icloud.com',
        url              = 'https://github.com/ay65535/monte_carlo.git',
        keywords         = 'monte carlo pip github python python3',
        packages         = find_packages(),
        install_requires = [],
        )