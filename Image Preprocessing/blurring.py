import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Image Preprocessing\cat3.jpg")

# averaging(mean blurring)
# avg_blurred_img = cv.blur(img, (5,5))
# # cv.imshow('average_blur_img',avg_blurred_img)
# plt.imshow(cv.cvtColor(avg_blurred_img, cv.COLOR_BGR2RGB))
# plt.title('Averaging using plt')
# plt.show()


# Gaussian blurr 
gaussian_blurr = cv.GaussianBlur(img, (5,5),0)
plt.imshow(cv.cvtColor(gaussian_blurr, cv.COLOR_BAYER_BG2BGR))
plt.title('Gaussian blurr')
plt.show()



cv.waitKey(0)