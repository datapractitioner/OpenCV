import cv2 as cv
import numpy as np
import os

# Reading and Displaying an image from

img = cv.imread('./Tutorials/python.jpg') # where 0 tells to read in grayscale

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()