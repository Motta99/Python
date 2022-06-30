#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
28. Escreva um programa que gere um dicionário chamado contas contendo nome e saldo de n clientes de
um banco. Em seguida use a função map para gerar uma lista contendo o valor False para as contas
com saldo menor ou igual 1000.00 e True, caso contrário. Ou seja, verificar quais contas possuem mais
de 1000 reais, a expressão lambda deve retornar os booleanos para cada uma das contas.
"""

contas = {}
i = 0
n = int(input("Número de contas: "))

while i < n: 
    nome = input("\nDigite o nome do dono da conta: ")
    saldo = int(input("Digite o saldo da conta: "))
    
    contas[nome] = saldo
    i += 1

print("\n\n")   
print(contas.keys()) 
p = list(map((lambda x : x > 1000 for x in contas), contas.items()))
print(p)