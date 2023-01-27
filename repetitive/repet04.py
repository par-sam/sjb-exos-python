#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# repet04.py – 27.01.2023

from random import randrange

print("Tirage d'un nombre aléatoire entre 1 et 6.")
aleat = randrange(1, 7)
guess = int(input("Devinez le nombre tiré: "))
attempts = 1

while guess != aleat:
    guess = int(input("Ce nombre ne correspond pas, devinez encore : "))
    attempts += 1

print(f"Vous avez deviné le nombre {aleat} en {attempts} coups !")