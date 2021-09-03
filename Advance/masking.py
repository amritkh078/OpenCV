''' Masking  allows us to focus us on the cretain parts of an image. For example: if we want to focus on the face 
of people in the image we remove the unwanted parts of the image.
'''

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8') # the dimension of mask should be the same sizew as the image 
cv.imshow('Blank Image', blank)

# creating a mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

# masked image
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)