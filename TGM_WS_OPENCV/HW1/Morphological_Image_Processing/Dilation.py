import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Morphological_Image_Processing/Test_Image.jpg')

kernel = np.ones((5, 5), np.uint8)
A_dil = cv2.dilate(A, kernel=kernel, iterations=2)

plt.subplot(1, 2, 1)
plt.imshow(A, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(A_dil, cmap='gray')
plt.title('Dilation_Image')
plt.show()
