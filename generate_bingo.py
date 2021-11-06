#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 10:21:54 2021

@author: michi
"""

import random


numbers = list(range(1, 76))
random.shuffle(numbers)

b = [v for v in numbers if (v >  0 and v <= 15)][0:5]
i = [v for v in numbers if (v > 15 and v <= 30)][0:5]
n = [v for v in numbers if (v > 30 and v <= 45)][0:5]
g = [v for v in numbers if (v > 45 and v <= 60)][0:5]
o = [v for v in numbers if (v > 60 and v <= 75)][0:5]

n[2] = ""

def print_line():
    print("|----|----|----|----|----|")

def print_bold_line():
    print("|====|====|====|====|====|")


def print_numbers(index):
    print("| {: >2} | {: >2} | {: >2} | {: >2} | {: >2} |".format(
        b[index], i[index], n[index], g[index], o[index]))

print()
print_bold_line()
print("|  B |  I |  N |  G |  O |")
print_bold_line()
print_numbers(0)
print_line()
print_numbers(1)
print_line()
print_numbers(2)
print_line()
print_numbers(3)
print_line()
print_numbers(4)
print_bold_line()
print()
