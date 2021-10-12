#!/usr/bin/env python3
from build import app
from build.db import database
from flask import request
from flask import render_template 

LOCALHOST = "localhost"
USER = "root"
PORT = 3306
DATABASE = "data"

def connection():
  db = database(LOCALHOST, USER, PORT, DATABASE)
  cursor = db.connect()
  return db, cursor

@app.route('/')
def index():
  return 'Hello World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
  db , cursor = connection()
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    error = None
    if not username:
      error = "username is required"
    elif not password:
      error = "password is required"
    if error is None:
      if db.insert(username, password, cursor):
        return "success"
      else:
        error = "fail"
  return render_template("register.html")




