#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
14 - Faça um programa para imprimir:
1
2 2
3 3 3
. . .
n n n n n n . . . n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a
n-ésima linha.
"""

def imprime(x):
    for i in range(x+1):
        for j in range(i):
            print(f"{i}", end=(" "))
        print(end=("\n"))
        
numero = int(input("Digite um número: "))
imprime(numero)


