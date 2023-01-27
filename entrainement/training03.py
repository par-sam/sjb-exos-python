#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# training03.py – 28.01.2023

for i in range(1, 31):
    div_two = "** " if i % 2 == 0 else ""
    div_three = "***" if i % 3 == 0 else ""
    print(str(i) + " " + div_two + div_three)
