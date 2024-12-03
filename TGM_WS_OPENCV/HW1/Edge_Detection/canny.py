import cv2 
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Edge_Detection/Test_Image.jpg', cv2.IMREAD_GRAYSCALE)

blur = cv2.GaussianBlur(A, (5, 5), 1.4) # Áp dụng bộ lọc Gaussian để giảm nhiễu 
edges = cv2.Canny(blur, 50, 150)

plt.subplot(1, 2, 1)
plt.imshow(A, cmap='gray')
plt.title('Original_Image')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Canny_Image')

plt.show()
