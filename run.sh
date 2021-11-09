#!/bin/bash
#sudo service mysql start
#sudo service mysql status
export FLASK_APP=build/__init__.py
export FLASK_ENV=development
export FLASK_DEBUG=1
python3 -m flask run --host=0.0.0.0 --port=80
