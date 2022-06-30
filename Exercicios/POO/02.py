class Conta(object):
  def __init__(self, nome, valor):
    self.__nome = nome
    self.__valor = valor
 
  def __add__(self, outro):
    novo_nome = self.__nome + " e " + outro.__nome
    novo_valor = self.__valor + outro.__valor
    ret = Conta(novo_nome, novo_valor)
    return(ret)
 
  def __repr__(self):
    return("titular: "+self.__nome+" - saldo: "+repr(self.__valor))
 
  def sacar(self, saq):
    self.__valor = self.__valor - saq
 
  def depositar(self, deposito):
    self.__valor = self.__valor + deposito
 
  def getSaldo(self):
    return self.__valor

  def imposto(self, v):
    self.__valor -= self.__valor * v
 
class ContaImposto(Conta):
  def __init__(self, nome, valor, percentualImposto):
    super().__init__(nome, valor)
    self.percentualImposto = percentualImposto
 
  def calcularImposto(self):
    super().imposto(self.percentualImposto)
 
c = ContaImposto("João", 5000, 0.4)
print(c)
c.sacar(2500)
print(c)
c.depositar(10000)
print(c)
c.calcularImposto()
print(c)
