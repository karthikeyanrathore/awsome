#!/bin/bash
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  printf "upgrading Ubuntu-18.04 packages \n"
  sudo apt-get -y update && sudo apt-get -y dist-upgrade
  sudo apt -y install python3 
  sudo apt -y install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa -y

  printf "switching to python3.8 -v \n"
  sudo apt-get install python3.8 -y
  sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
  sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
  sudo update-alternatives --config python3 # mark 2
  sudo apt -y install python python3-pip
  yes | pip3 install --upgrade pip

  printf "installing tensorflow \n"
  yes | pip3 install --no-cache-dir tensorflow
  python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

  printf "for opencv \n"
  sudo apt-get install python3.8-dev -y
  sudo apt-get install ffmpeg libsm6 libxext6  -y 

  printf "installing MySQL server \n"
  sudo apt-get install mysql-server -y


  printf "installing .... \n"
  yes | pip3 install pymysql opencv-python flask

  exit

else
  printf "only works under linux-gnu Ubuntu-18.04 \n"
fi

