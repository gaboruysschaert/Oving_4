#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:41:41 2023

@author: gabrielruysschaert
"""

def sum_større_5(liste):
    total = 0
    for num in liste:
        if num > 5:
            total += num - 5
    return total


grader_bruker =  input("skriv en liste med temperaturene og mellomrom: ")
grader_bruker_liste = [int(x) for x in grader_bruker.split()]
vokse_rate = sum_større_5(grader_bruker_liste)
print(f" planten vokste med {vokse_rate} for dager med temperatur høyere enn 5 grader")


#L

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
total_vekst = sum_større_5(temperaturer)
print(f" planten vokste med {total_vekst} for dager med temperatur høyere enn 5 grader")