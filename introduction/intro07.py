#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# intro07.py – 27.01.2023

number_one = int(input("Entrer un nombre : "))
number_two = int(input("Entrer un nombre : "))
number_three = int(input("Entrer un nombre : "))
number_four = int(input("Entrer un nombre : "))
number_five = int(input("Entrer un nombre : "))

print(f"La moyenne des 5 nombres entrés est de {(number_one + number_two + number_three + number_four + number_five) / 5}")

# Ici on attend de nous que l'on utilise 5 variables mais j'aurais plutôt utilisé une liste et une boucle for comme ici:

# numbers = []
# for i in range(5):
#     numbers.append(int(input("Entrer un nombre : ")))
#
# print(f"La moyenne des 5 nombres entrés est de {sum(numbers) / len(numbers)}")