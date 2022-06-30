#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9. Escreva um programa que dado um número natural na base decimal, transformá-lo para a base binária.
Exemplo: Dado 18 a saída deverá ser 10010.
"""

n = int(input("Digite um número natural: "))
lista = []
contador = 0
div = 0

while contador == 0:
    div = n // 2
    lista.append(n % 2) 
    n = div
    
    if n == 0:
        contador = 1
        
for i in lista[::-1]:
    print(i, end=(""))
