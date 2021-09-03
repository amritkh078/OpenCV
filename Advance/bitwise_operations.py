import cv2 as cv
import numpy as np

blank = np.zeros((4000,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255 , -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)  # this returns the intersection(common area) between two images
cv.imshow("Bitwise AND",bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle) # this returns both images put together
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle) # this returns non-intersecting regions
cv.imshow('Bitwise XOR', bitwise_xor) 

# Bitwise NOT  --> inverts binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)