#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Escreva um programa para calcular a redução do tempo de vida de 
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos 
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, 
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

cigarroDia = int(input("Digite quantos cigarros você fuma por dia: "))
anosFumados = int(input("Digite há quantos anos você fuma: "))

mataFumante = ( (cigarroDia * 10) * (anosFumados * 365) ) / 1440

print("\nVocê perdeu %.2f dias de vida" % mataFumante)