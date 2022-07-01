# -*- coding: utf-8 -*-
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)

a = fibo(10)
print(a)