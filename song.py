import sqlite3
from sqlite3 import Error

class Song():
  db=r"./development.sqlite3"
  def get_db():
      return self.db
  def create_connection(self,db_file):
      """ create a database connection to a SQLite database """
      conn = None
      try:
          conn = sqlite3.connect(db_file)
          print(sqlite3.version)
      except Error as e:
          print(e)
      finally:
          if conn:
              conn.close()
  def create_table(self,conn, create_table_sql):
      """ create a table from the create_table_sql statement
      :param conn: Connection object
      :param create_table_sql: a CREATE TABLE statement
      :return:
      """
      try:
          c = conn.cursor()
          c.execute(create_table_sql)
      except Error as e:
          print(e)
  def get_sum(self,x):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select sum(case when price is not null then price else 0 end) as mysum from items group by date having date = ?'''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        myval=None
        if x:
          cur.execute(sql,(str(x),))
          conn.commit()
          myitems= cur.fetchone()
          myval=myitems["mysum"]
        else:
          myval=0
        if not myval:
          myval=0

      except Error as e:
        print(e)
        myval="0"
      finally:
        if conn:
          conn.close()
        return str(myval) if myval is not None else "0"
  def save_heure_passage(self,project):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select * from songs
                  where file = ? '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql, project)
        conn.commit()
        bb= cur.fetchone()
        sql = ''' insert or ignore into songpassages (file,time)
values (?,?)
        cur.execute(sql, project)
        conn.commit()
'''
        aa= cur.fetchone()
      except Error as e:
        print(e)
        bb= {"title":"","artist":""}
        aa= {"filename":"","time":""}
      finally:
          if conn:
              conn.close()
          return {"filename":aa["file"],"time":aa["time"],"title":bb["title"],"artist":bb["artist"]}
  def get_song(self,project):
      """
      Create a new project into the projects table
      :param conn:
      :param project:
      :return: project id
      """
      try:
        sql = ''' select * from songs
                  where file = ? '''
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.row_factory = sqlite3.Row
        cur.execute(sql, project)
        conn.commit()
        aa= cur.fetchone()
      except Error as e:
        print(e)
        aa= None
      finally:
          if conn:
              conn.close()
          return aa
  def __init__(self):


    sql1 = """ CREATE TABLE IF NOT EXISTS songs (
                                        id integer PRIMARY KEY autoincrement,
                                        title string NOT NULL,
                                        artist string NOT NULL,
                                        mytype string default 'song',
                                        file string NOT NULL,
                                        image string NOT NULL 
                                    ); """
    sql2 = """ CREATE TABLE IF NOT EXISTS songpassages (
                                        id integer PRIMARY KEY autoincrement,
                                        file string NOT NULL,
                                        time datetime NOT NULL 
                                    ); """

    self.create_connection(self.db)
    conn = sqlite3.connect(self.db)
    if conn is not None:
        self.create_table(conn,sql1)
        self.create_table(conn,sql2)
        print("key")
        if conn:
            conn.close()
    else:
        print("error crete table")

