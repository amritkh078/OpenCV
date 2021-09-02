import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

b,g,r = cv.split(img)

# cv.imshow('Blue', b)    # this gives grayscale images, where the color channels are represented by white pixels-
# cv.imshow('Green', g)   # -where its concentration is the most
# cv.imshow('Red', r)

# TO display image of respective color 
blank= np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank, blank])
green = cv.merge([ blank,g, blank])
red = cv.merge([ blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b,g,r])  # this merges three different color channels into a single image
cv.imshow('Merged Image', merged)



cv.waitKey(0)