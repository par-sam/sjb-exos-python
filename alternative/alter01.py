#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# alter01.py – 27.01.2023

nombre = int(input("Donnez un nombre compris entre 0 et 19 : "))

if nombre >= 0 and nombre <= 19:
    print("OK. Merci !")
else:
    print("ERREUR : le nombre devait être compris entre 0 et 19 inclus !")