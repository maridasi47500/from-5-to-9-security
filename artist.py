# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Artist(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists artist(
        id integer primary key autoincrement,
        name text not null,
            pic text,
           constraint hey unique (name)
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from artist")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from artist where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from artist where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        return row
    def getbyname(self,myhash):
        try:
          self.cur.execute("select * from artist where name = ?",(myhash["name"],))
          self.con.commit()
          row=int(self.cur.fetchone()["id"])
        except:
          row=None
        return row
    def getwithoutpic(self):
        try:
          self.cur.execute("select * from artist where pic = ?",("mypic",))
          self.con.commit()
          row=self.cur.fetchall()
        except:
          row=None
        return row
    def getwithpic(self):
        try:
          self.cur.execute("select * from artist where pic <> ?",("mypic",))
          self.con.commit()
          row=self.cur.fetchall()
        except:
          row=None
        return row
    def update(self,myhash):
        print("ok")
        print("M Y H A S H update artist")
        print(myhash,myhash.keys())
        myid=None
        try:
          print("artist",myhash)
          print("hey artist")
          self.cur.execute("update artist set pic = :pic where id = :id",myhash)
          self.con.commit()
          myid=int(self.cur.lastrowid)
          print("myid",myid)
        except Exception as e:
          print("my error ARTIST"+str(e))
        return myid
    def findorcreate(self,params):
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
        print("M Y H A S H artist")
        print(myhash,myhash.keys())
        myid=None
        try:
          myhash["pic"]="mypic"
          print("artist",myhash)
          print("hey artist")
          myid=self.getbyname(myhash)
          if not myid:
            self.cur.execute("insert or ignore into artist (name,pic) values (:name,:pic)",myhash)
            self.con.commit()
          myid=int(self.cur.lastrowid)
          print("myid",myid)

        except Exception as e:
          print("my error ARTIST"+str(e))
        return myid
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
        print("M Y H A S H ARTIST")
        print(myhash,myhash.keys())
        myhash["pic"]="mypic"
        myid=None
        try:
          print("artist",myhash)
          print("hey artist")
          self.cur.execute("insert or ignore into artist (name,pic) values (:name,:pic)",myhash)
          self.con.commit()
          print("hey artist")
          myid=str(self.cur.lastrowid)
          print("hey artist",myid)
        except Exception as e:
          print("my error ARTIST"+str(e))
        azerty={}
        azerty["artist_id"]=myid
        azerty["notice"]="votre artist a été ajouté"
        return azerty




