from subprocess import check_output as runmyscript
class Executeprogram:
  def __init__(self,hey=""):
    self.hey="./uploads/"+hey
    if hey.endswith(".py"):
      self.someargs=["python3",self.hey]
    elif hey.endswith(".rb"):
      self.someargs=["ruby",self.hey]
    else:
      self.someargs=["python3",self.hey]
    self.runprogram=runmyscript
  def myargs(self,a):
    #print(a)
    for x in a:
        print("arg len",len(x))
    self.someargs=a
  def run(self):
    return runmyscript(self.someargs).decode()
    
