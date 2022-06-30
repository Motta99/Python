""" 26. Crie um dicionário com nomes como chave e número de telefone como valor. Em seguida, use compre-
ensão de dicionários para criar um novo dicionário de contatos a partir do dicionário criado, mas que
adicione um 9 no início de cada valor."""

lista = {"Pedro":"800432", "Maria":"882346", "Julia":"324789", "João":"987346"}
l = {key: "9" + value for key, value in lista.items()}
print(f"\nQuestão 26 :\n{l}")