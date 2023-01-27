#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# alter04.py – 27.01.2023

nombre = int(input("Entrez un nombre quelconque : "))

if nombre > 0:
    print(f"Le nombre {nombre} est positif.")
elif nombre < 0:
    print(f"Le nombre {nombre} est négatif.")
else:
    print(f"Vous avez entré zéro!")