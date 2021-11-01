#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:41:46 2021

@author: michi
"""

import gtts
import time
import random
import subprocess

with open("nouns.txt") as fid:
    nouns = fid.read().split()
random.shuffle(nouns)

b_s = []
i_s = []
n_s = []
g_s = []
o_s = []

print("Initialisierung")

words = nouns
b_s = [word for word in words if word.lower().startswith("b")] + b_s
i_s = [word for word in words if word.lower().startswith("i")] + i_s
n_s = [word for word in words if word.lower().startswith("n")] + n_s
g_s = [word for word in words if word.lower().startswith("g")] + g_s
o_s = [word for word in words if word.lower().startswith("o")] + o_s

print("b: " + str(len(b_s)) + 
      "\ni: " + str(len(i_s)) + 
      "\nn: " + str(len(n_s)) + 
      "\ng: " + str(len(g_s)) + 
      "\no: " + str(len(o_s)))
    
word_dict = {
    "b" : b_s,
    "i" : i_s,
    "n" : n_s,
    "g" : g_s,
    "o" : o_s}

numbers = list(range(1, 76))

input("Start")
while any(numbers):
    pos = random.randint(0, len(numbers) - 1)
    value = numbers[pos]
    numbers.remove(value)
    
    if value > 0 and value <= 15: 
        char = "b"
    if value > 15 and value <= 30:
        char = "i"
    if value > 30 and value <= 45:
        char = "n"
    if value > 45 and value <= 60:
        char = "g"
    if value > 60 and value <= 75:
        char = "o"
        
    word = word_dict[char].pop()    
    text = "{} {}".format(word, value) 
    
    obj = gtts.gTTS(text = text, lang = "de")
    obj.save("bingo.mp3")
    time.sleep(1)
    
    subprocess.run(["vlc", "--intf", "dummy", "bingo.mp3", "--play-and-exit"], capture_output = True)
    print(text)
    
    input("Weiter")
