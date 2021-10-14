#!/usr/bin/env python3
import pymysql as py
from werkzeug.security import check_password_hash, generate_password_hash
#db = py.connect(host="localhost",user="root", port=3306)

class database(object):
  def __init__(self , host , user , port, prime_db):
    self.db = py.connect(host=host,user=user, port=port, db=prime_db)
  
  def connect(self):
    cursor = self.db.cursor()
    return cursor
  
  def insert(self, username, password, cursor):
    try:
      cursor.execute("INSERT INTO user (username,password) VALUES (%s,%s)", (username,generate_password_hash(password)))
      self.db.commit()
      print("done")
      return 1
    except:
      print("fail")
      self.db.rollback()
      return 0
 
  def exists(self, cursor, username):
    ex = cursor.execute("SELECT username FROM user WHERE username = %s", (username))
    if ex:
      return 1
    return 0

  def auth(self, cursor, username, password):
    cursor.execute("SELECT * FROM user WHERE username = %s", (username))
    user = None
    user = cursor.fetchone()
    if user is not None:
      if check_password_hash(user[2], password):
        return 1, user
      else:
        return -1, user
    else:
      return 0, user
    
  def version(self, cursor):
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print ("Database version : %s " % data)
  
  def close(self, cursor):
    self.db.close()
    cursor.close()


