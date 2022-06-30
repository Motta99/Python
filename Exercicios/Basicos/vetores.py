#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
12. Faça um programa que leia dois vetores com 10 elementos inteiros cada. Gere um terceiro vetor de 20
elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

v1 = []
v2 = []
v3 = []
n = 0
tam = 10

for i in range(tam): 
    v1.append(int(input("Digite um elemento para v1: ")))
    v2.append(int(input("Digite um elemento para v2: ")))
    
while n < tam:
    v3.append(v1[n])
    v3.append(v2[n])
    n += 1
    
print(f'\n{v3}')