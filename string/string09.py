#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string09.py – 28.01.2023

from random import randrange

mot = input("Entrez un mot : ")
melange = ""

while len(mot) > 0:
    index = randrange(len(mot))
    melange += mot[index]
    mot = mot[:index] + mot[index + 1:]

print(melange)