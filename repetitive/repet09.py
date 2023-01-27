#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet09.py – 27.01.2023

dividende = int(input("Donner le dividende : "))
diviseur = int(input("Donner le diviseur : "))
quotient = 0
reste = dividende

while reste >= diviseur:
    reste -= diviseur
    quotient += 1

print(f"{dividende} = {diviseur} x {quotient} + {reste}")