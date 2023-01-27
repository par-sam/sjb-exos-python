#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet02.py – 27.01.2023

nombre = int(input("Donner le nombre de départ : "))

result = ""

for i in range(12):
    result += str(nombre) + " "
    nombre *= 3

print(result)