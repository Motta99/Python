#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
19. Dado o conjunto de palavras [“fila”, “Adriana”, “armário”, “gaveta”, “Ana”,“avião”, “faca”, “impressora”],
monte um filtro que remove todas as palavras que comecem com “A” ou “a”.
"""

lista = ["fila", "Adriana", "armário", "gaveta", "Ana", "avião", "faca", "impressora"]

def filter(n):
     if n[0] == "A":
         return 1
     
     elif n[0] == "a":
         return 1
     
     else:
         return 0
     
for i in lista:
    if filter(i) != 0:
        lista.remove(i)
        
print(lista)