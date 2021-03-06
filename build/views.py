#!/usr/bin/env python3
from build import app
import config
import os
import json
from build.db import database
from build.predict import Predict
from flask import request
from flask import render_template 
from flask import session 
from flask import redirect, url_for 

UPLOAD_FOLDER = 'build/images'
LOCALHOST = config.LOCALHOST
USER = config.USER
PORT = config.PORT
DATABASE = config.DATABASE
PASSWORD = config.PASSWORD
app.secret_key = config.secret_key
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# connect to database
def connection():
  db = database(LOCALHOST, USER, PORT, DATABASE, PASSWORD)
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
      # incorrect-password
      elif(ex == -1):
        error = "password is incorrect"
      # user does not exists
      elif(ex == 0):
        error = "username does not exists"
  if "user_id" in session:
    return redirect(url_for("home"))
  return render_template('login.html', error=error)

@app.route("/logout")
def logout():
  session.pop("user_id" , None)
  return redirect(url_for("index"))

@app.route("/home", methods=["GET", "POST"])
def home():
  db , cursor = connection()
  if request.method == "POST":
    image = request.files['img']
    path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(path)
    emo, a = Predict(path).get()
    if emo is None:
      return "invalid image"
    if int(emo) == 1:
      return redirect(url_for("get_happy"))
    elif int(emo) == 3:
      return redirect(url_for("get_sad"))
    elif int(emo) == 0:
      return redirect(url_for("get_neutral"))
    else:
      return "other emotion %s" % (a[emo])
  if "user_id" in session:
    id = session['user_id']
    username = db.get_username(cursor, id)
    print(username)
    if username is not None:
      return render_template("home.html", username=username)
    else:
      return "error"
  else:
    return redirect(url_for("login"))

@app.route("/home/happy", methods=['POST', 'GET'])
def get_happy():
  if "user_id" in session:
    counter=1
    f = open("build/data/happy_data.json")
    data = json.load(f)
    return render_template("tracks.html", data=data, counter=counter)
  else:
    return redirect(url_for("login"))

@app.route("/home/sad", methods=['POST', 'GET'])
def get_sad():
  if "user_id" in session:
    counter=2
    f = open("build/data/sad_data.json")
    data = json.load(f)
    return render_template("tracks.html", data=data, counter=counter)
  else:
    return redirect(url_for("login"))

@app.route("/home/neutral", methods=['POST', 'GET'])
def get_neutral():
  if "user_id" in session:
    counter=3
    f = open("build/data/neutral_data.json")
    data = json.load(f)
    return render_template("tracks.html", data=data, counter=counter)
  else:
    return redirect(url_for("login"))

