#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet10.py – 27.01.2023

nombre = int(input("Donner un nombre : "))
puissance = int(input("Donner une puissance : "))
result = 1

for i in range(puissance):
    result *= nombre

print(f"Le résultat de {nombre}^{puissance} = {result}")