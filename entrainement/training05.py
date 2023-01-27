#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# training05.py – 28.01.2023

from random import randrange

mult_3 = 0
mult_5 = 0
not_mult_3_5 = 0
impairs = 0

for i in range(100):
    nb = randrange(0, 100)

    if nb % 3 == 0:
        mult_3 += 1
    if nb % 5 == 0:
        mult_5 += 1
    if nb % 3 != 0 and nb % 5 != 0:
        not_mult_3_5 += 1

    if nb % 2 != 0:
        impairs += 1

print(f"""{impairs}% des 100 nombres tirés au hasard entre 0 et 99 inclus sont impairs

Statistiques
------------
* {mult_3}% des nombres tirés sont multiples de 3 ;
* {mult_5}% des nombres tirés sont multiples de 5 ;
* {not_mult_3_5}% des nombres tirés ne sont ni multiples de 3 ni multiples de 5.""")
