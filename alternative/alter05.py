#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# alter05.py – 27.01.2023

val_a = int(input("Entrez la valeur associée à A : "))
val_b = int(input("Entrez la valeur associée à B : "))
val_c = int(input("Entrez la valeur associée à C : "))

if val_a > val_b and val_a > val_c:
    print(f"La valeur la plus grande se trouve dans A.")
elif val_b > val_a and val_b > val_c:
    print(f"La valeur la plus grande se trouve dans B.")
else:
    print(f"La valeur la plus grande se trouve dans C.")