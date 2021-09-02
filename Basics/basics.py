import cv2 as cv

img = cv.imread('Photos/boston.jpg')

cv.imshow('Boston', img)

# Converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Bluring the image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# creating a edge cascading
cascade = cv.Canny(img,125,175)
cv.imshow('Cascade Edge', cascade)

# Dilating the image
dilated = cv.dilate(img, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Crpooed', cropped)

cv.waitKey(0)
