#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string11.py – 28.01.2023

lettre = input("Entrez une lettre de l'alphabet : ")
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alpha)):
    if lettre == alpha[i]:
        print(f"La lettre '{lettre}' est la {i + 1}e lettre de l'alphabet.")

# J'avais ajouté une ternaire pour mettre "ere" si c'est la 1ere lettre mais ce n'est pas obligatoire
# "ere" if i == 0 else "e"