#!/usr/bin/env python3
from build import app

@app.route('/')
def index():
  return 'Hello World!'

