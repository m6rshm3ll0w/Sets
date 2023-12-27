import numpy as np
import cv2

image = cv2.imread("img.jpg")
image = cv2.resize(image, (int(image.shape[1] * 50 / 100), int(image.shape[0] * 50 / 100)))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred,80,300)

cv2.imshow("sets.img", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
