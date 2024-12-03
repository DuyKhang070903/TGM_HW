import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Point_Processing/Test_Image2.jpg',0)
_, B = cv2.threshold(A, 127, 255, cv2.THRESH_BINARY)
# dau gach truoc la gia tri nguong tra ve sau khi threshold

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(A, cmap='gray')
plt.title("Ảnh Gốc")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(B, cmap='gray')
plt.title("Ảnh Sau Khi Thresholding")
plt.axis("off")

plt.show()
