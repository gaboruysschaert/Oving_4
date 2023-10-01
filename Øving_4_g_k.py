#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 01:22:59 2023

@author: gabrielruysschaert
"""

def calculate_trend(x_values, y_values):
    n = len(x_values)
    x_mean = sum(x_values) / n
    y_mean = sum(y_values) / n

    numerator = 0
    denominator = 0

    for i in range(n):
        x = x_values[i]
        y = y_values[i]
        numerator += (x - x_mean) * (y - y_mean)
        denominator += (x - x_mean) ** 2

    a = numerator / denominator
    b = y_mean - a * x_mean
    return a, b


x_bruker = input("skriv en liste med nummerer og mellomrom: ")
x_liste_bruker = [int(x) for x in x_bruker.split()]
y_bruker = input("skriv en liste med nummerer og mellomrom: ")
y_liste_bruker = [int(x) for x in y_bruker.split()]

a, b = calculate_trend(x_liste_bruker, y_liste_bruker)
print(f"Trenden i datasettet er gitt ved formelen verdi = {a}x + {b}.")

#k fra filen lsiter for del 1

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]

temperaturer_tidspunkter = list()

for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)
    

a, b = calculate_trend(temperaturer_tidspunkter, temperaturer)
if a > 0:
    print(f"Trenden i datasettet er gitt ved formelen verdi = {a}x + {b} og er stygende")
elif a < 0:
    print(f"Trenden i datasettet er gitt ved formelen verdi = {a}x + {b} og er synkende")
else: 
    print(f"Trenden i datasettet er gitt ved formelen verdi = {a}x + {b} og er ingen trend")
    
