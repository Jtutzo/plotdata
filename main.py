#!/usr/bin/env python3.8
# coding: utf-8

import os
import re
import sys
import traceback

import matplotlib.pyplot as plt

from util import io
from util.io import Color

input_files = ['./demo.txt', 'demo.txt']
output_file = './demo.png'


class ReadFileError(RuntimeError):
    def __init__(self, message="File doesn't exist"):
        super().__init__(message)


def main():
    try:
        line_filtered = read_files(input_files)

        create_graph([float(i[1]) for i in line_filtered],
                     [float(i[2]) for i in line_filtered],
                     [float(i[4]) for i in line_filtered])
        return 0

    except RuntimeError as e:
        io.stderr(f"{Color.FAIL}{e}")
        return 1

    except:
        io.stderr(f"{Color.FAIL}{traceback.format_exc()}")
        return 1


def read_files(files):
    line_filtered = []
    for file in files:
        line_filtered += read_file(file)
    return line_filtered


def read_file(file):
    if file is None:
        file = input_files[0]
    if not os.path.exists(file):
        raise ReadFileError
    with open(file) as f:
        line_filtered = [re.split(r'\s+', line) for line in f if not line.startswith("#")]
    f.close()
    return line_filtered


def create_graph(x, y1, y2, file=output_file):
    plt.figure(figsize=(8, 6), dpi=160)
    plt.subplot(111)

    plt.plot(x, y1, color="blue", linewidth=1.0, linestyle="-")
    plt.plot(x, y2, color="red", linewidth=1.0, linestyle="-")

    plt.savefig(file, dpi=160)

    plt.show()


if __name__ == "__main__":
    sys.exit(main())
