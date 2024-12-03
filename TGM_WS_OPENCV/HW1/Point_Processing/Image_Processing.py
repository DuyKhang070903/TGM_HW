import cv2
import numpy as np
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Point_Processing/HW1_OnePiece.jpg')
# cv2.imshow('Display Image', A)
gray_A = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY) # chuyển sang ảnh xám
# # cv2.imshow('Display Image', gray_A)
negative_A = 255 - gray_A
# cv2.imshow('Display Image', negative_A)
fig, axes = plt.subplots(1, 3, figsize=(12, 6))
axes[0].imshow(A)
# axes[0].axis("off")
axes[0].set_title('ẢNH MÀU')

axes[1].imshow(gray_A, cmap='gray')
axes[1].axis("off")
axes[1].set_title('ẢNH XÁM')

axes[2].imshow(negative_A, cmap='gray')
axes[2].axis("off")
axes[2].set_title('Negative Image')
plt.show()



