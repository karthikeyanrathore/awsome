#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
import build.views

'''
if __name__ == "__main__":
  app.run() 
  #serve(app, host='0.0.0.0', port=80)
'''




