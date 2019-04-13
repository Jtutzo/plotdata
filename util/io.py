#!/usr/bin/env python3.6
# coding: utf-8


import sys
import platform


class Color:
    HEADER = '\033[95m' if platform.system() != 'Windows' else ''
    BLUE = '\033[94m' if platform.system() != 'Windows' else ''
    GREEN = '\033[92m' if platform.system() != 'Windows' else ''
    RED = '\033[91m' if platform.system() != 'Windows' else ''
    OK = GREEN
    WARNING = '\033[93m' if platform.system() != 'Windows' else ''
    FAIL = RED
    ENDC = '\033[0m' if platform.system() != 'Windows' else ''
    BOLD = '\033[1m' if platform.system() != 'Windows' else ''
    UNDERLINE = '\033[4m' if platform.system() != 'Windows' else ''


def stderr(*args, **kwargs):
    kwargs['file'] = sys.stderr
    new_list = list(args)
    new_list.append(Color.ENDC)
    print(*tuple(new_list), **kwargs)
