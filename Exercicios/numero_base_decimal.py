#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
8. Escreva um programa que dado um número natural na base binária, transformá-lo para a base decimal.
Exemplo: Dado 10010 a saída será 18, pois 1.2^4 + 0.2^3 + 0.2^2 + 1.2^1 + 0.2^0 = 18.
"""
from math import pow

n = input("Digite um número natural na base binária: ")
soma = 0
contador = 0

for i in n:
    x = int(i)
    soma += x * pow(2, len(n)-1 - contador)
    contador += 1

print(f'\nO número em base decimal é: {soma}')
    
