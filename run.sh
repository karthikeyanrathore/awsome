#!/bin/bash
#sudo service mysql start
#sudo service mysql status
if [ ! -d build/images ]; then
  mkdir build/images
fi

if [[ "$OSTYPE" == "darwin"* ]]  && [[ $LOCAL == 1 ]]; then
  source ~/.bash_profile
  conda activate
  export FLASK_APP=build/__init__.py
  export FLASK_ENV=development
  export FLASK_DEBUG=1
  python3 -m flask run --host=0.0.0.0 --port=80
  rm build/images/*

elif [[ "$OSTYPE" == "linux-gnu"* ]]  && [[ $PRO == 1 ]]; then
  export FLASK_APP=build/__init__.py
  export FLASK_ENV=development
  export FLASK_DEBUG=1
  python3 -m flask run --host=0.0.0.0 --port=80
  rm build/images/*
fi

