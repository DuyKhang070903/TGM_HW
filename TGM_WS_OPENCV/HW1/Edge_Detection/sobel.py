import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Edge_Detection/Test_Image.jpg', cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(A, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(A, cv2.CV_64F, 0, 1, ksize=5)
sobelxy = cv2.Sobel(A, cv2.CV_64F, 1, 1, ksize=5)

plt.subplot(2, 2, 1)
plt.imshow(A, cmap='gray')
plt.title('Original_Image')

plt.subplot(2, 2, 2)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobelx_Image')

plt.subplot(2, 2, 3)
plt.imshow(sobely, cmap='gray')
plt.title('Sobely_Image')

plt.subplot(2, 2, 4)
plt.imshow(sobelxy, cmap='gray')
plt.title('Sobelxy_Image')
plt.show()