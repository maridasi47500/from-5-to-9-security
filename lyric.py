# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Lyric(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists lyric(
        id integer primary key autoincrement,
        song_id text,
            text text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from lyric")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from lyric where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbysongid(self,myid):
        self.cur.execute("select * from lyric where song_id = ?",(myid,))
        row=self.cur.fetchall()
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from lyric where id = ?",(myid,))
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
          self.cur.execute("insert into lyric (song_id,text) values (:song_id,:text)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["lyric_id"]=myid
        azerty["notice"]="votre lyric a été ajouté"
        return azerty




