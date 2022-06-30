#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
16. Dizemos que um inteiro positivo n é perfeito se for igual à soma de seus divisores positivos diferentes
de n.
Exemplo: 6 é perfeito, pois 1 + 2 + 3 = 6.
Escreva um programa que dado um inteiro positivo n, verificar se n é perfeito.
"""

x = int(input("Digite um número: "))

lista = []

for i in range(1, x):
    if x % i == 0:
        lista.append(i)

soma = sum(lista)

if soma == x:
    print("O número é perfeito")  
    
else:
    print("O número não é perfeito")