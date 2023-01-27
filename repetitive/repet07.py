#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet07.py – 27.01.2023

termes = int(input("Suite de Fibonacci, combien de termes voules-vous afficher ? "))
u1 = 1
u2 = 1

print(u1, u2, end=" ")

for i in range(termes - 2):
    u1, u2 = u2, u1 + u2
    print(u2, end=" ")