#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# training04.py – 28.01.2023

from math import sqrt

for i in range(16, 226):
    if sqrt(i) % 1 == 0:
        print(f"Carré parfait {i}; racine carrée {int(sqrt(i))}")
