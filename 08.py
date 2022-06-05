class ingresso(object):
  def __init__(self, valor):
    self.valor = valor
 
  def imprimeIngresso(self):
    print(f"O valor do ingresso é {self.valor} R$")
 
 
class IngressoVIP(ingresso):
  def __init__(self, valor, adicional):
    super().__init__(valor)
    self.valorVIP = self.valor + adicional
  
  def imprimeIngressoVIP(self):
    print(f"O valor do ingresso VIP é {self.valorVIP} R$")
 
 
class Normal(ingresso):
  def __init__(self, valor):
    super().__init__(valor)
 
  def imprime(self):
    print("Ingresso normal")
 
 
class CamaroteInferior(IngressoVIP):
  def __init__(self, localizacao, valor, adicional):
    super().__init__(valor, adicional)
    self.localizacao = localizacao
  
  def imprimeLocalizacao(self):
    print(f"A localização é {self.localizacao}")
  
  def imprime(self):
    print("Camarote inferior")
 
 
class CamaroteSuperior(IngressoVIP):
  def __init__(self, valor, adicional):
    super().__init__(valor, adicional)
 
  def imprime(self):
    print("Camarote superior")
 
x = int(input("Digite 1 para ingresso normal e 2 para vip: "))
if x == 1:
  ingresso = Normal(15)
  ingresso.imprime()
  ingresso.imprimeIngresso()
 
elif x == 2:
  x = int(input("Digite 1 para camarote superior e 2 para camarote inferior: "))
  
  if x == 1:
    ingresso = CamaroteSuperior(15, 10)
    ingresso.imprime()
    ingresso.imprimeIngressoVIP()
 
  elif x == 2:
    ingresso = CamaroteInferior("pista", 15, 5)
    ingresso.imprime()
    ingresso.imprimeIngressoVIP()
    ingresso.imprimeLocalizacao()
 
else:
  print("Digite um valor válido")