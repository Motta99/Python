class Ingresso(object):
  def __init__(self, valor):
    self.valor = valor
 
  def imprimeIngresso(self):
    print(f"O valor do ingresso é {self.valor} R$")
 
class IngressoVIP(Ingresso):
  def __init__(self, v, adicional):
    super().__init__(v)
    self.valorVIP = self.valor + adicional
  
  def imprimeIngressoVIP(self):
    print(f"O valor do ingresso VIP é {self.valorVIP} R$")

i = IngressoVIP(20, 10)
i.imprimeIngressoVIP()
i.imprimeIngresso()
print(f"Diferença de preço: {i.valorVIP - i.valor} R$")
