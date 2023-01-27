#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet05.py – 27.01.2023

notes = int(input("Combien de notes à entrer ? "))
somme = 0

for i in range(notes):
    somme += int(input(f"Entrez la note no {i + 1} : "))

print(f"La somme de ces notes est de {somme}. La moyenne est de {somme / notes:.1f}")