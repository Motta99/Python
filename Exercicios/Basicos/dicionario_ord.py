""" 25. Use compreensão de dicionários para criar um dicionário que utilize como chave as letras de uma string
dada e use como valor o número inteiro que representa o código ASCII de determinado caracter. Use
a função ord."""

d = "Python é melhor do que C"
d2 = {letra:ord(letra) for letra in d}
print(f"\nQuestão 25 :\n{d2}")