#!/usr/bin/env python3
import cv2
from keras.models import load_model
from keras.initializers import glorot_uniform
import tensorflow as tf
import numpy as np

class Model:
  @staticmethod
  def get():
    with open('build/model/model.json', 'r') as json_file:
      json_savedModel= json_file.read()
      model_j = tf.keras.models.model_from_json(json_savedModel)
      model_j.summary()
    
    model_j.load_weights('build/model/model.h5')
    model_j.compile(loss='sparse_categorical_crossentropy',
         optimizer='SGD',
         metrics=['accuracy'])
    return model_j
  

class Predict(object):
  def __init__(self , img_path):
    image = cv2.imread(img_path)
    self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(self.gray.shape)
  
  def get_emotion(self):
    facecasc = cv2.CascadeClassifier('build/xml/haarcascade_frontalface_default.xml')
    faces = facecasc.detectMultiScale(self.gray,scaleFactor=1.3, minNeighbors=10)
    for (x, y, w, h) in faces:
      roi_gray = self.gray[y:y + h, x:x + w]                      
      cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
      model = Model.get()
      prediction = model.predict(cropped_img)
      return np.argmax(prediction)

