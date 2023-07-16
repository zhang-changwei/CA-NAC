#!/usr/bin/env python

from distutils.core import setup

setup(
    name         = 'CA-NAC',
    version      = '0.2',
    description  = 'Concentric Approximation - Nonadiabatic Coupling.',
    author       = 'Weibin Chu',
    author_email = 'wbchu@mail.ustc.edu.cn',
    url          = 'https://github.com/WeibinChu/CA-NAC',
    py_modules   = [
        'abacuswfc', 'aeolap', 'CAnac',
        'hamnetwfc', 'mod_hungarian', 'siestawfc'
    ],
)