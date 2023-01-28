#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string02.py – 28.01.2023

string = input("Entrez une chaîne : ")

i = len(string) - 1

while i >= 0:
    print(string[i], end=" ")
    i -= 1