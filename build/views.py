#!/usr/bin/env python3
from build import app
import config
from build.db import database
from flask import request
from flask import render_template 
from flask import session 
from flask import redirect, url_for 

LOCALHOST = config.LOCALHOST
USER = config.USER
PORT = config.PORT
DATABASE = config.DATABASE
PASSWORD = config.PASSWORD
app.secret_key = config.secret_key

# connect to database
def connection():
  db = database(LOCALHOST, USER, PORT, DATABASE, PASSWORD)
  cursor = db.connect()
  return db, cursor

@app.route('/')
def index():
  return render_template("index.html")

# register user to database
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
    # check if user exists
    elif db.exists(cursor, username):
      error = "username already exists in the database"
    if error is None:
      if db.insert(username, password, cursor):
        return redirect(url_for("login"))
      # rollback 
      else:
        error = "fail"
  print(error)
  return render_template("register.html", error=error)

# authentication. 
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
      # success auth
      if(ex == 1):
        session.clear()
        session['user_id'] = str(user[0])
        return redirect(url_for("home"))
      # incorrect-password
      elif(ex == -1):
        error = "password is incorrect"
      # user does not exists
      elif(ex == 0):
        error = "username does not exists"
  if "user_id" in session:
    return redirect(url_for("home"))
  return render_template('login.html', error=error)

# user_id in session dict.
@app.route("/logout")
def logout():
  session.pop("user_id" , None)
  return redirect(url_for("index"))

@app.route("/home")
def home():
  db , cursor = connection()
  if "user_id" in session:
    id = session['user_id']
    # get user-name from database
    username = db.get_username(cursor, id)
    print(username)
    if username is not None:
      return render_template("home.html", username=username)
    else:
      return "error"
  else:
    return redirect(url_for("login"))



