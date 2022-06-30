from datetime import datetime
 
class Pessoa(object):
  def __init__(self, nome, dataNascimento, altura):
    self.setNome(nome)
    self.setDataNascimento(dataNascimento)
    self.setAltura(altura)
 
  def setNome(self, nome):
    self.__nome = nome
 
  def setDataNascimento(self, dataNascimento):
    self.__dataNascimento = datetime.strptime(dataNascimento, "%d/%m/%Y")
 
  def setAltura(self, altura):
    self.__altura = altura
 
  def getNome(self):
    return self.__nome
 
  def getDataNascimento(self):
    return self.__dataNascimento
 
  def getAltura(self):
    return self.__altura
 
  def idade(self):
    return datetime.now().year - self.getDataNascimento().year
 
  def imprime(self):
    print(f"Nome: {self.getNome()}\nData de nascimento: {self.getDataNascimento()}\nAltura: {self.getAltura()} m\nIdade: {self.idade()} anos\n")
