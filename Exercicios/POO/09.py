class Funcionario(object):
  def __init__(self, nome, CPF, salario, departamento):
    self.nome = nome
    self.CPF = CPF
    self.salario = salario
    self.departamento = departamento
  
  def bonificar(self):
    self.salario = self.salario + (self.salario * 0.10)
 
class Gerente(Funcionario):
  def __init__(self, nome, CPF, salario, departamento, funcionariosGerenciados, senha):
    super().__init__(nome, CPF, salario, departamento)
    self.funcionariosGerenciados = funcionariosGerenciados
    self.senha = senha
 
  def bonificar(self):
    self.salario = self.salario + (self.salario * 0.15)
 
  def autenticarSenha(self, s):
    if self.senha == s:
      return True
    else:
      return False
