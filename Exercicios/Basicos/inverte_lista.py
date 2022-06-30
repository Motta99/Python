#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
13. Programa que leia do teclado uma lista e inverta esta lista sem usar funções pré-definidas.
"""

lista = []
tam = 5

for i in range(tam):
    lista.append(int(input("Digite um valor: ")))
    
listaInvertida = lista.copy()

for i in range(tam):
    listaInvertida[tam-1] = lista[i]
    tam -= 1
    
print(f'\n{lista}\n\n{listaInvertida}\n')
