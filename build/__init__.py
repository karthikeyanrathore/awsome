#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
import build.views
import build.db

if __name__ == "__main__":
  app.run(debug=True)






