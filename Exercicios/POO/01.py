from datetime import datetime
 
class Jogador(object):
 
  def __init__(self, nome, posicao, dataNascimento, nacionalidade, altura, peso):
    self.setNome(nome)
    self.setPosicao(posicao)
    self.setDataNascimento(datetime.strptime(dataNascimento, "%d/%m/%Y"))
    self.setNacionalidade(nacionalidade)
    self.setAltura(altura)
    self.setPeso(peso)

  def setNome(self, c):
    self.nome = c
  
  def getNome(self):
    return self.nome

  def setPosicao(self, c):
    self.posicao = c
  
  def getPosicao(self):
    return self.posicao

  def setDataNascimento(self, c):
    self.dataNascimento = c
  
  def getDataNascimento(self):
    return self.dataNascimento

  def setNacionalidade(self, c):
    self.nacionalidade = c
  
  def getNacionalidade(self):
    return self.nacionalidade
  
  def setAltura(self, c):
    self.altura = c
  
  def getAltura(self):
    return self.altura

  def setPeso(self, c):
    self.peso = c
  
  def getPeso(self):
    return self.peso

  def calcIdade(self):
    return datetime.now().year - self.getDataNascimento().year
  
  def imprime(self):
    print(f"Nome: {self.getNome()}\nPosição: {self.getPosicao()}\nData de nascimento: {self.getDataNascimento()}\nNacionalidade: {self.getNacionalidade()}\nAltura: {self.getAltura()} m\nPeso: {self.getPeso()} kg\nIdade: {self.calcIdade()} anos\n")
    self.aposentadoria()
 
  def aposentadoria(self):
    if self.posicao == "defesa":
      print(f"Faltam {40 - self.calcIdade()} anos para você se aposentar")
 
    elif self.posicao == "ataque":
       print(f"Faltam {35 - self.calcIdade()} anos para você se aposentar")
 
    elif self.posicao == "meio-campo":
       print(f"Faltam {38 - self.calcIdade()} anos para você se aposentar")
 
    else:
      print("Você não escolheu uma posição válida")

play=Jogador("Antonio", "lateral", "20/02/2006", "brasileira", 1.75, 52)
play.imprime()
