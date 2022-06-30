#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
17. Faça um programa que solicite 20 números ao usuário, depois disso, exiba apenas os números maiores
do que 10. Utilize a função filter para fazer isso.
"""
lista = []

def filter(n):
     if n > 10: return n

for i in range(20):
    x = filter(int(input("Digite um número: ")))
    
    if x != None:
        lista.append(x)

print(f'\n{lista}')