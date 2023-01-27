#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# intro09.py – 27.01.2023

prix_ht = float(input("Donnez le prix hors taxe : "))
kilos = float(input("Donnez le nombre de kilos achetés : "))
taux_tva = float(input("Donnez le montant de la T.V.A (en %) : "))

prix_ttc = prix_ht * (1 + taux_tva / 100) * kilos

print(f"Le prix TTC est de {prix_ttc} €.")