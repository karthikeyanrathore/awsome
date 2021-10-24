#!/bin/bash
#sudo service mysql start
#sudo service mysql status
export FLASK_APP=build/__init__.py
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
