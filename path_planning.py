import cv2 as cv
import numpy as np

map = np.zeros((500, 500, 3), dtype='uint8')

start_point = (50, 250)
end_point = (450, 250)


cv.circle(map, start_point, 10, (0, 255, 0), -1)
cv.circle(map, end_point, 10, (0, 0, 255), -1)

cv.line(map, start_point, end_point, (255, 0, 0), 2)

cv.imshow('Planned Path', map)

cv.waitKey(0)
