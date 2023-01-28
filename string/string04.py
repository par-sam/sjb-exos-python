#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string04.py – 28.01.2023

string = input("Entrez une chaîne : ")
voyelles = "aeiouy"
voyelles_count = 0

for i in string:
    if i in voyelles:
        voyelles_count += 1

print(f"Il y a {voyelles_count} voyelles dans la chaîne")