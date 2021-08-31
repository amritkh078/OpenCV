import cv2 as cv
import numpy as np

# creating a blank image
# np.zeros((height, width, colour_channels))
blank = np.zeros((500, 500, 3), dtype='uint8')
#cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# 2. Draw a rectangle
#cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
#cv.imshow('Rectangle', blank)

# 3. Draw a circle
# cv.circle(blank,(250,250), 40,(250,0,0), thickness=2)
# cv.imshow('Circle', blank)

# 4.Draw a line
# cv.line(blank, (100,250), (300,400), (96,52,192), thickness=3, )
# cv.imshow('Line', blank)

#5. Write a text
cv.putText(blank, 'This is OpenCV Tutorial.', (0,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,12,45), thickness=2)
cv.imshow('Text', blank) 

cv.waitKey(0)
