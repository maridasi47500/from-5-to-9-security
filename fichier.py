class Fichier:
  def __init__(self,path,name):
    self.path=path
    self.name=name
  def lire(self):
    print(self.path+"/"+self.name)
    j=open(self.path+"/"+self.name, "r")
    return j.read()
  def ligneparligne(self):
    j=open(self.path+"/"+self.name, "r")
    return j.readlines()
  def lirefichier(self):
    print(self.path+"/"+self.name)
    j=open(self.path+"/"+self.name, "rb")
    return j.read()
  def ecrire(self,mycontent):
    hey=open((self.path+"/"+self.name),"a")
    hey.write(mycontent)
    hey.close()
