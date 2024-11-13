import cv2
import numpy as np
image = cv2.imread('car2.png')
median = cv2.medianBlur(image, 5)
median1 = cv2.medianBlur(median, 9)
sharp = median + (median - median1)

cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.imshow('Blurred Image', median)
cv2.waitKey(0)
cv2.imshow('Sharpened Image', sharp)
cv2.waitKey(0)
