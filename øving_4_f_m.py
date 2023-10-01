#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:30:13 2023

@author: gabrielruysschaert
"""

def finn_zero(liste):
    max_lengde = 0
    lengde_1 = 0
    for x in liste:
        if x == 0:
            lengde_1 += 1
            max_lengde = max(max_lengde,lengde_1)
        else:
            lengde_1 = 0
    return max_lengde

tall_bruker = input("skriv en liste med nummerer og mellomrom: ")
tall_liste_bruker = [int(x) for x in tall_bruker.split()]

lengste_sekvens = finn_zero(tall_liste_bruker)
print(f"Lengden til den lengste sammenhengende sekvensen av nuller i listen er {lengste_sekvens}.")


#m
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
lengste_periode = finn_zero(dogn_nedbor)
print(f"den lengste perioden uten nedbør var {lengste_periode} dager")