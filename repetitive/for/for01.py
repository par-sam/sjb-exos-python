#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# for01.py – 27.01.2023

nombre = int(input("Entrer un nombre compris entre 0 et 20 non inclus : "))

if nombre < 0 or nombre >= 20:
    print("Nombre invalide")
else:
    for i in range(20):
        print(f"{i+1} x {nombre} = {(i+1) * nombre}")