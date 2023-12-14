from subprocess import check_output as runmyscript
class Myprogram:
  def __init__(self,hey=""):
    self.hey=hey
    self.someargs=[hey]
    self.runprogram=runmyscript
  def myargs(self,a):
    #print(a)
    for x in a:
        print("arg len",len(x))
    self.someargs=a
  def run(self):
    runmyscript(self.someargs)
    
