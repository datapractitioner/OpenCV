import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) # istanzia l'oggetto VideoCapture

while(True):

    _, frame = cap.read() # lettura input dalla videocamera

    gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # conversione frame in altra scala colore

    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

# OpenCV può essere usato anche per riprodurre video

cap = cv.VideoCapture('nome_file_video.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
