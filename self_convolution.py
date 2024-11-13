import cv2
import numpy as np

def convolve(image, kernel):
    new_image = np.zeros_like(image)
    k_height, k_width = kernel.shape
    pad_height, pad_width = k_height // 2, k_width // 2
    for i in range(pad_height, image.shape[0]-pad_height):
        for j in range(pad_height, image.shape[1]-pad_width):
            patch = image[i-kernel.shape[0]//2:i+kernel.shape[0]//2+1, j-kernel.shape[1]//2:j+kernel.shape[1]//2+1]
            patch_k = np.zeros_like(kernel)
            for h in range (0, kernel.shape[0]):
                for w in range(0, kernel.shape[1]):
                    patch_k[h, w] = patch[h, w].mean() 
            sum = (np.multiply(patch_k, kernel)).sum()
            new_image[i, j] = sum
    print(patch)
    print(kernel)
    return new_image

kernel_average = np.array([[1, 1, 1],
                           [1, 1, 1],
                            [1, 1, 1]]) * 1/9

image = cv2.imread('mandrill.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
blurred = convolve(image, kernel_average)
detail = image - blurred
sharpen = image + detail
cv2.imshow('Averaged Image', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()