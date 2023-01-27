#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# intro08.py – 27.01.2023

number_a = int(input("Entrez le nombre A : "))
number_b = int(input("Entrez le nombre B : "))

print(f"AVANT échange, A : {number_a}; B : {number_b}")

number_a, number_b = number_b, number_a

print(f"APRES échange, A : {number_a}; B : {number_b}")