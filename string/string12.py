#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string12.py – 28.01.2023

chaine = input("Entrez une chaîne : ")
decal = int(input("Entrez un décalage : "))

for i in chaine:
    print(chr(ord(i) + decal), end="")