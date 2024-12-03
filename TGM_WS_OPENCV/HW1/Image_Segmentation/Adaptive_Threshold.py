import cv2 
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_WS_OPENCV/HW1/Image_Segmentation/Test_Image.jpg', cv2.IMREAD_GRAYSCALE)
A = cv2.medianBlur(A, 5)

_, thresh1 = cv2.threshold(A, 127, 255, cv2.THRESH_BINARY)

thresh2 = cv2.adaptiveThreshold(A, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh3 = cv2.adaptiveThreshold(A, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 100)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [A, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
