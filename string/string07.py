#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string07.py – 28.01.2023

mot = input("Entrez un mot : ")

last_letter, doubles, voyelles = "", 0, "aeiouy"

for i in mot:
    if last_letter == i and i not in voyelles:
        doubles += 1
    last_letter = i

print(f"Le mot \"{mot}\" contient {doubles} consonnes doubles")