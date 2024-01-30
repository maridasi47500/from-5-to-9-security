# coding=utf-8
import random
import sqlite3
import sys
import re
from model import Model
class Email(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists email(
        id integer primary key autoincrement,
        subject text,
        text text,
            user_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from email")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from email where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from email where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def createfake(self):
        print("ok")
        myhash={}
        print("M Y H A S H")
        gift=""
        choice=random.choice(["prize_event","prize_gift","credit","offer"])
        color=random.choice(["red","blue","yellow","green","purple","orange","brown","grey","rose"])
        size=random.choice(["3","5","7","9","11","13"])
        mytype=random.choice(["solid","dotted"])
        mytext="<div style='border-color:%spx %s %s;'>" % (size,color,mytype)
        subject=""
        if choice == "prize_event":
          subject+="vous êtes le gagnant"

          phrase=random.choice(["Félicitations ! vous avez été sélectionné pour participer à %s"])
        elif choice == "prize_gift":

          gift=random.choice(["carte-cadeau"])
          subject+="vous avez gagné un cadeau "
          link=random.choice(["http://"+gift.replace(" ","")+".com"])
          phrase=random.choice(["Félicitations ! vous avez gagné %s"])
          mytext+=phrase
          phrase1=random.choice(["Aidez-nous","Votre avis compte"])
          phrasecliquez=random.choice(["Répondez à un sondage pour réclamer votre %s","vous avez bien gagné un %s, remplissez ce formulaire "])
          mytext+=phrasecliquez % gift

        elif choice == "credit":
          subject+="carte bancaire bloquée"
          credit=random.choice(["carte debiter.org"])
          link=random.choice(["http://"+credit.replace(" ","")+".com"])
          phrase=random.choice(["Nous vous informons que votre carte bancaire a été bloquée par notre service. Suite aux mesurs de sécurité, nous vous invitons à débloquer votre CB en cliquant sur le lien ci-dessous."])
          mytext+=phrase
        elif choice == "offer":
          subject+="promos et prix bas"
          credit=random.choice(["soldes.fr","prix bas.com","promo.fr"])
          link=random.choice(["http://"+credit.replace(" ","")+".com"])
          promo=random.choice(["Des Tickets Coco Air","des Plantes vertes"])
          mapromo=random.choice(["10","20","30","40","50","60","è0","80","90","-10","-20","-30","-40","-50","-60","-70","-80","-90"])
          phrase=random.choice(["{item} à {valeurpromo}% ! Achetez {item} en cliquant sur le lien ci-dessous.","{item} à seulement {valeurpromo}%. Payez en ligne tout de suite."])
          mytext+=phrase.format(valeurpromo=mapromo,item=promo)


        mytext+="<a href='%s'>cliquez ici</a></div>" % link
        myhash={"text":mytext,"subject":subject,"user_id":"1"}

        myid=None
        try:
          self.cur.execute("insert into email (subject,text,user_id) values (:subject,:text,:user_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["email_id"]=myid
        azerty["text"]=mytext
        azerty["notice"]="votre email a été ajouté"
        return azerty
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into email (text,user_id) values (:text,:user_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["email_id"]=myid
        azerty["notice"]="votre email a été ajouté"
        return azerty




