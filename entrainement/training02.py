#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# training02.py – 28.01.2023

for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
