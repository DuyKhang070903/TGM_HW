import cv2
import numpy as np
from matplotlib import pyplot as plt

# J ảnh gốc đã được chuyển sang grayscale
J = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Filter/HW1_OrderStatisticFilter.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng Median filter (tương tự A_med = ordfilt2(J, 5, ones(3,3)) trong MATLAB)
A_med = cv2.medianBlur(J, 3)

# Hiển thị ảnh sau khi lọc median
plt.subplot(1, 2, 1)
plt.imshow(A_med, cmap='gray')
plt.title('Median filter')

# Áp dụng Max filter (tương tự A_max = ordfilt2(J, 9, ones(3,3)) trong MATLAB)
# Dùng phép giãn ảnh với kernel 3x3
kernel = np.ones((3, 3), np.uint8)
A_max = cv2.dilate(J, kernel)

# Hiển thị ảnh sau khi lọc max
plt.subplot(1, 2, 2)
plt.imshow(A_max, cmap='gray')
plt.title('Max filter')
plt.show()




