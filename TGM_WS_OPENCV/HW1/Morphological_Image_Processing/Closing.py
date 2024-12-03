import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Morphological_Image_Processing/Test_Image.jpg')
if len(A.shape) == 3:  
    A = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(A, 128, 255, cv2.THRESH_BINARY)

def add_black_noise(img, noise_value):
    noisy_img = img.copy()
    h, w = noisy_img.shape  
    for _ in range(noise_value):
        x = random.randint(0, w - 1)
        y = random.randint(0, h - 1)
        noisy_img[y, x] = 0  
    return noisy_img

noisy_image = add_black_noise(A, noise_value=100000)
kernel = np.ones((3, 3), np.uint8)  
closed_image = cv2.morphologyEx(noisy_image, cv2.MORPH_CLOSE, kernel)

plt.subplot(1, 2, 1)
plt.imshow(noisy_image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(closed_image, cmap='gray')
plt.title('Closing_Image')
plt.show()




