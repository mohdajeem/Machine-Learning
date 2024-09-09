import cv2 as cv
import numpy as np

# translation (moving the image)

image = cv.imread("Image Preprocessing\cat3.jpg")


"""


# define the transformation matrix(move by 100 pixels in x and y direction)
M = np.float32([[1,0,10], [0,1,10]])

# apply the transfromation
# cv.imshow('cat', image)

shifter_image = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))

"""

# rotatiion(Spinning the image)
"""

center = (image.shape[1]//2, image.shape[0]//2)
# print(center)
M = cv.getRotationMatrix2D(center, 90, 1.0)

rotated_img = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv.imshow('rotated_image', rotated_img)

cv.imshow('cat image', image)

"""


"""

## Scaling the image(zooming In and out)
# resized_img = cv.resize(image, None, fx = 0.3, fy = 0.8)
# cv.imshow('resized_img', resized_img) 

cv.imshow('original', image) 

# Flipping the image - Mirror the image 
flipped_img_horiz = cv.flip(image, 1) # 1 for horizontally , 0 for vertically
cv.imshow('flipped_img_hori',flipped_img_horiz)

flipped_img_vert = cv.flip(image, 0)
cv.imshow('flipped_image_vertically', flipped_img_vert)


"""


# Affine Transformation (Skewing the image)

pt1 = np.float32([[10,50],[200,100], [50,200]]) # creating a 2D array
# print(pt1)
pt2 = np.float32([[10,100],[200,50],[100,250]])

# Affine transforation matrix
M = cv.getAffineTransform(pt1, pt2)
transformed_image = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv.imshow('Transformed_affine_imgae', transformed_image)


cv.waitKey(0)