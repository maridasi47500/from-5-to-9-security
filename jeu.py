# coding=utf-8
import sqlite3
import sys
import re
from chaine import Chaine
from model import Model
from program import Myprogram
class Jeu(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.program=Myprogram()
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists jeu(
        id integer primary key autoincrement,
        pic text,
            lyric_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select jeu.id,lyric.text,jeu.pic, song.title,artist.name as artistname from jeu left join lyric on lyric.id = jeu.lyric_id left join song on song.id = lyric.song_id left join artist on artist.id = song.artist_id",())

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from jeu where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getlyricbyid(self,myid):
        self.cur.execute("select lyric.*, song.title,artist.pic from lyric left join song on song.id = lyric.song_id left join artist on artist.id = song.artist_id where lyric.id = ?",(myid,))
        row=self.cur.fetchone()
        return row
    def getbyid(self,myid):
        self.cur.execute("select lyric.*, song.title,artist.pic from lyric left join song on song.id = lyric.song_id left join artist on artist.id = song.artist_id where lyric.id = ?",(myid,))
        row=dict(self.cur.fetchone())
        return row
    def createwithlyric(self,params):
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
        lyric=self.getlyricbyid(myhash["lyric_id"])
        print(lyric,"M Y H A S H")
        filename=Chaine().fichier("hey.gif")
        print(filename,"M Y H A S H")
        myhash["pic"]=filename
        self.program.myargs(["sh","./cado/textjeu.sh",lyric["text"],lyric["pic"],filename])
        self.program.run()
        myid=None
        try:
          self.cur.execute("insert into jeu (pic,lyric_id) values (:pic,:lyric_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["jeu_id"]=myid
        azerty["notice"]="votre jeu a été ajouté"
        return azerty




