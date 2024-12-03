import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Morphological_Image_Processing/Test_Image.jpg')
noise = np.random.randint(0, 2, size=A.shape, dtype=np.uint8) * 255  
A_noisy = cv2.add(A, noise)  

kernel = np.ones((7, 7), np.uint8)
A_op = cv2.morphologyEx(A_noisy, cv2.MORPH_OPEN, kernel)

plt.subplot(1, 2, 1)
plt.imshow(A_noisy, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(A_op, cmap='gray')
plt.title('Opening_Image')
plt.show()
