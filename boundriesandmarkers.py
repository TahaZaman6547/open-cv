import cv2 as cv
import numpy as np

lawn = np.zeros((600, 600, 3), dtype='uint8')  
cv.imshow('Lawn', lawn)  

cv.rectangle(lawn, (50, 50), (550, 550), (0, 255, 0), thickness=2)  
cv.imshow('Lawn with Boundary', lawn)  

cv.circle(lawn, (300, 300), 50, (0, 0, 255), thickness=-1)  
cv.imshow('Lawn with Obstacle', lawn)

cv.putText(lawn, 'Start Position', (50, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), thickness=2) 
cv.imshow('Lawn with Text', lawn) 

cv.waitKey(0)  
cv.destroyAllWindows()  
