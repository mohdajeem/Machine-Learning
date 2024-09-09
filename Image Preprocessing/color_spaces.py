import cv2 as cv

img = cv.imread("Image Preprocessing\cat3.jpg")

# RGB representation 
bgr_img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.imshow('Original',img)
cv.imshow('RGB image', bgr_img)

# HSV (hue, saturation, value)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv_image', hsv_img)

# LAB image 
lab_image = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab image', lab_image)

# YCrCb image (luma and chroma channels)

ycrcb_img = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
cv.imshow('Ycrcb image',ycrcb_img)

# GrayScale image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img',gray_img)

# HLS 
hls_img = cv.cvtColor(img, cv.COLOR_BGR2HLS)
cv.imshow('hls_img', hls_img)


cv.waitKey(0)

