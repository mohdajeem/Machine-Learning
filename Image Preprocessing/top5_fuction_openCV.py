import cv2 as cv

img = cv.imread('Image Preprocessing\cat3.jpg')
cv.resize(img, (300,300), interpolation=cv.INTER_LINEAR)
cv.imshow('img',img)

# # GrayScale Image 
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# blurr 

# blurr = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur',blurr)


# Edge cascade 
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dilating the image 
dilated = cv.dilate(canny, (3,3), iterations=5)
cv.imshow('dilated',dilated)

# Eroding 
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Erode', eroded)

# Resize
# resized = cv.resize(img, (500,500))
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)