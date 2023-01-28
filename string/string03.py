#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string03.py – 28.01.2023

string = input("Entrez une chaîne : ")
e_count = 0

for i in string:
    if i == "e":
        e_count += 1

print(f"Il y a {e_count} 'e' dans la chaîne")