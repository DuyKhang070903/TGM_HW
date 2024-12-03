import cv2
from matplotlib import pyplot as plt

A = cv2.imread('D:/TGM_HW_DK/TGM_WS_OPENCV/HW1/Filter/HW1_WeightedAverageFilter.jpg')

# Áp dụng Gaussian filter với sigma = 2 (tương đương imgaussfilt(A, 2) trong MATLAB)
# (0,0) kich thước cửa sổ kernel dùng để lọc, Sigma càng lớn thì mờ nhiều
A_filter = cv2.GaussianBlur(A, (0, 0), 2)

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(A, cv2.COLOR_BGR2RGB))
plt.title('Original image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(A_filter, cv2.COLOR_BGR2RGB))
plt.title('Gaussian filter (sigma=2)')
plt.show()
