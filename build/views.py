#!/usr/bin/env python3
from build import app
from build.db import database
from flask import request
from flask import render_template 
from flask import session 
from flask import redirect, url_for 

LOCALHOST = "localhost"
USER = "root"
PORT = 3306
DATABASE = "data"
app.secret_key = "dev"


def connection():
  db = database(LOCALHOST, USER, PORT, DATABASE)
  cursor = db.connect()
  return db, cursor

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
  db , cursor = connection()
  error = None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if not username:
      error = "username is required"
    elif not password:
      error = "password is required"
    elif db.exists(cursor, username):
      error = "username already exists in the database"
    if error is None:
      if db.insert(username, password, cursor):
        return redirect(url_for("login"))
      else:
        error = "fail"
  print(error)
  return render_template("register.html", error=error)

@app.route("/login" , methods=['POST' ,'GET'])
def login():
  db , cursor = connection()
  error = None
  print(session)
  if request.method == "POST":
    username = request.form['username']
    password = request.form['password']
    if not username:
      error = "username is required"
    elif not password:
      error = "password is required"
    if error is None:
      ex, user = db.auth(cursor , username, password)
      if(ex == 1):
        session.clear()
        session['user_id'] = str(user[0])
        return redirect(url_for("home"))
      elif(ex == -1):
        error = "password is incorrect"
      elif(ex == 0):
        error = "username does not exists"
  if "user_id" in session:
    return redirect(url_for("home"))
  return render_template('login.html', error=error)

@app.route("/logout")
def logout():
  session.pop("user_id" , None)
  return redirect(url_for("index"))

@app.route("/home")
def home():
  if "user_id" in session:
    id = session['user_id']
    return '<h1> Hey %s </h1> <br></br> <a href="/logout">Logout ffao?</a>' % (id)
  else:
    return redirect(url_for("login"))



