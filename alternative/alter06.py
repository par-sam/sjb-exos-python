#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# alter06.py – 27.01.2023

val_a = int(input("Entrez la valeur associée à A : "))
val_b = int(input("Entrez la valeur associée à B : "))
val_c = int(input("Entrez la valeur associée à C : "))

print(f"Les valeurs non triées : A(={val_a}), B(={val_b}), C(={val_c})")

if val_a > val_b:
    val_a, val_b = val_b, val_a

if val_b > val_c:
    val_b, val_c = val_c, val_b

if val_a > val_b:
    val_a, val_b = val_b, val_a

print(f"Les valeurs triées : A(={val_a}), B(={val_b}), C(={val_c})")