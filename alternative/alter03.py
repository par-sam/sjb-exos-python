#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# alter03.py – 27.01.2023

nombre = int(input("Donner un nombre entier : "))

if nombre % 3 == 0 and nombre % 2 == 0:
    print(f"Le nombre {nombre} est multiple de 2 et 3 ({nombre} = 2 * {nombre // 2} et {nombre} = 3 * {nombre // 3}).")
elif nombre % 3 == 0:
    print(f"Le nombre {nombre} est multiple de 3 ({nombre} = 3 * {nombre // 3}).")
elif nombre % 2 == 0:
    print(f"Le nombre {nombre} est multiple de 2 ({nombre} = 2 * {nombre // 2}).")
else:
    print(f"Le nombre {nombre} n'est ni multiple de 2 ni multiple de 3.")