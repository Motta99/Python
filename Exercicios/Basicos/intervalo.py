#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
11. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar
quando for lido um número negativo.
"""
lista, a, b, c, d = [], [], [], [], []
x = 0

while x >= 0:
    x = int(input("Digite um número: "))
    lista.append(x)
    
for i in lista:
    if i >= 0 and i <= 25:
        a.append(i)   
        
    elif i >= 26 and i <= 50:
        b.append(i)
        
    elif i >= 51 and i <= 75:
        c.append(i)
        
    elif i >= 76 and i <= 100:
        d.append(i)
        
print(f'\nExistem {len(a)} elementos de [0-25], e os elementos são: {a}\n\nExistem {len(b)} elementos de [26-50], e os elementos são: {b}\n\nExistem {len(c)} elementos de [51-75], e os elementos são: {c}\n\nExistem {len(d)} elementos de [76-100], e os elementos são: {d}\n')
