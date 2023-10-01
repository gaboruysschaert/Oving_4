#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:25:27 2023

@author: gabrielruysschaert
"""

#d)

def count_tall(numbers, value):
    count = 0
    for number in numbers:
        if number >= value:
            count += 1
    return count


numbers = [1.5, 2.7, 4, 7, 9, 15, 12]
value = 3.0

result = count_tall(numbers, value)
print(f"Antall elementer i listen som er større enn eller lik {value}: {result}")

#i lager ny variabler med data fra lista_files

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]

sommerdager = count_tall(temperaturer, 20)
print(f"Antall sommerdager med temperaturer over {20}: {sommerdager}")

hoy_sommerdager = count_tall(temperaturer, 25)
print(f"Antall sommerdager med temperaturer over {25}: {hoy_sommerdager}")

trope_dager = count_tall(temperaturer, 30)
print(f"Antall sommerdager med temperaturer over {30}: {trope_dager}")