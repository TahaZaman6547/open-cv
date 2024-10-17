import cv2 as cv
import numpy as np

img = cv.imread('lawn_with_obstacles.jpg')  
cv.imshow('Lawn Image', img)  

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blurred Grayscale Lawn', blur)  

edges = cv.Canny(blur, 125, 175)
cv.imshow('Detected Lawn Edges', edges)

contours, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 
print(f'Found {len(contours)} contours!')

blank = np.zeros(img.shape, dtype='uint8')  
cv.drawContours(blank, contours, -1, (0, 255, 0), thickness=2)  
cv.imshow('Contours on Lawn', blank)  

cv.waitKey(0)  
cv.destroyAllWindows()  
