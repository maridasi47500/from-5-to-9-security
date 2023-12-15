import re
import os
import traceback
from artist import Artist
from song import Song
from cado import Cado
from gagnant import Gagnant
from jeu import Jeu
import sys
class RenderFigure():
    def __init__(self,program):
        self.session={"name":"","notice":"","mysession":False}
        self.mytemplate="./mypage/index.html"
        self.path=program.get_path()
        self.title=program.get_title()
        self.dbCado=Cado()
        self.dbJeu=Jeu()
        self.dbSong=Song()
        self.dbArtist=Artist()
        self.dbGagnant=Gagnant()
        self.headingone=program.get_title()
        self.redirect=""
        self.body=""
        self.params={"current_user_email":None,"current_user_name":None}
    
    def set_redirect(self,x):
        self.redirect=x
    def get_redirect(self):
        return self.redirect
    def set_session(self,x):
        self.session=x
    def get_session(self):
        return self.session
    def set_param(self,x,y):
        self.params[x]=y
    def getparams(self,param):
        try:
            x=self.params[param]
        except:
            x=None
        return x
    def render_body(self):
        try:
          mystr=""
          for j in self.body.split("<%="):
              if "%>" not in j:
                  mystr+=j
                  continue
              k=j.split("%>")
              print("my session",self.session)
              loc={"session": self.session,"render_collection": self.render_collection,"params":self.params,"getparams": self.getparams,"dbCado":self.dbCado, "dbGagnant":self.dbGagnant,"dbSong":self.dbSong,"dbArtist":self.dbArtist,"dbJeu":self.dbJeu}
              for n in self.params:
                  loc[n]=self.params[n]
              print(k[0])
              l=exec("myvalue="+k[0], globals(), loc)
              mystr+=str(loc["myvalue"]) if loc["myvalue"] is not None else ""
              mystr+=k[1]
          return mystr
        except Exception:
          mystr="erreur : "+traceback.format_exc()
          self.body=mystr
          return mystr
    def render_collection(self, collection,partial,as_):
        myview=open(os.path.abspath("./"+partial),"r").read()
        mystr=""
        i=0
        paspremier=False
        for x in collection:
            for j in myview.split("<%="):
                if "%>" not in j:
                    mystr+=j
                    continue

                k=j.split("%>")
                loc={"paspremier":paspremier,as_: x,"index":i,  "params": self.params,"render_collection":self.render_collection,"dbSong":self.dbSong}
                print(dict(x))
                if k[0]:
                  print(k[0], "content render")
                  print(k[0])
                  l=exec("myvalue="+k[0], globals(), loc)
                  mystr+=str(loc["myvalue"])
                if k[1]:
                  mystr+=k[1]
            i+=1
            paspremier=True
        return mystr
    def partie_de_mes_mots(self,balise="",text=""):
        r="<{balise}>{text}</{balise}>"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
        return re.search(r, s)
    def debut_de_mes_mots(self,balise="div",text=""):
        r="<{balise}>{text}</{balise}>"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(debutmots=self.title, mot=self.headingone,plusdemots=self.body)
        return re.match(r, s)
    def fin_de_mes_mots(self,balise="div",text=""):
        r="<{balise}>{text}</{balise}>$"
        s="""
        <html>
        <head>
        <title>{debutmots}</title>
        <h1>{mot}</h1>
        {plusdemots}
        </head>
        </html>
        """.format(mot=self.headingone,plusdemots=self.body)
        return re.search(r, s)
    def ajouter_a_mes_mots(self,balise,text):
        r="<{balise}>{text}</{balise}>".format(balise=balise,text=text)
        self.body+=r

    def render_redirect(self):
        self.body="<a href=\"{url}\">{text}</a>".format(url=self.get_redirect(),text="la page a été redirigée")
        
        return self.body
    def set_json(self,x):
        self.json=True
        self.body=(x).encode("utf-8")
    def render_my_json(self,filename):

        self.body=filename
        self.body=self.render_body()
        try:
          return self.body.encode("utf-8")
        except:
          return self.body

    def render_some_json(self,filename):

        self.body=open(os.path.abspath(self.path+"/"+filename),"r").read()
        self.body=self.render_body()
        try:
          return self.body.encode("utf-8")
        except:
          return self.body

    def render_json(self):
        return self.body
    def render_figure(self,filename):
        self.body+=open(os.path.abspath(self.path+"/"+filename),"r").read()
        if self.mytemplate is not None:
            self.body= open(os.path.abspath(self.mytemplate),"r").read().format(debutmots=self.title, mot=self.headingone,plusdemot=self.body)
        self.body=self.render_body()
        try:
          return self.body.encode("utf-8")
        except:
          return self.body
