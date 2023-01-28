#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PARENTE Samuel
# string06.py – 28.01.2023

sms = input("Entrez un SMS : ")

if sms[:2] == "lg":
    print("[Message destiné à la filiale liégeoise]: \n" + sms[2:])
elif sms[:2] == "bx":
    print("[Message destiné à la filiale bruxelloise]: \n" + sms[2:])
elif sms[:2] == "nm":
    print("[Message destiné à la filiale namuroise]: \n" + sms[2:])
else:
    print("Filiale inconnue")