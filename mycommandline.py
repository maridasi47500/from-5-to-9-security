# coding=utf-8
import sqlite3
import os
from fichier import Fichier
import sys
import re
from model import Model
class Mycommandline(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists mycommandline(
        id integer primary key autoincrement,
        name text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from mycommandline")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from mycommandline where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from mycommandline where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
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
          self.cur.execute("insert into mycommandline (name) values (:name)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["mycommandline_id"]=myid
        azerty["notice"]="votre mycommandline a été ajouté"
        matermin=params["name"].split(".")[-1]
        myprogram=""
        if matermin == "rb":
            myprogram="ruby"
        if matermin == "php":
            myprogram="php"
        if matermin == "py":
            myprogram="python3"
        monfichier=Fichier("./monscript","lancer_"+params["name"]+".sh").ecrire("""xterm -l -hold -e "cd {myroot}/monscript && echo 'c\'est mon script' && bash -l -c '{program} ./{name}'"
                """.format(myroot=os.getcwd(), name=params['name'],program=myprogram))
        return azerty




