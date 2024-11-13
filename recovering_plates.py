import cv2
import numpy as np
image = cv2.imread('car1.png')
blur = cv2.GaussianBlur(image, (5, 5), 0)


sharpen = image + (image - blur)
sharpen2 = sharpen + (sharpen - image)
sharpen3 = sharpen2 + (sharpen2 - sharpen)
sharpen4 = sharpen3 + (sharpen3 - blur)
sharpen5 = sharpen4 + (sharpen4 - image)
cv2.imshow('Original Image', image)
cv2.waitKey
cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)
cv2.imshow('Sharpened Image', sharpen)
cv2.waitKey(0)
cv2.imshow('Sharpened Image 2', sharpen2)
cv2.waitKey(0)
cv2.imshow('Sharpened Image 3', sharpen3)
cv2.waitKey(0)
cv2.imshow('Sharpened Image 4', sharpen4)
cv2.waitKey(0)
cv2.imshow('Sharpened Image 5', sharpen5)
cv2.waitKey(0)