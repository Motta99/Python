#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10. Escreva um programa para ler o número de 
termos da série (N) e imprimir o valor de S, sendo
"""

N = int(input("Digite um número: "))
S = 0

for i in range(N+1):
    S += (N - (N - i)) / (N - (i - 1))
    

print(S)
    