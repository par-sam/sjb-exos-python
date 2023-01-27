#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# intro04.py – 27.01.2023

secondes = int(input("Donner un nombre (en secondes) : "))
secondes_initiales = secondes

minutes = secondes // 60
secondes = secondes % 60
heures = minutes // 60
minutes = minutes % 60
jours = heures // 24
heures = heures % 24

print(f"{secondes_initiales} secondes = {jours} jour(s) {heures} heure(s) {minutes} minute(s) {secondes} seconde(s)")

# On peut éventuellement faire une ternaire pour ajouter ou non le "s" en fin de mot
# Exemple: print(f"{secondes_initiales} seconde{"s" if secondes_initiales > 1 else ""}")