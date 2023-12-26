import sys
import numpy as np
import cv2 as cv

hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

img = cv.imread('img.jpg')


cv.imshow('contours', img)

cv.waitKey()
cv.destroyAllWindows()
