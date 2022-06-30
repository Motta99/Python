""" 27. Use compreensão de conjuntos para criar um conjunto que, a partir de uma string dada, retorne
tuplas com dois valores em que o primeiro valor é um caracter da string dada e o segundo o índice
correspondente do caracter na string."""

s = "Pedro"
s2 = {(letra, s.index(letra)) for letra in s}
print(f"\nQuestão 27 :\n{s2}")
