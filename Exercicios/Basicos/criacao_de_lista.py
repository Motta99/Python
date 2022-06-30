""" 24. Use compreensão de listas para criar a seguinte lista: [(1,3),(1,2),(1,1),(2,3),(2,2),(2,1),(3,3),(3,2),(3,1)]."""

lista24 = [(x,y) for x in range(1,4) for y in [3,2,1]]
print(f"\nQuestão 24 :\n{lista24}")
