import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Average Blur
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur 
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur ( applies bluring be retaining the edges in the image)
bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)