import cv2
import sys

webcam = cv2.VideoCapture(0)
model = cv2.CascadeClassifier()
model.load('haarcascade_frontalface_default.xml')

while True:
    ret, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Building the rectangle around the face
    faces = model.detectMultiScale(gray, minNeighbors=6, flags= cv2.CASCADE_SCALE_IMAGE )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #displaying each frame
    cv2.imshow('Video', frame)
    
    #Press Q to finish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#Initializing the webcam
video_capture.release()