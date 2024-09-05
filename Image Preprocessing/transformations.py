import cv2 as cv
import numpy as np

img = cv.imread('Image Preprocessing/cat3.jpg')
cv.imshow('Image', img)

def translate(img, x ,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimenstions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimenstions)

# -x -> left
# -y -> up
# x -> Right
# y -> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)


# rotation 
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width/2, height/2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, -45)
cv.imshow('Rotated',rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated_rotated',rotated_rotated)
rotated_rotated = rotate(img, -90)
cv.imshow('Rotated_rotated',rotated_rotated)


# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resiezed', resized)


# flipping 

flip = cv.flip(img, 0)
cv.imshow('Flip0', flip)
flip = cv.flip(img, 1)
cv.imshow('Flip1', flip)
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)


cv.waitKey(0)