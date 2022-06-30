#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Escreva um programa que pergunte a quantidade de km percorridos 
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais 
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por 
dia e R$ 0,15 por km rodado.
"""

diasCarro = int(input("Digite a quantidade de dias que você está com o carro: "));
kmPercorrido = float(input("Digite a quantidade de km's percorridos com o carro: "));

calculoPreco = diasCarro * 60 + kmPercorrido * 0.15;

print("\nO preço do aluguel é R$ %.2f" % calculoPreco);