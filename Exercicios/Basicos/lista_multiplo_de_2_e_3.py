"""23. Use compreensão de listas para criar uma lista com os múltiplos de 2 e 3 entre 0 e 20."""

lista23 = [x for x in range(21) if x  % 2 == 0 or x % 3 == 0]
print(f"\nQuestão 23 :\n{lista23}")