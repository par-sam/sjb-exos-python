#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet06.py – 27.01.2023

factorielle = int(input("Calculer la factorielle de quel nombre ? "))

print(f"{factorielle}! = ", end="")
result = 1

for i in range(1, factorielle + 1):
    result *= i
    print(i, end="")
    if i != factorielle:
        print(".", end="")
    else:
        print(" = ", end="")

print(result)