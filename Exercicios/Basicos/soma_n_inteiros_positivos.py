#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
20. Escreva um programa que leia um número inteiro positivo n. Chame uma função que recebe o n lido
e calcula e retorna a soma dos n primeiros números inteiros positivos.
"""

def soma(l):
    s = 0
    
    for i in range(1, int(input("Somar os primeiros: "))):
        s = l[i] + s
    
    return s

lista = []

for i in range(int(input("Digite a quantidade de números: "))):
    x = int(input("Digite um número: "))
    
    if x > 0:
        lista.append(i)
        
print(soma(lista))