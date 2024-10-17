import cv2 as cv

img = cv.imread('lawn.jpg')  
cv.imshow('Lawn Area', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Lawn', gray)

blur = cv.GaussianBlur(gray, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blurred Lawn', blur)

edges = cv.Canny(blur, 125, 175)
cv.imshow('Lawn Edges', edges)

resized = cv.resize(img, (600, 600), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Lawn', resized)

cv.waitKey(0)
cv.destroyAllWindows()
