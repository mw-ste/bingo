#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:57:09 2021

@author: michi
"""

# In[]
nouns = []

with open("nouns.csv") as fid:
    line = fid.readline()
    line = fid.readline()
    while line:
        elements = line.split(",")
        if elements[1] == "Substantiv" and all([e.isalpha() for e in elements[0]]):
            nouns.append(elements[0])
        
        line = fid.readline()
        
print(len(nouns))


# In[]
with open("nouns.txt", "w") as fid:
    for noun in nouns:
        fid.write("{}\n".format(noun))
