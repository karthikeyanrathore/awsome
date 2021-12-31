#!/usr/bin/env python3
import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image
class Predict():
  def __init__(self, img):
    self.img = img
  def get(self):
    f = open('build/model/fer.json', 'r')
    m = f.read()
    f.close()
    model = model_from_json(m)
    model.load_weights('build/model/fer.h5')
    classifier = cv2.CascadeClassifier('build/model/haarcascade_frontalface_default.xml')
    img = cv2.imread(self.img)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_detected = classifier.detectMultiScale(gray_img, 1.18, 5)
    for (x, y, w, h) in faces_detected:
      cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
      roi_gray = gray_img[y:y + w, x:x + h]
      roi_gray = cv2.resize(roi_gray, (48, 48))
      img_pixels = image.img_to_array(roi_gray)
      img_pixels = np.expand_dims(img_pixels, axis=0)
      img_pixels /= 255.0
      predictions = model.predict(img_pixels)
      max_index = int(np.argmax(predictions))
      emotions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear']
      predicted_emotion = emotions[max_index]
      print(predicted_emotion)
      return max_index, emotions
    return None, None

