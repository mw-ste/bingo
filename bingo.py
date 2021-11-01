#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:41:46 2021

@author: michi
"""

import os
import sys
import gtts
import random
import subprocess

print("Initialisierung")

with open("nouns.txt") as fid:
    words = fid.read().split()
random.shuffle(words)

word_dict = {
    "b" : [word for word in words if word.lower().startswith("b")],
    "i" : [word for word in words if word.lower().startswith("i")],
    "n" : [word for word in words if word.lower().startswith("n")],
    "g" : [word for word in words if word.lower().startswith("g")],
    "o" : [word for word in words if word.lower().startswith("o")]}

print()
print("b: {}\ni: {}\nn: {}\ng: {}\no: {}".format(
    len(word_dict["b"]),
    len(word_dict["i"]),
    len(word_dict["n"]),
    len(word_dict["g"]),
    len(word_dict["o"])))

numbers = list(range(1, 76))
random.shuffle(numbers)

input("Enter drücken zum Starten")
user_input = ""

while any(numbers) and not user_input == "c":
    value = numbers.pop()

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

    cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")

    number_audio = os.path.join(cache_dir, "{}.mp3".format(value))
    if not os.path.exists(number_audio):
        voice = gtts.gTTS(text = str(value), lang = "de")
        voice.save(number_audio)

    word = word_dict[char].pop()
    word_audio =  os.path.join(cache_dir, "{}.mp3".format(word.lower()))
    if not os.path.exists(word_audio):
        voice = gtts.gTTS(text = word, lang = "de")
        voice.save(word_audio)

    subprocess.run(["vlc", "--intf", "dummy", "--play-and-exit", word_audio], capture_output = True)
    subprocess.run(["vlc", "--intf", "dummy", "--play-and-exit", number_audio], capture_output = True)
    text = "{} {}".format(word, value)
    print(text)

    user_input = input("Weiter (\"c\" zum Beenden) ")

bingo = input("Bingo-Zahlen eingeben, mit Leerzeichen getrennt: ")
bingo = bingo.replace(",", " ")
bingo = bingo.split()
bingo = [int(b.strip()) for b in bingo]
if not len(set(bingo)) == 5:
    print("Ups, du hast {} Zahlen für dein Bingo eingegeben, aber es müssen genau 5 sein!".format(len(set(bingo))))
    sys.exit()

missing_numbers = [b for b in bingo if b in numbers]

if any(missing_numbers):
    missing_numbers = [str(m) for m in missing_numbers]
    print("Ups, die folgenden Zahlen wurden noch nicht aufgerufen: {}".format(str.join(", ", missing_numbers)))
else:
    print("Glückwunsch zum Bingo!")