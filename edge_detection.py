import cv2 as cv
import numpy as np

img = cv.imread('path_to_lawn_boundary.jpg') 
cv.imshow('Lawn Area', img)  

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
cv.imshow('Grayscale Lawn', gray) 

edges = cv.Canny(gray, 100, 200) 
cv.imshow('Detected Lawn Boundary', edges)  

cv.waitKey(0)  
cv.destroyAllWindows()  #
