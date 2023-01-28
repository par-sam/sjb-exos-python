#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string10.py – 28.01.2023

string = input("Entrez une chaîne : ")

print("La chaîne a une taille " + ("paire" if len(string) % 2 == 0 else "impaire") + f" ({len(string)})")

if len(string) % 2 == 0:
    print("Les caractères d'indice pair sont : " + ", ".join(string[::2]))
else:
    print("Les caractères d'indice impair sont : " + ", ".join(string[1::2]))