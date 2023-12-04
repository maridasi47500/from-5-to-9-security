class Chaine:
  def __init__(self,hey):
    self.chaine=hey
  def minuscules(self):
    return lower(self.chaine)
  def premiere_lettre_capitale(self):
    return capitalize(lower(self.chaine))
  def majuscules(self):
    return upper(self.chaine)
  def faire_une_liste_avec_caractere(self,caracter):
    return self.chaine.split(caracter)
