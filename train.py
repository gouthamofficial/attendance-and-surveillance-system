'''
   To run this, you have to install the cv2 library.
!! This file trains the face recognizer from the features & labels list.
!! After training this file creates the 'face_trained.yml' file.

   Training requires a lot of images for each person... 
!! Less than 200 images worked for me. But I recommend more images.
!! Do not over-train the recognizer, it will put out some errors if you do so.

'''


import os
import cv2 as cv
import numpy as np

# you can decide how many person you want to be recognised
people = ['person 1', 'person 2', 'person 3', 'person 4', 'person 5'] 
DIR = r'path/to/faces/folder'

haar_cascade = cv.CascadeClassifier(" path_to /face_detector.xml") 

features = []
labels = []

# This functions creates the features & labels lists which are required to train the face recognizer
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.0485258, minNeighbors = 6)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)  # type: ignore
                labels.append(label)  # type: ignore

create_train()

features = np.array(features, dtype='object')
labels = np.array(labels)

# Creating the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Training the face recognizer
face_recognizer.train(features, labels)
print('training done ...........................................!')

# Saving the 'face_trained.yml' file
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)