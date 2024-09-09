import cv2 as cv

image = cv.imread("Image Preprocessing\cat3.jpg")


# contours , hierarchy = cv.findContours(image, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) 
# UPPER ONE WILL NOT WORK 
# FIRST CREATE GRAY IMAGE AFTER USE THRESHOLDING THEN USE CONTOURS

gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img', gray_img)

_, thresholded_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

cv.imshow('Thresholded_img',thresholded_img)

contours, _ = cv.findContours(thresholded_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(image, contours, -1,(255,0,222),2)
cv.imshow('cat',image)


cv.waitKey(0)
cv.destroyAllWindows()