import cv2 as cv
import numpy as np

img = cv.imread('path_to_image.jpg')
cv.imshow('Lawn Area', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

edges = cv.Canny(gray, 100, 200)
cv.imshow('Edges', edges)

contours, _ = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.imshow('Detected Obstacles', img)

cv.waitKey(0)
