class Agenda(object): 
  agenda = {}

  def armazenaPessoa(self, nome, idade, altura):
    self.nome = nome.strip()
    self.idade = idade
    self.altura = altura
    agenda[self.nome] = {"nome": self.nome, "idade": self.idade, "altura": self.altura}

  def removePessoa(self, nome):
    del agenda[nome]

  def buscaPessoa(self, nome):
    return list(agenda).index(nome) + 1

  def imprimeAgenda(self):
    print(agenda)   

  def imprimePessoa(self, index):
    i = 0

    if index > len(agenda) - 1 or index < 0:
      print("O indice escolhido não está na agenda")

    for key in agenda:
      if i == index:
        print(agenda[key])

      i += 1
