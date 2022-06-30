from random import randint
from random import randrange

lista = []
x = 0

while x < 39:

    num = randrange(start=1, stop=13, step=2)

    if (num in lista):

        x = x - 1

    else:

        lista.append(num)

    x = x + 1

print(sorted(lista))