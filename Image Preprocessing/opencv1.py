import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
# print(blank)
cv.imshow('Blank', blank)

blank[200:300,300:400] = 0,0,255
cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=3)
cv.imshow('Rectanlge ', blank)

cv.waitKey(0)