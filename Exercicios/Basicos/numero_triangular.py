#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
21. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120.
Escreva um programa que leia um inteiro não-negativo n, verifique se n é triangular.
"""
n = int(input("Digite um número: "))
i = 1

while i < n:
    prod = i * (i+1) * (i+2)
    
    if prod == n:
        print(f"\n{n} é triangular, pois {i}.{i+1}.{i+2} = {n}.")
        break
    
    elif prod > n:
        print("\nO número não é triangular")
        break
    
    i += 1;