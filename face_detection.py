import cv2 
import numpy as np
import subprocess
import time
from . import  msg

face_classfier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_classfier.detectMultiScale(gray , 1.3 , 5)
    if faces is ():
        return None
    
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h , x:x+w]
        
    return cropped_face

cap = cv2.VideoCapture(0)
count = 0

for i in range(2):
    input()
    count = 0
    while True:
        ret , frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame) , (200 , 200))
            face = cv2.cvtColor(face , cv2.COLOR_BGR2GRAY)
            
            cmd  = "mkdir C:\\Users\\Dell\\Desktop\\faces\\user" + str(i)
            subprocess.getoutput(cmd)
            file_name_path = 'C:\\Users\\Dell\\Desktop\\faces\\user'+ str(i) + '\\' + str(count) + '.jpg'
            cv2.imwrite(file_name_path , face)

            cv2.putText(face , str(count) , (50,50) , cv2.FONT_HERSHEY_COMPLEX , 1  , (0,255,0) , 2)
            cv2.imshow('face detector' , face)

        else:
            print("Face not found")
            pass

        if cv2.waitKey(1) == 13 or count == 100:
            print("user " + str(i) + " done")
            break
        
cap.release()
cv2.destroyAllWindows()
print("collecting samples complete")


import cv2
import numpy as np
from os import listdir
from os.path import isfile , join

onlyfiles = []
for i in range(2):
    data_path = 'C:\\Users\\Dell\\Desktop\\faces\\user' + str(i)
    for f in listdir(data_path):
        onlyfiles.append(join(data_path , f))       
    # onlyfiles.append(f for f in listdir(data_path) if isfile(join(data_path , f)))

# print(onlyfiles)
training_Data , Labels = [] , []

for i in range(2):
    for files in onlyfiles:
        image_path = files
        images = cv2.imread(image_path , cv2.IMREAD_GRAYSCALE)
        training_Data.append(np.asarray(images , dtype=np.uint8))
        Labels.append(i)
    
Labels = np.asarray(Labels , dtype=np.int32)

model = cv2.face_LBPHFaceRecognizer.create()

model.train(np.asarray(training_Data) , np.asarray(Labels))
print("model trained successfully")

def face_detector(img , size=0.5):
    
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_classfier.detectMultiScale(gray , 1.3 , 5)
    if faces is ():
        return img , []
    
  
    for (x,y,w,h) in faces:
        cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,255,255) , 2)
        roi = img[y:y+h , x:x+w]
        roi = cv2.resize(roi , (200 , 200))

    return img , roi 

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    image , face = face_detector(frame)
    
    try:
        face = cv2.cvtColor(face , cv2.COLOR_BGR2GRAY)
        results = model.predict(face)
        
        if results[0] < results[1]:
            sendMail('sourabhmishra1262@gmail.com' , 'sourabh')
                    
        if results[0] > results[1]:
            sendMail('preetimishra@gmail.com' , 'preeti')
            
        else:
            cv2.putText(image , "No face found and locked" , (250,450) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) ,2)
            cv2.imshow('face recognition' , image)
            
    except:
            cv2.putText(image , "no face found" , (250,450) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) ,2)
            cv2.imshow('face recognition' , image)
            pass
    
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cv2.destroyAllWindows()

def face_detector(img , size=0.5):
    
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_classfier.detectMultiScale(gray , 1.3 , 5)
    if faces is ():
        return img , []
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img , (x,y) , (x+w , y+h) , (0,255,255) , 2)
        roi = img[y:y+h , x:x+w]
        roi = cv2.resize(roi , (200 , 200))
    
    return img , roi 

cap = cv2.VideoCapture(0)
if cv2.waitKey(1) == 13:
    ret , frame = cap.read()

image , face = face_detector(frame)


cap.release()
cv2.destroyAllWindows()

face = cv2.cvtColor(face , cv2.COLOR_BGR2GRAY)
results = model.predict(face)


results
