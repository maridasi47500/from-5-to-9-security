import random, string

class Chaine:
    def __init__(self,x=""):
        self.chaine=x
    def fichier(self,oh):
        length=10
        letters = string.ascii_lowercase
        hey=''.join(random.choice(letters) for i in range(length))
        return hey+"."+oh.split(".")[-1]

