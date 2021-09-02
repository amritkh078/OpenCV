# Contours are the boundaries of the objects, the lines/curves that joins the continuous points
# along the boundary of an object
# Contours are used for shape analysis and object detection and recognition.

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# First convert the image into grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY )
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# Using Edge cascade
canny = cv.Canny(blur, 125, 125)
cv.imshow('Canny Edges',canny)

# Using Threshold
ret, thresh = cv.threshold(gray, 125,125, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Countours Drawn', blank)


cv.waitKey(0)