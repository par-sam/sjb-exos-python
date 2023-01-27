#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# training01.py – 28.01.2023

note = int(input("Donnez une note (-1 pour terminer) : "))

maxi, mini = note, note
nbMaxi, nbMini = 0, 0

while note != -1:
    if note > maxi:
        maxi = note
        nbMaxi = 1
    elif note == maxi:
        nbMaxi += 1

    if note < mini:
        mini = note
        nbMini = 1
    elif note == mini:
        nbMini += 1

    note = int(input("Donnez une note (-1 pour terminer) : "))

print(f"Note maximale : {maxi} attribuée {nbMaxi} fois")
print(f"Note minimale : {mini} attribuée {nbMini} fois")
