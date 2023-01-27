#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# intro10.py – 27.01.2023

from math import sqrt

abs_a = int(input("Donnez l'abscisse du point A : "))
ord_a = int(input("Donnez l'ordonnée du point A : "))
abs_b = int(input("Donnez l'abscisse du point B : "))
ord_b = int(input("Donnez l'ordonnée du point B : "))

distance = sqrt((abs_a - abs_b) ** 2 + (ord_a - ord_b) ** 2)

print(f"La distance entre les points ({abs_a}, {ord_a}) et ({abs_b}, {ord_b}) est de {distance:.2f}.)")