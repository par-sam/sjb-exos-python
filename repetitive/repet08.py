#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet08.py – 27.01.2023

lignes = int(input("Combien de lignes ? "))

print("Triangle Rectangle :")

for i in range(lignes):
    print("*" + "**" * i)

print("Triangle Isocèle")

for i in range(lignes):
    print(" " * (lignes - i - 1) + "*" * (2 * i + 1))

print("Triangle Isocèle Vide (fait au test)")

for i in range(lignes):
    print(" " * (lignes - i - 1) + "*" + ("*" if i == lignes - 1 else " ") * (2 * i - 1) + "*" * (i != 0))