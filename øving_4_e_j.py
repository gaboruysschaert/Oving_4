#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:42:25 2023

@author: gabrielruysschaert
"""

def beregn_diff(tall):
    differences = []
    for i in range(len(tall)-1):
        difference = tall[i+1] - tall[i]
        differences.append(difference)
    return differences


tall_bruker = input("skriv en liste med nummerer og mellomrom: ")
#gjør om fra string i input til integer ved å bruke for loop til å convertere 
#de nummer angitt fra en bruker til integer

tall_liste_bruker = [int(x) for x in tall_bruker.split()]

#kaller inn vår definerte funksjon som regner ut differansen
differences = beregn_diff(tall_liste_bruker)

#skriv ut resultat: 
    
print(f"Differansene mellom tallene i listen {tall_bruker} er {differences}")


#j
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]

ny_liste = beregn_diff(temperaturer)

def differanser(liste):
    diff_list = []
    for i in range(len(liste)-1):
        diff = liste[i+1] - liste[i]
        if diff > 0:
            print(f"Element {i}: stigende")
        elif diff < 0:
            print(f"Element {i}: synkende")
        else:
            print(f"Element {i}: uforandret")
        diff_list.append(diff)
    return diff_list

x = differanser(ny_liste)

