class Televisao(object):
  def volume(self, volume):
    if self.volume == 0 and volume == -1:
      self.volume = 0
 
    else:
      self.volume += volume
 
  def canal(self, canal):
    if self.canal == 1 and canal == -1:
      self.canal = 1
 
    else:
      self.canal += canal
 
  def canalDireto(self, canal):
    self.canal = canal
  
  def getCanal(self):
    return self.canal
 
  def getVolume(self):
    return self.volume
 
class ControleRemoto(Televisao):
  def __init__(self):
    self.canal = 1
    self.volume = 0
 
  def aumentarVolume(self):
    super().volume(1)
 
  def diminuirVolume(self):
    super().volume(-1)
 
  def aumentarCanal(self):
    super().canal(1)
 
  def diminuirCanal(self):
    super().canal(-1)
 
  def setCanal(self, c):
    super().canalDireto(c)
  
  def consulta(self):
    print(f"O volume da televisão é {super().getVolume()} e está no canal {super().getCanal()}")
