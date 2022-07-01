# -*- coding: utf-8 -*-
def pi(n):
    denominador = 1.0
    numerador = 4.0
    m = 1.0
    pi = 0.0
    for _ in range(n):
        pi += m * (numerador / denominador)
        m *= -1
        denominador += 2
        
    return pi
        
a = pi(100)
print(a)
