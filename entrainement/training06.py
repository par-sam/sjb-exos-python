#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# training06.py – 28.01.2023

first = int(input("Entrez un premier nombre : "))
second = int(input("Entrez un second nombre : "))

print(
    f"Le PGCD de {first} et de {second} à l'aide de l'algorithme d'Euclide :")

if first < second:
    first, second = second, first

print(f"""{first} = {second} x {first // second} + {first % second}
{second} = {first % second} x {second // (first % second)} + {second % (first % second)}
{first % second} = {second % (first % second)} x {first % second // (second % (first % second))} + {first % second % (second % (first % second))}
PGCD({first} ; {second}) =  {second % (first % second)}.""")
