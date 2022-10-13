'''
   This is the main file where most of the functions take place.
   To run this, you have to install the cv2 library.
!! You have to give the path to the files and folders.
!! Download the 'face_detector.xml' file from this repository.
!! The file which creates the 'face_trained.yml' file can be downloaded from this repository.
!! You have to create the 'face_trained.yml' file as per your need.

   For more information check the README.md file
   
'''


import cv2 as cv
from datetime import datetime
from uploading import mark_attendance

# face detection file
haar_cascade = cv.CascadeClassifier(" path_to /face_detector.xml") 

# you can decide how many person you want to be recognised
people = ['person 1', 'person 2', 'person 3', 'person 4', 'person 5'] 
strength = len(people) # number of persons

# creating face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# reading the features and labels of the face from 'yml' file
face_recognizer.read(' path_to /face_trained.yml')

# capturing from the webcamerea
cam = cv.VideoCapture(0)
if (cam.isOpened() == False):
	print("Error reading cam file")

# defining the size of the video that will be saved for future use / surveillance
frame_width = int(cam.get(3))
frame_height = int(cam.get(4))
size = (frame_width, frame_height)

# obtaining the date and time for naming the video
now = datetime.now().time().strftime("%H:%M:%S")
date = datetime.now().strftime("%Y-%m-%d")
not_valid = str(date+'---'+now)
date_time = not_valid.replace(':', '-')

# defining the path, name, format, and size of the video
result = cv.VideoWriter(f' path_to_video_folder /{date_time}.avi', cv.VideoWriter_fourcc(*'MJPG'),10, size)

# declaring the attendance list (list of lists)
attendance = []
    
def end():
    cam.release()

# checking for a label(name) in the attendance list to eliminate repetition
def label_check(strlabel):
    found = False
    for i in range(0, len(attendance)):
        if strlabel in attendance[i]:
            found = True
            break
        else: found = False
    return found

# The main function 
def main():
    while(True):
        # Reading, converting and detecting the faces from the visual
        ret, frame = cam.read()
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        face_rect = haar_cascade.detectMultiScale(gray_frame, scaleFactor = 1.0485258, minNeighbors = 6)

        # Detecting each faces
        for (x, y, w, h) in face_rect:
            # Defining the region of the face
            faces_roi = gray_frame[y:y+h, x:x+w]

            # Predicting the face with the highly trained face recognizer
            label, confidence = face_recognizer.predict(faces_roi)
            #print(f"name: {label} ## confidence of: {confidence}")

            # Checking the label of the face wheather it is included in the attendance list
            if confidence < 68:
                strlabel = people[label]
                pending = label_check(strlabel)

                # Appending the person to the attendance list if it is not included before
                if pending != True:
                    person = []
                    now = datetime.now().time().strftime("%I:%M:%S") # time object
                    date = datetime.now().strftime("%d-%m-%Y") # date object
                    person.append(date)
                    person.append(now)
                    person.append(strlabel)

                    # Appending the person with name, date & time of identification as a list to the attendance list
                    attendance.append(person)

                # Checking if the number of persons in the attendance list is equal to the number of people
                if len(attendance) == strength:
                    # If it is true the attendance list will be handed to the uploading file
                    is_Marked = mark_attendance(attendance)
                    # The uploading file returns True if the attendance is uploaded without any errors
                    if is_Marked == True:
                        # If it is uploaded correctly the program will end
                        end()

        # If the visual is recorded correcty, each frame will be stored to the video, else will output an error
        if ret == True:
            if cv.waitKey(0) == ord('x'):
                end()
            result.write(frame)
        else:
            print("error")
            end()

main()
