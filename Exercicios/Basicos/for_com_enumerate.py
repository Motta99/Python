#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
31. Use a função enumerate() para a partir de uma string dada imprimir uma tupla em que o primeiro
elemento é um caracter da string maiúsculo e o outro elemento é o índice do caracter.
"""
l = "pedro"
for index, item in enumerate("pedro"):
    print(item.upper(), ':', index)