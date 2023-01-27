#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet01.py – 27.01.2023

table = int(input("Quelle table de multiplication désirez-vous afficher ? "))

print(f"Table de multiplication par {table}")

for i in range(20):
    print(i + 1, "x", table, "=", (i + 1) * table)

print("Terminé !")