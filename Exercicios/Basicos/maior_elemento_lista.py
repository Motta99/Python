#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
29. Dada uma lista com n elementos. Use a função reduce para achar o maior elemento presente na lista.
Dica: use um condicional if na expressão lambda.
"""
from functools import reduce

lista = [1,2,3,4,5,6,74,8]
print(reduce((lambda x, y : x if x > y else y), lista))