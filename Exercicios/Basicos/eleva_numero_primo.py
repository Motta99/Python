#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C22. Crie uma função para verificar se um número é primo. Use a função range para criar uma lista com
valores de 0 a 30. A partir dessa lista, use compreensão de listas para criar uma nova lista que eleva o
número ao quadrado se ele é primo e imprime o número caso contrário.
"""

def primo(n):
    somaPrimo = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            somaPrimo += 1
    
    if somaPrimo == 2:
        return n
    
lista = [x * x if primo(x) == x else x for x in list(range(31))]
print(lista)
            
