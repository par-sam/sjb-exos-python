#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string13.py – 28.01.2023

chaine = input("Entrez une chaîne : ")
last_letter = ""

for i in chaine:
    if i != last_letter:
        print(i, end="")
    last_letter = i
