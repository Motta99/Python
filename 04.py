class Elevador(object):
  def setTotalAndares(self, andares):
    self.totalAndares = andares
  
  def getTotalAndares(self):
    return self.totalAndares

  def setAndarAtual(self, andar):
    self.andarAtual = andar

  def getAndarAtual(self):
    return self.andarAtual
  
  def getTotalAndares(self):
    return self.andarAtual

  def setCapacidade(self, capacidade):
    self.capacidade = capacidade
  
  def getCapacidade(self):
    return self.capacidade

  def setQuantidadePessoasElevador(self, qtd):
    self.quantidadePessoasElevador = qtd
  
  def getQuantidadePessoasElevador(self):
    return self.quantidadePessoasElevador
  
  def inicializar(self, totalAndares, capacidade):
    self.setAndarAtual(0)
    self.setTotalAndares(totalAndares)
    self.setCapacidade(capacidade)
    self.setQuantidadePessoasElevador(0)
 
  def entrar(self):
    if self.quantidadePessoasElevador < self.capacidade:
      self.quantidadePessoasElevador += 1
    else:
      print("Elevador lotado\n")
  
  def sair(self):
    if self.quantidadePessoasElevador > 0:
      self.quantidadePessoasElevador -= 1
    else:
      print("Elevador vazio\n")
 
  def subir(self):
    if self.andarAtual != self.totalAndares:
      self.andarAtual += 1
    else:
      print("O elevador está no último andar\n")
 
  def descer(self):
    if self.andarAtual != 0:
      self.andarAtual -= 1
    else:
      print("O elevador está no térreo\n")
 
  def imprime(self):
    print(f"Andar atual: {self.getAndarAtual()}\nTotal andares: {self.getTotalAndares()}\nQuantidade de pessoas: {self.getQuantidadePessoasElevador()}\nCapacidade: {self.getCapacidade()}\n")

