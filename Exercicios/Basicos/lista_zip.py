#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
30. Crie uma lista de tuplas em que o primeiro elemento da tupla será o índice o segundo o índice ao
quadrado, faça isso de 0 a 9 e use zip().
"""

t = (range(10))
a = (map(lambda x: x** 2, t))

x = list(zip(t, a))
    
print(x)