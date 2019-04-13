#!/usr/bin/env python3.6

import sys

from cx_Freeze import setup, Executable

name = "plotdata"
version = "1.0.0"
auteur = "jtutzo"
description = ""
directory = "bin"

executables = [Executable('main.py', targetName=name)]
additional_mods = ['matplotlib.backends.backend_tkagg', 'numpy.core._methods', 'numpy.lib.format']

packages = ["idna"]

options = {
    'build_exe': {
        'path': sys.path,
        'build_exe': directory,
        'packages': packages,
        'include_files': 'demo.txt',
        'includes': additional_mods,
    },
}

setup(
    name=name,
    options=options,
    version=version,
    description=description,
    auteur=auteur,
    executables=executables,
    requires=['cx_Freeze']
)
