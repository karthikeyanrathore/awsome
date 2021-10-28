#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import sys

DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///user.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String(255), nullable=False)

  def __repr__(self):
    return "<User %d %s" % (self.id, self.name)


@app.route("/")
def hello():
  return ("hello world")


if __name__ == "__main__":
  if "create-db" in sys.argv:
    db.create_all()
    print("user  db fine")
  else: 
    app.run()

