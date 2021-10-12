#!/usr/bin/env python3
import pymysql as py
#db = py.connect(host="localhost",user="root", port=3306)

class database(object):
  def __init__(self , host , user , port, prime_db):
    self.db = py.connect(host=host,user=user, port=port, db=prime_db)
  
  def connect(self):
    cursor = self.db.cursor()
    return cursor
  
  def insert(self, username, password, cursor):
    try:
      cursor.execute("INSERT INTO user (username,password) VALUES (%s,%s)", (username,password))
      self.db.commit()
      print("done")
    except:
      print("fail")
      self.db.rollback()
 
  def exists(self, username):
    pass

  def auth(self, username, password):
    pass
    
  def version(self, cursor):
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print ("Database version : %s " % data)
  
  def close(self, cursor):
    self.db.close()
    cursor.close()

'''
x = database("localhost" , "root", 3306, "data")
cursor = x.connect()
x.version(cursor)
x.insert("karthikeyan", "sys" , cursor)
x.close(cursor)
'''

